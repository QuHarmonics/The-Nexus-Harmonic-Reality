"""Run of seal_five_holes_replication.txt (R1-R4). Dean A. Kulik, QuHarmonics Research Group, ORCID 0009-0003-3128-8828."""
import sys, os, json, time, hashlib
from fractions import Fraction
from math import floor
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import wheels as wh

here = os.path.dirname(os.path.abspath(__file__))
out = {'seal': hashlib.sha256(open(os.path.join(here, 'seal_five_holes_replication.txt'), 'rb').read()).hexdigest()}
T0 = time.time()
print('seal', out['seal'])


def radial_bit(u, L):
    x = (1 << L) * u
    i = floor(x)
    f = x - i
    k = floor(L * f)
    wd = wh.word(i, L)
    return (wd >> (L - 1 - k)) & 1, i, k, wd


# R1
u = Fraction(49, 128)
b, i, k, wd = radial_bit(u, 4)
tau_first = int(u >= Fraction(3, 8))            # 1 - sqrt(1-2u) >= 1/2  <=>  u >= 3/8
r1 = dict(address=i, slice=k, word=format(wd, '04b'), bit=b, tau_first_digit=tau_first)
r1['ok'] = (i == 6 and k == 0 and format(wd, '04b') == '0111' and b == 0 and tau_first == 1)
print('R1', r1)
out['R1'] = r1

# R2
cls = {0: [0, 0], 1: [0, 0], 2: [0, 0]}
fails = []
passes2 = []
first14 = None
for D in range(13, 97):
    p = (2 * D) // 3 + 1
    uD = Fraction(1, 2) + Fraction(1, 1 << p) + Fraction(2, 3) * Fraction(1, 1 << (D - 1))
    target = '1' + '00' + '1' * (D - 5) + '00'
    prof = []
    detail = None
    for L in range(1, D + 1):
        bb, ii, kk, ww = radial_bit(uD, L)
        prof.append(str(bb))
        if detail is None and str(bb) != target[L - 1]:
            detail = dict(L=L, address=ii, slice=kk, word=format(ww, f'0{L}b'), read=bb, need=int(target[L - 1]))
    ok = ''.join(prof) == target
    cls[D % 3][1] += 1
    cls[D % 3][0] += int(ok)
    if not ok:
        fails.append(dict(D=D, **detail))
    elif D % 3 == 2:
        passes2.append(D)
    if D == 14:
        first14 = detail
r2 = dict(class0=cls[0], class1=cls[1], class2=cls[2], class2_passing_D=passes2, D14=first14,
          first_fail=fails[0] if fails else None)
r2['ok'] = (cls[0] == [28, 28] and cls[1] == [28, 28] and cls[2] == [6, 28] and fails[0]['D'] == 14 and
            first14 == dict(L=12, address=2052, slice=4, word='111101001111', read=0, need=1))
print('R2', r2)
out['R2'] = r2


# R3 and R4: Walsh machinery
def fwht(a):
    a = a.copy()
    h = 1
    n = len(a)
    while h < n:
        a = a.reshape(-1, 2 * h)
        x = a[:, :h].copy()
        y = a[:, h:].copy()
        a[:, :h] = x + y
        a[:, h:] = x - y
        a = a.reshape(-1)
        h *= 2
    return a


def popcount_arr(x):
    c = np.zeros_like(x)
    y = x.copy()
    while np.any(y):
        c += y & 1
        y >>= 1
    return c


def lat2(n):
    """2 z(i) = 2 wt(R[i]) - n, integer, ring address order"""
    _, _, _, R, _ = wh.ring_arrays(n)
    return 2 * popcount_arr(R) - n


def body_direct(n):
    z2 = lat2(n)
    E2 = (z2 + z2[::-1]) // 2           # 2 E(i) = z2(i) + z2(N-1-i) halved: exact (pal: 0; non-pal: equal)
    return fwht(E2.astype(np.int64))     # transform of 2E


