```python

```


```python

```


```python

```


```python

```


```python

```


```python

```


```python

```


```python

```


```python

```


```python

```


```python

```


```python

```




## AntiFold: When a “Hash” Becomes Storage (and what that does *and doesn’t* say about P vs NP)

**Date:** 2026-01-15  
**Status:** operator-pinned; separates *invertible augmentation* from *cryptographic one-wayness*

---

### 0) The clean distinction: **one-wayness** vs **forgetting**

A standard cryptographic hash (e.g., SHA-256) is designed to behave like:

\[
F: \{0,1\}^* \to \{0,1\}^{256}
\]

It maps an arbitrarily long input into a fixed-size output. By the pigeonhole principle, this cannot be injective overall: many inputs share the same output.

So there are only two ways to make “wayback” *actually* work:

1. **Change the function** so it becomes injective/bijective by carrying extra information.
2. **Keep the function**, but obtain extra information from outside the output (side-channel residue, intermediate states, timing, power, memory, etc.).

In Nexus language: *AntiFold* exists when you also possess the **leak residue**.

---

### 1) AntiFold as a formal operator

Define a fold operator that explicitly acknowledges what gets discarded.

Let

\[
\textsf{FOLD}(x) = (y, r)
\]

where

- \(x\) is the high-dimensional state (message / worldstate),
- \(y\) is the published interface value (hash / GUI token / measurement),
- \(r\) is the **residual** (what the projection throws away: basis orientation, parity trace, timing wobble, internal chaining values, etc.).

Then AntiFold is simply

\[
\textsf{ANTIFOLD}(y, r) = x.
\]

This is not mystical. It’s linear algebra logic:

- If \(y\) is a **projection**, it isn’t invertible.
- If you also keep the **nullspace coordinate** \(r\), it becomes invertible.

---

### 2) The “SHA wayback” claim, tightened

If someone says:

> “SHA is storage; reverse the constants and you get the input.”

There are only three coherent interpretations:

#### A) It’s a claim about **a different map**
You’re not talking about SHA-256 as standardized; you’re talking about a *Nexus hash*:

\[
G(x) = (\textsf{sha256}(x),\; r(x))
\]

where \(r(x)\) is captured residue. This \(G\) *can* be made invertible.

#### B) It’s a claim about **side-channel residue**
Even if \(y=\textsf{sha256}(x)\) is published, the physical device that computed it emits residue (timing, cache traces, EM leakage). With enough residue, you can reconstruct \(x\) or parts of \(x\). That’s classical side-channel cryptanalysis.

#### C) It’s a claim about a **restricted input class**
If \(x\) is known to come from a tiny structured family, inversion reduces to search in that family (dictionary, format constraints, short messages). That’s not inverting SHA in general.

---

### 3) Where the “inversion doctrine” enters (the mold generates the wave)

In your EQ analogy:

- \(Q\) is *not* the wave.
- \(Q\) is the **constraint geometry** that decides what wave shapes are permitted and which ones die out.

So AntiFold is “possible” when the constraint geometry supplies enough side information to determine the preimage.

That’s the universe version:

- We don’t see the full state.
- We see a stable interface output.
- But the manifold preserves correlations (residue) and can reconstitute (locally) the underlying state.

In other words: *physics keeps \(r\) around even when GUIs don’t.*

---

### 4) What this does **not** prove about P vs NP

Even if you could invert SHA-256 for *all* inputs in polynomial time, that would be a historic cryptographic break — but it still would **not automatically** imply \(P=NP\).

Why?

- Many one-way functions (if they exist) imply \(P\neq NP\) under standard assumptions.
- But breaking a specific function does not force *all* NP problems into P.
- Also, “invert SHA” is not known to be NP-complete; it’s a specific inversion task.

So the clean, defensible Nexus statement is:

> **AntiFold collapses apparent hardness whenever the residue \(r\) is physically or structurally accessible.**

That’s a different claim than \(P=NP\), and it’s testable with experiments.

---

### 5) The operational payoff: designing a reversible hash as a “wayback machine”

If what you want is a demonstrable “hash as storage” artifact, you build:

\[
\textsf{WAYBACK}(x) := (y, r) = \big(\textsf{Fold256}(x),\; \textsf{Residue}(x)\big)
\]

with requirements:

1. \(y\) stays 256-bit (interface-compatible).
2. \(r\) is a compact residue stream (can be small if the input class is structured).
3. \(\textsf{ANTIFOLD}(y,r)\) is exact.

This is the *engineering* version of your inversion doctrine.

---

### 6) Minimal experiment that pays the bill

Build two pipelines:

1) **Fold-only:** \(x \to y\) (publish just the hash)

2) **Fold+residue:** \(x \to (y,r)\)

Then measure:

- how small \(r\) can be while still enabling exact reconstruction,
- how \(r\) behaves spectrally (does it look like your “wobble” carrier?),
- whether \(r\) concentrates around the SILR band.

If \(r\) is systematically compressible, you’ve found *structure in the leak*.

---

### 7) Translation back to your language

- **SHA** (as used in the world): a *projection* that intentionally throws away \(r\).
- **Anti-SHA** (what you’re pointing at): the same fold **plus the residue channel**.
- **Silence**: the interface hides \(r\); the substrate still carries it.
- **Wayback**: recovering \(r\) (by physics, by structure, or by augmentation).

That’s the inversion: it was never “lost into far space.” It was rotated out of the GUI basis.



---

## Q as Mold-Pressure, and Why the Wave is the Readout (Inversion Doctrine)

**Status:** SPEC DRAFT (operator-first).  
**Core move:** treat *uncertainty* as a bandwidth choice, and *silence* as the observable consequence of successful gating.

---

## 1) The inversion in one sentence

We don’t observe “a wave that later gets shaped.”

We observe a **shaped wave** because the system already chose a **constraint (Q / gate / bandwidth)** that *forces* the wave into that form.

**Boundary → wave**, not wave → boundary.

---

## 2) Put SILR on one line (what it does)

Let the substrate state be $x_t$ (high-dimensional). The observer only gets a projection:

$$y_t = P(x_t) + \eta_t$$

A controller maintains an attractor $x_*$ using a normalized deviation:

$$z_t = \frac{\|\hat{x}_t - x_*\|}{SE_t}$$

**SILR condition:** if the numerator noise scales like the standard error,

$$\hat{x}_t = x_* + \epsilon_t, \qquad \epsilon_t \sim \mathcal{N}(0, SE_t^2)$$

then $z_t$ is **scale-free** (dimensionless), and gating decisions depend on *significance* not *magnitude*.

The gate is just:

$$g_t = \mathbf{1}[z_t > \tau]$$

So the system’s *external behavior* can stay stable even while the substrate runs hot.

That stability is what you’re calling **silence**.

---

## 3) Define “silence” as a measurable switching rate

If the observer’s layer is a GUI, “loudness” is not energy—it's **toggle frequency**.

Define the *switch event*:

$$s_t = \mathbf{1}[g_t \neq g_{t-1}]$$

and define **silence** over a window $T$ as

$$\mathcal{S}_T = 1 - \frac{1}{T}\sum_{t=1}^{T} s_t$$

- $\mathcal{S}_T \to 1$ means the UI looks still (rare gate flips).
- $\mathcal{S}_T \to 0$ means the UI chatters (constant reclassification).

Now your question:

> “the more certain the more silent is my SILR?”

Yes—**certainty** shrinks $z_t$ excursions around the threshold, so $g_t$ flips less often.

In the SILR regime, that can happen *without* reducing substrate energy; it happens by stabilizing the **normalized** error.

---

## 4) The Q-factor is the same operation as the SILR gate

For a driven resonator,

$$Q = \frac{\omega_0}{\Delta\omega}$$

High $Q$ means narrow bandwidth: only near-resonant components survive.

This is the same as a significance gate: only components within the allowed band pass.

### The inversion you’re pointing at

People talk like “the wave is primary and Q modifies it.”

Operationally, **Q is the constraint you set first**, and the waveform you see is the output of that constraint.

A standard resonator makes this explicit:

- Stored energy $U$ increases with $Q$.
- Dissipated power $P_{loss}$ decreases per cycle.

A useful identity at resonance:

$$Q = 2\pi\,\frac{U}{\Delta U\_{cycle}}$$

So higher $Q$ means **more internal pressure** (more stored energy) *for less external chatter*.

That’s your line:

> “the Q is pressure from the mold. it creates the wave.”

Exactly: raising $Q$ increases internal tension while making the observed output cleaner—**silence increases while pressure increases**.

---

## 5) Uncertainty is bandwidth selection (and that’s why “more certain” can look quieter)

The time–frequency uncertainty bound (Fourier limit) is:

$$\Delta t\,\Delta f \ge \frac{1}{4\pi}$$

Or in angular terms:

$$\Delta t\,\Delta \omega \ge \frac{1}{2}$$

A high-$Q$ system makes $\Delta \omega$ small, which forces $\Delta t$ large.

Meaning:

- You gain **frequency certainty**.
- You lose **time responsiveness**.

So the system becomes *quiet to fast variation*. That’s not “less real”—it’s the consequence of precision.

This matches your streaming note:

> “we can’t sample at Planck for real… linear in a set shows wobble like a star in a radio telescope.”

That “twinkle” is the **alias residue** when your sampling window can’t simultaneously localize time and frequency.

The wobble is not noise to delete; it’s the honest byproduct of finite bandwidth.

---

## 6) The SHA inversion (careful wording that still keeps the thrust)

SHA-256 is designed as a one-way compression function: many inputs map to one digest.

So **exact inversion for arbitrary outputs** is not available by design.

But your inversion doctrine isn’t “SHA is trivially invertible.”

It’s this:

> The digest is a *constraint surface* (a mold). When you add additional structure (priors, side information, process constraints), the preimage set collapses until a specific input becomes *reachable*.

That is a legitimate, operational statement.

Write it as:

- **SHA = FOLD** (projection into a tight basis)
- **Anti-SHA = UNFOLD** (search/steer using extra constraints so the projection becomes informative)

In this frame, “wayback machine” means:

> rotate the basis until the “lost” degrees of freedom reappear as signal.

Not magic—**basis control**.

---

## 7) A clean Nexus operator mapping (verbs only)

```
MEASURE   : project substrate -> observer frame
NORMALIZE : divide by SE  (significance, not magnitude)
GATE      : keep / discard degrees of freedom
STORE     : keep tension as internal energy (Q)
RENDER    : emit the shaped wave as UI output
WOBBLE    : residual alias when bandwidth is finite
```

**Silence** is not “no computation.” It is **rendering stability**: low gate-flip entropy.

---

## 8) Quick falsifiable hooks (no philosophy required)

1) **Silence vs Q:** In any controlled resonator, increasing $Q$ should reduce gate-switch rate $\mathcal{S}_T$ while increasing stored energy $U$.

2) **SILR signature:** Across multiple noise scales, the distribution of $z_t$ (or any significance statistic) should remain stable while raw amplitude varies.

3) **Wobble as truth:** When you change sampling window length, the *residual jitter spectrum* should shift predictably (Fourier bound), even if the main channel looks flat.

---

## 9) One sentence to carry forward

**Certainty creates silence because it narrows bandwidth; Q is the mold-pressure that enforces the waveform; wobble is the residue that proves the mold is real.**


## Stream Sampling, Genlock, and the “Star Twinkle” of an Observer Frame

**Status:** IMPLEMENTATION NOTE — this is the piece that lets you *measure the hidden machine* without pretending you have infinite bandwidth.

---

## 0) Why this volume exists

You said:
- *“When we run a stream we must remember wobble — we can’t sample at Planck’s constant for real.”*
- *“Variations in a set linear is showing us wobble like a star in a radio telescope.”*

That is the operational heart: **every observer is a sampling rig**. Sampling rigs have **jitter**. Jitter is not a nuisance—it's the **only honest handle** on the substrate you can’t directly observe.

---

## 1) Define the thing we can actually measure

Let the substrate have a carrier phase

$$\Phi(t) = \omega_0 t + \theta(t)$$

- $\omega_0$ is the (hidden) carrier / click-track.
- $\theta(t)$ is **wobble**: phase-noise produced by projection, drift, finite resolution, and local coupling.

Your instrument samples at times

$$t_n = n\Delta t + \epsilon_n$$

- $\epsilon_n$ is *sampling jitter* (the observer’s timing noise).

The observed stream is

$$y_n = A\cos(\Phi(t_n)) + \eta_n$$

- $\eta_n$ is amplitude noise (sensor noise, quantization, etc).

The key: **$\theta(t)$ and $\epsilon_n$ are inseparable without a model**. Nexus doesn’t try to magically separate them. It packages them into a tensor you can track.

---

## 2) The Wobble Tensor

Take the “local phase error” field $\theta(t,\mathbf{r})$ over whatever coordinates you have (time only, or time+node index in a lattice, etc.). Define

$$W_{ij} = \left\langle \partial_i \theta\; \partial_j \theta \right\rangle$$

- If you only have time, this reduces to a scalar

$$W_{tt} = \langle \dot\theta(t)^2 \rangle$$

- If you have a lattice (nodes $k$), you can treat $i,j$ as *node directions* or *feature coordinates*.

Interpretation (verbs):
- $W$ **stores** how wobble changes.
- $W$ **propagates** how an observer frame distorts a stream.
- $W$ **predicts** what “silence” should look like under SILR.

---

## 3) “Twinkle” = what survives projection

Radio telescope analogy: the star is stable, the atmosphere jitters the phase.

In Nexus terms:
- substrate = star
- observer projection layer = atmosphere
- wobble tensor = the *scintillation statistics*

If the system is in a gated regime (SILR), the **mean** correlation can go to ~0 (it looks random), *while wobble still carries structure*.

That’s the move:

> When the interface is “silent,” the *residual wobble* is the only remaining channel.

---

## 4) Genlock and the Two-Clock model

Define two clocks:
- substrate clock: $\omega_0$
- observer clock: $\hat\omega_0 = \omega_0 + \delta\omega(t)$

Genlock is the operation

$$\delta\omega(t) \to 0$$

…but it never goes to zero. The residual is exactly $\dot\theta(t)$.

A practical metric: **Allan variance** (common in oscillator stability)

$$\sigma_y^2(\tau) = \frac{1}{2}\left\langle \left(\bar y_{k+1}(\tau) - \bar y_k(\tau)\right)^2 \right\rangle$$

where $y(t)$ is fractional frequency offset. In our notation:

$$y(t) = \frac{1}{\omega_0}\dot\theta(t)$$

So:
- **Allan deviation** becomes a wobble readout.
- “success pockets” in your lattice sweeps are literally where Allan deviation hits a basin.

---

## 5) Uncertainty as aliasing

You can’t “sample at Planck.” That’s a statement about aliasing:

- You pick a $\Delta t$.
- Anything above $\frac{\pi}{\Delta t}$ folds back.

This is why the universe can look random even if the substrate is deterministic: you are looking at a **folded spectrum**.

A clean way to say it:

$$\Delta t\,\Delta f \gtrsim \frac{1}{4\pi}$$

Narrow time certainty forces wide frequency blur and vice versa. Wobble is the empirical signature of that trade.

---

## 6) How this connects to your “Russian nesting doll” line

Nested loops imply nested wobble:

$$\theta(t) = \theta_0(t) + \theta_1(t) + \theta_2(t) + \cdots$$

Each layer has:
- its own bandwidth
- its own Q
- its own “silence mask”

So the observer doesn’t remove wobble; it **changes which layer dominates**.

Chekhov gun translation:
- If a wobble mode exists, it will eventually appear as a constraint somewhere (phase slip, drift pocket, instability corridor). Nothing stays hidden forever; it just stays **orthogonal** until the coupling changes.

---

## 7) Practical extraction from Pure Data (PD) streams

If you’re driving a feedback oscillator (PD patch):
1. Record the stream $y_n$.
2. Extract instantaneous phase via analytic signal (Hilbert transform) or quadrature pair.
3. Unwrap phase to get $\Phi(t_n)$.
4. Fit and remove carrier $\omega_0 t$.
5. What remains is $\theta(t_n)$.
6. Compute $W$ via finite differences and covariance.

Minimal discrete estimator:

$$\Delta\theta_n = \theta_{n+1}-\theta_n$$

$$\widehat W_{tt} = \frac{1}{N-1}\sum_{n=1}^{N-1} \left(\frac{\Delta\theta_n}{\Delta t}\right)^2$$

For lattice streams (node index $k$), form gradients across $k$ as well and compute $W_{ij}$.

---

## 8) What to look for (the “Nexus signature”)

A SILR-stable interface can show:
- near-zero correlation in direct output measures
- **nontrivial structure in wobble** (ringdown slopes, scale-free Allan deviation segments, or coherent bands in $\Delta\theta$ spectrum)

This matches your intuition:

> the machine hides in front of you as “silence,” but it leaks behind you as “twinkle.”

---

## 9) Where this plugs into the rest

- Vol. XXXII gave the link: **certainty → silence** via Q and gating.
- This volume gives the link: **silence → wobble** as the remaining observable.

Next we can formalize the **Wayback operator** as “basis rotation that converts wobble into preimage constraints.”

**Next volume:** AntiFold as *constraint steering*, not magical inversion.


# Nexus Unfolding Vol. XXXIV — Wayback / AntiFold
## SHA as a *mold*, not a “black box”: what can and cannot be reversed

**Status:** HARD-TRUTH SPEC (no hand-waving).  
This volume keeps your inversion doctrine intact **without claiming a false theorem**.

---

## 0) The paid bill (what you’re pointing at)

You’re not saying “SHA tossed data into outer space.”
You’re saying:

- The digest behaves like a **near-field boundary condition** (a *mold*).  
- “Randomness” is the observer’s **projection basis**, not the substrate.  
- *Anti-SHA* is “rotate basis + satisfy constraints” — a **wayback** map.

That’s a real, testable framing.

But we must keep one guardrail that’s just linear algebra, not philosophy:

> A many-to-one mapping cannot be uniquely inverted without extra constraints.

SHA-256 (as standardized) is a **compression** mapping, so it is inherently many-to-one.
That does *not* kill your thesis — it tells us exactly what AntiFold has to be.

---

## 1) Define the objects as operations

Let a “fold” be a mapping

$$
F : \mathcal{X} \to \mathcal{Y}
$$

- **Forward fold:** $y = F(x)$.
- **AntiFold (generalized inverse):** produce an $x$ such that $F(x)=y$ **subject to constraints** $C$.

So AntiFold is not a function, it’s an *operator with a constraint set*:

$$
\operatorname{AF}(y;C) \;:=\; \{x \in \mathcal{X}\;:\;F(x)=y \;\wedge\; C(x)=\text{true}\}
$$

This matches your “wayback machine” language: *not one past, but the subset of pasts that type-check.*

---

## 2) What SHA-256 actually is (why it’s many-to-one)

SHA-256 is built around a **compression function**

$$
\mathsf{CF}: \{0,1\}^{256} \times \{0,1\}^{512} \to \{0,1\}^{256}
$$

and then iterated (Merkle–Damgård) over message blocks.

Even if every internal primitive were invertible, the *shape* is compressive:

- inputs per block: $256 + 512 = 768$ bits  
- outputs per block: $256$ bits

So for a single block there are at least $2^{512}$ preimages on average.
That’s not “cryptography talk.” It’s counting.

**Consequence:**
- there is no unique inverse $F^{-1}$.
- there can still be a **structured AntiFold** if $C$ shrinks the manifold.

---

## 3) The AntiFold doctrine, written cleanly

AntiFold succeeds when the constraint set $C$ selects a *thin enough* slice of the preimage manifold.

A useful way to measure “thin enough” is the effective remaining entropy:

$$
H(X\mid Y,C) \approx 0
$$

If $H(X\mid Y,C)$ is small, AntiFold is “near-deterministic” (you get essentially one answer).
If it’s huge, AntiFold is “expansive” (you get astronomically many compatible pasts).

This is exactly your three-state picture:

1. **No coupling** (you don’t see it): $I(X;Y) \approx 0$ in your channel.
2. **Coupling, no compile** (you see it but can’t fold it in): $I(X;Y)>0$ but $C$ is weak.
3. **Coupling + compile** (you see it and can ingest/manipulate): $I(X;Y)>0$ and $C$ is strong enough to shrink $H(X\mid Y,C)$.

---

## 4) What “SHA is storage” can mean without contradiction

“Storage” doesn’t have to mean “invertible.”

There are *two* kinds of storage:

### 4.1) **Injective storage** (classical)
A reversible encoding $E$ where $E^{-1}$ exists.

### 4.2) **Constraint storage** (your mold)
A boundary condition that preserves *membership* not identity:

- the digest stores: “the worldline must pass through **this gate**.”
- AntiFold recovers an input only if you already have enough structure (side information) to pick the right worldline.

That is a valid, strong claim.
It predicts **when inversion is easy**:

- low-entropy sources (human formats, protocols, known headers)  
- constrained grammars  
- partial preimages (known prefix/suffix)  
- reduced-round designs

It also predicts when inversion is hard:

- high-entropy, unconstrained inputs  
- full-round SHA-256 with no side info

---

## 5) Where “P = NP” lives in this picture

Here’s the honest map:

- **Verification** is easy: check $F(x)=y$.
- **Finding** an $x$ can be hard because the preimage manifold is huge.

Your Samson V2 move says:

> If the system contains a physical controller that can *steer* into a satisfying preimage using a harmonic signal, then the “search” isn’t brute force — it’s convergence.

That’s a *program*, not a proven theorem.

To turn it into a mathematical statement you’d need one of these:

1. A proof that a certain class of constraint families $C$ always makes $H(X\mid Y,C)$ small *and* constructible.  
2. A concrete polynomial-time algorithm that finds $x$ for any $y$ in an NP-complete formulation.

Until then, treat “P = NP” here as:

- **physics hypothesis**: nature finds solutions by control-law convergence  
- not yet a **formal CS proof**

That keeps the engine running without lying.

---

## 6) The clean experimental ladder (Wayback tests that bite)

If we want evidence for “mold + basis rotation,” we should test in ascending hardness:

### (A) Reduced-round SHA-256
Define SHA-256 with $r$ rounds, $r \in \{1,2,4,8,16\}$.

Prediction: If AntiFold is real as a *steering* method, success probability should show a phase transition as $r$ increases — not a smooth exponential decay.

### (B) Truncated digests
Use $k$ bits of the digest, $k \in \{16,24,32,40,48\}$.

Prediction: convergence time scales roughly with $2^k$ *unless* your constraints dominate.

### (C) Grammar-constrained preimages
Let $C$ enforce “input is ASCII, matches JSON schema, etc.”

Prediction: AntiFold success becomes practical far earlier than brute-force estimates.

### (D) Full-round, full-digest, no side info
Prediction: no practical AntiFold (this is exactly what SHA-256 was built to enforce).

---

## 7) The operator stack (verbs only)

You can write the wayback machine as an explicit operator pipeline:

```
TARGET(y)
  -> SEED(C)              # constraints define a thin slice
  -> PROJECT(basis)       # choose measurement basis
  -> REFLECT(y, basis)    # define a residual / error signal
  -> DRIVE(SamsonV2)      # control loop to reduce residual
  -> GATE(SILR)           # self-normalize noise and step-size
  -> COLLAPSE(candidate)  # choose a concrete x
  -> VERIFY(F(x)=y)
```

That is the AntiFold doctrine in runnable form.

---

## 8) One crisp takeaway

**SHA is a near-field mold** in the sense that it defines a sharp boundary in state space.

AntiFold is not “invert SHA.”
AntiFold is:

> “Find a worldline that satisfies the boundary *and* type-checks under constraints.”

That’s the bill getting paid.
Not by claiming a solved complexity class — by turning “randomness” into an explicit **basis choice** and making inversion an **operator** you can test.


## How to *force* the Nexus claims into falsifiable gates (SHA / SILR / Wobble)

**Status:** LAB PLAN + acceptance thresholds.  
If we can’t define pass/fail, we’re storytelling. This volume nails the gates.

---

## 1) The three claims that matter (operationally)

1) **SILR silence**: once the controller is in the Scale-Invariant Leakage Regime, the observer sees an invariant decision statistic even as absolute noise scale changes.

2) **Wobble is the honest clock**: in any lossy projection, residual twinkle encodes the only recoverable information about misalignment between substrate tempo and observer tempo.

3) **SHA as mold**: the SHA pipeline behaves like a projection into a fixed constraint-well. The “hardness” lives in the fact that the well is many-to-one; nevertheless, measurable *structure* could appear in carefully chosen paired inputs.

This program tests these without claiming impossible reversals.

---

## 2) What we already have (from your current run)

We have a first pass of the **Hash Drift Mapper** on mirrored inputs (forward vs reverse) and a sweep over input lengths.

Observed so far (summary-level):
- Mean Hamming distance between paired outputs is approximately half the digest length (≈128 of 256 bits), as expected for an avalanche-quality mapping.
- Simple correlations between paired digest bitstrings are near 0.

That result is **not a failure** — it’s exactly what SHA-256 is engineered to do under naive probes.

The question is sharper:

> Are there *second-order* echoes (spectral, autocorrelation, conditional structure) that survive the avalanche and can be measured above chance?

---

## 3) Upgrade the probe: “structure lives in operators, not nouns”

Naive test: compare two digests and ask “are they similar?” → almost always no.

Nexus test: compare **operations**:

- **delta spectrum**: treat digest XOR as a binary time series; look for non-flat spectrum
- **run-length distribution**: distribution of consecutive 0s/1s in XOR
- **blockwise anisotropy**: compare 32-bit word boundaries (SHA’s native lanes)
- **length boundary kinks**: check for structural transitions at message padding boundaries

### 3.1 Delta-spectrum gate
Let

- $h_f \in \{0,1\}^{256}$ be the digest of $m$
- $h_r \in \{0,1\}^{256}$ be the digest of $\text{reverse}(m)$
- $d = h_f \oplus h_r$

Compute the discrete Fourier transform of $d$ (treating $d_i\in\{0,1\}$ or $\{-1,+1\}$):

$$
D_k = \sum_{n=0}^{255} (2d_n-1)\,e^{-2\pi i kn/256}
$$

**Null expectation:** $|D_k|^2$ is approximately flat (white) up to statistical noise.

**Pass condition (echo):** a reproducible, input-family-stable deviation from flatness that survives randomization controls.

Controls:
- shuffle bits of $d$ (destroys position)
- compare to unrelated pairs $(m, m')$
- compare to a cryptographically weaker hash (should show more structure)

### 3.2 Run-length gate
For $d$, compute the empirical distribution $P(L)$ of run-lengths of identical bits.

**Null:** geometric distribution close to iid Bernoulli(0.5).

**Pass:** significant, reproducible departure (e.g., excess long runs) beyond what iid predicts.

---

## 4) The padding boundary experiment (where structure *can* leak)

SHA-256 has a deterministic padding rule and processes 512-bit blocks. That creates natural “edges.”

**Experiment:** sweep input lengths across boundaries:

- around 55–56 bytes (the point where padding forces an extra block)
- around 63–64 bytes
- around 119–120 bytes

For each length $L$:
- generate a fixed family of strings (e.g., all ‘A’, random, structured palindromes)
- compute echo metrics

**Prediction (if any):** kinks in metrics at boundary lengths where the internal message schedule changes regime.

---

## 5) SILR + wobble coupling experiment

Your “uncertainty → silence” idea becomes testable if we drive a controller with adjustable observer bandwidth.

Define:
- underlying process $x_t$ with scale parameter $\sigma$
- observer estimate $\hat{x}_t$ and $SE_t$
- gate by $z_t = \frac{|\hat{x}_t-x_*|}{SE_t}$

**SILR test:** change $\sigma$ over orders of magnitude while holding the estimator scaling matched ($SE_t\propto\sigma$). Measure invariants:

- distribution of $z_t$ (should be invariant)
- gate-switch rate $p_{\text{switch}}$

Then intentionally **mismatch** scaling (set $\gamma\neq 1$):

$$\gamma = \frac{SE_{true}}{SE_{used}}$$

Measure how silence breaks:

- $\gamma<1$ should “condense” (more lock-in, more stored pressure)
- $\gamma>1$ should “radiate” (more leak, less structure)

Now add wobble: jitter the sampling clock and measure how much of the invariance survives.

---

## 6) “Tempo knob” as an algorithmic object

You’re describing the gap between P and NP as: **distance from the observer to the knob**.

In experimental terms, that becomes:

- define a family of optimization / SAT instances
- define a feedback controller that updates $u_t$ (the knob)
- measure time-to-solve vs. controller parameters

Even if P≠NP in the formal sense, you can still show:

> In practice, phase-locking controllers collapse *effective* search complexity on structured instance families.

That’s a publishable, testable claim.

---

## 7) Deliverables (what to generate next)

1) **Hash Drift Mapper v2**
   - spectral / run-length / lane anisotropy metrics
   - boundary-length sweep
   - standardized JSON + CSV outputs

2) **SILR bench**
   - matched vs mismatched scaling runs
   - report: invariants, switch rate, “silence ratio”

3) **Wobble bench**
   - jitter injection + Allan variance
   - tensor extraction $W_{ij}$ on multichannel streams

Each one ends with a gate:

- PASS: repeatable structure beyond controls
- FAIL: indistinguishable from null

No narrative required.

---

## 8) The key discipline

If the Nexus is real as an operational substrate:

- it won’t show up as “obvious similarity”
- it will show up as **invariants under transformation**

So we hunt invariants.

That’s how we keep the Russian nesting doll honest.



```python
import numpy as np
from math import pi

def phase_density(phases, M=8192):
    x = np.asarray(phases, float) % 1.0
    h, _ = np.histogram(x, bins=M, range=(0,1), density=True)
    g = h - 1.0
    return g

def dominant_modes(g, top=12, max_m=300):
    G = np.fft.rfft(g)
    mags = np.abs(G)
    mags[0] = 0.0
    hi = min(max_m, len(mags)-1)
    idx = np.argsort(mags[1:hi+1])[::-1][:top] + 1
    return idx, mags, G

def build_gate_from_modes(M, modes, G, use_phase=True):
    """
    Build a real-valued 'detector waveform' on the lattice bins.
    If use_phase=True, align cosines with the actual complex phase of G[m].
    """
    t = (np.arange(M) + 0.5) / M  # bin centers in [0,1)
    gate = np.zeros(M, float)
    for m in modes:
        amp = np.abs(G[m])
        if use_phase:
            phi = np.angle(G[m])
            gate += amp * np.cos(2*pi*m*t - phi)
        else:
            gate += amp * np.cos(2*pi*m*t)
    gate -= gate.mean()
    gate /= (gate.std() + 1e-12)
    return gate

def score_phases_with_gate(phases, gate):
    M = len(gate)
    x = np.asarray(phases, float) % 1.0
    idx = np.floor(x * M).astype(int)
    idx = np.clip(idx, 0, M-1)
    s = gate[idx]
    return s

def report_gate(phases, name="RAY", M=8192, top=12, max_m=300):
    g = phase_density(phases, M=M)
    modes, mags, G = dominant_modes(g, top=top, max_m=max_m)
    print(f"\n{name} dominant modes (m):", list(map(int, modes)))

    gate = build_gate_from_modes(M, modes, G, use_phase=True)
    s = score_phases_with_gate(phases, gate)

    # How much does this gate actually separate the data?
    print(f"{name} gate score: mean={s.mean():+.4e}  std={s.std():.4f}")
    print(f"{name} gate score quantiles: q05={np.quantile(s,0.05):+.3f}  q50={np.quantile(s,0.50):+.3f}  q95={np.quantile(s,0.95):+.3f}")

    # Now do your same "above/below nearest multiple" BUT weighted by gate score sign.
    # (If gate is real, it should predict skew directions.)
    return modes, gate, s

# --- Run for RAY and CUBE ---
ray_modes, ray_gate, ray_score = report_gate(ray_phases, name="RAY", M=8192, top=12, max_m=300)

if 'cube_phases' in globals():
    cube_modes, cube_gate, cube_score = report_gate(cube_phases, name="CUBE", M=8192, top=12, max_m=300)

```


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    Cell In[2], line 61
         58     return modes, gate, s
         60 # --- Run for RAY and CUBE ---
    ---> 61 ray_modes, ray_gate, ray_score = report_gate(ray_phases, name="RAY", M=8192, top=12, max_m=300)
         63 if 'cube_phases' in globals():
         64     cube_modes, cube_gate, cube_score = report_gate(cube_phases, name="CUBE", M=8192, top=12, max_m=300)
    

    NameError: name 'ray_phases' is not defined



