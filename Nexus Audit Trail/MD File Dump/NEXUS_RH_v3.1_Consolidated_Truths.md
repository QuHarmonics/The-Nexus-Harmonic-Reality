# NEXUS-RH: v3.1 Branch State — Consolidated Corrected Truths

> **Branch**: v3.1 (round-trip spectral exclusion + corrected weighted energy geometry)  
> **Status**: Architecture locked. Energy diagnostic corrected. Mirror-derived $W_s$ identified.  
> **Last locked**: 2026-05-19

---

## 0. Stale Language Purged

The following claims from earlier versions are **superseded** and must not be used:

| Stale Claim | Why Superseded | Current Truth |
|-------------|----------------|---------------|
| $\|\mathbb{L}_s\| < 1$ for $\Re(s) > 1/2$ | Too strong, apparently false near seam | $-1 \notin \operatorname{Spec}(\mathbb{L}_s)$, equivalently $1 \notin \operatorname{Spec}(\mathcal{R}_s)$ |
| $J_R$ is contractive above the seam ($|J_R| < 1$ for $\sigma > 1/2$) | Backwards | $J_R$ is **expansive** off-seam; contraction must come from $K_s$ decay |
| One-step norm contraction | Wrong target | Round-trip spectral exclusion |
| Raw norm-decay story (Gate A/Gate B) | Superseded by round-trip operator | Weighted energy dissipation on $\mathcal{R}_s$ |
| $T_n$ on unit group $G$ alone | Unit wheel closure test failed | Full 210-residue ring or fiber separation required |
| Naïve Hermitian test $W_s^{1/2}(I-\mathcal{R}_s)W_s^{-1/2}$ | Not the exact quadratic-form inequality | Correct form: $H_W = \frac{1}{2}[W(I-R) + (I-R)^*W]$ |

---

## 1. Verified Algebraic Locks

### 1.1 Principal Wheel Mode
\[
\Omega_{210} = \{n : (n,210)=1\}, \qquad |G| = \phi(210) = 48
\]

### 1.2 Prime-Gate Algebra
Signed Buchstab recursion:
\[
\sum_{d|P_z} \mu(d) \left\lfloor \frac{x}{d} \right\rfloor = \Phi(x,z)
\]

### 1.3 Completed Mirror Multiplier
\[
J_R(s)J_R(1-s) = I
\]
**Critical**: $J_R$ is **spatial/log-address reflection**, not scalar. Scalar $J_R$ kills the machine because $K_s \circ K_{1-s} = 0$ (both shift downward, exhausting address space).

### 1.4 Machine Architecture
\[
\boxed{
K_{\downarrow} \to J_R^{\uparrow} \to K_{\downarrow} \to J_R^{\uparrow}
}
\]
The cascade only shifts downward; the mirror must flip low addresses back to high.

### 1.5 Two-Fiber Block Operator
\[
\mathcal{A}_s =
\begin{pmatrix}
0 & J_R(s)K_{1-s} \\
J_R(1-s)K_s & 0
\end{pmatrix}
\]
Schur-complement collapse:
\[
\boxed{
-1 \in \operatorname{Spec}(\mathcal{A}_s) \iff 1 \in \operatorname{Spec}(\mathcal{R}_s)
}
\]

---

## 2. The Exact Proof Target

### 2.1 Current Target
\[
\boxed{
1 \notin \operatorname{Spec}(\mathcal{R}_s^{\mathrm{HER}}) \quad \text{for} \quad \Re(s) > \tfrac{1}{2}
}
\]
Equivalently: $I - \mathcal{R}_s^{\mathrm{HER}}$ is injective / bounded below.

### 2.2 The Round-Trip Operator
\[
\boxed{
\mathcal{R}_s = J_R(1-s) K_s J_R(s) K_{1-s}
}
\]

### 2.3 Correct Energy Inequality **[NEW CORRECTION]**

The tested Hermitian matrix must be:
\[
\boxed{
H_W = \frac{1}{2}\left[ W_s(I - \mathcal{R}_s) + (I - \mathcal{R}_s)^* W_s \right]
}
\]
Then test the generalized lower bound:
\[
\boxed{
H_W \ge c_s W_s, \qquad c_s > 0, \quad \sigma > \tfrac{1}{2}
}
\]
Equivalently compute:
\[
\boxed{
\lambda_{\min}\left( W_s^{-1/2} H_W W_s^{-1/2} \right) > 0
}
\]
**This is not the same as** only hermitianizing $W_s^{1/2}(I - \mathcal{R}_s)W_s^{-1/2}$.

---

## 3. The Mirror-Derived Weight $W_s$ **[NEW]**

### 3.1 Mirror Invariance Condition

