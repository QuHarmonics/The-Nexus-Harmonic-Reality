# SHA-256 Input Transport Geometry  
## Full Schedule Window, Boundary Reset, Re-injection Horizon, Schedule-Space Echo, and Recursive Path Multiplicity  
**QuHarmonics Research Group — Dean Kulik — April 2026**

---

## Abstract

This document consolidates and extends the SHA-256 transport-geometry program through Probes A–N into a single corrected formulation. The central result is that SHA-256 contains exactly one native transport gradient in *state space*: the word-level message schedule under temporally staggered injection. The schedule injects words $W[k]$ sequentially at rounds $k=0,\dots,15$, producing a direct early-energy gradient, a wavefront/saturation law, and a carry-timing gradient. The chaining state and the 32 bits inside any single word are both injected simultaneously, so neither produces a positional gradient.

The complete 16-word scan confirms that the inner early-energy law is linear over $W[0]\dots W[11]$ with slope approximately $-7.921$ bits/word and correlation $r=-0.9998$, while a boundary layer appears in $W[12]\dots W[15]$ because only $1$–$4$ early rounds remain. The saturation law extends cleanly across all $16$ words:

$$
r_{\mathrm{sat}}(k) \approx k + 5,
$$

with fitted slope $+0.9991$ rounds/word and $r=0.9998$. The full 16-word carry-centroid scan sharpens the direct timing gradient to

$$
\Gamma(k) \approx \Gamma_0 + 0.4648\,k,
$$

with $r=0.9817$. The cross-block measurement remains flat within noise, with slope $-0.0632$ bits/word and $r=-0.3679$, confirming the block boundary as a reset of measured schedule-position observables.

The schedule algebra guarantees a second appearance of each input word at round $k+16$ through the direct $W[i-16]$ term in the recurrence. Probes J–M show that this secondary re-injection is *not* transport-visible in state space under the present observables: carry-delta probing yields a mean secondary-window SNR of only $1.041$, a cumulative new-bit probe yields a mean secondary-window SNR of $0.004$, amplitude-inside-support ratios remain approximately unity, and lag-$16$ support similarity shows no special peak. Thus the secondary re-injection does not create a second measurable support-expansion wave, a strong second amplitude wave, or a phase-locked support echo in the state.

Probe N resolves the hidden stage directly in *schedule space*. For each source word, the direct schedule echoes at $t=k$, $t=k+16$, $t=k+32$, and $t=k+48$ are all nonzero with mean XOR-Hamming weights $1.000$, $4.910$, $15.945$, and $16.107$ respectively, and unit nonzero incidence at all four direct echo points. Therefore the secondary injector is causal and exact in $W$-space but becomes state-subcritical after primary saturation.

Probe P closes the remaining tail question. The strong rise of the $k+16$ schedule echo for late words is **not** explained by local carry susceptibility of the landing word $W[k+16]$ alone. It is explained by **recursive schedule path multiplicity**. If $P_{i,k}$ denotes the number of syntactic dependency paths from source word $W[k]$ to schedule word $W[i]$, then $P_{k+16,k}$ takes the values $1$ for $k=0\dots 8$, $3$ for $k=9\dots 13$, and $5$ for $k=14,15$. The measured secondary Hamming response tracks this regime change with correlation $0.948957$. Thus the secondary tail geometry is a branching property of the schedule graph, not a single landing-site arithmetic effect. The resulting transport picture is: primary injection is support-forming; secondary and later injections are support-revisiting in schedule space; and late secondary amplification is governed by recursive path count rather than by a new state-space transport law.

---

## 1. Preliminaries and notation

SHA-256 operates on a sequence of $512$-bit blocks, each represented as $16$ input words of $32$ bits each:

$$
W[0],W[1],\dots,W[15] \in \{0,1\}^{32}.
$$

For a single compression block, the message schedule is expanded to $64$ words by

$$
W[i] = \sigma_1\!\left(W[i-2]\right) + W[i-7] + \sigma_0\!\left(W[i-15]\right) + W[i-16]
\qquad \text{for } i=16,\dots,63,
$$

where all additions are modulo $2^{32}$ and

$$
\sigma_0(x) = \operatorname{ROTR}^7(x)\oplus \operatorname{ROTR}^{18}(x)\oplus (x \gg 3),
$$

$$
\sigma_1(x) = \operatorname{ROTR}^{17}(x)\oplus \operatorname{ROTR}^{19}(x)\oplus (x \gg 10).
$$

The compression state is the 8-word register tuple

$$
(a,b,c,d,e,f,g,h)\in(\mathbb{Z}/2^{32}\mathbb{Z})^8.
$$

