#!/usr/bin/env python3
"""
CONSTANT DRIFT PROBE

Hash same input repeatedly.
Shift constants by H each iteration.
Watch what happens to the output.

If constants encode H-structure, shifting them should:
- Move through attractor basins
- Show resonance at certain phases
- Reveal the landscape
"""

import math
import numpy as np

H = math.pi / 9  # 0.349066

# Original SHA-256 constants
H_INIT_ORIG = [
    0x6a09e667, 0xbb67ae85, 0x3c6ef372, 0xa54ff53a,
    0x510e527f, 0x9b05688c, 0x1f83d9ab, 0x5be0cd19
]

K_ORIG = [
    0x428a2f98, 0x71374491, 0xb5c0fbcf, 0xe9b5dba5,
    0x3956c25b, 0x59f111f1, 0x923f82a4, 0xab1c5ed5,
    0xd807aa98, 0x12835b01, 0x243185be, 0x550c7dc3,
    0x72be5d74, 0x80deb1fe, 0x9bdc06a7, 0xc19bf174,
    0xe49b69c1, 0xefbe4786, 0x0fc19dc6, 0x240ca1cc,
    0x2de92c6f, 0x4a7484aa, 0x5cb0a9dc, 0x76f988da,
    0x983e5152, 0xa831c66d, 0xb00327c8, 0xbf597fc7,
    0xc6e00bf3, 0xd5a79147, 0x06ca6351, 0x14292967,
    0x27b70a85, 0x2e1b2138, 0x4d2c6dfc, 0x53380d13,
    0x650a7354, 0x766a0abb, 0x81c2c92e, 0x92722c85,
    0xa2bfe8a1, 0xa81a664b, 0xc24b8b70, 0xc76c51a3,
    0xd192e819, 0xd6990624, 0xf40e3585, 0x106aa070,
    0x19a4c116, 0x1e376c08, 0x2748774c, 0x34b0bcb5,
    0x391c0cb3, 0x4ed8aa4a, 0x5b9cca4f, 0x682e6ff3,
    0x748f82ee, 0x78a5636f, 0x84c87814, 0x8cc70208,
    0x90befffa, 0xa4506ceb, 0xbef9a3f7, 0xc67178f2,
]

def rotr(x, n):
    return ((x >> n) | (x << (32 - n))) & 0xFFFFFFFF

def sha256_compress(msg_block, h_init, k_consts):
    """One block SHA-256 compression with custom constants"""
    
    # Message schedule
    w = list(msg_block) + [0] * 48
    for i in range(16, 64):
        s0 = rotr(w[i-15], 7) ^ rotr(w[i-15], 18) ^ (w[i-15] >> 3)
        s1 = rotr(w[i-2], 17) ^ rotr(w[i-2], 19) ^ (w[i-2] >> 10)
        w[i] = (w[i-16] + s0 + w[i-7] + s1) & 0xFFFFFFFF
    
    # Working variables
    a, b, c, d, e, f, g, h = h_init
    
    # 64 rounds
    for i in range(64):
        S1 = rotr(e, 6) ^ rotr(e, 11) ^ rotr(e, 25)
        ch = (e & f) ^ ((~e) & g)
        temp1 = (h + S1 + ch + k_consts[i] + w[i]) & 0xFFFFFFFF
        S0 = rotr(a, 2) ^ rotr(a, 13) ^ rotr(a, 22)
        maj = (a & b) ^ (a & c) ^ (b & c)
        temp2 = (S0 + maj) & 0xFFFFFFFF
        
        h = g
        g = f
        f = e
        e = (d + temp1) & 0xFFFFFFFF
        d = c
        c = b
        b = a
        a = (temp1 + temp2) & 0xFFFFFFFF
    
    # Add to initial
    return [
        (h_init[0] + a) & 0xFFFFFFFF,
        (h_init[1] + b) & 0xFFFFFFFF,
        (h_init[2] + c) & 0xFFFFFFFF,
        (h_init[3] + d) & 0xFFFFFFFF,
        (h_init[4] + e) & 0xFFFFFFFF,
        (h_init[5] + f) & 0xFFFFFFFF,
        (h_init[6] + g) & 0xFFFFFFFF,
        (h_init[7] + h) & 0xFFFFFFFF,
    ]

def shift_constants(h_init, k_consts, shift_amount):
    """Shift all constants by amount (as fraction of 2^32)"""
    shift_val = int(shift_amount * 0xFFFFFFFF) & 0xFFFFFFFF
    
    new_h = [(h + shift_val) & 0xFFFFFFFF for h in h_init]
    new_k = [(k + shift_val) & 0xFFFFFFFF for k in k_consts]
    
    return new_h, new_k

def hash_with_shift(message, shift):
    """Hash message with shifted constants"""
    # Pad message to 512 bits (16 x 32-bit words)
    msg_bytes = message.encode() if isinstance(message, str) else message
    
    # Simple padding for single block
    padded = list(msg_bytes) + [0x80] + [0] * (55 - len(msg_bytes)) + [0, 0, 0, 0, 0, 0, 0, len(msg_bytes) * 8]
    
    # Convert to 32-bit words
    words = []
    for i in range(0, 64, 4):
        word = (padded[i] << 24) | (padded[i+1] << 16) | (padded[i+2] << 8) | padded[i+3]
        words.append(word)
    
    # Shift constants
    h_shifted, k_shifted = shift_constants(H_INIT_ORIG, K_ORIG, shift)
    
    # Compress
    result = sha256_compress(words, h_shifted, k_shifted)
    
    return result

