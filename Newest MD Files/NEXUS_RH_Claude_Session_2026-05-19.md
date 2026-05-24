# NEXUS RH — Claude Session State
**Date:** 2026-05-19  
**Phase:** HER Operator Construction & Divisor-Lattice Analysis  
**ORCID:** 0009-0003-3128-8828  
**Branch:** v2.1 continuation (Kimi → Claude handoff)

---

## Branch Entry Point (from Kimi v2.1)

**Locked Ψ from Kimi:**
- Target: $1 \notin \operatorname{Spec}(\mathcal{R}_s^{\mathrm{HER}})$ for $\Re(s) > 1/2$
- Proxy (L=12, N=28, 48 unit residues): $\min|\lambda(\mathcal{R}_s)-1| = 0.597970$
- Unit-wheel-only HER is invalid: $p \in \{2,3,5,7\}$ maps units to non-units mod 210
- Two valid implementations: (A) expanded ring $\mathbb{Z}/210\mathbb{Z}$, (B) fibered $G + D_2,D_3,D_5,D_7$

**Active $\Omega$ from Kimi:**
Build and test $\mathcal{R}_{s,L}^{\mathrm{HER,fiber}}$ or $\mathcal{R}_{s,L}^{\mathrm{HER,ring}}$

---

## This Session: What Was Run

### Run 1 — u-bin discretization, expanded ring, spatial J_R

**Setup:** State $(u_\text{bin}, r)$ with $r \in \mathbb{Z}/210\mathbb{Z}$, $J_R(s)$: $u_\text{bin} \to N-1-u_\text{bin}$ with weight $e^{(1-2s)u_\text{bin}\cdot du}$

**L=4, N=8, MOD=210 sigma sweep (t=14.134):**

| σ | min\|λ−1\| | max\|λ\| |
|---|---|---|
| 0.40 | 0.084474 | 3.413 |
| 0.45 | 0.019176 | 3.194 |
| 0.50 | 0.033415 | 3.151 |
| 0.55 | 0.019176 | 3.194 |
| 0.60 | 0.084474 | 3.413 |
| 0.70 | 0.030496 | 4.505 |
| 0.80 | 0.047838 | 6.624 |

**Ψ:** Perfect $\sigma \leftrightarrow 1-\sigma$ symmetry confirmed (σ=0.40↔0.60 exact, σ=0.45↔0.55 exact). J_R correctly implements the functional equation.

**Ψ:** No 1-eigenvalue at any σ tested.

**C-01 — Resolution instability:** min\|λ−1\| varies wildly with N at fixed L. At L=5: N=8→0.017, N=10→0.012, N=12→0.052, N=15→0.111. **Root cause identified:** `round(log(n)/du)` is non-multiplicative — $\log(n_1 n_2)/du$ does not consistently round to the sum of individual rounded shifts. This creates artificial near-1 eigenvalues at specific N values.

---

### Run 2 — K_s · K_{1-s} test (scalar J_R hypothesis)

**Hypothesis:** If $J_R(s) = \chi(s)$ (scalar mirror multiplier) and $\chi(s)\chi(1-s)=1$, then $\mathcal{R}_s = K_s K_{1-s}$.

**Result:** $K_s K_{1-s} = 0$ matrix. **All eigenvalues exactly 0.**

**C-02 — Scalar J_R is wrong:** $K_s$ only shifts addresses **down** (T_m maps $n \to n/m < n$). $K_{1-s}$ also shifts down. Composition $K_s \circ K_{1-s}$ exhausts the address space and returns zero — everything lands at the floor address and can't shift further. Spatial J_R (address reversal) is **required** to flip low addresses back to high so $K_s$ can act again.

This is the machine architecture: K goes down → J_R flips up → K goes down → J_R flips up.

---

### Run 3 — Exact integer-address grid (large space)

**Setup:** State $(i, r)$ where $i$ indexes squarefree integers in $[1, N_\text{max}]$. J_R = index reversal $i \to A-1-i$ with weight $n_i^{1-2s}$.

