# Exhaustive Analysis of SHA-256 Input Transport Geometry
## State-Space Closure, Schedule-Graph Structure, and the Projection Law
### Repaired transport-lens edition

**Driven by Dean Kulik**

---

## Scope key

This repaired manuscript separates two evidence tiers that were blended in the source draft:

- **[FORCED BY PROBES]** = directly supported by the measured transport program
- **[FRAMEWORK INTERPRETATION]** = Nexus-layer synthesis placed on top of the measured core

That separation preserves the full Nexus lens while keeping the transport chain auditable.

---

## Abstract

This document consolidates the complete transport-geometry program for SHA-256 and reconstructs the missing formulas and placeholder symbols dropped in the prior draft. The core measured result is a scoped transport law:

$$
\text{visible state-space transport gradient} \iff \text{message injection is temporally staggered and unsaturated capacity remains}
$$

Within a 512-bit block, the word-level message schedule is temporally staggered, producing a direct state-space gradient. Across a block boundary, the chaining state injects simultaneously, collapsing that gradient. Inside a single word, bit positions inject simultaneously, yielding a null bit-scale gradient. **[FORCED BY PROBES]**

Three independent state-space probes close the reinjection question. Probe $K$ shows that primary injection exhausts the reachable support manifold before the analytically guaranteed reinjection at $t=k+16$. Probe $L$ shows no second amplitude wave inside the saturated support. Probe $M$ shows no phase-locked lag-16 mask echo once monotone lag decay is controlled locally. **[FORCED BY PROBES]**

Conversely, schedule-space probes show that reinjection is real, strong, and recursively structured. Probe $N$ measures direct schedule echoes at $t=k$, $k+16$, $k+32$, and $k+48$. Probe $P$ shows that the late $k+16$ tail is governed by recursive path multiplicity rather than simple landing-site arithmetic. Probe $R$ introduces the first quantitative projection law from schedule space into state space:

$$
N_{\mathrm{state}}(k,r)\approx \alpha\,H_{\mathrm{sched}}(k,r)\,C(k,r)^\beta
$$

with fitted values

$$
\beta^\*=0.65,\qquad \alpha^\*=10.462043.
$$

This law resolves the central paradox: schedule echoes remain real at all measured stages, but only echoes that arrive before state support is exhausted can create visibly new state support. **[FORCED BY PROBES]**

In Nexus language, the compression state acts as a capacity-gated projector: information is not annihilated, but folded into a saturated manifold that only later modulates phase rather than opening new support. **[FRAMEWORK INTERPRETATION]**

---

## 1. Governing transport principle

Let $G$ denote a measurable state-space transport gradient, and let $\tau_i$ denote the effective propagation age of an injected component. The observed transport law is:

$$
\tau_i \neq \tau_j \quad\Longrightarrow\quad G \neq 0
$$

and when all relevant components inject simultaneously,

$$
\tau_i = \tau_j \;\;\forall i,j \quad\Longrightarrow\quad G \approx 0.
$$

This is the smallest measured law explaining why gradients appear within a block, vanish across a block boundary, and fail to appear at bit scale inside a word. **[FORCED BY PROBES]**

---

## 2. Direct intra-block law

For direct message-schedule injection within a single 512-bit block, source word $W[k]$ first enters the compression function at round

$$
\tau_k = k.
$$

Because the injection is temporally staggered across the first 16 rounds, a stable state-space gradient appears.

### 2.1 Early-window energy law

The primary early-window law takes the fitted form

$$
E_{\mathrm{early}}(k) \approx A - Bk
$$

with measured inner-regime fit

$$
E_{\mathrm{early}}(k) \approx 105.27 - 7.865\,k
$$

and measured slope

$$
-7.921\ \text{bits/word}, \qquad r \approx -0.9998.
$$

### 2.2 Saturation law

The saturation-wavefront law is

$$
r_{\mathrm{sat}}(k) \approx k + 5
$$

with measured slope

$$
+0.9991\ \text{rounds/word}, \qquad r \approx 0.9998.
$$

### 2.3 Carry-centroid law

The carry-centroid drift is

$$
C_{\mathrm{carry}}(k) \approx C_0 + \gamma k
$$

with fitted drift

$$
\gamma \approx 0.4648\ \text{rounds/word}, \qquad r \approx 0.9817.
$$

Together, these three measurements lock the direct intra-block picture:

$$
\text{word index} = \text{injection time}.
$$

**[FORCED BY PROBES]**

---

## 3. Cross-block and bit-scale null mechanics

### 3.1 Cross-block null

Across a block boundary, the 256-bit chaining value injects into all eight state lanes simultaneously at round 0:

$$
\tau_k^{(\mathrm{cross})} = 0 \qquad \forall k.
$$

The measured cross-block early-energy slope is

