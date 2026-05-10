# Phase 6 Corrected Closure Ledger
## Typed Prime Gap Families, Primorial Renewal Geometry, and Finite-$X$ Rendering Corrections

**Complete Solution Draft**  
**Driven by Dean A. Kulik**  
**April 2026**

---

## Abstract

This document consolidates the corrected Phase 6 state of the primorial prime-gap program. It separates theorem-grade structure from empirical structure, removes two false positives that arose from using the wrong null model, and identifies the exact remaining computational targets. The locked algebraic core remains unchanged: prime-pair families decompose exactly by primorial residue class, midpoint centers obey a fixed congruence law, and same-thread midpoint differences obey a strict step law. What changes in Phase 6 is the interpretation of several higher-order signals.

Two important corrections emerge. First, the apparent period-$2310$ signal at $X=5\text{M}$ is not an independent algebraic layer; it is explained by the correct geometric renewal baseline for $\Delta H/210$. Second, the deficit in the mixed-thread statistic $\pi_{30}(X)$ is not evidence of Hawkes-style excitatory clustering; it is consistent with a finite-$X$ logarithmic correction that decays toward the equal-rate limit. These corrections do not weaken the project. They sharpen it by removing structure that was only apparent under a mismatched rendering lens.

The principal Phase 6 conclusions are therefore:

$$
H \equiv r + \frac{k}{2} \pmod W,
\qquad
\Delta H \equiv 0 \pmod W
$$

remain theorem-grade;

$$
\text{Poisson base} \quad \text{is rejected},
$$

while a geometric or negative-binomial renewal base with primorial spike correction is the correct modeling direction; and

$$
Q(X) = Q_\infty - \frac{A}{\ln X} + O\!\left(\frac{1}{\ln^2 X}\right)
$$

now appears to be the right asymptotic template for multiple finite-$X$ observables on the mixed-thread field.

---

## 1. Foundations and Locked Structure

### 1.1 Primorial wheel setup

Let

$$
W = \prod_{q \le Q} q
$$

be a primorial wheel, where the product ranges over primes up to $Q$. Let

$$
U_W = (\mathbb Z / W\mathbb Z)^*
$$

be the reduced residue classes modulo $W$. For an even gap $k$, define the admissible subtype set

$$
S_W(k) = \{r \in U_W : r + k \in U_W \pmod W\}.
$$

A prime pair $(p,p+k)$ with $p > \max\{q : q \mid W\}$ belongs to subtype $r$ when

$$
p \equiv r \pmod W.
$$

Define the midpoint center

$$
H = p + \frac{k}{2}.
$$

Then for every subtype $r \in S_W(k)$,

$$
H \equiv r + \frac{k}{2} \pmod W.
$$

This is the **Family Lattice Theorem**.

### 1.2 Step Theorem

If $p$ and $p'$ are two primes in the same subtype $r$, with midpoint centers

$$
H = p + \frac{k}{2},
\qquad
H' = p' + \frac{k}{2},
$$

then

$$
H \equiv H' \equiv r + \frac{k}{2} \pmod W,
$$

hence

$$
\Delta H = H' - H \equiv 0 \pmod W.
$$

So within any fixed subtype,

$$
\boxed{\Delta H \equiv 0 \pmod W.}
$$

This is the **Step Theorem**.

### 1.3 Exact subtype-count formula

For each odd prime $q \mid W$:

- if $q \nmid k$, then two residue classes are forbidden modulo $q$, namely $r \equiv 0$ and $r \equiv -k$;
- if $q \mid k$, then those two forbidden classes collapse into one.

Therefore the exact number of admissible subtypes is

$$
|S_W(k)|
=
\prod_{\substack{q \mid W \\ q>2 \\ q \nmid k}} (q-2)
\prod_{\substack{q \mid W \\ q>2 \\ q \mid k}} (q-1).
$$

This remains theorem-grade and unchanged by Phase 6.

### 1.4 Surface examples

For the low wheels used throughout the program:

$$
|S_6(2)| = 1,
\qquad
|S_{30}(2)| = 3,
\qquad
|S_{210}(2)| = 15,
\qquad
|S_{2310}(2)| = 135.
$$

For gaps divisible by more wheel factors, the subtype count increases accordingly. For example,

