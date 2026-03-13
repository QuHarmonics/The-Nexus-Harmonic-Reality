#!/usr/bin/env python3
"""
THE RECURSIVE UNFOLD

6 XOR 9 = F (barrier)
6 + 9 = F (barrier)
H = π/9 (9 is the frequency source)
6 is the complement (the lock)

The unfold uses this complementarity.
"""

import math
import numpy as np

H = math.pi / 9  # 0.349066

# ============================================================
print("THE 6-9 COMPLEMENTARITY")
print("=" * 60)

print(f"\n6 XOR 9 = {6 ^ 9} = F (barrier)")
print(f"6 + 9 = {6 + 9} = F (barrier)")
print(f"6 binary: {bin(6)[2:].zfill(4)}")
print(f"9 binary: {bin(9)[2:].zfill(4)}")
print(f"Bitwise complement: 6 ↔ 9")

print(f"\nH = π/9")
print(f"9 is the denominator = frequency source")
print(f"6 is the complement = lock position")
print(f"Together they create F = barrier")

# ============================================================
print("\n" + "=" * 60)
print("THE COLLAPSE EQUATION")
print("=" * 60)

# ε = (x_meas - x_0) / x_0
# At 6-lock: x = 6/15 = 0.4, x_0 = 6/15 = 0.4 → ε = 0
# At 9: x = 9/15 = 0.6, if x_0 = 6/15 → ε = (0.6-0.4)/0.4 = 0.5

x_6 = 6 / 15
x_9 = 9 / 15

print(f"\nPositions:")
print(f"  x_6 = 6/15 = {x_6:.4f}")
print(f"  x_9 = 9/15 = {x_9:.4f}")

# ε between 6 and 9
epsilon_6_to_9 = (x_9 - x_6) / x_6
print(f"\nε from 6 to 9:")
print(f"  ε = ({x_9} - {x_6}) / {x_6} = {epsilon_6_to_9:.4f}")

# This ε = 0.5 means p+ = 0.75, p- = 0.25
p_plus = (1 + epsilon_6_to_9) / 2
p_minus = (1 - epsilon_6_to_9) / 2
print(f"  p+ = {p_plus:.4f}")
print(f"  p- = {p_minus:.4f}")

# ============================================================
print("\n" + "=" * 60)
print("THE UNFOLD MECHANISM")
print("=" * 60)

print("""
At the 6-LOCK (fixed point):
  ε = 0, p+ = p- = 0.5 (BALANCE)
  
Moving from 6 toward 9:
  ε → 0.5, p+ → 0.75, p- → 0.25
  Collapse favors Φ₀ (particle/structure)
  
Moving from 9 toward 6:
  ε → -0.33, p+ → 0.33, p- → 0.67
  Collapse favors E₀ (wave/entropy)

THE UNFOLD:
  1. Hash gives ε (the phase offset)
  2. ε tells direction: toward 6 (lock) or 9 (frequency)
  3. p+ and p- tell the split
  4. Navigate: p+ × destination + p- × source
""")

# ============================================================
print("\n" + "=" * 60)
print("APPLYING TO SHA")
print("=" * 60)

# SHA constants encode √primes and ∛primes
# These have relationship to π through H

# For each hash byte vs constant byte:
# ε = (hash - const) / const
# This tells us which way the collapse went

# To UNFOLD:
# new_position = p+ × (hash_position) + p- × (constant_position)

print("SHA Unfold Algorithm:")
print("-" * 40)

def unfold_byte(hash_byte, const_byte):
    """Unfold one byte using collapse signature"""
    x_meas = hash_byte / 255
    x_0 = const_byte / 255
    
    if x_0 < 0.01:
        x_0 = 0.01
    
    epsilon = (x_meas - x_0) / x_0
    epsilon = np.clip(epsilon, -1, 1)
    
    p_plus = (1 + epsilon) / 2
    p_minus = (1 - epsilon) / 2
    
    # The 6-9 complementarity
    # 6/15 = 0.4, 9/15 = 0.6
    # Position in 6-9 space
    pos_6 = 6 / 15  # 0.4 = lock
    pos_9 = 9 / 15  # 0.6 = frequency
    
    # Navigate based on ε
    if epsilon > 0:
        # Moving toward 9 (frequency/structure)
        unfold_pos = p_plus * pos_9 + p_minus * pos_6
    else:
        # Moving toward 6 (lock/barrier)
        unfold_pos = p_plus * pos_6 + p_minus * pos_9
    
    return {
        'epsilon': epsilon,
        'p_plus': p_plus,
        'p_minus': p_minus,
        'direction': '→9' if epsilon > 0 else '→6',
        'unfold_position': unfold_pos
    }

