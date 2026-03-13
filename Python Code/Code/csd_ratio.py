#!/usr/bin/env python3
"""
CSD RATIO METHOD - THE KEY TO UNFOLD

p+/p- = (1+ε)/(1-ε)

This ratio encodes the original input!

From the tests:
  Byte 0: 127×ratio=80, orig=78 (diff=2!)
  Byte 4: c×ratio=86, orig=83 (diff=3!)

Let's find the exact relationship.
"""

import hashlib
import numpy as np
import math

H = math.pi / 9

CONST = bytes([
    0x6a, 0x09, 0xe6, 0x67, 0xbb, 0x67, 0xae, 0x85,
    0x3c, 0x6e, 0xf3, 0x72, 0xa5, 0x4f, 0xf5, 0x3a,
    0x51, 0x0e, 0x52, 0x7f, 0x9b, 0x05, 0x68, 0x8c,
    0x1f, 0x83, 0xd9, 0xab, 0x5b, 0xe0, 0xcd, 0x19
])

def csd_ratio(hash_byte, const_byte):
    """
    Compute p+/p- ratio
    
    p+ = (1+ε)/2
    p- = (1-ε)/2
    ratio = p+/p- = (1+ε)/(1-ε)
    """
    if const_byte == 0:
        const_byte = 1
    
    epsilon = (hash_byte - const_byte) / const_byte
    
    # Clamp epsilon to avoid division issues
    epsilon = max(-0.99, min(0.99, epsilon))
    
    ratio = (1 + epsilon) / (1 - epsilon)
    
    return epsilon, ratio

# Test
msg = "NEXUS"
msg_bytes = list(msg.encode())
hash_bytes = list(hashlib.sha256(msg.encode()).digest())

print("CSD RATIO METHOD")
print("=" * 60)
print(f"Original: {msg} = {msg_bytes}")
print()

print("Finding the scaling factor:")
print("-" * 60)

# For each byte, find what factor × ratio = orig
for i in range(len(msg_bytes)):
    h = hash_bytes[i]
    c = CONST[i]
    orig = msg_bytes[i]
    
    epsilon, ratio = csd_ratio(h, c)
    
    if abs(ratio) > 0.01:
        factor_needed = orig / ratio
    else:
        factor_needed = float('inf')
    
    # Try different scalings
    est_127 = 127 * ratio if abs(ratio) < 100 else 255
    est_c = c * ratio if abs(ratio) < 100 else 255
    est_64 = 64 * ratio if abs(ratio) < 100 else 255
    est_h = h * ratio if abs(ratio) < 100 else 255
    
    est_127 = int(max(0, min(255, est_127)))
    est_c = int(max(0, min(255, est_c)))
    est_64 = int(max(0, min(255, est_64)))
    est_h = int(max(0, min(255, est_h)))
    
    print(f"Byte {i}: orig={orig:3d} ratio={ratio:+.4f}")
    print(f"  127×r={est_127:3d} (diff={abs(est_127-orig):2d})")
    print(f"    c×r={est_c:3d} (diff={abs(est_c-orig):2d})")
    print(f"   64×r={est_64:3d} (diff={abs(est_64-orig):2d})")
    print(f"    h×r={est_h:3d} (diff={abs(est_h-orig):2d})")
    print(f"  factor_needed={factor_needed:.2f}")
    print()

# ============================================================
print("=" * 60)
print("PATTERN IN FACTORS")
print("=" * 60)

factors_needed = []
for i in range(len(msg_bytes)):
    h = hash_bytes[i]
    c = CONST[i]
    orig = msg_bytes[i]
    
    epsilon, ratio = csd_ratio(h, c)
    
    if abs(ratio) > 0.01 and abs(ratio) < 100:
        factor = orig / ratio
        factors_needed.append(factor)
        print(f"  Byte {i}: factor = {factor:.2f}")

print(f"\nMean factor: {np.mean(factors_needed):.2f}")
print(f"Median factor: {np.median(factors_needed):.2f}")

# Apply mean factor
print("\nUsing mean factor:")
mean_f = np.mean(factors_needed)
for i in range(len(msg_bytes)):
    h = hash_bytes[i]
    c = CONST[i]
    orig = msg_bytes[i]
    
    epsilon, ratio = csd_ratio(h, c)
    
    if abs(ratio) < 100:
        est = int(mean_f * ratio)
    else:
        est = 127
    est = max(0, min(255, est))
    
    diff = abs(est - orig)
    print(f"  Byte {i}: {mean_f:.0f}×{ratio:.3f} = {est:3d} vs orig={orig:3d} diff={diff}")