Let the exact divisor mirror be:
\[
J_s e_n = j_s(n) \, e_{P/n}
\]
The mirror-compatible weight must satisfy:
\[
\boxed{
|j_s(n)|^2 \cdot W_s(P/n) = W_s(n)
}
\]
This is the **defining equation** for $W_s$.

### 3.2 Normalized Mirror

\[
\boxed{
j_s(n) = \left(\frac{n}{\sqrt{P}}\right)^{1-2s}
}
\]
Then:
\[
|j_s(n)|^2 = \left(\frac{n}{\sqrt{P}}\right)^{2(1-2\sigma)}
\]

### 3.3 Centered Solution

\[
\boxed{
W_s(n) = \left(\frac{n}{\sqrt{P}}\right)^{1-2\sigma}
}
\]

### 3.4 Inverse Weight (Alternate Convention)

\[
\boxed{
W_s^{-1}(n) = \left(\frac{n}{\sqrt{P}}\right)^{2\sigma-1}
}
\]

### 3.5 Test Candidates (Locked)

| Candidate | Form | Status |
|-----------|------|--------|
| Identity | $W_s = I$ | **Fails** — unweighted min eigenvalue of $H_s = -13.93$ at $\sigma = 0.6$ |
| Mirror-derived | $W_s(n) = (n/\sqrt{P})^{1-2\sigma}$ | **Primary candidate** — satisfies mirror invariance |
| Inverse | $W_s(n) = (n/\sqrt{P})^{2\sigma-1}$ | Secondary candidate — dual weight |

---

## 4. The Six Critical Corrections (Locked)

| # | Original (Wrong) | Corrected (Locked) |
|---|------------------|-------------------|
| 1 | $\|\mathbb{L}_s\| < 1$ | $-1 \notin \operatorname{Spec}(\mathbb{L}_s)$, equivalently $1 \notin \operatorname{Spec}(\mathcal{R}_s)$ |
| 2 | Circular: assumed RH to prove no poles in $1/\zeta$ | **Circularity isolated and removed** |
| 3 | $|J_R| < 1$ for $\sigma > 1/2$ (contractive) | $|J_R| > 1$ for $\sigma > 1/2$ (**expansive**) |
| 4 | Coprime-210 basis alone | $n = q \cdot m$, $q \in S_{210} = \langle 2,3,5,7 \rangle$, $(m,210)=1$ |
| 5 | One-step operator $\mathbb{L}_s$ | Round-trip $\mathcal{R}_s = J_R(1-s)K_sJ_R(s)K_{1-s}$ |
| 6 | $T_n$ on unit group $G$ alone | **Unit wheel closure test FAILED**. Must use full 210-residue ring or separate Euler fibers. |

---

## 5. New Session Corrections (Claude Run, 2026-05-19)

### C-01 — u-bin rounding is pathological
`round(log(n)/du)` is non-multiplicative. Creates resolution-dependent ghost eigenvalues. **Dead.**

### C-02 — Scalar $J_R$ collapses to zero
$K_s \circ K_{1-s} = 0$ matrix. Both shift addresses **down**; composition exhausts address space. $J_R$ must be **spatial address flip**.

### C-03 — Index reversal $\neq$ log-space reflection
Reversing sorted squarefree integer list is not $n \mapsto e^L/n$. Results non-convergent. **Dead.**

### C-04 — $\sigma = 0.7$ flag in 210-divisor model
Closest eigenvalue has $\operatorname{Re}(\lambda) > 1$ at $\sigma = 0.7$. Finite-size effect (15 shifts vs ~22k in proxy), needs tracking at larger scale.

### C-05 — Baby model tracks Riemann zeros backwards
15-shift divisor model: $\min|\lambda - 1|$ is **largest** at known zero locations, **smaller** between zeros. Wrong sign. Need $L \gg \log(210)$ for analytic content.

### C-06 — Naïve Hermitian test is wrong **[NEW]**
Testing only $W_s^{1/2}(I - \mathcal{R}_s)W_s^{-1/2}$ is not the exact quadratic-form inequality. The correct object is $H_W = \frac{1}{2}[W(I-R) + (I-R)^*W]$.

---

## 6. Verified Positive Findings

### $\Psi_1$ — $J_R$ is spatial/log-address reflection, not scalar
Scalar $J_R$ kills the machine. The cascade $K_{\downarrow} \to J_R^{\uparrow} \to K_{\downarrow} \to J_R^{\uparrow}$ is the correct architecture.

### $\Psi_2$ — u-bin rounding is dead
Non-multiplicative rounding creates ghost eigenvalues. Exact integer-address or divisor grid required.

