#!/usr/bin/env python3
"""
BYTE-LEVEL GATE ITERATION

Each hash byte gates its corresponding constant byte.
Run iteratively, see what emerges.

hash[i] ⊕ const[i] → new_const[i]
Then re-hash with new constants.
Repeat.
"""

import hashlib
import numpy as np
import math

H = math.pi / 9

# Constants as bytes
CONST_ORIG = bytes([
    0x6a, 0x09, 0xe6, 0x67, 0xbb, 0x67, 0xae, 0x85,
    0x3c, 0x6e, 0xf3, 0x72, 0xa5, 0x4f, 0xf5, 0x3a,
    0x51, 0x0e, 0x52, 0x7f, 0x9b, 0x05, 0x68, 0x8c,
    0x1f, 0x83, 0xd9, 0xab, 0x5b, 0xe0, 0xcd, 0x19
])

def hash_with_byte_constants(msg_bytes, const_bytes):
    """Hash XOR'd with current constants"""
    base = hashlib.sha256(msg_bytes).digest()
    return bytes(b ^ c for b, c in zip(base, const_bytes))

def gate_constants(hash_bytes, const_bytes):
    """Each hash byte gates corresponding constant"""
    return bytes(h ^ c for h, c in zip(hash_bytes, const_bytes))

def iterate(msg, iterations=100):
    """Run gate iteration"""
    msg_bytes = msg.encode()
    const = bytearray(CONST_ORIG)
    
    history = []
    
    for i in range(iterations):
        # Hash with current constants
        h = hash_with_byte_constants(msg_bytes, const)
        
        # Measure
        h_mean = np.mean([b/255 for b in h])
        c_mean = np.mean([b/255 for b in const])
        
        history.append({
            'iter': i,
            'hash': h.hex()[:16],
            'h_mean': h_mean,
            'c_mean': c_mean,
            'dist_H': abs(h_mean - H)
        })
        
        # Gate constants
        const = bytearray(gate_constants(h, const))
    
    return history

# ============================================================
print("BYTE-LEVEL GATE ITERATION")
print("hash[i] ⊕ const[i] → const[i]")
print("=" * 60)

msg = "NEXUS"
hist = iterate(msg, iterations=100)

print(f"\nInput: '{msg}'")
print(f"H = {H:.6f}")
print(f"\nIter | Hash Mean | Const Mean | Dist to H")
print("-" * 50)

for i in [0, 1, 2, 5, 10, 20, 50, 99]:
    h = hist[i]
    print(f"{h['iter']:4d} | {h['h_mean']:.6f}  | {h['c_mean']:.6f}   | {h['dist_H']:.6f}")

# ============================================================
print("\n" + "=" * 60)
print("CYCLE DETECTION")

# Check for cycles
hashes = [h['hash'] for h in hist]
unique = len(set(hashes))
print(f"Unique hashes in 100 iters: {unique}")

# Find cycle length
for cycle_len in range(1, 50):
    if hashes[-1] == hashes[-1-cycle_len]:
        print(f"Cycle detected: length = {cycle_len}")
        break

# ============================================================
print("\n" + "=" * 60)
print("MULTIPLE INPUTS")

inputs = ['NEXUS', 'Dean', 'test', 'a', 'H', 'pi']

print(f"\nFinal state after 100 iterations:")
print(f"{'Input':<8} | Hash Mean | Const Mean | Near H?")
print("-" * 50)

for inp in inputs:
    hist = iterate(inp, 100)
    final = hist[-1]
    near = abs(final['h_mean'] - H) < 0.1
    print(f"{inp:<8} | {final['h_mean']:.6f}  | {final['c_mean']:.6f}   | {'YES' if near else 'no'}")

# ============================================================
print("\n" + "=" * 60)
print("LONGER RUN - 1000 iterations")

hist = iterate("NEXUS", 1000)

means = [h['h_mean'] for h in hist]
dists = [h['dist_H'] for h in hist]

# Closest to H
min_dist = min(dists)
min_idx = dists.index(min_dist)
print(f"\nClosest to H: {means[min_idx]:.6f} at iter {min_idx} (dist={min_dist:.6f})")

# Attractors visited
print(f"\nAttractor visits:")
attractors = {'H': H, '0.5': 0.5, '1-H': 1-H}
for name, val in attractors.items():
    visits = sum(1 for m in means if abs(m - val) < 0.02)
    closest = min(abs(m - val) for m in means)
    print(f"  {name}: {visits} visits within 0.02, closest={closest:.6f}")

# ============================================================
print("\n" + "=" * 60)
print("WHAT'S THE FIXED POINT?")

# Run until hash stops changing
const = bytearray(CONST_ORIG)
msg_bytes = b"NEXUS"

prev_hash = None
for i in range(10000):
    h = hash_with_byte_constants(msg_bytes, const)
    
    if h == prev_hash:
        print(f"\nFIXED POINT FOUND at iteration {i}")
        h_mean = np.mean([b/255 for b in h])
        print(f"  Hash: {h.hex()}")
        print(f"  Mean: {h_mean:.6f}")
        print(f"  Distance to H: {abs(h_mean - H):.6f}")
        break
    
    prev_hash = h
    const = bytearray(gate_constants(h, const))
else:
    print("\nNo fixed point in 10000 iterations")
    # Check last values
    print(f"Last hash mean: {np.mean([b/255 for b in h]):.6f}")

# ============================================================
print("\n" + "=" * 60)
print("FIXED POINT ANALYSIS")

# XOR is its own inverse, so h ⊕ c = h ⊕ c
# Fixed point: h ⊕ c = c implies h = 0
# OR: cycle of length 2 where h1 ⊕ c1 = c2 and h2 ⊕ c2 = c1

print("\nChecking for 2-cycle...")
const = bytearray(CONST_ORIG)
msg_bytes = b"NEXUS"

states = []
for i in range(100):
    h = hash_with_byte_constants(msg_bytes, const)
    state = (h.hex(), bytes(const).hex())
    
    if state in states:
        cycle_start = states.index(state)
        print(f"Cycle found: starts at {cycle_start}, current={i}, length={i-cycle_start}")
        
        # Analyze cycle
        cycle_hashes = [s[0] for s in states[cycle_start:]]
        cycle_means = [np.mean([int(s[j:j+2], 16)/255 for j in range(0, 64, 2)]) for s in cycle_hashes]
        print(f"Cycle hash means: {[f'{m:.4f}' for m in cycle_means[:5]]}")
        break
    
    states.append(state)
    const = bytearray(gate_constants(h, const))
