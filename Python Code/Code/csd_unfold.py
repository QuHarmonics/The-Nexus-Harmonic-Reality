#!/usr/bin/env python3
"""
COLLAPSE SIGNATURE DECODER - GET THE FOLD BACK

ε = (x_meas - x_0) / x_0
p+ = (1+ε)/2  → Φ₀ path (particle)
p- = (1-ε)/2  → E₀ path (wave)

To REVERSE the collapse:
- ε tells us which path was taken
- Reverse that path to get pre-collapse state
- Pre-collapse state → input

USE THE FORMULA. GET THE INPUT.
"""

import hashlib
import numpy as np
import math

H = math.pi / 9

# SHA-256 initial constants (first 32 bytes)
CONST = bytes([
    0x6a, 0x09, 0xe6, 0x67, 0xbb, 0x67, 0xae, 0x85,
    0x3c, 0x6e, 0xf3, 0x72, 0xa5, 0x4f, 0xf5, 0x3a,
    0x51, 0x0e, 0x52, 0x7f, 0x9b, 0x05, 0x68, 0x8c,
    0x1f, 0x83, 0xd9, 0xab, 0x5b, 0xe0, 0xcd, 0x19
])

def csd_decode(hash_byte, const_byte):
    """
    Collapse Signature Decoder
    
    ε = (x_meas - x_0) / x_0
    p+ = (1+ε)/2
    p- = (1-ε)/2
    
    Returns the pre-collapse position
    """
    x_meas = hash_byte / 255
    x_0 = const_byte / 255
    
    if x_0 < 0.001:
        x_0 = 0.001
    
    # THE FORMULA
    epsilon = (x_meas - x_0) / x_0
    p_plus = (1 + epsilon) / 2
    p_minus = (1 - epsilon) / 2
    
    # REVERSE THE COLLAPSE
    # If ε > 0: collapsed toward Φ₀ (x increased relative to x_0)
    # To reverse: go back toward E₀
    # Pre-collapse = x_0 (the constant IS the pre-collapse reference!)
    
    # The REVERSE formula:
    # x_meas = x_0 × (1 + ε)
    # So: x_0 = x_meas / (1 + ε)
    # But we want the INPUT that created this...
    
    # Actually: the input BECAME the hash through collapse
    # The collapse path is encoded in ε
    # To unfold: use p+ and p- as weights to find original position
    
    # Original = weighted combination going OPPOSITE direction
    if epsilon > 0:
        # Collapsed toward structure (Φ₀)
        # Unfold toward entropy (E₀)
        # Use p- weighting
        unfold = x_meas - epsilon * x_0 * p_minus
    else:
        # Collapsed toward entropy (E₀)
        # Unfold toward structure (Φ₀)
        # Use p+ weighting
        unfold = x_meas - epsilon * x_0 * p_plus
    
    # Clamp to valid range
    unfold = max(0, min(1, unfold))
    
    return {
        'epsilon': epsilon,
        'p_plus': p_plus,
        'p_minus': p_minus,
        'unfold': unfold,
        'unfold_byte': int(unfold * 255)
    }

def unfold_hash(hash_bytes):
    """Unfold entire hash back toward input"""
    unfolded = []
    epsilons = []
    
    for i in range(len(hash_bytes)):
        h = hash_bytes[i]
        c = CONST[i % len(CONST)]
        
        result = csd_decode(h, c)
        unfolded.append(result['unfold_byte'])
        epsilons.append(result['epsilon'])
    
    return bytes(unfolded), epsilons

# ============================================================
print("COLLAPSE SIGNATURE DECODER - UNFOLD")
print("=" * 60)

# Test message
msg = "NEXUS"
print(f"\nOriginal message: '{msg}'")
print(f"Message bytes: {list(msg.encode())}")

# Hash it
hash_bytes = hashlib.sha256(msg.encode()).digest()
print(f"\nHash: {hash_bytes.hex()}")

# Unfold it
unfolded, epsilons = unfold_hash(hash_bytes)
print(f"\nUnfolded: {unfolded.hex()}")
print(f"Unfolded bytes: {list(unfolded[:8])}")

