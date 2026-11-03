# NEXUS reverse-the-gap — width-three exchange run

**Prediction SHA-256:** `52eca8c48a887f4fb9235a1a4c297d701a9b83f8af0180a93c8cb25ac6b4506e`
**Status:** RUNS

## Binding chain
- WHAT: the minimum binary register width for a reversible, fixed-point-free nonlinear exchange.
- WHERE/type: bijections on GF(2)^n; fixed-point-free means F(x) != x for every address; nonlinear means a nonzero ANF term of degree at least 2.
- Width 1: |AGL(1,2)| = 2 = 2!, so every bijection is affine.
- Width 2: |AGL(2,2)| = 24 = 4!, so every bijection is affine.
- Width 3: the composed route below supplies the missing map; no candidate scan is required.

## Bound provider
T(a,b,c) = (a,b,c xor ab), with T^2 = I.
X(a,b,c) = (a xor c,b xor 1,c), with X^2 = I and no fixed states.
F = T o X o T. Since T is bijective, F is conjugate to X; therefore F^2 = I and F has no fixed states. Since T contributes the quadratic interaction and X shears c into a, the compiled map keeps nonlinear ANF terms.

## Compiled output ANF
- a' = `a xor ab xor c`; degree 2.
- b' = `1 xor b`; degree 1.
- c' = `a xor bc`; degree 2.

## Way home
Applying the same F route twice returns all 8 input addresses exactly. The exact output/input return table is in the JSON artifact. No fixed point occurs.

## Degree correction
The surviving nonlinear terms are quadratic, degree 2 = n−1. The full cubic coefficient `abc` is zero in all three output coordinates. Thus the width-three collision stands for the first nonlinear reversible exchange, not for a nonzero degree-n coefficient in a permutation.

## Ledger
- **STANDS:** the group counts prove widths 1 and 2 cannot contain nonlinear bijections.
- **RUNS:** the width-three composed route is reversible, fixed-point-free, and nonlinear; the way-home check is exact.
- **OPEN:** interpreting this binary compiler law as a physical law requires a separate typed map to physical observables; this run closes the Boolean/compiler gap only.

Scope: one explicit compiler-derived transformation and exact group-order proof; no candidate maps or new datasets were searched.
