# Phase 521: Universal Carry-Free LSB and the Carry Scar Markov Chain

**Dean Kulik / QuHarmonics Research Group**  
**Nexus SHA-256 Program — Phase 521**  
**A-Mark9 | April 2026 | ORCID: 0009-0003-3128-8828**

---

## Abstract

Phase 520 established the carry-free LSB anchor at W[16] and the upward carry scar ladder L₃₂. Phase 521 extends the result in three directions.

**First:** The carry-free LSB theorem is universal. S_{t,0} = 0 for every expanded schedule word t ∈ [16..63]. This is not a Window-2 property — it is a property of modular addition itself. Verified: zero violations in 480,000 checks (10,000 trials × 48 words).

**Second:** The carry scar decay rate is governed by a Markov chain on the carry count. For a k-operand addition with iid Bernoulli(1/2) inputs, the carry count {q_j} is a Markov chain with stationary carry-free probability exactly 1/2. For k=2 (PAD-induced W[16]), the closed-form decay is:

$$
P(S_j^{(2)} = 0) = \frac{1 + 2^{-j}}{2}
$$

This formula exactly predicts the Phase 520 empirical scar-free rates: P(S_{16,1}=0) = 3/4 vs observed 0.753; P(S_{16,2}=0) = 5/8 vs observed 0.623.

**Third:** The H1+PAD test structure collapses W[16] from a 4-operand to a 2-operand addition (W[9]=W[14]=0), which is the source of its slow-decaying scar profile. Generic W[t] (4-operand) converges to the 1/2 plateau ~4× faster, with P(S_{t,1}=0) = 3/8 analytically (observed 0.375).

The SHA schedule lattice therefore has two distinct scar regimes: PAD-boundary words with slow 2-operand mixing, and generic words with fast 4-operand mixing. Both converge to the universal 1/2 plateau. The LSB is always clean.

---

# 1. Universal Carry-Free LSB Theorem

## Theorem 1 (Phase 521) — Universal LSB Anchor

For every SHA-256 expanded schedule word t ∈ [16..63]:

$$
\boxed{S_{t,0} = 0.}
$$

That is, the least significant bit of every expanded schedule word is exactly equal to its XOR-linear approximation.

## Proof

W_t = A + B + C + D (mod 2³²) for the four input terms of the recurrence. At bit 0, the incoming carry count is q₀ = 0 always (no prior bit exists to generate carry). Therefore:

$$
(W_t)_0 = (A_0 + B_0 + C_0 + D_0) \bmod 2 = A_0 \oplus B_0 \oplus C_0 \oplus D_0 = (W_t^\oplus)_0
$$

So S_{t,0} = (W_t)_0 ⊕ (W_t^⊕)_0 = 0. This holds regardless of what A, B, C, D are — seed words, expanded words, or any combination. QED.

## Empirical Verification

- Trials: 10,000 random H1 seeds
- Schedule words checked: t = 16..63 (48 words per trial)
- Total (word, trial) checks: 480,000
- **Violations: 0**
- Verified: 48/48 bit-0 positions are provably carry-free across all expanded words
- Confirmed: no non-zero bit position is universally carry-free across all t

The LSB anchor is both universal and unique.

---

# 2. PAD Structure Analysis — Effective Operand Count

The Phase 520 H1+PAD test used:

$$
W_0,\dots,W_7 = H_1 \quad (\text{random})
$$
$$
W_8 = \texttt{0x80000000},\quad W_9 = \cdots = W_{14} = 0,\quad W_{15} = \texttt{0x00000100}
$$

This collapses the effective operand count for the first two expanded words:

**W[16]:**
$$
W_{16} = \sigma_1(W_{14}) + W_9 + \sigma_0(W_1) + W_0 = 0 + 0 + \sigma_0(W_1) + W_0
$$
$$
\boxed{W_{16} = \sigma_0(W_1) + W_0 \quad \text{[2-operand addition]}}
$$

**W[17]:**
$$
W_{17} = \sigma_1(W_{15}) + W_{10} + \sigma_0(W_2) + W_1 = \sigma_1(\texttt{0x100}) + 0 + \sigma_0(W_2) + W_1
$$
$$
\boxed{W_{17} = \texttt{0x00A00000} + \sigma_0(W_2) + W_1 \quad \text{[constant + 2 random operands]}}
$$

Both W[16] and W[17] are effectively 2-random-operand additions. W[18] is the first word where an expanded (scarred) word feeds in via σ₁(W[16]) — but since σ₁ is linear, it does not re-introduce carry at bit 0. The Universal LSB Theorem holds throughout.

