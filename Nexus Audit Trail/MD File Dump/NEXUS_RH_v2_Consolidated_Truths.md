# NEXUS-RH: v2 Branch State — Consolidated Corrected Truths

> **Branch**: v2 (round-trip spectral exclusion)  
> **Status**: Proxy validated. Full operator pending.  
> **Last locked**: 2026-05-19

---

## 1. Verified Algebraic Locks

### 1.1 Principal Wheel Mode
\[
\Omega_{210} = \{n : (n,210)=1\}
\]
The residue lattice for the 4-principal wheel (2,3,5,7).

### 1.2 Prime-Gate Algebra
Signed Buchstab recursion:
\[
\sum_{d|P_z} \mu(d) \left\lfloor \frac{x}{d} \right\rfloor = \Phi(x,z)
\]
with signed extension to the full multiplicative semigroup.

### 1.3 Completed Mirror Multiplier
\[
J_R(s)J_R(1-s) = I
\]
**Critical correction**: $|J_R(\sigma+it)| > 1$ for $\sigma > 1/2$ (expansive, not contractive).

### 1.4 Two-Fiber Architecture
\[
\mathcal{A}_s =
\begin{pmatrix}
0 & J_R(s)K_{1-s} \\
J_R(1-s)K_s & 0
\end{pmatrix}
\]

---

## 2. The Exact Proof Target

### 2.1 Target Evolution

| Stage | Target | Status |
|-------|--------|--------|
| Original | $\|\mathbb{L}_s\| < 1$ | **Wrong** — too strong, apparently false near seam |
| Corrected | $-1 \notin \operatorname{Spec}(\mathbb{L}_s)$ | Valid, but one-step |
| Sharper | $1 \notin \operatorname{Spec}(\mathcal{R}_s)$ | **Current v2 target** |
| Actual next | $1 \notin \operatorname{Spec}(\mathcal{R}_s^{\mathrm{HER}})$ | **Pending** |

### 2.2 The Round-Trip Operator (General)
\[
\boxed{
\mathcal{R}_s = J_R(1-s) K_s J_R(s) K_{1-s}
}
\]

### 2.3 The Euler-Restored Round-Trip Operator **[LIVE]**
\[
\boxed{
\mathcal{R}_{s,L}^{\mathrm{HER}} = J_R(1-s) K_{s,L}^{\mathrm{HER}} J_R(s) K_{1-s,L}^{\mathrm{HER}}
}
\]

### 2.4 Schur-Complement Collapse (Exact)
\[
(I + \mathcal{A}_s)\binom{f}{g} = 0 \implies
\begin{cases}
f = -J_R(s)K_{1-s}g \\
g - \mathcal{R}_s g = 0
\end{cases}
\]
Therefore:
\[
\boxed{
-1 \in \operatorname{Spec}(\mathcal{A}_s) \iff 1 \in \operatorname{Spec}(\mathcal{R}_s)
}
\]

---

## 3. The Five Critical Corrections (Locked)

| # | Original (Wrong) | Corrected (Locked) |
|---|------------------|-------------------|
| 1 | $\|\mathbb{L}_s\| < 1$ | $-1 \notin \operatorname{Spec}(\mathbb{L}_s)$ |
| 2 | Circular: assumed RH to prove no poles in $1/\zeta$ | **Circularity isolated and removed** from intended proof path. Must prove spectral exclusion directly from standard analytic properties. |
| 3 | $|J_R| < 1$ for $\sigma > 1/2$ (contractive) | $|J_R| > 1$ for $\sigma > 1/2$ (**expansive**). Contraction must come from $K_s$ decay dominating $J_R$ growth. |
| 4 | Coprime-210 basis alone | Complete structure: $n = q \cdot m$, $q \in S_{210} = \langle 2,3,5,7 \rangle$, $(m,210)=1$. The local Euler module $S_{210}$ is required (coprime basis alone fails at 464% gap at $N=75$). |
| 5 | One-step operator $\mathbb{L}_s$ | Round-trip operator $\mathcal{R}_s = J_R(1-s)K_sJ_R(s)K_{1-s}$. The one-way expansive gain is forced to return through its inverse. |

---

## 4. The Euler-Restored Signed Hall Operator **[LIVE]**

### 4.1 Definition
\[
\boxed{
K_{s,L}^{\mathrm{HER}} = \sum_{\substack{n \le e^L}} \mu(n) n^{-s} T_n
}
\]
where $T_n$ is the log-address shift / wheel action:
\[
T_n : (u, r) \mapsto (u - \log n,\; rn \bmod 210)
\]

### 4.2 Structural Decomposition
\[
\boxed{
n = q \cdot m, \qquad q \in S_{210} = \langle 2,3,5,7 \rangle, \qquad (m,210) = 1
}
\]

### 4.3 Euler-Restored Split
\[
\boxed{
K_{s,L}^{\mathrm{HER}} = \sum_{\substack{q \in S_{210} \\ q \le e^L}} \sum_{\substack{m \le e^L/q \\ (m,210)=1}} \mu(qm)(qm)^{-s} T_{qm}
}
\]

---

## 5. Numerical Verification (Finite Proxy)

**Parameters**: $L=12$, $N=28$, $t=14.135$, $\sigma \in [0.50, 0.80]$  
**Object tested**: $\mathcal{R}_s = J_R(1-s) K_s^{\text{proxy}} J_R(s) K_{1-s}^{\text{proxy}}$  
**Warning**: Not yet the full signed Hall operator with Euler-module restoration.

