# NEXUS Prime-Gap Program
## Integrated Full Writeup of the Current State

**Dean A. Kulik**  
**QuHarmonics Research Group**  
**A-Mark9 / NEXUS Phase 1163+**

---

## Abstract

This document is a full integrated writeup of the current NEXUS prime-gap program as it stands after the corrective work through Phase 10. It separates the project into four layers:

1. the **theorem-grade algebraic core**,  
2. the **correctly defined empirical renewal shell**,  
3. the **retired or corrected interpretations**,  
4. the **remaining open analytic frontier**.

The main outcome is clarity. The project is no longer a pile of partially overlapping claims. The current state is structurally simple:

- the **Primorial Family Lattice Theorem** is the locked core,
- the **$k=2$ renewal shell** is the best-resolved empirical branch,
- the **spike signs** are analytically positive,
- the **$\pi_{30}(X)$ law** is numerically stable,
- the **$k=30$ shell** is reproducible but not yet tail-faithful,
- the deep frontier remains classical: subtype asymptotics and infinitude.

This document is designed to be self-contained, separating what is proved, what is fitted, what was retired, and what is still open.

---

## 1. Orientation

The prime-gap branch of the NEXUS program evolved through multiple phases, and several of those phases used partially misaligned variables or over-strong interpretations. The later corrective work showed that the confusion was not in the algebraic kernel itself. The confusion came from mixing together:

- theorem,
- empirical fit,
- diagnostic statistic,
- and interpretation.

The correct current method is to keep those layers separate.

The full state of the branch now breaks naturally into:

$$
\text{theorem core}
\;\to\;
\text{empirical renewal shell}
\;\to\;
\text{finite-}X\text{ corrections}
\;\to\;
\text{analytic frontier}.
$$

That is the organizing principle of this writeup.

---

## 2. The Theorem-Grade Kernel

### 2.1 Primorial wheel and admissible subtypes

Let $W$ be a primorial wheel and let

$$
U_W = (\mathbb{Z}/W\mathbb{Z})^\times
$$

denote the reduced residue system modulo $W$.

For an even prime gap $k$, define the admissible subtype set

$$
S_W(k) = \{\, r \in U_W : r+k \in U_W \pmod W \,\}.
$$

A prime pair $(p,p+k)$ belongs to subtype $r$ when

$$
p \equiv r \pmod W.
$$

Define the midpoint center

$$
H = p + \frac{k}{2}.
$$

Then the basic structural law is immediate.

### 2.2 Family Lattice Theorem

For every admissible subtype $r$,

$$
H \equiv r + \frac{k}{2} \pmod W.
$$

This means that within each subtype, midpoint centers live on a fixed residue class modulo the wheel.

### 2.3 Step Theorem

If

$$
H_1^{(r)} < H_2^{(r)} < H_3^{(r)} < \cdots
$$

are the midpoint centers in one fixed subtype $r$, then consecutive centers satisfy

$$
\Delta H_n^{(r)} = H_{n+1}^{(r)} - H_n^{(r)} \equiv 0 \pmod W.
$$

So within a subtype, midpoint differences are exact multiples of the wheel.

### 2.4 Exact subtype count

The exact number of admissible subtypes is

$$
|S_W(k)| =
\prod_{\substack{q\mid W\\ q>2\\ q\nmid k}} (q-2)
\prod_{\substack{q\mid W\\ q>2\\ q\mid k}} (q-1).
$$

This is the closed branch-count formula for the family lattice.

### 2.5 Status

These three facts are the theorem-grade floor:

$$
H \equiv r+\frac{k}{2}\pmod W,
\qquad
\Delta H \equiv 0\pmod W,
\qquad
|S_W(k)| \text{ by closed product law}.
$$

Everything else in the project depends on them. These have survived every later correction unchanged.

---

## 3. Correct Variable Definitions

The biggest cleanup in the later phases was not conceptual. It was definitional.

### 3.1 The correct renewal variable

The correct normalized midpoint-gap variable is

$$
M = \frac{\Delta H}{W},
$$

where $\Delta H$ is the difference between **consecutive midpoint centers within the same subtype**.

Equivalently,

$$
M_n^{(r)} = \frac{H_{n+1}^{(r)} - H_n^{(r)}}{W} \in \mathbb{N}_{>0}.
$$

This is forced by the Step Theorem, because the numerator is always divisible by $W$ inside a fixed subtype.

This variable is **not** the same thing as:

- pooled inter-arrival gaps across all subtypes,
- raw startpoint gaps divided by $W$,
- or gap-index spacings without subtype conditioning.

That distinction matters. Several earlier misreads came from silently swapping those objects.

### 3.2 Correct definition of $\pi_{30}(X)$

For the twin-prime family at $W=30$, the admissible subtype residues are

$$
\{11,17,29\}.
$$

