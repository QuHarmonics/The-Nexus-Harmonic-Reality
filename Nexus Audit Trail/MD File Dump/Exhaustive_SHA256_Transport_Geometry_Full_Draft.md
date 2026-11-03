# Exhaustive Analysis of SHA-256 Input Transport Geometry
## State-Space Closure, Schedule-Graph Structure, and the Capacity-Gated Projection Law

**Driven by Dean Kulik**  
**Drafted from the locked transport bench**

---

## Abstract

This paper consolidates the SHA-256 transport-geometry program into a single scoped result. The central finding is that a visible state-space transport gradient appears only when informational injection is temporally staggered and unsaturated support capacity remains available within the 256-bit compression state. Within a single 512-bit block, direct message-schedule injection satisfies this condition: source word $W[k]$ first enters the compression function at round $k$, generating a measurable intra-block transport law. Across a block boundary, the chaining state injects simultaneously, and the gradient collapses. Within a single word, bit positions likewise enter simultaneously, and no stable bit-scale transport gradient appears.

The state-space re-injection question is closed by three independent probes. Probe $K$ shows that the cumulative new-bit support rate in the secondary window collapses to near zero, with literal float64 zeros for $W[12]$ and $W[13]$. Probe $L$ shows that secondary activity inside the already-lit support manifold remains close to isometric modulation rather than a second amplitude wave, with only a small statistically real overlap dip at $W[9]$. Probe $M$ removes the remaining phase-echo hypothesis by applying a local adjacent-lag control to lag-16 support similarity and finding no systematic lag-16 peak. Together these results establish a state-space support-growth null, amplitude-wave null, and phase-echo null for the $k+16$ re-injection regime.

The apparent paradox is resolved by changing basis from state space to schedule space. Direct schedule probing shows that perturbations recur unconditionally at $k+16$, $k+32$, and $k+48$, with measured mean echo amplitudes
$$
H(k)=1.000,\qquad H(k+16)=4.910,\qquad H(k+32)=15.945,\qquad H(k+48)=16.107.
$$
The late secondary tail is not a local landing-site artifact; it is governed by recursive path multiplicity in the schedule graph. The translation from these strong schedule-space echoes to mostly null state-space effects is captured by the capacity-gated projection fit
$$
N_{\mathrm{state}}(k,r)\approx \alpha^\* H_{\mathrm{sched}}(k,r) C(k,r)^{\beta^\*},
$$
with
$$
\alpha^\*=10.462043,\qquad \beta^\*=0.65,
$$
and fitted performance
$$
R^2=0.842533,\qquad \mathrm{corr}=0.918257.
$$
The resulting picture is not generic diffusion, but a layered transport system governed by entry, branching, saturation, and reset.

---

## 1. Scope, Problem Statement, and Evidence Discipline

SHA-256 is ordinarily described as a one-way compression function whose internal mixing rapidly destroys accessible lineage between an input perturbation and later internal states. That description is operationally useful, but too coarse for the transport question addressed here. The problem is not whether SHA-256 exhibits diffusion in the broad cryptographic sense. The narrower problem is whether perturbations move through the compression process according to a measurable geometry, and if so, what conditions make that geometry visible or invisible inside the working state.

This paper answers that question with a scoped law rather than a metaphor. It does **not** claim that the transport bench alone proves general cryptographic inversion, nor does it claim that every broader Nexus interpretation is numerically forced by the probe stack. Instead, it separates the result into two layers:

1. **Transport-forced layer.** These are the claims directly compelled by the measured probe outputs.
2. **Framework-interpretive layer.** These are the broader Nexus readings that become available once the transport layer is established.

This separation is necessary. The measurement program is already strong enough to stand on its own. It should not be weakened by blurring empirical claims and interpretive extensions into one evidentiary class.

The governing transport result can be stated immediately:
$$
\text{visible state-space transport gradient} \iff \text{temporal stagger at injection and remaining unsaturated capacity}.
$$
Inside a block, source word $W[k]$ first enters the compression process at round $k$, so word index is injection time. That stagger generates the measured direct transport laws. Across a block boundary, all eight chaining-state lanes inject simultaneously at round $0$, so the age structure collapses. Within a single 32-bit word, the bit positions likewise share the same entry time, so no stable bit-scale gradient emerges. The direct state-space transport geometry is therefore not a generic property of “difference” alone. It is a property of difference under ordered entry.

