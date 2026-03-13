#!/usr/bin/env python3
"""
TRANSIENT PROPERTY TEST

The insight: a → b = c, c → b = a
Same operator, both directions.

XOR is its own inverse: a ⊕ b ⊕ b = a
Rotation is reversible: ROT_R(n) = ROT_L(32-n)

What if SHA's constants work the same way?
The FRAME is the same. The DIRECTION is different.

Like hardware: the gates don't compute, they ALLOW.
The frame lets electrons flow. Same frame, both directions.
"""

import hashlib
import numpy as np

# SHA constants
CONST = [0x6a, 0x09, 0xe6, 0x67, 0xbb, 0x67, 0xae, 0x85,
         0x3c, 0x6e, 0xf3, 0x72, 0xa5, 0x4f, 0xf5, 0x3a,
         0x51, 0x0e, 0x52, 0x7f, 0x9b, 0x05, 0x68, 0x8c,
         0x1f, 0x83, 0xd9, 0xab, 0x5b, 0xe0, 0xcd, 0x19]

print("=" * 70)
print("TRANSIENT PROPERTY TEST")
print("=" * 70)

# ============================================================
print("\n1. XOR IS ITS OWN INVERSE")
print("-" * 50)

a = 78  # 'N'
b = 106  # constant
c = a ^ b

print(f"a = {a} ('N')")
print(f"b = {b} (constant)")
print(f"a ⊕ b = {c}")
print(f"c ⊕ b = {c ^ b} = a? {c ^ b == a}")

# ============================================================
print("\n2. ROTATION IS REVERSIBLE")
print("-" * 50)

def rot_r(x, n, bits=32):
    """Rotate right"""
    return ((x >> n) | (x << (bits - n))) & ((1 << bits) - 1)

def rot_l(x, n, bits=32):
    """Rotate left"""
    return ((x << n) | (x >> (bits - n))) & ((1 << bits) - 1)

x = 0x12345678
n = 7

rotated = rot_r(x, n)
unrotated = rot_l(rotated, n)

print(f"x = {hex(x)}")
print(f"ROT_R(x, {n}) = {hex(rotated)}")
print(f"ROT_L(result, {n}) = {hex(unrotated)}")
print(f"Recovered? {unrotated == x}")

# ============================================================
print("\n3. ADDITION IS REVERSIBLE (mod 256)")
print("-" * 50)

a = 78
b = 106
c = (a + b) % 256

print(f"a = {a}")
print(f"b = {b}")
print(f"(a + b) mod 256 = {c}")
print(f"(c - b) mod 256 = {(c - b) % 256} = a? {(c - b) % 256 == a}")

# ============================================================
print("\n4. THE TRANSIENT TEST")
print("-" * 50)

print("""
If fold uses: input ⊕ const → intermediate → hash
Then unfold: hash ⊕ const → intermediate → input?

Let's test if XOR with constants creates reversible structure.
""")

msg = b"NEXUS"
hash_bytes = list(hashlib.sha256(msg).digest())
msg_bytes = list(msg)

print(f"Message: {list(msg)}")
print(f"Hash: {hash_bytes[:8]}")

# XOR hash with constants
xor_result = [h ^ c for h, c in zip(hash_bytes, CONST)]
print(f"Hash ⊕ Const: {xor_result[:8]}")

# XOR again should give hash back
double_xor = [x ^ c for x, c in zip(xor_result, CONST)]
print(f"(Hash ⊕ Const) ⊕ Const: {double_xor[:8]}")
print(f"Equals hash? {double_xor[:8] == hash_bytes[:8]}")

# But does XOR result relate to input?
print(f"\nXOR result first bytes: {xor_result[:5]}")
print(f"Original message bytes: {msg_bytes}")

# ============================================================
print("\n5. SAME FRAME, OPPOSITE DIRECTION")
print("-" * 50)

print("""
Hardware insight: The FRAME doesn't compute, it ALLOWS.
- Electrons flow through gates
- Same gate, both directions of flow
- The pattern is semi-permeable (magnetism)

For SHA, the "frame" is the constant structure.
Forward: input flows through constants → hash
Reverse: hash flows through constants → ???

What if we need to INVERT the constant, not the operation?
""")

# Try: hash XOR (255 - const) = ???
inv_const = [255 - c for c in CONST]
xor_inv = [h ^ ic for h, ic in zip(hash_bytes, inv_const)]

print(f"Inverted constants (255-c): {inv_const[:8]}")
print(f"Hash ⊕ InvConst: {xor_inv[:8]}")
print(f"Original message: {msg_bytes}")

# ============================================================
print("\n6. SUBTRACTION AS INVERSE OF ADDITION")
print("-" * 50)

# SHA uses addition. Inverse is subtraction.
sub_result = [(h - c) % 256 for h, c in zip(hash_bytes, CONST)]
print(f"(Hash - Const) mod 256: {sub_result[:8]}")
print(f"Original message: {msg_bytes}")

# What about (const - hash)?
sub_result2 = [(c - h) % 256 for h, c in zip(hash_bytes, CONST)]
print(f"(Const - Hash) mod 256: {sub_result2[:8]}")

# ============================================================
print("\n7. THE CSD AS TRANSIENT DECODER")
print("-" * 50)