$$
|S_{30}(6)| = 6,
\qquad
|S_{30}(30)| = 8,
\qquad
|S_{210}(30)| = 40.
$$

These counts come directly from the product formula and do not require analytic number theory.

---

## 2. Stable Empirical Layer

The following claims remain empirically strong and are not overturned by Phase 6.

### 2.1 Equal-split tendency across subtypes

The per-subtype count appears to approach equal density within each admissible family. In the standard notation,

$$
\pi_{k,\tau}(X)
\sim
\frac{C_k}{|S_W(k)|} \cdot \frac{X}{(\ln X)^2},
$$

where $\tau$ indexes a subtype thread. This remains an empirical or conditional-analytic statement, not an unconditional theorem.

A useful finite-$X$ normalization is

$$
R_\tau(X)
=
\frac{n_\tau(X)}{n_{\text{total}}(X)/|S_W(k)|}.
$$

Equal-split means

$$
R_\tau(X) \to 1
\qquad \text{as } X \to \infty.
$$

### 2.2 T0A/T0B drift

The imbalance between the two $k \equiv 0 \pmod 6$ surface families still shows slow monotone drift. The current empirical scaling is

$$
z(X) \approx C \frac{\sqrt{X}}{\ln X}.
$$

This means:

- the effect is still present,
- the significance crossing has not yet occurred,
- and the original crossing estimate was too optimistic.

Phase 6 revises the expected significance-crossing scale upward to approximately

$$
X_* \approx 4.0 \times 10^7.
$$

This should be treated as a numerical forecast, not a theorem.

---

## 3. Phase 6 Corrections: What Was Overturned

Phase 6 removes two claims from the active solved stack.

### 3.1 No independent period-$2310$ signal at $X=5\text{M}$

The earlier claim arose from testing the distribution of

$$
M = \frac{\Delta H}{210}
$$

modulo $11$ against a uniform baseline. That null is incorrect because $M$ is not uniformly distributed on the positive integers; its tail is geometric-like.

If the correct null is geometric,

$$
\mathbb P(M=m) = p(1-p)^{m-1},
\qquad m \ge 1,
$$

then the expected residue-class probabilities modulo $11$ are not uniform. For a residue class $a \in \{1,2,\dots,11\}$, the correct baseline is

$$
\mathbb P(M \equiv a \pmod{11})
=
\sum_{j \ge 0} p(1-p)^{a-1+11j},
$$

with the obvious wrap convention for the class $0 \pmod{11}$.

Against this corrected geometric null, the conditional mod-$11$ test passes. Therefore:

$$
\boxed{
\text{No independent period-}2310\text{ algebraic layer is established at } X=5\text{M}.
}
$$

The earlier effect was a rendering artifact of the tail law.

### 3.2 No Hawkes-style excitatory clustering requirement

The earlier interpretation of the mixed-thread statistic

$$
\pi_{30}(X)
$$

was that a deficit below $1/3$ indicated self-exciting clustering of thread adjacency. Phase 6 overturns that reading.

The revised fit is

$$
\pi_{30}(X)
=
\frac{1}{3} - \frac{A_\pi}{\ln X} + O\!\left(\frac{1}{\ln^2 X}\right),
$$

with empirical coefficient approximately

$$
A_\pi \approx 0.43.
$$

Thus the deficit is now interpreted as a finite-$X$ convergence effect, not a structural excitation process.

So the corrected statement is

$$
\boxed{
\pi_{30}(X) < \frac13
\text{ at finite }X
\text{ because of slow logarithmic convergence, not Hawkes excitation.}
}
$$

---

## 4. Renewal Geometry: Corrected Model Class

### 4.1 Poisson base is rejected

The original proposal treated the spacing law as approximately Poisson with a primorial spike correction. Phase 6 rejects that base family.

Let $M = \Delta H / W$ denote the normalized same-thread gap variable. The Fano factor is

$$
F = \frac{\operatorname{Var}(M)}{\mathbb E[M]}.
$$

For Poisson, one must have

$$
F = 1.
$$

But empirically,

$$
F \gg 1,
$$

so the spacing process is strongly overdispersed and cannot be Poisson.

### 4.2 Primorial-corrected geometric (PCG) shell

The corrected working shell is a geometric-base renewal law with a primorial spike correction:

$$
\mathbb P(M=m)
\propto
p(1-p)^{m-1}\Bigl(1 + \alpha_7\,\mathbf 1_{7 \mid m}\Bigr),
\qquad m \ge 1.
$$

Equivalently, after normalization,

$$
\mathbb P(M=m)
=
\frac{1}{Z(p,\alpha_7)}
\, p(1-p)^{m-1}
\Bigl(1 + \alpha_7\,\mathbf 1_{7 \mid m}\Bigr),
$$

where

$$
Z(p,\alpha_7)
=
\sum_{m \ge 1} p(1-p)^{m-1}\Bigl(1 + \alpha_7\,\mathbf 1_{7 \mid m}\Bigr).
$$

Phase 6 finds an empirical spike amplitude around

$$
\alpha_7 \approx 0.46.
$$

This model improves the fit substantially, but it is still rejected by KS at current sample size. Therefore it should be treated as a corrected intermediate shell, not the final law.

### 4.3 Candidate next model: negative-binomial with primorial correction

The natural next extension is a negative-binomial base, which absorbs overdispersion while preserving discrete support. One useful parameterization is

$$
\operatorname{NB}(m; r,p)
=
\binom{m+r-2}{m-1} (1-p)^{m-1} p^r,
\qquad m \ge 1.
$$

Then the corrected primorial model becomes

$$
\mathbb P(M=m)
=
\frac{1}{Z(r,p,\alpha_7)}
\operatorname{NB}(m; r,p)
\Bigl(1 + \alpha_7\,\mathbf 1_{7 \mid m}\Bigr).
$$

This is the most natural next computational target because it preserves the primorial spike mechanism while replacing the memoryless base with a heavier discrete law.

### 4.4 Alternative candidate: finite geometric-hazard mixture

A second candidate is a finite mixture of geometric hazards:

$$
\mathbb P(M=m)
=
\sum_{j=1}^{J} w_j\, p_j (1-p_j)^{m-1},
$$

with

$$
\sum_{j=1}^{J} w_j = 1,
\qquad
w_j \ge 0.
$$

This allows multiple decay scales without committing to a single overdispersion parameter. It is flexible but less interpretable than the negative-binomial route.

---

## 5. Finite-$X$ Rendering Corrections

The major conceptual advance of Phase 6 is that several apparent structural deficits now look like finite-$X$ rendering effects of the same type.

### 5.1 Generic correction template

The conjectured universal template is

$$
Q(X)
=
Q_\infty - \frac{A}{\ln X} + \frac{B}{\ln^2 X} + o\!\left(\frac{1}{\ln^2 X}\right),
$$

where $Q(X)$ is an observable rendered from the mixed-thread field.

Candidate observables include:

$$
Q(X) \in \left\{
\pi_{30}(X),
\ R_\tau(X),
\ \text{T0A/T0B imbalance},
\ \text{other finite-}X\text{ subtype ratios}
\right\}.
$$

### 5.2 Mixed-thread statistic

For the mixed-thread same-thread adjacency statistic,

$$
\pi_{30}(X)
=
\frac13 - \frac{A_\pi}{\ln X} + O\!\left(\frac{1}{\ln^2 X}\right).
$$

The key change is interpretive: the deficit is no longer treated as a new structural law. It is treated as a slow approach to the equal-rate limit.

### 5.3 Equal-split ratio deficit

The same ansatz should be tested against subtype-density corrections:

$$
R_\tau(X)
=
1 - \frac{A_\tau}{\ln X} + O\!\left(\frac{1}{\ln^2 X}\right).
$$

If the same correction form governs both $\pi_{30}(X)$ and the subtype-density ratio deficits, then a significant amount of what looked like extra thread structure may be explained by one shared finite-$X$ kernel.

This is the most promising next analytic theorem on the empirical side of the program.

---

## 6. Clarifying the Observable Layer

Phase 6 makes one methodological point very clear: several earlier “signals” depended on using the wrong measurement lens.

That is, one must distinguish between:

- theorem-grade congruence structure,
- empirical renewal structure,
- and artifacts produced by testing against a null model that does not match the support or hazard of the observed variable.

In formal terms, a rendered observable is always a functional of the chosen measurement frame:

$$
Q = \mathcal M[\mathcal D; \mathcal N],
$$

where:

- $\mathcal D$ is the data stream,
- $\mathcal N$ is the null model,
- $\mathcal M$ is the measurement or test functional.

Changing $\mathcal N$ from uniform to geometric changed the interpretation of the mod-$11$ projection completely. So the correct statement is not “the period-$2310$ signal ceased to exist,” but rather:

$$
\boxed{
\text{Under the corrected null model, the Phase 5 period-}2310\text{ claim does not survive as an independent invariant.}
}
$$

That is a disciplined rendering correction.

---

## 7. Clean Closure Ledger

### 7.1 Proven structure

The following are theorem-grade:

1. **Family Lattice Theorem**
   $$
   H \equiv r + \frac{k}{2} \pmod W
   $$

2. **Step Theorem**
   $$
   \Delta H \equiv 0 \pmod W
   $$

3. **Exact subtype count**
   $$
   |S_W(k)|
   =
   \prod_{\substack{q \mid W \\ q>2 \\ q \nmid k}} (q-2)
   \prod_{\substack{q \mid W \\ q>2 \\ q \mid k}} (q-1)
   $$

### 7.2 Confirmed empirical structure

The following are strong numerical results but remain empirical or conditional:

1. **Equal-split tendency across admissible subtypes**
2. **Slow T0A/T0B drift**
3. **Primorial spike enhancement at the $7/210$ scale**
4. **Finite-$X$ logarithmic correction in mixed-thread observables**

### 7.3 Corrected or overturned claims

The following are removed from the active solved stack:

1. **Independent period-$2310$ algebraic signal at $X=5\text{M}$**
2. **Hawkes-style excitatory clustering as the explanation of the $\pi_{30}$ deficit**
3. **Poisson base as the correct renewal class**

### 7.4 Open problems

The open center is now much narrower.

#### OPEN-1: exact discrete renewal law

Find the correct distribution of

$$
M = \frac{\Delta H}{W}
$$

within a fixed subtype thread.

#### OPEN-2: analytic finite-$X$ correction law

Derive the coefficients in

$$
Q(X)
=
Q_\infty - \frac{A}{\ln X} + \frac{B}{\ln^2 X} + o\!\left(\frac{1}{\ln^2 X}\right).
$$

#### OPEN-3: per-subtype Hardy--Littlewood asymptotics

Make precise, conditionally or otherwise, the asymptotic equal-split law

$$
\pi_{k,\tau}(X)
\sim
\frac{C_k}{|S_W(k)|} \cdot \frac{X}{(\ln X)^2}.
$$

#### OPEN-4: infinitude of each subtype family

Show that every admissible subtype thread contains infinitely many prime pairs. This subsumes the deep bounded-gap / Polignac frontier and remains outside present reach.

---

## 8. Phase 7 Computational Targets

The next engine should attack only two fronts.

### P7-A: Negative-binomial primorial renewal fit

Fit

$$
\mathbb P(M=m)
=
\frac{1}{Z(r,p,\alpha_7)}
\operatorname{NB}(m; r,p)
\Bigl(1 + \alpha_7\,\mathbf 1_{7 \mid m}\Bigr)
$$

against the current geometric-base shell and compare KS, AIC, and residual spike structure.

### P7-B: Shared finite-$X$ correction kernel

Test whether the same logarithmic correction form

$$
Q(X)
=
Q_\infty - \frac{A}{\ln X} + \frac{B}{\ln^2 X}
$$

explains both:

$$
\pi_{30}(X)
\qquad \text{and} \qquad
R_\tau(X).
$$

If successful, this would replace multiple apparent anomalies with one clean analytic correction law.

---

## 9. Final Collapse

Phase 6 does not weaken the prime-gap program. It improves it by removing claims that depended on the wrong null model or the wrong stochastic family.

The corrected picture is:

$$
\boxed{
\text{The lattice law is exact, the renewal law is not yet closed, and several earlier anomalies are finite-}X\text{ rendering artifacts.}
}
$$

More sharply:

$$
\boxed{
\text{What remains is narrower, cleaner, and more mathematically real than the Phase 5 frontier map.}
}
$$

The next solve is no longer “find more surprising structure.” It is:

$$
\boxed{
\text{derive the exact discrete renewal law and the analytic finite-}X\text{ correction kernel.}
}
$$