That result raises the next question. The message schedule is recursive. A perturbation introduced in $W[k]$ is guaranteed by the schedule recurrence to reappear later, especially at $k+16$, and then again at deeper stages. Why, then, do these later echoes fail to produce a second visible wave in the compression state? The answer developed in this paper is that schedule-space reality and state-space visibility are not identical. The schedule behaves as a recursive branching field, while the compression state behaves as a capacity-limited projector. Later echoes are real, measurable, and strongly path-governed in schedule space, but they arrive after the primary wave has already exhausted most or all of the reachable support manifold in state space. The state does not deny the later echoes; it bottlenecks them.

The paper proceeds in that order. Sections 2–4 establish the direct intra-block transport law and the simultaneity nulls. Sections 5–7 close the $k+16$ state-space question through Probes $K$, $L$, and $M$. Sections 8–9 change basis into schedule space through Probes $N$ and $P$, showing that recursive echoes are unconditional and that the late secondary tail is governed by path multiplicity rather than simple landing arithmetic. Section 10 introduces the capacity-gated projection law, which provides the first quantitative bridge from schedule-space signal to state-space visibility. Only after that measured backbone is complete does Section 12 widen into the broader Nexus synthesis.

---

## 2. Architectural Frame: Schedule, State, and Boundary

Let the SHA-256 message schedule be denoted by $W[0],\dots,W[63]$, where the first 16 words are direct message words and the remaining 48 are recursively expanded. Let the compression state after round $r$ be
$$
S(r)=(a_r,b_r,c_r,d_r,e_r,f_r,g_r,h_r).
$$
For any single-bit perturbation of the source block, define the round-$r$ state difference mask
$$
M_k(r)=S_k^{\mathrm{pert}}(r)\oplus S^{\mathrm{ref}}(r),
$$
where $k$ indicates the perturbed source word and $\oplus$ is bitwise XOR.

Two spaces must be distinguished:

- **Schedule space.** This tracks how the message perturbation propagates through the expanded schedule.
- **State space.** This tracks how that schedule perturbation manifests in the eight-lane 256-bit compression state.

These spaces are coupled, but not identical. The schedule may carry a strong later echo even when the state shows no new support growth.

At the round-function level, the core update remains
$$
T_1[r]=h_r+\Sigma_1(e_r)+Ch(e_r,f_r,g_r)+K_r+W[r] \pmod{2^{32}},
$$
$$
T_2[r]=\Sigma_0(a_r)+Maj(a_r,b_r,c_r) \pmod{2^{32}},
$$
followed by the standard state-lane shift and overwrite. For the present paper, the details of the Boolean operators matter less than the timing structure induced by the schedule and the compression boundary.

The state interface is a finite 256-bit support manifold. Once a perturbation has activated most of the reachable support, later perturbations can still revisit, modulate, or rearrange active structure, but may fail to create genuinely new state support. This distinction between **support-forming** and **support-revisiting** injections is the axis on which the rest of the paper turns.

---

## 3. Governing Transport Principle

The fundamental law of transport is empirical but clean:
$$
\tau_i \neq \tau_j \Longrightarrow G \neq 0,
$$
$$
\tau_i=\tau_j\ \forall i,j \Longrightarrow G\approx 0.
$$
Here $\tau$ denotes effective propagation age at injection and $G$ denotes a measurable state-space transport gradient.

This law does not say that every temporal difference produces the same gradient. It says that visible gradient requires a timing asymmetry among the injected components. If the entries are synchronized, the state may still respond in magnitude, but the ordered geometry of transport collapses.

Within a block, the direct message-schedule law is
$$
\tau_k = k.
$$
Word index is injection time. The transport program shows that this ordered entry produces a stable gradient in several independent observables.

Across a block boundary, the chaining state injects simultaneously:
$$
\tau_k^{(\mathrm{cross})}=0 \qquad \forall k.
$$
The perturbation magnitude survives, but age structure does not.

Within a single 32-bit word, the bit positions all enter when the word enters. Therefore the bit scale does not inherit the staggered word-scale age coordinate. This is why the transport geometry is visible at the word scale but not at the bit scale.

The rest of the paper amounts to a refinement of this law. The direct wave is state-visible because it combines temporal stagger and available capacity. The later waves are schedule-real but mostly state-subcritical because they arrive after the primary wave has already consumed the support headroom.

