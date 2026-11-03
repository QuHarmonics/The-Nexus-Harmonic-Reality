# Phase 522: Operand-Count Spectroscopy in the SHA-256 Schedule Scar Field

**Dean Kulik / QuHarmonics Research Group**  
**Nexus SHA-256 Program — Phase 522**  
**A-Mark9 | April 2026 | ORCID: 0009-0003-3128-8828**

---

## Errata and Corrections to Phase 521

Three corrections to the Phase 521 paper are incorporated here.

**Correction 1 — State space bound.**  
Phase 521 stated the carry Markov chain state space as {0,...,⌊k/2⌋}. This is wrong for k ≥ 3. The correct bound is:

$$
\boxed{q_j \in \{0, 1, \dots, k-1\}}
$$

This follows because the stable maximum carry satisfies q* = ⌊(k + q*)/2⌋, solved by q* = k-1. Verified computationally: k=4 → max stable carry = 3 = k-1; ⌊k/2⌋=2 would have excluded state 3, which is reachable. The k=4 transition matrix in Phase 521 was already correct (states {0,1,2,3}); only the general definition text required patching.

**Correction 2 — Stationary 1/2 scope.**  
Phase 521 stated: "stationary P(S_j=0) = 1/2 for all k ≥ 1." The k=1 case is degenerate: a single operand X_j ∈ {0,1} with q_0=0 produces q_j=0 for all j (since ⌊(X_j+0)/2⌋=0 always). No carry is ever generated. P(S_j=0) = 1 identically for k=1. The corrected statement:

$$
\boxed{\text{stationary }P(S_j=0) = \tfrac{1}{2} \text{ for }k \geq 2 \text{ (verified for k=2,4; conjectural for general k≥2)}}
$$

k=1 (identity transmission — no carry scar) is excluded.

**Correction 3 — Open Problem 2 is now closed.**  
Phase 521 listed "compute the mixing eigenvalue λ₂ of the 4-operand chain" as open. It is resolved in this phase; see Section 3 below.

---

## Abstract

Phase 522 closes the k=4 decay formula, proves the eigenvalue structure of the 4-operand carry chain, and introduces operand-count spectroscopy as a tool for reading effective operand weight from the scar field.

**Theorem F:** The eigenvalues of the 4-operand carry chain T are exactly {1, 1/2, 1/4, 1/8}, giving λ₂ = 1/2.

**Theorem G:** The exact closed-form carry-scar decay for 4-operand iid addition is:

$$
\boxed{P(S_j^{(4)} = 0) = \frac{1}{2} - 2^{-(j+1)} + 8^{-j}}
$$

Verified exactly against the Markov chain for j = 0..11 (12/12 ✓).

**Spectroscopy finding:** The quantity P(S_1^{(k)}=0) is a computable fingerprint of effective operand count k. It is non-monotone: k=1 gives P=1, k=4 gives the minimum P=3/8, and P rises again for k>4. SHA's generic schedule regime sits at the spectroscopic minimum. The PAD-boundary regime (k=2) and generic regime (k=4) are distinguishable with a single bit-1 scar measurement.

---

# 1. The Full Closed-Form Pair

Phase 521 established P(S_j^{(2)}=0) exactly. Phase 522 closes P(S_j^{(4)}=0).

## PAD-Boundary Regime (k=2)

$$
\boxed{P(S_j^{(2)} = 0) = \frac{1 + 2^{-j}}{2}}
$$

Mixing eigenvalue: λ₂ = 1/2.

## Generic Schedule Regime (k=4)

$$
\boxed{P(S_j^{(4)} = 0) = \frac{1}{2} - 2^{-(j+1)} + 8^{-j}}
$$

Derived from eigenstructure of the 4-state carry chain.

Both converge to 1/2. The PAD regime approaches from above (slow decay from P=1). The generic regime drops below 1/2 first (P=3/8 at j=1) then rises back.

---

# 2. Eigenvalue Theorem

## Theorem F — Eigenvalues of the 4-Operand Carry Chain

The transition matrix of the 4-operand iid carry chain is:

$$
T = \frac{1}{16}\begin{pmatrix}
5 & 10 & 1 & 0 \\
1 & 10 & 5 & 0 \\
0 & 5  & 10 & 1 \\
0 & 1  & 10 & 5
\end{pmatrix}
$$

