# NEXUS Prime-Gap Phase 10
## Corrected Variable Definitions, Settled Results, and Remaining Open Frontier

**Complete Solution**  
**Dean A. Kulik**  
**QuHarmonics Research Group / A-Mark9 / NEXUS Phase 1163+**

---

## Abstract

This document consolidates the corrected Phase 8–10 state of the NEXUS prime-gap program into one coherent solution ledger. The central result is that the project only becomes internally consistent once the variables are aligned with the code that generated the published numerical results.

Three variable-definition errors had previously contaminated interpretation:

1. the gap variable $M$ was accidentally treated as a pooled inter-arrival statistic rather than an **intra-subtype midpoint-gap** statistic,
2. the quantity $\pi_{30}(X)$ was accidentally measured as a max-class deviation rather than the **consecutive same-subtype fraction**,
3. the $k=30$ shell was interpreted with a tail story that the corrected diagnostics do not support.

After correcting these, the state of the program is:

- the **Primorial Family Lattice Theorem** remains the theorem-grade kernel,
- the **$k=2$ empirical shell** is now correctly keyed,
- the **spike signs** are analytically positive for all relevant primes $q>5$,
- the **$\pi_{30}$ finite-$X$ law** is numerically locked,
- the **$k=30$ shell** is reproducible but still requires a body/tail split model.

The result is not a final solution to the deep number-theoretic frontier, but it is a clean resolution of the project’s current empirical architecture.

---

## 1. The Locked Algebraic Core

Let $W$ be a primorial wheel and let

$$
U_W = (\mathbb{Z}/W\mathbb{Z})^\times
$$

be the reduced residue system modulo $W$.

For an even gap $k$, define the admissible subtype set

$$
S_W(k) = \{\, r \in U_W : r+k \in U_W \pmod W \,\}.
$$

For each prime pair $(p,p+k)$ in subtype $r$, define the midpoint center

$$
H = p + \frac{k}{2}.
$$

Then the theorem-grade kernel is:

### Family Lattice Theorem
$$
H \equiv r + \frac{k}{2} \pmod W.
$$

### Step Theorem
Within a fixed subtype, consecutive midpoint centers satisfy

$$
\Delta H \equiv 0 \pmod W.
$$

### Exact subtype count
The admissible subtype count is

$$
|S_W(k)| =
\prod_{\substack{q\mid W\\ q>2\\ q\nmid k}} (q-2)
\prod_{\substack{q\mid W\\ q>2\\ q\mid k}} (q-1).
$$

These three statements are the load-bearing algebraic floor of the program. Everything empirical sits on top of them.

---

## 2. Correct Variable Definitions

### 2.1 Intra-subtype midpoint-gap variable

The correct normalized gap variable is

$$
M = \frac{\Delta H}{W},
$$

where $\Delta H$ is the difference between **consecutive midpoint centers within the same subtype**.

Equivalently, if

$$
H_1^{(r)} < H_2^{(r)} < H_3^{(r)} < \cdots
$$

are the ordered midpoint centers in a fixed subtype $r$, then

$$
M_n^{(r)} = \frac{H_{n+1}^{(r)} - H_n^{(r)}}{W} \in \mathbb{N}_{>0}.
$$

This is **not** the same as pooling all prime-pair startpoints and dividing raw inter-arrivals by $W$.

The corrected construction is forced by the Step Theorem:

$$
H_{n+1}^{(r)} - H_n^{(r)} \equiv 0 \pmod W.
$$

Hence the quotient $M_n^{(r)}$ is an integer-valued renewal variable.

### 2.2 Correct definition of $\pi_{30}(X)$

For the twin-prime family at $W=30$, let the subtype labels of consecutive pairs up to $X$ be

$$
r_1, r_2, \dots, r_N \in \{11,17,29\}.
$$

The correct statistic is the fraction of **consecutive pairs** that land in the same subtype:

$$
\pi_{30}(X)
=
\frac{1}{N-1}
\sum_{j=1}^{N-1} \mathbf{1}_{r_j = r_{j+1}}.
$$

This is not the same thing as a max-class deviation from $1/3$.

### 2.3 Correct interpretation of the $k=30$ shell