---

## 4. Direct Intra-Block Law and Simultaneity Nulls

### 4.1 Direct intra-block transport

For the primary 16 message words within a single 512-bit block, the measured early-window law is
$$
E_{\mathrm{early}}(k)\approx 105.27-7.865k.
$$
The inner-regime fitted slope over $W[0..11]$ is approximately
$$
-7.921\ \text{bits/word},
$$
with correlation
$$
r\approx -0.9998.
$$
This is the first strong indicator that word entry time acts as a direct transport coordinate.

The saturation-wavefront law advances almost perfectly in lockstep with source word index:
$$
r_{\mathrm{sat}}(k)\approx k+5,
$$
with fitted slope
$$
+0.9991\ \text{rounds/word},
$$
and
$$
r\approx 0.9998.
$$
Thus later-entering words do not merely carry less early energy; their visible saturation event is delayed by almost exactly the same word index offset.

The carry-centroid timing law provides a third independent measure:
$$
C_{\mathrm{carry}}(k)\approx C_0+\gamma k,
$$
with
$$
\gamma\approx 0.4648\ \text{rounds/word},
$$
and
$$
r\approx 0.9817.
$$
These three laws—early energy, saturation wavefront, and carry-centroid drift—jointly establish that the word index is not an arbitrary label. It is the visible time coordinate of direct state-space transport.

### 4.2 Boundary regime and terminal layer

The terminal region near $W[12..15]$ is a boundary layer, not a refutation of the direct law. By then, only a small number of rounds remain before the fixed early window is cut off, so the available measurement interval itself shrinks. The law therefore continues to hold structurally even where the observable window becomes truncated.

### 4.3 Cross-block null

Across the block boundary, the measured early-energy slope collapses to approximately
$$
-0.0632\ \text{bits/word},
$$
with weak correlation
$$
r\approx -0.3679.
$$
Relative to the direct intra-block law, this is a null. The chaining boundary therefore behaves as a temporal reset: it preserves magnitude while erasing schedule-position age.

### 4.4 Bit-scale null

The bit scale shows no stable direct transport gradient. All bits within a word inject simultaneously when the word is called. Therefore the bit axis is not a transport-age axis, even though bit-level toggling remains essential to the mechanics of the round function.

These observations justify the first main conclusion of the paper:

> The only native state-visible transport scale observed so far is the staggered **word-entry** scale.

---

## 5. Probe K: Cumulative New-Bit Support

The first re-injection question is whether the algebraically guaranteed return at $k+16$ creates a second support-growth wave in state space.

Define the cumulative new-bit count
$$
N_k(r)=\mathrm{HW}\!\left(M_k(r)\wedge \neg\bigvee_{t<r}M_k(t)\right),
$$
where $\mathrm{HW}$ is Hamming weight and the union is taken over all earlier state masks for source word $k$.

Define the secondary-window signal-to-noise ratio
$$
\mathrm{SNR}_K(k)=
\frac{\displaystyle\operatorname{mean}_{r\in[k+15,\ k+21]}N_k(r)}
{\displaystyle\operatorname{mean}_{r\in[k+6,\ k+14]}N_k(r)}.
$$

The measured mean is
$$
\overline{\mathrm{SNR}}_K=0.0035755736,
$$
with maximum
$$
\max_k \mathrm{SNR}_K(k)=0.0089409895.
$$
This is not a small positive second wave. It is essentially zero across all 16 words.

The strongest sub-result is the exact-zero audit on the late secondary window for $W[12]$ and $W[13]$:
$$
N_{12}(r)=0.0\qquad \forall r\in[27,33],
$$
$$
N_{13}(r)=0.0\qquad \forall r\in[28,34].
$$
These are literal float64 zeros in the measured bench, not display artifacts or rounded residues.

The forced conclusion of Probe $K$ is:

> The primary wave exhausts the support-growth manifold before the secondary $k+16$ re-entry can create new support.

This does **not** mean there is no later re-entry. It means the later re-entry is not support-forming in the state observables measured here.

---

## 6. Probe L: Amplitude Inside Saturated Support

Probe $K$ closes the support-growth question. Probe $L$ asks the next one: if secondary injection cannot create new support, can it at least create a second amplitude wave inside the already-active support manifold?