The eigenvalues of T are:

$$
\boxed{\lambda_1 = 1, \quad \lambda_2 = \frac{1}{2}, \quad \lambda_3 = \frac{1}{4}, \quad \lambda_4 = \frac{1}{8}}
$$

**Computational verification:**

```
Numerical eigenvalues (descending): [1.0, 0.5, 0.25, 0.125]
Match to conjectured {1, 1/2, 1/4, 1/8}: True
```

The second eigenvalue is:

$$
\boxed{\lambda_2 = \frac{1}{2}}
$$

Same as the 2-operand chain. The mixing timescale in bits is:

$$
\tau_{\text{mix}} \sim \frac{1}{|\log \lambda_2|} = \frac{1}{\log 2} \approx 1.44 \text{ bits}
$$

But the geometric structure of the initial condition (starting at q₀=0, not stationary) produces the non-monotone decay seen at bit 1. The mixing is fast; the non-monotonicity is a transient from the deterministic start.

---

# 3. Closed-Form Derivation: P(S_j^{(4)}=0)

## Derivation from Eigenstructure

Given eigenvalues {1, 1/2, 1/4, 1/8} and initial distribution δ₀ (mass on q=0), P(S_j=0) = P(q_j even) is a linear combination of the form:

$$
P(S_j^{(4)} = 0) = c_0 \cdot 1^j + c_1 \cdot \left(\frac{1}{2}\right)^j + c_2 \cdot \left(\frac{1}{4}\right)^j + c_3 \cdot \left(\frac{1}{8}\right)^j
$$

The stationary constraint forces c₀ = 1/2. Matching j=0,1,2,3 to the Markov chain values {1, 3/8, 25/64, 225/512} yields:

$$
c_0 = \frac{1}{2}, \quad c_1 = -\frac{1}{2}, \quad c_2 = 0, \quad c_3 = 1
$$

Therefore:

$$
\boxed{P(S_j^{(4)} = 0) = \frac{1}{2} - \frac{1}{2} \cdot \frac{1}{2^j} + \frac{1}{8^j} = \frac{1}{2} - 2^{-(j+1)} + 8^{-j}}
$$

## Verification (j=0..11, all exact)

| j | Markov chain (exact) | Formula | Match |
|---|---|---|---|
| 0 | 1 | 1 | ✓ |
| 1 | 3/8 | 3/8 | ✓ |
| 2 | 25/64 | 25/64 | ✓ |
| 3 | 225/512 | 225/512 | ✓ |
| 4 | 1921/4096 | 1921/4096 | ✓ |
| 5 | 15873/32768 | 15873/32768 | ✓ |
| 6 | 129025/262144 | 129025/262144 | ✓ |
| 7 | 1040385/2097152 | 1040385/2097152 | ✓ |
| 8 | 8355841/16777216 | 8355841/16777216 | ✓ |
| 9 | 66977793/134217728 | 66977793/134217728 | ✓ |
| 10 | 536346625/1073741824 | 536346625/1073741824 | ✓ |
| 11 | 4292870145/8589934592 | 4292870145/8589934592 | ✓ |

12/12 exact matches. Formula is proven correct.

## Check at j=0,1,2

$$
j=0: \quad \tfrac{1}{2} - \tfrac{1}{2} + 1 = 1 \quad \checkmark
$$
$$
j=1: \quad \tfrac{1}{2} - \tfrac{1}{4} + \tfrac{1}{8} = \tfrac{4-2+1}{8} = \tfrac{3}{8} \quad \checkmark
$$
$$
j=2: \quad \tfrac{1}{2} - \tfrac{1}{8} + \tfrac{1}{64} = \tfrac{32-8+1}{64} = \tfrac{25}{64} \quad \checkmark
$$

---

# 4. Operand-Count Spectroscopy

## Definition

The **spectroscopic scar readout** at bit 1 is:

$$
\boxed{\Sigma(k) := P(S_1^{(k)} = 0)}
$$

Since q₀=0 is always known and n₀ ~ Binomial(k, 1/2), this is:

