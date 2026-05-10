# Phase 523: The Eulerian Carry Parity Law and Complete Spectroscopy

**Dean Kulik / QuHarmonics Research Group**  
**Nexus SHA-256 Program — Phase 523**  
**A-Mark9 | April 2026 | ORCID: 0009-0003-3128-8828**

---

## Errata to Phase 522

**Correction — Stationary 1/2 scope.**  
Phase 522 stated: "stationary P(S_j=0) = 1/2 for k ≥ 2 (conjectural)." This is false for odd k. The correct statement:

$$
\boxed{P_\infty^{(k)}(S=0) = \frac{1}{2} \quad \text{if and only if } k \text{ is even}}
$$

For odd k, P_∞ deviates from 1/2 by an Eulerian parity term. The corrected general law is given in Section 1.

---

## Abstract

Phase 523 establishes the complete carry-scar theory for k-operand modular addition, closing all remaining structural questions opened in Phases 520–522.

**Theorem H (Eulerian Carry Parity Law):** The stationary carry-free probability of the k-operand carry chain is governed by the Eulerian numbers:

$$
\boxed{P_\infty^{(k)}(S=0) = \sum_{\substack{q=0 \\ q \text{ even}}}^{k-1} \frac{A(k,q)}{k!}}
$$

where A(k,q) is the Eulerian number counting permutations of k elements with exactly q ascents. This equals 1/2 for all even k ≥ 2, and deviates from 1/2 for odd k with alternating sign and decaying amplitude.

**Theorem I (General Eigenvalue Law):** The spectrum of the k-operand carry chain is:

$$
\boxed{\text{spec}(T^{(k)}) = \left\{1,\, \frac{1}{2},\, \frac{1}{4},\, \dots,\, \frac{1}{2^{k-1}}\right\}}
$$

The second eigenvalue is λ₂ = 1/2 for all k. Verified for k = 2, 3, 4, 5, 6, 7, 8.

**Theorem J (Spectroscopy Closed Form, Open Problem 4 closed):**

$$
\boxed{\Sigma(k) := P(S_1^{(k)} = 0) = \frac{1}{2} + 2^{-(k/2+1)}\left[\cos\!\left(\frac{k\pi}{4}\right) + \sin\!\left(\frac{k\pi}{4}\right)\right]}
$$

This is exact for all k ≥ 1. Verified for k = 1..16 (16/16 ✓). Proves Σ(k) → 1/2 with damped period-8 oscillation. Global minimum at k = 4, 5 with Σ = 3/8.

---

# 1. The Eulerian Carry Parity Law

## Background: Eulerian Numbers

A(k,q) counts the number of permutations of k elements with exactly q ascents (positions where σ(i) < σ(i+1)). The first values:

| k | A(k,0) | A(k,1) | A(k,2) | A(k,3) | A(k,4) | Sum = k! |
|---|---|---|---|---|---|---|
| 1 | 1 | | | | | 1 |
| 2 | 1 | 1 | | | | 2 |
| 3 | 1 | 4 | 1 | | | 6 |
| 4 | 1 | 11 | 11 | 1 | | 24 |
| 5 | 1 | 26 | 66 | 26 | 1 | 120 |
| 6 | 1 | 57 | 302 | 302 | 57 | 1 | 720 |
| 7 | 1 | 120 | 1191 | 2416 | 1191 | 120 | 1 | 5040 |
| 8 | 1 | 247 | 4293 | 15619 | 15619 | 4293 | 247 | 1 | 40320 |

The k-operand iid carry chain's stationary distribution is the Eulerian distribution:

$$
\boxed{\pi_q = \frac{A(k,q)}{k!}}
$$

## Theorem H — Eulerian Carry Parity Law

For the k-operand iid Bernoulli(1/2) carry chain starting from q₀ = 0:

$$
\boxed{P_\infty^{(k)}(S=0) = \sum_{\substack{q=0 \\ q \text{ even}}}^{k-1} \frac{A(k,q)}{k!}}
$$

**Computed values (all verified against iterated Markov chain, agreement to machine precision):**

