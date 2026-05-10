# NEXUS Prime-Gap Program
## Canonical Closure Ledger
### Integrated Final State Through Phase 10 + Extension

**Dean A. Kulik**  
**QuHarmonics Research Group**  
**A-Mark9 / NEXUS Phase 1163+**

---

## Abstract

This document closes the **current program state** of the NEXUS prime-gap branch by merging the corrected Phase 10 writeup with the Phase 10 Extension into one canonical ledger.

The purpose of this document is precision. It does **not** claim that the deep classical frontier is solved. It does claim that the current NEXUS branch is now cleanly separated into:

1. a **theorem-grade algebraic core**,  
2. a **correctly keyed empirical shell**,  
3. a set of **identified analytic mechanisms**,  
4. a sharply delimited **remaining frontier**.

The main result is that the branch is no longer a stack of overlapping claims. The present closure state is:

- the **Primorial Family Lattice Theorem** is locked,
- the **Step Theorem** is locked,
- the **exact subtype-count law** is locked,
- the **$k=2$ renewal shell** is corrected and stable,
- the **spike signs** are analytically positive,
- the **$\pi_{30}(X)$ deficit law** is numerically locked and mechanistically decomposed,
- the **body correction** has a concrete wheel-overflow mechanism,
- the **$k=30$ branch** now has a body/tail-aware replacement shell,
- the **subtype Hardy–Littlewood asymptotic** is stated precisely,
- the remaining open problems are now specific and finite.

This is the canonical closure of what the project has so far.

---

## 1. Closure Convention

In this document, **closure** means one of four things:

### 1.1 Locked
A statement that is theorem-grade or exact within the branch.

### 1.2 Fitted
A statement that is numerically stable and internally consistent, but still empirical.

### 1.3 Mechanized
A statement for which the missing mechanism has been identified, even if the final derivation is incomplete.

### 1.4 Open
A statement that still requires new analytic work.

The purpose of this ledger is to prevent theorem, fit, mechanism, and speculation from bleeding into one another.

---

## 2. Locked Algebraic Core

Let $W$ be a primorial wheel and define

$$
U_W = (\mathbb{Z}/W\mathbb{Z})^\times.
$$

For an even gap $k$, define the admissible subtype set

$$
S_W(k) = \{\, r \in U_W : r+k \in U_W \pmod W \,\}.
$$

For each prime pair $(p,p+k)$ in subtype $r$, define the midpoint center

$$
H = p + \frac{k}{2}.
$$

Then the theorem-grade kernel is:

### 2.1 Family Lattice Theorem
$$
H \equiv r + \frac{k}{2} \pmod W.
$$

### 2.2 Step Theorem
For consecutive midpoint centers in a fixed subtype,

$$
\Delta H \equiv 0 \pmod W.
$$

### 2.3 Exact subtype count
$$
|S_W(k)| =
\prod_{\substack{q\mid W\\ q>2\\ q\nmid k}} (q-2)
\prod_{\substack{q\mid W\\ q>2\\ q\mid k}} (q-1).
$$

These three statements are the algebraic floor of the branch.

### 2.4 Closure state
$$
\boxed{
\text{LOCKED}
}
$$

---

## 3. Correct Variable Definitions

The later corrective phases showed that most instability in the branch was not caused by bad algebra. It was caused by bad variable identification.

### 3.1 Intra-subtype midpoint-gap variable

The correct renewal variable is

$$
M = \frac{\Delta H}{W},
$$

where $\Delta H$ is the midpoint difference between **consecutive centers in the same subtype**.

Equivalently, if

$$
H_1^{(r)} < H_2^{(r)} < H_3^{(r)} < \cdots
$$

are the ordered midpoint centers for subtype $r$, then

$$
M_n^{(r)} = \frac{H_{n+1}^{(r)} - H_n^{(r)}}{W} \in \mathbb{N}_{>0}.
$$

This is **not** the same as:

- pooled raw inter-arrivals,
- pooled startpoint gaps divided by $W$,
- or any subtype-unaware spacing variable.

### 3.2 Correct definition of $\pi_{30}(X)$

For the twin-prime family at $W=30$, with subtype labels

$$
r_1,r_2,\dots,r_N \in \{11,17,29\},
$$

the correct same-subtype adjacency statistic is

$$
\pi_{30}(X)
=
\frac{1}{N-1}\sum_{j=1}^{N-1}\mathbf{1}_{r_j=r_{j+1}}.
$$

