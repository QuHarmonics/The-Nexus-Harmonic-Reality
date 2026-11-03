"""The compiler as a difference engine. Python standard library only; exact integer/GF(2) arithmetic.
Seal 1ddc66b8... written before this file was first run. Blocks K1-K8 follow the seal's numbering."""
from math import comb, log2
from itertools import permutations
from collections import Counter
import random

def popcount(x): return bin(x).count('1')

# ------------------------------------------------------------------ the engine
def fuse_stack(values, keep_frames=False):
    """First-run stack. A value arrives as a block of LEN 1. Equal-LEN neighbours fuse (A,B) -> (A, A xor B)."""
    stack, frames = [], []
    for v in values:
        stack.append([v])
        while len(stack) > 1 and len(stack[-1]) == len(stack[-2]):
            B = stack.pop(); A = stack.pop()
            stack.append(A + [a ^ b for a, b in zip(A, B)])
        if keep_frames: frames.append([list(b) for b in stack])
    return (stack, frames) if keep_frames else stack

def diff_table_def(f, n):
    """a_S = xor over T subset S of f(T): the nested differences at the origin."""
    out = []
    for S in range(1 << n):
        a, T = 0, S
        while True:
            a ^= f[T]
            if T == 0: break
            T = (T - 1) & S
        out.append(a)
    return out

def D(f, a): return [f[x ^ a] ^ f[x] for x in range(len(f))]
def degree(f):
    n = len(f).bit_length() - 1
    a = fuse_stack(f)[0] if len(f) > 1 else f
    return max((popcount(S) for S in range(len(f)) if a[S]), default=-1)

print("== K1. The first-run stack with the mixer fuse is the difference engine ==")
ok_all = 0; tot = 0
for n in range(1, 5):
    for code in range(1 << (1 << n)):
        f = [(code >> x) & 1 for x in range(1 << n)]
        st = fuse_stack(f)
        a = st[0]
        ok = len(st) == 1 and a == diff_table_def(f, n) and fuse_stack(a)[0] == f
        ok_all += ok; tot += 1
print(f"every function on n = 1..4 bits ({tot} functions): stack = nested-difference table, and the stack is its own inverse: {ok_all}/{tot}")
random.seed(17)
good = 0
for n in range(5, 13):
    f = [random.getrandbits(1) for _ in range(1 << n)]
    a = fuse_stack(f)[0]
    S_list = random.sample(range(1 << n), min(40, 1 << n))
    nested = True
    for S in S_list:
        g = f
        for i in range(n):
            if S >> i & 1: g = D(g, 1 << i)
        nested &= g[0] == a[S]
    good += nested and fuse_stack(a)[0] == f
print(f"random f, n = 5..12: a_S = (prod_(i in S) D_i f)(0) on 40 sampled S each, and involution: {good}/8")
n = 8; f = [random.getrandbits(1) for _ in range(1 << n)]; a = fuse_stack(f)[0]
_, frames = fuse_stack(f, keep_frames=True)
fold_ok = fold_tot = 0
for N in range(1, 1 << n):
    pos = 0
    for blk in frames[N - 1]:
        j = len(blk).bit_length() - 1; h = pos >> j
        for T in range(len(blk)):
            want = 0; U = h
            while True:
                want ^= a[T | (U << j)]
                if U == 0: break
                U = (U - 1) & h
            fold_ok += blk[T] == want; fold_tot += 1
        pos += len(blk)
print(f"every partial stack, n = 8: block at context h holds b_T(h) = xor_(U subset h) a_(T u U): {fold_ok}/{fold_tot}")

print("\n== K2. Difference depth is bounded by LEN ==")
for n in range(1, 5):
    dist = Counter(degree([(c >> x) & 1 for x in range(1 << n)]) for c in range(1 << (1 << n)))
    cum, ok = 0, True
    for d in range(-1, n + 1):
        cum += dist.get(d, 0)
        if d >= 0: ok &= cum == 2 ** sum(comb(n, i) for i in range(d + 1))
    print(f"n = {n}: functions by depth {dict(sorted(dist.items()))}; cumulative = 2^(sum C(n,i)): {ok}")