Each round $r=0,\dots,63$ computes

$$
T_1^{(r)} = h + \Sigma_1(e) + \operatorname{Ch}(e,f,g) + K[r] + W[r],
$$

$$
T_2^{(r)} = \Sigma_0(a) + \operatorname{Maj}(a,b,c),
$$

with

$$
\Sigma_0(x)=\operatorname{ROTR}^2(x)\oplus \operatorname{ROTR}^{13}(x)\oplus \operatorname{ROTR}^{22}(x),
$$

$$
\Sigma_1(x)=\operatorname{ROTR}^6(x)\oplus \operatorname{ROTR}^{11}(x)\oplus \operatorname{ROTR}^{25}(x),
$$

$$
\operatorname{Ch}(x,y,z)=(x\land y)\oplus(\neg x \land z),
$$

$$
\operatorname{Maj}(x,y,z)=(x\land y)\oplus(x\land z)\oplus(y\land z).
$$

The state update is

$$
a' = T_1^{(r)} + T_2^{(r)}, \qquad e' = d + T_1^{(r)},
$$

followed by the standard shift:

$$
(h,g,f,e,d,c,b,a)\mapsto(g,f,e,e',c,b,a,a').
$$

---

## 2. Corrected probe architecture

The corrected two-block geometry uses the raw compression core directly, not padded messages. This avoids the padding ambiguity that a $128$-byte message pads to three SHA-256 blocks, not two.

### Probe A — Direct intra-block, block 0
Perturb one bit in block 0 and measure the perturbation inside block 0 using initial value $H_0$.

### Probe B — Direct intra-block, block 1
Perturb one bit in block 1 and measure inside block 1 using the chaining value from the unperturbed block 0 as IV.

### Probe C — Cross-block
Perturb one bit in block 0, recompute the chaining value, and measure the perturbation in block 1 with fixed block-1 words.

### Probe D — First-entry theory
Analytic explanation of the early-energy gradient from first-entry round.

### Probe E — Transport wavefront
Full $64$-round state-delta profile per word.

### Probe F — Carry centroid
Round-weighted center of mass of carry-delta activity.

### Probe G — Sub-word bit scan
Bit-position scan inside each 32-bit word.

### Probe H — Injection simultaneity principle
The unifying rule extracted from Probes A–G.

### Probe I — Full 16-word scan
Extends Probes A, E, and F from $W[0..7]$ to $W[0..15]$.

### Probe J — Schedule re-injection fingerprint
Tests whether the analytically guaranteed re-entry at round $k+16$ is visible in carry-delta.

### Probe K — Cumulative new-bit probe
Tests whether re-entry at round $k+16$ creates genuinely new support in state space.

---

## 3. Measurement formulas

Let $S_{k,b}^{(r)}$ denote the round-$r$ state after flipping bit $b$ in word $W[k]$, and let $S^{(r)}$ be the unperturbed reference state.

Define the roundwise state-delta magnitude by total Hamming distance across all 8 state words:

$$
\Delta_{k,b}(r)=\sum_{j=0}^{7}\operatorname{HW}\!\left(S_j^{(r)} \oplus S_{j,k,b}^{(r)}\right).
$$

### 3.1 Early, mid, and late energy

For word $W[k]$, averaged over its 32 bits,

$$
E_{\mathrm{early}}(k)=\frac{1}{32}\sum_{b=0}^{31}\frac{1}{16}\sum_{r=0}^{15}\Delta_{k,b}(r),
$$

$$
E_{\mathrm{mid}}(k)=\frac{1}{32}\sum_{b=0}^{31}\frac{1}{16}\sum_{r=16}^{31}\Delta_{k,b}(r),
$$

$$
E_{\mathrm{late}}(k)=\frac{1}{32}\sum_{b=0}^{31}\frac{1}{32}\sum_{r=32}^{63}\Delta_{k,b}(r).
$$

### 3.2 Saturation round

With saturation threshold $\theta=110$ bits, define

$$
r_{\mathrm{sat}}(k,b)=\min\{r:\Delta_{k,b}(r)\ge \theta\},
$$

and the word-level mean saturation round

$$
r_{\mathrm{sat}}(k)=\frac{1}{32}\sum_{b=0}^{31} r_{\mathrm{sat}}(k,b).
$$

### 3.3 Carry shadow and carry centroid

For each round, define the carry count as the number of overflows among the three 32-bit additions that create $T_1$, $e_{\text{new}}$, and $a_{\text{new}}$:

$$
C^{(r)}=
\mathbf{1}\!\left[T_{1,\mathrm{raw}}^{(r)}\ge 2^{32}\right]
+
\mathbf{1}\!\left[d+T_1^{(r)}\ge 2^{32}\right]
+
\mathbf{1}\!\left[T_1^{(r)}+T_2^{(r)}\ge 2^{32}\right].
$$

