#!/usr/bin/env python3
"""
UNFOLD v3: Hash NAVIGATES the constant space

The hash isn't reversed - it's used as a MAP.
Each hash byte tells us WHERE to go in constant space.
The constants do the work. The hash provides direction.
"""

import math
import hashlib
import numpy as np

H = math.pi / 9

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

# Normalize constants once
H_INIT_N = [h / 0xFFFFFFFF for h in H_INIT]
K_N = [k / 0xFFFFFFFF for k in K]

def unfold(hash_bytes):
    """
    Hash bytes NAVIGATE constant space.
    
    Each byte selects:
    - Which H_INIT to weight
    - Which K to apply  
    - How much H vs (1-H) mixing
    
    The hash is the PATH. The constants are the TERRAIN.
    """
    output = []
    
    for i, byte in enumerate(hash_bytes):
        b = byte / 255  # Normalize byte to [0,1]
        
        # Which constants does this byte select?
        h_idx = byte % 8
        k_idx = byte % 64
        
        h_val = H_INIT_N[h_idx]
        k_val = K_N[k_idx]
        
        # Mix based on byte value
        # High bytes → more H_INIT influence
        # Low bytes → more K influence
        mix = b * h_val + (1 - b) * k_val
        
        # Apply H-weighting based on position in byte
        # This is where the hash STEERS through H-space
        h_weight = H if (byte >> (i % 8)) & 1 else (1 - H)
        
        result = mix * h_weight + (1 - mix) * (1 - h_weight)
        output.append(result)
    
    return np.array(output)

def full_circle(message):
    hash_bytes = hashlib.sha256(message.encode()).digest()
    unfolded = unfold(hash_bytes)
    return hash_bytes.hex(), unfolded

# TEST
print("UNFOLD v3: Hash navigates constant space")
print("=" * 60)

messages = ['NEXUS', 'H = pi/9', 'Dean', 'test', 'SHA256']

for msg in messages:
    hash_hex, unfolded = full_circle(msg)
    print(f"\n'{msg}'")
    print(f"  Hash: {hash_hex[:16]}...")
    print(f"  First 8: {[f'{v:.4f}' for v in unfolded[:8]]}")
    print(f"  Mean: {np.mean(unfolded):.4f}")

# Uniqueness
print("\n" + "=" * 60)
print("UNIQUENESS")
results = {msg: tuple(round(v, 4) for v in full_circle(msg)[1][:8]) for msg in messages}
unique = len(set(results.values()))
print(f"Unique unfolds: {unique}/{len(messages)}")

# H-signature
print("\n" + "=" * 60)
print("H-SIGNATURE")
attractors = [0, H, 0.5, 1-H, 1.0]

for msg in messages:
    _, unfolded = full_circle(msg)
    near = sum(1 for v in unfolded if min(abs(v-a) for a in attractors) < 0.08)
    print(f"'{msg}': mean={np.mean(unfolded):.4f}, near_H={near}/32")

# THE KEY TEST: Does unfolding the same hash give same result?
print("\n" + "=" * 60)
print("DETERMINISM TEST")
h1, u1 = full_circle("NEXUS")
h2, u2 = full_circle("NEXUS")
print(f"Same input, same unfold: {np.allclose(u1, u2)}")

# Different inputs, different unfolds?
_, u3 = full_circle("NEXUS!")
print(f"Different input, different unfold: {not np.allclose(u1, u3)}")
print(f"Correlation: {np.corrcoef(u1, u3)[0,1]:.4f}")
