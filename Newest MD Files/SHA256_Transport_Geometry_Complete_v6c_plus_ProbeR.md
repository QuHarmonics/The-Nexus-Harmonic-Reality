# SHA-256 Input Transport Geometry  
## Complete Solution Through State-Space Closure, Schedule-Graph Structure, and Projection Law

**QuHarmonics Research Group — Dean Kulik — April 2026**

---

## Abstract

This document consolidates the SHA-256 transport-geometry program through the corrected state-space closure, the schedule-graph branching results, and the first quantitative projection law from schedule space into state space.

The central result is a scoped transport law:

$$
\text{visible state-space transport gradient} \iff \text{injection is temporally staggered and unsaturated capacity remains}
$$

Within a block, the word-level message schedule is temporally staggered, so a direct transport gradient appears. Across a block boundary, the chaining state injects simultaneously, so the gradient collapses. Inside a word, bit positions also inject simultaneously, so no bit-scale transport gradient appears.

At the state-space level, Probes $K$, $L$, and $M$ close the re-injection question for first-order observables. Probe $K$ shows that primary injection exhausts the reachable support manifold before the analytically guaranteed re-entry at $t=k+16$; the mean new-support SNR is

$$
\overline{\mathrm{SNR}}_K = 0.0035755736
$$

with exact float64 secondary-window zeros for $W[12]$ and $W[13]$. Probe $L$ shows no second amplitude wave inside the saturated support: active, toggle, and overlap ratios remain near unity, while the new-support ratio remains near zero. A per-bit permutation/bootstrap refinement finds a statistically real but weak overlap dip only for $W[9]$; it remains a within-saturation modulation effect rather than a second wave. Probe $M$ shows no phase-locked lag-16 support echo once the monotone-decay baseline is removed by a local adjacent-lag control.

At the schedule-space level, Probe $N$ changes basis and finds the opposite answer. The re-injection is directly visible in the expanded schedule, with mean direct-echo amplitudes

$$
H(k)=1.000,\qquad H(k+16)=4.910,\qquad H(k+32)=15.945,\qquad H(k+48)=16.107
$$

for the four analytically predicted echo positions. Probe $P$ explains the late $k+16$ tail structurally: the amplitude is governed by recursive path multiplicity in the schedule graph, not by local landing-site arithmetic.

Finally, Probe $R$ proposes the first quantitative projection law from schedule space into state space. The best pooled fit is

$$
N_{\mathrm{state}}(k,r)\approx \alpha\,H_{\mathrm{sched}}(k,r)\,C(k,r)^\beta
$$

with

$$
\beta^\*=0.65,\qquad \alpha^\*=10.462043
$$

where $C(k,r)$ is the remaining unsaturated support capacity. Schedule signal alone has no predictive value for new support, but the capacity-weighted model achieves

$$
R^2=0.842533,\qquad \mathrm{corr}=0.918257
$$

This identifies the state interface as a **capacity-gated projector**: schedule echoes remain real at all stages, but only those arriving before saturation can create visibly new state support.

---

## 1. Governing Principle

The smallest governing law supported by the full probe stack is:

$$
\text{visible transport gradient} \iff \text{different propagation age at injection}
$$

Equivalently, if relevant inputs enter at different effective times,

$$
\tau_i \neq \tau_j
\quad\Longrightarrow\quad
G \neq 0
$$

where $G$ denotes a measurable state-space transport gradient. If all relevant inputs enter simultaneously,

$$
\tau_i = \tau_j \;\;\forall i,j
\quad\Longrightarrow\quad
G \approx 0
$$

This law explains:

1. the direct intra-block word gradient,
2. the cross-block boundary reset,
3. the null bit-scale gradient inside a word,
4. the state-space invisibility of later schedule echoes after primary saturation.

The refined form after Probe $R$ is:

$$
\text{state-visible transport} \iff H_{\mathrm{sched}}(k,r)\,C(k,r)^\beta \text{ is non-negligible}
$$

So visibility requires both:
- a schedule-space signal,
- and unsaturated state-space capacity.