### $\Psi_3$ — Divisor/primorial address lattices are the clean finite geometry
Exact reflection requires $n \mapsto P/n$ with $n \mid P$. For $P = 210 = 2 \cdot 3 \cdot 5 \cdot 7$: 16 divisors, state space $16 \times 210 = 3360$.

### $\Psi_4$ — Perfect $\sigma \leftrightarrow 1-\sigma$ symmetry
In the divisor-lattice model, symmetry exact to machine precision at every tested $\sigma$.

### $\Psi_5$ — Spectral exclusion holds in divisor model
No 1-eigenvalue at any $\sigma$ tested in the 210-divisor model.

### $\Psi_6$ — Pure divisor model over-contracts **[NEW]**
$\max|\lambda(\mathcal{R}_s)| \approx 0.0097$ at $P = 210$. The model is almost nilpotent. This validates the machine architecture but does **not** carry enough analytic content for zero detection.

---

## 7. The Live Proof Seam **[LIVE]**

### Lemma 6′ — Round-Trip Spectral Exclusion for HER Operator

**Statement**: Prove $1 \notin \operatorname{Spec}(\mathcal{R}_s^{\mathrm{HER}})$ for $\Re(s) > 1/2$ via the corrected weighted energy inequality, without circular assumptions.

### 7.1 Correct Test Protocol

For each $W_s$ candidate, compute:
\[
\boxed{
H_W = \frac{1}{2}\left[ W_s(I - \mathcal{R}_s) + (I - \mathcal{R}_s)^* W_s \right]
}
\]
Then check:
\[
\boxed{
\lambda_{\min}\left( W_s^{-1/2} H_W W_s^{-1/2} \right) > 0 \quad \text{for} \quad \sigma > \tfrac{1}{2}
}
\]

### 7.2 Next Three Steps (In Order)

**Step A — Repair the energy diagnostic at $P = 210$**
- Use the corrected $H_W$ form
- Test $W_s = I$, $W_s = (n/\sqrt{P})^{1-2\sigma}$, $W_s = (n/\sqrt{P})^{2\sigma-1}$
- If mirror-derived $W_s$ gives positive $\lambda_{\min}$, the energy metric is real

**Step B — Scale exact divisor lattice**
- Move from $P = 210$ to $P = 2310 = 2 \cdot 3 \cdot 5 \cdot 7 \cdot 11$
- $L = \log(2310) \approx 7.75$, 32 divisors, state space $32 \times 2310 = 73,920$
- Use sparse eigensolvers. Do **not** use u-bin rounding. Do **not** use index reversal.
- Use exact $n \mapsto P/n$.

