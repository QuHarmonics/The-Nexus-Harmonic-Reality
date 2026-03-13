Extensions of BBP Formulas to the Riemann Zeta Function

The Bailey-Borwein-Plouffe (BBP) formula, originally discovered in 1995 for computing
hexadecimal digits of it without prior digits, has inspired extensions to other mathematical
constants, including the Riemann zeta function Z(s) at positive integer points. These
extensions typically involve series representations that allow for digit—by—digit extraction or
fast convergence, particularly for even integers where closed forms exist in terms of
1t"{2n}. For odd integers, the extensions are more challenging due to the absence of simple
closed forms, but BBP-like series have been conjectured and derived using polylogarithms
and harmonic numbers. Below, I structure the exploration by distinguishing even and odd

cases, including key formulas, derivations, implications, and computational examples.

1. BBP Extensions for Even Zeta Values (Z(2n))

Even zeta values are rational multiples of Tt"{2n}, as established by Euler (e.g., Z(2) = 112/6,

Z(4) = n4/90). BBP-type formulas rovide series for these, enabling efficient computation
similar to ft's digit extraction. W)

- Key Formulas:

Extensions of BBP Formulas to the Riemann Zeta Function

The Bailey-Borwein-Plouffe (BBP) formula, originally discovered in 1995 for computing
hexadecimal digits of it without prior digits, has inspired extensions to other mathematical
constants, including the Riemann zeta function Z(s) at positive integer points. These
extensions typically involve series representations that allow for digit—by—digit extraction or
fast convergence, particularly for even integers where closed forms exist in terms of
1t"{2n}. For odd integers, the extensions are more challenging due to the absence of simple
closed forms, but BBP-like series have been conjectured and derived using polylogarithms
and harmonic numbers. Below, I structure the exploration by distinguishing even and odd

cases, including key formulas, derivations, implications, and computational examples.

1. BBP Extensions for Even Zeta Values (Z(2n))

Even zeta values are rational multiples of Tt"{2n}, as established by Euler (e.g., Z(2) = 112/6,

Z(4) = n4/90). BBP-type formulas rovide series for these, enabling efficient computation
similar to ft's digit extraction. W)

- Key Formulas:

- For Z(2): Two notable BBP-type series from Bailey (2000) and Borwein & Bailey
(2003) are:

. Generalization for Z(2n): Recent works extend this to higher even n via integral

representations, such as:

((27%)

This form connects to polylogarithms through substitutions like t = -ln u.

@

- Derivations:

- These series arise from polylogarithm ladders or generating functions, often using
the inverse sine integral or Bernoulli polynomials. For Z(2), the derivations involve
summing rational fractions over powers of bases like 64 or 729, ensuring
convergence rates suitable for digit extraction (e.g., hexadecimal). The integral

forms derive from Fourier transforms or substitutions in Dirichlet eta functions

n(s) = (1 - 2"{1-s}) Z(s). W

- Implications:

- Digit Extraction: Like the original BBP for T[, these allow computation of isolated
digits of Z(2n) without full series summation, useful for high-precision

verifications in number theory.

- Computational Efficiency: Bases like 64 ensure rapid convergence (e.g., each

term reduces by ~6 digits), outperforming traditional Euler sums.

~ Links to Polylogarithms: The formulas often express Z(2n) in terms of Polylog(n,

2) at rational z, bridging to multiple zeta values and potential RH insights via

analytic continuation.

- Computational Example: Using the first formula for 2(2) with high precision (50 digits),

the computed value matches the known n2/6 z
1.6449340668482264364724151666460251892189499012068 exactly within

precision, with difference 0.0.

2. BBP Extensions for Odd Zeta Values (Z(2n+1))

Odd zeta values, like Apéry's constant Z(3) 2 1.2020569, lack simple closed forms in TI and
are conjectured irrational. BBP-like series exist but are more complex, often involving

exponential denominators and harmonic numbers, without straightforward digit extraction

like for It or even zeta. @-

- Key Formulas:

- Plouffe's Conjectures (2011): For Z(3), Z(5), etc., using Sn(r) = Z{k=1}"°°1/k"n/
(e"{tt r k} -1):

((3) = 2883(1) — 3733(2) + 753(4)

((5) = 2435(1) — 2f§S5(2) -l— 11655(4)

- From Bernoulli Polynomial Representations (2023): For Z(3):

if ﬂew) f;ﬁ%(:)

3 = —
C() 12 2n2n+1)(2n+2)

Similar for Z(5) and Z(7), incorporating P—polynomials for faster Bernoulli

computation.
- Trigonometric Families (e.g., Cot x): For Z(2n+1) at x=Tt:

TL

00
a23—2B23H2n+1—2s —l—
0(2n-l—1—23)! ;s=20(n

These use Bernoulli (B{23}) and Euler (E{2s}) numbers, with variants for tan, csc,

sec. m

- Derivations:

- Plouffe's series use generating functions and integer relations (e.g., PSLQ

algorithm) to find rational coefficients fitting numerical data.

- Trigonometric series derive from recursive substitutions into zeta expressions,

using Taylor coefficients of functions like cot x or sec x, simEIified via lemmas on
vanishing sums and generating functions.

- Polynomial approaches reduce Bernoulli computations to P-polynomials,

accelerating series via decoupled recurrences.

- Implications:

