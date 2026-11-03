"""Way home for seal_compression.txt (E1-E4). Dean A. Kulik, QuHarmonics Research Group."""
import hashlib, glob, gzip, json, lzma, bz2, zlib, os, random, subprocess, time
import numpy as np
from PIL import Image
import matplotlib
from scipy.signal import firwin
import ringpack as rp

T0 = time.time()
SEAL = open('seal_compression.txt', 'rb').read()
assert hashlib.sha256(SEAL).hexdigest() == '2051041e62bc6753aa37ea731b19dcf97d83841e627a8f26c9849715c8fe6156', 'seal mismatch'
print('seal verified 2051041e...8fe6156')
SD = os.path.join(matplotlib.get_data_path(), 'sample_data')
coders = {'lzma': lambda b: lzma.compress(b, preset=9 | lzma.PRESET_EXTREME),
          'bz2': lambda b: bz2.compress(b, 9), 'zlib': lambda b: zlib.compress(b, 9)}
RES = {'seal': hashlib.sha256(SEAL).hexdigest(), 'datasets': {}, 'E': {}}

# ------------------------------------------------------------------ datasets
rand = random.Random(20261020).randbytes(1 << 20)
text = b''.join(subprocess.run(['pandoc', '-t', 'plain', f], capture_output=True, check=True).stdout
                for f in sorted(glob.glob('/mnt/user-data/uploads/*.docx')))
img = np.array(Image.open(os.path.join(SD, 'grace_hopper.jpg')).convert('L'))
mri_bytes = gzip.open(os.path.join(SD, 's1045.ima.gz')).read()
mri = np.frombuffer(mri_bytes, dtype='<u2')
dem = np.load(os.path.join(SD, 'jacksboro_fault_dem.npz'))['elevation']
dem16 = np.round(dem).astype('<i2').view('<u2').ravel()
rng = np.random.default_rng(20261020)
fir = []
for c in rng.uniform(0.02, 0.98, 512):
    h = firwin(255, c, window='hamming'); fir.append(np.round(h * (32767 / np.abs(h).max())).astype(np.int64))