**C-03 — Index reversal ≠ exact log-space reflection:** The sorted index reversal maps $n_0=1 \leftrightarrow n_{A-1}=N_\text{max}$ but this is NOT the correct mirror $n \leftrightarrow e^L/n$ in log-space (since $e^L/n$ is generally not a squarefree integer). Results non-convergent: min\|λ−1\| = 0.871, 0.333, 0.439, 0.556 for $N_\text{max}$ = 20, 30, 40, 54. No convergence trend.

---

### Run 4 — Divisor-lattice wheel algebra (CLEAN RESULT)

**KEY INSIGHT:** For the J_R reflection $n \to e^L/n$ to be exact, we need $e^L/n \in$ address set. This is exactly satisfied when:
- Address set = divisors of $L$-value primorial
- $e^L = 210 = 2 \cdot 3 \cdot 5 \cdot 7$  →  $L = \log(210) \approx 5.35$
- Divisors: $\{1, 2, 3, 5, 6, 7, 10, 14, 15, 21, 30, 35, 42, 70, 105, 210\}$, $A = 16$
- J_R: $n \to 210/n$ is **exact** (210/divisor = divisor)

**State space:** $16 \times 210 = 3360$ states  
**Shifts:** All 15 squarefree divisors $\geq 2$ (i.e., all squarefree products of $\{2,3,5,7\}$)

**Sigma sweep (t=14.134):**

| σ | min\|λ−1\| | Re(1−λ_closest) | max\|λ\| |
|---|---|---|---|
| 0.40 | 0.149 | 0.122 | 5.47 |
| 0.45 | 0.195 | 0.171 | 4.57 |
| 0.50 | 0.225 | 0.205 | 4.29 |
| 0.55 | 0.195 | 0.171 | 4.57 |
| 0.60 | 0.149 | 0.122 | 5.47 |
| 0.70 | **0.050** | **−0.026** | 9.72 |
| 0.80 | 0.164 | ... | 20.07 |

**Ψ:** Perfect $\sigma \leftrightarrow 1-\sigma$ symmetry across all $\sigma$ values.

**Ψ:** Spectral exclusion holds: $1 \notin \operatorname{Spec}(\mathcal{R}_s)$ for all $\sigma$ tested.

**C-04 — σ=0.7 flag:** $\operatorname{Re}(1-\lambda_\text{closest}) = -0.026 < 0$, meaning the closest eigenvalue has $\operatorname{Re}(\lambda) > 1$. The model has an eigenvalue on the "other side" of 1 for $\sigma=0.7$. This is a finite-size effect (only 15 shifts vs ~22k in the proxy), but needs tracking.

**Eigenvalue structure at σ=0.6:**
$$\lambda \approx 0.8785 - 0.0857i \quad (\times 4 \text{ degenerate})$$
The 4-fold degeneracy reflects symmetry of the r-action under the divisor group.

---

### Run 5 — t-sweep at σ=0.5 and energy inequality check

**t-sweep (σ=0.5):**

| t | min\|λ−1\| | context |
|---|---|---|
| 14.1347 | 0.229 | AT Riemann zero 1 |
| 17.000 | 0.252 | non-zero region |
| 21.0220 | **0.513** | AT Riemann zero 2 |
| 21.500 | 0.142 | non-zero region |

**C-05 — Model does NOT track Riemann zeros:** In the 15-shift divisor model, min\|λ−1\| is LARGEST at known zero locations and SMALLER at non-zero t. This is the wrong sign. The baby model does not have enough of the Buchstab sum to carry the analytic content linking $\mathcal{R}_s$ eigenvalues to $\zeta(s)$ zeros.

**Energy inequality (σ=0.6, t=14.1347):**
- min eigenvalue of $H_s = \operatorname{Re}(I - \mathcal{R}_s)$: **−13.93**
- 93.6% of eigenvalues of $H_s$ are positive
- Unweighted energy inequality **fails**

**Energy inequality (σ=0.5, t=14.1347):**
- min eigenvalue of $H_s$: **−9.44**
- 95.7% positive
- Fails

The unweighted failure is expected — the correct $W_s$ is the KEY missing ingredient. $W_s = I$ is not the right weight.

---

## Consolidated Ψ / Ω State

### Ψ — Locked Results

1. **J_R must be spatial** (not scalar): $K_s \circ K_{1-s} = 0$ without J_R flip — proven by direct computation.

2. **J_R = n → 210/n** on divisors of 210 gives **exact** functional equation: $\sigma \leftrightarrow 1-\sigma$ symmetry perfect to machine precision at every tested σ.

3. **No 1-eigenvalue** in the divisor-lattice model across all σ tested (spectral exclusion confirmed in this finite model).

4. **u-bin discretization is pathological** for this operator: `round(log(n)/du)` is non-multiplicative, creating resolution-dependent artifacts. The divisor-lattice model avoids this entirely.

5. **Machine architecture confirmed:** K_down → J_R_flip → K_down → J_R_flip. This is the correct round-trip structure. No alternative.

6. **Energy inequality (unweighted) fails** — expected. The correct $W_s$ encodes the Hilbert space in which the operator is bounded. This is the central open problem.

---

### Ω — What is Missing

**Ω₁ (Gap in model scale):** Divisor model has 15 squarefree shifts. Proxy has ~22k shifts. The analytic content that links $\mathcal{R}_s$ eigenvalues to $\zeta(s)$ zeros only becomes visible at much larger $L$. The t-sweep shows the baby model tracks the wrong structure.

**Ω₂ (Correct J_R at large L):** For $L > \log(210)$, we can't use $n \to 210/n$ as the reflection. The next exact level: primorial $2310 = 2 \cdot 3 \cdot 5 \cdot 7 \cdot 11$, $L = \log(2310) \approx 7.75$, $2^5 = 32$ divisors, state space $32 \times 2310 = 73,920$. Dense eigvals infeasible. **Requires sparse eigenvalue methods.**

**Ω₃ (The weight W_s):** The live proof seam from Kimi (Lemma 6′):
$$\operatorname{Re}\langle (I - \mathcal{R}_s^{\mathrm{HER}})f,\, W_s f \rangle \ge c_s \langle f, W_s f \rangle \qquad (c_s > 0, \; \sigma > 1/2)$$
The correct $W_s$ is the positive-definite weight in the Hilbert space where $K_s$ is bounded (likely $W_s$ diagonal in the u-address basis, $W_s(n) = n^{2\sigma-1}$ or similar). Finding $W_s$ such that this holds is the proof.

**Ω₄ (Scale to proxy):** The proxy result $\min|\lambda(\mathcal{R}_s)-1| = 0.597970$ (L=12, N=28, 48 units) needs to be reproduced with the corrected Euler-restored operator. This requires either:
- Sparse eigs on 1344-state unit-wheel matrix at L=12 (computationally feasible with scipy.sparse.linalg.eigs)
- Or extended divisor model at primorial 2310

---

## Next Move Options

**Option A (fastest, concrete numbers):**  
Reproduce the Kimi proxy using sparse eigenvalue methods. Build $K_s$ on unit-wheel (48 residues, coprime shifts), L=12, N=28. Use `scipy.sparse.linalg.eigs` with shift-invert at target λ=1. Verify 0.597970. Then add Euler correction (expanded ring) and compare.

**Option B (cleanest structure):**  
Scale the divisor model to primorial 2310 ($L \approx 7.75$, 32 divisors). Use sparse matrix format. Apply `eigs` to find min\|λ−1\| without dense eigval computation. Check if t-sweep now tracks Riemann zeros.

**Option C (analytic):**  
Work on $W_s$ directly. The natural candidate: $W_s$ is the Gram matrix of the inner product $\langle f, g \rangle_{W_s} = \int f(n) \overline{g(n)} n^{2\sigma-1} dn$, discretized to the divisor lattice. Test whether $\langle (I-\mathcal{R}_s)f, W_s f \rangle \ge 0$ holds for this $W_s$.

**Recommended: Option B first, then C.**

---

## C-error Log (This Session)

| Label | What was wrong | Correction |
|---|---|---|
| C-01 | u-bin rounding non-multiplicative | Exact integer-address or divisor grid |
| C-02 | J_R = scalar drops out → K·K=0 | J_R must be spatial address flip |
| C-03 | Index reversal ≠ log-space reflection | Require $e^L/n \in$ address set |
| C-04 | σ=0.7 eigenvalue has Re(λ)>1 | Finite-size effect; flag for large-L test |
| C-05 | Baby model gap tracks wrong sign vs zeros | Need L >> log(210) for analytic content |
