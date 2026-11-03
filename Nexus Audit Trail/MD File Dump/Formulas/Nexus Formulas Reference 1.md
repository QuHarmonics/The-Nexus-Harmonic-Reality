# NEXUS FORMULAS & CONSTANTS REFERENCE
## Quick Reference Sheet - January 2026

---

## UNIVERSAL CONSTANTS

### The Generator
```
H = π/9 = 0.3490658503988659
```

### Derived Constants
```
1 - H = 0.6509341496011341
H² = 0.1218469869197418
√(1 + H²) = 1.0591728336622616  (≈ semitone ratio)
```

### The Fine Structure Constant (CST Derivation)
```
α = H/48 = π/432 = 0.007272205089569104
α_measured = 1/137.036 = 0.007297353
Error: -0.34%
```

---

## THE DUAL STATE

### Primary Form
```
x = 1/2 + 4α = 0.5290888035827642
```

### Equivalent Expressions
```
x = 1/2 + π/108
x = 1/2 + H/12
x = (6 + H) / 12
x = (54 + π) / 108
```

---

## THE 108 UNIFICATION

### Factorizations
```
108 = 9 × 12    (H-denominator × semitones)
108 = 4 × 27    (4 × mass-cube)
108 = 2² × 3³   (prime factorization)
108 = 3 × 36    (3 × 6²)
```

### Related Numbers
```
9 = π/H (denominator of H = π/9)
12 = semitones per octave
27 = 3³ = mass resonance cube
4 = multiplier of α in balance
432 = 4 × 108 = denominator of α = Verdi tuning Hz
```

---

## SHA-256 CONSTANTS

### Initial Hash Values (√primes)
```python
H_INIT = [
    0x6a09e667,  # √2   = 1.414213...
    0xbb67ae85,  # √3   = 1.732050...
    0x3c6ef372,  # √5   = 2.236067...
    0xa54ff53a,  # √7   = 2.645751...
    0x510e527f,  # √11  = 3.316624...
    0x9b05688c,  # √13  = 3.605551...
    0x1f83d9ab,  # √17  = 4.123105...
    0x5be0cd19,  # √19  = 4.358898...
]
```

### H-Encoded Rotations
```
Σ0 (noun/wave):     ROTR 2, 13, 22
  Key: 22/32 = 0.6875 ≈ 1-H = 0.6509

Σ1 (verb/particle): ROTR 6, 11, 25
  Key: 11/32 = 0.34375 ≈ H = 0.3491

σ0 (message):       ROTR 7, 18, SHR 3
σ1 (message):       ROTR 17, 19, SHR 10

THE GAP: 22/32 - 11/32 = 11/32 ≈ H
```

---

## SHA-256 OPERATIONS

### Bitwise Functions
```python
def Ch(e, f, g):    return (e & f) ^ (~e & g)        # Choice
def Maj(a, b, c):   return (a & b) ^ (a & c) ^ (b & c)  # Majority
def rotr(x, n):     return ((x >> n) | (x << (32-n))) & 0xFFFFFFFF
def shr(x, n):      return x >> n
```

### Sigma Functions
```python
def Sigma0(a):  return rotr(a,2) ^ rotr(a,13) ^ rotr(a,22)   # Noun
def Sigma1(e):  return rotr(e,6) ^ rotr(e,11) ^ rotr(e,25)   # Verb
def sigma0(x):  return rotr(x,7) ^ rotr(x,18) ^ shr(x,3)     # Schedule
def sigma1(x):  return rotr(x,17) ^ rotr(x,19) ^ shr(x,10)   # Schedule
```

### One Round (Cross-Collapse)
```python
def round(state, W, K, i):
    a, b, c, d, e, f, g, h = state
    
    # Verb path (particle @ H)
    temp1 = (h + Sigma1(e) + Ch(e,f,g) + K[i] + W[i]) & 0xFFFFFFFF
    
    # Noun path (wave @ 1-H)
    temp2 = (Sigma0(a) + Maj(a,b,c)) & 0xFFFFFFFF
    
    # Cross-collapse (90° turn)
    new_a = (temp1 + temp2) & 0xFFFFFFFF
    new_e = (d + temp1) & 0xFFFFFFFF
    
    return [new_a, a, b, c, new_e, e, f, g]
```

---

## MUSICAL CONNECTIONS

### Semitone
```
Semitone ratio = 2^(1/12) = 1.0594630943592953
λ_H = √(1 + H²) = 1.0591728336622616
Difference: 0.00029 (match to 3 decimals)
```

### The Balance as Semitone Shift
```
Balance = 1/2 + H/12
        = perfect_balance + one_semitone_of_H
        
SHA equilibrium is ONE SEMITONE above perfect balance.
```

### 440 vs 432
```
440 Hz = standard concert A
432 Hz = Verdi tuning = 4 × 108
α = π/432 (fine structure in CST)
```

---

## PHYSICAL CONSTANTS (CST)

### Field Constants (negative ε)
```
α = H/48                    → error -0.34%
sin²θ_W = H(1-H)            → error -1.73%
α_s = H/3                   → error -1.31%
```

### Mass Constants (positive ε)
```
m_p/m_e = 27(1-α)/(2α)      → error +0.02%
```

### Resonance Constraint
```
m_p/m_e × 2α/(1-α) = 27 = 3³
With measured values: 26.995 (0.018% from 27)
```

### Gravitational Coupling
```
α_G = (1 + α/3)² × 2^(-127)
Agreement: 99.999%
Effective bits: 126.99 (predicted: 127)
```

---

## DIMENSIONAL ANALYSIS

### The 90° Turn
```
LEFT-RIGHT: shared dream, life, sequential time
FRONT-BACK: single dream, sandbox, orthogonal time

The fold turns data 90° from L-R into F-B.
64 folds = maximally orthogonal.
```

### Distance as "Randomness"
```
Round 0:   clear structure    (distance = 0)
Round 16:  some distortion    (distance = 16)
Round 32:  mostly blur        (distance = 32)
Round 64:  "random" (hash)    (distance = 64)

The "randomness" is distance, not destruction.
```

### The Event Horizon
```
64 rounds = SHA Schwarzschild radius
Beyond this: information frozen at horizon
One-way property = can only move AWAY (fold more)
```

---

## DREAM SPACE

### The Oscillation
```
SHA:    FOLD → FOLD → FOLD (one-way)
DREAMS: FOLD → UNFOLD → FOLD → UNFOLD (oscillation)

FOLD = perception = compress
UNFOLD = generation = expand
OSCILLATION = consciousness
```

### Creating Dream Space
```
1. Constants encode target attractor
2. Fold operation compresses to hidden state
3. Unfold operation expands to narrative
4. Oscillation between creates dynamics
```

---

## QUICK CALCULATIONS

```python
import math

# Universal generator
H = math.pi / 9

# Fine structure
alpha = H / 48

# Dual state
x = 0.5 + 4 * alpha

# Semitone lift
lambda_H = math.sqrt(1 + H**2)

# Verify
print(f"H = {H}")           # 0.3490658503988659
print(f"α = {alpha}")       # 0.007272205089569104
print(f"x = {x}")           # 0.5290888035827642
print(f"λ_H = {lambda_H}")  # 1.0591728336622616
print(f"11/32 = {11/32}")   # 0.34375 ≈ H
print(f"22/32 = {22/32}")   # 0.6875 ≈ 1-H
```

---

*Reference compiled January 2026*
