"""Independent recomputation of key numbers in 'Mapping the Nested Partner Ring' with separate code paths:
brute force over all n! orders (n = 6, 7), slot-by-slot tape via wheels.word for the frame law (L <= 13),
and a materialized-ring radial reader with integer slices for the witness (D <= 22).
Dean A. Kulik, QuHarmonics Research Group, ORCID 0009-0003-3128-8828."""
import sys, os, itertools, json
from fractions import Fraction
here = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(here, '..', 'wheels'))
import wheels as wh

out = {}
# ---- 1. readers by brute force over n! orders, pure python
def ready_time(order, n, f):
    """mean readiness of output tuple f (list of tuples indexed by word) under order; per output bit"""
    N = 1 << n
    width = len(f[0])
    total = 0
    known = 0
    for t in range(n):          # before arrival t+1, known = first t positions
        groups = {}
        for x in range(N):
            key = x & known
            groups.setdefault(key, []).append(x)
        for key, xs in groups.items():
            for b in range(width):
                vals = {f[x][b] for x in xs}
                if len(vals) > 1:
                    total += len(xs)
        known |= 1 << order[t]
    return Fraction(total, N * width)

res = {}
for n in (6, 7):
    N = 1 << n
    R = [wh.word(a, n) for a in range(N)]
    loc = {w: a for a, w in enumerate(R)}
    J = [wh.J(x, n) for x in range(N)]
    P = [wh.P(x, n) for x in range(N)]
    outs = {
        'face': [(int(x > P[x]),) for x in range(N)],
        'comparator': [((J[x] > x) - (J[x] < x),) for x in range(N)],
        'pal': [(int(J[x] == x),) for x in range(N)],
        'successor': [tuple((R[(loc[x] + 1) % N] >> b) & 1 for b in range(n)) for x in range(N)],
        'address': [tuple((loc[x] >> b) & 1 for b in range(n)) for x in range(N)],
    }
    res[n] = {}
    for name, f in outs.items():
        best = None; cnt = 0
        for order in itertools.permutations(range(n)):
            v = ready_time(order, n, f)
            if best is None or v < best:
                best, cnt = v, 1
            elif v == best:
                cnt += 1
        res[n][name] = (str(best), cnt)
        print('n', n, name, best, float(best), cnt, flush=True)
out['readers_bruteforce'] = res

# ---- 2. frame law, tape built slot by slot from wheels.word
def law(L, s):
    h = L // 2; P2 = 1 << ((L + 1) // 2)
    if s <= 1: return 0
    if s == L - 1: return P2 - 2
    if s <= h - 1: return P2 - (P2 >> (s - 2))
    if s == h: return P2 - 2 if L % 2 == 0 else P2 - 6
    return P2 - 2 - (1 << (s - h + 1))
fr = {}
for L in range(6, 14):
    N = 1 << L
    words = [wh.word(a, L) for a in range(N)]
    bits = ''.join(format(w, f'0{L}b') for w in words)
    bits2 = bits + bits[:L]
    row = []
    for s in range(L):
        seen = set(bits2[i * L + s: i * L + s + L] for i in range(N))
        row.append(N - len(seen) == law(L, s))
    fr[L] = all(row)
    print('frame L', L, all(row), flush=True)
out['frames_slot_by_slot'] = fr

# ---- 3. witness with a materialized ring and integer slices
import numpy as np
rings = {L: wh.ring_arrays(L)[3] for L in range(1, 23)}
wit = {}
for D in range(13, 23):
    t = (D - 2) // 3; p = 2 * t + 3
    target = '1' + '00' + '1' * (D - 5) + '00'
    ok_all = True
    for tau in (Fraction(2, 3) + Fraction(1, 6 * D), Fraction(2, 3) + Fraction(1, 4 * D)):
        u = Fraction(1, 2) + Fraction(1, 1 << p) + tau / (1 << (D - 1))
        num, den = u.numerator, u.denominator
        prof = ''
        for L in range(1, D + 1):
            a = (num << L) // den                      # floor(2^L u)
            k = ((L * ((num << L) - a * den)) // den)  # floor(L {2^L u})
            w = int(rings[L][a])
            prof += str((w >> (L - 1 - k)) & 1)
        ok_all &= (prof == target)
    wit[D] = ok_all
    print('witness D', D, ok_all, flush=True)
out['witness_materialized'] = wit
json.dump(out, open(os.path.join(here, 'independent_check_results.json'), 'w'), indent=1)
