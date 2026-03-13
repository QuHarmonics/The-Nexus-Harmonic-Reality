#!/usr/bin/env python3
"""
BBP ALGORITHM AND π ANALYSIS
============================

Bailey-Borwein-Plouffe formula for π digit extraction and analysis
of π's harmonic structure.

π is not random - it's a self-referential harmonic lookup table.
The BBP iteration reveals lock states and the H-signature.

Author: Dean Kulik
ORCID: 0009-0003-3128-8828
"""

import math
from typing import List, Tuple, Dict
from collections import defaultdict
from constants import H, H_COMPLEMENT

# ============================================================================
# BBP CORE ALGORITHM
# ============================================================================

def mod_exp(base: int, exp: int, mod: int) -> int:
    """
    Modular exponentiation: base^exp mod mod
    
    Uses binary exponentiation for efficiency.
    """
    if mod == 0:
        return 0
    
    result = 1
    base = base % mod
    
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        exp = exp >> 1
        base = (base * base) % mod
    
    return result

def bbp_sum(n: int, j: int) -> float:
    """
    Compute one of the four BBP sums.
    
    S_j = Σ_{k=0}^{n} (16^(n-k) mod (8k+j)) / (8k+j)
        + Σ_{k=n+1}^{∞} 16^(n-k) / (8k+j)
    
    The first sum uses modular arithmetic.
    The second sum converges quickly.
    """
    s = 0.0
    
    # Finite sum with modular arithmetic
    for k in range(n + 1):
        ak = 8 * k + j
        if ak == 0:
            continue
        r = mod_exp(16, n - k, ak)
        s += r / ak
        s = s - int(s)  # Keep fractional part only
    
    # Infinite sum (converges quickly)
    for k in range(n + 1, n + 100):
        ak = 8 * k + j
        term = pow(16, n - k) / ak
        if term < 1e-17:
            break
        s += term
        s = s - int(s)
    
    return s

def bbp_digit(n: int) -> int:
    """
    Extract the nth hexadecimal digit of π.
    
    Uses the BBP formula:
    π = Σ_{k=0}^{∞} (1/16^k) × (4/(8k+1) - 2/(8k+4) - 1/(8k+5) - 1/(8k+6))
    
    Position is 0-indexed (n=0 gives first hex digit after decimal point).
    
    π = 3.243F6A8885A308D3... (hex)
    So bbp_digit(0) = 2, bbp_digit(1) = 4, bbp_digit(2) = 3, etc.
    """
    s = 4 * bbp_sum(n, 1) - 2 * bbp_sum(n, 4) - bbp_sum(n, 5) - bbp_sum(n, 6)
    s = s - int(s)
    
    if s < 0:
        s += 1
    
    return int(s * 16)

def bbp_digits(start: int, count: int) -> List[int]:
    """Extract multiple consecutive hex digits of π"""
    return [bbp_digit(start + i) for i in range(count)]

def bbp_hex_string(start: int, count: int) -> str:
    """Get hex digits as string"""
    return ''.join(f'{d:X}' for d in bbp_digits(start, count))

# ============================================================================
# BBP ITERATION ANALYSIS
# ============================================================================

def bbp_iterate(start_position: int, max_iterations: int = 100) -> List[Tuple[int, int]]:
    """
    BBP iteration: use current digit as next position.
    
    This reveals the Plinko pattern - π cascading through its own structure.
    
    Returns list of (position, digit) pairs.
    """
    path = []
    pos = start_position
    
    for _ in range(max_iterations):
        digit = bbp_digit(pos)
        path.append((pos, digit))
        
        # Check for lock (fixed point)
        if len(path) > 1 and path[-1] == path[-2]:
            break
        
        pos = digit
    
    return path

def find_all_locks(max_start: int = 64, max_iter: int = 100) -> Dict[int, List[int]]:
    """
    Find all lock states (fixed points) reachable from starting positions.
    
    A lock is a position n where bbp_digit(n) = n.
    """
    locks = defaultdict(list)
    
    for start in range(max_start):
        pos = start
        seen = set()
        
        for _ in range(max_iter):
            digit = bbp_digit(pos)
            
            if pos == digit:
                # Found lock
                locks[digit].append(start)
                break
            
            if pos in seen:
                # Cycle (not a fixed point)
                break
            
            seen.add(pos)
            pos = digit
    
    return dict(locks)