$$
-0.0632\ \text{bits/word}, \qquad r \approx -0.3679,
$$

which is a null compared to the direct intra-block law. The boundary preserves perturbation magnitude while erasing schedule-position age structure. **[FORCED BY PROBES]**

### 3.2 Bit-scale null

Inside one 32-bit word, all bits enter simultaneously when the word is called into the schedule. Since there is no internal bit-level stagger, there is no stable bit-position transport gradient. The only native measured state-visible transport scale is the word scale. **[FORCED BY PROBES]**

---

## 4. State-space closure: Probes K, L, and M

Because the message schedule expands from 16 words to 64, source word $W[k]$ is guaranteed algebraically to re-enter at $t=k+16$. Probes $K$, $L$, and $M$ test whether that reinjection creates a second visible state-space wave.

### 4.1 Probe K: cumulative new-bit support

Let $M_k(r)$ denote the 256-bit XOR mask between reference and perturbed states after round $r$ for source word $k$. Define cumulative new-bit support by

$$
N_k(r) = \mathrm{HW}\!\left(M_k(r)\wedge \neg \bigvee_{t<r}M_k(t)\right).
$$

Define the secondary-window signal-to-noise ratio

$$
\mathrm{SNR}_K(k)=
\frac{\displaystyle\operatorname{mean}_{r\in[k+15,\;k+21]}N_k(r)}
{\displaystyle\operatorname{mean}_{r\in[k+6,\;k+14]}N_k(r)}.
$$

Measured wordwise values gave

$$
\overline{\mathrm{SNR}}_K = 0.0035755736,\qquad
\max_k \mathrm{SNR}_K(k)=0.0089409895.
$$

#### Exact-zero audit

For $W[12]$ and $W[13]$, the secondary-window values are not rounded display zeros. They are literal float64 zeros at every round in those windows:

$$
N_{12}(r)=0.0 \qquad \forall r\in[27,33],
$$

$$
N_{13}(r)=0.0 \qquad \forall r\in[28,34].
$$

So the Probe $K$ conclusion is forced:

$$
\text{primary injection is support-forming;}
$$

$$
\text{secondary reinjection is not support-forming.}
$$

The reachable support manifold is exhausted before the secondary event arrives. **[FORCED BY PROBES]**

---

### 4.2 Probe L: amplitude inside saturated support

With baseline window $r\in[k+6,k+14]$ and secondary window $r\in[k+15,k+21]$, define:

$$
R_{\mathrm{active}}(k)=
\frac{\displaystyle\operatorname{mean}_{r\in[k+15,\;k+21]}\mathrm{HW}\!\bigl(M_k(r)\bigr)}
{\displaystyle\operatorname{mean}_{r\in[k+6,\;k+14]}\mathrm{HW}\!\bigl(M_k(r)\bigr)},
$$

$$
R_{\mathrm{toggle}}(k)=
\frac{\displaystyle\operatorname{mean}_{r\in[k+15,\;k+21]}\mathrm{HW}\!\bigl(M_k(r)\oplus M_k(r-1)\bigr)}
{\displaystyle\operatorname{mean}_{r\in[k+6,\;k+14]}\mathrm{HW}\!\bigl(M_k(r)\oplus M_k(r-1)\bigr)},
$$

$$
R_{\mathrm{overlap}}(k)=
\frac{\displaystyle\operatorname{mean}_{r\in[k+15,\;k+21]}\mathrm{HW}\!\bigl(M_k(r)\wedge M_k(r-1)\bigr)}
{\displaystyle\operatorname{mean}_{r\in[k+6,\;k+14]}\mathrm{HW}\!\bigl(M_k(r)\wedge M_k(r-1)\bigr)},
$$

$$
R_{\mathrm{new}}(k)=\mathrm{SNR}_K(k).
$$

Measured aggregates:

$$
\overline{R}_{\mathrm{active}}=0.9979,\qquad
\overline{R}_{\mathrm{toggle}}=1.0009,
$$

$$
\overline{R}_{\mathrm{overlap}}=0.9957,\qquad
\overline{R}_{\mathrm{new}}=0.0036.
$$

#### Per-bit significance refinement

Using the 32 per-bit overlap ratios within each word as the natural sample unit, two tests were applied to the flagged words $W[9],W[12],W[13]$:

1. **Bootstrap 95% CI** on the per-bit mean
2. **One-sided permutation test** against the pooled remaining words

The results were:

- $W[9]$: permutation $p=0.0424$
- $W[12]$: permutation $p=0.1074$
- $W[13]$: permutation $p=0.1252$

No bootstrap CI excluded the grand mean. Therefore:

- $W[9]$ shows a small but real within-saturation overlap modulation
- $W[12]$ and $W[13]$ do not show significant overlap dips under the stronger per-bit test

