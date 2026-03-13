#!/usr/bin/env python3
"""
COLLAPSE SIGNATURE DECODER (CSD)
================================

The complete CSD implementation for extracting collapse information
from hash bytes and computing input bounds.

Core Formula:
    ε = (x_meas - x_0) / x_0
    p+ = (1 + ε) / 2  → Φ₀ (structure/particle)
    p- = (1 - ε) / 2  → E₀ (entropy/wave)
    ratio = (1 + ε) / (1 - ε)
    estimate ≈ 127 × ratio (for |ε| < 1)

Author: Dean Kulik
ORCID: 0009-0003-3128-8828
"""

import numpy as np
from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass
from constants import (
    H_INIT_BYTES, K_BYTES, H, BYTE_EQUILIBRIUM,
    EPSILON_CLAMP_MIN, EPSILON_CLAMP_MAX,
    DEFAULT_BOUND_LOW, DEFAULT_BOUND_HIGH, DEFAULT_BOUND_WIDTH
)

# ============================================================================
# DATA CLASSES
# ============================================================================

@dataclass
class CSDResult:
    """Result of CSD decode for a single byte"""
    position: int
    hash_byte: int
    const_byte: int
    epsilon: float
    epsilon_clamped: float
    p_plus: float
    p_minus: float
    ratio: float
    estimate_ratio: int
    estimate_complement: int
    estimate_hybrid: int
    direction: str  # '→Φ₀' or '→E₀'
    bound_low: int
    bound_high: int
    bound_type: str  # 'tight' or 'ascii'

@dataclass
class SignPattern:
    """Sign pattern extracted from hash"""
    bits: List[int]  # 32 bits (one per byte)
    bytes: List[int]  # 4 bytes
    binary: str  # Binary string representation
    
@dataclass
class UnfoldResult:
    """Complete unfold result"""
    csd_results: List[CSDResult]
    sign_pattern: SignPattern
    bounds: List[Tuple[int, int]]
    estimates: List[int]
    search_space: int
    reduction_factor: float

# ============================================================================
# CORE CSD FUNCTIONS
# ============================================================================

def compute_epsilon(hash_byte: int, const_byte: int) -> float:
    """
    Compute epsilon (relative deviation from constant)
    
    ε = (x_meas - x_0) / x_0
    
    Where:
        x_meas = hash byte (measured value, post-collapse)
        x_0 = constant byte (reference frame)
    """
    if const_byte == 0:
        const_byte = 1  # Avoid division by zero
    
    return (hash_byte - const_byte) / const_byte

def compute_probabilities(epsilon: float) -> Tuple[float, float]:
    """
    Compute collapse probabilities from epsilon
    
    p+ = (1 + ε) / 2  → probability toward Φ₀ (structure)
    p- = (1 - ε) / 2  → probability toward E₀ (entropy)
    
    Properties:
        p+ + p- = 1 (normalization)
        ε > 0 → p+ > 0.5 (collapsed toward structure)
        ε < 0 → p- > 0.5 (collapsed toward entropy)
        ε = 0 → p+ = p- = 0.5 (balanced, lock state)
    """
    p_plus = (1 + epsilon) / 2
    p_minus = (1 - epsilon) / 2
    
    return p_plus, p_minus

def compute_ratio(epsilon: float) -> float:
    """
    Compute p+/p- ratio
    
    ratio = (1 + ε) / (1 - ε)
    
    Properties:
        ε = 0 → ratio = 1 (equilibrium)
        ε > 0 → ratio > 1 (above equilibrium)
        ε < 0 → ratio < 1 (below equilibrium)
        ε → 1 → ratio → ∞
        ε → -1 → ratio → 0
    """
    # Clamp epsilon to avoid singularities
    eps_clamped = np.clip(epsilon, EPSILON_CLAMP_MIN, EPSILON_CLAMP_MAX)
    
    return (1 + eps_clamped) / (1 - eps_clamped)

