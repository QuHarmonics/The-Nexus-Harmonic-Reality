"""Certificate: an explicit witness u for q_D = 100 1^(D-5) 00 at every D in [8, 40], each checked by the
exact O(L) reader (no ring built). Method recorded per D:
  LAW    u = 1/2 + 2^-(floor(2D/3)+1) + (2/3) 2^-(D-1)              (D = 0,1 mod 3, D >= 13)
  BIT    u = 1/2 + 2^-p + phi 2^-(D-1), one isolated bit p, phi in {1/3,2/3}
  J2     u = 1/2 + 2^-(D-1) (J + phi)      (2-cycle tail, J read on the derived family)
  ATOM   leftmost component of A_{q_D}    (small D, exact interval propagation)
Then: the law alone to D=75 (D = 0,1 mod 3)."""
import json, math
from fractions import Fraction as F
from witness_Kd import profile, qD, A_profile
from Kd_law import uD, KD
half = F(1, 2)

def witness(D):
    if D % 3 != 2 and D >= 13:
        return "LAW", uD(D)
    for p in range(D // 2, D - 1):
        for ph in (F(2, 3), F(1, 3)):
            u = half + F(1, 1 << p) + ph * F(1, 1 << (D - 1))
            if profile(u, D) == qD(D): return f"BIT p={p} phi={ph}", u
    for J in range(0, 8 * D):
        for ph in (F(2, 3), F(1, 3)):
            u = half + F(1, 1 << (D - 1)) * (J + ph)
            if profile(u, D) == qD(D): return f"J2 J={J} phi={ph}", u
    a, b = A_profile(qD(D), D)[0]
    return "ATOM", a + (b - a) / 2

cert = []
for D in range(8, 41):
    how, u = witness(D)
    ok = profile(u, D) == qD(D)
    cert.append({"D": D, "q_D": qD(D), "method": how, "u": f"{u.numerator}/{u.denominator}",
                 "reads": profile(u, D), "RUNS": ok})
    print(f"D={D:2d} (D%3={D%3})  {'RUNS' if ok else 'FAIL'}  {how:<22s}  u-1/2 ~ 2^{math.log2(float(u-half)):6.2f}")
allok = all(c["RUNS"] for c in cert)
print(f"\nevery D in [8,40] has a checked witness: {allok}")

law = []
for D in range(13, 76):
    if D % 3 == 2: continue
    lo, hi, _ = KD(D)
    law.append({"D": D, "RUNS": profile(uD(D), D) == qD(D),
                "K_D": [f"{lo.numerator}/{lo.denominator}", f"{hi.numerator}/{hi.denominator}"]})
print(f"law u_D, D = 0,1 mod 3, 13..75: {sum(x['RUNS'] for x in law)}/{len(law)} RUNS")
json.dump({"per_D_witness_8_40": cert, "law_0_1_mod3_13_75": law}, open("Kd_certificate.json", "w"), indent=1)
print("wrote Kd_certificate.json")