---

## 2. Direct Intra-Block Law

For direct message-schedule injection, source word $W[k]$ first enters the compression function at round

$$
\tau_k = k
$$

This gives the primary early-window law

$$
E_{\mathrm{early}}(k)\approx A-Bk
$$

with fitted inner-regime values

$$
E_{\mathrm{early}}(k)\approx 105.27-7.865\,k
$$

and measured inner slope

$$
-7.921\ \text{bits/word},\qquad r\approx -0.9998
$$

over $W[0..11]$.

The saturation law is

$$
r_{\mathrm{sat}}(k)\approx k+5
$$

with fitted slope

$$
+0.9991\ \text{rounds/word},\qquad r\approx 0.9998
$$

The direct carry-centroid law over all 16 words is

$$
C_{\mathrm{carry}}(k)\approx C_0+\gamma k
$$

with

$$
\gamma\approx 0.4648\ \text{rounds/word},\qquad r\approx 0.9817
$$

These three results establish the primary geometry:

$$
\text{word index} = \text{injection time}
$$

The boundary layer at $W[12..15]$ does not break this model; it marks the regime in which only 1–4 early rounds remain in the fixed measurement window.

---

## 3. Cross-Block Boundary Law

Across a block boundary, the chaining value injects into all eight state lanes simultaneously at round 0, so

$$
\tau_k^{(\mathrm{cross})}=0\qquad \forall k
$$

The measured cross-block early-energy slope is

$$
-0.0632\ \text{bits/word},\qquad r\approx -0.3679
$$

That is effectively a null gradient relative to the direct intra-block law. The boundary therefore preserves perturbation magnitude while erasing schedule-position age structure:

$$
\text{preserve magnitude, erase age}
$$

This is the boundary reset law.

---

## 4. Bit-Scale Null

Below the word scale, no systematic bit-position gradient was found. The direct state-space transport gradient is therefore a word-scale phenomenon only. Inside a word, all 32 bits enter compression simultaneously when the word enters, so no stable age gradient exists at bit scale.

This gives a clean hierarchy:

$$
\text{block boundary: simultaneous} \;\Rightarrow\; \text{no gradient}
$$

$$
\text{word entry: staggered} \;\Rightarrow\; \text{gradient}
$$

$$
\text{bit positions within a word: simultaneous} \;\Rightarrow\; \text{no gradient}
$$

---

## 5. State-Space Closure: Probes K, L, and M

Three independently defined observable classes test whether the analytically guaranteed re-entry at $t=k+16$ creates a second visible wave in state space.

### 5.1 Probe K — Cumulative New-Bit Support

Let $M_k(r)$ denote the 256-bit XOR mask between the reference and perturbed state after round $r$ for source word $k$. Define the cumulative new-bit count

$$
N_k(r)=\mathrm{HW}\!\left(M_k(r)\wedge \neg \bigvee_{t<r}M_k(t)\right)
$$

This counts bits that appear for the first time at round $r$.

Define the secondary-window signal-to-noise ratio by

$$
\mathrm{SNR}_K(k)=
\frac{\displaystyle \operatorname{mean}_{r\in[k+15,\;k+21]} N_k(r)}
     {\displaystyle \operatorname{mean}_{r\in[k+6,\;k+14]}  N_k(r)}
$$

Measured values include:

- mean SNR:

$$
\overline{\mathrm{SNR}}_K = 0.0035755736
$$

- maximum over all 16 words:

$$
\max_k \mathrm{SNR}_K(k)=0.0089409895
$$

The strongest refinement is the exact-zero audit. For $W[12]$ and $W[13]$:

$$
N_{12}(r)=0.0 \quad \forall r\in[27,33]
$$

$$
N_{13}(r)=0.0 \quad \forall r\in[28,34]
$$

These are literal float64 zeros, not display artifacts.

**Conclusion (FORCED):**

$$
\text{primary injection is support-forming}
$$

$$
\text{secondary re-injection is not support-forming}
$$

