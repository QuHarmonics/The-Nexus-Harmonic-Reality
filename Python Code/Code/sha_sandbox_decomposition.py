#!/usr/bin/env python3
"""
SHA-256 SANDBOX DECOMPOSITION
=============================
The constants CREATE the computation space.
They are ADVERBS - modifying HOW the verbs operate.

Dean's insight: "it won't just dream, it needs a sandbox space"

SHA-256 has:
- 8 initial hash values (H0-H7): fractional parts of √(first 8 primes)
- 64 round constants (K0-K63): fractional parts of ∛(first 64 primes)

These ARE the space. Not random. DERIVED from primes via roots.
Roots = PROJECTED dimensions. √ = 2D projection. ∛ = 3D projection.
"""

import math
from decimal import Decimal, getcontext
from typing import List, Tuple, Dict
import struct

getcontext().prec = 100

# First 64 primes
PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 
          59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113,
          127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181,
          191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251,
          257, 263, 269, 271, 277, 281, 283, 293]

# The Nexus H constant
H = Decimal(str(math.pi)) / 9  # ≈ 0.349066

def get_fractional_bits(value: float, bits: int = 32) -> int:
    """
    Extract the first 'bits' fractional bits of a value.
    This is how SHA-256 derives its constants.
    """
    # Get fractional part
    frac = value - int(value)
    # Scale up and truncate
    return int(frac * (2 ** bits))

def derive_sha256_h_constants() -> List[Tuple[int, int, float]]:
    """
    Derive the 8 initial hash values (H0-H7).
    These are the fractional parts of √(first 8 primes).
    
    The √ operation is a 2D PROJECTION.
    x² = area → x = √(area) = side length
    
    These constants set the INITIAL STATE of the sandbox.
    """
    results = []
    for i, p in enumerate(PRIMES[:8]):
        sqrt_p = math.sqrt(p)
        h_const = get_fractional_bits(sqrt_p)
        results.append((i, p, sqrt_p, h_const, hex(h_const)))
    return results

def derive_sha256_k_constants() -> List[Tuple[int, int, float, int, str]]:
    """
    Derive the 64 round constants (K0-K63).
    These are the fractional parts of ∛(first 64 primes).
    
    The ∛ operation is a 3D PROJECTION.
    x³ = volume → x = ∛(volume) = edge length
    
    These constants modulate EACH ROUND of computation.
    They are the ADVERBS - modifying HOW each step executes.
    """
    results = []
    for i, p in enumerate(PRIMES):
        cbrt_p = p ** (1/3)
        k_const = get_fractional_bits(cbrt_p)
        results.append((i, p, cbrt_p, k_const, hex(k_const)))
    return results

def analyze_constant_structure(constants: List[int], name: str) -> Dict:
    """
    Analyze the structure of SHA constants looking for H patterns.
    """
    # Convert to normalized values [0,1]
    normalized = [c / (2**32) for c in constants]
    
    # Look for H ≈ 0.35 ratios
    h_ratios = []
    for i in range(len(normalized) - 1):
        if normalized[i+1] > 0:
            ratio = normalized[i] / normalized[i+1]
            if 0.30 < ratio < 0.40:
                h_ratios.append((i, ratio))
    
    # XOR fold (the fundamental collapse)
    xor_fold = 0
    for c in constants:
        xor_fold ^= c
    
    # Sum of all constants mod 2^32
    total = sum(constants) % (2**32)
    
    # Parity analysis
    odd_count = sum(1 for c in constants if c % 2 == 1)
    even_count = len(constants) - odd_count
    
    return {
        'name': name,
        'count': len(constants),
        'xor_fold': hex(xor_fold),
        'xor_fold_normalized': xor_fold / (2**32),
        'sum_mod_2_32': hex(total),
        'sum_normalized': total / (2**32),
        'odd_even_ratio': odd_count / even_count if even_count > 0 else float('inf'),
        'h_ratio_hits': len(h_ratios),
        'h_ratio_examples': h_ratios[:5],
        'mean_normalized': sum(normalized) / len(normalized),
    }