dd_ok = 0
for _ in range(300):
    n = random.randint(2, 9); f = [random.getrandbits(1) for _ in range(1 << n)]
    a_dir = random.randrange(1, 1 << n); g = D(f, a_dir)
    z = f
    for _ in range(n + 1): z = D(z, random.randrange(1, 1 << n))
    dd_ok += (degree(g) <= degree(f) - 1 or degree(f) <= 0) and not any(z)
print(f"300 random (f, a): deg D_a f <= deg f - 1 and an (n+1)-fold difference vanishes: {dd_ok}/300")

print("\n== K3. A write at latitude j reaches 2^(n-j) cells of the other side ==")
n = 6; ok = True
f0 = [random.getrandbits(1) for _ in range(1 << n)]; a0 = fuse_stack(f0)[0]
for y in range(1 << n):
    f1 = list(f0); f1[y] ^= 1; a1 = fuse_stack(f1)[0]
    ok &= sum(p != q for p, q in zip(a0, a1)) == 2 ** (n - popcount(y))
    a2 = list(a0); a2[y] ^= 1; f2 = fuse_stack(a2)[0]
    ok &= sum(p != q for p, q in zip(f0, f2)) == 2 ** (n - popcount(y))
print(f"n = 6, all 64 cells, value side and difference side: exact {ok}")
print("reach by latitude j = 0..6:", [2 ** (6 - j) for j in range(7)])

print("\n== K4. Leak: entropy of the output difference ==")
def entropy(c):
    t = sum(c.values()); return -sum(v / t * log2(v / t) for v in c.values())
def leak(F, n):
    return sum(entropy(Counter(F[x ^ a] ^ F[x] for x in range(1 << n))) for a in range(1, 1 << n)) / ((1 << n) - 1)
def is_affine(F, n, m):
    return all(degree([(F[x] >> b) & 1 for x in range(1 << n)]) <= 1 for b in range(m))
for n, m in [(2, 1), (3, 1), (4, 1), (2, 2)]:
    allmaps = range(1 << (m << n)) if m * (1 << n) <= 16 else []
    ok = cnt = 0
    for code in allmaps:
        F = [(code >> (m * x)) & ((1 << m) - 1) for x in range(1 << n)]
        ok += (leak(F, n) < 1e-12) == is_affine(F, n, m); cnt += 1
    print(f"all maps {n}->{m} ({cnt}): leak = 0 exactly when affine: {ok}/{cnt}")
def gf8_mul(a, b):
    r = 0
    for i in range(3):
        if b >> i & 1: r ^= a << i
    for i in (4, 3):
        if r >> i & 1: r ^= 0b1011 << (i - 3)
    return r
named = {
    "pass / mixer (a, a^b)": ([x ^ ((x & 1) << 1) for x in range(4)], 2),
    "AND merge (a&b)": ([(x & 1) & (x >> 1) for x in range(4)], 2),
    "half adder (a^b, a&b)": ([((x & 1) ^ (x >> 1)) | (((x & 1) & (x >> 1)) << 1) for x in range(4)], 2),
    "Toffoli (a, b, c ^ ab)": ([x ^ ((x & 1) & (x >> 1 & 1)) << 2 for x in range(8)], 3),
    "x^3 in GF(8)": ([gf8_mul(gf8_mul(x, x), x) for x in range(8)], 3),
}
for name, (F, n) in named.items():
    ddt = max(Counter(F[x ^ a] ^ F[x] for x in range(1 << n)).most_common(1)[0][1] for a in range(1, 1 << n))
    print(f"{name:<24} degree {max(degree([(F[x] >> b) & 1 for x in range(1 << n)]) for b in range(3))}  leak {leak(F, n):.4f} bits  "
          f"(max possible {n - 1})  largest DDT entry {ddt}")

print("\n== K5. Permutations cannot use the top latitude ==")
for n in (2, 3):
    dist = Counter()
    for P in permutations(range(1 << n)):
        dist[max(degree([(P[x] >> b) & 1 for x in range(1 << n)]) for b in range(n))] += 1
    print(f"n = {n}: permutations by degree {dict(sorted(dist.items()))}")
dist = Counter()
for _ in range(20000):
    P = list(range(16)); random.shuffle(P)
    dist[max(degree([(P[x] >> b) & 1 for x in range(16)]) for b in range(4))] += 1
print(f"n = 4, 20000 random permutations, by degree: {dict(sorted(dist.items()))}")