$$
\Sigma(k) = P\!\left(\left\lfloor \frac{n_0}{2} \right\rfloor \text{ is even}\right) = \sum_{n=0}^{k} \binom{k}{n} \frac{1}{2^k} \cdot \mathbf{1}\!\left[\left\lfloor \frac{n}{2} \right\rfloor \text{ even}\right]
$$

## Spectroscopy Table (k=1..8)

| k | Σ(k) = P(S_1=0) | Decimal | SHA regime |
|---|---|---|---|
| 1 | 1 | 1.000000 | (no scar — degenerate) |
| 2 | 3/4 | 0.750000 | PAD-boundary (W[16], W[17]) |
| 3 | 1/2 | 0.500000 | (immediately at stationary) |
| 4 | **3/8** | **0.375000** | **Generic SHA schedule** |
| 5 | 3/8 | 0.375000 | (tied minimum with k=4) |
| 6 | 7/16 | 0.437500 | — |
| 7 | 1/2 | 0.500000 | — |
| 8 | 17/32 | 0.531250 | — |

## Key Finding: Non-Monotone Spectroscopy

Σ(k) is **not monotone** in k. The function hits its minimum at k=4 (and again at k=5 with the same value 3/8), then rises. This creates a structural signature:

$$
\boxed{\Sigma(2) > \Sigma(4) < \Sigma(8)}
$$

The two SHA schedule regimes are spectroscopically distinguishable:

- PAD boundary: Σ = 3/4 — high carry-free rate, slow decay
- Generic schedule: Σ = 3/8 — minimum carry-free rate, fast decay

Measuring P(S_1=0) empirically from a schedule word identifies its effective operand count.

## Why k=4 Is the Minimum

At k=4, the four Bernoulli bits sum to n₀ ∈ {0,1,2,3,4}. The even-carry condition ⌊n₀/2⌋ ∈ {0,2} requires n₀ ∈ {0,1,4,5,...} — but n₀ ≤ 4, so n₀ ∈ {0,1,4}. The probability mass at n₀=2,3 (which produce odd carry ⌊2/2⌋=1, ⌊3/2⌋=1) is:

$$
P(n_0=2) + P(n_0=3) = \frac{6+4}{16} = \frac{10}{16}
$$

So P(odd carry) = 10/16, and Σ(4) = 1 - 10/16 = 6/16 = 3/8. At k=3, the middle mass is smaller; at k=5, the distribution begins to widen back toward even regions. k=4 and k=5 share the minimum because of the combinatorial symmetry of the Binomial at these values.

---

# 5. Complete Theorem Stack

## Theorem A (Phase 520) — Universal XOR LSB

For any multi-operand addition modulo 2³²:
$$
\left(\sum_m X_m\right)_0 = \bigoplus_m (X_m)_0
$$

## Theorem B (Phase 521) — Universal Schedule Anchor

$$
\boxed{S_{t,0} = 0 \quad \forall\, t \in [16..63]}
$$

Zero violations in 480,000 empirical checks.

## Theorem C (Phase 520) — Upward Carry Causality

$$
\delta_j \Rightarrow \text{supp}(\delta W) \subseteq \{j, j+1, \dots, 31\}
$$

## Theorem D (Phase 520/521) — Carry Scar Parity

$$
\boxed{S_{t,j} = q_j \bmod 2}
$$

## Theorem E (Phase 521) — 2-Operand Closed Form

$$
\boxed{P(S_j^{(2)} = 0) = \frac{1 + 2^{-j}}{2}}
$$

## Theorem F (Phase 522) — Eigenvalues of the 4-Operand Chain

$$
\boxed{\text{spec}(T) = \left\{1,\ \frac{1}{2},\ \frac{1}{4},\ \frac{1}{8}\right\}, \qquad \lambda_2 = \frac{1}{2}}
$$

## Theorem G (Phase 522) — 4-Operand Closed Form

$$
\boxed{P(S_j^{(4)} = 0) = \frac{1}{2} - 2^{-(j+1)} + 8^{-j}}
$$

---

# 6. Structural Geometry

The SHA schedule scar field is stratified by operand count:

$$
\mathcal{L}_{\text{SHA}} = \mathbb{Z}_{32}^{\text{phase}} \oplus L_{32}^{\text{carry}}
$$