This is the fraction of **consecutive twin-prime pairs** that land in the same subtype.

It is not the max-class deviation from $1/3$.

### 3.3 Correct handling of the $k=30$ branch

The same midpoint-gap construction must be used for $k=30$:

$$
M_{k=30} = \frac{\Delta H}{30}
$$

within fixed subtypes.

### 3.4 Closure state
$$
\boxed{
\text{LOCKED}
}
$$

---

## 4. The Corrected $k=2$ Renewal Shell

The twin-prime family at $W=30$ is the best-resolved empirical branch.

### 4.1 NB base kernel

The corrected shell lives on

$$
M \in \{1,2,3,\dots\}.
$$

The base kernel is

$$
\operatorname{NB}(m;r,p)
=
\binom{m+r-2}{m-1}(1-p)^{m-1}p^r,
\qquad m\ge 1.
$$

This corresponds to

$$
M-1 \sim \operatorname{NB}(r,p)
$$

in the standard zero-based convention.

Hence the correct moments are

$$
\mathbb{E}[M] = 1 + \frac{r(1-p)}{p},
\qquad
\operatorname{Var}(M) = \frac{r(1-p)}{p^2}.
$$

### 4.2 Additive spike law

The canonical spike law is additive:

$$
f_{\text{spike}}(m)
=
1
+
\alpha_7\,\mathbf{1}_{7\mid m}
+
\alpha_{11}\,\mathbf{1}_{11\mid m}
+
\alpha_{13}\,\mathbf{1}_{13\mid m}.
$$

### 4.3 Empirical body correction

The current working body correction is

$$
f_{\text{body}}(m)
=
1+\gamma\,\mathbf{1}_{6\le m\le 15}.
$$

This is an empirical correction, not yet theorem-grade.

### 4.4 Full corrected shell

The active $k=2$ shell is

$$
\mathbb{P}(M=m)
=
\frac{1}{Z}
\operatorname{NB}(m;r,p)\,
f_{\text{spike}}(m)\,
f_{\text{body}}(m),
$$

with fitted values

$$
r = 1.021,\qquad p = 0.050,
$$

$$
\alpha_7 = +0.488,\qquad
\alpha_{11} = +0.208,\qquad
\alpha_{13} = +0.240,
$$

$$
\gamma = +0.075.
$$

### 4.5 Closure state
$$
\boxed{
\text{FITTED}
}
$$

---

## 5. Spike Signs

This is the strongest analytic gain beyond the core algebra.

Let $g$ be the gap between consecutive twin-prime startpoints and let $q>5$ be prime.

### 5.1 Generic case: $q \nmid g$
The forbidden residue set

$$
\{0,2,g,g+2\}\pmod q
$$

contains four distinct classes, so the local factor is proportional to

$$
\frac{q-4}{q}.
$$

### 5.2 Spike case: $q \mid g$
Then $0$ and $g$ coincide mod $q$, and $2$ and $g+2$ coincide mod $q$, leaving only two occupied classes. The factor becomes

$$
\frac{q-2}{q}.
$$

Thus the enhancement ratio is

$$
\frac{(q-2)/q}{(q-4)/q}
=
\frac{q-2}{q-4}.
$$

Since

$$
\frac{q-2}{q-4} > 1
\qquad \text{for all } q>5,
$$

the spike signs must be positive.

### 5.3 Consequence

$$
\boxed{
\alpha_q > 0 \quad \text{for the relevant } k=2 \text{ spike primes } q>5.
}
$$

### 5.4 Closure state
$$
\boxed{
\text{LOCKED for sign, OPEN for exact finite-}X\text{ amplitude}
}
$$

---

## 6. Equal-Split and Subtype Symmetry

For the $k=2$, $W=30$ family, the admissible subtype residues are

$$
\{11,17,29\}.
$$

The asymptotic equal-split target is

$$
R_\tau(X)\to 1,
\qquad \tau \in \{11,17,29\},
$$

where $R_\tau(X)$ denotes subtype density relative to perfect equal split.

### 6.1 Structural statement

The admissible set $S_W(k)$ is acted on by the automorphism structure of the reduced residue system. For $k=2$, $W=30$, the subtype set behaves as one orbit under the wheel symmetry, which is the structural reason the equal-split law is the correct asymptotic target.

### 6.2 Conditional reading

The equal-split law follows from orbit symmetry **once** subtype infinitude / asymptotic existence is granted.

So the clean statement is:

$$
\boxed{
\text{equal-split follows from wheel symmetry given subtype asymptotic existence.}
}
$$

### 6.3 Closure state
$$
\boxed{
\text{MECHANIZED}
}
$$

---

## 7. The $\pi_{30}(X)$ Deficit Law

Define the same-subtype adjacency deficit

$$
D_{30}(X)=\frac{1}{3}-\pi_{30}(X).
$$

The numerically locked law is

$$
D_{30}(X)
=
\frac{0.104115}{\ln X}
+
\frac{6.662432}{\ln^2 X}.
$$

Equivalently,

$$
\boxed{
\frac{1}{3}-\pi_{30}(X)
=
\frac{0.104115}{\ln X}
+
\frac{6.662432}{\ln^2 X}.
}
$$

### 7.1 What is locked numerically
- the statistic,
- the sign,
- the two-term structure,
- consistency with the corrected large-scale runs.

### 7.2 Mechanism: two-layer decomposition

The extension identifies two analytically distinct layers.

#### Layer 1 — competing-renewal process structure
For three identical subtype-renewal processes with common inter-arrival PMF $P(M=m)$, the same-component consecutive probability is

$$
\pi_\infty
=
\sum_{m=1}^{\infty} P(M=m)\,[P(R>m)]^2,
$$

where the forward recurrence distribution satisfies

$$
P(R=r)
=
\frac{P(M\ge r)}{\mathbb{E}[M]},
\qquad r\ge 1.
$$

In the geometric approximation this yields

$$
\pi_\infty^{\mathrm{geo}}(p)
=
\frac{p(1-p)^2}{1-(1-p)^3},
$$

so

$$
D_\infty^{\mathrm{geo}}(p)
=
\frac13-\pi_\infty^{\mathrm{geo}}(p)
\approx \frac{p}{3}+O(p^2).
$$

This gives an upper-side bracket for the observed $A$ coefficient.

#### Layer 2 — Hardy–Littlewood singular-series weighting
Same-subtype and cross-subtype transitions carry different 4-tuple singular-series weights. The weighted finite-$X$ approximation is

$$
\pi_{30}(X)
\approx
\frac{\displaystyle\sum_{\substack{g \le G(X)\\30\mid g}} S(g)\,\ln^{-2}(X/g)}
{\displaystyle\sum_{g \le G(X)} S(g)\,\ln^{-2}(X/g)}.
$$

This gives the lower-side bracket for the observed $A$ coefficient.

### 7.3 Current closure state

$$
\boxed{
\text{FITTED: } D_{30}(X)
}
$$

$$
\boxed{
\text{MECHANIZED: competing renewal + HL weighting}
}
$$

$$
\boxed{
\text{OPEN: exact analytic derivation of } A=0.104115.
}
$$

---

## 8. Body Correction Mechanism

The body term is no longer just a fitted patch. It has a concrete proposed source.

### 8.1 Wheel-overflow from $q=7$

The wheel

$$
W=30=2\cdot 3\cdot 5
$$

screens divisibility by $2,3,5$ but is silent on the first unscreened prime

$$
q_{\text{next}}=7.
$$

This induces a systematic overflow scale

$$
m_* \approx \frac{W}{q_{\text{next}}} = \frac{30}{7}\approx 4.3,
$$

and a doubled scale

$$
2m_* \approx 8.6.
$$

So the primary overflow window sits roughly in the lower body, exactly where the residual excess concentrates.

### 8.2 Empirical meaning

The spike at $m=7$ captures the exact resonance.  
The body term captures the smooth excess around that resonance and its spill into the nearby zone.

### 8.3 Analytic path

The document’s proposed derivation path is to extend the wheel from

$$
W=30
\quad\text{to}\quad
W'=210=2\cdot 3\cdot 5\cdot 7,
$$

then compare the induced PMFs in the $m\in[6,15]$ region.

### 8.4 Current closure state

$$
\boxed{
\text{MECHANIZED: body correction as wheel-overflow from } q=7
}
$$

$$
\boxed{
\text{OPEN: first-principles derivation of } \gamma.
}
$$

---

## 9. The $k=30$ Branch

This branch is no longer summarized by a single-NB story.

### 9.1 Historical single-NB shell

The old fit is reproducible:

$$
r\approx 0.534,\qquad p\approx 0.0272.
$$

But the mean-excess diagnostic showed this shell was not tail-faithful.

### 9.2 Two-regime replacement model

The extension introduces a body/tail-aware shell:

$$
\mathbb{P}(M=m)
=
\begin{cases}
\dfrac{w_b \operatorname{NB}(m;r_b,p_b)}{\displaystyle\sum_{j=1}^{T}\operatorname{NB}(j;r_b,p_b)}
& 1\le m\le T,\\[10pt]
w_t\,p_t(1-p_t)^{m-T-1}
& m>T.
\end{cases}
$$

with fitted parameters

$$
T=62,\qquad
r_b=0.480,\qquad
p_b=0.021,
$$

$$
p_t=0.056,\qquad
w_b=0.972,\qquad
w_t=0.028.
$$

### 9.3 Interpretation

- the body is sub-geometric and over-dispersed,
- the tail is much closer to geometric,
- the old single shell collapsed two regimes into one parameter pair.

### 9.4 Closure state

$$
\boxed{
\text{FITTED: two-regime shell}
}
$$

$$
\boxed{
\text{MECHANIZED: body/tail split}
}
$$

This is the best current shell for $k=30$.

---

## 10. Subtype Hardy–Littlewood Asymptotics

For each admissible subtype $r\in S_W(k)$, define

$$
\pi_r(X)
=
\#\{\, p\le X : p\equiv r\pmod W,\ p\text{ and }p+k\text{ prime}\,\}.
$$

The precise subtype asymptotic statement is:

$$
\pi_r(X)
\sim
\frac{1}{|S_W(k)|}\,C_k\,\operatorname{Li}_2(X),
\qquad X\to\infty.
$$

For the twin-prime case at $W=30$,

$$
\pi_r(X)
\sim
\frac{C_2}{3}\frac{X}{\ln^2 X},
\qquad
r\in\{11,17,29\}.
$$

### 10.1 What is structural
The subtype partition and equal-split factor
$$
\frac{1}{|S_W(k)|}
$$
are structurally correct.

### 10.2 What is still classical-hard
The asymptotic rate still depends on the underlying prime-pair existence problem. So this branch ultimately inherits the difficulty of the twin-prime / Polignac frontier.

### 10.3 Closure state

$$
\boxed{
\text{MECHANIZED: precise subtype HL statement}
}
$$

$$
\boxed{
\text{OPEN: proof of infinitude and full asymptotic rate.}
}
$$

---

## 11. Retired Claims

The following are no longer active truth claims in the canonical ledger:

1. pooled raw inter-arrival definitions of $M$,
2. max-class deviation as the definition of $\pi_{30}$,
3. Poisson as the base renewal law,
4. Hawkes / excitatory clustering as the explanation of the deficit,
5. shared finite-$X$ kernel for all observed corrections,
6. strong persistent T0A/T0B directional bias,
7. the claim that the old single-NB $k=30$ shell correctly captures the tail.

These are retired and should not be carried forward into canonical statements.

---

## 12. Canonical State Map

The full branch now compresses to:

$$
\boxed{
\text{algebra locked}
}
$$

$$
\boxed{
\text{variables locked}
}
$$

$$
\boxed{
\text{$k=2$ shell corrected}
}
$$

$$
\boxed{
\text{spike signs positive}
}
$$

$$
\boxed{
\text{$\pi_{30}$ numerically locked, mechanism identified}
}
$$

$$
\boxed{
\text{body correction mechanism identified}
}
$$

$$
\boxed{
\text{$k=30$ body/tail shell fitted}
}
$$

$$
\boxed{
\text{subtype HL stated precisely}
}
$$

$$
\boxed{
\text{deep number theory still open}
}
$$

---

## 13. Remaining Open Problems

The remaining frontier is now short and precise.

### Open Problem 1 — Exact $A$ coefficient
Prove or compute

$$
A=0.104115
$$

in the expansion

$$
\pi_{30}(X)
=
\frac13+\frac{a}{\ln X}+\frac{b}{\ln^2 X}+O\!\left(\frac{1}{\ln^3 X}\right),
\qquad a=-A.
$$

### Open Problem 2 — Derive $\gamma$ from the $W'=210$ lift
Compute the body correction from the explicit wheel extension:

$$
W=30 \to W'=210.
$$

### Open Problem 3 — Analytic origin of the $k=30$ threshold
Explain the onset threshold $T$ in the two-regime shell from first principles.

### Open Problem 4 — Infinitude of each subtype family
For every admissible $r\in S_W(k)$, prove

$$
\pi_r(X)\to\infty
\qquad \text{as } X\to\infty.
$$

This is the deepest unresolved branch.

---

## 14. Final Closure Statement