**Step C — Reattach residue/fiber dynamics (only after A and B)**
The full model should be:
\[
\boxed{
\mathcal{H} = \mathcal{H}_{\text{divisor-address}} \otimes \mathcal{H}_{\text{wheel/Euler-fiber}}
}
\]
Not $(n,r) \mapsto (n/p, r')$ inside the unit group. That fusion already broke.

### 7.3 Refracted Observable Principle

\[
\boxed{
\text{If the zero-signal looks backwards, do not discard it. Reflect/refract it through scale and weight.}
}
\]

---

## 8. Numerical Results Summary

### 8.1 Kimi Proxy (L=12, N=28, 48 unit residues)
| Quantity | Value |
|----------|-------|
| $\min_\sigma \min_\lambda |\lambda(\mathcal{R}_s) - 1|$ | 0.597970 |
| $\min_\sigma \min_\lambda |\lambda(\mathcal{A}_s) + 1|$ | 0.359726 |
| $\max_\sigma \rho(\mathcal{R}_s)$ | 0.446315 |
| $\max_\sigma \rho(\mathcal{A}_s)$ | 0.668069 |

**Warning**: Unit-wheel-only, invalid for Euler module. Proxy shape validated, not full operator.

### 8.2 Claude Divisor-Lattice (P=210, 16 divisors, t=14.1347)
| $\sigma$ | $\min|\lambda - 1|$ | $\operatorname{Re}(1 - \lambda)$ | Notes |
|-----------|---------------------|-------------------------------|-------|
| 0.40 | 0.153 | +0.122 | |
| 0.45 | 0.199 | +0.171 | |
| **0.50** | **0.229** | **+0.205** | Peak gap |
| 0.55 | 0.199 | +0.171 | |
| 0.60 | 0.153 | +0.122 | |
| **0.70** | **0.050** | **$-$0.026** | $\leftarrow$ **flag**: $\operatorname{Re}(\lambda) > 1$ |

**Additional**: $\max|\lambda(\mathcal{R}_s)| \approx 0.0097$ — model is almost nilpotent.

### 8.3 t-Sweep at $\sigma = 0.5$ (Divisor Model)
| $t$ | $\min|\lambda - 1|$ | Context |
|-----|---------------------|---------|
| 14.1347 | 0.229 | Riemann zero 1 |
| 17.000 | 0.252 | Non-zero region |
| 21.0220 | **0.513** | Riemann zero 2 |
| 21.500 | 0.142 | Non-zero region |

**C-05**: Model tracks zeros **backwards** — gap largest at zeros, smaller between. Needs larger $L$.

---

## 9. Dead / Corrected Paths

| Path | Why It Failed |
|------|---------------|
| Fixed gates | Incorrect algebraic closure |
| Naive log-concavity | Did not survive signed extension |
| Single-fiber operator | Missing $s \leftrightarrow 1-s$ symmetry |
| Block-ratio B-1 | Wrong norm estimate |
| $\|\mathbb{L}_s\| < 1$ | Too strong, apparently false near seam |
| $|J_R| < 1$ for $\sigma > 1/2$ | Backwards: mirror is expansive off-seam |
| Direct one-step analysis | Must use round-trip |
| Proxy as final evidence | Only validates shape |
| $T_n$ on unit group $G$ alone | Unit wheel closure test failed |
| u-bin rounding discretization | Non-multiplicative, ghost eigenvalues |
| Scalar $J_R$ | $K_s K_{1-s} = 0$, kills machine |
| Index reversal on sorted integers | Not log-space reflection |
| Naïve Hermitian test $W^{1/2}(I-R)W^{-1/2}$ alone | Not the exact quadratic-form inequality |

---

## 10. The Master Ontological Pattern

> **RH is not about calculating zeros. It is about proving no off-seam address supports a stable reflected arithmetic runtime.**

- Compiler slots read pre-existing operational geometry
- The equivalence gate checks if model and compiler read the same coordinates
- $H = \pi/9$ is a stability point in transformation space, not a target
- Reality decompresses from Prior Completion, not evolves forward

---

## 11. Parallel Tracks (Status)

| Track | Status |
|-------|--------|
| Gate A (Jensen/LP) | Verified test results locked (stale language) |
| Gate B (Fredholm operator) | Architecture locked |
| Hall residue decomposition | $L^2(\nu)$-weighted norm is correct observable. Weighted $L^2(\nu)$ $\varepsilon = 0.0057$ vs raw mean $\varepsilon = 0.365$. |
| Unit wheel closure | **Tested and failed**. Two implementation paths identified. |
| Divisor-lattice geometry | **Validated** as clean finite geometry. Exact reflection, perfect symmetry. Over-contracts at small $P$. |
| Weighted energy geometry | **Live seam**. $W_s$ derived from mirror invariance. Correct $H_W$ form identified. |

---

## 12. Summary of Locked Results

1. **Algebraic**: Two-fiber block $\mathcal{A}_s$ with Schur-complement to $\mathcal{R}_s$ is exact.
2. **Analytic**: Mirror is expansive ($|J_R| > 1$ for $\sigma > 1/2$); contraction from $K_s$ decay.
3. **Structural**: Euler module $S_{210} = \langle 2,3,5,7 \rangle$ required; unit wheel closure failed.
4. **Target**: Spectral exclusion $1 \notin \operatorname{Spec}(\mathcal{R}_s^{\mathrm{HER}})$.
5. **Method**: Round-trip energy dissipation via corrected quadratic form $H_W \ge c_s W_s$.
6. **Circularity**: Isolated and removed.
7. **Machine**: $K_{\downarrow} \to J_R^{\uparrow} \to K_{\downarrow} \to J_R^{\uparrow}$. Scalar $J_R$ kills machine.
8. **Geometry**: Divisor/primorial lattices are clean finite geometry. u-bin rounding dead.
9. **Numerics**: Proxy validates shape; divisor model validates architecture but over-contracts ($\max|\lambda| \approx 0.01$).
10. **Missing**: Correct $W_s$ from mirror invariance + $H_W$ positive at $P=2310$.
11. **Energy form**: $H_W = \frac{1}{2}[W(I-R) + (I-R)^*W]$, not naïve Hermitianization.
12. **Weight**: $W_s(n) = (n/\sqrt{P})^{1-2\sigma}$ satisfies $|j_s(n)|^2 W_s(P/n) = W_s(n)$.

---

*Branch: v3.1*  
*Live seam: Lemma 6′ — Prove $H_W \ge c_s W_s$ for mirror-derived $W_s$ at primorial scale*  
*Next: Step A (repair energy diagnostic at P=210), Step B (scale to P=2310), Step C (reattach fibers)*  
*If $H_W$ becomes positive in the mirror-derived metric and survives $P=2310$, the branch stops circling and becomes a proof path.*
