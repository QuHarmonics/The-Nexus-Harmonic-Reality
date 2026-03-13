#!/usr/bin/env python3
"""Permuted-Constant SHA-256-like hash (research toy)

What this is:
- A SHA-256-*style* one-way compressor: same padding + 512-bit blocks + 64-step schedule.
- Uses the same *constant derivation method* (fractional cube roots of primes -> 32-bit words)
  but consumes the constants in a NON-SHA order (default: largest->smallest).

What this is NOT:
- Not SHA-256.
- Not a vetted cryptographic primitive. Do not use for security.

Design constraint (Nexus-safe):
- NEVER consume the constant table in the prime-ascending order that SHA-256 uses.
  This script guards against that (it will refuse to run if an order equals identity).

CLI examples:
  python permuted_sha256.py "hello"
  python permuted_sha256.py --hex 000102030405060708090a0b0c0d0e0f
  python permuted_sha256.py --order desc "NEXUS"
  python permuted_sha256.py --order popdesc "NEXUS"
"""

from __future__ import annotations

import argparse
import math
from typing import List

MASK32 = 0xFFFFFFFF

# --- bit ops ---

def rotr(x: int, n: int) -> int:
    n &= 31
    return ((x >> n) | ((x << (32 - n)) & MASK32)) & MASK32


def shr(x: int, n: int) -> int:
    return (x >> n) & MASK32


def ch(x: int, y: int, z: int) -> int:
    return (x & y) ^ (~x & z)


def maj(x: int, y: int, z: int) -> int:
    return (x & y) ^ (x & z) ^ (y & z)


def big_sigma0(x: int) -> int:
    return rotr(x, 2) ^ rotr(x, 13) ^ rotr(x, 22)


def big_sigma1(x: int) -> int:
    return rotr(x, 6) ^ rotr(x, 11) ^ rotr(x, 25)


def small_sigma0(x: int) -> int:
    return rotr(x, 7) ^ rotr(x, 18) ^ shr(x, 3)


def small_sigma1(x: int) -> int:
    return rotr(x, 17) ^ rotr(x, 19) ^ shr(x, 10)


def popcount32(x: int) -> int:
    return int(x & MASK32).bit_count()


# --- primes + constants ---

def first_n_primes(n: int) -> List[int]:
    primes: List[int] = []
    x = 2
    while len(primes) < n:
        is_p = True
        r = int(math.isqrt(x))
        for p in primes:
            if p > r:
                break
            if x % p == 0:
                is_p = False
                break
        if is_p:
            primes.append(x)
        x += 1
    return primes


def frac(x: float) -> float:
    return x - math.floor(x)


def cube_root_constants_32(n: int = 64) -> List[int]:
    """K[i] = floor(2^32 * frac(cuberoot(prime_i)))."""
    primes = first_n_primes(n)
    out: List[int] = []
    for p in primes:
        c = p ** (1.0 / 3.0)
        k = int(frac(c) * (2 ** 32)) & MASK32
        out.append(k)
    return out


def sqrt_iv_32(n: int = 8) -> List[int]:
    """IV[j] = floor(2^32 * frac(sqrt(prime_j)))."""
    primes = first_n_primes(n)
    out: List[int] = []
    for p in primes:
        s = math.sqrt(p)
        h = int(frac(s) * (2 ** 32)) & MASK32
        out.append(h)
    return out


def permute_constants(constants: List[int], order: str) -> List[int]:
    """Return a NON-identity permutation of the constant list."""
    if order == "desc":
        perm = sorted(constants, reverse=True)
    elif order == "asc":
        perm = sorted(constants)
    elif order == "popdesc":
        perm = sorted(constants, key=lambda x: (popcount32(x), x), reverse=True)
    else:
        raise ValueError(f"Unknown order: {order}")

    # Guardrail: refuse identity (prime-ascending) ordering.
    if perm == constants:
        raise RuntimeError(
            "Refusing to run: selected ordering equals the prime-ascending identity order. "
            "Pick a different --order." 
        )

    return perm


# --- padding + blocks ---

def pad_message(m: bytes) -> bytes:
    ml = len(m) * 8
    m += b"\x80"
    while ((len(m) * 8) % 512) != 448:
        m += b"\x00"
    m += ml.to_bytes(8, "big")
    return m


def words_from_block(block: bytes) -> List[int]:
    return [int.from_bytes(block[i:i+4], "big") for i in range(0, 64, 4)]


# --- hash ---

def permuted_sha256_like(data: bytes, order: str = "desc") -> bytes:
    # Build the ROM in prime-ascending order (derivation method), then permute it.
    K0 = cube_root_constants_32(64)
    K = permute_constants(K0, order)

    # IV: derived similarly, and permuted to avoid SHA identity.
    H0 = sqrt_iv_32(8)
    H = permute_constants(H0, order)

    msg = pad_message(data)

    for bi in range(0, len(msg), 64):
        block = msg[bi:bi+64]
        W = words_from_block(block)
        for t in range(16, 64):
            W.append((small_sigma1(W[t-2]) + W[t-7] + small_sigma0(W[t-15]) + W[t-16]) & MASK32)

        a, b, c, d, e, f, g, h = H

        for t in range(64):
            T1 = (h + big_sigma1(e) + ch(e, f, g) + K[t] + W[t]) & MASK32
            T2 = (big_sigma0(a) + maj(a, b, c)) & MASK32
            h = g
            g = f
            f = e
            e = (d + T1) & MASK32
            d = c
            c = b
            b = a
            a = (T1 + T2) & MASK32

        H = [
            (H[0] + a) & MASK32,
            (H[1] + b) & MASK32,
            (H[2] + c) & MASK32,
            (H[3] + d) & MASK32,
            (H[4] + e) & MASK32,
            (H[5] + f) & MASK32,
            (H[6] + g) & MASK32,
            (H[7] + h) & MASK32,
        ]

    return b"".join(x.to_bytes(4, "big") for x in H)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("input", nargs="?", default="")
    ap.add_argument("--hex", action="store_true", help="treat input as hex bytes")
    ap.add_argument("--order", default="desc", choices=["desc", "asc", "popdesc"],
                    help="constant consumption order (must not be identity)")
    args = ap.parse_args()

    if args.hex:
        data = bytes.fromhex(args.input)
    else:
        data = args.input.encode("utf-8")

    digest = permuted_sha256_like(data, order=args.order)
    print(digest.hex())


if __name__ == "__main__":
    main()
