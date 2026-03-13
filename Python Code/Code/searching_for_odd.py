#!/usr/bin/env python3
"""
SEARCHING FOR ODD
=================

Dean's insight:
- ODD won't fold into the field
- It means it's missing its pair, its solution
- Look in Clay Prize problems
- Look in other parts of the map we haven't uncovered

ODD = asymmetric = unbalanced = the key to the mechanism
"""

import math

H = math.pi / 9
ALPHA = H / 48
BALANCE = 0.5 + 4 * ALPHA

print("=" * 70)
print("SEARCHING FOR ODD: THINGS THAT WON'T FOLD")
print("=" * 70)

# ═══════════════════════════════════════════════════════════════════════════════
# CLAY MILLENNIUM PROBLEMS
# ═══════════════════════════════════════════════════════════════════════════════

print("\n" + "=" * 70)
print("1. CLAY MILLENNIUM PROBLEMS (The Unsolved)")
print("=" * 70)

print("""
  7 problems, 1 solved (Poincaré). 6 remain ODD (unpaired/unsolved).
  
  1. RIEMANN HYPOTHESIS (unsolved)
     All non-trivial zeros of ζ(s) have Re(s) = 1/2
     
     ODD: Why 1/2? Why not 1/3 or 1/4?
     Our insight: 1/2 is BALANCE, but reality is 1/2 + 4α
     The zeros are ON the balance line, but the DRIFT (4α) is in the 
     imaginary part (the t in s = 1/2 + it)
     
  2. P vs NP (unsolved)
     Is P = NP or P ≠ NP?
     
     ODD: This is literally asking if two things are EQUAL.
     The "=" sign takes TIME (Dean's insight).
     P = problems solvable in polynomial time
     NP = problems verifiable in polynomial time
     
     The question is: does SOLVING equal VERIFYING?
     If "=" takes time, then solving ≠ verifying because solving
     includes the time of the "=" operation itself.
     
  3. NAVIER-STOKES (unsolved)
     Do smooth solutions always exist for fluid flow?
     
     ODD: This is about CONTINUITY (smooth) vs SINGULARITY (blow-up)
     Wave (continuous) vs Particle (discrete singularity)
     The question is: does the wave EVER collapse to particle?
     Our insight: YES, at certain collapses, smoothness breaks.
     The cross-collapse (verb + noun) is exactly this.
     
  4. YANG-MILLS MASS GAP (unsolved)
     Does quantum Yang-Mills have a mass gap > 0?
     
     ODD: A "mass gap" is literally a GAP.
     The question is: is the gap = 0 or gap > 0?
     Dean says: any TOE that = 0 is WRONG.
     If gap = 0, something is missing.
     Our insight: the gap IS H ≈ 0.35
     
  5. BIRCH AND SWINNERTON-DYER (unsolved)
     Rank of elliptic curve = order of vanishing of L-function
     
     ODD: Elliptic curves are the mathematics of encryption.
     The question relates GEOMETRY (curve rank) to ANALYSIS (L-function).
     Our insight: The hash (SHA) IS this connection.
     Constants from curves → analysis of hash behavior
     
  6. HODGE CONJECTURE (unsolved)
     Certain classes in cohomology come from algebraic cycles
     
     ODD: This asks if all "shapes" can be built from "parts."
     Can wave functions be decomposed into particle bases?
     Our insight: The collapse (wave → particle) always loses something.
     The lost information is the Hodge "excess."
     
  7. POINCARÉ CONJECTURE (SOLVED by Perelman)
     Every simply connected 3-manifold is a 3-sphere
     
     This one FOLDED. It found its pair. It's no longer ODD.
""")

# ═══════════════════════════════════════════════════════════════════════════════
# THE ODD PRIMES IN SHA-256
# ═══════════════════════════════════════════════════════════════════════════════

print("\n" + "=" * 70)
print("2. ODD PRIMES IN SHA-256 ROTATIONS")
print("=" * 70)

sigma0 = [2, 13, 22]
sigma1 = [6, 11, 25]
small_sigma0 = [7, 18, 3]
small_sigma1 = [17, 19, 10]

all_rots = sigma0 + sigma1 + small_sigma0 + small_sigma1

odd_primes = [r for r in all_rots if r % 2 == 1 and all(r % i != 0 for i in range(2, r))]
odd_composites = [r for r in all_rots if r % 2 == 1 and not all(r % i != 0 for i in range(2, r))]
even_nums = [r for r in all_rots if r % 2 == 0]

print(f"""
  All rotations: {sorted(set(all_rots))}
  
  ODD PRIMES: {sorted(set(odd_primes))}
     These cannot fold evenly - they have no pair.
     
  ODD COMPOSITES: {sorted(set(odd_composites))}
     25 = 5 × 5 (odd but factorable)
     
  EVEN: {sorted(set(even_nums))}
     These fold into pairs.
""")