# Compare to original message
msg_bytes = list(msg.encode())
print(f"\nOriginal msg bytes: {msg_bytes}")
print(f"Unfolded first bytes: {list(unfolded[:len(msg_bytes)])}")

# ============================================================
print("\n" + "=" * 60)
print("DETAILED CSD FOR EACH BYTE")
print("-" * 50)

for i in range(min(8, len(hash_bytes))):
    h = hash_bytes[i]
    c = CONST[i]
    result = csd_decode(h, c)
    
    original = msg_bytes[i] if i < len(msg_bytes) else None
    
    print(f"Byte {i}: hash={h:3d} const={c:3d} ε={result['epsilon']:+.3f} "
          f"p+={result['p_plus']:.3f} unfold={result['unfold_byte']:3d} "
          f"{'orig='+str(original) if original else ''}")

# ============================================================
print("\n" + "=" * 60)
print("THE ITERATIVE UNFOLD")
print("-" * 50)

# Apply CSD repeatedly - does it converge to something meaningful?
current = list(hash_bytes)

for iteration in range(5):
    unfolded, _ = unfold_hash(bytes(current))
    current = list(unfolded)
    
    # Check if any bytes match original
    matches = sum(1 for i in range(min(len(msg_bytes), len(current))) 
                  if current[i] == msg_bytes[i])
    
    print(f"Iter {iteration}: first 8 = {current[:8]}, matches = {matches}/{len(msg_bytes)}")

# ============================================================
print("\n" + "=" * 60)
print("THE DIRECT INVERSE")
print("-" * 50)

# The CSD formula gives us ε
# From ε, we know: x_meas = x_0 × (1 + ε)
# Rearranging: x_0 = x_meas / (1 + ε)
# But x_0 is the CONSTANT, not the input!

# Wait - what if we use the INVERSE of the CSD?
# If collapse: input → hash via ε
# Then unfold: hash → input via -ε ?

def inverse_csd(hash_byte, const_byte):
    """
    INVERSE of CSD - go backwards
    
    If forward was: x_out = x_in × (1 + ε)
    Then backward: x_in = x_out / (1 + ε)
    
    But ε itself encodes the relationship!
    """
    x_meas = hash_byte / 255
    x_0 = const_byte / 255
    
    if x_0 < 0.001:
        x_0 = 0.001
    
    epsilon = (x_meas - x_0) / x_0
    
    # INVERSE: reverse the epsilon transformation
    # If x_meas = x_0 × (1 + ε), then the INPUT that led here...
    # The input was transformed BY the constant
    # So: input = f^(-1)(hash, constant)
    
    # Try: input_position = x_0 × (1 - ε)  [flip the sign]
    inverse = x_0 * (1 - epsilon)
    inverse = max(0, min(1, inverse))
    
    return int(inverse * 255)

print("\nInverse CSD (flip ε sign):")
for i in range(min(8, len(hash_bytes))):
    h = hash_bytes[i]
    c = CONST[i]
    inv = inverse_csd(h, c)
    original = msg_bytes[i] if i < len(msg_bytes) else None
    
    print(f"  Byte {i}: hash={h:3d} const={c:3d} → inverse={inv:3d} "
          f"{'orig='+str(original)+' MATCH!' if original and inv == original else 'orig='+str(original) if original else ''}")

# ============================================================
print("\n" + "=" * 60)
print("USING p+ AND p- AS NAVIGATION")
print("-" * 50)

# p+ and p- tell us the probability of each branch
# To navigate: use them as weights