For $k=30$, the same midpoint-gap construction must be used:

$$
M_{k=30} = \frac{\Delta H}{30}
$$

within fixed subtypes. Earlier pooled or alternate inter-arrival interpretations were phase-misaligned.

---

## 3. Corrected $k=2$ Empirical Shell

Using the correct $M$ definition, the $k=2$ shell at $W=30$ is modeled on the support

$$
M \in \{1,2,3,\dots\}.
$$

The NB base kernel is

$$
\operatorname{NB}(m;r,p)
=
\binom{m+r-2}{m-1}(1-p)^{m-1}p^r,
\qquad m \ge 1.
$$

This corresponds to

$$
M-1 \sim \operatorname{NB}(r,p)
$$

in the standard zero-based convention. Therefore the correct moments are

$$
\mathbb{E}[M] = 1 + \frac{r(1-p)}{p},
\qquad
\operatorname{Var}(M) = \frac{r(1-p)}{p^2}.
$$

### 3.1 Canonical additive spike law

The spike-corrected shell uses the additive law

$$
f_{\text{spike}}(m)
=
1
+
\alpha_7 \mathbf{1}_{7\mid m}
+
\alpha_{11} \mathbf{1}_{11\mid m}
+
\alpha_{13} \mathbf{1}_{13\mid m}.
$$

The full corrected shell is therefore

$$
\mathbb{P}(M=m)
=
\frac{1}{Z}
\operatorname{NB}(m;r,p)\,
f_{\text{spike}}(m)\,
f_{\text{body}}(m),
$$

where $Z$ is the normalization constant.

### 3.2 Empirical body correction

The currently effective body correction is modeled as a window boost

$$
f_{\text{body}}(m)
=
1 + \gamma\,\mathbf{1}_{6 \le m \le 15}.
$$

This is an **empirical** correction, not yet an analytic theorem. The data indicate that the main residual mass mismatch concentrates in the low-to-mid body, especially near the interval $[6,10]$, rather than uniformly across all $[6,15]$.

### 3.3 Active fitted shell

The working corrected $k=2$ shell is

$$
r = 1.021,\qquad
p = 0.050,
$$

$$
\alpha_7 = +0.488,\qquad
\alpha_{11} = +0.208,\qquad
\alpha_{13} = +0.240,
$$

$$
\gamma = +0.075.
$$

Interpretation:

- the NB base captures the coarse renewal law,
- the positive spikes capture primorial resonance at $7,11,13$,
- the body term repairs the low-mid block mass deficiency.

---

## 4. Analytic Spike-Sign Proof

This is the cleanest analytic advance of the corrected program.

Consider the gap $g$ between consecutive twin-prime **startpoints**. For a prime $q>5$, compare two cases in the Hardy–Littlewood singular-series local factor.

### Generic case: $q \nmid g$
The forbidden residues are

$$
\{0,2,g,g+2\}\pmod q,
$$

and are generically four distinct classes. The local factor is proportional to

$$
\frac{q-4}{q}.
$$

### Spike case: $q \mid g$
Then $0$ and $g$ coincide modulo $q$, and $2$ and $g+2$ coincide modulo $q$, leaving only two occupied classes. The local factor becomes

$$
\frac{q-2}{q}.
$$

Therefore the enhancement ratio is

$$
\frac{(q-2)/q}{(q-4)/q}
=
\frac{q-2}{q-4}.
$$

Since for every prime $q>5$,

$$
q-2 > q-4 > 0,
$$

we obtain

$$
\frac{q-2}{q-4} > 1.
$$

Hence all such spike corrections are positive:

$$
\boxed{
\alpha_q > 0
\quad\text{for the relevant }k=2\text{ inter-arrival spikes at }q>5.
}
$$

This replaces the earlier sign-alternation narrative for the $k=2$ shell.

---

## 5. The $\pi_{30}(X)$ Finite-$X$ Law

With the correct definition of consecutive same-subtype fraction, the finite-$X$ deficit law is numerically stable:

$$
\frac{1}{3} - \pi_{30}(X)
=
\frac{A}{\ln X}
+
\frac{B}{\ln^2 X},
$$

with fitted coefficients

$$
A = 0.104115,
\qquad
B = 6.662432.
$$