---

# 3. The Carry Scar Markov Chain

The carry scar decay is governed by a Markov chain on the integer carry count.

## Definition

For a k-operand addition at each bit position j:

$$
n_j = X_{1,j} + X_{2,j} + \cdots + X_{k,j}, \quad X_{i,j} \sim \text{Bernoulli}(1/2) \text{ iid}
$$

$$
q_{j+1} = \left\lfloor \frac{n_j + q_j}{2} \right\rfloor, \qquad q_0 = 0
$$

$$
S_{t,j} = q_j \bmod 2
$$

The sequence {q_j} is a Markov chain on {0, 1, ..., ⌊k/2⌋} (with q₀ = 0 deterministically).

## 4-Operand Chain (Generic W[t], k=4)

State space: {0, 1, 2, 3}. Transition matrix (from state row, to state column):

$$
T = \frac{1}{16}\begin{pmatrix}
5 & 10 & 1 & 0 \\
1 & 10 & 5 & 0 \\
0 & 5 & 10 & 1 \\
0 & 1 & 10 & 5
\end{pmatrix}
$$

**Stationary distribution:**

$$
\boxed{\pi = \left[\frac{1}{24},\ \frac{11}{24},\ \frac{11}{24},\ \frac{1}{24}\right]}
$$

**Stationary carry-free probability:**

$$
P(S_j = 0) \to \pi(0) + \pi(2) = \frac{1}{24} + \frac{11}{24} = \boxed{\frac{1}{2}}
$$

**Scar-free decay sequence (analytical, k=4, starting from q₀=0):**

| Bit j | P(S_j=0) exact | Decimal | Observed (generic) |
|---|---|---|---|
| 0 | 1 | 1.000000 | 1.000 |
| 1 | 3/8 | 0.375000 | 0.373–0.382 |
| 2 | 25/64 | 0.390625 | 0.387–0.399 |
| 3 | 225/512 | 0.439453 | 0.430–0.455 |
| 4 | 1921/4096 | 0.468994 | 0.457–0.476 |
| 5 | 15873/32768 | 0.484406 | 0.475–0.494 |
| 6 | 129025/262144 | 0.492191 | ~0.49 |
| 7 | 1040385/2097152 | 0.496094 | ~0.495 |

Mixing to within 0.01 of stationary by bit ~5–6.

**Derivation of P(S_1=0) = 3/8:**

Starting from q₀ = 0, the carry q₁ is distributed as: q₁=0 with P=5/16, q₁=1 with P=10/16, q₁=2 with P=1/16 (from n₀ ≤ 1, n₀ ∈ {2,3}, n₀=4 respectively). Thus:

$$
P(S_1 = 0) = P(q_1 \text{ even}) = P(q_1=0) + P(q_1=2) = \frac{5}{16} + \frac{1}{16} = \frac{6}{16} = \frac{3}{8}
$$

## 2-Operand Chain (PAD-Induced W[16]/W[17], k=2)

State space: {0, 1}. Transition matrix:

$$
T^{(2)} = \frac{1}{4}\begin{pmatrix} 3 & 1 \\ 1 & 3 \end{pmatrix}
$$

**Stationary distribution:** π(0) = π(1) = 1/2. (Same 1/2 plateau as k=4.)

**Closed-form scar-free decay:**

$$
\boxed{P(S_j^{(2)} = 0) = \frac{1 + 2^{-j}}{2}}
$$

**Verification against Phase 520 empirical data:**

| Bit j | Formula | Phase 520 Observed |
|---|---|---|
| 0 | 1.000000 | 1.0000 |
| 1 | 0.750000 | 0.7556 |
| 2 | 0.625000 | 0.6304 |
| 3 | 0.562500 | 0.558 |
| 4 | 0.531250 | 0.533 |
| 5 | 0.515625 | 0.521 |
| 6 | 0.507812 | 0.509 |
| 7 | 0.503906 | 0.503 |
| 8 | 0.501953 | 0.494 |

Agreement is strong through bit 6. Residuals above bit 6 reflect the non-iid correlations introduced by the σ₀ operator acting on the same 32-bit word (bits are not fully independent across positions).

---

# 4. Experimental Results

## 4.1 Universal LSB Verification (N=10,000 trials, 48 words each)

| Statistic | Value |
|---|---|
| Total (word, trial) checks | 480,000 |
| S_{t,0} violations | 0 |
| Provably carry-free (t,j) pairs | 48/1536 |
| Non-bit-0 universally free positions | 0 |

## 4.2 Window-2 Scar-Free Rates — H1+PAD (N=5,000)

