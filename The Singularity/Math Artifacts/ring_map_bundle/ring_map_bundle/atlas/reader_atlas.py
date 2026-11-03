"""Run of seal_readers.txt (RA1-RA6): the exact best reading order for each thing the ring computes.
Dean A. Kulik, QuHarmonics Research Group, ORCID 0009-0003-3128-8828."""
import sys, os, json, time, hashlib, itertools
from math import factorial
from fractions import Fraction
here = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(here, '..', 'wheels'))
import numpy as np
import wheels as wh

T0 = time.time()
seal = hashlib.sha256(open(os.path.join(here, 'seal_readers.txt'), 'rb').read()).hexdigest()
print('seal', seal, flush=True)
NMAX = int(os.environ.get('NMAX', '16'))


# ----------------------------------------------------------------------------- not-ready counts for every arrived set
def fold_counts(V, n, masks):
    """V: uint64 truth table (bit-packed outputs) indexed by the input word. For every arrived set S (bit i = position
    i arrived) and every output group (mask), the number of not-ready (word, output bit) pairs and of words with any
    output bit of the group not ready. Folding the table along each unarrived position: 3^n work."""
    N = 1 << n
    full = N - 1
    G = len(masks)
    perbit = np.zeros((G, N), np.int64)
    anyc = np.zeros((G, N), np.int64)
    ms = [np.uint64(m) for m in masks]

    def rec(val, und, U, k, start):
        S = full ^ U
        mult = 1 << k
        for gi, m in enumerate(ms):
            um = und & m
            perbit[gi, S] = int(np.bitwise_count(um).sum()) * mult
            anyc[gi, S] = int(np.count_nonzero(um)) * mult
        for b in range(start, n):
            cb = b - k
            v = val.reshape(-1, 2, 1 << cb)
            w = und.reshape(-1, 2, 1 << cb)
            v0 = v[:, 0, :]
            nu = w[:, 0, :] | w[:, 1, :] | (v0 ^ v[:, 1, :])
            rec(np.ascontiguousarray(v0).reshape(-1), np.ascontiguousarray(nu).reshape(-1), U | (1 << b), k + 1, b + 1)

    rec(V.astype(np.uint64), np.zeros(N, np.uint64), 0, 0, 0)
    return perbit, anyc


# ----------------------------------------------------------------------------- exact optimum over all n! orders
def dp(u, n):
    N = 1 << n
    S_all = np.arange(N, dtype=np.int64)
    pc = np.bitwise_count(S_all.astype(np.uint64)).astype(np.int64)
    f = np.zeros(N, np.int64)
    cnt = np.zeros(N, np.int64)
    cnt[N - 1] = 1
    BIG = np.iinfo(np.int64).max // 4
    for k in range(n - 1, -1, -1):
        S = S_all[pc == k]
        cands = []
        for b in range(n):
            T = S | (1 << b)
            has = (S >> b) & 1
            cands.append(np.where(has == 1, BIG, f[T]))
        C = np.stack(cands)
        best = C.min(axis=0)
        c = np.zeros(len(S), np.int64)
        for b in range(n):
            T = S | (1 << b)
            c += np.where(C[b] == best, cnt[T], 0)
        f[S] = u[S] + best
        cnt[S] = c
    return f, cnt


def optimal_orders(n, u, f, limit=5000):
    res = []
    stack = [(0, ())]
    while stack and len(res) < limit:
        S, seq = stack.pop()
        if S == (1 << n) - 1:
            res.append(seq)
            continue
        need = f[S] - u[S]
        for b in range(n - 1, -1, -1):
            if not (S >> b) & 1 and f[S | (1 << b)] == need:
                stack.append((S | (1 << b), seq + (b,)))
    return res


def restricted_count(n, u, f, allowed):
    """number of optimal orders whose every move is allowed(S, b)"""
    from functools import lru_cache
    full = (1 << n) - 1

    @lru_cache(maxsize=None)
    def g(S):
        if S == full:
            return 1
        need = f[S] - u[S]
        t = 0
        for b in range(n):
            if not (S >> b) & 1 and f[S | (1 << b)] == need and allowed(S, b):
                t += g(S | (1 << b))
        return t
    return g(0)


