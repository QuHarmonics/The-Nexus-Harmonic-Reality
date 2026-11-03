"""u = 1/2 + 2^-p + phi*2^-(D-1):  seam bit, ONE isolated bit at depth p, 2-cycle tail (phi in {1/3,2/3}).
Which (p,phi) realise q_D?  report p relative to 2D/3, all three residues."""
from fractions import Fraction as F
from witness_Kd import profile, qD
half=F(1,2)
def works(D,p,ph):
    return profile(half + F(1,1<<p) + ph*F(1,1<<(D-1)), D) == qD(D)
for D in range(13, 41):
    hits=[]
    for p in range(D//2, D-1):
        for ph,n in ((F(2,3),"2/3"),(F(1,3),"1/3")):
            if works(D,p,ph): hits.append(f"p={p}({n})")
    print(f"D={D:2d} (D%3={D%3})  2D/3={2*D/3:5.1f}  single-bit witnesses: {', '.join(hits) if hits else 'NONE'}", flush=True)
