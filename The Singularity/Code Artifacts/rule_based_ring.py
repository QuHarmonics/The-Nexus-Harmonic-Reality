from functools import lru_cache

def reverse_bits(x,L):
    return int(format(x,f"0{L}b")[::-1],2)

def partner(x,L):
    y=reverse_bits(x,L)
    return y if y!=x else x^((1<<L)-1)

def cmp(a,b):
    return (a>b)-(a<b)

@lru_cache(maxsize=4096)
def representatives_below(t,L):
    if t<=0:return 0
    if t>=(1<<L):return 1<<(L-1)
    bound=format(t-1,f"0{L}b")
    states={(0,0,0,-1):1}
    for i in range(L//2):
        nxt={};left=int(bound[i]);right=int(bound[L-1-i])
        for (cl,cr,cj,first),n in states.items():
            for a in (0,1):
                for b in (0,1):
                    key=(cl if cl else cmp(a,left),cmp(b,right) or cr,
                         cj if cj else cmp(a,b),a if i==0 else first)
                    nxt[key]=nxt.get(key,0)+n
        states=nxt
    total=0
    for (cl,cr,cj,first),n in states.items():
        for mid in ((0,1) if L%2 else (None,)):
            comparison=cl or (cmp(mid,int(bound[L//2])) if mid is not None else 0) or cr
            first_bit=mid if first==-1 else first
            if comparison<=0 and (cj<0 or (cj==0 and first_bit==0)):
                total+=n
    return total

def representative_at(k,L):
    if not 0<=k<(1<<(L-1)):raise ValueError("representative rank")
    lo,hi=0,(1<<L)-1
    while lo<hi:
        mid=(lo+hi)//2
        if representatives_below(mid+1,L)>k:hi=mid
        else:lo=mid+1
    return lo

def word_at(position,L):
    N=1<<L;M=N//2
    if not 0<=position<N:raise ValueError("word position")
    p=position
    if M>1 and p in (M-1,M):p=N-1-p
    if p<M:return representative_at(p,L)
    return partner(representative_at(N-1-p,L),L)

def location(x,L):
    if not 0<=x<(1<<L):raise ValueError("word")
    N=1<<L;M=N//2;y=partner(x,L);a=min(x,y)
    k=representatives_below(a,L)
    p=k if x==a else N-1-k
    return N-1-p if M>1 and p in (M-1,M) else p