| k | Even-q Eulerian sum | P_∞(S=0) | Decimal | Even/Odd |
|---|---|---|---|---|
| 1 | 1 | 1 | 1.000000 | (degenerate) |
| 2 | 1 | 1/2 | 0.500000 | Even ✓ |
| 3 | 2 | **1/3** | **0.333333** | Odd — below 1/2 |
| 4 | 12 | 1/2 | 0.500000 | Even ✓ |
| 5 | 68 | **17/30** | **0.566667** | Odd — above 1/2 |
| 6 | 360 | 1/2 | 0.500000 | Even ✓ |
| 7 | 2384 | **149/315** | **0.473016** | Odd — below 1/2 |
| 8 | 20160 | 1/2 | 0.500000 | Even ✓ |

## Why Even k Gives Exactly 1/2

The Eulerian numbers satisfy the symmetry A(k,q) = A(k, k-1-q). For even k, the state space {0,...,k-1} has even size k, and the symmetry q ↔ k-1-q pairs each even-q state with an odd-q state with equal Eulerian weight. Therefore the even-q and odd-q totals are equal: each is k!/2, giving P_∞ = 1/2 exactly.

For odd k, the state space has odd size k. The symmetry pairs all states except the middle state q* = (k-1)/2. The middle state falls in an even or odd slot depending on k:

$$
q^* = \frac{k-1}{2} \quad \text{is even iff } k \equiv 1 \pmod{4}
$$

This unpaired mass at q* produces the Eulerian parity offset, alternating sign as k steps through odd values:

| k (odd) | q* | q* parity | Direction of offset |
|---|---|---|---|
| 3 | 1 | odd | P_∞ < 1/2 |
| 5 | 2 | even | P_∞ > 1/2 |
| 7 | 3 | odd | P_∞ < 1/2 |
| 9 | 4 | even | P_∞ > 1/2 |

The deviations from 1/2 are: k=3: −1/6, k=5: +1/15, k=7: −17/630. These are damped by the factorial denominator.

---

# 2. Theorem I — General Eigenvalue Law

## Theorem I

For the k-operand iid carry chain on states {0,...,k-1}:

$$
\boxed{\text{spec}(T^{(k)}) = \left\{1,\, \frac{1}{2},\, \frac{1}{4},\, \dots,\, \frac{1}{2^{k-1}}\right\} = \left\{2^{-j} : j = 0,\dots,k-1\right\}}
$$

**Verification (computed eigenvalues, k=2..8):**

| k | Computed eigenvalues | Expected | Match |
|---|---|---|---|
| 2 | [1.0000, 0.5000] | [1, 1/2] | ✓ |
| 3 | [1.0000, 0.5000, 0.2500] | [1, 1/2, 1/4] | ✓ |
| 4 | [1.0000, 0.5000, 0.2500, 0.1250] | [1, 1/2, 1/4, 1/8] | ✓ |
| 5 | [1.0000, 0.5000, 0.2500, 0.1250, 0.0625] | [1, ..., 1/16] | ✓ |
| 6 | [1.0000, ..., 0.0313] | [1, ..., 1/32] | ✓ |
| 7 | [1.0000, ..., 0.0156] | [1, ..., 1/64] | ✓ |
| 8 | [1.0000, ..., 0.0078] | [1, ..., 1/128] | ✓ |

The second eigenvalue is universally:

$$
\boxed{\lambda_2 = \frac{1}{2} \quad \text{for all } k \geq 2}
$$

The mixing timescale in bits is thus the same for every k: τ_mix ~ 1/log 2 ≈ 1.44 bits, regardless of how many operands are summed. What changes between k values is the initial transient structure (the amplitudes of each eigenmode in the initial condition δ₀), not the decay rate.

---

# 3. Theorem J — Spectroscopy Closed Form

## Theorem J

$$
\boxed{\Sigma(k) = P(S_1^{(k)} = 0) = \frac{1}{2} + 2^{-(k/2+1)}\left[\cos\!\left(\frac{k\pi}{4}\right) + \sin\!\left(\frac{k\pi}{4}\right)\right]}
$$

**Derivation:** Since q₀ = 0, the carry after bit 0 is q₁ = ⌊n₀/2⌋ where n₀ ~ Binomial(k, 1/2). So:

$$
\Sigma(k) = P(\lfloor n_0/2 \rfloor \text{ even}) = \sum_{n=0}^{k} \binom{k}{n} \frac{1}{2^k} \cdot \mathbf{1}[\lfloor n/2 \rfloor \text{ even}]
$$

Grouping by residue class of n mod 4: the condition ⌊n/2⌋ even holds for n ∈ {0,1,4,5,8,9,...} (i.e., n ≡ 0,1 mod 4). Writing the Binomial generating function evaluated at 4th roots of unity extracts these terms, yielding the cos+sin formula.

**Verification for k=1..16 — all 16 exact matches ✓.**

**Extended spectroscopy table:**

| k | Σ(k) | Decimal |
|---|---|---|
| 1 | 1 | 1.000000 |
| 2 | 3/4 | 0.750000 |
| 3 | 1/2 | 0.500000 |
| **4** | **3/8** | **0.375000 ← minimum** |
| **5** | **3/8** | **0.375000 ← minimum** |
| 6 | 7/16 | 0.437500 |
| 7 | 1/2 | 0.500000 |
| 8 | 17/32 | 0.531250 |
| 9 | 17/32 | 0.531250 |
| 10 | 33/64 | 0.515625 |
| 11 | 1/2 | 0.500000 |
| 12 | 63/128 | 0.492188 |
| 13 | 63/128 | 0.492188 |
| 14 | 127/256 | 0.496094 |
| 15 | 1/2 | 0.500000 |
| 16 | 257/512 | 0.501953 |

**Properties proven:**

$$
\boxed{\lim_{k \to \infty} \Sigma(k) = \frac{1}{2}}
$$

$$
\boxed{\min_k \Sigma(k) = \frac{3}{8}, \quad \text{achieved at } k = 4, 5}
$$

$$
\boxed{\Sigma(k) \text{ has period 8 in the oscillatory envelope}}
$$

$$
\boxed{\Sigma(k+1) = \Sigma(k) \text{ for } k \in \{4,5\},\ \{8,9\},\ \{12,13\},\dots \quad \text{(twin-k pairs)}}
$$

---

# 4. Odd-k Regimes in SHA

The SHA schedule is nominally k=4 (four operands in the recurrence). But structural zeros — from PAD entries, SHR boundaries, and σ operator shift-outs — can create effective odd-k windows at specific bit positions.

**PAD-induced k=2:** W[16] = σ₀(W₁) + W₀. Even k. P_∞ = 1/2. Σ = 3/4.

**SHR^10 boundary in σ₁:** At bit positions j=0..9 of a word drawing σ₁(W_{t-2}), the SHR^10 component contributes 0. The effective operand count at those bit positions drops: at bit j < 10, σ₁(W_{t-2})[j] = ROTR₁₇(W_{t-2})[j] ⊕ ROTR₁₉(W_{t-2})[j] (XOR of two bits from W_{t-2}). This does not eliminate the operand — the ROTR terms are still present — but it removes one term from the XOR structure, producing a 3-bit XOR instead of 3-bit XOR + shifted term. The effective carry contribution at these positions is between k=3 and k=4.

**Implication:** Odd effective-k windows create P_∞ ≠ 1/2. For k_eff = 3: P_∞ = 1/3. This is a measurable deviation from the even-k baseline, detectable in empirical scar statistics. The spectroscopic measurement Σ(k) can distinguish these regimes from a single bit-1 scar survey.

---

# 5. Complete Theorem Stack (Phases 520–523)

| Theorem | Phase | Statement |
|---|---|---|
| A | 520 | Universal XOR LSB: (Σ X_m)₀ = ⊕ (X_m)₀ |
| B | 521 | S_{t,0} = 0 ∀ t ∈ [16..63] — universal schedule anchor |
| C | 520 | Upward carry causality: δ_j → supp(δW) ⊆ {j,...,31} |
| D | 520/521 | Carry scar parity: S_{t,j} = q_j mod 2 |
| E | 521 | P(S_j^{(2)}=0) = (1 + 2^{-j})/2 — PAD boundary closed form |
| F | 522 | spec(T^{(4)}) = {1, 1/2, 1/4, 1/8}, λ₂ = 1/2 |
| G | 522 | P(S_j^{(4)}=0) = 1/2 − 2^{-(j+1)} + 8^{-j} — generic schedule closed form |
| **H** | **523** | **Eulerian carry parity: P_∞^{(k)}(S=0) = Σ_{q even} A(k,q)/k!** |
| **I** | **523** | **General eigenvalue law: spec(T^{(k)}) = {2^{-j} : j=0,...,k-1}** |
| **J** | **523** | **Spectroscopy: Σ(k) = 1/2 + 2^{-(k/2+1)}[cos(kπ/4)+sin(kπ/4)]** |

