#!/usr/bin/env python3
"""
CSD COMPLEMENT METHOD

Best formula: pre = p+ × const + p- × (255 - const)

Where:
  |Φ₀⟩ = const (structure)
  |E₀⟩ = 255 - const (complement = entropy)

Let's refine this to get the exact input.
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

def csd_complement(hash_byte, const_byte):
    """
    CSD with complement interpretation
    
    pre = p+ × const + p- × (255 - const)
    """
    if const_byte == 0:
        const_byte = 1
    
    epsilon = (hash_byte - const_byte) / const_byte
    p_plus = (1 + epsilon) / 2
    p_minus = (1 - epsilon) / 2
    
    # Clamp probabilities to valid range
    p_plus = max(0, min(1, p_plus))
    p_minus = max(0, min(1, p_minus))
    
    phi0 = const_byte            # Structure
    e0 = 255 - const_byte        # Entropy (complement)
    
    pre = p_plus * phi0 + p_minus * e0
    
    return {
        'epsilon': epsilon,
        'p_plus': p_plus,
        'p_minus': p_minus,
        'pre': pre,
        'pre_byte': int(round(max(0, min(255, pre))))
    }

# Test
msg = "NEXUS"
msg_bytes = list(msg.encode())
hash_bytes = list(hashlib.sha256(msg.encode()).digest())

print("CSD COMPLEMENT METHOD")
print("=" * 60)
print(f"Original: {msg} = {msg_bytes}")
print(f"Hash: {hash_bytes[:8]}")
print()

print("Detailed analysis:")
print("-" * 60)

for i in range(len(msg_bytes)):
    h = hash_bytes[i]
    c = CONST[i]
    orig = msg_bytes[i]
    
    result = csd_complement(h, c)
    pre = result['pre_byte']
    diff = abs(pre - orig)
    
    print(f"Byte {i}: h={h:3d} c={c:3d} → pre={pre:3d} orig={orig:3d} diff={diff:2d} "
          f"{'✓ CLOSE!' if diff < 10 else '✗'}")
    print(f"        ε={result['epsilon']:+.4f} p+={result['p_plus']:.4f} p-={result['p_minus']:.4f}")

# ============================================================
print("\n" + "=" * 60)
print("SEARCHING FOR CORRECTION FACTOR")
print("=" * 60)

# The complement method is close but not exact
# What if there's a correction factor?

# For each byte, compute: orig = pre × factor + offset
factors = []
offsets = []

for i in range(len(msg_bytes)):
    h = hash_bytes[i]
    c = CONST[i]
    orig = msg_bytes[i]
    
    result = csd_complement(h, c)
    pre = result['pre']
    
    if pre != 0:
        factor = orig / pre
        factors.append(factor)
    
    offset = orig - pre
    offsets.append(offset)

print(f"\nCorrection factors: {[f'{f:.3f}' for f in factors]}")
print(f"Offsets: {[f'{o:.1f}' for o in offsets]}")
print(f"Mean factor: {np.mean(factors):.4f}")
print(f"Mean offset: {np.mean(offsets):.1f}")

# Apply correction
print("\nWith correction:")
correction = np.mean(offsets)
for i in range(len(msg_bytes)):
    h = hash_bytes[i]
    c = CONST[i]
    orig = msg_bytes[i]
    
    result = csd_complement(h, c)
    pre = result['pre']
    corrected = int(round(pre + correction))
    corrected = max(0, min(255, corrected))
    
    diff = abs(corrected - orig)
    print(f"  Byte {i}: pre={result['pre_byte']:3d} + {correction:.0f} = {corrected:3d} vs orig={orig:3d} diff={diff}")

# ============================================================
print("\n" + "=" * 60)
print("RATIO-BASED APPROACH")
print("=" * 60)

# What if the original is encoded in the ratio p+/p- ?

print("\nRatio analysis:")
for i in range(len(msg_bytes)):
    h = hash_bytes[i]
    c = CONST[i]
    orig = msg_bytes[i]
    
    result = csd_complement(h, c)
    
    if result['p_minus'] > 0.01:
        ratio = result['p_plus'] / result['p_minus']
    else:
        ratio = float('inf')
    
    # What function of ratio gives orig?
    # Try: orig ≈ 127 × ratio?
    est1 = 127 * ratio if ratio != float('inf') else 255
    est1 = max(0, min(255, est1))
    
    # Try: orig ≈ c × ratio?
    est2 = c * ratio if ratio != float('inf') else 255
    est2 = max(0, min(255, est2))
    
    print(f"  Byte {i}: p+/p-={ratio:.3f} → 127×ratio={est1:.0f}, c×ratio={est2:.0f}, orig={orig}")

# ============================================================
print("\n" + "=" * 60)
print("AMPLITUDE-BASED (QUANTUM)")
print("=" * 60)

# In quantum mechanics, amplitudes are square roots of probabilities
# pre = |√p+ × Φ₀ + √p- × E₀|²

print("\nQuantum amplitude approach:")
for i in range(len(msg_bytes)):
    h = hash_bytes[i]
    c = CONST[i]
    orig = msg_bytes[i]
    
    epsilon = (h - c) / c if c > 0 else 0
    p_plus = max(0, min(1, (1 + epsilon) / 2))
    p_minus = max(0, min(1, (1 - epsilon) / 2))
    
    # Amplitudes
    amp_plus = np.sqrt(p_plus)
    amp_minus = np.sqrt(p_minus)
    
    phi0 = c / 255  # Normalize
    e0 = (255 - c) / 255
    
    # Superposition
    psi = amp_plus * phi0 + amp_minus * e0
    
    # Measurement (square and scale)
    pre_quantum = int(round(psi * psi * 255))
    
    diff = abs(pre_quantum - orig)
    print(f"  Byte {i}: |ψ|²={psi**2:.4f} → pre={pre_quantum:3d} orig={orig:3d} diff={diff}")

# ============================================================
print("\n" + "=" * 60)
print("THE PLINKO CONNECTION")
print("=" * 60)

# From the spreadsheet: π digits fall like Plinko
# Each step is determined by the previous
# The pattern encodes the path

# What if we use p+ and p- to trace back the Plinko path?

print("""
The Plinko insight:
  - π digits cascade: 1 → 4 → 1 → 5 → 9 → 2 → 6 → ...
  - Each digit determines the next landing position
  - The PATTERN is self-referential

