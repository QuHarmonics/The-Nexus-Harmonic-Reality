import numpy as np, hashlib
assert hashlib.sha256(open('seal.txt','rb').read()).hexdigest().startswith('5910642e')
def revarr(w,n):
    r=np.zeros_like(w)
    for b in range(n): r|=((w>>b)&1)<<(n-1-b)
    return r
for n in range(2,21):
    N=1<<n; w=np.arange(N,dtype=np.int64); J=revarr(w,n)
    part=np.where(J==w,(N-1)^w,J); reps=w[w<part]
    R=np.concatenate([reps,part[reps][::-1]]); R[N//2-1],R[N//2]=R[N//2],R[N//2-1]
    loc=np.empty(N,dtype=np.int64); loc[R]=np.arange(N)
    c=np.sign(J-w); Delta=np.concatenate([[0],np.cumsum(c)[:-1]])   # sum over x<p
    m=(n+1)//2; H=1<<m; ok=True
    for u in range(H):
        s=format(u,f'0{m}b'); p=int(s+(s[::-1] if n%2==0 else s[:-1][::-1]),2)
        if u<H//2: pred=(p+u+Delta[p])//2; ok&= (p+u+Delta[p])%2==0
        else:
            s2=format(H-1-u,f'0{m}b'); q=int(s2+(s2[::-1] if n%2==0 else s2[:-1][::-1]),2)
            pred=N-1-(q+(H-1-u)+Delta[q])//2
        ok&= pred==loc[p]
    line=f"n={n:2d} P1 {'RUNS' if ok else 'DEAD END'}"
    if n<=16:
        # explicit ripple-borrow Maj chain, LSB->MSB, a=x, b=J(x)
        a,b=w,J; bor=np.zeros(N,dtype=np.int64)
        for k in range(n):
            ak=(a>>k)&1; bk=(b>>k)&1; na=1-ak
            bor=(na&bk)|(na&bor)|(bk&bor)            # Maj(not a, b, borrow)
        a2=J; b2=w; bor2=np.zeros(N,dtype=np.int64)
        for k in range(n):
            ak=(a2>>k)&1; bk=(b2>>k)&1; na=1-ak
            bor2=(na&bk)|(na&bor2)|(bk&bor2)
        line+=f"  P2 c == borrow(x-J) - borrow(J-x): {'RUNS' if np.array_equal(c,bor-bor2) else 'DEAD END'}"
    print(line)