Define the baseline window as $r\in[k+6,k+14]$ and the secondary window as $r\in[k+15,k+21]$. Then define the four secondary-to-baseline ratios:

Active ratio:
$$
R_{\mathrm{active}}(k)=
\frac{
\operatorname{mean}_{r\in[k+15,k+21]}\mathrm{HW}(M_k(r))
}{
\operatorname{mean}_{r\in[k+6,k+14]}\mathrm{HW}(M_k(r))
}.
$$

Toggle ratio:
$$
R_{\mathrm{toggle}}(k)=
\frac{
\operatorname{mean}_{r\in[k+15,k+21]}
\mathrm{HW}\!\bigl(M_k(r)\oplus M_k(r-1)\bigr)
}{
\operatorname{mean}_{r\in[k+6,k+14]}
\mathrm{HW}\!\bigl(M_k(r)\oplus M_k(r-1)\bigr)
}.
$$

Overlap ratio:
$$
R_{\mathrm{overlap}}(k)=
\frac{
\operatorname{mean}_{r\in[k+15,k+21]}
\mathrm{HW}\!\bigl(M_k(r)\wedge M_k(r-1)\bigr)
}{
\operatorname{mean}_{r\in[k+6,k+14]}
\mathrm{HW}\!\bigl(M_k(r)\wedge M_k(r-1)\bigr)
}.
$$

New-support ratio:
$$
R_{\mathrm{new}}(k)=\mathrm{SNR}_K(k).
$$

The aggregate means are
$$
\overline{R}_{\mathrm{active}}=0.9979,\qquad
\overline{R}_{\mathrm{toggle}}=1.0009,\qquad
\overline{R}_{\mathrm{overlap}}=0.9957,\qquad
\overline{R}_{\mathrm{new}}=0.0036.
$$
These numbers remain pinned near unity for active/toggle/overlap and near zero for new support. This is the signature of **within-saturation modulation**, not a new amplitude wave.

A stronger per-bit significance audit was then applied using 32 per-bit overlap ratios per word, 4000-resample bootstrap confidence intervals, and a one-sided permutation test against the pooled unflagged words. The result is precise:

- only **$W[9]$** shows a statistically real overlap dip,
- $W[12]$ and $W[13]$ do **not**,
- and even for $W[9]$, the word-level overlap ratio remains near unity.

Thus Probe $L$ yields a careful but still negative conclusion:

> No second amplitude wave exists in state space.  
> A small within-saturation overlap modulation appears at $W[9]$, but it is not a support-forming or amplitude-bearing second wave.

This is exactly the kind of nuance that should be preserved in the paper rather than flattened into a binary “all null” or “signal found” slogan.

---

## 7. Probe M: Phase-Selective Support Echo

The final state-space loophole is that a lag-16 phase echo could exist beneath the amplitude threshold. Probe $M$ tests whether the state masks exhibit a hidden phase-locked support resonance at lag 16.

For lag $L$, define Jaccard similarity and cosine similarity between round-$r$ and round-$(r+L)$ masks. Because the lag profile decays monotonically with $L$, a global mean control is misleading. The correct control is the local adjacent-lag interpolant:
$$
\Delta J_{16}^{\mathrm{local}}(k)=
J_k(16)-\frac12\bigl(J_k(15)+J_k(17)\bigr).
$$
A genuine lag-16 echo should show a systematic positive deviation above this local baseline and should produce per-word peaks at lag 16.

The measured mean local lag-16 Jaccard advantage is
$$
\overline{\Delta J_{16}^{\mathrm{local}}}=+5.44\times 10^{-4},
$$
with standard deviation
$$
\hat{\sigma}_{\Delta J}=1.35324\times 10^{-3}.
$$
The number of words peaking at lag 16 is
$$
0/16.
$$
This closes the phase-echo loophole.

Probe $M$ therefore forces the third and final state-space closure:

> There is no phase-locked lag-16 support echo in the measured state observables.

At this point the $k+16$ state-space question is completely closed by three independent classes:

1. support-growth null,
2. amplitude-wave null,
3. phase-echo null.

The only remaining way later echoes can remain real is if they are strong somewhere **other than** direct state-space support growth. This is precisely what the schedule-space probes show.

---

## 8. Probe N: Direct Schedule-Space Echoes