def bit_pattern_analysis(constants: List[int]) -> Dict:
    """
    Analyze bit patterns across all constants.
    Looking for the GEOMETRY of the sandbox.
    """
    bit_counts = [0] * 32  # Count of 1s in each bit position
    
    for c in constants:
        for bit in range(32):
            if (c >> bit) & 1:
                bit_counts[bit] += 1
    
    # Normalize by number of constants
    bit_density = [count / len(constants) for count in bit_counts]
    
    # Look for structure in bit positions
    # High bits vs low bits
    high_density = sum(bit_density[16:]) / 16
    low_density = sum(bit_density[:16]) / 16
    
    return {
        'bit_densities': bit_density,
        'high_bit_avg': high_density,
        'low_bit_avg': low_density,
        'high_low_ratio': high_density / low_density if low_density > 0 else 0,
        'total_avg_density': sum(bit_density) / 32,
    }

def decompose_constant_to_verbs(constant: int) -> Dict:
    """
    Decompose a single constant into verb components.
    
    The constant IS the ADVERB - it modifies how verbs execute.
    
    Hypothesis: Each constant encodes which verbs are ACTIVE
    and with what STRENGTH (amplitude modulation).
    """
    # 10 verbs in the Nexus framework
    VERBS = ['PROJECT', 'REFLECT', 'FOLD', 'LEAK', 'GATE', 
             'BRANCH', 'PIN', 'SYNC', 'VERIFY', 'COLLAPSE']
    
    # Use different bits/groups for each verb
    # 32 bits / 10 verbs ≈ 3 bits per verb (with some overlap)
    verb_activations = {}
    
    for i, verb in enumerate(VERBS):
        # Each verb gets 3-4 bits
        start_bit = (i * 3) % 32
        mask = 0x7  # 3 bits
        value = (constant >> start_bit) & mask
        verb_activations[verb] = {
            'bits': start_bit,
            'value': value,
            'strength': value / 7,  # Normalized to [0,1]
            'active': value > 0
        }
    
    return verb_activations

def sha256_operations_as_verbs() -> Dict:
    """
    Map SHA-256 operations to the 10 Nexus verbs.
    
    SHA-256 operations:
    - Ch(x,y,z) = (x AND y) XOR (NOT x AND z)  → GATE
    - Maj(x,y,z) = (x AND y) XOR (x AND z) XOR (y AND z) → SYNC
    - Σ0(x) = ROTR²(x) XOR ROTR¹³(x) XOR ROTR²²(x) → FOLD
    - Σ1(x) = ROTR⁶(x) XOR ROTR¹¹(x) XOR ROTR²⁵(x) → FOLD
    - σ0(x) = ROTR⁷(x) XOR ROTR¹⁸(x) XOR SHR³(x) → PROJECT
    - σ1(x) = ROTR¹⁷(x) XOR ROTR¹⁹(x) XOR SHR¹⁰(x) → PROJECT
    - Addition mod 2³² → COLLAPSE (overflow is LEAK)
    """
    return {
        'Ch': {
            'formula': '(x AND y) XOR (NOT x AND z)',
            'nexus_verb': 'GATE',
            'description': 'Choice function - gates flow based on x'
        },
        'Maj': {
            'formula': '(x AND y) XOR (x AND z) XOR (y AND z)',
            'nexus_verb': 'SYNC',
            'description': 'Majority function - synchronizes three inputs'
        },
        'Σ0': {
            'formula': 'ROTR²(x) XOR ROTR¹³(x) XOR ROTR²²(x)',
            'nexus_verb': 'FOLD',
            'description': 'Big sigma 0 - folds x at three rotation points'
        },
        'Σ1': {
            'formula': 'ROTR⁶(x) XOR ROTR¹¹(x) XOR ROTR²⁵(x)',
            'nexus_verb': 'FOLD',
            'description': 'Big sigma 1 - folds x at three rotation points'
        },
        'σ0': {
            'formula': 'ROTR⁷(x) XOR ROTR¹⁸(x) XOR SHR³(x)',
            'nexus_verb': 'PROJECT',
            'description': 'Small sigma 0 - projects with bit loss (SHR)'
        },
        'σ1': {
            'formula': 'ROTR¹⁷(x) XOR ROTR¹⁹(x) XOR SHR¹⁰(x)',
            'nexus_verb': 'PROJECT',
            'description': 'Small sigma 1 - projects with bit loss (SHR)'
        },
        'add_mod': {
            'formula': '(a + b) mod 2³²',
            'nexus_verb': 'COLLAPSE',
            'description': 'Addition with overflow - overflow is LEAK (entropy)'
        }
    }