For a perturbed trace, define carry delta

$$
\delta C_{k,b}(r)=\left|C^{(r)}-C_{k,b}^{(r)}\right|.
$$

The carry centroid is

$$
\Gamma_{k,b}=
\frac{\sum_{r=0}^{63} r\,\delta C_{k,b}(r)}
{\sum_{r=0}^{63} \delta C_{k,b}(r)}.
$$

The word-level carry centroid is

$$
\Gamma(k)=\frac{1}{32}\sum_{b=0}^{31}\Gamma_{k,b}.
$$

### 3.4 Re-injection SNR (Probe J)

For each word $W[k]$, define:

- primary window: rounds $k,\dots,k+5$
- baseline window: rounds $k+6,\dots,k+14$
- secondary window: rounds $k+15,\dots,k+21$

Then

$$
\mu_{\mathrm{prim}}(k)=\frac{1}{6}\sum_{r=k}^{k+5}\delta C_k(r),
$$

$$
\mu_{\mathrm{base}}(k)=\frac{1}{9}\sum_{r=k+6}^{k+14}\delta C_k(r),
$$

$$
\mu_{\mathrm{sec}}(k)=\frac{1}{7}\sum_{r=k+15}^{k+21}\delta C_k(r),
$$

and

$$
\mathrm{SNR}^{(\mathrm{carry})}_k=
\frac{\mu_{\mathrm{sec}}(k)}{\mu_{\mathrm{base}}(k)}.
$$

### 3.5 Cumulative new-bit metric (Probe K)

Define the round-$r$ active support mask

$$
M_{k,b}(r)=S^{(r)}\oplus S_{k,b}^{(r)},
$$

viewed as a 256-bit mask over the 8 state words. Let the support previously seen before round $r$ be

$$
U_{k,b}(r-1)=\bigvee_{t=0}^{r-1} M_{k,b}(t).
$$

Then the number of newly flipped state bits at round $r$ is

$$
N_{k,b}(r)=\operatorname{HW}\!\left(M_{k,b}(r)\land \neg U_{k,b}(r-1)\right).
$$

The Probe-K secondary-window mean is

$$
\mu_{\mathrm{sec}}^{(\mathrm{new})}(k)=
\frac{1}{32}\sum_{b=0}^{31}\frac{1}{7}\sum_{r=k+15}^{k+21}N_{k,b}(r),
$$

with baseline

$$
\mu_{\mathrm{base}}^{(\mathrm{new})}(k)=
\frac{1}{32}\sum_{b=0}^{31}\frac{1}{9}\sum_{r=k+6}^{k+14}N_{k,b}(r),
$$

and corresponding SNR

$$
\mathrm{SNR}^{(\mathrm{new})}_k=
\frac{\mu_{\mathrm{sec}}^{(\mathrm{new})}(k)}
{\mu_{\mathrm{base}}^{(\mathrm{new})}(k)}.
$$

---

## 4. First-entry law and primary transport geometry

The direct early-energy gradient is explained by a single geometric fact:

> $W[k]$ is first consumed by the compression function at round $k$.

Since the early window is rounds $0$ through $15$, word $W[k]$ has exactly

$$
16-k
$$

early rounds available to propagate before the early window closes.

The first-entry linear model is

$$
E_{\mathrm{early}}(k)\approx 105.27 - 7.865\,k.
$$

On the original $8$-word scan this gave the measured slope

$$
-7.860 \text{ bits/word}, \qquad r= -0.99934.
$$

On the full inner 16-word scan, restricting to the linear regime $W[0]\dots W[11]$, the fitted slope sharpens to

$$
-7.921 \text{ bits/word}, \qquad r=-0.9998.
$$

The full 16-word fit is flatter because the final four words form a boundary layer and should not be forced into the same unconstrained linear fit:

$$
-7.436 \text{ bits/word}, \qquad r=-0.9964.
$$

### 4.1 Primary wavefront and saturation

The wavefront law is

$$
r_{\mathrm{sat}}(k)\approx k+5.
$$

Empirically, over $W[0]\dots W[15]$:

$$
r_{\mathrm{sat}}(k)\approx 4.38 + 0.9991\,k,
\qquad r=0.9998.
$$

This is the cleanest expression of the direct transport geometry: the schedule creates a one-round stagger at injection, and that stagger propagates into a one-round stagger in the saturation time.

---

## 5. Carry-centroid timing channel

Even after state energy saturates near the random-diffusion floor of $\sim 128$ bits, word position remains visible in the *timing* of carry activity.