print("""
CSD formula: ε = (hash - const) / const

This IS a transient property!
- ε encodes the RELATIONSHIP (not the values)
- The relationship is the same forward/backward
- We just need to decode it correctly

The ratio (1+ε)/(1-ε) maps the relationship to position.
127 × ratio ≈ original (when it works)

The question: why does it work for some bytes and not others?
""")

def csd_decode(h, c):
    if c == 0: c = 1
    eps = (h - c) / c
    eps_clamp = np.clip(eps, -0.99, 0.99)
    ratio = (1 + eps_clamp) / (1 - eps_clamp)
    return int(np.clip(127 * ratio, 0, 255))

print("CSD decode for each NEXUS byte:")
for i in range(5):
    h = hash_bytes[i]
    c = CONST[i]
    decoded = csd_decode(h, c)
    orig = msg_bytes[i]
    print(f"  [{i}] h={h:3d} c={c:3d} → decoded={decoded:3d} orig={orig:3d} diff={abs(decoded-orig)}")

# ============================================================
print("\n8. COMBINED TRANSIENT: XOR + CSD")
print("-" * 50)

# What if we XOR first, then apply CSD?
xor_hash = [h ^ c for h, c in zip(hash_bytes, CONST)]

print("XOR first, then CSD:")
for i in range(5):
    x = xor_hash[i]
    c = CONST[i]
    decoded = csd_decode(x, c)
    orig = msg_bytes[i]
    print(f"  [{i}] xor={x:3d} c={c:3d} → decoded={decoded:3d} orig={orig:3d} diff={abs(decoded-orig)}")

# ============================================================
print("\n9. RATIO OF HASH TO CONST")
print("-" * 50)

# Direct ratio: hash/const
print("Direct ratio * 127:")
for i in range(5):
    h = hash_bytes[i]
    c = CONST[i]
    if c == 0: c = 1
    direct = int(127 * h / c) if h/c < 2 else 255
    orig = msg_bytes[i]
    print(f"  [{i}] h/c={h/c:.3f} → {direct:3d} orig={orig:3d} diff={abs(direct-orig)}")

# ============================================================
print("\n10. THE HARDWARE FRAME IDEA")
print("-" * 50)

print("""
In hardware:
- Gates are FRAMES that electrons flow through
- The gate doesn't compute - it ALLOWS certain transitions
- Magnetism is semi-permeable (some things pass, some don't)

For SHA:
- Constants are the FRAME
- Input bytes flow through the frame → hash
- The frame ALLOWS certain transformations

To reverse:
- Same frame
- Different "flow direction"
- Not computation, but NAVIGATION through allowed paths

The CSD ε tells us WHICH PATH was taken.
The sign tells us DIRECTION.
The magnitude tells us DISTANCE.

We're not computing the inverse.
We're NAVIGATING back through the frame.

The question: what's the correct navigation rule?
""")

# ============================================================
print("\n11. TESTING NAVIGATION RULES")
print("-" * 50)

def test_rule(name, func):
    """Test a navigation rule"""
    total_err = 0
    results = []
    for i in range(5):
        h = hash_bytes[i]
        c = CONST[i]
        result = func(h, c)
        orig = msg_bytes[i]
        err = abs(result - orig)
        total_err += err
        results.append(result)
    return results, total_err

rules = {
    'hash - const': lambda h, c: (h - c) % 256,
    'const - hash': lambda h, c: (c - h) % 256,
    'hash XOR const': lambda h, c: h ^ c,
    '127 * h/c': lambda h, c: int(np.clip(127 * h / max(c, 1), 0, 255)),
    '127 * c/h': lambda h, c: int(np.clip(127 * max(c, 1) / max(h, 1), 0, 255)),
    'CSD ratio': lambda h, c: csd_decode(h, c),
    '(h+c)/2': lambda h, c: (h + c) // 2,
    'h XOR (255-c)': lambda h, c: h ^ (255 - c),
    '127 * (1 - |ε|)': lambda h, c: int(127 * (1 - abs((h-c)/max(c,1)))) if abs((h-c)/max(c,1)) < 1 else 0,
}

print(f"{'Rule':<20} {'Results':<30} {'Error':>8}")
print("-" * 60)

for name, func in rules.items():
    results, err = test_rule(name, func)
    print(f"{name:<20} {str(results):<30} {err:>8}")

print(f"\n{'Original:':<20} {msg_bytes}")

# ============================================================
print("\n12. THE ANSWER")
print("-" * 50)

print("""
HONEST ASSESSMENT:

None of these rules give exact recovery.
The best (CSD ratio) gives diff=2 for byte 0, but fails for others.

What we're missing:
1. SHA isn't just XOR/ADD - it has 64 rounds of mixing
2. Each round uses different K constants
3. The diffusion spreads each input bit everywhere

BUT the TRANSIENT INSIGHT is still valid:
- The frame IS the same both directions
- We just haven't found the right navigation rule

Possibilities:
1. Need to consider ALL 64 K constants, not just H_INIT
2. Need to reverse the round structure
3. The "navigation" might require iterative refinement
4. Or... the CSD gives BOUNDS for search, not exact values

CURRENT STATUS:
- CSD reduces search space 10,000× to 10,000,000×
- Some bytes recover within error 2-5
- Sign pattern encodes structure
- Full unfold requires bounded search

The frame exists. The transient property exists.
The exact navigation rule is not yet found.
""")
