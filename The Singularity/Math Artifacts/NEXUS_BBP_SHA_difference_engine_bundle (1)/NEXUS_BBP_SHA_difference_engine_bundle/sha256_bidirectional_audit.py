#!/usr/bin/env python3
"""Bidirectional SHA-256 transformation audit for the NEXUS observer model.

This script uses only the Python standard library. It tests:
  1. Standard SHA-256 compatibility against hashlib.
  2. Reversal of the 64-word message schedule from W[48:64].
  3. Exact inversion of each SHA-256 round when W[t] and K[t] are known.
  4. Observer-assisted return from digest + schedule-tail records.
  5. The finite two-nibble XOR fiber witness and one-byte SHA injectivity.

Important: the schedule tail is an invertible 512-bit recoding of a 512-bit
padded block. It is not compression and is not a digest-only inverse.
"""
from __future__ import annotations
import hashlib
import json
import random
import struct
from pathlib import Path

MASK = 0xFFFFFFFF

def rotr(x: int, n: int) -> int:
    return ((x >> n) | (x << (32 - n))) & MASK

def Ch(x: int, y: int, z: int) -> int:
    return (x & y) ^ ((~x & MASK) & z)

def Maj(x: int, y: int, z: int) -> int:
    return (x & y) ^ (x & z) ^ (y & z)

def BSIG0(x: int) -> int:
    return rotr(x, 2) ^ rotr(x, 13) ^ rotr(x, 22)

def BSIG1(x: int) -> int:
    return rotr(x, 6) ^ rotr(x, 11) ^ rotr(x, 25)

def SSIG0(x: int) -> int:
    return rotr(x, 7) ^ rotr(x, 18) ^ (x >> 3)

def SSIG1(x: int) -> int:
    return rotr(x, 17) ^ rotr(x, 19) ^ (x >> 10)

IV = [
    0x6A09E667, 0xBB67AE85, 0x3C6EF372, 0xA54FF53A,
    0x510E527F, 0x9B05688C, 0x1F83D9AB, 0x5BE0CD19,
]
K = [
    0x428A2F98,0x71374491,0xB5C0FBCF,0xE9B5DBA5,0x3956C25B,0x59F111F1,0x923F82A4,0xAB1C5ED5,
    0xD807AA98,0x12835B01,0x243185BE,0x550C7DC3,0x72BE5D74,0x80DEB1FE,0x9BDC06A7,0xC19BF174,
    0xE49B69C1,0xEFBE4786,0x0FC19DC6,0x240CA1CC,0x2DE92C6F,0x4A7484AA,0x5CB0A9DC,0x76F988DA,
    0x983E5152,0xA831C66D,0xB00327C8,0xBF597FC7,0xC6E00BF3,0xD5A79147,0x06CA6351,0x14292967,
    0x27B70A85,0x2E1B2138,0x4D2C6DFC,0x53380D13,0x650A7354,0x766A0ABB,0x81C2C92E,0x92722C85,
    0xA2BFE8A1,0xA81A664B,0xC24B8B70,0xC76C51A3,0xD192E819,0xD6990624,0xF40E3585,0x106AA070,
    0x19A4C116,0x1E376C08,0x2748774C,0x34B0BCB5,0x391C0CB3,0x4ED8AA4A,0x5B9CCA4F,0x682E6FF3,
    0x748F82EE,0x78A5636F,0x84C87814,0x8CC70208,0x90BEFFFA,0xA4506CEB,0xBEF9A3F7,0xC67178F2,
]

def pad(data: bytes) -> bytes:
    bit_len = len(data) * 8
    out = data + b"\x80"
    out += b"\x00" * ((56 - len(out) % 64) % 64)
    out += struct.pack(">Q", bit_len)
    assert len(out) % 64 == 0
    return out

def block_words(block: bytes) -> list[int]:
    if len(block) != 64:
        raise ValueError("SHA-256 block must be 64 bytes")
    return list(struct.unpack(">16I", block))

def expand_schedule(block: bytes) -> list[int]:
    w = block_words(block) + [0] * 48
    for t in range(16, 64):
        w[t] = (SSIG1(w[t-2]) + w[t-7] + SSIG0(w[t-15]) + w[t-16]) & MASK
    return w