Over the first 8 words, the carry-centroid gradient was

$$
\Gamma(k)\approx 31.73 + 0.392\,k,
\qquad r=0.88.
$$

The full 16-word scan refines this to

$$
\Gamma(k)\approx \Gamma_0 + 0.4648\,k,
\qquad r=0.9817.
$$

Thus $W[15]$ trails $W[0]$ in carry-centroid time by approximately

$$
0.4648\times 15 \approx 6.97 \text{ rounds},
$$

while the $W[7]-W[0]$ lag is about

$$
0.4648\times 7 \approx 3.25 \text{ rounds}.
$$

This sharpens the v3/v4 estimate and shows that timing memory survives longer than amplitude memory.

---

## 6. Boundary reset across blocks

In the corrected two-block probe, the direct block law repeats in block 1 under a nonstandard IV, which proves that the direct schedule gradient is a local block law and not an artifact of the standard IV.

Cross-block perturbations, however, behave differently because they enter block 1 through the chaining state rather than the message schedule. The chaining value initializes all eight state words simultaneously at round $0$.

The 8-word cross-block result was

$$
+0.085 \text{ bits/word}, \qquad r=0.38,
$$

and the 16-word cross-block result sharpened this to

$$
-0.0632 \text{ bits/word}, \qquad r=-0.3679.
$$

Both are noise-level slopes centered near the same flat value:

$$
E_{\mathrm{early}}^{(\mathrm{cross})}(k)\approx 128 + \varepsilon_k,
\qquad |\varepsilon_k|\ll 1.
$$

This is the boundary reset:

- no early-energy gradient,
- no wavefront staggering,
- no carry-centroid gradient,
- but perturbation magnitude survives.

The cross-block carry amplification remains in the range $1.22\times$ to $2.09\times$, so the reset destroys *position* while preserving and even amplifying *total diffusion activity*.

---

## 7. Injection simultaneity principle

The v4 unifying rule is:

$$
\text{A transport gradient exists if and only if injection is temporally staggered.}
$$

This can be expressed in terms of injection time $\tau(x)$ assigned to an input component $x$.

If $\tau(x)$ varies across a family of inputs, then those inputs have different propagation ages at round $r$, and a transport gradient can exist.

If $\tau(x)$ is constant across the family, all inputs have the same propagation age at every round, so no gradient can emerge from entry timing alone.

In SHA-256 there are three relevant injection modes:

| Injection mode | Timing | Gradient? |
|---|---:|---:|
| Schedule words $W[0..15]$ | Sequential, one word per round | Yes |
| Chaining state | Simultaneous at round $0$ | No |
| Bits inside $W[k]$ | Simultaneous at round $k$ | No |

Thus the schedule is the only native stagger source in SHA-256.

---

## 8. Full 16-word schedule window and boundary layer

The 16-word scan adds two essential results.

### 8.1 Inner linear regime

Over $W[0]\dots W[11]$ the first-entry law remains extremely accurate:

| Word | $E_{\mathrm{early}}$ | Predicted | Residual |
|---|---:|---:|---:|
| $W[0]$ | 105.56 | 105.27 | +0.29 |
| $W[1]$ | 98.07 | 97.41 | +0.66 |
| $W[2]$ | 88.39 | 89.54 | -1.15 |
| $W[3]$ | 81.64 | 81.67 | -0.03 |
| $W[4]$ | 73.57 | 73.81 | -0.24 |
| $W[5]$ | 66.39 | 65.94 | +0.44 |
| $W[6]$ | 57.22 | 58.08 | -0.86 |
| $W[7]$ | 50.99 | 50.21 | +0.78 |
| $W[8]$ | 41.71 | 42.35 | -0.64 |
| $W[9]$ | 33.97 | 34.48 | -0.52 |
| $W[10]$ | 26.31 | 26.62 | -0.31 |
| $W[11]$ | 18.09 | 18.75 | -0.67 |

### 8.2 Boundary layer

For $W[12]\dots W[15]$, only $4,3,2,1$ early rounds remain. The linear extrapolation wants to cross below zero, but measured early energy remains nonnegative:

| Word | $E_{\mathrm{early}}$ | Linear prediction | Effective clipped prediction | Residual |
|---|---:|---:|---:|---:|
| $W[12]$ | 10.48 | 10.89 | 10.89 | -0.41 |
| $W[13]$ | 5.18 | 3.02 | 3.02 | +2.16 |
| $W[14]$ | 1.68 | -4.84 | 0.00 | +1.68 |
| $W[15]$ | 0.25 | -12.71 | 0.00 | +0.25 |

