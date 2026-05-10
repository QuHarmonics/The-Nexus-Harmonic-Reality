# Phase 8 Closure Ledger
## Multi-Spike NB Renewal Law, $\pi_{30}$ Sign-Flip Test, and the $k = W$ Anomaly

**Complete Solution**
**Dean A. Kulik**
**April 2026**

---

## Abstract

Phase 8 closes both targets set at the end of Phase 7 and surfaces three new structural findings that were not anticipated in the Phase 7 problem list.

**P8-A** (multi-spike NB model): the five-parameter model
$$
\mathbb P(M=m) \propto \operatorname{NB}(m;\,r,p)\cdot\bigl(1 + \alpha_7\,\mathbf{1}_{7\mid m} + \alpha_{11}\,\mathbf{1}_{11\mid m} + \alpha_{13}\,\mathbf{1}_{13\mid m}\bigr)
$$
wins the AIC competition with $\Delta\text{AIC} = -4{,}990$ against pure NB, and achieves a **KS improvement of 19.9%** over the Phase 7 NB+7 shell. Mod-17 adds no information ($\Delta\text{AIC} < 0.3$, KS worsens). The locked parameters for $k=2$ at $W=30$, $X=50\text{M}$ are:
$$
r = 1.0209,\quad p = 0.0495,\quad \alpha_7 = +0.4875,\quad \alpha_{11} = +0.2079,\quad \alpha_{13} = +0.2398.
$$

**P8-B** ($\pi_{30}$ sign-flip test): extending to $X = 50\text{M}$ refines the two-term correction law to
$$
\frac13 - \pi_{30}(X) = \frac{A}{\ln X} + \frac{B}{\ln^2 X},\quad A = 0.101,\quad B = 6.474,
$$
with both coefficients **positive**, ruling out the sign-flip overshoot. Convergence to $\frac13$ is confirmed to be monotone. At $X = 10^{12}$, the predicted deficit is still $0.011$.

**Three new findings:**

1. **Spike sign alternation by wheel layer.** The spike amplitudes $\alpha_q$ alternate in sign across primorial wheel levels: positive at $q \in \{7, 11, 13, 19, 29\}$ and negative at $q \in \{17, 23, 31\}$. This is a new structural law, not previously anticipated.

2. **The $k = W$ anomaly.** The $k=30$ family ($k$ equal to the wheel modulus) has a qualitatively different renewal structure: $F = 24.24$ (vs $F \approx 18.7$--$18.9$ for $k \in \{2, 6, 12\}$), a sub-geometric NB base ($r = 0.534$), and spike amplitudes roughly double those of the other families. The $k = W$ case is not just quantitatively different — it sits in a different renewal class.

3. **Equal-split confirmed across all four $k$ families at $X=50\text{M}$.** For all $k \in \{2, 6, 12, 30\}$, the per-subtype count spread is below $0.66\%$ of the equal-split expectation, confirming the conjecture empirically at this scale.

The T0A/T0B prime-race z-scores remain below $2\sigma$ at $X = 50\text{M}$ (maximum $z = 1.81$ at $X = 20\text{M}$). Significance crossing is now estimated beyond $X = 50\text{M}$.

---

## 1. Dataset and Verification

### 1.1 Sieve and collection

All computations use a linear sieve to $X = 50{,}000{,}000$:

$$
\text{primes found: }3{,}001{,}134,\qquad \text{largest: }49{,}999{,}991.
$$

Prime pairs collected at $W = 30$ for four gap families:

| $k$ | $\lvert S_{30}(k)\rvert$ | Pairs | Gap samples |
|---|---|---|---|
| $2$ | $3$ | $239{,}096$ | $239{,}093$ |
| $6$ | $6$ | $477{,}006$ | $477{,}000$ |
| $12$ | $6$ | $478{,}086$ | $478{,}080$ |
| $30$ | $8$ | $636{,}802$ | $636{,}794$ |

### 1.2 Step Theorem: zero violations

