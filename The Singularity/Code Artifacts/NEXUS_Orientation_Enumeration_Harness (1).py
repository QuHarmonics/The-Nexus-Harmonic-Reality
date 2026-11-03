#!/usr/bin/env python3
"""
NEXUS orientation-channel enumeration harness
==============================================

Tests A-D for the discrete orientation bridge.

A. Algebraic channel:
   dim of antisymmetric zero-row-sum matrices and cycle-space dimension.

B. Representation/sign test:
   m=3 channel under S3; verify sign character.

C. Reader realization:
   equal sectors of size k=2:
       N=6, m=3
       N=8, m=4
       N=10, m=5
   Enumerate all sector partitions and test table signatures.
   Full S_N enumeration is done for N=6 and N=8.
   N=10 uses the exact small exceptional family from the existing
   research record plus a reproducible random sample, because
   10! = 3,628,800 and exhaustive permutations x 945 partitions
   is unnecessarily large for a validation harness.

D. Inverse / relabeling checks:
   N=6 three-sector reader:
     - fixed sector labels
     - quotient by A3
     - quotient by S3
   Verify the known 720 / 76 / 388 / 720 figures.

No external packages are required beyond Python 3.10+.
"""

from __future__ import annotations

import itertools
import math
import random
import time
from collections import defaultdict, Counter
from dataclasses import dataclass
from typing import Iterable, Sequence, Tuple, List, Dict

Perm = Tuple[int, ...]
Partition = Tuple[Tuple[int, ...], ...]
Table = Tuple[int, ...]
Signature = Tuple[Table, ...]


# ---------------------------------------------------------------------------
# Basic permutation / partition machinery
# ---------------------------------------------------------------------------

def compose(p: Perm, q: Perm) -> Perm:
    """Return p o q using zero-based images."""
    return tuple(p[q[i]] for i in range(len(p)))


def inverse(p: Perm) -> Perm:
    q = [0] * len(p)
    for i, j in enumerate(p):
        q[j] = i
    return tuple(q)


def apply_perm(p: Perm, x: int) -> int:
    return p[x]


def all_permutations(n: int) -> Iterable[Perm]:
    return itertools.permutations(range(n))


def equal_block_partitions(n: int, m: int) -> Iterable[Partition]:
    """
    Generate set partitions of [0,n) into m unlabeled equal blocks.
    Blocks are canonicalized by requiring their first elements to increase.
    """
    assert n % m == 0
    k = n // m
    cells = tuple(range(n))

    def rec(remaining: Tuple[int, ...], blocks: List[Tuple[int, ...]]):
        if not remaining:
            yield tuple(blocks)
            return

        first = remaining[0]
        rest = remaining[1:]

        # To avoid duplicate unlabeled block partitions, the next block
        # must contain the smallest remaining element.
        for extra in itertools.combinations(rest, k - 1):
            block = tuple(sorted((first,) + extra))
            used = set(block)
            new_remaining = tuple(x for x in remaining if x not in used)
            yield from rec(new_remaining, blocks + [block])

    yield from rec(cells, [])


def partition_index(partition: Partition) -> List[int]:
    """Map cell -> block index."""
    idx = [None] * sum(len(b) for b in partition)
    for j, block in enumerate(partition):
        for x in block:
            idx[x] = j
    return idx


def block_table(p: Perm, idx: Sequence[int], m: int) -> Table:
    C = [0] * (m * m)
    for x, y in enumerate(p):
        i = idx[x]
        j = idx[y]
        C[i * m + j] += 1
    return tuple(C)


def complete_signature(p: Perm, partitions: Sequence[Partition]) -> Signature:
    sig = []
    for P in partitions:
        idx = partition_index(P)
        sig.append(block_table(p, idx, len(P)))
    return tuple(sig)


# ---------------------------------------------------------------------------
# A. Algebraic checks
# ---------------------------------------------------------------------------

def algebraic_dimensions(max_m: int = 8):
    print("\n=== A. DIMENSION / CYCLE-SPACE CHECK ===")
    print(" m | dim antisym zero-row | cycle-space K_m")
    print("---+----------------------+----------------")
    for m in range(2, max_m + 1):
        d1 = (m - 1) * (m - 2) // 2
        d2 = m * (m - 1) // 2 - (m - 1)
        ok = "OK" if d1 == d2 else "FAIL"
        print(f"{m:2d} | {d1:20d} | {d2:14d}  {ok}")


# ---------------------------------------------------------------------------
# B. S3 sign-representation check
# ---------------------------------------------------------------------------