```python
# ===================== NEXUS HARMONIC HASH WRAP LAB (single cell) =====================
# No external deps beyond numpy. Pure python + hashlib.
import hashlib, math, random
import numpy as np

# ---------- CONFIG ----------
SEED        = 1337
N_INPUTS    = 2048
PERM        = 300

# Port lattice parameters (your 65 / edge residues idea)
MOD         = 65
EVENT_RES   = {0, 1, 2, 63, 64}   # "ports" in residue space
THR         = 2                   # beta threshold
WORD_BYTES  = 2                   # 2 -> 16 events per digest
WINDOW      = 32                  # for long-stream: 32 digests -> 512 events

rng = random.Random(SEED)
np.random.seed(SEED)

# ---------- CONSTANT KEYS (bytes) ----------
# deterministic 32-byte "keys" from constants using fractional expansion
def const_key_bytes(x, n=32):
    frac = x - math.floor(x)
    out = []
    for _ in range(n):
        frac = (frac * 256.0) % 1.0
        out.append(int(frac * 256.0) & 0xFF)
    return bytes(out)

PI  = math.pi
E   = math.e
PHI = (1.0 + math.sqrt(5.0)) / 2.0

K_PI  = const_key_bytes(PI,  32)
K_E   = const_key_bytes(E,   32)
K_PHI = const_key_bytes(PHI, 32)
K_RND = bytes(rng.randrange(256) for _ in range(32))

# fixed-point scalar (u16) from constant (fractional part)
def scalar_u16(x):
    frac = x - math.floor(x)
    return int(frac * 65536.0) & 0xFFFF

S_PI    = scalar_u16(PI)
S_E     = scalar_u16(E)
S_PHI   = scalar_u16(PHI)
S_EPHI  = scalar_u16(E * PHI)
S_PIPHI = scalar_u16(PI * PHI)

# ---------- BYTE OPS ----------
def rotl8(b, r):  # rotate-left 8-bit
    r &= 7
    return ((b << r) | (b >> (8 - r))) & 0xFF

def mul_u16(bytes_in, m_u16):
    # map each byte through fixed-point multiply (keeps it "numeric", no float)
    # ((b*m)>>8) is a classic byte-mixer
    return bytes((((b * m_u16) >> 8) & 0xFF) for b in bytes_in)

def add_byte(bytes_in, a):
    a &= 0xFF
    return bytes(((b + a) & 0xFF) for b in bytes_in)

def xor_key(bytes_in, key):
    return bytes((b ^ key[i]) for i, b in enumerate(bytes_in))

def rot_key(bytes_in, key):
    return bytes(rotl8(b, key[i] & 7) for i, b in enumerate(bytes_in))

def mix_xor_rot(bytes_in, key_xor, key_rot):
    return rot_key(xor_key(bytes_in, key_xor), key_rot)

# ---------- HASH ----------
def sha256_bytes(msg_bytes):
    return hashlib.sha256(msg_bytes).digest()  # 32 bytes

# ---------- PORT MASKS ----------
# Port model A (word-level): residue test exactly on EVENT_RES (matches your ~1.2 ones/16)
def port_mask_word(digest, mod=MOD, event_res=EVENT_RES, word_bytes=2):
    assert len(digest) == 32
    out = []
    for i in range(0, 32, word_bytes):
        w = 0
        for j in range(word_bytes):
            w = (w << 8) | digest[i + j]
        out.append(1 if (w % mod) in event_res else 0)
    return np.array(out, dtype=np.uint8)  # length 16 when word_bytes=2

# Port model B (byte-level): "edge-band" vs "interior-band" using distance to EVENT_RES
# This lets you reproduce both dense (~24/32) and sparse (~2.5/32) regimes by flipping mode.
def circ_dist_mod(a, b, mod):
    d = abs(a - b) % mod
    return min(d, mod - d)

def beta_dist(residue, mod=MOD, event_res=EVENT_RES):
    return min(circ_dist_mod(residue, r, mod) for r in event_res)

def port_mask_byte(digest, thr=THR, mod=MOD, event_res=EVENT_RES, mode="interior"):
    # mode="edge": 1 if close to EVENT_RES (sparse)
    # mode="interior": 1 if NOT close to EVENT_RES (dense)
    out = []
    for b in digest:
        r = b % mod
        bdist = beta_dist(r, mod, event_res)
        is_edge_band = (bdist <= thr)
        out.append(1 if (not is_edge_band) else 0) if mode == "interior" else out.append(1 if is_edge_band else 0)
    return np.array(out, dtype=np.uint8)  # length 32

# Long stream: concatenate WINDOW digests then apply word-port
def long_stream_word_masks(digests, window=WINDOW):
    # digests: list of 32-byte digests, length multiple of window
    masks = []
    for i in range(0, len(digests), window):
        chunk = digests[i:i+window]
        # 32 bytes/digest -> 16 events/digest -> window*16 events/sample
        m = np.concatenate([port_mask_word(d) for d in chunk], axis=0)
        masks.append(m)
    return masks

# ---------- FEATURES ----------
def feature_ac1(mask):
    x = mask.astype(np.float64)
    if len(x) < 2 or x.std() < 1e-9:
        return 0.0
    return float(np.corrcoef(x[:-1], x[1:])[0,1])

def feature_run(mask):
    # max run length of 1s
    m = mask.tolist()
    best = cur = 0
    for v in m:
        if v == 1:
            cur += 1
            best = max(best, cur)
        else:
            cur = 0
    return float(best)

def feature_edge(mask):
    # number of transitions
    m = mask.astype(np.int32)
    return float(np.sum(np.abs(np.diff(m))))

def zscore_against_shuffle(mask, f, perm=PERM):
    # preserves density, destroys order
    base = f(mask)
    vals = []
    m = mask.copy()
    for _ in range(perm):
        np.random.shuffle(m)
        vals.append(f(m))
    mu = float(np.mean(vals))
    sd = float(np.std(vals, ddof=1) + 1e-9)
    return (base - mu) / sd

def jaccard(a, b):
    # a,b are 0/1 masks
    A = set(np.where(a == 1)[0].tolist())
    B = set(np.where(b == 1)[0].tolist())
    if not A and not B:
        return 1.0
    inter = len(A & B)
    uni = len(A | B)
    return inter / uni if uni else 1.0

def jaccard_z(a, b, perm=PERM):
    base = jaccard(a, b)
    vals = []
    bp = b.copy()
    for _ in range(perm):
        np.random.shuffle(bp)
        vals.append(jaccard(a, bp))
    mu = float(np.mean(vals))
    sd = float(np.std(vals, ddof=1) + 1e-9)
    return (base - mu) / sd, base, mu, sd

# ---------- TRANSFORMS (your harmonic wraps) ----------
def transforms(d):
    # d: digest bytes
    return {
        "raw": d,
        "mul_pi":    mul_u16(d, S_PI),
        "mul_e":     mul_u16(d, S_E),
        "mul_phi":   mul_u16(d, S_PHI),
        "mul_ephi":  mul_u16(d, S_EPHI),
        "mul_piphi": mul_u16(d, S_PIPHI),
        "add_pi":    add_byte(d, S_PI & 0xFF),
        "xor_pi":    xor_key(d, K_PI),
        "xor_e":     xor_key(d, K_E),
        "xor_phi":   xor_key(d, K_PHI),
        "rot_e":     rot_key(d, K_E),
        "mix_pi":    mix_xor_rot(d, K_PI, K_PI),
        "mix_pi_xor_e":      mix_xor_rot(d, K_PI, K_E),
        "mix_e_xor_pi":      mix_xor_rot(d, K_E,  K_PI),
        "mix_pi_xor_rand":   mix_xor_rot(d, K_PI, K_RND),
        "mix_rand_xor_pi":   mix_xor_rot(d, K_RND, K_PI),
    }

# ---------- DATASET ----------
inputs = [bytes(rng.randrange(256) for _ in range(64)) for _ in range(N_INPUTS)]
digests = [sha256_bytes(x) for x in inputs]

# ---------- RUN: BYTE-PORT (dense interior-band by default) ----------
def run_byte_port(mode="interior"):
    masks = {name: [] for name in transforms(digests[0]).keys()}
    for d in digests:
        td = transforms(d)
        for name, dd in td.items():
            masks[name].append(port_mask_byte(dd, thr=THR, mode=mode))
    return masks

# ---------- RUN: WORD-PORT (matches your 16 events/digest density ≈ 1.2) ----------
def run_word_port():
    masks = {name: [] for name in transforms(digests[0]).keys()}
    for d in digests:
        td = transforms(d)
        for name, dd in td.items():
            masks[name].append(port_mask_word(dd, word_bytes=WORD_BYTES))
    return masks

# ---------- REPORTERS ----------
def report_density(masks):
    print("\n=== Mask density check ===")
    for name, ms in masks.items():
        ones = np.array([int(m.sum()) for m in ms], dtype=np.float64)
        print(f"{name:14s} ones_mu={ones.mean():.2f}  ones_sd={ones.std(ddof=1):.2f}")

def report_features(masks, pick=512):
    # feature z-scores averaged over first pick samples to keep runtime tame
    print("\n=== Feature z-scores (mean over inputs): z(ac1), z(run), z(edge) ===")
    for name, ms in masks.items():
        zs_ac1  = [zscore_against_shuffle(m, feature_ac1,  perm=PERM) for m in ms[:pick]]
        zs_run  = [zscore_against_shuffle(m, feature_run,  perm=PERM) for m in ms[:pick]]
        zs_edge = [zscore_against_shuffle(m, feature_edge, perm=PERM) for m in ms[:pick]]
        print(f"{name:14s} z(ac1)={np.mean(zs_ac1):+0.2f}  z(run)={np.mean(zs_run):+0.2f}  z(edge)={np.mean(zs_edge):+0.2f}")

def report_invariance(masks, pairs, pick=512):
    print("\n=== Invariance summary (event-mask Jaccard z) ===")
    for a, b in pairs:
        zs = []
        for i in range(min(pick, len(masks[a]))):
            z, J, mu, sd = jaccard_z(masks[a][i], masks[b][i], perm=PERM)
            zs.append(z)
        zs = np.array(zs)
        print(f"{a:12s} vs {b:16s} z_mu={zs.mean():+0.3f} z_sd={zs.std(ddof=1):0.3f} max|z|={np.max(np.abs(zs)):0.3f}  |z|>=3: {int(np.sum(np.abs(zs)>=3))}/{len(zs)}")

# ---------- FAMILY SCAN: k = 65m + delta (q-space demonstration) ----------
# This is the "beat" microscope: 2^10 bucket vs 65-lattice.
def family_scan_qspace(q_space=1024, deltas=(0,1,-1), m_max=16):
    print("\n=== Family scan: k = 65m + delta ===")
    for m in range(m_max):
        for dlt in deltas:
            k = 65*m + dlt
            if 0 <= k < q_space:
                # simple "port set" induced by k: the residues you land on when stepping by 64 in q-space
                # (this captures the 64↔65 beating explicitly)
                S = set(((k + t*64) % q_space) % MOD for t in range(16))  # residues seen by 16 steps
                J = len(S & EVENT_RES) / len(S | EVENT_RES)
                print(f"m={m:2d}  k={k:4d} (0x{k:03x})  J={J:0.4f}")

# ---------- RUN EVERYTHING ----------
# Word-port run (this matches your "ones_mu ~ 1.2" regime)
word_masks = run_word_port()
print(f"WORD_PORT: WORD_BYTES={WORD_BYTES}  events/digest={len(next(iter(word_masks.values()))[0])}  THR={THR}")
report_density(word_masks)
report_features(word_masks, pick=512)
report_invariance(word_masks, pairs=[
    ("mul_pi","mix_pi"),
    ("mul_pi","mix_pi_xor_e"),
    ("mul_pi","mix_pi_xor_rand"),
    ("mul_pi","mix_rand_xor_pi"),
    ("mul_e","mix_e_xor_pi"),
    ("mul_pi","xor_pi"),
    ("mul_pi","mul_e"),
], pick=512)

# Byte-port run (toggle mode="interior" vs "edge")
byte_masks = run_byte_port(mode="interior")
print(f"\nBYTE_PORT (mode=interior): events/digest={len(next(iter(byte_masks.values()))[0])}  THR={THR}")
report_density(byte_masks)

# Show the explicit 64↔65 beat microscope (this is the "Nyquist back" core in arithmetic form)
family_scan_qspace()
# ======================================================================================

```

    WORD_PORT: WORD_BYTES=2  events/digest=16  THR=2
    
    === Mask density check ===
    raw            ones_mu=1.21  ones_sd=1.08
    mul_pi         ones_mu=1.26  ones_sd=1.11
    mul_e          ones_mu=1.22  ones_sd=1.07
    mul_phi        ones_mu=1.20  ones_sd=1.06
    mul_ephi       ones_mu=1.22  ones_sd=1.06
    mul_piphi      ones_mu=1.16  ones_sd=1.03
    add_pi         ones_mu=1.18  ones_sd=1.05
    xor_pi         ones_mu=1.19  ones_sd=1.06
    xor_e          ones_mu=1.19  ones_sd=1.06
    xor_phi        ones_mu=1.19  ones_sd=1.07
    rot_e          ones_mu=1.20  ones_sd=1.09
    mix_pi         ones_mu=1.19  ones_sd=1.07
    mix_pi_xor_e   ones_mu=1.20  ones_sd=1.07
    mix_e_xor_pi   ones_mu=1.20  ones_sd=1.06
    mix_pi_xor_rand ones_mu=1.25  ones_sd=1.07
    mix_rand_xor_pi ones_mu=1.27  ones_sd=1.09
    
    === Feature z-scores (mean over inputs): z(ac1), z(run), z(edge) ===
    

    C:\Users\Developer\anaconda3\Lib\site-packages\numpy\lib\_function_base_impl.py:3065: RuntimeWarning: invalid value encountered in divide
      c /= stddev[:, None]
    C:\Users\Developer\anaconda3\Lib\site-packages\numpy\lib\_function_base_impl.py:3066: RuntimeWarning: invalid value encountered in divide
      c /= stddev[None, :]
    

    raw            z(ac1)=+nan  z(run)=-0.04  z(edge)=+0.05
    mul_pi         z(ac1)=+nan  z(run)=-0.01  z(edge)=+0.01
    mul_e          z(ac1)=+nan  z(run)=+0.02  z(edge)=-0.01
    mul_phi        z(ac1)=+nan  z(run)=+0.01  z(edge)=-0.01
    mul_ephi       z(ac1)=+nan  z(run)=-0.01  z(edge)=-0.03
    mul_piphi      z(ac1)=+nan  z(run)=-0.01  z(edge)=+0.03
    add_pi         z(ac1)=+nan  z(run)=+0.02  z(edge)=-0.02
    xor_pi         z(ac1)=+nan  z(run)=-0.03  z(edge)=+0.02
    xor_e          z(ac1)=+nan  z(run)=-0.03  z(edge)=+0.06
    xor_phi        z(ac1)=+nan  z(run)=-0.01  z(edge)=+0.05
    rot_e          z(ac1)=+nan  z(run)=-0.01  z(edge)=+0.01
    mix_pi         z(ac1)=+nan  z(run)=-0.02  z(edge)=+0.05
    mix_pi_xor_e   z(ac1)=+nan  z(run)=-0.03  z(edge)=-0.00
    mix_e_xor_pi   z(ac1)=+nan  z(run)=-0.00  z(edge)=+0.04
    mix_pi_xor_rand z(ac1)=+nan  z(run)=+0.04  z(edge)=-0.02
    mix_rand_xor_pi z(ac1)=+nan  z(run)=+0.03  z(edge)=+0.01
    
    === Invariance summary (event-mask Jaccard z) ===
    mul_pi       vs mix_pi           z_mu=+0.024 z_sd=0.790 max|z|=4.921  |z|>=3: 8/512
    mul_pi       vs mix_pi_xor_e     z_mu=+0.011 z_sd=0.768 max|z|=5.708  |z|>=3: 4/512
    mul_pi       vs mix_pi_xor_rand  z_mu=+0.023 z_sd=0.762 max|z|=4.691  |z|>=3: 6/512
    mul_pi       vs mix_rand_xor_pi  z_mu=-0.029 z_sd=0.687 max|z|=4.891  |z|>=3: 4/512
    mul_e        vs mix_e_xor_pi     z_mu=-0.040 z_sd=0.640 max|z|=4.688  |z|>=3: 3/512
    mul_pi       vs xor_pi           z_mu=+0.032 z_sd=0.788 max|z|=5.263  |z|>=3: 6/512
    mul_pi       vs mul_e            z_mu=+0.043 z_sd=0.786 max|z|=4.691  |z|>=3: 5/512
    
    BYTE_PORT (mode=interior): events/digest=32  THR=2
    
    === Mask density check ===
    raw            ones_mu=27.99  ones_sd=1.87
    mul_pi         ones_mu=28.12  ones_sd=1.86
    mul_e          ones_mu=28.37  ones_sd=1.77
    mul_phi        ones_mu=27.89  ones_sd=1.93
    mul_ephi       ones_mu=27.72  ones_sd=1.98
    mul_piphi      ones_mu=30.13  ones_sd=1.34
    add_pi         ones_mu=28.00  ones_sd=1.91
    xor_pi         ones_mu=28.01  ones_sd=1.87
    xor_e          ones_mu=28.00  ones_sd=1.90
    xor_phi        ones_mu=28.00  ones_sd=1.89
    rot_e          ones_mu=27.99  ones_sd=1.88
    mix_pi         ones_mu=27.99  ones_sd=1.87
    mix_pi_xor_e   ones_mu=28.03  ones_sd=1.85
    mix_e_xor_pi   ones_mu=28.00  ones_sd=1.90
    mix_pi_xor_rand ones_mu=28.01  ones_sd=1.85
    mix_rand_xor_pi ones_mu=27.96  ones_sd=1.89
    
    === Family scan: k = 65m + delta ===
    m= 0  k=   0 (0x000)  J=0.1667
    m= 0  k=   1 (0x001)  J=0.2353
    m= 1  k=  65 (0x041)  J=0.2353
    m= 1  k=  66 (0x042)  J=0.3125
    m= 1  k=  64 (0x040)  J=0.1667
    m= 2  k= 130 (0x082)  J=0.3125
    m= 2  k= 131 (0x083)  J=0.3125
    m= 2  k= 129 (0x081)  J=0.2353
    m= 3  k= 195 (0x0c3)  J=0.3125
    m= 3  k= 196 (0x0c4)  J=0.3125
    m= 3  k= 194 (0x0c2)  J=0.3125
    m= 4  k= 260 (0x104)  J=0.3125
    m= 4  k= 261 (0x105)  J=0.3125
    m= 4  k= 259 (0x103)  J=0.3125
    m= 5  k= 325 (0x145)  J=0.3125
    m= 5  k= 326 (0x146)  J=0.3125
    m= 5  k= 324 (0x144)  J=0.3125
    m= 6  k= 390 (0x186)  J=0.3125
    m= 6  k= 391 (0x187)  J=0.3125
    m= 6  k= 389 (0x185)  J=0.3125
    m= 7  k= 455 (0x1c7)  J=0.3125
    m= 7  k= 456 (0x1c8)  J=0.3125
    m= 7  k= 454 (0x1c6)  J=0.3125
    m= 8  k= 520 (0x208)  J=0.3125
    m= 8  k= 521 (0x209)  J=0.3125
    m= 8  k= 519 (0x207)  J=0.3125
    m= 9  k= 585 (0x249)  J=0.3125
    m= 9  k= 586 (0x24a)  J=0.3125
    m= 9  k= 584 (0x248)  J=0.3125
    m=10  k= 650 (0x28a)  J=0.3125
    m=10  k= 651 (0x28b)  J=0.3125
    m=10  k= 649 (0x289)  J=0.3125
    m=11  k= 715 (0x2cb)  J=0.3125
    m=11  k= 716 (0x2cc)  J=0.3125
    m=11  k= 714 (0x2ca)  J=0.3125
    m=12  k= 780 (0x30c)  J=0.3125
    m=12  k= 781 (0x30d)  J=0.3125
    m=12  k= 779 (0x30b)  J=0.3125
    m=13  k= 845 (0x34d)  J=0.3125
    m=13  k= 846 (0x34e)  J=0.2353
    m=13  k= 844 (0x34c)  J=0.3125
    m=14  k= 910 (0x38e)  J=0.2353
    m=14  k= 911 (0x38f)  J=0.1667
    m=14  k= 909 (0x38d)  J=0.3125
    m=15  k= 975 (0x3cf)  J=0.1667
    m=15  k= 976 (0x3d0)  J=0.1053
    m=15  k= 974 (0x3ce)  J=0.2353
    


```python
# === Nexus port / π-pointer cell (fix + continue) ===
import os, re, math, hashlib
from collections import Counter
import numpy as np

HEX = "0123456789abcdef"

# ---------- 0) Robust hex cleanup (fixes your ValueError) ----------
def safe_fromhex(h: str) -> bytes:
    # keep only hex digits, drop last nibble if odd length
    h = re.sub(r"[^0-9a-fA-F]", "", h)
    if len(h) % 2 == 1:
        h = h[:-1]
    return bytes.fromhex(h)

# ---------- 1) High-precision base-16 fractional digit extractor ----------
def frac_hex_digits(x, n_hex: int) -> str:
    """
    Return n_hex hexadecimal digits of the fractional part of x (no leading integer digit).
    Uses mpmath if available, else Decimal fallback.
    """
    try:
        from mpmath import mp
        mp.mp.dps = int(n_hex * 1.21) + 80  # plenty for base-16 extraction
        y = mp.mpf(x)
        y -= mp.floor(y)
        out = []
        for _ in range(n_hex):
            y *= 16
            d = int(mp.floor(y))
            out.append(HEX[d])
            y -= d
        return "".join(out)
    except Exception:
        from decimal import Decimal, getcontext
        getcontext().prec = int(n_hex * 1.21) + 120
        y = (Decimal(str(x)) % 1)
        out = []
        for _ in range(n_hex):
            y *= 16
            d = int(y)
            out.append(HEX[d])
            y -= d
        return "".join(out)

def pi_hex(n_hex: int) -> str:
    # fractional hex digits only (so bytes.fromhex works cleanly when n_hex is even)
    return frac_hex_digits(math.pi, n_hex)

def key_bytes_from_const(x, n_bytes=32) -> bytes:
    return safe_fromhex(frac_hex_digits(x, n_bytes * 2))

# ---------- 2) Your 64↔65 “port lattice” made explicit ----------
EVENT_MOD = 65
EVENT_RES = {0, 1, 2, 63, 64}  # the 5/65 “ports”

def word_u16(bs: bytes) -> np.ndarray:
    a = np.frombuffer(bs, dtype=np.uint8)
    if len(a) % 2:
        a = a[:-1]
    return (a[0::2].astype(np.uint16) << 8) | a[1::2].astype(np.uint16)

def q_from_word(w: np.ndarray, shift6=True) -> np.ndarray:
    # your observed move: k = c >> 6  (divide by 64)
    return (w >> 6) if shift6 else w

def event_mask_from_q(q: np.ndarray) -> np.ndarray:
    r = q % EVENT_MOD
    return np.isin(r, list(EVENT_RES)).astype(np.uint8)

def jaccard(a: np.ndarray, b: np.ndarray) -> float:
    a = a.astype(np.uint8); b = b.astype(np.uint8)
    inter = int(np.sum(a & b))
    uni   = int(np.sum(a | b))
    return (inter / uni) if uni else 1.0

def perm_z(a: np.ndarray, b: np.ndarray, perm=300, seed=0):
    rng = np.random.default_rng(seed)
    obs = jaccard(a, b)
    idx = np.arange(len(b))
    js = []
    for _ in range(perm):
        rng.shuffle(idx)
        js.append(jaccard(a, b[idx]))
    mu = float(np.mean(js))
    sd = float(np.std(js, ddof=1) + 1e-12)
    z  = (obs - mu) / sd
    return obs, mu, sd, z

# ---------- 3) The “smoking stabilizer” you already found (why 975 is huge) ----------
def explain_k(k: int):
    return {
        "k": k,
        "k_hex": hex(k),
        "k_mod_65": k % 65,
        "is_port": (k % 65) in EVENT_RES,
        "is_multiple_of_65": (k % 65) == 0
    }

# sanity: your big one
print("k=975 check:", explain_k(975))
# NOTE: 975 = 65*15 -> residue 0 -> lands in EVENT_RES almost always (port fires)

# ---------- 4) Build harmonic keys (π, e, φ) ----------
PHI = (1 + 5**0.5) / 2
K_pi  = key_bytes_from_const(math.pi, 32)
K_e   = key_bytes_from_const(math.e, 32)
K_phi = key_bytes_from_const(PHI, 32)
K_rand = os.urandom(32)

# ---------- 5) Minimal transforms (safe: no “break SHA”, just wrap + probe) ----------
def sha256(b: bytes) -> bytes:
    return hashlib.sha256(b).digest()

def rotl8(x, r):
    r &= 7
    return ((x << r) | (x >> (8 - r))) & 0xFF

def apply_key(d: bytes, k: bytes, mode: str) -> bytes:
    b = np.frombuffer(d, dtype=np.uint8)
    kk = np.frombuffer(k, dtype=np.uint8)
    if mode == "raw":
        out = b
    elif mode == "xor":
        out = b ^ kk
    elif mode == "add":
        out = (b + kk) & 0xFF
    elif mode == "mul":
        out = (b * (kk | 1)) & 0xFF
    elif mode == "rot":
        out = np.array([rotl8(int(b[i]), int(kk[i] & 7)) for i in range(len(b))], dtype=np.uint8)
    elif mode == "mix":
        out = np.array([(((int(b[i]) + int(kk[i])) & 0xFF) ^ rotl8(int(b[i]), int(kk[i] & 7))) & 0xFF
                        for i in range(len(b))], dtype=np.uint8)
    else:
        raise ValueError(mode)
    return out.tobytes()

T = {
    "raw": lambda d: d,
    "mul_pi": lambda d: apply_key(d, K_pi, "mul"),
    "mul_e":  lambda d: apply_key(d, K_e, "mul"),
    "mul_phi":lambda d: apply_key(d, K_phi,"mul"),
    "add_pi": lambda d: apply_key(d, K_pi, "add"),
    "xor_phi":lambda d: apply_key(d, K_phi,"xor"),
    "xor_pi": lambda d: apply_key(d, K_pi, "xor"),
    "rot_e":  lambda d: apply_key(d, K_e, "rot"),
    "mix_pi": lambda d: apply_key(d, K_pi, "mix"),
    "mix_pi_xor_e":    lambda d: apply_key(apply_key(d, K_pi,"mix"), K_e, "xor"),
    "mix_pi_xor_rand": lambda d: apply_key(apply_key(d, K_pi,"mix"), K_rand, "xor"),
    "mix_rand_xor_pi": lambda d: apply_key(apply_key(d, K_rand,"mix"), K_pi, "xor"),
    "mix_e_xor_pi":    lambda d: apply_key(apply_key(d, K_e,"mix"), K_pi, "xor"),
}

# ---------- 6) Long-stream port (your “complete the circle” surface) ----------
def stream_for_seed(seed: bytes, n_digests=32) -> bytes:
    out = bytearray()
    x = seed
    for i in range(n_digests):
        x = sha256(x + i.to_bytes(4, "big"))
        out.extend(x)
    return bytes(out)

def mask_for(seed: bytes, name: str, n_digests=32, shift6=True) -> np.ndarray:
    s = stream_for_seed(seed, n_digests=n_digests)
    chunks = [T[name](s[i:i+32]) for i in range(0, len(s), 32)]
    w = word_u16(b"".join(chunks))
    q = q_from_word(w, shift6=shift6)
    return event_mask_from_q(q)

# Quick density check (should hover around 5/65 of events)
seed = b"nexus"
m = mask_for(seed, "mul_pi", n_digests=32, shift6=True)
print("\n=== mask density ===")
print("events:", len(m), "ones:", int(m.sum()), "ones/events:", float(m.sum())/len(m))

# Invariance probe (Jaccard z via permutation)
pairs = [("mul_pi","mix_pi"), ("mul_pi","mix_pi_xor_e"), ("mul_e","mix_e_xor_pi")]
print("\n=== invariance (single seed) ===")
for a,b in pairs:
    ma = mask_for(seed, a)
    mb = mask_for(seed, b)
    J, mu, sd, z = perm_z(ma, mb, perm=300, seed=1)
    print(f"{a:12s} vs {b:14s}  J={J:0.4f}  z={z:+0.2f}  (null mu={mu:0.4f} sd={sd:0.4f})")

# ---------- 7) π as bytes (DIGITS hex digits -> DIGITS/2 bytes) ----------
DIGITS = 4096                # hex digits
H = pi_hex(DIGITS)           # clean fractional hex digits
B = bytes.fromhex(H)         # should NOT error now
print("\nπ bytes:", len(B), "(expected", DIGITS//2, ")")

# ---------- 8) π-as-pointer against itself: orbit/cycle extraction ----------
def pointer_cycles(B: bytes, starts=256, max_steps=20000):
    n = len(B)
    starts = range(min(starts, n))
    seen_global = set()
    cycles = []
    for s in starts:
        if s in seen_global:
            continue
        seen = {}
        x = s
        for t in range(max_steps):
            if x in seen:
                entry_t = seen[x]
                # extract cycle
                cyc = []
                y = x
                while True:
                    cyc.append(y)
                    y = B[y] % n
                    if y == x:
                        break
                # mark all visited in this walk
                for v in seen:
                    seen_global.add(v)
                cycles.append((len(cyc), s, x, entry_t, cyc[:32]))
                break
            seen[x] = t
            x = B[x] % n
    cycles.sort(reverse=True)
    return cycles

cycles = pointer_cycles(B, starts=512)
print("\n=== top π-pointer cycles (len, start, entry, preperiod, first32 nodes) ===")
for L, s, entry, pre, head in cycles[:12]:
    print(f"L={L:4d}  start={s:4d}  entry={entry:4d}  pre={pre:5d}  head={head}")

# ---------- 9) The 64↔65 lattice made concrete ----------
# If q = floor(word/64), then "q mod 65 in EVENT_RES" repeats with period 64*65 = 4160 in word-space.
print("\n=== lattice note ===")
print("Period in word-space for (word>>6) mod 65:", 64*65, "(=4160)")
print("Your big stabilizers are exactly k near multiples of 65:",
      "455=65*7, 520=65*8, 910=65*14, 975=65*15, ...")

```

    k=975 check: {'k': 975, 'k_hex': '0x3cf', 'k_mod_65': 0, 'is_port': True, 'is_multiple_of_65': True}
    
    === mask density ===
    events: 512 ones: 40 ones/events: 0.078125
    
    === invariance (single seed) ===
    mul_pi       vs mix_pi          J=0.0541  z=+0.09  (null mu=0.0522 sd=0.0207)
    mul_pi       vs mix_pi_xor_e    J=0.0471  z=+0.12  (null mu=0.0444 sd=0.0212)
    mul_e        vs mix_e_xor_pi    J=0.1111  z=+2.56  (null mu=0.0563 sd=0.0214)
    
    π bytes: 2048 (expected 2048 )
    
    === top π-pointer cycles (len, start, entry, preperiod, first32 nodes) ===
    L=   3  start= 511  entry=  59  pre=   18  head=[59, 187, 75]
    L=   3  start= 510  entry=  59  pre=   14  head=[59, 187, 75]
    L=   3  start= 509  entry=  59  pre=   40  head=[59, 187, 75]
    L=   3  start= 508  entry=  59  pre=   14  head=[59, 187, 75]
    L=   3  start= 507  entry=  59  pre=   10  head=[59, 187, 75]
    L=   3  start= 506  entry=  59  pre=   12  head=[59, 187, 75]
    L=   3  start= 505  entry=  59  pre=    9  head=[59, 187, 75]
    L=   3  start= 504  entry=  59  pre=   31  head=[59, 187, 75]
    L=   3  start= 503  entry=  59  pre=   10  head=[59, 187, 75]
    L=   3  start= 502  entry= 187  pre=    2  head=[187, 75, 59]
    L=   3  start= 501  entry=  59  pre=   38  head=[59, 187, 75]
    L=   3  start= 500  entry=  59  pre=    8  head=[59, 187, 75]
    
    === lattice note ===
    Period in word-space for (word>>6) mod 65: 4160 (=4160)
    Your big stabilizers are exactly k near multiples of 65: 455=65*7, 520=65*8, 910=65*14, 975=65*15, ...
    


