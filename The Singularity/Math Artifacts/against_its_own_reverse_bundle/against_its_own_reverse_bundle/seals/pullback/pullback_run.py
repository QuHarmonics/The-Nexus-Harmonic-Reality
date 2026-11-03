"""Way home for seal_pullback.txt (PB1-PB6). Dean A. Kulik, QuHarmonics Research Group.
Words are MSB-first: x_0 is the most significant bit. Exact integer arithmetic throughout."""
import hashlib, random, sys, time
from math import comb
import numpy as np

SEAL = open('seal_pullback.txt', 'rb').read()
assert hashlib.sha256(SEAL).hexdigest() == '359b4d3e9e043262928226047a9bed3feb0122a7b5c672464c11909bcd1584bd', 'seal mismatch'
print('seal verified 359b4d3e...1584bd')
t0 = time.time()

# ---------- strings: partner, canon, E/G route ----------
def P(w):
    r = w[::-1]
    return r if r != w else ''.join('1' if c == '0' else '0' for c in w)
canon = lambda w: min(w, P(w))
Cs = lambda s: ''.join('1' if c == '0' else '0' for c in s)
ins = lambda x, m: x[:len(x)//2] + m + x[len(x)//2:]

def up_even(w):
    """E/G inverse on a canonical even word of width >= 4 -> (odd parent, d)."""
    a, c, u = w[0], w[-1], w[1:-1]
    if a != c:
        return ins(canon(u), '1' if u != canon(u) else '0'), 1
    if a == '1':
        return ins(u, '1'), 0
    if u == u[::-1] and u[0] == '1':
        return ins(Cs(u), '1'), 0
    return ins(u, '0'), 0

def route(x):
    """Forward route as list of (kind, bit), kind 'd' (root or residual) or 'm' (middle); plus side bit."""
    a = canon(x); e = int(x != a); back = []
    while len(a) > 1:
        L = len(a)
        if L == 2:
            back.append(('d', int(a[1]))); a = '0'
        elif L % 2:
            h = L // 2; back.append(('m', int(a[h]))); a = a[:h] + a[h+1:]
        else:
            a, d = up_even(a); back.append(('d', d))
    return back[::-1], e

def decode(rt, e):
    """Forward E/G construction from canonical '0'."""
    a = '0'
    for kind, b in rt:
        if len(a) == 1:
            a = '0' + str(b)
        elif len(a) % 2 == 0:
            a = ins(a, str(b))
        else:
            h = len(a) // 2; m = a[h]; x = a[:h] + a[h+1:]
            a = canon(m + x + m) if b == 0 else '0' + (P(x) if m == '1' else x) + '1'
    return P(a) if e else a

def sgn(v): return (v > 0) - (v < 0)

# ---------- PB1 ----------
print('\nPB1  route residual bits = mirror differences, innermost first; c = [d!=0](1-2e)')
for n in range(2, 19):
    h = n // 2; bad = 0; badc = 0; badrt = 0
    for i in range(1 << n):
        x = format(i, f'0{n}b')
        rt, e = route(x)
        dbits = [b for k, b in rt if k == 'd']
        delta = [int(x[j] != x[n-1-j]) for j in range(h)]
        if dbits != delta[::-1]: bad += 1
        c = sgn(int(x[::-1], 2) - i)
        if c != (1 if any(delta) else 0) * (1 - 2*e): badc += 1
        if n <= 12 and decode(rt, e) != x: badrt += 1
    print(f'  n={n:2d}  residual-order fails {bad}  comparator-sign fails {badc}' + (f'  round-trip fails {badrt}' if n <= 12 else ''))
    assert bad == badc == badrt == 0

# ---------- numpy helpers ----------
def revarr(w, n):
    r = np.zeros_like(w)
    for b in range(n): r |= ((w >> b) & 1) << (n - 1 - b)
    return r
def bitsMSB(w, n, j): return (w >> (n - 1 - j)) & 1     # string position j
def popc(w, n):
    s = np.zeros_like(w)
    for b in range(n): s += (w >> b) & 1
    return s

# ---------- PB2, PB3, PB4 ----------
print('\nPB2  partner in lifted coordinates;  PB3  latitude = value half, bound, census;  PB4  orthogonality')
for n in range(2, 19):
    N = 1 << n; h = n // 2; odd = n % 2
    w = np.arange(N, dtype=np.int64); J = revarr(w, n); pal = J == w
    Pw = np.where(pal, (N - 1) ^ w, J)
    D = np.zeros((N, h), dtype=np.int64); V = np.zeros((N, h), dtype=np.int64)
    DP = np.zeros((N, h), dtype=np.int64); VP = np.zeros((N, h), dtype=np.int64)
    for j in range(h):
        D[:, j] = bitsMSB(w, n, j) ^ bitsMSB(w, n, n-1-j); V[:, j] = bitsMSB(w, n, j)
        DP[:, j] = bitsMSB(Pw, n, j) ^ bitsMSB(Pw, n, n-1-j); VP[:, j] = bitsMSB(Pw, n, j)
    pb2 = np.array_equal(D, DP)
    flip = V ^ VP
    nonpal = ~pal
    pb2 &= np.array_equal(flip[nonpal], D[nonpal])                       # flips exactly on unequal pairs
    pb2 &= bool((flip[pal] == 1).all())                                  # palindromes: every value flips
    if odd:
        mid = bitsMSB(w, n, h); midP = bitsMSB(Pw, n, h)
        pb2 &= bool((mid[nonpal] == midP[nonpal]).all()) and bool((mid[pal] != midP[pal]).all())
    # PB3
    k = D.sum(1); twoz = 2 * popc(w, n) - n
    pred2z = 2 * ((1 - D) * (2 * V - 1)).sum(1) + (2 * bitsMSB(w, n, h) - 1 if odd else 0)
    pb3 = np.array_equal(twoz, pred2z)
    bound2 = 2 * (h - k) + odd
    pb3 &= bool((np.abs(twoz) <= bound2).all())
    for kk in range(h + 1):
        sel = k == kk
        pb3 &= bool((np.abs(twoz[sel]) == bound2[sel]).any())
    # census
    ones_eq = ((1 - D) * V).sum(1)
    cens = True
    for kk in range(h + 1):
        for t in range(h - kk + 1):
            got = int(((k == kk) & (ones_eq == t)).sum())
            cens &= got == comb(h, kk) * 2**kk * comb(h - kk, t) * (2 if odd else 1)
    pb3 &= cens
    # PB4
    c = np.sign(J - w); wt = popc(w, n)
    pb4 = all(int(c[wt == ww].sum()) == 0 for ww in range(n + 1))
    print(f'  n={n:2d}  PB2 {pb2}  PB3 {pb3}  PB4 {pb4}')
    assert pb2 and pb3 and pb4

# ---------- PB5 ----------
def ring(n):
    N = 1 << n; w = np.arange(N, dtype=np.int64); J = revarr(w, n)
    part = np.where(J == w, (N - 1) ^ w, J); reps = w[w < part]
    R = np.concatenate([reps, part[reps][::-1]])
    if n > 1: R[N//2 - 1], R[N//2] = R[N//2], R[N//2 - 1]
    return R
def fwht(a):
    a = a.copy(); hh = 1
    while hh < len(a):
        a = a.reshape(-1, 2*hh); x = a[:, :hh].copy(); y = a[:, hh:].copy()
        a[:, :hh] = x + y; a[:, hh:] = x - y; a = a.reshape(-1); hh *= 2
    return a
print('\nPB5  the ring makes the comparison one bit; P-parity -> Walsh parity')
from fractions import Fraction as F
for n in range(2, 21):
    N = 1 << n; M = N // 2; m = (n + 1) // 2
    R = ring(n); JR = revarr(R, n); palR = JR == R
    C = np.sign(JR - R)
    i = np.arange(N); chi = np.where(i < M, 1, -1)
    centre = (i == M - 1) | (i == M)
    pred = chi * (1 - palR.astype(np.int64) - 2 * centre.astype(np.int64))
    ok = np.array_equal(C, pred)
    Ch = fwht(C)
    coef = int(Ch[M])                                # chi_top is the Walsh character of address bit n-1 from LSB = index M
    energy = int((C * C).sum())
    ok &= coef == N - 2**m - 4 and energy == N - 2**m
    share = F(coef * coef, N * energy)
    deg = np.array([bin(s).count('1') for s in range(N)])
    odd_only = not Ch[deg % 2 == 0].any()
    line = f'  n={n:2d}  C formula {ok}  coef {coef}  share {float(share):.6f}  odd-degree only {odd_only}'
    if n <= 16:
        absz = np.abs(2 * popc(R, n) - n)              # |z| is P-even
        zp = np.where(palR, 2 * popc(R, n) - n, 0)     # z on palindromes is P-odd
        e1 = not fwht(absz)[deg % 2 == 1].any(); e2 = not fwht(zp)[deg % 2 == 0].any()
        line += f'  |z| even-only {e1}  z*pal odd-only {e2}'
        ok &= e1 and e2
    print(line)
    assert ok and odd_only

# ---------- PB6 ----------
def Jint(x, n):
    r = 0
    for _ in range(n): r = (r << 1) | (x & 1); x >>= 1
    return r
def Pint(x, n):
    r = Jint(x, n)
    return r if r != x else ((1 << n) - 1) ^ x
def cdiv(a, b): return -((-a) // b)
def Rrect(h, u, v):
    H = 1 << h
    if u >= H: return v
    s = 0; rho = 0
    for j in range(h):
        uj = (u >> (h - 1 - j)) & 1
        if uj: s += cdiv(v - rho, 1 << (j + 1))
        rho += uj << j
    return s
def Delta(p, n):
    h = n // 2; H = 1 << h
    if p >= 1 << n: return 0
    B = p & (H - 1)
    if n % 2 == 0:
        A = p >> h
        return A * (H - A) + B - 2 * Rrect(h, B, A) - int(Jint(A, h) < B)
    mu = (p >> h) & 1; A = p >> (h + 1)
    return 2 * A * (H - A) + mu * (H - 1 - 2 * A) + B - 2 * Rrect(h, B, A) - int(Jint(A, h) < B)
def palcomp(u, n):
    m = (n + 1) // 2
    low = Jint(u, m) if n % 2 == 0 else Jint(u >> 1, m - 1)
    return (u << (n - m)) | low
def pi_below(p, n):
    m = (n + 1) // 2; u = p >> (n - m)
    return u + int(palcomp(u, n) < p)
def rank(p, n):
    m = (n + 1) // 2; pi = pi_below(p, n)
    return (p - pi + Delta(p, n)) // 2 + min(pi, 1 << (m - 1))
def position(x, n):
    N = 1 << n; M = N >> 1
    a = min(x, Pint(x, n)); r = rank(a, n)
    pa = M if r == M - 1 else r
    return pa if x == a else N - 1 - pa

# DP ranker from Decompiling Addressable Binary Rings (count_reps_below), string form
def partner_str(s):
    rev = s[::-1]
    return rev if rev != s else ''.join('1' if b == '0' else '0' for b in s)
def count_reps_below(r_str):
    L = len(r_str); h = L // 2; has_mid = L % 2 == 1
    dp = {(0, 0, 0): 1}
    for j in range(h):
        rl = int(r_str[j]); rr = int(r_str[L-1-j]); nxt = {}
        for (ltp, sc, rs), ways in dp.items():
            for xl in (0, 1):
                if ltp == 0 and xl > rl: continue
                nltp = 1 if (ltp == 1 or xl < rl) else 0
                for xr in (0, 1):
                    if rs == 0:
                        if xl == 1 and xr == 0: continue
                        nrs = 1 if (xl == 0 and xr == 1) else 0
                    else: nrs = 1
                    nsc = -1 if xr < rr else (1 if xr > rr else sc)
                    key = (nltp, nsc, nrs); nxt[key] = nxt.get(key, 0) + ways
        dp = nxt
    total = 0
    for (ltp, sc, rs), ways in dp.items():
        if has_mid:
            rm = int(r_str[h])
            for xm in (0, 1):
                if ltp == 0 and xm > rm: continue
                ml = 1 if (ltp == 1 or xm < rm) else 0
                if not (ml == 1 or sc == -1): continue
                if rs == 1: total += ways
        else:
            if not (ltp == 1 or sc == -1): continue
            if rs == 1: total += ways
    if L == 1: pal = 1 if r_str > '0' else 0
    else:
        k = (L + 1) // 2; pr = r_str[:k]
        if pr[0] == '1': pal = 1 << (k - 1)
        else:
            pal = int(pr[1:], 2) if k > 1 else 0
            pr_full = pr + (pr[:-1][::-1] if has_mid else pr[::-1])
            if pr_full < r_str: pal += 1
    return total + pal

print('\nPB6  closed address')
x = 0x243F6A8885A308D3
pos = position(x, 64)
print(f'  pi, 64 bits: position {pos:,}  partner at {(1<<64)-1-pos:,}  expected 2,427,008,858,123,944,441: {pos == 2427008858123944441}')
assert pos == 2427008858123944441
rng = random.Random(20261020); agree = 0
for n in (64, 255, 256, 512, 1024):
    for _ in range(12):
        xx = rng.getrandbits(n); a = min(xx, Pint(xx, n))
        r1 = rank(a, n); r2 = count_reps_below(format(a, f'0{n}b'))
        assert r1 == r2, (n, xx); agree += 1
print(f'  closed rank == DP rank on {agree} random canonical words at widths 64, 255, 256, 512, 1024')
# exhaustive small widths against the materialized ring
for n in range(2, 15):
    R = ring(n)
    assert all(position(int(R[i]), n) == i for i in range(1 << n)), n
print('  closed position == materialized ring address at every position, n = 2..14')
print(f'\nall PB1-PB6 RUN   ({time.time()-t0:.1f}s)')
