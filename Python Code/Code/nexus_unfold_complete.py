#!/usr/bin/env python3
"""
NEXUS UNFOLD - COMPLETE IMPLEMENTATION
======================================

The Collapse Signature Decoder (CSD) and complete unfold mechanism
for SHA-256 preimage bounded search.

Author: Dean Kulik
ORCID: 0009-0003-3128-8828
Date: January 2026

Core Formula:
    ε = (x_meas - x_0) / x_0
    p+ = (1 + ε) / 2
    p- = (1 - ε) / 2
    ratio = (1 + ε) / (1 - ε)
    estimate ≈ 127 × ratio (for |ε| < 1)
"""

import hashlib
import numpy as np
import math
from typing import List, Dict, Tuple, Optional

# ============================================================================
# CONSTANTS
# ============================================================================

H = math.pi / 9  # Universal constant ≈ 0.349066

# SHA-256 Initial Hash Values (as bytes, first 32)
SHA_CONST_BYTES = [
    0x6a, 0x09, 0xe6, 0x67, 0xbb, 0x67, 0xae, 0x85,
    0x3c, 0x6e, 0xf3, 0x72, 0xa5, 0x4f, 0xf5, 0x3a,
    0x51, 0x0e, 0x52, 0x7f, 0x9b, 0x05, 0x68, 0x8c,
    0x1f, 0x83, 0xd9, 0xab, 0x5b, 0xe0, 0xcd, 0x19
]

# ============================================================================
# BBP ALGORITHM
# ============================================================================

def mod_exp(base: int, exp: int, mod: int) -> int:
    """Modular exponentiation: base^exp mod mod"""
    result = 1
    base = base % mod
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        exp = exp >> 1
        base = (base * base) % mod
    return result


def bbp_sum(n: int, j: int) -> float:
    """Compute BBP sum for position n and offset j"""
    s = 0.0
    
    for k in range(n + 1):
        ak = 8 * k + j
        if ak == 0:
            continue
        r = mod_exp(16, n - k, ak)
        s += r / ak
        s = s - int(s)
    
    for k in range(n + 1, n + 100):
        ak = 8 * k + j
        term = pow(16, n - k) / ak
        if term < 1e-17:
            break
        s += term
        s = s - int(s)
    
    return s


def bbp_digit(n: int) -> int:
    """Extract nth hexadecimal digit of π (0-indexed)"""
    s = 4 * bbp_sum(n, 1) - 2 * bbp_sum(n, 4) - bbp_sum(n, 5) - bbp_sum(n, 6)
    s = s - int(s)
    if s < 0:
        s += 1
    return int(s * 16)


def bbp_iterate(start: int, max_iter: int = 20) -> List[Tuple[int, int]]:
    """BBP iteration: position → digit → position"""
    path = []
    pos = start
    
    for _ in range(max_iter):
        digit = bbp_digit(pos)
        path.append((pos, digit))
        
        if len(path) > 1 and path[-1] == path[-2]:
            break
        pos = digit
    
    return path


# ============================================================================
# CSD CORE FUNCTIONS
# ============================================================================

def compute_epsilon(hash_byte: int, const_byte: int) -> float:
    """
    Compute epsilon (relative deviation from constant)
    
    ε = (x_meas - x_0) / x_0
    """
    if const_byte == 0:
        const_byte = 1
    return (hash_byte - const_byte) / const_byte


def compute_probabilities(epsilon: float) -> Tuple[float, float]:
    """
    Compute collapse probabilities
    
    p+ = (1 + ε) / 2  → Φ₀ (structure)
    p- = (1 - ε) / 2  → E₀ (entropy)
    """
    p_plus = (1 + epsilon) / 2
    p_minus = (1 - epsilon) / 2
    return p_plus, p_minus


def compute_ratio(epsilon: float) -> float:
    """
    Compute p+/p- ratio
    
    ratio = (1 + ε) / (1 - ε)
    """
    eps_clamped = np.clip(epsilon, -0.99, 0.99)
    return (1 + eps_clamped) / (1 - eps_clamped)