The reachable state-space support manifold is exhausted before the secondary event.

---

### 5.2 Probe L — Amplitude Inside Support

Even if no new support is created, the secondary event could still create a second amplitude wave inside already-active support.

Define the secondary/baseline ratios:

$$
R_{\mathrm{active}}(k)=
\frac{\displaystyle\operatorname{mean}_{r\in[k+15,\;k+21]}\mathrm{HW}\!\bigl(M_k(r)\bigr)}
     {\displaystyle\operatorname{mean}_{r\in[k+6,\;k+14]}\mathrm{HW}\!\bigl(M_k(r)\bigr)}
$$

$$
R_{\mathrm{toggle}}(k)=
\frac{\displaystyle\operatorname{mean}_{r\in[k+15,\;k+21]}\mathrm{HW}\!\bigl(M_k(r)\oplus M_k(r-1)\bigr)}
     {\displaystyle\operatorname{mean}_{r\in[k+6,\;k+14]}\mathrm{HW}\!\bigl(M_k(r)\oplus M_k(r-1)\bigr)}
$$

$$
R_{\mathrm{overlap}}(k)=
\frac{\displaystyle\operatorname{mean}_{r\in[k+15,\;k+21]}\mathrm{HW}\!\bigl(M_k(r)\wedge M_k(r-1)\bigr)}
     {\displaystyle\operatorname{mean}_{r\in[k+6,\;k+14]}\mathrm{HW}\!\bigl(M_k(r)\wedge M_k(r-1)\bigr)}
$$

$$
R_{\mathrm{new}}(k)=\mathrm{SNR}_K(k)
$$

Aggregate means are:

$$
\overline{R}_{\mathrm{active}}=0.9979,\qquad
\overline{R}_{\mathrm{toggle}}=1.0009,\qquad
\overline{R}_{\mathrm{overlap}}=0.9957,\qquad
\overline{R}_{\mathrm{new}}=0.0036
$$

A significance refinement was then applied at the **per-bit** level, using 32 per-bit overlap ratios per word, with:
- a bootstrap 95% CI on the per-bit mean,
- a one-sided permutation test against the pooled per-bit ratios from the remaining words.

Results:

- $W[9]$: permutation $p=0.042$
- $W[12]$: permutation $p=0.107$
- $W[13]$: permutation $p=0.125$

So only $W[9]$ shows a statistically distinguishable overlap dip, but the actual word-level overlap ratio remains near unity:

$$
R_{\mathrm{overlap}}(9)=0.962814
$$

and its other metrics remain within 1–2% of unity.

**Conclusion:**

There is no second amplitude wave. The $W[9]$ result is a real but weak **within-saturation modulation effect**, not a second transport wave.

---

### 5.3 Probe M — Phase-Selective Support Echo

The final state-space question is whether a phase-coherent lag-16 echo exists even when amplitude observables are flat.

Define lag-$L$ Jaccard and cosine similarity:

$$
J_k(L)=\operatorname{mean}_{r=0}^{63-L}
\frac{|M_k(r)\wedge M_k(r+L)|}{|M_k(r)\vee M_k(r+L)|}
$$

$$
C_k(L)=\operatorname{mean}_{r=0}^{63-L}
\frac{|M_k(r)\wedge M_k(r+L)|}
     {\sqrt{\mathrm{HW}(M_k(r))\,\mathrm{HW}(M_k(r+L))}}
$$

Because the lag profile is monotone-decreasing, the correct control is **local**, not global:

$$
\Delta J_{16}^{\mathrm{local}}(k)=
J_k(16)-\frac12\bigl[J_k(15)+J_k(17)\bigr]
$$

The measured mean local lag-16 Jaccard advantage is

$$
\overline{\Delta J_{16}^{\mathrm{local}}}=+0.00054372
$$

with standard deviation

$$
\hat{\sigma}_{\Delta J}=0.00135324
$$

and the number of words peaking at lag 16 is

$$
0/16
$$

**Conclusion (FORCED):**

No phase-locked support echo exists at lag 16.

---