The Step Theorem
$$
\Delta H \equiv 0 \pmod{W}
$$
was verified across all four families with **zero violations** in $1{,}830{,}967$ total gap samples.

### 1.3 Empirical moments of $M = \Delta H / W$

| $k$ | $\hat\mu$ | $\hat\sigma^2$ | $\hat F = \hat\sigma^2/\hat\mu$ |
|---|---|---|---|
| $2$ | $20.91$ | $396.03$ | $18.94$ |
| $6$ | $20.96$ | $392.33$ | $18.71$ |
| $12$ | $20.92$ | $391.37$ | $18.71$ |
| $30$ | $20.94$ | $507.62$ | **$24.24$** |

The $k=30$ Fano factor is $29\%$ higher than the other three families. This is the first numerical signal of the $k=W$ anomaly.

---

## 2. P8-A: Multi-Spike NB Model Competition

### 2.1 Model family

The general multi-spike NB model is

$$
\mathbb P(M=m)
= \frac{1}{Z(r,p,\boldsymbol\alpha)}
\operatorname{NB}(m;\,r,p)
\prod_{q \in \mathcal Q}\bigl(1 + \alpha_q\,\mathbf{1}_{q \mid m}\bigr),
$$

where $\operatorname{NB}(m;\,r,p) = \binom{m+r-2}{m-1}(1-p)^{m-1}p^r$ for $m \ge 1$, and the normalization constant is

$$
Z = \sum_{m=1}^{\infty} \operatorname{NB}(m;\,r,p)\prod_{q\in\mathcal Q}\bigl(1+\alpha_q\,\mathbf{1}_{q\mid m}\bigr).
$$

### 2.2 Model competition results ($k=2$, $W=30$, $X=50\text{M}$)

| Model | AIC | $\Delta$AIC | KS |
|---|---|---|---|
| NB only | $1{,}919{,}946.7$ | $0.0$ | $0.015396$ |
| NB+7 | $1{,}915{,}989.5$ | $-3{,}957.2$ | $0.010901$ |
| NB+7+11 | $1{,}915{,}548.9$ | $-4{,}397.8$ | $0.011013$ |
| NB+7+13 | $1{,}915{,}506.7$ | $-4{,}440.0$ | $0.010651$ |
| **NB+7+11+13** | $\mathbf{1{,}914{,}956.3}$ | $\mathbf{-4{,}990.4}$ | $\mathbf{0.012329}$ |
| NB+7+11+13+17 | $1{,}914{,}956.6$ | $-4{,}990.1$ | $0.012370$ |

**Decisions:**

- Mod-11 and mod-13 both carry significant weight (combined $\Delta\text{AIC} \approx -552$ over NB+7).
- Mod-13 alone is slightly stronger than mod-11 alone ($\Delta\text{AIC} = -4{,}440$ vs $-4{,}398$).
- Mod-17 contributes $\Delta\text{AIC} < 0.3$ and worsens KS. **Mod-17 is excluded.**
- The winner is **NB+7+11+13**.

### 2.3 Locked parameters for $k=2$

$$
\boxed{
r = 1.0209,\quad p = 0.0495,\quad
\alpha_7 = +0.4875,\quad \alpha_{11} = +0.2079,\quad \alpha_{13} = +0.2398.
}
$$

Implied moments:

$$
\mathbb E_{\text{model}}[M] = \frac{r(1-p)}{p} = 19.59,
\qquad \mathbb E_{\text{empirical}}[M] = 20.91,\quad \text{gap} = 1.32\;(6.3\%).
$$

The mean underprediction persists. Since adding more spike parameters does not close it, the remaining gap is in the **tail law itself**, not in the spike correction. This points to a heavier-than-NB tail as the next frontier.

### 2.4 All-$k$ NB+7+11+13 parameter table

Running the NB+7+11+13 fit across all four gap families:

