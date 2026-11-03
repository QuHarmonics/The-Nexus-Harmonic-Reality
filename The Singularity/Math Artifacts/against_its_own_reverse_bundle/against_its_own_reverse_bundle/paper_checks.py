"""paper_checks.py - every identity stated in "Against Its Own Reverse", rechecked from scratch,
and the figures. Dean A. Kulik, QuHarmonics Research Group, ORCID 0009-0003-3128-8828.
Words are MSB-first strings x_0..x_{n-1}; as integers, string position j is integer bit n-1-j.
Exact integer arithmetic throughout. Run: python3 paper_checks.py"""
import time, random
from math import comb, isqrt
import numpy as np

T0 = time.time()
LOG = []
def report(tag, ok, scope):
    LOG.append((tag, ok, scope)); print(f'[{"RUNS" if ok else "FAILS"}] {tag}: {scope}'); assert ok, tag

# ---------------------------------------------------------------- basic machinery
def revarr(w, n):
    r = np.zeros_like(w)
    for b in range(n): r |= ((w >> b) & 1) << (n - 1 - b)
    return r
def popc(w, n):
    s = np.zeros_like(w)
    for b in range(n): s += (w >> b) & 1
    return s
def partner_arr(w, n):
    J = revarr(w, n); return np.where(J == w, ((1 << n) - 1) ^ w, J)