def reverse_schedule_tail(tail: list[int]) -> list[int]:
    if len(tail) != 16:
        raise ValueError("schedule tail must be W[48..63], sixteen words")
    w: list[int | None] = [None] * 64
    w[48:64] = tail[:]
    # W[t-16] = W[t] - sigma1(W[t-2]) - W[t-7] - sigma0(W[t-15]) mod 2^32
    for t in range(63, 15, -1):
        needed = (t, t-2, t-7, t-15)
        if any(w[i] is None for i in needed):
            raise AssertionError(f"inverse schedule dependency unavailable at t={t}")
        w[t-16] = (w[t] - SSIG1(w[t-2]) - w[t-7] - SSIG0(w[t-15])) & MASK
    if any(v is None for v in w):
        raise AssertionError("inverse schedule left unknown words")
    return [int(v) for v in w]

def round_forward(s: list[int], wt: int, kt: int) -> list[int]:
    a,b,c,d,e,f,g,h = s
    t1 = (h + BSIG1(e) + Ch(e,f,g) + kt + wt) & MASK
    t2 = (BSIG0(a) + Maj(a,b,c)) & MASK
    return [(t1+t2)&MASK, a, b, c, (d+t1)&MASK, e, f, g]

def round_inverse(sp: list[int], wt: int, kt: int) -> list[int]:
    ap,bp,cp,dp,ep,fp,gp,hp = sp
    # The shift wires directly reveal a,b,c,e,f,g.
    a,b,c,e,f,g = bp,cp,dp,fp,gp,hp
    t2 = (BSIG0(a) + Maj(a,b,c)) & MASK
    t1 = (ap - t2) & MASK
    d = (ep - t1) & MASK
    h = (t1 - BSIG1(e) - Ch(e,f,g) - kt - wt) & MASK
    return [a,b,c,d,e,f,g,h]

def compress_with_trace(hin: list[int], block: bytes):
    w = expand_schedule(block)
    state = hin[:]
    snapshots = [state[:]]
    for t in range(64):
        state = round_forward(state, w[t], K[t])
        snapshots.append(state[:])
    e_state = state[:]
    hout = [(x+y)&MASK for x,y in zip(hin, e_state)]
    return hout, e_state, w, snapshots

def digest_custom_and_tail_records(data: bytes):
    padded = pad(data)
    chain = IV[:]
    tails = []
    trace = []
    schedule_matches = 0
    round_inversions = 0
    for bidx in range(0, len(padded), 64):
        block = padded[bidx:bidx+64]
        hout, estate, w, snaps = compress_with_trace(chain, block)
        # Verify the current block's schedule tail is a reversible coordinate.
        w_back = reverse_schedule_tail(w[48:64])
        assert w_back == w
        schedule_matches += 1
        # Invert all 64 rounds from E without using stored intermediate states
        # as operands; compare each recovered state against the forward trace.
        rev = estate[:]
        for t in range(63, -1, -1):
            rev = round_inverse(rev, w[t], K[t])
            assert rev == snaps[t], f"round reverse mismatch at block {bidx//64}, t={t}"
            round_inversions += 1
        assert rev == chain
        tails.append(w[48:64])
        trace.append({"e_state": estate, "hout": hout})
        chain = hout
    return b"".join(struct.pack(">I", x) for x in chain), tails, trace, schedule_matches, round_inversions

def return_from_digest_and_tails(digest: bytes, tails: list[list[int]]):
    if len(digest) != 32:
        raise ValueError("digest must be 32 bytes")
    # The schedule tails decode each padded block independently.
    padded_blocks = []
    schedules = []
    for tail in tails:
        w = reverse_schedule_tail(tail)
        block = b"".join(struct.pack(">I", x) for x in w[:16])
        assert expand_schedule(block) == w
        schedules.append(w)
        padded_blocks.append(block)
    padded = b"".join(padded_blocks)
    if len(padded) < 64 or len(padded) % 64:
        raise AssertionError("reconstructed padding invalid")
    bit_len = struct.unpack(">Q", padded[-8:])[0]
    if bit_len % 8:
        raise AssertionError("only byte-aligned messages are expected in this test")
    length = bit_len // 8
    if length + 9 > len(padded) or (length + 9 + 63)//64 != len(padded)//64:
        raise AssertionError("embedded source length inconsistent with block count")
    recovered = padded[:length]
    if pad(recovered) != padded:
        raise AssertionError("reconstructed blocks do not contain valid SHA-256 padding")
    # Now run from IV, derive the round states anew, reverse each round, and verify digest.
    chain = IV[:]
    inverse_count = 0
    for bi, (block, w) in enumerate(zip(padded_blocks, schedules)):
        hout, estate, wf, snapshots = compress_with_trace(chain, block)
        assert wf == w
        # No E-state or per-round trace is retained in the route record. The
        # E state is regenerated from the recovered block and current chain.
        # Reverse the rounds and compare every recovered state to the forward path.
        rev = estate[:]
        for t in range(63, -1, -1):
            rev = round_inverse(rev, w[t], K[t])
            assert rev == snapshots[t]
            inverse_count += 1
        assert rev == chain
        chain = hout
    assert b"".join(struct.pack(">I", x) for x in chain) == digest
    return recovered, inverse_count

