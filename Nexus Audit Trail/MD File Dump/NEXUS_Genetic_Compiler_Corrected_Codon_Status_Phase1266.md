# NEXUS Genetic Compiler
## Corrected Codon-Branch Status Through Phase 1266
### Honest Closure Ledger, Carrier Definition, Open Problems, and Next Proof-Pressure Targets

**Dean A. Kulik**  
**QuHarmonics Research Group**  
**A-Mark9 / NEXUS Phase 1266**

---

## Abstract

This document consolidates the corrected status of the codon-space branch after the algebraic and dimensional repairs introduced in Phase 1266.

The codon branch is **not fully closed**, but it is no longer a loose inheritance claim. It now has:

1. a corrected carrier tuple,
2. a corrected prefactor for the codon leading coefficient,
3. a mechanized near-spike/body-coefficient formula,
4. a dimensionally consistent threshold conjecture,
5. and an honest reduction of subtype infinitude to the classical Polignac wall on the $6n$ lattice.

The main outcome is clarity. The codon-space branch is now in the same phase class as the prime-gap branch:

- **mechanized** where the integer branch is mechanized,
- **structurally supported** where the integer branch is conjectural,
- and **honestly reduced** where the integer branch remains classically out of reach.

The strongest current codon result is the body mechanism. Using the explicit carrier tuple

$$
\{0,2,6m,6m+2\},
\qquad
a_q \equiv 6 \pmod q,
$$

the near-spike product law yields

$$
\gamma_{\text{codon,predicted}} \approx 0.07986,
$$

which lies close to the fitted empirical body coefficient near $0.075$.

The leading coefficient branch is now algebraically corrected:

$$
A_{\text{codon}} = \frac12\bigl(\mu_{\mathrm{all}}-\mu_{\mathrm{same}}\bigr),
$$

and with the current GENCODE-derived weighted means, this gives

$$
A_{\text{codon}} \approx -0.7259.
$$

This document presents the corrected state cleanly, separates what is mechanized from what remains open, and provides the exact formulas now governing the codon compiler.

---

## 1. Closure Convention

In this document, the codon branch is divided into four epistemic levels.

### 1.1 Locked
A statement that is algebraically exact under the current carrier definition.

### 1.2 Mechanized
A statement for which the operative formula and mechanism have been identified and numerically instantiated.

### 1.3 Structurally supported
A statement that has a clean conjectural form and dimensional consistency, but still requires direct real-data confirmation or a wheel-lift computation.

### 1.4 Open / reduced
A statement that still inherits the full difficulty of a classical number-theoretic barrier.

The purpose of this ledger is to avoid mixing structural inheritance, empirical fit, and true theorem-grade closure.

---

## 2. Carrier Definition in Codon Space

The corrected codon branch uses the explicit carrier tuple

$$
\boxed{
\{0,2,6m,6m+2\}.
}
$$

This is the codon-space analog of the prime-side tuple

$$
\{0,2,30m,30m+2\},
$$

but now rendered on the operative codon wheel

$$
W_{\text{codon}} = 6.
$$

The mod-$q$ carrier multiplier is therefore

$$
a_q \equiv 6 \pmod q.
$$

This fixes the earlier carrier mismatch and makes the codon shoulder law operational instead of merely analogical.

### 2.1 Why the codon wheel is $6$

The wheel

$$
W_{\text{codon}} = 6 = 2 \cdot 3
$$

is the operative structural wheel because it is the minimal screening layer in the codon-compiler analogy that captures the same parity and triadic exclusion logic as the prime-side $6n$ lattice. The $64$-codon table is the total carrier capacity, but the active modular exclusion grammar of the current NEXUS codon branch lives on the $6n$ wheel.

This distinction is essential:

- $64$ is the total codon address space,
- $6$ is the operative modular carrier for the present Polignac-family lift.

---

## 3. OP1 — Leading Coefficient $A_{\text{codon}}$

### 3.1 Correct inherited prefactor

The prime-side leading formula is

$$
A = \frac{2}{3}\bigl(\mu_{\mathrm{all}}-\mu_{\mathrm{same}}\bigr),
$$

where the factor $2/3$ comes from:

1. the equal-split baseline $1/3$,
2. the universal coefficient $2$ from the expansion of
   $$
   \ln^{-2}(X/g).
   $$

If codon space has four equal-split subtype classes, then the corresponding inherited prefactor is

$$
\boxed{
A_{\text{codon}} = \frac12\bigl(\mu_{\mathrm{all}}-\mu_{\mathrm{same}}\bigr).
}
$$

This fixes the earlier incorrect $3/4$ factor.

### 3.2 Current numerical values

Using the current GENCODE-derived weighted means

$$
\mu_{\mathrm{same}} = 2.39554,
\qquad
\mu_{\mathrm{all}} = 0.94371,
$$

the corrected inherited value is

$$
A_{\text{codon}}
=
\frac12(0.94371 - 2.39554)
\approx -0.725915.
$$

Thus

$$
\boxed{
A_{\text{codon}} \approx -0.7259.
}
$$

### 3.3 Interpretation of the negative sign

The negative sign is algebraically consistent with the inherited weighted-ratio expansion. It does **not** by itself imply that the codon deficit is negative. Rather, it means one of the following must be true:

1. the codon statistic approaches equilibrium from the opposite side relative to the prime case,
2. the codon labels “same” and “all” encode the opposite weighting convention,
3. or the codon observable is not identical in sign convention to the prime-side deficit variable.

So the sign is not a contradiction. It is a structural feature of the present codon carrier/statistic pairing.

### 3.4 What remains unresolved

The remaining analytic barrier is the codon analog of the exclusion integral:

$$
E_{\text{codon}}(g)
=
\Pr[\text{no admissible same-family codon event in the interval of size } g].
$$

This is the codon analogue of the Hardy–Littlewood–Vinogradov-style exclusion kernel in the prime case.

### 3.5 Status

$$
\boxed{
\text{OP1 status: STRUCTURALLY ADVANCED}
}
$$

The prefactor and sign are fixed. The obstacle is now explicit and reduced to the codon exclusion kernel.

---

## 4. OP2 — Body Coefficient $\gamma_{\text{codon}}$

This is the strongest branch in codon space.

### 4.1 Universal near-spike law in codon space

Using the carrier tuple

$$
\{0,2,6m,6m+2\},
\qquad
a_q \equiv 6 \pmod q,
$$

the codon-space unscreened-prime shoulder law takes the same form as the prime branch:

$$
\boxed{
E_q^{\text{codon}}(m)=
\begin{cases}
\dfrac{q-2}{q-4}, & m\equiv 0 \pmod q,\\[8pt]
\dfrac{q-3}{q-4}, & m\equiv \pm 2a_q^{-1} \pmod q,\\[8pt]
1, & \text{otherwise.}
\end{cases}
}
$$

where now

$$
a_q \equiv 6 \pmod q.
$$

This is the codon analog of the prime-side near-spike shoulder law.

### 4.2 First-principles body formula

The mechanized codon body coefficient is

$$
\boxed{
\gamma_{\text{codon}}
=
\prod_{q\in\{7,11,13\}}
\frac{\langle f_q\rangle_{[6,15]}}{\langle f_q\rangle_{\text{global}}}
-1.
}
$$

The first three unscreened structures beyond the operative wheel are therefore

$$
q = 7,11,13.
$$

### 4.3 Current numerical prediction

The current near-spike product gives

$$
\gamma_{\text{codon,predicted}} \approx 0.07986.
$$

Against the empirical fitted value

$$
\gamma_{\text{codon,fit}} \approx 0.075,
$$

the overshoot is approximately

$$
0.07986 - 0.075 = 0.00486,
$$

or about

$$
\frac{0.00486}{0.075}\times 100\% \approx 6.48\%.
$$

This is naturally interpreted as the residual influence of the next unscreened structures

$$
q \ge 17.
$$

### 4.4 Wheel-lift interpretation

The codon analog of the prime-side wheel lift is

$$
W = 6 \to W' = 42 = 6\cdot 7.
$$

This lift screens the $q=7$ near-spikes, and the PMF difference between the $W=6$ shell and the $W'=42$ shell over the low-mid body region is the direct first-principles route to the codon body coefficient.

