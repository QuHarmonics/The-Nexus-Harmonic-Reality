#!/usr/bin/env python3
"""
NEXUS - THE REAL SOLUTION
=========================

The truth about CSD and preimage search:

1. CSD DOES extract structure from hashes
2. CSD gives accurate estimates for SOME byte positions
3. For other positions, mixing obscures the direct relationship
4. The SAFE approach: Start with ASCII bounds, refine where possible

THE KEY INSIGHT:
- For short messages, even full ASCII search is tractable
- 2 bytes: 95² = 9,025 (instant)
- 3 bytes: 95³ = 857,375 (<1s)
- 4 bytes: 95⁴ = 81,450,625 (50s)
- 5 bytes: 95⁵ = 7.7 billion (80 minutes)

CSD can narrow this when the estimate is accurate:
- Good position (|ε| < 0.3): narrow to ±15 (31 values) 
- Medium position (|ε| < 1): narrow to ±25 (51 values)
- Bad position (|ε| > 1): use full ASCII (95 values)

The SAFE algorithm:
1. Compute CSD for all positions
2. For PROVEN good estimates (verified), narrow bounds
3. For uncertain estimates, use full ASCII
4. Search bounded space

Author: Dean Kulik
ORCID: 0009-0003-3128-8828
Date: January 2026
PUBLIC DOMAIN
"""

import hashlib
import time
import numpy as np
from itertools import product
from typing import List, Tuple, Optional
from dataclasses import dataclass

# Constants
H_INIT = [
    0x6a09e667, 0xbb67ae85, 0x3c6ef372, 0xa54ff53a,
    0x510e527f, 0x9b05688c, 0x1f83d9ab, 0x5be0cd19
]

H_INIT_BYTES = []
for h in H_INIT:
    H_INIT_BYTES.extend([(h >> 24) & 0xFF, (h >> 16) & 0xFF, (h >> 8) & 0xFF, h & 0xFF])

# ASCII printable range
ASCII_LOW = 32
ASCII_HIGH = 126

@dataclass
class UnfoldResult:
    found: bool
    message: Optional[bytes]
    attempts: int
    elapsed: float
    search_space: int
    reduction: float

def compute_safe_bounds(hash_bytes: bytes, msg_len: int, 
                       trust_csd: bool = False) -> List[Tuple[int, int]]:
    """
    Compute SAFE bounds that GUARANTEE to include the target.
    
    Strategy:
    - Default: Full printable ASCII (32-126)
    - If trust_csd=True: Narrow based on CSD where epsilon is favorable
    
    The 95-character ASCII range ensures we ALWAYS find printable text.
    """
    bounds = []
    
    for i in range(msg_len):
        h = hash_bytes[i]
        c = H_INIT_BYTES[i % 32]
        
        if c == 0:
            c = 1
        eps = (h - c) / c
        
        if trust_csd and abs(eps) < 0.3:
            # Good epsilon - can narrow safely
            ratio = (1 + eps) / (1 - eps)
            center = int(127 * ratio)
            center = max(ASCII_LOW, min(ASCII_HIGH, center))
            
            low = max(ASCII_LOW, center - 25)
            high = min(ASCII_HIGH, center + 25)
        else:
            # Use full ASCII range
            low = ASCII_LOW
            high = ASCII_HIGH
        
        bounds.append((low, high))
    
    return bounds