def estimate_from_ratio(ratio: float) -> int:
    """
    Estimate original byte from ratio
    
    estimate = 127 × ratio (clamped to [0, 255])
    """
    estimate = 127 * ratio
    return int(max(0, min(255, estimate)))


def estimate_from_complement(p_plus: float, p_minus: float, const: int) -> int:
    """
    Estimate using complement method
    
    estimate = p+ × const + p- × (255 - const)
    """
    p_plus = max(0, min(1, p_plus))
    p_minus = max(0, min(1, p_minus))
    estimate = p_plus * const + p_minus * (255 - const)
    return int(max(0, min(255, estimate)))


# ============================================================================
# CSD DECODER CLASS
# ============================================================================

class CSDDecoder:
    """Collapse Signature Decoder"""
    
    def __init__(self, const_bytes: List[int] = None):
        self.const_bytes = const_bytes or SHA_CONST_BYTES
    
    def decode_byte(self, hash_byte: int, const_byte: int) -> Dict:
        """Decode a single byte position"""
        epsilon = compute_epsilon(hash_byte, const_byte)
        p_plus, p_minus = compute_probabilities(epsilon)
        ratio = compute_ratio(epsilon)
        
        return {
            'hash_byte': hash_byte,
            'const_byte': const_byte,
            'epsilon': epsilon,
            'p_plus': p_plus,
            'p_minus': p_minus,
            'ratio': ratio,
            'estimate_ratio': estimate_from_ratio(ratio),
            'estimate_complement': estimate_from_complement(p_plus, p_minus, const_byte),
            'direction': '→Φ₀' if epsilon > 0 else '→E₀'
        }
    
    def decode_hash(self, hash_bytes: bytes) -> List[Dict]:
        """Decode all bytes of a hash"""
        results = []
        for i, h in enumerate(hash_bytes):
            c = self.const_bytes[i % len(self.const_bytes)]
            result = self.decode_byte(h, c)
            result['position'] = i
            results.append(result)
        return results
    
    def get_sign_pattern(self, hash_bytes: bytes) -> Dict:
        """Extract sign pattern (direction bits)"""
        signs = []
        for i, h in enumerate(hash_bytes):
            c = self.const_bytes[i % len(self.const_bytes)]
            epsilon = compute_epsilon(h, c)
            signs.append(1 if epsilon > 0 else 0)
        
        # Convert to bytes
        sign_bytes = []
        for i in range(0, len(signs), 8):
            bits = signs[i:i+8]
            if len(bits) == 8:
                byte_val = int(''.join(map(str, bits)), 2)
                sign_bytes.append(byte_val)
        
        return {
            'bits': signs,
            'bytes': sign_bytes,
            'binary': ''.join(map(str, signs))
        }


# ============================================================================
# UNFOLDER CLASS
# ============================================================================