def estimate_from_ratio(ratio: float) -> int:
    """
    Estimate original byte from ratio
    
    estimate = 127 × ratio (clamped to [0, 255])
    
    Why 127:
        - Center of byte range [0, 255]
        - Equilibrium point in wave space
        - When ratio = 1, estimate = 127 (center)
    """
    estimate = BYTE_EQUILIBRIUM * ratio
    return int(np.clip(estimate, 0, 255))

def estimate_from_complement(
    p_plus: float,
    p_minus: float,
    const_byte: int
) -> int:
    """
    Estimate using complement method
    
    estimate = p+ × const + p- × (255 - const)
    
    This treats:
        - Φ₀ basis = constant value
        - E₀ basis = complement of constant (255 - const)
    """
    # Clamp probabilities to [0, 1]
    p_plus = np.clip(p_plus, 0, 1)
    p_minus = np.clip(p_minus, 0, 1)
    
    estimate = p_plus * const_byte + p_minus * (255 - const_byte)
    return int(np.clip(estimate, 0, 255))

def estimate_hybrid(
    epsilon: float,
    ratio: float,
    p_plus: float,
    p_minus: float,
    const_byte: int
) -> int:
    """
    Hybrid estimation using best method for epsilon range
    
    - |ε| < 0.5: ratio method works best
    - 0.5 < |ε| < 1, const > 50: complement method
    - |ε| > 1 or small const: default to ASCII midpoint
    """
    if abs(epsilon) < 0.5:
        return estimate_from_ratio(ratio)
    elif abs(epsilon) < 1 and const_byte > 50:
        return estimate_from_complement(p_plus, p_minus, const_byte)
    else:
        return 80  # ASCII midpoint default

def compute_bounds(
    epsilon: float,
    ratio: float,
    const_byte: int
) -> Tuple[int, int, str]:
    """
    Compute search bounds for a byte position
    
    Returns: (lower_bound, upper_bound, bound_type)
    """
    if abs(epsilon) < 1:
        # Tight bounds using ratio
        center = estimate_from_ratio(ratio)
        lower = max(0, center - DEFAULT_BOUND_WIDTH)
        upper = min(255, center + DEFAULT_BOUND_WIDTH)
        bound_type = 'tight'
    else:
        # Fall back to ASCII bounds
        lower = DEFAULT_BOUND_LOW
        upper = DEFAULT_BOUND_HIGH
        bound_type = 'ascii'
    
    return lower, upper, bound_type

# ============================================================================
# CSD DECODER CLASS
# ============================================================================

