from fractions import Fraction
from functools import lru_cache
from itertools import count

def reverse_bits(x,L):
    return int(format(x,f"0{L}b")[::-1],2)

def partner(x,L):
    if L<1 or not 0<=x<(1<<L):raise ValueError("width or word")
    j=reverse_bits(x,L)
    return j if j!=x else x^((1<<L)-1)

def compare(a,b):return (a>b)-(a<b)

@lru_cache(maxsize=1024)
def representatives_below(t,L):
    if t<=0:return 0
    if t>=(1<<L):return 1<<(L-1)
    bound=format(t-1,f"0{L}b");states={(0,0,0,-1):1}
    for i in range(L//2):
        nxt={};left=int(bound[i]);right=int(bound[L-1-i])
        for (cl,cr,cj,first),n in states.items():
            for a in (0,1):
                for b in (0,1):
                    key=(cl or compare(a,left),compare(b,right) or cr,
                         cj or compare(a,b),a if i==0 else first)
                    nxt[key]=nxt.get(key,0)+n
        states=nxt
    total=0
    for (cl,cr,cj,first),n in states.items():
        for mid in ((0,1) if L%2 else (None,)):
            c=cl or (compare(mid,int(bound[L//2])) if mid is not None else 0) or cr
            f=mid if first==-1 else first
            if c<=0 and (cj<0 or (cj==0 and f==0)):total+=n
    return total

def representative_at(k,L):
    if L<1 or not 0<=k<(1<<(L-1)):raise ValueError("rank")
    lo,hi=0,(1<<L)-1
    while lo<hi:
        mid=(lo+hi)//2
        if representatives_below(mid+1,L)>k:hi=mid
        else:lo=mid+1
    return lo

def word_at(L,i):
    if L<1 or not 0<=i<(1<<L):raise ValueError("position")
    N=1<<L;M=N//2
    if M>1 and i in (M-1,M):i=N-1-i
    return representative_at(i,L) if i<M else partner(representative_at(N-1-i,L),L)

def location(L,x):
    y=partner(x,L);a=min(x,y);N=1<<L;M=N//2
    k=representatives_below(a,L);i=k if x==a else N-1-k
    return N-1-i if M>1 and i in (M-1,M) else i

def advance(L,a):
    if a!=min(a,partner(a,L)):raise ValueError("canonical representative required")
    w=(1<<(L+1))|(a<<1)|1
    return L+2,min(w,partner(w,L+2))

def predecessor(L,a):
    if L<=2:return None
    w=format(a,f"0{L}b")
    if w!=w[::-1] and w[0]==w[-1]=='1':return L-2,int(w[1:-1],2)
    if w==w[::-1] and w.startswith('01'):
        return L-2,int(w[1:-1],2)^((1<<(L-2))-1)
    return None

def encode(L,x):
    a=min(x,partner(x,L));side=int(x!=a);depth=0
    while True:
        previous=predecessor(L,a)
        if previous is None:break
        L,a=previous;depth+=1
    return {'root_width':L,'root':a,'depth':depth,'side':side}

def decode(record):
    L,a=record['root_width'],record['root']
    for _ in range(record['depth']):L,a=advance(L,a)
    return L,partner(a,L) if record['side'] else a

def ray(root_width,root,side=0):
    L,a=root_width,root
    if a!=min(a,partner(a,L)) or predecessor(L,a) is not None:raise ValueError("root required")
    while True:
        yield L,partner(a,L) if side else a
        L,a=advance(L,a)

def angular_stream(u):
    u=Fraction(u)
    if not 0<=u<1:raise ValueError("angle in [0,1)")
    for L in count(1):
        scaled=(1<<L)*u;i=scaled.numerator//scaled.denominator
        tail=scaled-i;z=L*tail;k=z.numerator//z.denominator
        x=word_at(L,i)
        yield L,(x>>(L-1-k))&1

if __name__=='__main__':
    from itertools import islice
    print('Ray:',[(L,format(x,f"0{L}b")) for L,x in islice(ray(2,1),6)])
    print('Radial prefix at 1/3:',''.join(str(b) for L,b in islice(angular_stream(Fraction(1,3)),24)))