def hamming(a: bytes, b: bytes) -> int:
    return sum((x ^ y).bit_count() for x,y in zip(a,b))

def main():
    # Deterministic 54-message corpus; lengths force several padding/block boundaries.
    rng = random.Random(20261016)
    lengths = [0, 1, 55] + [192 + (i % 9) for i in range(51)]
    assert len(lengths) == 54
    messages = [bytes(rng.randrange(256) for _ in range(n)) for n in lengths]
    total_blocks = sum(len(pad(m)) // 64 for m in messages)
    assert total_blocks == 207, total_blocks

    message_results = []
    total_rounds = 0
    total_schedule = 0
    total_inv2 = 0
    for i, msg in enumerate(messages):
        digest, tails, _trace, sched_n, inv_n = digest_custom_and_tail_records(msg)
        assert digest == hashlib.sha256(msg).digest(), f"hashlib mismatch message {i}"
        returned, inv_n2 = return_from_digest_and_tails(digest, tails)
        assert returned == msg, f"observer return mismatch message {i}"
        assert hashlib.sha256(returned).digest() == digest
        blocks = len(pad(msg)) // 64
        total_rounds += inv_n
        total_schedule += sched_n
        total_inv2 += inv_n2
        message_results.append({
            "index": i, "length_bytes": len(msg), "blocks": blocks,
            "digest": digest.hex(), "return_exact": True,
            "hashlib_match": True, "schedule_tail_bits": 512 * blocks,
            "original_padded_block_bits": 512 * blocks,
        })

    # Exhaustive one-byte domain: no duplicate SHA digest among 256 candidates.
    byte_map = {}
    for x in range(256):
        d = hashlib.sha256(bytes([x])).digest()
        assert d not in byte_map
        byte_map[d] = x
    one_byte_roundtrip = all(byte_map[hashlib.sha256(bytes([x])).digest()] == x for x in range(256))

    # Exact fiber witness H(a,b)=a XOR b; store r=a, recover b=h XOR r.
    fiber_count = 0
    for a in range(16):
        for b in range(16):
            h = a ^ b
            r = a
            b_back = h ^ r
            assert b_back == b
            fiber_count += 1
    assert fiber_count == 256

    report = {
        "test_name": "NEXUS SHA-256 bidirectional audit",
        "corpus_messages": len(messages),
        "compression_blocks": total_blocks,
        "sha256_matches_hashlib": len(messages),
        "exact_message_returns": len(messages),
        "schedule_tail_reconstructions": total_schedule,
        "round_inversions_first_pass": total_rounds,
        "round_inversions_return_pass": total_inv2,
        "total_round_inverse_checks": total_rounds + total_inv2,
        "schedule_tail_bits_per_block": 512,
        "original_padded_block_bits_per_block": 512,
        "schedule_tail_is_compression": False,
        "one_byte_domain": {
            "candidate_messages": 256,
            "distinct_digests": len(byte_map),
            "exact_domain_reverse_lookup": one_byte_roundtrip,
            "digest_only_general_inverse_proven": False,
        },
        "xor_fiber_witness": {
            "source_pairs": fiber_count,
            "surface_values": 16,
            "members_per_fiber": 16,
            "residual_bits_sufficient": 4,
            "return_exact": True,
        },
        "message_results": message_results,
        "interpretation": {
            "verified": [
                "The SHA-256 message schedule can be reversed exactly from W[48..63].",
                "Each SHA-256 round can be inverted exactly when W[t] and K[t] are known.",
                "Schedule-tail route records reconstruct all messages exactly; the supplied digest then verifies closure.",
                "The reconstructed sources hash to the exact digest given at closure.",
            ],
            "not_established": [
                "A general SHA-256 inverse from digest alone.",
                "A smaller-than-source residual for unrestricted inputs.",
                "That the schedule tail compresses a 512-bit block; it is a 512-bit bijective recoding.",
            ],
        },
    }
    out = Path(__file__).with_name("sha256_bidirectional_audit_results.json")
    out.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({k:v for k,v in report.items() if k != "message_results"}, indent=2))
    print(f"RESULT_JSON={out}")

if __name__ == "__main__":
    main()
