# Observation (not sealed): each reader is simple in its own coordinates and spread in the other's.
import numpy as np, sys
sys.argv=['x']; exec(open('pullback_run.py').read().split("# ---------- PB1")[0].split("SEAL = open")[0])
def revarr(w,n):
    r=np.zeros_like(w)
    for b in range(n): r|=((w>>b)&1)<<(n-1-b)
    return r
def popc(w,n):
    s=np.zeros_like(w)
    for b in range(n): s+=(w>>b)&1
    return s
def ring(n):
    N=1<<n; w=np.arange(N,dtype=np.int64); J=revarr(w,n)
    part=np.where(J==w,(N-1)^w,J); reps=w[w<part]
    R=np.concatenate([reps,part[reps][::-1]]); R[N//2-1],R[N//2]=R[N//2],R[N//2-1]; return R
def fwht(a):
    a=a.copy(); hh=1
    while hh<len(a):
        a=a.reshape(-1,2*hh); x=a[:,:hh].copy(); y=a[:,hh:].copy(); a[:,:hh]=x+y; a[:,hh:]=x-y; a=a.reshape(-1); hh*=2
    return a
def pr(v):  # participation ratio of spectrum: (sum c^2)^2 / sum c^4  = effective number of modes
    v=v.astype(float); s2=(v*v).sum(); return s2*s2/((v**4).sum())
print(" n | word coords: #modes z, c | ring coords: #modes Z, C | effective modes (participation) z, c | Z, C")
for n in (8,10,12,14,16,18,20):
    N=1<<n; w=np.arange(N,dtype=np.int64); J=revarr(w,n)
    z=2*popc(w,n)-n; c=np.sign(J-w)
    R=ring(n); Z=2*popc(R,n)-n; C=np.sign(revarr(R,n)-R)
    fz,fc,fZ,fC=fwht(z),fwht(c),fwht(Z),fwht(C)
    nz=lambda f:int((f!=0).sum())
    print(f"{n:2d} | {nz(fz):6d} {nz(fc):7d} | {nz(fZ):8d} {nz(fC):8d} | {pr(fz):7.1f} {pr(fc):8.1f} | {pr(fZ):9.1f} {pr(fC):6.2f}")