### 5.4 Combined State-Space Closure

The three probes now close the state-space question:

1. **Support-growth null** (Probe $K$)
2. **Amplitude-wave null** (Probe $L$)
3. **Phase-echo null** (Probe $M$)

The joint conclusion is:

> Secondary re-injection at $t=k+16$ is algebraically certain in schedule space, but under the state-space observables defined here it produces no second support-expansion front, no second amplitude wave, and no phase-locked lag-16 support echo.

---

## 6. Schedule-Space Echo Scan (Probe N)

The state-space nulls do **not** imply the absence of a second injector. They imply that the current state interface cannot resolve it after primary saturation.

The schedule expansion is

$$
W[i]=\sigma_1(W[i-2])+W[i-7]+\sigma_0(W[i-15])+W[i-16]
\pmod{2^{32}}
$$

So a perturbation in $W[k]$ is analytically guaranteed to affect:

$$
W[k],\qquad W[k+16],\qquad W[k+32],\qquad W[k+48]
$$

Probe $N$ measures the XOR-Hamming distance between reference and perturbed schedules:

$$
H_k(t)=\mathrm{HW}\!\bigl(W_k^{(\mathrm{ref})}(t)\oplus W_k^{(\mathrm{pert})}(t)\bigr)
$$

The mean direct-echo amplitudes are:

$$
H(k)=1.000
$$

$$
H(k+16)=4.910
$$

$$
H(k+32)=15.945
$$

$$
H(k+48)=16.107
$$

So the reinjection is unconditionally real in schedule space.

**Conclusion:**

$$
\text{schedule-space positive result} \;\;\not\Rightarrow\;\; \text{state-space visibility}
$$

The bottleneck is the state interface, not the schedule.

---

## 7. Schedule-Graph Structure (Probe P)

Probe $N$ revealed the characteristic tail at $k+16$: weak for early words, stronger for middle words, strongest for late words. A local landing-site arithmetic explanation was tested and rejected.

The correct explanation is **recursive path multiplicity**.

Define the path-multiplicity matrix:

$$
P_{i,k}=\delta_{ik},\qquad i<16
$$

$$
P_{i,k}=P_{i-2,k}+P_{i-7,k}+P_{i-15,k}+P_{i-16,k},\qquad i\ge 16
$$

Thus $P_{i,k}$ counts the number of distinct syntactic dependency paths through which source word $W[k]$ reaches schedule word $W[i]$.

At the secondary stage, three regimes appear:

$$
P_{k+16,k}=1,\qquad k=0..8
$$

$$
P_{k+16,k}=3,\qquad k=9..13
$$

$$
P_{k+16,k}=5,\qquad k=14,15
$$

The correlation between measured secondary amplitude and path multiplicity is

$$
\rho\bigl(H_{\mathrm{sec}},P_{k+16,k}\bigr)=0.949
$$

compared with the weaker immediate-parent-hit count correlation

$$
\rho\bigl(H_{\mathrm{sec}},H_k\bigr)=0.729
$$

So the late $k+16$ tail is a **recursive multi-path schedule echo**, not a local arithmetic artifact.

---

## 8. Projection Law (Probe R)

The remaining open problem after v6c was the exact projection law:

$$
\Delta W[t]\longrightarrow \Delta S[r]
$$

Probe $R$ provides the first quantitative candidate.

### 8.1 Definitions

Let:

- $H_{\mathrm{sched}}(k,r)$ = mean schedule-space XOR-Hamming signal at round $r$ for source word $k$,
- $N_{\mathrm{state}}(k,r)$ = mean newly activated state bits at round $r$,
- $U(k,r)$ = cumulative union Hamming weight of the perturbed state support through round $r$.

Define remaining unsaturated capacity:

$$
C(k,r)=\frac{256-U(k,r)}{256}
$$

This is the fraction of the 256-bit state support that has **not yet** been activated.

### 8.2 Model family

Probe $R$ tests the model

$$
N_{\mathrm{state}}(k,r)\approx \alpha\,H_{\mathrm{sched}}(k,r)\,C(k,r)^\beta
$$