The SHA-256 schedule recurrence is
$$
W[t]=W[t-16]+\sigma_0(W[t-15])+W[t-7]+\sigma_1(W[t-2]) \pmod{2^{32}}.
$$
A perturbation in source word $W[k]$ must therefore reappear at deeper schedule locations even if state space fails to show a visible second wave.

Probe $N$ measures the schedule-space XOR-Hamming signal
$$
H_{\mathrm{sched}}(k,t)=\mathrm{HW}\bigl(W_k^{\mathrm{pert}}(t)\oplus W^{\mathrm{ref}}(t)\bigr).
$$

The measured mean direct echoes are
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

These values matter because they directly refute the easy but false inference

$$
\text{state-space null} \Longrightarrow \text{later echo absent}.
$$

The later echoes are not absent. They are large, orderly, and increasing in schedule space. What disappears is not the schedule echo itself, but its ability to create **new state support** after the state manifold has saturated.

This is the basis change that turns the whole program. Once schedule space is treated as a distinct field rather than as a hidden nuisance variable, the later re-entry becomes measurable and structured.

---

## 9. Probe P: Recursive Path Multiplicity and the Secondary Tail

Probe $N$ reveals a characteristic tail at $k+16$: the later source words show much stronger secondary schedule echoes than the earlier ones. The next question is whether this tail is merely a landing-site arithmetic artifact or a true property of the schedule graph.

Define the path-multiplicity matrix by
$$
P_{i,k}=\delta_{ik},\qquad i<16,
$$
$$
P_{i,k}=P_{i-2,k}+P_{i-7,k}+P_{i-15,k}+P_{i-16,k},\qquad i\ge 16.
$$
This counts the number of recursive dependency paths through which source word $W[k]$ reaches schedule position $W[i]$.

At the secondary stage $i=k+16$, three regimes appear:
$$
P=1 \quad \text{for } k=0..8,
$$
$$
P=3 \quad \text{for } k=9..13,
$$
$$
P=5 \quad \text{for } k=14..15.
$$

This is the exact schedule-graph explanation for the secondary tail turn-on.

The measured secondary amplitude correlates strongly with path multiplicity, substantially better than with the simpler immediate-parent-hit count. The late tail is therefore not a local arithmetic accident. It is a recursive multi-path schedule echo.

This result matters for two reasons.

First, it explains why the secondary schedule echo is weak for early words, jumps at $k=9$, and jumps again at $k=14$.

Second, it reveals that “position” in SHA-256 changes role as the computation advances. At first, position means **when** a word enters. Later, position means **how many recursive routes** it has back into the schedule field.

The schedule is therefore not just a staggered injector. It is a branching field whose later amplitudes are shaped by graph multiplicity.

---

## 10. Probe R: The Capacity-Gated Projection Law

The central paradox now becomes sharp.

- Schedule-space echoes are real, large, and increasing.
- State-space support growth after the primary wave is essentially zero.

The missing bridge is the projection law from schedule space into state space.

Let
$$
H_{\mathrm{sched}}(k,r)
$$
be the mean schedule-space XOR-Hamming signal at round $r$ for source word $k$.

Let
$$
N_{\mathrm{state}}(k,r)
$$
be the newly activated state bits at round $r$.

Let
$$
U(k,r)=\mathrm{HW}\!\left(\bigcup_{j=0}^{r}M_k(j)\right)
$$
be the cumulative union support through round $r$.

Then define the remaining unsaturated capacity
$$
C(k,r)=\frac{256-U(k,r)}{256}.
$$

Probe $R$ fits the model
$$
N_{\mathrm{state}}(k,r)\approx \alpha^\* H_{\mathrm{sched}}(k,r) C(k,r)^{\beta^\*},
$$
with optimal parameters
$$
\alpha^\*=10.462043,\qquad \beta^\*=0.65.
$$

The crucial comparison is this:

- schedule-only prediction fails,
- capacity-weighted prediction succeeds.

The fitted performance of the capacity-gated model is
$$
R^2=0.842533,\qquad \mathrm{corr}=0.918257.
$$

This is the first concrete quantitative answer to the schedule-to-state projection question.

The meaning of the law is straightforward:

- In the primary window, schedule signal is moderate but capacity is still large, so new support appears.
- In the secondary and tertiary windows, schedule signal may be large or even very large, but capacity has collapsed toward zero, so new support does not appear.
- The state interface is therefore not a passive image of the schedule. It is a nonlinear projector gated by residual support headroom.

