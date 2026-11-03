IV=(1779033703, 3144134277, 1013904242, 2773480762, 1359893119, 2600822924, 528734635, 1541459225)
K=(1116352408, 1899447441, 3049323471, 3921009573, 961987163, 1508970993, 2453635748, 2870763221, 3624381080, 310598401, 607225278, 1426881987, 1925078388, 2162078206, 2614888103, 3248222580, 3835390401, 4022224774, 264347078, 604807628, 770255983, 1249150122, 1555081692, 1996064986, 2554220882, 2821834349, 2952996808, 3210313671, 3336571891, 3584528711, 113926993, 338241895, 666307205, 773529912, 1294757372, 1396182291, 1695183700, 1986661051, 2177026350, 2456956037, 2730485921, 2820302411, 3259730800, 3345764771, 3516065817, 3600352804, 4094571909, 275423344, 430227734, 506948616, 659060556, 883997877, 958139571, 1322822218, 1537002063, 1747873779, 1955562222, 2024104815, 2227730452, 2361852424, 2428436474, 2756734187, 3204031479, 3329325298)

import struct
from collections import deque,Counter

class DAG:
    def __init__(self,width):
        self.width=width
        self.nodes=[('const',0,0),('const',1,0)]+[('var',i,0) for i in range(width)]
        self.unique={};self.reuses=0;self.simple=0
    def gate(self,op,a,b):
        if a>b:a,b=b,a
        key=(op,a,b)
        if key in self.unique:self.reuses+=1;return self.unique[key]
        i=len(self.nodes);self.nodes.append(key);self.unique[key]=i;return i
    def negated_pair(self,a,b):
        return self.nodes[a]==('xor',1,b) or self.nodes[b]==('xor',1,a)
    def xor(self,a,b):
        if a==0:self.simple+=1;return b
        if b==0:self.simple+=1;return a
        if a==b:self.simple+=1;return 0
        if a==1 and self.nodes[b][0:2]==('xor',1):self.simple+=1;return self.nodes[b][2]
        if b==1 and self.nodes[a][0:2]==('xor',1):self.simple+=1;return self.nodes[a][2]
        return self.gate('xor',a,b)
    def and_(self,a,b):
        if a==0 or b==0:self.simple+=1;return 0
        if a==1 or a==b:self.simple+=1;return b
        if b==1:self.simple+=1;return a
        if self.negated_pair(a,b):self.simple+=1;return 0
        return self.gate('and',a,b)
    def not_(self,a):return self.xor(a,1)
    def const_word(self,w):return [(w>>i)&1 for i in range(32)]
    def xor_word(self,a,b):return [self.xor(x,y) for x,y in zip(a,b)]
    def sigma(self,a,rotations,shift=None):
        out=[0]*32
        for n in rotations:out=self.xor_word(out,[a[(i+n)%32] for i in range(32)])
        if shift is not None:out=self.xor_word(out,[a[i+shift] if i+shift<32 else 0 for i in range(32)])
        return out
    def add(self,a,b):
        carry=0;out=[]
        for x,y in zip(a,b):
            p=self.xor(x,y);g=self.and_(x,y)
            out.append(self.xor(p,carry))
            carry=self.xor(g,self.and_(p,carry))
        return out
    def sub(self,a,b):
        borrow=0;out=[]
        for x,y in zip(a,b):
            p=self.xor(x,y);h=self.and_(self.not_(x),y)
            out.append(self.xor(p,borrow))
            borrow=self.xor(h,self.and_(self.not_(p),borrow))
        return out
    def sum(self,*args):
        a=args[0]
        for b in args[1:]:a=self.add(a,b)
        return a
    def choose(self,x,y,z):
        return [self.xor(c,self.and_(a,self.xor(b,c))) for a,b,c in zip(x,y,z)]
    def majority(self,x,y,z):
        return [self.xor(self.and_(a,b),self.and_(c,self.xor(a,b))) for a,b,c in zip(x,y,z)]
    def evaluate(self,message_integer):
        values=[0,1]+[(message_integer>>i)&1 for i in range(self.width)]
        for op,a,b in self.nodes[2+self.width:]:
            values.append(values[a]^values[b] if op=='xor' else values[a]&values[b])
        return values

def compile_closure(digest,width):
    if width not in (8,16,24):raise ValueError('one, two, or three-byte interface')
    d=DAG(width)
    W=[[0]*32 for _ in range(64)]
    for j in range(width):W[0][32-width+j]=2+j
    W[0][31-width]=1;W[15]=d.const_word(width)
    for t in range(16,64):W[t]=d.sum(W[t-16],d.sigma(W[t-15],(7,18),3),W[t-7],d.sigma(W[t-2],(17,19),10))
    terminal=[(a-b)&0xffffffff for a,b in zip(struct.unpack('>8I',digest),IV)]
    a,b,c,e0,e,f,g,h=[d.const_word(x) for x in terminal]
    dd=e0
    for t in range(63,-1,-1):
        aa,bb,cc,ee,ff,gg=b,c,dd,f,g,h
        T2=d.add(d.sigma(aa,(2,13,22)),d.majority(aa,bb,cc))
        T1=d.sub(a,T2);old_d=d.sub(e,T1);old_h=T1
        for x in (d.sigma(ee,(6,11,25)),d.choose(ee,ff,gg),d.const_word(K[t]),W[t]):old_h=d.sub(old_h,x)
        a,b,c,dd,e,f,g,h=aa,bb,cc,old_d,ee,ff,gg,old_h
    residual=[]
    for word,initial in zip((a,b,c,dd,e,f,g,h),IV):residual.extend(d.xor_word(word,d.const_word(initial)))
    return d,residual

def propagate(d,outputs):
    adj=[[] for _ in d.nodes]
    for i,(op,a,b) in enumerate(d.nodes):
        if op in ('xor','and'):adj[a].append(i);adj[b].append(i)
    values=[None]*len(d.nodes);queue=deque();contradiction=False
    def assign(i,v):
        nonlocal contradiction
        if values[i] is None:values[i]=v;queue.extend(adj[i]);queue.append(i)
        elif values[i]!=v:contradiction=True
    assign(0,0);assign(1,1)
    for i in outputs:assign(i,0)
    while queue and not contradiction:
        z=queue.popleft();op,a,b=d.nodes[z]
        if op not in ('xor','and'):continue
        x,y,v=values[a],values[b],values[z]
        if op=='xor':
            if x is not None and y is not None:assign(z,x^y)
            if v is not None and x is not None:assign(b,v^x)
            if v is not None and y is not None:assign(a,v^y)
        else:
            if x==0 or y==0:assign(z,0)
            if x==1 and y==1:assign(z,1)
            if v==1:assign(a,1);assign(b,1)
            if v==0 and x==1:assign(b,0)
            if v==0 and y==1:assign(a,0)
    forced={str(i):values[2+i] for i in range(d.width) if values[2+i] is not None}
    return {'contradiction':contradiction,'forced_message_bits_LSB_index':forced,'unresolved_message_bits':d.width-len(forced),'assigned_graph_nodes':sum(x is not None for x in values)}