The best pooled fit over all source words and all rounds with nonzero schedule signal is:

$$
\beta^\*=0.65
$$

$$
\alpha^\*=10.462043
$$

The comparison to schedule signal alone is decisive:

$$
R^2(\text{schedule only})=-0.017618
$$

$$
R^2\bigl(\text{schedule}\times C^\beta\bigr)=0.842533
$$

with

$$
\mathrm{corr}=0.918257
$$

### 8.3 Interpretation

Schedule echo alone has essentially no predictive value for newly created state support. But once it is weighted by the remaining unsaturated capacity, it becomes a strong predictor.

This gives the first concrete projection law:

$$
\text{state-visible new support} \sim \text{schedule echo} \times \text{remaining capacity}^{0.65}
$$

This explains the hierarchy:

- **Primary stage**: moderate schedule signal, large capacity $\Rightarrow$ visible support growth
- **Secondary stage**: stronger schedule signal, near-zero capacity $\Rightarrow$ no new support
- **Tertiary/quaternary stages**: very strong schedule signal, still near-zero capacity $\Rightarrow$ still no new support

So the state interface acts as a **capacity-gated projector**.

---

## 9. Final Layered Model

The final transport model is:

### Stage 1 — Entry
At

$$
t=k
$$

the source word enters the schedule directly.

This stage is:
- temporally staggered,
- support-forming,
- state-visible.

### Stage 2 — Branch
At

$$
t=k+16,\;k+32,\;k+48
$$

the schedule recursively re-injects the source word along branching paths.

This stage is:
- schedule-visible,
- path-governed,
- increasingly strong in $W$-space.

### Stage 3 — Saturate
As the primary wave progresses, the cumulative support union $U(k,r)$ rises and the remaining capacity

$$
C(k,r)=\frac{256-U(k,r)}{256}
$$

falls toward zero.

This stage determines whether a schedule echo can remain support-forming in state space.

### Stage 4 — Reset
Across a block boundary, the chaining state injects simultaneously into all state lanes, erasing age structure while preserving perturbation magnitude.

---

## 10. Final Interpretation

The machine is not best described as “a generic diffusion engine.”

It is better described as:

$$
\text{entry} \rightarrow \text{branch} \rightarrow \text{saturate} \rightarrow \text{reset}
$$

or, more explicitly,

$$
\text{message schedule} = \text{temporally staggered injector + recursive branching field}
$$

$$
\text{compression state} = \text{capacity-gated saturating projector of that field}
$$

$$
\text{chaining boundary} = \text{temporal reset operator}
$$

This yields the final scoped law:

$$
\text{visible state-space transport} \iff
\text{schedule signal arrives before support capacity is exhausted}
$$

Equivalently,

$$
\text{state-visible transport} \iff
H_{\mathrm{sched}}(k,r)\,C(k,r)^\beta
\text{ remains non-negligible}
$$

with the current best fitted exponent

$$
\beta^\*=0.65
$$

This is the completed transport picture through Probe $R$.

---

## 11. What Remains Open

The remaining narrow problems are now sharply defined:

1. **Exact projection law refinement**  
   The current law is empirical:
   $$
   N_{\mathrm{state}}\approx \alpha\,H_{\mathrm{sched}}\,C^\beta
   $$
   The next step is to derive or justify this form from the compression topology rather than fitting it phenomenologically.

2. **Path law at deeper echoes**  
   Probe $P$ establishes path multiplicity at $k+16$. A full analytic law for
   $$
   P_{k+32,k},\qquad P_{k+48,k}
   $$
   should be matched against the stronger tertiary and quaternary schedule echoes.

3. **Support-modulating vs support-forming criterion**  
   We now know that later schedule echoes are real but usually state-subcritical. The remaining task is to sharpen the exact threshold separating:
   - support-forming echoes,
   - within-saturation modulation,
   - state-invisible echoes.

At this point, the framework is no longer open in a broad sense. The remaining work is narrow, local, and quantitative.