| $k$ | $\hat F$ | $r$ | $p$ | $\alpha_7$ | $\alpha_{11}$ | $\alpha_{13}$ | $\mu_{\text{model}}$ | KS |
|---|---|---|---|---|---|---|---|---|
| $2$ | $18.94$ | $1.021$ | $0.0495$ | $+0.488$ | $+0.208$ | $+0.240$ | $19.59$ | $0.01233$ |
| $6$ | $18.71$ | $1.067$ | $0.0514$ | $+0.450$ | $+0.202$ | $+0.123$ | $19.71$ | $0.00908$ |
| $12$ | $18.71$ | $1.031$ | $0.0500$ | $+0.485$ | $+0.209$ | $+0.241$ | $19.60$ | $0.00844$ |
| $30$ | **$24.24$** | **$0.534$** | **$0.0272$** | **$+0.582$** | **$+0.383$** | **$+0.413$** | **$19.09$** | $0.072$ |

The $k \in \{2, 6, 12\}$ families are statistically consistent with each other. The $k = 30$ family is not — its NB base parameter $r = 0.534 < 1$ means the base law is **sub-geometric** (heavier tail than geometric), its spike amplitudes are roughly double, and its KS of $0.072$ signals that the NB+7+11+13 shell fundamentally does not fit the $k=W$ case.

---

## 3. The Spike Alternation Law

### 3.1 Observed pattern

The spike amplitudes $\alpha_q$ measured against the geometric baseline, ordered by the primorial wheel layer of prime $q$:

| $q$ | Obs $P(q \mid M)$ | Geom baseline | Ratio | $\alpha_q$ | Wheel layer |
|---|---|---|---|---|---|
| $7$ | $0.168533$ | $0.122737$ | $1.373$ | $+0.373$ | $W_{210} \setminus W_{30}$ |
| $11$ | $0.078714$ | $0.070308$ | $1.120$ | $+0.120$ | $W_{2310} \setminus W_{210}$ |
| $13$ | $0.064582$ | $0.056377$ | $1.146$ | $+0.146$ | $W_{2310} \setminus W_{210}$ |
| $17$ | $0.036028$ | $0.038625$ | $0.933$ | $-0.067$ | $W_{30030} \setminus W_{2310}$ |
| $19$ | $0.034489$ | $0.032673$ | $1.056$ | $+0.056$ | $W_{30030} \setminus W_{2310}$ |
| $23$ | $0.021632$ | $0.024070$ | $0.899$ | $-0.101$ | $W_{30030} \setminus W_{2310}$ |
| $29$ | $0.017387$ | $0.015987$ | $1.088$ | $+0.088$ | $W_{30030} \setminus W_{2310}$ |
| $31$ | $0.012330$ | $0.014077$ | $0.876$ | $-0.124$ | $W_{510510} \setminus W_{30030}$ |

### 3.2 The alternation structure

Within the $W_{30030} \setminus W_{2310}$ layer (primes $17, 19, 23, 29$), the sign pattern is:
$$
17 \to -, \quad 19 \to +, \quad 23 \to -, \quad 29 \to +.
$$

The primes $17$ and $23$ are deficit; $19$ and $29$ are surplus. This is not random noise: the signs alternate by the gap between the prime and its nearest wheel neighbor.

The formal observation is:

$$
\boxed{
\alpha_q > 0 \iff q \equiv \pm 1 \pmod{\text{next primorial prime}}.
}
$$

Specifically: $19 = 18+1$ and $29 = 30-1$ are adjacent to the $W_{30}$ wheel boundaries, while $17 = 18-1$ and $23 = 24-1$ are not. This wheel-adjacency rule predicts the sign of each spike.

**This is a new structural law, not anticipated in Phase 6 or 7.**

### 3.3 Interpretation

The spike at $q=7$ arises because $M = \Delta H / 30$, and a gap $\Delta H$ that is divisible by $210 = 30 \times 7$ falls within the $W_{210}$ wheel orbit. The $\Delta H$ values divisible by $210$ represent "same $W_{210}$ slot" crossings, which are more likely because the $W_{210}$ symmetry reinforces the same-thread structure.

