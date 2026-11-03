IV=(1779033703, 3144134277, 1013904242, 2773480762, 1359893119, 2600822924, 528734635, 1541459225)
K=(1116352408, 1899447441, 3049323471, 3921009573, 961987163, 1508970993, 2453635748, 2870763221, 3624381080, 310598401, 607225278, 1426881987, 1925078388, 2162078206, 2614888103, 3248222580, 3835390401, 4022224774, 264347078, 604807628, 770255983, 1249150122, 1555081692, 1996064986, 2554220882, 2821834349, 2952996808, 3210313671, 3336571891, 3584528711, 113926993, 338241895, 666307205, 773529912, 1294757372, 1396182291, 1695183700, 1986661051, 2177026350, 2456956037, 2730485921, 2820302411, 3259730800, 3345764771, 3516065817, 3600352804, 4094571909, 275423344, 430227734, 506948616, 659060556, 883997877, 958139571, 1322822218, 1537002063, 1747873779, 1955562222, 2024104815, 2227730452, 2361852424, 2428436474, 2756734187, 3204031479, 3329325298)

import sys,json,time,struct,hashlib
from functools import lru_cache

class BDD:
    def __init__(self,order):
        self.order=list(order);self.width=len(order)
        if sorted(order)!=list(range(self.width)):raise ValueError('permutation required')
        self.nodes=[(self.width,0,0),(self.width,1,1)];self.unique={};self.cache={};self.negcache={0:1,1:0}
        self.created=0;self.peak=2;self.gc_passes=0
        self.variables=[self.mk(self.order.index(bit),0,1) for bit in range(self.width)]
    def mk(self,v,lo,hi):
        if lo==hi:return lo
        key=(v,lo,hi)
        if key in self.unique:return self.unique[key]
        i=len(self.nodes);self.nodes.append(key);self.unique[key]=i
        self.created+=1;self.peak=max(self.peak,len(self.nodes));return i
    def not_(self,u):
        if u in self.negcache:return self.negcache[u]
        v,lo,hi=self.nodes[u];out=self.mk(v,self.not_(lo),self.not_(hi))
        self.negcache[u]=out;self.negcache[out]=u;return out
    def op(self,kind,u,v):
        if u>v:u,v=v,u
        if kind=='xor':
            if u==0:return v
            if u==v:return 0
            if u==1:return self.not_(v)
        else:
            if u==0:return 0
            if u==1 or u==v:return v
        key=(kind,u,v)
        if key in self.cache:return self.cache[key]
        vu,lu,hu=self.nodes[u];vv,lv,hv=self.nodes[v];top=min(vu,vv)
        if vu!=top:lu=hu=u
        if vv!=top:lv=hv=v
        low=self.op(kind,lu,lv);high=self.op(kind,hu,hv)
        out=self.mk(top,low,high)
        if len(self.cache)>150000:self.cache.clear()
        self.cache[key]=out;return out
    def xor(self,a,b):return self.op('xor',a,b)
    def and_(self,a,b):return self.op('and',a,b)
    def collect(self,words,extra=()):
        words=list({id(w):w for w in words}.values())
        roots=set(self.variables)|set(extra)
        for w in words:roots.update(w)
        live={0,1};stack=list(roots)
        while stack:
            i=stack.pop()
            if i in live:continue
            live.add(i);stack.extend(self.nodes[i][1:])
        mapping={0:0,1:1};new=[(self.width,0,0),(self.width,1,1)];unique={}
        for i in sorted(live-{0,1}):
            v,a,b=self.nodes[i];node=(v,mapping[a],mapping[b])
            mapping[i]=len(new);unique[node]=len(new);new.append(node)
        for w in words:w[:]=[mapping[i] for i in w]
        self.variables=[mapping[i] for i in self.variables]
        extras=[mapping[i] for i in extra]
        self.nodes=new;self.unique=unique;self.cache.clear();self.negcache={0:1,1:0};self.gc_passes+=1
        return extras
    def count_from(self,root,level=0):
        @lru_cache(None)
        def count(u,lev):
            if u==0:return 0
            if u==1:return 1<<(self.width-lev)
            v,a,b=self.nodes[u]
            return (1<<(v-lev))*(count(a,v+1)+count(b,v+1))
        return count(root,level)
    def size(self,root):
        seen=set();stack=[root]
        while stack:
            u=stack.pop()
            if u<2 or u in seen:continue
            seen.add(u);stack.extend(self.nodes[u][1:])
        return len(seen)
    def unique_path(self,root):
        if self.count_from(root)!=1:return None,[]
        u=root;value=0;trace=[]
        while u>1:
            level,low,high=self.nodes[u];bit=self.order[level]
            lc=self.count_from(low,level+1);hc=self.count_from(high,level+1)
            if lc==0:chosen=1;u=high
            elif hc==0:chosen=0;u=low
            else:raise AssertionError('not unique')
            trace.append({'bit_index':bit,'chosen':chosen,'low_solutions':lc,'high_solutions':hc})
            value|=chosen<<bit
        assert len(trace)==self.width
        return value,trace
    def evaluate(self,root,value):
        while root>1:
            level,low,high=self.nodes[root]
            root=high if (value>>self.order[level])&1 else low
        return root

