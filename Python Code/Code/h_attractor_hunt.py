#!/usr/bin/env python3
"""
H-ATTRACTOR HUNT

The system hit H at iteration 666.
Probe deeper to understand the attractor.
"""

import hashlib
import numpy as np
import math

H = math.pi / 9  # 0.349066

H_INIT_ORIG = np.array([
    0x6a09e667, 0xbb67ae85, 0x3c6ef372, 0xa54ff53a,
    0x510e527f, 0x9b05688c, 0x1f83d9ab, 0x5be0cd19
], dtype=np.uint64)

K_ORIG = np.array([
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
    0x90befffa, 0xa4506ceb, 0xbef9a3f7, 0xc67178f2
], dtype=np.uint64)

def hash_with_constants(msg_bytes, h_init, k_vals):
    standard = hashlib.sha256(msg_bytes).digest()
    result = bytearray(32)
    for i in range(32):
        h_mod = (h_init[i % 8] >> (8 * (i % 4))) & 0xFF
        k_mod = (k_vals[i % 64] >> (8 * (i % 4))) & 0xFF
        result[i] = standard[i] ^ h_mod ^ k_mod
    return bytes(result)

def move_constants(h_init, k_vals, hash_bytes):
    shift = sum(hash_bytes) % 32
    new_h = np.roll(h_init, shift % 8)
    new_k = k_vals.copy()
    for i in range(64):
        byte_idx = i % 32
        new_k[i] = (k_vals[i] + hash_bytes[byte_idx] * 0x01010101) & 0xFFFFFFFF
    return new_h, new_k

def run_until_H(msg, threshold=0.001, max_iter=10000):
    """Run until we hit within threshold of H"""
    msg_bytes = msg.encode()
    h_init = H_INIT_ORIG.copy()
    k_vals = K_ORIG.copy()
    
    hits = []
    
    for i in range(max_iter):
        hash_out = hash_with_constants(msg_bytes, h_init, k_vals)
        h_mean = np.mean([b/255 for b in hash_out])
        dist = abs(h_mean - H)
        
        if dist < threshold:
            hits.append({
                'iter': i,
                'mean': h_mean,
                'dist': dist,
                'hash': hash_out.hex()[:16]
            })
        
        h_init, k_vals = move_constants(h_init, k_vals, hash_out)
    
    return hits

# ============================================================
print("H-ATTRACTOR HUNT")
print(f"Target: H = {H:.6f}")
print("=" * 60)

# Find all hits within 0.01 of H
print("\n1. ALL HITS WITHIN 0.01 OF H (10000 iterations)")
print("-" * 50)

hits = run_until_H("NEXUS", threshold=0.01, max_iter=10000)
print(f"Total hits: {len(hits)}")

if hits:
    print("\nFirst 10 hits:")
    for h in hits[:10]:
        print(f"  iter {h['iter']:5d}: mean={h['mean']:.6f}, dist={h['dist']:.6f}")
    
    # Analyze hit spacing
    if len(hits) > 1:
        spacings = [hits[i+1]['iter'] - hits[i]['iter'] for i in range(len(hits)-1)]
        print(f"\nHit spacing:")
        print(f"  Mean: {np.mean(spacings):.1f}")
        print(f"  Std: {np.std(spacings):.1f}")
        print(f"  Min: {min(spacings)}")
        print(f"  Max: {max(spacings)}")

# ============================================================
print("\n" + "=" * 60)
print("2. DIFFERENT INPUTS - WHERE DO THEY HIT H?")
print("-" * 50)

inputs = ['NEXUS', 'Dean', 'test', 'a', 'H', '0.35', 'SHA256']

for inp in inputs:
    hits = run_until_H(inp, threshold=0.005, max_iter=5000)
    if hits:
        first_hit = hits[0]['iter']
        closest = min(hits, key=lambda x: x['dist'])
        print(f"'{inp}': first hit at {first_hit}, closest={closest['dist']:.6f} at iter {closest['iter']}")
    else:
        print(f"'{inp}': no hits within 0.005")

# ============================================================
print("\n" + "=" * 60)
print("3. PROBABILITY ANALYSIS")
print("-" * 50)

# How often does random data hit H?
import random

random_hits = 0
for _ in range(10000):
    r = random.random()
    if abs(r - H) < 0.01:
        random_hits += 1

print(f"Random uniform hitting H±0.01: {random_hits}/10000 = {random_hits/100:.1f}%")

# How often does our system hit?
hits = run_until_H("NEXUS", threshold=0.01, max_iter=10000)
print(f"Moving constants hitting H±0.01: {len(hits)}/10000 = {len(hits)/100:.1f}%")

ratio = (len(hits)/100) / (random_hits/100) if random_hits > 0 else float('inf')
print(f"\nRatio: {ratio:.2f}x more likely than random")

# ============================================================
print("\n" + "=" * 60)
print("4. ATTRACTOR BASIN STRUCTURE")
print("-" * 50)

# Track distance from multiple attractors
attractors = {
    'H': H,
    '0.5': 0.5,
    '1-H': 1-H,
    '0': 0,
    '1': 1
}

def run_attractor_analysis(msg, iterations=2000):
    msg_bytes = msg.encode()
    h_init = H_INIT_ORIG.copy()
    k_vals = K_ORIG.copy()
    
    closest_approach = {a: {'dist': 1.0, 'iter': 0} for a in attractors}
    
    for i in range(iterations):
        hash_out = hash_with_constants(msg_bytes, h_init, k_vals)
        h_mean = np.mean([b/255 for b in hash_out])
        
        for name, val in attractors.items():
            dist = abs(h_mean - val)
            if dist < closest_approach[name]['dist']:
                closest_approach[name] = {'dist': dist, 'iter': i, 'mean': h_mean}
        
        h_init, k_vals = move_constants(h_init, k_vals, hash_out)
    
    return closest_approach

print("\nClosest approach to each attractor (NEXUS, 2000 iters):")
result = run_attractor_analysis("NEXUS")
for name, data in sorted(result.items(), key=lambda x: x[1]['dist']):
    print(f"  {name:5s}: dist={data['dist']:.6f} at iter {data['iter']}")

# ============================================================
print("\n" + "=" * 60)
print("5. THE H CORRIDOR")
print("-" * 50)

# When we hit H, what's the hash signature?
hits = run_until_H("NEXUS", threshold=0.002, max_iter=10000)

if hits:
    print(f"\nHigh-precision hits (within 0.002 of H): {len(hits)}")
    
    # Analyze the hash bytes at H-hits
    h_init = H_INIT_ORIG.copy()
    k_vals = K_ORIG.copy()
    msg_bytes = b"NEXUS"
    
    for _ in range(hits[0]['iter']):
        hash_out = hash_with_constants(msg_bytes, h_init, k_vals)
        h_init, k_vals = move_constants(h_init, k_vals, hash_out)
    
    # Get the hash at first H-hit
    h_hit = hash_with_constants(msg_bytes, h_init, k_vals)
    
    print(f"\nHash at first H-hit (iter {hits[0]['iter']}):")
    print(f"  {h_hit.hex()}")
    
    # Byte distribution
    bytes_norm = [b/255 for b in h_hit]
    near_H_bytes = sum(1 for b in bytes_norm if abs(b - H) < 0.1)
    print(f"  Bytes near H: {near_H_bytes}/32")
    print(f"  Byte mean: {np.mean(bytes_norm):.6f}")