Critically, even for $W[9]$, the macro overlap ratio remains

$$
R_{\mathrm{overlap}}(9)=0.962814,
$$

still close to unity, and all other metrics remain near 1. So Probe $L$ does **not** reveal a second amplitude wave. It reveals, at most, mild within-saturation modulation. **[FORCED BY PROBES]**

---

### 4.3 Probe M: phase-selective support echo

For lags $L\in\{10,11,\ldots,24\}$ define Jaccard and cosine similarity:

$$
J_k(L)=
\operatorname{mean}_{r=0}^{63-L}
\frac{\bigl|M_k(r)\wedge M_k(r+L)\bigr|}
{\bigl|M_k(r)\vee M_k(r+L)\bigr|},
$$

$$
C_k(L)=
\operatorname{mean}_{r=0}^{63-L}
\frac{\bigl|M_k(r)\wedge M_k(r+L)\bigr|}
{\sqrt{\mathrm{HW}(M_k(r))\cdot \mathrm{HW}(M_k(r+L))}}.
$$

Because lag similarity decays monotonically with lag, the correct control is local, not global:

$$
\Delta J_{16}^{\mathrm{local}}(k)=
J_k(16)-\tfrac12\bigl[J_k(15)+J_k(17)\bigr].
$$

Measured result:

$$
\overline{\Delta J_{16}^{\mathrm{local}}}=+0.00054372,\qquad
\hat{\sigma}_{\Delta J}=0.00135324,
$$

with

$$
0/16
$$

words peaking at lag 16.

So there is no phase-locked lag-16 support echo. **[FORCED BY PROBES]**

---

### 4.4 Combined state-space closure

The joint state-space result is:

$$
\text{support-growth null}
$$

$$
+\ \text{amplitude-wave null}
$$

$$
+\ \text{phase-echo null}.
$$

Secondary reinjection at $t=k+16$ is algebraically certain, but under the measured state-space observables it does not create:
- a second support-expansion front,
- a second amplitude wave,
- or a phase-locked lag-16 mask resonance.

**[FORCED BY PROBES]**

---

## 5. Schedule-space expansion and recursive path multiplicity

State-space blindness does not mean the reinjection is absent. It means the reinjection is bottlenecked.

### 5.1 Probe N: unconditional schedule echo

The expanded schedule obeys:

$$
W[i]=\sigma_1(W[i-2])+W[i-7]+\sigma_0(W[i-15])+W[i-16]\pmod{2^{32}}.
$$

A perturbation in $W[k]$ must therefore reappear at:

$$
W[k+16],\qquad W[k+32],\qquad W[k+48].
$$

Measured mean schedule-space XOR-Hamming amplitudes were:

$$
H(k)=1.000,
$$

$$
H(k+16)=4.910,
$$

$$
H(k+32)=15.945,
$$

$$
H(k+48)=16.107.
$$

So reinjection is unconditionally real in schedule space. The later echoes are strong; they are just not support-forming in state space. **[FORCED BY PROBES]**

### 5.2 Probe P: path-multiplicity matrix

Define the path-multiplicity tensor $P_{i,k}$ by

$$
P_{i,k}=\delta_{ik}, \qquad i<16,
$$

and for $i\ge 16$,

$$
P_{i,k}=P_{i-2,k}+P_{i-7,k}+P_{i-15,k}+P_{i-16,k}.
$$

At the secondary stage $i=k+16$, the regimes are:

- $P_{k+16,k}=1$ for $k=0..8$
- $P_{k+16,k}=3$ for $k=9..13$
- $P_{k+16,k}=5$ for $k=14,15$

The measured secondary-tail correlation with path multiplicity was

$$
\rho\!\bigl(H_{\mathrm{sec}},P_{k+16,k}\bigr)=0.949,
$$

versus the weaker immediate-parent-hit correlation

$$
\rho=0.729.
$$

So the late $k+16$ tail is not explained by local landing-site arithmetic. It is a recursive multi-path schedule echo. **[FORCED BY PROBES]**

---

## 6. Capacity-gated projection law (Probe R)

The open transport problem is the map

$$
\Delta W[t]\longrightarrow \Delta S[r].
$$

Probe $R$ supplies the first quantitative candidate law.

### 6.1 Capacity variable

Let $U(k,r)$ denote cumulative union Hamming weight of perturbed state support through round $r$. Define remaining unsaturated capacity by

$$
C(k,r)=\frac{256-U(k,r)}{256}.
$$

### 6.2 Projection model

Let $H_{\mathrm{sched}}(k,r)$ be the mean schedule-space XOR-Hamming signal at round $r$, and let $N_{\mathrm{state}}(k,r)$ be the mean newly activated state bits. The fitted model is