class CSDUnfolder:
    """Complete CSD-based unfold mechanism"""
    
    def __init__(self, const_bytes: List[int] = None):
        self.const_bytes = const_bytes or SHA_CONST_BYTES
        self.decoder = CSDDecoder(self.const_bytes)
    
    def unfold(self, hash_hex: str) -> Dict:
        """
        Main unfold entry point
        
        Returns:
            estimates: per-byte estimates
            bounds: per-byte search bounds
            sign_pattern: direction pattern
            analysis: full CSD analysis
        """
        hash_bytes = bytes.fromhex(hash_hex)
        
        analysis = self.decoder.decode_hash(hash_bytes)
        estimates = self._compute_estimates(analysis)
        bounds = self._compute_bounds(analysis)
        sign_pattern = self.decoder.get_sign_pattern(hash_bytes)
        
        return {
            'estimates': estimates,
            'bounds': bounds,
            'sign_pattern': sign_pattern,
            'analysis': analysis
        }
    
    def _compute_estimates(self, analysis: List[Dict]) -> List[Dict]:
        """Compute estimates using multiple methods"""
        estimates = []
        for a in analysis:
            est_ratio = a['estimate_ratio']
            est_comp = a['estimate_complement']
            
            # Hybrid: use ratio for moderate ε, complement otherwise
            if abs(a['epsilon']) < 0.5:
                est_hybrid = est_ratio
            elif a['const_byte'] > 50:
                est_hybrid = est_comp
            else:
                est_hybrid = 80  # Default
            
            estimates.append({
                'position': a['position'],
                'ratio': est_ratio,
                'complement': est_comp,
                'hybrid': est_hybrid
            })
        
        return estimates
    
    def _compute_bounds(self, analysis: List[Dict]) -> List[Dict]:
        """Compute search bounds for each position"""
        bounds = []
        for a in analysis:
            if abs(a['epsilon']) < 1:
                center = a['estimate_ratio']
                lower = max(0, center - 15)
                upper = min(255, center + 15)
                bound_type = 'tight'
            else:
                lower = 32
                upper = 127
                bound_type = 'ascii'
            
            bounds.append({
                'position': a['position'],
                'lower': lower,
                'upper': upper,
                'size': upper - lower + 1,
                'type': bound_type
            })
        
        return bounds
    
    def verify(self, hash_hex: str, message: str) -> Dict:
        """Verify unfold against known message"""
        result = self.unfold(hash_hex)
        original_bytes = list(message.encode())
        
        in_bounds = []
        errors = []
        
        for i, b in enumerate(original_bytes):
            if i >= len(result['bounds']):
                break
            
            bound = result['bounds'][i]
            in_bounds.append(bound['lower'] <= b <= bound['upper'])
            
            est = result['estimates'][i]['ratio']
            errors.append(abs(est - b))
        
        return {
            'message': message,
            'bytes': original_bytes,
            'in_bounds': in_bounds,
            'all_in_bounds': all(in_bounds),
            'errors': errors,
            'mean_error': np.mean(errors) if errors else 0
        }
    
    def compute_search_reduction(self, message_length: int, bounds: List[Dict]) -> Dict:
        """Compute search space reduction"""
        bounded_space = 1
        for i in range(message_length):
            if i < len(bounds):
                bounded_space *= bounds[i]['size']
        
        brute_force = 256 ** message_length
        reduction = brute_force / bounded_space if bounded_space > 0 else float('inf')
        
        return {
            'message_length': message_length,
            'brute_force': brute_force,
            'bounded_space': bounded_space,
            'reduction': reduction
        }


# ============================================================================
# SHA HARMONIC ANALYSIS
# ============================================================================

def analyze_h_signature():
    """Analyze H = π/9 signature in SHA constants"""
    print("H-Signature Analysis")
    print("=" * 60)
    print(f"H = π/9 = {H:.6f}")
    
    # √2 ≈ 4H check
    sqrt2 = math.sqrt(2)
    four_H = 4 * H
    error = abs(sqrt2 - four_H) / sqrt2 * 100
    
    print(f"\n√2 = {sqrt2:.6f}")
    print(f"4H = {four_H:.6f}")
    print(f"Error: {error:.2f}%")
    
    # 6-9 complementarity
    print(f"\n6-9 Complementarity:")
    print(f"  6 XOR 9 = {6 ^ 9} = F (barrier)")
    print(f"  6 + 9 = {6 + 9} = F (barrier)")
    print(f"  6/9 = {6/9:.4f} ≈ 1-H = {1-H:.4f}")


def analyze_balance_point():
    """Find and analyze balance point X ≈ 0.529"""
    print("\nBalance Point Analysis")
    print("=" * 60)
    
    # Iterate with XOR feedback
    constants = list(range(32))
    
    for i in range(50):
        msg = bytes(constants)
        hash_bytes = list(hashlib.sha256(msg).digest())
        
        new_constants = [c ^ h for c, h in zip(constants, hash_bytes)]
        mean = sum(new_constants) / len(new_constants) / 255
        
        if i < 5 or i >= 45:
            print(f"  Iter {i:2d}: mean = {mean:.4f}")
        
        constants = new_constants