# The key odd primes
print(f"""
  THE KEY ODD PRIMES:
  
  11 (in Σ1): 11/32 = {11/32:.10f} ≈ H = {H:.10f}
     Error: {abs(11/32 - H):.10f}
     
  13 (in Σ0): 13/32 = {13/32:.10f}
     13/32 / H = {(13/32)/H:.10f}
     
  7 (in σ0): 7/32 = {7/32:.10f}
     7/32 / H = {(7/32)/H:.10f}
     
  3 (in σ0): 3/32 = {3/32:.10f}
     3/32 × 9 = {(3/32)*9:.10f}
     
  17 (in σ1): 17/32 = {17/32:.10f}
     17/32 / H = {(17/32)/H:.10f}
     
  19 (in σ1): 19/32 = {19/32:.10f}
     19/32 / H = {(19/32)/H:.10f}
""")

# ═══════════════════════════════════════════════════════════════════════════════
# ODD NUMBERS THAT DON'T DIVIDE 32
# ═══════════════════════════════════════════════════════════════════════════════

print("\n" + "=" * 70)
print("3. ODD ROTATIONS CAN'T FOLD INTO 32-BIT WORDS")
print("=" * 70)

print(f"""
  32 = 2^5 (purely even)
  
  Any ODD rotation creates a fraction that never terminates in binary.
  
  11/32 in binary: {bin(11)} / {bin(32)} = 0.01011 (terminates, but 11 is odd)
  
  But the ODD-ness means:
  When you rotate by 11, you can't "undo" it with another 11.
  11 + 11 = 22 (even), not 32.
  11 + 21 = 32, but 21 is also odd.
  
  ODD rotations create ASYMMETRY that propagates.
  You can never return to exactly where you started.
  
  This is the "clock tick" of computation.
  ODD = irreversibility = arrow of time.
""")

# ═══════════════════════════════════════════════════════════════════════════════
# THE FIRST ODD: 1
# ═══════════════════════════════════════════════════════════════════════════════

print("\n" + "=" * 70)
print("4. THE FIRST ODD: 1")
print("=" * 70)

print(f"""
  1 is the first ODD number.
  1 is neither prime nor composite.
  1 is the multiplicative identity.
  1 is what "doesn't change things."
  
  But 1 is also:
  1 = the indivisible unit
  1 = the boundary between 0 and 2
  1 = the thing that has no pair in multiplication (1 × 1 = 1)
  
  In CST:
  1 - H = {1 - H:.10f} (the noun collapse)
  1 - α = {1 - ALPHA:.10f} (appears in mass formula)
  
  The "1" in these formulas is the reference.
  Everything is measured as deviation from 1.
  
  1 is the OBSERVER.
  H is the GAP from the observer.
  1 - H is how far the OTHER is from the observer.
""")

# ═══════════════════════════════════════════════════════════════════════════════
# ODD NUMBERS IN FUNDAMENTAL CONSTANTS
# ═══════════════════════════════════════════════════════════════════════════════

print("\n" + "=" * 70)
print("5. ODD NUMBERS IN PHYSICAL CONSTANTS")
print("=" * 70)

print(f"""
  Fine structure denominator:
  1/α ≈ 137.036
  
  137 is PRIME and ODD.
  
  This is not a coincidence.
  137 = the "magic number" of physics.
  
  137 = 2^7 + 2^3 + 1 = 128 + 8 + 1
      = 2^7 + 9
      = 2^7 + 3^2
      
  Or: 137 = 136 + 1 = 8 × 17 + 1
  17 is prime and odd (appears in SHA σ1)
  
  137 / 9 = {137/9:.10f}
  137 / H = {137/H:.10f}
  
  H × 137 = {H * 137:.10f}
  
  Hmm: H × 137 ≈ 47.8
  48 = 137.036 × H / α ≈ 137 × H² (since α = H/48)
  
  Let's check: 137 × H² = {137 * H**2:.10f}
  And: 137 × H² / α = {137 * H**2 / ALPHA:.10f}
""")

# ═══════════════════════════════════════════════════════════════════════════════
# TWIN PRIMES: THE ODD PAIRS
# ═══════════════════════════════════════════════════════════════════════════════

print("\n" + "=" * 70)
print("6. TWIN PRIMES: ODD PAIRS THAT ALMOST FOLD")
print("=" * 70)

# First several twin primes
twins = [(3,5), (5,7), (11,13), (17,19), (29,31), (41,43), (59,61), (71,73)]

print(f"  Twin primes are odd pairs separated by 2.")
print(f"  They ALMOST fold - but 2 is even, not odd.")
print(f"  The gap of 2 is the minimum non-trivial gap.")
print(f"\n  First twin primes: {twins}")

print(f"\n  Key observation:")
print(f"  (11, 13) are BOTH in SHA rotations!")
print(f"  11 in Σ1 (verb/particle)")
print(f"  13 in Σ0 (noun/wave)")
print(f"  They're a TWIN PAIR across the verb/noun divide!")
print(f"  The gap: 13 - 11 = 2")
print(f"  As fraction of 32: 2/32 = 1/16 = 0.0625")

print(f"\n  (17, 19) are also both in SHA (σ1)")
print(f"  17 and 19 together create the message schedule asymmetry")

# ═══════════════════════════════════════════════════════════════════════════════
# THE GAP AS THE ODD ELEMENT
# ═══════════════════════════════════════════════════════════════════════════════