This proves that the linear model is an interior approximation. The first one or two propagation rounds contribute less than the saturated per-round average of $7.87$ bits, so the boundary words sit above the naive unconstrained extrapolation.

### 8.3 Boundary-layer formula

A more complete expression is to replace the constant per-round contribution with a growth kernel $g(t)$, where $t$ is propagation age. Then

$$
E_{\mathrm{early}}(k)=\frac{1}{16}\sum_{t=0}^{15-k} g(t),
\qquad 0\le k\le 15.
$$

The linear law is recovered when $g(t)\approx \alpha$ is approximately constant over the useful interior range. The boundary layer appears because $g(0),g(1),\dots$ are smaller than the interior average, and the last words see only these startup terms.

This is the correct form for any future closed-form boundary correction.

---

## 9. Schedule re-injection geometry

The schedule recurrence contains a direct copy pathway:

$$
W[k]\longrightarrow W[k+16]
$$

through the explicit $W[i-16]$ addend in

$$
W[i]=\sigma_1(W[i-2])+W[i-7]+\sigma_0(W[i-15])+W[i-16].
$$

Therefore the second injection round is analytically exact:

$$
r_{\mathrm{reinj}}(k)=k+16.
$$

Likewise, repeated expansion implies tertiary and quaternary direct echo locations at

$$
r_{\mathrm{reinj},2}(k)=k+32,
\qquad
r_{\mathrm{reinj},3}(k)=k+48,
$$

whenever those indices remain inside the 64-word schedule window.

This means each input word is injected at least twice in the causal graph, and in schedule space it can echo four times within the 64-word window.

### 9.1 Probe J result: carry-delta transport horizon

Probe J attempted to detect the $k+16$ reinjection in state space using carry-delta windows. The mean SNR across all 16 words is

$$
\overline{\mathrm{SNR}}^{(\mathrm{carry})}=1.041.
$$

This is too close to unity to count as a resolved second transport layer. The per-word SNR values are irregular, mixed between mild “signal,” noise, and suppression, with no clean positional structure.

So the correct statement is:

- re-injection is **algebraically certain**,
- but **not resolved** by the present carry-delta probe after primary saturation.

This identifies the first transport horizon in the SHA-256 study: after the primary wave has saturated, the carry-delta baseline is already near a stationary noise floor of about 1 carry event per round, so later injections are buried inside an already diffused state.

## 10. Probe K result: no second support-growth wave

Probe K tests the same question using a stricter metric: newly activated state support.

If a second injection at round $k+16$ were creating a second wave of *new* state support, then $N_{k,b}(r)$ should rise again in the secondary window.

It does not.

The measured mean secondary-window SNR is

$$
\overline{\mathrm{SNR}}^{(\mathrm{new})}=0.004,
$$

and the mean absolute peak error relative to the predicted round $k+16$ is approximately

$$
1.0 \text{ round},
$$

with the window maxima consistently falling one round early at $k+15$ but with essentially zero amplitude.

The correct interpretation is therefore:

$$
\text{secondary re-injection exists causally, but not as a second support-expansion wave.}
$$

Equivalently:

- primary injection is **support-forming**,
- secondary re-injection is **support-revisiting**.

By the time the exact $k+16$ re-entry occurs, the reachable support manifold has already been activated by the primary wave. The second injection may still modulate amplitudes inside that active support, but it does not create a second measurable front of new state bits.

This sharpens the transport-horizon interpretation:

$$
\text{the probe is not merely noisy; the support has already been exhausted.}
$$

## 11. Probe L result: no strong amplitude bump inside saturated support

Probe L asks the next natural question: if re-injection does not create new support, does it at least create a strong amplitude change inside the support that already exists?

The answer is again no, at least for first-order support observables.

Averaged over all 16 source words, the secondary-to-baseline ratios are

$$
\overline{R_A}=0.9979,
\qquad
\overline{R_T}=1.0009,
\qquad
\overline{R_O}=0.9957,
\qquad
\overline{R_N}=0.0036.
$$

Thus:

- active support in the secondary window is essentially unchanged,
- mask-to-mask toggle activity is essentially unchanged,
- support overlap with the previous round is essentially unchanged,
- new support remains effectively zero.

So the secondary injection does **not** produce a strong second amplitude wave inside state space either. It acts, at most, as a low-contrast modulation inside an already saturated manifold.

## 12. Probe M result: no phase-locked support echo at lag $16$

A hidden secondary layer might still have appeared as a phase-selective echo even if amplitude and support-growth probes were flat. Probe M tested this directly by asking whether the round-$r$ primary support mask resembles the round-$(r+16)$ mask more than nearby control lags.

