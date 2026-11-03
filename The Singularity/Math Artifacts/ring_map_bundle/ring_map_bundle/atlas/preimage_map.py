"""Measured, not sealed: the complete preimage A(q_D) = {u in [0,1) : radial profile of u at depth D is q_D},
computed by exact interval refinement ring by ring (Hole 2A, the full set rather than one witness).
Dean A. Kulik, QuHarmonics Research Group, ORCID 0009-0003-3128-8828."""
import sys, os, json, time
from fractions import Fraction
from math import floor, ceil
here = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(here, '..', 'wheels'))
import wheels as wh

cache = {}
def bit(c, L):
    i, k = divmod(c, L)
    key = (i, L)
    if key not in cache:
        cache[key] = wh.word(i, L)
    return (cache[key] >> (L - 1 - k)) & 1


def refine(intervals, L, want):
    out = []
    S = L << L
    for a, b in intervals:
        c0 = floor(a * S)
        c1 = ceil(b * S) - 1
        run = None
        for c in range(c0, c1 + 1):
            lo = max(a, Fraction(c, S)); hi = min(b, Fraction(c + 1, S))
            if lo >= hi:
                continue
            if bit(c, L) == want:
                if run is not None and run[1] == lo:
                    run[1] = hi
                else:
                    if run is not None:
                        out.append(tuple(run))
                    run = [lo, hi]
        if run is not None:
            out.append(tuple(run))
    # merge touching
    merged = []
    for a, b in out:
        if merged and merged[-1][1] == a:
            merged[-1] = (merged[-1][0], b)
        else:
            merged.append((a, b))
    return merged


T0 = time.time()
res = {}
for D in range(13, int(os.environ.get('DMAX', '40')) + 1):
    target = '1' + '00' + '1' * (D - 5) + '00'
    A = [(Fraction(0), Fraction(1))]
    sizes = []
    for L in range(1, D + 1):
        A = refine(A, L, int(target[L - 1]))
        sizes.append(len(A))
    meas = sum(b - a for a, b in A)
    t = (D - 2) // 3
    p = 2 * t + 3
    unit = Fraction(1, 1 << (D - 1))
    rows = []
    for a, b in A:
        rows.append({"lo_minus_half_in_2^-(D-1)": float((a - Fraction(1, 2)) / unit), "width": str(b - a)})
    res[D] = dict(intervals=len(A), measure=str(meas), measure_times_2D=float(meas * (1 << D)), max_intervals_during=max(sizes),
                  p=p, first_offset_units=float(Fraction(1, 1 << p) / unit), rows=rows[:12])
    print(f'D={D:2d} intervals {len(A):3d} (peak {max(sizes):4d})  measure*2^D {float(meas * (1 << D)):.6f}  '
          f'starts at 1/2 + ' + ', '.join(f'{r["lo_minus_half_in_2^-(D-1)"]:.3f}' for r in rows[:6]) + f'  x 2^-(D-1)   [2^-p = {float(Fraction(1, 1 << p) / unit):.0f}]', flush=True)
    if len(cache) > 300000:
        cache.clear()
json.dump(res, open(os.path.join(here, 'preimage_results.json'), 'w'), indent=1)
print('seconds %.1f' % (time.time() - T0))
