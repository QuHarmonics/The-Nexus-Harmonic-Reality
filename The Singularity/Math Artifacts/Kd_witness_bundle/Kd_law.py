"""All-depth witness for D = 0,1 (mod 3):
   u_D = 1/2 + 2^-(floor(2D/3)+1) + (2/3) 2^-(D-1)
   K_D = intersection over L<=D of the half-open slice [j/S_L,(j+1)/S_L) containing u_D.
   Every point of K_D shares u_D's slice on every ring, so every point reads profile(u_D)."""
from fractions import Fraction as F
import time, math, sys
from witness_Kd import profile, qD
half = F(1, 2)

def uD(D):
    return half + F(1, 1 << (2 * D // 3 + 1)) + F(2, 3) * F(1, 1 << (D - 1))

def KD(D):
    u = uD(D); lo, hi = F(0), F(1); edge = []
    for L in range(1, D + 1):
        S = L * (1 << L); x = u * S; j = math.floor(x)
        if x == j: edge.append(L)
        lo = max(lo, F(j, S)); hi = min(hi, F(j + 1, S))
    return lo, hi, edge

if __name__ == "__main__":
    Dmax = int(sys.argv[1]) if len(sys.argv) > 1 else 90
    t = time.time(); bad = []; first_ok = None
    for D in range(8, Dmax + 1):
        if D % 3 == 2: continue
        lo, hi, edge = KD(D)
        ok   = profile(uD(D), D) == qD(D)
        ends = profile(lo, D) == qD(D) and profile(hi - (hi - lo) / 1000, D) == qD(D)
        good = ok and ends and hi > lo
        if good and first_ok is None: first_ok = D
        if not good: bad.append(D)
        if D <= 24 or D % 15 == 0 or not good:
            print(f"D={D:3d}  {'RUNS' if good else 'FAIL'}  (profile ok={ok}, ends ok={ends})  "
                  f"left-edge rings {edge}  log2|K_D|={math.log2(float(hi - lo)):8.2f}  ({time.time() - t:.0f}s)",
                  flush=True)
    print(f"\nD=0,1 mod 3 in [8,{Dmax}]: failures -> {bad if bad else 'none'};  first RUNS at D={first_ok}")