The aggregate lag-$16$ advantages are

$$
\overline{\Delta J_{16}}=0.000333,
\qquad
\overline{\Delta C_{16}}=0.000121.
$$

Only $2/16$ words have a Jaccard peak exactly at lag $16$, and only $1/16$ have a cosine peak exactly at lag $16$.

Therefore no clean phase-locked support echo is visible at the reinjection scale under mask-similarity probes either.

The state-space conclusion after Probes J–M is now robust across four observable classes:

1. carry-delta amplitude,
2. cumulative new support,
3. amplitude-inside-support ratios,
4. lag-selective support similarity.

All four fail to reveal a second transport-visible wave at $k+16$.

## 13. Probe N result: the hidden second stage is real in schedule space

Probe N changes basis completely. Instead of asking whether reinjection is visible after it has passed through a saturated compression state, it measures the schedule itself.

For each source word $W[k]$, the direct echo amplitudes in schedule space are measured at the analytically predicted positions $t=k$, $t=k+16$, $t=k+32$, and $t=k+48$.

The mean schedule-space XOR-Hamming weights are

$$
\overline{H(t=k)}=1.000,
$$

$$
\overline{H(t=k+16)}=4.910,
$$

$$
\overline{H(t=k+32)}=15.945,
$$

$$
\overline{H(t=k+48)}=16.107.
$$

The corresponding nonzero incidences are all exactly

$$
\overline{P(t=k)}=
\overline{P(t=k+16)}=
\overline{P(t=k+32)}=
\overline{P(t=k+48)}=1.000.
$$

So the hidden second stage is not hypothetical. It is directly visible in schedule space.

Moreover, the local secondary peak occurs near the predicted $k+16$ window with mean absolute peak error

$$
\overline{|\delta r_{\mathrm{sec}}|}=1.0 \text{ round}.
$$

The per-word secondary echo is weak for early words and rises sharply near the tail of the 16-word window, for example:

$$
H_{W[0]}(k+16)\approx 1.688,
\qquad
H_{W[10]}(k+16)\approx 6.250,
\qquad
H_{W[14]}(k+16)\approx 16.875,
\qquad
H_{W[15]}(k+16)\approx 15.938.
$$

This reveals the real split:

$$
\text{schedule space: reinjection is directly visible}
$$

$$
\text{state space: reinjection is mostly compressed below current transport-visible thresholds.}
$$

The state interface, not the schedule itself, is the bottleneck.


## 14. Probe P result: recursive path multiplicity explains the tail turn-on

Probe N left one sharp question unresolved: why does the direct second-stage schedule echo at $t=k+16$ remain small for $W[0]\dots W[8]$, jump at $W[9]$, and then spike strongly at $W[14],W[15]$?

A local landing-site hypothesis was tested and rejected: the tail is **not** explained by the carry/borrow susceptibility of the landing word $W[k+16]$ alone. The correct explanation is **recursive path multiplicity** in the schedule graph.

Define the path-multiplicity matrix $P_{i,k}$ by

$$
P_{i,k} = \delta_{ik}, \qquad 0 \le i < 16,
$$

$$
P_{i,k} = P_{i-2,k} + P_{i-7,k} + P_{i-15,k} + P_{i-16,k}, \qquad 16 \le i < 64.
$$

Here $P_{i,k}$ counts the number of syntactic dependency paths by which input word $W[k]$ reaches schedule word $W[i]$.

It is also useful to define the dependency-set recurrence

$$
D_i = \{i\}, \qquad 0 \le i < 16,
$$

$$
D_i = D_{i-2} \cup D_{i-7} \cup D_{i-15} \cup D_{i-16}, \qquad 16 \le i < 64,
$$

so that the immediate-parent hit count for the direct second-stage landing site is

$$
H_k = \mathbf{1}_{k \in D_{k+14}} + \mathbf{1}_{k \in D_{k+9}} + \mathbf{1}_{k \in D_{k+1}} + \mathbf{1}_{k \in D_k}.
$$

The measured $t=k+16$ secondary response falls into three clean regimes:

- $W[0]\dots W[8]$: $H_k=1$ and $P_{k+16,k}=1$
- $W[9]\dots W[13]$: $H_k=3$ and $P_{k+16,k}=3$
- $W[14],W[15]$: $H_k=3$ and $P_{k+16,k}=5$

The corresponding measured secondary schedule-space XOR-Hamming responses are:

$$
H_{\mathrm{sec}}(W[0]) \approx 1.688,
\qquad
H_{\mathrm{sec}}(W[9]) \approx 5.156,
\qquad
H_{\mathrm{sec}}(W[14]) \approx 16.875,
\qquad
H_{\mathrm{sec}}(W[15]) \approx 15.938.
$$

