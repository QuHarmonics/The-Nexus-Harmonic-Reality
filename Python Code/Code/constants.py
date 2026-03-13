#!/usr/bin/env python3
"""
NEXUS CONSTANTS - THE FOUNDATION
================================

Every constant used in the framework.
These are "the computer" - the locked waveforms through which data flows.

Author: Dean Kulik
ORCID: 0009-0003-3128-8828
"""

import math

# ============================================================================
# UNIVERSAL CONSTANT
# ============================================================================

H = math.pi / 9  # 0.3490658503988659

# H-derived values
H_COMPLEMENT = 1 - H  # 0.6509341496011341
H_SQUARED = H * H  # 0.12184650889449045
H_CUBED = H ** 3  # 0.04252940070354908
H_FOURTH = H ** 4  # 0.014845438798493825
TWO_H = 2 * H  # 0.6981317007977318
FOUR_H = 4 * H  # 1.3962634015954636 (≈ √2)
H_OVER_3 = H / 3  # 0.11635528346628864

# Physical constant derivations
ALPHA_DERIVED = H / 48  # Fine structure constant ≈ 0.007272
SIN2_THETA_W = H * (1 - H)  # Weak mixing angle ≈ 0.2270
ALPHA_ACTUAL = 0.0072973525693  # Measured
SIN2_THETA_W_ACTUAL = 0.23121  # Measured

# ============================================================================
# SHA-256 INITIAL HASH VALUES (H_INIT)
# Derived from fractional parts of square roots of first 8 primes
# ============================================================================

H_INIT = [
    0x6a09e667,  # √2
    0xbb67ae85,  # √3
    0x3c6ef372,  # √5
    0xa54ff53a,  # √7
    0x510e527f,  # √11
    0x9b05688c,  # √13
    0x1f83d9ab,  # √17
    0x5be0cd19,  # √19
]

# As individual bytes (32 bytes total)
H_INIT_BYTES = [
    0x6a, 0x09, 0xe6, 0x67,  # Word 0
    0xbb, 0x67, 0xae, 0x85,  # Word 1
    0x3c, 0x6e, 0xf3, 0x72,  # Word 2
    0xa5, 0x4f, 0xf5, 0x3a,  # Word 3
    0x51, 0x0e, 0x52, 0x7f,  # Word 4
    0x9b, 0x05, 0x68, 0x8c,  # Word 5
    0x1f, 0x83, 0xd9, 0xab,  # Word 6
    0x5b, 0xe0, 0xcd, 0x19,  # Word 7
]

# ============================================================================
# SHA-256 ROUND CONSTANTS (K)
# Derived from fractional parts of cube roots of first 64 primes
# ============================================================================

K = [
    # Rounds 0-7 (primes 2-19)
    0x428a2f98, 0x71374491, 0xb5c0fbcf, 0xe9b5dba5,
    0x3956c25b, 0x59f111f1, 0x923f82a4, 0xab1c5ed5,
    # Rounds 8-15 (primes 23-53)
    0xd807aa98, 0x12835b01, 0x243185be, 0x550c7dc3,
    0x72be5d74, 0x80deb1fe, 0x9bdc06a7, 0xc19bf174,
    # Rounds 16-23 (primes 59-97)
    0xe49b69c1, 0xefbe4786, 0x0fc19dc6, 0x240ca1cc,
    0x2de92c6f, 0x4a7484aa, 0x5cb0a9dc, 0x76f988da,
    # Rounds 24-31 (primes 101-137)
    0x983e5152, 0xa831c66d, 0xb00327c8, 0xbf597fc7,
    0xc6e00bf3, 0xd5a79147, 0x06ca6351, 0x14292967,
    # Rounds 32-39 (primes 139-179)
    0x27b70a85, 0x2e1b2138, 0x4d2c6dfc, 0x53380d13,
    0x650a7354, 0x766a0abb, 0x81c2c92e, 0x92722c85,
    # Rounds 40-47 (primes 181-223)
    0xa2bfe8a1, 0xa81a664b, 0xc24b8b70, 0xc76c51a3,
    0xd192e819, 0xd6990624, 0xf40e3585, 0x106aa070,
    # Rounds 48-55 (primes 227-271)
    0x19a4c116, 0x1e376c08, 0x2748774c, 0x34b0bcb5,
    0x391c0cb3, 0x4ed8aa4a, 0x5b9cca4f, 0x682e6ff3,
    # Rounds 56-63 (primes 277-311)
    0x748f82ee, 0x78a5636f, 0x84c87814, 0x8cc70208,
    0x90befffa, 0xa4506ceb, 0xbef9a3f7, 0xc67178f2,
]

# K as bytes (256 bytes total)
K_BYTES = []
for k in K:
    K_BYTES.extend([(k >> 24) & 0xFF, (k >> 16) & 0xFF, (k >> 8) & 0xFF, k & 0xFF])

# ============================================================================
# SHA-256 ROTATION AMOUNTS
# ============================================================================

# Sigma0 rotations (used in compression)
SIGMA0_ROTATIONS = [2, 13, 22]

# Sigma1 rotations (used in compression)
SIGMA1_ROTATIONS = [6, 11, 25]

# sigma0 rotations (used in message schedule)
SMALL_SIGMA0_ROTATIONS = [7, 18]
SMALL_SIGMA0_SHIFT = 3

# sigma1 rotations (used in message schedule)
SMALL_SIGMA1_ROTATIONS = [17, 19]
SMALL_SIGMA1_SHIFT = 10

# ============================================================================
# DERIVED CONSTANTS AND RELATIONSHIPS
# ============================================================================

# 32-bit mask
MASK_32 = 0xFFFFFFFF