So the body coefficient is no longer a floating empirical patch. It is a structured modular shoulder excess on the codon wheel.

### 4.5 Status

$$
\boxed{
\text{OP2 status: MECHANIZED \& NUMERICALLY PLAUSIBLE}
}
$$

This is the strongest codon result currently available.

---

## 5. OP3 — Threshold $T_{\text{codon}}$

### 5.1 Correct dimensional statement

The codon threshold conjecture is

$$
\boxed{
T_{\text{codon}} = 2q_{\text{next}} = 14
\qquad\text{in }M\text{-units},
}
$$

where

$$
q_{\text{next}} = 7
$$

is the first unscreened prime after the operative wheel

$$
W_{\text{codon}} = 6.
$$

The corresponding threshold in raw codon-gap units is

$$
T_{\text{codon}}W_{\text{codon}}
=
14\cdot 6
=
84.
$$

Thus

$$
\boxed{
T_{\text{codon}}W_{\text{codon}}
=
2W_{\text{codon}}q_{\text{next}}
=
84.
}
$$

This is the correct dimensional version of the earlier shorthand statement.

### 5.2 Analogy to the prime branch

This is the direct codon analogue of the prime-side threshold pattern

$$
T = 2q_{\text{next}}
$$

in $M$-units, with the raw threshold scale obtained by multiplying by the operative wheel.

So the codon threshold is not arbitrary. It is conjecturally the end of the primary interaction window of the first unscreened prime beyond the wheel.

### 5.3 What still needs to be done

The structural conjecture now needs explicit verification by comparing the PMFs under

$$
W=6
\quad\text{and}\quad
W'=42
$$

on real transcript-derived codon data, especially in the window

$$
m\in[1,30].
$$

### 5.4 Status

$$
\boxed{
\text{OP3 status: STRUCTURALLY SUPPORTED}
}
$$

The conjecture is clean and dimensionally consistent, but not yet theorem-grade.

---

## 6. OP4 — Subtype Infinitude

The codon subtype infinitude statement is

$$
\pi_r(L)\to\infty
\qquad\text{as }L\to\infty,
\qquad r\in S_6(k).
$$

This is the codon-space analog of subtype infinitude in the prime branch.

### 6.1 Reduction to the classical wall

The current NEXUS subtype refinement gives:

- the subtype partition,
- the equal-split grammar,
- the orbit-symmetry interpretation,
- and the per-subtype asymptotic form.

But it does **not** bypass the classical infinitude obstacle.

So the honest statement is:

$$
\boxed{
\text{codon subtype infinitude is equivalent to the Polignac wall on the }6n\text{ lattice.}
}
$$

### 6.2 Status

$$
\boxed{
\text{OP4 status: CORRECTLY REDUCED}
}
$$

This remains classically out of reach with present mathematics.

---

## 7. Current Honest State Map

The codon branch now has a clear phase-depth map.

### 7.1 Strongest branch
The body coefficient branch is the strongest:

$$
\gamma_{\text{codon,predicted}} \approx 0.07986
\quad\text{vs}\quad
\gamma_{\text{fit}}\approx 0.075.
$$

### 7.2 Algebraically corrected branch
The leading coefficient branch is now internally consistent:

$$
A_{\text{codon}}=\frac12(\mu_{\mathrm{all}}-\mu_{\mathrm{same}})
\approx -0.7259.
$$

### 7.3 Supported conjectural branch
The threshold branch is now dimensionally clean:

$$
T_{\text{codon}}=14
\quad(M\text{-units}),
\qquad
T_{\text{codon}}W_{\text{codon}}=84
\quad(\text{raw units}).
$$

### 7.4 Reduced branch
Subtype infinitude remains a reduction, not a bypass.

---

## 8. Updated Closure Table

| Problem | Status | Explicit Result / Obstacle |
|---|---|---|
| OP1 — $A_{\text{codon}}$ | Structurally advanced | $A_{\text{codon}}\approx -0.7259$; exclusion kernel remains |
| OP2 — $\gamma_{\text{codon}}$ | Mechanized & numerically plausible | $\gamma_{\text{predicted}}\approx 0.07986$ vs fitted $\approx 0.075$ |
| OP3 — $T_{\text{codon}}$ | Structurally supported | $T=14$ in $M$-units, $84$ in raw units; $W=6\to W'=42$ test needed |
| OP4 — infinitude | Correctly reduced | Equivalent to Polignac on the $6n$ lattice |