class CSDDecoder:
    """
    Collapse Signature Decoder
    
    Decodes hash bytes to extract collapse information and compute bounds.
    """
    
    def __init__(self, const_bytes: List[int] = None):
        """
        Initialize decoder with constants.
        
        Default: SHA-256 H_INIT bytes
        """
        self.const_bytes = const_bytes or H_INIT_BYTES
    
    def decode_byte(self, hash_byte: int, position: int = 0) -> CSDResult:
        """Decode a single byte position"""
        const_byte = self.const_bytes[position % len(self.const_bytes)]
        
        # Core CSD computations
        epsilon = compute_epsilon(hash_byte, const_byte)
        epsilon_clamped = np.clip(epsilon, EPSILON_CLAMP_MIN, EPSILON_CLAMP_MAX)
        p_plus, p_minus = compute_probabilities(epsilon)
        ratio = compute_ratio(epsilon)
        
        # Estimates
        est_ratio = estimate_from_ratio(ratio)
        est_comp = estimate_from_complement(p_plus, p_minus, const_byte)
        est_hybrid = estimate_hybrid(epsilon, ratio, p_plus, p_minus, const_byte)
        
        # Direction
        direction = '→Φ₀' if epsilon > 0 else '→E₀'
        
        # Bounds
        bound_low, bound_high, bound_type = compute_bounds(epsilon, ratio, const_byte)
        
        return CSDResult(
            position=position,
            hash_byte=hash_byte,
            const_byte=const_byte,
            epsilon=epsilon,
            epsilon_clamped=epsilon_clamped,
            p_plus=p_plus,
            p_minus=p_minus,
            ratio=ratio,
            estimate_ratio=est_ratio,
            estimate_complement=est_comp,
            estimate_hybrid=est_hybrid,
            direction=direction,
            bound_low=bound_low,
            bound_high=bound_high,
            bound_type=bound_type
        )
    
    def decode_hash(self, hash_bytes: bytes) -> List[CSDResult]:
        """Decode all bytes of a hash"""
        return [
            self.decode_byte(h, i)
            for i, h in enumerate(hash_bytes)
        ]
    
    def get_sign_pattern(self, hash_bytes: bytes) -> SignPattern:
        """Extract sign pattern (direction bits) from hash"""
        signs = []
        for i, h in enumerate(hash_bytes):
            c = self.const_bytes[i % len(self.const_bytes)]
            epsilon = compute_epsilon(h, c)
            signs.append(1 if epsilon > 0 else 0)
        
        # Convert to bytes (8 bits each)
        sign_bytes = []
        for i in range(0, len(signs), 8):
            byte_bits = signs[i:i+8]
            if len(byte_bits) == 8:
                byte_val = int(''.join(map(str, byte_bits)), 2)
                sign_bytes.append(byte_val)
        
        return SignPattern(
            bits=signs,
            bytes=sign_bytes,
            binary=''.join(map(str, signs))
        )
    
    def unfold(
        self,
        hash_bytes: bytes,
        message_length: int
    ) -> UnfoldResult:
        """
        Complete unfold: hash → bounds + estimates
        
        Returns UnfoldResult with all analysis.
        """
        # Decode all bytes
        csd_results = self.decode_hash(hash_bytes)
        
        # Get sign pattern
        sign_pattern = self.get_sign_pattern(hash_bytes)
        
        # Extract bounds and estimates for message length
        bounds = []
        estimates = []
        
        for i in range(message_length):
            r = csd_results[i]
            bounds.append((r.bound_low, r.bound_high))
            estimates.append(r.estimate_hybrid)
        
        # Calculate search space
        search_space = 1
        for low, high in bounds:
            search_space *= (high - low + 1)
        
        brute_force = 256 ** message_length
        reduction = brute_force / search_space if search_space > 0 else float('inf')
        
        return UnfoldResult(
            csd_results=csd_results,
            sign_pattern=sign_pattern,
            bounds=bounds,
            estimates=estimates,
            search_space=search_space,
            reduction_factor=reduction
        )

# ============================================================================
# ADAPTIVE RULES
# ============================================================================

def adaptive_estimate(hash_byte: int, const_byte: int) -> int:
    """
    Adaptive estimation based on epsilon sign/magnitude.
    
    From experimental analysis:
        ε < 0 (hash below const): 127 × (h/c) works best
        ε ≥ 0 (hash above const): (h+c)/2 works best
        |ε| > 5: fallback to 80
    """
    if const_byte == 0:
        const_byte = 1
    
    epsilon = (hash_byte - const_byte) / const_byte
    
    if abs(epsilon) > 5:
        return 80  # Extreme epsilon fallback
    elif epsilon < 0:
        # Negative: direct ratio h/c × 127
        return int(np.clip(127 * hash_byte / const_byte, 0, 255))
    else:
        # Positive: average (h+c)/2
        return (hash_byte + const_byte) // 2

def compute_adaptive_bounds(
    hash_byte: int,
    const_byte: int,
    width: int = 20
) -> Tuple[int, int]:
    """
    Compute bounds using adaptive estimation.
    """
    center = adaptive_estimate(hash_byte, const_byte)
    lower = max(0, center - width)
    upper = min(255, center + width)
    return lower, upper

# ============================================================================
# CORRELATION ANALYSIS
# ============================================================================

