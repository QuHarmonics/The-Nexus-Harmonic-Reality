"""NEXUS Working Paper 5 - One Program, Infinite Compilers.
Every number in the paper is printed by this script. Python 3 standard library only; exact integer and
rational arithmetic except where a measurement is labelled as one (seeded). Blocks A-H match the paper."""
from fractions import Fraction as F
from math import gcd, comb, lgamma, log, exp, sqrt, pi, ceil, log2
from itertools import product, permutations
import random
 
def divisors(n): return [d for d in range(1, n + 1) if n % d == 0]
def mobius(n):
    r, p, m = 1, 2, n
    while p * p <= m:
        if m % p == 0:
            m //= p
            if m % p == 0: return 0
            r = -r
        p += 1
    return -r if m > 1 else r
def P(n): return sum(mobius(d) * 2 ** (n // d) for d in divisors(n)) // n
def is_prime(n): return n > 1 and all(n % p for p in range(2, int(n ** .5) + 1))
def rot(w, k, n): return ((w << k) | (w >> (n - k))) & ((1 << n) - 1) if k % n else w
 
# ---------------------------------------------------------------- A. the register stack
print("== A. The register stack, read from 64 down ==")
ISA = [1, 2, 4, 8, 16, 32, 64]
for n in ISA:
    inh = sum(d * P(d) for d in divisors(n) if d < n)
    assert 2 ** n == sum(d * P(d) for d in divisors(n))
    print(f"LEN {n:>2}: words 2^{n}, inherited {inh}, new rings P = {P(n)}")
print("2^64 = sum over the stack of LEN*P(LEN):", 2 ** 64 == sum(n * P(n) for n in ISA))
for n in [2, 4, 8, 16]:
    h = n // 2
    fixed = {w for w in range(2 ** n) if rot(w, h, n) == w}
    print(f"half-turn fixed set of layer {n:>2} = {{uu : u in layer {h}}}:", fixed == {(u << h) | u for u in range(2 ** h)})
print("prime LEN p: every non-pole word on an orbit of exactly p (p <= 13):",
      all(all(min(k for k in range(1, p + 1) if rot(w, k % p, p) == w) == p for w in range(1, 2 ** p - 1))
          for p in [2, 3, 5, 7, 11, 13]))
def pmod(a, b):
    db = b.bit_length()
    while a.bit_length() >= db: a ^= b << (a.bit_length() - db)
    return a
def irreducible(f):
    d = f.bit_length() - 1
    return all(pmod(f, g) for g in range(2, 1 << (d // 2 + 1)))
irr = [sum(1 for f in range(1 << n, 1 << (n + 1)) if irreducible(f)) for n in range(1, 13)]
print("irreducible binary polynomials, degree 1..12:", irr, " = rings P(n):", irr == [P(n) for n in range(1, 13)])
def gf_mul(a, b, f, n):
    r = 0
    while b:
        if b & 1: r ^= a
        b >>= 1; a <<= 1
        if a >> n: a ^= f
    return r
def rank2(vs):
    vs, r = [v for v in vs if v], 0
    while vs:
        piv = max(vs); top = piv.bit_length() - 1
        vs = [v ^ piv if v >> top & 1 else v for v in vs if v != piv]; vs = [v for v in vs if v]; r += 1
    return r
for n, f in [(4, 0b10011), (8, 0b100011011)]:
    sq = lambda x: gf_mul(x, x, f, n)
    def conj(b):
        out = [b]
        for _ in range(n - 1): out.append(sq(out[-1]))
        return out
    beta = next(b for b in range(1, 2 ** n) if rank2(conj(b)) == n)
    basis = conj(beta)
    table = {}
    for c in range(2 ** n):
        x = 0
        for i in range(n):
            if c >> i & 1: x ^= basis[i]
        table[x] = c
    ok = all(table[sq(x)] == rot(table[x], 1, n) for x in range(2 ** n))
    half = lambda x: [x := sq(x) for _ in range(n // 2)][-1]
    sub = {table[x] for x in range(2 ** n) if half(x) == x}
    print(f"GF(2^{n}) normal basis: squaring = one-bit rotation: {ok}; half-turn fixed field = words uu: "
          f"{sub == {(u << n // 2) | u for u in range(2 ** (n // 2))}}")
def factor_small(m):
    fs, p = [], 2
    while p * p <= m and p < 10 ** 7:
        while m % p == 0: fs.append(p); m //= p
        p += 1
    if m > 1: fs.append(m)
    return fs
def ord2(p):
    k, x = 1, 2 % p
    while x != 1: x = x * 2 % p; k += 1
    return k
for n in [1, 2, 4, 8, 16, 32]:
    nf = factor_small(2 ** n + 1)
    print(f"layer {2 * n:>2} adds 2^{n}+1 = {'*'.join(map(str, nf))}; 2^{n} = -1 mod each: {all(pow(2, n, p) == p - 1 for p in nf)}")
print("3*5*17*257*641*65537*6700417 = 2^64 - 1:", 3 * 5 * 17 * 257 * 641 * 65537 * 6700417 == 2 ** 64 - 1)
print("odd primes < 60 that never close in a power-of-2 register:",
      [p for p in range(3, 60) if is_prime(p) and ord2(p) & (ord2(p) - 1)])
 
# ---------------------------------------------------------------- B. the first run
print("\n== B. The first run: one move (a difference arrives), one rule (equal LEN fuses) ==")
def run(bits):
    stack, closes = [], []
    for b in bits:
        stack.append(str(b)); c = 0
        while len(stack) > 1 and len(stack[-1]) == len(stack[-2]):
            t = stack.pop(); stack[-1] += t; c += 1
        closes.append(c)
    return stack, closes
print("closures per arrival, 1..16:", ''.join(map(str, run([1] * 16)[1])))
for n in [3, 7, 8, 11]:
    print(f"frame after {n:>2} arrivals: {[len(x) for x in run([1] * n)[0]]}")
first = {}
for n in range(1, 129):
    for x in run([0] * n)[0]: first.setdefault(len(x), n)
print("first arrival of each block size:", first)
random.seed(11)
fr, ct = set(), set()
for _ in range(4000):
    st, _ = run([random.randint(0, 1) for _ in range(11)])
    fr.add(tuple(map(len, st))); ct.add(tuple(st))
print(f"11 arrivals, 4000 seeded random runs: frames {fr}, distinct contents {len(ct)}")
print("all 1024 arrival strings of length 10 give distinct stacks:",
      len({tuple(run([int(c) for c in format(i, '010b')])[0]) for i in range(1024)}) == 1024)
 
# ---------------------------------------------------------------- C. wrap and join
print("\n== C. The wrapper built from the centre: WRAP S -> (S), JOIN S,T -> ST ==")
def closed(w):
    h = 0
    for c in w:
        h += 1 if c == '(' else -1
        if h < 0: return False
    return h == 0
def prime_w(w): return closed(w) and not any(closed(w[:i]) and closed(w[i:]) for i in range(2, len(w), 2))
layers = {0: ['']}
for n in range(1, 8):
    clo = [''.join(p) for p in product('()', repeat=2 * n) if closed(''.join(p))]
    pr = [w for w in clo if prime_w(w)]
    layers[n] = clo
    eq_ok = all(any(closed(w[i:] + w[:i]) for i in range(2 * n))
                for w in (''.join(p) for p in product('()', repeat=2 * n)) if w.count('(') == n)
    print(f"size {n}: closed {len(clo):>3}  wraps {len(pr):>3}  joins {len(clo) - len(pr):>3}  "
          f"wraps = whole size-{n - 1} layer wrapped: {set(pr) == {'(' + s + ')' for s in layers[n - 1]}}  "
          f"every equator ring closes from a rotation: {eq_ok}")
 
# ---------------------------------------------------------------- D. the reader's step
print("\n== D. Vocabulary is the reader's step; only whole blocks are readings ==")
def route(start, dest, w, n=8):
    x = start
    for i in range(n // w):
        x = ((x << w) | ((dest >> (n - w * (i + 1))) & ((1 << w) - 1))) & ((1 << n) - 1)
    return x
for w in (1, 2, 4):
    print(f"step {w} bit(s): lands from every start {all(route(s, d, w) == d for s in range(256) for d in range(256))}, "
          f"in {8 // w} steps; steps x width = 8")
def digits(x, b, n):
    out = []
    for _ in range(n): out.append(x % b); x //= b
    return out
random.seed(1)
for b in [2, 3, 10, 16, 22, 256]:
    n = ceil(64 / log2(b)) + 1; ch = []
    for _ in range(4000):
        x = random.getrandbits(64); k = random.randrange(64)
        ch.append(sum(p != q for p, q in zip(digits(x, b, n), digits(x ^ (1 << k), b, n))))
    print(f"base {b:>3}: one flipped bit changes {sum(ch) / len(ch):.2f} digits on average, max {max(ch)}")
print("digit widths tiling every register width 4..64:", [w for w in range(1, 9) if all(r % w == 0 for r in [4, 8, 16, 32, 64])])
def baker(x, y, b):
    q = int(b * x); return b * x - q, (y + q) / b
rev4 = lambda q: int(format(q, '04b')[::-1], 2)
random.seed(7); xs = ys = pal = 0
for _ in range(2000):
    x = F(random.getrandbits(60), 2 ** 60); y = F(random.getrandbits(60), 2 ** 60); Q = int(16 * x)
    a = baker(x, y, 16); c = (x, y)
    for _ in range(4): c = baker(*c, 2)
    xs += a[0] == c[0]; ys += c[1] == (y + rev4(Q)) / 16; pal += (a == c) == (Q == rev4(Q))
print(f"one base-16 tick vs four base-2 ticks: shape side equal {xs}/2000; value side holds the digit mirrored {ys}/2000; "
      f"identical exactly on palindromic digits {pal}/2000")
 
# ---------------------------------------------------------------- E. orientation from the rings
print("\n== E. The orientation count from the rings ==")
print("latitudes of 2l-bit words, l = 0..6:", [len({bin(w).count('1') for w in range(2 ** (2 * l))}) for l in range(7)])
def S2_on_dicke(m, k):
    # Dicke state: uniform sum of m-bit words with k ones; S^2 = S-S+ + Sz(Sz+1), up = 1
    state = {w: F(1) for w in range(2 ** m) if bin(w).count('1') == k}
    def Splus(st):
        out = {}
        for w, a in st.items():
            for i in range(m):
                if not w >> i & 1: out[w | 1 << i] = out.get(w | 1 << i, 0) + a
        return out
    def Sminus(st):
        out = {}
        for w, a in st.items():
            for i in range(m):
                if w >> i & 1: out[w ^ 1 << i] = out.get(w ^ 1 << i, 0) + a
        return out
    sz = F(2 * k - m, 2)
    res = Sminus(Splus(state))
    for w in state: res[w] = res.get(w, 0) + sz * (sz + 1) * state[w]
    ratios = {res[w] / state[w] for w in state}
    return ratios if all(w in state for w in res if res[w]) else None
for l in range(1, 5):
    vals = set().union(*[S2_on_dicke(2 * l, k) for k in range(2 * l + 1)])
    print(f"l = {l}: order-free layer of {2 * l} bits has {2 * l + 1} states; S^2 on every one = {vals} (l(l+1) = {l * (l + 1)})")
cap = [sum(2 * (2 * l + 1) for l in range(n)) for n in range(1, 8)]
print("one bit x surface, summed over l < n:", cap, " 2n^2:", [2 * n * n for n in range(1, 8)])
orbs = sorted([(n + l, n, l) for n in range(1, 9) for l in range(n)])
z, closures = 0, []
for _, n, l in orbs:
    if l == 0 and z > 0: closures.append(z)
    z += 2 * (2 * l + 1)
    if z >= 118: closures.append(118); break
print("Madelung fill on these capacities, cut at each new s:", closures)
 
# ---------------------------------------------------------------- F. pi as a stack of rings
print("\n== F. BBP is column addition on a stack of rational rings ==")
N, G = 64, 12
W = {1: 4, 4: -2, 5: -1, 6: -1}
cols = [0] * (N + G + 1)
for k in range(N + G):
    for j, c in W.items():
        d = 8 * k + j
        if k == 0 and j == 1: cols[0] += c; continue
        for m in range(1, N + G + 1 - k):
            cols[k + m] += c * ((16 * pow(16, m - 1, d)) // d)
carry = 0
for i in range(N + G, 0, -1):
    v = cols[i] + carry; cols[i], carry = v % 16, v // 16
cols[0] += carry
built = format(cols[0], 'x') + '.' + ''.join(format(x, 'x') for x in cols[1:N + 1])
def arctan_inv(x, one):
    s, t, k, sign = 0, one // x, 1, 1
    while t:
        s += sign * (t // k); t //= x * x; k += 2; sign = -sign
    return s
one = 16 ** (N + 10)
pi_fixed = (16 * arctan_inv(5, one) - 4 * arctan_inv(239, one)) // 16 ** 10   # Machin, independent of BBP
ref = format(pi_fixed, 'x'); ref = ref[0] + '.' + ref[1:N + 1]
print("ring stack:", built)
print("Machin    :", ref)
print("equal:", built == ref)
def ring_len(d):
    o = d
    while o % 2 == 0: o //= 2
    if o == 1: return 0
    k, x = 1, 16 % o
    while x != 1: x = x * 16 % o; k += 1
    return k
print("ring lengths, layer 1:", [ring_len(8 + j) for j in (1, 4, 5, 6)], " layer 6:", [ring_len(48 + j) for j in (1, 4, 5, 6)])
print("ring digits added into column 64:", sum(1 for k in range(64) for j in W if not (k == 0 and j == 1)))
 
# ---------------------------------------------------------------- G. the middle
print("\n== G. The middle of the field: words of length 2n with n ones ==")
for n in [1, 10, 1000, 10 ** 6]:
    s = exp(lgamma(2 * n + 1) - 2 * lgamma(n + 1) - 2 * n * log(2))
    print(f"2n = {2 * n:>8}: share {s:.9f}, share*sqrt(pi n) {s * sqrt(pi * n):.9f}, pi from the middle 1/(n share^2) {1 / (n * s * s):.9f}")
p_ = F(1)
for n in range(1, 2001): p_ *= F(4 * n * n, 4 * n * n - 1)
print(f"Wallis product of middle-to-middle ratios, n <= 2000: {float(2 * p_):.6f}")
print("closed wrappers / middle = 1/(n+1), 2n <= 16:", all(F(comb(2 * n, n) // (n + 1), comb(2 * n, n)) == F(1, n + 1) for n in range(1, 9)))
random.seed(3)
home = sum(1 for _ in range(200000) if sum(random.choice((1, -1)) for _ in range(100)) == 0)
print(f"walker home after 100 steps (seeded, 200000 walks): {home / 200000:.4f}; middle share {comb(100, 50) / 4 ** 50:.4f}")
 
# ---------------------------------------------------------------- H. a lane decompiled
print("\n== H. Which partial lanes balance: measured, then decompiled ==")
def orbit(x0, m):
    out, x = [], x0 % m
    while True:
        out.append(x); x = x * 16 % m
        if x == x0 % m: break
    return out
def ordm(m):
    k, x = 1, 16 % m
    while x != 1: x = x * 16 % m; k += 1
    return k
tot = indep = ok1 = ok2 = bal = bal_i = oddA = mirA = 0
for k in range(0, 2001):
    for j, a in ((1, 1), (4, 4), (5, 1), (6, 8)):
        d = 8 * k + j; o = d
        while o % 2 == 0: o //= 2
        if o <= 1: continue
        h = ordm(o); H = orbit(1, o)
        if h % 2 or (o - 1) in H: continue
        tot += 1
        eps = pow(16, h // 2, o); o1 = gcd(eps - 1, o); o2 = o // o1
        cos = orbit(a % o, o); mu = F(sum(cos), len(cos) * o)
        i2, i1 = pow(o2, -1, o1), pow(o1, -1, o2)
        lean, good = F(0), True
        for y in cos:
            al, be = F(y * i2 % o1, o1), F(y * i1 % o2, o2)
            good &= (al + be - F(y, o)) % 1 == 0
            lean += al - (1 if be < al else 0)
        ok1 += good and lean / len(cos) == mu - F(1, 2)
        bal += mu == F(1, 2)
        h1, h2 = ordm(o1), ordm(o2)
        if gcd(h1, h2) == 1:
            indep += 1
            A = [F(x, o1) for x in orbit(a * i2 % o1, o1)]
            B = [F(x, o2) for x in orbit(a * i1 % o2, o2)]
            l2 = sum(al - F(sum(1 for b in B if b < al), len(B)) for al in A) / len(A)
            ok2 += l2 == mu - F(1, 2); bal_i += mu == F(1, 2)
            oddA += h1 % 2; mirA += (o1 - 1) in orbit(1, o1)
print(f"partial-inversion lanes k <= 2000: {tot}; balanced: {bal}")
print(f"split y/o = alpha + beta and lean = E[alpha] - P(beta < alpha), exact: {ok1}/{tot}")
print(f"independent lanes (coprime ring periods): {indep}; rebuilt from the two parent rings alone: {ok2}/{indep}")
print(f"reader ring has odd period: {oddA}/{indep}; reader ring contains its mirror: {mirA}/{indep}")
print(f"balanced lanes decided by the two parent rings alone: {bal_i} of {bal}")
 
# ---------------------------------------------------------------- H2. the measured route, for the record
import cmath
from math import lcm
def factor_odd(n):
    f, p = {}, 3
    while p * p <= n:
        while n % p == 0: f[p] = f.get(p, 0) + 1; n //= p
        p += 2
    if n > 1: f[n] = f.get(n, 0) + 1
    return f
def primroot(q, e):
    m = q ** e; ph = m // q * (q - 1); fs, x = set(), ph
    for p in range(2, int(x ** .5) + 2):
        while x % p == 0: fs.add(p); x //= p
    if x > 1: fs.add(x)
    return next(g for g in range(2, m) if gcd(g, m) == 1 and all(pow(g, ph // p, m) != 1 for p in fs))
def characters(o):
    info = []
    for q, e in factor_odd(o).items():
        m = q ** e; ph = m // q * (q - 1); g = primroot(q, e); dl, x = {}, 1
        for i in range(ph): dl[x] = i; x = x * g % m
        info.append((q, m, ph, dl))
    L = 1
    for _, _, ph, _ in info: L = lcm(L, ph)
    def num(av, x, skip=None):
        return sum(a * dl[x % m] * (L // ph) for (q, m, ph, dl), a in zip(info, av) if q != skip) % L
    cs = [av for av in product(*[range(ph) for _, _, ph, _ in info]) if num(av, 16) == 0 and num(av, o - 1) == L // 2]
    return info, L, num, cs
ek = worst = 0; orbitwise = 0; nbal = 0
for k in range(0, 2001):
    for j, a in ((1, 1), (4, 4), (5, 1), (6, 8)):
        d = 8 * k + j; o = d
        while o % 2 == 0: o //= 2
        if o <= 1: continue
        h = ordm(o); H = orbit(1, o)
        if h % 2 or (o - 1) in H: continue
        info, L, num, cs = characters(o)
        killed = all(any(av_q % ph == 0 and num(av, q, skip=q) == 0 for (q, m, ph, dl), av_q in zip(info, av)) for av in cs)
        ek += killed
        cos = orbit(a % o, o); mu = F(sum(cos), len(cos) * o)
        units = [y for y in range(1, o) if gcd(y, o) == 1]; phi = len(units); ainv = pow(a % o, -1, o)
        def term(av):
            zz = lambda x: cmath.exp(2j * cmath.pi * num(av, x) / L)
            return zz(ainv) * sum(zz(y) * y for y in units) / o
        T = {av: term(av) for av in cs}
        worst = max(worst, abs(sum(T.values()) / phi - float(mu - F(1, 2))))
        if mu == F(1, 2):
            nbal += 1; seen, contrib = set(), []
            for av in cs:
                if av in seen: continue
                g_ = L // gcd(L, gcd(*[x * (L // ph) for (q, m, ph, dl), x in zip(info, av)] + [L]))
                orb = {tuple(x * u % ph for (q, m, ph, dl), x in zip(info, av)) for u in range(1, g_ + 1) if gcd(u, g_) == 1}
                seen |= orb; contrib.append(round((sum(T[w] for w in orb)).real))
            orbitwise += all(c == 0 for c in contrib)
            if d in (476, 493, 582): print(f"d = {d}: Galois-orbit contributions x phi(o) = {contrib}")
print(f"Nest Thm 10 character sum vs direct lean, all 804 partial lanes: max error {worst:.1e}")
print(f"lanes in which every surviving character has a vanishing Euler factor: {ek} of 804")
print(f"balanced lanes in which every Galois orbit vanishes on its own: {orbitwise} of {nbal}")