---

# 6. Open Problems (Revised — Phase 523)

~~2. Compute the mixing eigenvalue λ₂ of the 4-operand chain.~~ **CLOSED — λ₂ = 1/2 (Phase 522).**

~~4. Characterize the global structure of Σ(k) and prove convergence.~~ **CLOSED — Theorem J (Phase 523).**

Remaining:

1. **Non-iid correction:** σ operators create within-word bit correlations. Derive the perturbative correction to P(S_{t,j}=0) from these correlations as a second-order term over the Markov baseline. This is the gap between the analytical 2-operand prediction and the observed residuals above bit 6 in Phase 521.

2. **Odd-k effective-window quantification:** The SHR boundary creates effective k=3 windows at specific (t,j) pairs. Compute the exact bit positions and word indices where k_eff deviates from 4, and measure P_∞ empirically at those positions. Compare against the Eulerian prediction 1/3.

3. **Proof of Theorem I:** The general eigenvalue law is computationally verified for k=2..8. A proof that spec(T^{(k)}) = {2^{-j} : j=0,...,k-1} for all k is open. The structure of T^{(k)} suggests a connection to the binary representation of carry counts.

4. **Reverse decoding algorithm:** Formalize the prefix-decoding procedure: given bits 0..r of W_t from the carry-free anchor upward, propagate q_j deterministically and constrain the remaining bits. The Eulerian stationary distribution gives the prior on q_j for large j; the Markov chain propagation gives the exact conditional.

5. **k-general closed-form decay:** The decay P(S_j^{(k)}=0) is solved for k=2 (Theorem E) and k=4 (Theorem G). Derive the general formula for all k from the eigendecomposition.

---

# Appendix — Live Output (Phase 523 Engines)

```
PHASE 523 — Eulerian Stationary Distribution Verification
Eulerian numbers A(k,q) verified for k=1..8: all match k!

Stationary P_inf(S=0) vs expected:
  k=1: 1 == 1 ✓
  k=2: 1/2 == 1/2 ✓
  k=3: 1/3 == 1/3 ✓
  k=4: 1/2 == 1/2 ✓
  k=5: 17/30 == 17/30 ✓
  k=6: 1/2 == 1/2 ✓
  k=7: 149/315 == 149/315 ✓
  k=8: 1/2 == 1/2 ✓

PHASE 523 — Sigma(k) Closed Form: k=1..16 — 16/16 exact matches ✓

PHASE 523 — General Eigenvalue Law: k=2..8 — 7/7 verified ✓

PHASE 523 — Stationary Markov vs Eulerian: k=3,5,7 — diff < 1e-10 ✓

Even/odd parity deviations from 1/2:
  k=3: deviation = -1/6 (below)
  k=5: deviation = +1/15 (above)
  k=7: deviation = -17/630 (below)
Alternating sign confirmed.
```

---

# Final Collapse

$$
\boxed{S_{t,0} = 0 \quad \forall\, t \in [16..63]}
$$

$$
\boxed{P_\infty^{(k)}(S=0) = \sum_{q \text{ even}} \frac{A(k,q)}{k!}}
$$

$$
\boxed{\text{spec}(T^{(k)}) = \left\{1,\, \frac{1}{2},\, \frac{1}{4},\, \dots,\, \frac{1}{2^{k-1}}\right\}}
$$

$$
\boxed{\Sigma(k) = \frac{1}{2} + 2^{-(k/2+1)}\left[\cos\!\frac{k\pi}{4} + \sin\!\frac{k\pi}{4}\right]}
$$

$$
\boxed{\text{The SHA schedule scar field is an operand-count spectrometer.}}
$$

$$
\boxed{\text{The scar is Markovian memory, and its first bit is an operand-count fingerprint.}}
$$