def cost(order, u):
    S = 0
    c = 0
    for b in order:
        c += int(u[S])
        S |= 1 << b
    return c


def outside_in_variants(n):
    h = n // 2
    vs = set()
    for flips in itertools.product((0, 1), repeat=h):
        seq = []
        for j, fl in enumerate(flips):
            a, b = n - 1 - j, j
            seq += [b, a] if fl else [a, b]
        if n % 2:
            seq.append(h)
        vs.add(tuple(seq))
    return vs


def ref_orders(n):
    h = n // 2
    oi = []
    for j in range(h):
        oi += [n - 1 - j, j]
    if n % 2:
        oi.append(h)
    co = [h] if n % 2 else []
    for j in range(h - 1, -1, -1):
        co += [n - 1 - j, j]
    k = h - 1 if n % 2 else h - 2
    tw = []
    for j in range(max(k, 0)):
        tw += [n - 1 - j, j]
    core = sorted(set(range(n)) - set(tw), reverse=True)
    return {'MSB': tuple(range(n - 1, -1, -1)), 'LSB': tuple(range(n)), 'outside_in': tuple(oi),
            'centre_out': tuple(co), 'two_wheel_by_value': tuple(tw + core)}


def J_arr(x, n):
    r = np.zeros_like(x)
    y = x.copy()
    for _ in range(n):
        r = (r << 1) | (y & 1)
        y >>= 1
    return r


def bits_into(V, arr, off, width):
    for b in range(width):
        V |= (((arr >> b) & 1).astype(np.uint64)) << np.uint64(off + b)
    return off + width


# ----------------------------------------------------------------------------- run
results = {'seal': seal, 'by_n': {}}
claims = {k: True for k in ('RA1', 'RA2', 'RA3', 'RA4', 'RA4_gemini_by_value', 'RA5', 'RA6')}
claim_notes = {k: [] for k in claims}