def ring(n):
    N = 1 << n; w = np.arange(N, dtype=np.int64); Pw = partner_arr(w, n)
    reps = w[w < Pw]; R = np.concatenate([reps, Pw[reps][::-1]])
    if n > 1: R[N//2 - 1], R[N//2] = R[N//2], R[N//2 - 1]
    return R
def fwht(a):
    a = a.astype(np.int64).copy(); hh = 1
    while hh < len(a):
        a = a.reshape(-1, 2*hh); x = a[:, :hh].copy(); y = a[:, hh:].copy()
        a[:, :hh] = x + y; a[:, hh:] = x - y; a = a.reshape(-1); hh *= 2
    return a
def degarr(N): return np.array([bin(s).count('1') for s in range(N)])
def Jint(x, n):
    r = 0
    for _ in range(n): r = (r << 1) | (x & 1); x >>= 1
    return r
def Pint(x, n):
    r = Jint(x, n); return r if r != x else ((1 << n) - 1) ^ x
def sgn(v): return (v > 0) - (v < 0)

# strings for the ladder
def Ps(w):
    r = w[::-1]; return r if r != w else ''.join('1' if c == '0' else '0' for c in w)
canon = lambda w: min(w, Ps(w))
Cs = lambda s: ''.join('1' if c == '0' else '0' for c in s)
ins = lambda x, m: x[:len(x)//2] + m + x[len(x)//2:]
def E_(x, m): return canon(m + x + m)
def G_(x, m): return '0' + (Ps(x) if m == '1' else x) + '1'
def up_even(w):
    a, c, u = w[0], w[-1], w[1:-1]
    if a != c: return ins(canon(u), '1' if u != canon(u) else '0'), 1
    if a == '1': return ins(u, '1'), 0
    if u == u[::-1] and u[0] == '1': return ins(Cs(u), '1'), 0
    return ins(u, '0'), 0
def route(x):
    a = canon(x); e = int(x != a); back = []
    while len(a) > 1:
        L = len(a)
        if L == 2: back.append(('d', int(a[1]))); a = '0'
        elif L % 2: hh = L // 2; back.append(('m', int(a[hh]))); a = a[:hh] + a[hh+1:]
        else: a, d = up_even(a); back.append(('d', d))
    return back[::-1], e
def decode(rt, e):
    a = '0'
    for kind, b in rt:
        if len(a) == 1: a = '0' + str(b)
        elif len(a) % 2 == 0: a = ins(a, str(b))
        else:
            hh = len(a) // 2; m = a[hh]; x = a[:hh] + a[hh+1:]
            a = E_(x, m) if b == 0 else G_(x, m)
    return Ps(a) if e else a

# closed address
def cdiv(a, b): return -((-a) // b)
def Rrect(h, u, v):
    if u >= 1 << h: return v
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
        A = p >> h; return A*(H - A) + B - 2*Rrect(h, B, A) - int(Jint(A, h) < B)
    mu = (p >> h) & 1; A = p >> (h + 1)
    return 2*A*(H - A) + mu*(H - 1 - 2*A) + B - 2*Rrect(h, B, A) - int(Jint(A, h) < B)
def palcomp(u, n):
    m = (n + 1) // 2
    return (u << (n - m)) | (Jint(u, m) if n % 2 == 0 else Jint(u >> 1, m - 1))
def pi_below(p, n):
    m = (n + 1) // 2; u = p >> (n - m); return u + int(palcomp(u, n) < p)
def rank(p, n):
    m = (n + 1) // 2; pi = pi_below(p, n)
    return (p - pi + Delta(p, n)) // 2 + min(pi, 1 << (m - 1))
def position(x, n):
    N = 1 << n; M = N >> 1; a = min(x, Pint(x, n)); r = rank(a, n)
    pa = M if r == M - 1 else r
    return pa if x == a else N - 1 - pa

# ---------------------------------------------------------------- 1. ring and pairing
ok = True
for n in range(1, 17):
    N = 1 << n; w = np.arange(N, dtype=np.int64); Pw = partner_arr(w, n)
    ok &= bool((Pw != w).all()) and np.array_equal(partner_arr(Pw, n), w)
    R = ring(n); ok &= np.array_equal(np.sort(R), w) and np.array_equal(R[::-1], partner_arr(R, n))
report('P is a fixed-point-free involution; facing law R[N-1-i] = P(R[i])', ok, 'n = 1..16, every word')

# ---------------------------------------------------------------- 2. comparator, straddle, rank
ok = True; okb = True
for n in range(2, 15):
    N = 1 << n; w = np.arange(N, dtype=np.int64); J = revarr(w, n); c = np.sign(J - w)
    D = np.concatenate([[0], np.cumsum(c)])            # D[p] = Delta(p), p = 0..N
    lo = np.minimum(w, J); hi = np.maximum(w, J); nonpal = J != w
    strad = np.zeros(N + 1, dtype=np.int64)            # #{x: x < p <= J(x)} via difference array over pairs (lo, hi]
    np.add.at(strad, lo[nonpal & (w < J)] + 1, 1); np.add.at(strad, hi[nonpal & (w < J)] + 1, -1)
    strad = np.cumsum(strad)
    ok &= np.array_equal(D, strad)
    ok &= all(Delta(p, n) == int(D[p]) for p in range(N))
    reps = (w < partner_arr(w, n)); rk = np.concatenate([[0], np.cumsum(reps)])
    ok &= all(rank(p, n) == int(rk[p]) for p in range(N))
    # borrow chain: borrow(a-b) with cells Maj(not a, b, beta), LSB first
    def borrow(a, b):
        bo = np.zeros(N, dtype=np.int64)
        for k in range(n):
            ak = (a >> k) & 1; bk = (b >> k) & 1; na = 1 - ak
            bo = (na & bk) | (na & bo) | (bk & bo)
        return bo
    okb &= np.array_equal(c, borrow(w, J) - borrow(J, w))
report('Delta(p) = sum_{x<p} c(x) = #{x : x < p <= J(x)} = closed even/odd formula', ok, 'n = 2..14, every threshold p')
report('rank r(p) = (p - pi(p) + Delta(p))/2 + min(pi(p), 2^(m-1))', ok, 'n = 2..14, every threshold p')
report('c(x) = borrow(x - J(x)) - borrow(J(x) - x), cells Maj(not a, b, beta)', okb, 'n = 2..14, every word')

ok = True
for n in range(2, 15):
    R = ring(n); ok &= all(position(int(R[i]), n) == i for i in range(1 << n))
pos_pi = position(0x243F6A8885A308D3, 64)
ok &= pos_pi == 2427008858123944441
report('closed position = ring address; pi at 64 bits = 2,427,008,858,123,944,441', ok, 'n = 2..14 every position; n = 64 one word')
ok = all(Delta(p, n) == Delta((1 << n) - p, n) for n in range(2, 15) for p in range(1, 1 << n))
report('Delta(N - p) = Delta(p)', ok, 'n = 2..14, every threshold')
w576 = format(int(ring(10)[576]), '010b')
report('Theorem C needs its parity hypothesis: R_10 at depth 64 is 1110000101 (five zeros)', w576 == '1110000101', 'n = 10, depth 64')

# canonical palindrome address (p + u + Delta)/2
ok = True
for n in range(2, 17):
    R = ring(n); N = 1 << n; loc = np.empty(N, dtype=np.int64); loc[R] = np.arange(N); m = (n + 1) // 2
    for u in range(1 << (m - 1)):
        p = palcomp(u, n); ok &= int(loc[p]) == (p + u + Delta(p, n)) // 2
report('canonical palindrome address i(u) = (p + u + Delta(p))/2', ok, 'n = 2..16, every canonical palindrome')

# ---------------------------------------------------------------- 3. the mirror lift
ok = True
for n in range(2, 17):
    N = 1 << n; h = n // 2; odd = n % 2; w = np.arange(N, dtype=np.int64); J = revarr(w, n); pal = J == w
    Pw = partner_arr(w, n)
    bit = lambda a, j: (a >> (n - 1 - j)) & 1
    d = np.stack([bit(w, j) ^ bit(w, n-1-j) for j in range(h)], 1) if h else np.zeros((N, 0), dtype=np.int64)
    v = np.stack([bit(w, j) for j in range(h)], 1) if h else np.zeros((N, 0), dtype=np.int64)
    dP = np.stack([bit(Pw, j) ^ bit(Pw, n-1-j) for j in range(h)], 1) if h else d
    vP = np.stack([bit(Pw, j) for j in range(h)], 1) if h else v
    ok &= np.array_equal(d, dP)
    ok &= np.array_equal((v ^ vP)[~pal], d[~pal]) and bool(((v ^ vP)[pal] == 1).all())
    # comparator = orientation of the outermost unequal pair
    c = np.sign(J - w)
    first = np.where(d.any(1), d.argmax(1), -1)
    pred = np.where(first < 0, 0, 1 - 2 * v[np.arange(N), np.maximum(first, 0)])
    ok &= np.array_equal(c, pred)
    # latitude = value half
    twoz = 2 * popc(w, n) - n
    pred2z = 2 * ((1 - d) * (2 * v - 1)).sum(1) + (2 * bit(w, h) - 1 if odd else 0)
    ok &= np.array_equal(twoz, pred2z)
    k = d.sum(1); ok &= bool((np.abs(twoz) <= 2 * (h - k) + odd).all())
    ok &= bool((np.abs(twoz[~pal]) <= n - 2).all())
    wt = popc(w, n); ok &= all(int(c[wt == ww].sum()) == 0 for ww in range(n + 1))
    # census
    ones = ((1 - d) * v).sum(1)
    for kk in range(h + 1):
        for t in range(h - kk + 1):
            ok &= int(((k == kk) & (ones == t)).sum()) == comb(h, kk) * 2**kk * comb(h - kk, t) * (1 + odd)
report('lifted partner, comparator = outermost unequal pair, latitude = equal pairs, bound, census, orthogonality', ok, 'n = 2..16, every word')

# ---------------------------------------------------------------- 4. the ladder
ok = True
for L in range(4, 17, 2):
    h = L // 2; H = 1 << h
    desc = sorted((format(i, f'0{L}b') for i in range(1 << L) if format(i, f'0{L}b') == canon(format(i, f'0{L}b'))), reverse=True)
    desc1 = sorted((format(i, f'0{L+1}b') for i in range(1 << (L+1)) if format(i, f'0{L+1}b') == canon(format(i, f'0{L+1}b'))), reverse=True)
    off1 = {x: q for q, x in enumerate(desc1)}
    for j, x in enumerate(desc):
        A = int(x[:h], 2); K = H - 1 - A
        DK = K*(K-1)//2 + max(0, K - H//2); sK = K + int(K >= H//2); i = j - DK
        ok &= 0 <= i < sK and off1[ins(x, '1')] == 2*DK + i and off1[ins(x, '0')] == 2*DK + sK + i
report('even -> odd: block K doubles; j1 = 2D_K + i, j0 = 2D_K + s_K + i', ok, 'even L = 4..16, every canonical parent')

ok = True
for L in range(2, 15, 2):
    A_L = [format(i, f'0{L}b') for i in range(1 << L) if format(i, f'0{L}b') == canon(format(i, f'0{L}b'))]
    A_L2 = {format(i, f'0{L+2}b') for i in range(1 << (L+2)) if format(i, f'0{L+2}b') == canon(format(i, f'0{L+2}b'))}
    out = []
    for x in A_L:
        for m in '01':
            e, g = E_(x, m), G_(x, m); out += [e, g]
            ok &= (int(e[0]) ^ int(e[-1])) == 0 and (int(g[0]) ^ int(g[-1])) == 1
    ok &= len(out) == len(set(out)) and set(out) == A_L2
report('E/G lift partitions the next even ring; branch bit d = a XOR c', ok, 'L = 2..14')

ok = True
for n in range(2, 15):
    h = n // 2
    for i in range(1 << n):
        x = format(i, f'0{n}b'); rt, e = route(x)
        dbits = [b for kd, b in rt if kd == 'd']; delta = [int(x[j] != x[n-1-j]) for j in range(h)]
        ok &= dbits == delta[::-1] and len(rt) == n - 1
        if n <= 12: ok &= decode(rt, e) == x
report('the route is the mirror lift: residual bits = differences, innermost first; n-1 route bits + side', ok, 'n = 2..14 every word (round trip n <= 12)')

# latitude walk along the route: two-step change (2m-1)[d=0], reflected at palindromic cores with m=1
ok = True
for L in range(2, 15, 2):
    A_L = [format(i, f'0{L}b') for i in range(1 << L) if format(i, f'0{L}b') == canon(format(i, f'0{L}b'))]
    for x in A_L:
        z0 = 2*x.count('1') - L
        for m in '01':
            mm = int(m); s = -1 if (x == x[::-1] and mm == 1) else 1
            for d, y in ((0, E_(x, m)), (1, G_(x, m))):
                zodd = z0 + (2*mm - 1)                     # twice-latitude after middle insertion
                pred = s * (zodd + (2*mm - 1) * (-1)**d)
                ok &= 2*y.count('1') - (L + 2) == pred
report('latitude walk: z_odd = z + (m - 1/2); z_child = s[z_odd + (m - 1/2)(-1)^d]', ok, 'L = 2..14, every lift output')

# ---------------------------------------------------------------- 5. spectra of c and Delta
ok = True
for n in range(2, 15):
    N = 1 << n; h = n // 2; w = np.arange(N, dtype=np.int64); c = np.sign(revarr(w, n) - w)
    ch = fwht(c); pred = np.zeros(N, dtype=np.int64)
    for j in range(h):
        for S in range(1 << j):
            mask = 0
            for k in range(j):
                if (S >> k) & 1: mask |= (1 << k) | (1 << (n - 1 - k))
            pred[mask | (1 << (n - 1 - j))] += N >> (j + 1)
            pred[mask | (1 << j)] -= N >> (j + 1)
    ok &= np.array_equal(ch, pred) and int((ch != 0).sum()) == 2*((1 << h) - 1)
    deg = degarr(N)
    for kk in range(h): ok &= int(((ch != 0) & (deg == 2*kk + 1)).sum()) == 2*comb(h, kk + 1)
    ok &= not ch[deg % 2 == 0].any()
    # Delta spectrum (doubled form), p = 0..N-1
    D = np.concatenate([[0], np.cumsum(c)[:-1]]); Dh = fwht(D)
    for s in range(1, N):
        if deg[s] % 2: ok &= 2*int(Dh[s]) == -int(ch[s])
        else:
            j = (s & -s).bit_length() - 1
            val = -(1 << j) * int(ch[s ^ (1 << j)]) + sum((1 << k) * int(ch[s ^ (1 << k)]) for k in range(j))
            ok &= 2*int(Dh[s]) == val
    dc = N*(N - 1)//6 - h*N//4 if n % 2 == 0 else N*(N - 2)//6 - h*N//4
    ok &= int(Dh[0]) == dc and int(Dh[0]) == N*(4*N - 3*n - 4 - (n % 2))//24
report('comparator spectrum: 2(2^h-1) odd modes, +-N/2^(j+1); Delta spectrum by the prefix kernel; zero mode closed', ok, 'n = 2..14, every mode')

# ---------------------------------------------------------------- 6. sphere and 7. waveform
ok = True; shares = []
for n in range(2, 17):
    N = 1 << n; M = N // 2; h = n // 2; m = (n + 1) // 2
    R = ring(n); JR = revarr(R, n); pal = JR == R; z2 = 2*popc(R, n) - n
    ok &= np.array_equal(z2[::-1][~pal], z2[~pal]) and np.array_equal(z2[::-1][pal], -z2[pal])
    deg = degarr(N); Z = fwht(z2); Zp = fwht(np.where(pal, z2, 0)); Zb = fwht(np.where(pal, 0, z2))
    ok &= not Zp[deg % 2 == 0].any() and not Zb[deg % 2 == 1].any()
    from fractions import Fraction as F
    share = F(int((Z[deg % 2 == 1].astype(object)**2).sum()), int((Z.astype(object)**2).sum()))
    ok &= share == (F(2, 2**h) if n % 2 == 0 else F(4*h + 1, (2*h + 1) * 2**h)); shares.append((n, share))
    # palindromes in ring order read their half-words in counting order
    halves = [int(x) >> (n - m) for x in R[pal]]; ok &= halves == list(range(1 << m))
    # the ring makes the comparison one bit
    C = np.sign(JR - R); i = np.arange(N); chi = np.where(i < M, 1, -1); ctr = (i == M-1) | (i == M)
    ok &= np.array_equal(C, chi * (1 - pal.astype(np.int64) - 2*ctr.astype(np.int64)))
    Ch = fwht(C); ok &= int(Ch[M]) == N - 2**m - 4 and int((C*C).sum()) == N - 2**m and not Ch[deg % 2 == 0].any()
report('partner on the sphere: reflection; palindromes reverse latitude', ok, 'n = 2..16, every address')
report('Walsh parity split; odd energy share 2^(1-n/2) / (4h+1)/((2h+1)2^h); half-words in counting order', ok, 'n = 2..16')
report('ring coordinates: C(i) = chi_top(i)(1 - pal - 2[centre]); coefficient N - 2^m - 4', ok, 'n = 2..16')

# carrier in half-word coordinates is degree one; first majority correction
ok = True
for n in range(2, 17):
    m = (n + 1) // 2; Mh = 1 << m
    z2u = np.array([2*bin(palcomp(u, n)).count('1') - n for u in range(Mh)], dtype=np.int64)
    f = fwht(z2u); deg = degarr(Mh); ok &= not f[deg != 1].any() if Mh > 1 else True
R5 = ring(5); loc5 = np.empty(32, dtype=np.int64); loc5[R5] = np.arange(32)
maj = lambda a, b, c: (a & b) | (a & c) | (b & c)
for u in range(8):
    u0, u1, u2 = u & 1, (u >> 1) & 1, (u >> 2) & 1
    ok &= int(loc5[palcomp(u, 5)]) == 4*u + 2*u2 + maj(1 - u0, u1, u2)
report('carrier is degree one in half-word coordinates; i_5(u) = 4u + 2u_2 + Maj(1-u_0, u_1, u_2)', ok, 'n = 2..16; n = 5 all u')

# ---------------------------------------------------------------- 8. the body
ok = True
for n in range(4, 21):
    N = 1 << n; h = n // 2; H = 1 << h
    R = ring(n); wt = popc(R, n)
    s2 = np.array([bin(i).count('1') for i in range(H)])
    ok &= np.array_equal(wt[:H], s2) and np.array_equal(wt[N-H:N-1][::-1], s2[1:]) and int(wt[N-1]) == n
report('closure: z(i) = s_2(i) - n/2 for i < 2^h, mirrored at the far end', ok, 'n = 4..20')

ok = True
for n in range(4, 19):
    N = 1 << n; M = N // 2; h = n // 2; H = 1 << h; odd = n % 2
    R = ring(n); zeros = n - popc(R, n)
    for K in range(1, H // 2):
        order = sorted(range(K), key=lambda r: Jint(r, h))
        for i, r in enumerate(order):
            if not odd:
                q = K*(K-1)//2 + i; dpred = bin(K).count('1') + bin(r).count('1')
                ok &= int(zeros[M + q]) == dpred and int(zeros[M - 1 - q]) == dpred
            else:
                for mu in (0, 1):
                    q = K*(K-1) + (1 - mu)*K + i; dpred = bin(K).count('1') + bin(r).count('1') + 1 - mu
                    ok &= int(zeros[M + q]) == dpred and int(zeros[M - 1 - q]) == dpred
            ok &= bin(K).count('1') + bin(r).count('1') <= 2*K.bit_length() - 1
report('seam: deficit = wt(K) + wt(r) (+1-mu), r in reversal order; envelope 2*bitlength(K) - 1', ok, 'n = 4..18, every block K < H/2, both faces')

ok = True
for n in range(4, 17):
    R = ring(n); R2 = ring(n + 2); N = 1 << n; M = N // 2; h = n // 2; H = 1 << h
    top = (H//2)*(H//2 - 1)//2 * (1 + n % 2)          # depths inside blocks K < H/2
    for q in range(top):
        ok &= (int(popc(np.array([R2[(N*4)//2 + q]]), n + 2)[0]) == int(popc(np.array([R[M + q]]), n)[0]) + 2)
report('radius invariance: at fixed depth the word gains a 1 at each end (pad law), the deficit is unchanged', ok, 'n = 4..16 -> n+2')

print(f'\nall checks RUN  ({time.time() - T0:.1f}s)')
open('paper_checks_output.txt', 'w').write('\n'.join(f'[{"RUNS" if o else "FAILS"}] {t}: {s}' for t, o, s in LOG) + f'\n\nall checks RUN ({time.time()-T0:.1f}s)\n')