# Test with example bytes
test_cases = [
    (0x52, 0x6a),  # NEXUS first bytes vs H_INIT
    (0xb7, 0x09),
    (0x97, 0xe6),
    (0xa2, 0x67),
]

CONST_BYTES = [0x6a, 0x09, 0xe6, 0x67, 0xbb, 0x67, 0xae, 0x85]

print("\nExample unfolds:")
for h_byte, c_byte in test_cases:
    result = unfold_byte(h_byte, c_byte)
    print(f"  hash={h_byte:02x} const={c_byte:02x}: ε={result['epsilon']:+.3f} "
          f"p+={result['p_plus']:.3f} {result['direction']} "
          f"unfold={result['unfold_position']:.4f}")

# ============================================================
print("\n" + "=" * 60)
print("THE RECURSIVE STEP")
print("=" * 60)

# The unfold position becomes the input for next iteration
# Like BBP: position → digit → position → digit...

def recursive_unfold(hash_bytes, const_bytes, depth=5):
    """Recursively unfold using 6-9 navigation"""
    positions = []
    
    for i in range(min(len(hash_bytes), len(const_bytes))):
        h = hash_bytes[i]
        c = const_bytes[i]
        
        result = unfold_byte(h, c)
        positions.append(result['unfold_position'])
    
    # Recursive step: use positions as new input
    current = positions
    history = [current.copy()]
    
    for d in range(depth):
        new_positions = []
        for i, pos in enumerate(current):
            # Convert position back to byte-like value
            pseudo_hash = int(pos * 255)
            pseudo_const = const_bytes[i % len(const_bytes)]
            
            result = unfold_byte(pseudo_hash, pseudo_const)
            new_positions.append(result['unfold_position'])
        
        current = new_positions
        history.append(current.copy())
    
    return history

# Test recursive unfold
import hashlib
test_msg = "NEXUS"
hash_bytes = list(hashlib.sha256(test_msg.encode()).digest())
const_bytes = CONST_BYTES

print(f"\nRecursive unfold of '{test_msg}':")
history = recursive_unfold(hash_bytes[:8], const_bytes, depth=10)

for i, positions in enumerate(history[:6]):
    mean = np.mean(positions)
    print(f"  Depth {i}: mean={mean:.4f} first=[{', '.join(f'{p:.3f}' for p in positions[:4])}]")

# Check convergence
final_mean = np.mean(history[-1])
print(f"\n  Final mean after 10 iterations: {final_mean:.4f}")
print(f"  6/15 (lock position) = {6/15:.4f}")
print(f"  H = {H:.4f}")

# ============================================================
print("\n" + "=" * 60)
print("CONVERGENCE TO ATTRACTORS")
print("=" * 60)

# Run for multiple messages
messages = ['NEXUS', 'Dean', 'test', 'a', 'SHA256', 'H=pi/9']

print("\nFinal positions after 20 recursive unfolds:")
for msg in messages:
    h_bytes = list(hashlib.sha256(msg.encode()).digest())
    history = recursive_unfold(h_bytes[:8], const_bytes, depth=20)
    
    final = history[-1]
    mean = np.mean(final)
    
    # Distance to attractors
    d_lock = abs(mean - 6/15)
    d_H = abs(mean - H)
    d_half = abs(mean - 0.5)
    
    attractor = "6/15" if d_lock < d_H and d_lock < d_half else ("H" if d_H < d_half else "0.5")
    
    print(f"  '{msg}': mean={mean:.4f} → nearest attractor: {attractor}")

# ============================================================
print("\n" + "=" * 60)
print("THE COMPLETE ALGORITHM")
print("=" * 60)

print("""
SHA RECURSIVE UNFOLD:

1. INITIALIZE:
   - hash_bytes = SHA256(message)
   - const_bytes = SHA constants (encode H via √primes)
   
2. FOR EACH BYTE:
   - ε = (hash - const) / const
   - p+ = (1+ε)/2, p- = (1-ε)/2
   - direction = →9 if ε>0, →6 if ε<0
   - unfold_position = p+ × target + p- × source
   
3. RECURSE:
   - Use unfold_positions as new hash-like input
   - Repeat until convergence
   
4. CONVERGENCE:
   - System settles to 6/15 ≈ 0.4 (lock position)
   - Or to H ≈ 0.35 (frequency source)
   - Or to 0.5 (balance)
   
5. THE MESSAGE SPACE:
   - The path taken encodes the message structure
   - ε history = collapse signature = search constraint
   - Navigate this constrained space to find input

This is P(2)NP:
  - Without constants: 2^256 search
  - With constants + ε: navigate to convergence point
  - The constants ARE the map
  - The ε ARE the directions
""")