def blocks(n, compressed=False):
    """2 B(q) on canonical offsets q from the seam, via the block decomposition (Theorem 9.2 + full masks)"""
    h = n // 2
    H = 1 << h
    M = 1 << (n - 1)
    B2 = np.zeros(M, dtype=np.int64)
    for K in range(1, H):
        S = K + (1 if 2 * K >= H else 0)
        DK = K * (K - 1) // 2 + max(0, K - H // 2)
        rs = sorted(range(S), key=lambda r: wh.J(r, h))
        if compressed:
            rs = [r for r in rs if r < K]
        for i, r in enumerate(rs):
            if r >= K:
                continue                          # palindrome slot: kept, value 0
            wK = bin(K).count('1')
            wr = bin(r).count('1')
            if n % 2 == 0:
                B2[DK + i] = 2 * (h - wK - wr)
            else:
                B2[2 * DK + i] = 2 * h - 1 + 2 - 2 * wK - 2 * wr       # mu = 1
                B2[2 * DK + S + i] = 2 * h - 1 - 2 * wK - 2 * wr        # mu = 0
    return B2


r3 = {}
ok3 = True
fold_ok = True
for n in range(4, 13):
    N = 1 << n
    M = N // 2
    Ed = body_direct(n)                       # transform of 2E
    B2 = blocks(n)
    Bh = fwht(B2)                              # transform of 2B over M offsets
    s = np.arange(N, dtype=np.int64)
    t = s & (M - 1)
    deg = popcount_arr(s)
    degt = popcount_arr(t)
    pred = np.where(deg % 2 == 0, 2 * ((-1) ** degt) * Bh[t], 0)
    match = bool(np.array_equal(pred, Ed))
    fold = bool(np.all((deg % 2 == 1) | (deg == degt + (degt % 2))))
    ok3 &= match
    fold_ok &= fold
    r3[n] = dict(all_modes_match=match, mismatched_modes=int(np.count_nonzero(pred != Ed)))
    if n == 6:
        Bc = fwht(blocks(n, compressed=True))
        sm = 3
        r3['n6_mode_000011'] = dict(direct=int(Ed[sm]) // 2, corrected=int(pred[sm]) // 2,
                                    compressed=int(2 * ((-1) ** int(degt[sm])) * Bc[int(t[sm])]) // 2)
print('R3', r3)
c6 = r3['n6_mode_000011']
r3_ok = ok3 and c6['direct'] == 0 and c6['corrected'] == 0 and c6['compressed'] == 8
out['R3'] = dict(ok=r3_ok, by_n={str(k): v for k, v in r3.items()})

shares = {}
extra = {}
for n in (4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20):
    z2 = lat2(n).astype(np.int64)
    Z = fwht(z2)
    en = Z.astype(np.float64) ** 2
    deg = popcount_arr(np.arange(1 << n, dtype=np.int64))
    tot = en.sum()
    bins = np.bincount(deg, weights=en, minlength=n + 1) / tot
    shares[n] = bins[2]
    extra[n] = dict(deg2=bins[2], deg1=bins[1], largest_bin=int(np.argmax(bins)),
                    active=int(np.count_nonzero(Z)), participation=float(tot ** 2 / (en ** 2).sum()))
    print(f'R4 n={n:2d} degree-2 share {100*bins[2]:.4f}%  degree-1 {100*bins[1]:.7f}%  largest bin {int(np.argmax(bins))}  active {extra[n]["active"]}  PR {extra[n]["participation"]:.4f}')
want = {6: 53.1250, 8: 55.9937, 10: 51.9287, 12: 46.7403, 16: 38.9498, 20: 32.7503}
r4_ok = all(abs(100 * shares[n] - v) < 5e-5 for n, v in want.items()) and fold_ok
out['R4'] = dict(ok=r4_ok, fold_ok=fold_ok, shares_percent={str(n): 100 * shares[n] for n in shares}, extra={str(k): v for k, v in extra.items()})
out['ledger'] = dict(R1=r1['ok'], R2=r2['ok'], R3=r3_ok, R4=r4_ok)
out['seconds'] = time.time() - T0
out['seal_after'] = hashlib.sha256(open(os.path.join(here, 'seal_five_holes_replication.txt'), 'rb').read()).hexdigest()
print('ledger', out['ledger'], 'seconds %.1f' % out['seconds'])
json.dump(out, open(os.path.join(here, 'five_holes_replication_results.json'), 'w'), indent=1, default=str)