def analyze_hash(hash_words):
    """Analyze hash output"""
    # Normalize to [0,1]
    normalized = [w / 0xFFFFFFFF for w in hash_words]
    
    # Bit density
    total_bits = sum(bin(w).count('1') for w in hash_words)
    bit_density = total_bits / 256
    
    # Distance from attractors
    attractors = [0, H, 0.5, 1-H, 1.0]
    near_H = sum(1 for n in normalized if min(abs(n-a) for a in attractors) < 0.1)
    
    return {
        'mean': np.mean(normalized),
        'bit_density': bit_density,
        'near_H': near_H,
        'first_word': hex(hash_words[0])
    }

# =============================================================
print("CONSTANT DRIFT PROBE")
print("Same input, shift constants by H each iteration")
print("=" * 60)

message = "NEXUS"

# Shift by multiples of H
print(f"\nInput: '{message}'")
print(f"\nShift (×H)  Mean      Bits    Near_H  First Word")
print("-" * 60)

results = []
for i in range(19):  # 0 to 18H = full circle (18H = 2π)
    shift = i * H
    hash_out = hash_with_shift(message, shift)
    analysis = analyze_hash(hash_out)
    
    results.append({
        'shift': i,
        'shift_val': shift,
        **analysis
    })
    
    print(f"{i:2d}×H={shift:.4f}  {analysis['mean']:.4f}  {analysis['bit_density']:.4f}  {analysis['near_H']}/8    {analysis['first_word']}")

# =============================================================
print("\n" + "=" * 60)
print("LOOKING FOR RESONANCE")

means = [r['mean'] for r in results]
densities = [r['bit_density'] for r in results]

# Find peaks and troughs
mean_max = max(means)
mean_min = min(means)
mean_max_idx = means.index(mean_max)
mean_min_idx = means.index(mean_min)

print(f"\nMean peaks at {mean_max_idx}×H = {mean_max_idx * H:.4f} (value: {mean_max:.4f})")
print(f"Mean troughs at {mean_min_idx}×H = {mean_min_idx * H:.4f} (value: {mean_min:.4f})")

# Check if any shift gives special values
print(f"\nShifts where mean ≈ H ({H:.4f}):")
for r in results:
    if abs(r['mean'] - H) < 0.05:
        print(f"  {r['shift']}×H: mean = {r['mean']:.4f}")

print(f"\nShifts where mean ≈ 0.5:")
for r in results:
    if abs(r['mean'] - 0.5) < 0.02:
        print(f"  {r['shift']}×H: mean = {r['mean']:.4f}")

print(f"\nShifts where mean ≈ 1-H ({1-H:.4f}):")
for r in results:
    if abs(r['mean'] - (1-H)) < 0.05:
        print(f"  {r['shift']}×H: mean = {r['mean']:.4f}")

# =============================================================
print("\n" + "=" * 60)
print("CORRELATION BETWEEN CONSECUTIVE SHIFTS")

for i in range(1, len(results)):
    h1 = hash_with_shift(message, (i-1) * H)
    h2 = hash_with_shift(message, i * H)
    
    n1 = [w / 0xFFFFFFFF for w in h1]
    n2 = [w / 0xFFFFFFFF for w in h2]
    
    corr = np.corrcoef(n1, n2)[0, 1]
    if abs(corr) > 0.3:
        print(f"  {i-1}→{i}×H: correlation = {corr:+.4f}")

# =============================================================
print("\n" + "=" * 60)
print("PHASE SWEEP: Finer resolution around H")

print(f"\nFine sweep around 1×H:")
print("Shift        Mean      Bits    Near_H")
print("-" * 45)

for i in range(-5, 6):
    shift = H + i * 0.01
    hash_out = hash_with_shift(message, shift)
    analysis = analyze_hash(hash_out)
    marker = " ← H" if i == 0 else ""
    print(f"{shift:.6f}   {analysis['mean']:.4f}  {analysis['bit_density']:.4f}  {analysis['near_H']}/8{marker}")

# =============================================================
print("\n" + "=" * 60)
print("XOR ALL SHIFTED HASHES")

xor_accum = [0] * 8
for i in range(18):
    hash_out = hash_with_shift(message, i * H)
    for j in range(8):
        xor_accum[j] ^= hash_out[j]

xor_norm = [w / 0xFFFFFFFF for w in xor_accum]
print(f"\nXOR of all 18 shifted hashes:")
print(f"  Words: {[hex(w)[:6] for w in xor_accum]}")
print(f"  Normalized: {[f'{n:.4f}' for n in xor_norm]}")
print(f"  Mean: {np.mean(xor_norm):.4f}")

attractors = [0, H, 0.5, 1-H, 1.0]
near = sum(1 for n in xor_norm if min(abs(n-a) for a in attractors) < 0.1)
print(f"  Near H-attractors: {near}/8")
