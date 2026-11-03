"""Run the sealed residue-2 law (seal 60a2aad0...fd65fd in residue2_prediction.sha256), then the unified
all-residue law, with K_D for every D.  Unified:  p_D = 2*floor((D+1)/3)+1 (always odd),
f_D = 2/3 + [D = 2 mod 3]/(6D),  u_D = 1/2 + 2^-p_D + f_D 2^-(D-1)."""
import sys, math, time, json, hashlib
from fractions import Fraction as F
sys.path.insert(0, "/home/claude/space/rings")
from witness_Kd import profile, qD
half = F(1, 2)
seal = open("residue2_prediction.sha256").read().split()[0]
assert hashlib.sha256(open("residue2_prediction.txt", "rb").read()).hexdigest() == seal, "seal broken"
print(f"seal verified {seal[:8]}...{seal[-8:]}")

def law(D, nudge=True):
    p = 2 * ((D + 1) // 3) + 1
    f = F(2, 3) + (F(1, 6 * D) if (D % 3 == 2 and nudge) else 0)
    return half + F(1, 1 << p) + f * F(1, 1 << (D - 1)), p, f

def K(u, D):
    lo, hi = F(0), F(1)
    for L in range(1, D + 1):
        S = L * (1 << L); j = math.floor(u * S)
        lo = max(lo, F(j, S)); hi = min(hi, F(j + 1, S))
    return lo, hi

t0 = time.time()
Dtop = int(sys.argv[1]) if len(sys.argv) > 1 else 119
print("\nSEALED RESIDUE-2 LAW and its control (f = 2/3 without the 1/(6D) term)")
r2 = []
for D in range(14, Dtop + 1, 3):
    u, p, f = law(D); u0, _, _ = law(D, nudge=False)
    lo, hi = K(u, D)
    ok = profile(u, D) == qD(D) and hi > lo
    c = profile(u0, D); diff = [i + 1 for i in range(D) if c[i] != qD(D)[i]]
    r2.append({"D": D, "RUNS": ok, "control_differs_at_rings": diff, "log2_K": math.log2(float(hi - lo))})
    if D < 30 or D % 15 == 2 or not ok:
        print(f"  D={D:3d}  p={p:3d}  {'RUNS' if ok else 'FAIL'}   control differs at ring(s) {diff}   log2|K_D|={math.log2(float(hi-lo)):8.2f}  ({time.time()-t0:.0f}s)", flush=True)
print(f"  residue 2: {sum(x['RUNS'] for x in r2)}/{len(r2)} RUNS;  control fails exactly at ring D in "
      f"{sum(x['control_differs_at_rings'] == [x['D']] for x in r2)}/{len(r2)}")

print("\nUNIFIED LAW, every D from 13 to", Dtop)
allD = []
for D in range(13, Dtop + 1):
    u, p, f = law(D); lo, hi = K(u, D)
    ok = profile(u, D) == qD(D) and hi > lo
    allD.append({"D": D, "p": p, "f": f"{f.numerator}/{f.denominator}", "RUNS": ok,
                 "K_D": [f"{lo.numerator}/{lo.denominator}", f"{hi.numerator}/{hi.denominator}"]})
    if not ok: print(f"  D={D}: FAIL")
fails = [x["D"] for x in allD if not x["RUNS"] and x["D"] >= 13]
print(f"  {sum(x['RUNS'] for x in allD)}/{len(allD)} RUNS   failures: {fails if fails else 'none'}   ({time.time()-t0:.0f}s)")
json.dump({"seal": seal, "residue2": r2, "unified": allD}, open("unified_certificate.json", "w"), indent=1)
print("wrote unified_certificate.json")