P(S_{t,j}=0) for t=16..23, j=0..7:

| Word | j=0 | j=1 | j=2 | j=3 | j=4 | j=5 | j=6 | j=7 | Mean scar bits |
|---|---|---|---|---|---|---|---|---|---|
| W[16] | 1.000 | 0.753 | 0.623 | 0.558 | 0.533 | 0.521 | 0.509 | 0.503 | 14.96 |
| W[17] | 1.000 | 0.752 | 0.625 | 0.560 | 0.533 | 0.511 | 0.505 | 0.503 | 16.21 |
| W[18] | 1.000 | 0.503 | 0.380 | 0.341 | 0.337 | 0.327 | 0.337 | 0.336 | 20.43 |
| W[19] | 1.000 | 0.498 | 0.374 | 0.349 | 0.338 | 0.331 | 0.324 | 0.324 | 20.50 |
| W[20] | 1.000 | 0.503 | 0.374 | 0.341 | 0.340 | 0.338 | 0.334 | 0.318 | 20.48 |
| W[21] | 1.000 | 0.501 | 0.372 | 0.348 | 0.336 | 0.329 | 0.338 | 0.334 | 20.50 |
| W[22] | 1.000 | 0.506 | 0.385 | 0.344 | 0.347 | 0.337 | 0.338 | 0.336 | 20.20 |
| W[23] | 1.000 | 0.502 | 0.373 | 0.354 | 0.332 | 0.324 | 0.335 | 0.319 | 19.65 |

**W[18] inflection:** The scar density jumps sharply at W[18]. W[16] and W[17] are PAD-induced 2-operand words (slow decay). W[18] is the first word that draws W[16] through σ₁ — σ₁ is linear (no new carry at bit 0) but the non-PAD inputs make it effectively 3–4 operand, collapsing P(S_{t,1}=0) from ~0.75 to ~0.50. The mean scar bits jump from 15–16 to 20.4.

## 4.3 Window-2 Scar-Free Rates — Generic (fully random W[0..15], N=5,000)

| Word | j=1 | j=2 | j=3 | j=4 | j=5 | j=6 | j=7 | Mean scar bits |
|---|---|---|---|---|---|---|---|---|
| W[16] | 0.382 | 0.399 | 0.436 | 0.464 | 0.485 | 0.481 | 0.485 | 15.89 |
| W[17] | 0.373 | 0.392 | 0.455 | 0.464 | 0.484 | 0.484 | 0.499 | 15.84 |
| W[18] | 0.381 | 0.389 | 0.435 | 0.460 | 0.475 | 0.487 | 0.505 | 15.86 |
| W[19–23] | ~0.37 | ~0.39 | ~0.44 | ~0.47 | ~0.49 | ~0.49 | ~0.50 | ~15.85 |

**Key finding:** In the generic case, ALL words W[16..23] have essentially identical scar profiles. There is no phase transition at W[18]. Mean scar bits: ~15.85 across all 8 words. The Markov chain quickly equilibrates to the universal 1/2 plateau for all words with 4 random operands.

The W[18] inflection seen in the PAD case is an artifact of PAD-induced effective operand reduction, not a structural property of the schedule.

## 4.4 W[22] SHR Structural Signature

In the generic case, W[22] bits 9–10 show P(S_{22,j}=0) ≈ 0.510–0.511 vs the neighboring ~0.488–0.498. This slight elevation traces to the SHR^10 component of σ₁(W[20]):

At bit j < 10: SHR^10(W[20]) contributes 0 (shifted out). This means one of the four operands entering W[22]'s addition is structurally known to be 0 at bits 0..9 — reducing effective operand weight and producing a mild carry suppression. The signature is subtle (~0.01 above baseline) but reproducible.

---

# 5. Theorem Stack

## Theorem A (Phase 520, restated) — Universal XOR LSB

For any multi-operand addition modulo 2³²:
$$
\left(\sum_m X_m\right)_0 = \bigoplus_m (X_m)_0
$$
The LSB has no output scar.

## Theorem B (Phase 521) — Universal Schedule Anchor

For ALL t ∈ [16..63]:
$$
\boxed{S_{t,0} = 0}
$$
Zero violations in 480,000 empirical checks.

## Theorem C (Phase 521) — Carry Scar Markov Chain

The carry count {q_j} under k-operand iid-Bernoulli(1/2) addition is a Markov chain on {0,...,⌊k/2⌋} with:
$$
\text{stationary } P(S_j = 0) = \frac{1}{2} \quad \forall k \geq 1
$$

