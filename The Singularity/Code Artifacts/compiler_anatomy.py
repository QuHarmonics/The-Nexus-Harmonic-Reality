# The compiler, taken apart: grow(L) / partner(x) from nested_rings.ipynb.
# Held end first: every word once, placed by its pair. Each block derives a property, then runs it.
import io, math, random
from fractions import Fraction
from functools import reduce
OUT = io.StringIO()
def say(*a):
    s = " ".join(str(x) for x in a); print(s); OUT.write(s + "\n")

# ---- the notebook's construction, verbatim ----
def partner(x):
    r = x[::-1]
    return r if r != x else "".join("1" if c == "0" else "0" for c in x)
def grow(L):
    seen, pairs = set(), []
    for w in range(1 << L):
        x = format(w, f"0{L}b")
        if x in seen: continue
        p = partner(x); seen |= {x, p}; pairs.append((x, p))
    seq = []
    for i, (a, b) in enumerate(pairs):
        if i == len(pairs) - 1 and len(pairs) > 1: a, b = b, a
        m = len(seq) // 2
        seq = seq[:m] + [a, b] + seq[m:]
    return seq

# ---- integer forms ----
def rev(x, L):  return int(format(x, f"0{L}b")[::-1], 2)
def comp(x, L): return x ^ ((1 << L) - 1)
def part(x, L):
    r = rev(x, L); return r if r != x else comp(x, L)
is_rep = lambda x, L: x < part(x, L)          # the smaller member of its pair (no word is its own partner)

say("== 1  What it is: one representative per pair ascending, partners descending, centre pair swapped ==")
def closed_form(L):
    reps = [x for x in range(1 << L) if is_rep(x, L)]
    M = len(reps); left = reps[:]; right = [part(a, L) for a in reversed(reps)]
    if M > 1: left[-1], right[0] = right[0], left[-1]           # the twist at the centre seam
    return [format(v, f"0{L}b") for v in left + right]
for L in range(1, 17):
    ok = closed_form(L) == grow(L)
    if L <= 3 or L in (8, 12, 16): say(f"  LEN {L:2d}: grow(L) == closed form: {ok}")
say("  centre insertion is a stack: each new pair goes to the middle and pushes the older pairs outward,")
say("  so the oldest pair (the poles 0..0 / 1..1) ends at the outer seam and the last pair at the centre.")

say("\n== 2  The partner rule is C1 in one line: reverse; if reversing would hold still, flip ==")
for L in (4, 5, 8, 9, 12):
    N = 1 << L
    fixed = sum(1 for x in range(N) if part(x, L) == x)
    invol = all(part(part(x, L), L) == x for x in range(N))
    pal = sum(1 for x in range(N) if rev(x, L) == x)
    anti = sum(1 for x in range(N) if rev(x, L) == comp(x, L))
    say(f"  LEN {L:2d}: fixed points {fixed}; involution {invol}; palindromes {pal} = 2^ceil(L/2) {pal == 2**math.ceil(L/2)}; "
        f"anti-palindromes (reverse = flip) {anti}; pairs {N//2}")
say("  The four moves {stay, reverse, flip, reverse+flip} form one Klein group. A pair is half of a 4-orbit,")
say("  except palindromes (reverse stalls, so flip) and anti-palindromes (reverse and flip are the same move).")

say("\n== 3  The twist: it makes the two seams on the mirror axis read the same way ==")
def seams(ring, L):
    N = len(ring); M = N // 2
    a = lambda i: int(ring[i], 2)
    outer = (a(N - 1), a(0)); centre = (a(M - 1), a(M))
    kind = lambda p: "partner->rep" if is_rep(p[1], L) and part(p[1], L) == p[0] else (
                     "rep->partner" if is_rep(p[0], L) and part(p[0], L) == p[1] else "other")
    return kind(outer), kind(centre)
for L in (2, 3, 4, 6, 8, 10):
    r = grow(L)
    untw = [x for x in r]; M = len(r) // 2; untw[M - 1], untw[M] = untw[M], untw[M - 1]
    say(f"  LEN {L:2d}: with twist outer/centre = {seams(r, L)};  without = {seams(untw, L)}")
say("  Clockwise, both seams cross from a partner into its representative only when the centre pair is swapped.")
say(f"  LEN 2 without the twist is counting order {''.join(format(i,'02b') for i in range(4))} = 1B; with it, 00100111.")