for n in range(4, NMAX + 1):
    t0 = time.time()
    N = 1 << n
    M = N // 2
    h = n // 2
    _, _, Pw, R, loc = wh.ring_arrays(n)
    x = np.arange(N, dtype=np.int64)
    Jx = J_arr(x, n)
    face = (x > Pw).astype(np.int64)
    pal = (Jx == x).astype(np.int64)
    lt = (x < Jx).astype(np.int64)
    gt = (x > Jx).astype(np.int64)
    addr = loc[x]
    reps = np.sort(x[x < Pw])
    canon = np.minimum(x, Pw)
    pidx = np.searchsorted(reps, canon).astype(np.int64)
    succ = R[(addr + 1) % N]
    face_a = (addr >= M).astype(np.int64)
    depth = np.where(addr < M, M - 1 - addr, addr - M)
    # pass A
    VA = np.zeros(N, np.uint64)
    o = 0
    o = bits_into(VA, face, o, 1); m_face = 1
    o = bits_into(VA, pal, o, 1); m_pal = 2
    o = bits_into(VA, lt, o, 1); o = bits_into(VA, gt, o, 1); m_c = 0b1100
    o0 = o; o = bits_into(VA, addr, o, n); m_addr = ((1 << n) - 1) << o0
    o0 = o; o = bits_into(VA, pidx, o, n - 1); m_pidx = ((1 << (n - 1)) - 1) << o0
    gA = [('face', m_face, 1), ('c', m_c, 2), ('pal', m_pal, 1), ('address', m_addr, n), ('pair_index', m_pidx, n - 1)]
    # pass B
    VB = np.zeros(N, np.uint64)
    o = 0
    o0 = o; o = bits_into(VB, Pw, o, n); m_par = ((1 << n) - 1) << o0
    o0 = o; o = bits_into(VB, succ, o, n); m_suc = ((1 << n) - 1) << o0
    o0 = o; o = bits_into(VB, face_a, o, 1); o = bits_into(VB, depth, o, n - 1); m_fold = ((1 << n) - 1) << o0
    gB = [('partner', m_par, n), ('successor', m_suc, n), ('folded', m_fold, n)]
    # pass C: decompile, the address arrives
    VC = np.zeros(N, np.uint64)
    bits_into(VC, R, 0, n)
    gC = [('decompile_word', (1 << n) - 1, n)]

    rec_n = {}
    refs = ref_orders(n)
    oiv = outside_in_variants(n)
    for V, groups in ((VA, gA), (VB, gB), (VC, gC)):
        perbit, anyc = fold_counts(V, n, [m for _, m, _ in groups])
        for gi, (name, m, width) in enumerate(groups):
            entry = {}
            for mode, u in (('per_bit', perbit[gi]), ('whole', anyc[gi])):
                if width == 1 and mode == 'whole':
                    continue
                f, cnt = dp(u, n)
                denom = N * (width if mode == 'per_bit' else 1)
                opt = optimal_orders(n, u, f)
                e = dict(min_mean=str(Fraction(int(f[0]), denom)), min_mean_float=f[0] / denom, optimal_count=int(cnt[0]),
                         optimal_orders=[list(q) for q in opt[:64]], enumerated=len(opt),
                         reference={k: cost(v, u) / denom for k, v in refs.items()})
                e['_f0'] = int(f[0])
                e['_opt_full'] = opt
                entry[mode] = e
                if name in ('face', 'c', 'pal') and mode == 'per_bit':
                    entry['_u'] = u
                    entry['_f'] = f
                if name == 'address' and mode == 'per_bit':
                    entry['_opt_all'] = opt
                if name == 'decompile_word' and mode == 'per_bit':
                    entry['_msb'] = cost(tuple(range(n - 1, -1, -1)), u)
            rec_n[name] = entry

    # ---- claims
    fa = rec_n['face']['per_bit']
    face_ok = (fa['_f0'] == 4 * N - 5 * N // (1 << h)) and fa['optimal_count'] == (1 << h) and \
        set(tuple(q) for q in fa['_opt_full']) == oiv
    if n in (15, 16):
        claims['RA1'] &= face_ok
    rec_n['face']['law'] = face_ok
    ce = rec_n['c']['whole']          # the comparator as one value (sealed: ready when its value is fixed)
    c_ok = (ce['_f0'] == 4 * N - 4 * N // (1 << h)) and ce['optimal_count'] == (1 << h) and \
        set(tuple(q) for q in ce['_opt_full']) == oiv
    claims['RA2'] &= c_ok
    if not c_ok:
        claim_notes['RA2'].append(n)
    rec_n['c']['law'] = c_ok
    pe = rec_n['pal']['per_bit']
    pair_of = {}
    for j in range(h):
        pair_of[j] = j
        pair_of[n - 1 - j] = j

    def pair_consecutive(S, b, n=n, h=h, pair_of=pair_of):
        half = [j for j in range(h) if ((S >> j) & 1) != ((S >> (n - 1 - j)) & 1)]
        if half:
            j = half[0]
            return b in (j, n - 1 - j)
        if n % 2 and b == h:
            return all((S >> j) & 1 for j in range(h))
        return True
    rc = restricted_count(n, rec_n['pal']['_u'], rec_n['pal']['_f'], pair_consecutive) if n <= 16 else None
    p_ok = (pe['_f0'] == 4 * N - 4 * N // (1 << h)) and pe['optimal_count'] == factorial(h) * (1 << h) and rc == pe['optimal_count']
    pe['pair_consecutive_optimal'] = rc
    claims['RA3'] &= p_ok
    if not p_ok:
        claim_notes['RA3'].append(n)
    rec_n['pal']['law'] = p_ok
    # address two-wheel structure
    ad = rec_n['address']['per_bit']
    k = h - 1 if n % 2 else h - 2
    opts = rec_n['address']['_opt_all']
    struct = None
    if ad['optimal_count'] == len(opts):
        heads_ok = all(set(q[2 * j:2 * j + 2]) == {n - 1 - j, j} for q in opts for j in range(max(k, 0)))
        cores = set(tuple(q[2 * max(k, 0):]) for q in opts)
        struct = dict(outer_pairs_outside_in=heads_ok, distinct_core_orders=[list(c) for c in sorted(cores)],
                      core_size=n - 2 * max(k, 0))
        a_ok = heads_ok and len(cores) == 1 and ad['optimal_count'] == (1 << max(k, 0))
        core = next(iter(cores))
        by_value = (len(cores) == 1 and list(core) == sorted(core, reverse=True))
        struct['core_by_value'] = by_value
    else:
        a_ok = False
        by_value = False
    ad['structure'] = struct
    if n >= 13:
        claims['RA4'] &= bool(a_ok)
        claims['RA4_gemini_by_value'] &= bool(a_ok and by_value)
    rec_n['address']['two_wheel_law'] = bool(a_ok)
    de = rec_n['decompile_word']['per_bit']
    d_ok = rec_n['decompile_word']['_msb'] == de['_f0']
    claims['RA5'] &= d_ok
    if not d_ok:
        claim_notes['RA5'].append(n)
    rec_n['decompile_word']['msb_optimal'] = d_ok
    # strip private
    for name in rec_n:
        for key in [kk for kk in rec_n[name] if kk.startswith('_')]:
            del rec_n[name][key]
        for mode in ('per_bit', 'whole'):
            if mode in rec_n[name]:
                for key in [kk for kk in rec_n[name][mode] if kk.startswith('_')]:
                    del rec_n[name][mode][key]
    results['by_n'][n] = rec_n
    line = (f'n={n:2d} face {fa["min_mean_float"]:.4f} [{fa["optimal_count"]}] law {face_ok} | c {ce["min_mean_float"]:.4f} '
            f'[{ce["optimal_count"]}] {c_ok} | pal {pe["min_mean_float"]:.4f} [{pe["optimal_count"]}] {p_ok} | address '
            f'{ad["min_mean_float"]:.4f} [{ad["optimal_count"]}] two-wheel {a_ok} core {struct["distinct_core_orders"] if struct else None} | '
            f'decompile MSB-first optimal {d_ok} | {time.time() - t0:.1f}s')
    print(line, flush=True)
    for name in ('partner', 'successor', 'folded', 'pair_index'):
        e = rec_n[name]['per_bit']
        print(f'      {name:11s} per-bit min {e["min_mean_float"]:.4f} [{e["optimal_count"]} orders] first {e["optimal_orders"][0] if e["optimal_orders"] else None}'
              f'  refs ' + ' '.join(f'{kk} {vv:.3f}' for kk, vv in e['reference'].items()), flush=True)

# ----------------------------------------------------------------------------- adder (RA6)
t0 = time.time()
n = 16
N = 1 << n
xx = np.arange(N, dtype=np.int64)
a = xx & 255
b = xx >> 8
VS = np.zeros(N, np.uint64)
bits_into(VS, a + b, 0, 9)
perbit, anyc = fold_counts(VS, n, [(1 << 9) - 1])
u = perbit[0]
f, cnt = dp(u, n)
opt = optimal_orders(n, u, f, limit=5000)
fam = set()
for flips in itertools.product((0, 1), repeat=8):
    seq = []
    for j, fl in enumerate(flips):
        seq += [j + 8, j] if fl else [j, j + 8]
    fam.add(tuple(seq))
add_ok = (Fraction(int(f[0]), N * 9) == Fraction(175, 18)) and int(cnt[0]) == 256 and set(opt) == fam
claims['RA6'] = add_ok
lsb_inter = tuple(itertools.chain.from_iterable((j, j + 8) for j in range(8)))
msb_inter = tuple(itertools.chain.from_iterable((j, j + 8) for j in range(7, -1, -1)))
results['adder'] = dict(min_mean=str(Fraction(int(f[0]), N * 9)), min_mean_float=f[0] / (N * 9), optimal_count=int(cnt[0]),
                        optimal_first=list(opt[0]) if opt else None, lsb_interleaved=cost(lsb_inter, u) / (N * 9),
                        msb_interleaved=cost(msb_inter, u) / (N * 9), ok=add_ok, seconds=time.time() - t0)
print('adder', {k: v for k, v in results['adder'].items()}, flush=True)

results['claims'] = claims
results['claim_failures_at_n'] = claim_notes
results['seconds'] = time.time() - T0
results['seal_after'] = hashlib.sha256(open(os.path.join(here, 'seal_readers.txt'), 'rb').read()).hexdigest()
print('claims', claims, 'failures at n', claim_notes, 'seconds %.1f' % results['seconds'], 'seal unchanged', results['seal_after'] == seal)
json.dump(results, open(os.path.join(here, 'reader_results.json'), 'w'), indent=1, default=str)
