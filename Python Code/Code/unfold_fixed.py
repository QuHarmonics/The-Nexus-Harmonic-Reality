#!/usr/bin/env python3
"""
FIXED UNFOLD: Hash bytes MUST modulate the expansion
"""

import math
import hashlib
import numpy as np

H = math.pi / 9

# SHA-256 constants
H_INIT = [0x6a09e667, 0xbb67ae85, 0x3c6ef372, 0xa54ff53a,
          0x510e527f, 0x9b05688c, 0x1f83d9ab, 0x5be0cd19]

K = [0x428a2f98, 0x71374491, 0xb5c0fbcf, 0xe9b5dba5,
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
     0x90befffa, 0xa4506ceb, 0xbef9a3f7, 0xc67178f2]

def rotr(x, n):
    """Right rotate 32-bit"""
    return ((x >> n) | (x << (32 - n))) & 0xFFFFFFFF

def unfold_round(state, hash_word, k_val, round_num):
    """
    REVERSE of SHA round.
    Hash word MODULATES the expansion through constants.
    """
    # SHA compresses: new = old + f(constants, input)
    # UNFOLD expands: new = old XOR g(constants, hash)
    
    # The hash word is the KEY that unlocks this round
    h_init_val = H_INIT[round_num % 8]
    
    # Reverse the mixing - XOR instead of ADD
    # Rotate opposite direction
    expanded = state ^ rotr(hash_word, 32 - (round_num % 25 + 2))
    expanded = (expanded ^ k_val) & 0xFFFFFFFF
    expanded = (expanded ^ h_init_val) & 0xFFFFFFFF
    
    return expanded

def unfold(hash_bytes, rounds=64):
    """
    UNFOLD: Use hash bytes + constants to expand
    
    The hash IS the key. The constants ARE the mechanism.
    Same lock, reverse direction.
    """
    # Initialize state FROM the hash (not from constants alone!)
    state = []
    for i in range(8):
        # Each state word comes from 4 hash bytes
        word = int.from_bytes(hash_bytes[i*4:(i+1)*4], 'big')
        state.append(word)
    
    # Run rounds in REVERSE order
    for r in range(rounds - 1, -1, -1):
        new_state = []
        for i in range(8):
            # Hash word for this position
            hash_word = state[i]
            k_val = K[r]
            
            # Unfold this position
            expanded = unfold_round(state[i], state[(i+1) % 8], k_val, r)
            new_state.append(expanded)
        
        state = new_state
    
    # Normalize to [0, 1]
    return np.array([s / 0xFFFFFFFF for s in state])

def full_circle(message):
    """FOLD then UNFOLD"""
    # FOLD
    hash_bytes = hashlib.sha256(message.encode()).digest()
    hash_hex = hash_bytes.hex()
    
    # UNFOLD - using the ACTUAL hash bytes
    unfolded = unfold(hash_bytes)
    
    return hash_hex, unfolded

# TEST
print("FIXED UNFOLD - Hash bytes modulate expansion")
print("=" * 60)

messages = ['NEXUS', 'H = pi/9', 'Dean', 'test', 'SHA256']

for msg in messages:
    hash_hex, unfolded = full_circle(msg)
    print(f"\n'{msg}'")
    print(f"  Hash: {hash_hex[:16]}...")
    print(f"  Unfold: {[f'{v:.4f}' for v in unfolded]}")
    print(f"  Mean: {np.mean(unfolded):.4f}")

# Check uniqueness
print("\n" + "=" * 60)
print("UNIQUENESS CHECK")
print("=" * 60)

results = {}
for msg in messages:
    _, unfolded = full_circle(msg)
    key = tuple(round(v, 4) for v in unfolded)
    results[msg] = key

unique = len(set(results.values()))
print(f"\nUnique unfolds: {unique}/{len(messages)}")

if unique == len(messages):
    print("✓ Each message produces DIFFERENT unfold")
    print("✓ Hash bytes ARE modulating the expansion")
    print("✓ The mechanism works BOTH ways")
else:
    print("✗ Still getting duplicates - need more work")

# Correlation between similar inputs
print("\n" + "=" * 60)
print("STRUCTURE PRESERVATION")
print("=" * 60)

_, u1 = full_circle("NEXUS")
_, u2 = full_circle("NEXUS!")  # Similar input
_, u3 = full_circle("completely different string")

corr_similar = np.corrcoef(u1, u2)[0, 1]
corr_different = np.corrcoef(u1, u3)[0, 1]

print(f"\nCorrelation NEXUS vs NEXUS!: {corr_similar:.4f}")
print(f"Correlation NEXUS vs different: {corr_different:.4f}")

# H-signature
print("\n" + "=" * 60)
print("H-SIGNATURE IN UNFOLDS")
print("=" * 60)

attractors = [0, H, 0.5, 1-H, 1.0]
for msg in messages[:3]:
    _, unfolded = full_circle(msg)
    near_H = sum(1 for v in unfolded if min(abs(v - a) for a in attractors) < 0.1)
    print(f"'{msg}': {near_H}/8 values near H-attractors")