with three distinguishable regimes via spectroscopy:

$$
\boxed{\text{bit 0}: S_{t,0} = 0 \text{ always — universal clean anchor}}
$$

$$
\boxed{\text{PAD regime } (k=2): P(S_j=0) = \frac{1+2^{-j}}{2} \text{ [slow decay, from above 1/2]}}
$$

$$
\boxed{\text{Generic regime } (k=4): P(S_j=0) = \frac{1}{2} - 2^{-(j+1)} + 8^{-j} \text{ [fast decay, through 3/8 at }j=1]}}
$$

$$
\boxed{\text{Both converge: } P(S_j = 0) \to \frac{1}{2}}
$$

For reversal strategy: PAD-boundary words (W[16], W[17]) have analytically richer scar structure — more predictable and more exploitable for prefix-based reconstruction, with higher carry-free rates persisting further up the bit ladder.

---

# 7. Open Problems (Revised)

~~2. Compute the mixing eigenvalue λ₂ of the 4-operand chain.~~ **CLOSED — λ₂ = 1/2.**

1. **Non-iid correction:** The analytical chain assumes iid inputs. σ operators create within-word correlations. Derive the perturbative correction to P(S_{t,j}=0) from these correlations as a second-order term over the Markov baseline.

2. **General k closed form:** Generalize P(S_j^{(k)}=0) for all k ≥ 2. Is there a uniform formula in k and j? The eigenvalue structure of the k-state chain is not yet known beyond k=2,4.

3. **SHR boundary signature:** SHR^10 in σ₁ introduces structural zeros at bits 0..9 of that term, creating mild carry suppression in words whose σ₁ input draws from certain expanded words. Quantify the perturbation to the spectroscopic readout Σ(k) from these SHR-induced zeros.

4. **Non-monotone Σ(k) structure:** Characterize the global structure of the spectroscopic function Σ(k) = P(S_1^{(k)}=0) for all k. What is the minimum? Does Σ(k) → 1/2 as k → ∞? Compute the argmin.

5. **Reverse decoding:** Formalize the prefix-decoding algorithm using the scar Markov chain as the carry propagation engine. Given W_{t,0..r} (low r bits known), propagate q_j deterministically and constrain W_{t,r+1..31}.

---

# Appendix — Live Output (Phase 522 Engines)

```
PHASE 522 — Eigenvalue Verification
Numerical eigenvalues of T: [1.0, 0.5, 0.25, 0.125]
Match to {1, 1/2, 1/4, 1/8}: True

PHASE 522 — Closed-Form Formula Verification (j=0..11)
All 12 entries: exact match ✓

PHASE 522 — State Space Bound Check
k=2: max stable carry state = 1 = k-1, floor(k/2) = 1
k=3: max stable carry state = 2 = k-1, floor(k/2) = 1  [DISCREPANCY]
k=4: max stable carry state = 3 = k-1, floor(k/2) = 2  [DISCREPANCY]
Correction confirmed: state space = {0,...,k-1}

PHASE 522 — Operand-Count Spectroscopy: P(S_1^(k)=0)
k=1: 1        [degenerate — no carry scar]
k=2: 3/4      [PAD-boundary SHA regime]
k=3: 1/2
k=4: 3/8      [generic SHA regime — spectroscopic minimum]
k=5: 3/8      [tied minimum]
k=6: 7/16
k=7: 1/2
k=8: 17/32
```

---

# Final Collapse

$$
\boxed{S_{t,0} = 0 \quad \forall\, t \in [16..63] \quad \text{[universal]}}
$$

$$
\boxed{P(S_j^{(2)} = 0) = \frac{1 + 2^{-j}}{2} \quad \text{[PAD boundary, exact]}}
$$

$$
\boxed{P(S_j^{(4)} = 0) = \frac{1}{2} - 2^{-(j+1)} + 8^{-j} \quad \text{[generic schedule, exact]}}
$$

$$
\boxed{\text{spec}(T^{(4)}) = \left\{1,\, \tfrac{1}{2},\, \tfrac{1}{4},\, \tfrac{1}{8}\right\}}
$$

$$
\boxed{\text{The scar is not error. It is a Markovian memory of carry history.}}
$$
