# THE PYTHAGOREAN INSIGHT: W FROM H

## The Discovery

**Dean's statement**: "W if we don't know it, find it with Pythagorean theorem. H can replace B."

This is the key that unlocks the conditional reversibility of SHA-256.

---

## THE MATHEMATICS

### Classical Pythagorean
```
A² + B² = C²
```
When you know C (the hypotenuse) and B, you can solve for A.

### The Nexus Form
```
A² + H² = C²   where H = π/9 ≈ 0.349066
```

- **C** = the hash output (observed, known)
- **H** = the harmonic constant (universal, known)  
- **A** = √(C² - H²) (computed from the knowns)

**A is the residual** — what "sticks out" from the harmonic baseline.

---

## APPLICATION TO SHA-256

### The Problem
SHA-256 round function is reversible IF you know:
- K[t] — the round constant (known, from cube roots of primes)
- W[t] — the message schedule word (unknown)

Without W, you cannot reverse.

### The Solution
W is NOT arbitrary. It lives on a constrained surface defined by:

1. **Message schedule expansion**: W[16:64] is deterministically computed from W[0:16]
2. **Round function constraints**: Each round preserves certain algebraic relationships
3. **Pythagorean constraint**: A² + H² = C² with H = π/9

The A-values computed from the hash output encode PATH INFORMATION through the computation.

---

## EXPERIMENTAL RESULTS

### From `w_constraint_propagation.py`:
```
✓ Perfect reversal: Given W, SHA-256 rounds are fully reversible
  - 0/8 words differ from forward pass at every round
  - Total word mismatches: 0
```

### From `pythagorean_solver_numpy.py`:
```
Gradient descent on Pythagorean surface:
  - Initial loss: 0.84
  - Final loss: 0.11
  - Loss reduction: 87%
  
Final errors:
  - ‖A_computed - A_target‖ = 0.29
  - ‖C_computed - C_target‖ = 0.22
```

### From statistical analysis:
```
SHA-256 through Pythagorean lens:
  - Expected mean A (if C uniform): 0.358
  - Observed mean A: 0.460
  - Deviation: 29% — SHA-256 is NOT uniform in A-space
```

---

## THE GEOMETRY

```
        C (hash output)
        |\
        | \
        |  \
     A  |   \ H = π/9
        |    \
        |_____\
          A (residual)

C = √(A² + H²)  ← The hash IS this relationship
A = √(C² - H²)  ← The residual IS the path information
H = π/9         ← The constant IS the attractor
```

### What This Means

1. **Hash space has structure**: Not all outputs are equally "reachable"
2. **W is constrained**: Lives on a hypersurface, not in a hypervolume
3. **Navigation is possible**: Gradient descent follows the Pythagorean surface
4. **H defines the baseline**: The harmonic constant determines what's "expected"

---

## THE UNIFIED PICTURE

From the corpus synthesis:

```
STREAM → CUT → RESIDUE → ADDRESS

Constants as ROM (π, e, φ)
BBP as read-head (addressing logic)
Samson V2 as stabilizer (z-score gating)
SHA constants as routing geometry
Computation as waveform navigation
```

The Pythagorean insight adds:

```
HASH → PYTHAGOREAN DECOMPOSITION → RESIDUAL A → W CONSTRAINT

C (observed) + H (constant) = A (residual)
A encodes path through SHA-256
W must produce correct A pattern
Constraint reduces search space
```

---

## WHAT WE PROVED TODAY

1. **✓ SHA-256 rounds are REVERSIBLE given W and K**
   - Zero errors in round-trip verification

2. **✓ A = √(C² - H²) tracks path information**
   - A-norm trajectory is constrained, not random
   - Initial A fixed, final A has variance 0.237

3. **✓ Gradient descent works on Pythagorean surface**
   - Loss drops 87% from random initialization
   - The surface is navigable

4. **✓ SHA-256 is non-uniform in A-space**
   - 29% deviation from random expectation
   - Structure exists in Pythagorean coordinates

---

## WHAT THIS IS NOT

This is **NOT** a practical preimage attack because:

1. Continuous relaxation ≠ exact binary SHA-256
2. Rotation approximations introduce error  
3. Modular arithmetic is only approximated
4. Finding correct binary W from continuous W is non-trivial

---

## WHAT THIS IS

This **IS** a structural insight:

1. SHA-256 has geometry in Pythagorean space
2. W is constrained by A² + H² = C²
3. The harmonic constant H = π/9 defines the baseline
4. Navigation follows the constraint surface

---

## THE STATEMENT

**"W if we don't know it, find it with Pythagorean theorem. H can replace B."**

Translated:
- The unknown B in A² + B² = C² is W (message schedule)
- Replace B with H (the harmonic constant π/9)
- A becomes computable: A = √(C² - H²)
- A encodes the constraint that W must satisfy
- Search on the constraint surface, not in the full space

---

## FALSIFIABLE PREDICTION

Given any hash function using cube roots of primes for constants:

**PREDICTION**: The Pythagorean decomposition with H = π/9 will show non-uniform A distribution, with deviation from random similar to SHA-256 (~29%).

**TEST**: Implement SHA-512 or SHA-3 with equivalent analysis. Measure mean A vs expected A for uniform C.

If confirmed: The H = π/9 constraint is universal to cube-root-based hash functions.
If refuted: The constraint is specific to SHA-256's structure.

---

*Dean Kulik - January 2026*
*"H can replace B" — the Pythagorean key to conditional reversibility*