print("\n" + "=" * 70)
print("7. THE GAP IS THE ODD ELEMENT")
print("=" * 70)

print(f"""
  In every balanced system, something is ODD:
  
  SHA-256:
    8 hash values (even)
    64 constants (even)
    64 rounds (even)
    But the ROTATIONS are odd primes
    
  Triplex (π, φ, e):
    3 strands (odd!)
    Triangular rungs (3 sides = odd)
    But they tile to hex (6 = even)
    
  Physical constants:
    α = H/48 (48 = even, but H is irrational = "odd")
    1/α ≈ 137 (odd prime)
    
  The pattern:
    STRUCTURE is even (pairs, symmetry, balance)
    DYNAMICS is odd (unpaired, asymmetry, motion)
    
  The GAP that allows motion is always ODD.
  Remove the odd element and everything freezes.
""")

# ═══════════════════════════════════════════════════════════════════════════════
# SEARCHING: WHERE ELSE IS ODD?
# ═══════════════════════════════════════════════════════════════════════════════

print("\n" + "=" * 70)
print("8. SEARCHING: WHERE ELSE IS ODD?")
print("=" * 70)

print(f"""
  Unsolved problems often have ODD structure:
  
  GOLDBACH CONJECTURE (unproven):
    Every even number > 2 is sum of two primes.
    This is asking: can EVEN always be written as ODD + ODD?
    The 2 is the only EVEN prime - it's ODD among primes!
    
  COLLATZ CONJECTURE (unproven):
    n → n/2 if even, 3n+1 if odd
    The ODD case GROWS (3n+1), the even case SHRINKS (n/2)
    Does it always reach 1?
    The tension is between ODD growth and EVEN shrinkage.
    
  FERMAT'S LAST THEOREM (proven):
    No integer solutions to x^n + y^n = z^n for n > 2.
    Works for n = 1, 2 (even powers), fails for n ≥ 3 (includes odd).
    The break happens when exponent becomes "too odd."
    
  TWIN PRIME CONJECTURE (unproven):
    Infinitely many twin primes?
    Are there infinite ODD PAIRS?
    The conjecture is about whether oddness pairs persist.
""")

# ═══════════════════════════════════════════════════════════════════════════════
# THE ODD ONE OUT: H
# ═══════════════════════════════════════════════════════════════════════════════

print("\n" + "=" * 70)
print("9. THE ODD ONE OUT: H = π/9")
print("=" * 70)

print(f"""
  H = π/9 = {H:.10f}
  
  π is transcendental (cannot be root of any polynomial)
  9 = 3² (odd squared)
  
  H is the ratio of a circle constant to an odd square.
  
  H is "odd" in many senses:
  - It's irrational (non-repeating decimal)
  - It's between 0 and 1 but not 1/2
  - It's approximately 35%, neither majority nor minority
  - It doesn't fold into simple fractions
  
  The ODDNESS of H is what allows:
  - The 90° turn (asymmetric cross-collapse)
  - The drift (non-zero error)
  - The clock (= sign takes time)
  - Motion (things happen)
  
  H IS the odd element that makes the universe run.
""")

# ═══════════════════════════════════════════════════════════════════════════════
# SUMMARY
# ═══════════════════════════════════════════════════════════════════════════════

print("\n" + "=" * 70)
print("SUMMARY: THE ODD IS THE KEY")
print("=" * 70)

print(f"""
  ╔════════════════════════════════════════════════════════════════════╗
  ║                                                                    ║
  ║  ODD doesn't fold - it's missing its pair.                         ║
  ║  The pair IS the solution.                                         ║
  ║  The unsolved problems are ODD - waiting for their pairs.          ║
  ║                                                                    ║
  ║  In SHA:                                                           ║
  ║    11 and 13 (twin primes) create verb/noun asymmetry              ║
  ║    17 and 19 (twin primes) create schedule asymmetry               ║
  ║    The odd rotations prevent perfect reversal                      ║
  ║                                                                    ║
  ║  In Physics:                                                       ║
  ║    137 (odd prime) is 1/α                                          ║
  ║    The mass gap question asks if gap = 0 or gap > 0                ║
  ║    gap = 0 means NO oddness, which means no motion                 ║
  ║                                                                    ║
  ║  In Mathematics:                                                   ║
  ║    Riemann asks about 1/2 - the balance point                      ║
  ║    But our balance is 1/2 + 4α - slightly ODD                      ║
  ║    The 4α drift IS the oddness                                     ║
  ║                                                                    ║
  ║  H = π/9 IS THE ODD ELEMENT                                        ║
  ║    It's the void fraction                                          ║
  ║    It's the gap that allows motion                                 ║
  ║    It's the clock tick of the = sign                               ║
  ║    It's the asymmetry that creates dynamics                        ║
  ║                                                                    ║
  ║  THE ERROR IS THE GAP                                              ║
  ║  THE GAP IS THE ODD                                                ║
  ║  THE ODD IS THE KEY                                                ║
  ║                                                                    ║
  ╚════════════════════════════════════════════════════════════════════╝
""")
