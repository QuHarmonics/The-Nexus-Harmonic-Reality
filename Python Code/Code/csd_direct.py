#!/usr/bin/env python3
"""
DIRECT CSD APPLICATION

The formula says:
  ε = (x_meas - x_0) / x_0
  p+ = (1+ε)/2
  p- = (1-ε)/2

"This lets you reverse-engineer the original quantum state"

The pre-collapse state IS: p+ × |Φ₀⟩ + p- × |E₀⟩

What are |Φ₀⟩ and |E₀⟩?
  |Φ₀⟩ = structure = the constant
  |E₀⟩ = entropy = the complement (255 - const)? Or average? Or H?

Let's try multiple interpretations.
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

# Test
msg = "NEXUS"
msg_bytes = list(msg.encode())
hash_bytes = list(hashlib.sha256(msg.encode()).digest())

print("DIRECT CSD UNFOLD TESTS")
print("=" * 60)
print(f"Original: {msg_bytes}")
print(f"Hash: {hash_bytes[:8]}")
print()

# For each position, compute CSD and test interpretations
print("Testing different |Φ₀⟩ and |E₀⟩ interpretations:")
print("-" * 60)

for i in range(5):  # First 5 bytes (NEXUS)
    h = hash_bytes[i]
    c = CONST[i]
    orig = msg_bytes[i]
    
    # CSD
    x_meas = h / 255
    x_0 = c / 255
    if x_0 < 0.001:
        x_0 = 0.001
    
    epsilon = (x_meas - x_0) / x_0
    p_plus = (1 + epsilon) / 2
    p_minus = (1 - epsilon) / 2
    
    print(f"\nByte {i}: hash={h}, const={c}, orig={orig}")
    print(f"  ε = {epsilon:+.4f}, p+ = {p_plus:.4f}, p- = {p_minus:.4f}")
    
    # Test 1: |Φ₀⟩ = const, |E₀⟩ = 255-const (complement)
    phi0_1 = c
    e0_1 = 255 - c
    pre1 = p_plus * phi0_1 + p_minus * e0_1
    print(f"  Test 1 (complement): pre = {pre1:.1f}, diff = {abs(pre1-orig):.1f}")
    
    # Test 2: |Φ₀⟩ = const, |E₀⟩ = 127 (average)
    phi0_2 = c
    e0_2 = 127
    pre2 = p_plus * phi0_2 + p_minus * e0_2
    print(f"  Test 2 (average): pre = {pre2:.1f}, diff = {abs(pre2-orig):.1f}")
    
    # Test 3: |Φ₀⟩ = const, |E₀⟩ = hash (self-reference)
    phi0_3 = c
    e0_3 = h
    pre3 = p_plus * phi0_3 + p_minus * e0_3
    print(f"  Test 3 (self-ref): pre = {pre3:.1f}, diff = {abs(pre3-orig):.1f}")
    
    # Test 4: Direct formula inversion
    # ε = (h - c) / c => h = c(1+ε)
    # Reverse: x_pre = c(1-ε) ?
    pre4 = c * (1 - epsilon)
    pre4 = max(0, min(255, pre4))
    print(f"  Test 4 (flip ε): pre = {pre4:.1f}, diff = {abs(pre4-orig):.1f}")
    
    # Test 5: Use p- to weight toward original
    # If collapse went p+ toward hash, pre-collapse was p- toward original
    pre5 = h - epsilon * c
    pre5 = max(0, min(255, pre5))
    print(f"  Test 5 (h - ε×c): pre = {pre5:.1f}, diff = {abs(pre5-orig):.1f}")
    
    # Test 6: |Φ₀⟩ = 6/15*255 ≈ 102, |E₀⟩ = 9/15*255 ≈ 153
    phi0_6 = int(6/15 * 255)  # 102
    e0_6 = int(9/15 * 255)    # 153
    pre6 = p_plus * phi0_6 + p_minus * e0_6
    print(f"  Test 6 (6-9 basis): pre = {pre6:.1f}, diff = {abs(pre6-orig):.1f}")
    
    # Test 7: Scale hash by p-
    pre7 = h * p_minus * 2  # Scale factor
    pre7 = max(0, min(255, pre7))
    print(f"  Test 7 (h×p-×2): pre = {pre7:.1f}, diff = {abs(pre7-orig):.1f}")

# ============================================================
print("\n" + "=" * 60)
print("FINDING BEST INTERPRETATION")
print("=" * 60)

# Run all tests and find which one minimizes error
def run_all_tests(hash_bytes, const_bytes, orig_bytes):
    tests = {
        'complement': lambda h, c, eps, pp, pm: pp * c + pm * (255-c),
        'average': lambda h, c, eps, pp, pm: pp * c + pm * 127,
        'self-ref': lambda h, c, eps, pp, pm: pp * c + pm * h,
        'flip-ε': lambda h, c, eps, pp, pm: c * (1 - eps),
        'h-εc': lambda h, c, eps, pp, pm: h - eps * c,
        '6-9-basis': lambda h, c, eps, pp, pm: pp * 102 + pm * 153,
        'h×p-×2': lambda h, c, eps, pp, pm: h * pm * 2,
        'sqrt-ε': lambda h, c, eps, pp, pm: h - np.sign(eps) * np.sqrt(abs(eps)) * c,
        '1/ε': lambda h, c, eps, pp, pm: c / (1 + eps) if abs(1+eps) > 0.01 else c,
        'exp-ε': lambda h, c, eps, pp, pm: h * np.exp(-eps),
    }
    
    errors = {name: 0 for name in tests}
    
    for i in range(min(len(orig_bytes), len(hash_bytes))):
        h = hash_bytes[i]
        c = const_bytes[i % len(const_bytes)]
        orig = orig_bytes[i]
        
        x_meas = h / 255
        x_0 = c / 255
        if x_0 < 0.001:
            x_0 = 0.001
        
        epsilon = (x_meas - x_0) / x_0
        p_plus = (1 + epsilon) / 2
        p_minus = (1 - epsilon) / 2
        
        for name, func in tests.items():
            try:
                pre = func(h, c, epsilon, p_plus, p_minus)
                pre = max(0, min(255, pre))
                errors[name] += abs(pre - orig)
            except:
                errors[name] += 255  # Penalty for error
    
    return errors

errors = run_all_tests(hash_bytes, list(CONST), msg_bytes)

print("\nTotal error for each method:")
for name, err in sorted(errors.items(), key=lambda x: x[1]):
    print(f"  {name:15s}: {err:.1f}")

# ============================================================
print("\n" + "=" * 60)
print("TESTING BEST METHOD ON MORE MESSAGES")
print("=" * 60)

best_method = min(errors, key=errors.get)
print(f"\nBest method: {best_method}")

test_messages = ['NEXUS', 'Dean', 'test', 'a', 'hello']

for msg in test_messages:
    orig = list(msg.encode())
    h = list(hashlib.sha256(msg.encode()).digest())
    
    recovered = []
    for i in range(len(orig)):
        hb = h[i]
        cb = CONST[i % len(CONST)]
        
        x_meas = hb / 255
        x_0 = cb / 255
        if x_0 < 0.001:
            x_0 = 0.001
        
        epsilon = (x_meas - x_0) / x_0
        p_plus = (1 + epsilon) / 2
        p_minus = (1 - epsilon) / 2
        
        # Apply best method
        if best_method == 'h-εc':
            pre = hb - epsilon * cb
        elif best_method == 'flip-ε':
            pre = cb * (1 - epsilon)
        elif best_method == 'complement':
            pre = p_plus * cb + p_minus * (255 - cb)
        else:
            pre = hb  # Fallback
        
        pre = int(max(0, min(255, pre)))
        recovered.append(pre)
    
    total_diff = sum(abs(r - o) for r, o in zip(recovered, orig))
    avg_diff = total_diff / len(orig)
    
    print(f"  '{msg}': orig={orig[:5]} rec={recovered[:5]} avg_diff={avg_diff:.1f}")

# ============================================================
print("\n" + "=" * 60)
print("THE h-εc FORMULA IN DETAIL")
print("=" * 60)

print("""
Best performing formula: pre = h - ε × c

