#!/usr/bin/env python3
"""
Exact word-tree collision audit for the SHA-256 schedule arms.

Purpose
-------
Enumerate all reduced words of length n over:
    a  = sigma_1
    A  = sigma_1^{-1}
    b  = sigma_0
    B  = sigma_0^{-1}

There are exactly 4 * 3^(n-1) reduced words of length n.

For each word, compute its exact 32x32 GF(2) transformation and
check whether two distinct reduced words have the same shape.

The script intentionally keeps ORDER.  It does not sort generators,
quotient reversal, or use scalar coefficients.

It also checks the n=11 case explicitly:
    4 * 3^10 = 236,196 words.

Matrix representation
---------------------
A 32x32 binary matrix is stored as 32 Python integers, one integer
per output row.  Matrix composition is exact over GF(2).

The SHA sigma functions are:
    sigma0(x) = ROTR7(x) ^ ROTR18(x) ^ (x >> 3)
    sigma1(x) = ROTR17(x) ^ ROTR19(x) ^ (x >> 10)

The inverses are obtained by Gaussian elimination over GF(2), so no
inverse formula is assumed.

Output
------
For each n:
  - number of reduced words
  - number of distinct shapes
  - number of collisions
  - largest fiber size

A collision is a genuine shape collision:
    phi(w1) == phi(w2), w1 != w2

This is distinct from additive cancellation in a coefficient sum.
"""

M = 0xFFFFFFFF
N = 32

def rotr(x, n):
    return ((x >> n) | (x << (32 - n))) & M

def sigma0(x):
    return rotr(x, 7) ^ rotr(x, 18) ^ (x >> 3)

def sigma1(x):
    return rotr(x, 17) ^ rotr(x, 19) ^ (x >> 10)

def identity_matrix():
    return tuple(1 << i for i in range(N))

def matrix_from_function(f):
    # Column j is f(e_j).  Convert columns to row-bit representation.
    cols = [f(1 << j) for j in range(N)]
    rows = []
    for i in range(N):
        row = 0
        for j in range(N):
            if (cols[j] >> i) & 1:
                row |= 1 << j
        rows.append(row)
    return tuple(rows)

def mat_apply(A, x):
    y = 0
    for i, row in enumerate(A):
        if (row & x).bit_count() & 1:
            y |= 1 << i
    return y

def mat_mul(A, B):
    # A*B: apply B first, then A.
    cols_B = []
    for j in range(N):
        col = 0
        for i in range(N):
            if (B[i] >> j) & 1:
                col |= 1 << i
        cols_B.append(col)

    out = []
    for i in range(N):
        row = 0
        ar = A[i]
        for j, col in enumerate(cols_B):
            if (ar & col).bit_count() & 1:
                row |= 1 << j
        out.append(row)
    return tuple(out)

def gf2_inverse(A):
    # Augment A | I, represented as 64-bit rows.
    aug = [A[i] | (1 << (N + i)) for i in range(N)]

    for col in range(N):
        pivot = next((r for r in range(col, N)
                      if (aug[r] >> col) & 1), None)
        if pivot is None:
            raise ValueError("Matrix is singular")

        aug[col], aug[pivot] = aug[pivot], aug[col]

        for r in range(N):
            if r != col and ((aug[r] >> col) & 1):
                aug[r] ^= aug[col]

    return tuple((row >> N) & M for row in aug)

S1 = matrix_from_function(sigma1)
S0 = matrix_from_function(sigma0)
I  = identity_matrix()

S1_INV = gf2_inverse(S1)
S0_INV = gf2_inverse(S0)

# Generator labels and their matrices.
GENS = {
    "a": S1,
    "A": S1_INV,
    "b": S0,
    "B": S0_INV,
}

INV = {
    "a": "A", "A": "a",
    "b": "B", "B": "b",
}

def reduced_words(n):
    """Generate reduced words without immediate inverse backtracking."""
    if n == 0:
        yield ()
        return

    for first in GENS:
        yield from extend((first,), n)

def extend(prefix, n):
    if len(prefix) == n:
        yield prefix
        return

    last = prefix[-1]
    forbidden = INV[last]

    for g in GENS:
        if g != forbidden:
            yield from extend(prefix + (g,), n)

def audit(n):
    # Rather than materializing all words first, walk the tree and
    # accumulate the composed matrix along each path.
    #
    # Word convention:
    #   phi(g1...gn) = G_gn ... G_g2 G_g1
    # because each new generator acts on the current transformed state.
    #
    # This preserves order exactly.

    shapes = {}
    word_count = 0

    def walk(word, current):
        nonlocal word_count

        if len(word) == n:
            word_count += 1
            prior = shapes.get(current)
            if prior is None:
                shapes[current] = word
            return

        if not word:
            candidates = GENS.keys()
        else:
            candidates = (g for g in GENS if g != INV[word[-1]])

        for g in candidates:
            nxt = mat_mul(GENS[g], current)
            walk(word + (g,), nxt)

    walk((), I)

    distinct = len(shapes)
    collisions = word_count - distinct

    # A second pass is unnecessary for largest fiber when no collision
    # exists. If collisions exist, compute exact fiber sizes.
    fibers = {}
    if collisions:
        def walk2(word, current):
            if len(word) == n:
                fibers[current] = fibers.get(current, 0) + 1
                return
            candidates = GENS if not word else (
                g for g in GENS if g != INV[word[-1]]
            )
            for g in candidates:
                walk2(word + (g,), mat_mul(GENS[g], current))
        walk2((), I)

    largest = max(fibers.values(), default=1)

    return word_count, distinct, collisions, largest, shapes

def main():
    print("=" * 78)
    print("ORDERED WORD / SHAPE COLLISION AUDIT")
    print("=" * 78)
    print(f"Expected n=11 words: 4 * 3^10 = {4 * 3**10:,}")
    print()

    # Sanity checks on the inverses.
    print("Inverse checks:")
    print("  sigma1 * sigma1^-1 =", mat_mul(S1, S1_INV) == I)
    print("  sigma0 * sigma0^-1 =", mat_mul(S0, S0_INV) == I)
    print()

    for n in range(1, 12):
        expected = 4 * 3 ** (n - 1)
        wc, distinct, collisions, largest, _ = audit(n)

        print(
            f"n={n:2d}  words={wc:7,}  expected={expected:7,}  "
            f"shapes={distinct:7,}  collisions={collisions:7,}  "
            f"largest_fiber={largest}"
        )

        if wc != expected:
            raise AssertionError(
                f"word-count failure at n={n}: {wc} != {expected}"
            )

    print()
    print("n=11 complete.")
    print("If collisions=0, every reduced ordered history at n=11")
    print("has a distinct 32x32 transformation shape.")
    print("If collisions>0, the printed fiber statistics identify")
    print("the first measured representational collapse at that length.")

if __name__ == "__main__":
    main()
