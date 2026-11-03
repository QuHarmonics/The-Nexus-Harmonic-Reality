"""Run of seal_readiness.txt (RD1-RD3, plus the measured decompile readiness).
Dean A. Kulik, QuHarmonics Research Group, ORCID 0009-0003-3128-8828."""
import sys, os, json, time, hashlib
from fractions import Fraction
here = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, here)
import numpy as np
import wheels as wh

T0 = time.time()
out = {'seal': hashlib.sha256(open(os.path.join(here, 'seal_readiness.txt'), 'rb').read()).hexdigest()}
print('seal', out['seal'])


def orders(n):
    h = n // 2
    msb = list(range(n - 1, -1, -1))
    lsb = list(range(n))
    oi = []
    for j in range(h):
        oi += [n - 1 - j, j]
    if n % 2:
        oi.append(h)
    co = [h] if n % 2 else []
    for j in range(h - 1, -1, -1):
        co += [n - 1 - j, j]
    return {'MSB': msb, 'LSB': lsb, 'centre_out': co, 'outside_in': oi}


def readiness(inputs, outs, order, n):
    """inputs: int array of input words; outs: list of 0/1 arrays; order: bit positions of the input; returns events"""
    Nw = len(inputs)
    R = [np.full(Nw, -1, dtype=np.int64) for _ in outs]
    mask = 0
    for k in range(n + 1):
        if k > 0:
            mask |= 1 << order[k - 1]
        key = inputs & mask
        _, inv = np.unique(key, return_inverse=True)
        cnt = np.bincount(inv)
        for o, v in enumerate(outs):
            s = np.bincount(inv, weights=v)
            const = (s == 0) | (s == cnt)
            ready = const[inv]
            sel = (R[o] < 0) & ready
            R[o][sel] = k
    return R


def face_pred_outside_in(x, n):
    h = n // 2
    if h == 1:
        return 1
    for j in range(h - 1):
        if ((x >> (n - 1 - j)) & 1) != ((x >> j) & 1):
            return 2 * (j + 1)
    return 2 * h - 1 if ((x >> (n - h)) & 1) == ((x >> (n - 1)) & 1) else 2 * h


def closed_means(n):
    h = n // 2
    q = Fraction(1, 2 ** h)
    oi = Fraction(1) if h == 1 else 4 - 5 * q
    msb = (n - 1 - (h - 1) * q) if n % 2 == 0 else (n - 1 - (h + 1) * q)
    lsb = n - 1 + (h + 1) * q
    co = n - Fraction(1, 2) - q
    return {'outside_in': oi, 'MSB': msb, 'LSB': lsb, 'centre_out': co}


rd1 = {}
rd2 = {}
ok1 = ok2 = True
for n in range(2, 17):
    _, _, Pw, R, loc = wh.ring_arrays(n)
    N = 1 << n
    x = np.arange(N, dtype=np.int64)
    face = (x > Pw).astype(np.int64)
    od = orders(n)
    means = {}
    for name, order in od.items():
        Rf = readiness(x, [face], order, n)[0]
        means[name] = Fraction(int(Rf.sum()), N)
        if name == 'outside_in':
            pred = np.array([face_pred_outside_in(int(v), n) for v in x])
            per_word = bool(np.array_equal(pred, Rf))
            ok1 &= per_word
            rd1[n] = dict(per_word_exact=per_word, mean=str(means[name]), max_event=int(Rf.max()))
    cm = closed_means(n)
    match = all(means[k] == cm[k] for k in cm)
    order_ok = True
    if n >= 5:
        order_ok = all(means['outside_in'] < means[k] for k in ('MSB', 'LSB', 'centre_out'))
    if n == 4:
        order_ok = means['outside_in'] == means['MSB'] == Fraction(11, 4)
    ok1 &= (means['outside_in'] == cm['outside_in'])
    ok2 &= match and order_ok
    rd2[n] = dict(measured={k: float(v) for k, v in means.items()}, closed={k: str(v) for k, v in cm.items()}, closed_match=match, outside_in_earliest=order_ok)
    print(f'n={n:2d} face mean  outside-in {float(means["outside_in"]):.4f}  MSB {float(means["MSB"]):.4f}  LSB {float(means["LSB"]):.4f}  centre-out {float(means["centre_out"]):.4f}  closed forms {match}  per-word {rd1[n]["per_word_exact"]}')