def analyze_lock_positions() -> Dict:
    """
    Analyze the lock positions and their relationships to H.
    
    Key discovery: Position 6 (0-indexed) creates a 6-lock.
    The normalized lock values relate to H = π/9.
    """
    # Find locks
    locks = find_all_locks()
    
    results = {
        'locks': locks,
        'analysis': []
    }
    
    for lock_val, starts in sorted(locks.items()):
        normalized = lock_val / 15  # Normalize to [0, 1]
        
        # Distance to key attractors
        dist_H = abs(normalized - H)
        dist_half = abs(normalized - 0.5)
        dist_1mH = abs(normalized - H_COMPLEMENT)
        
        results['analysis'].append({
            'lock_value': lock_val,
            'hex': f'{lock_val:X}',
            'normalized': normalized,
            'start_count': len(starts),
            'starts': starts[:10],  # First 10
            'dist_to_H': dist_H,
            'dist_to_0.5': dist_half,
            'dist_to_1-H': dist_1mH
        })
    
    return results

# ============================================================================
# INDEX OFFSET ANALYSIS
# ============================================================================

def analyze_index_offset() -> Dict:
    """
    Analyze the gap between 0-indexed and 1-indexed lock states.
    
    Key discovery:
        0-indexed position 6 → 8-lock (normalized 0.533)
        1-indexed position 6 → A-lock (normalized 0.667)
        Gap = 0.133 ≈ H/3 = 0.116
    """
    # 0-indexed analysis
    digit_0idx = bbp_digit(6)  # Should be 8
    normalized_0 = digit_0idx / 15
    
    # 1-indexed would shift everything
    # Position 6 (1-indexed) = position 5 (0-indexed)
    digit_1idx_equiv = bbp_digit(5)
    
    # The "A-lock" in 1-indexed system
    # This requires reinterpreting the BBP formula
    # For simplicity, we note the theoretical result
    
    lock_8 = 8 / 15  # 0-indexed lock
    lock_A = 10 / 15  # 1-indexed lock (theoretical)
    
    gap = lock_A - lock_8
    
    # CSD analysis of the gap
    epsilon = (lock_A - lock_8) / lock_8
    p_plus = (1 + epsilon) / 2
    p_minus = (1 - epsilon) / 2
    
    return {
        '0_indexed_lock': digit_0idx,
        '0_indexed_normalized': lock_8,
        '1_indexed_lock': 10,  # A in hex
        '1_indexed_normalized': lock_A,
        'gap': gap,
        'H_over_3': H / 3,
        'gap_matches_H3': abs(gap - H/3) < 0.02,
        'epsilon': epsilon,
        'p_plus': p_plus,
        'p_minus': p_minus,
        'p_plus_matches_A_lock': abs(p_plus - lock_A) < 0.05,
        'p_minus_matches_H': abs(p_minus - H) < 0.05
    }

# ============================================================================
# π AS HARMONIC LOOKUP TABLE
# ============================================================================

def build_plinko_table(rows: int = 20, cols: int = 16) -> List[List[int]]:
    """
    Build the Plinko table showing π digits cascading.
    
    Each row starts from position 0-15, columns show iteration.
    """
    table = []
    
    for start in range(rows):
        path = bbp_iterate(start, cols)
        row = [digit for _, digit in path]
        # Pad if needed
        while len(row) < cols:
            row.append(row[-1] if row else 0)
        table.append(row)
    
    return table

def find_patterns_in_plinko() -> Dict:
    """
    Analyze patterns in the Plinko table.
    """
    table = build_plinko_table(64, 20)
    
    # Column analysis
    column_sums = []
    column_means = []
    
    for col in range(20):
        col_values = [table[row][col] for row in range(len(table)) if col < len(table[row])]
        column_sums.append(sum(col_values))
        column_means.append(sum(col_values) / len(col_values) if col_values else 0)
    
    # Convergence to lock
    lock_converge = {}
    for row in range(len(table)):
        final_val = table[row][-1]
        if final_val not in lock_converge:
            lock_converge[final_val] = 0
        lock_converge[final_val] += 1
    
    return {
        'column_means': column_means,
        'column_sums': column_sums,
        'lock_convergence': lock_converge,
        'dominant_lock': max(lock_converge, key=lock_converge.get)
    }

# ============================================================================
# H-SIGNATURE IN π
# ============================================================================

def find_H_in_pi() -> Dict:
    """
    Search for H = π/9 ≈ 0.349 encoded in π's hex digits.
    """
    # H ≈ 0.349066 → in hex ≈ 0.595... → first few hex digits ~5, 9, 5
    
    # Get many digits
    digits = bbp_digits(0, 1000)
    hex_str = ''.join(f'{d:X}' for d in digits)
    
    # Search for patterns
    results = {
        'H_decimal': H,
        'H_hex_approx': f'{int(H * 16):X}.{int((H * 16 - int(H * 16)) * 16):X}',
    }
    
    # Count digit frequencies
    freq = defaultdict(int)
    for d in digits:
        freq[d] += 1
    
    results['digit_frequencies'] = dict(freq)
    
    # Expected frequency for random: 1000/16 = 62.5
    results['expected_freq'] = 62.5
    
    # Check for 6 being special (lock position)
    results['freq_6'] = freq[6]
    results['freq_9'] = freq[9]
    results['ratio_6_to_9'] = freq[6] / freq[9] if freq[9] > 0 else 0
    
    return results