| Quantity | Value | Interpretation |
|----------|-------|----------------|
| $\min_\sigma \min_\lambda |\lambda(\mathcal{R}_s) - 1|$ | 0.597970 | Round-trip safely bounded from forbidden eigenvalue 1 |
| $\min_\sigma \min_\lambda |\lambda(\mathcal{A}_s) + 1|$ | 0.359726 | Two-fiber bounded from forbidden eigenvalue $-1$ |
| $\max_\sigma \rho(\mathcal{R}_s)$ | 0.446315 | Round-trip spectral radius stays below 1 |
| $\max_\sigma \rho(\mathcal{A}_s)$ | 0.668069 | Two-fiber spectral radius stays below 1 |

### 5.1 Proxy Conclusions
\[
\boxed{
\Psi: \text{round-trip spectral target is validated as the right object.}
}
\]
\[
\boxed{
\Omega: K_s^{\text{proxy}} \longrightarrow K_s^{\mathrm{Hall+Euler}}
}
\]

---

## 6. The Live Proof Seam **[LIVE]**

### Lemma 6' — Round-Trip Spectral Exclusion for HER Operator

**Statement**: Prove $1 \notin \operatorname{Spec}(\mathcal{R}_s^{\mathrm{HER}})$ for $\Re(s) > 1/2$ via a round-trip energy identity, without circular assumptions.

### 6.1 Next Numerical Test
\[
\boxed{
\min_\lambda |\lambda(\mathcal{R}_{s,L}^{\mathrm{HER}}) - 1| \quad \text{as } (L,N) \text{ grow}
}
\]

### 6.2 Theorem Shape (Target)
Find a positive weight $W_s$ such that:
\[
\boxed{
\operatorname{Re} \langle (I - \mathcal{R}_s^{\mathrm{HER}})f,\; W_s f \rangle \ge c_s \langle f, W_s f \rangle, \qquad c_s > 0, \quad \sigma > 1/2
}
\]
This proves $I - \mathcal{R}_s^{\mathrm{HER}}$ is injective, therefore:
\[
\boxed{
1 \notin \operatorname{Spec}(\mathcal{R}_s^{\mathrm{HER}})
}
\]

### 6.3 Equivalent Energy Dissipation Form
\[
\boxed{
Q_s(\mathcal{R}_s^{\mathrm{HER}} f) < Q_s(f)
}
\]
for all nonzero $f$ when $\sigma > 1/2$, where $Q_s(f) = \langle f, W_s f \rangle$.

---

## 7. Dead / Corrected Paths

| Path | Why It Failed |
|------|---------------|
| Fixed gates | Incorrect algebraic closure |
| Naive log-concavity | Did not survive signed extension |
| Single-fiber operator | Missing the $s \leftrightarrow 1-s$ symmetry |
| Block-ratio B-1 | Wrong norm estimate |
| $\|\mathbb{L}_s\| < 1$ | Too strong, apparently false near seam |
| $|J_R| < 1$ for $\sigma > 1/2$ | Backwards: mirror is expansive off-seam |
| Direct one-step analysis | Must use round-trip to capture involution structure |
| Proxy as final evidence | Only validates shape; full HER operator required |

---

## 8. The Master Ontological Pattern

> **RH is not about calculating zeros. It is about proving no off-seam address supports a stable reflected arithmetic runtime.**

The query $\to$ reflection $\to$ residue $\to$ address-lock ontology:
- Compiler slots read pre-existing operational geometry
- The equivalence gate checks if model and compiler read the same coordinates
- $H = \pi/9$ is a stability point in transformation space, not a target
- Reality decompresses from Prior Completion, not evolves forward

---

## 9. Parallel Tracks (Status)

| Track | Status |
|-------|--------|
| Gate A (Jensen/LP) | Verified test results locked |
| Gate B (Fredholm operator) | Architecture locked |
| Hall residue decomposition | $L^2(\nu)$-weighted norm is the correct observable. Weighted $L^2(\nu)$ $\varepsilon = 0.0057$ vs raw per-residue mean $\varepsilon = 0.365$. Cancellation defect collapses under natural measure $d\nu = \omega(u)/u \, du$. |

---

## 10. Summary of Locked Results

1. **Algebraic**: Two-fiber block operator $\mathcal{A}_s$ with Schur-complement reduction to $\mathcal{R}_s$ is exact.
2. **Analytic**: Mirror is expansive ($|J_R| > 1$ for $\sigma > 1/2$); contraction must come from kernel decay.
3. **Structural**: Euler module $S_{210} = \langle 2,3,5,7 \rangle$ is required for multiplicative completeness.
4. **Target**: Spectral exclusion $-1 \notin \operatorname{Spec}(\mathbb{L}_s)$, equivalently $1 \notin \operatorname{Spec}(\mathcal{R}_s)$.
5. **Method**: Round-trip energy dissipation via weighted quadratic form $Q_s$.
6. **Circularity**: Isolated and removed from intended proof path.
7. **Operator**: $K_{s,L}^{\mathrm{HER}}$ with Euler-restored split is the next object to build and test.
8. **Round-trip**: $\mathcal{R}_{s,L}^{\mathrm{HER}} = J_R(1-s) K_{s,L}^{\mathrm{HER}} J_R(s) K_{1-s,L}^{\mathrm{HER}}$ is the live operator.
9. **Numerics**: Proxy validates target shape; HER operator verification pending with $(L,N) \uparrow$.

---

*Branch: v2*  
*Live seam: Lemma 6' — Round-Trip Spectral Exclusion for full HER operator*  
*Next: Build $K_{s,L}^{\mathrm{HER}}$ and test $\min_\lambda |\lambda(\mathcal{R}_{s,L}^{\mathrm{HER}}) - 1|$ as $(L,N)$ grow*