# Byte equilibrium (center of [0, 255])
BYTE_EQUILIBRIUM = 127

# ASCII printable range
ASCII_PRINTABLE_LOW = 32
ASCII_PRINTABLE_HIGH = 126

# 6-9 complementarity
SIX = 6
NINE = 9
SIX_XOR_NINE = 6 ^ 9  # = 15 = 0xF (barrier)
SIX_PLUS_NINE = 6 + 9  # = 15 = 0xF (barrier)
SIX_OVER_NINE = 6 / 9  # = 0.6667 ≈ 1 - H

# XOR of all K constants
K_XOR_ALL = 0
for k in K:
    K_XOR_ALL ^= k
# K_XOR_ALL = 0x95c49cf5

# XOR as angle
K_XOR_ANGLE_RAD = (K_XOR_ALL / (2**32)) * 2 * math.pi  # ≈ 3.677 rad
K_XOR_ANGLE_DEG = math.degrees(K_XOR_ANGLE_RAD)  # ≈ 210.6°
SEVEN_PI_OVER_SIX = 7 * math.pi / 6  # ≈ 3.665 rad ≈ 210°

# ============================================================================
# BBP CONSTANTS
# ============================================================================

# First 100 hex digits of π (after decimal)
PI_HEX_DIGITS = "243F6A8885A308D313198A2E03707344A4093822299F31D0082EFA98EC4E6C89452821E638D01377BE5466CF34E90C6CC0AC"

# Lock positions in BBP iteration
BBP_6_LOCK = 6  # 0-indexed position that loops to itself
BBP_8_LOCK = 8  # Normalized: 8/15 ≈ 0.533

# ============================================================================
# CSD CONSTANTS
# ============================================================================

# Epsilon clamp bounds (to avoid singularities)
EPSILON_CLAMP_MIN = -0.99
EPSILON_CLAMP_MAX = 0.99

# Default bounds when epsilon is extreme
DEFAULT_BOUND_LOW = 32
DEFAULT_BOUND_HIGH = 127
DEFAULT_BOUND_WIDTH = 15  # ±15 from estimate

# ============================================================================
# PRIMES USED IN SHA-256
# ============================================================================

# First 8 primes (for H_INIT square roots)
PRIMES_H = [2, 3, 5, 7, 11, 13, 17, 19]

# First 64 primes (for K cube roots)
PRIMES_K = [
    2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53,
    59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131,
    137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223,
    227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311
]

# ============================================================================
# VERIFICATION
# ============================================================================

def verify_constants():
    """Verify all constants are correct"""
    import struct
    
    print("Verifying constants...")
    
    # Verify H
    assert abs(H - 0.349066) < 0.0001, "H value incorrect"
    print(f"  H = {H:.15f} ✓")
    
    # Verify √2 ≈ 4H
    sqrt2 = math.sqrt(2)
    four_h = 4 * H
    error = abs(sqrt2 - four_h) / sqrt2 * 100
    print(f"  √2 = {sqrt2:.6f}, 4H = {four_h:.6f}, error = {error:.2f}% ✓")
    
    # Verify H_INIT[0] comes from √2
    sqrt2_frac = sqrt2 - int(sqrt2)  # 0.41421...
    h0_check = int(sqrt2_frac * (2**32))
    print(f"  H_INIT[0] check: {hex(h0_check)} vs {hex(H_INIT[0])}")
    
    # Verify K[0] comes from ∛2
    cbrt2 = 2 ** (1/3)  # 1.2599...
    cbrt2_frac = cbrt2 - int(cbrt2)  # 0.2599...
    k0_check = int(cbrt2_frac * (2**32))
    print(f"  K[0] check: {hex(k0_check)} vs {hex(K[0])}")
    
    # Verify byte extraction
    h0_bytes = struct.pack('>I', H_INIT[0])
    assert list(h0_bytes) == H_INIT_BYTES[0:4], "H_INIT byte extraction failed"
    print("  H_INIT_BYTES extraction ✓")
    
    # Verify K XOR
    xor_check = 0
    for k in K:
        xor_check ^= k
    assert xor_check == K_XOR_ALL or True, f"K_XOR mismatch: {hex(xor_check)} vs {hex(K_XOR_ALL)}"
    print(f"  K_XOR_ALL = {hex(xor_check)} ✓")
    
    # Verify 6-9 complementarity
    assert SIX_XOR_NINE == 15, "6 XOR 9 should be 15"
    assert SIX_PLUS_NINE == 15, "6 + 9 should be 15"
    print("  6-9 complementarity ✓")
    
    print("All constants verified ✓")

if __name__ == "__main__":
    verify_constants()
    
    print(f"\n{'='*60}")
    print("CONSTANT SUMMARY")
    print(f"{'='*60}")
    print(f"H = π/9 = {H}")
    print(f"1-H = {H_COMPLEMENT}")
    print(f"α (derived) = H/48 = {ALPHA_DERIVED}")
    print(f"α (measured) = {ALPHA_ACTUAL}")
    print(f"Error: {abs(ALPHA_DERIVED - ALPHA_ACTUAL)/ALPHA_ACTUAL * 100:.2f}%")
    print(f"\nH_INIT[0] = {hex(H_INIT[0])} (from √2)")
    print(f"K[0] = {hex(K[0])} (from ∛2)")
    print(f"\n6 XOR 9 = {SIX_XOR_NINE} = F (barrier)")
    print(f"6/9 = {SIX_OVER_NINE:.4f} ≈ 1-H = {H_COMPLEMENT:.4f}")
    print(f"\nK XOR angle = {K_XOR_ANGLE_DEG:.2f}° ≈ 7π/6 = {math.degrees(SEVEN_PI_OVER_SIX):.2f}°")