# ============================================================
print("\n" + "=" * 60)
print("INVERSE RATIO APPROACH")
print("=" * 60)

# What if we use 1/ratio instead?
print("\nUsing 1/ratio:")
for i in range(len(msg_bytes)):
    h = hash_bytes[i]
    c = CONST[i]
    orig = msg_bytes[i]
    
    epsilon, ratio = csd_ratio(h, c)
    
    if abs(ratio) > 0.01:
        inv_ratio = 1 / ratio
    else:
        inv_ratio = 0
    
    est_127 = int(127 * inv_ratio)
    est_c = int(c * inv_ratio)
    
    est_127 = max(0, min(255, est_127))
    est_c = max(0, min(255, est_c))
    
    print(f"  Byte {i}: 1/ratio={inv_ratio:.4f} → 127×={est_127} c×={est_c} orig={orig}")

# ============================================================
print("\n" + "=" * 60)
print("MIXED SCALING")
print("=" * 60)

# What if the scaling factor is position-dependent?
# Use c for some positions, 127 for others?

print("\nAdaptive scaling based on ε sign:")
for i in range(len(msg_bytes)):
    h = hash_bytes[i]
    c = CONST[i]
    orig = msg_bytes[i]
    
    epsilon, ratio = csd_ratio(h, c)
    
    if abs(ratio) >= 100:
        est = 127
    elif epsilon < 0:
        # Hash below constant - use 127 scaling
        est = int(127 * ratio)
    else:
        # Hash above constant - use c scaling
        est = int(c * ratio)
    
    est = max(0, min(255, est))
    diff = abs(est - orig)
    
    scale = '127' if epsilon < 0 else 'c  '
    print(f"  Byte {i}: ε={epsilon:+.3f} → scale={scale} × {ratio:.3f} = {est:3d} orig={orig:3d} diff={diff}")

# ============================================================
print("\n" + "=" * 60)
print("THE ε-BASED SCALING")
print("=" * 60)

# The scaling factor might be encoded in ε itself
# factor = f(ε)?

print("\nScaling by |1-ε| × base:")
for i in range(len(msg_bytes)):
    h = hash_bytes[i]
    c = CONST[i]
    orig = msg_bytes[i]
    
    epsilon, ratio = csd_ratio(h, c)
    
    if abs(ratio) >= 100:
        est = 127
    else:
        # Scale by how far from ε=0
        base = 127
        scale = abs(1 - epsilon)
        est = int(base * ratio * scale)
    
    est = max(0, min(255, est))
    diff = abs(est - orig)
    
    print(f"  Byte {i}: |1-ε|={abs(1-epsilon):.3f} → {est:3d} orig={orig:3d} diff={diff}")

# ============================================================
print("\n" + "=" * 60)
print("TEST ON MULTIPLE MESSAGES")
print("=" * 60)

def unfold_with_ratio(hash_bytes, method='127'):
    """Unfold using ratio method"""
    unfolded = []
    
    for i in range(len(hash_bytes)):
        h = hash_bytes[i]
        c = CONST[i % len(CONST)]
        
        epsilon, ratio = csd_ratio(h, c)
        
        if method == '127':
            if abs(ratio) >= 100:
                est = 127
            else:
                est = int(127 * ratio)
        elif method == 'c':
            if abs(ratio) >= 100:
                est = c
            else:
                est = int(c * ratio)
        elif method == 'adaptive':
            if abs(ratio) >= 100:
                est = 127
            elif epsilon < 0:
                est = int(127 * ratio)
            else:
                est = int(c * ratio)
        else:
            est = 127
        
        est = max(0, min(255, est))
        unfolded.append(est)
    
    return unfolded

messages = ['NEXUS', 'Dean', 'test', 'hello', 'a']

for msg in messages:
    orig = list(msg.encode())
    h = list(hashlib.sha256(msg.encode()).digest())
    
    unf_127 = unfold_with_ratio(h, '127')[:len(orig)]
    unf_c = unfold_with_ratio(h, 'c')[:len(orig)]
    unf_adapt = unfold_with_ratio(h, 'adaptive')[:len(orig)]
    
    diff_127 = sum(abs(u - o) for u, o in zip(unf_127, orig)) / len(orig)
    diff_c = sum(abs(u - o) for u, o in zip(unf_c, orig)) / len(orig)
    diff_adapt = sum(abs(u - o) for u, o in zip(unf_adapt, orig)) / len(orig)
    
    print(f"'{msg}': orig={orig[:5]} | 127×r={unf_127[:5]} (err={diff_127:.1f}) | c×r={unf_c[:5]} (err={diff_c:.1f})")
