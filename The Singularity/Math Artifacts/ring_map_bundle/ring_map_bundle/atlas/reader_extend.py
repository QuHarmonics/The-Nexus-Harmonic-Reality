"""Run of seal_readers2.txt (RA7a-d): reader atlas at fresh widths 17-19.
Dean A. Kulik, QuHarmonics Research Group, ORCID 0009-0003-3128-8828."""
import sys, os, json, time, hashlib, itertools
from math import factorial
from fractions import Fraction
here = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, here)
sys.path.insert(0, os.path.join(here, '..', 'wheels'))
import numpy as np
import wheels as wh
import importlib.util
spec = importlib.util.spec_from_file_location('ra', os.path.join(here, 'reader_atlas_lib.py'))
ra = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ra)

T0 = time.time()
seal = hashlib.sha256(open(os.path.join(here, 'seal_readers2.txt'), 'rb').read()).hexdigest()
print('seal', seal, flush=True)
out = {'seal': seal, 'by_n': {}}
claims = dict(RA7a=True, RA7b=True, RA7c=True, RA7d=True)
for n in [int(v) for v in os.environ.get('NS', '17,18,19').split(',')]:
    t0 = time.time()
    N = 1 << n
    h = n // 2
    _, _, Pw, R, loc = wh.ring_arrays(n)
    x = np.arange(N, dtype=np.int64)
    face = (x > Pw).astype(np.int64)
    addr = loc[x]
    succ = R[(addr + 1) % N]
    V = np.zeros(N, np.uint64)
    o = ra.bits_into(V, face, 0, 1)
    o0 = o; o = ra.bits_into(V, addr, o, n); m_addr = ((1 << n) - 1) << o0
    o0 = o; o = ra.bits_into(V, succ, o, n); m_succ = ((1 << n) - 1) << o0
    o0 = o; o = ra.bits_into(V, Pw, o, n); m_par = ((1 << n) - 1) << o0
    perbit, _ = ra.fold_counts(V, n, [1, m_addr, m_succ, m_par])
    print(f'n={n} fold done {time.time() - t0:.1f}s', flush=True)
    rec = {}
    # face
    u = perbit[0]; f, cnt = ra.dp(u, n); opt = ra.optimal_orders(n, u, f, limit=5000)
    a_ok = (int(f[0]) == 4 * N - 5 * N // (1 << h)) and int(cnt[0]) == (1 << h) and set(opt) == ra.outside_in_variants(n)
    rec['face'] = dict(min_mean=str(Fraction(int(f[0]), N)), count=int(cnt[0]), ok=a_ok)
    claims['RA7a'] &= a_ok
    # address
    u = perbit[1]; f, cnt = ra.dp(u, n); opt = ra.optimal_orders(n, u, f, limit=5000)
    k = 2 + int(np.floor(np.log2(n - 7)))
    fam = set()
    for flips in itertools.product((0, 1), repeat=k):
        seq = []
        for j, fl in enumerate(flips):
            seq += [j, n - 1 - j] if fl else [n - 1 - j, j]
        rest = sorted(set(range(n)) - set(seq), reverse=True)
        fam.add(tuple(seq + rest))
    b_ok = int(cnt[0]) == (1 << k) and set(opt) == fam
    rec['address'] = dict(min_mean=str(Fraction(int(f[0]), N * n)), min_mean_float=f[0] / (N * n), count=int(cnt[0]),
                          k_predicted=k, ok=b_ok, optimal=[list(q) for q in opt[:64]])
    claims['RA7b'] &= b_ok
    # successor
    u = perbit[2]; f, cnt = ra.dp(u, n); opt = ra.optimal_orders(n, u, f, limit=5000)
    tail = [n - 2]
    for j in range(2, h):
        tail += [j, n - 1 - j]
    if n % 2:
        tail.append(h)
    fam_s = set(tuple(list(p) + tail) for p in itertools.permutations((0, 1, n - 1)))
    c_ok = int(cnt[0]) == 6 and set(opt) == fam_s
    rec['successor'] = dict(min_mean=str(Fraction(int(f[0]), N * n)), min_mean_float=f[0] / (N * n), count=int(cnt[0]), ok=c_ok,
                            optimal=[list(q) for q in opt[:8]])
    claims['RA7c'] &= c_ok
    # partner
    u = perbit[3]; f, cnt = ra.dp(u, n)
    pair_of = {}
    def pc(S, b, n=n, h=h):
        half = [j for j in range(h) if ((S >> j) & 1) != ((S >> (n - 1 - j)) & 1)]
        if half:
            j = half[0]
            return b in (j, n - 1 - j)
        if n % 2 and b == h:
            return all((S >> j) & 1 for j in range(h))
        return True
    rc = ra.restricted_count(n, u, f, pc)
    d_ok = int(cnt[0]) == factorial(h) * (1 << h) and rc == int(cnt[0])
    rec['partner'] = dict(min_mean=str(Fraction(int(f[0]), N * n)), min_mean_float=f[0] / (N * n), count=int(cnt[0]),
                          pair_consecutive_optimal=rc, ok=d_ok)
    claims['RA7d'] &= d_ok
    rec['seconds'] = time.time() - t0
    out['by_n'][n] = rec
    print(f'n={n} face {a_ok} [{rec["face"]["count"]}] | address {b_ok} [{rec["address"]["count"]}] k={k} min {rec["address"]["min_mean_float"]:.5f} '
          f'first {rec["address"]["optimal"][0]} | successor {c_ok} [{rec["successor"]["count"]}] | partner {d_ok} [{rec["partner"]["count"]}] | {rec["seconds"]:.1f}s', flush=True)
out['claims'] = claims
out['seconds'] = time.time() - T0
out['seal_after'] = hashlib.sha256(open(os.path.join(here, 'seal_readers2.txt'), 'rb').read()).hexdigest()
print('claims', claims, 'seconds %.1f' % out['seconds'], 'seal unchanged', out['seal_after'] == seal)
json.dump(out, open(os.path.join(here, 'reader_extend_results.json'), 'w'), indent=1, default=str)