The canonical closure of the NEXUS prime-gap branch is therefore:

$$
\boxed{
\text{The algebraic scaffold is complete.}
}
$$

$$
\boxed{
\text{The empirical twin-prime shell is coherent.}
}
$$

$$
\boxed{
\text{The main residual corrections now have identified mechanisms.}
}
$$

$$
\boxed{
\text{The remaining open problems are sharply posed analytic tasks, not conceptual confusion.}
}
$$

That is the present closure state.

---

## Appendix A. Core Equations

### A.1 Admissible subtype set
$$
S_W(k)=\{\,r\in U_W:r+k\in U_W\pmod W\,\}.
$$

### A.2 Family Lattice Theorem
$$
H\equiv r+\frac{k}{2}\pmod W.
$$

### A.3 Step Theorem
$$
\Delta H\equiv 0\pmod W.
$$

### A.4 Exact subtype count
$$
|S_W(k)|=
\prod_{\substack{q\mid W\\q>2\\q\nmid k}}(q-2)
\prod_{\substack{q\mid W\\q>2\\q\mid k}}(q-1).
$$

### A.5 Midpoint-gap variable
$$
M=\frac{\Delta H}{W}.
$$

### A.6 NB base kernel
$$
\operatorname{NB}(m;r,p)=
\binom{m+r-2}{m-1}(1-p)^{m-1}p^r.
$$

### A.7 Correct moments
$$
\mathbb{E}[M]=1+\frac{r(1-p)}{p},
\qquad
\operatorname{Var}(M)=\frac{r(1-p)}{p^2}.
$$

### A.8 Additive spike law
$$
f_{\text{spike}}(m)
=
1+\alpha_7\mathbf{1}_{7\mid m}
+\alpha_{11}\mathbf{1}_{11\mid m}
+\alpha_{13}\mathbf{1}_{13\mid m}.
$$

### A.9 Body term
$$
f_{\text{body}}(m)=1+\gamma\,\mathbf{1}_{6\le m\le 15}.
$$

### A.10 Full $k=2$ shell
$$
\mathbb{P}(M=m)
=
\frac{1}{Z}\operatorname{NB}(m;r,p)\,f_{\text{spike}}(m)\,f_{\text{body}}(m).
$$

### A.11 Spike enhancement ratio
$$
\text{Enhancement}(q)=\frac{q-2}{q-4},\qquad q>5.
$$

### A.12 Same-subtype adjacency statistic
$$
\pi_{30}(X)=\frac{1}{N-1}\sum_{j=1}^{N-1}\mathbf{1}_{r_j=r_{j+1}}.
$$

### A.13 Deficit law
$$
\frac13-\pi_{30}(X)
=
\frac{0.104115}{\ln X}
+
\frac{6.662432}{\ln^2 X}.
$$

### A.14 Competing-renewal formula
$$
\pi_\infty
=
\sum_{m=1}^{\infty}P(M=m)\,[P(R>m)]^2.
$$

### A.15 Forward recurrence law
$$
P(R=r)=\frac{P(M\ge r)}{\mathbb{E}[M]},\qquad r\ge 1.
$$

### A.16 Geometric approximation
$$
\pi_\infty^{\mathrm{geo}}(p)
=
\frac{p(1-p)^2}{1-(1-p)^3}.
$$

### A.17 Weighted HL transition formula
$$
\pi_{30}(X)
\approx
\frac{\displaystyle\sum_{\substack{g\le G(X)\\30\mid g}}S(g)\,\ln^{-2}(X/g)}
{\displaystyle\sum_{g\le G(X)}S(g)\,\ln^{-2}(X/g)}.
$$

### A.18 Two-regime $k=30$ shell
$$
\mathbb{P}(M=m)=
\begin{cases}
\dfrac{w_b \operatorname{NB}(m;r_b,p_b)}{\displaystyle\sum_{j=1}^{T}\operatorname{NB}(j;r_b,p_b)}, & 1\le m\le T,\\[10pt]
w_t\,p_t(1-p_t)^{m-T-1}, & m>T.
\end{cases}
$$

### A.19 Fitted two-regime parameters
$$
T=62,\quad r_b=0.480,\quad p_b=0.021,\quad p_t=0.056,\quad
w_b=0.972,\quad w_t=0.028.
$$

### A.20 Subtype HL asymptotic
$$
\pi_r(X)\sim \frac{1}{|S_W(k)|}C_k\operatorname{Li}_2(X).
$$

