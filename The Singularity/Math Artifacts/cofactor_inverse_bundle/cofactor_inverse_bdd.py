IV=(1779033703, 3144134277, 1013904242, 2773480762, 1359893119, 2600822924, 528734635, 1541459225)
K=(1116352408, 1899447441, 3049323471, 3921009573, 961987163, 1508970993, 2453635748, 2870763221, 3624381080, 310598401, 607225278, 1426881987, 1925078388, 2162078206, 2614888103, 3248222580, 3835390401, 4022224774, 264347078, 604807628, 770255983, 1249150122, 1555081692, 1996064986, 2554220882, 2821834349, 2952996808, 3210313671, 3336571891, 3584528711, 113926993, 338241895, 666307205, 773529912, 1294757372, 1396182291, 1695183700, 1986661051, 2177026350, 2456956037, 2730485921, 2820302411, 3259730800, 3345764771, 3516065817, 3600352804, 4094571909, 275423344, 430227734, 506948616, 659060556, 883997877, 958139571, 1322822218, 1537002063, 1747873779, 1955562222, 2024104815, 2227730452, 2361852424, 2428436474, 2756734187, 3204031479, 3329325298)

import sys,json,time,struct,hashlib
from functools import lru_cache

class BDD:
    def __init__(self,width):
        self.width=width;self.nodes=[(width,0,0),(width,1,1)]
        self.unique={};self.cache={};self.negcache={0:1,1:0}
        self.created=0;self.peak=2;self.gc_passes=0
        self.variables=[self.mk(i,0,1) for i in range(width)]
    def mk(self,v,lo,hi):
        if lo==hi:return lo
        key=(v,lo,hi)
        if key in self.unique:return self.unique[key]
        i=len(self.nodes);self.nodes.append(key);self.unique[key]=i
        self.created+=1;self.peak=max(self.peak,len(self.nodes))
        if len(self.nodes)>1000000:raise MemoryError('declared live-node budget exceeded')
        return i
    def not_(self,u):
        if u in self.negcache:return self.negcache[u]
        v,lo,hi=self.nodes[u]
        out=self.mk(v,self.not_(lo),self.not_(hi))
        self.negcache[u]=out;self.negcache[out]=u
        return out
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
        lo=self.op(kind,lu,lv);hi=self.op(kind,hu,hv)
        out=self.mk(top,lo,hi)
        if len(self.cache)>150000:self.cache.clear()
        self.cache[key]=out
        return out
    def xor(self,a,b):return self.op('xor',a,b)
    def and_(self,a,b):return self.op('and',a,b)
    def collect(self,words,extra=()):
        unique_words=list({id(w):w for w in words}.values())
        roots=set(self.variables)|set(extra)
        for w in unique_words:roots.update(w)
        live={0,1};stack=list(roots)
        while stack:
            i=stack.pop()
            if i in live:continue
            live.add(i);_,a,b=self.nodes[i];stack.extend((a,b))
        mapping={0:0,1:1};new=[(self.width,0,0),(self.width,1,1)];uni={}
        for i in sorted(live-{0,1}):
            v,a,b=self.nodes[i];node=(v,mapping[a],mapping[b])
            mapping[i]=len(new);uni[node]=len(new);new.append(node)
        for w in unique_words:w[:]=[mapping[i] for i in w]
        self.variables=[mapping[i] for i in self.variables]
        extras=[mapping[i] for i in extra]
        self.nodes=new;self.unique=uni;self.cache.clear();self.negcache={0:1,1:0};self.gc_passes+=1
        return extras
    def satcount(self,root):
        @lru_cache(None)
        def count(u,level):
            if u==0:return 0
            if u==1:return 1<<(self.width-level)
            v,a,b=self.nodes[u]
            return (1<<(v-level))*(count(a,v+1)+count(b,v+1))
        return count(root,0)
    def unique_model(self,root):
        if self.satcount(root)!=1:return None
        assignment={};u=root
        while u>1:
            v,lo,hi=self.nodes[u]
            if lo==0:assignment[v]=1;u=hi
            elif hi==0:assignment[v]=0;u=lo
            else:raise AssertionError('not a unique path')
        assert len(assignment)==self.width
        return sum(bit<<v for v,bit in assignment.items())
    def reachable_count(self,root):
        seen=set();stack=[root]
        while stack:
            u=stack.pop()
            if u in seen or u<2:continue
            seen.add(u);stack.extend(self.nodes[u][1:])
        return len(seen)