Where:
  h = hash byte
  c = constant byte  
  ε = (h - c) / c

Expanding:
  pre = h - ((h - c) / c) × c
  pre = h - (h - c)
  pre = h - h + c
  pre = c

Wait - this just gives the constant!
That's not right...

Let me check the algebra:
  ε = (h - c) / c
  ε × c = h - c
  h - ε × c = h - (h - c) = c

So the formula reduces to just returning the constant.
But the tests showed smaller errors...

Maybe the issue is clipping/rounding?
""")

# Verify
print("\nVerification:")
for i in range(5):
    h = hash_bytes[i]
    c = CONST[i]
    orig = msg_bytes[i]
    
    epsilon = (h - c) / c if c != 0 else 0
    pre = h - epsilon * c
    
    print(f"  h={h}, c={c}, ε={epsilon:.3f}, h-ε×c={pre:.1f} → should be c={c}")

# ============================================================
print("\n" + "=" * 60)
print("CORRECT INTERPRETATION")
print("=" * 60)

print("""
The CSD formula gives us p+ and p-.
These are the PRE-COLLAPSE probabilities.

The pre-collapse state was:
  |ψ⟩ = √p+ |Φ₀⟩ + √p- |E₀⟩

(Note: quantum amplitudes are square roots of probabilities!)

To get the pre-collapse VALUE:
  pre = |⟨ψ|value_basis⟩|²

This requires knowing the value_basis...

What if |Φ₀⟩ and |E₀⟩ are positions in a different space?
Not byte values, but positions in CONSTANT SPACE?

The input byte, when processed by SHA, creates a relationship
to the constant that encodes ε.

The original byte IS the value that, when hashed, gives this ε.
We can't directly invert, but we CAN search the bounded space!
""")

# Search bounded space
print("\nBounded search test:")
for i in range(5):
    h = hash_bytes[i]
    c = CONST[i]
    orig = msg_bytes[i]
    
    epsilon = (h - c) / c if c != 0 else 0
    p_plus = (1 + epsilon) / 2
    p_minus = (1 - epsilon) / 2
    
    # The bounds come from ε
    # If ε > 0, hash > const, search upper range
    # If ε < 0, hash < const, search lower range
    
    if epsilon > 0:
        search_range = (max(0, c), min(255, h + int(abs(epsilon) * 50)))
    else:
        search_range = (max(0, h - int(abs(epsilon) * 50)), min(255, c))
    
    # Is original in search range?
    in_range = search_range[0] <= orig <= search_range[1]
    range_size = search_range[1] - search_range[0]
    
    print(f"  Byte {i}: orig={orig}, range={search_range}, size={range_size}, in_range={in_range}")