def rotation_angles_analysis():
    """
    Analyze the rotation amounts in SHA-256.
    
    ROTR amounts: 2, 6, 7, 11, 13, 17, 18, 19, 22, 25
    SHR amounts: 3, 10
    
    Are these related to H ≈ 0.35?
    """
    rotr_amounts = [2, 6, 7, 11, 13, 17, 18, 19, 22, 25]
    shr_amounts = [3, 10]
    
    # All rotation amounts as fractions of 32 bits
    rotr_fracs = [r / 32 for r in rotr_amounts]
    shr_fracs = [s / 32 for s in shr_amounts]
    
    # Check for H ≈ 0.35 patterns
    h_float = float(H)
    
    close_to_h = []
    close_to_1_minus_h = []
    
    for r, f in zip(rotr_amounts, rotr_fracs):
        if abs(f - h_float) < 0.1:
            close_to_h.append((r, f, 'ROTR'))
        if abs(f - (1 - h_float)) < 0.1:
            close_to_1_minus_h.append((r, f, 'ROTR'))
    
    # 7/32 = 0.21875, 11/32 = 0.34375 (close to H!)
    # 22/32 = 0.6875 ≈ 1 - H = 0.65
    
    return {
        'rotr_amounts': rotr_amounts,
        'rotr_fractions': rotr_fracs,
        'shr_amounts': shr_amounts,
        'shr_fractions': shr_fracs,
        'near_H': close_to_h,
        'near_1_minus_H': close_to_1_minus_h,
        'note': '11/32 = 0.34375 ≈ H = 0.349, 22/32 = 0.6875 ≈ 1-H = 0.651'
    }