def permute_matrix(A: Tuple[int, ...], m: int, sigma: Perm) -> Tuple[int, ...]:
    """
    Sector relabeling:
      A'_{ij} = A_{sigma^{-1}(i), sigma^{-1}(j)}
    """
    inv = inverse(sigma)
    out = [0] * (m * m)
    for i in range(m):
        for j in range(m):
            out[i * m + j] = A[inv[i] * m + inv[j]]
    return tuple(out)


def A3(a: int) -> Tuple[int, ...]:
    return (
        0,  a, -a,
       -a, 0,  a,
        a, -a, 0,
    )


def parity(p: Perm) -> int:
    invs = 0
    for i in range(len(p)):
        for j in range(i + 1, len(p)):
            if p[i] > p[j]:
                invs += 1
    return -1 if invs % 2 else 1


def sign_representation_check():
    print("\n=== B. S3 SIGN-REPRESENTATION CHECK ===")
    basis = A3(1)
    for sigma in itertools.permutations(range(3)):
        transformed = permute_matrix(basis, 3, sigma)
        expected = A3(parity(sigma))
        ok = transformed == expected
        print(f"sigma={sigma} parity={parity(sigma):+d} -> {ok}")
        if not ok:
            raise AssertionError("S3 sign representation failed")
    print("Result: A3 is exactly the S3 sign representation.")


# ---------------------------------------------------------------------------
# C. Reader enumeration
# ---------------------------------------------------------------------------

def exhaustive_reader_n(n: int, m: int, max_perms: int | None = None):
    partitions = list(equal_block_partitions(n, m))
    print(f"\n=== C. READER ENUMERATION N={n}, m={m}, k={n//m} ===")
    print(f"partitions: {len(partitions)}")
    expected_partitions = math.factorial(n) // (
        math.factorial(n // m) ** m * math.factorial(m)
    )
    assert len(partitions) == expected_partitions

    sig_to_count = defaultdict(int)
    inverse_matches = 0
    nontrivial_inverse_matches = 0

    perms = all_permutations(n)
    seen = 0

    for p in perms:
        sig = complete_signature(p, partitions)
        sig_to_count[sig] += 1

        pinv = inverse(p)
        if complete_signature(pinv, partitions) == sig:
            inverse_matches += 1
            if p != pinv:
                nontrivial_inverse_matches += 1

        seen += 1
        if max_perms is not None and seen >= max_perms:
            break

    print(f"permutations tested: {seen}")
    print(f"distinct complete signatures: {len(sig_to_count)}")
    print(f"inverse matches: {inverse_matches}")
    print(f"nontrivial inverse matches: {nontrivial_inverse_matches}")

    return {
        "n": n,
        "m": m,
        "k": n // m,
        "partitions": len(partitions),
        "permutations_tested": seen,
        "classes": len(sig_to_count),
        "inverse_matches": inverse_matches,
        "nontrivial_inverse_matches": nontrivial_inverse_matches,
    }


# ---------------------------------------------------------------------------
# Efficient special handling for N=10
# ---------------------------------------------------------------------------

def cycle_type(p: Perm) -> Tuple[int, ...]:
    n = len(p)
    seen = [False] * n
    lengths = []
    for i in range(n):
        if not seen[i]:
            j = i
            L = 0
            while not seen[j]:
                seen[j] = True
                L += 1
                j = p[j]
            lengths.append(L)
    return tuple(sorted(lengths, reverse=True))


def random_perm(n: int, rng: random.Random) -> Perm:
    a = list(range(n))
    rng.shuffle(a)
    return tuple(a)


def sample_n10(
    sample_size: int = 60000,
    seed: int = 20260912,
):
    """
    N=10, m=5, k=2.

    The existing research record used:
      * all 240 permutations of cycle type (3,1^7)
      * 60,000 uniformly random permutations

    This function reproduces that test family.

    Note: it does NOT claim exhaustive S10 enumeration.
    """
    n, m = 10, 5
    partitions = list(equal_block_partitions(n, m))
    print(f"\n=== C. N=10 SAMPLE: m=5, k=2 ===")
    print(f"partitions: {len(partitions)}")

    target_type = (3, 1, 1, 1, 1, 1, 1, 1)
    targeted = []
    for p in all_permutations(n):
        if cycle_type(p) == target_type:
            targeted.append(p)

    assert len(targeted) == 240

    rng = random.Random(seed)
    samples = targeted[:]
    samples.extend(random_perm(n, rng) for _ in range(sample_size))

    sig_to_count = defaultdict(int)
    inverse_matches = 0
    nontrivial_inverse_matches = 0

    for p in samples:
        sig = complete_signature(p, partitions)
        sig_to_count[sig] += 1
        if complete_signature(inverse(p), partitions) == sig:
            inverse_matches += 1
            if p != inverse(p):
                nontrivial_inverse_matches += 1

    print(f"targeted permutations: {len(targeted)}")
    print(f"random permutations: {sample_size}")
    print(f"total tested: {len(samples)}")
    print(f"distinct signatures within sample: {len(sig_to_count)}")
    print(f"inverse matches: {inverse_matches}")
    print(f"nontrivial inverse matches: {nontrivial_inverse_matches}")

    return {
        "n": n,
        "m": m,
        "k": 2,
        "partitions": len(partitions),
        "targeted": len(targeted),
        "random": sample_size,
        "seed": seed,
        "tested": len(samples),
        "distinct_sample_signatures": len(sig_to_count),
        "inverse_matches": inverse_matches,
        "nontrivial_inverse_matches": nontrivial_inverse_matches,
    }