say("\n== 4  Location is computable directly: route, not search ==")
def reps_below_nonpal(x, L):
    # count y < x with y < rev(y): DP over mirrored bit pairs, outside in. state = (prefix vs x, suffix vs x, y vs rev(y))
    bx = [(x >> (L - 1 - i)) & 1 for i in range(L)]
    st = {("EQ", "EQ", "U"): 1}
    for j in range(L // 2):
        r = L - 1 - j; nxt = {}
        for (pre, suf, mir), c in st.items():
            for yl in (0, 1):
                if pre == "EQ" and yl > bx[j]: continue
                npre = "LT" if (pre == "LT" or yl < bx[j]) else "EQ"
                for yr in (0, 1):
                    nsuf = suf if yr == bx[r] else ("LT" if yr < bx[r] else "GT")
                    nmir = mir if mir != "U" or yl == yr else ("LT" if yl < yr else "GT")
                    k = (npre, nsuf, nmir); nxt[k] = nxt.get(k, 0) + c
        st = nxt
    total = 0
    for (pre, suf, mir), c in st.items():
        if mir != "LT": continue
        if L % 2:
            mx = bx[L // 2]
            for ym in (0, 1):
                if pre == "LT" or (pre == "EQ" and (ym < mx or (ym == mx and suf == "LT"))): total += c
        else:
            if pre == "LT" or (pre == "EQ" and suf == "LT"): total += c
    return total
def pal_below(x, L):                     # palindromes y < x
    h = (L + 1) // 2; p = x >> (L - h)
    mk = lambda q: (q << (L - h)) | int(format(q, f"0{h}b")[:L - h][::-1] or "0", 2) if L - h else q
    return p + (1 if mk(p) < x else 0)
def reps_below(x, L):
    return reps_below_nonpal(x, L) + pal_below(min(x, 1 << (L - 1)), L)
def location(x, L):
    N = 1 << L; M = N // 2
    rep = x if is_rep(x, L) else part(x, L)
    k = reps_below(rep, L)
    if M > 1 and k == M - 1: return M if x == rep else M - 1      # the twisted centre pair
    return k if x == rep else N - 1 - k
def word_at(p, L):
    N = 1 << L; M = N // 2
    if M > 1 and p in (M - 1, M): k, want_rep = M - 1, (p == M)
    elif p < M: k, want_rep = p, True
    else: k, want_rep = N - 1 - p, False
    lo, hi = 0, (1 << L) - 1                                       # k-th representative: smallest x with reps_below(x+1) = k+1
    while lo < hi:
        mid = (lo + hi) // 2
        if reps_below(mid + 1, L) >= k + 1: hi = mid
        else: lo = mid + 1
    return lo if want_rep else part(lo, L)
for L in range(1, 15):
    r = grow(L)
    ok = all(location(int(w, 2), L) == i for i, w in enumerate(r))
    ok2 = all(word_at(i, L) == int(w, 2) for i, w in enumerate(r))
    if L <= 2 or L in (8, 12, 14): say(f"  LEN {L:2d}: location(word) correct for every word {ok}; word_at(position) correct {ok2}")
L = 16; r = grow(L); sample = random.Random(1).sample(range(1 << L), 3000)
say(f"  LEN 16: 3000 sampled words, location correct {all(location(int(r[i],2),L)==i for i in sample)}, word_at correct {all(word_at(i,L)==int(r[i],2) for i in sample)}")
L = 64
pi64 = 0x243F6A8885A308D3                                          # the first 64 fractional bits of pi
loc = location(pi64, L)
say(f"  LEN 64 (2^64 words, never built): pi's first 64 bits sit at position {loc:,} of {2**64:,}")
say(f"    and word_at({loc:,}) returns {word_at(loc, L):#018x}: round trip {word_at(loc, L) == pi64}; its partner sits at {location(part(pi64, L), L):,} = N-1-position: {location(part(pi64, L), L) == 2**64 - 1 - loc}")
say("  location costs one pass over L/2 mirrored bit pairs; word_at adds a binary search of L steps.")

say("\n== 5  The ring as a bit circle: L*2^L slices, mirror law at the slice level ==")
for L in (2, 3, 4, 6, 8):
    bits = "".join(grow(L)); S = len(bits)
    flips = sum(1 for s in range(S) if bits[s] != bits[S - 1 - s])
    pal = 2 ** math.ceil(L / 2)
    per = next(d for d in range(1, S + 1) if S % d == 0 and bits == bits[d:] + bits[:d])
    say(f"  LEN {L}: {S:5d} slices; mirrored slices that flip {flips} = palindrome slices {pal*L}: {flips == pal*L}; "
        f"rotation orbit {per} (primitive {per == S}); ones = half {bits.count('1') == S//2}")
say("  slices 2, 8, 24, 64, 160, 384, 896, 2048: the 2-bit ring is a byte, the 4-bit ring is a 64-bit word.")

say("\n== 6  How wide a reader must be to know where it is on the circle ==")
for L in range(1, 9):
    bits = "".join(grow(L)); S = len(bits); ext = bits + bits
    w = next(w for w in range(1, S + 1) if len({ext[i:i + w] for i in range(S)}) == S)
    say(f"  LEN {L}: {S:5d} slices, address floor log2 = {math.log2(S):5.2f}, shortest window that names every position: {w}")

say("\n== 7  The across read: one bit from each ring at one angle ==")
top = 10; rings = [ "".join(grow(L)) for L in range(1, top + 1) ]
cuts = sorted({Fraction(k, len(b)) for b in rings for k in range(len(b))} | {Fraction(1)})
profiles = {}
for a, b in zip(cuts[:-1], cuts[1:]):
    mid = (a + b) / 2
    prof = "".join(rg[int(mid * len(rg))] for rg in rings)
    profiles[prof] = profiles.get(prof, 0) + 1
say(f"  rings 1..{top}: {len(cuts)-1} angular cells, {len(profiles)} distinct profiles of {2**top}")
absent = [format(v, f"0{top}b") for v in range(2 ** top) if format(v, f"0{top}b") not in profiles]
seen_pref = lambda k: {p[:k] for p in profiles}
minimal = []
for k in range(1, top + 1):
    have = seen_pref(k); prev = seen_pref(k - 1) if k > 1 else {""}
    for v in range(2 ** k):
        q = format(v, f"0{k}b")
        if q not in have and q[:-1] in prev and not any(q.startswith(m) for m in minimal): minimal.append(q)
cover = sum(1 for p in absent if any(p.startswith(m) for m in minimal))
say(f"  minimal forbidden prefixes (inner ring first): {minimal}")
say(f"  they account for {cover} of the {len(absent)} absent profiles")
open("compiler_anatomy_output.txt", "w").write(OUT.getvalue())
