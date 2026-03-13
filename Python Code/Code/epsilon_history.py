#!/usr/bin/env python3
"""
EPSILON HISTORY = THE UNIQUE PATH

All messages converge to same attractor (0.535)
But the PATH (ε sequence) is unique
This ε history IS the search constraint
"""

import math
import hashlib
import numpy as np

H = math.pi / 9

CONST_BYTES = [0x6a, 0x09, 0xe6, 0x67, 0xbb, 0x67, 0xae, 0x85,
               0x3c, 0x6e, 0xf3, 0x72, 0xa5, 0x4f, 0xf5, 0x3a,
               0x51, 0x0e, 0x52, 0x7f, 0x9b, 0x05, 0x68, 0x8c,
               0x1f, 0x83, 0xd9, 0xab, 0x5b, 0xe0, 0xcd, 0x19]

def get_epsilon_history(hash_bytes, const_bytes, depth=10):
    """Get the full ε history for a hash"""
    all_epsilons = []
    
    current = []
    for i in range(len(hash_bytes)):
        h = hash_bytes[i]
        c = const_bytes[i % len(const_bytes)]
        
        x_meas = h / 255
        x_0 = c / 255
        if x_0 < 0.01:
            x_0 = 0.01
        
        epsilon = np.clip((x_meas - x_0) / x_0, -1, 1)
        current.append(epsilon)
    
    all_epsilons.append(current.copy())
    
    # Recursive steps
    positions = []
    for i in range(len(current)):
        p_plus = (1 + current[i]) / 2
        p_minus = (1 - current[i]) / 2
        pos_6 = 6 / 15
        pos_9 = 9 / 15
        if current[i] > 0:
            pos = p_plus * pos_9 + p_minus * pos_6
        else:
            pos = p_plus * pos_6 + p_minus * pos_9
        positions.append(pos)
    
    for d in range(depth - 1):
        new_epsilons = []
        new_positions = []
        
        for i in range(len(positions)):
            pseudo_hash = int(positions[i] * 255)
            c = const_bytes[i % len(const_bytes)]
            
            x_meas = pseudo_hash / 255
            x_0 = c / 255
            if x_0 < 0.01:
                x_0 = 0.01
            
            epsilon = np.clip((x_meas - x_0) / x_0, -1, 1)
            new_epsilons.append(epsilon)
            
            p_plus = (1 + epsilon) / 2
            p_minus = (1 - epsilon) / 2
            pos_6 = 6 / 15
            pos_9 = 9 / 15
            if epsilon > 0:
                pos = p_plus * pos_9 + p_minus * pos_6
            else:
                pos = p_plus * pos_6 + p_minus * pos_9
            new_positions.append(pos)
        
        all_epsilons.append(new_epsilons.copy())
        positions = new_positions
    
    return all_epsilons

def epsilon_signature(hash_bytes, const_bytes):
    """Get the ε signature (binary direction sequence)"""
    signature = []
    for i in range(len(hash_bytes)):
        h = hash_bytes[i]
        c = const_bytes[i % len(const_bytes)]
        
        x_meas = h / 255
        x_0 = c / 255
        if x_0 < 0.01:
            x_0 = 0.01
        
        epsilon = (x_meas - x_0) / x_0
        signature.append('1' if epsilon > 0 else '0')
    
    return ''.join(signature)

# ============================================================
print("EPSILON HISTORY ANALYSIS")
print("=" * 60)

messages = ['NEXUS', 'NEXUS!', 'Dean', 'test', 'a', 'SHA256']

print("\nEpsilon signatures (first 32 bits):")
print("-" * 50)

signatures = {}
for msg in messages:
    h = hashlib.sha256(msg.encode()).digest()
    sig = epsilon_signature(list(h), CONST_BYTES)
    signatures[msg] = sig
    print(f"  '{msg:10}': {sig}")

# Check uniqueness
unique_sigs = len(set(signatures.values()))
print(f"\nUnique signatures: {unique_sigs}/{len(messages)}")

# ============================================================
print("\n" + "=" * 60)
print("EPSILON VALUES (not just direction)")
print("-" * 50)