The correlation between measured secondary Hamming response and total path multiplicity is

$$
\rho\bigl(H_{\mathrm{sec}},P_{k+16,k}\bigr) \approx 0.948957,
$$

while the correlation with the simpler immediate-parent hit count is

$$
\rho\bigl(H_{\mathrm{sec}},H_k\bigr) \approx 0.729272.
$$

So the tail turn-on is not a local landing-site phenomenon. It is a **multi-path recursive echo**.

The corrected interpretation is therefore:

$$
W[k] \to W[k+16]
$$

is weak and single-path for early words, but becomes recursively amplified once the parent terms $W[k+14]$ and $W[k+9]$ themselves begin to carry $W[k]$.

This gives the first explicit evidence that the schedule is not only temporally staggered but also **branching in path count**.
## 15. Complete transport geometry model

The complete model through Probe P is:

### 15.1 Inside a block: position is time

Within one block,

$$
\text{word index }k = \text{injection time}.
$$

That identity creates three direct observables:

1. **Early energy**

   $$
   E_{\mathrm{early}}(k)\approx 105.27-7.865\,k
   $$

   over the interior regime, with boundary-layer correction near $k\ge 13$.

2. **Wavefront/saturation**

   $$
   r_{\mathrm{sat}}(k)\approx k+5.
   $$

3. **Carry timing**

   $$
   \Gamma(k)\approx \Gamma_0 + 0.4648\,k.
   $$

### 15.2 Across the block boundary: time is reset

Through the chaining state, all eight state words are injected simultaneously at round $0$, so schedule-position observables are reset:

$$
\partial_k E_{\mathrm{early}}^{(\mathrm{cross})}\approx 0,
\qquad
\partial_k \Gamma^{(\mathrm{cross})}\approx 0.
$$

The boundary preserves magnitude but destroys word-position timing in the measured state-space observables.

### 15.3 Below the word scale: no stagger, no gradient

Bits inside a word enter simultaneously at round $k$, so there is no word-like gradient inside $W[k]$:

$$
\partial_b E_{\mathrm{early}}(k,b)\approx 0,
\qquad
\partial_b \Gamma(k,b)\approx 0
$$

up to unstable data-dependent arithmetic noise.

### 15.4 Re-injection after saturation: branching schedule echoes, one transport-visible state stage

The schedule is a multi-stage injector in the causal graph. However, only the first stage is transport-visible in state space under the present probes:

$$
W[k]\xrightarrow{\;k\;}\text{support growth in state space},
$$

$$
W[k]\xrightarrow{\;k+16\;}\text{schedule-visible revisitation with path multiplicity }P_{k+16,k},
$$

$$
W[k]\xrightarrow{\;k+32\;}\text{strong schedule-space echo},
$$

$$
W[k]\xrightarrow{\;k+48\;}\text{strong schedule-space echo}.
$$

The second-stage echo is therefore governed by two distinct mechanisms:

1. **temporal offset**: the direct $W[i-16]$ term guarantees re-entry exactly $16$ rounds later;
2. **graph branching**: the amplitude of that re-entry depends on how many recursive schedule paths connect $W[k]$ to $W[k+16]$.

Thus the correct distinction is:

- **primary injection** is support-forming and transport-visible in state space,
- **secondary and later injections** are schedule-visible and branch-amplified in $W$-space,
- **late secondary amplification** is governed by path multiplicity rather than by a new state-space transport law.

## 16. Consolidated results table

| Observable | Direct slope / level | $r$ | Cross / secondary result | $r$ | Interpretation |
|---|---:|---:|---:|---:|---|
| Early energy, $W[0..11]$ | $-7.921$ bits/word | $-0.9998$ | cross: $-0.0632$ bits/word | $-0.3679$ | direct word-level gradient, boundary reset |
| Saturation round, $W[0..15]$ | $+0.9991$ rounds/word | $0.9998$ | cross: all words active immediately | — | $k+5$ law |
| Carry centroid, $W[0..15]$ | $+0.4648$ rounds/word | $0.9817$ | cross approximately flat | — | timing channel inside block |
| Bit-scale early energy | $\approx 0$ bits/bit | $|r|<0.43$ | — | — | no bit-level gradient |
| Bit-scale carry centroid | $\approx 0$ rounds/bit | $|r|<0.32$ | — | — | no bit-level timing gradient |
| Probe J carry SNR | — | — | $\overline{\mathrm{SNR}}^{(\mathrm{carry})}=1.041$ | — | no resolved secondary state-space wave |
| Probe K new-support SNR | — | — | $\overline{\mathrm{SNR}}^{(\mathrm{new})}=0.004$ | — | no second support-growth wave |
| Probe L active/toggle/overlap ratios | — | — | all approximately $1$, with $\overline{R_N}=0.0036$ | — | no strong amplitude bump inside support |
| Probe M lag-16 advantage | — | — | $\overline{\Delta J_{16}}=0.000333$, $\overline{\Delta C_{16}}=0.000121$ | — | no phase-locked support echo |
| Probe N schedule-space echoes | $H(k)=1.000$ | — | $H(k+16)=4.910$, $H(k+32)=15.945$, $H(k+48)=16.107$ | — | hidden second stage is real in $W$-space |
| Probe P path-multiplicity law | $\rho(H_{\mathrm{sec}},P_{k+16,k})=0.948957$ | — | $\rho(H_{\mathrm{sec}},H_k)=0.729272$ | — | late $k+16$ tail is recursive branching, not landing-site arithmetic |