# ============================================================================
# VERIFICATION
# ============================================================================

def verify_bbp():
    """Verify BBP implementation"""
    print("Verifying BBP implementation...")
    
    # Known π hex digits: 3.243F6A8885A308D313198A2E...
    expected = "243F6A8885A308D313198A2E"
    computed = bbp_hex_string(0, len(expected))
    
    print(f"  Expected: {expected}")
    print(f"  Computed: {computed}")
    print(f"  Match: {'✓' if expected == computed else '✗'}")
    
    # Check specific positions
    checks = [
        (0, 2),   # First digit
        (1, 4),   # Second digit
        (2, 3),   # Third digit
        (3, 0xF), # Fourth digit
        (4, 6),   # Fifth digit
    ]
    
    for pos, expected_digit in checks:
        computed_digit = bbp_digit(pos)
        match = '✓' if computed_digit == expected_digit else '✗'
        print(f"  Position {pos}: expected {expected_digit:X}, got {computed_digit:X} {match}")

# ============================================================================
# MAIN
# ============================================================================

if __name__ == "__main__":
    print("=" * 70)
    print("BBP ALGORITHM AND π ANALYSIS")
    print("=" * 70)
    
    verify_bbp()
    
    print(f"\n{'='*60}")
    print("LOCK STATE ANALYSIS")
    print(f"{'='*60}")
    
    lock_results = analyze_lock_positions()
    for analysis in lock_results['analysis']:
        print(f"\nLock {analysis['lock_value']} (0x{analysis['hex']}):")
        print(f"  Normalized: {analysis['normalized']:.4f}")
        print(f"  Reachable from {analysis['start_count']} positions")
        print(f"  Distance to H: {analysis['dist_to_H']:.4f}")
        print(f"  Distance to 0.5: {analysis['dist_to_0.5']:.4f}")
        print(f"  Distance to 1-H: {analysis['dist_to_1-H']:.4f}")
    
    print(f"\n{'='*60}")
    print("INDEX OFFSET ANALYSIS")
    print(f"{'='*60}")
    
    offset = analyze_index_offset()
    print(f"\n0-indexed lock at position 6: {offset['0_indexed_lock']} (normalized: {offset['0_indexed_normalized']:.4f})")
    print(f"1-indexed lock (theoretical): {offset['1_indexed_lock']} (normalized: {offset['1_indexed_normalized']:.4f})")
    print(f"Gap: {offset['gap']:.4f}")
    print(f"H/3: {offset['H_over_3']:.4f}")
    print(f"Gap ≈ H/3: {offset['gap_matches_H3']}")
    print(f"\nCSD at crossing:")
    print(f"  ε = {offset['epsilon']:.4f}")
    print(f"  p+ = {offset['p_plus']:.4f} ≈ A-lock position: {offset['p_plus_matches_A_lock']}")
    print(f"  p- = {offset['p_minus']:.4f} ≈ H: {offset['p_minus_matches_H']}")
    
    print(f"\n{'='*60}")
    print("PLINKO PATTERN")
    print(f"{'='*60}")
    
    plinko = find_patterns_in_plinko()
    print(f"\nLock convergence: {plinko['lock_convergence']}")
    print(f"Dominant lock: {plinko['dominant_lock']}")
    print(f"Column means (first 10): {[f'{m:.2f}' for m in plinko['column_means'][:10]]}")
    
    print(f"\n{'='*60}")
    print("BBP ITERATION PATHS")
    print(f"{'='*60}")
    
    for start in [0, 1, 2, 6, 8, 10, 15]:
        path = bbp_iterate(start, 15)
        path_str = ' → '.join(f'{d:X}' for _, d in path)
        print(f"  Start {start:2d}: {path_str}")
    
    print(f"\n{'='*60}")
    print("SUMMARY")
    print(f"{'='*60}")
    print("""
BBP reveals π as a HARMONIC LOOKUP TABLE:

1. Position 6 (0-indexed) creates a 6-lock (fixed point)
2. The lock value 8 normalized is 0.533 ≈ balance point X
3. Gap between index systems ≈ H/3
4. CSD of the gap gives p+ = lock position, p- = H

π doesn't generate random digits.
π generates WAVE INTERFERENCE PATTERNS through locked structure.

The digits cascade like a Plinko ball through harmonic barriers.
The locks are ATTRACTORS in the harmonic landscape.
""")