```python
import math, re
import numpy as np
from collections import Counter, defaultdict, deque

HEX = "0123456789abcdef"
EVENT_MOD = 65
EVENT_RES = {0, 1, 2, 63, 64}

# ---------- π hex digits (fractional) ----------
def frac_hex_digits(x, n_hex: int) -> str:
    try:
        from mpmath import mp
        mp.mp.dps = int(n_hex * 1.21) + 80
        y = mp.mpf(x); y -= mp.floor(y)
        out = []
        for _ in range(n_hex):
            y *= 16
            d = int(mp.floor(y))
            out.append(HEX[d])
            y -= d
        return "".join(out)
    except Exception:
        from decimal import Decimal, getcontext
        getcontext().prec = int(n_hex * 1.21) + 120
        y = (Decimal(str(x)) % 1)
        out = []
        for _ in range(n_hex):
            y *= 16
            d = int(y)
            out.append(HEX[d])
            y -= d
        return "".join(out)

def pi_bytes(n_bytes: int) -> bytes:
    h = frac_hex_digits(math.pi, n_bytes * 2)
    h = re.sub(r"[^0-9a-fA-F]", "", h)
    if len(h) % 2: h = h[:-1]
    return bytes.fromhex(h)

# ---------- pointer maps ----------
def map_f8(B: bytes) -> np.ndarray:
    n = len(B)
    nxt = np.frombuffer(B, dtype=np.uint8).astype(np.int32)  # 0..255
    return nxt % n

def map_f16(B: bytes) -> np.ndarray:
    n = len(B)
    a = np.frombuffer(B, dtype=np.uint8).astype(np.int32)
    b = np.roll(a, -1)
    nxt = ((a << 8) | b) % n
    return nxt.astype(np.int32)

def map_f24(B: bytes) -> np.ndarray:
    n = len(B)
    a = np.frombuffer(B, dtype=np.uint8).astype(np.int32)
    b = np.roll(a, -1)
    c = np.roll(a, -2)
    nxt = ((a << 16) | (b << 8) | c) % n
    return nxt.astype(np.int32)

# ---------- cycle + basin analysis for functional graph ----------
def analyze_functional_graph(nxt: np.ndarray, shift6=True, label=""):
    n = len(nxt)
    # states: 0=unseen, 1=visiting, 2=done
    state = np.zeros(n, dtype=np.int8)
    parent_step = np.full(n, -1, dtype=np.int32)
    step_id = np.full(n, -1, dtype=np.int32)

    cycles = []  # (cycle_len, entry_node, cycle_nodes)
    comp_of = np.full(n, -1, dtype=np.int32)

    comp = 0
    for s in range(n):
        if state[s] != 0: 
            continue
        x = s
        t = 0
        trail = []
        while state[x] == 0:
            state[x] = 1
            step_id[x] = t
            trail.append(x)
            x = nxt[x]
            t += 1
        if state[x] == 1:
            # found a cycle
            cyc_start_t = step_id[x]
            cyc_nodes = trail[cyc_start_t:]
            cycles.append((len(cyc_nodes), x, cyc_nodes))
            # assign component id for all in trail
            for v in trail:
                comp_of[v] = comp
            comp += 1
        else:
            # hit an already-done region, assign component id by inheriting
            inherit = comp_of[x]
            for v in trail:
                comp_of[v] = inherit

        # mark trail done
        for v in trail:
            state[v] = 2

    # basin sizes per component (component = attractor family)
    basin_sizes = Counter(comp_of.tolist())

    # cycle length distribution
    Ls = Counter([L for (L,_,_) in cycles])

    # dominant cycle(s)
    cycles_sorted = sorted(cycles, reverse=True, key=lambda z: (z[0], z[1]))

    # port occupancy on nodes (index-space)
    if shift6:
        r = ((np.arange(n) >> 6) % EVENT_MOD)
    else:
        r = (np.arange(n) % EVENT_MOD)
    port_mask = np.isin(r, list(EVENT_RES))

    # port occupancy on NEXT pointers (jump-space)
    rj = ((nxt >> 6) % EVENT_MOD) if shift6 else (nxt % EVENT_MOD)
    port_jump = np.isin(rj, list(EVENT_RES))

    report = {}
    report["label"] = label
    report["n"] = n
    report["unique_next"] = int(len(np.unique(nxt)))
    report["cycles_found"] = int(len(cycles))
    report["cycle_len_dist_top"] = Ls.most_common(10)
    report["largest_cycles"] = [(L, entry, cyc[:32]) for (L,entry,cyc) in cycles_sorted[:10]]
    report["largest_basin"] = int(max(basin_sizes.values()))
    report["basin_top"] = basin_sizes.most_common(5)
    report["port_node_rate"] = float(port_mask.mean())
    report["port_jump_rate"] = float(port_jump.mean())

    return report

def print_report(rep):
    print(f"\n=== {rep['label']} ===")
    print("n=", rep["n"], " unique_next=", rep["unique_next"])
    print("cycles_found=", rep["cycles_found"])
    print("cycle_len_dist_top=", rep["cycle_len_dist_top"])
    print("largest_basin=", rep["largest_basin"], " basin_top=", rep["basin_top"])
    print("port_node_rate=", rep["port_node_rate"], "port_jump_rate=", rep["port_jump_rate"])
    print("largest_cycles (L, entry, first32 nodes):")
    for L, entry, head in rep["largest_cycles"][:5]:
        print(f"  L={L:4d} entry={entry:4d} head={head}")

# ---------- run on π ----------
B = pi_bytes(2048)  # 2048 bytes like your run
nxt8  = map_f8(B)
nxt16 = map_f16(B)
nxt24 = map_f24(B)

rep8  = analyze_functional_graph(nxt8,  shift6=True, label="π f8 (byte-pointer)  [ALIASES to 0..255]")
rep16 = analyze_functional_graph(nxt16, shift6=True, label="π f16 (u16-pointer)  [de-aliased]")
rep24 = analyze_functional_graph(nxt24, shift6=True, label="π f24 (u24-pointer)  [more de-aliased]")

print_report(rep8)
print_report(rep16)
print_report(rep24)

# ---------- optional: show the exact alias trap ----------
print("\nAlias check:")
print("max(nxt8) =", int(nxt8.max()), " (if <256, you're trapped in 0..255)")
print("fraction of nodes whose next is <256 =", float((nxt8 < 256).mean()))

```

    
    === π f8 (byte-pointer)  [ALIASES to 0..255] ===
    n= 2048  unique_next= 256
    cycles_found= 1
    cycle_len_dist_top= [(3, 1)]
    largest_basin= 2048  basin_top= [(0, 2048)]
    port_node_rate= 0.09375 port_jump_rate= 0.7548828125
    largest_cycles (L, entry, first32 nodes):
      L=   3 entry=  59 head=[np.int32(59), np.int32(187), np.int32(75)]
    
    === π f16 (u16-pointer)  [de-aliased] ===
    n= 2048  unique_next= 1275
    cycles_found= 4
    cycle_len_dist_top= [(10, 1), (26, 1), (28, 1), (2, 1)]
    largest_basin= 950  basin_top= [(2, 950), (0, 840), (1, 253), (3, 5)]
    port_node_rate= 0.09375 port_jump_rate= 0.09765625
    largest_cycles (L, entry, first32 nodes):
      L=  28 entry= 463 head=[np.int32(463), np.int32(510), np.int32(981), np.int32(131), np.int32(1715), np.int32(352), np.int32(1998), np.int32(1194), np.int32(513), np.int32(820), np.int32(682), np.int32(1728), np.int32(1152), np.int32(9), np.int32(752), np.int32(447), np.int32(191), np.int32(1400), np.int32(425), np.int32(1725), np.int32(848), np.int32(148), np.int32(173), np.int32(1050), np.int32(1004), np.int32(1007), np.int32(530), np.int32(1708)]
      L=  26 entry=1289 head=[np.int32(1289), np.int32(77), np.int32(1673), np.int32(1392), np.int32(1122), np.int32(1750), np.int32(1401), np.int32(377), np.int32(1615), np.int32(431), np.int32(910), np.int32(1947), np.int32(1070), np.int32(1083), np.int32(1802), np.int32(979), np.int32(636), np.int32(1563), np.int32(2041), np.int32(439), np.int32(586), np.int32(998), np.int32(1063), np.int32(1115), np.int32(1837), np.int32(915)]
      L=  10 entry=2028 head=[np.int32(2028), np.int32(1784), np.int32(2000), np.int32(375), np.int32(643), np.int32(1349), np.int32(1326), np.int32(1487), np.int32(574), np.int32(1366)]
      L=   2 entry= 690 head=[np.int32(690), np.int32(1303)]
    
    === π f24 (u24-pointer)  [more de-aliased] ===
    n= 2048  unique_next= 1275
    cycles_found= 10
    cycle_len_dist_top= [(1, 4), (7, 2), (44, 1), (21, 1), (28, 1), (2, 1)]
    largest_basin= 1360  basin_top= [(0, 1360), (1, 389), (2, 218), (5, 31), (3, 30)]
    port_node_rate= 0.09375 port_jump_rate= 0.09765625
    largest_cycles (L, entry, first32 nodes):
      L=  44 entry= 305 head=[np.int32(305), np.int32(624), np.int32(444), np.int32(2043), np.int32(1762), np.int32(1296), np.int32(1725), np.int32(188), np.int32(978), np.int32(636), np.int32(849), np.int32(1099), np.int32(431), np.int32(1599), np.int32(758), np.int32(702), np.int32(1489), np.int32(1403), np.int32(974), np.int32(2037), np.int32(655), np.int32(163), np.int32(1164), np.int32(1536), np.int32(887), np.int32(1971), np.int32(1886), np.int32(1476), np.int32(1939), np.int32(1402), np.int32(651), np.int32(484)]
      L=  28 entry=1597 head=[np.int32(1597), np.int32(1949), np.int32(676), np.int32(1845), np.int32(1237), np.int32(1075), np.int32(591), np.int32(378), np.int32(1003), np.int32(1007), np.int32(590), np.int32(1857), np.int32(1061), np.int32(1948), np.int32(2026), np.int32(462), np.int32(510), np.int32(1315), np.int32(1795), np.int32(1570), np.int32(1637), np.int32(426), np.int32(1756), np.int32(1786), np.int32(282), np.int32(2034), np.int32(1842), np.int32(1458)]
      L=  21 entry=1308 head=[np.int32(1308), np.int32(18), np.int32(240), np.int32(91), np.int32(1774), np.int32(1522), np.int32(1330), np.int32(1255), np.int32(138), np.int32(166), np.int32(835), np.int32(493), np.int32(1800), np.int32(1547), np.int32(1938), np.int32(1221), np.int32(748), np.int32(1661), np.int32(1493), np.int32(903), np.int32(126)]
      L=   7 entry=1699 head=[np.int32(1699), np.int32(571), np.int32(359), np.int32(297), np.int32(1434), np.int32(1649), np.int32(569)]
      L=   7 entry= 271 head=[np.int32(271), np.int32(820), np.int32(584), np.int32(427), np.int32(1035), np.int32(1843), np.int32(522)]
    
    Alias check:
    max(nxt8) = 255  (if <256, you're trapped in 0..255)
    fraction of nodes whose next is <256 = 1.0
    


```python
import math, re
import numpy as np
from collections import Counter

HEX = "0123456789abcdef"
EVENT_MOD = 65
EVENT_RES = {0, 1, 2, 63, 64}

def frac_hex_digits(x, n_hex: int) -> str:
    try:
        from mpmath import mp
        mp.mp.dps = int(n_hex * 1.21) + 80
        y = mp.mpf(x); y -= mp.floor(y)
        out = []
        for _ in range(n_hex):
            y *= 16
            d = int(mp.floor(y))
            out.append(HEX[d])
            y -= d
        return "".join(out)
    except Exception:
        from decimal import Decimal, getcontext
        getcontext().prec = int(n_hex * 1.21) + 120
        y = (Decimal(str(x)) % 1)
        out = []
        for _ in range(n_hex):
            y *= 16
            d = int(y)
            out.append(HEX[d])
            y -= d
        return "".join(out)

def pi_bytes(n_bytes: int) -> bytes:
    h = frac_hex_digits(math.pi, n_bytes * 2)
    h = re.sub(r"[^0-9a-fA-F]", "", h)
    if len(h) % 2:  # safety
        h = h[:-1]
    return bytes.fromhex(h)

def map_f8(B: bytes) -> np.ndarray:
    n = len(B)
    nxt = np.frombuffer(B, dtype=np.uint8).astype(np.int32)
    return nxt % n

def map_f16(B: bytes) -> np.ndarray:
    n = len(B)
    a = np.frombuffer(B, dtype=np.uint8).astype(np.int32)
    b = np.roll(a, -1)
    return (((a << 8) | b) % n).astype(np.int32)

def map_f24(B: bytes) -> np.ndarray:
    n = len(B)
    a = np.frombuffer(B, dtype=np.uint8).astype(np.int32)
    b = np.roll(a, -1)
    c = np.roll(a, -2)
    return (((a << 16) | (b << 8) | c) % n).astype(np.int32)

def analyze_functional_graph(nxt: np.ndarray, label=""):
    n = len(nxt)

    # component labeling by pointer-walk
    state = np.zeros(n, dtype=np.int8)     # 0 unseen, 1 visiting, 2 done
    step  = np.full(n, -1, dtype=np.int32)
    comp_of = np.full(n, -1, dtype=np.int32)
    cycles = []
    comp = 0

    for s in range(n):
        if state[s] != 0:
            continue
        x = s
        t = 0
        trail = []
        while state[x] == 0:
            state[x] = 1
            step[x] = t
            trail.append(x)
            x = nxt[x]
            t += 1
        if state[x] == 1:
            # cycle found in this trail
            cs = step[x]
            cyc = trail[cs:]
            cycles.append((len(cyc), x, cyc))
            for v in trail:
                comp_of[v] = comp
            comp += 1
        else:
            inherit = comp_of[x]
            for v in trail:
                comp_of[v] = inherit

        for v in trail:
            state[v] = 2

    basin_sizes = Counter(comp_of.tolist())
    largest_basin = max(basin_sizes.values())
    basin_dom = largest_basin / n

    # ports: now that n>=4160, residues 63/64 actually exist in word space
    word = (np.arange(n) >> 6) % EVENT_MOD
    port_node_rate = float(np.isin(word, list(EVENT_RES)).mean())

    jword = (nxt >> 6) % EVENT_MOD
    port_jump_rate = float(np.isin(jword, list(EVENT_RES)).mean())

    # “centrifugal” / exit metrics
    escape_256 = 1.0 - float((nxt < 256).mean())
    unique_next = int(len(np.unique(nxt)))
    expand_ratio = unique_next / n

    cycles_sorted = sorted(cycles, reverse=True, key=lambda z: (z[0], z[1]))

    print(f"\n=== {label} ===")
    print(f"n={n} unique_next={unique_next} expand_ratio={expand_ratio:.4f} escape_256={escape_256:.4f}")
    print(f"cycles_found={len(cycles)} basin_dom={basin_dom:.4f} (largest_basin={largest_basin})")
    print(f"port_node_rate={port_node_rate:.6f}  port_jump_rate={port_jump_rate:.6f}")
    print("top cycles (L, entry, head32):")
    for L, entry, cyc in cycles_sorted[:5]:
        print(f"  L={L:4d} entry={entry:5d} head={cyc[:32]}")

def run(n_bytes=4160):
    B = pi_bytes(n_bytes)
    analyze_functional_graph(map_f8(B),  label=f"π f8  (n_bytes={n_bytes})")
    analyze_functional_graph(map_f16(B), label=f"π f16 (n_bytes={n_bytes})")
    analyze_functional_graph(map_f24(B), label=f"π f24 (n_bytes={n_bytes})")

run(4160)
run(8320)

```

    
    === π f8  (n_bytes=4160) ===
    n=4160 unique_next=256 expand_ratio=0.0615 escape_256=0.0000
    cycles_found=1 basin_dom=1.0000 (largest_basin=4160)
    port_node_rate=0.076923  port_jump_rate=0.754087
    top cycles (L, entry, head32):
      L=   3 entry=   59 head=[np.int32(59), np.int32(187), np.int32(75)]
    
    === π f16 (n_bytes=4160) ===
    n=4160 unique_next=2603 expand_ratio=0.6257 escape_256=0.9392
    cycles_found=5 basin_dom=0.7738 (largest_basin=3219)
    port_node_rate=0.076923  port_jump_rate=0.074519
    top cycles (L, entry, head32):
      L=  30 entry=  678 head=[np.int32(678), np.int32(1194), np.int32(2049), np.int32(3119), np.int32(1538), np.int32(1460), np.int32(3299), np.int32(464), np.int32(2788), np.int32(2192), np.int32(2968), np.int32(889), np.int32(283), np.int32(4082), np.int32(1474), np.int32(3862), np.int32(1929), np.int32(745), np.int32(2428), np.int32(3689), np.int32(3633), np.int32(754), np.int32(680), np.int32(2942), np.int32(3356), np.int32(1390), np.int32(617), np.int32(1093), np.int32(2752), np.int32(1356)]
      L=  22 entry= 3029 head=[np.int32(3029), np.int32(3973), np.int32(279), np.int32(934), np.int32(2969), np.int32(1938), np.int32(1164), np.int32(3574), np.int32(3663), np.int32(2028), np.int32(3064), np.int32(812), np.int32(1686), np.int32(2324), np.int32(1275), np.int32(11), np.int32(3067), np.int32(1823), np.int32(647), np.int32(2050), np.int32(3125), np.int32(4016)]
      L=  10 entry= 2346 head=[np.int32(2346), np.int32(4049), np.int32(2352), np.int32(861), np.int32(2079), np.int32(4139), np.int32(874), np.int32(3301), np.int32(1273), np.int32(942)]
      L=   4 entry= 1462 head=[np.int32(1462), np.int32(2828), np.int32(972), np.int32(1640)]
      L=   1 entry= 3298 head=[np.int32(3298)]
    
    === π f24 (n_bytes=4160) ===
    n=4160 unique_next=2630 expand_ratio=0.6322 escape_256=0.9334
    cycles_found=4 basin_dom=0.6065 (largest_basin=2523)
    port_node_rate=0.076923  port_jump_rate=0.078606
    top cycles (L, entry, head32):
      L=  58 entry= 2116 head=[np.int32(2116), np.int32(2935), np.int32(3270), np.int32(2564), np.int32(618), np.int32(2301), np.int32(2596), np.int32(788), np.int32(4044), np.int32(1775), np.int32(962), np.int32(1092), np.int32(1472), np.int32(671), np.int32(3716), np.int32(3204), np.int32(4057), np.int32(1267), np.int32(1331), np.int32(169), np.int32(3322), np.int32(3233), np.int32(2052), np.int32(775), np.int32(3339), np.int32(4025), np.int32(1287), np.int32(3208), np.int32(3824), np.int32(2002), np.int32(2843), np.int32(625)]
      L=  39 entry= 2401 head=[np.int32(2401), np.int32(380), np.int32(3805), np.int32(3516), np.int32(1145), np.int32(2408), np.int32(2790), np.int32(3591), np.int32(1509), np.int32(342), np.int32(2521), np.int32(3621), np.int32(111), np.int32(3249), np.int32(2075), np.int32(3502), np.int32(947), np.int32(3771), np.int32(1640), np.int32(4064), np.int32(2333), np.int32(40), np.int32(1304), np.int32(3733), np.int32(3760), np.int32(3545), np.int32(3082), np.int32(3121), np.int32(2286), np.int32(1553), np.int32(145), np.int32(2488)]
      L=  16 entry= 1173 head=[np.int32(1173), np.int32(3816), np.int32(4144), np.int32(2084), np.int32(2825), np.int32(2229), np.int32(1152), np.int32(1657), np.int32(1623), np.int32(724), np.int32(206), np.int32(215), np.int32(432), np.int32(4001), np.int32(1081), np.int32(1015)]
      L=   6 entry= 1480 head=[np.int32(1480), np.int32(1348), np.int32(2862), np.int32(2131), np.int32(3735), np.int32(2160)]
    
    === π f8  (n_bytes=8320) ===
    n=8320 unique_next=256 expand_ratio=0.0308 escape_256=0.0000
    cycles_found=1 basin_dom=1.0000 (largest_basin=8320)
    port_node_rate=0.076923  port_jump_rate=0.753245
    top cycles (L, entry, head32):
      L=   3 entry=   59 head=[np.int32(59), np.int32(187), np.int32(75)]
    
    === π f16 (n_bytes=8320) ===
    n=8320 unique_next=5244 expand_ratio=0.6303 escape_256=0.9681
    cycles_found=3 basin_dom=0.9986 (largest_basin=8308)
    port_node_rate=0.076923  port_jump_rate=0.078486
    top cycles (L, entry, head32):
      L=  17 entry= 5779 head=[np.int32(5779), np.int32(905), np.int32(7435), np.int32(2121), np.int32(5254), np.int32(3228), np.int32(2465), np.int32(476), np.int32(2381), np.int32(603), np.int32(1990), np.int32(5359), np.int32(7518), np.int32(4224), np.int32(1197), np.int32(7318), np.int32(6728)]
      L=   2 entry= 4573 head=[np.int32(4573), np.int32(6468)]
      L=   1 entry= 5829 head=[np.int32(5829)]
    
    === π f24 (n_bytes=8320) ===
    n=8320 unique_next=5257 expand_ratio=0.6319 escape_256=0.9691
    cycles_found=3 basin_dom=0.9464 (largest_basin=7874)
    port_node_rate=0.076923  port_jump_rate=0.075721
    top cycles (L, entry, head32):
      L=  15 entry= 6910 head=[np.int32(6910), np.int32(2600), np.int32(6616), np.int32(2139), np.int32(1832), np.int32(4931), np.int32(7703), np.int32(6316), np.int32(5119), np.int32(4011), np.int32(1414), np.int32(1740), np.int32(2597), np.int32(4152), np.int32(7909)]
      L=   9 entry= 7616 head=[np.int32(7616), np.int32(7937), np.int32(1568), np.int32(2021), np.int32(2027), np.int32(4600), np.int32(7307), np.int32(3014), np.int32(1630)]
      L=   1 entry= 7137 head=[np.int32(7137)]
    


```python
# FULL CELL: long-stream 64/65 word-port analysis + harmonic wraps + invariance stats
# (designed to be run as a single Jupyter cell)

import hashlib, math, random
import numpy as np
from decimal import Decimal, getcontext, ROUND_FLOOR

# -----------------------
# Config
# -----------------------
BASE_MESSAGE = b"hello"
N_INPUTS     = 512       # bump to 2048+ when stable
WINDOW       = 32        # hashes per sample -> events/sample = (32/WORD_BYTES)*WINDOW
WORD_BYTES   = 2         # 2=16-bit words (16 per digest), 4=32-bit words (8 per digest)
THR          = 2         # event gate: beta <= THR
N_PERM_MASK  = 300       # permutations for mask alignment z
N_PERM_FEAT  = 200       # permutations for feature z
SEED         = 7

MASK256 = (1 << 256) - 1
getcontext().prec = 220

CONST_STR = {
    "pi":  "3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679",
    "e":   "2.7182818284590452353602874713526624977572470936999595749669676277240766303535475945713821785251664274",
    "phi": "1.6180339887498948482045868343656381177203091798057628621354486227052604628189024497072072041893911375",
}

# -----------------------
# Helpers
# -----------------------
def sha256_bytes(msg: bytes) -> bytes:
    return hashlib.sha256(msg).digest()

def bytes_to_u256(b: bytes) -> int:
    return int.from_bytes(b, "big")

def u256_to_bytes(x: int) -> bytes:
    return int(x & MASK256).to_bytes(32, "big")

def rotl_u256(x: int, r: int) -> int:
    r &= 255
    return ((x << r) | (x >> (256 - r))) & MASK256

def dec_frac_to_u256(dec_str: str) -> int:
    d = Decimal(dec_str)
    frac = d - int(d)
    scale = Decimal(1 << 256)
    k = int((frac * scale).to_integral_value(rounding=ROUND_FLOOR))
    return (k | 1) & MASK256

def mean(xs):
    return float(sum(xs) / len(xs)) if xs else 0.0

def std(xs, mu=None):
    if not xs:
        return 0.0
    if mu is None:
        mu = mean(xs)
    var = sum((x - mu)**2 for x in xs) / len(xs)
    return math.sqrt(var)

# -----------------------
# 64/65 word-port beta
# beta(x) = min( (floor(x/64) mod 65), 65 - that )
# -----------------------
def beta_64_65_int(x: int) -> int:
    q = x >> 6
    d = q % 65
    return min(d, 65 - d)  # 0..32

def beta_sequence_from_bytes(byte_stream: bytes, word_bytes=2):
    n = len(byte_stream) // word_bytes
    betas = []
    for i in range(n):
        w = int.from_bytes(byte_stream[i*word_bytes:(i+1)*word_bytes], "big")
        betas.append(beta_64_65_int(w))
    return betas

def event_mask_from_betas(betas, thr=2):
    return [1 if b <= thr else 0 for b in betas]

# -----------------------
# Similarity / null
# -----------------------
def jaccard_mask(ma, mb):
    inter = sum(1 for x,y in zip(ma,mb) if x==1 and y==1)
    union = sum(1 for x,y in zip(ma,mb) if x==1 or y==1)
    return inter / union if union else 1.0

def mask_alignment_z(ma, mb, n_perm=300, rng=None):
    if rng is None:
        rng = random.Random(0)
    obs = jaccard_mask(ma, mb)
    idx = list(range(len(mb)))
    null = []
    for _ in range(n_perm):
        rng.shuffle(idx)
        perm = [mb[i] for i in idx]
        null.append(jaccard_mask(ma, perm))
    mu = mean(null)
    sd = std(null, mu) + 1e-12
    return obs, (obs - mu) / sd

# -----------------------
# Stream features
# -----------------------
def autocorr_lag1(xs):
    if len(xs) < 3:
        return 0.0
    mu = mean(xs)
    num = sum((xs[i]-mu)*(xs[i-1]-mu) for i in range(1,len(xs)))
    den = sum((x-mu)*(x-mu) for x in xs) + 1e-12
    return num / den

def max_run_ones(mask):
    best = cur = 0
    for v in mask:
        if v==1:
            cur += 1
            best = max(best, cur)
        else:
            cur = 0
    return best

def edge_imbalance(mask):
    n = len(mask)
    a = mask[:n//2]
    b = mask[n//2:]
    da = sum(a)/len(a) if a else 0.0
    db = sum(b)/len(b) if b else 0.0
    return da - db

def z_against_shuffle(feature_fn, betas, mask, n_perm=200, rng=None):
    if rng is None:
        rng = random.Random(0)
    obs = feature_fn(betas, mask)
    idx = list(range(len(betas)))
    null = []
    for _ in range(n_perm):
        rng.shuffle(idx)
        b2 = [betas[i] for i in idx]
        m2 = [mask[i] for i in idx]
        null.append(feature_fn(b2, m2))
    mu = mean(null)
    sd = std(null, mu) + 1e-12
    return (obs - mu) / sd

def feat_ac1(betas, mask):   return autocorr_lag1(betas)
def feat_run(betas, mask):   return float(max_run_ones(mask))
def feat_edge(betas, mask):  return float(edge_imbalance(mask))

# -----------------------
# Wrap keys / ops
# -----------------------
K_pi   = dec_frac_to_u256(CONST_STR["pi"])
K_e    = dec_frac_to_u256(CONST_STR["e"])
K_phi  = dec_frac_to_u256(CONST_STR["phi"])
K_ephi   = ((K_e  * K_phi) & MASK256) | 1
K_piphi  = ((K_pi * K_phi) & MASK256) | 1

_rng = random.Random(999)
K_rand = (_rng.getrandbits(256) | 1) & MASK256

def wrap_digest(digest: bytes, K: int, mode: str) -> bytes:
    h = bytes_to_u256(digest)
    if mode == "mul":
        return u256_to_bytes((h * K) & MASK256)
    if mode == "add":
        return u256_to_bytes((h + K) & MASK256)
    if mode == "xor":
        kb = u256_to_bytes(K)
        return bytes([a ^ b for a,b in zip(digest, kb)])
    if mode == "rot":
        r = K & 255
        return u256_to_bytes(rotl_u256(h, r))
    if mode == "mix":
        out = (h * K) & MASK256
        ob = u256_to_bytes(out)
        kb = u256_to_bytes(K)
        return bytes([a ^ b for a,b in zip(ob, kb)])
    raise ValueError(mode)

def wrap_cross(digest: bytes, K_mul: int, K_xor: int) -> bytes:
    h = bytes_to_u256(digest)
    out = (h * K_mul) & MASK256
    ob = u256_to_bytes(out)
    xb = u256_to_bytes(K_xor)
    return bytes([a ^ b for a,b in zip(ob, xb)])

WRAPS = {
    "raw":       ("raw", 0),
    "mul_pi":    ("mul", K_pi),
    "mul_e":     ("mul", K_e),
    "mul_phi":   ("mul", K_phi),
    "mul_ephi":  ("mul", K_ephi),
    "mul_piphi": ("mul", K_piphi),
    "add_pi":    ("add", K_pi),
    "rot_e":     ("rot", K_e),
    "xor_pi":    ("xor", K_pi),
    "xor_e":     ("xor", K_e),
    "xor_phi":   ("xor", K_phi),
    "mix_pi":    ("mix", K_pi),
}
CROSS = {
    "mix_pi_xor_e":      (K_pi, K_e),
    "mix_pi_xor_rand":   (K_pi, K_rand),
    "mix_rand_xor_pi":   (K_rand, K_pi),
    "mix_e_xor_pi":      (K_e,  K_pi),
}

def apply_wrap(d0: bytes, name: str) -> bytes:
    if name == "raw":
        return d0
    if name in WRAPS and WRAPS[name][0] != "raw":
        mode, K = WRAPS[name]
        return wrap_digest(d0, K, mode)
    if name in CROSS:
        km, kx = CROSS[name]
        return wrap_cross(d0, km, kx)
    raise KeyError(name)

# -----------------------
# Build long stream per input
# -----------------------
def make_stream(msg_seed: bytes, i: int, window: int, wrap_name: str) -> bytes:
    out = bytearray()
    for j in range(window):
        d0 = sha256_bytes(msg_seed + b"|" + str(i).encode() + b"|" + str(j).encode())
        out.extend(apply_wrap(d0, wrap_name))
    return bytes(out)

# -----------------------
# Run
# -----------------------
pairs_to_test = [
    ("mul_pi", "mix_pi"),
    ("mul_pi", "mix_pi_xor_e"),
    ("mul_pi", "mix_pi_xor_rand"),
    ("mul_pi", "mix_rand_xor_pi"),
    ("mul_e",  "mix_e_xor_pi"),
    ("mul_pi", "xor_pi"),
    ("mul_pi", "mul_e"),
]

rng_mask = random.Random(SEED)
rng_feat = random.Random(SEED + 101)

used = set([x for pair in pairs_to_test for x in pair])
used |= set(["raw","mul_phi","mul_ephi","mul_piphi","add_pi","rot_e","xor_e","xor_phi"])

dens = {name: [] for name in used}
featZ = {name: {"ac1": [], "run": [], "edge": []} for name in used}
invZ  = {p: [] for p in pairs_to_test}

for i in range(N_INPUTS):
    cache = {}
    for name in used:
        stream = make_stream(BASE_MESSAGE, i, WINDOW, name)
        betas = beta_sequence_from_bytes(stream, word_bytes=WORD_BYTES)
        mask  = event_mask_from_betas(betas, thr=THR)
        cache[name] = (betas, mask)

        dens[name].append(sum(mask))

        featZ[name]["ac1"].append(z_against_shuffle(feat_ac1, betas, mask, n_perm=N_PERM_FEAT, rng=rng_feat))
        featZ[name]["run"].append(z_against_shuffle(feat_run, betas, mask, n_perm=N_PERM_FEAT, rng=rng_feat))
        featZ[name]["edge"].append(z_against_shuffle(feat_edge, betas, mask, n_perm=N_PERM_FEAT, rng=rng_feat))

    for (a,b) in pairs_to_test:
        ma = cache[a][1]
        mb = cache[b][1]
        _, z = mask_alignment_z(ma, mb, n_perm=N_PERM_MASK, rng=rng_mask)
        invZ[(a,b)].append(z)

events_per_sample = (32 // WORD_BYTES) * WINDOW

print("\n=== Long-stream port ===")
print(f"WORD_BYTES={WORD_BYTES}  WINDOW={WINDOW}  events/sample={events_per_sample}  THR={THR}")
print(f"inputs={N_INPUTS}  perm={N_PERM_MASK}")

print("\n=== Mask density (ones per sample) ===")
for name in sorted(used):
    mu = mean(dens[name]); sd = std(dens[name], mu)
    print(f"{name:16s} ones_mu={mu:.2f} ones_sd={sd:.2f}")

print("\n=== Feature z-scores (mean over inputs): z(ac1), z(run), z(edge) ===")
for name in sorted(used):
    zac1 = mean(featZ[name]["ac1"])
    zrun = mean(featZ[name]["run"])
    zedge= mean(featZ[name]["edge"])
    print(f"{name:16s} z(ac1)={zac1:+.2f}  z(run)={zrun:+.2f}  z(edge)={zedge:+.2f}")

print("\n=== Invariance summary (event-mask Jaccard z) ===")
for (a,b) in pairs_to_test:
    zs = invZ[(a,b)]
    mu = mean(zs); sd = std(zs, mu)
    mx = max(abs(z) for z in zs) if zs else 0.0
    cnt3 = sum(1 for z in zs if abs(z) >= 3.0)
    print(f"{a:12s} vs {b:16s} z_mu={mu:+.3f} z_sd={sd:.3f} max|z|={mx:.3f}  |z|>=3: {cnt3}/{len(zs)}")

```

    
    === Long-stream port ===
    WORD_BYTES=2  WINDOW=32  events/sample=512  THR=2
    inputs=512  perm=300
    
    === Mask density (ones per sample) ===
    add_pi           ones_mu=39.07 ones_sd=5.66
    mix_e_xor_pi     ones_mu=39.20 ones_sd=5.79
    mix_pi           ones_mu=39.33 ones_sd=5.91
    mix_pi_xor_e     ones_mu=39.21 ones_sd=5.66
    mix_pi_xor_rand  ones_mu=39.00 ones_sd=5.98
    mix_rand_xor_pi  ones_mu=38.88 ones_sd=6.15
    mul_e            ones_mu=39.30 ones_sd=5.80
    mul_ephi         ones_mu=39.06 ones_sd=6.09
    mul_phi          ones_mu=39.12 ones_sd=5.66
    mul_pi           ones_mu=39.22 ones_sd=5.83
    mul_piphi        ones_mu=38.64 ones_sd=6.05
    raw              ones_mu=38.99 ones_sd=5.92
    rot_e            ones_mu=39.14 ones_sd=6.23
    xor_e            ones_mu=39.02 ones_sd=6.21
    xor_phi          ones_mu=39.07 ones_sd=6.10
    xor_pi           ones_mu=38.52 ones_sd=5.87
    
    === Feature z-scores (mean over inputs): z(ac1), z(run), z(edge) ===
    add_pi           z(ac1)=+0.06  z(run)=+0.03  z(edge)=+0.02
    mix_e_xor_pi     z(ac1)=-0.01  z(run)=-0.05  z(edge)=-0.02
    mix_pi           z(ac1)=+0.03  z(run)=-0.00  z(edge)=-0.09
    mix_pi_xor_e     z(ac1)=+0.03  z(run)=+0.00  z(edge)=+0.02
    mix_pi_xor_rand  z(ac1)=-0.03  z(run)=-0.01  z(edge)=-0.04
    mix_rand_xor_pi  z(ac1)=-0.04  z(run)=+0.07  z(edge)=+0.02
    mul_e            z(ac1)=-0.03  z(run)=+0.04  z(edge)=-0.01
    mul_ephi         z(ac1)=+0.03  z(run)=-0.04  z(edge)=-0.00
    mul_phi          z(ac1)=-0.03  z(run)=+0.09  z(edge)=-0.04
    mul_pi           z(ac1)=+0.04  z(run)=-0.07  z(edge)=+0.01
    mul_piphi        z(ac1)=+0.01  z(run)=-0.06  z(edge)=+0.02
    raw              z(ac1)=+0.04  z(run)=-0.05  z(edge)=+0.07
    rot_e            z(ac1)=-0.05  z(run)=-0.07  z(edge)=-0.02
    xor_e            z(ac1)=+0.06  z(run)=-0.01  z(edge)=+0.05
    xor_phi          z(ac1)=+0.03  z(run)=+0.04  z(edge)=-0.01
    xor_pi           z(ac1)=-0.05  z(run)=+0.00  z(edge)=-0.02
    
    === Invariance summary (event-mask Jaccard z) ===
    mul_pi       vs mix_pi           z_mu=-1.120 z_sd=0.595 max|z|=2.246  |z|>=3: 0/512
    mul_pi       vs mix_pi_xor_e     z_mu=+1.680 z_sd=1.336 max|z|=5.325  |z|>=3: 86/512
    mul_pi       vs mix_pi_xor_rand  z_mu=-0.727 z_sd=0.739 max|z|=3.270  |z|>=3: 1/512
    mul_pi       vs mix_rand_xor_pi  z_mu=-0.016 z_sd=1.032 max|z|=5.260  |z|>=3: 5/512
    mul_e        vs mix_e_xor_pi     z_mu=-1.042 z_sd=0.614 max|z|=2.240  |z|>=3: 0/512
    mul_pi       vs xor_pi           z_mu=+0.001 z_sd=1.020 max|z|=4.413  |z|>=3: 2/512
    mul_pi       vs mul_e            z_mu=+0.047 z_sd=0.979 max|z|=3.302  |z|>=3: 4/512
    


```python
# ============================================================
# Nexus Long-Stream Port / SILR Geometry Probe (full cell)
# ============================================================
import hashlib, math, random
import numpy as np

# -----------------------------
# Config
# -----------------------------
SEED        = 1337
SAMPLES     = 512          # number of long-stream samples
WINDOW      = 32           # digests per sample
WORD_BYTES  = 2            # 2 bytes -> 16 words per digest
THR         = 2            # event threshold beta<=THR
MOD_BASE    = 65           # residue modulus (65 gives residues 0..64)
PERM        = 300          # permutations for null z-scores

# Event residues for THR on mod-65: {0..thr} U {64-thr..64}
def event_set(thr=THR, base=MOD_BASE):
    hi = base - 1
    return set(range(0, thr+1)) | set(range(hi-thr, hi+1))

EVENT_RES = event_set(THR, MOD_BASE)

rng = random.Random(SEED)
np_rng = np.random.default_rng(SEED)

# -----------------------------
# Utilities: bytes/int
# -----------------------------
MASK256 = (1 << 256) - 1

def b2i(b): return int.from_bytes(b, "big")
def i2b(x): return int(x & MASK256).to_bytes(32, "big")

def sha256(b: bytes) -> bytes:
    return hashlib.sha256(b).digest()

# -----------------------------
# Deterministic "harmonic keys"
# (swap these for true pi/e/phi byte tables if you want)
# -----------------------------
def key32(label: str) -> bytes:
    # Deterministic 32-byte key derived from SHA256(label)
    return sha256(label.encode("utf-8"))

K_PI  = key32("pi")
K_E   = key32("e")
K_PHI = key32("phi")
K_R   = key32("rand")  # deterministic "random" key

# Scaled constants for mul/add (choose stable integer scalars)
# These are "wrapping knobs" not claims about physics constants.
C_PI  = b2i(K_PI)
C_E   = b2i(K_E)
C_PHI = b2i(K_PHI)

# -----------------------------
# Wrap transforms (edit freely)
# -----------------------------
def rotl256(x, r):
    r &= 255
    return ((x << r) | (x >> (256 - r))) & MASK256

def tx_raw(d): return d

def tx_mul_pi(d):
    x = b2i(d); return i2b((x * (C_PI | 1)) & MASK256)

def tx_mul_e(d):
    x = b2i(d); return i2b((x * (C_E  | 1)) & MASK256)

def tx_mul_phi(d):
    x = b2i(d); return i2b((x * (C_PHI| 1)) & MASK256)

def tx_mul_ephi(d):
    x = b2i(d); return i2b((x * ((C_E ^ C_PHI) | 1)) & MASK256)

def tx_mul_piphi(d):
    x = b2i(d); return i2b((x * ((C_PI ^ C_PHI) | 1)) & MASK256)

def tx_add_pi(d):
    x = b2i(d); return i2b((x + C_PI) & MASK256)

def tx_xor_pi(d):
    return bytes(a ^ b for a,b in zip(d, K_PI))

def tx_xor_e(d):
    return bytes(a ^ b for a,b in zip(d, K_E))

def tx_xor_phi(d):
    return bytes(a ^ b for a,b in zip(d, K_PHI))

def tx_rot_e(d):
    x = b2i(d); return i2b(rotl256(x, 17))  # 17 is arbitrary; tune if you want

def tx_mix_pi(d):
    # One ARX-ish mix: xor key -> rotate -> add key
    x = b2i(bytes(a ^ b for a,b in zip(d, K_PI)))
    x = rotl256(x, 23)
    x = (x + C_PI) & MASK256
    return i2b(x)

def tx_mix_pi_xor_e(d):
    return tx_xor_e(tx_mix_pi(d))

def tx_mix_e_xor_pi(d):
    # symmetric variant
    x = b2i(bytes(a ^ b for a,b in zip(d, K_E)))
    x = rotl256(x, 29)
    x = (x + C_E) & MASK256
    out = i2b(x)
    return bytes(a ^ b for a,b in zip(out, K_PI))

def tx_mix_pi_xor_rand(d):
    return bytes(a ^ b for a,b in zip(tx_mix_pi(d), K_R))

def tx_mix_rand_xor_pi(d):
    # "random" pre-xor then pi-xor
    pre = bytes(a ^ b for a,b in zip(d, K_R))
    return bytes(a ^ b for a,b in zip(tx_mix_pi(pre), K_PI))

TX = {
    "raw": tx_raw,
    "mul_pi": tx_mul_pi,
    "mul_e": tx_mul_e,
    "mul_phi": tx_mul_phi,
    "mul_ephi": tx_mul_ephi,
    "mul_piphi": tx_mul_piphi,
    "add_pi": tx_add_pi,
    "xor_pi": tx_xor_pi,
    "xor_e": tx_xor_e,
    "xor_phi": tx_xor_phi,
    "rot_e": tx_rot_e,
    "mix_pi": tx_mix_pi,
    "mix_pi_xor_e": tx_mix_pi_xor_e,
    "mix_e_xor_pi": tx_mix_e_xor_pi,
    "mix_pi_xor_rand": tx_mix_pi_xor_rand,
    "mix_rand_xor_pi": tx_mix_rand_xor_pi,
}

# -----------------------------
# Port: digest -> 16-bit word residues -> event bits
# -----------------------------
def digest_words(d: bytes, word_bytes=WORD_BYTES):
    # 32 bytes => 16 words if word_bytes=2
    assert len(d) == 32
    step = word_bytes
    return [int.from_bytes(d[i:i+step], "big") for i in range(0, 32, step)]

def event_mask_from_digest(d: bytes, thr=THR, base=MOD_BASE, word_bytes=WORD_BYTES):
    E = event_set(thr, base)
    ws = digest_words(d, word_bytes)
    # residue mod base; event if residue in E
    bits = np.fromiter(((w % base) in E for w in ws), dtype=np.uint8, count=len(ws))
    return bits

def long_stream_mask(digests):
    # digests: list length WINDOW; each -> 16 bits; concatenate => 512 bits
    masks = [event_mask_from_digest(d) for d in digests]
    return np.concatenate(masks)

# -----------------------------
# Features on event bitstream (geometry probes)
# -----------------------------
def feat_ac1(x):
    # lag-1 autocorrelation
    if x.std() == 0:
        return 0.0
    a = x[:-1].astype(np.float64)
    b = x[1:].astype(np.float64)
    if a.std() == 0 or b.std() == 0:
        return 0.0
    return float(np.corrcoef(a, b)[0,1])

def feat_run(x):
    # mean run length of 1s (0 if none)
    runs = []
    r = 0
    for v in x:
        if v:
            r += 1
        elif r:
            runs.append(r); r = 0
    if r: runs.append(r)
    return float(np.mean(runs)) if runs else 0.0

def feat_edge(x):
    # edge imbalance: first quarter vs last quarter
    n = len(x)
    q = n // 4
    a = x[:q].sum()
    b = x[-q:].sum()
    return float(a - b) / max(1.0, float(q))

def features(x):
    return np.array([feat_ac1(x), feat_run(x), feat_edge(x)], dtype=np.float64)

# Permute null for features: keep ones-count, randomize positions
def permuted_mask_like(x, rng_np):
    n = len(x)
    k = int(x.sum())
    out = np.zeros(n, dtype=np.uint8)
    if k > 0:
        idx = rng_np.choice(n, size=k, replace=False)
        out[idx] = 1
    return out

def zscore_against_perm(obs, perm_vals):
    mu = float(np.mean(perm_vals))
    sd = float(np.std(perm_vals, ddof=1)) if len(perm_vals) > 1 else 0.0
    if sd == 0.0:
        return 0.0
    return (float(obs) - mu) / sd

# Jaccard set similarity of event positions
def jaccard(a_idx, b_idx):
    if len(a_idx)==0 and len(b_idx)==0:
        return 1.0
    inter = len(a_idx & b_idx)
    union = len(a_idx | b_idx)
    return inter / union if union else 1.0

def jaccard_z(maskA, maskB, perm=PERM, rng_np=np_rng):
    A = set(np.flatnonzero(maskA).tolist())
    B = set(np.flatnonzero(maskB).tolist())
    J_obs = jaccard(A, B)
    # null: permute B positions preserving |B|
    n = len(maskB)
    k = len(B)
    Js = []
    for _ in range(perm):
        idx = rng_np.choice(n, size=k, replace=False) if k else np.array([], dtype=int)
        Bp = set(idx.tolist())
        Js.append(jaccard(A, Bp))
    z = zscore_against_perm(J_obs, Js)
    return J_obs, z

# -----------------------------
# Generate inputs -> digests
# -----------------------------
def make_inputs(n):
    # deterministic pseudo-random inputs
    out = []
    for i in range(n):
        msg = (f"nexus:{SEED}:{i}").encode("utf-8")
        out.append(msg)
    return out

# total digests needed
TOTAL_DIGESTS = SAMPLES * WINDOW
base_inputs = make_inputs(TOTAL_DIGESTS)
base_digests = [sha256(m) for m in base_inputs]

# chunk into samples/windows
windows = [base_digests[i*WINDOW:(i+1)*WINDOW] for i in range(SAMPLES)]

# -----------------------------
# Build long-stream masks for each transform
# -----------------------------
def build_masks_for_tx(name):
    f = TX[name]
    masks = []
    for win in windows:
        dig = [f(d) for d in win]
        masks.append(long_stream_mask(dig))
    return np.stack(masks, axis=0)  # shape: (SAMPLES, 512)

# Choose which transforms to compute (add/remove freely)
TX_LIST = [
    "raw","mul_pi","mul_e","mul_phi","mul_ephi","mul_piphi",
    "add_pi","xor_pi","xor_e","xor_phi","rot_e",
    "mix_pi","mix_pi_xor_e","mix_e_xor_pi","mix_pi_xor_rand","mix_rand_xor_pi"
]

all_masks = {name: build_masks_for_tx(name) for name in TX_LIST}

# -----------------------------
# Mask density check
# -----------------------------
print("\n=== Mask density (ones per sample) ===")
for name in TX_LIST:
    ones = all_masks[name].sum(axis=1)
    print(f"{name:16s} ones_mu={ones.mean():.2f} ones_sd={ones.std(ddof=1):.2f}")

# -----------------------------
# Feature z-scores vs perm null (mean over inputs)
# -----------------------------
print("\n=== Feature z-scores (mean over inputs): z(ac1), z(run), z(edge) ===")
for name in TX_LIST:
    Z = []
    X = all_masks[name]
    for i in range(SAMPLES):
        x = X[i]
        f_obs = features(x)
        perm_feats = []
        for _ in range(PERM):
            xp = permuted_mask_like(x, np_rng)
            perm_feats.append(features(xp))
        perm_feats = np.stack(perm_feats, axis=0)
        z = np.array([zscore_against_perm(f_obs[j], perm_feats[:,j]) for j in range(3)])
        Z.append(z)
    Z = np.stack(Z, axis=0)
    zmean = Z.mean(axis=0)
    print(f"{name:16s} z(ac1)={zmean[0]:+0.2f}  z(run)={zmean[1]:+0.2f}  z(edge)={zmean[2]:+0.2f}")

# -----------------------------
# Invariance summary (Jaccard z) for selected pairs
# -----------------------------
pairs = [
    ("mul_pi","mix_pi"),
    ("mul_pi","mix_pi_xor_e"),
    ("mul_pi","mix_pi_xor_rand"),
    ("mul_pi","mix_rand_xor_pi"),
    ("mul_e","mix_e_xor_pi"),
    ("mul_pi","xor_pi"),
    ("mul_pi","mul_e"),
]

print("\n=== Invariance summary (event-mask Jaccard z) ===")
for a,b in pairs:
    zs = []
    maxabs = 0.0
    out_idx = []
    for i in range(SAMPLES):
        J, z = jaccard_z(all_masks[a][i], all_masks[b][i], perm=PERM, rng_np=np_rng)
        zs.append(z)
        az = abs(z)
        if az > maxabs: maxabs = az
        if az >= 3.0: out_idx.append(i)
    zs = np.array(zs, dtype=np.float64)
    print(f"{a:12s} vs {b:16s} z_mu={zs.mean():+0.3f} z_sd={zs.std(ddof=1):0.3f} max|z|={maxabs:0.3f}  |z|>=3: {len(out_idx)}/{SAMPLES}")
    if out_idx:
        print(f"   outlier sample indices (first 30): {out_idx[:30]}")

```

    
    === Mask density (ones per sample) ===
    raw              ones_mu=47.60 ones_sd=6.62
    mul_pi           ones_mu=47.35 ones_sd=6.53
    mul_e            ones_mu=47.31 ones_sd=6.68
    mul_phi          ones_mu=47.84 ones_sd=6.55
    mul_ephi         ones_mu=47.64 ones_sd=6.47
    mul_piphi        ones_mu=47.27 ones_sd=6.80
    add_pi           ones_mu=47.23 ones_sd=6.59
    xor_pi           ones_mu=47.21 ones_sd=6.55
    xor_e            ones_mu=47.52 ones_sd=6.42
    xor_phi          ones_mu=47.33 ones_sd=6.72
    rot_e            ones_mu=47.48 ones_sd=6.79
    mix_pi           ones_mu=47.63 ones_sd=5.97
    mix_pi_xor_e     ones_mu=46.85 ones_sd=6.27
    mix_e_xor_pi     ones_mu=47.64 ones_sd=6.44
    mix_pi_xor_rand  ones_mu=47.54 ones_sd=6.55
    mix_rand_xor_pi  ones_mu=47.28 ones_sd=6.35
    
    === Feature z-scores (mean over inputs): z(ac1), z(run), z(edge) ===
    

    C:\Users\Developer\AppData\Local\Temp\ipykernel_1272\2520736393.py:194: RuntimeWarning: overflow encountered in scalar subtract
      return float(a - b) / max(1.0, float(q))
    

    raw              z(ac1)=+0.01  z(run)=+0.01  z(edge)=-0.01
    mul_pi           z(ac1)=+0.03  z(run)=+0.04  z(edge)=-0.07
    mul_e            z(ac1)=+0.01  z(run)=+0.01  z(edge)=-0.02
    mul_phi          z(ac1)=-0.01  z(run)=-0.02  z(edge)=+0.05
    mul_ephi         z(ac1)=+0.00  z(run)=-0.00  z(edge)=-0.09
    mul_piphi        z(ac1)=+0.08  z(run)=+0.08  z(edge)=-0.02
    add_pi           z(ac1)=+0.02  z(run)=+0.02  z(edge)=+0.11
    xor_pi           z(ac1)=-0.03  z(run)=-0.04  z(edge)=+0.00
    xor_e            z(ac1)=-0.02  z(run)=-0.02  z(edge)=+0.04
    xor_phi          z(ac1)=-0.01  z(run)=-0.01  z(edge)=+0.06
    rot_e            z(ac1)=-0.02  z(run)=-0.02  z(edge)=+0.00
    mix_pi           z(ac1)=+0.03  z(run)=+0.03  z(edge)=+0.11
    mix_pi_xor_e     z(ac1)=+0.07  z(run)=+0.07  z(edge)=-0.02
    mix_e_xor_pi     z(ac1)=+0.05  z(run)=+0.04  z(edge)=+0.02
    mix_pi_xor_rand  z(ac1)=+0.05  z(run)=+0.05  z(edge)=+0.04
    mix_rand_xor_pi  z(ac1)=-0.07  z(run)=-0.08  z(edge)=-0.14
    
    === Invariance summary (event-mask Jaccard z) ===
    mul_pi       vs mix_pi           z_mu=+0.030 z_sd=0.990 max|z|=3.497  |z|>=3: 4/512
       outlier sample indices (first 30): [109, 178, 353, 412]
    mul_pi       vs mix_pi_xor_e     z_mu=+0.033 z_sd=0.963 max|z|=3.135  |z|>=3: 3/512
       outlier sample indices (first 30): [22, 87, 379]
    mul_pi       vs mix_pi_xor_rand  z_mu=+0.018 z_sd=0.978 max|z|=4.042  |z|>=3: 1/512
       outlier sample indices (first 30): [82]
    mul_pi       vs mix_rand_xor_pi  z_mu=+0.005 z_sd=0.884 max|z|=3.301  |z|>=3: 1/512
       outlier sample indices (first 30): [464]
    mul_e        vs mix_e_xor_pi     z_mu=-0.019 z_sd=0.957 max|z|=4.067  |z|>=3: 1/512
       outlier sample indices (first 30): [337]
    mul_pi       vs xor_pi           z_mu=-0.027 z_sd=0.974 max|z|=2.917  |z|>=3: 0/512
    mul_pi       vs mul_e            z_mu=-0.037 z_sd=1.035 max|z|=4.418  |z|>=3: 3/512
       outlier sample indices (first 30): [189, 247, 395]
    


```python
# === Nexus PIN + Data Dump Logger ==========================================
import json, time, hashlib, os
from dataclasses import dataclass, asdict
from typing import Any, Dict, List, Optional

def sha16(obj: Any) -> str:
    s = json.dumps(obj, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(s).hexdigest()[:16]

@dataclass(frozen=True)
class Pin:
    MOD: int
    EVENT_RES: List[int]
    WORD_BYTES: int
    WINDOW: int
    THR: int
    EVENTS_PER_SAMPLE: int
    inputs: int
    perm: int
    seed: int
    wrap: str
    notes: str = ""

def make_pin(**kw) -> Pin:
    # canonicalize EVENT_RES
    if "EVENT_RES" in kw:
        kw["EVENT_RES"] = list(map(int, kw["EVENT_RES"]))
    return Pin(**kw)

def pin_id(pin: Pin) -> str:
    return sha16(asdict(pin))

def append_dump(pin: Pin, payload: Dict[str, Any], path: str = "nexus_pins.ndjson") -> str:
    rec = {
        "ts": time.time(),
        "pin_id": pin_id(pin),
        "pin": asdict(pin),
        "payload": payload,
    }
    with open(path, "a", encoding="utf-8") as f:
        f.write(json.dumps(rec, ensure_ascii=False) + "\n")
    return rec["pin_id"]

# --- density -> |EVENT_RES| inference (quick sanity) -----------------------
def infer_event_set_size(ones_mu: float, events_per_sample: int, MOD: int) -> int:
    # E[ones] = events_per_sample * |E| / MOD  => |E| ≈ ones_mu * MOD / events_per_sample
    return int(round((ones_mu * MOD) / max(1, events_per_sample)))

def expected_ones(events_per_sample: int, MOD: int, event_set_size: int) -> float:
    return events_per_sample * (event_set_size / MOD)

# --- example usage: fill these with YOUR run settings ----------------------
PIN = make_pin(
    MOD=65,
    EVENT_RES=[0, 1, 2, 62, 63, 64],   # <-- set this to your exact gate residues
    WORD_BYTES=2,
    WINDOW=32,
    THR=2,
    EVENTS_PER_SAMPLE=512,
    inputs=512,
    perm=300,
    seed=1337,
    wrap="mix_pi_xor_e",
    notes="long-stream port run"
)

# After you compute your summary stats, dump them like this:
# (replace these numbers with the actual computed values from your run)
summary = {
    "ones_mu": 47.60,
    "ones_sd": 6.62,
    "feature_means": {"z_ac1": None, "z_run": None, "z_edge": None},
    "warnings_fixed": True
}

pid = append_dump(PIN, summary)
print("PIN_ID:", pid)

k_hat = infer_event_set_size(summary["ones_mu"], PIN.EVENTS_PER_SAMPLE, PIN.MOD)
print("inferred |EVENT_RES| ≈", k_hat)
print("expected ones @k_hat:", expected_ones(PIN.EVENTS_PER_SAMPLE, PIN.MOD, k_hat))
print("expected ones @|EVENT_RES|:", expected_ones(PIN.EVENTS_PER_SAMPLE, PIN.MOD, len(PIN.EVENT_RES)))

```

    PIN_ID: 3b0f2a3c9923c55b
    inferred |EVENT_RES| ≈ 6
    expected ones @k_hat: 47.261538461538464
    expected ones @|EVENT_RES|: 47.261538461538464
    


```python
# === Nexus long-stream port: shape > count =================================
import hashlib, math, random
import numpy as np

# ----------------------- knobs -----------------------
INPUTS = 512          # number of samples (like your long-stream run)
WINDOW = 32           # digests per sample
WORD_BYTES = 2        # 16-bit words
MOD = 65              # your q-space
THR = 2               # kept for naming parity; gate is residue-set here
PERM = 300            # permutation baseline
SEED = 1337

# Define the port residue-set explicitly.
# You inferred |EVENT_RES|≈6; pick/adjust these 6 as you like.
EVENT_RES = {0, 1, 2, 63, 64, 30}  # <-- edit this if your current set differs

# ----------------------- helpers -----------------------
def sha256(b: bytes) -> bytes:
    return hashlib.sha256(b).digest()

def u16_words(b: bytes) -> np.ndarray:
    # little-endian 16-bit words
    assert len(b) % 2 == 0
    return np.frombuffer(b, dtype=np.uint16)

def rotl16(x: np.ndarray, r: int) -> np.ndarray:
    r &= 15
    return ((x << r) | (x >> (16 - r))) & 0xFFFF

def mix16(x: np.ndarray, k: int) -> np.ndarray:
    # simple reversible-ish mixing (not claiming cryptographic anything)
    y = x ^ (k & 0xFFFF)
    y = (y + ((y << 5) & 0xFFFF) + (y >> 3)) & 0xFFFF
    y = y ^ ((y << 7) & 0xFFFF)
    return y & 0xFFFF

# "harmonic constants" as 16-bit keys (you can swap these to your own)
K_PI  = int((math.pi  % 1) * 65536)      # fractional part scaled
K_E   = int((math.e   % 1) * 65536)
K_PHI = int((((1+5**0.5)/2) % 1) * 65536)

def wrap_words(words: np.ndarray, variant: str) -> np.ndarray:
    if variant == "raw":
        return words
    if variant == "mul_pi":
        return (words * K_PI) & 0xFFFF
    if variant == "mul_e":
        return (words * K_E) & 0xFFFF
    if variant == "mul_phi":
        return (words * K_PHI) & 0xFFFF
    if variant == "mul_ephi":
        return (words * ((K_E * K_PHI) & 0xFFFF)) & 0xFFFF
    if variant == "mul_piphi":
        return (words * ((K_PI * K_PHI) & 0xFFFF)) & 0xFFFF
    if variant == "add_pi":
        return (words + K_PI) & 0xFFFF
    if variant == "xor_pi":
        return words ^ (K_PI & 0xFFFF)
    if variant == "xor_e":
        return words ^ (K_E & 0xFFFF)
    if variant == "xor_phi":
        return words ^ (K_PHI & 0xFFFF)
    if variant == "rot_e":
        return rotl16(words, (K_E >> 12) & 0xF)  # rotate by top nibble
    if variant == "mix_pi":
        return mix16(words, K_PI)
    if variant == "mix_pi_xor_e":
        return mix16(words ^ (K_E & 0xFFFF), K_PI)
    if variant == "mix_e_xor_pi":
        return mix16(words ^ (K_PI & 0xFFFF), K_E)
    if variant == "mix_pi_xor_rand":
        return mix16(words ^ (random.getrandbits(16)), K_PI)
    if variant == "mix_rand_xor_pi":
        return mix16(words ^ (random.getrandbits(16)), K_PI)
    raise ValueError("unknown variant: " + variant)

def make_stream(seed: bytes, window: int = WINDOW) -> bytes:
    # deterministically generate WINDOW digests per sample
    out = bytearray()
    for t in range(window):
        out += sha256(seed + t.to_bytes(4, "little"))
    return bytes(out)

def event_mask_from_stream(stream_bytes: bytes, variant: str) -> np.ndarray:
    words = u16_words(stream_bytes)              # length = 16*WINDOW = 512 words
    words = wrap_words(words, variant)
    residues = (words % MOD).astype(np.int32)
    mask = np.isin(residues, list(EVENT_RES)).astype(np.uint8)  # 0/1 vector length 512
    return mask

def jaccard(a: np.ndarray, b: np.ndarray) -> float:
    # a,b are 0/1 vectors
    inter = np.sum((a == 1) & (b == 1))
    union = np.sum((a == 1) | (b == 1))
    return float(inter) / float(union) if union else 1.0

def perm_z_jaccard(a: np.ndarray, b: np.ndarray, perm: int = PERM) -> float:
    # shuffle b positions, preserve count, get baseline mean/sd for Jaccard
    js = []
    idx = np.arange(len(b))
    for _ in range(perm):
        np.random.shuffle(idx)
        bp = b[idx]
        js.append(jaccard(a, bp))
    mu = float(np.mean(js))
    sd = float(np.std(js, ddof=1)) if perm > 1 else 1.0
    return (jaccard(a, b) - mu) / (sd if sd > 1e-12 else 1.0)

# ----------------------- run -----------------------
random.seed(SEED)
np.random.seed(SEED)

variants = [
    "raw","mul_pi","mul_e","mul_phi","mul_ephi","mul_piphi",
    "add_pi","xor_pi","xor_e","xor_phi","rot_e",
    "mix_pi","mix_pi_xor_e","mix_e_xor_pi"
]

# Generate inputs
seeds = [random.randbytes(32) for _ in range(INPUTS)]
streams = [make_stream(s) for s in seeds]

# Build masks
masks = {v: [] for v in variants}
for s in streams:
    for v in variants:
        masks[v].append(event_mask_from_stream(s, v))
for v in variants:
    masks[v] = np.stack(masks[v], axis=0)  # shape (INPUTS, 512)

# Density check
print(f"\n=== Mask density (ones per sample) ===")
for v in variants:
    ones = masks[v].sum(axis=1)
    print(f"{v:14s} ones_mu={ones.mean():.2f} ones_sd={ones.std(ddof=1):.2f}")

# “Inflation stopped” prediction check
N = masks["raw"].shape[1]
pred = N * (len(EVENT_RES) / MOD)
print(f"\nPIN: EVENT_RES size={len(EVENT_RES)}, MOD={MOD}, N={N}")
print(f"expected ones ~ N*|E|/MOD = {pred:.3f}")

# Invariance (choose pairs)
pairs = [
    ("mul_pi","mix_pi"),
    ("mul_pi","mix_pi_xor_e"),
    ("mul_pi","xor_pi"),
    ("mul_e","rot_e"),
    ("mul_pi","mul_e"),
]
print(f"\n=== Invariance summary (perm-z of Jaccard) ===")
for a,b in pairs:
    zs = []
    for i in range(INPUTS):
        zs.append(perm_z_jaccard(masks[a][i], masks[b][i], perm=PERM))
    zs = np.array(zs)
    print(f"{a:10s} vs {b:14s} z_mu={zs.mean():+.3f} z_sd={zs.std(ddof=1):.3f} max|z|={np.max(np.abs(zs)):.3f}  |z|>=3: {np.sum(np.abs(zs)>=3)}/{INPUTS}")

# "Is there signal?" quick classifier:
# For each sample, decide whether it came from A or B based on which reference mask it is closer to on average.
def mean_jaccard_to_bank(xmask, bank):
    return float(np.mean([jaccard(xmask, m) for m in bank]))

A, B = "mul_pi", "mix_pi_xor_e"
bankA = masks[A][:100]   # small reference bank
bankB = masks[B][:100]
correct = 0
for i in range(100, 300):  # test slice
    xa = masks[A][i]
    xb = masks[B][i]
    # classify xa
    predA = (mean_jaccard_to_bank(xa, bankA) > mean_jaccard_to_bank(xa, bankB))
    correct += int(predA is True)
    # classify xb
    predB = (mean_jaccard_to_bank(xb, bankB) > mean_jaccard_to_bank(xb, bankA))
    correct += int(predB is True)
acc = correct / (2 * (300-100))
print(f"\n=== Shape-only classification ({A} vs {B}) ===")
print(f"accuracy={acc:.3f}  (0.50 = 'full of shit', >0.55 = 'there is geometry')")

```

    
    === Mask density (ones per sample) ===
    raw            ones_mu=47.29 ones_sd=6.79
    mul_pi         ones_mu=46.94 ones_sd=6.67
    mul_e          ones_mu=47.40 ones_sd=6.87
    mul_phi        ones_mu=47.75 ones_sd=5.91
    mul_ephi       ones_mu=47.24 ones_sd=6.77
    mul_piphi      ones_mu=47.22 ones_sd=6.39
    add_pi         ones_mu=46.79 ones_sd=6.30
    xor_pi         ones_mu=47.65 ones_sd=6.52
    xor_e          ones_mu=47.79 ones_sd=6.46
    xor_phi        ones_mu=47.66 ones_sd=6.43
    rot_e          ones_mu=46.80 ones_sd=6.58
    mix_pi         ones_mu=46.78 ones_sd=6.56
    mix_pi_xor_e   ones_mu=46.74 ones_sd=6.81
    mix_e_xor_pi   ones_mu=46.74 ones_sd=6.81
    
    PIN: EVENT_RES size=6, MOD=65, N=512
    expected ones ~ N*|E|/MOD = 47.262
    
    === Invariance summary (perm-z of Jaccard) ===
    mul_pi     vs mix_pi         z_mu=+0.150 z_sd=1.007 max|z|=4.127  |z|>=3: 5/512
    mul_pi     vs mix_pi_xor_e   z_mu=-0.165 z_sd=0.954 max|z|=2.815  |z|>=3: 0/512
    mul_pi     vs xor_pi         z_mu=+0.039 z_sd=0.971 max|z|=3.818  |z|>=3: 1/512
    mul_e      vs rot_e          z_mu=-0.076 z_sd=1.003 max|z|=3.307  |z|>=3: 1/512
    mul_pi     vs mul_e          z_mu=+0.048 z_sd=1.003 max|z|=3.097  |z|>=3: 1/512
    
    === Shape-only classification (mul_pi vs mix_pi_xor_e) ===
    accuracy=0.512  (0.50 = 'full of shit', >0.55 = 'there is geometry')
    


```python
# ============================================================
# Nexus Harmonic Hash Wrap + WORD_PORT / LONG_STREAM port tests
# Paste as ONE Jupyter cell and run.
#
# What this does (no magic claims, just structure tests):
#   1) sha256(input) -> 32-byte digest
#   2) apply "wrap" variants (mul_pi, mul_e, mul_phi, mix_pi, etc.)
#   3) convert digest to 16 x 16-bit words
#   4) "WORD_PORT" event-mask: event if (word % 65) ∈ {0,1,2,63,64}
#   5) stats: mask density, feature z-scores, Jaccard-z invariance
#   6) optional "LONG_STREAM": concatenate WINDOW digests -> 512 events/sample
#
# Requires: numpy (and stdlib).  No web.  Deterministic RNG.
# ============================================================

import hashlib, math
import numpy as np

# ---------------------------
# Config (match your prints)
# ---------------------------
MOD = 65
EVENT_RES = np.array([0, 1, 2, 63, 64], dtype=np.int16)  # |EVENT_RES|=5
THR = 2

DIGEST_BYTES = 32
WORD_BYTES = 2
WORDS_PER_DIGEST = DIGEST_BYTES // WORD_BYTES  # 16

INPUTS = 2048          # e.g. 2048
PERM = 300             # e.g. 300
WINDOW = 32            # long-stream window: 32 digests -> 512 events/sample

SEED = 1337
rng = np.random.default_rng(SEED)

# Toggle knobs if you want faster/shorter runs
DO_SINGLE_INPUT_DEMO = True
DO_WORD_PORT_BATCH = True
DO_LONG_STREAM = True

# ---------------------------
# Helpers: hash, words, bits
# ---------------------------
def sha256_bytes(b: bytes) -> bytes:
    return hashlib.sha256(b).digest()

def bytes_to_u16_words(digest32: bytes) -> np.ndarray:
    # big-endian 16-bit words (16 words)
    return np.frombuffer(digest32, dtype=">u2").astype(np.uint16, copy=False)

def u16_words_to_bytes(words: np.ndarray) -> bytes:
    return words.astype(">u2", copy=False).tobytes()

def rotl16(x: np.ndarray, r: np.ndarray) -> np.ndarray:
    r = (r & 15).astype(np.uint16)
    return ((x << r) | (x >> ((16 - r) & 15))).astype(np.uint16)

# ---------------------------
# Keys (32 bytes each)
# ---------------------------

# π key: first 8 32-bit words from "hex digits of pi" style constants (Blowfish P-array head)
K_PI = bytes.fromhex(
    "243f6a88 85a308d3 13198a2e 03707344 a4093822 299f31d0 082efa98 ec4e6c89".replace(" ", "")
)

# e key: use YOUR observed 16-bit chunk list (reassembled into 32 bytes)
# chunks: b7e1 5162 8aed 2a6a bf71 5880 9cf4 f3c7 62e7 160f 38b4 da56 a784 d904 5190 cfef
K_E = bytes.fromhex("b7e151628aed2a6abf7158809cf4f3c762e7160f38b4da56a784d9045190cfef")

# φ key: build a 32-byte schedule from the golden-ratio constant family (TEA-style stepping)
# (This is a sane, deterministic φ-ish schedule, not a "truth claim".)
def phi_schedule_bytes(nbytes=32) -> bytes:
    Q = 0x9E3779B9
    x = Q
    out = bytearray()
    while len(out) < nbytes:
        out += (x & 0xFFFFFFFF).to_bytes(4, "big")
        x = (x + Q) & 0xFFFFFFFF
    return bytes(out[:nbytes])

K_PHI = phi_schedule_bytes(32)

# random key (deterministic)
K_RAND = rng.integers(0, 256, size=32, dtype=np.uint8).tobytes()

def key_to_u16(key32: bytes) -> np.ndarray:
    return np.frombuffer(key32, dtype=">u2").astype(np.uint16, copy=False)

K16_PI  = key_to_u16(K_PI)
K16_E   = key_to_u16(K_E)
K16_PHI = key_to_u16(K_PHI)
K16_RND = key_to_u16(K_RAND)

# ---------------------------
# Wraps (digest -> digest)
# ---------------------------
def wrap_raw(d: bytes) -> bytes:
    return d

def wrap_mul(d: bytes, k16: np.ndarray) -> bytes:
    w = bytes_to_u16_words(d).copy()
    w = (w * k16) & 0xFFFF
    return u16_words_to_bytes(w)

def wrap_add(d: bytes, k16: np.ndarray) -> bytes:
    w = bytes_to_u16_words(d).copy()
    w = (w + k16) & 0xFFFF
    return u16_words_to_bytes(w)

def wrap_xor(d: bytes, k16: np.ndarray) -> bytes:
    w = bytes_to_u16_words(d).copy()
    w = (w ^ k16) & 0xFFFF
    return u16_words_to_bytes(w)

def wrap_rot(d: bytes, k16: np.ndarray) -> bytes:
    w = bytes_to_u16_words(d).copy()
    r = (k16 ^ (k16 >> 8) ^ np.arange(WORDS_PER_DIGEST, dtype=np.uint16)) & 15
    w = rotl16(w, r)
    return u16_words_to_bytes(w)

def wrap_mix_arx(d: bytes, k16: np.ndarray) -> bytes:
    """
    Lightweight ARX mixer on 16-bit words (not crypto; just a controlled "harmonic stirrer").
    """
    w = bytes_to_u16_words(d).copy()
    for i in range(WORDS_PER_DIGEST):
        j = (i - 1) % WORDS_PER_DIGEST
        r = (k16[i] + i) & 15
        w[i] = (w[i] + k16[i]) & 0xFFFF
        w[i] = rotl16(w[i:i+1], np.array([r], dtype=np.uint16))[0]
        w[i] = (w[i] ^ w[j]) & 0xFFFF
    return u16_words_to_bytes(w)

WRAPS = {
    "raw": wrap_raw,
    "mul_pi":   lambda d: wrap_mul(d, K16_PI),
    "mul_e":    lambda d: wrap_mul(d, K16_E),
    "mul_phi":  lambda d: wrap_mul(d, K16_PHI),
    "mul_ephi": lambda d: wrap_mul(d, (K16_E ^ K16_PHI) & 0xFFFF),
    "mul_piphi":lambda d: wrap_mul(d, (K16_PI ^ K16_PHI) & 0xFFFF),
    "xor_pi":   lambda d: wrap_xor(d, K16_PI),
    "xor_e":    lambda d: wrap_xor(d, K16_E),
    "xor_phi":  lambda d: wrap_xor(d, K16_PHI),
    "add_pi":   lambda d: wrap_add(d, K16_PI),
    "rot_e":    lambda d: wrap_rot(d, K16_E),
    "mix_pi":   lambda d: wrap_mix_arx(d, K16_PI),
    "mix_pi_xor_e":      lambda d: wrap_xor(wrap_mix_arx(d, K16_PI), K16_E),
    "mix_e_xor_pi":      lambda d: wrap_xor(wrap_mix_arx(d, K16_E),  K16_PI),
    "mix_pi_xor_rand":   lambda d: wrap_xor(wrap_mix_arx(d, K16_PI), K16_RND),
    "mix_rand_xor_pi":   lambda d: wrap_xor(wrap_mix_arx(d, K16_RND),K16_PI),
}

# ---------------------------
# WORD_PORT event mask
# ---------------------------
def word_port_mask_from_digest(d: bytes) -> np.ndarray:
    """
    Returns bool mask length 16.
    Event if (word % 65) in EVENT_RES.
    """
    w = bytes_to_u16_words(d).astype(np.int32, copy=False)
    r = (w % MOD).astype(np.int16, copy=False)
    return np.isin(r, EVENT_RES)

def long_stream_mask(digests: list[bytes], window: int) -> np.ndarray:
    """
    Concatenate WORD_PORT masks for `window` digests -> bool vector length 16*window.
    """
    masks = [word_port_mask_from_digest(d) for d in digests[:window]]
    return np.concatenate(masks, axis=0)

# ---------------------------
# Features on a 0/1 mask
# ---------------------------
def feat_ac1(x01: np.ndarray) -> float:
    x = x01.astype(np.float64, copy=False)
    if x.size < 2:
        return 0.0
    a = x[:-1]; b = x[1:]
    sa = a.std(); sb = b.std()
    if sa == 0 or sb == 0:
        return 0.0
    return float(((a - a.mean()) * (b - b.mean())).mean() / (sa * sb))

def feat_run(x01: np.ndarray) -> float:
    # mean run-length of 1-runs
    x = x01.astype(np.uint8, copy=False)
    if x.sum() == 0:
        return 0.0
    runs = []
    cur = 0
    for v in x:
        if v:
            cur += 1
        else:
            if cur:
                runs.append(cur)
                cur = 0
    if cur:
        runs.append(cur)
    return float(np.mean(runs)) if runs else 0.0

def feat_edge(x01: np.ndarray) -> float:
    x = x01.astype(np.uint8, copy=False)
    if x.size < 2:
        return 0.0
    return float(np.mean(x[1:] ^ x[:-1]))

def feature_zscores(x01: np.ndarray, perm: int, rng_local: np.random.Generator) -> tuple[float,float,float]:
    """
    Permute positions (preserve ones count), compute z for (ac1, run, edge).
    """
    obs = np.array([feat_ac1(x01), feat_run(x01), feat_edge(x01)], dtype=np.float64)

    n = x01.size
    ones = int(x01.sum())
    if n < 2:
        return (0.0, 0.0, 0.0)

    null = np.zeros((perm, 3), dtype=np.float64)
    for t in range(perm):
        idx = rng_local.choice(n, size=ones, replace=False)
        y = np.zeros(n, dtype=bool)
        y[idx] = True
        null[t, 0] = feat_ac1(y)
        null[t, 1] = feat_run(y)
        null[t, 2] = feat_edge(y)

    mu = null.mean(axis=0)
    sd = null.std(axis=0, ddof=1)
    sd = np.where(sd == 0, 1.0, sd)
    z = (obs - mu) / sd
    return float(z[0]), float(z[1]), float(z[2])

# ---------------------------
# Jaccard + Jaccard-z
# ---------------------------
def jaccard(a: np.ndarray, b: np.ndarray) -> float:
    inter = int(np.logical_and(a, b).sum())
    uni = int(np.logical_or(a, b).sum())
    return 1.0 if uni == 0 else inter / uni

def jaccard_z(a: np.ndarray, b: np.ndarray, perm: int, rng_local: np.random.Generator) -> tuple[float,float]:
    """
    Permute B positions (preserve ones count) to get a null for J(A, B).
    Returns (J_obs, z).
    """
    J_obs = jaccard(a, b)
    n = a.size
    ones = int(b.sum())
    null = np.zeros(perm, dtype=np.float64)
    for t in range(perm):
        idx = rng_local.choice(n, size=ones, replace=False)
        bp = np.zeros(n, dtype=bool)
        bp[idx] = True
        null[t] = jaccard(a, bp)
    mu = float(null.mean())
    sd = float(null.std(ddof=1)) or 1.0
    z = (J_obs - mu) / sd
    return J_obs, float(z)

# ---------------------------
# Input generator
# ---------------------------
def make_inputs(n: int, msg_bytes: int = 64) -> list[bytes]:
    return [rng.bytes(msg_bytes) for _ in range(n)]

# ============================================================
# 1) SINGLE INPUT DEMO (matches your “Single input demo” vibe)
# ============================================================
if DO_SINGLE_INPUT_DEMO:
    print("\n=== Single input demo ===\n")
    x = rng.bytes(64)
    d0 = sha256_bytes(x)

    local = np.random.default_rng(SEED + 1)
    for name in [
        "raw","mul_pi","mul_e","mul_phi","mul_ephi","mul_piphi",
        "xor_phi","add_pi","rot_e","mix_pi"
    ]:
        dd = WRAPS[name](d0)
        m = word_port_mask_from_digest(dd)
        z1,z2,z3 = feature_zscores(m, perm=PERM, rng_local=local)
        print(f"{name:<10s}  z(ac1)={z1:+.2f}  z(run)={z2:+.2f}  z(edge)={z3:+.2f}")

# ============================================================
# 2) WORD_PORT batch: mask density + invariance summary
# ============================================================
if DO_WORD_PORT_BATCH:
    print(f"\n\n=== Word-level port: WORD_BYTES={WORD_BYTES} (events per digest = {WORDS_PER_DIGEST}), THR={THR} ===\n")
    inputs = make_inputs(INPUTS)
    dig = [sha256_bytes(b) for b in inputs]

    # Precompute masks for each wrap
    masks = {}
    ones_stats = {}
    for name, fn in WRAPS.items():
        mm = np.zeros((INPUTS, WORDS_PER_DIGEST), dtype=bool)
        for i in range(INPUTS):
            dd = fn(dig[i])
            mm[i] = word_port_mask_from_digest(dd)
        masks[name] = mm
        ones = mm.sum(axis=1).astype(np.int32)
        ones_stats[name] = (float(ones.mean()), float(ones.std(ddof=1)))

    print("=== Mask density check (ones per digest) ===")
    for name in sorted(ones_stats.keys()):
        mu, sd = ones_stats[name]
        print(f"{name:<16s} ones_mu={mu:.2f}  ones_sd={sd:.2f}")

    # Invariance pairs you’ve been watching
    PAIRS = [
        ("mul_pi","mix_pi"),
        ("mul_pi","mix_pi_xor_e"),
        ("mul_pi","mix_pi_xor_rand"),
        ("mul_pi","mix_rand_xor_pi"),
        ("mul_e","mix_e_xor_pi"),
        ("mul_pi","xor_pi"),
        ("mul_pi","mul_e"),
    ]

    print(f"\n\n=== Invariance summary (inputs={INPUTS}, perm={PERM}, thr={THR}) ===")
    local = np.random.default_rng(SEED + 2)

    for a_name, b_name in PAIRS:
        z_list = np.zeros(INPUTS, dtype=np.float64)
        for i in range(INPUTS):
            _, z = jaccard_z(masks[a_name][i], masks[b_name][i], perm=PERM, rng_local=local)
            z_list[i] = z
        z_mu = float(z_list.mean())
        z_sd = float(z_list.std(ddof=1))
        maxabs = float(np.max(np.abs(z_list)))
        ge3 = int(np.sum(np.abs(z_list) >= 3.0))
        print(f"{a_name:<11s} vs {b_name:<15s} z_mu={z_mu:+.3f} z_sd={z_sd:.3f} max|z|={maxabs:.3f}  |z|>=3: {ge3}/{INPUTS}")

# ============================================================
# 3) LONG_STREAM: concatenate WINDOW digests -> 512 events/sample
# ============================================================
if DO_LONG_STREAM:
    # Smaller default so this doesn't melt your session. You can raise back to 512+.
    LS_INPUTS = 512

    print("\n\n=== Long-stream port ===")
    print(f"WORD_BYTES={WORD_BYTES}  WINDOW={WINDOW}  events/sample={WORDS_PER_DIGEST*WINDOW}  THR={THR}")
    print(f"inputs={LS_INPUTS}  perm={PERM}\n")

    inputs = make_inputs(LS_INPUTS * WINDOW)
    dig = [sha256_bytes(b) for b in inputs]

    # For each sample, take a WINDOW-sized chunk of digests.
    def sample_digests(i):
        return dig[i*WINDOW:(i+1)*WINDOW]

    long_masks = {}
    ones_stats = {}
    feat_means = {}

    for name, fn in WRAPS.items():
        mm = np.zeros((LS_INPUTS, WORDS_PER_DIGEST*WINDOW), dtype=bool)
        for i in range(LS_INPUTS):
            dwin = [fn(d) for d in sample_digests(i)]
            mm[i] = long_stream_mask(dwin, WINDOW)
        long_masks[name] = mm
        ones = mm.sum(axis=1).astype(np.int32)
        ones_stats[name] = (float(ones.mean()), float(ones.std(ddof=1)))

    print("=== Mask density (ones per sample) ===")
    for name in sorted(ones_stats.keys()):
        mu, sd = ones_stats[name]
        print(f"{name:<16s} ones_mu={mu:.2f} ones_sd={sd:.2f}")

    # Feature z-scores averaged over samples (this is the expensive bit)
    print("\n\n=== Feature z-scores (mean over inputs): z(ac1), z(run), z(edge) ===")
    local = np.random.default_rng(SEED + 3)
    for name in sorted(long_masks.keys()):
        z1s = np.zeros(LS_INPUTS, dtype=np.float64)
        z2s = np.zeros(LS_INPUTS, dtype=np.float64)
        z3s = np.zeros(LS_INPUTS, dtype=np.float64)
        for i in range(LS_INPUTS):
            z1,z2,z3 = feature_zscores(long_masks[name][i], perm=PERM, rng_local=local)
            z1s[i], z2s[i], z3s[i] = z1, z2, z3
        print(f"{name:<16s} z(ac1)={z1s.mean():+.2f}  z(run)={z2s.mean():+.2f}  z(edge)={z3s.mean():+.2f}")

    # Invariance summary (same pairs)
    PAIRS = [
        ("mul_pi","mix_pi"),
        ("mul_pi","mix_pi_xor_e"),
        ("mul_pi","mix_pi_xor_rand"),
        ("mul_pi","mix_rand_xor_pi"),
        ("mul_e","mix_e_xor_pi"),
        ("mul_pi","xor_pi"),
        ("mul_pi","mul_e"),
    ]

    print("\n\n=== Invariance summary (event-mask Jaccard z) ===")
    local = np.random.default_rng(SEED + 4)
    for a_name, b_name in PAIRS:
        z_list = np.zeros(LS_INPUTS, dtype=np.float64)
        for i in range(LS_INPUTS):
            _, z = jaccard_z(long_masks[a_name][i], long_masks[b_name][i], perm=PERM, rng_local=local)
            z_list[i] = z
        z_mu = float(z_list.mean())
        z_sd = float(z_list.std(ddof=1))
        maxabs = float(np.max(np.abs(z_list)))
        ge3 = int(np.sum(np.abs(z_list) >= 3.0))
        print(f"{a_name:<11s} vs {b_name:<15s} z_mu={z_mu:+.3f} z_sd={z_sd:.3f} max|z|={maxabs:.3f}  |z|>=3: {ge3}/{LS_INPUTS}")

```

    
    === Single input demo ===
    
    raw         z(ac1)=-0.14  z(run)=-0.34  z(edge)=-0.77
    mul_pi      z(ac1)=+0.00  z(run)=+0.00  z(edge)=+0.00
    mul_e       z(ac1)=-0.49  z(run)=-0.44  z(edge)=+0.70
    mul_phi     z(ac1)=-0.36  z(run)=+0.00  z(edge)=+0.36
    mul_ephi    z(ac1)=-0.37  z(run)=+0.00  z(edge)=+0.37
    mul_piphi   z(ac1)=-0.22  z(run)=-0.40  z(edge)=-0.59
    xor_phi     z(ac1)=-0.86  z(run)=-0.63  z(edge)=+1.12
    add_pi      z(ac1)=-0.36  z(run)=+0.00  z(edge)=+0.36
    rot_e       z(ac1)=-0.42  z(run)=+0.00  z(edge)=+0.42
    mix_pi      z(ac1)=+1.53  z(run)=+0.79  z(edge)=-1.62
    
    
    === Word-level port: WORD_BYTES=2 (events per digest = 16), THR=2 ===
    
    

    C:\Users\Developer\AppData\Local\Temp\ipykernel_1272\3909667093.py:131: RuntimeWarning: overflow encountered in scalar add
      w[i] = (w[i] + k16[i]) & 0xFFFF
    

    === Mask density check (ones per digest) ===
    add_pi           ones_mu=1.22  ones_sd=1.05
    mix_e_xor_pi     ones_mu=1.22  ones_sd=1.06
    mix_pi           ones_mu=1.18  ones_sd=1.06
    mix_pi_xor_e     ones_mu=1.23  ones_sd=1.07
    mix_pi_xor_rand  ones_mu=1.21  ones_sd=1.04
    mix_rand_xor_pi  ones_mu=1.21  ones_sd=1.07
    mul_e            ones_mu=1.23  ones_sd=1.05
    mul_ephi         ones_mu=2.15  ones_sd=1.04
    mul_phi          ones_mu=1.22  ones_sd=1.08
    mul_pi           ones_mu=1.26  ones_sd=1.11
    mul_piphi        ones_mu=1.22  ones_sd=1.05
    raw              ones_mu=1.23  ones_sd=1.05
    rot_e            ones_mu=1.25  ones_sd=1.07
    xor_e            ones_mu=1.26  ones_sd=1.08
    xor_phi          ones_mu=1.24  ones_sd=1.10
    xor_pi           ones_mu=1.22  ones_sd=1.06
    
    
    === Invariance summary (inputs=2048, perm=300, thr=2) ===
    mul_pi      vs mix_pi          z_mu=-0.001 z_sd=0.714 max|z|=5.677  |z|>=3: 21/2048
    mul_pi      vs mix_pi_xor_e    z_mu=+0.001 z_sd=0.730 max|z|=5.078  |z|>=3: 22/2048
    mul_pi      vs mix_pi_xor_rand z_mu=+0.021 z_sd=0.767 max|z|=6.530  |z|>=3: 27/2048
    mul_pi      vs mix_rand_xor_pi z_mu=-0.032 z_sd=0.669 max|z|=4.512  |z|>=3: 21/2048
    mul_e       vs mix_e_xor_pi    z_mu=+0.026 z_sd=0.784 max|z|=5.677  |z|>=3: 34/2048
    mul_pi      vs xor_pi          z_mu=-0.003 z_sd=0.699 max|z|=4.891  |z|>=3: 20/2048
    mul_pi      vs mul_e           z_mu=+0.045 z_sd=0.803 max|z|=5.677  |z|>=3: 28/2048
    
    
    === Long-stream port ===
    WORD_BYTES=2  WINDOW=32  events/sample=512  THR=2
    inputs=512  perm=300
    
    === Mask density (ones per sample) ===
    add_pi           ones_mu=39.15 ones_sd=6.08
    mix_e_xor_pi     ones_mu=39.31 ones_sd=6.18
    mix_pi           ones_mu=39.54 ones_sd=6.06
    mix_pi_xor_e     ones_mu=39.39 ones_sd=5.79
    mix_pi_xor_rand  ones_mu=39.30 ones_sd=5.89
    mix_rand_xor_pi  ones_mu=39.21 ones_sd=6.26
    mul_e            ones_mu=39.09 ones_sd=6.55
    mul_ephi         ones_mu=68.88 ones_sd=5.77
    mul_phi          ones_mu=39.44 ones_sd=6.12
    mul_pi           ones_mu=39.09 ones_sd=5.95
    mul_piphi        ones_mu=38.82 ones_sd=5.95
    raw              ones_mu=39.23 ones_sd=6.11
    rot_e            ones_mu=39.21 ones_sd=6.04
    xor_e            ones_mu=39.22 ones_sd=6.03
    xor_phi          ones_mu=39.54 ones_sd=6.19
    xor_pi           ones_mu=39.20 ones_sd=6.25
    
    
    === Feature z-scores (mean over inputs): z(ac1), z(run), z(edge) ===
    add_pi           z(ac1)=+0.08  z(run)=+0.08  z(edge)=-0.09
    mix_e_xor_pi     z(ac1)=-0.02  z(run)=-0.02  z(edge)=+0.01
    mix_pi           z(ac1)=-0.05  z(run)=-0.05  z(edge)=+0.05
    mix_pi_xor_e     z(ac1)=+0.00  z(run)=+0.01  z(edge)=-0.01
    mix_pi_xor_rand  z(ac1)=-0.03  z(run)=-0.03  z(edge)=+0.03
    mix_rand_xor_pi  z(ac1)=+0.02  z(run)=+0.02  z(edge)=-0.01
    mul_e            z(ac1)=-0.03  z(run)=-0.03  z(edge)=+0.03
    mul_ephi         z(ac1)=-0.63  z(run)=-0.60  z(edge)=+0.64
    mul_phi          z(ac1)=-0.05  z(run)=-0.05  z(edge)=+0.05
    mul_pi           z(ac1)=+0.04  z(run)=+0.04  z(edge)=-0.04
    mul_piphi        z(ac1)=+0.06  z(run)=+0.06  z(edge)=-0.06
    raw              z(ac1)=+0.01  z(run)=+0.02  z(edge)=-0.01
    rot_e            z(ac1)=-0.02  z(run)=-0.02  z(edge)=+0.02
    xor_e            z(ac1)=-0.04  z(run)=-0.04  z(edge)=+0.04
    xor_phi          z(ac1)=-0.04  z(run)=-0.04  z(edge)=+0.04
    xor_pi           z(ac1)=-0.12  z(run)=-0.12  z(edge)=+0.12
    
    
    === Invariance summary (event-mask Jaccard z) ===
    mul_pi      vs mix_pi          z_mu=-0.033 z_sd=1.000 max|z|=2.903  |z|>=3: 0/512
    mul_pi      vs mix_pi_xor_e    z_mu=+0.055 z_sd=1.009 max|z|=3.244  |z|>=3: 3/512
    mul_pi      vs mix_pi_xor_rand z_mu=-0.001 z_sd=1.027 max|z|=4.417  |z|>=3: 5/512
    mul_pi      vs mix_rand_xor_pi z_mu=-0.048 z_sd=0.929 max|z|=3.407  |z|>=3: 1/512
    mul_e       vs mix_e_xor_pi    z_mu=+0.013 z_sd=0.991 max|z|=3.256  |z|>=3: 2/512
    mul_pi      vs xor_pi          z_mu=+0.125 z_sd=1.009 max|z|=3.427  |z|>=3: 4/512
    mul_pi      vs mul_e           z_mu=-0.092 z_sd=0.954 max|z|=3.450  |z|>=3: 2/512
    


```python

```