If the residue labels of consecutive twin-prime pairs up to $X$ are

$$
r_1,r_2,\dots,r_N,
$$

then the correct same-subtype adjacency statistic is

$$
\pi_{30}(X)
=
\frac{1}{N-1}
\sum_{j=1}^{N-1}\mathbf{1}_{r_j=r_{j+1}}.
$$

This measures the fraction of **consecutive pairs** that share the same subtype.

It is not:

- the max-class deviation from $1/3$,
- the largest subtype fraction minus $1/3$,
- or any pooled class-imbalance measure.

Once this definition was restored, the later Phase 9 coefficients became internally consistent again.

### 3.3 Correct handling of $k=30$

For $k=30$, the same midpoint-gap construction must be used:

$$
M_{k=30} = \frac{\Delta H}{30}
$$

within fixed subtypes.

The earlier confusion came from using a different inter-arrival variable there, which made the shell look more exotic than it really was.

---

## 4. The $k=2$ Renewal Shell

The twin-prime family at $W=30$ is the best-resolved empirical branch.

### 4.1 Support and NB kernel

The corrected shell lives on the support

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

in the standard zero-based negative-binomial convention.

So the correct moments are

$$
\mathbb{E}[M] = 1 + \frac{r(1-p)}{p},
\qquad
\operatorname{Var}(M) = \frac{r(1-p)}{p^2}.
$$

Fixing this shift was one of the major corrections of the later phases.

### 4.2 Canonical spike law

The spike correction is additive:

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

This is now the canonical form. Earlier prose sometimes described a multiplicative spike law, but the corrected state of the program adopts the additive law consistently.

### 4.3 Body correction

The empirical body correction currently used is

$$
f_{\text{body}}(m)
=
1+\gamma\,\mathbf{1}_{6\le m\le 15}.
$$

This is best understood as a practical shell repair. It is not yet theorem-grade.

The data suggest that the strongest residual deficiency is concentrated especially in the low-mid body, near roughly $m\in[6,10]$, rather than uniformly across all of $[6,15]$. So the present body window is a good working shell, but not yet the final analytic object.

### 4.4 Full corrected $k=2$ shell

The active shell is

$$
\mathbb{P}(M=m)
=
\frac{1}{Z}
\operatorname{NB}(m;r,p)\,
f_{\text{spike}}(m)\,
f_{\text{body}}(m),
$$

with the fitted values

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

The interpretation is:

- the NB base captures the coarse renewal geometry,
- the spike terms capture primorial resonance beyond the wheel boundary,
- the body term repairs the local body mismatch.

This is the best empirical shell presently available for the $k=2$ family.

---

## 5. Spike Signs

This is the clearest analytic success of the later corrective work.

### 5.1 Singular-series comparison

Let $g$ be the gap between consecutive twin-prime startpoints, and let $q>5$ be prime.

In the generic case $q\nmid g$, the forbidden residue classes are

$$
\{0,2,g,g+2\}\pmod q,
$$

which are generically four distinct classes. The local factor is proportional to

$$
\frac{q-4}{q}.
$$

In the spike case $q\mid g$, the pairs $(0,g)$ and $(2,g+2)$ collapse modulo $q$, leaving only two occupied classes. The local factor becomes

$$
\frac{q-2}{q}.
$$

Therefore the enhancement ratio is

$$
\frac{(q-2)/q}{(q-4)/q}
=
\frac{q-2}{q-4}.
$$

Since

$$
\frac{q-2}{q-4} > 1
\qquad\text{for all }q>5,
$$

the spike signs must be positive.

### 5.2 Consequence

For the $k=2$ inter-arrival shell,

$$
\boxed{
\alpha_q > 0 \quad \text{for all relevant spike primes } q>5.
}
$$

This replaces the earlier sign-alternation story.

What remains open is not the sign, but the precise finite-$X$ size and ordering of the fitted $\alpha_q$ values.

---

## 6. Equal-Split and Subtype Symmetry

The asymptotic equal-split target for the three admissible $k=2$ subtypes at $W=30$ is

$$
R_\tau(X)\to 1
\qquad
(\tau\in\{11,17,29\}),
$$

where $R_\tau(X)$ is the subtype density normalized against perfect equal split.

The strongest current empirical reading is:

$$
\boxed{
\text{equal-split is numerically very strong at current tested scales.}
}
$$

This does not yet prove subtype Hardy–Littlewood asymptotics, but it strongly supports the symmetry picture.

### 6.1 T0A/T0B race

The earlier branch briefly treated T0A/T0B as though it might show a persistent directional bias. The corrected larger-scale reading no longer supports that stronger interpretation.

The correct current statement is:

$$
\boxed{
\text{No persistent directional bias is detected through the tested range.}
}
$$

The race shows finite-$X$ movement and temporary z-score peaks, but the best reading is oscillatory prime-race behavior rather than a permanently favored subtype.