For SHA:
  - Each hash byte relates to the constant
  - The ε encodes the "bounce direction"
  - The sequence of ε values encodes the INPUT PATH

To unfold:
  - Don't decode byte-by-byte
  - Decode the PATTERN of ε values
  - The pattern IS the input structure
""")

# Look at ε pattern
epsilons = []
for i in range(len(hash_bytes)):
    h = hash_bytes[i]
    c = CONST[i]
    if c > 0:
        epsilon = (h - c) / c
    else:
        epsilon = 0
    epsilons.append(epsilon)

print(f"\nε pattern (first 16):")
print(f"  {[f'{e:+.2f}' for e in epsilons[:16]]}")

# Sign pattern (direction of bounces)
signs = ['↑' if e > 0 else '↓' for e in epsilons[:16]]
print(f"\nBounce directions: {''.join(signs)}")

# What does this pattern encode?
# The ASCII values of NEXUS are: 78, 69, 88, 85, 83
# In binary: 01001110, 01000101, 01011000, 01010101, 01010011
# The sign pattern: ↓↑↓↑↓↑↓↑↓↓↑↓↓↑↓↓

# Map signs to bits
bits = ''.join(['1' if e > 0 else '0' for e in epsilons[:8]])
print(f"\nSign pattern as bits: {bits}")
print(f"As number: {int(bits, 2)}")
print(f"Original N = {msg_bytes[0]} = {bin(msg_bytes[0])}")

# ============================================================
print("\n" + "=" * 60)
print("ITERATIVE REFINEMENT")
print("=" * 60)

# Start with complement estimate, refine iteratively

def refine_estimate(hash_bytes, const_bytes, iterations=10):
    """Iteratively refine the input estimate"""
    
    # Initial estimate from complement method
    estimate = []
    for i in range(len(hash_bytes)):
        h = hash_bytes[i]
        c = const_bytes[i % len(const_bytes)]
        result = csd_complement(h, c)
        estimate.append(result['pre_byte'])
    
    print(f"Initial estimate: {estimate[:5]}")
    
    for iteration in range(iterations):
        # Hash the current estimate
        est_hash = list(hashlib.sha256(bytes(estimate)).digest())
        
        # Compare to target hash
        diff = sum(abs(a - b) for a, b in zip(est_hash, hash_bytes))
        
        # Adjust estimate based on hash difference
        new_estimate = []
        for i in range(len(estimate)):
            h_target = hash_bytes[i]
            h_current = est_hash[i]
            
            # If current hash is too high, lower the estimate
            adjustment = (h_target - h_current) // 4
            new_val = estimate[i] + adjustment
            new_val = max(0, min(255, new_val))
            new_estimate.append(new_val)
        
        estimate = new_estimate
        
        if iteration < 5 or iteration == iterations - 1:
            print(f"Iter {iteration}: estimate={estimate[:5]} hash_diff={diff}")
    
    return estimate

refined = refine_estimate(hash_bytes, CONST, iterations=20)
print(f"\nFinal refined: {refined[:5]}")
print(f"Original:      {msg_bytes}")
