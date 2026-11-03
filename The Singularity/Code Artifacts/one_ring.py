# One ring: the angle's binary expansion is the location in every ring at once.
# Then: where the across read's forbidden branches live, and what the twist does to them.
import io, random
from fractions import Fraction as F
OUT = io.StringIO()
def say(*a):
    s = " ".join(str(x) for x in a); print(s); OUT.write(s + "\n")

def partner(x):
    r = x[::-1]
    return r if r != x else "".join("1" if c == "0" else "0" for c in x)
def grow(L, twist=True):
    seen, pairs = set(), []
    for w in range(1 << L):
        x = format(w, f"0{L}b")
        if x in seen: continue
        p = partner(x); seen |= {x, p}; pairs.append((x, p))
    seq = []
    for i, (a, b) in enumerate(pairs):
        if twist and i == len(pairs) - 1 and len(pairs) > 1: a, b = b, a
        m = len(seq) // 2
        seq = seq[:m] + [a, b] + seq[m:]
    return seq

say("== 1  The across read factors through the angle's binary address ==")
TOP = 12
R = {L: grow(L) for L in range(1, TOP + 1)}
rng = random.Random(5); ok = True
for _ in range(20000):
    u = F(rng.randrange(1 << 40), 1 << 40)
    for L in range(1, TOP + 1):
        S = L << L; bits = "".join(R[L])
        by_slice = bits[int(u * S)]
        i = int(u * (1 << L))                       # the first L bits of u: which word
        t = int(L * (u * (1 << L) - i))             # the rest of u, scaled by L: which slice inside it
        ok &= by_slice == R[L][i][t]
say(f"  20,000 angles x rings 1..{TOP}: bit = ring_L[first L bits of u][floor(L * rest of u)]  ->  {ok}")
say("  Every ring reads the same address. Ring L takes its first L bits as the word's location and the")
say("  remainder as the location inside the word. One angle is a location in all rings at once.")

say("\n== 2  The centre seam: what every ring reads just past u = 1/2 ==")
for L in range(1, 13):
    form = "1" * (L // 2 - 1) + "0" + "1" * ((L + 1) // 2)
    say(f"  LEN {L:2d}: word at the centre (index 2^(L-1)) = {R[L][1 << (L-1)]:12s}" + (f"  = 1^(floor(L/2)-1) 0 1^(ceil(L/2)): {R[L][1 << (L-1)] == form}" if L >= 4 else ""))
say("  For L >= 4 the twist puts the largest representative at the centre: one 0, just left of the middle.")

def propagate(rings):
    live = {"": [(F(0), F(1))]}; forb = []; hist = []
    for depth, bits in enumerate(rings, 1):
        S = len(bits); nxt = {}
        for p, ivs in live.items():
            seen = set()
            for a, b in ivs:
                j0 = (a.numerator * S) // a.denominator
                j1 = -((-b.numerator * S) // b.denominator)
                for j in range(j0, min(j1, S)):
                    lo, hi = max(a, F(j, S)), min(b, F(j + 1, S))
                    if lo < hi:
                        seen.add(bits[j]); nxt.setdefault(p + bits[j], []).append((lo, hi))
            for v in "01":
                if v not in seen: forb.append((p + v, ivs))
        merged = {}
        for p, iv in nxt.items():
            iv.sort(); out = [list(iv[0])]
            for a, b in iv[1:]:
                if a <= out[-1][1]: out[-1][1] = max(out[-1][1], b)
                else: out.append([a, b])
            merged[p] = [tuple(x) for x in out]
        live = merged; hist.append(len(live))
    return live, forb, hist

say("\n== 3  The first forbidden branch, read as a location ==")
rings = ["".join(R[L]) for L in range(1, TOP + 1)]
live, forb, hist = propagate(rings)
say(f"  reachable prefixes by depth: {hist}")
p, ivs = forb[0]
say(f"  first forbidden: {p}; its parent sits at {[(str(a), str(b)) for a, b in ivs]}, just past the centre seam u = 1/2")
say("  there rings 1-5 read their centre words 1, 01, 011, 1011, 10111; the parent reaches offsets 2-4 of 10111,")
say("  all 1s, so the fifth bit cannot be 0. The branch dies inside the run the twist placed at the centre.")

say("\n== 4  Every forbidden branch is a location set inside one run of the next ring ==")
def run_contains(ivs, bits):
    S = len(bits); vals = set()
    for a, b in ivs:
        j0 = (a.numerator * S) // a.denominator; j1 = -((-b.numerator * S) // b.denominator)
        vals |= {bits[j] for j in range(j0, min(j1, S)) if max(a, F(j, S)) < min(b, F(j + 1, S))}
    return len(vals) == 1
ok = all(run_contains(ivs, rings[len(p) - 1]) for p, ivs in forb)
say(f"  {len(forb)} forbidden branches through depth {TOP}: each parent location lies wholly in slices of one bit: {ok}")
near = lambda ivs, c, w: all(abs(a - c) <= w and abs(b - c) <= w for a, b in ivs)
cen = sum(1 for p, ivs in forb if near(ivs, F(1, 2), F(1, 16)))
quart = sum(1 for p, ivs in forb if any(near(ivs, F(k, 4), F(1, 32)) for k in (1, 3)))
say(f"  parents within 1/16 of the centre seam: {cen};  within 1/32 of the quarter seams: {quart};  elsewhere: {len(forb)-cen-quart}")

say("\n== 5  What the twist does to the across language ==")
rings_u = ["".join(grow(L, twist=False)) for L in range(1, TOP + 1)]
live_u, forb_u, hist_u = propagate(rings_u)
say(f"  with twist:    reachable {hist}")
say(f"  without twist: reachable {hist_u}")
ft = {p for p, _ in forb}; fu = {p for p, _ in forb_u}
say(f"  forbidden through depth {TOP}: with {len(ft)}, without {len(fu)}, shared {len(ft & fu)}; 10000 forbidden without twist: {'10000' in fu}")
say(f"  without the twist the centre holds {grow(5, False)[16]} at LEN 5 instead of {R[5][16]}")
open("one_ring_output.txt", "w").write(OUT.getvalue())