So the strong-bias story has been retired.

---

## 7. The $\pi_{30}(X)$ Law

With the corrected statistic in hand, the same-subtype adjacency deficit is numerically stable.

Define the deficit

$$
D_{30}(X)=\frac{1}{3}-\pi_{30}(X).
$$

Then the fitted law is

$$
D_{30}(X)
=
\frac{A}{\ln X}
+
\frac{B}{\ln^2 X},
$$

with

$$
A=0.104115,
\qquad
B=6.662432.
$$

So the current law is

$$
\boxed{
\frac{1}{3}-\pi_{30}(X)
=
\frac{0.104115}{\ln X}
+
\frac{6.662432}{\ln^2 X}.
}
$$

### 7.1 What is settled

The following are currently settled numerically:

- the definition of the statistic,
- the sign of the deficit,
- the positive two-term structure,
- the agreement with the earlier large-$X$ phase outputs.

### 7.2 What remains open

The **analytic form** is plausible and well-supported:

$$
\pi_{30}(X)
=
\frac{1}{3}
+
\frac{a}{\ln X}
+
\frac{b}{\ln^2 X}
+
O\!\left(\frac{1}{\ln^3 X}\right).
$$

But the derivation of the specific coefficients

$$
a=-0.104115,\qquad b=-6.662432
$$

for the direct expansion, or equivalently the positive deficit coefficients above, is still open.

So this branch is in a strong hybrid state:

$$
\text{numerically locked}
\quad\text{but}\quad
\text{not yet analytically derived}.
$$

---

## 8. The $k=30$ Branch

The $k=30$ family is no longer interpreted the same way it was in the earlier phases.

### 8.1 Reproducible historical shell

Using the corrected midpoint-gap construction, the earlier NB fit is reproducible:

$$
r \approx 0.534,\qquad p \approx 0.0272.
$$

So the old shell was not a numerical hallucination. It is a real fit to the historical variable.

### 8.2 Mean-excess correction

Define the mean-excess function

$$
e(t)=\mathbb{E}[M-t\mid M>t].
$$

Empirically for $k=30$, the tail is approximately flat near

$$
e(t)\approx 23.3.
$$

That implies an effective geometric tail rate

$$
p_{\text{eff}}
\approx
\frac{1}{e(t)+1}
\approx
0.041\text{–}0.042.
$$

But the published NB fit uses $p\approx 0.0272$, which is significantly heavier-tailed.

### 8.3 Interpretation

So the correct reading is:

$$
\boxed{
\text{the old }k=30\text{ shell is reproducible, but it is not tail-faithful.}
}
$$

What the shell is likely doing is this:

- fitting the body reasonably,
- over-weighting the tail,
- and thereby compressing two regimes into one parameter pair.

That means the next model here should be either:

- a two-regime body/tail model, or
- a mixture model.

So the $k=30$ branch is not broken, but it is still incomplete.

---

## 9. Retired Claims

The branch is much cleaner once the retired stories are listed explicitly.

The following are no longer active truth claims:

1. pooled raw inter-arrival definitions of $M$ for the active shells,
2. max-class deviation as the definition of $\pi_{30}$,
3. Poisson as the renewal base,
4. Hawkes / excitatory clustering as the explanation of the subtype-adjacency deficit,
5. shared finite-$X$ kernel for $\pi_{30}$ and subtype equal-split,
6. strong persistent T0A/T0B directional bias,
7. the claim that the old $k=30$ NB shell correctly describes the tail.

These were all useful exploratory states, but they are not the current resolved view.

---

## 10. What Is Settled

The whole state of the project is best summarized by separating the closed layer from the open layer.

### 10.1 Closed or effectively settled
- Primorial Family Lattice Theorem,
- Step Theorem,
- exact subtype-count law,
- correct variable definitions,
- corrected $k=2$ shell architecture,
- positive spike-sign logic,
- numerical stability of the $\pi_{30}$ law,
- retirement of the older T0A/T0B bias claim.

### 10.2 Open but narrowed
- analytic derivation of the $\pi_{30}$ coefficients,
- analytic explanation of the body correction,
- final body/tail-aware $k=30$ shell,
- subtype Hardy–Littlewood asymptotics,
- infinitude of subtype families.

---

## 11. Current State Map

The cleanest possible state map is:

$$
\boxed{
\text{theorem core locked}
}
$$

$$
\boxed{
\text{$k=2$ empirical shell corrected}
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
\text{$k=30$ still needs a body/tail split model}
}
$$

$$
\boxed{
\text{deep number theory still open}
}
$$

That is what the project actually has so far.

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
\sum_{j=1}^{N-1}\mathbf{1}_{r_j=r_{j+1}}.
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

### A.15 Effective geometric tail rate
$$
p_{\text{eff}}\approx \frac{1}{e(t)+1}.
$$
