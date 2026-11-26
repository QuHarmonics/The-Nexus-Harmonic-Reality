"""Small reference implementation of the native core, equations 1.1–3.2.

Source: NEXUS_Domain_Core_20261103.md at df0d09f8c430bce44660e4986209afdb20395e04.
The finite exhaustive check is scoped to widths 1 and 2 for full reader states.
No claim about unknown return depths or external physical measurements.
"""
from itertools import product

def mask(n):
    if type(n) is not int or n < 1:
        raise ValueError("positive integer width required")
    return (1 << n) - 1

def word(x, n):
    if type(x) is not int or not 0 <= x <= mask(n):
        raise ValueError("out-of-width word")
    return x

def complement(x, n):
    return word(x, n) ^ mask(n)

def reverse(x, n):
    return int(f"{word(x, n):0{n}b}"[::-1], 2)

def partner(x, n):
    r = reverse(x, n)
    return complement(x, n) if r == x else r

def ring(n):
    reps = [x for x in range(mask(n) + 1) if x < partner(x, n)]
    r = reps + [partner(x, n) for x in reversed(reps)]
    if n >= 2:
        m = len(r) // 2
        r[m - 1], r[m] = r[m], r[m - 1]
    return tuple(r)

def tick(x, n):
    # MSB-first register: complement last bit, prepend, shift remaining bits.
    return (((word(x, n) & 1) ^ 1) << (n - 1)) | (x >> 1)

def untick(y, n):
    return ((word(y, n) << 1) & mask(n)) | ((y >> (n - 1)) ^ 1)

def state(p, w, d, n):
    word(p, n); word(w, n)
    d = tuple(d)
    if len(d) != mask(n) + 1:
        raise ValueError("complete field required")
    for x in d:
        word(x, n)
    return p, w, d

def step(s, n):
    p, w, d = state(*s, n)
    x = d[p] ^ w
    wp = partner(x, n)
    dp = list(d)
    dp[p] ^= wp
    return p ^ x, wp, tuple(dp)

def unstep(s, n):
    pp, wp, dp = state(*s, n)
    x = partner(wp, n)
    p = pp ^ x
    d = list(dp)
    d[p] ^= wp
    return p, x ^ d[p], tuple(d)

def audit():
    assert ring(2) == (0, 2, 1, 3), "Atlas seam order"
    counts = {"ring_words": 0, "clock_words": 0, "reader_states": 0}
    for n in range(1, 7):
        r = ring(n)
        N = 1 << n
        assert len(set(r)) == len(r) == N
        if n >= 2:
            m = N // 2
            assert r[m - 1] > r[m] and partner(r[m - 1], n) == r[m]
            reps = [x for x in range(N) if x < partner(x, n)]
            assert list(r[:m - 1]) == reps[:-1] and r[m] == reps[-1]
        for i, x in enumerate(r):
            p = partner(x, n)
            assert p != x and partner(p, n) == x and r[N - 1 - i] == p
            assert complement(complement(x,n),n) == x and reverse(reverse(x,n),n) == x
            counts["ring_words"] += 1
            assert untick(tick(x,n),n) == x and tick(untick(x,n),n) == x
            y = x
            for _ in range(n):
                y = tick(y,n)
            assert y == complement(x,n)
            for _ in range(n):
                y = tick(y,n)
            assert y == x
            counts["clock_words"] += 1
    for n in (1, 2):
        N = 1 << n
        for p, w in product(range(N), repeat=2):
            for d in product(range(N), repeat=N):
                s = (p, w, d)
                assert unstep(step(s,n),n) == s and step(unstep(s,n),n) == s
                counts["reader_states"] += 1
    return counts

if __name__ == "__main__":
    print(audit())