print("\n== K6. A saturated ring must carry the full-width merge ==")
def necklaces(n):
    s = 0
    for d in range(1, n + 1):
        if n % d == 0:
            phi = sum(1 for k in range(1, d + 1) if __import__('math').gcd(k, d) == 1)
            s += phi * 2 ** (n // d)
    return s // n
print("Z(n) parity, n = 1..64: odd at n =", [n for n in range(1, 65) if necklaces(n) % 2], "; even everywhere else")
def cycles(g, n):
    N, mask = 1 << n, (1 << (n - 1)) - 1
    seen = bytearray(N); c = 0
    for s in range(N):
        if seen[s]: continue
        c += 1
        while not seen[s]:
            seen[s] = 1
            s = ((s << 1) & (N - 1)) | ((s >> (n - 1)) ^ g[s & mask])
    return c
for n in range(2, 6):
    Z = necklaces(n); par_ok = 0; rings = []; total = 1 << (1 << (n - 1))
    for code in range(total):
        g = [(code >> r) & 1 for r in range(1 << (n - 1))]
        c = cycles(g, n)
        par_ok += c % 2 == (Z + sum(g)) % 2
        if c == 1: rings.append(g)
    full = sum(1 for g in rings if fuse_stack(g)[0][-1] == 1)
    print(f"n = {n}: cycles = Z(n) + wt(g) mod 2 for {par_ok}/{total} feedbacks; single-cycle feedbacks {len(rings)} "
          f"(2^(2^(n-1)-n) = {2 ** (2 ** (n - 1) - n)}); carrying the full monomial x2..x{n}: {full}/{len(rings)}")
samp_ok = 0
for _ in range(2000):
    n = random.randint(6, 12); g = [random.getrandbits(1) for _ in range(1 << (n - 1))]
    samp_ok += cycles(g, n) % 2 == (necklaces(n) + sum(g)) % 2
print(f"2000 random feedbacks, n = 6..12: parity law holds {samp_ok}/2000")
print("sign of the state map = (-1)^(cycles) = (-1)^(Z(n) + top coefficient of g): follows, since 2^n is even")

print("\n== K7. A prime-base digit holds p-1 nested differences ==")
for p in (2, 3, 5, 7):
    ok = True
    for _ in range(200):
        f = [random.randrange(p) for _ in range(p)]
        g = f
        for _ in range(p): g = [(g[(x + 1) % p] - g[x]) % p for x in range(p)]
        ok &= not any(g)
    h = [pow(x, p - 1, p) for x in range(p)]
    for _ in range(p - 1): h = [(h[(x + 1) % p] - h[x]) % p for x in range(p)]
    print(f"p = {p}: Delta^p vanishes on 200 random digit functions: {ok}; Delta^(p-1) x^(p-1) = {h[0]} (nonzero: {h[0] != 0})")

print("\n== K8. One level up the engine is linear ==")
maps22 = [[(code >> (2 * x)) & 3 for x in range(4)] for code in range(256)]
def table_bits(G): return [(G[x] >> b) & 1 for x in range(4) for b in range(2)]
okG = okF = 0
for F in maps22:
    degF = max(degree([(F[x] >> b) & 1 for x in range(4)]) for b in range(2))
    outs = [[0] * 256 for _ in range(8)]
    for gi, G in enumerate(maps22):
        FG = table_bits([F[G[x]] for x in range(4)])
        for k in range(8): outs[k][gi] = FG[k]
    okG += max(degree(o) for o in outs) == degF   # zero map: both sides -1
for G in maps22:
    outs = [[0] * 256 for _ in range(8)]
    for fi, F in enumerate(maps22):
        FG = table_bits([F[G[x]] for x in range(4)])
        for k in range(8): outs[k][fi] = FG[k]
    okF += max(degree(o) for o in outs) <= 1
print(f"G -> F o G has degree deg F in G's 8 table bits: {okG}/256;  F -> F o G has degree <= 1 in F's table bits: {okF}/256")
lin = all(D([x ^ y for x, y in zip(f, g)], a) == [p ^ q for p, q in zip(D(f, a), D(g, a))]
          for f, g, a in [([random.getrandbits(1) for _ in range(64)], [random.getrandbits(1) for _ in range(64)], random.randrange(1, 64)) for _ in range(200)])
print(f"D_a(f xor g) = D_a f xor D_a g on 200 random pairs: {lin}")