class WordOps:
    def __init__(self,b):self.b=b
    def const(self,x):return [(x>>j)&1 for j in range(32)]
    def xor(self,a,b):return [self.b.xor(x,y) for x,y in zip(a,b)]
    def sigma(self,a,rotations,shift=None):
        out=[0]*32
        for n in rotations:out=self.xor(out,[a[(i+n)%32] for i in range(32)])
        if shift is not None:out=self.xor(out,[a[i+shift] if i+shift<32 else 0 for i in range(32)])
        return out
    def add(self,a,b):
        c=0;out=[]
        for x,y in zip(a,b):
            p=self.b.xor(x,y);g=self.b.and_(x,y)
            out.append(self.b.xor(p,c));c=self.b.xor(g,self.b.and_(p,c))
        return out
    def sub(self,a,b):
        c=0;out=[]
        for x,y in zip(a,b):
            p=self.b.xor(x,y);g=self.b.and_(self.b.not_(x),y)
            out.append(self.b.xor(p,c));c=self.b.xor(g,self.b.and_(self.b.not_(p),c))
        return out
    def sum(self,*args):
        out=args[0]
        for b in args[1:]:out=self.add(out,b)
        return out
    def choose(self,x,y,z):return [self.b.xor(c,self.b.and_(a,self.b.xor(b,c))) for a,b,c in zip(x,y,z)]
    def majority(self,x,y,z):return [self.b.xor(self.b.and_(a,b),self.b.and_(c,self.b.xor(a,b))) for a,b,c in zip(x,y,z)]

def solve(digest,order):
    start=time.perf_counter();b=BDD(order);w=WordOps(b);width=len(order)
    if width!=8:raise ValueError('complete one-byte interface')
    W=[[0]*32 for _ in range(64)]
    for j in range(width):W[0][32-width+j]=b.variables[j]
    W[0][31-width]=1;W[15]=w.const(width)
    for t in range(16,64):
        W[t]=w.sum(W[t-16],w.sigma(W[t-15],(7,18),3),W[t-7],w.sigma(W[t-2],(17,19),10));b.collect(W)
    schedule_seconds=time.perf_counter()-start
    terminal=[(a-v)&0xffffffff for a,v in zip(struct.unpack('>8I',bytes.fromhex(digest)),IV)]
    state=[w.const(x) for x in terminal]
    for t in range(63,-1,-1):
        a,bb,c,d,e,f,g,h=state;aa,bc,cc,ee,ff,gg=bb,c,d,f,g,h
        T2=w.add(w.sigma(aa,(2,13,22)),w.majority(aa,bc,cc));T1=w.sub(a,T2)
        dd=w.sub(e,T1);hh=T1
        for z in (w.sigma(ee,(6,11,25)),w.choose(ee,ff,gg),w.const(K[t]),W[t]):hh=w.sub(hh,z)
        state=[aa,bc,cc,dd,ee,ff,gg,hh];b.collect(W+state)
    trace=[{'constraints':0,'survivors':256,'decision_nodes':0,'word_index':None,'bit_index':None,'required':None}]
    root=1
    for row,(bits,initial) in enumerate(zip(state,IV)):
        for j,node in enumerate(bits):
            required=(initial>>j)&1
            clause=node if required else b.not_(node)
            root=b.and_(root,clause)
            trace.append({'constraints':len(trace),'survivors':b.count_from(root),'decision_nodes':b.size(root),'word_index':row,'bit_index':j,'required':required})
    models=b.count_from(root);answer,path=b.unique_path(root)
    result={'variable_order':order,'models':models,'recovered_hex':None if answer is None else format(answer,'02x'),
        'solution_decision_nodes':b.size(root),'peak_nodes':b.peak,'total_nodes_created':b.created,
        'schedule_seconds':schedule_seconds,'total_seconds':time.perf_counter()-start,
        'candidate_inverse_calls':0,'forward_check':answer is not None and hashlib.sha256(bytes([answer])).hexdigest()==digest,
        'constraint_trace':trace,'unique_cofactor_path':path}
    return result

if __name__=='__main__':
    digest=sys.argv[1];order=[int(x) for x in sys.argv[2].split(',')]
    result=solve(digest,order)
    with open(sys.argv[3],'w') as f:json.dump(result,f,indent=2)
    print(json.dumps({k:v for k,v in result.items() if k not in ('constraint_trace','unique_cofactor_path')},indent=2))
