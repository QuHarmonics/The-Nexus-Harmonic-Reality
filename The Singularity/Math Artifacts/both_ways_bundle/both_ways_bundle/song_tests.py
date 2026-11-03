"""Run of seal_song.txt (S1-S5) and the rendered audio. Dean A. Kulik, QuHarmonics Research Group, ORCID 0009-0003-3128-8828."""
import sys, os, json, time, hashlib, itertools, wave
here = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, here)
import numpy as np
import wheels as wh

T0 = time.time()
out = {'seal': hashlib.sha256(open(os.path.join(here, 'seal_song.txt'), 'rb').read()).hexdigest()}
print('seal', out['seal'])
os.makedirs(os.path.join(here, 'audio'), exist_ok=True)


def rev_bits(s):
    return s[::-1]


# ----------------------------------------------------------------------------- S1 bar law
ok1 = True
n_checked = 0
for B in range(1, 5):
    for l in range(1, 4):
        for v in range(1 << (B * l)):
            s = format(v, f'0{B * l}b')
            bars = [s[k * l:(k + 1) * l] for k in range(B)]
            pal = (s == s[::-1])
            twins = all(bars[B - 1 - k] == bars[k][::-1] for k in range(B))
            n_checked += 1
            if pal != twins:
                ok1 = False
print('S1 bar law', ok1, 'songs checked', n_checked)
out['S1'] = dict(ok=ok1, songs=n_checked)

# ----------------------------------------------------------------------------- S2 every bar once
ok2 = True
s2 = {}
for L in (1, 2, 3):
    words = [format(i, f'0{L}b') for i in range(1 << L)]
    pal_orders = 0
    total = 0
    for perm in itertools.permutations(words):
        s = ''.join(perm)
        total += 1
        if s == s[::-1]:
            pal_orders += 1
    s2[L] = dict(orderings=total, palindromic=pal_orders)
    ok2 &= (pal_orders == 0)
tw = {}
for L in range(1, 17):
    _, _, Pw, R, loc = wh.ring_arrays(L)
    T = ''.join(format(int(x), f'0{L}b') for x in R)
    inv = ''.join((''.join('1' if c == '0' else '0' for c in format(int(x), f'0{L}b')) if wh.J(int(x), L) == int(x)
                   else format(int(x), f'0{L}b')) for x in R)
    good = (T[::-1] == inv)
    tw[L] = good
    ok2 &= good
print('S2 no palindromic ordering', s2, 'tape backward = palindromic bars inverted', all(tw.values()))
out['S2'] = dict(ok=ok2, exhaustive=s2, ring_twist_by_L=tw)

# ----------------------------------------------------------------------------- S3 audio
SR = 22050
NOTE = int(0.40 * SR)
FREQ = {'c': 261.6255653, 'd': 293.6647679, 'e': 329.6275569}
INV = {'c': 'e', 'd': 'd', 'e': 'c'}           # inversion about d


def sym_note(f, S=NOTE):
    j = np.arange(S)
    tt = (j - (S - 1) / 2) / SR
    w = np.sin(np.pi * j / (S - 1)) ** 2
    return w * np.cos(2 * np.pi * f * tt)


def adsr_note(f, S=NOTE):
    t = np.arange(S) / SR
    return np.sin(2 * np.pi * f * t) * np.exp(-t / 0.12) * (1 - np.exp(-t / 0.003))


def render(seq, kind):
    gen = sym_note if kind == 'sym' else adsr_note
    return np.concatenate([gen(FREQ[c]) for c in seq])


def rel(a, b):
    return float(np.linalg.norm(a - b) / np.linalg.norm(a))


def write_wav(name, x):
    y = x / (np.max(np.abs(x)) + 1e-12) * 0.8
    pcm = (y * 32767).astype('<i2')
    with wave.open(os.path.join(here, 'audio', name), 'wb') as wv:
        wv.setnchannels(1)
        wv.setsampwidth(2)
        wv.setframerate(SR)
        wv.writeframes(pcm.tobytes())


pal = list('cdedc')
crash = list('cdedc') + list('edcde')
x_pal = render(pal, 'sym')
x_crash = render(crash, 'sym')
x_crash_inv = render([INV[c] for c in crash], 'sym')
x_piano = render(pal, 'adsr')
e_pal = rel(x_pal, x_pal[::-1])
e_crash_back_vs_inv = rel(x_crash[::-1], x_crash_inv)
e_crash_back_vs_fwd = rel(x_crash[::-1], x_crash)
e_piano = rel(x_piano, x_piano[::-1])

