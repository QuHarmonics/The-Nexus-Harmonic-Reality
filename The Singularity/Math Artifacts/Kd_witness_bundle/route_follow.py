"""Nested location test: is the q_{D+k} witness the same path as q_D, relocated by delta -> delta/2^k ?"""
from fractions import Fraction as F
import time
from witness_Kd import A_profile, qD, profile
half = F(1,2)
comps = {}
t=time.time()
for D in range(8, 19):
    comps[D] = [(a-half, b-half) for a,b in A_profile(qD(D), D) if a >= half]   # right of seam, as delta
    print(f"D={D}: {len(comps[D])} comps right of seam   ({time.time()-t:.1f}s)", flush=True)

def hits(dlo, dhi, D):
    return [(a,b) for a,b in comps.get(D,[]) if a < dhi and dlo < b]

for k in (1, 2):
    print(f"\n== delta -> delta/{2**k}: does component at D land inside a component at D+{k}? ==")
    for D in range(8, 19-k):
        n_in = 0
        for a,b in comps[D]:
            A,B = a/2**k, b/2**k
            if any(x<=A and B<=y for x,y in comps[D+k]): n_in += 1
        print(f"  D={D}->{D+k}: {n_in}/{len(comps[D])} components map wholly inside")

print("\n== trace chains under delta/2 (consecutive D) ==")
def inside(a,b,D):
    for x,y in comps[D]:
        if x<=a and b<=y: return (x,y)
    return None
for D0 in range(13, 18):
    for a,b in comps[D0]:
        chain=[(D0,a,b)]; ca,cb=a,b; D=D0
        while D+1 in comps:
            c = inside(ca/2, cb/2, D+1)
            if not c: break
            D+=1; ca,cb=c; chain.append((D,ca,cb))
        if len(chain)>=3:
            print(f"  start D={D0}: chain length {len(chain)}")
            for (d,x,y) in chain:
                Sd=d*(1<<d); n=x*Sd
                print(f"     D={d}: delta=[{x}, {y})  delta*S_D={float(n):.3f}  j=floor(2^D d)={int(x*(1<<d))}")
