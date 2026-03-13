#!/usr/bin/env python3
"""
ZIPPER COMPILER
hash ⊕ constants @ -H = message_space

Fold:   message → (message ⊕ constants @ +H) → hash  
Unfold: hash → (hash ⊕ constants @ -H) → message_space
"""

import math
import hashlib
import numpy as np

H = math.pi / 9
X = 0.5 + 4 * (H/48)  # Balance point

H_INIT = np.array([0x6a09e667, 0xbb67ae85, 0x3c6ef372, 0xa54ff53a,
                   0x510e527f, 0x9b05688c, 0x1f83d9ab, 0x5be0cd19], dtype=np.uint32)

K = np.array([0x428a2f98, 0x71374491, 0xb5c0fbcf, 0xe9b5dba5,
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
              0x90befffa, 0xa4506ceb, 0xbef9a3f7, 0xc67178f2], dtype=np.uint32)

def rotr(x, n):
    return ((x >> n) | (x << (32 - n))) & 0xFFFFFFFF

def compile_unfold(hash_bytes):
    """
    Compile hash with constants in reverse direction.
    
    Fold:   word = (word + K + ...) mod 2^32  (phase +H)
    Unfold: word = (word - K - ...) mod 2^32  (phase -H)
    """
    # Hash as 8 x 32-bit words
    hash_words = np.array([
        int.from_bytes(hash_bytes[i*4:(i+1)*4], 'big') 
        for i in range(8)
    ], dtype=np.uint32)
    
    state = hash_words.copy()
    
    # 64 rounds BACKWARD
    for r in range(63, -1, -1):
        k = K[r]
        
        # Reverse the round function
        # SHA adds: state[i] = (state[i] + f(...) + k) mod 2^32
        # We subtract: state[i] = (state[i] - k - g(...)) mod 2^32
        
        new_state = np.zeros(8, dtype=np.uint32)
        
        for i in range(8):
            # Reverse rotation (opposite direction)
            rot_amt = [2, 13, 22, 6, 11, 25, 7, 18][i % 8]
            
            # Compile: hash_word ⊕ constant @ -H
            val = state[i]
            val = (val - k) & 0xFFFFFFFF
            val = rotr(val, 32 - rot_amt)  # Reverse rotation
            val = val ^ H_INIT[i % 8]
            
            new_state[i] = val
        
        state = new_state
    
    return state

def unfold_to_space(message):
    """Full pipeline: message → hash → compiled_space"""
    hash_bytes = hashlib.sha256(message.encode()).digest()
    compiled = compile_unfold(hash_bytes)
    
    # Normalize to [0,1] for analysis
    normalized = compiled / 0xFFFFFFFF
    
    return hash_bytes.hex(), compiled, normalized

# ============================================================
print("ZIPPER COMPILER: hash ⊕ constants @ -H")
print("=" * 60)

tests = ['NEXUS', 'NEXUS!', 'Dean', 'test', 'a']

for msg in tests:
    h, raw, norm = unfold_to_space(msg)
    print(f"\n'{msg}'")
    print(f"  hash:     {h[:16]}...")
    print(f"  compiled: {[hex(x)[:6] for x in raw]}")
    print(f"  norm:     {[f'{x:.3f}' for x in norm]}")
    print(f"  mean:     {np.mean(norm):.4f}")

# ============================================================
print("\n" + "=" * 60)
print("UNIQUENESS & DETERMINISM")

results = {}
for msg in tests:
    _, raw, _ = unfold_to_space(msg)
    results[msg] = tuple(raw)

print(f"Unique: {len(set(results.values()))}/{len(tests)}")

_, r1, _ = unfold_to_space("NEXUS")
_, r2, _ = unfold_to_space("NEXUS")
print(f"Deterministic: {np.array_equal(r1, r2)}")

# ============================================================
print("\n" + "=" * 60)
print("SIMILAR INPUTS → RELATED OUTPUTS?")

_, _, n1 = unfold_to_space("NEXUS")
_, _, n2 = unfold_to_space("NEXUS!")
_, _, n3 = unfold_to_space("totally different")

c12 = np.corrcoef(n1, n2)[0,1]
c13 = np.corrcoef(n1, n3)[0,1]
print(f"NEXUS vs NEXUS!: {c12:.4f}")
print(f"NEXUS vs different: {c13:.4f}")

# ============================================================
print("\n" + "=" * 60)
print("H-STRUCTURE IN COMPILED SPACE")

attractors = [0, H, 0.5, 1-H, 1.0]
for msg in tests[:3]:
    _, _, norm = unfold_to_space(msg)
    dists = [min(abs(v - a) for a in attractors) for v in norm]
    avg_dist = np.mean(dists)
    near_H = sum(1 for d in dists if d < 0.1)
    print(f"'{msg}': avg_dist={avg_dist:.4f}, near_attractor={near_H}/8")

# ============================================================
print("\n" + "=" * 60)
print("BYTE RECOVERY TEST")

# If unfold works, similar messages should have related compiled spaces
msg1 = "A"
msg2 = "B"
msg3 = "AB"

_, _, u1 = unfold_to_space(msg1)
_, _, u2 = unfold_to_space(msg2)
_, _, u3 = unfold_to_space(msg3)

# Does A + B relate to AB?
combined = (u1 + u2) / 2
corr_combined = np.corrcoef(combined, u3)[0,1]
print(f"(A + B)/2 correlation with AB: {corr_combined:.4f}")