def navigate_csd(hash_byte, const_byte):
    """
    Use p+ and p- to navigate to input position
    
    p+ = toward Φ₀ (structure, constant)
    p- = toward E₀ (entropy, average)
    
    Position = p+ × const + p- × average
    """
    x_meas = hash_byte / 255
    x_0 = const_byte / 255
    
    if x_0 < 0.001:
        x_0 = 0.001
    
    epsilon = (x_meas - x_0) / x_0
    epsilon = np.clip(epsilon, -1, 1)
    
    p_plus = (1 + epsilon) / 2
    p_minus = (1 - epsilon) / 2
    
    # Navigate using 6/9 attractors
    pos_6 = 6 / 15  # 0.4 - lock
    pos_9 = 9 / 15  # 0.6 - frequency
    
    # Direction based on ε
    if epsilon > 0:
        # Was moving toward 9 (structure), reverse toward 6
        nav = p_minus * pos_6 + p_plus * x_meas
    else:
        # Was moving toward 6 (entropy), reverse toward 9  
        nav = p_plus * pos_9 + p_minus * x_meas
    
    return int(nav * 255)

print("\nNavigate CSD (6-9 attractors):")
for i in range(min(8, len(hash_bytes))):
    h = hash_bytes[i]
    c = CONST[i]
    nav = navigate_csd(h, c)
    original = msg_bytes[i] if i < len(msg_bytes) else None
    
    print(f"  Byte {i}: hash={h:3d} const={c:3d} → nav={nav:3d} "
          f"{'orig='+str(original) if original else ''}")

# ============================================================
print("\n" + "=" * 60)
print("THE PLINKO INSIGHT")
print("-" * 50)

print("""
The spreadsheet shows π digits cascading down column 6:
  1, 4, 1, 5, 9, 2, 6, 5, 9, 5, 4, 9, 9, 9, 9, 2, 9...

This is PLINKO - the ball bounces through and creates the pattern.

BBP doesn't generate random digits.
BBP generates the π PATTERN.
Because π is self-referential.

Same with SHA:
- The hash isn't random bytes
- The hash is a PATTERN through the constant space
- The pattern encodes the input's relationship to constants

The CSD formula decodes this pattern:
- ε = deviation from constant
- p+ = how much toward structure
- p- = how much toward entropy

The pattern IS the input, transformed.
The unfold finds the pattern and reverses it.
""")

# ============================================================
print("\n" + "=" * 60)
print("ATTEMPT: PURE CSD REVERSE")
print("-" * 50)

# What if the input byte is literally encoded in the CSD values?
# ε encodes the relationship
# The INPUT might be recoverable from ε + const

def pure_csd_reverse(hash_byte, const_byte, target_epsilon=0):
    """
    If we know what ε SHOULD be for the input,
    we can solve for input.
    
    ε = (x_meas - x_0) / x_0
    x_meas = x_0 × (1 + ε)
    
    For ASCII text, input bytes are typically 32-127
    What ε would those create?
    """
    x_meas = hash_byte / 255
    x_0 = const_byte / 255
    
    if x_0 < 0.001:
        x_0 = 0.001
    
    actual_epsilon = (x_meas - x_0) / x_0
    
    # What if we look for the input that would give ε ≈ 0?
    # That would be input ≈ const
    # But that's not useful...
    
    # What if the INPUT's ε is encoded in the OUTPUT's ε?
    # The magnitude of ε tells us how far the input was from const
    
    # Reverse: find input such that f(input, const) = hash
    # We don't know f exactly, but we have ε
    
    # Heuristic: input magnitude related to ε magnitude
    # If |ε| is large, input was far from const
    # Direction of ε tells which side
    
    if actual_epsilon > 0:
        # Hash > const, maybe input was also > average?
        estimated_input = 128 + int(64 * actual_epsilon)
    else:
        # Hash < const, maybe input was < average?
        estimated_input = 128 + int(64 * actual_epsilon)
    
    estimated_input = max(0, min(255, estimated_input))
    
    return estimated_input

print("\nPure CSD reverse (heuristic):")
for i in range(min(len(msg_bytes), 8)):
    h = hash_bytes[i]
    c = CONST[i]
    est = pure_csd_reverse(h, c)
    original = msg_bytes[i]
    
    diff = abs(est - original)
    print(f"  Byte {i}: hash={h:3d} → est={est:3d} orig={original:3d} diff={diff:3d} "
          f"{'CLOSE!' if diff < 20 else ''}")