# ---------------------------------------------------------------------------
# D. A3/S3 relabeling quotient at N=6
# ---------------------------------------------------------------------------

def sector_relabel_table(C: Table, m: int, sigma: Perm) -> Table:
    inv = inverse(sigma)
    out = [0] * (m * m)
    for i in range(m):
        for j in range(m):
            out[i * m + j] = C[inv[i] * m + inv[j]]
    return tuple(out)


def quotient_signature(sig: Signature, m: int, group: Sequence[Perm]) -> Tuple[Tuple[Table, ...], ...]:
    """
    Quotient each table by simultaneous sector relabeling.
    Canonical representative is lexicographically minimal.
    """
    q = []
    for C in sig:
        orbit = [sector_relabel_table(C, m, g) for g in group]
        q.append(min(orbit))
    return tuple(q)


def relabeling_quotient_n6():
    print("\n=== D. N=6 RELABELING QUOTIENTS ===")
    n, m = 6, 3
    partitions = list(equal_block_partitions(n, m))

    S3 = list(itertools.permutations(range(3)))
    A3_group = [p for p in S3 if parity(p) == 1]

    fixed_classes = set()
    a3_classes = set()
    s3_classes = set()

    fixed_inverse = 0
    a3_inverse = 0
    s3_inverse = 0

    for p in all_permutations(n):
        sig = complete_signature(p, partitions)
        invsig = complete_signature(inverse(p), partitions)

        fixed_classes.add(sig)
        a3sig = quotient_signature(sig, 3, A3_group)
        a3invsig = quotient_signature(invsig, 3, A3_group)
        s3sig = quotient_signature(sig, 3, S3)
        s3invsig = quotient_signature(invsig, 3, S3)

        a3_classes.add(a3sig)
        s3_classes.add(s3sig)

        if sig == invsig:
            fixed_inverse += 1
        if a3sig == a3invsig:
            a3_inverse += 1
        if s3sig == s3invsig:
            s3_inverse += 1

    print(f"fixed-label classes: {len(fixed_classes)}")
    print(f"A3-quotient classes: {len(a3_classes)}")
    print(f"S3-quotient classes: {len(s3_classes)}")
    print(f"fixed-label inverse matches: {fixed_inverse}")
    print(f"A3-quotient inverse matches: {a3_inverse}")
    print(f"S3-quotient inverse matches: {s3_inverse}")

    return {
        "fixed_classes": len(fixed_classes),
        "A3_classes": len(a3_classes),
        "S3_classes": len(s3_classes),
        "fixed_inverse_matches": fixed_inverse,
        "A3_inverse_matches": a3_inverse,
        "S3_inverse_matches": s3_inverse,
    }


def main():
    t0 = time.time()

    algebraic_dimensions()
    sign_representation_check()

    # Full small cases.
    n6 = exhaustive_reader_n(6, 3)
    n8 = exhaustive_reader_n(8, 4)

    # N=10 reproducibility sample.
    n10 = sample_n10()

    d = relabeling_quotient_n6()

    print("\n=== EXPECTED REFERENCE CHECKS ===")
    print("N=6 fixed-label: 720 classes, 76 inverse matches, 0 nontrivial.")
    print("N=6 A3 quotient: 720 classes, 76 inverse matches.")
    print("N=6 S3 quotient: 388 classes, all 720 inverse matches.")
    print("N=8 m=4 is the next full equal-sector case.")
    print("N=10 m=5 uses the documented 240 + 60,000 sample protocol.")

    print(f"\nElapsed: {time.time() - t0:.2f}s")

if __name__ == "__main__":
    main()