fir = np.array(fir)
P16 = img[:img.shape[0] // 16 * 16, :img.shape[1] // 16 * 16].astype(float)
X = P16.reshape(P16.shape[0] // 16, 16, P16.shape[1] // 16, 16).swapaxes(1, 2).reshape(-1, 256)
cov = np.cov(X, rowvar=False); cov = np.round(cov * (32767 / np.abs(cov).max())).astype(np.int64)

def u16(a):            # signed/unsigned 16-bit array -> uint16 words
    return (np.asarray(a, dtype=np.int64) & 0xFFFF).astype(np.int64)
words = {
    'RAND':   (np.frombuffer(rand, dtype=np.uint8).astype(np.int64), 8),
    'TEXT':   (np.frombuffer(text, dtype=np.uint8).astype(np.int64), 8),
    'IMAGE':  (img.ravel().astype(np.int64), 8),
    'RAND16': (np.frombuffer(rand, dtype='<u2').astype(np.int64), 16),
    'MRI':    (mri.astype(np.int64), 16),
    'DEM':    (dem16.astype(np.int64), 16),
    'FIR':    (u16(fir.ravel()), 16),
    'COV':    (u16(cov.ravel()), 16)}
for k, (w, n) in words.items():
    RES['datasets'][k] = {'words': int(len(w)), 'bits_per_word': n, 'bytes': int(len(w) * n // 8)}
    print(f'{k:6s} {len(w):8d} words of {n} bits')

def ser(w, n):
    return (w.astype('<u2') if n == 16 else w.astype(np.uint8)).tobytes()
def packbits(bits):
    return np.packbits(bits.astype(np.uint8)).tobytes()
def sizes(b):
    return {c: len(f(b)) for c, f in coders.items()}

# ------------------------------------------------------------------ word coordinates
tables = {}
for n in (8, 16):
    R, loc = rp.ring_table(n); lift = rp.lift_table(n); route = rp.route_table(n)
    N = 1 << n; w = np.arange(N, dtype=np.int64); Jw = rp._revarr(w, n); Pw = np.where(Jw == w, (N - 1) ^ w, Jw)
    cn = np.minimum(w, Pw); side = (w != cn).astype(np.int64)
    # half index from the closed rank, vectorised below via rank_np (defined in E3); exact table here by counting
    reps = (w < Pw).astype(np.int64); rk = np.concatenate([[0], np.cumsum(reps)])[:-1]
    hidx = rk[cn]
    for name, t in (('ring', loc), ('lift', lift), ('route', route)):
        assert np.array_equal(np.sort(t), w), (n, name)                  # bijection on n bits
    assert np.array_equal(np.sort(hidx[cn == w]), np.arange(N // 2))     # pairs -> [0, 2^(n-1)) one-to-one
    tables[n] = {'ring': loc, 'lift': lift, 'route': route, 'hidx': hidx, 'side': side}

def entropy_counts(s):
    _, cnt = np.unique(s, return_counts=True); return np.sort(cnt)
def H0(s):
    _, cnt = np.unique(s, return_counts=True); p = cnt / cnt.sum(); return float(-(p * np.log2(p)).sum())

out = {}
for k, (w, n) in words.items():
    t = tables[n]; row = {'H0_bits_per_word': H0(w), 'raw': sizes(ser(w, n))}
    base = entropy_counts(w)
    e1 = True
    for name in ('ring', 'lift', 'route'):
        s = t[name][w]; e1 &= np.array_equal(entropy_counts(s), base)
        inv = rp.inverse(t[name]); assert np.array_equal(inv[s], w)      # exact round trip
        row[name] = sizes(ser(s, n))
    hs = t['hidx'][w]; sd = t['side'][w]
    # side split round trip: canonical word from its index, then the side bit picks the face
    canon_from_idx = np.empty(1 << (n - 1), dtype=np.int64); N = 1 << n
    ww = np.arange(N, dtype=np.int64); Jw = rp._revarr(ww, n); Pw = np.where(Jw == ww, (N - 1) ^ ww, Jw)
    cn_all = np.minimum(ww, Pw); canon_from_idx[t['hidx'][cn_all]] = cn_all
    back = np.where(sd == 1, Pw[canon_from_idx[hs]], canon_from_idx[hs]); assert np.array_equal(back, w)
    a, b = sizes(ser(hs, n)), sizes(packbits(sd))
    row['side_split'] = {c: a[c] + b[c] for c in coders}
    row['side_bit_entropy'] = H0(sd)
    row['E1_order0_invariant'] = bool(e1)
    out[k] = row
RES['streams'] = out

print('\nbytes after coding (raw | ring | lift | route | side split), best coder marked')
for k, row in out.items():
    inp = RES['datasets'][k]['bytes']
    best = lambda d: min(d.values())
    print(f"{k:6s} in {inp:8d}  " + '  '.join(f"{nm}:{best(row[nm]):8d}" for nm in ('raw', 'ring', 'lift', 'route', 'side_split'))
          + f"   H0 {row['H0_bits_per_word']:.3f} b/w   side-bit H {row['side_bit_entropy']:.3f}")

# ------------------------------------------------------------------ E1
e1 = all(out[k]['E1_order0_invariant'] for k in out)
for k in ('RAND', 'RAND16'):
    inp = RES['datasets'][k]['bytes']
    e1 &= all(v >= inp for nm in ('raw', 'ring', 'lift', 'route', 'side_split') for v in out[k][nm].values())
RES['E']['E1'] = e1; print(f"\nE1 pigeonhole (order-0 invariant everywhere; RAND, RAND16 never shrink): {'RUNS' if e1 else 'DEAD END'}")

# ------------------------------------------------------------------ E2
e2 = True; detail = {}
for k in ('TEXT', 'IMAGE', 'MRI', 'DEM'):
    braw = min(out[k]['raw'].values()); btr = min(min(out[k][nm].values()) for nm in ('ring', 'lift', 'route', 'side_split'))
    ok = btr >= 0.98 * braw; detail[k] = {'best_raw': braw, 'best_transformed': btr, 'ratio': btr / braw}
    if k in ('IMAGE', 'MRI', 'DEM'):
        worse = out[k]['ring']['lzma'] > out[k]['raw']['lzma']; detail[k]['ring_lzma_over_raw_lzma'] = out[k]['ring']['lzma'] / out[k]['raw']['lzma']
        ok &= worse
    e2 &= ok
RES['E']['E2'] = {'pass': e2, 'detail': detail}
print(f"E2 no free compression of natural data: {'RUNS' if e2 else 'DEAD END'}")
for k, d in detail.items(): print(f"   {k:6s} best transformed / best raw = {d['ratio']:.4f}" + (f";  ring lzma / raw lzma = {d['ring_lzma_over_raw_lzma']:.3f}" if 'ring_lzma_over_raw_lzma' in d else ''))

# ------------------------------------------------------------------ E3: half index from the closed formula
def rank_np(p, n):
    m = (n + 1) // 2; h = n // 2; H = 1 << h
    u = p >> (n - m)
    pal = (u << (n - m)) | (rp._revarr(u, m) if n % 2 == 0 else rp._revarr(u >> 1, m - 1))
    pi = u + (pal < p)
    B = p & (H - 1)
    if n % 2 == 0: A = p >> h; lead = A * (H - A)
    else: b = (p >> h) & 1; A = p >> (h + 1); lead = 2 * A * (H - A) + b * (H - 1 - 2 * A)
    s = np.zeros_like(p); rho = np.zeros_like(p)
    for j in range(h):
        uj = (B >> (h - 1 - j)) & 1
        s += uj * (-((-(A - rho)) // (1 << (j + 1))))
        rho += uj << j
    JA = rp._revarr(A, h) if h else np.zeros_like(A)
    D = lead + B - 2 * s - (JA < B)
    return (p - pi + D) // 2 + np.minimum(pi, 1 << (m - 1))
e3 = True
for n in range(2, 21):
    N = 1 << n; w = np.arange(N, dtype=np.int64); Jw = rp._revarr(w, n); Pw = np.where(Jw == w, (N - 1) ^ w, Jw)
    cn = np.minimum(w, Pw); idx = rank_np(cn, n)
    reps = (w < Pw); true_rank = np.concatenate([[0], np.cumsum(reps)])[:-1]
    e3 &= np.array_equal(idx, true_rank[cn]) and np.array_equal(np.sort(idx[reps]), np.arange(N // 2)) and np.array_equal(idx, idx[Pw])
wide = {}
R = random.Random(20261020)
for n, cnt in ((64, 20), (256, 8), (1024, 3)):
    ok = True
    for _ in range(cnt):
        x = R.getrandbits(n); i = rp.half_index(x, n)
        ok &= i == rp.half_index(rp.partner(x, n), n) and 0 <= i < 1 << (n - 1) and rp.half_unindex(i, n) == rp.canon(x, n)
    wide[n] = ok; e3 &= ok
# the table itself: symmetric and antisymmetric, n = 20, random writes then reads through both members of each pair
T = rp.HalfTable(20); A = rp.HalfTable(20, antisymmetric=True); ok = True
for _ in range(4000):
    x = R.getrandbits(20); v = R.randrange(1, 10**9); T[x] = v; A[x] = v
    y = rp.partner(x, 20); ok &= T[y] == v and A[y] == (v if rp.canon(x, 20) == rp.canon(y, 20) and x == y else -v)
e3 &= ok and len(T.v) == 1 << 19
RES['E']['E3'] = {'pass': bool(e3), 'wide': wide, 'table_entries_n20': int(len(T.v))}
print(f"E3 half index: exhaustive n = 2..20, wide {wide}, HalfTable(20) holds {len(T.v):,} entries: {'RUNS' if e3 else 'DEAD END'}")

# ------------------------------------------------------------------ E4: the mirror at the data's own scale
L = fir.shape[1]
first, diff = rp.block_lift(fir); assert np.array_equal(rp.block_unlift(first, diff, L), fir)
fir_lifted = np.concatenate([np.concatenate([u16(first[i]), diff[i]]) for i in range(fir.shape[0])])
up, dl = rp.triangle_lift(cov); assert np.array_equal(rp.triangle_unlift(up, dl, cov.shape[0]), cov)
cov_lifted = np.concatenate([u16(up), dl])
lift16 = tables[16]['lift']
def lz(w): return len(coders['lzma'](ser(w, 16)))
e4 = {}
for k, raw, lifted in (('FIR', u16(fir.ravel()), fir_lifted), ('COV', u16(cov.ravel()), cov_lifted)):
    r0 = lz(raw); r1 = lz(lifted); r2 = lz(lift16[raw])
    e4[k] = {'raw_lzma': r0, 'mirror_lift_lzma': r1, 'ratio': r1 / r0, 'wrong_location_lift_lzma': r2, 'wrong_ratio': r2 / r0,
             'exact_mirror_fraction': float(np.mean(diff == 0) if k == 'FIR' else np.mean(dl == 0))}
ok4 = e4['FIR']['ratio'] <= 0.55 and e4['COV']['ratio'] <= 0.60 and e4['FIR']['wrong_ratio'] >= 0.95 and e4['COV']['wrong_ratio'] >= 0.95
RES['E']['E4'] = {'pass': ok4, **e4}
print(f"E4 mirror at the data's scale: {'RUNS' if ok4 else 'DEAD END'}")
for k, d in e4.items():
    print(f"   {k}: raw lzma {d['raw_lzma']:,}  lifted {d['mirror_lift_lzma']:,} ({d['ratio']:.3f})  "
          f"bit-level lift {d['wrong_location_lift_lzma']:,} ({d['wrong_ratio']:.3f})  exact-mirror share {d['exact_mirror_fraction']:.3f}")
RES['seconds'] = time.time() - T0
json.dump(RES, open('ring_compression_results.json', 'w'), indent=2, default=lambda o: int(o) if isinstance(o, np.integer) else float(o))
print(f'\n({RES["seconds"]:.1f}s)  results -> ring_compression_results.json')
