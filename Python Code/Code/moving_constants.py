#!/usr/bin/env python3
"""
MOVING CONSTANTS EXPERIMENT

Hash same input repeatedly.
Each iteration: constants shift based on previous hash.
See what emerges.
"""

import hashlib
import numpy as np
import math

H = math.pi / 9  # 0.349066

# Original SHA constants
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
    """
    Custom SHA-256 with movable constants.
    Simplified - just XOR constants into standard hash.
    """
    # Get standard hash
    standard = hashlib.sha256(msg_bytes).digest()
    
    # Modify by XORing with shifted constants
    result = bytearray(32)
    for i in range(32):
        h_mod = (h_init[i % 8] >> (8 * (i % 4))) & 0xFF
        k_mod = (k_vals[i % 64] >> (8 * (i % 4))) & 0xFF
        result[i] = standard[i] ^ h_mod ^ k_mod
    
    return bytes(result)

def move_constants(h_init, k_vals, hash_bytes):
    """
    Move constants based on hash output.
    This is the feedback loop.
    """
    # Extract shift amount from hash
    shift = sum(hash_bytes) % 32
    
    # Rotate H_INIT based on hash
    new_h = np.roll(h_init, shift % 8)
    
    # Shift K values based on hash bytes
    new_k = k_vals.copy()
    for i in range(64):
        byte_idx = i % 32
        new_k[i] = (k_vals[i] + hash_bytes[byte_idx] * 0x01010101) & 0xFFFFFFFF
    
    return new_h, new_k

def measure_state(hash_bytes, h_init, k_vals):
    """Measure current state"""
    # Hash normalized mean
    h_mean = np.mean([b/255 for b in hash_bytes])
    
    # Constants normalized mean
    h_init_mean = np.mean(h_init / 0xFFFFFFFF)
    k_mean = np.mean(k_vals / 0xFFFFFFFF)
    
    # Distance to H
    h_dist = abs(h_mean - H)
    
    # Bit density
    bits = bin(int.from_bytes(hash_bytes, 'big'))[2:].zfill(256)
    density = bits.count('1') / 256
    
    return h_mean, h_init_mean, k_mean, h_dist, density

def run_experiment(msg, iterations=100):
    """Run the moving constants experiment"""
    msg_bytes = msg.encode()
    
    # Start with original constants
    h_init = H_INIT_ORIG.copy()
    k_vals = K_ORIG.copy()
    
    history = []
    
    for i in range(iterations):
        # Hash with current constants
        hash_out = hash_with_constants(msg_bytes, h_init, k_vals)
        
        # Measure
        h_mean, h_init_mean, k_mean, h_dist, density = measure_state(hash_out, h_init, k_vals)
        
        history.append({
            'iter': i,
            'h_mean': h_mean,
            'h_init_mean': h_init_mean,
            'k_mean': k_mean,
            'h_dist': h_dist,
            'density': density,
            'hash': hash_out.hex()[:16]
        })
        
        # Move constants based on hash
        h_init, k_vals = move_constants(h_init, k_vals, hash_out)
    
    return history, h_init, k_vals

# ============================================================
print("MOVING CONSTANTS EXPERIMENT")
print("Hash same input, move constants each iteration")
print("=" * 60)

msg = "NEXUS"
history, final_h, final_k = run_experiment(msg, iterations=100)

print(f"\nInput: '{msg}'")
print(f"H = {H:.6f}")
print(f"\nIteration | Hash Mean | H_dist | Density | Hash")
print("-" * 60)

for h in [history[0], history[1], history[9], history[49], history[99]]:
    print(f"{h['iter']:4d}      | {h['h_mean']:.6f}  | {h['h_dist']:.6f} | {h['density']:.4f}  | {h['hash']}")

# ============================================================
print("\n" + "=" * 60)
print("CONVERGENCE ANALYSIS")

means = [h['h_mean'] for h in history]
dists = [h['h_dist'] for h in history]
densities = [h['density'] for h in history]

print(f"\nHash mean:")
print(f"  Start: {means[0]:.6f}")
print(f"  End:   {means[-1]:.6f}")
print(f"  Min:   {min(means):.6f} at iter {means.index(min(means))}")
print(f"  Max:   {max(means):.6f} at iter {means.index(max(means))}")

print(f"\nDistance to H ({H:.4f}):")
print(f"  Start: {dists[0]:.6f}")
print(f"  End:   {dists[-1]:.6f}")
print(f"  Min:   {min(dists):.6f} at iter {dists.index(min(dists))}")

print(f"\nBit density (target 0.529):")
print(f"  Start: {densities[0]:.6f}")
print(f"  End:   {densities[-1]:.6f}")
print(f"  Mean:  {np.mean(densities):.6f}")

# ============================================================
print("\n" + "=" * 60)
print("ATTRACTOR DETECTION")

# Check if it converges to a cycle
last_10 = [h['hash'] for h in history[-10:]]
unique_last_10 = len(set(last_10))
print(f"\nUnique hashes in last 10: {unique_last_10}/10")

if unique_last_10 < 10:
    print("  → CYCLE DETECTED")
else:
    print("  → Still exploring")

# Check for H-attractor convergence
near_H_count = sum(1 for d in dists if d < 0.05)
print(f"\nIterations within 0.05 of H: {near_H_count}/100")

# ============================================================
print("\n" + "=" * 60)
print("MULTIPLE INPUTS")

inputs = ['NEXUS', 'Dean', 'test', 'a', 'H = pi/9']

print("\nFinal state after 100 iterations:")
print(f"{'Input':<12} | Final Mean | Dist to H | Near H?")
print("-" * 50)

for inp in inputs:
    hist, _, _ = run_experiment(inp, iterations=100)
    final_mean = hist[-1]['h_mean']
    final_dist = hist[-1]['h_dist']
    near = "YES" if final_dist < 0.1 else "no"
    print(f"{inp:<12} | {final_mean:.6f}   | {final_dist:.6f}  | {near}")

# ============================================================
print("\n" + "=" * 60)
print("LONG RUN - 1000 iterations")

hist_long, _, _ = run_experiment("NEXUS", iterations=1000)

means_long = [h['h_mean'] for h in hist_long]
dists_long = [h['h_dist'] for h in hist_long]

# Find minimum distance to H
min_dist = min(dists_long)
min_idx = dists_long.index(min_dist)

print(f"\nClosest approach to H:")
print(f"  Distance: {min_dist:.6f}")
print(f"  At iteration: {min_idx}")
print(f"  Mean at that point: {means_long[min_idx]:.6f}")

# Check for oscillation around H
crossings = 0
for i in range(1, len(means_long)):
    if (means_long[i-1] < H) != (means_long[i] < H):
        crossings += 1

print(f"\nCrossings through H: {crossings}")
print(f"  (oscillation indicator)")

# Final 100 stats
final_100_means = means_long[-100:]
print(f"\nFinal 100 iterations:")
print(f"  Mean of means: {np.mean(final_100_means):.6f}")
print(f"  Std: {np.std(final_100_means):.6f}")
print(f"  Range: [{min(final_100_means):.4f}, {max(final_100_means):.4f}]")