# R3 tape as a rhythm: one slice per 0.12 s, a symmetric 1 kHz burst on a 1, silence on a 0
SL = int(0.12 * SR)
_, _, _, R3, _ = wh.ring_arrays(3)
T3 = ''.join(format(int(x), '03b') for x in R3)
T3_inv = ''.join((''.join('1' if c == '0' else '0' for c in format(int(x), '03b')) if wh.J(int(x), 3) == int(x)
                  else format(int(x), '03b')) for x in R3)
burst = sym_note(1000.0, SL)
def rhythm(bits):
    return np.concatenate([burst if b == '1' else np.zeros(SL) for b in bits])
r_fwd = rhythm(T3)
r_back = r_fwd[::-1]
e_rhythm_inv = rel(r_back, rhythm(T3_inv))
e_rhythm_fwd = rel(r_back, r_fwd)
ok3 = (e_pal < 1e-9 and e_crash_back_vs_inv < 1e-9 and e_crash_back_vs_fwd > 0.5 and e_piano > 0.5 and e_rhythm_inv < 1e-9)
out['S3'] = dict(ok=ok3, palindrome_cdedc_backward_vs_forward=e_pal, crash_backward_vs_inverted=e_crash_back_vs_inv,
                 crash_backward_vs_forward=e_crash_back_vs_fwd, attack_decay_cdedc_backward_vs_forward=e_piano,
                 R3_rhythm_backward_vs_palindromic_bars_inverted=e_rhythm_inv, R3_rhythm_backward_vs_forward=e_rhythm_fwd,
                 R3_tape=T3)
print('S3', out['S3'])
write_wav('01_cdedc_symmetric_notes.wav', x_pal)
write_wav('02_cdedc_symmetric_notes_backward.wav', x_pal[::-1])
write_wav('03_crash_cdedc_edcde.wav', x_crash)
write_wav('04_crash_backward.wav', x_crash[::-1])
write_wav('05_crash_inverted_about_d.wav', x_crash_inv)
write_wav('06_cdedc_attack_decay.wav', x_piano)
write_wav('07_cdedc_attack_decay_backward.wav', x_piano[::-1])
write_wav('08_ring3_rhythm.wav', r_fwd)
write_wav('09_ring3_rhythm_backward.wav', r_back)