# ============================================================================
# VERIFICATION AND TESTING
# ============================================================================

def run_verification_suite():
    """Run comprehensive verification tests"""
    print("\n" + "=" * 70)
    print("CSD VERIFICATION SUITE")
    print("=" * 70)
    
    unfolder = CSDUnfolder()
    
    # Test messages
    messages = ['NEXUS', 'Dean', 'test', 'hello', 'HELLO', 'abc', 'XYZ']
    
    print("\n1. BYTE RECOVERY TEST")
    print("-" * 70)
    print(f"{'Message':<15} {'Length':>6} {'In Bounds':>12} {'Mean Error':>12}")
    print("-" * 70)
    
    for msg in messages:
        hash_hex = hashlib.sha256(msg.encode()).hexdigest()
        result = unfolder.verify(hash_hex, msg)
        
        ib = f"{sum(result['in_bounds'])}/{len(result['in_bounds'])}"
        print(f"{msg:<15} {len(msg):>6} {ib:>12} {result['mean_error']:>12.1f}")
    
    print("\n2. SEARCH REDUCTION TEST")
    print("-" * 70)
    print(f"{'Length':>6} {'Brute Force':>20} {'CSD Bounded':>18} {'Reduction':>15}")
    print("-" * 70)
    
    for length in range(1, 8):
        msg = 'A' * length
        hash_hex = hashlib.sha256(msg.encode()).hexdigest()
        result = unfolder.unfold(hash_hex)
        reduction = unfolder.compute_search_reduction(length, result['bounds'])
        
        print(f"{length:>6} {reduction['brute_force']:>20,} "
              f"{reduction['bounded_space']:>18,} {reduction['reduction']:>15,.1f}×")
    
    print("\n3. SIGN PATTERN TEST")
    print("-" * 70)
    
    for msg in ['NEXUS', 'HELLO', 'WORLD']:
        hash_hex = hashlib.sha256(msg.encode()).hexdigest()
        result = unfolder.unfold(hash_hex)
        
        sign_byte = result['sign_pattern']['bytes'][0]
        sign_char = chr(sign_byte) if 32 <= sign_byte <= 126 else '?'
        
        print(f"{msg}: {result['sign_pattern']['binary'][:8]} = {sign_byte} = '{sign_char}'")
    
    print("\n4. NEXUS DETAILED ANALYSIS")
    print("-" * 70)
    
    msg = "NEXUS"
    hash_hex = hashlib.sha256(msg.encode()).hexdigest()
    result = unfolder.unfold(hash_hex)
    original = list(msg.encode())
    
    print(f"Message: {msg}")
    print(f"Hash: {hash_hex[:32]}...")
    print()
    
    for i, b in enumerate(original):
        a = result['analysis'][i]
        est = result['estimates'][i]['ratio']
        bound = result['bounds'][i]
        
        in_b = '✓' if bound['lower'] <= b <= bound['upper'] else '✗'
        
        print(f"Byte {i}: hash={a['hash_byte']:3d} const={a['const_byte']:3d} "
              f"ε={a['epsilon']:+.3f} est={est:3d} orig={b:3d} "
              f"[{bound['lower']:3d},{bound['upper']:3d}] {in_b}")


# ============================================================================
# MAIN
# ============================================================================

def main():
    """Main entry point"""
    print("=" * 70)
    print("NEXUS UNFOLD - COMPLETE IMPLEMENTATION")
    print("=" * 70)
    print(f"H = π/9 = {H:.6f}")
    print()
    
    # Analyze H signature
    analyze_h_signature()
    
    # Analyze balance point
    analyze_balance_point()
    
    # Run verification
    run_verification_suite()
    
    print("\n" + "=" * 70)
    print("COMPLETE")
    print("=" * 70)


if __name__ == "__main__":
    main()