out['RD1'] = dict(ok=ok1, by_n=rd1)
out['RD2'] = dict(ok=ok2, by_n=rd2)

rd3 = {}
ok3 = True
for n in range(4, 15):
    _, _, Pw, R, loc = wh.ring_arrays(n)
    N = 1 << n
    M = N // 2
    x = np.arange(N, dtype=np.int64)
    addr = loc[x]
    face_a = (addr >= M).astype(np.int64)
    depth = np.where(addr < M, M - 1 - addr, addr - M)
    addr_bits = [((addr >> b) & 1) for b in range(n)]
    fold_bits = [face_a] + [((depth >> b) & 1) for b in range(n - 1)]
    res = {}
    for name, order in orders(n).items():
        Ra = readiness(x, addr_bits, order, n)
        Rf = readiness(x, fold_bits, order, n)
        res[name] = dict(address=float(np.mean([r.mean() for r in Ra])), folded=float(np.mean([r.mean() for r in Rf])),
                         address_top=float(Ra[n - 1].mean()), depth_top=float(Rf[n - 1].mean() if n - 1 >= 1 else 0),
                         per_bit_address=[float(r.mean()) for r in Ra[::-1]])
    earliest_a = min(res, key=lambda k: res[k]['address'])
    earliest_f = min(res, key=lambda k: res[k]['folded'])
    strict_a = all(res['outside_in']['address'] < res[k]['address'] for k in res if k != 'outside_in')
    strict_f = all(res['outside_in']['folded'] < res[k]['folded'] for k in res if k != 'outside_in')
    if n >= 5:
        ok3 &= strict_a and strict_f
    rd3[n] = dict(res=res, earliest_address=earliest_a, earliest_folded=earliest_f, strict=(strict_a and strict_f))
    print(f'n={n:2d} address mean ' + '  '.join(f'{k} {v["address"]:.3f}' for k, v in res.items()) + f'   folded mean ' + '  '.join(f'{k} {v["folded"]:.3f}' for k, v in res.items()))
out['RD3'] = dict(ok=ok3, by_n={str(k): v for k, v in rd3.items()})

# measured: decompile, address bits MSB-first -> word bits
dec = {}
for n in range(4, 15):
    _, _, Pw, R, loc = wh.ring_arrays(n)
    N = 1 << n
    a = np.arange(N, dtype=np.int64)
    w = R[a]
    wbits = [((w >> b) & 1) for b in range(n)]           # index b = word bit x_b
    Rw = readiness(a, wbits, list(range(n - 1, -1, -1)), n)
    per = [float(r.mean()) for r in Rw]
    # by mirror pair j: (x_{n-1-j}, x_j)
    pairs = [(per[n - 1 - j] + per[j]) / 2 for j in range(n // 2)]
    dec[n] = dict(per_word_bit_msb_to_lsb=per[::-1], pair_means_outer_to_inner=pairs, middle=per[n // 2] if n % 2 else None)
    print(f'decompile n={n:2d} word-bit readiness (MSB..LSB): ' + ' '.join(f'{v:.2f}' for v in per[::-1]) + '   pairs outer->inner: ' + ' '.join(f'{v:.2f}' for v in pairs))
out['decompile_measured'] = {str(k): v for k, v in dec.items()}
out['ledger'] = dict(RD1=ok1, RD2=ok2, RD3=ok3)
out['seconds'] = time.time() - T0
out['seal_after'] = hashlib.sha256(open(os.path.join(here, 'seal_readiness.txt'), 'rb').read()).hexdigest()
print('ledger', out['ledger'], 'seconds %.1f' % out['seconds'])
json.dump(out, open(os.path.join(here, 'readiness_results.json'), 'w'), indent=1, default=str)
