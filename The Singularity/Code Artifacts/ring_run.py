"""Nested-ring runner. Rings of LEN 1,2,4,...,64. Ring L = every L-bit word in counting order around a circle,
L slices per word, L*2^L slices total. An entry is just a position on the outer ring. The fall is geometry only:
same angle, next ring in. Each ring is read as a CIRCLE: a window of L slices from any offset, so unaligned reads count.
The route is never given; we only watch it."""
import random, sys
from collections import Counter

def size(L): return L * (1 << L)
def bit(L, o):
    w, k = divmod(o % size(L), L)
    return (w >> (L - 1 - k)) & 1
def window(L, o):                       # L slices read clockwise from slice o (wraps the circle)
    v = 0
    for i in range(L): v = (v << 1) | bit(L, o + i)
    return v
def fall(L, o):                         # same angle, next ring in
    L2 = L // 2
    return (o * size(L2)) // size(L)
def trace(L, o):
    path = []
    while True:
        path.append((L, o, window(L, o)))
        if L == 1: return path
        o, L = fall(L, o), L // 2

def all_at_once(L):
    seen = {}; fan = {}; codes = Counter(); top = Counter()
    for o in range(size(L)):
        p = trace(L, o); codes[tuple(x[2] for x in p)] += 1; top[p[0][2]] += 1
        for (a, oa, _), (b, ob, _) in zip(p, p[1:]):
            seen.setdefault(a, set()).add(oa); seen.setdefault(b, set()).add(ob)
            fan.setdefault(a, Counter())[ob] += 1
    return seen, fan, codes, top

if __name__ == "__main__":
    for L in (8, 16):
        seen, fan, codes, top = all_at_once(L)
        print(f"== all {size(L)} entries on ring {L} at once")
        print(" positions reached per ring:", {k: len(v) for k, v in sorted(seen.items(), reverse=True)})
        print(" fan-in per ring (entries per next-ring slice):", {k: sorted(set(v.values())) for k, v in sorted(fan.items(), reverse=True)})
        print(f" distinct emitted codes: {len(codes)}   opcode (window) hits: min {min(top.values())} max {max(top.values())} over {len(top)} values")
    L = 8; n = 1 << L; mask = n - 1
    print("\n== circular read = rotate, with a carry exception (ring 8)")
    for k in range(1, L):
        same = tot = 0
        for w in range(n):
            win = window(L, w * L + k)
            rol = ((w << k) & mask) | (w >> (L - k))
            head = ((w + 1) & mask) >> (L - k)
            assert win == (((w << k) & mask) | head)         # exact rule
            same += (win == rol); tot += 1
        print(f" phase {k}: window == ROL_k(word) in {same}/{tot};  differs only when the low {L-k} bits are all 1 (carry)")
    print("\n== 64-bit ring: entries are ignorant of the route; watch three")
    random.seed(11)
    for _ in range(3):
        o = random.getrandbits(70) % size(64)
        print(" entry slice", o)
        for (l, off, w) in trace(64, o): print(f"   ring {l:2d} offset {off:>22d}  reads {w:0{l}b}" if l <= 8 else f"   ring {l:2d} offset {off:>22d}  reads {w:#0{l//4+2}x}")