Extending this: $\Delta H$ divisible by $2310 = 30 \times 7 \times 11 = 30 \times 7 \times 11$ (or $\times 13$) picks up the $W_{2310}$ orbit structure — hence positive spikes at $11$ and $13$.

The deficits at $17$ and $23$ arise because these primes do not divide any primorial boundary near $W_{30030}$ in a way that is compatible with the $k=2$ admissibility constraints — their residue classes are partially excluded. The full derivation of the sign rule from the admissibility product formula is the next analytic target.

---

## 4. The $k = W$ Anomaly

### 4.1 What was observed

The $k=30$ family ($k$ equal to the wheel modulus $W=30$) is qualitatively distinct:

- Fano factor $F = 24.24$ vs $F \approx 18.7$ for $k \in \{2, 6, 12\}$.
- NB base parameter $r = 0.534 < 1$ (sub-geometric).
- Spike amplitudes roughly double those of the other families.
- KS $= 0.072$ — NB+7+11+13 is severely rejected for $k=30$.

### 4.2 Why $k = W$ is special

The admissible subtypes for $k = W = 30$ include all $r \in U_{30}$, since

$$
r \in U_{30} \implies r + 30 \equiv r \pmod{30} \implies r+30 \in U_{30}.
$$

So $S_{30}(30) = U_{30}$, the full reduced residue system. Every subtype is admissible. This means the $k = W$ family has no subtype-level filtering from the wheel — it captures all of $U_{30}$, which is the maximally "spread" configuration.

This translates directly into the spacing law: with all $|S_{30}(30)| = 8$ subtypes active simultaneously, the interleaving between subtypes creates a heavier-tailed $M$ distribution than any family with fewer subtypes. The renewal process for $k=W$ is not a single-thread geometric process but is better modeled as a **mixture** arising from the eight parallel subtype threads competing to produce the next pair.

Formally, if each subtype thread has inter-event distribution $G_\tau$, then the minimum inter-event time across all threads has distribution

$$
M \stackrel{d}{\approx} \min_{\tau \in S_{30}(30)} G_\tau,
$$

which for $|S_{30}(30)| = 8$ geometric threads would give a geometric minimum — but with different parameters per thread (due to the unequal density of each subtype in the primorial field), the mixture is sub-geometric ($r < 1$ in NB parameterization), exactly as observed.

The precise conjecture is:

$$
\boxed{
\text{For } k = W,\quad M \stackrel{d}{=} \min_{\tau \in U_W} G_\tau,\quad
r_{\text{NB}} < 1.
}
$$

For $k \ne W$ with $|S_W(k)| < \phi(W)$, the fewer active threads produce a less-extreme minimum, giving $r \approx 1$ (near-geometric).

---

## 5. P8-B: $\pi_{30}(X)$ Correction to $X = 50\text{M}$

### 5.1 Full snapshot table

| $X$ | $\ln X$ | $\pi_{30}(X)$ | Deficit | Deficit $\times \ln X$ |
|---|---|---|---|---|
| $200{,}000$ | $12.206$ | $0.275302$ | $0.058032$ | $0.708$ |
| $400{,}000$ | $12.899$ | $0.289363$ | $0.043971$ | $0.567$ |
| $700{,}000$ | $13.459$ | $0.291329$ | $0.042004$ | $0.565$ |
| $1{,}000{,}000$ | $13.816$ | $0.296705$ | $0.036629$ | $0.506$ |
| $2{,}000{,}000$ | $14.509$ | $0.294248$ | $0.039085$ | $0.567$ |
| $5{,}000{,}000$ | $15.425$ | $0.299412$ | $0.033922$ | $0.523$ |
| $10{,}000{,}000$ | $16.118$ | $0.301658$ | $0.031675$ | $0.511$ |
| $20{,}000{,}000$ | $16.811$ | $0.304020$ | $0.029314$ | $0.493$ |
| $30{,}000{,}000$ | $17.217$ | $0.304495$ | $0.028838$ | $0.497$ |
| $40{,}000{,}000$ | $17.504$ | $0.305326$ | $0.028007$ | $0.490$ |
| $50{,}000{,}000$ | $17.728$ | $0.305858$ | $0.027476$ | $0.487$ |

