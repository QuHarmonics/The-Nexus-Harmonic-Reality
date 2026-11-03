# SHA-256 Final Transport Model

## Core collapse

The machine is best described as a **scoped transport system** with four distinct regimes:

1. **Staggered injection**
2. **Recursive schedule branching**
3. **State-space saturation**
4. **Block-boundary temporal reset**

The governing law is:

$$
\text{visible transport gradient} \iff \text{different propagation age at injection}
$$

Equivalently,

$$
G \neq 0 \iff \exists\, i,j \text{ such that } \tau_i \neq \tau_j
$$

and if all relevant inputs are injected simultaneously,

$$
\tau_i = \tau_j \ \forall i,j \quad \Longrightarrow \quad G \approx 0
$$

---

## 1. Direct intra-block law

For direct message-schedule injection, the source word $W[k]$ first enters the compression function at round

$$
\tau_k = k
$$

This gives the primary early-window law:

$$
E_{\mathrm{early}}(k) \approx A - Bk
$$

with measured values

$$
A \approx 105.27, \qquad B \approx 7.87 \text{ bits/word}
$$

For the clean inner regime $W[0..11]$:

$$
E_{\mathrm{early}}(k) \approx 105.27 - 7.865\,k
$$

with measured slope approximately

$$
-7.921 \text{ bits/word}, \qquad r \approx -0.9998
$$

The saturation law is:

$$
r_{\mathrm{sat}}(k) \approx k + 5
$$

with measured slope

$$
+0.9991 \text{ rounds/word}, \qquad r \approx 0.9998
$$

The carry-centroid timing law is:

$$
C_{\mathrm{carry}}(k) \approx C_0 + \gamma k
$$

with fitted 16-word slope

$$
\gamma \approx 0.4648 \text{ rounds/word}, \qquad r \approx 0.9817
$$

So within one block:

$$
\text{word index} = \text{injection time}
$$

---

## 2. Cross-block boundary law

Across a block boundary, the chaining value injects into all eight state lanes simultaneously at round 0:

$$
\tau_k^{(\mathrm{cross})} = 0 \quad \forall k
$$

Therefore the direct gradient collapses:

$$
\frac{\partial E_{\mathrm{early}}}{\partial k} \approx 0
$$

Measured cross-block slope over all 16 words:

$$
-0.0632 \text{ bits/word}, \qquad r \approx -0.3679
$$

This means the boundary preserves perturbation magnitude but erases schedule-position age structure:

$$
\text{preserve magnitude, erase age}
$$

---

## 3. Schedule branching law

The schedule is not a one-shot injector. It is a recursive branching system:

$$
W[i] = \sigma_1(W[i-2]) + W[i-7] + \sigma_0(W[i-15]) + W[i-16]
\pmod{2^{32}}
$$

Define path multiplicity from input word $W[k]$ to schedule word $W[i]$ by

$$
P_{i,k} = \delta_{ik}, \qquad i < 16
$$

and for $i \ge 16$,

$$
P_{i,k} = P_{i-2,k} + P_{i-7,k} + P_{i-15,k} + P_{i-16,k}
$$

This captures **how many recursive routes** the source word has into a later schedule location.

---

## 4. Multi-stage schedule echoes

Direct schedule-space probing shows the echo hierarchy:

$$
\Delta W[k] \rightarrow \Delta W[k+16] \rightarrow \Delta W[k+32] \rightarrow \Delta W[k+48]
$$

Measured mean schedule-space Hamming responses:

$$
\mathbb{E}\big[\mathrm{HW}(\Delta W[k])\big] \approx 1.000
$$

$$
\mathbb{E}\big[\mathrm{HW}(\Delta W[k+16])\big] \approx 4.910
$$

$$
\mathbb{E}\big[\mathrm{HW}(\Delta W[k+32])\big] \approx 15.945
$$

$$
\mathbb{E}\big[\mathrm{HW}(\Delta W[k+48])\big] \approx 16.107
$$

So the schedule behaves like a recursive branching amplifier:

$$
\text{schedule space} = \text{recursive branching amplifier}
$$

### Secondary echo structure

At the secondary stage, the late tail is not explained by the landing word $W[k+16]$ alone.

Instead, the measured secondary echo strength tracks recursive path multiplicity:

- $W[0..8]$: path multiplicity $= 1$, low secondary response
- $W[9..13]$: path multiplicity $= 3$, secondary response jumps
- $W[14..15]$: path multiplicity $= 5$, secondary response is highest

This is the correct explanation of the tail turn-on.

---

## 5. State-space compression law

The state does **not** expose the deeper schedule echoes cleanly.

Primary injection is state-visible because it builds support:

$$
W[k] \text{ at round } k \quad \Longrightarrow \quad \text{support growth}
$$

But later schedule echoes occur after the state manifold is already saturated.

The state-space nulls can be summarized as:

### No second support-growth wave
For the cumulative new-bit metric,

$$
\text{new support at } k+16 \approx 0
$$

### No strong amplitude bump inside saturated support
Measured secondary-to-baseline ratios are approximately

$$
R_{\mathrm{active}} \approx 0.998,\qquad
R_{\mathrm{toggle}} \approx 1.001,\qquad
R_{\mathrm{overlap}} \approx 1.000
$$

while

$$
R_{\mathrm{new}} \approx 0.002
$$

So secondary reinjection is not creating a new transport wave in state space.

### No phase-locked support echo
Lag-16 support-similarity probes also stay flat, so there is no strong mask-space resonance at lag 16.

Therefore:

$$
\text{state space} = \text{saturating projection of the schedule amplifier}
$$

---

## 6. Final layered law

The final model is:

### Stage 1: primary entry
$$
t = k
$$

This stage is:

- support-forming
- gradient-bearing
- state-visible

### Stage 2: secondary echo
$$
t = k + 16
$$

This stage is:

- schedule-visible
- branching-dependent
- mostly state-subcritical

### Stage 3: tertiary echo
$$
t = k + 32
$$

This stage is:

- strong in schedule space
- still shaped by recursive branching
- heavily compressed at the state interface

### Stage 4: quaternary echo
$$
t = k + 48
$$

This stage is:

- again strong in schedule space
- near the observable ceiling for 32-bit schedule-word Hamming response

---

## 7. Final interpretation

The machine is not best understood as “a diffusion engine” in the abstract.

It looks like:

$$
\text{entry} \rightarrow \text{branch} \rightarrow \text{saturate} \rightarrow \text{reset}
$$

More explicitly:

$$
\text{message schedule} = \text{temporally staggered injector + recursive branching field}
$$

$$
\text{compression state} = \text{saturating projector of that field}
$$

$$
\text{chaining boundary} = \text{temporal reset operator}
$$

That gives the final scoped law:

$$
\text{position in SHA means first } \textbf{when} \text{ a word enters, then later } \textbf{how many routes} \text{ it has back into the schedule}
$$

This is the finished transport picture.

---

## 8. What remains open

The main unresolved object is the exact projection law from schedule space to state space:

$$
\Delta W[t] \longrightarrow \Delta S[r]
$$

In particular, we still want a closed-form criterion for when a schedule-space echo is:

- support-forming,
- support-modulating,
- or state-invisible due to saturation.

That is now the narrow remaining problem, not the whole framework.
