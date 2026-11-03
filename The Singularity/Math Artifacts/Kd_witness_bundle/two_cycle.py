"""q_D tail rides the doubling 2-cycle {1/3,2/3}.  delta = 2^-(D-1) * (J + 2/3).
Read which J realise q_D, per D, with the exact O(L) reader. No ring built."""
from fractions import Fraction as F
from witness_Kd import profile, qD
half=F(1,2)
def works(D,J):
    u = half + F(1, 1<<(D-1)) * (J + F(2,3))
    return profile(u,D) == qD(D)
for D in range(8, 33):
    Js=[J for J in range(0, 4*D) if works(D,J)]
    print(f"D={D:2d}  J in [0,{4*D}) realising q_D: {Js[:12]}{' ...' if len(Js)>12 else ''}  (count {len(Js)})", flush=True)