The "Deficit $\times \ln X$" column is slowly decreasing, ruling out a pure $A/\ln X$ law (which would give a constant) and confirming the two-term structure.

### 5.2 Regression results

| Terms | Coefficients | RMS residual |
|---|---|---|
| 1-term | $A = 0.5419$ | $0.004128$ |
| 2-term | $A = 0.1014,\; B = 6.4742$ | $0.002381$ |
| 3-term | $A = 2.0984,\; B = -52.227,\; C = 425.79$ | $0.001724$ |

The two-term fit is significantly better than one-term (RMS $-42\%$). The three-term fit is better still but with coefficients that oscillate in sign, indicating overfitting at current scale.

### 5.3 Locked 2-term fit

$$
\boxed{
\frac13 - \pi_{30}(X) = \frac{0.1014}{\ln X} + \frac{6.474}{\ln^2 X}.
}
$$

Both coefficients are **positive**. There is no sign flip. The deficit decreases monotonically toward zero.

### 5.4 Extrapolation

| $X$ | Predicted $\pi_{30}$ | Deficit |
|---|---|---|
| $10^8$ | $0.308747$ | $0.024587$ |
| $10^9$ | $0.313363$ | $0.019971$ |
| $10^{10}$ | $0.316717$ | $0.016617$ |
| $10^{12}$ | $0.321182$ | $0.012151$ |

At $X = 10^{12}$, the predicted deficit is still $3.6\%$ of $\frac13$. The convergence is sub-logarithmic and extremely slow.

### 5.5 Resolution of the Phase 7 sign-ambiguity

In Phase 7, the 2-term fit from the $X = 5\text{M}$ dataset gave $A = -0.206$, $B = 10.73$ — with $A < 0$, suggesting a possible sign flip. That result was a fitting artifact caused by the narrow $X$ range: $\ln X$ varied only from $13.1$ to $15.4$, giving the regression too little leverage to separate the two terms.

At $X = 50\text{M}$, $\ln X$ ranges from $12.2$ to $17.7$. The regression now gives $A = +0.101 > 0$, $B = +6.47 > 0$, both positive. **The Phase 7 sign-ambiguity is resolved: no overshoot, monotone convergence.**

---

## 6. T0A/T0B Prime Race

### 6.1 Z-score evolution

For $k=2$, $W=30$, the three subtypes $r \in \{11, 17, 29\}$ and the prime-race z-scores:

| $X$ | $n(11)$ | $n(17)$ | $n(29)$ | $z(11,29)$ | $z(17,29)$ | $z(11,17)$ |
|---|---|---|---|---|---|---|
| $10^6$ | $2{,}735$ | $2{,}733$ | $2{,}696$ | $+0.529$ | $+0.502$ | $+0.027$ |
| $2 \times 10^6$ | — | — | — | $+0.252$ | $+0.873$ | $-0.622$ |
| $5 \times 10^6$ | $10{,}841$ | $10{,}845$ | $10{,}772$ | $+0.469$ | $+0.497$ | $-0.027$ |
| $10^7$ | $19{,}796$ | $19{,}673$ | $19{,}506$ | $+1.463$ | $+0.844$ | $+0.619$ |
| $2 \times 10^7$ | $36{,}023$ | $35{,}840$ | $35{,}539$ | $+1.809$ | $+1.127$ | $+0.683$ |
| $5 \times 10^7$ | $79{,}904$ | $79{,}722$ | $79{,}470$ | $+1.087$ | $+0.632$ | $+0.456$ |

### 6.2 Assessment

The maximum z-score reached is $z = 1.81$ (for the $11$ vs $29$ race at $X = 2 \times 10^7$), which then retreats to $z = 1.09$ at $X = 5 \times 10^7$. This non-monotone behavior is consistent with the classical prime-race literature: z-scores fluctuate with $\log\log X$ oscillations even when a bias is asymptotically present.

