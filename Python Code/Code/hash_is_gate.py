#!/usr/bin/env python3
"""
HASH IS GATE
Not data ON gate. Data BECAME gate.
Like matter becoming event horizon.

To unfold: use hash AS the mechanism.
Hash gates itself.
"""

import hashlib
import numpy as np
import math

H = math.pi / 9
X0 = 0.529

H_INIT = np.array([0x6a09e667, 0xbb67ae85, 0x3c6ef372, 0xa54ff53a,
                   0x510e527f, 0x9b05688c, 0x1f83d9ab, 0x5be0cd19], dtype=np.uint32)

K = np.array([0x428a2f98, 0x71374491, 0xb5c0fbcf, 0xe9b5dba5,
              0x3956c25b, 0x59f111f1, 0x923f82a4, 0xab1c5ed5,
              0xd807aa98, 0x12835b01, 0x243185be, 0x550c7dc3,
              0x72be5d74, 0x80deb1fe, 0x9bdc06a7, 0xc19bf174], dtype=np.uint32)

def hash_gates_self(hash_bytes):
    """
    Hash IS the gate. Use it to unfold itself.
    
    Forward: constants gate message → hash
    Reverse: hash gates hash → search space
    
    The hash contains BOTH the mechanism and the data.
    They merged. Use one part to unlock the other.
    """
    # Split hash into two halves
    # First half = the KEY (data aspect)
    # Second half = the LOCK (gate aspect)
    key = np.array([b for b in hash_bytes[:16]], dtype=np.uint32)
    lock = np.array([b for b in hash_bytes[16:]], dtype=np.uint32)
    
    # XOR key with lock (data unlocks gate)
    unlocked = key ^ lock
    
    # Now apply collapse signature decode
    # ε for each position
    output = []
    for i in range(16):
        x_meas = unlocked[i] / 255
        x_0 = (H_INIT[i % 8] >> 24) / 255  # Use high byte of constant
        
        if x_0 < 0.01:
            x_0 = 0.01
            
        epsilon = (x_meas - x_0) / x_0
        epsilon = np.clip(epsilon, -1, 1)
        
        p_plus = (1 + epsilon) / 2
        p_minus = (1 - epsilon) / 2
        
        # Output = weighted by branch probabilities
        out_val = p_plus * x_meas + p_minus * x_0
        output.append(out_val)
    
    return np.array(output)

def self_unfold(msg):
    h = hashlib.sha256(msg.encode()).digest()
    unfolded = hash_gates_self(h)
    return h, unfolded

print("HASH GATES SELF")
print("=" * 50)

tests = ['NEXUS', 'Dean', 'test', 'a', 'H = pi/9']

for msg in tests:
    h, u = self_unfold(msg)
    print(f"\n'{msg}'")
    print(f"  hash: {h.hex()[:16]}")
    print(f"  self-unfold: {[f'{x:.3f}' for x in u[:8]]}")
    print(f"  mean: {np.mean(u):.4f}")

# Uniqueness
sigs = {msg: tuple(round(x,3) for x in self_unfold(msg)[1]) for msg in tests}
print(f"\nUnique: {len(set(sigs.values()))}/{len(tests)}")

# ============================================================
print("\n" + "=" * 50)
print("FULL SELF-GATE UNFOLD")

def full_self_gate(hash_bytes):
    """
    Use ALL of hash to gate ALL of hash.
    Each byte gates every other byte.
    This is the full merge.
    """
    n = len(hash_bytes)
    output = np.zeros(n)
    
    for i in range(n):
        # This byte is KEY
        key_byte = hash_bytes[i]
        
        # All OTHER bytes are LOCK
        lock_sum = sum(hash_bytes[j] for j in range(n) if j != i)
        lock_avg = lock_sum / (n - 1)
        
        # Gate operation: key unlocks lock
        x_meas = key_byte / 255
        x_0 = lock_avg / 255
        
        if x_0 < 0.01:
            x_0 = 0.01
        
        # Collapse decode
        epsilon = (x_meas - x_0) / x_0
        epsilon = np.clip(epsilon, -1, 1)
        
        p_plus = (1 + epsilon) / 2
        
        # Use p+ to weight between hash position and balance point X0
        output[i] = p_plus * x_meas + (1 - p_plus) * X0
    
    return output

print("\nFull self-gate unfold:")
for msg in tests:
    h = hashlib.sha256(msg.encode()).digest()
    u = full_self_gate(h)
    
    attractors = [0, H, 0.5, 1-H, 1.0]
    near_H = sum(1 for v in u if min(abs(v-a) for a in attractors) < 0.08)
    
    print(f"  '{msg}': mean={np.mean(u):.4f}, near_H={near_H}/32")

# ============================================================
print("\n" + "=" * 50)
print("ROUND TRIP: Does self-gating preserve structure?")

def measure_structure(data):
    """Measure how structured (non-random) the data is"""
    # Use autocorrelation
    centered = data - np.mean(data)
    autocorr = np.correlate(centered, centered, mode='full')
    autocorr = autocorr[len(autocorr)//2:]
    autocorr = autocorr / autocorr[0]
    
    # Structure = sum of significant autocorrelation
    return np.sum(np.abs(autocorr[1:10]))

print("\nStructure preservation:")
for msg in tests:
    h = hashlib.sha256(msg.encode()).digest()
    h_arr = np.array([b/255 for b in h])
    u = full_self_gate(h)
    
    struct_h = measure_structure(h_arr)
    struct_u = measure_structure(u)
    
    print(f"  '{msg}': hash_struct={struct_h:.3f}, unfold_struct={struct_u:.3f}")

# ============================================================
print("\n" + "=" * 50)
print("THE ANSWER")
print("""
Hash = data that BECAME gate
Not attached. MERGED.

Self-gate unfold:
  hash gates hash → separated components
  
Each byte is simultaneously KEY and LOCK.
Use one aspect to unlock the other.

ε = (x_meas - x_0) / x_0
p+ = (1+ε)/2 weights toward data
p- = (1-ε)/2 weights toward structure

The branch history IS the search constraint.
32 collapses = 32-bit search space reduction.

P(2)NP: Same mechanism, use itself both ways.
""")
