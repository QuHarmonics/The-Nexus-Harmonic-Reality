"""
Sphere engine v0 — standard library only.

A field of N cells (the LED bar). A hex stream drives a transformation of the field
(a permutation: every cell goes somewhere, no two land in the same place).
Readers sit at every depth: a reader at depth m cuts the bar into m equal segments
and sees only the segment-to-segment crossing table.

For each depth the engine reports what the reader sees, what stays hidden,
whether it can tell the transformation from its inverse (direction),
and how many closed loops it can prove exist.
Claims are assertions: if one is wrong, the script stops.
"""
import hashlib
from math import lgamma, log, log2, pi, e

N = 128                      # cells on the bar (power of two so every depth splits evenly)
LN2 = log(2)


# ---------------------------------------------------------------- hex sources
def sha_stream(seed: bytes, n_hex: int) -> str:
    """SHA-256 chained on itself: h0 = sha(seed), h1 = sha(h0), ..."""
    out, h = [], hashlib.sha256(seed).digest()
    while len(out) * 64 < n_hex:
        out.append(h.hex())
        h = hashlib.sha256(h).digest()
    return "".join(out)[:n_hex]


def pi_hex(n_hex: int) -> str:
    """Hex digits of pi after the point, by Machin's formula in exact integer arithmetic."""
    bits = 4 * (n_hex + 16)
    one = 1 << bits

    def arctan_inv(x):
        total = term = one // x
        x2, k, sign = x * x, 1, -1
        while term:
            term //= x2
            total += sign * (term // (2 * k + 1))
            sign, k = -sign, k + 1
        return total

    p = 16 * arctan_inv(5) - 4 * arctan_inv(239)          # pi * 2^bits
    frac = p - (3 << bits)
    return format(frac >> (4 * 16), "x").zfill(n_hex)[:n_hex]


# ---------------------------------------------------------------- hex -> transformation
def permutation_from_hex(hexstr: str, n: int):
    """Fisher-Yates shuffle driven by the hex stream, one byte per draw, with rejection (no bias)."""
    p = list(range(n))
    stream = bytes.fromhex(hexstr[: len(hexstr) // 2 * 2])
    pos = 0
    for i in range(n - 1, 0, -1):
        mask = (1 << i.bit_length()) - 1
        while True:
            assert pos < len(stream), "hex stream too short to drive the whole bar"
            r = stream[pos] & mask
            pos += 1
            if r <= i:
                break
        p[i], p[r] = p[r], p[i]
    return tuple(p)


# ---------------------------------------------------------------- readers
def log2_fact(k):
    return lgamma(k + 1) / LN2


def read_at_depth(perm, m):
    """Reader with m equal contiguous segments: returns its crossing table."""
    n = len(perm); size = n // m
    T = [[0] * m for _ in range(m)]
    for x, y in enumerate(perm):
        T[x // size][y // size] += 1
    return T


def hidden_bits(T):
    """log2 of how many transformations give this same table (Fisher-Yates double-coset size)."""
    d = [sum(r) for r in T]
    return 2 * sum(log2_fact(x) for x in d) - sum(log2_fact(v) for r in T for v in r)


def components(T):
    m = len(T); parent = list(range(m))
    def f(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]; x = parent[x]
        return x
    for i in range(m):
        for j in range(m):
            if T[i][j]:
                parent[f(i)] = f(j)
    return len({f(i) for i in range(m)})


def cycles(perm):
    seen, c = [False] * len(perm), 0
    for s in range(len(perm)):
        if not seen[s]:
            c += 1; x = s
            while not seen[x]:
                seen[x] = True; x = perm[x]
    return c


def inverse(perm):
    q = [0] * len(perm)
    for i, v in enumerate(perm):
        q[v] = i
    return tuple(q)


# ---------------------------------------------------------------- the radial profile
def profile(name, perm):
    total = log2_fact(N)
    depths = [2 ** k for k in range(N.bit_length()) if 2 ** k <= N]
    inv = inverse(perm)
    print(f"\n{name}: {cycles(perm)} closed loops on the bar")
    print(f"{'depth m':>7} {'cuts':>5} {'seen bits':>10} {'hidden bits':>12} {'direction?':>11} {'loops proven >=':>16}")
    prev_seen = -1.0
    for m in depths:
        T = read_at_depth(perm, m)
        hid = hidden_bits(T)
        seen = total - hid
        sym = all(T[i][j] == T[j][i] for i in range(m) for j in range(m))
        direction = read_at_depth(inv, m) != T               # can this reader tell perm from its inverse?
        comp = components(T)

        # ---- claims (the code stops if any is false)
        assert seen >= prev_seen - 1e-9, "a finer reader must never see less"
        assert cycles(perm) >= comp, "a reader can only prove loops that exist"
        if m == 1:
            assert abs(seen) < 1e-9, "the undivided field sees nothing"
        if m == 2:
            assert sym and not direction, "the first reader must be blind to direction"
        if m == N:
            assert abs(hid) < 1e-9, "the full-resolution reader sees everything"
        prev_seen = seen

        print(f"{m:>7} {log2(m):>5.0f} {seen:>10.2f} {hid:>12.2f} {('yes' if direction else 'no'):>11} {comp:>16}")
    print(f"  radius of the bar: {log2(N):.0f} cuts to locate a cell, {total:.1f} bits to know the whole transformation")


def first_reader_check(samples=2000):
    """Across many hash-driven transformations, the first reader's average view must match the
    exact hypergeometric entropy of the crossing count, about 0.5*log2(pi*e*N/8) bits."""
    d = N // 2
    lc = lambda a, b: lgamma(a + 1) - lgamma(b + 1) - lgamma(a - b + 1)
    exact = 0.0
    for k in range(d + 1):
        lp = lc(d, k) + lc(N - d, d - k) - lc(N, d)
        exact -= (2.718281828459045 ** lp) * lp / LN2
    total = log2_fact(N)
    mean_seen = sum(total - hidden_bits(read_at_depth(permutation_from_hex(sha_stream(str(s).encode(), 1200), N), 2))
                    for s in range(samples)) / samples
    print(f"\nfirst reader over {samples} hash-driven transformations: average seen {mean_seen:.3f} bits | "
          f"exact {exact:.3f} | approximation 0.5*log2(pi*e*N/8) = {0.5 * log2(pi * e * N / 8):.3f}")
    assert abs(mean_seen - exact) < 0.1, "the first reader does not see scale the way the theory says"


if __name__ == "__main__":
    profile("SHA-256 of empty input, chained", permutation_from_hex(sha_stream(b"", 1200), N))
    profile("hex digits of pi", permutation_from_hex(pi_hex(1200), N))
    first_reader_check()
    print("\nall claims held")