## 17. Reproducibility

All measurements across Probes A–P are produced by deterministic Python scripts requiring only NumPy. All numbers are computed fresh at runtime from the raw compression core or directly from the expanded schedule. No cached values are assumed.

The probe family is now:

| Probe | Scope | New result |
|---|---|---|
| A, B, C | direct / cross block, 256 bits | early-energy gradient, boundary reset |
| D | analytical | first-entry law |
| E | 64-round wavefront | $k+5$ saturation law |
| F | carry timing | carry-centroid gradient |
| G | bit scale | no bit-level gradient |
| H | analytical | injection simultaneity principle |
| I | 512-bit full 16-word scan | boundary layer and full-window fit |
| J | carry-delta reinjection | transport horizon |
| K | cumulative new support | no second support-growth wave |
| L | inside-support amplitude | no strong secondary amplitude bump |
| M | lag-$16$ support similarity | no phase-locked support echo |
| N | schedule-space echo scan | direct visibility of secondary and later echoes |
| O | local landing-site arithmetic test | falsified as complete explanation of the tail |
| P | schedule-path multiplicity scan | secondary tail turn-on explained by recursive path count |

## 18. Conclusions

The complete solution through Probe P is:

1. **The only native transport gradient in SHA-256 state space is the word-level schedule.**
2. **A gradient exists in state space if and only if injection is temporally staggered.**
3. **The block boundary is a reset of measured schedule-position observables, not of perturbation magnitude.**
4. **The schedule re-injects each input word at rounds $k+16$, $k+32$, and $k+48$ causally and measurably in schedule space.**
5. **Only the first injection is transport-visible in state space under the present probes.**
6. **Primary injection builds support; later injections revisit and modulate an already saturated support manifold.**
7. **The late $k+16$ schedule tail is governed by recursive path multiplicity, not by local landing-site arithmetic alone.**

The resulting transport hierarchy is:

| Scale | Injection type | Temporal stagger? | Gradient in state space? | Observable outcome |
|---|---|---:|---:|---|
| Block boundary | chaining state | No | No | magnitude survives, position erased |
| Word level, first entry | schedule | Yes | Yes | energy, wavefront, carry-timing gradients |
| Bit level | within-word | No | No | data-dependent noise only |
| Schedule re-entry | $k+16$, $k+32$, $k+48$ | Yes in schedule space | not resolved as a second state-space wave | causal revisitation below current state-space threshold; late $k+16$ tail scales with path multiplicity |

## 19. Open questions

1. **General branching law beyond $k+16$**  
   Probe P explains the secondary tail using path multiplicity $P_{k+16,k}$. Does the same recurrence predict the tertiary and quaternary echoes at $k+32$ and $k+48$ quantitatively?

2. **Exact state-interface bottleneck**  
   What map from schedule perturbation to state perturbation compresses the strong $W$-space echoes into state-subcritical modulation after saturation?

3. **Tertiary and quaternary state visibility**  
   Since $W[k]\to W[k+32]\to W[k+48]$ is strong in schedule space, can any higher-order observable recover those later echoes in state space?

4. **Second-order differential probe**  
   Compare perturbations in $W[k]$ and $W[k+16]$ directly to isolate the shared causal pathway while subtracting the saturated baseline.

5. **Sub-saturation probe design**  
   Reduce primary saturation so that the $k+16$ event enters a less-saturated state and may become directly resolvable in state space.

6. **Multi-block accumulation**  
   Determine whether $3+$ block chains allow schedule-structured information to re-emerge after repeated chaining.

7. **Closed-form path-count asymptotics**  
   Derive analytic formulas or bounds for $P_{i,k}$ near the tail of the schedule window, and relate them to the measured secondary Hamming amplitudes.