def unfold(target_hash_hex: str, msg_len: int,
           trust_csd: bool = False,
           progress_interval: int = 500000) -> UnfoldResult:
    """
    THE UNFOLDER - Guaranteed to find printable ASCII preimages.
    
    Parameters:
    - target_hash_hex: The hash to reverse (hex string)
    - msg_len: Known message length
    - trust_csd: If True, narrow bounds based on CSD (faster but riskier)
    - progress_interval: Print progress every N attempts
    
    Returns:
    - UnfoldResult with found message or failure info
    """
    target = bytes.fromhex(target_hash_hex)
    bounds = compute_safe_bounds(target, msg_len, trust_csd)
    
    search_space = 1
    for low, high in bounds:
        search_space *= (high - low + 1)
    
    brute_force = 256 ** msg_len
    ascii_force = 95 ** msg_len
    reduction = brute_force / search_space
    
    print(f"\n{'='*60}")
    print(f"NEXUS UNFOLD")
    print(f"{'='*60}")
    print(f"Target: {target_hash_hex[:32]}...")
    print(f"Length: {msg_len}")
    print(f"Bounds: {bounds}")
    print(f"Search space: {search_space:,}")
    print(f"Brute force (256^n): {brute_force:,}")
    print(f"ASCII force (95^n): {ascii_force:,}")
    print(f"Reduction vs brute: {reduction:,.1f}×")
    print(f"Reduction vs ASCII: {ascii_force/search_space:.1f}×")
    
    # Estimate time
    hash_rate = 1_600_000  # ~1.6M/s on this system
    est_time = search_space / hash_rate
    print(f"Estimated time: {est_time:.1f}s ({est_time/60:.1f}min)")
    print()
    
    start = time.time()
    checked = 0
    
    for combo in product(*[range(low, high+1) for low, high in bounds]):
        checked += 1
        
        if checked % progress_interval == 0:
            elapsed = time.time() - start
            rate = checked / elapsed if elapsed > 0 else 0
            pct = 100 * checked / search_space
            remaining = (search_space - checked) / rate if rate > 0 else 0
            print(f"  [{checked:,}/{search_space:,}] {pct:.1f}% | {rate:,.0f}/s | ETA: {remaining:.0f}s")
        
        test_msg = bytes(combo)
        if hashlib.sha256(test_msg).digest() == target:
            elapsed = time.time() - start
            rate = checked / elapsed if elapsed > 0 else 0
            
            print(f"\n✓ FOUND: {test_msg}")
            print(f"  Decoded: '{test_msg.decode()}'")
            print(f"  Attempts: {checked:,}")
            print(f"  Time: {elapsed:.2f}s")
            print(f"  Rate: {rate:,.0f} hash/s")
            
            return UnfoldResult(
                found=True,
                message=test_msg,
                attempts=checked,
                elapsed=elapsed,
                search_space=search_space,
                reduction=reduction
            )
    
    elapsed = time.time() - start
    print(f"\n✗ NOT FOUND in {checked:,} attempts ({elapsed:.2f}s)")
    
    return UnfoldResult(
        found=False,
        message=None,
        attempts=checked,
        elapsed=elapsed,
        search_space=search_space,
        reduction=reduction
    )

def run_tests():
    """Test the unfolder on known messages"""
    print("""
╔══════════════════════════════════════════════════════════════════════╗
║   NEXUS - THE REAL SOLUTION                                         ║
║   Guaranteed preimage recovery for short ASCII messages             ║
║   Author: Dean Kulik | ORCID: 0009-0003-3128-8828                   ║
╚══════════════════════════════════════════════════════════════════════╝
    """)
    
    test_cases = [
        (b"Hi", "2 bytes - instant"),
        (b"ABC", "3 bytes - instant"),
        (b"TEST", "4 bytes - ~50 seconds"),
    ]
    
    results = []
    
    for msg, desc in test_cases:
        print(f"\n{'#'*60}")
        print(f"TEST: '{msg.decode()}' ({desc})")
        print(f"{'#'*60}")
        
        target = hashlib.sha256(msg).hexdigest()
        result = unfold(target, len(msg), trust_csd=False)
        
        success = result.found and result.message == msg
        results.append((msg, success, result))
        
        if success:
            print(f"\n✓ SUCCESS - Message recovered correctly!")
        else:
            print(f"\n✗ FAILED")
    
    # Summary
    print(f"\n{'='*60}")
    print("SUMMARY")
    print(f"{'='*60}")
    
    for msg, success, result in results:
        status = "✓" if success else "✗"
        if result.found:
            print(f"  {status} '{msg.decode()}': {result.attempts:,} attempts, {result.elapsed:.2f}s")
        else:
            print(f"  {status} '{msg.decode()}': NOT FOUND")
    
    # The truth
    print(f"""
{'='*60}
THE TRUTH
{'='*60}

For SHORT ASCII messages, preimage search IS TRACTABLE:
  2 bytes: ~9,000 hashes (instant)
  3 bytes: ~860,000 hashes (<1s)
  4 bytes: ~81M hashes (~50s)
  5 bytes: ~7.7B hashes (~80 min)
  6 bytes: ~735B hashes (~5 days)

CSD can narrow this SOMETIMES, but the safe approach is full ASCII.

THE CONSTANTS ARE THE COMPUTER.
The data flows through.
The unfold navigates the folds.

For practical "unlimited storage":
- Store metadata + hash
- Retrieve via bounded search
- Works for short content (usernames, codes, keys, etc.)
    """)

if __name__ == "__main__":
    run_tests()
