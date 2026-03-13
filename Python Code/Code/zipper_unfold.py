#!/usr/bin/env python3
"""
ZIPPER UNFOLD
Hash = one wave
Constants = other wave
Out of sync by H on fold
Resync on unfold
"""

import math
import hashlib
import numpy as np

H = math.pi / 9  # 0.349066

# Constants as wave 1
H_INIT = np.array([0x6a09e667, 0xbb67ae85, 0x3c6ef372, 0xa54ff53a,
                   0x510e527f, 0x9b05688c, 0x1f83d9ab, 0x5be0cd19]) / 0xFFFFFFFF

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
              0x90befffa, 0xa4506ceb, 0xbef9a3f7, 0xc67178f2]) / 0xFFFFFFFF

def zipper_unfold(hash_bytes):
    """
    Two waves, out of phase by H.
    Zipper them back together.
    """
    # Hash as wave 2 (32 bytes = 32 teeth)
    hash_wave = np.array([b / 255 for b in hash_bytes])
    
    # Phase shift = H (this is what folding did)
    phase_shift = H * 2 * np.pi
    
    output = np.zeros(32)
    
    for i in range(32):
        # Hash tooth
        h_tooth = hash_wave[i]
        
        # Constant tooth (interleaved H_INIT and K)
        if i < 8:
            c_tooth = H_INIT[i]
        else:
            c_tooth = K[i % 64]
        
        # Current phase of hash (folded = shifted by H)
        hash_phase = h_tooth * 2 * np.pi
        
        # Constant phase
        const_phase = c_tooth * 2 * np.pi
        
        # RESYNC: subtract the H shift that folding added
        resynced_phase = hash_phase - phase_shift * (i / 32)
        
        # Zipper: combine when in phase
        phase_diff = abs(resynced_phase - const_phase)
        coherence = np.cos(phase_diff)
        
        # Output = coherent combination
        output[i] = (h_tooth * coherence + c_tooth * (1 - abs(coherence))) % 1.0
    
    return output

def unfold(message):
    hash_bytes = hashlib.sha256(message.encode()).digest()
    return hash_bytes.hex(), zipper_unfold(hash_bytes)

# Run
print("ZIPPER UNFOLD")
print("=" * 50)

tests = ['NEXUS', 'H = pi/9', 'Dean', 'test', 'hello']

for msg in tests:
    h, u = unfold(msg)
    print(f"\n{msg}")
    print(f"  hash: {h[:16]}")
    print(f"  unf:  {[f'{x:.3f}' for x in u[:8]]}")
    print(f"  mean: {np.mean(u):.4f}")

# Verify uniqueness
print("\n" + "=" * 50)
sigs = [tuple(round(x,3) for x in unfold(m)[1]) for m in tests]
print(f"Unique: {len(set(sigs))}/{len(tests)}")

# Verify determinism
_, u1 = unfold("NEXUS")
_, u2 = unfold("NEXUS")
print(f"Deterministic: {np.allclose(u1, u2)}")

# H distribution
print("\n" + "=" * 50)
print("H-ATTRACTOR DISTRIBUTION")
attractors = [0, H, 0.5, 1-H, 1.0]
for msg in tests[:3]:
    _, u = unfold(msg)
    counts = {round(a,2): 0 for a in attractors}
    for v in u:
        nearest = min(attractors, key=lambda a: abs(v-a))
        counts[round(nearest,2)] += 1
    print(f"{msg}: {counts}")
