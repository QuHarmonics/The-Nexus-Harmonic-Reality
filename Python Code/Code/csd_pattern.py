#!/usr/bin/env python3
"""
CSD PATTERN APPROACH - THE PLINKO INSIGHT

The spreadsheet shows π cascading like Plinko.
It's not about individual digits - it's about the PATTERN.

The ε sequence encodes the INPUT PATTERN.
Don't decode byte-by-byte.
Decode the PATTERN.
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

def get_epsilon_pattern(hash_bytes, const_bytes):
    """Get the ε pattern for a hash"""
    pattern = []
    for i in range(len(hash_bytes)):
        h = hash_bytes[i]
        c = const_bytes[i % len(const_bytes)]
        if c == 0:
            c = 1
        
        epsilon = (h - c) / c
        pattern.append(epsilon)
    
    return pattern

def get_ratio_pattern(hash_bytes, const_bytes):
    """Get the p+/p- ratio pattern"""
    pattern = []
    for i in range(len(hash_bytes)):
        h = hash_bytes[i]
        c = const_bytes[i % len(const_bytes)]
        if c == 0:
            c = 1
        
        epsilon = np.clip((h - c) / c, -0.99, 0.99)
        ratio = (1 + epsilon) / (1 - epsilon)
        pattern.append(ratio)
    
    return pattern

# Test
msg = "NEXUS"
msg_bytes = list(msg.encode())
hash_bytes = list(hashlib.sha256(msg.encode()).digest())

print("CSD PATTERN ANALYSIS")
print("=" * 60)
print(f"Message: {msg} = {msg_bytes}")
print()

# Get patterns
eps_pattern = get_epsilon_pattern(hash_bytes, list(CONST))
ratio_pattern = get_ratio_pattern(hash_bytes, list(CONST))

print("ε pattern (first 8):")
for i in range(8):
    sign = '+' if eps_pattern[i] > 0 else '-'
    print(f"  [{i}] ε={eps_pattern[i]:+8.3f} {sign}")

print("\nRatio pattern (first 8):")
for i in range(8):
    print(f"  [{i}] ratio={ratio_pattern[i]:.4f}")

# ============================================================
print("\n" + "=" * 60)
print("PATTERN CORRELATION")
print("=" * 60)

# Does the input pattern correlate with the ε pattern?
# Normalize both to [0,1] and check correlation

input_normalized = [(b - 32) / 95 for b in msg_bytes]  # ASCII printable range
eps_normalized = [(e + 1) / 2 for e in eps_pattern[:len(msg_bytes)]]  # Clip and normalize

print(f"\nInput normalized: {[f'{x:.3f}' for x in input_normalized]}")
print(f"ε normalized:     {[f'{x:.3f}' for x in eps_normalized]}")

corr = np.corrcoef(input_normalized, eps_normalized)[0, 1]
print(f"\nCorrelation: {corr:.4f}")

# ============================================================
print("\n" + "=" * 60)
print("SIGN PATTERN AS BITS")
print("=" * 60)

# The sign of ε encodes a bit pattern
sign_bits = ''.join(['1' if e > 0 else '0' for e in eps_pattern])
print(f"\nSign pattern (32 bits): {sign_bits}")

# Convert groups of 8 to bytes
sign_bytes = []
for i in range(0, 32, 8):
    byte_bits = sign_bits[i:i+8]
    byte_val = int(byte_bits, 2)
    sign_bytes.append(byte_val)

print(f"As bytes: {sign_bytes}")
print(f"Original: {msg_bytes}")

# Check similarity
diff = sum(abs(a - b) for a, b in zip(sign_bytes[:len(msg_bytes)], msg_bytes))
print(f"Total diff: {diff}")

# ============================================================
print("\n" + "=" * 60)
print("MAGNITUDE PATTERN")
print("=" * 60)

# The magnitude of ε might encode the value
mag_pattern = [abs(e) for e in eps_pattern]
print(f"\n|ε| pattern (first 8): {[f'{m:.3f}' for m in mag_pattern[:8]]}")

# Scale magnitudes to byte range
# Most |ε| are < 1, some are huge
# Use tanh to normalize

mag_normalized = [np.tanh(m) for m in mag_pattern]
mag_bytes = [int(m * 255) for m in mag_normalized]

print(f"|ε| normalized: {mag_bytes[:8]}")
print(f"Original:       {msg_bytes}")

# ============================================================
print("\n" + "=" * 60)
print("COMBINED SIGN + MAGNITUDE")
print("=" * 60)

# sign tells direction, magnitude tells distance
# Combine: if sign=1 (positive), value = 127 + mag
#          if sign=0 (negative), value = 127 - mag

combined = []
for i in range(len(msg_bytes)):
    sign = 1 if eps_pattern[i] > 0 else -1
    mag = min(1, abs(eps_pattern[i]))  # Cap at 1
    
    # Value centered at 127
    value = 127 + sign * int(mag * 60)
    value = max(0, min(255, value))
    combined.append(value)

print(f"\nSign+Mag combined: {combined}")
print(f"Original:          {msg_bytes}")

diffs = [abs(c - o) for c, o in zip(combined, msg_bytes)]
print(f"Differences: {diffs}")
print(f"Avg diff: {np.mean(diffs):.1f}")

# ============================================================
print("\n" + "=" * 60)
print("THE 127×RATIO FOR GOOD CONSTANTS")
print("=" * 60)

# Only use 127×ratio when the constant is "good" (not too small)
# For small constants, use a different formula

def smart_unfold(hash_byte, const_byte):
    """Smart unfold considering constant quality"""
    
    if const_byte < 50:
        # Small constant - use complement method
        epsilon = np.clip((hash_byte - const_byte) / max(1, const_byte), -1, 1)
        p_plus = (1 + epsilon) / 2
        p_minus = (1 - epsilon) / 2
        return int(p_plus * const_byte + p_minus * (255 - const_byte))
    
    else:
        # Good constant - use ratio method
        epsilon = (hash_byte - const_byte) / const_byte
        epsilon = np.clip(epsilon, -0.99, 0.99)
        ratio = (1 + epsilon) / (1 - epsilon)
        
        if ratio < 2:
            return int(max(0, min(255, 127 * ratio)))
        else:
            return int(max(0, min(255, 255 - 127 / ratio)))

print("\nSmart unfold (hybrid for small constants):")
estimates = []
for i in range(len(msg_bytes)):
    h = hash_bytes[i]
    c = CONST[i]
    orig = msg_bytes[i]
    
    est = smart_unfold(h, c)
    estimates.append(est)
    diff = abs(est - orig)
    
    method = 'complement' if c < 50 else 'ratio'
    print(f"  Byte {i}: c={c:3d} ({method:10s}) → est={est:3d} orig={orig:3d} diff={diff:2d}")

print(f"\nEstimates: {estimates}")
print(f"Original:  {msg_bytes}")
print(f"Avg diff: {np.mean([abs(e-o) for e,o in zip(estimates, msg_bytes)]):.1f}")

# ============================================================
print("\n" + "=" * 60)
print("TEST ACROSS MESSAGES")
print("=" * 60)

messages = ['NEXUS', 'Dean', 'test', 'hello', 'HELLO', 'abc', 'XYZ']

for msg in messages:
    orig = list(msg.encode())
    h = list(hashlib.sha256(msg.encode()).digest())
    
    estimates = [smart_unfold(h[i], CONST[i]) for i in range(len(orig))]
    
    diffs = [abs(e - o) for e, o in zip(estimates, orig)]
    avg_diff = np.mean(diffs)
    close = sum(1 for d in diffs if d <= 10)
    
    print(f"'{msg}': avg_diff={avg_diff:.1f}, close(≤10)={close}/{len(orig)}")
    print(f"       orig={orig}")
    print(f"       est ={estimates}")