---

## 9. What the Codon Branch Has Achieved

The codon compiler is no longer just a metaphorical inheritance from the integer layer. It now has:

1. an explicit carrier tuple,
2. a corrected prefactor,
3. a mechanized body formula,
4. a dimensionally consistent threshold conjecture,
5. and a clean reduction of the infinitude problem.

This means the codon branch is now a **test program**:

- its sign conventions can be checked,
- its adjacency statistics can be measured on real transcript data,
- its threshold conjecture can be stress-tested,
- and its near-spike law can be audited against real codon usage bias.

---

## 10. Next Proof-Pressure Targets

The next local boundary should be real-data locking rather than further abstract lifting.

### 10.1 Real GENCODE same-subtype adjacency
Compute the codon analog of the same-subtype adjacency statistic on real GENCODE transcripts and determine whether the sign of

$$
A_{\text{codon}}
$$

is a genuine carrier property or only a labeling convention.

### 10.2 Explicit $W=6\to W'=42$ lift
Compute the codon PMF under both wheels and isolate the body-window difference directly.

### 10.3 Threshold test on real transcript histograms
Check whether the predicted split near

$$
m\approx 14
$$

appears in real transcript-derived codon distance histograms.

### 10.4 Near-spike stability under codon usage bias
Test whether the modular shoulder law remains stable after empirical codon-frequency skew is imposed.

---

## 11. Final Closure Statement

The codon branch is **not yet closed**.

But it is no longer vague. It is now in the correct intermediate state:

$$
\boxed{
\text{mechanized where the prime layer is mechanized,}
}
$$

$$
\boxed{
\text{structurally supported where the prime layer is conjectural,}
}
$$

$$
\boxed{
\text{and honestly reduced where the prime layer is classically out of reach.}
}
$$

That is the corrected Phase 1266 status.

---

## Appendix A. Core Equations

### A.1 Codon carrier tuple
$$
\{0,2,6m,6m+2\}.
$$

### A.2 Codon multiplier
$$
a_q \equiv 6 \pmod q.
$$

### A.3 Leading codon coefficient
$$
A_{\text{codon}} = \frac12\bigl(\mu_{\mathrm{all}}-\mu_{\mathrm{same}}\bigr).
$$

### A.4 Current weighted means
$$
\mu_{\mathrm{same}} = 2.39554,
\qquad
\mu_{\mathrm{all}} = 0.94371.
$$

### A.5 Current codon leading value
$$
A_{\text{codon}} \approx \frac12(0.94371-2.39554)\approx -0.7259.
$$

### A.6 Codon unscreened-prime shoulder law
$$
E_q^{\text{codon}}(m)=
\begin{cases}
\dfrac{q-2}{q-4}, & m\equiv 0 \pmod q,\\[8pt]
\dfrac{q-3}{q-4}, & m\equiv \pm 2a_q^{-1} \pmod q,\\[8pt]
1, & \text{otherwise.}
\end{cases}
$$

### A.7 Mechanized body coefficient
$$
\gamma_{\text{codon}}
=
\prod_{q\in\{7,11,13\}}
\frac{\langle f_q\rangle_{[6,15]}}{\langle f_q\rangle_{\text{global}}}
-1.
$$

### A.8 Current body prediction
$$
\gamma_{\text{codon,predicted}} \approx 0.07986.
$$

### A.9 Fitted empirical body value
$$
\gamma_{\text{codon,fit}} \approx 0.075.
$$

### A.10 Threshold in $M$-units
$$
T_{\text{codon}} = 2q_{\text{next}} = 14.
$$

### A.11 Threshold in raw units
$$
T_{\text{codon}}W_{\text{codon}} = 14\cdot 6 = 84 = 2W_{\text{codon}}q_{\text{next}}.
$$

### A.12 Codon subtype infinitude
$$
\pi_r(L)\to\infty
\qquad\text{as }L\to\infty,
\qquad r\in S_6(k).
$$