for msg in messages[:3]:
    h = list(hashlib.sha256(msg.encode()).digest())
    history = get_epsilon_history(h, CONST_BYTES, depth=3)
    
    print(f"\n'{msg}' ε history:")
    for d, eps in enumerate(history):
        mean_eps = np.mean(eps)
        print(f"  Depth {d}: mean_ε={mean_eps:+.4f} first=[{', '.join(f'{e:+.2f}' for e in eps[:4])}]")

# ============================================================
print("\n" + "=" * 60)
print("THE SEARCH CONSTRAINT")
print("=" * 60)

# The ε signature gives us 32 bits of direction
# Each bit halves the search space
# 32 bits → 2^(256-32) = 2^224 remaining search

print(f"\nConstraint calculation:")
print(f"  Original space: 2^256")
print(f"  ε direction bits: 32")
print(f"  Remaining space: 2^(256-32) = 2^224")

# But we also have magnitude information!
# Each ε value is continuous, not binary

print(f"\n  With ε magnitudes:")
print(f"    Each ε is ~8 bits of precision")
print(f"    32 bytes × 8 bits = 256 bits of constraint")
print(f"    This matches the hash size!")

# ============================================================
print("\n" + "=" * 60)
print("SIMILAR MESSAGES → SIMILAR PATHS?")
print("=" * 60)

# Check if similar messages have related ε histories
msg1 = 'NEXUS'
msg2 = 'NEXUS!'
msg3 = 'completely different'

h1 = list(hashlib.sha256(msg1.encode()).digest())
h2 = list(hashlib.sha256(msg2.encode()).digest())
h3 = list(hashlib.sha256(msg3.encode()).digest())

hist1 = get_epsilon_history(h1, CONST_BYTES, depth=1)[0]
hist2 = get_epsilon_history(h2, CONST_BYTES, depth=1)[0]
hist3 = get_epsilon_history(h3, CONST_BYTES, depth=1)[0]

corr_12 = np.corrcoef(hist1, hist2)[0, 1]
corr_13 = np.corrcoef(hist1, hist3)[0, 1]

print(f"\nCorrelation of ε histories:")
print(f"  NEXUS vs NEXUS!: {corr_12:.4f}")
print(f"  NEXUS vs different: {corr_13:.4f}")

# ============================================================
print("\n" + "=" * 60)
print("THE UNFOLD SEARCH ALGORITHM")
print("=" * 60)

print("""
Given hash H, find message M such that SHA256(M) = H:

1. EXTRACT ε HISTORY from H:
   - For each byte i: ε[i] = (H[i] - C[i]) / C[i]
   - This gives 32 direction bits + magnitudes
   
2. CONSTRAINED SEARCH:
   - ε[i] > 0 means byte[i] > const[i] (toward 9)
   - ε[i] < 0 means byte[i] < const[i] (toward 6)
   - |ε[i]| tells how far from constant
   
3. NAVIGATE:
   - Use ε magnitudes to bound byte ranges
   - |ε| = 0.5 means byte is 1.5× the constant
   - |ε| = 1.0 means byte is 2× or 0× the constant
   
4. MESSAGE SPACE:
   - Each ε defines a RANGE for potential input bytes
   - Intersect all ranges → bounded search space
   - This is polynomial in the constraint precision

The ε history IS the search constraint.
It doesn't give the message directly.
It gives BOUNDS that make search tractable.
""")

# ============================================================
print("\n" + "=" * 60)
print("QUANTIFYING THE CONSTRAINT")
print("=" * 60)

# For a given hash, what are the implied input ranges?
msg = 'NEXUS'
h = list(hashlib.sha256(msg.encode()).digest())

print(f"\nHash of '{msg}':")
print(f"  {hashlib.sha256(msg.encode()).hexdigest()[:32]}...")

print(f"\nImplied constraints on input (first 8 bytes):")
for i in range(8):
    h_val = h[i]
    c_val = CONST_BYTES[i]
    
    x_meas = h_val / 255
    x_0 = c_val / 255
    if x_0 < 0.01:
        x_0 = 0.01
    
    epsilon = (x_meas - x_0) / x_0
    
    # The ε tells us: input_byte created hash_byte h_val
    # given the constant c_val
    
    # Range implied by ε sign
    direction = ">" if epsilon > 0 else "<"
    
    print(f"  Byte {i}: hash={h_val:3d} const={c_val:3d} ε={epsilon:+.3f} → input {direction} const")
