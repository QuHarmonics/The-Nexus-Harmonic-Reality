# Are the pairs, and their cancellation, forced by the transformation, or added?
# Held: the orbit's own group, and the nested ring's own construction (notebook grow/partner, verbatim).
import io
OUT = io.StringIO()
def say(*a):
    s = " ".join(str(x) for x in a); print(s); OUT.write(s + "\n")

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

say("== A  the nested ring: every word once, and the ring is its own partner read backwards ==")
for L in range(1, 17):
    r = grow(L); N = len(r)
    once = len(set(r)) == N == 2 ** L
    mirror = all(partner(r[i]) == r[N - 1 - i] for i in range(N))
    if L <= 4 or L in (8, 12, 16): say(f"  LEN {L:2d}: {N:6d} words, each once: {once}, partner(ring[i]) == ring[N-1-i]: {mirror}")
say(f"  ring 2 = {''.join(grow(2))}  (the 2-bit circle as drawn)")

rot = lambda x, k, n: ((x << k) | (x >> (n - k))) & ((1 << n) - 1)
rev = lambda x, n: int(format(x, f"0{n}b")[::-1], 2)

say("\n== B  the pairing is the orbit's own: a cyclic orbit of even length has exactly one involution ==")
for n in (4, 6, 8, 10, 12, 16):
    inv = [k for k in range(1, n) if (2 * k) % n == 0]
    say(f"  rotations of {n:2d} bits: elements of order 2 = {inv}  -> the half-turn R^{n//2} only")

say("\n== C  the pair readout x XOR Hx: cancels what the pair shares, lands one layer down ==")
for name, H, ns in (("half-turn", lambda x, n: rot(x, n // 2, n), (4, 6, 8, 10, 12)),
                    ("mirror   ", lambda x, n: rev(x, n), (4, 6, 8, 10, 12))):
    for n in ns:
        N = 1 << n
        fix = {x for x in range(N) if H(x, n) == x}
        P = [x ^ H(x, n) for x in range(N)]
        in_fix = all(P[x] in fix for x in range(N))
        same = all(P[x] == P[H(x, n)] for x in range(N))
        ker = {x for x in range(N) if P[x] == 0} == fix
        img = len(set(P))
        say(f"  {name} n={n:2d}: residual always in Fix(H) {in_fix}; both members give one residual {same}; "
            f"what cancels completely = Fix(H) {ker}; |Fix| {len(fix):4d}, |image| {img:4d}")
say("  half-turn: Fix = {uu}, the whole layer below; residual of x = uv is (u^v)(u^v)")

say("\n== D  the 8-bit orbit of 1B, three readouts ==")
orb = [rot(0x1B, k, 8) for k in range(8)]
say("  orbit:", " ".join(f"{x:02X}" for x in orb))
allx = 0
for x in orb: allx ^= x
say(f"  whole orbit read at once (XOR of all 8):            {allx:02X}   -> everything cancels, nothing left")
say("  pairs (x, half-turn x):                            " + "  ".join(f"({x:02X},{rot(x,4,8):02X})->{x ^ rot(x,4,8):02X}" for x in orb[:4]))
say("  residual orbit: AA <-> 55, period 2: the bare flip, one layer down (1010 / 0101)")
w = (0x1B >> 4) ^ (0x1B & 0xF)
w2 = (w >> 2) ^ (w & 3)
say(f"  fold again: 1B -> {w:04b} -> {w2:02b}   (1010 is half-turn fixed at 4 bits, so it cancels completely next)")

say("\n== E  folded all the way down, the pair readout is the difference engine ==")
def fold_down(f, n):                       # (u, v) -> (u, u ^ v) at every scale: the first-run mixer
    a = f; h = 1
    while h < n:
        for i in range(0, n, 2 * h):
            for j in range(i, i + h):
                a = a ^ (((a >> (n - 1 - j)) & 1) << (n - 1 - (j + h)))
        h *= 2
    return a
def anf(f, n):                             # algebraic normal form by subset XOR, computed directly
    bits = [(f >> (n - 1 - i)) & 1 for i in range(n)]
    out = 0
    for S in range(n):
        c = 0
        for T in range(n):
            if T & S == T: c ^= bits[T]
        out |= c << (n - 1 - S)
    return out
for n in (4, 8, 16):
    ok = all(fold_down(f, n) == anf(f, n) for f in range(1 << n)) if n <= 8 else \
         all(fold_down(f, n) == anf(f, n) for f in range(0, 1 << n, 37))
    say(f"  n={n:2d}: pair-difference folded to the bottom == Mobius/ANF transform: {ok}")
say("  read upward, every layer is (u, u^v): a copy and a difference. That is the whole build, from 2 bits.")

say("\n== F  on the nested ring, the pair residual is a mirror word; palindrome pairs give all ones ==")
for L in (4, 6, 8, 10):
    r = grow(L); N = len(r); ok = pal = True
    for i in range(N // 2):
        x, y = int(r[i], 2), int(r[N - 1 - i], 2); res = format(x ^ y, f"0{L}b")
        ok &= res == res[::-1]
        if r[i] == r[i][::-1]: pal &= res == "1" * L
    say(f"  LEN {L:2d}: every pair residual is a palindrome {ok}; palindrome pairs give {'1'*L}: {pal}")
open("pairs_forced_output.txt", "w").write(OUT.getvalue())