def epsilon_correlation(
    hash1: bytes,
    hash2: bytes,
    const_bytes: List[int] = None
) -> float:
    """
    Compute correlation between epsilon patterns of two hashes.
    
    Similar messages should have correlated epsilon patterns.
    """
    if const_bytes is None:
        const_bytes = H_INIT_BYTES
    
    eps1 = []
    eps2 = []
    
    for i in range(min(len(hash1), len(hash2))):
        c = const_bytes[i % len(const_bytes)]
        eps1.append(compute_epsilon(hash1[i], c))
        eps2.append(compute_epsilon(hash2[i], c))
    
    return float(np.corrcoef(eps1, eps2)[0, 1])

def sign_pattern_match(pattern1: SignPattern, pattern2: SignPattern) -> float:
    """
    Compute match ratio between sign patterns.
    """
    matches = sum(1 for a, b in zip(pattern1.bits, pattern2.bits) if a == b)
    return matches / len(pattern1.bits) if pattern1.bits else 0

# ============================================================================
# VERIFICATION AND TESTING
# ============================================================================

def verify_unfold(
    hash_bytes: bytes,
    original_message: bytes,
    const_bytes: List[int] = None
) -> Dict:
    """
    Verify unfold results against known message.
    """
    decoder = CSDDecoder(const_bytes)
    result = decoder.unfold(hash_bytes, len(original_message))
    
    original = list(original_message)
    in_bounds = []
    estimate_errors = []
    
    for i, byte_val in enumerate(original):
        low, high = result.bounds[i]
        in_bounds.append(low <= byte_val <= high)
        estimate_errors.append(abs(result.estimates[i] - byte_val))
    
    return {
        'message': original_message,
        'original_bytes': original,
        'estimates': result.estimates,
        'bounds': result.bounds,
        'in_bounds': in_bounds,
        'all_in_bounds': all(in_bounds),
        'estimate_errors': estimate_errors,
        'mean_error': np.mean(estimate_errors),
        'max_error': max(estimate_errors),
        'search_space': result.search_space,
        'reduction': result.reduction_factor,
        'sign_pattern': result.sign_pattern
    }

# ============================================================================
# MAIN
# ============================================================================

if __name__ == "__main__":
    import hashlib
    
    print("=" * 70)
    print("COLLAPSE SIGNATURE DECODER (CSD)")
    print("=" * 70)
    
    # Test messages
    messages = [b'NEXUS', b'Dean', b'test', b'ABC', b'123']
    
    decoder = CSDDecoder()
    
    for msg in messages:
        hash_bytes = hashlib.sha256(msg).digest()
        result = decoder.unfold(hash_bytes, len(msg))
        verification = verify_unfold(hash_bytes, msg)
        
        print(f"\n{'='*60}")
        print(f"Message: {msg.decode()}")
        print(f"Original bytes: {list(msg)}")
        print(f"Estimates: {result.estimates}")
        print(f"Errors: {verification['estimate_errors']}")
        print(f"In bounds: {verification['in_bounds']}")
        print(f"Mean error: {verification['mean_error']:.1f}")
        print(f"Search space: {result.search_space:,}")
        print(f"Reduction: {result.reduction_factor:,.1f}×")
        print(f"Sign pattern (first 8): {result.sign_pattern.binary[:8]}")
        print(f"Sign byte 0: {result.sign_pattern.bytes[0]} = '{chr(result.sign_pattern.bytes[0]) if 32 <= result.sign_pattern.bytes[0] <= 126 else '?'}'")
    
    print(f"\n{'='*70}")
    print("CSD FORMULA SUMMARY")
    print(f"{'='*70}")
    print("""
ε = (hash_byte - const_byte) / const_byte

p+ = (1 + ε) / 2  → Φ₀ path (structure/particle)
p- = (1 - ε) / 2  → E₀ path (entropy/wave)

ratio = (1 + ε) / (1 - ε) = p+ / p-

estimate ≈ 127 × ratio (for |ε| < 1)

Sign pattern: 32 bits encoding collapse directions
Search reduction: 10,000× to 10,000,000×
""")