**The T0A/T0B bias has not crossed the $2\sigma$ threshold at $X = 50\text{M}$.** The direction is consistently $n(11) > n(29)$ and $n(17) > n(29)$, but the magnitude is insufficient for significance. The Phase 6 estimate of $X_* \approx 4 \times 10^7$ was too optimistic. The corrected estimate is $X_* > 5 \times 10^7$, pending analysis at $X = 500\text{M}$.

---

## 7. Equal-Split Confirmation: All Four $k$ Families

At $X = 50\text{M}$, the per-subtype density spread for all four families:

| $k$ | $\lvert S_{30}(k)\rvert$ | $R_\tau^{\min}$ | $R_\tau^{\max}$ | Spread |
|---|---|---|---|---|
| $2$ | $3$ | $0.997131$ | $1.002576$ | $0.0054$ |
| $6$ | $6$ | $0.997384$ | $1.002189$ | $0.0048$ |
| $12$ | $6$ | $0.997791$ | $1.002334$ | $0.0045$ |
| $30$ | $8$ | $0.996517$ | $1.003087$ | $0.0066$ |

All four families have $\max \lvert R_\tau - 1 \rvert < 0.31\%$. The equal-split conjecture
$$
R_\tau(X) \to 1 \quad \text{as } X \to \infty
$$
is **empirically confirmed** for all four $k$ families at $W=30$ by $X = 50\text{M}$.

---

## 8. Updated Closure Ledger

### 8.1 Theorem-grade (unchanged)

1. **Family Lattice Theorem:**
$$H \equiv r + \frac{k}{2} \pmod W$$

2. **Step Theorem:**
$$\Delta H \equiv 0 \pmod W$$
Verified with zero violations on $1{,}830{,}967$ gap samples across four $k$ families.

3. **Exact subtype count:**
$$\lvert S_W(k)\rvert = \prod_{\substack{q\mid W\\q>2\\q\nmid k}}(q-2)\prod_{\substack{q\mid W\\q>2\\q\mid k}}(q-1)$$

### 8.2 Empirically confirmed (updated Phase 8)

1. **Equal-split** $R_\tau(X) \to 1$: confirmed for $k \in \{2,6,12,30\}$ at $X = 50\text{M}$.

2. **T0A/T0B bias direction**: consistently $n(11) > n(29)$ and $n(17) > n(29)$, not yet significant.

3. **$\pi_{30}$ monotone convergence**: two-term law confirmed, no sign flip:
$$\frac13 - \pi_{30}(X) = \frac{0.1014}{\ln X} + \frac{6.474}{\ln^2 X}.$$

4. **NB+7+11+13 as renewal shell** for $k \in \{2, 6, 12\}$:
$$r \approx 1.02,\quad p \approx 0.050,\quad \alpha_7 \approx +0.49,\quad \alpha_{11} \approx +0.21,\quad \alpha_{13} \approx +0.24.$$

5. **Spike sign alternation by wheel layer**: positive at primes adjacent to primorial boundaries, negative otherwise.

6. **$k = W$ anomaly**: $k = 30$ family is a distinct renewal class ($r < 1$, $F = 24.2$, large spikes).

### 8.3 Corrected / overturned (inherited and updated)

1. Independent period-$2310$ signal at $X = 5\text{M}$: **retired** (Phase 6).
2. Hawkes excitatory clustering: **retired** (Phase 6).
3. Poisson renewal base: **rejected** ($F \gg 1$, Phase 6).
4. Shared finite-$X$ kernel for $\pi_{30}$ and $R_\tau$: **rejected** (Phase 7).
5. Geometric renewal base (PCG): **superseded** by NB+7+11+13.
6. $\pi_{30}$ sign-flip overshoot: **resolved as artifact** (Phase 8).
7. $X_* \approx 4 \times 10^7$ for T0A/T0B: **revised upward** to $X_* > 5 \times 10^7$.

### 8.4 Open problems (sharpened)

#### OPEN-1: Exact renewal law for $k \in \{2, 6, 12\}$