The law does not yet claim a first-principles derivation of $\alpha^\*$ and $\beta^\*$. It remains a phenomenological fit. But it is already strong enough to explain why the state-space nulls and the schedule-space positives coexist without contradiction.

---

## 11. Unified Layered Transport Model

The measured system is best described by a four-stage sequence:
$$
\text{Entry}\rightarrow \text{Branch}\rightarrow \text{Saturate}\rightarrow \text{Reset}.
$$

### Stage 1 — Entry

At
$$
t=k,
$$
the direct source word enters the schedule. Because capacity is still available and injection is staggered, this stage is support-forming and state-visible.

### Stage 2 — Branch

At
$$
t=k+16,\quad k+32,\quad k+48,
$$
the recursive schedule topology forces later echoes. These echoes are strongly schedule-visible and increasingly shaped by path multiplicity.

### Stage 3 — Saturate

As the primary state wave progresses, cumulative support grows and remaining capacity collapses:
$$
C(k,r)\to 0.
$$
The state therefore rejects later echoes as support-forming waves even while schedule-space amplitude continues to grow.

### Stage 4 — Reset

At the block boundary, the chaining digest injects simultaneously into all eight lanes. The perturbation magnitude is preserved, but the schedule-position age structure is erased.

This yields the final scoped transport law:
$$
\text{visible state-space transport}
\iff
H_{\mathrm{sched}}(k,r)\,C(k,r)^{\beta^\*}\ \text{remains non-negligible}.
$$

This law is the compact synthesis of the entire bench:

- direct visible transport requires stagger,
- later recursive echoes are path-governed,
- state visibility is capacity-gated,
- and the block boundary resets age while preserving magnitude.

---

## 12. Nexus Interpretation Layer

The sections above are the transport-forced layer. They stand on the bench. What follows is the framework-interpretive layer: the broader Nexus reading that becomes available once the transport result is accepted.

In the Nexus lens, SHA-256 is not treated as a black-box shredder but as a constrained folding environment. The direct transport program supports this reading in a precise sense: the algorithm preserves ordered informational lineage in schedule space even when state space ceases to show new support. The later echoes are not destroyed; they are projected below the support-forming visibility threshold. That already shifts the conceptual center of gravity away from “entropy as destruction” and toward “constraint as projection.”

Under this reading, the state behaves less like a sink and more like a finite geometric aperture. The schedule acts as a branching field. The state acts as a capacity-limited rendering surface. The block boundary acts as a temporal reset operator. This is exactly the kind of layered operational object that the broader Nexus framework expects to find when a recursive manifold is instrumented at multiple scales.

The Mark 1 attractor language enters here, not in the forced transport layer. The fitted exponent
$$
\beta^\*=0.65
$$
naturally invites the complementary headroom reading
$$
1-\beta^\*=0.35.
$$
Within the broader framework, that is interpreted in relation to the harmonic attractor
$$
H=\frac{\pi}{9}\approx 0.349065.
$$
That interpretation may be meaningful inside Nexus, but the transport bench alone only forces the existence of the fitted exponent $\beta^\*=0.65$ and its predictive success inside the capacity-gated projection law. The stronger harmonic identification belongs to the interpretation layer.

Likewise, the broader hardware-isomorphism reading is framework-native but should be expressed with scope discipline. The transport result shows that SHA-256 contains:

- a temporally staggered injector,
- a recursive branching field,
- a capacity-limited projector,
- and a temporal reset boundary.

That already makes the algorithm look more like a structured machine than like an undifferentiated diffuser. Whether one then reads that machine as a local mirror of broader computational ontology is a legitimate Nexus move, but it should still be marked as interpretation rather than bench-forced proof.

This is not a weakness. It is the correct way to make the paper survive both inside and outside the framework. The transport backbone remains strong. The Nexus synthesis remains visible. The two are no longer forced into a false evidentiary merger.

---

## 13. Open Problems

The broad transport geometry is now closed enough to isolate the remaining narrow problems.

### 13.1 First-principles derivation of the projection law

The current law
$$
N_{\mathrm{state}}(k,r)\approx \alpha^\* H_{\mathrm{sched}}(k,r) C(k,r)^{\beta^\*}
$$
is fitted, not yet derived. The next step is to derive $\alpha^\*$ and $\beta^\*$ directly from compression topology rather than from pooled regression.