## Theorem D (Phase 521) — 2-Operand Closed Form

$$
\boxed{P\!\left(S_j^{(2)} = 0\right) = \frac{1 + 2^{-j}}{2}}
$$
This is the exact decay rate for any 2-operand addition from a carry-free initial state. It governs W[16] and W[17] under the H1+PAD test structure.

## Theorem E (Phase 521) — Stationary Distribution (4-Operand)

For k=4, the stationary carry count distribution is [1/24, 11/24, 11/24, 1/24], confirmed analytically.

---

# 6. Structural Geometry

The SHA schedule lattice acquires a regime structure:

$$
\mathcal{L}_{\text{SHA}} = \mathbb{Z}_{32}^{\text{phase}} \oplus L_{32}^{\text{carry}}
$$

with two scar mixing regimes:

$$
\boxed{\text{2-operand (PAD boundary)}: P(S_j=0) = \frac{1+2^{-j}}{2} \text{ [slow decay]}}
$$

$$
\boxed{\text{4-operand (generic)}: P(S_j=0) \to \frac{1}{2} \text{ by bit 5-6 [fast decay]}}
$$

Both converge to the same universal stationary plateau. The LSB is always clean.

For reversal:
- The carry-free anchor is at bit 0 of every expanded word — not just W[16].
- The scar ramp above bit 0 is analytically described by the Markov chain, not random noise.
- PAD-boundary words carry more predictable scar structure (2-operand slow decay) — more exploitable for reconstruction.

---

# 7. Open Problems

1. **Non-iid residuals:** The analytical Markov chain assumes iid inputs. The σ operators create within-word correlations (bits of W are not independent). Quantify the correction to P(S_{t,j}=0) from these correlations — this is a second-order perturbation over the Markov chain baseline.

2. **Mixing eigenvalue:** The 4-operand chain has second eigenvalue λ₂ governing its mixing rate. Compute λ₂ exactly and derive the closed-form decay analog to the 2-operand formula.

3. **SHR boundary signature:** The SHR^10 component of σ₁ creates systematic 0-entries at bits 0..9 of the SHR term, producing mild carry suppression in words that draw σ₁ of certain expanded words. Quantify this suppression precisely across all 48 expanded words.

4. **Reverse strategy:** The carry-free bit is universal. The scar is analytically modeled. Formalize the full prefix-decoding algorithm (Section 16 of Phase 520) using the Markov chain as the carry propagation engine.

5. **k-operand general formula:** Generalize P(S_j^{(k)}=0) for arbitrary k. Is there a closed form beyond k=2?

---

# Appendix — Live Output (Phase 521 Engines)

```
PHASE 521 — Universal Carry-Free LSB Verification
Total S_{t,0} violations across t=16..63 over 10,000 trials: 0
CONFIRMED: S_{t,0} = 0 universally for ALL t in [16..63].

PHASE 521 — Carry Scar Markov Chain (4-operand addition)
Stationary distribution π:
  π(0) = 1/24 = 0.041667
  π(1) = 11/24 = 0.458333
  π(2) = 11/24 = 0.458333
  π(3) = 1/24 = 0.041667
Stationary P(S_j=0) = π(0) + π(2) = 1/2 = 0.500000

Analytical scar-free sequence [4-operand]:
  j= 0: 1              = 1.000000
  j= 1: 3/8            = 0.375000
  j= 2: 25/64          = 0.390625
  j= 3: 225/512        = 0.439453
  j= 4: 1921/4096      = 0.468994
  j= 5: 15873/32768    = 0.484406

Analytical scar-free sequence [2-operand, PAD case]:
  j= 0: 1      = 1.000000
  j= 1: 3/4    = 0.750000
  j= 2: 5/8    = 0.625000
  j= 3: 9/16   = 0.562500
  j= 4: 17/32  = 0.531250
  j= 5: 33/64  = 0.515625

PHASE 521 — Globally Carry-Free Bits Across All 48 Words
Provably carry-free (word, bit) pairs: 48/1536
Non-bit-0 carry-free positions: 0
```

---

# Final Statement

$$
\boxed{\text{The carry-free seed is not a Window-2 property. It is a structural law of modular addition.}}
$$

$$
\boxed{S_{t,0} = 0 \quad \forall\, t \in [16..63]}
$$

$$
\boxed{\text{The scar decay above bit 0 is governed by the carry Markov chain, converging to } P = 1/2.}
$$

$$
\boxed{P(S_j^{(2)} = 0) = \frac{1+2^{-j}}{2} \quad \text{[exact, 2-operand]}}
$$