# ----------------------------------------------------------------------------- S4 Fourier split of the tape
ok4 = True
s4 = {}
for L in range(1, 17):
    _, _, _, R, _ = wh.ring_arrays(L)
    words = R
    C = L * (1 << L)
    sh = np.arange(L - 1, -1, -1)
    Tb = ((words[:, None] >> sh[None, :]) & 1).reshape(-1).astype(np.float64)
    palw = (np.array([wh.J(int(w), L) == int(w) for w in words]))
    mask = np.repeat(palw, L).astype(np.float64)
    s = 1 - 2 * Tb
    b = s * (1 - mask)
    c = s * mask
    m = np.arange(C)
    phase = np.exp(1j * np.pi * ((m * (C - 1)) % (2 * C)) / C)          # exact angle reduction
    X = np.fft.fft(s) * phase
    Bc = np.fft.fft(b) * phase
    Cc = np.fft.fft(c) * phase
    peak = np.max(np.abs(X))
    dev = max(np.max(np.abs(Bc.imag)), np.max(np.abs(Cc.real)), np.max(np.abs(X.real - Bc.real)), np.max(np.abs(X.imag - Cc.imag))) / peak
    share = float(np.sum(X.imag ** 2) / np.sum(np.abs(X) ** 2))
    pred = 2.0 ** (-(L - (L + 1) // 2))
    good = dev < 1e-9 and abs(share - pred) < 1e-9
    ok4 &= good
    s4[L] = dict(deviation_over_peak=float(dev), imaginary_share=share, predicted=pred, ok=good)
    print(f'S4 L={L:2d} samples {C:8d} deviation/peak {dev:.2e} imaginary share {share:.6f} predicted {pred:.6f}')
out['S4'] = dict(ok=ok4, by_L=s4)


# ----------------------------------------------------------------------------- S5 all reading orders, exact DP
def not_ready_counts(n, outs):
    N = 1 << n
    x = np.arange(N, dtype=np.int64)
    u = np.zeros(N, dtype=np.int64)          # indexed by observed-position set S
    for S in range(N):
        key = x & S
        cnt = np.bincount(key, minlength=N)
        tot = 0
        for v in outs:
            sm = np.bincount(key, weights=v, minlength=N)
            nc = (sm > 0) & (sm < cnt)
            tot += int(cnt[nc].sum())
        u[S] = tot
    return u


def dp(n, u):
    N = 1 << n
    full = N - 1
    f = np.zeros(N, dtype=np.int64)
    g = np.zeros(N, dtype=object)
    g[full] = 1
    order = sorted(range(N), key=lambda S: -bin(S).count('1'))
    for S in order:
        if S == full:
            continue
        best = None
        cnt = 0
        for i in range(n):
            if not (S >> i) & 1:
                v = f[S | (1 << i)]
                if best is None or v < best:
                    best, cnt = v, g[S | (1 << i)]
                elif v == best:
                    cnt += g[S | (1 << i)]
        f[S] = u[S] + best
        g[S] = cnt
    return f, g


def optimal_orders(n, u, f, limit=4096):
    res = []
    def walk(S, seq):
        if len(res) >= limit:
            return
        if S == (1 << n) - 1:
            res.append(tuple(seq))
            return
        need = f[S] - u[S]
        for i in range(n):
            if not (S >> i) & 1 and f[S | (1 << i)] == need:
                walk(S | (1 << i), seq + [i])
    walk(0, [])
    return res


def outside_in_variants(n):
    h = n // 2
    pairs = [(n - 1 - j, j) for j in range(h)]
    vs = set()
    for flips in itertools.product((0, 1), repeat=h):
        seq = []
        for (a, b), fl in zip(pairs, flips):
            seq += [b, a] if fl else [a, b]
        if n % 2:
            seq.append(h)
        vs.add(tuple(seq))
    return vs


def cost(order, u):
    S = 0
    c = 0
    for i in order:
        c += u[S]
        S |= 1 << i
    return c


ok5 = True
s5 = {}
for n in range(4, 15):
    N = 1 << n
    _, _, Pw, R, loc = wh.ring_arrays(n)
    x = np.arange(N, dtype=np.int64)
    face = (x > Pw).astype(np.float64)
    u = not_ready_counts(n, [face])
    f, g = dp(n, u)
    best = f[0]
    h = n // 2
    pred = (4 * N - 5 * N // (1 << h)) if h >= 2 else N
    opt = optimal_orders(n, u, f)
    variants = outside_in_variants(n)
    msb = tuple(range(n - 1, -1, -1))
    rec = dict(min_mean=best / N, predicted=pred / N, optimal_orders=int(g[0]), all_outside_in=all(o in variants for o in opt),
               msb_optimal=cost(msb, u) == best)
    if n == 4:
        good = (best == 11 * N // 4) and rec['msb_optimal']
    else:
        good = (best == pred) and int(g[0]) == (1 << h) and set(opt) == variants
    if n <= 12:
        abits = [((loc[x] >> b) & 1).astype(np.float64) for b in range(n)]
        ua = not_ready_counts(n, abits)
        fa, ga = dp(n, ua)
        opta = optimal_orders(n, ua, fa, limit=256)
        oi_best = min(cost(v, ua) for v in variants)
        rec.update(addr_min_mean=fa[0] / (n * N), addr_outside_in_mean=oi_best / (n * N),
                   addr_optimal_orders=int(ga[0]), addr_outside_in_optimal=(oi_best == fa[0]),
                   addr_first_optimal=list(opta[0]) if opta else None)
        if n >= 5:
            good = good and (oi_best == fa[0])
    rec['ok'] = bool(good)
    ok5 &= bool(good)
    s5[n] = rec
    print('S5 n=%2d' % n, rec)
out['S5'] = dict(ok=ok5, by_n={str(k): v for k, v in s5.items()})
out['ledger'] = dict(S1=ok1, S2=ok2, S3=ok3, S4=ok4, S5=ok5)
out['seconds'] = time.time() - T0
out['seal_after'] = hashlib.sha256(open(os.path.join(here, 'seal_song.txt'), 'rb').read()).hexdigest()
print('ledger', out['ledger'], 'seconds %.1f' % out['seconds'])
json.dump(out, open(os.path.join(here, 'song_results.json'), 'w'), indent=1, default=str)