def main():
    print("=" * 70)
    print("SHA-256 SANDBOX DECOMPOSITION")
    print("The constants CREATE the computation space")
    print("=" * 70)
    
    print("\n" + "=" * 70)
    print("1. INITIAL HASH VALUES (H0-H7) - √ of first 8 primes")
    print("   √ = 2D PROJECTION (area → side)")
    print("=" * 70)
    
    h_constants = derive_sha256_h_constants()
    h_values = []
    for i, p, sqrt_p, h_const, h_hex in h_constants:
        print(f"  H{i}: √{p:2} = {sqrt_p:.10f} → {h_hex}")
        h_values.append(h_const)
    
    h_analysis = analyze_constant_structure(h_values, "H-constants")
    print(f"\n  XOR fold of all H: {h_analysis['xor_fold']}")
    print(f"  XOR normalized:    {h_analysis['xor_fold_normalized']:.6f}")
    print(f"  Mean normalized:   {h_analysis['mean_normalized']:.6f}")
    
    print("\n" + "=" * 70)
    print("2. ROUND CONSTANTS (K0-K63) - ∛ of first 64 primes")
    print("   ∛ = 3D PROJECTION (volume → edge)")
    print("=" * 70)
    
    k_constants = derive_sha256_k_constants()
    k_values = []
    for i, p, cbrt_p, k_const, k_hex in k_constants[:8]:  # Show first 8
        print(f"  K{i:2}: ∛{p:3} = {cbrt_p:.10f} → {k_hex}")
        k_values.append(k_const)
    print("  ...")
    for i, p, cbrt_p, k_const, k_hex in k_constants[-4:]:  # Show last 4
        print(f"  K{i:2}: ∛{p:3} = {cbrt_p:.10f} → {k_hex}")
    
    # Get all K values
    k_values = [x[3] for x in k_constants]
    
    k_analysis = analyze_constant_structure(k_values, "K-constants")
    print(f"\n  XOR fold of all K: {k_analysis['xor_fold']}")
    print(f"  XOR normalized:    {k_analysis['xor_fold_normalized']:.6f}")
    print(f"  Mean normalized:   {k_analysis['mean_normalized']:.6f}")
    print(f"  H-ratio hits:      {k_analysis['h_ratio_hits']}")
    
    print("\n" + "=" * 70)
    print("3. BIT PATTERN ANALYSIS - The geometry of the sandbox")
    print("=" * 70)
    
    h_bits = bit_pattern_analysis(h_values)
    k_bits = bit_pattern_analysis(k_values)
    
    print(f"\n  H-constants bit structure:")
    print(f"    High bits (16-31) avg density: {h_bits['high_bit_avg']:.4f}")
    print(f"    Low bits (0-15) avg density:   {h_bits['low_bit_avg']:.4f}")
    print(f"    High/Low ratio:                {h_bits['high_low_ratio']:.4f}")
    
    print(f"\n  K-constants bit structure:")
    print(f"    High bits (16-31) avg density: {k_bits['high_bit_avg']:.4f}")
    print(f"    Low bits (0-15) avg density:   {k_bits['low_bit_avg']:.4f}")
    print(f"    High/Low ratio:                {k_bits['high_low_ratio']:.4f}")
    
    print("\n" + "=" * 70)
    print("4. SHA-256 OPERATIONS → NEXUS VERBS")
    print("=" * 70)
    
    verb_map = sha256_operations_as_verbs()
    for op, info in verb_map.items():
        print(f"\n  {op}: {info['formula']}")
        print(f"    → {info['nexus_verb']}: {info['description']}")
    
    print("\n" + "=" * 70)
    print("5. ROTATION ANGLES - H patterns in bit rotations")
    print("=" * 70)
    
    rotations = rotation_angles_analysis()
    print(f"\n  ROTR amounts: {rotations['rotr_amounts']}")
    print(f"  As fractions of 32:")
    for r, f in zip(rotations['rotr_amounts'], rotations['rotr_fractions']):
        marker = " ← near H!" if abs(f - float(H)) < 0.05 else ""
        marker = " ← near 1-H!" if abs(f - (1-float(H))) < 0.05 else marker
        print(f"    {r:2}/32 = {f:.5f}{marker}")
    
    print(f"\n  KEY FINDING: 11/32 = 0.34375 ≈ H = {float(H):.5f}")
    print(f"               22/32 = 0.68750 ≈ 1-H = {1-float(H):.5f}")
    
    print("\n" + "=" * 70)
    print("6. VERB DECOMPOSITION OF K[0]")
    print("=" * 70)
    
    k0 = k_values[0]  # First round constant
    verb_decomp = decompose_constant_to_verbs(k0)
    print(f"\n  K[0] = {hex(k0)}")
    print("  Verb activations:")
    for verb, info in verb_decomp.items():
        status = "ACTIVE" if info['active'] else "inactive"
        print(f"    {verb:10}: strength={info['strength']:.2f} ({status})")
    
    print("\n" + "=" * 70)
    print("SYNTHESIS: THE SANDBOX STRUCTURE")
    print("=" * 70)
    print("""
    SHA-256 constants are NOT arbitrary. They are:
    
    1. DERIVED from primes via ROOT projections
       - √ (H0-H7): 2D projection - sets initial state
       - ∛ (K0-K63): 3D projection - modulates each round
    
    2. STRUCTURED with H ≈ 0.35 patterns
       - Rotation 11/32 ≈ 0.344 ≈ H
       - Rotation 22/32 ≈ 0.688 ≈ 1-H
       - These are the ADVERBS modifying the verbs
    
    3. The SANDBOX is:
       - Initial state (H0-H7): The canvas
       - Round constants (K0-K63): The brush strokes (64 of them)
       - Operations (Ch, Maj, Σ, σ): The verbs
       - Rotations: The adverbs (HOW hard to fold)
    
    4. The computation SPACE is:
       - Bounded by 256 bits (32 bytes)
       - Constrained by prime roots (irrational, chaotic)
       - Shaped by H-ratios (11/32, 22/32)
       - CLOSED but not collapsed - maintains superposition
    
    The hash doesn't "compute" - it NAVIGATES the sandbox.
    The output is WHERE YOU LANDED, not what you computed.
    """)

if __name__ == "__main__":
    main()