### 13.2 Closed-form deeper path laws

Probe $P$ resolves the $k+16$ threshold cleanly. The deeper $k+32$ and $k+48$ regimes still need full closed-form path-law treatment, even though the measured echo amplitudes are already known.

### 13.3 Modulation threshold

The paper cleanly distinguishes support-forming and support-subcritical echoes. The remaining boundary is the thin middle band of within-saturation modulation, exemplified by the small but statistically real $W[9]$ overlap dip. A sharper criterion is needed for when a later echo remains support-null but still leaves a measurable within-saturation signature.

### 13.4 Projection timing

The capacity-gated law explains visibility, but not yet the full timing structure of when schedule-space signal is admitted or rejected by the state manifold. A deeper derivation may require a more detailed account of how round-local schedule signal, carry structure, and available support interact.

---

## 14. Conclusion

The transport program has resolved the central paradox.

Within SHA-256, direct intra-block perturbations generate a visible state-space gradient because word entry is temporally staggered and support capacity remains available. Across a block boundary, the gradient collapses because injection is simultaneous. Within a word, the gradient collapses because the bit positions do not carry distinct entry ages. The direct state-space transport geometry is therefore a word-scale, temporally ordered phenomenon.

The later recursive echoes are real. Probe $N$ measures them directly in schedule space. Probe $P$ shows that the late secondary tail is governed by recursive path multiplicity rather than local landing arithmetic. Probe $R$ then resolves the state-space paradox by showing that visibility is gated by remaining support capacity. Later echoes are not absent. They are schedule-real and state-subcritical.

The most compact final statement is therefore:
$$
\text{SHA-256 transport is governed by entry, branching, saturation, and reset.}
$$
Or, in explicit transport form,
$$
\text{state-visible transport}
\iff
\text{temporally staggered schedule signal arrives before capacity is exhausted}.
$$

That result is already enough to move beyond the coarse language of “generic diffusion” or “information shredding.” It reveals a layered machine with one native state-visible transport stage, deeper recursive schedule echoes, and a nonlinear projection interface between them. The remaining task is not to rediscover the system, but to derive its final coefficients and thresholds from first principles.

---

## Appendix A. Key Measured Quantities

### Direct state-space transport
$$
E_{\mathrm{early}}(k)\approx 105.27-7.865k
$$
$$
\text{inner slope}\approx -7.921\ \text{bits/word},\qquad r\approx -0.9998
$$
$$
r_{\mathrm{sat}}(k)\approx k+5
$$
$$
\text{saturation slope}\approx +0.9991\ \text{rounds/word},\qquad r\approx 0.9998
$$
$$
\gamma\approx 0.4648\ \text{rounds/word},\qquad r\approx 0.9817
$$

### Cross-block null
$$
\text{cross-block early slope}\approx -0.0632\ \text{bits/word},\qquad r\approx -0.3679
$$

### Probe K
$$
\overline{\mathrm{SNR}}_K=0.0035755736
$$
$$
N_{12}(r)=0,\quad r\in[27,33]
$$
$$
N_{13}(r)=0,\quad r\in[28,34]
$$

### Probe L
$$
\overline{R}_{\mathrm{active}}=0.9979,\quad
\overline{R}_{\mathrm{toggle}}=1.0009,\quad
\overline{R}_{\mathrm{overlap}}=0.9957,\quad
\overline{R}_{\mathrm{new}}=0.0036
$$
Only $W[9]$ shows a statistically real but weak overlap dip.

### Probe M
$$
\overline{\Delta J_{16}^{\mathrm{local}}}=+5.44\times10^{-4},
\qquad
0/16\ \text{words peak at lag 16}
$$

### Probe N
$$
H(k)=1.000,\qquad
H(k+16)=4.910,\qquad
H(k+32)=15.945,\qquad
H(k+48)=16.107
$$

### Probe P
$$
P=1 \text{ for } k=0..8,\qquad
P=3 \text{ for } k=9..13,\qquad
P=5 \text{ for } k=14..15
$$

### Probe R
$$
N_{\mathrm{state}}(k,r)\approx \alpha^\* H_{\mathrm{sched}}(k,r) C(k,r)^{\beta^\*}
$$
$$
\alpha^\*=10.462043,\qquad \beta^\*=0.65
$$
$$
R^2=0.842533,\qquad \mathrm{corr}=0.918257
$$