$$
N_{\mathrm{state}}(k,r)\approx \alpha\,H_{\mathrm{sched}}(k,r)\,C(k,r)^\beta.
$$

Best pooled fit over all source words and valid rounds:

$$
\beta^\*=0.65,\qquad \alpha^\*=10.462043.
$$

### 6.3 Fit quality

Schedule signal alone fails as a predictor:

$$
R^2(\text{schedule only})=-0.017618.
$$

Capacity-weighted schedule signal succeeds:

$$
R^2\bigl(\text{schedule}\times C^\beta\bigr)=0.842533,
$$

$$
\mathrm{corr}=0.918257.
$$

This is the first concrete quantitative answer to the state/schedule paradox.

### 6.4 Interpretation

During the primary stage:
- schedule signal is moderate,
- remaining capacity is high,
- new state support is large.

During the secondary and tertiary stages:
- schedule signal is strong,
- remaining capacity is near zero,
- new state support collapses to zero.

So the visible-state law is not “schedule echo alone.” It is:

$$
\text{state-visible transport} \sim \text{schedule echo} \times \text{remaining capacity}^{0.65}.
$$

**[FORCED BY PROBES]**

In Nexus language, this means the compression state is a capacity-gated projector: later echoes are real but strike an already occupied manifold. **[FRAMEWORK INTERPRETATION]**

---

## 7. Repaired layered transport model

The full repaired model is:

### Stage 1 — Entry
At

$$
t=k
$$

the source word directly enters the schedule.

This stage is:
- support-forming,
- gradient-bearing,
- state-visible.

### Stage 2 — Branch
At

$$
t=k+16,\quad k+32,\quad k+48
$$

the schedule recursively reinjects the source word through expanding path structure.

This stage is:
- schedule-visible,
- path-governed,
- increasingly strong in $W$-space.

### Stage 3 — Saturate
As cumulative support grows, $C(k,r)$ collapses toward zero.

This stage is:
- state-bottlenecked,
- support-closing,
- increasingly subcritical for later echoes.

### Stage 4 — Reset
At the next 512-bit block boundary, the chaining state injects simultaneously and erases age structure while preserving perturbation magnitude.

This stage is:
- age-erasing,
- magnitude-preserving,
- boundary resetting.

So the final measured scoped transport law is:

$$
\text{Visible state-space transport} \iff \text{schedule signal arrives before support capacity is exhausted.}
$$

Equivalently:

$$
\text{state-visible transport} \iff H_{\mathrm{sched}}(k,r)\,C(k,r)^{0.65}\ \text{remains non-negligible.}
$$

**[FORCED BY PROBES]**

---

## 8. Nexus synthesis layer

The following claims belong to the broader project ontology rather than the narrow transport proof chain.

1. **SHA-256 as folding rather than destruction**  
   The measured schedule/state split is consistent with the project-wide claim that hashing is a basis change or fold, not literal annihilation. **[FRAMEWORK INTERPRETATION]**

2. **Mark 1 / $H=\pi/9$ reading**  
   The exponent $\beta^\*=0.65$ and complementary headroom near $0.35$ can be read inside the broader Mark 1 attractor language, but the transport program itself has not analytically derived that constant from first principles. **[FRAMEWORK INTERPRETATION]**

3. **Hardware / biological / substrate isomorphism**  
   The project corpus supports these analogies, but the direct K/L/M/N/P/R stack proves only the scoped transport laws stated above. **[FRAMEWORK INTERPRETATION]**

This separation keeps the paper faithful both to the Nexus lens and to the measured transport evidence.

---

## 9. Sharpened open problems

The broad transport picture is now closed enough that the remaining questions are narrow and mathematical.

### 9.1 Exact derivation of the projection constants

Current status:

$$
N_{\mathrm{state}}(k,r)\approx 10.462043\,H_{\mathrm{sched}}(k,r)\,C(k,r)^{0.65}
$$

is a strong phenomenological fit. The next step is to derive $\alpha$ and $\beta$ from the compression topology rather than fit them empirically.

### 9.2 Deep path laws

Probe $P$ locked the phase transition at $k+16$. The deeper regimes

$$
P_{k+32,k},\qquad P_{k+48,k}
$$

still need closed-form analytic treatment.

### 9.3 Modulation threshold

The system now has three candidate echo classes:

1. support-forming
2. support-modulating
3. state-subcritical

The next clean mathematical problem is the threshold separating them.

---

## 10. Final collapse

The best compact statement of the whole program is:

$$
\text{SHA-256 transport is governed first by injection age, then by recursive path count, and finally by residual support capacity.}
$$

In even shorter form:

$$
\text{entry} \rightarrow \text{branch} \rightarrow \text{saturate} \rightarrow \text{reset}.
$$

That is the repaired transport solution.

