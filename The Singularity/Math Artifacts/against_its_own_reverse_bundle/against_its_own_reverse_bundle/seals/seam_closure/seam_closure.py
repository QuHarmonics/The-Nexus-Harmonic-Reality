import numpy as np, hashlib
from fractions import Fraction as F
assert hashlib.sha256(open('seal.txt','rb').read()).hexdigest().startswith('947b3f56')
def ring(n):
    N=1<<n; w=np.arange(N,dtype=np.int64); J=np.zeros_like(w)
    for b in range(n): J|=((w>>b)&1)<<(n-1-b)
    part=np.where(J==w,(N-1)^w,J); reps=w[w<part]
    R=np.concatenate([reps,part[reps][::-1]]); R[N//2-1],R[N//2]=R[N//2],R[N//2-1]
    return R, reps
def zsum_pred(K,mu):
    g=K.bit_length()-1; v=K-(1<<g); bits=[(v>>(g-1-k))&1 for k in range(g)]
    s=F(K*bin(K).count('1')) + F(g*(1<<g),2)
    o=0
    for k in range(g):
        if bits[k]: s+=(1<<(g-1-k))*(1+o+F(g-1-k,2))
        o+=bits[k]
    return mu*s+(mu-1)*K
for n in range(4,21):
    R,reps=ring(n); N=1<<n; h=n//2; H=1<<h; mu=1 if n%2==0 else 2
    wt=np.zeros(N,dtype=np.int64)
    for b in range(n): wt+=(R>>b)&1
    s2=np.array([bin(i).count('1') for i in range(H)])
    s1 = np.array_equal(wt[:H], s2) and np.array_equal(wt[N-H:N-1][::-1], s2[1:]) and wt[N-1]==n
    desc=reps[::-1]; zw=n-np.array([bin(int(x)).count('1') for x in desc[:mu*(H//2)*(H//2+1)//2+mu]])
    ok=True; start=0; worst=None
    for K in range(1,H//2):
        size=mu*K; got=int(zw[start:start+size].sum()); pred=zsum_pred(K,mu)
        if got!=pred: ok=False; worst=(K,got,pred); break
        start+=size
    print(f"n={n:2d} S1 {'RUNS' if s1 else 'DEAD END'}  S2 blocks K<{H//2}: {'RUNS' if ok else 'DEAD END '+str(worst)}")
