import numpy as np
from fractions import Fraction as F
def ring(L):
    N=1<<L; w=np.arange(N,dtype=np.int64)
    rev=np.zeros(N,dtype=np.int64)
    for b in range(L): rev|=((w>>b)&1)<<(L-1-b)
    pal=rev==w; part=np.where(pal,(N-1)^w,rev)
    reps=w[w<part]
    R=np.concatenate([reps,part[reps][::-1]])
    if L>1: R[N//2-1],R[N//2]=R[N//2],R[N//2-1]
    return R,pal[R]
def fwht(a):
    a=a.copy(); h=1
    while h<len(a):
        a=a.reshape(-1,2*h); x=a[:,:h].copy(); y=a[:,h:].copy()
        a[:,:h]=x+y; a[:,h:]=x-y; a=a.reshape(-1); h*=2
    return a
pc=np.vectorize(lambda s:bin(s).count('1'))
for n in range(2,21):
    R,pal=ring(n); N=1<<n
    wt=np.zeros(N,dtype=np.int64)
    for b in range(n): wt+=(R>>b)&1
    z2=2*wt-n                         # 2z, integer
    Z=fwht(z2); Zp=fwht(np.where(pal,z2,0)); Zn=fwht(np.where(pal,0,z2))
    odd=(pc(np.arange(N))%2==1)
    p1 = np.array_equal(Z[odd],Zp[odd]) and np.array_equal(Z[~odd],Zn[~odd]) and not Zp[~odd].any() and not Zn[odd].any()
    frac=F(int((Z[odd].astype(object)**2).sum()), int((Z.astype(object)**2).sum()))
    h=n//2; pred = F(2,2**h) if n%2==0 else F(4*h+1,(2*h+1)*2**h)
    print(f"n={n:2d} P1 {p1}  P2 measured {str(frac):>14} predicted {str(pred):>14} {'RUNS' if frac==pred else 'DEAD END'}")