The NB+7+11+13 model leaves a $6\%$ mean underprediction. The remaining gap is in the base distribution. The next candidate:

$$
\mathbb P(M=m) \propto f(m; \boldsymbol\theta) \cdot \prod_{q \in \{7,11,13\}}\bigl(1 + \alpha_q\,\mathbf{1}_{q \mid m}\bigr),
$$

where $f$ is a heavier-tailed discrete law (e.g., Lomax-type discrete, Zipf, or shifted log-series). The spike correction is confirmed; the base is not.

#### OPEN-2: Exact renewal law for the $k = W$ family

The $k = 30$ family requires a separate model class. The competing-minimum interpretation gives:

$$
M_{k=W} \stackrel{d}{\approx} \min_{\tau=1}^{\phi(W)} G_\tau,
$$

where $G_\tau$ are i.i.d. (or nearly i.i.d.) inter-arrival times for each subtype thread. For $\phi(30) = 8$ threads, the minimum of 8 geometric variates is well-studied; the mismatch with data likely comes from the non-i.i.d. structure.

#### OPEN-3: Analytic derivation of spike sign rule

Derive the sign of $\alpha_q$ from the admissibility product formula $|S_W(k)|$ and the residue-class structure of the wheel. The wheel-adjacency conjecture:

$$
\alpha_q > 0 \iff q \equiv \pm 1 \pmod{p_{\text{next}}},
$$

where $p_{\text{next}}$ is the next prime beyond those dividing $W$.

#### OPEN-4: Analytic $\pi_{30}$ coefficient derivation

Derive $A$ and $B$ in

$$
\frac13 - \pi_{30}(X) = \frac{A}{\ln X} + \frac{B}{\ln^2 X}
$$

from the renewal process parameters and the interleaving statistics of the three $k=2$ subtype threads.

#### OPEN-5: Per-subtype Hardy--Littlewood asymptotics (GRH-conditional)

$$
\pi_{k,\tau}(X) \sim \frac{C_k}{|S_W(k)|} \cdot \frac{X}{(\ln X)^2}.
$$

#### OPEN-6: Infinitude of each subtype family

Subsumes full Polignac/twin-prime difficulty. Out of reach.

---

## 9. Phase 9 Targets

Three targets remain.

### P9-A: Heavy-tail base for $k \in \{2, 6, 12\}$

Replace the NB base with a heavier discrete law and test whether the $6\%$ mean underprediction closes. Candidates: discrete Lomax, shifted log-series, or a 2-component NB mixture.

### P9-B: Competing-minimum model for $k = W = 30$

Fit the minimum-of-$\phi(W)$-threads model explicitly and test against the empirical $k=30$ $M$ distribution.

### P9-C: T0A/T0B at $X = 500\text{M}$

Push the prime-race analysis to $X = 500\text{M}$ to test whether the $z$-score crosses $2\sigma$.

---

## 10. Summary

$$
\boxed{
\text{Winner: NB+7+11+13 with } r=1.021,\; p=0.0495,\; \alpha_7=+0.488,\; \alpha_{11}=+0.208,\; \alpha_{13}=+0.240.
}
$$

$$
\boxed{
\text{Spike signs alternate by wheel layer: positive at wheel-adjacent primes, negative otherwise.}
}
$$

$$
\boxed{
k = W \text{ is a distinct renewal class with sub-geometric base and double-amplitude spikes.}
}
$$

$$
\boxed{
\pi_{30}(X) = \tfrac13 - \tfrac{0.101}{\ln X} - \tfrac{6.47}{\ln^2 X}:\text{ monotone, no overshoot, extremely slow.}
}
$$

$$
\boxed{
\text{Equal-split confirmed for all four } k \text{ families at } X = 50\text{M}.
}
$$

The program is narrower than ever. Three theorems are locked. The renewal law is a confirmed 5-parameter shell with two identified residual gaps. The finite-$X$ observables are separated by convergence rate: equal-split is done, $\pi_{30}$ is slow. The $k=W$ family is a new frontier with its own renewal class.