class Words:
    def __init__(self,bdd):self.b=bdd
    def const(self,x):return [(x>>j)&1 for j in range(32)]
    def xor(self,a,b):return [self.b.xor(x,y) for x,y in zip(a,b)]
    def sigma(self,a,rotations,shift=None):
        out=[0]*32
        for n in rotations:out=self.xor(out,[a[(i+n)%32] for i in range(32)])
        if shift is not None:out=self.xor(out,[a[i+shift] if i+shift<32 else 0 for i in range(32)])
        return out
    def add(self,a,b):
        carry=0;out=[]
        for x,y in zip(a,b):
            p=self.b.xor(x,y);g=self.b.and_(x,y)
            out.append(self.b.xor(p,carry));carry=self.b.xor(g,self.b.and_(p,carry))
        return out
    def sub(self,a,b):
        borrow=0;out=[]
        for x,y in zip(a,b):
            p=self.b.xor(x,y);h=self.b.and_(self.b.not_(x),y)
            out.append(self.b.xor(p,borrow));borrow=self.b.xor(h,self.b.and_(self.b.not_(p),borrow))
        return out
    def sum(self,*args):
        out=args[0]
        for b in args[1:]:out=self.add(out,b)
        return out
    def choose(self,x,y,z):
        return [self.b.xor(c,self.b.and_(a,self.b.xor(b,c))) for a,b,c in zip(x,y,z)]
    def majority(self,x,y,z):
        return [self.b.xor(self.b.and_(a,b),self.b.and_(c,self.b.xor(a,b))) for a,b,c in zip(x,y,z)]

def solve(digest,width=8):
    if width!=8:raise ValueError('declared execution domain: all one-byte messages')
    started=time.perf_counter();b=BDD(width);w=Words(b)
    W=[[0]*32 for _ in range(64)]
    for j in range(width):W[0][32-width+j]=b.variables[j]
    W[0][31-width]=1;W[15]=w.const(width)
    for t in range(16,64):
        W[t]=w.sum(W[t-16],w.sigma(W[t-15],(7,18),3),W[t-7],w.sigma(W[t-2],(17,19),10))
        b.collect(W)
    schedule_time=time.perf_counter()-started
    terminal=[(a-v)&0xffffffff for a,v in zip(struct.unpack('>8I',bytes.fromhex(digest)),IV)]
    state=[w.const(x) for x in terminal]
    for t in range(63,-1,-1):
        a,bb,c,d,e,f,g,h=state
        aa,bc,cc,ee,ff,gg=bb,c,d,f,g,h
        T2=w.add(w.sigma(aa,(2,13,22)),w.majority(aa,bc,cc))
        T1=w.sub(a,T2);dd=w.sub(e,T1);hh=T1
        for z in (w.sigma(ee,(6,11,25)),w.choose(ee,ff,gg),w.const(K[t]),W[t]):hh=w.sub(hh,z)
        state=[aa,bc,cc,dd,ee,ff,gg,hh]
        b.collect(W+state)
        if t%16==0:print('round',t,'retained nodes',len(b.nodes),flush=True)
    inverse_time=time.perf_counter()-started-schedule_time
    root=1;survivors=[]
    for row,initial in zip(state,IV):
        for j,node in enumerate(row):
            clause=node if (initial>>j)&1 else b.not_(node)
            root=b.and_(root,clause);survivors.append(b.satcount(root))
    models=b.satcount(root);answer=b.unique_model(root)
    width_nodes=b.reachable_count(root)
    result={'method':'ROBDD exact Boolean cofactoring over unknown message bits; no candidate-message inverse loop',
        'domain_bits':width,'models':models,'recovered_hex':None if answer is None else answer.to_bytes(1,'big').hex(),
        'recovered_ascii':None if answer is None else repr(answer.to_bytes(1,'big')),
        'digest':digest,'solution_decision_nodes':width_nodes,'peak_retained_and_temporary_nodes':b.peak,
        'total_nodes_created':b.created,'garbage_collection_passes':b.gc_passes,
        'schedule_seconds':schedule_time,'inverse_seconds':inverse_time,'total_seconds':time.perf_counter()-started,
        'candidate_message_inverse_calls':0,'surviving_assignments_after_closure_bits':survivors,
        'forward_check':False if answer is None else hashlib.sha256(answer.to_bytes(1,'big')).hexdigest()==digest}
    return result

if __name__=='__main__':
    result=solve(sys.argv[1])
    with open(sys.argv[2],'w') as f:json.dump(result,f,indent=2)
    print(json.dumps({k:v for k,v in result.items() if k!='surviving_assignments_after_closure_bits'},indent=2),flush=True)