The law is therefore

$$
\boxed{
\frac{1}{3} - \pi_{30}(X)
=
\frac{0.104115}{\ln X}
+
\frac{6.662432}{\ln^2 X}.
}
$$

### 5.1 What is closed
The following are now numerically settled:

1. the statistic itself,
2. the sign,
3. the positive two-term structure,
4. consistency with the earlier $X=500\text{M}$ phase outputs.

### 5.2 What is still open
The **functional form** is supported, but the **analytic derivation of the coefficients** is still open.

The expected analytic shape is

$$
\pi_{30}(X)
=
\frac{1}{3}
+
\frac{a}{\ln X}
+
\frac{b}{\ln^2 X}
+
O\!\left(\frac{1}{\ln^3 X}\right),
$$

with the leading structure plausibly governed by Siegel–Walfisz-type control of residue-class imbalance. But the exact derivation of the observed pair

$$
(a,b)=(-0.104115,-6.662432)
$$

for the deficit form, or equivalently the positive coefficients in the deficit expression above, remains unfinished.

---

## 6. Equal-Split and Prime-Race Interpretation

The equal-split target across the three admissible $k=2$ subtypes at $W=30$ is

$$
R_\tau(X) \to 1
\qquad (\tau \in \{11,17,29\})
$$

where $R_\tau(X)$ denotes normalized subtype density relative to perfect equal split.

Empirically, the later runs support:

$$
\boxed{
\text{No persistent directional bias is detected through the tested range.}
}
$$

The T0A/T0B race does not sustain the earlier strong-bias interpretation. The better reading is:

- finite-$X$ fluctuations are real,
- temporary z-score peaks occur,
- but no monotone persistent subtype bias survives the corrected larger-scale analysis.

So the correct epistemic statement is:

$$
\boxed{
\text{the observed race behavior is consistent with oscillatory prime-race effects, not a locked directional asymmetry.}
}
$$

---

## 7. The $k=30$ Shell: Reproducible Fit vs Tail Truth

Using the corrected midpoint-gap construction, the earlier published NB fit for $k=30$ is reproducible:

$$
r \approx 0.534,\qquad p \approx 0.0272.
$$

That reproduces the historical shell numerically. However, the corrected diagnostics show that this fitted shell misidentifies the tail.

### 7.1 Mean-excess diagnostic

Define the mean-excess function

$$
e(t) = \mathbb{E}[M-t \mid M>t].
$$

Empirically for $k=30$, the tail is approximately flat near

$$
e(t) \approx 23.3.
$$

That implies an effective geometric tail scale

$$
p_{\text{eff}}
\approx
\frac{1}{e(t)+1}
\approx
\frac{1}{24.3}
\approx
0.041\text{–}0.042.
$$

But the published NB fit uses

$$
p \approx 0.0272,
$$

which corresponds to a much heavier tail than the empirical mean-excess suggests.

### 7.2 Interpretation

Therefore:

$$
\boxed{
\text{the historical }k=30\text{ NB shell is reproducible but not tail-faithful.}
}
$$

The current best reading is:

- the old shell fits the **body** reasonably,
- the tail is closer to geometric-like behavior with $p_{\text{eff}}\approx 0.042$,
- and a body/tail split or mixture model is the correct next step.

---

## 8. What Is Actually Settled

The current state can be separated cleanly.

### 8.1 Locked theorem core
$$
H \equiv r+\frac{k}{2}\pmod W,
\qquad
\Delta H \equiv 0 \pmod W,
$$

and the exact subtype-count product law.

### 8.2 Settled empirical shell for $k=2$
A corrected NB + additive spikes + body-correction shell on the properly defined intra-subtype midpoint-gap variable.

### 8.3 Settled spike-sign logic
For the $k=2$ shell, the spike signs are positive, explained by

$$
\frac{q-2}{q-4}>1.
$$

### 8.4 Settled $\pi_{30}$ numerical law
The finite-$X$ deficit law is numerically stable and matches the corrected large-scale outputs.

### 8.5 Settled re-interpretation of earlier claims
The following earlier stories are no longer active truth claims:

- pooled raw inter-arrival $M$ definitions,
- max-class deviation as $\pi_{30}$,
- strong persistent T0A/T0B directional bias,
- the claim that the $k=30$ tail is correctly captured by the old NB shell.

---

## 9. What Is Still Open

The open frontier is now short and precise.

### OPEN-1: Analytic derivation of the $\pi_{30}$ coefficients
The two-term form is numerically locked, but the derivation of

$$
A=0.104115,\qquad B=6.662432
$$

remains open.

### OPEN-2: Analytic explanation of the body correction
The body correction is real, but the exact window and amplitude are still empirical. The previously claimed “proof” of the lower bound was phase-misaligned.

### OPEN-3: Correct body/tail-aware model for $k=30$
The old shell is reproducible but not tail-faithful. The next model should separate body fit from tail fit, likely through either:
- a two-regime model, or
- a mixture model.

### OPEN-4: Deep analytic frontier
Beyond the empirical shell remain the hard classical questions:

- subtype Hardy–Littlewood asymptotics,
- infinitude of each subtype family,
- Polignac/twin-prime level statements.

---

## 10. Final State Map

The shortest clean summary is:

$$
\boxed{
\text{algebra locked}
}
$$

$$
\boxed{
\text{$k=2$ shell corrected}
}
$$

$$
\boxed{
\text{spike signs analytically positive}
}
$$

$$
\boxed{
\text{$\pi_{30}$ numerically stable}
}
$$

$$
\boxed{
\text{$k=30$ still needs body/tail separation}
}
$$

That is the current complete solution state.

---

## Appendix A. Core Equations

### A.1 Admissible subtype set
$$
S_W(k) = \{\, r \in U_W : r+k \in U_W \pmod W \,\}.
$$

### A.2 Center constraint
$$
H \equiv r + \frac{k}{2} \pmod W.
$$

### A.3 Step theorem
$$
\Delta H \equiv 0 \pmod W.
$$

### A.4 Exact subtype count
$$
|S_W(k)| =
\prod_{\substack{q\mid W\\ q>2\\ q\nmid k}} (q-2)
\prod_{\substack{q\mid W\\ q>2\\ q\mid k}} (q-1).
$$

### A.5 Intra-subtype midpoint-gap variable
$$
M = \frac{\Delta H}{W}.
$$

### A.6 NB base kernel
$$
\operatorname{NB}(m;r,p)
=
\binom{m+r-2}{m-1}(1-p)^{m-1}p^r.
$$

### A.7 Correct NB moments
$$
\mathbb{E}[M] = 1 + \frac{r(1-p)}{p},
\qquad
\operatorname{Var}(M)=\frac{r(1-p)}{p^2}.
$$

### A.8 Additive spike shell
$$
f_{\text{spike}}(m)
=
1
+
\alpha_7 \mathbf{1}_{7\mid m}
+
\alpha_{11} \mathbf{1}_{11\mid m}
+
\alpha_{13} \mathbf{1}_{13\mid m}.
$$

### A.9 Body correction
$$
f_{\text{body}}(m)
=
1+\gamma\,\mathbf{1}_{6\le m\le 15}.
$$

### A.10 Full corrected $k=2$ shell
$$
\mathbb{P}(M=m)
=
\frac{1}{Z}
\operatorname{NB}(m;r,p)\,
f_{\text{spike}}(m)\,
f_{\text{body}}(m).
$$

### A.11 Spike enhancement ratio
$$
\text{Enhancement}(q)=\frac{q-2}{q-4},\qquad q>5.
$$

### A.12 Correct $\pi_{30}$ statistic
$$
\pi_{30}(X)
=
\frac{1}{N-1}
\sum_{j=1}^{N-1} \mathbf{1}_{r_j=r_{j+1}}.
$$

### A.13 Finite-$X$ deficit law
$$
\frac{1}{3}-\pi_{30}(X)
=
\frac{0.104115}{\ln X}
+
\frac{6.662432}{\ln^2 X}.
$$

### A.14 Mean-excess function
$$
e(t)=\mathbb{E}[M-t\mid M>t].
$$

### A.15 Effective geometric tail rate from mean-excess
$$
p_{\text{eff}} \approx \frac{1}{e(t)+1}.
$$
