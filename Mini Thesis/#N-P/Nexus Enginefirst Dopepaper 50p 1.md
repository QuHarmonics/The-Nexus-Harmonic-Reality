# The Nexus Engine‑First Architecture
A Grand Unified Specification of Observerless Computation
Version 1.0 (Expanded “Dope Paper” Edition)

**BBP ⇄ π, SILR, Samson‑style gating, SHA mirrors, primes as pins, e↔φ breath, and the +4/+56 residue grid**

**Dean Kulik (concept)
Compiled & expanded in Nexus style (Markdown + LaTeX)
Date: January 2026**

---

## Abstract

**Nexus** (Recursive Harmonic Architecture; RHA) is written “verbs‑first”: *process precedes object*. This paper is an engine‑first specification—an attempt to describe a self‑consistent computational substrate where **stable structure is what survives recursive pressure**, and where “constants” arise as **fixed points / attractors** of update rules.

We treat three constructs as the core demonstrators:

1) **BBP ⇄ π**: the Bailey–Borwein–Plouffe series as a *digit‑rendering engine* in base‑16, with “π” understood as the observer’s name for the series limit.
2) **SILR / Samson gating**: a control law expressed as a significance ratio $z_t$ that is (by design) insensitive to absolute noise scale—capturing the intuition that *existence is a bandwidth*.
3) **Affine residue grid**: a 2‑D deterministic lattice that looks hash‑random until the frame is rotated into the generator’s coordinates.

Along the way we connect SHA‑256’s “mirrored” length discipline to infrastructure↔application asymmetry, show the Fibonacci‑indexed approximation $e_n=(1+1/F_n)^{F_n}\to e$ as an **$e\leftrightarrow\varphi$ bridge**, and lay out a reproducible experiment set (normality tests, discrepancy tests, gate simulations, lattice diagnostics). Where claims are mathematical theorems we label them as such; where claims are *operational metaphors* we label them too. The goal is not to force a single metaphysics, but to provide a **complete runnable spec** for the Nexus style of thinking.

---


## Table of Contents

- [0. Reading Mode: Verbs First](#0-reading-mode-verbs-first)
- [1. Engine‑First Ontology](#1-engine-first-ontology)
- [2. BBP as Digit Engine](#2-bbp-as-digit-engine)
- [3. π as Name, Limit, and Exhaust](#3-π-as-name-limit-and-exhaust)
- [4. SILR and the Samson‑Style Gate](#4-silr-and-the-samson-style-gate)
- [5. SHA‑256 as Mirror](#5-sha-256-as-mirror)
- [6. Primes, Twin Primes, and “Pins”](#6-primes-twin-primes-and-pins)
- [7. $e\leftrightarrow\varphi$: Breathing Irrationals](#7-evarphi-breathing-irrationals)
- [8. The +4/+56 Residue Grid](#8-the-456-residue-grid)
- [9. What Is Actually Testable](#9-what-is-actually-testable)
- [10. Nexus Protocols](#10-nexus-protocols)
- [11. Synthesis: The Mirror Discovery](#11-synthesis-the-mirror-discovery)
- [Appendix A. Core Formulas](#appendix-a-core-formulas)
- [Appendix B. Code](#appendix-b-code)
- [Appendix C. Tables](#appendix-c-tables)

---

## 0. Reading Mode: Verbs First

Read this document like this:

- **Verb layer**: what *operates* (updates, folds, gates, projects, samples).
- **Noun layer**: what *persists* (objects, constants, glyphs, states).

In Nexus framing:

- **Objects** are stable *gap‑patterns* (persistent differences $\Delta$).
- **Truth** is survival under recursion (what survives repeated update).
- **Randomness** is often a *projection artifact* (wrong basis / wrong frame).

Keep that orientation. It matters.

---

## 1. Engine‑First Ontology

### 1.1 The impossibility challenge

Try to design a universe that *works* but is *not computational*.

To “work” you need:

- distinguishable states,
- rules (constraints) on states,
- transitions between states.

That trio is computation by definition. So the question “is reality computational?” can be reframed:

> If reality has stable states, constraints, and transitions, then computation is not an optional metaphor; it is the operational substrate.

### 1.2 Observerless computation vs observer‑named outputs

A key Nexus insistence is **decoupling**:

- The **engine** runs without the observer.
- The **name** (“π”, “e”, “hash”, “entropy”) is applied by the observer *after* the fact.

This is the “mind the gaps” move: separate the generator from the label.

### 1.3 What “fold” means here

When you say “even folds, odd doesn’t,” you’re pointing at an operation boundary:

- even $\Rightarrow$ divisible by $2$ $\Rightarrow$ admits a clean halving map,
- odd $\Rightarrow$ forces remainders and carry, which is where *structure* can persist under repeated reduction.

In this paper we use **folding** to mean: a deterministic map that compresses state while preserving invariants (or preserving enough structure to be recognized later).

---

## 2. BBP as Digit Engine

### 2.1 The BBP series

The classical BBP identity is:

$$
\pi = \sum_{k=0}^{\infty} \frac{1}{16^k}
\left(\frac{4}{8k+1} - \frac{2}{8k+4} - \frac{1}{8k+5} - \frac{1}{8k+6}\right).
$$

Two readings:

- **Math reading**: an infinite series equals a real number.
- **Engine reading**: a fixed update rule emits a base‑16 digit stream when sampled.

### 2.2 Digit extraction as “rendering”

BBP is famous because it enables **hex digit extraction** without computing all prior digits.
A standard way to express “digit $n$” is to isolate fractional parts of sums of the form:

$$
\{16^n\pi\} = \left\{\sum_{k=0}^{\infty} \frac{16^{n-k}}{1}
\left(\frac{4}{8k+1} - \frac{2}{8k+4} - \frac{1}{8k+5} - \frac{1}{8k+6}\right)\right\},
$$

then compute

$$
d_n = \left\lfloor 16\,\{16^n\pi\}\right\rfloor \in \{0,1,\dots,15\}
$$

as the $n$‑th hexadecimal digit.

### 2.3 “BBP doesn’t know π” (decoupling made precise)

Engine‑first framing says:

- BBP is a deterministic operator on integers and rationals.
- The output digit stream is what it is.
- Calling the limit “π” is an observer move.

That’s coherent. Here’s the precise statement that preserves both truths:

1) Define a number $x$ by the BBP series:
$$x := \sum_{k=0}^{\infty} \frac{1}{16^k}\left(\frac{4}{8k+1}-\frac{2}{8k+4}-\frac{1}{8k+5}-\frac{1}{8k+6}\right).$$
2) A theorem (proved in the BBP paper) shows $x=\pi$.

In other words: **π “lives” in the equivalence class of representations**, not as an intention inside the engine.
The engine can be run by an agent who has never heard the word “π”; they still obtain the same digits. Naming comes later.

### 2.4 “What input breaks BBP?”

Mathematically, no finite $n$ breaks digit extraction: the identities are defined for all non‑negative integers $n$.
Practically, physical machines have resource limits (time/memory/precision), but that’s a hardware limit—not a formula limit.

---

## 3. π as Name, Limit, and Exhaust

### 3.1 The synth analogy (kept, but cleaned)

A synthesizer is a stable mapping:

- input (key/trigger) $\rightarrow$ deterministic oscillation,
- projection (speaker/ear) $\rightarrow$ audible waveform,
- “this sounds like a piano” $\rightarrow$ observer labeling.

BBP fits this structure:

- integer index $n$ is the trigger,
- modular arithmetic and weighted series are the oscillator,
- base‑16 digit readout is the projection,
- “that digit stream matches π” is the observer label.

The key is **not** that BBP “contains π,” but that **π is the name for the stable attractor of that operator**.

### 3.2 Normality: two meanings

People use “π is normal” in two different ways:

1) **Operational‑infinite**: the digit stream never halts (you can keep generating digits forever in principle).
2) **Statistical normality**: every finite block of digits occurs with the expected limiting frequency.

BBP supports (1) immediately: the process can be iterated for arbitrarily large indices.
BBP does **not** by itself prove (2). Statistical normality for π remains unproved in standard mathematics.

That gap matters. Nexus can treat it as *SILR territory* (self‑normalization), but the proof obligation is real.

---

## 4. SILR and the Samson‑Style Gate

### 4.1 Core control variables

We write a control loop in the simplest Nexus form:

- measured state: $\hat\alpha_t$ (scope exponent / order indicator)
- target: $\alpha^*$ (Mark‑1 attractor; typically $\alpha^*=H$)
- noise scale: $SE_t$ (standard error / entropy proxy)

Define the *significance* of deviation as

$$
z_t = \frac{|\hat\alpha_t-\alpha^*|}{SE_t}.
$$

### 4.2 Leakage as a logistic gate

A soft gate can be written:

$$
p_t = \frac{1}{1+e^{-\beta(z_t-z_0)}}
$$

where:

- $z_0$ is the threshold (bandwidth of allowed deviation)
- $\beta$ is gate hardness (gain).

Interpretation:

- $z_t<z_0$ $\Rightarrow$ low leakage (structure persists)
- $z_t>z_0$ $\Rightarrow$ high leakage (state dissolves)

### 4.3 SILR: scale‑invariant leakage regime

SILR is the regime where leakage depends on *relative* deviation, not absolute magnitude.
That is the point of the ratio $z_t$.

If both numerator and denominator scale with environmental intensity, then $z_t$ can stay stable:

$$
|\hat\alpha_t-\alpha^*|\propto SE_t\quad\Rightarrow\quad z_t\approx\text{const}.
$$

### 4.4 The attractor $H=\pi/9$ (Mark‑1)

The Mark‑1 constant is defined as

$$
H = \frac{\pi}{9} \approx 0.3490658503988659.
$$

Engine‑first reading: $H$ is a *chosen* or *selected* operating point, not a mystical property.
The claim “stable feedback lives near $\approx 0.35$” is an empirical/engineering claim: test it across domains.

### 4.5 Two biasing protocols (noise up vs noise down)

Using $z_t=|\hat\alpha_t-\alpha^*|/SE_t$:

- **Forward SILR** (“God mode”): increase $SE_t$ so $z_t$ falls below threshold.
  $$SE_t\uparrow\Rightarrow z_t\downarrow.$$
- **Reverse SILR** (“Creation mode”): decrease $SE_t$ so $z_t$ becomes strict.
  $$SE_t\downarrow\Rightarrow z_t\uparrow.$$

These are control‑law statements. Whether they map to vacuum physics is a separate hypothesis.

---

## 5. SHA‑256 as Mirror

### 5.1 The mirror asymmetry: length written last, needed first

SHA‑256 preprocessing is (conceptually):

1) append a single ‘1’ bit,
2) append ‘0’ bits until length $\equiv 448 \pmod{512}$,
3) append the 64‑bit message length.

Forward direction:

$$\text{MESSAGE}\to\text{STOP}\to\text{PADDING}\to\text{LENGTH}.$$

Reverse parsing direction:

$$\text{LENGTH}\to\text{PADDING}\to\text{STOP}\to\text{MESSAGE}.$$

This is the “infrastructure runs backwards from application” intuition.

### 5.2 Prime‑root constants as diffusion scaffolding

SHA‑256 uses:

- initial values $H_0[i] = \lfloor 2^{32}\,\{\sqrt{p_i}\}\rfloor$,
- round constants $K[i] = \lfloor 2^{32}\,\{\sqrt[3]{p_i}\}\rfloor$,

where $p_i$ are primes and $\{x\}$ is fractional part.

Nexus framing: primes act as “sync pins”; root‑fractionals spread bits with good diffusion.
This is engineering, not mysticism.

### 5.3 A concrete “near‑H” coincidence you can actually compute

Let $H=\pi/9$.
For the 6th prime $13$ (index 5 if counting from 0):

$$
\{\sqrt[3]{13}\}\approx 0.3513346876,
\quad |\{\sqrt[3]{13}\}-H|\approx 0.0022688372\; (\approx 0.65\%\text{ of }H).
$$

This is a measurable proximity claim. Whether it’s structural or accidental is testable:
scan all 64 constants and rank distances.

### 5.4 Twin primes in rotation constants

In the message schedule, SHA‑256 uses

$$
\sigma_1(x)=\operatorname{ROTR}^{17}(x)\oplus\operatorname{ROTR}^{19}(x)\oplus\operatorname{SHR}^{10}(x).
$$

$17$ and $19$ are a twin prime pair. Nexus reads this as “boundary markers.”
Engineering reads it as “good mixing offsets.” Both can be true.

---

## 6. Primes, Twin Primes, and “Pins”

### 6.1 What is exact vs what is poetic

Exact:

- primes are integers with no nontrivial divisors,
- twin primes are prime pairs with gap 2.

Poetic/operational:

- primes are places where division ‘breaks cleanly’,
- twin primes act like *sampling anchors* (“Nyquist pins”).

### 6.2 Nyquist theorem (the actual theorem)

Nyquist–Shannon sampling says: a band‑limited signal of max frequency $f_{max}$ can be reconstructed from samples at $\ge 2f_{max}$.

Nexus analogy: in number‑field “spectra,” regions of high information density demand denser sampling. Twin primes are an evocative way to talk about minimum gaps.

### 6.3 How to test the “pin” idea without hand‑waving

Define a numeric proxy for “information density” along the integers (choose one):

- local entropy of residues,
- discrepancy of digit sequences,
- compressibility of windows,
- spectral flatness of modular orbits.

Then test whether twin prime neighborhoods correlate with extremal values of that proxy.

---

## 7. $e\leftrightarrow\varphi$: Breathing Irrationals

### 7.1 The bridge construction

Let $F_n$ be Fibonacci numbers:

$$
F_0=0,\;F_1=1,\;F_n=F_{n-1}+F_{n-2}\ (n\ge 2).
$$

The golden ratio is the limit of ratios:

$$
\varphi = \lim_{n\to\infty}\frac{F_{n+1}}{F_n} = \frac{1+\sqrt{5}}{2} \approx 1.6180339887.
$$

Define a Fibonacci‑indexed approximation to $e$:

$$
e_n = \left(1+\frac{1}{F_n}\right)^{F_n}.
$$

As $n\to\infty$, $F_n\to\infty$, so we inherit the classic limit:

$$
\lim_{m\to\infty}\left(1+\frac{1}{m}\right)^m = e.
$$

Therefore:

$$
\lim_{n\to\infty} e_n = e.
$$

### 7.2 Error scale (why it drops fast)

Using the expansion $\ln(1+1/m)=1/m-1/(2m^2)+O(1/m^3)$:

$$
\left(1+\frac{1}{m}\right)^m = e\left(1-\frac{1}{2m}+O\left(\frac{1}{m^2}\right)\right).
$$

So for $m=F_n$:

$$
|e_n-e|\approx \frac{e}{2F_n}.
$$

Since $F_n\sim \varphi^n/\sqrt{5}$, the error decays like $O(\varphi^{-n})$.

### 7.3 Timeless integers vs breathing irrationals

A crisp computational metaphor:

- Integers can be represented exactly in finite precision (sometimes), so “error can be zero.”
- Irrationals can’t be represented exactly in finite bits, so “error never reaches zero,” forcing perpetual refinement.

That’s one way to formalize “breathing” vs “halt.”

---

## 8. The +4/+56 Residue Grid

### 8.1 The generator (exact)

Define a 2‑D lattice indexed by integers $a,b\ge 1$.
Seed residue at $(1,1)$ is 53.
Vertical step (increase $a$): +4.
Horizontal step (increase $b$): +56.
Wrap by mod 100.

Exact formula:

$$
r(a,b) = \bigl(53 + 4(a-1) + 56(b-1)\bigr)\bmod 100.
$$

Optionally apply a *mask* (a frame):

$$
\text{show}(a,b)=\mathbf{1}[a+b\le 10].
$$

### 8.2 Why it looks random

This is an affine map on $\mathbb{Z}_{100}$; it’s deterministic.
It looks random because:

- you’re viewing a 2‑D orbit through a lossy mask,
- mod 100 scrambles decimal representation,
- then you *reproject* into ASCII windows (33–126).

Chaos is in the projection, not the generator.

### 8.3 The 9×9 masked grid (exact example)

Using the mask $a+b\le 10$ within a $9\times 9$ crop gives 45 visible cells.
Since total cells are 81:

$$
\rho=\frac{45}{81}=\frac{5}{9}\approx 0.555\ldots
$$

If you see a claim like $45/129\approx 0.3488$ (close to $H$), that depends on a different definition of the denominator.
Keep denominators honest; frames matter.

### 8.4 The “π via 3.5” idea (interpretive)

The step ratio is exact:

$$\frac{56}{4}=14.$$

One interpretive embedding is to note:

$$56 = 16\cdot 3.5 = 16\cdot \frac{7}{2}.$$

Since $16$ is the BBP base, and $7/2$ is a crude overestimate of $\pi$,
the “residual” is:

$$
\epsilon = 3.5-\pi \approx 0.3584073464.
$$

Compare to $H=\pi/9\approx 0.3490658504$.
This is *close*, not equal.

Correct reading:

- Exact: the grid is an affine lattice with steps 4 and 56.
- Interpretive: choosing 56 as $16\cdot(7/2)$ makes the step ‘look like’ hex‑base times a rough circle constant.
- If you want to claim a structural link to $H$, you must define a mechanism that maps $\epsilon$ to $H$ (or explain why the observed closeness is expected).

### 8.5 Periods and classification (exact)

Because the update is linear mod 100, periods are determined by gcds:

- vertical period: smallest $p_a$ with $4p_a\equiv 0\pmod{100}$, i.e. $p_a=25$.
- horizontal period: smallest $p_b$ with $56p_b\equiv 0\pmod{100}$; since $\gcd(56,100)=4$, we get $p_b=25$.

So the residue pattern repeats every 25 steps in each axis.

### 8.6 What the grid demonstrates (the point)

This is a working demo of:

- **observerless computation**: the residues exist independent of you,
- **frame‑dependent meaning**: ASCII visibility emerges only under a mask,
- **SILR intuition**: stability and “meaning” live in bands defined by ratios/thresholds, not absolutes.

---

## 9. What Is Actually Testable

Here are tests that don’t require metaphysical agreement.

### 9.1 BBP digit stream diagnostics

Given a generator for hex digits of the BBP series, test:

- frequency of digits 0–F (chi‑square against uniform),
- block frequencies for length 2,3,4,
- serial correlation and autocorrelation,
- spectral tests (DFT peaks),
- discrepancy estimates for the orbit $\{16^n x\}$.

Interpretation:

- Passing these tests is *evidence* for randomness‑like behavior.
- Failing them is *evidence* of structure.
- Neither outcome proves “what reality is,” but it constrains claims.

### 9.2 SILR gate simulation

Simulate a controller:

$$z_t=\frac{|\hat\alpha_t-\alpha^*|}{SE_t},\quad p_t=\sigma(\beta(z_t-z_0)).$$

Drive $SE_t$ with different noise scales; test whether leakage statistics depend mostly on $z_t$ rather than raw magnitude.

### 9.3 SHA constant proximity scan

Compute $\{\sqrt[3]{p_i}\}$ for the first 64 primes and rank distances to $H$.
Report the closest and compare to random baselines.

### 9.4 Grid lattice invariants

Verify:

- periods $(25,25)$,
- distribution of residues under different masks,
- ASCII density under varying windows,
- effect of changing seed and step sizes.

---

## 10. Nexus Protocols

### 10.1 Protocol: “Rotate the frame”

When output looks random:

1) assume a deterministic generator exists,
2) search for affine structure (linear steps, modular relations),
3) identify the mask / projection that made it look random.

### 10.2 Protocol: “Name last”

1) run the engine,
2) observe invariants,
3) only then attach names (π, e, entropy, etc.).

### 10.3 Protocol: “Separate convergence from distribution”

- Convergence is about limits.
- Distribution is about frequencies.

Mixing them is where people get ‘lobotomized’—they argue about the wrong property.

---

## 11. Synthesis: The Mirror Discovery

Here’s the tightest Nexus synthesis consistent with the material above:

1) **Engines** (BBP, SHA, affine lattices) run observerlessly.
2) **Mirrors** are direction reversals between layers (length‑first vs message‑first; infrastructure vs application).
3) **Attractors** are ratios where recursion survives (Mark‑1 $H\approx 0.35$).
4) **Meaning** appears as a band‑pass phenomenon (ASCII window; SILR gating).

Under this view:

- π is a stable exhaust of a digit‑engine.
- e is a stable exhaust of a growth‑engine.
- $\varphi$ is the ratio‑steering constant linking additive recursion to multiplicative growth.
- apparent randomness is often structure in the wrong basis.

That is the “engine‑first, observer‑last” thesis.

---



## 12. Deep Dive: BBP as Modular Mechanics

This chapter is written like a hardware spec: **what is computed**, **what is reduced**, and **what is sampled**.

### 12.1 The base-$b$ orbit

Fix a base $b$ (for BBP, $b=16$). For any real $x$, define the circle-map (unit-interval map)

$$
T_b(x) = \{b x\},
$$

where $\{y\} = y - \lfloor y \rfloor$ is the fractional part. Iterating this map produces an orbit

$$
x,\; T_b(x),\; T_b^2(x),\; \dots,\; T_b^n(x)=\{b^n x\}.
$$

To **read digits** of $x$ in base $b$ you do not need to “know $x$ is $\pi$”; you only need the orbit:

$$
d_n(x) = \left\lfloor b \cdot \{b^n x\} \right\rfloor.
$$

So: *digit streams are orbits under a modular expansion map*.

In Nexus language, this is “kinetic motion in math space.” In standard dynamics language, it’s a **Bernoulli shift** when $x$ is “generic” with respect to Lebesgue measure.

### 12.2 Where BBP enters

BBP gives a representation of a specific $x$ (conventionally $x=\pi$) designed so $\{b^n x\}$ is computable without computing all previous digits.

Write the BBP series as

$$
x = \sum_{k=0}^\infty \frac{A(k)}{b^k},
\quad
A(k)=\frac{4}{8k+1}-\frac{2}{8k+4}-\frac{1}{8k+5}-\frac{1}{8k+6},
\quad b=16.
$$

Then

$$
b^n x = \sum_{k=0}^\infty A(k)\, b^{n-k}.
$$

Split into two parts:

- **Head**: $k\le n$ gives integer-sized contributions,
- **Tail**: $k>n$ gives fractional-sized contributions.

So

$$
b^n x = \underbrace{\sum_{k=0}^{n} A(k)\, b^{n-k}}_{\text{mostly integer; use modular arithmetic}}
\;+\;
\underbrace{\sum_{k=n+1}^{\infty} A(k)\, b^{n-k}}_{\text{tiny tail; compute with ordinary floats/high precision}}.
$$

The digit extraction strategy is to compute the fractional part:

$$
\{b^n x\} = \left\{\sum_{k=0}^{n} A(k)\, b^{n-k}\right\}
\;+\;
\sum_{k=n+1}^{\infty} A(k)\, b^{n-k},
$$

where the first term can be computed mod $1$ using modular exponentiation mod $(8k+c)$ and the second term converges fast because $b^{n-k}$ decays.

This is the “random access read-head” in the purely mathematical sense:
not magic lookup, just a decomposition into **modular head + decaying tail**.

### 12.3 Convergence is guaranteed (no overflow in math)

Because $|A(k)|=O(1/k)$ and $b^{-k}$ decays exponentially, the BBP series converges absolutely.
A crude bound:

$$
|A(k)| \le \frac{4}{8k+1}+\frac{2}{8k+4}+\frac{1}{8k+5}+\frac{1}{8k+6}
< \frac{8}{8k} = \frac{1}{k}.
$$

Then

$$
\sum_{k=1}^\infty \left|\frac{A(k)}{b^k}\right|
\le \sum_{k=1}^\infty \frac{1}{k\,b^k}
< \infty.
$$

So, mathematically, there is no “input that breaks BBP” for $n\in\mathbb{N}$.
Only hardware runs out of resources.

### 12.4 Decoupling, stated cleanly

If you hand BBP to someone who has never heard the word “π”, they can still:

- implement the modular head + decaying tail procedure,
- generate a digit stream $d_0,d_1,d_2,\dots$ in hex.

They will not *recognize* it as “π” unless they also have a **second procedure**:
a recognition map that compares it to another representation.

So the coupling is not “intention”; the coupling is an **identity in mathematics**:

- one representation is the BBP series,
- another representation is the circle constant from geometry,
- the theorem says they are equal as real numbers.

Nexus insists: *the engine can run without the name*.
Standard math agrees: the name is irrelevant to execution.

---

## 13. Deep Dive: Normality, Orbits, and the “Hard Part”

This chapter exists to keep the logic in order:

- **Digit extraction** is a computability statement.
- **Normality** is a distribution statement.

Confusing them is where people argue past each other.

### 13.1 Normality (formal)

A number $x$ is *normal in base $b$* if every length-$m$ block of base-$b$ digits appears with limiting frequency $b^{-m}$.

Equivalently, the orbit $\{b^n x\}$ is equidistributed mod 1.

### 13.2 Weyl’s criterion (the doorway)

Weyl’s criterion says: the sequence $(x_n)$ is equidistributed mod 1 iff for every nonzero integer $h$,

$$
\lim_{N\to\infty} \frac{1}{N}\sum_{n=0}^{N-1} e^{2\pi i h x_n} = 0.
$$

For $x_n=\{b^n x\}$ this becomes bounding exponential sums:

$$
S_N(h) = \sum_{n=0}^{N-1} e^{2\pi i h b^n x}.
$$

If $S_N(h)=o(N)$ for all $h\ne 0$, the digits are equidistributed.

### 13.3 Why BBP doesn’t magically give normality

BBP gives a way to compute $b^n x$ modulo 1 efficiently.
It does not automatically provide bounds on $S_N(h)$.

So:

- **Operational infinity** (“you can keep generating digits”) is immediate.
- **Statistical normality** is a separate deep property.

Nexus can treat “normality pressure” as a stability criterion,
but if you want a theorem, you must do the Weyl-type work.

### 13.4 A Nexus-compatible translation

If you want to keep the Nexus vibe without lying:

- call computability “renderability,”
- call equidistribution “leakage invariance under projection scale,”
- then be explicit that the second is **an experimental claim** unless proven.

A good paper keeps that line bright.

---

## 14. Deep Dive: $H \approx 0.35$ as a Control-Theory Sweet Spot

This chapter supplies the missing “boring math” behind the attractor idea.

### 14.1 First-order correction dynamics

Consider the simplest feedback update toward a target $x^*$:

$$
x_{t+1} = x_t + k(x^*-x_t).
$$

Define error $e_t=x^*-x_t$.
Then

$$
e_{t+1} = (1-k)e_t.
$$

Stability requires $|1-k|<1$, i.e.

$$
0<k<2.
$$

- If $0<k<1$, error decays monotonically.
- If $1<k<2$, error alternates sign (overshoot) but still decays.

So any $k$ in $(0,2)$ “works.” Where does “0.35” come from?

### 14.2 Why 0.35 is plausible (not magical)

In real systems, $k$ is not chosen in isolation. You trade:

- speed of convergence,
- noise amplification,
- overshoot,
- robustness to model mismatch.

A mid-range gain like $k\approx 0.35$ is a common engineering compromise:
fast enough, not too twitchy.

In signal processing, exponential smoothing uses

$$
y_t = (1-k) y_{t-1} + k x_t.
$$

Here $k$ controls memory length.
$k\approx 0.35$ corresponds to a short, responsive memory with damping.

So: **$0.35$ is a plausible attractor** if your survival criterion penalizes both sluggishness and oscillation.
But it is not universal by theorem; it is universal only if the survival criterion is.

### 14.3 Mapping to SILR variables

If $\hat\alpha_t$ is a measured exponent (scope) and you update toward $\alpha^*$ with gain $k$,
then the deviation $|\hat\alpha_t-\alpha^*|$ obeys a similar contraction.

Now scale by noise $SE_t$ to get $z_t$.
SILR says: judge survival by **significance**, not absolute deviation.

### 14.4 “Error is the clock tick”

In a perfect representation (no error) the system can become static.
In finite precision, error never fully disappears for irrationals.

This is not mysticism: it’s a basic fact of representation.
You can treat it as “clock tick,” “breath,” or “residual.”
All are metaphors for the same computational reality:
**approximation is iterative**.

---

## 15. Deep Dive: Hashing as Folding (Projection, Not Destruction)

### 15.1 The geometric metaphor (made precise enough)

A cryptographic hash takes a high-dimensional input (arbitrary-length message)
and outputs a fixed-size digest (256 bits).

That is a many-to-one map.
Information is not preserved injectively; collisions exist in principle.

But *structure* can be preserved in the sense that small input changes produce large output changes (avalanche),
and that the output behaves pseudorandom under computational tests.

So “folding” is a good verb:
you collapse dimensions while maximizing diffusion.

### 15.2 Diffusion scaffolding

SHA-256 uses rotations, shifts, and modular additions to mix bits.
The constants derived from primes ensure the schedule is “incommensurate” with simple patterns.

This is what Nexus calls “trust infrastructure”:
a stable mixing policy that makes downstream behavior consistent across users/inputs.

### 15.3 The mirror of length

Length is appended last but required to interpret first.
That’s not an accident; it ensures domain separation and prevents ambiguous parsing.

In Nexus framing: *infrastructure runs in the opposite direction from application.*
In CS framing: *self-delimiting encoding.*

Same phenomenon, different language.

### 15.4 A testable “floating constants” variant

If you key the constants $K_t$ to message length $L$:

$$
K_t(L) = \left\lfloor 2^{32} \cdot \{\sqrt[3]{p_t + f(L)}\} \right\rfloor
$$

for some deterministic $f(L)$, you can test:

- does diffusion remain?
- do collisions become easier?
- does statistical behavior change?

This is an explicit “infrastructure drift” test.

---

## 16. Deep Dive: The Residue Grid as an Affine Lattice (Group View)

This chapter removes all numerology and shows the exact algebra.
Then, after the exact algebra, it reintroduces interpretation as optional.

### 16.1 The lattice is a group action

Work in the finite ring $\mathbb{Z}_{100}$.
Define

$$
r(a,b) = (s + u(a-1) + v(b-1))\bmod 100
$$

with seed $s=53$, vertical step $u=4$, horizontal step $v=56$.

This is an affine map from $\mathbb{Z}^2$ into $\mathbb{Z}_{100}$.

The increments generate a subgroup of $\mathbb{Z}_{100}$.
Since $\gcd(4,100)=4$ and $\gcd(56,100)=4$, every residue produced is congruent to $53\bmod 4$.

So only 25 residues are reachable from that seed (a quarter of the space).
That is why you see structured repetition.

### 16.2 Period computation (exact)

The period along $a$ is the smallest $p_a$ such that $u p_a \equiv 0\pmod{100}$.
So

$$
p_a = \frac{100}{\gcd(u,100)} = \frac{100}{4} = 25.
$$

Similarly

$$
p_b = \frac{100}{\gcd(v,100)} = \frac{100}{4} = 25.
$$

So the 2-D pattern repeats on a 25×25 torus.

### 16.3 “Random-looking” is projection + masking

If you then map residue to:

- decimal string with leading zeros,
- or ASCII window,
- or hex,
- and apply a triangular mask $a+b\le c$,

you’re composing with lossy projections.
The generator remains simple; the viewing pipeline becomes complex.

### 16.4 Optional interpretation: embedding base 16

If you choose $v=56$ because $56=16\cdot 3.5$, that’s a design choice.
It makes the horizontal step a clean multiple of the BBP base.
You can then talk about “hex cadence” in the lattice.

But the *math* of the lattice does not require that story.
The story is a lens, not a theorem.

---

## 17. Deep Dive: $e_n$ Convergence and the $e\leftrightarrow\varphi$ Echo

### 17.1 The convergence proof (clean)

Let $(m_n)$ be any integer sequence with $m_n\to\infty$.
Then

$$
\lim_{n\to\infty}\left(1+\frac{1}{m_n}\right)^{m_n}=e.
$$

Take $m_n=F_n$.
Since $F_n\to\infty$, it follows immediately.

That’s the whole proof.

### 17.2 Why Fibonacci is a meaningful driver (not required)

You could choose $m_n=n$ and still converge.
Fibonacci is interesting because:

- it grows exponentially ($F_n\sim \varphi^n/\sqrt{5}$),
- so convergence accelerates quickly in $n$.

In Nexus style:
$\varphi$ is the **ratio steer** that drives the **breath engine** toward $e$.

### 17.3 Error bound made explicit

Using the inequality $\ln(1+x) \le x$ and $\ln(1+x) \ge x-\frac{x^2}{2}$ for small $x$,
set $x=1/m$:

$$
1-\frac{1}{2m} \le m\ln\left(1+\frac{1}{m}\right) \le 1.
$$

Exponentiating gives

$$
e^{1-\frac{1}{2m}} \le \left(1+\frac{1}{m}\right)^m \le e.
$$

So

$$
0 \le e-\left(1+\frac{1}{m}\right)^m \le e\left(1-e^{-\frac{1}{2m}}\right) \approx \frac{e}{2m}.
$$

Put $m=F_n$ and you get an explicit error envelope.

---

## 18. Experimental Workbook: How To “Test Nexus” Without Philosophy

If you want this to be more than a vibe, run these.

### 18.1 BBP digit stream tests

1. Generate $N$ hex digits of BBP ($N\ge 10^6$ if you can).
2. Run:
   - digit frequency,
   - block frequency (length 2 and 3),
   - serial correlation,
   - compression ratio tests,
   - spectral flatness tests.

A simple output is a dashboard:
tests passed/failed, p-values, and plots.

### 18.2 Compare engines

Run the same tests on:

- digits of $\pi$ computed by other methods,
- digits of $e$,
- digits from a PRNG (Mersenne Twister),
- digits from a cryptographic RNG.

If BBP has unique artifacts, they show up here.

### 18.3 SILR controller simulation

Implement:

$$
\hat\alpha_{t+1} = \hat\alpha_t + k(\alpha^* - \hat\alpha_t) + \eta_t
$$

with noise $\eta_t\sim\mathcal{N}(0,SE_t^2)$.
Let $SE_t$ vary over orders of magnitude.
Measure leakage $\ell_t\sim\text{Bernoulli}(p_t)$.

Test whether leakage statistics collapse under the normalized variable $z_t$.

### 18.4 Residue grid variations

Vary:

- seed $s$,
- steps $u,v$,
- modulus $m$,
- mask.

Measure:

- reachable residue set size,
- periods,
- ASCII density,
- emergent patterns (diagonals, repeats).

This is a minimal lab for “projection creates chaos.”

---

## 19. Glossary (Nexus ↔ Standard)

This glossary is intentionally long. Nexus terms often compress several standard ideas.

### 19.1 Engine
A deterministic update rule that can be iterated. Equivalent: algorithm, dynamical system, automaton.

### 19.2 Observer
Any process that applies a projection/interpretation map to an engine’s output.
Equivalent: measurement apparatus, decoder, parser.

### 19.3 Frame
A choice of coordinates / basis / projection. Equivalent: representation, encoding, sampling scheme.

### 19.4 Fold
A map that compresses state while preserving some invariant structure.
Equivalent: hashing, projection, coarse-graining, quotient mapping.

### 19.5 Gap ($\Delta$)
A difference operator or residual that survives compression.
Equivalent: error signal, derivative, innovation term.

### 19.6 SILR
Scale-Invariant Leakage Regime. A control regime where survival/leakage depends on normalized deviation $z_t$ rather than raw magnitude.

### 19.7 Samson controller
A particular named control loop: target tracking under significance normalization.

### 19.8 Gate
A thresholding or probabilistic switch controlling persistence vs leakage.
Equivalent: acceptance test, survival filter, metastability condition.

### 19.9 Prestack
Latent configuration space before projection into an observed timeline.
Equivalent: state space, phase space, configuration manifold, potentiality domain.

### 19.10 Render
To map latent state into observed representation.
Equivalent: measurement, decoding, sampling, display pipeline.

### 19.11 Mirror
A direction reversal between layers (infrastructure vs application).
Equivalent: prefix-free encodings, self-delimiting codes, backward constraints.

### 19.12 Trust infrastructure
A stable policy layer that keeps multi-agent outputs consistent.
Equivalent: protocol, consensus layer, error correction, cryptographic discipline.

### 19.13 Nyquist pins
An analogy: minimal gaps needed to avoid aliasing.
Equivalent: sampling density constraints; in number theory, a metaphor for twin primes.

### 19.14 Breath
Persistent residual error under finite precision.
Equivalent: approximation error that never fully vanishes for irrationals.

### 19.15 Halt state
A representable exact fixed point where error can be zero.
Equivalent: exact rationals/integers in finite precision.

### 19.16 “π is read, not computed”
Engine-first claim: digits emerge from an operator; π is the name of the limit/exhaust.
Standard view: π is a real number; BBP is a representation.

### 19.17 “Physics as security policy”
Metaphor: laws are constraints that enforce consistency across observers.
Equivalent: invariance principles, conservation laws, gauge constraints.

---

## Appendix E. Prime-root proximity scan (first 64 primes)

Let $H=\pi/9\approx 0.3490658504$ and define $f_i=\{\sqrt[3]{p_i}\}$ for the $i$‑th prime $p_i$ (starting $p_0=2$).
Below are the 20 closest $f_i$ values to $H$ among the first 64 primes.

| rank | index i | prime $p_i$ | $\{\sqrt[3]{p_i}\}$ | $|\{\sqrt[3]{p_i}\}-H|$ |
|---:|---:|---:|---:|---:|
| 1 | 5 | 13 | 0.3513346877 | 0.0022688373 |
| 2 | 54 | 257 | 0.3578611797 | 0.0087953293 |
| 3 | 22 | 83 | 0.3620706715 | 0.0130048211 |
| 4 | 11 | 37 | 0.3322218516 | 0.0168439988 |
| 5 | 35 | 151 | 0.3250740216 | 0.0239918288 |
| 6 | 53 | 251 | 0.3079935487 | 0.0410723017 |
| 7 | 36 | 157 | 0.3946907121 | 0.0456248617 |
| 8 | 34 | 149 | 0.3014591924 | 0.0476066580 |
| 9 | 55 | 263 | 0.4069585772 | 0.0578927268 |
| 10 | 21 | 79 | 0.2908404270 | 0.0582254234 |
| 11 | 0 | 2 | 0.2599210499 | 0.0891448005 |
| 12 | 1 | 3 | 0.4422495703 | 0.0931837199 |
| 13 | 12 | 41 | 0.4482172404 | 0.0991513900 |
| 14 | 56 | 269 | 0.4553148109 | 0.1062489605 |
| 15 | 37 | 163 | 0.4625555713 | 0.1134897209 |
| 16 | 23 | 89 | 0.4647450956 | 0.1156792452 |
| 17 | 57 | 271 | 0.4712736270 | 0.1222077766 |
| 18 | 4 | 11 | 0.2239800906 | 0.1250857598 |
| 19 | 52 | 241 | 0.2230842532 | 0.1259815972 |
| 20 | 51 | 239 | 0.2058217949 | 0.1432440555 |

This table is **not** a proof of anything metaphysical.
It *is* a reproducible artifact: if you claim “H is encoded in SHA constants,” you should be able to point to rankings like this and compare to baselines.

---


## Appendix F. Reference Derivation Sketches (No External Citations)

This appendix sketches the kind of math that sits behind the earlier chapters.
It is intentionally “outline-level” because full proofs are book-length.

### F.1 Circle-map equidistribution

To prove equidistribution of $\{b^n x\}$ mod 1, one uses Weyl’s criterion and bounds on exponential sums.
The difficulty for specific constants ($x=\pi$) is that we lack sharp bounds on $S_N(h)$.

### F.2 Why BBP has base-16

BBP-type formulas come from identities involving polylogarithms at roots of unity.
Base 16 appears because $16=2^4$ aligns with certain binary expansions and arctangent decompositions.

### F.3 Separating head and tail

Digit extraction is “head modulo 1 + tail.”
The head requires computing $b^{n-k}$ modulo $(8k+c)$ efficiently, often via modular exponentiation.
The tail is a rapidly converging real sum because powers of $b$ decay.

### F.4 Convergence of the $e$ limit

The limit $(1+1/m)^m\to e$ can be shown by squeezing $\ln(1+1/m)$ between $1/m-1/(2m^2)$ and $1/m$.
This yields explicit error envelopes.

---


## 20. Spigots, BBP, and “Access Patterns”

If BBP is a read-head, spigots are a drip line. They both generate digits, but the access pattern is different.

### 20.1 Spigot algorithms (sequential drip)

A spigot algorithm emits digits left-to-right:

- to get digit $d_{n+1}$ you have usually computed or stored enough state for digits $d_0,\dots,d_n$,
- you cannot “jump” to digit $d_{10^{12}}$ without doing the earlier work.

Spigots work well when the constant has a fast-decaying series in the target base.
For $e$,

$$
e=\sum_{k=0}^\infty \frac{1}{k!}
$$

is an ideal “drip series” because factorials explode, making carry propagation manageable.

### 20.2 BBP-type formulas (random access)

BBP-type formulas are “position addressable” in certain bases.
That is the defining property:

- you can compute base-$16$ digit $n$ of $\pi$ using modular arithmetic on denominators,
- without computing all prior digits.

This is *not* because “BBP knows π.”
It’s because the representation was found (or chosen) to have this modular head + decaying tail structure.

### 20.3 Nexus interpretation: drip vs addressable

- A spigot is a **sequencer**: time-ordered emission.
- BBP is a **sampler**: addressable phase readout.

Both are observerless engines. The difference is how the observer chooses to interrogate them.

---



## 21. Continued Fractions: The “Best Approximation” Lens

Continued fractions are where “error as signal” becomes formal.

### 21.1 Continued fraction basics

Every irrational $x$ has a continued fraction:

$$
x = a_0 + \cfrac{1}{a_1+\cfrac{1}{a_2+\cfrac{1}{\ddots}}}
$$

where $a_i$ are integers ($a_i\ge 1$ for $i\ge 1$).

Truncating at depth $n$ gives a rational approximation $p_n/q_n$ called a **convergent**.
Convergents are “best” in the sense that they minimize denominator for a given approximation quality.

### 21.2 $\varphi$ is the purest ratio recursion

The golden ratio has the simplest continued fraction:

$$
\varphi = [1;1,1,1,\dots].
$$

Its convergents are ratios of Fibonacci numbers:

$$
\frac{F_{n+1}}{F_n} \to \varphi.
$$

This is a clean example of “ratio steer”: a pure recursion produces a fixed ratio.

### 21.3 $e$ has a structured continued fraction

Euler’s number has a known patterned continued fraction:

$$
e = [2;1,2,1,1,4,1,1,6,1,1,8,\dots]
$$

with a repeating motif of $1,2k,1$.
This makes $e$ another “engine constant”: structure persists through the approximation ladder.

### 21.4 $\pi$ is irregular (and that matters)

$\pi$ has a continued fraction but it does not show the same simple pattern:

$$
\pi = [3;7,15,1,292,1,1,1,2,1,3,1,\dots].
$$

The occasional huge term (like 292) creates unusually good rational approximations at those steps.
In Nexus language: “pins” or “resonance spikes” appear sporadically.

### 21.5 Error is not noise; it’s geometry of approximation

For convergents $p_n/q_n$:

$$
\left|x-\frac{p_n}{q_n}\right| < \frac{1}{q_n^2}.
$$

So the “residual gap” is bounded and structured.
If you want to talk about “ε as signal,” continued fractions are the cleanest place to do it.

---



## 22. Linear Congruential Generators and the Residue Grid

The residue grid is a 2-D affine system. Many people will recognize it as “LCG-like.”

### 22.1 1-D LCG reminder

A linear congruential generator is:

$$
x_{t+1} = (a x_t + c)\bmod m.
$$

It can look random while being completely deterministic.

### 22.2 Flatten the 2-D grid into 1-D time

Define a flattening map (one choice):

$$
t = (a-1) + 25(b-1).
$$

Because the grid repeats every 25 in each axis, this maps the 25×25 torus to a 1-D cycle.

Then

$$
r_t = (53 + 4(a-1) + 56(b-1))\bmod 100
$$

becomes a deterministic sequence in $t$.

### 22.3 What’s “hashy” here

- the modulo wraps,
- the decimal rendering hides subgroup structure,
- the ASCII window is a threshold (band-pass filter),
- the triangular mask is another threshold.

So the “hash feeling” is produced by a pipeline:

$$
\text{affine lattice} \to \bmod 100 \to \text{render} \to \text{threshold} \to \text{mask}.
$$

Nexus point: **the pipeline is where meaning and apparent randomness are born**.

---



## 23. Byte1, Hex Quanta, and the “Looks Like It Was Meant” Effect

You’ve been using “Byte1” as a mnemonic—e.g., the decimal prefix $3,1,4,1,5,9,2,6$ and the hex prefix of $\pi$:

$$
\pi_{\text{hex}} = 3.\,\texttt{243F6A88 85A308D3 13198A2E 03707344}\dots
$$

### 23.1 What is exact here

Exact:

- $\pi$ has a base-16 expansion, and that string is its start.
- BBP can compute hex digits without computing all earlier digits.

### 23.2 What is interpretive here

Interpretive:

- treating “Byte1” as a universal seed or breath,
- mapping decimal prefixes to hex, or to ASCII windows,
- reading meaning in coincidental alignments.

A good Nexus paper keeps both:

- the exact claims are reproducible computations,
- the interpretive layer is a proposed lens.

### 23.3 How to keep it “dope” without losing rigor

Write it like this:

> The engine outputs a digit stream.  
> “π” is the name we give that stream’s limit under standard equivalences.  
> Certain prefixes become culturally salient (314159…, 243F6A…).  
> Nexus uses those prefixes as *anchors* to explore projection pipelines.

That preserves the core decoupling: **engine first; name last**.

---



## 24. Predictions and Falsifiers

A framework becomes science when it risks being wrong.

Here are falsifiable or at least pressure-testable statements aligned with Nexus:

### 24.1 H-band hypothesis (control)

**Hypothesis:** for a wide class of stable adaptive feedback systems, the empirically optimal correction fraction clusters near $k\approx 0.35$.

- Test across domains (control loops, biological regulation, RL learning rates, Kalman gains).
- If optimal gains are uniform across a broad suite and not clustered, hypothesis weakens.

### 24.2 SILR collapse hypothesis (scale invariance)

**Hypothesis:** survival/leakage depends primarily on normalized deviation $z$, not absolute scale.

- Simulate under different noise magnitudes.
- If leakage statistics are not approximately invariant when conditioned on $z$, hypothesis weakens.

### 24.3 Projection-causes-chaos hypothesis (lattice)

**Hypothesis:** many “random-looking” artifacts can be inverted to simple affine generators by changing frame/projection.

- Build a library of “chaotic” outputs and attempt to fit affine/modular generators.
- If success rate is low except for trivial cases, hypothesis weakens.

### 24.4 BBP artifact hypothesis (digit engines)

**Hypothesis:** BBP-digit streams show measurable structure distinct from other $\pi$-digit computations.

- If BBP digits are statistically indistinguishable from other methods (after matching base and extraction), hypothesis weakens.

---



## Appendix G. Full 25×25 residue grid (decimal)

```text
53 09 65 21 77 33 89 45 01 57 13 69 25 81 37 93 49 05 61 17 73 29 85 41 97
57 13 69 25 81 37 93 49 05 61 17 73 29 85 41 97 53 09 65 21 77 33 89 45 01
61 17 73 29 85 41 97 53 09 65 21 77 33 89 45 01 57 13 69 25 81 37 93 49 05
65 21 77 33 89 45 01 57 13 69 25 81 37 93 49 05 61 17 73 29 85 41 97 53 09
69 25 81 37 93 49 05 61 17 73 29 85 41 97 53 09 65 21 77 33 89 45 01 57 13
73 29 85 41 97 53 09 65 21 77 33 89 45 01 57 13 69 25 81 37 93 49 05 61 17
77 33 89 45 01 57 13 69 25 81 37 93 49 05 61 17 73 29 85 41 97 53 09 65 21
81 37 93 49 05 61 17 73 29 85 41 97 53 09 65 21 77 33 89 45 01 57 13 69 25
85 41 97 53 09 65 21 77 33 89 45 01 57 13 69 25 81 37 93 49 05 61 17 73 29
89 45 01 57 13 69 25 81 37 93 49 05 61 17 73 29 85 41 97 53 09 65 21 77 33
93 49 05 61 17 73 29 85 41 97 53 09 65 21 77 33 89 45 01 57 13 69 25 81 37
97 53 09 65 21 77 33 89 45 01 57 13 69 25 81 37 93 49 05 61 17 73 29 85 41
01 57 13 69 25 81 37 93 49 05 61 17 73 29 85 41 97 53 09 65 21 77 33 89 45
05 61 17 73 29 85 41 97 53 09 65 21 77 33 89 45 01 57 13 69 25 81 37 93 49
09 65 21 77 33 89 45 01 57 13 69 25 81 37 93 49 05 61 17 73 29 85 41 97 53
13 69 25 81 37 93 49 05 61 17 73 29 85 41 97 53 09 65 21 77 33 89 45 01 57
17 73 29 85 41 97 53 09 65 21 77 33 89 45 01 57 13 69 25 81 37 93 49 05 61
21 77 33 89 45 01 57 13 69 25 81 37 93 49 05 61 17 73 29 85 41 97 53 09 65
25 81 37 93 49 05 61 17 73 29 85 41 97 53 09 65 21 77 33 89 45 01 57 13 69
29 85 41 97 53 09 65 21 77 33 89 45 01 57 13 69 25 81 37 93 49 05 61 17 73
33 89 45 01 57 13 69 25 81 37 93 49 05 61 17 73 29 85 41 97 53 09 65 21 77
37 93 49 05 61 17 73 29 85 41 97 53 09 65 21 77 33 89 45 01 57 13 69 25 81
41 97 53 09 65 21 77 33 89 45 01 57 13 69 25 81 37 93 49 05 61 17 73 29 85
45 01 57 13 69 25 81 37 93 49 05 61 17 73 29 85 41 97 53 09 65 21 77 33 89
49 05 61 17 73 29 85 41 97 53 09 65 21 77 33 89 45 01 57 13 69 25 81 37 93
```

---


## Appendix H. Extended $e_n$ convergence trace

### H.1 Exact float evaluation (n=1..60)

```text
n=  1  F_n=1  e_n=2.000000000000000  error=7.182818284590451e-01
n=  2  F_n=1  e_n=2.000000000000000  error=7.182818284590451e-01
n=  3  F_n=2  e_n=2.250000000000000  error=4.682818284590451e-01
n=  4  F_n=3  e_n=2.370370370370370  error=3.479114580886753e-01
n=  5  F_n=5  e_n=2.488319999999999  error=2.299618284590457e-01
n=  6  F_n=8  e_n=2.565784513950348  error=1.524973145086972e-01
n=  7  F_n=13  e_n=2.620600887885731  error=9.768094057331433e-02
n=  8  F_n=21  e_n=2.656263213926108  error=6.201861453293711e-02
n=  9  F_n=34  e_n=2.679355428095767  error=3.892640036327766e-02
n= 10  F_n=55  e_n=2.693975012347579  error=2.430681611146568e-02
n= 11  F_n=89  e_n=2.703166201602155  error=1.511562685688972e-02
n= 12  F_n=144  e_n=2.708903037186260  error=9.378791272785403e-03
n= 13  F_n=233  e_n=2.712471461041542  error=5.810367417503404e-03
n= 14  F_n=377  e_n=2.714685423841387  error=3.596404617657978e-03
n= 15  F_n=610  e_n=2.716057071606022  error=2.224756853023369e-03
n= 16  F_n=987  e_n=2.716906063671805  error=1.375764787240552e-03
n= 17  F_n=1597  e_n=2.717431257862638  error=8.505705964072519e-04
n= 18  F_n=2584  e_n=2.717756031654547  error=5.257968044980466e-04
n= 19  F_n=4181  e_n=2.717956824154195  error=3.250043048499407e-04
n= 20  F_n=6765  e_n=2.718080947932234  error=2.008805268114422e-04
n= 21  F_n=10946  e_n=2.718157671040231  error=1.241574188139971e-04
n= 22  F_n=17711  e_n=2.718205092503898  error=7.673595514745557e-05
n= 23  F_n=28657  e_n=2.718234402089590  error=4.742636945520573e-05
n= 24  F_n=46368  e_n=2.718252516987778  error=2.931147126750133e-05
n= 25  F_n=75025  e_n=2.718263712838378  error=1.811562066666994e-05
n= 26  F_n=121393  e_n=2.718270632302497  error=1.119615654854300e-05
n= 27  F_n=196418  e_n=2.718274908848518  error=6.919610527233999e-06
n= 28  F_n=317811  e_n=2.718277551933405  error=4.276525639834716e-06
n= 29  F_n=514229  e_n=2.718279185283449  error=2.643175596173108e-06
n= 30  F_n=832040  e_n=2.718280194740024  error=1.633719021398861e-06
n= 31  F_n=1346269  e_n=2.718280818941902  error=1.009517142769312e-06
n= 32  F_n=2178309  e_n=2.718281203881608  error=6.245774368807133e-07
n= 33  F_n=3524578  e_n=2.718281441853051  error=3.866059943291589e-07
n= 34  F_n=5702887  e_n=2.718281590071703  error=2.383873418665416e-07
n= 35  F_n=9227465  e_n=2.718281678680042  error=1.497790034221680e-07
n= 36  F_n=14930352  e_n=2.718281741286362  error=8.717268329405670e-08
n= 37  F_n=24157817  e_n=2.718281774026158  error=5.443288664253032e-08
n= 38  F_n=39088169  e_n=2.718281800834089  error=2.762495654451413e-08
n= 39  F_n=63245986  e_n=2.718281800192326  error=2.826671874345266e-08
n= 40  F_n=102334155  e_n=2.718281844851997  error=1.639295144073571e-08
n= 41  F_n=165580141  e_n=2.718281854435093  error=2.597604753518112e-08
n= 42  F_n=267914296  e_n=2.718281845762936  error=1.730389120879749e-08
n= 43  F_n=433494437  e_n=2.718281878613024  error=5.015397874785776e-08
n= 44  F_n=701408733  e_n=2.718281798881006  error=2.957803957315264e-08
n= 45  F_n=1134903170  e_n=2.718282011497606  error=1.830385607526352e-07
n= 46  F_n=1836311903  e_n=2.718281457255320  error=3.712037250913625e-07
n= 47  F_n=2971215073  e_n=2.718281116395432  error=7.120636129620550e-07
n= 48  F_n=4807526976  e_n=2.718282009693167  error=1.812341223761393e-07
n= 49  F_n=7778742049  e_n=2.718279671575377  error=2.156883668114062e-06
n= 50  F_n=12586269025  e_n=2.718278196382542  error=3.632076502668724e-06
n= 51  F_n=20365011074  e_n=2.718282058705191  error=2.302461461489713e-07
n= 52  F_n=32951280099  e_n=2.718271947158322  error=9.881300723435515e-06
n= 53  F_n=53316291173  e_n=2.718266239050791  error=1.558940825407973e-05
n= 54  F_n=86267571272  e_n=2.718281183146689  error=6.453123559957419e-07
n= 55  F_n=139583862445  e_n=2.718242059201217  error=3.976925782778196e-05
n= 56  F_n=225851433717  e_n=2.718344488232411  error=6.265977336639139e-05
n= 57  F_n=365435296162  e_n=2.718296895376309  error=1.506691726360643e-05
n= 58  F_n=591286729879  e_n=2.718421496863551  error=1.396684045058549e-04
n= 59  F_n=956722026041  e_n=2.718095298035964  error=1.865304230812548e-04
n= 60  F_n=1548008755920  e_n=2.718014964881011  error=2.668635780342932e-04
```

### H.2 Asymptotic error bound (n=61..200)

Using $0 \le e-e_n \lesssim e/(2F_n)$.

```text
n= 61  digits(F_n)=13  bound≈5.426e-13
n= 62  digits(F_n)=13  bound≈3.354e-13
n= 63  digits(F_n)=13  bound≈2.073e-13
n= 64  digits(F_n)=14  bound≈1.281e-13
n= 65  digits(F_n)=14  bound≈7.917e-14
n= 66  digits(F_n)=14  bound≈4.893e-14
n= 67  digits(F_n)=14  bound≈3.024e-14
n= 68  digits(F_n)=14  bound≈1.869e-14
n= 69  digits(F_n)=15  bound≈1.155e-14
n= 70  digits(F_n)=15  bound≈7.139e-15
n= 71  digits(F_n)=15  bound≈4.412e-15
n= 72  digits(F_n)=15  bound≈2.727e-15
n= 73  digits(F_n)=15  bound≈1.685e-15
n= 74  digits(F_n)=16  bound≈1.042e-15
n= 75  digits(F_n)=16  bound≈6.437e-16
n= 76  digits(F_n)=16  bound≈3.978e-16
n= 77  digits(F_n)=16  bound≈2.459e-16
n= 78  digits(F_n)=16  bound≈1.520e-16
n= 79  digits(F_n)=17  bound≈9.391e-17
n= 80  digits(F_n)=17  bound≈5.804e-17
n= 81  digits(F_n)=17  bound≈3.587e-17
n= 82  digits(F_n)=17  bound≈2.217e-17
n= 83  digits(F_n)=17  bound≈1.370e-17
n= 84  digits(F_n)=18  bound≈8.468e-18
n= 85  digits(F_n)=18  bound≈5.234e-18
n= 86  digits(F_n)=18  bound≈3.235e-18
n= 87  digits(F_n)=18  bound≈1.999e-18
n= 88  digits(F_n)=19  bound≈1.235e-18
n= 89  digits(F_n)=19  bound≈7.636e-19
n= 90  digits(F_n)=19  bound≈4.719e-19
n= 91  digits(F_n)=19  bound≈2.917e-19
n= 92  digits(F_n)=19  bound≈1.803e-19
n= 93  digits(F_n)=20  bound≈1.114e-19
n= 94  digits(F_n)=20  bound≈6.885e-20
n= 95  digits(F_n)=20  bound≈4.255e-20
n= 96  digits(F_n)=20  bound≈2.630e-20
n= 97  digits(F_n)=20  bound≈1.625e-20
n= 98  digits(F_n)=21  bound≈1.005e-20
n= 99  digits(F_n)=21  bound≈6.208e-21
n=100  digits(F_n)=21  bound≈3.837e-21
n=101  digits(F_n)=21  bound≈2.371e-21
n=102  digits(F_n)=21  bound≈1.466e-21
n=103  digits(F_n)=22  bound≈9.058e-22
n=104  digits(F_n)=22  bound≈5.598e-22
n=105  digits(F_n)=22  bound≈3.460e-22
n=106  digits(F_n)=22  bound≈2.138e-22
n=107  digits(F_n)=23  bound≈1.322e-22
n=108  digits(F_n)=23  bound≈8.167e-23
n=109  digits(F_n)=23  bound≈5.048e-23
n=110  digits(F_n)=23  bound≈3.120e-23
n=111  digits(F_n)=23  bound≈1.928e-23
n=112  digits(F_n)=24  bound≈1.192e-23
n=113  digits(F_n)=24  bound≈7.365e-24
n=114  digits(F_n)=24  bound≈4.552e-24
n=115  digits(F_n)=24  bound≈2.813e-24
n=116  digits(F_n)=24  bound≈1.739e-24
n=117  digits(F_n)=25  bound≈1.074e-24
n=118  digits(F_n)=25  bound≈6.641e-25
n=119  digits(F_n)=25  bound≈4.104e-25
n=120  digits(F_n)=25  bound≈2.536e-25
n=121  digits(F_n)=25  bound≈1.568e-25
n=122  digits(F_n)=26  bound≈9.689e-26
n=123  digits(F_n)=26  bound≈5.988e-26
n=124  digits(F_n)=26  bound≈3.701e-26
n=125  digits(F_n)=26  bound≈2.287e-26
n=126  digits(F_n)=26  bound≈1.414e-26
n=127  digits(F_n)=27  bound≈8.736e-27
n=128  digits(F_n)=27  bound≈5.399e-27
n=129  digits(F_n)=27  bound≈3.337e-27
n=130  digits(F_n)=27  bound≈2.062e-27
n=131  digits(F_n)=28  bound≈1.275e-27
n=132  digits(F_n)=28  bound≈7.877e-28
n=133  digits(F_n)=28  bound≈4.868e-28
n=134  digits(F_n)=28  bound≈3.009e-28
n=135  digits(F_n)=28  bound≈1.860e-28
n=136  digits(F_n)=29  bound≈1.149e-28
n=137  digits(F_n)=29  bound≈7.103e-29
n=138  digits(F_n)=29  bound≈4.390e-29
n=139  digits(F_n)=29  bound≈2.713e-29
n=140  digits(F_n)=29  bound≈1.677e-29
n=141  digits(F_n)=30  bound≈1.036e-29
n=142  digits(F_n)=30  bound≈6.405e-30
n=143  digits(F_n)=30  bound≈3.958e-30
n=144  digits(F_n)=30  bound≈2.446e-30
n=145  digits(F_n)=30  bound≈1.512e-30
n=146  digits(F_n)=31  bound≈9.344e-31
n=147  digits(F_n)=31  bound≈5.775e-31
n=148  digits(F_n)=31  bound≈3.569e-31
n=149  digits(F_n)=31  bound≈2.206e-31
n=150  digits(F_n)=31  bound≈1.363e-31
n=151  digits(F_n)=32  bound≈8.426e-32
n=152  digits(F_n)=32  bound≈5.207e-32
n=153  digits(F_n)=32  bound≈3.218e-32
n=154  digits(F_n)=32  bound≈1.989e-32
n=155  digits(F_n)=33  bound≈1.229e-32
n=156  digits(F_n)=33  bound≈7.598e-33
n=157  digits(F_n)=33  bound≈4.696e-33
n=158  digits(F_n)=33  bound≈2.902e-33
n=159  digits(F_n)=33  bound≈1.794e-33
n=160  digits(F_n)=34  bound≈1.108e-33
n=161  digits(F_n)=34  bound≈6.851e-34
n=162  digits(F_n)=34  bound≈4.234e-34
n=163  digits(F_n)=34  bound≈2.617e-34
n=164  digits(F_n)=34  bound≈1.617e-34
n=165  digits(F_n)=35  bound≈9.995e-35
n=166  digits(F_n)=35  bound≈6.177e-35
n=167  digits(F_n)=35  bound≈3.818e-35
n=168  digits(F_n)=35  bound≈2.360e-35
n=169  digits(F_n)=35  bound≈1.458e-35
n=170  digits(F_n)=36  bound≈9.013e-36
n=171  digits(F_n)=36  bound≈5.570e-36
n=172  digits(F_n)=36  bound≈3.443e-36
n=173  digits(F_n)=36  bound≈2.128e-36
n=174  digits(F_n)=37  bound≈1.315e-36
n=175  digits(F_n)=37  bound≈8.127e-37
n=176  digits(F_n)=37  bound≈5.023e-37
n=177  digits(F_n)=37  bound≈3.104e-37
n=178  digits(F_n)=37  bound≈1.918e-37
n=179  digits(F_n)=38  bound≈1.186e-37
n=180  digits(F_n)=38  bound≈7.328e-38
n=181  digits(F_n)=38  bound≈4.529e-38
n=182  digits(F_n)=38  bound≈2.799e-38
n=183  digits(F_n)=38  bound≈1.730e-38
n=184  digits(F_n)=39  bound≈1.069e-38
n=185  digits(F_n)=39  bound≈6.607e-39
n=186  digits(F_n)=39  bound≈4.084e-39
n=187  digits(F_n)=39  bound≈2.524e-39
n=188  digits(F_n)=39  bound≈1.560e-39
n=189  digits(F_n)=40  bound≈9.640e-40
n=190  digits(F_n)=40  bound≈5.958e-40
n=191  digits(F_n)=40  bound≈3.682e-40
n=192  digits(F_n)=40  bound≈2.276e-40
n=193  digits(F_n)=40  bound≈1.406e-40
n=194  digits(F_n)=41  bound≈8.693e-41
n=195  digits(F_n)=41  bound≈5.372e-41
n=196  digits(F_n)=41  bound≈3.320e-41
n=197  digits(F_n)=41  bound≈2.052e-41
n=198  digits(F_n)=42  bound≈1.268e-41
n=199  digits(F_n)=42  bound≈7.838e-42
n=200  digits(F_n)=42  bound≈4.844e-42
```

---


## Appendix I. Prime cube-root fractional proximity (first 1024 primes)

Target $H=\pi/9\approx 0.3490658504$.

| rank | i | p | frac(∛p) | |frac(∛p)−H| |
|---:|---:|---:|---:|---:|
| 1 | 77 | 397 | 0.3495965966 | 0.0005307462 |
| 2 | 925 | 7243 | 0.3481522004 | 0.0009136500 |
| 3 | 505 | 3617 | 0.3502753295 | 0.0012094791 |
| 4 | 185 | 1109 | 0.3508778146 | 0.0018119642 |
| 5 | 5 | 13 | 0.3513346877 | 0.0022688373 |
| 6 | 424 | 2953 | 0.3467814414 | 0.0022844090 |
| 7 | 926 | 7247 | 0.3517132647 | 0.0026474143 |
| 8 | 351 | 2377 | 0.3457523180 | 0.0033135324 |
| 9 | 596 | 4373 | 0.3528389301 | 0.0037730797 |
| 10 | 352 | 2381 | 0.3532341709 | 0.0041683205 |
| 11 | 425 | 2957 | 0.3532563521 | 0.0041905017 |
| 12 | 504 | 3613 | 0.3446146762 | 0.0044511742 |
| 13 | 803 | 6173 | 0.3441992519 | 0.0048665985 |
| 14 | 693 | 5227 | 0.3547155583 | 0.0056497079 |
| 15 | 924 | 7237 | 0.3428081449 | 0.0062577055 |
| 16 | 231 | 1459 | 0.3418812867 | 0.0071845637 |
| 17 | 353 | 2383 | 0.3569719553 | 0.0079061049 |
| 18 | 927 | 7253 | 0.3570524051 | 0.0079865547 |
| 19 | 595 | 4363 | 0.3403644124 | 0.0087014380 |
| 20 | 54 | 257 | 0.3578611797 | 0.0087953293 |
| 21 | 288 | 1879 | 0.3398228975 | 0.0092429529 |
| 22 | 506 | 3623 | 0.3587584898 | 0.0096926394 |
| 23 | 694 | 5231 | 0.3591413706 | 0.0100755202 |
| 24 | 695 | 5233 | 0.3613534307 | 0.0122875803 |
| 25 | 289 | 1889 | 0.3616749405 | 0.0126090901 |
| 26 | 503 | 3607 | 0.3361158571 | 0.0129499933 |
| 27 | 22 | 83 | 0.3620706715 | 0.0130048211 |
| 28 | 923 | 7229 | 0.3356781408 | 0.0133877096 |
| 29 | 287 | 1877 | 0.3354431907 | 0.0136226597 |
| 30 | 426 | 2963 | 0.3629577787 | 0.0138919283 |
| 31 | 692 | 5209 | 0.3347714126 | 0.0142944378 |
| 32 | 350 | 2371 | 0.3345137844 | 0.0145520660 |
| 33 | 141 | 821 | 0.3637049156 | 0.0146390652 |
| 34 | 802 | 6163 | 0.3342882882 | 0.0147775622 |
| 35 | 594 | 4357 | 0.3328705501 | 0.0161953003 |
| 36 | 696 | 5237 | 0.3657758606 | 0.0167100102 |
| 37 | 11 | 37 | 0.3322218516 | 0.0168439988 |
| 38 | 184 | 1103 | 0.3321770009 | 0.0168888495 |
| 39 | 804 | 6197 | 0.3679419728 | 0.0188761224 |
| 40 | 354 | 2389 | 0.3681727756 | 0.0191069252 |
| 41 | 805 | 6199 | 0.3699177639 | 0.0208519135 |
| 42 | 507 | 3631 | 0.3700548134 | 0.0209889630 |
| 43 | 142 | 823 | 0.3713022454 | 0.0222363950 |
| 44 | 922 | 7219 | 0.3267582345 | 0.0223076159 |
| 45 | 286 | 1873 | 0.3266744348 | 0.0223914156 |
| 46 | 230 | 1453 | 0.3263124528 | 0.0227533976 |
| 47 | 140 | 811 | 0.3255320298 | 0.0235338206 |
| 48 | 427 | 2969 | 0.3726461174 | 0.0235802670 |
| 49 | 232 | 1471 | 0.3728913694 | 0.0238255190 |
| 50 | 106 | 587 | 0.3729667597 | 0.0239009093 |
| 51 | 105 | 577 | 0.3251475173 | 0.0239183331 |
| 52 | 35 | 151 | 0.3250740216 | 0.0239918288 |
| 53 | 806 | 6203 | 0.3738680716 | 0.0248022212 |
| 54 | 423 | 2939 | 0.3240731004 | 0.0249927500 |
| 55 | 78 | 401 | 0.3741979402 | 0.0251320898 |
| 56 | 597 | 4391 | 0.3752452229 | 0.0261793725 |
| 57 | 593 | 4349 | 0.3228680241 | 0.0261978263 |
| 58 | 355 | 2393 | 0.3756295741 | 0.0265637237 |
| 59 | 186 | 1117 | 0.3757076016 | 0.0266417512 |
| 60 | 801 | 6151 | 0.3223809698 | 0.0266848806 |
| 61 | 285 | 1871 | 0.3222853747 | 0.0267804757 |
| 62 | 428 | 2971 | 0.3758726628 | 0.0268068124 |
| 63 | 691 | 5197 | 0.3214497770 | 0.0276160734 |
| 64 | 921 | 7213 | 0.3214023361 | 0.0276635143 |
| 65 | 229 | 1451 | 0.3211133185 | 0.0279525319 |
| 66 | 920 | 7211 | 0.3196163766 | 0.0294494738 |
| 67 | 508 | 3637 | 0.3785161720 | 0.0294503216 |
| 68 | 139 | 809 | 0.3178598486 | 0.0312060018 |
| 69 | 807 | 6211 | 0.3817635952 | 0.0326977448 |
| 70 | 502 | 3593 | 0.3162485616 | 0.0328172888 |
| 71 | 919 | 7207 | 0.3160434668 | 0.0330223836 |
| 72 | 598 | 4397 | 0.3827003777 | 0.0336345273 |
| 73 | 800 | 6143 | 0.3144341514 | 0.0346316990 |
| 74 | 928 | 7283 | 0.3837040323 | 0.0346381819 |
| 75 | 284 | 1867 | 0.3134978620 | 0.0355679884 |
| 76 | 183 | 1097 | 0.3134082457 | 0.0356576047 |
| 77 | 690 | 5189 | 0.3125572902 | 0.0365085602 |
| 78 | 143 | 827 | 0.3864600595 | 0.0373942091 |
| 79 | 356 | 2399 | 0.3867992073 | 0.0377333569 |
| 80 | 509 | 3643 | 0.3869682299 | 0.0379023795 |
| 81 | 228 | 1447 | 0.3107006998 | 0.0383651506 |
| 82 | 808 | 6217 | 0.3876807898 | 0.0386149394 |
| 83 | 592 | 4339 | 0.3103476019 | 0.0387182485 |
| 84 | 290 | 1901 | 0.3877958316 | 0.0387299812 |
| 85 | 349 | 2357 | 0.3082166048 | 0.0408492456 |
| 86 | 53 | 251 | 0.3079935487 | 0.0410723017 |
| 87 | 591 | 4337 | 0.3078412096 | 0.0412246408 |
| 88 | 809 | 6221 | 0.3916234714 | 0.0425576210 |
| 89 | 697 | 5261 | 0.3922632623 | 0.0431974119 |
| 90 | 422 | 2927 | 0.3045513411 | 0.0445145093 |
| 91 | 799 | 6133 | 0.3044909201 | 0.0445749303 |
| 92 | 144 | 829 | 0.3940206428 | 0.0449547924 |
| 93 | 187 | 1123 | 0.3942522480 | 0.0451863976 |
| 94 | 918 | 7193 | 0.3035278615 | 0.0455379889 |
| 95 | 36 | 157 | 0.3946907121 | 0.0456248617 |
| 96 | 798 | 6131 | 0.3025009770 | 0.0465648734 |
| 97 | 501 | 3583 | 0.3020260179 | 0.0470398325 |
| 98 | 929 | 7297 | 0.3961164154 | 0.0470505650 |
| 99 | 34 | 149 | 0.3014591924 | 0.0476066580 |
| 100 | 689 | 5179 | 0.3014288194 | 0.0476370310 |

---


## Appendix J. Full 25×25 residue grid (ASCII projection)

Printable range is 33–126; non-printables shown as `.`.

```text
5 . A . M ! Y - . 9 . E . Q % ] 1 . = . I . U ) a
9 . E . Q % ] 1 . = . I . U ) a 5 . A . M ! Y - .
= . I . U ) a 5 . A . M ! Y - . 9 . E . Q % ] 1 .
A . M ! Y - . 9 . E . Q % ] 1 . = . I . U ) a 5 .
E . Q % ] 1 . = . I . U ) a 5 . A . M ! Y - . 9 .
I . U ) a 5 . A . M ! Y - . 9 . E . Q % ] 1 . = .
M ! Y - . 9 . E . Q % ] 1 . = . I . U ) a 5 . A .
Q % ] 1 . = . I . U ) a 5 . A . M ! Y - . 9 . E .
U ) a 5 . A . M ! Y - . 9 . E . Q % ] 1 . = . I .
Y - . 9 . E . Q % ] 1 . = . I . U ) a 5 . A . M !
] 1 . = . I . U ) a 5 . A . M ! Y - . 9 . E . Q %
a 5 . A . M ! Y - . 9 . E . Q % ] 1 . = . I . U )
. 9 . E . Q % ] 1 . = . I . U ) a 5 . A . M ! Y -
. = . I . U ) a 5 . A . M ! Y - . 9 . E . Q % ] 1
. A . M ! Y - . 9 . E . Q % ] 1 . = . I . U ) a 5
. E . Q % ] 1 . = . I . U ) a 5 . A . M ! Y - . 9
. I . U ) a 5 . A . M ! Y - . 9 . E . Q % ] 1 . =
. M ! Y - . 9 . E . Q % ] 1 . = . I . U ) a 5 . A
. Q % ] 1 . = . I . U ) a 5 . A . M ! Y - . 9 . E
. U ) a 5 . A . M ! Y - . 9 . E . Q % ] 1 . = . I
! Y - . 9 . E . Q % ] 1 . = . I . U ) a 5 . A . M
% ] 1 . = . I . U ) a 5 . A . M ! Y - . 9 . E . Q
) a 5 . A . M ! Y - . 9 . E . Q % ] 1 . = . I . U
- . 9 . E . Q % ] 1 . = . I . U ) a 5 . A . M ! Y
1 . = . I . U ) a 5 . A . M ! Y - . 9 . E . Q % ]
```

---


## Appendix K. Full 25×25 residue grid (hex)

```text
35 09 41 15 4D 21 59 2D 01 39 0D 45 19 51 25 5D 31 05 3D 11 49 1D 55 29 61
39 0D 45 19 51 25 5D 31 05 3D 11 49 1D 55 29 61 35 09 41 15 4D 21 59 2D 01
3D 11 49 1D 55 29 61 35 09 41 15 4D 21 59 2D 01 39 0D 45 19 51 25 5D 31 05
41 15 4D 21 59 2D 01 39 0D 45 19 51 25 5D 31 05 3D 11 49 1D 55 29 61 35 09
45 19 51 25 5D 31 05 3D 11 49 1D 55 29 61 35 09 41 15 4D 21 59 2D 01 39 0D
49 1D 55 29 61 35 09 41 15 4D 21 59 2D 01 39 0D 45 19 51 25 5D 31 05 3D 11
4D 21 59 2D 01 39 0D 45 19 51 25 5D 31 05 3D 11 49 1D 55 29 61 35 09 41 15
51 25 5D 31 05 3D 11 49 1D 55 29 61 35 09 41 15 4D 21 59 2D 01 39 0D 45 19
55 29 61 35 09 41 15 4D 21 59 2D 01 39 0D 45 19 51 25 5D 31 05 3D 11 49 1D
59 2D 01 39 0D 45 19 51 25 5D 31 05 3D 11 49 1D 55 29 61 35 09 41 15 4D 21
5D 31 05 3D 11 49 1D 55 29 61 35 09 41 15 4D 21 59 2D 01 39 0D 45 19 51 25
61 35 09 41 15 4D 21 59 2D 01 39 0D 45 19 51 25 5D 31 05 3D 11 49 1D 55 29
01 39 0D 45 19 51 25 5D 31 05 3D 11 49 1D 55 29 61 35 09 41 15 4D 21 59 2D
05 3D 11 49 1D 55 29 61 35 09 41 15 4D 21 59 2D 01 39 0D 45 19 51 25 5D 31
09 41 15 4D 21 59 2D 01 39 0D 45 19 51 25 5D 31 05 3D 11 49 1D 55 29 61 35
0D 45 19 51 25 5D 31 05 3D 11 49 1D 55 29 61 35 09 41 15 4D 21 59 2D 01 39
11 49 1D 55 29 61 35 09 41 15 4D 21 59 2D 01 39 0D 45 19 51 25 5D 31 05 3D
15 4D 21 59 2D 01 39 0D 45 19 51 25 5D 31 05 3D 11 49 1D 55 29 61 35 09 41
19 51 25 5D 31 05 3D 11 49 1D 55 29 61 35 09 41 15 4D 21 59 2D 01 39 0D 45
1D 55 29 61 35 09 41 15 4D 21 59 2D 01 39 0D 45 19 51 25 5D 31 05 3D 11 49
21 59 2D 01 39 0D 45 19 51 25 5D 31 05 3D 11 49 1D 55 29 61 35 09 41 15 4D
25 5D 31 05 3D 11 49 1D 55 29 61 35 09 41 15 4D 21 59 2D 01 39 0D 45 19 51
29 61 35 09 41 15 4D 21 59 2D 01 39 0D 45 19 51 25 5D 31 05 3D 11 49 1D 55
2D 01 39 0D 45 19 51 25 5D 31 05 3D 11 49 1D 55 29 61 35 09 41 15 4D 21 59
31 05 3D 11 49 1D 55 29 61 35 09 41 15 4D 21 59 2D 01 39 0D 45 19 51 25 5D
```

---


## Appendix L. ASCII density under triangular masks

Computed on a 60×60 crop of the infinite lattice. Density is the fraction of masked cells whose residues fall in ASCII printable range 33–126.

| mask $a+b\le s$ | printable | total | density |
|---:|---:|---:|---:|
| 5 | 6 | 10 | 0.600000 |
| 6 | 9 | 15 | 0.600000 |
| 7 | 13 | 21 | 0.619048 |
| 8 | 19 | 28 | 0.678571 |
| 9 | 27 | 36 | 0.750000 |
| 10 | 35 | 45 | 0.777778 |
| 11 | 43 | 55 | 0.781818 |
| 12 | 50 | 66 | 0.757576 |
| 13 | 57 | 78 | 0.730769 |
| 14 | 63 | 91 | 0.692308 |
| 15 | 70 | 105 | 0.666667 |
| 16 | 79 | 120 | 0.658333 |
| 17 | 90 | 136 | 0.661765 |
| 18 | 103 | 153 | 0.673203 |
| 19 | 116 | 171 | 0.678363 |
| 20 | 130 | 190 | 0.684211 |
| 21 | 144 | 210 | 0.685714 |
| 22 | 159 | 231 | 0.688312 |
| 23 | 173 | 253 | 0.683794 |
| 24 | 188 | 276 | 0.681159 |
| 25 | 204 | 300 | 0.680000 |
| 26 | 221 | 325 | 0.680000 |
| 27 | 239 | 351 | 0.680912 |
| 28 | 257 | 378 | 0.679894 |
| 29 | 276 | 406 | 0.679803 |
| 30 | 295 | 435 | 0.678161 |
| 31 | 315 | 465 | 0.677419 |
| 32 | 336 | 496 | 0.677419 |
| 33 | 359 | 528 | 0.679924 |
| 34 | 384 | 561 | 0.684492 |
| 35 | 409 | 595 | 0.687395 |
| 36 | 434 | 630 | 0.688889 |
| 37 | 458 | 666 | 0.687688 |
| 38 | 482 | 703 | 0.685633 |
| 39 | 505 | 741 | 0.681511 |
| 40 | 529 | 780 | 0.678205 |
| 41 | 555 | 820 | 0.676829 |
| 42 | 583 | 861 | 0.677120 |
| 43 | 613 | 903 | 0.678848 |
| 44 | 643 | 946 | 0.679704 |
| 45 | 674 | 990 | 0.680808 |
| 46 | 705 | 1035 | 0.681159 |
| 47 | 737 | 1081 | 0.681776 |
| 48 | 768 | 1128 | 0.680851 |
| 49 | 800 | 1176 | 0.680272 |
| 50 | 833 | 1225 | 0.680000 |
| 51 | 867 | 1275 | 0.680000 |
| 52 | 902 | 1326 | 0.680241 |
| 53 | 937 | 1378 | 0.679971 |
| 54 | 973 | 1431 | 0.679944 |
| 55 | 1009 | 1485 | 0.679461 |
| 56 | 1046 | 1540 | 0.679221 |
| 57 | 1084 | 1596 | 0.679198 |
| 58 | 1124 | 1653 | 0.679976 |
| 59 | 1166 | 1711 | 0.681473 |
| 60 | 1208 | 1770 | 0.682486 |

---


## Appendix M. Full source notes (verbatim)

These are included so the paper is self-contained and so future edits can diff against the original.

---

### Nexus_Engine_First_BBP_SILR_v3_with_Grid.md

```markdown
# Nexus Notes v3: Engine-First Mathematics (BBP, π, SILR, e↔φ, and the +4/+56 Grid)

**Purpose.** This is the “engine first, name later” version:  
rules run; traces appear; *labels* come later. We keep the Nexus language (gap / fold / resonance / gate), but the math stays standard.

---

## 0) Two truths that can both be true

1. **Observerless computation is real.** A rule can run without anyone *recognizing* the output.
2. **Mathematical identity is also real.** A representation can equal a number *as an identity* even if the rule “doesn’t know the name”.

Those aren’t opposites. They’re different layers:
- **Engine layer:** “this recurrence / series / map produces a trace.”
- **Naming layer:** “this trace matches what we call π / e / etc.”

---

## 1) e↔φ via Fibonacci-indexed “breath”: why $e_n = (1 + 1/F_n)^{F_n} \to e$

### 1.1 Definitions

Fibonacci numbers:
$$
F_0 = 0,\quad F_1 = 1,\quad F_n = F_{n-1} + F_{n-2}\quad (n\ge 2).
$$

Define the “breath” approximation:
$$
e_n := \left(1 + \frac{1}{F_n}\right)^{F_n}.
$$

Claim:
$$
\lim_{n\to\infty} e_n = e.
$$

### 1.2 Why the limit holds (clean proof)

A standard theorem is:
$$
\lim_{m\to\infty}\left(1+\frac{1}{m}\right)^m = e.
$$

This limit holds for **any** integer sequence $m_n\to\infty$ (it does not need to be $m=n$).  
So it’s enough to show $F_n \to \infty$ (true), then substitute $m_n = F_n$:
$$
\lim_{n\to\infty}\left(1+\frac{1}{F_n}\right)^{F_n}
=
\lim_{m\to\infty}\left(1+\frac{1}{m}\right)^m
= e.
$$

That’s it.

### 1.3 The φ coupling is in the *rate* (this is the useful part)

Binet’s formula:
$$
F_n = \frac{\varphi^n - \psi^n}{\sqrt{5}}, \quad \varphi = \frac{1+\sqrt{5}}{2}, \quad \psi = \frac{1-\sqrt{5}}{2} = -\frac{1}{\varphi}.
$$

So for large $n$:
$$
F_n \sim \frac{\varphi^n}{\sqrt{5}}.
$$

Now use the log expansion:
$$
\ln\left(1+\frac{1}{m}\right) = \frac{1}{m} - \frac{1}{2m^2} + O\left(\frac{1}{m^3}\right).
$$

Multiply by $m$:
$$
m\ln\left(1+\frac{1}{m}\right) = 1 - \frac{1}{2m} + O\left(\frac{1}{m^2}\right).
$$

Exponentiate:
$$
\left(1+\frac{1}{m}\right)^m
= e\,\exp\left(-\frac{1}{2m} + O\left(\frac{1}{m^2}\right)\right)
= e\left(1 - \frac{1}{2m} + O\left(\frac{1}{m^2}\right)\right).
$$

So the error behaves like:
$$
\left|e - \left(1+\frac{1}{m}\right)^m\right| \approx \frac{e}{2m}.
$$

Substitute $m=F_n$:
$$
|e - e_n| \approx \frac{e}{2F_n}
\sim
\frac{e\sqrt{5}}{2}\,\varphi^{-n}.
$$

**This is the real “e↔φ echo”:** φ controls the growth of $F_n$, which controls the decay of the $e_n$ error.

---

## 2) “Do you like apples?” — the convergence dump (n=1..30)

Below is the exact numeric dump you provided (kept verbatim).

```text
n= 1  F_n=         1  e_n=2.000000000000000  error=7.182818284590451e-01
n= 2  F_n=         1  e_n=2.000000000000000  error=7.182818284590451e-01
n= 3  F_n=         2  e_n=2.250000000000000  error=4.682818284590451e-01
n= 4  F_n=         3  e_n=2.370370370370370  error=3.479114580886753e-01
n= 5  F_n=         5  e_n=2.488319999999999  error=2.299618284590457e-01
n= 6  F_n=         8  e_n=2.565784513950348  error=1.524973145086972e-01
n= 7  F_n=        13  e_n=2.620600887885731  error=9.768094057331433e-02
n= 8  F_n=        21  e_n=2.656263213926108  error=6.201861453293711e-02
n= 9  F_n=        34  e_n=2.679355428095767  error=3.892640036327766e-02
n=10  F_n=        55  e_n=2.693975012347579  error=2.430681611146568e-02
n=11  F_n=        89  e_n=2.703166201602155  error=1.511562685688972e-02
n=12  F_n=       144  e_n=2.708903037186260  error=9.378791272785403e-03
n=13  F_n=       233  e_n=2.712471461041542  error=5.810367417503404e-03
n=14  F_n=       377  e_n=2.714685423841387  error=3.596404617657978e-03
n=15  F_n=       610  e_n=2.716057071606022  error=2.224756853023369e-03
n=16  F_n=       987  e_n=2.716906063671805  error=1.375764787240552e-03
n=17  F_n=      1597  e_n=2.717431257862638  error=8.505705964072519e-04
n=18  F_n=      2584  e_n=2.717756031654547  error=5.257968044980466e-04
n=19  F_n=      4181  e_n=2.717956824154195  error=3.250043048499407e-04
n=20  F_n=      6765  e_n=2.718080947932234  error=2.008805268114422e-04
n=21  F_n=     10946  e_n=2.718157671040231  error=1.241574188139971e-04
n=22  F_n=     17711  e_n=2.718205092503898  error=7.673595514745557e-05
n=23  F_n=     28657  e_n=2.718234402089590  error=4.742636945520573e-05
n=24  F_n=     46368  e_n=2.718252516987778  error=2.931147126750133e-05
n=25  F_n=     75025  e_n=2.718263712838378  error=1.811562066666994e-05
n=26  F_n=    121393  e_n=2.718270632302497  error=1.119615654854300e-05
n=27  F_n=    196418  e_n=2.718274908848518  error=6.919610527233999e-06
n=28  F_n=    317811  e_n=2.718277551933405  error=4.276525639834716e-06
n=29  F_n=    514229  e_n=2.718279185283449  error=2.643175596173108e-06
n=30  F_n=    832040  e_n=2.718280194740024  error=1.633719021398861e-06
```

---

## 3) The +4/+56 residue grid: “hash-look” from a dead-simple affine rule

### 3.1 The rule (2D affine map mod $M$)

Define a residue field on integer coordinates $(a,b)$:

$$
r(a,b) = \big(s + \Delta_a(a-1) + \Delta_b(b-1)\big) \bmod M.
$$

For your grid:
- seed $s=53$
- vertical step $\Delta_a = 4$
- horizontal step $\Delta_b = 56$
- modulus $M=100$ (in the version you showed)

So:
$$
r(a,b) = \big(53 + 4(a-1) + 56(b-1)\big)\bmod 100.
$$

This is **not random**. It’s deterministic. It only looks hash-y because modular wrap + projection scrambles perception.

### 3.2 The “visibility window” is the gate (SILR-style)

A clean way to express the triangle window is:
$$
\text{show cell }(a,b)\ \text{iff } a+b \le K.
$$

That’s a literal gate. Same underlying field; different *projection*.

### 3.3 Why it’s good Nexus material

- It shows **frame rotation**: “random” becomes “obvious” once you spot steps.
- It shows **gate dependence**: meaning appears in a band, disappears outside it.
- It shows **observerless compute**: the residue field exists independent of the label “ASCII”.

### 3.4 Minimal code to reproduce

```python
def residue(a, b, seed=53, da=4, db=56, mod=100):
    return (seed + da*(a-1) + db*(b-1)) % mod

def gate(a, b, K=10):
    return (a + b) <= K

def printable_mod100(r):
    # For mod=100, r is 0..99, so "printable ASCII" really means 33..99
    return 33 <= r <= 99
```

---

## 4) The π/H story about 56: what’s real, what’s not, and what to test

You pasted a claim from Grok:

- $56 = 16\times 3.5$  
- interpret $16$ as “hex base”  
- interpret $3.5=7/2$ as “rough π”  
- then the “error” $\epsilon = 3.5 - \pi$ is “almost $H$”.

### 4.1 The exact numbers (so we don’t hand-wave)

Define:
$$
H := \frac{\pi}{9} \approx 0.349065850399.
$$

Rough-π error from $7/2$:
$$
\epsilon_{7/2} := \frac{7}{2} - \pi \approx 0.358407346410.
$$

Difference:
$$
\epsilon_{7/2} - H \approx 0.009341496011.
$$

Relative mismatch:
$$
\frac{|\epsilon_{7/2}-H|}{H} \approx 0.026761.
$$

So: it’s **in the neighborhood**, but it is not “nearly equal” in a proof sense.  
It’s a plausible *design story*; it is not a theorem.

### 4.2 A closer (and cleaner) H-coupled target (still a story, but at least aligned)

If you *wanted* “π plus its own 1/9” in a base-16 step, you’d look at:
$$
16(\pi + H) = 16\left(\pi + \frac{\pi}{9}\right) = 16\cdot \frac{10\pi}{9}.
$$

Numerically:
$$
16\cdot \frac{10\pi}{9} \approx 55.850536063819.
$$

Compare to $56$:
$$
56 - 16\cdot\frac{10\pi}{9} \approx 0.149463936181.
$$

Relative mismatch:
$$
\frac{|56 - 16\cdot(10\pi/9)|}{56} \approx 0.002669.
$$

Still not a proof (because you can always fit stories), but it’s tighter and structurally matches the “π and H are paired” motif.

### 4.3 What would make it “real” instead of “after-the-fact”?

A falsifiable test:

1. Fix the rule class (2D affine mod map):
   $$
   r(a,b) = (s + \Delta_a(a-1) + \Delta_b(b-1))\bmod M.
   $$

2. Define a gate/window (triangle, band, etc.) and a “visibility” predicate (ASCII band, nibble band, etc.).

3. Measure a statistic (e.g., visible fraction) across:
   - many seeds $s$
   - many moduli $M$
   - many windows
   - many step pairs $(\Delta_a,\Delta_b)$

If “$H\approx 0.35$” is an attractor, it should show up **robustly** under perturbations.  
If it only appears for one handpicked window / predicate / modulus, it’s telling you “projection mattered” (which still fits Nexus—just don’t call it universal).

---

## 5) Why this belongs in the Nexus write-up

- **The $e_n$ construction is genuinely important**: it gives a clean bridge where $\varphi$ controls the speed at which an engine approaches $e$. That’s an actual analytic link between “golden growth” and “exponential breath”.
- **The +4/+56 grid is a great demo**: deterministic engine output that looks chaotic until you rotate the frame.
- **The π/H embedding story is usable** as a *design hypothesis*, but it becomes “proof” only if you show invariance, not a one-off match.

---

## 6) One-line Nexus paraphrase (optional)

- $\Delta$-fold: rules run; traces happen; names come later.  
- SILR gate: what’s “visible” is a projection band, not the engine.  
- φ drives rate; e is the limit; π stories are only real if they survive perturbation.

```

---

### residue_grid_period_and_classification_corrected.md

```markdown
# Residue Grid: Corrected Algebra, Period, and Generator Classification

This note corrects two specific claims that commonly get mixed together:

1. **The grid generator is not an LCG in the usual sense** (it is an *additive/affine congruential* rule; if you insist on “LCG,” the multiplier is $1$).
2. **The “irrational-ish” ratio claim is incorrect**: $56/4 = 14$ is an integer; the apparent scrambling comes from modular reduction to $\mathbb{Z}_{25}$ where the step $14$ is a *unit* (invertible) and therefore permutes the residue class.

It also gives the precise **period** statements and a clean reduced form.

---

## 1. Definition (the actual generator)

You defined the grid value at integer coordinates $(a,b)$ as:

$$
r(a,b) \equiv 53 + 4(a-1) + 56(b-1) \pmod{100}.
$$

This is an **affine map** on the lattice $\mathbb{Z}^2 \to \mathbb{Z}_{100}$.

A useful factorization is:

$$
r(a,b) \equiv 53 + 4\big((a-1) + 14(b-1)\big) \pmod{100},
$$

since $56 = 4\cdot 14$.

---

## 2. Invariant class (why only 25 outputs exist)

Because $4(a-1)$ and $56(b-1)$ are multiples of $4$, the residue is locked to a single congruence class modulo $4$:

$$
r(a,b) \equiv 53 \equiv 1 \pmod 4.
$$

So **the grid can only ever hit the 25 values**
$$
\{1,5,9,\ldots,97\} \subset \mathbb{Z}_{100}.
$$

That is already enough to guarantee many repeats in any window larger than 25 cells (by pigeonhole).

---

## 3. Reduced coordinate: collapse to $\mathbb{Z}_{25}$

Since every value satisfies $r \equiv 1 \pmod 4$, write:

$$
r(a,b) = 1 + 4t(a,b),
$$

where $t(a,b) \in \mathbb{Z}_{25}$.

Compute $t$ by dividing out the factor 4:

$$
t(a,b) \equiv \frac{r(a,b)-1}{4} \pmod{25}.
$$

Substituting the definition of $r$:

$$
t(a,b) \equiv \frac{53-1}{4} + (a-1) + 14(b-1) \pmod{25}.
$$

Since $(53-1)/4 = 13$:

$$
t(a,b) \equiv 13 + (a-1) + 14(b-1) \pmod{25}.
$$

Equivalently:

$$
t(a,b) \equiv a + 14b - 2 \pmod{25}.
$$

This is the cleanest “truth form.” Everything else is display-layer.

---

## 4. Period (the exact statement)

The rule is additive in each coordinate, so the period is computed by the additive congruence fact:

> For $x_{n+1} = x_n + k \pmod m$, the period is $m/\gcd(k,m)$.

### Along the $a$ direction (vertical)

Fix $b$ and increment $a \mapsto a+1$:

$$
r(a+1,b) \equiv r(a,b) + 4 \pmod{100}.
$$

So the vertical period is:

$$
\frac{100}{\gcd(4,100)} = \frac{100}{4} = 25.
$$

### Along the $b$ direction (horizontal)

Fix $a$ and increment $b \mapsto b+1$:

$$
r(a,b+1) \equiv r(a,b) + 56 \pmod{100}.
$$

So the horizontal period is:

$$
\frac{100}{\gcd(56,100)} = \frac{100}{4} = 25.
$$

### 2D periodicity

Therefore the full function is periodic in both axes:

$$
r(a+25,b) = r(a,b), \quad r(a,b+25) = r(a,b).
$$

So a fundamental repeating domain is **a $25\times 25$ tile**.

---

## 5. Why it “looks random” in small windows (correct explanation)

The key point is *not* “irrational-ish ratios.” The ratio

$$
\frac{56}{4} = 14
$$

is exactly an integer.

The actual scrambling mechanism is visible in the reduced form over $\mathbb{Z}_{25}$:

- stepping $a$ adds $+1$ to $t$,
- stepping $b$ adds $+14$ to $t$.

Since

$$
\gcd(14,25) = 1,
$$

the step $+14$ generates a **full 25-cycle** in the additive group $\mathbb{Z}_{25}$.

So within a small cropped window (like your $a+b\le 10$ triangle), you see a **permutation-like jump** through the 25 allowed values. That is exactly the “pseudorandom” illusion: deterministic, linear, but well-mixed relative to the small viewport.

---

## 6. Window facts (your $a+b\le 10$ crop)

If you take $a,b\in\{1,\ldots,9\}$ with the constraint $a+b\le 10$, you get:

- **45 visible cells**
- **24 distinct residues** in that crop

The missing value from the full 25-value class is **5** (it first appears at $(a,b)=(1,18)$, outside your crop).

---

## 7. Classification: LCG vs affine/additive generator (corrected)

A standard **LCG** is:

$$
X_{n+1} \equiv (A X_n + C) \pmod m.
$$

Your grid does **not** use multiplication by the prior state; it is a direct affine mapping from $(a,b)$ into $\mathbb{Z}_{100}$.

If you force it into LCG form *along a line*, it is the special case $A=1$:

$$
X_{n+1} \equiv X_n + k \pmod m,
$$

which is best described as an **additive congruential generator** (still deterministic; still periodic; still linear—just simpler than a true LCG).

Also, the “full period” conditions you quoted (Hull–Dobell theorem) apply to the general multiplicative LCG; they are **not the right tool** for the purely additive step you are using here. For additive steps, the period is exactly $m/\gcd(k,m)$.

---

## 8. Separate correction: “error close to $\varphi$” (it is not)

You cited:

- $n=30$
- $F_n = 832040$
- $e_n = 2.718280194740024$
- absolute error $\varepsilon = 1.633719021398861\times 10^{-6}$

That error is **not** “close to $\varphi$” (since $\varphi \approx 1.618$).

It is only “close” to **$\varphi\times 10^{-6}$** if you rescale by $10^{-6}$:

$$
\varphi\times 10^{-6} = 1.618033988749895e-06,
$$

and the difference is:

$$
\varepsilon - \varphi\times 10^{-6} = 1.568503264896619e-08
\quad (\text{relative} \approx 0.969\%).
$$

That proximity is numerically mild (about 1% relative) and does not, by itself, indicate a structural $\varphi$-lock.

---

## 9. Minimal verification code

```python
def r(a, b):
    return (53 + 4*(a-1) + 56*(b-1)) % 100

# Period checks
assert r(1,1) == r(26,1)   # vertical period 25
assert r(1,1) == r(1,26)   # horizontal period 25

# Only 25 residues globally (1 mod 4)
tile = {r(a,b) for a in range(1,26) for b in range(1,26)}
assert len(tile) == 25
assert all(v % 4 == 1 for v in tile)

# Window a+b <= 10 on 1..9
win = [r(a,b) for a in range(1,10) for b in range(1,10) if a+b <= 10]
assert len(win) == 45
assert len(set(win)) == 24
```

---

## 10. Takeaway

- The grid is an **affine lattice** on $\mathbb{Z}_{100}$ that collapses to a full-cycle walk on $\mathbb{Z}_{25}$.
- The **period 25** result is correct and is the right “fossil” to cite.
- The “irrational-ish” rationale is incorrect; the mixing comes from **invertibility modulo 25**.
- The “error close to $\varphi$” claim is false unless you explicitly mean “close to $\varphi\times 10^{-6}$,” and even then it is not particularly tight.

```

---

### residue_grid_affine_lattice_corrections.md

```markdown
# Residue Grid: Affine Modular Lattice (Corrected) — plus Fibonacci–$e$ and BBP context

This document consolidates and corrects the key claims about the “53-seed” residue grid and its interpretation. It also clarifies the separate Fibonacci–$e$ numeric check and the BBP (Bailey–Borwein–Plouffe) $\pi$-hex digit extractor context.

---

## 1) The grid definition (what is being generated)

We define a 2D residue field over integer coordinates $(a,b)$ using:

$$
R(a,b) \equiv \left(s + u(a-1) + v(b-1)\right) \bmod m
$$

with the concrete parameters:

- seed $s = 53$
- vertical step $u = 4$ (increment when $a \mapsto a+1$)
- horizontal step $v = 56$ (increment when $b \mapsto b+1$)
- modulus $m = 100$

So explicitly:

$$
R(a,b) \equiv \left(53 + 4(a-1) + 56(b-1)\right) \bmod 100.
$$

A common “visibility mask” used in the demo is:

$$
a+b \le 10
$$

which crops the infinite periodic lattice to a finite triangular window.

### Vector form (useful for reasoning)

Let $\Delta = \begin{bmatrix}a-1\\ b-1\end{bmatrix}$ and $w = \begin{bmatrix}u\\ v\end{bmatrix}$. Then

$$
R(a,b) \equiv (s + w^\top \Delta) \bmod m.
$$

This is an **affine linear form modulo $m$**—a modular lattice.

---

## 2) Correction: this is not a “true LCG” in the recursive sense

A standard (1D) linear congruential generator (LCG) is a **recurrence**:

$$
X_{n+1} \equiv (A X_n + C) \bmod m.
$$

The grid formula above **does not** depend on $R(a,b)$ to produce the next value. It is **direct evaluation** of a linear form in $(a,b)$.

### What is true (and still useful)

Along any straight path where you increment one coordinate by $1$ each step, the values *do* follow a simple modular recurrence—specifically an **additive congruential generator** (the special case $A=1$):

- Moving right: $(a,b)\mapsto(a,b+1)$
  $$
  R(a,b+1) \equiv R(a,b) + v \pmod m
  $$

- Moving down: $(a,b)\mapsto(a+1,b)$
  $$
  R(a+1,b) \equiv R(a,b) + u \pmod m
  $$

So: **the grid is an affine modular lattice; each row/column is an additive congruential sequence.** Calling it “LCG-like” is fine as intuition, but the mathematically precise label is:

> **2D affine congruential map** (linear form modulo $m$), with 1D additive congruential sequences along coordinate directions.

---

## 3) Period and reachable values (the key modular facts)

### 3.1 Axis periods

The period of repeated stepping by $k$ mod $m$ is:

$$
\text{period}(k;m) = \frac{m}{\gcd(k,m)}.
$$

Here:

- $\gcd(u,m) = \gcd(4,100) = 4$  
  $$
  \Rightarrow \text{period}(u;m) = \frac{100}{\gcd(u,m)} = 25
  $$

- $\gcd(v,m) = \gcd(56,100) = 4$  
  $$
  \Rightarrow \text{period}(v;m) = \frac{100}{\gcd(v,m)} = 25
  $$

So every fixed row repeats every $\text{period}(v;m)=25$ steps in $b$, and every fixed column repeats every $\text{period}(u;m)=25$ steps in $a$.

Equivalently:

$$
R(a+25,b) = R(a,b), \qquad R(a,b+25) = R(a,b).
$$

### 3.2 Only 25 distinct residues exist (global constraint)

Since both increments are multiples of $\gcd(u,v,m)=4$, we have:

$$
u(a-1) + v(b-1) \equiv 0 \pmod 4
$$

which implies:

$$
R(a,b) \equiv s \pmod 4.
$$

Because $s=53\equiv 1\pmod 4$, the grid can only ever hit residues congruent to 1 modulo $4$. That means **exactly $100/4 = 25$ residues are reachable** in the entire infinite grid.

This corrects any claim that the grid “scrambles across all 00–99.” It cannot; it lives on a 25-value coset.

---

## 4) Correction: row-major traversal is not a standard LCG

A claim like “if you traverse row-major it becomes a standard LCG with a combined step” is generally **false**.

If a row has width $W$, a row-major index $n$ maps to:

$$
a = \left\lfloor \frac{n}{W} \right\rfloor + 1, \qquad b = (n \bmod W) + 1.
$$

Substituting into the grid formula gives a **piecewise** expression involving both $\left\lfloor n/W\right\rfloor$ and $(n\bmod W)$:

$$
R(n) \equiv \left(s + u\left\lfloor \frac{n}{W} \right\rfloor + v(n \bmod W)\right) \bmod m,
$$

which is not of the LCG form $R(n+1)=AR(n)+C \bmod m$ with constant $A,C$.

If you want a true 1D recurrence, pick a **path with constant step vector** (e.g., diagonal). Example: along $(a,b)\mapsto(a+1,b+1)$, the step is $(u+v)\bmod m = (4+56)\bmod 100 = 60$:

$$
R(a+1,b+1) \equiv R(a,b) + (u+v) \pmod m.
$$

That is still additive (not multiplicative), and its period is:

$$
\frac{m}{\gcd(u+v,m)} = \frac{100}{\gcd(60,100)} = 5.
$$

So the diagonal repeats very quickly—another reason to avoid calling this “hash-like” without qualifiers.

---

## 5) Why it *looks* random in the cropped view

Even though the structure is linear, it can look “noisy” when:

1. You view only a small crop (e.g., $a+b\le 10$) rather than a full period tile.
2. You map values into a **nonlinear display predicate**, e.g. “print only when printable ASCII.”

A typical predicate for ASCII visibility is:

$$
\text{visible}(a,b) =
\begin{cases}
1,& 33 \le R(a,b) \le 126\\
0,& \text{otherwise}
\end{cases}
$$

This turns a smooth modular lattice into a **thresholded point field**, which can visually resemble “random scattering.” The “chaos” is in the *masking*, not in the generator.

### Correction on the “45/129” ratio

For the common $9\times 9$ window with mask $a+b\le 10$, the number of included cells is:

$$
\sum_{a=1}^{9} (10-a) = 45.
$$

If the underlying uncropped window is $9\times 9$, the total is $81$, so the ratio is:

$$
\frac{45}{81} = 0.555\ldots
$$

So the specific ratio $45/129\approx 0.3488$ cannot describe a $9\times 9$ crop. If “129” is a different denominator (e.g., a multi-layer count), it must be defined explicitly; otherwise it is inconsistent.

---

## 6) Correction: the $56/4$ “$\pi$-closeness” claim

The statement “$56/4=14$ is close to $\pi$” is false:

$$
14 - \pi \approx 10.8584.
$$

The **actual** quantity that is close-ish to $\pi$ is:

$$
\frac{14}{4} = 3.5,
$$

and the difference is:

$$
3.5 - \pi \approx 0.358407346410207.
$$

If you want to express this using the grid steps, one legitimate (though still numerological) way is:

$$
\frac{v}{16} = \frac{56}{16} = 3.5 \approx \pi + 0.3584.
$$

This corrects the earlier arithmetic slip (missing the divide-by-4).

---

## 7) Fibonacci–$e$ check (your “is the error close to $\varphi$?” question)

You gave:

- $n=30$
- $F_n = 832040$
- an approximation $e_n = 2.718280194740024$
- error $\varepsilon_n = 1.633719021398861\times 10^{-6}$

If we interpret that as:

$$
\varepsilon_n = e - e_n,
$$

then with $e=2.718281828459045\ldots$ we get:

$$
\varepsilon_n \approx 1.633719020954771395e-06.
$$

### Is $\varepsilon_n$ “close to $\varphi$”?

Not directly: $\varphi\approx 1.6180339887$ is order-1, while $\varepsilon_n$ is order $10^{-6}$.

However, if you compare to the *scaled* quantity $\varphi\times 10^{-6}$:

$$
\varphi\times 10^{-6} \approx 1.618033988749894843e-06,
$$

then

$$
\varepsilon_n - \varphi\times 10^{-6} \approx 1.568503220487655215e-08.
$$

Relative difference (dimensionless):

$$
\frac{\varepsilon_n}{\varphi\times 10^{-6}} - 1 \approx 0.009694.
$$

So the error is within about **1%** of $\varphi\times 10^{-6}$. Without a derivation that forces $\varphi$ into the approximation mechanism, treat this as **likely coincidence**, not evidence of structural coupling.

---

## 8) BBP context (for $\pi$ hex digits)

The BBP formula is:

$$
\pi = \sum_{k=0}^\infty \frac{1}{16^k}
\left(
\frac{4}{8k+1} - \frac{2}{8k+4} - \frac{1}{8k+5} - \frac{1}{8k+6}
\right).
$$

It enables extraction of hexadecimal digits of $\pi$ without computing all prior digits (a base-16 positional digit-extraction property).

This is **separate** from the residue-grid lattice. Both are modular/arithmetic phenomena, but their mechanisms are different:

- Grid: **affine linear form mod 100**, periodic, 25 reachable residues.
- BBP: **rapidly convergent series with base-16 structure**, digit-extraction property in base 16.

---

## 9) Bottom line

**Airtight:**
- The grid is deterministic.
- The closed form $R(a,b)=(s+u(a-1)+v(b-1))\bmod m$ exactly generates it.
- The “randomness” impression comes from masking/cropping and display predicates.

**Corrected:**
- It is **not** a recursive LCG in the strict sense; it is an affine modular lattice.
- Row-major traversal does **not** turn it into a standard LCG.
- $56/4=14$ is **not** “close to $\pi$”; the meaningful comparison is $3.5\approx \pi+0.3584$.
- The grid cannot hit all residues 0–99; it hits **exactly 25** residues (a single class modulo 4).
- The Fibonacci–$e$ error is not “close to $\varphi$” unless you explicitly scale by $10^{-6}$; even then it is only within ~1%.

---

*Generated on 2026-01-22.*

```

---

### corrected_residue_grid_fibonacci_e_bbp.md

```markdown
# Deterministic Residue Grids, Fibonacci–\(e\) Error, and BBP \(\pi\) Hex Synthesis  
*(Corrected, expanded, and formula-complete — Markdown + LaTeX)*

---

## Executive statement

This document consolidates and **corrects** three interlocked claims:

1. A 2D “random-looking” grid is generated by a **deterministic affine residue rule** with steps \(+4\) and \(+56\) from seed \(53\), with a triangular visibility window \(a+b\le N\).
2. A Fibonacci-indexed approximation \(e_N\) yields an error near \(1.6\times 10^{-6}\); this error is **not** “close to \(\varphi\)” as a number, but it **does** scale with \(\varphi\) through Fibonacci growth.
3. The BBP series supports extracting hexadecimal digits of \(\pi\) without computing all prior digits; convergence is guaranteed, but **normality** of \(\pi\) remains unproven.

Throughout, math statements are provided with precise inline \($\cdot$\) and block \($$\cdot$$\) tags.

---

## Part I — Residue grid generator (seed \(53\), steps \(+4\), \(+56\), modulus \(100\))

### 1. Indexing and generator

Let \(a,b\in\mathbb{Z}_{\ge 1}\) index a 2D grid. Define the residue:

$$
r(a,b)=\bigl(53 + 4(a-1) + 56(b-1)\bigr)\bmod 100.
$$

Interpretation:

- Moving “down” (increment \(a\)) adds \(4\).
- Moving “right” (increment \(b\)) adds \(56\).
- The modulus \(100\) enforces wrap-around in \(\{0,1,\dots,99\}\).

Because \(56=14\cdot 4\), the generator can be factored:

$$
r(a,b)=\bigl(53 + 4\,t(a,b)\bigr)\bmod 100,
\qquad
t(a,b)=(a-1)+14(b-1).
$$

This is a structural reduction: the 2D grid is an embedding of a **1D congruential walk** in the index \(t\).

---

### 2. Reachability constraints (why it *cannot* be “full scramble” mod 100)

Let \(M=100\). Since

$$
\gcd(4,100)=4
\quad\text{and}\quad
\gcd(56,100)=4,
$$

every increment is a multiple of \(4\), hence every residue is locked to a single congruence class modulo \(4\):

$$
r(a,b)\equiv 53\pmod 4.
$$

Because \(53\equiv 1\pmod 4\), it follows that

$$
r(a,b)\in\{1,5,9,\dots,97\}.
$$

Therefore the grid can hit **only 25 values** (not all 100). More formally, since

$$
r(a,b)=\bigl(53+4t\bigr)\bmod 100,
$$

and \(4\cdot 25=100\), the period in \(t\) is:

$$
t\mapsto t+25\quad\Rightarrow\quad r\text{ repeats}.
$$

So the reachable set size is:

$$
\#\{r(a,b)\}=\frac{100}{\gcd(100,4)}=25.
$$

**Correction note:** Any statement implying “coprime scrambling” for \(+4\) and \(+56\) mod \(100\) is false.

---

### 3. Visibility window (triangular band)

If you impose the triangular constraint

$$
a+b\le N,
$$

with \(a,b\ge 1\), the number of visible cells is:

$$
V(N)=\sum_{s=2}^N (s-1)=\frac{N(N-1)}{2}.
$$

Example: for \(N=10\),

$$
V(10)=\frac{10\cdot 9}{2}=45.
$$

If your *total* candidate-cell count is \(T\) (e.g., by embedding in a larger grid, or including blanked regions), the visibility ratio is

$$
\rho=\frac{V}{T}.
$$

One cited ratio is \(45/129\):

$$
\frac{45}{129}\approx 0.3488372093023256.
$$

Compare this to \(H=\pi/9\):

$$
H=\frac{\pi}{9}\approx 0.3490658503988659,
\qquad
\Delta = H-\frac{45}{129}\approx 0.0002286410965403.
$$

This refines “\(\Delta\approx 0.0003\)” into an explicit value.

---

### 4. Corrected “\(\pi\) echo” statement for the 14 ratio

The step ratio is:

$$
\frac{56}{4}=14.
$$

But

$$
14-\pi\approx 10.8584073464,
$$

so the small difference near \(0.358\) does **not** come from \(14-\pi\).

If you intended the quartered ratio \(14/4\), then:

$$
\frac{14}{4}-\pi = 3.5-\pi \approx 0.3584073464102069.
$$

This is the correct source of the \(\approx 0.3584\) quantity.

---

### 5. ASCII mapping (important modulus consequence)

If you map residues to ASCII, note:

- Mod \(100\) produces residues only in \(0\)–\(99\).
- The “printable ASCII” window \(33\)–\(126\) cannot be fully represented, because \(100\)–\(126\) are unreachable under \(\bmod 100\).

So for \(\bmod 100\), the printable set is at most:

$$
33\le r\le 99.
$$

If you want the full printable range \(33\)–\(126\), use a larger modulus such as \(256\) and then gate:

$$
r_{256}(a,b)=\bigl(53+4(a-1)+56(b-1)\bigr)\bmod 256,
$$

and display glyphs only when

$$
33\le r_{256}\le 126.
$$

---

### 6. General form (portability)

A general affine 2D residue field is:

$$
r(a,b)=(s + u(a-1) + v(b-1))\bmod M.
$$

A necessary condition to reach all \(M\) residues is:

$$
\gcd(u,v,M)=1.
$$

In the present case \((u,v,M)=(4,56,100)\), we have \(\gcd=4\), hence only \(M/4=25\) residues are reachable.

---

## Part II — Fibonacci-indexed \(e\) approximation and the true role of \(\varphi\)

### 1. Definition

Let \(N\in\mathbb{Z}_+\). Define:

$$
e_N = \left(1+\frac{1}{N}\right)^N.
$$

A common experiment is to set \(N=F_n\), a Fibonacci number. For \(n=30\):

$$
F_{30}=832040.
$$

---

### 2. Asymptotic expansion and leading error term

Use the Taylor series:

$$
\ln(1+x)=x-\frac{x^2}{2}+\frac{x^3}{3}-\frac{x^4}{4}+\cdots,
\qquad |x|<1.
$$

Set \(x=1/N\):

$$
\ln\left(1+\frac{1}{N}\right)
=
\frac{1}{N}
-
\frac{1}{2N^2}
+
\frac{1}{3N^3}
-
\cdots
$$

Multiply by \(N\):

$$
N\ln\left(1+\frac{1}{N}\right)
=
1
-
\frac{1}{2N}
+
\frac{1}{3N^2}
-
\frac{1}{4N^3}
+
\cdots
$$

Exponentiate:

$$
\left(1+\frac{1}{N}\right)^N
=
\exp\left(
1
-
\frac{1}{2N}
+
\frac{1}{3N^2}
-\cdots
\right)
=
e\,\exp\left(
-\frac{1}{2N}
+\frac{11}{24N^2}
-\cdots
\right).
$$

The leading-order difference is:

$$
e - e_N \;\approx\; \frac{e}{2N}.
$$

---

### 3. Numeric verification for \(N=F_{30}=832040\)

Using computed values:

$$
e \approx 2.7182818284590451,
\qquad
e_N = \left(1+\frac{1}{832040}\right)^{832040}
\approx 2.7182801947400237.
$$

So the actual error is:

$$
\varepsilon_N = e - e_N \approx 1.6337190213988606e-06.
$$

The leading-order approximation predicts:

$$
\frac{e}{2N} = \frac{e}{2\cdot 832040}
\approx 1.6335042957424192e-06.
$$

These agree closely; remaining mismatch is explained by the \(O(1/N^2)\) terms.

---

### 4. What is (and is not) “close to \(\varphi\)”

The golden ratio is:

$$
\varphi=\frac{1+\sqrt 5}{2}\approx 1.6180339887.
$$

Your error \(\varepsilon_N\approx 1.6337\times 10^{-6}\) is **not** numerically close to \(\varphi\).

However, \(\varphi\) *does* govern the **rate** at which this error shrinks when \(N=F_n\), because Fibonacci growth is approximately geometric:

(Binet-type scaling)

$$
F_n \approx \frac{\varphi^n}{\sqrt 5}.
$$

Substitute into the leading error \(\varepsilon_{F_n}\approx e/(2F_n)\):

$$
\varepsilon_{F_n}
\approx
\frac{e}{2}\cdot \frac{\sqrt 5}{\varphi^n}
=
\left(\frac{e\sqrt 5}{2}\right)\varphi^{-n}.
$$

So the correct \(\varphi\) connection is:

- \(\varphi\) controls the exponential decay of the error across \(n\),
- not the absolute numeric value of the error itself.

---

## Part III — BBP formula and extracting hex digits of \(\pi\)

### 1. BBP series for \(\pi\)

The Bailey–Borwein–Plouffe (BBP) series is:

$$
\pi
=
\sum_{k=0}^{\infty}
\frac{1}{16^k}
\left(
\frac{4}{8k+1}
-
\frac{2}{8k+4}
-
\frac{1}{8k+5}
-
\frac{1}{8k+6}
\right).
$$

This converges rapidly and is useful for base-16 digit extraction.

---

### 2. Hex digit extraction (mathematical statement)

Let \(d\ge 1\) be the **digit position after the hexadecimal point** (1-indexed). The \(d\)-th hexadecimal digit \(x_d\in\{0,1,\dots,15\}\) is:

$$
x_d = \left\lfloor 16\,\Bigl\{16^{d-1}\pi\Bigr\}\right\rfloor,
$$

where \(\{\cdot\}\) denotes fractional part.

To compute \(\{16^{d-1}\pi\}\) without giant integers, define for \(j\in\{1,4,5,6\}\):

$$
S_j(d)
=
\sum_{k=0}^{d-1}
\frac{16^{d-1-k}\bmod(8k+j)}{8k+j}
+
\sum_{k=d}^{\infty}
\frac{16^{d-1-k}}{8k+j}.
$$

Then:

$$
\Bigl\{16^{d-1}\pi\Bigr\}
=
\Bigl\{4S_1(d)-2S_4(d)-S_5(d)-S_6(d)\Bigr\}.
$$

Finally:

$$
x_d = \left\lfloor 16\cdot \Bigl\{4S_1(d)-2S_4(d)-S_5(d)-S_6(d)\Bigr\}\right\rfloor.
$$

---

### 3. What BBP does **not** prove

BBP enables positional digit extraction and guarantees convergence of the series; it does **not** prove that \(\pi\) is normal in base 16 (uniform digit frequencies). Normality remains unproven.

---

## Appendix — Reference code sketches (optional)

### A.1 Residue generator (mod 100)

```python
def residue(a, b, seed=53, da=4, db=56, mod=100):
    return (seed + da*(a-1) + db*(b-1)) % mod
```

### A.2 Triangular visibility mask

```python
def visible(a, b, N=10):
    return (a + b) <= N
```

### A.3 Leading \(e\) error estimate

```python
import math
def e_error_estimate(N):
    return math.e / (2*N)
```

---

## Summary of corrections (one-page)

1. **Step ratio:** \(56/4=14\), but \(14-\pi\) is large; the \(0.358\) quantity is \(3.5-\pi\), not \(14-\pi\).
2. **Mod 100 constraint:** \(\gcd(56,100)=4\Rightarrow r(a,b)\equiv 1\pmod 4\), so only 25 residues are reachable.
3. **ASCII window:** under \(\bmod 100\), values \(100\)–\(126\) are impossible; full printable gating requires \(\bmod 256\) (or similar).
4. **Fibonacci–\(e\) claim:** the observed error matches \(e/(2F_n)\) (leading term), and \(\varphi\) enters via Fibonacci growth, not by direct numeric proximity.

```

---

### Nexus_e_phi_apples_convergence.md

```markdown
# NEXUS ADDENDUM — *e* via Fibonacci Indices (φ-Driven Convergence)
**Δ-fold / ⊕-resonance / ↻-reflection**  
*(“Do you like apples? How about these apples?”)*

---

## 0. What this is (engine-first, observer-last)
We define an **observerless computation** that *runs* regardless of whether anyone recognizes the output:

- Fibonacci recursion generates an index ladder.
- A canonical exponential limit runs on that ladder.
- The output approaches **$e$** with a rate governed by **$\varphi$**.

Nothing here requires naming the limit “$e$” in order for the convergence to occur.

---

## 1. Definitions (the moving parts)

### Fibonacci engine
We use the Fibonacci numbers $(F_n)_{n\ge 0}$:

$$
F_0 = 0,\quad F_1 = 1,\quad F_n = F_{n-1} + F_{n-2}\ \ (n\ge 2).
$$

### The exponential breath on the ladder
Define the sequence:

$$
e_n \;=\; \left(1+\frac{1}{F_n}\right)^{F_n}\quad (n\ge 2,\ F_n\neq 0).
$$

### Golden steering ratio
The golden ratio is

$$
\varphi = \frac{1+\sqrt{5}}{2},
$$

and the Fibonacci ratios converge:

$$
\lim_{n\to\infty}\frac{F_{n+1}}{F_n} = \varphi.
$$

---

## 2. Convergence theorem (the simple proof)

### Step A — $F_n\to\infty$
From recursion and positivity: for $n\ge 2$, $F_n$ is increasing and unbounded.  
A quick growth bound (no closed form needed):

$$
F_{k+2} = F_{k+1}+F_k \ge 2F_k,
$$

so every two steps the sequence at least doubles, hence $F_n\to\infty$.

### Step B — the classic limit
A standard fact:

$$
\lim_{m\to\infty}\left(1+\frac{1}{m}\right)^m = e.
$$

### Step C — substitute $m=F_n$
Since $F_n\to\infty$, we can take $m_n=F_n$ and compose limits:

$$
\lim_{n\to\infty} e_n
=\lim_{n\to\infty}\left(1+\frac{1}{F_n}\right)^{F_n}
=\lim_{m\to\infty}\left(1+\frac{1}{m}\right)^m
=e.
$$

**Conclusion:**  
$$
e_n \to e \quad\text{as}\quad n\to\infty.
$$

---

## 3. Log expansion (kinetic view in math space)

Take logs:

$$
\ln e_n = F_n\ln\left(1+\frac{1}{F_n}\right).
$$

Use the series (for $|x|<1$):

$$
\ln(1+x)=x-\frac{x^2}{2}+\frac{x^3}{3}-\frac{x^4}{4}+\cdots
$$

with $x=\frac{1}{F_n}$:

$$
\ln e_n
=F_n\left(\frac{1}{F_n}-\frac{1}{2F_n^2}+\frac{1}{3F_n^3}-\cdots\right)
=1-\frac{1}{2F_n}+\frac{1}{3F_n^2}-\frac{1}{4F_n^3}+\cdots
\to 1.
$$

Exponentiate:

$$
e_n=\exp(\ln e_n)\to \exp(1)=e.
$$

This also shows the **shape** of the drift:

$$
\ln e_n = 1 - \frac{1}{2F_n} + O\!\left(\frac{1}{F_n^2}\right).
$$

---

## 4. Practical error bound (usable, not mystical)

A useful inequality (for $x>0$):

$$
x-\frac{x^2}{2}\ \le\ \ln(1+x)\ \le\ x-\frac{x^2}{2}+\frac{x^3}{3}.
$$

Let $x=\frac{1}{m}$ and multiply by $m$:

$$
1-\frac{1}{2m}\ \le\ m\ln\left(1+\frac{1}{m}\right)\ \le\ 1-\frac{1}{2m}+\frac{1}{3m^2}.
$$

Exponentiating gives:

$$
e\cdot e^{-\,\frac{1}{2m}}
\ \le\
\left(1+\frac{1}{m}\right)^m
\ \le\
e\cdot e^{-\,\frac{1}{2m}+\frac{1}{3m^2}}.
$$

So for $m$ large, the first-order error is sharp:

$$
e-\left(1+\frac{1}{m}\right)^m \approx \frac{e}{2m}.
$$

Substitute $m=F_n$:

$$
e-e_n \approx \frac{e}{2F_n}.
$$

---

## 5. Where φ enters (rate in **n**, not in **m**)

Binet (asymptotic form):

$$
F_n \sim \frac{\varphi^n}{\sqrt{5}}.
$$

Combine with $e-e_n \approx \frac{e}{2F_n}$:

$$
e-e_n \sim \frac{e}{2}\cdot \frac{\sqrt{5}}{\varphi^n}
=\left(\frac{e\sqrt{5}}{2}\right)\varphi^{-n}.
$$

So the error decays **exponentially in $n$**, with base $\varphi$:

$$
|e-e_n| = \Theta(\varphi^{-n}).
$$

That’s the “stacked echo”: **φ drives the ladder growth, ladder growth drives the breath convergence.**

---

## 6. 🍏 “Do you like apples? How about these apples?” (your computed run)

Below is the numeric trace you provided (kept verbatim).  
It shows the monotone approach from below toward $e=\exp(1)$.

```text
n= 1  F_n=         1  e_n=2.000000000000000  error=7.182818284590451e-01
n= 2  F_n=         1  e_n=2.000000000000000  error=7.182818284590451e-01
n= 3  F_n=         2  e_n=2.250000000000000  error=4.682818284590451e-01
n= 4  F_n=         3  e_n=2.370370370370370  error=3.479114580886753e-01
n= 5  F_n=         5  e_n=2.488319999999999  error=2.299618284590457e-01
n= 6  F_n=         8  e_n=2.565784513950348  error=1.524973145086972e-01
n= 7  F_n=        13  e_n=2.620600887885731  error=9.768094057331433e-02
n= 8  F_n=        21  e_n=2.656263213926108  error=6.201861453293711e-02
n= 9  F_n=        34  e_n=2.679355428095767  error=3.892640036327766e-02
n=10  F_n=        55  e_n=2.693975012347579  error=2.430681611146568e-02
n=11  F_n=        89  e_n=2.703166201602155  error=1.511562685688972e-02
n=12  F_n=       144  e_n=2.708903037186260  error=9.378791272785403e-03
n=13  F_n=       233  e_n=2.712471461041542  error=5.810367417503404e-03
n=14  F_n=       377  e_n=2.714685423841387  error=3.596404617657978e-03
n=15  F_n=       610  e_n=2.716057071606022  error=2.224756853023369e-03
n=16  F_n=       987  e_n=2.716906063671805  error=1.375764787240552e-03
n=17  F_n=      1597  e_n=2.717431257862638  error=8.505705964072519e-04
n=18  F_n=      2584  e_n=2.717756031654547  error=5.257968044980466e-04
n=19  F_n=      4181  e_n=2.717956824154195  error=3.250043048499407e-04
n=20  F_n=      6765  e_n=2.718080947932234  error=2.008805268114422e-04
n=21  F_n=     10946  e_n=2.718157671040231  error=1.241574188139971e-04
n=22  F_n=     17711  e_n=2.718205092503898  error=7.673595514745557e-05
n=23  F_n=     28657  e_n=2.718234402089590  error=4.742636945520573e-05
n=24  F_n=     46368  e_n=2.718252516987778  error=2.931147126750133e-05
n=25  F_n=     75025  e_n=2.718263712838378  error=1.811562066666994e-05
n=26  F_n=    121393  e_n=2.718270632302497  error=1.119615654854300e-05
n=27  F_n=    196418  e_n=2.718274908848518  error=6.919610527233999e-06
n=28  F_n=    317811  e_n=2.718277551933405  error=4.276525639834716e-06
n=29  F_n=    514229  e_n=2.718279185283449  error=2.643175596173108e-06
n=30  F_n=    832040  e_n=2.718280194740024  error=1.633719021398861e-06
```

---

## 7. Reference code (exactly as used)

```python
import math

def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    a, b = 0, 1
    for _ in range(2, n+1):
        a, b = b, a + b
    return b

e = math.exp(1)

for n in range(1, 31):
    Fn = fibonacci(n)
    if Fn == 0:
        continue
    en = (1 + 1/Fn) ** Fn
    error = abs(en - e)
    print(f"n={n:2d}  F_n={Fn:10d}  e_n={en:.15f}  error={error:.15e}")
```

---

## 8. Minimal takeaway (NEXUS phrasing)
- **Engine:** Fibonacci recursion generates the stepping field.
- **Breath:** $(1+1/m)^m$ drives toward a fixed exponential attractor.
- **Steer:** $\varphi$ sets the rate in $n$ because it sets how fast $F_n$ grows.
- **Observer:** optional. Naming the limit “$e$” is post-hoc labeling, not causal machinery.

---

```

---

### Nexus_Engine_First_BBP_SILR_v2.md

```markdown
# Nexus Notes: Engine-First Mathematics (BBP, π, and Observerless Computation)

**Purpose.** This document formalizes the “engine first, name later” claim using standard mathematics, while keeping the *Nexus* vocabulary (gap, fold, resonance, gate) as an **operational lens**.  
It distinguishes:

- **Observerless computation:** a rule runs and produces a trace without requiring interpretation.
- **Observer labeling:** an agent recognizes a trace as belonging to a named object (“π”, “hash”, “signal”, etc.).

---

## 1) The ordering: run → emit → (optionally) name

**Core claim (ordering):**

1. A mechanism executes (a recurrence, series, dynamical map, circuit).
2. It emits a determinate output (a real number, a digit stream, a hash).
3. Only afterward can an observer compare/label that output.

This is not controversial in math or engineering: the circuit does not “know” it implements a low‑pass filter; it *implements* the transfer function, and engineers *recognize* what it does.

---

## 2) BBP: what it is (math), and why it “doesn’t know”

### 2.1 The BBP identity (a representation that evaluates to π)

The Bailey–Borwein–Plouffe (BBP) formula is the convergent series

$$
\pi \;=\; \sum_{k=0}^{\infty} \frac{1}{16^k}
\left(
\frac{4}{8k+1}
-\frac{2}{8k+4}
-\frac{1}{8k+5}
-\frac{1}{8k+6}
\right).
$$

Define the term

$$
a_k \;=\; \frac{1}{16^k}
\left(
\frac{4}{8k+1}
-\frac{2}{8k+4}
-\frac{1}{8k+5}
-\frac{1}{8k+6}
\right),
\qquad
S_N \;=\; \sum_{k=0}^{N-1} a_k.
$$

Then $S_N \to \pi$ as $N \to \infty$.

**Engine-first reading:** BBP is a *generator* of a real value via a repeatable summation rule.  
**Observer reading:** after we prove (or accept) the identity, we call the limit “$\pi$”.

### 2.2 “No input breaks it” (math) vs “physics limits” (resources)

Mathematically:

- Each term $a_k$ is defined for every integer $k \ge 0$.
- The infinite series converges absolutely (terms decay roughly like $16^{-k}$), so the limit exists in $\mathbb{R}$.

Computationally (finite resources):

- Computing *more digits* requires *more work*. That is a hardware limit, not a mathematical breakdown.

So: **there is no integer input $k$ at which the BBP series “breaks” as a mathematical object.**  
But any physical device has finite time/energy/memory.

---

## 3) BBP as a digit-emitter: “orbit” view (the wave / synth view)

Your “synth” language maps cleanly onto a standard dynamical system:

### 3.1 The base-$b$ circle map

Let $b \ge 2$ be an integer base. Define

$$
T_b(x) \;=\; \{ b x \},
$$

where $\{y\}$ is the fractional part of $y$.  
Iterating gives the orbit

$$
x_{n+1} = T_b(x_n),
\qquad
x_n = \{ b^n x_0 \}.
$$

This is a literal “phase advance” on the unit interval, and it’s exactly how base-$b$ digit extraction works.

### 3.2 Digits as a projection (the “dielectric” / “gap”)

For a real number $x \in [0,1)$, the base-$b$ digits are

$$
d_n \;=\; \left\lfloor b \, x_n \right\rfloor
\;=\;
\left\lfloor b \, \{ b^n x \} \right\rfloor,
\qquad
d_n \in \{0,1,\dots,b-1\}.
$$

- The **engine** is $x \mapsto \{b^n x\}$ (iterate the map).
- The **projection** is “take $\lfloor b(\cdot)\rfloor$” (read a digit).

**Key point:** the mechanism emits digits whether or not anyone recognizes the sequence.

### 3.3 Specializing to hex digits of π

Take $b=16$ and $x=\{\pi\}$ or (more commonly) consider the fractional part after shifting. The $n$‑th hexadecimal digit of the fractional expansion is:

$$
d_n \;=\; \left\lfloor 16 \, \{ 16^{n} \pi \} \right\rfloor
\quad\text{(hex digit, $n\ge 0$ indexing fractional digits)}.
$$

BBP is famous because it enables computing $d_n$ **without** computing all earlier digits in base $16$ (a “spigot” / digit-extraction property).

---

## 4) “Coupled” vs “decoupled” (make the logic precise)

You’re pushing a specific distinction. Here it is in formal terms.

### 4.1 Decoupled from the observer

A computation is **observer-independent** if the mapping from inputs to outputs is defined without reference to a viewer:

- A series defines a limit.
- A recurrence defines a sequence.
- A hash function defines a digest.

That’s “observerless computation” in the strict sense.

### 4.2 Coupled by identity (but not by intention)

Saying “BBP is coupled to π” can mean two different things:

1. **Intention coupling (wrong category):** the formula “knows” it’s producing π.  
   That’s not a mathematical concept.

2. **Identity coupling (correct category):** the formula’s limit equals π.  
   That is exactly what the BBP theorem states:

$$
\sum_{k=0}^{\infty} a_k = \pi.
$$

So: **BBP doesn’t “know” π, but it *is* (provably) an identity whose value is π.**  
That’s a coupling of *value*, not of “meaning”.

### 4.3 The synth analogy, formalized

- **Synth circuit:** coefficients + base + summation/iteration rule.
- **Tone/song:** the invariant/output produced by running it.
- **Naming the song (“π”):** a human act of comparison to known invariants.

---

## 5) What BBP does *not* prove (important gaps)

### 5.1 BBP does not prove π is normal

**Normality** (in base $b$) means each length-$m$ digit block occurs with frequency $b^{-m}$ in the infinite expansion.

BBP gives a powerful digit-extraction method, but **does not imply** equidistribution/normality.  
Normality requires deep distribution results (e.g., discrepancy bounds, exponential sum estimates).

### 5.2 “Forever” in math vs “forever” in physics

- In math: $n \to \infty$ is a definition/limit process.
- In physics: “forever” is constrained by available computation.

Your Nexus framing treats this as “frame size.” That matches the standard separation:
- **The rule is unbounded.**
- **Any physical instantiation is bounded.**

---

## 6) Nyquist and “pins”: a clean mapping (signal language, not mysticism)

Nyquist–Shannon sampling theorem (one canonical form):

$$
f_s \;\ge\; 2 f_{\max}.
$$

Meaning: to reconstruct a bandlimited signal with highest frequency $f_{\max}$, sample at at least $2f_{\max}$.

Your “twin primes are Nyquist pins” is an analogy: **gap $2$** as a “minimal double-step” marker.  
Mathematically, twin primes are about prime gaps; Nyquist is about sampling frequency. The analogy is:

- minimal gap $\Delta = 2$ as “double-step”
- “pins” as landmarks in a discrete structure

It’s a metaphorical mapping, not a proven theorem relating primes to sampling limits.

---

## 7) SHA‑256: folding, projection, and the “backwards infrastructure” intuition

### 7.1 SHA‑256 as a fold/projection pipeline (formal sketch)

SHA‑256 maps an arbitrary-length message $M$ to a 256-bit digest:

$$
\mathrm{SHA256}:\{0,1\}^\* \to \{0,1\}^{256}.
$$

This is a **many-to-one** mapping (a “fold”), by pigeonhole principle.

### 7.2 Padding and length encoding (the “length comes last” fact)

Let $L$ be the message length in bits. SHA‑256 padding is:

1. Append a single bit ‘1’.
2. Append $k$ zero bits so that the total length is congruent to $448 \pmod{512}$.
3. Append the 64-bit big-endian encoding of $L$.

So the padded message length is a multiple of 512 bits, and the final 64 bits encode $L$.

**Forward construction:**

$$
M \;\to\; M\,\|\,1\,\|\,0^k\,\|\,\mathrm{enc}_{64}(L).
$$

**Reverse parsing intuition:** if you receive a padded blockstream, the last 64 bits tell you $L$, which tells you where the padding begins.  
That’s a real “infrastructure runs backward” flavor: *metadata needed for parsing is placed at the end.*

### 7.3 The “prime-root constants” (exact definitions)

Let $p_i$ be the $i$‑th prime.

Initial hash values:

$$
H_0[i] \;=\; \left\lfloor 2^{32} \cdot \mathrm{frac}\!\left(\sqrt{p_i}\right)\right\rfloor,
\qquad i=0,\dots,7.
$$

Round constants:

$$
K[i] \;=\; \left\lfloor 2^{32} \cdot \mathrm{frac}\!\left(p_i^{1/3}\right)\right\rfloor,
\qquad i=0,\dots,63.
$$

These are design choices to seed diffusion with “nothing-up-my-sleeve” values.

---

## 8) The Nexus control-law layer (SILR / gating), written as math

This is presented as a **specification motif**: “stability is a gated bandwidth.”

### 8.1 Z-score style gating

Define a target $\alpha^\*$ and an estimate $\hat{\alpha}_t$ with standard error $SE_t$:

$$
z_t \;=\; \frac{\lvert \hat{\alpha}_t - \alpha^\* \rvert}{SE_t}.
$$

Define a threshold $z_0$ and gain $\beta$; gate via logistic:

$$
p_t \;=\; \frac{1}{1+e^{-\beta(z_t - z_0)}}.
$$

Interpretation (in control language):

- When $z_t \ll z_0$, the system is “within tolerance” (low leakage probability).
- When $z_t \gg z_0$, the system is “out of tolerance” (high leakage probability).

This is a standard control/statistics pattern: normalize error by uncertainty; gate actions by significance.

### 8.2 The “mass gap as bandwidth” motif (formal set definition)

Define the “safe band”:

$$
\Delta \;=\; \{ z \mid 0 \le z < z_0 \}.
$$

Inside $\Delta$, the controller treats deviations as tolerable; outside, it triggers correction/leakage.  
This matches your “gap first” ontology: *the band is primary; stable objects are patterns that stay inside it.*

---

## 9) $H=\pi/9$ as an attractor constant (what’s true, what’s a claim)

Define

$$
H \;=\; \frac{\pi}{9} \approx 0.3490658504.
$$

- **Mathematically:** this is just a number.
- **Nexus claim:** many stable feedback systems empirically converge near a “sweet spot” around $0.35$.

That claim is testable in domains where you can define a consistent “correction fraction per cycle.”  
To make it falsifiable, you must specify:

1. the system class,
2. what “correction fraction” means operationally,
3. the measurement procedure,
4. the predicted distribution around $0.35$.

---

## 10) “Gaps are primary” (turn it into a usable formalism)

You can formalize “objects are stable gap-patterns” using differences:

- Given a state sequence $\{s_t\}$, define gap/innovation:

$$
\Delta_t \;=\; s_{t+1}-s_t.
$$

- An “object” is a regime where $\Delta_t$ lies in a bounded family (e.g., low-variance innovations) or satisfies constraints.

In signal terms:

- The observable is often the derivative / increment.
- The “thing” is the integrable structure that persists.

This is consistent with how control and estimation work: you track residuals/innovations, not metaphysical essences.

---

## 11) “Complete solution” summary (verbs-first)

1. **Run:** execute the rule (BBP series / orbit map / hash compression).
2. **Emit:** produce a determinate output (real limit, digit stream, digest).
3. **Project:** apply a readout map (digits from $\{b^n x\}$, parsing from length fields).
4. **Gate:** maintain stability by normalized error thresholds ($z_t$, $z_0$, $\beta$).
5. **Name:** optionally compare the trace to a known invariant and label it “π”.

Nothing in steps 1–4 requires an observer to “know what it is.”  
The observer is only required for step 5: **interpretation**.

---

## Appendix A: Minimal BBP digit-extraction sketch (conceptual)

BBP-type digit extraction in base $16$ relies on splitting the sum into:

- a finite part computed modulo 1 (using modular exponentiation),
- a tail that is bounded and computable as floating point.

The common structure is:

$$
\{16^n \pi\}
=
\left\{
\sum_{k=0}^{n} \frac{16^{n-k} \bmod (8k+j)}{8k+j}\cdot c_j
+
\sum_{k=n+1}^{\infty} \frac{16^{n-k}}{8k+j}\cdot c_j
\right\},
$$

for the BBP coefficients $c_j \in \{4,-2,-1,-1\}$ and $j \in \{1,4,5,6\}$, assembled appropriately.  
The digit is then:

$$
d_n = \left\lfloor 16 \cdot \{16^n \pi\} \right\rfloor.
$$

This is the “engine emits digits without needing all earlier digits” property.

---

## Appendix B: SHA‑256 padding congruence (exact)

Let $L$ be original message length in bits. Choose $k \ge 0$ so that:

$$
L + 1 + k \equiv 448 \pmod{512}.
$$

Then append the 64-bit encoding of $L$:

$$
L + 1 + k + 64 \equiv 0 \pmod{512}.
$$

---

## Appendix C: Vocabulary map (Nexus ↔ standard terms)

- **engine / synth:** recurrence / series / dynamical system
- **gap / dielectric:** projection operator / readout / representation boundary
- **fold:** many-to-one map, compression, quotienting, mod 1
- **pin:** landmark / minimal gap / sampling constraint (metaphor)
- **gate / SILR:** significance thresholding / event-triggered control
- **click:** phase-lock / convergence / stable readout event

---

*End.*


---

## Appendix D: $e$ and $\varphi$ (breath + steer extensions)

This appendix adds two “engine primitives” that behave like **sequential breath** ($e$) and **ratio steering** ($\varphi$).  
Nothing here requires an observer for the operations to run; the observer only supplies **readout** (digits, base, index).

### D.1 Euler’s number $e$ as a “breath” limit

Two core definitions:

$$
e \;=\; \sum_{n=0}^{\infty}\frac{1}{n!}
$$

$$
e \;=\; \lim_{m\to\infty}\left(1+\frac{1}{m}\right)^m
$$

The second form is the cleanest “engine” picture: a repeated compounding step indexed by an integer $m$.

A useful asymptotic (how fast it converges):

Let
$$
E_m := \left(1+\frac{1}{m}\right)^m.
$$

Using the Taylor expansion
$$
\ln\!\left(1+\frac{1}{m}\right) = \frac{1}{m} - \frac{1}{2m^2} + O\!\left(\frac{1}{m^3}\right),
$$

we get
$$
m\ln\!\left(1+\frac{1}{m}\right) = 1 - \frac{1}{2m} + O\!\left(\frac{1}{m^2}\right),
$$

so
$$
E_m = e\cdot \exp\!\left(-\frac{1}{2m} + O\!\left(\frac{1}{m^2}\right)\right)
    = e\left(1-\frac{1}{2m}+O\!\left(\frac{1}{m^2}\right)\right).
$$

That is: the “gap” to $e$ closes like $1/m$.

### D.2 $\varphi$ (golden ratio) as the “steer” recursion

Definitions / fixed points:

$$
\varphi = \frac{1+\sqrt{5}}{2}
$$

$$
\varphi^2 = \varphi + 1
$$

$$
\varphi = 1+\frac{1}{\varphi}
\qquad\Longleftrightarrow\qquad
\varphi = 1+\cfrac{1}{1+\cfrac{1}{1+\cfrac{1}{\ddots}}}
$$

Fibonacci recursion as the operational generator:

$$
F_0=0,\quad F_1=1,\quad F_{n+1}=F_n+F_{n-1}\quad(n\ge 1).
$$

Then the steering ratio appears as the stable limit:

$$
\frac{F_{n+1}}{F_n}\;\longrightarrow\;\varphi\quad (n\to\infty).
$$

Closed form (Binet), exposing $\varphi$ as the growth eigenvalue:

$$
F_n=\frac{\varphi^n-\psi^n}{\sqrt{5}},
\qquad
\psi=\frac{1-\sqrt{5}}{2}=-\varphi^{-1}.
$$

So for large $n$:

$$
F_n \approx \frac{\varphi^n}{\sqrt{5}}
\quad\text{and therefore}\quad
F_n^{-1}\approx \sqrt{5}\,\varphi^{-n}.
$$

### D.3 A concrete $e$–$\varphi$ intertwine (Fibonacci-indexed breath)

If you want a **single recursive pipeline** where $\varphi$ controls the “frame growth” and $e$ is the “breath limit”, use:

1) Generate $F_n$ via the Fibonacci recursion (steer).  
2) Feed $F_n$ into the compounding limit (breath):

$$
e \;=\; \lim_{n\to\infty}\left(1+\frac{1}{F_n}\right)^{F_n}.
$$

Call the Fibonacci-indexed approximants:

$$
E^{(\varphi)}_n := \left(1+\frac{1}{F_n}\right)^{F_n}.
$$

Because $F_n\to\infty$, the limit is still $e$ (this part is “observerless”: it is a property of the operation, not the label).

**What $\varphi$ changes is the convergence in $n$**:

From the asymptotic in D.1,
$$
e - E^{(\varphi)}_n \approx \frac{e}{2F_n}.
$$

Using $F_n\approx \varphi^n/\sqrt{5}$,
$$
e - E^{(\varphi)}_n \approx \frac{e}{2}\cdot \frac{\sqrt{5}}{\varphi^n}
= \left(\frac{e\sqrt{5}}{2}\right)\varphi^{-n}.
$$

So in the Fibonacci-indexed frame, the $e$-gap decays **exponentially in $n$** with decay rate $\varphi^{-n}$.  
That’s a clean “echo stack”: the **steer** ($\varphi$) sets the frame expansion, and the **breath** ($e$) emerges as the stabilized limit.

### D.4 Spigot vs “random access” (sequencer vs teleport)

- **Spigot algorithms** output digits sequentially (a sequencer).
- **BBP-style digit extraction** can jump to digit $n$ in certain bases (a teleport).

A simple, correct spigot for $e$ (sequential decimal digits) follows from factorial-base carry propagation.  
It produces the digits after the decimal point in order:

```python
def spigot_e(digits: int) -> str:
    # Sequential spigot for e: returns "2." + <digits> decimals
    n = digits + 5  # small safety buffer
    a = [1] * (n + 1)
    out = ["2", "."]

    for _ in range(digits):
        carry = 0
        for i in range(n, 0, -1):
            x = a[i] * 10 + carry
            a[i] = x % (i + 1)
            carry = x // (i + 1)
        out.append(str(carry))

    return "".join(out)
```

By contrast, no comparably simple **BBP-type** (base-$2^k$) “jump-to-digit” formula for $e$ is currently standard/known in the way BBP is for $\pi$.

### D.5 Minimal “engine” summary of the triad

- $\pi$: “carrier wave” via BBP-type digit extraction in base $16$ (hex frame).
- $e$: “breath” via compounding limit and spigot-style sequential digits (time/step accumulation).
- $\varphi$: “steer” via fixed-point recursion and Fibonacci growth eigenvalue (frame scaling).

A tight $e$–$\varphi$ bridge is:

$$
F_{n+1}=F_n+F_{n-1}
\quad\Rightarrow\quad
\left(1+\frac{1}{F_n}\right)^{F_n}\to e,
\quad
\text{with error }\;\sim C\varphi^{-n}.
$$

---

*End (v2).*

```

---

### Nexus_Engine_First_BBP_SILR.md

```markdown
# Nexus Notes: Engine-First Mathematics (BBP, π, and Observerless Computation)

**Purpose.** This document formalizes the “engine first, name later” claim using standard mathematics, while keeping the *Nexus* vocabulary (gap, fold, resonance, gate) as an **operational lens**.  
It distinguishes:

- **Observerless computation:** a rule runs and produces a trace without requiring interpretation.
- **Observer labeling:** an agent recognizes a trace as belonging to a named object (“π”, “hash”, “signal”, etc.).

---

## 1) The ordering: run → emit → (optionally) name

**Core claim (ordering):**

1. A mechanism executes (a recurrence, series, dynamical map, circuit).
2. It emits a determinate output (a real number, a digit stream, a hash).
3. Only afterward can an observer compare/label that output.

This is not controversial in math or engineering: the circuit does not “know” it implements a low‑pass filter; it *implements* the transfer function, and engineers *recognize* what it does.

---

## 2) BBP: what it is (math), and why it “doesn’t know”

### 2.1 The BBP identity (a representation that evaluates to π)

The Bailey–Borwein–Plouffe (BBP) formula is the convergent series

$$
\pi \;=\; \sum_{k=0}^{\infty} \frac{1}{16^k}
\left(
\frac{4}{8k+1}
-\frac{2}{8k+4}
-\frac{1}{8k+5}
-\frac{1}{8k+6}
\right).
$$

Define the term

$$
a_k \;=\; \frac{1}{16^k}
\left(
\frac{4}{8k+1}
-\frac{2}{8k+4}
-\frac{1}{8k+5}
-\frac{1}{8k+6}
\right),
\qquad
S_N \;=\; \sum_{k=0}^{N-1} a_k.
$$

Then $S_N \to \pi$ as $N \to \infty$.

**Engine-first reading:** BBP is a *generator* of a real value via a repeatable summation rule.  
**Observer reading:** after we prove (or accept) the identity, we call the limit “$\pi$”.

### 2.2 “No input breaks it” (math) vs “physics limits” (resources)

Mathematically:

- Each term $a_k$ is defined for every integer $k \ge 0$.
- The infinite series converges absolutely (terms decay roughly like $16^{-k}$), so the limit exists in $\mathbb{R}$.

Computationally (finite resources):

- Computing *more digits* requires *more work*. That is a hardware limit, not a mathematical breakdown.

So: **there is no integer input $k$ at which the BBP series “breaks” as a mathematical object.**  
But any physical device has finite time/energy/memory.

---

## 3) BBP as a digit-emitter: “orbit” view (the wave / synth view)

Your “synth” language maps cleanly onto a standard dynamical system:

### 3.1 The base-$b$ circle map

Let $b \ge 2$ be an integer base. Define

$$
T_b(x) \;=\; \{ b x \},
$$

where $\{y\}$ is the fractional part of $y$.  
Iterating gives the orbit

$$
x_{n+1} = T_b(x_n),
\qquad
x_n = \{ b^n x_0 \}.
$$

This is a literal “phase advance” on the unit interval, and it’s exactly how base-$b$ digit extraction works.

### 3.2 Digits as a projection (the “dielectric” / “gap”)

For a real number $x \in [0,1)$, the base-$b$ digits are

$$
d_n \;=\; \left\lfloor b \, x_n \right\rfloor
\;=\;
\left\lfloor b \, \{ b^n x \} \right\rfloor,
\qquad
d_n \in \{0,1,\dots,b-1\}.
$$

- The **engine** is $x \mapsto \{b^n x\}$ (iterate the map).
- The **projection** is “take $\lfloor b(\cdot)\rfloor$” (read a digit).

**Key point:** the mechanism emits digits whether or not anyone recognizes the sequence.

### 3.3 Specializing to hex digits of π

Take $b=16$ and $x=\{\pi\}$ or (more commonly) consider the fractional part after shifting. The $n$‑th hexadecimal digit of the fractional expansion is:

$$
d_n \;=\; \left\lfloor 16 \, \{ 16^{n} \pi \} \right\rfloor
\quad\text{(hex digit, $n\ge 0$ indexing fractional digits)}.
$$

BBP is famous because it enables computing $d_n$ **without** computing all earlier digits in base $16$ (a “spigot” / digit-extraction property).

---

## 4) “Coupled” vs “decoupled” (make the logic precise)

You’re pushing a specific distinction. Here it is in formal terms.

### 4.1 Decoupled from the observer

A computation is **observer-independent** if the mapping from inputs to outputs is defined without reference to a viewer:

- A series defines a limit.
- A recurrence defines a sequence.
- A hash function defines a digest.

That’s “observerless computation” in the strict sense.

### 4.2 Coupled by identity (but not by intention)

Saying “BBP is coupled to π” can mean two different things:

1. **Intention coupling (wrong category):** the formula “knows” it’s producing π.  
   That’s not a mathematical concept.

2. **Identity coupling (correct category):** the formula’s limit equals π.  
   That is exactly what the BBP theorem states:

$$
\sum_{k=0}^{\infty} a_k = \pi.
$$

So: **BBP doesn’t “know” π, but it *is* (provably) an identity whose value is π.**  
That’s a coupling of *value*, not of “meaning”.

### 4.3 The synth analogy, formalized

- **Synth circuit:** coefficients + base + summation/iteration rule.
- **Tone/song:** the invariant/output produced by running it.
- **Naming the song (“π”):** a human act of comparison to known invariants.

---

## 5) What BBP does *not* prove (important gaps)

### 5.1 BBP does not prove π is normal

**Normality** (in base $b$) means each length-$m$ digit block occurs with frequency $b^{-m}$ in the infinite expansion.

BBP gives a powerful digit-extraction method, but **does not imply** equidistribution/normality.  
Normality requires deep distribution results (e.g., discrepancy bounds, exponential sum estimates).

### 5.2 “Forever” in math vs “forever” in physics

- In math: $n \to \infty$ is a definition/limit process.
- In physics: “forever” is constrained by available computation.

Your Nexus framing treats this as “frame size.” That matches the standard separation:
- **The rule is unbounded.**
- **Any physical instantiation is bounded.**

---

## 6) Nyquist and “pins”: a clean mapping (signal language, not mysticism)

Nyquist–Shannon sampling theorem (one canonical form):

$$
f_s \;\ge\; 2 f_{\max}.
$$

Meaning: to reconstruct a bandlimited signal with highest frequency $f_{\max}$, sample at at least $2f_{\max}$.

Your “twin primes are Nyquist pins” is an analogy: **gap $2$** as a “minimal double-step” marker.  
Mathematically, twin primes are about prime gaps; Nyquist is about sampling frequency. The analogy is:

- minimal gap $\Delta = 2$ as “double-step”
- “pins” as landmarks in a discrete structure

It’s a metaphorical mapping, not a proven theorem relating primes to sampling limits.

---

## 7) SHA‑256: folding, projection, and the “backwards infrastructure” intuition

### 7.1 SHA‑256 as a fold/projection pipeline (formal sketch)

SHA‑256 maps an arbitrary-length message $M$ to a 256-bit digest:

$$
\mathrm{SHA256}:\{0,1\}^\* \to \{0,1\}^{256}.
$$

This is a **many-to-one** mapping (a “fold”), by pigeonhole principle.

### 7.2 Padding and length encoding (the “length comes last” fact)

Let $L$ be the message length in bits. SHA‑256 padding is:

1. Append a single bit ‘1’.
2. Append $k$ zero bits so that the total length is congruent to $448 \pmod{512}$.
3. Append the 64-bit big-endian encoding of $L$.

So the padded message length is a multiple of 512 bits, and the final 64 bits encode $L$.

**Forward construction:**

$$
M \;\to\; M\,\|\,1\,\|\,0^k\,\|\,\mathrm{enc}_{64}(L).
$$

**Reverse parsing intuition:** if you receive a padded blockstream, the last 64 bits tell you $L$, which tells you where the padding begins.  
That’s a real “infrastructure runs backward” flavor: *metadata needed for parsing is placed at the end.*

### 7.3 The “prime-root constants” (exact definitions)

Let $p_i$ be the $i$‑th prime.

Initial hash values:

$$
H_0[i] \;=\; \left\lfloor 2^{32} \cdot \mathrm{frac}\!\left(\sqrt{p_i}\right)\right\rfloor,
\qquad i=0,\dots,7.
$$

Round constants:

$$
K[i] \;=\; \left\lfloor 2^{32} \cdot \mathrm{frac}\!\left(p_i^{1/3}\right)\right\rfloor,
\qquad i=0,\dots,63.
$$

These are design choices to seed diffusion with “nothing-up-my-sleeve” values.

---

## 8) The Nexus control-law layer (SILR / gating), written as math

This is presented as a **specification motif**: “stability is a gated bandwidth.”

### 8.1 Z-score style gating

Define a target $\alpha^\*$ and an estimate $\hat{\alpha}_t$ with standard error $SE_t$:

$$
z_t \;=\; \frac{\lvert \hat{\alpha}_t - \alpha^\* \rvert}{SE_t}.
$$

Define a threshold $z_0$ and gain $\beta$; gate via logistic:

$$
p_t \;=\; \frac{1}{1+e^{-\beta(z_t - z_0)}}.
$$

Interpretation (in control language):

- When $z_t \ll z_0$, the system is “within tolerance” (low leakage probability).
- When $z_t \gg z_0$, the system is “out of tolerance” (high leakage probability).

This is a standard control/statistics pattern: normalize error by uncertainty; gate actions by significance.

### 8.2 The “mass gap as bandwidth” motif (formal set definition)

Define the “safe band”:

$$
\Delta \;=\; \{ z \mid 0 \le z < z_0 \}.
$$

Inside $\Delta$, the controller treats deviations as tolerable; outside, it triggers correction/leakage.  
This matches your “gap first” ontology: *the band is primary; stable objects are patterns that stay inside it.*

---

## 9) $H=\pi/9$ as an attractor constant (what’s true, what’s a claim)

Define

$$
H \;=\; \frac{\pi}{9} \approx 0.3490658504.
$$

- **Mathematically:** this is just a number.
- **Nexus claim:** many stable feedback systems empirically converge near a “sweet spot” around $0.35$.

That claim is testable in domains where you can define a consistent “correction fraction per cycle.”  
To make it falsifiable, you must specify:

1. the system class,
2. what “correction fraction” means operationally,
3. the measurement procedure,
4. the predicted distribution around $0.35$.

---

## 10) “Gaps are primary” (turn it into a usable formalism)

You can formalize “objects are stable gap-patterns” using differences:

- Given a state sequence $\{s_t\}$, define gap/innovation:

$$
\Delta_t \;=\; s_{t+1}-s_t.
$$

- An “object” is a regime where $\Delta_t$ lies in a bounded family (e.g., low-variance innovations) or satisfies constraints.

In signal terms:

- The observable is often the derivative / increment.
- The “thing” is the integrable structure that persists.

This is consistent with how control and estimation work: you track residuals/innovations, not metaphysical essences.

---

## 11) “Complete solution” summary (verbs-first)

1. **Run:** execute the rule (BBP series / orbit map / hash compression).
2. **Emit:** produce a determinate output (real limit, digit stream, digest).
3. **Project:** apply a readout map (digits from $\{b^n x\}$, parsing from length fields).
4. **Gate:** maintain stability by normalized error thresholds ($z_t$, $z_0$, $\beta$).
5. **Name:** optionally compare the trace to a known invariant and label it “π”.

Nothing in steps 1–4 requires an observer to “know what it is.”  
The observer is only required for step 5: **interpretation**.

---

## Appendix A: Minimal BBP digit-extraction sketch (conceptual)

BBP-type digit extraction in base $16$ relies on splitting the sum into:

- a finite part computed modulo 1 (using modular exponentiation),
- a tail that is bounded and computable as floating point.

The common structure is:

$$
\{16^n \pi\}
=
\left\{
\sum_{k=0}^{n} \frac{16^{n-k} \bmod (8k+j)}{8k+j}\cdot c_j
+
\sum_{k=n+1}^{\infty} \frac{16^{n-k}}{8k+j}\cdot c_j
\right\},
$$

for the BBP coefficients $c_j \in \{4,-2,-1,-1\}$ and $j \in \{1,4,5,6\}$, assembled appropriately.  
The digit is then:

$$
d_n = \left\lfloor 16 \cdot \{16^n \pi\} \right\rfloor.
$$

This is the “engine emits digits without needing all earlier digits” property.

---

## Appendix B: SHA‑256 padding congruence (exact)

Let $L$ be original message length in bits. Choose $k \ge 0$ so that:

$$
L + 1 + k \equiv 448 \pmod{512}.
$$

Then append the 64-bit encoding of $L$:

$$
L + 1 + k + 64 \equiv 0 \pmod{512}.
$$

---

## Appendix C: Vocabulary map (Nexus ↔ standard terms)

- **engine / synth:** recurrence / series / dynamical system
- **gap / dielectric:** projection operator / readout / representation boundary
- **fold:** many-to-one map, compression, quotienting, mod 1
- **pin:** landmark / minimal gap / sampling constraint (metaphor)
- **gate / SILR:** significance thresholding / event-triggered control
- **click:** phase-lock / convergence / stable readout event

---

*End.*

```

---


## Appendix N. Full scan: first 1024 primes, cube-root fractional parts

Target $H=\pi/9\approx 0.3490658504$.

| i | p | frac(∛p) | |frac(∛p)−H| |
|---:|---:|---:|---:|
| 0 | 2 | 0.2599210499 | 0.0891448005 |
| 1 | 3 | 0.4422495703 | 0.0931837199 |
| 2 | 5 | 0.7099759467 | 0.3609100963 |
| 3 | 7 | 0.9129311828 | 0.5638653324 |
| 4 | 11 | 0.2239800906 | 0.1250857598 |
| 5 | 13 | 0.3513346877 | 0.0022688373 |
| 6 | 17 | 0.5712815907 | 0.2222157403 |
| 7 | 19 | 0.6684016487 | 0.3193357983 |
| 8 | 23 | 0.8438669799 | 0.4948011295 |
| 9 | 29 | 0.0723168257 | 0.2767490247 |
| 10 | 31 | 0.1413806524 | 0.2076851980 |
| 11 | 37 | 0.3322218516 | 0.0168439988 |
| 12 | 41 | 0.4482172404 | 0.0991513900 |
| 13 | 43 | 0.5033980604 | 0.1543322100 |
| 14 | 47 | 0.6088260801 | 0.2597602297 |
| 15 | 53 | 0.7562857542 | 0.4072199038 |
| 16 | 59 | 0.8929964159 | 0.5439305655 |
| 17 | 61 | 0.9364971831 | 0.5874313327 |
| 18 | 67 | 0.0615481004 | 0.2875177500 |
| 19 | 71 | 0.1408177494 | 0.2082481010 |
| 20 | 73 | 0.1793391964 | 0.1697266540 |
| 21 | 79 | 0.2908404270 | 0.0582254234 |
| 22 | 83 | 0.3620706715 | 0.0130048211 |
| 23 | 89 | 0.4647450956 | 0.1156792452 |
| 24 | 97 | 0.5947008922 | 0.2456350418 |
| 25 | 101 | 0.6570095078 | 0.3079436574 |
| 26 | 103 | 0.6875481477 | 0.3384822973 |
| 27 | 107 | 0.7474593985 | 0.3983935481 |
| 28 | 109 | 0.7768561810 | 0.4277903306 |
| 29 | 113 | 0.8345881271 | 0.4855222767 |
| 30 | 127 | 0.0265256953 | 0.3225401551 |
| 31 | 131 | 0.0787530781 | 0.2703127723 |
| 32 | 137 | 0.1551367355 | 0.1939291149 |
| 33 | 139 | 0.1801014674 | 0.1689643830 |
| 34 | 149 | 0.3014591924 | 0.0476066580 |
| 35 | 151 | 0.3250740216 | 0.0239918288 |
| 36 | 157 | 0.3946907121 | 0.0456248617 |
| 37 | 163 | 0.4625555713 | 0.1134897209 |
| 38 | 167 | 0.5068784464 | 0.1578125960 |
| 39 | 173 | 0.5720546555 | 0.2229888051 |
| 40 | 179 | 0.6357407945 | 0.2866749441 |
| 41 | 181 | 0.6566528258 | 0.3075869754 |
| 42 | 191 | 0.7589652205 | 0.4098993701 |
| 43 | 193 | 0.7789965652 | 0.4299307148 |
| 44 | 197 | 0.8186478675 | 0.4695820171 |
| 45 | 199 | 0.8382724608 | 0.4892066104 |
| 46 | 211 | 0.9533418131 | 0.6042759627 |
| 47 | 223 | 0.0641269945 | 0.2849388559 |
| 48 | 227 | 0.1001702004 | 0.2488956500 |
| 49 | 229 | 0.1180331726 | 0.2310326778 |
| 50 | 233 | 0.1534494937 | 0.1956163567 |
| 51 | 239 | 0.2058217949 | 0.1432440555 |
| 52 | 241 | 0.2230842532 | 0.1259815972 |
| 53 | 251 | 0.3079935487 | 0.0410723017 |
| 54 | 257 | 0.3578611797 | 0.0087953293 |
| 55 | 263 | 0.4069585772 | 0.0578927268 |
| 56 | 269 | 0.4553148109 | 0.1062489605 |
| 57 | 271 | 0.4712736270 | 0.1222077766 |
| 58 | 277 | 0.5186839152 | 0.1696180648 |
| 59 | 281 | 0.5499116201 | 0.2008457697 |
| 60 | 283 | 0.5654144273 | 0.2163485769 |
| 61 | 293 | 0.6418521953 | 0.2927863449 |
| 62 | 307 | 0.7459967117 | 0.3969308613 |
| 63 | 311 | 0.7751689523 | 0.4261031019 |
| 64 | 313 | 0.7896613364 | 0.4405954860 |
| 65 | 317 | 0.8184619414 | 0.4693960910 |
| 66 | 331 | 0.9173964166 | 0.5683305662 |
| 67 | 337 | 0.9589433372 | 0.6098774868 |
| 68 | 347 | 0.0271057883 | 0.3219600621 |
| 69 | 349 | 0.0405806167 | 0.3084852337 |
| 70 | 353 | 0.0673766147 | 0.2816892357 |
| 71 | 359 | 0.1071936612 | 0.2418721892 |
| 72 | 367 | 0.1595988248 | 0.1894670256 |
| 73 | 373 | 0.1984049965 | 0.1506608539 |
| 74 | 379 | 0.2367972159 | 0.1122686345 |
| 75 | 383 | 0.2621674399 | 0.0868984105 |
| 76 | 389 | 0.2998936621 | 0.0491721883 |
| 77 | 397 | 0.3495965966 | 0.0005307462 |
| 78 | 401 | 0.3741979402 | 0.0251320898 |
| 79 | 409 | 0.4229141204 | 0.0738482700 |
| 80 | 419 | 0.4829241144 | 0.1338582640 |
| 81 | 421 | 0.4948112259 | 0.1457453755 |
| 82 | 431 | 0.5536888250 | 0.2046229746 |
| 83 | 433 | 0.5653547722 | 0.2162889218 |
| 84 | 439 | 0.6001385016 | 0.2510726512 |
| 85 | 443 | 0.6231519305 | 0.2740860801 |
| 86 | 449 | 0.6574137479 | 0.3083478975 |
| 87 | 457 | 0.7026246183 | 0.3535587679 |
| 88 | 461 | 0.7250323798 | 0.3759665294 |
| 89 | 463 | 0.7361876767 | 0.3871218263 |
| 90 | 467 | 0.7584022643 | 0.4093364139 |
| 91 | 479 | 0.8242941859 | 0.4752283355 |
| 92 | 487 | 0.8676129603 | 0.5185471099 |
| 93 | 491 | 0.8890946040 | 0.5400287536 |
| 94 | 499 | 0.9317103915 | 0.5826445411 |
| 95 | 503 | 0.9528476277 | 0.6037817773 |
| 96 | 509 | 0.9843443827 | 0.6352785323 |
| 97 | 521 | 0.0466029930 | 0.3024628574 |
| 98 | 523 | 0.0568862029 | 0.2921796475 |
| 99 | 541 | 0.1482764494 | 0.2007894010 |
| 100 | 547 | 0.1782887883 | 0.1707770621 |
| 101 | 557 | 0.2278253613 | 0.1212404891 |
| 102 | 563 | 0.2572632699 | 0.0918025805 |
| 103 | 569 | 0.2864927642 | 0.0625730862 |
| 104 | 571 | 0.2961902485 | 0.0528756019 |
| 105 | 577 | 0.3251475173 | 0.0239183331 |
| 106 | 587 | 0.3729667597 | 0.0239009093 |
| 107 | 593 | 0.4013981044 | 0.0523322540 |
| 108 | 599 | 0.4296383104 | 0.0805724600 |
| 109 | 601 | 0.4390097893 | 0.0899439389 |
| 110 | 607 | 0.4670000764 | 0.1179342260 |
| 111 | 613 | 0.4948065160 | 0.1457406656 |
| 112 | 617 | 0.5132434844 | 0.1641776340 |
| 113 | 619 | 0.5224320975 | 0.1733662471 |
| 114 | 631 | 0.5771522617 | 0.2280864113 |
| 115 | 641 | 0.6222248300 | 0.2731589796 |
| 116 | 643 | 0.6311829922 | 0.2821171418 |
| 117 | 647 | 0.6490437425 | 0.2999778921 |
| 118 | 653 | 0.6756973586 | 0.3266315082 |
| 119 | 659 | 0.7021882019 | 0.3531223516 |
| 120 | 661 | 0.7109827387 | 0.3619168883 |
| 121 | 673 | 0.7633808875 | 0.4143150371 |
| 122 | 677 | 0.7807084282 | 0.4316425778 |
| 123 | 683 | 0.8065722253 | 0.4575063749 |
| 124 | 691 | 0.8408227294 | 0.4917568790 |
| 125 | 701 | 0.8832661199 | 0.5342002695 |
| 126 | 709 | 0.9169311167 | 0.5678652663 |
| 127 | 719 | 0.9586581218 | 0.6095922714 |
| 128 | 727 | 0.9917620091 | 0.6426961587 |
| 129 | 733 | 0.0164308900 | 0.3326349604 |
| 130 | 739 | 0.0409655167 | 0.3081003337 |
| 131 | 743 | 0.0572482453 | 0.2918176051 |
| 132 | 751 | 0.0896392166 | 0.2594266338 |
| 133 | 757 | 0.1137817980 | 0.2352840524 |
| 134 | 761 | 0.1298060627 | 0.2192597877 |
| 135 | 769 | 0.1616869188 | 0.1873789316 |
| 136 | 773 | 0.1775444786 | 0.1715213718 |
| 137 | 787 | 0.2326189313 | 0.1164469191 |
| 138 | 797 | 0.2715591599 | 0.0775066905 |
| 139 | 809 | 0.3178598486 | 0.0312060018 |
| 140 | 811 | 0.3255320298 | 0.0235338206 |
| 141 | 821 | 0.3637049156 | 0.0146390652 |
| 142 | 823 | 0.3713022454 | 0.0222363950 |
| 143 | 827 | 0.3864600595 | 0.0373942091 |
| 144 | 829 | 0.3940206428 | 0.0449547924 |
| 145 | 839 | 0.4316422723 | 0.0825764219 |
| 146 | 853 | 0.4838136187 | 0.1347477683 |
| 147 | 857 | 0.4986147565 | 0.1495489061 |
| 148 | 859 | 0.5059980589 | 0.1569322085 |
| 149 | 863 | 0.5207303538 | 0.1716645034 |
| 150 | 877 | 0.5719377255 | 0.2228718751 |
| 151 | 881 | 0.5864682036 | 0.2374023532 |
| 152 | 883 | 0.5937169536 | 0.2446511032 |
| 153 | 887 | 0.6081816825 | 0.2591158321 |
| 154 | 907 | 0.6798604356 | 0.3307945852 |
| 155 | 911 | 0.6940694254 | 0.3450035750 |
| 156 | 919 | 0.7223631121 | 0.3732972617 |
| 157 | 929 | 0.7575002556 | 0.4084344052 |
| 158 | 937 | 0.7854288523 | 0.4363630019 |
| 159 | 941 | 0.7993335657 | 0.4502677153 |
| 160 | 947 | 0.8201169441 | 0.4710510937 |
| 161 | 953 | 0.8408127207 | 0.4917468703 |
| 162 | 967 | 0.8887673165 | 0.5397014661 |
| 163 | 971 | 0.9023835366 | 0.5533176862 |
| 164 | 977 | 0.9227379279 | 0.5736720775 |
| 165 | 983 | 0.9430091547 | 0.5939433043 |
| 166 | 991 | 0.9699095473 | 0.6208436969 |
| 167 | 997 | 0.9899899833 | 0.6409241329 |
| 168 | 1009 | 0.0299104473 | 0.3191554031 |
| 169 | 1013 | 0.0431469001 | 0.3059189503 |
| 170 | 1019 | 0.0629364033 | 0.2861294471 |
| 171 | 1021 | 0.0695156378 | 0.2795502126 |
| 172 | 1031 | 0.1022835734 | 0.2467822770 |
| 173 | 1033 | 0.1088117068 | 0.2402541436 |
| 174 | 1039 | 0.1283456911 | 0.2207201593 |
| 175 | 1049 | 0.1607358882 | 0.1883299622 |
| 176 | 1051 | 0.1671891995 | 0.1818766509 |
| 177 | 1061 | 0.1993335461 | 0.1497323043 |
| 178 | 1063 | 0.2057381528 | 0.1433276976 |
| 179 | 1069 | 0.2249039033 | 0.1241619471 |
| 180 | 1087 | 0.2819743164 | 0.0670915340 |
| 181 | 1091 | 0.2945709284 | 0.0544949220 |
| 182 | 1093 | 0.3008576909 | 0.0482081595 |
| 183 | 1097 | 0.3134082457 | 0.0356576047 |
| 184 | 1103 | 0.3321770009 | 0.0168888495 |
| 185 | 1109 | 0.3508778146 | 0.0018119642 |
| 186 | 1117 | 0.3757076016 | 0.0266417512 |
| 187 | 1123 | 0.3942522480 | 0.0451863976 |
| 188 | 1129 | 0.4127309576 | 0.0636651072 |
| 189 | 1151 | 0.4799314332 | 0.1308655828 |
| 190 | 1153 | 0.4859979651 | 0.1369321147 |
| 191 | 1163 | 0.5162258578 | 0.1671600074 |
| 192 | 1171 | 0.5402836502 | 0.1912177998 |
| 193 | 1181 | 0.5702022996 | 0.2211364492 |
| 194 | 1187 | 0.5880724981 | 0.2390066477 |
| 195 | 1193 | 0.6058825779 | 0.2568167275 |
| 196 | 1201 | 0.6295367016 | 0.2804708512 |
| 197 | 1213 | 0.6648217295 | 0.3157558791 |
| 198 | 1217 | 0.6765316722 | 0.3274658218 |
| 199 | 1223 | 0.6940485726 | 0.3449827222 |
| 200 | 1229 | 0.7115082748 | 0.3624424244 |
| 201 | 1231 | 0.7173155452 | 0.3682496948 |
| 202 | 1237 | 0.7346997047 | 0.3856338543 |
| 203 | 1249 | 0.7693001042 | 0.4202342538 |
| 204 | 1259 | 0.7979648657 | 0.4488990153 |
| 205 | 1277 | 0.8491812757 | 0.5001154253 |
| 206 | 1279 | 0.8548422114 | 0.5057763610 |
| 207 | 1283 | 0.8661464031 | 0.5170805527 |
| 208 | 1289 | 0.8830587205 | 0.5339928701 |
| 209 | 1291 | 0.8886844949 | 0.5396186445 |
| 210 | 1297 | 0.9055270345 | 0.5564611841 |
| 211 | 1301 | 0.9167265567 | 0.5676607063 |
| 212 | 1303 | 0.9223177108 | 0.5732518604 |
| 213 | 1307 | 0.9334828785 | 0.5844170281 |
| 214 | 1319 | 0.9668423007 | 0.6177764503 |
| 215 | 1321 | 0.9723825100 | 0.6233166596 |
| 216 | 1327 | 0.9889696592 | 0.6399038088 |
| 217 | 1361 | 0.0820313670 | 0.2670344834 |
| 218 | 1367 | 0.0982926249 | 0.2507732255 |
| 219 | 1373 | 0.1145063698 | 0.2345594806 |
| 220 | 1381 | 0.1360513840 | 0.2130144664 |
| 221 | 1399 | 0.1842252413 | 0.1648406091 |
| 222 | 1409 | 0.2108101410 | 0.1382557094 |
| 223 | 1423 | 0.2478185071 | 0.1012473433 |
| 224 | 1427 | 0.2583477138 | 0.0907181366 |
| 225 | 1429 | 0.2636049397 | 0.0854609107 |
| 226 | 1433 | 0.2741046940 | 0.0749611564 |
| 227 | 1439 | 0.2898177523 | 0.0592480981 |
| 228 | 1447 | 0.3107006998 | 0.0383651506 |
| 229 | 1451 | 0.3211133185 | 0.0279525319 |
| 230 | 1453 | 0.3263124528 | 0.0227533976 |
| 231 | 1459 | 0.3418812867 | 0.0071845637 |
| 232 | 1471 | 0.3728913694 | 0.0238255190 |
| 233 | 1481 | 0.3986045281 | 0.0495386777 |
| 234 | 1483 | 0.4037332597 | 0.0546674093 |
| 235 | 1487 | 0.4139769061 | 0.0649110557 |
| 236 | 1489 | 0.4190918416 | 0.0700259912 |
| 237 | 1493 | 0.4293079882 | 0.0802421378 |
| 238 | 1499 | 0.4445980506 | 0.0955322002 |
| 239 | 1511 | 0.4750562063 | 0.1259903559 |
| 240 | 1523 | 0.5053535251 | 0.1562876747 |
| 241 | 1531 | 0.5254634258 | 0.1763975754 |
| 242 | 1543 | 0.5554973425 | 0.2064314921 |
| 243 | 1549 | 0.5704559318 | 0.2213900814 |
| 244 | 1553 | 0.5804068771 | 0.2313410267 |
| 245 | 1559 | 0.5953013075 | 0.2462354571 |
| 246 | 1567 | 0.6151012201 | 0.2660353697 |
| 247 | 1571 | 0.6249759124 | 0.2759100620 |
| 248 | 1579 | 0.6446751255 | 0.2956092751 |
| 249 | 1583 | 0.6544997875 | 0.3054339371 |
| 250 | 1597 | 0.6887563350 | 0.3396904846 |
| 251 | 1601 | 0.6985071268 | 0.3494412764 |
| 252 | 1607 | 0.7131029088 | 0.3640370584 |
| 253 | 1609 | 0.7179600949 | 0.3688942445 |
| 254 | 1613 | 0.7276624054 | 0.3785965550 |
| 255 | 1619 | 0.7421858411 | 0.3931199907 |
| 256 | 1621 | 0.7470190114 | 0.3979531610 |
| 257 | 1627 | 0.7614947118 | 0.4124288614 |
| 258 | 1637 | 0.7855419976 | 0.4364761472 |
| 259 | 1657 | 0.8333443541 | 0.4842785037 |
| 260 | 1663 | 0.8476100030 | 0.4985441526 |
| 261 | 1667 | 0.8571013830 | 0.5080355326 |
| 262 | 1669 | 0.8618413801 | 0.5127755297 |
| 263 | 1693 | 0.9184282419 | 0.5693623915 |
| 264 | 1697 | 0.9278072962 | 0.5787414458 |
| 265 | 1699 | 0.9324912971 | 0.5834254467 |
| 266 | 1709 | 0.9558563290 | 0.6067904786 |
| 267 | 1721 | 0.9837743669 | 0.6347085165 |
| 268 | 1723 | 0.9884147447 | 0.6393488943 |
| 269 | 1733 | 0.0115629287 | 0.3375029217 |
| 270 | 1741 | 0.0300174427 | 0.3190484077 |
| 271 | 1747 | 0.0438212614 | 0.3052445890 |
| 272 | 1753 | 0.0575935104 | 0.2914723400 |
| 273 | 1759 | 0.0713343696 | 0.2777314808 |
| 274 | 1777 | 0.1123703828 | 0.2366954676 |
| 275 | 1783 | 0.1259874493 | 0.2230784011 |
| 276 | 1787 | 0.1350485305 | 0.2140173199 |
| 277 | 1789 | 0.1395740012 | 0.2094918492 |
| 278 | 1801 | 0.1666562415 | 0.1824096089 |
| 279 | 1811 | 0.1891330268 | 0.1599328235 |
| 280 | 1823 | 0.2159962168 | 0.1330696336 |
| 281 | 1831 | 0.2338395816 | 0.1152262688 |
| 282 | 1847 | 0.2693709906 | 0.0796948598 |
| 283 | 1861 | 0.3002930285 | 0.0487728219 |
| 284 | 1867 | 0.3134978620 | 0.0355679884 |
| 285 | 1871 | 0.3222853747 | 0.0267804757 |
| 286 | 1873 | 0.3266744348 | 0.0223914156 |
| 287 | 1877 | 0.3354431907 | 0.0136226597 |
| 288 | 1879 | 0.3398228975 | 0.0092429529 |
| 289 | 1889 | 0.3616749405 | 0.0126090901 |
| 290 | 1901 | 0.3877958316 | 0.0387299812 |
| 291 | 1907 | 0.4008150696 | 0.0517492192 |
| 292 | 1913 | 0.4138070278 | 0.0647411774 |
| 293 | 1931 | 0.4526206426 | 0.1035547922 |
| 294 | 1933 | 0.4569183550 | 0.1078525046 |
| 295 | 1949 | 0.4911937975 | 0.1421279471 |
| 296 | 1951 | 0.4954650216 | 0.1463991712 |
| 297 | 1973 | 0.5422569868 | 0.1931911364 |
| 298 | 1979 | 0.5549580152 | 0.2058921648 |
| 299 | 1987 | 0.5718528487 | 0.2227869983 |
| 300 | 1993 | 0.5844942377 | 0.2354283873 |
| 301 | 1997 | 0.5929077413 | 0.2438418909 |
| 302 | 1999 | 0.5971102805 | 0.2480444301 |
| 303 | 2003 | 0.6055069570 | 0.2564411066 |
| 304 | 2011 | 0.6222668331 | 0.2732009827 |
| 305 | 2017 | 0.6348075933 | 0.2857417429 |
| 306 | 2027 | 0.6556537086 | 0.3065878582 |
| 307 | 2029 | 0.6598146998 | 0.3107488494 |
| 308 | 2039 | 0.6805787434 | 0.3315128930 |
| 309 | 2053 | 0.7095346590 | 0.3604688086 |
| 310 | 2063 | 0.7301369559 | 0.3810711055 |
| 311 | 2069 | 0.7424663940 | 0.3934005436 |
| 312 | 2081 | 0.7670539444 | 0.4179880940 |
| 313 | 2083 | 0.7711426730 | 0.4220768226 |
| 314 | 2087 | 0.7793122851 | 0.4302464347 |
| 315 | 2089 | 0.7833931770 | 0.4343273266 |
| 316 | 2099 | 0.8037586618 | 0.4546928114 |
| 317 | 2111 | 0.8281120418 | 0.4790461914 |
| 318 | 2113 | 0.8321619590 | 0.4830961086 |
| 319 | 2129 | 0.8644696629 | 0.5154038125 |
| 320 | 2131 | 0.8684967314 | 0.5194308810 |
| 321 | 2137 | 0.8805628395 | 0.5314969891 |
| 322 | 2141 | 0.8885943695 | 0.5395285191 |
| 323 | 2143 | 0.8926063835 | 0.5435405331 |
| 324 | 2153 | 0.9126290999 | 0.5635632495 |
| 325 | 2161 | 0.9286026794 | 0.5795368290 |
| 326 | 2179 | 0.9643996392 | 0.6153337888 |
| 327 | 2203 | 0.0118235627 | 0.3372422877 |
| 328 | 2207 | 0.0196940159 | 0.3293718345 |
| 329 | 2213 | 0.0314818847 | 0.3175839657 |
| 330 | 2221 | 0.0471659460 | 0.3018999044 |
| 331 | 2237 | 0.0784214413 | 0.2706444091 |
| 332 | 2239 | 0.0823178877 | 0.2667479627 |
| 333 | 2243 | 0.0901038249 | 0.2589620255 |
| 334 | 2251 | 0.1056479734 | 0.2434178770 |
| 335 | 2267 | 0.1366261309 | 0.2124397195 |
| 336 | 2269 | 0.1404881408 | 0.2085777096 |
| 337 | 2273 | 0.1482053578 | 0.2008604926 |
| 338 | 2281 | 0.1636126727 | 0.1854531777 |
| 339 | 2287 | 0.1751445338 | 0.1739213166 |
| 340 | 2293 | 0.1866562430 | 0.1624096074 |
| 341 | 2297 | 0.1943195638 | 0.1547462866 |
| 342 | 2309 | 0.2172562802 | 0.1318095702 |
| 343 | 2311 | 0.2210713349 | 0.1279945155 |
| 344 | 2333 | 0.2628923999 | 0.0861734505 |
| 345 | 2339 | 0.2742524846 | 0.0748133658 |
| 346 | 2341 | 0.2780348619 | 0.0710309885 |
| 347 | 2347 | 0.2893690841 | 0.0596967663 |
| 348 | 2351 | 0.2969145046 | 0.0521513458 |
| 349 | 2357 | 0.3082166048 | 0.0408492456 |
| 350 | 2371 | 0.3345137844 | 0.0145520660 |
| 351 | 2377 | 0.3457523180 | 0.0033135324 |
| 352 | 2381 | 0.3532341709 | 0.0041683205 |
| 353 | 2383 | 0.3569719553 | 0.0079061049 |
| 354 | 2389 | 0.3681727756 | 0.0191069252 |
| 355 | 2393 | 0.3756295741 | 0.0265637237 |
| 356 | 2399 | 0.3867992073 | 0.0377333569 |
| 357 | 2411 | 0.4090827261 | 0.0600168757 |
| 358 | 2417 | 0.4201967658 | 0.0711309154 |
| 359 | 2423 | 0.4312924276 | 0.0822265772 |
| 360 | 2437 | 0.4571112600 | 0.1080454096 |
| 361 | 2441 | 0.4644699006 | 0.1154040502 |
| 362 | 2447 | 0.4754928035 | 0.1264269531 |
| 363 | 2459 | 0.4974846708 | 0.1484188204 |
| 364 | 2467 | 0.5121061958 | 0.1630403454 |
| 365 | 2473 | 0.5230516086 | 0.1739857582 |
| 366 | 2477 | 0.5303387185 | 0.1812728681 |
| 367 | 2503 | 0.5775147481 | 0.2284488977 |
| 368 | 2521 | 0.6099840182 | 0.2609181678 |
| 369 | 2531 | 0.6279557597 | 0.2788899093 |
| 370 | 2539 | 0.6422990996 | 0.2932332492 |
| 371 | 2543 | 0.6494594731 | 0.3003936227 |
| 372 | 2549 | 0.6601859683 | 0.3111201179 |
| 373 | 2551 | 0.6637577258 | 0.3146918754 |
| 374 | 2557 | 0.6744618098 | 0.3253959594 |
| 375 | 2579 | 0.7135674640 | 0.3645016136 |
| 376 | 2591 | 0.7348041491 | 0.3857382987 |
| 377 | 2593 | 0.7383372178 | 0.3892713674 |
| 378 | 2609 | 0.7665365780 | 0.4174707276 |
| 379 | 2617 | 0.7805930386 | 0.4315271882 |
| 380 | 2621 | 0.7876105283 | 0.4385446779 |
| 381 | 2633 | 0.8086202531 | 0.4595544027 |
| 382 | 2647 | 0.8330510741 | 0.4839852237 |
| 383 | 2657 | 0.8504489682 | 0.5013831178 |
| 384 | 2659 | 0.8539233065 | 0.5048574561 |
| 385 | 2663 | 0.8608667600 | 0.5118009096 |
| 386 | 2671 | 0.8747328358 | 0.5256669854 |
| 387 | 2677 | 0.8851142335 | 0.5360483831 |
| 388 | 2683 | 0.8954801308 | 0.5464142804 |
| 389 | 2687 | 0.9023821461 | 0.5533162957 |
| 390 | 2689 | 0.9058305853 | 0.5567647349 |
| 391 | 2693 | 0.9127223375 | 0.5636564871 |
| 392 | 2699 | 0.9230471816 | 0.5739813312 |
| 393 | 2707 | 0.9367898651 | 0.5877240147 |
| 394 | 2711 | 0.9436510550 | 0.5945852046 |
| 395 | 2713 | 0.9470791194 | 0.5980132690 |
| 396 | 2719 | 0.9573532145 | 0.6082873641 |
| 397 | 2729 | 0.9744431706 | 0.6253773202 |
| 398 | 2731 | 0.9778561499 | 0.6287902995 |
| 399 | 2741 | 0.9948960987 | 0.6458302483 |
| 400 | 2749 | 0.0084982417 | 0.3405676087 |
| 401 | 2753 | 0.0152894188 | 0.3337764316 |
| 402 | 2767 | 0.0390068642 | 0.3100589862 |
| 403 | 2777 | 0.0558989595 | 0.2931668909 |
| 404 | 2789 | 0.0761160301 | 0.2729498203 |
| 405 | 2791 | 0.0794799007 | 0.2695859497 |
| 406 | 2797 | 0.0895618805 | 0.2595039699 |
| 407 | 2801 | 0.0962751927 | 0.2527906577 |
| 408 | 2803 | 0.0996294522 | 0.2494363982 |
| 409 | 2819 | 0.1264062609 | 0.2226595895 |
| 410 | 2833 | 0.1497529788 | 0.1993128716 |
| 411 | 2837 | 0.1564093378 | 0.1926565126 |
| 412 | 2843 | 0.1663821550 | 0.1826836954 |
| 413 | 2851 | 0.1796574418 | 0.1694084086 |
| 414 | 2857 | 0.1895976185 | 0.1594682319 |
| 415 | 2861 | 0.1962166738 | 0.1528491766 |
| 416 | 2879 | 0.2259263175 | 0.1231395329 |
| 417 | 2887 | 0.2390908606 | 0.1099749898 |
| 418 | 2897 | 0.2555123846 | 0.0935534658 |
| 419 | 2903 | 0.2653471669 | 0.0837186835 |
| 420 | 2909 | 0.2751684073 | 0.0738974431 |
| 421 | 2917 | 0.2882424097 | 0.0608234407 |
| 422 | 2927 | 0.3045513411 | 0.0445145093 |
| 423 | 2939 | 0.3240731004 | 0.0249927500 |
| 424 | 2953 | 0.3467814414 | 0.0022844090 |
| 425 | 2957 | 0.3532563521 | 0.0041905017 |
| 426 | 2963 | 0.3629577787 | 0.0138919283 |
| 427 | 2969 | 0.3726461174 | 0.0235802670 |
| 428 | 2971 | 0.3758726628 | 0.0268068124 |
| 429 | 2999 | 0.4208930255 | 0.0718271751 |
| 430 | 3001 | 0.4240980246 | 0.0750321742 |
| 431 | 3011 | 0.4401016969 | 0.0910358465 |
| 432 | 3019 | 0.4528791412 | 0.1038132908 |
| 433 | 3023 | 0.4592593999 | 0.1101935495 |
| 434 | 3037 | 0.4815460840 | 0.1324802336 |
| 435 | 3041 | 0.4879011242 | 0.1388352738 |
| 436 | 3049 | 0.5005945059 | 0.1515286555 |
| 437 | 3061 | 0.5195930138 | 0.1705271634 |
| 438 | 3067 | 0.5290736518 | 0.1800078014 |
| 439 | 3079 | 0.5479978981 | 0.1989320477 |
| 440 | 3083 | 0.5542950519 | 0.2052292015 |
| 441 | 3089 | 0.5637305781 | 0.2146647277 |
| 442 | 3109 | 0.5950943674 | 0.2460285170 |
| 443 | 3119 | 0.6107258395 | 0.2616599891 |
| 444 | 3121 | 0.6138481232 | 0.2647822728 |
| 445 | 3137 | 0.6387785020 | 0.2897126516 |
| 446 | 3163 | 0.6791101926 | 0.3300443422 |
| 447 | 3167 | 0.6852954289 | 0.3362295785 |
| 448 | 3169 | 0.6883860941 | 0.3393202437 |
| 449 | 3181 | 0.7069028311 | 0.3578369807 |
| 450 | 3187 | 0.7161437402 | 0.3670778898 |
| 451 | 3191 | 0.7222979045 | 0.3732320541 |
| 452 | 3203 | 0.7407295956 | 0.3916637452 |
| 453 | 3209 | 0.7499281812 | 0.4008623308 |
| 454 | 3217 | 0.7621751433 | 0.4131092929 |
| 455 | 3221 | 0.7682910115 | 0.4192251611 |
| 456 | 3229 | 0.7805075746 | 0.4314417242 |
| 457 | 3251 | 0.8139994150 | 0.4649335646 |
| 458 | 3253 | 0.8170366266 | 0.4679707763 |
| 459 | 3257 | 0.8231073173 | 0.4740414669 |
| 460 | 3259 | 0.8261407989 | 0.4770749485 |
| 461 | 3271 | 0.8443156756 | 0.4952498252 |
| 462 | 3299 | 0.8865515336 | 0.5374856832 |
| 463 | 3301 | 0.8895592217 | 0.5404933713 |
| 464 | 3307 | 0.8985750030 | 0.5495091526 |
| 465 | 3313 | 0.9075798858 | 0.5585140354 |
| 466 | 3319 | 0.9165739030 | 0.5675080526 |
| 467 | 3323 | 0.9225638942 | 0.5734980438 |
| 468 | 3329 | 0.9315398746 | 0.5824740242 |
| 469 | 3331 | 0.9345294712 | 0.5854636208 |
| 470 | 3343 | 0.9524419675 | 0.6033761171 |
| 471 | 3347 | 0.9584032726 | 0.6093374222 |
| 472 | 3359 | 0.9762587396 | 0.6271928892 |
| 473 | 3361 | 0.9792305144 | 0.6301646640 |
| 474 | 3371 | 0.9940717314 | 0.6450058810 |
| 475 | 3373 | 0.9970364516 | 0.6479706012 |
| 476 | 3389 | 0.0207121281 | 0.3283537223 |
| 477 | 3391 | 0.0236663443 | 0.3253995061 |
| 478 | 3407 | 0.0472583609 | 0.3018074895 |
| 479 | 3413 | 0.0560863232 | 0.2929795272 |
| 480 | 3433 | 0.0854383545 | 0.2636274959 |
| 481 | 3449 | 0.1088380055 | 0.2402278449 |
| 482 | 3457 | 0.1205107001 | 0.2285551503 |
| 483 | 3461 | 0.1263402951 | 0.2227255553 |
| 484 | 3463 | 0.1292534084 | 0.2198124420 |
| 485 | 3467 | 0.1350762718 | 0.2139895786 |
| 486 | 3469 | 0.1379860241 | 0.2110798263 |
| 487 | 3491 | 0.1699197359 | 0.1791461145 |
| 488 | 3499 | 0.1814987269 | 0.1675671235 |
| 489 | 3511 | 0.1988341673 | 0.1502316831 |
| 490 | 3517 | 0.2074870779 | 0.1415787725 |
| 491 | 3527 | 0.2218867523 | 0.1271790981 |
| 492 | 3529 | 0.2247634200 | 0.1243024304 |
| 493 | 3533 | 0.2305134964 | 0.1185523540 |
| 494 | 3539 | 0.2391304790 | 0.1099353714 |
| 495 | 3541 | 0.2420006421 | 0.1070652083 |
| 496 | 3547 | 0.2506046522 | 0.0984611982 |
| 497 | 3557 | 0.2649231327 | 0.0841427177 |
| 498 | 3559 | 0.2677836075 | 0.0812822429 |
| 499 | 3571 | 0.2849239908 | 0.0641418596 |
| 500 | 3581 | 0.2991783346 | 0.0498875158 |
| 501 | 3583 | 0.3020260179 | 0.0470398325 |
| 502 | 3593 | 0.3162485616 | 0.0328172888 |
| 503 | 3607 | 0.3361158571 | 0.0129499933 |
| 504 | 3613 | 0.3446146762 | 0.0044511742 |
| 505 | 3617 | 0.3502753295 | 0.0012094791 |
| 506 | 3623 | 0.3587584898 | 0.0096926394 |
| 507 | 3631 | 0.3700548134 | 0.0209889630 |
| 508 | 3637 | 0.3785161720 | 0.0294503216 |
| 509 | 3643 | 0.3869682299 | 0.0379023795 |
| 510 | 3659 | 0.4094617742 | 0.0603959238 |
| 511 | 3671 | 0.4262889366 | 0.0772230862 |
| 512 | 3673 | 0.4290898970 | 0.0800240466 |
| 513 | 3677 | 0.4346887689 | 0.0856229185 |
| 514 | 3691 | 0.4542529042 | 0.1051870538 |
| 515 | 3697 | 0.4626223902 | 0.1135565398 |
| 516 | 3701 | 0.4681970179 | 0.1191311676 |
| 517 | 3709 | 0.4793342350 | 0.1302683846 |
| 518 | 3719 | 0.4932332586 | 0.1441674082 |
| 519 | 3727 | 0.5043345491 | 0.1552686987 |
| 520 | 3733 | 0.5126500962 | 0.1635842458 |
| 521 | 3739 | 0.5209567377 | 0.1718908873 |
| 522 | 3761 | 0.5513386151 | 0.2022727647 |
| 523 | 3767 | 0.5596040105 | 0.2105381601 |
| 524 | 3769 | 0.5623571919 | 0.2132913415 |
| 525 | 3779 | 0.5761085087 | 0.2270426583 |
| 526 | 3793 | 0.5953196566 | 0.2462538062 |
| 527 | 3797 | 0.6007998713 | 0.2517340209 |
| 528 | 3803 | 0.6090129815 | 0.2599471311 |
| 529 | 3821 | 0.6336005984 | 0.2845347480 |
| 530 | 3823 | 0.6363277856 | 0.2872619352 |
| 531 | 3833 | 0.6499494737 | 0.3008836233 |
| 532 | 3847 | 0.6689800920 | 0.3199142416 |
| 533 | 3851 | 0.6744089291 | 0.3253430787 |
| 534 | 3853 | 0.6771219381 | 0.3280560877 |
| 535 | 3863 | 0.6906729189 | 0.3416070685 |
| 536 | 3877 | 0.7096050601 | 0.3605392097 |
| 537 | 3881 | 0.7150058702 | 0.3659400198 |
| 538 | 3889 | 0.7257963677 | 0.3767305173 |
| 539 | 3907 | 0.7500209960 | 0.4009551456 |
| 540 | 3911 | 0.7553941379 | 0.4063282875 |
| 541 | 3917 | 0.7634469858 | 0.4143811354 |
| 542 | 3919 | 0.7661294409 | 0.4170635905 |
| 543 | 3923 | 0.7714916144 | 0.4224257640 |
| 544 | 3929 | 0.7795280446 | 0.4304621942 |
| 545 | 3931 | 0.7822050365 | 0.4331391861 |
| 546 | 3943 | 0.7982479497 | 0.4491820993 |
| 547 | 3947 | 0.8035883534 | 0.4545225030 |
| 548 | 3967 | 0.8302363903 | 0.4811705399 |
| 549 | 3989 | 0.8594459844 | 0.5103801340 |
| 550 | 4001 | 0.8753332437 | 0.5262673933 |
| 551 | 4003 | 0.8779780306 | 0.5289121802 |
| 552 | 4007 | 0.8832649628 | 0.5341991124 |
| 553 | 4013 | 0.8911887681 | 0.5421229177 |
| 554 | 4019 | 0.8991046791 | 0.5500388287 |
| 555 | 4021 | 0.9017415652 | 0.5526757148 |
| 556 | 4027 | 0.9096469812 | 0.5605811308 |
| 557 | 4049 | 0.9385665056 | 0.5895006552 |
| 558 | 4051 | 0.9411903539 | 0.5921245035 |
| 559 | 4057 | 0.9490567210 | 0.5999908706 |
| 560 | 4073 | 0.9699958530 | 0.6209300026 |
| 561 | 4079 | 0.9778338890 | 0.6287680386 |
| 562 | 4091 | 0.9934869324 | 0.6444210820 |
| 563 | 4093 | 0.9960927959 | 0.6470269455 |
| 564 | 4099 | 0.0039052967 | 0.3451605537 |
| 565 | 4111 | 0.0195074565 | 0.3295583939 |
| 566 | 4127 | 0.0402631781 | 0.3088026723 |
| 567 | 4129 | 0.0428538691 | 0.3062119813 |
| 568 | 4133 | 0.0480327425 | 0.3010331079 |
| 569 | 4139 | 0.0557947910 | 0.2932710594 |
| 570 | 4153 | 0.0738771108 | 0.2751887396 |
| 571 | 4157 | 0.0790360222 | 0.2700298282 |
| 572 | 4159 | 0.0816142369 | 0.2674516135 |
| 573 | 4177 | 0.1047810602 | 0.2442847902 |
| 574 | 4201 | 0.1355668576 | 0.2134989928 |
| 575 | 4211 | 0.1483596694 | 0.2007061810 |
| 576 | 4217 | 0.1560256377 | 0.1930402127 |
| 577 | 4219 | 0.1585793444 | 0.1904865060 |
| 578 | 4229 | 0.1713357872 | 0.1777300632 |
| 579 | 4231 | 0.1738846620 | 0.1751811884 |
| 580 | 4241 | 0.1866170019 | 0.1624488485 |
| 581 | 4243 | 0.1891610675 | 0.1599047829 |
| 582 | 4253 | 0.2018694180 | 0.1471964324 |
| 583 | 4259 | 0.2094848689 | 0.1395809815 |
| 584 | 4261 | 0.2120217630 | 0.1370440874 |
| 585 | 4271 | 0.2246943405 | 0.1243715099 |
| 586 | 4273 | 0.2272264817 | 0.1218393687 |
| 587 | 4283 | 0.2398753499 | 0.1091905005 |
| 588 | 4289 | 0.2474552228 | 0.1016106276 |
| 589 | 4297 | 0.2575507316 | 0.0915151188 |
| 590 | 4327 | 0.2952976763 | 0.0537681741 |
| 591 | 4337 | 0.3078412096 | 0.0412246408 |
| 592 | 4339 | 0.3103476019 | 0.0387182485 |
| 593 | 4349 | 0.3228680241 | 0.0261978263 |
| 594 | 4357 | 0.3328705501 | 0.0161953003 |
| 595 | 4363 | 0.3403644124 | 0.0087014380 |
| 596 | 4373 | 0.3528389301 | 0.0037730797 |
| 597 | 4391 | 0.3752452229 | 0.0261793725 |
| 598 | 4397 | 0.3827003777 | 0.0336345273 |
| 599 | 4409 | 0.3975903658 | 0.0485245154 |
| 600 | 4421 | 0.4124533609 | 0.0633875105 |
| 601 | 4423 | 0.4149279110 | 0.0658620606 |
| 602 | 4441 | 0.4371653659 | 0.0880995155 |
| 603 | 4447 | 0.4445644961 | 0.0954986457 |
| 604 | 4451 | 0.4494935528 | 0.1004277024 |
| 605 | 4457 | 0.4568816039 | 0.1078157535 |
| 606 | 4463 | 0.4642630274 | 0.1151971770 |
| 607 | 4481 | 0.4863676810 | 0.1373018306 |
| 608 | 4483 | 0.4888200972 | 0.1397542468 |
| 609 | 4493 | 0.5010712497 | 0.1520053993 |
| 610 | 4507 | 0.5181923616 | 0.1691265112 |
| 611 | 4513 | 0.5255191279 | 0.1764532775 |
| 612 | 4517 | 0.5304000317 | 0.1813341813 |
| 613 | 4519 | 0.5328394031 | 0.1837735527 |
| 614 | 4523 | 0.5377159875 | 0.1886501371 |
| 615 | 4547 | 0.5669152819 | 0.2178494315 |
| 616 | 4549 | 0.5693439142 | 0.2202780638 |
| 617 | 4561 | 0.5839007799 | 0.2348349295 |
| 618 | 4567 | 0.5911696394 | 0.2421037890 |
| 619 | 4583 | 0.6105221914 | 0.2614563410 |
| 620 | 4591 | 0.6201815799 | 0.2711157295 |
| 621 | 4597 | 0.6274187598 | 0.2783529094 |
| 622 | 4603 | 0.6346496451 | 0.2855837947 |
| 623 | 4621 | 0.6563046702 | 0.3072388198 |
| 624 | 4637 | 0.6755064218 | 0.3264405714 |
| 625 | 4639 | 0.6779035334 | 0.3288376830 |
| 626 | 4643 | 0.6826956904 | 0.3336298400 |
| 627 | 4649 | 0.6898787680 | 0.3408129176 |
| 628 | 4651 | 0.6922717537 | 0.3432059033 |
| 629 | 4657 | 0.6994465974 | 0.3503807470 |
| 630 | 4663 | 0.7066152811 | 0.3575494307 |
| 631 | 4673 | 0.7185494342 | 0.3694835838 |
| 632 | 4679 | 0.7257017557 | 0.3766359053 |
| 633 | 4691 | 0.7399880764 | 0.3909222260 |
| 634 | 4703 | 0.7542500539 | 0.4051842035 |
| 635 | 4721 | 0.7755976031 | 0.4265317527 |
| 636 | 4723 | 0.7779662014 | 0.4289003510 |
| 637 | 4729 | 0.7850679869 | 0.4360021365 |
| 638 | 4733 | 0.7897991740 | 0.4407333236 |
| 639 | 4751 | 0.8110565917 | 0.4619907413 |
| 640 | 4759 | 0.8204871002 | 0.4714212498 |
| 641 | 4783 | 0.8487153673 | 0.4996495169 |
| 642 | 4787 | 0.8534108919 | 0.5043450415 |
| 643 | 4789 | 0.8557576734 | 0.5066918230 |
| 644 | 4793 | 0.8604492769 | 0.5113834265 |
| 645 | 4799 | 0.8674817904 | 0.5184159400 |
| 646 | 4801 | 0.8698246590 | 0.5207588086 |
| 647 | 4813 | 0.8838682239 | 0.5348023735 |
| 648 | 4817 | 0.8885442245 | 0.5394783741 |
| 649 | 4831 | 0.9048898703 | 0.5558240199 |
| 650 | 4861 | 0.9398102131 | 0.5907443627 |
| 651 | 4871 | 0.9514183920 | 0.6023525416 |
| 652 | 4877 | 0.9583756751 | 0.6093098247 |
| 653 | 4889 | 0.9722731414 | 0.6232072910 |
| 654 | 4903 | 0.9884581402 | 0.6393922899 |
| 655 | 4909 | 0.9953851372 | 0.6463192868 |
| 656 | 4919 | 0.0069175999 | 0.3421482504 |
| 657 | 4931 | 0.0207359425 | 0.3283299079 |
| 658 | 4933 | 0.0230368193 | 0.3260290311 |
| 659 | 4937 | 0.0276367079 | 0.3214291425 |
| 660 | 4943 | 0.0345318845 | 0.3145339659 |
| 661 | 4951 | 0.0437167791 | 0.3053490713 |
| 662 | 4957 | 0.0505989590 | 0.2984668914 |
| 663 | 4967 | 0.0620569283 | 0.2870089221 |
| 664 | 4969 | 0.0643466763 | 0.2847191741 |
| 665 | 4973 | 0.0689243297 | 0.2801415207 |
| 666 | 4987 | 0.0849268128 | 0.2641390376 |
| 667 | 4993 | 0.0917758522 | 0.2572899982 |
| 668 | 4999 | 0.0986194068 | 0.2504464436 |
| 669 | 5003 | 0.1031787349 | 0.2458871155 |
| 670 | 5009 | 0.1100131727 | 0.2390526777 |
| 671 | 5011 | 0.1122901057 | 0.2367757447 |
| 672 | 5021 | 0.1236656925 | 0.2254001579 |
| 673 | 5023 | 0.1259389969 | 0.2231268535 |
| 674 | 5039 | 0.1441037453 | 0.2049621051 |
| 675 | 5051 | 0.1577020883 | 0.1913637621 |
| 676 | 5059 | 0.1667556892 | 0.1823101612 |
| 677 | 5077 | 0.1870914503 | 0.1619744001 |
| 678 | 5081 | 0.1916039787 | 0.1574618717 |
| 679 | 5087 | 0.1983683327 | 0.1506975177 |
| 680 | 5099 | 0.2118811006 | 0.1371847498 |
| 681 | 5101 | 0.2141311668 | 0.1349346836 |
| 682 | 5107 | 0.2208778386 | 0.1281880118 |
| 683 | 5113 | 0.2276192281 | 0.1214466223 |
| 684 | 5119 | 0.2343553458 | 0.1147105046 |
| 685 | 5147 | 0.2657211576 | 0.0833446928 |
| 686 | 5153 | 0.2724275949 | 0.0766382555 |
| 687 | 5167 | 0.2880557290 | 0.0610101214 |
| 688 | 5171 | 0.2925157242 | 0.0565501262 |
| 689 | 5179 | 0.3014288194 | 0.0476370310 |
| 690 | 5189 | 0.3125572902 | 0.0365085602 |
| 691 | 5197 | 0.3214497770 | 0.0276160734 |
| 692 | 5209 | 0.3347714126 | 0.0142944378 |
| 693 | 5227 | 0.3547155583 | 0.0056497079 |
| 694 | 5231 | 0.3591413706 | 0.0100755202 |
| 695 | 5233 | 0.3613534307 | 0.0122875803 |
| 696 | 5237 | 0.3657758606 | 0.0167100102 |
| 697 | 5261 | 0.3922632623 | 0.0431974119 |
| 698 | 5273 | 0.4054767628 | 0.0564109124 |
| 699 | 5279 | 0.4120759963 | 0.0630101459 |
| 700 | 5281 | 0.4142746296 | 0.0652087792 |
| 701 | 5297 | 0.4318437438 | 0.0827778934 |
| 702 | 5303 | 0.4384230401 | 0.0893571897 |
| 703 | 5309 | 0.4449973755 | 0.0959315251 |
| 704 | 5323 | 0.4603182518 | 0.1112524014 |
| 705 | 5333 | 0.4712452953 | 0.1221794449 |
| 706 | 5347 | 0.4865202318 | 0.1374543814 |
| 707 | 5351 | 0.4908796013 | 0.1418137509 |
| 708 | 5381 | 0.5235058280 | 0.1744399776 |
| 709 | 5387 | 0.5300165126 | 0.1809506622 |
| 710 | 5393 | 0.5365223645 | 0.1874565141 |
| 711 | 5399 | 0.5430233929 | 0.1939575425 |
| 712 | 5407 | 0.5516839427 | 0.2026180923 |
| 713 | 5413 | 0.5581737506 | 0.2091079002 |
| 714 | 5417 | 0.5624976254 | 0.2134317750 |
| 715 | 5419 | 0.5646587646 | 0.2155929142 |
| 716 | 5431 | 0.5776144461 | 0.2285485957 |
| 717 | 5437 | 0.5840851312 | 0.2350192808 |
| 718 | 5441 | 0.5883962769 | 0.2393304265 |
| 719 | 5443 | 0.5905510575 | 0.2414852071 |
| 720 | 5449 | 0.5970122339 | 0.2479463835 |
| 721 | 5471 | 0.6206627156 | 0.2715968652 |
| 722 | 5477 | 0.6271018401 | 0.2780359897 |
| 723 | 5479 | 0.6292471699 | 0.2801813195 |
| 724 | 5483 | 0.6335362637 | 0.2844704133 |
| 725 | 5501 | 0.6528114143 | 0.3037455639 |
| 726 | 5503 | 0.6549505009 | 0.3058846505 |
| 727 | 5507 | 0.6592271196 | 0.3101612692 |
| 728 | 5519 | 0.6720445635 | 0.3229787131 |
| 729 | 5521 | 0.6741789973 | 0.3251131469 |
| 730 | 5527 | 0.6805792075 | 0.3315133571 |
| 731 | 5531 | 0.6848434414 | 0.3357775910 |
| 732 | 5557 | 0.7125109713 | 0.3634451209 |
| 733 | 5563 | 0.7188835248 | 0.3698176744 |
| 734 | 5569 | 0.7252514979 | 0.3761856475 |
| 735 | 5573 | 0.7294942726 | 0.3804284222 |
| 736 | 5581 | 0.7379737355 | 0.3889078851 |
| 737 | 5591 | 0.7485616767 | 0.3994958263 |
| 738 | 5623 | 0.7823584840 | 0.4332926336 |
| 739 | 5639 | 0.7992088189 | 0.4501429685 |
| 740 | 5641 | 0.8013128687 | 0.4522470183 |
| 741 | 5647 | 0.8076220356 | 0.4585561852 |
| 742 | 5651 | 0.8118256644 | 0.4627598140 |
| 743 | 5653 | 0.8139267350 | 0.4648608846 |
| 744 | 5657 | 0.8181273899 | 0.4690615395 |
| 745 | 5659 | 0.8202269749 | 0.4711611245 |
| 746 | 5669 | 0.8307174859 | 0.4816516355 |
| 747 | 5683 | 0.8453834960 | 0.4963176456 |
| 748 | 5689 | 0.8516615558 | 0.5025957054 |
| 749 | 5693 | 0.8558444770 | 0.5067786266 |
| 750 | 5701 | 0.8642044452 | 0.5151385948 |
| 751 | 5711 | 0.8746434147 | 0.5255775643 |
| 752 | 5717 | 0.8809009484 | 0.5318350980 |
| 753 | 5737 | 0.9017278276 | 0.5526619772 |
| 754 | 5741 | 0.9058873927 | 0.5568215423 |
| 755 | 5743 | 0.9079664508 | 0.5589006004 |
| 756 | 5749 | 0.9142007303 | 0.5651348799 |
| 757 | 5779 | 0.9453072361 | 0.5962413857 |
| 758 | 5783 | 0.9494466301 | 0.6003807797 |
| 759 | 5791 | 0.9577196953 | 0.6086538449 |
| 760 | 5801 | 0.9680503193 | 0.6189844689 |
| 761 | 5807 | 0.9742429961 | 0.6251771457 |
| 762 | 5813 | 0.9804314087 | 0.6313655583 |
| 763 | 5821 | 0.9886760050 | 0.6396101546 |
| 764 | 5827 | 0.9948544963 | 0.6457886459 |
| 765 | 5839 | 0.0071987667 | 0.3418670837 |
| 766 | 5843 | 0.0113097648 | 0.3377560856 |
| 767 | 5849 | 0.0174727455 | 0.3315931049 |
| 768 | 5851 | 0.0195261358 | 0.3295397146 |
| 769 | 5857 | 0.0256835004 | 0.3233823500 |
| 770 | 5861 | 0.0297860743 | 0.3192797761 |
| 771 | 5867 | 0.0359364367 | 0.3131294137 |
| 772 | 5869 | 0.0379856257 | 0.3110802247 |
| 773 | 5879 | 0.0482245934 | 0.3008412570 |
| 774 | 5881 | 0.0502709934 | 0.2987948570 |
| 775 | 5897 | 0.0666255149 | 0.2824403355 |
| 776 | 5903 | 0.0727508334 | 0.2763150170 |
| 777 | 5923 | 0.0931386343 | 0.2559272161 |
| 778 | 5927 | 0.0972106850 | 0.2518551654 |
| 779 | 5939 | 0.1094158553 | 0.2396499951 |
| 780 | 5953 | 0.1236344592 | 0.2254313912 |
| 781 | 5981 | 0.1520049289 | 0.1970609215 |
| 782 | 5987 | 0.1580727900 | 0.1909930604 |
| 783 | 6007 | 0.1782697621 | 0.1707960883 |
| 784 | 6011 | 0.1823037749 | 0.1667620755 |
| 785 | 6029 | 0.2004347197 | 0.1486311307 |
| 786 | 6037 | 0.2084813346 | 0.1405845158 |
| 787 | 6043 | 0.2145116319 | 0.1345542185 |
| 788 | 6047 | 0.2185296129 | 0.1305362375 |
| 789 | 6053 | 0.2245532634 | 0.1245125870 |
| 790 | 6067 | 0.2385929842 | 0.1104728662 |
| 791 | 6073 | 0.2446033959 | 0.1044624545 |
| 792 | 6079 | 0.2506098501 | 0.0984560003 |
| 793 | 6089 | 0.2606118305 | 0.0884540199 |
| 794 | 6091 | 0.2626109122 | 0.0864549382 |
| 795 | 6101 | 0.2725997622 | 0.0764660882 |
| 796 | 6113 | 0.2845719850 | 0.0644938654 |
| 797 | 6121 | 0.2925447650 | 0.0565210854 |
| 798 | 6131 | 0.3025009770 | 0.0465648734 |
| 799 | 6133 | 0.3044909201 | 0.0445749303 |
| 800 | 6143 | 0.3144341514 | 0.0346316990 |
| 801 | 6151 | 0.3223809698 | 0.0266848806 |
| 802 | 6163 | 0.3342882882 | 0.0147775622 |
| 803 | 6173 | 0.3441992519 | 0.0048665985 |
| 804 | 6197 | 0.3679419728 | 0.0188761224 |
| 805 | 6199 | 0.3699177639 | 0.0208519135 |
| 806 | 6203 | 0.3738680716 | 0.0248022212 |
| 807 | 6211 | 0.3817635952 | 0.0326977448 |
| 808 | 6217 | 0.3876807898 | 0.0386149394 |
| 809 | 6221 | 0.3916234714 | 0.0425576210 |
| 810 | 6229 | 0.3995037673 | 0.0504379169 |
| 811 | 6247 | 0.4172097963 | 0.0681439459 |
| 812 | 6257 | 0.4270317862 | 0.0779659358 |
| 813 | 6263 | 0.4329199578 | 0.0838541074 |
| 814 | 6269 | 0.4388043700 | 0.0897385196 |
| 815 | 6271 | 0.4407650064 | 0.0916991560 |
| 816 | 6277 | 0.4466444154 | 0.0975785650 |
| 817 | 6287 | 0.4564351101 | 0.1073692597 |
| 818 | 6299 | 0.4681702492 | 0.1191043988 |
| 819 | 6301 | 0.4701246564 | 0.1210588060 |
| 820 | 6311 | 0.4798904937 | 0.1308246433 |
| 821 | 6317 | 0.4857450451 | 0.1366791947 |
| 822 | 6323 | 0.4915958906 | 0.1425300402 |
| 823 | 6329 | 0.4974430359 | 0.1483771855 |
| 824 | 6337 | 0.5052334840 | 0.1561676337 |
| 825 | 6343 | 0.5110720184 | 0.1620061680 |
| 826 | 6353 | 0.5207947326 | 0.1717288822 |
| 827 | 6359 | 0.5266234646 | 0.1775576142 |
| 828 | 6361 | 0.5285655604 | 0.1794997100 |
| 829 | 6367 | 0.5343894067 | 0.1853235563 |
| 830 | 6373 | 0.5402095953 | 0.1911437449 |
| 831 | 6379 | 0.5460261320 | 0.1969602816 |
| 832 | 6389 | 0.5557122601 | 0.2066464097 |
| 833 | 6397 | 0.5634538880 | 0.2143880376 |
| 834 | 6421 | 0.5866401153 | 0.2375742649 |
| 835 | 6427 | 0.5924276418 | 0.2433617914 |
| 836 | 6449 | 0.6136178071 | 0.2645519567 |
| 837 | 6451 | 0.6155417947 | 0.2664759443 |
| 838 | 6469 | 0.6328398147 | 0.2837739643 |
| 839 | 6473 | 0.6366794603 | 0.2876136099 |
| 840 | 6481 | 0.6443540088 | 0.2952881584 |
| 841 | 6491 | 0.6539383183 | 0.3048724679 |
| 842 | 6521 | 0.6826323157 | 0.3335664653 |
| 843 | 6529 | 0.6902691802 | 0.3412033298 |
| 844 | 6547 | 0.7074293452 | 0.3583634948 |
| 845 | 6551 | 0.7112384426 | 0.3621725922 |
| 846 | 6553 | 0.7131424099 | 0.3640765595 |
| 847 | 6563 | 0.7226564399 | 0.3735905895 |
| 848 | 6569 | 0.7283602199 | 0.3792943695 |
| 849 | 6571 | 0.7302607080 | 0.3811948576 |
| 850 | 6577 | 0.7359598596 | 0.3868940092 |
| 851 | 6581 | 0.7397573687 | 0.3906915183 |
| 852 | 6599 | 0.7568271435 | 0.4077612931 |
| 853 | 6607 | 0.7644037470 | 0.4153378966 |
| 854 | 6619 | 0.7757571933 | 0.4266913429 |
| 855 | 6637 | 0.7927616619 | 0.4436958115 |
| 856 | 6653 | 0.8078509536 | 0.4587851032 |
| 857 | 6659 | 0.8135032007 | 0.4644373503 |
| 858 | 6661 | 0.8153865285 | 0.4663206781 |
| 859 | 6673 | 0.8266785862 | 0.4776127358 |
| 860 | 6679 | 0.8323195389 | 0.4832536885 |
| 861 | 6689 | 0.8417136241 | 0.4926477737 |
| 862 | 6691 | 0.8435913175 | 0.4945254671 |
| 863 | 6701 | 0.8529741758 | 0.5039083254 |
| 864 | 6703 | 0.8548496271 | 0.5057837767 |
| 865 | 6709 | 0.8604737437 | 0.5114078933 |
| 866 | 6719 | 0.8698398244 | 0.5207739740 |
| 867 | 6733 | 0.8829367379 | 0.5338708875 |
| 868 | 6737 | 0.8866753782 | 0.5376095278 |
| 869 | 6761 | 0.9090762002 | 0.5600103498 |
| 870 | 6763 | 0.9109405410 | 0.5618746906 |
| 871 | 6779 | 0.9258420517 | 0.5767762013 |
| 872 | 6781 | 0.9277030913 | 0.5786372409 |
| 873 | 6791 | 0.9370028044 | 0.5879369540 |
| 874 | 6793 | 0.9388616513 | 0.5897958009 |
| 875 | 6803 | 0.9481504172 | 0.5990845668 |
| 876 | 6823 | 0.9667006766 | 0.6176348262 |
| 877 | 6827 | 0.9704063770 | 0.6213405266 |
| 878 | 6829 | 0.9722586844 | 0.6231928340 |
| 879 | 6833 | 0.9759622146 | 0.6268963642 |
| 880 | 6841 | 0.9833649412 | 0.6342990908 |
| 881 | 6857 | 0.9981530984 | 0.6490872480 |
| 882 | 6863 | 0.0036927264 | 0.3453731240 |
| 883 | 6869 | 0.0092291266 | 0.3398367238 |
| 884 | 6871 | 0.0110738769 | 0.3379919735 |
| 885 | 6883 | 0.0221348678 | 0.3269309826 |
| 886 | 6899 | 0.0368628756 | 0.3122029748 |
| 887 | 6907 | 0.0442183413 | 0.3048475091 |
| 888 | 6911 | 0.0478939444 | 0.3011719060 |
| 889 | 6917 | 0.0534046909 | 0.2956611595 |
| 890 | 6947 | 0.0809107269 | 0.2681551235 |
| 891 | 6949 | 0.0827416448 | 0.2663242056 |
| 892 | 6959 | 0.0918909685 | 0.2571748819 |
| 893 | 6961 | 0.0937197813 | 0.2553460691 |
| 894 | 6967 | 0.0992041188 | 0.2498617316 |
| 895 | 6971 | 0.1028585947 | 0.2462072557 |
| 896 | 6977 | 0.1083376882 | 0.2407281622 |
| 897 | 6983 | 0.1138136414 | 0.2352522090 |
| 898 | 6991 | 0.1211100352 | 0.2279558152 |
| 899 | 6997 | 0.1265786784 | 0.2224871720 |
| 900 | 7001 | 0.1302227040 | 0.2188431464 |
| 901 | 7013 | 0.1411464595 | 0.2079193909 |
| 902 | 7019 | 0.1466036648 | 0.2024621856 |
| 903 | 7027 | 0.1538751029 | 0.1951907475 |
| 904 | 7039 | 0.1647719194 | 0.1842939310 |
| 905 | 7043 | 0.1684014393 | 0.1806644111 |
| 906 | 7057 | 0.1810939474 | 0.1679719030 |
| 907 | 7069 | 0.1919598859 | 0.1571059645 |
| 908 | 7079 | 0.2010054450 | 0.1480604054 |
| 909 | 7103 | 0.2226800851 | 0.1263857653 |
| 910 | 7109 | 0.2280911142 | 0.1209747362 |
| 911 | 7121 | 0.2389040456 | 0.1101618048 |
| 912 | 7127 | 0.2443059563 | 0.1047598941 |
| 913 | 7129 | 0.2461059195 | 0.1029599309 |
| 914 | 7151 | 0.2658833321 | 0.0831825182 |
| 915 | 7159 | 0.2730650609 | 0.0760007895 |
| 916 | 7177 | 0.2892044111 | 0.0598614393 |
| 917 | 7187 | 0.2981590591 | 0.0509067913 |
| 918 | 7193 | 0.3035278615 | 0.0455379889 |
| 919 | 7207 | 0.3160434668 | 0.0330223836 |
| 920 | 7211 | 0.3196163766 | 0.0294494738 |
| 921 | 7213 | 0.3214023361 | 0.0276635143 |
| 922 | 7219 | 0.3267582345 | 0.0223076159 |
| 923 | 7229 | 0.3356781408 | 0.0133877096 |
| 924 | 7237 | 0.3428081449 | 0.0062577055 |
| 925 | 7243 | 0.3481522004 | 0.0009136500 |
| 926 | 7247 | 0.3517132647 | 0.0026474143 |
| 927 | 7253 | 0.3570524051 | 0.0079865547 |
| 928 | 7283 | 0.3837040323 | 0.0346381819 |
| 929 | 7297 | 0.3961164154 | 0.0470505650 |
| 930 | 7307 | 0.4049726864 | 0.0559068360 |
| 931 | 7309 | 0.4067429708 | 0.0576771204 |
| 932 | 7321 | 0.4173579014 | 0.0682920510 |
| 933 | 7331 | 0.4261948197 | 0.0771289693 |
| 934 | 7333 | 0.4279612389 | 0.0788953885 |
| 935 | 7349 | 0.4420810431 | 0.0930151927 |
| 936 | 7351 | 0.4438445771 | 0.0947787267 |
| 937 | 7369 | 0.4597020080 | 0.1106361576 |
| 938 | 7393 | 0.4808051310 | 0.1317392806 |
| 939 | 7411 | 0.4966025201 | 0.1475366697 |
| 940 | 7417 | 0.5018626316 | 0.1527967812 |
| 941 | 7433 | 0.5158757411 | 0.1668098907 |
| 942 | 7451 | 0.5316164731 | 0.1825506227 |
| 943 | 7457 | 0.5368577498 | 0.1877918994 |
| 944 | 7459 | 0.5386042172 | 0.1895383668 |
| 945 | 7477 | 0.5543083935 | 0.2052425431 |
| 946 | 7481 | 0.5577947868 | 0.2087289364 |
| 947 | 7487 | 0.5630220475 | 0.2139561971 |
| 948 | 7489 | 0.5647638471 | 0.2156979967 |
| 949 | 7499 | 0.5734681966 | 0.2244023462 |
| 950 | 7507 | 0.5804261063 | 0.2313602559 |
| 951 | 7517 | 0.5891165456 | 0.2400506952 |
| 952 | 7523 | 0.5943271101 | 0.2452612597 |
| 953 | 7529 | 0.5995349050 | 0.2504690546 |
| 954 | 7537 | 0.6064743293 | 0.2574084789 |
| 955 | 7541 | 0.6099422001 | 0.2608763497 |
| 956 | 7547 | 0.6151417078 | 0.2660758574 |
| 957 | 7549 | 0.6168742646 | 0.2678084142 |
| 958 | 7559 | 0.6255324615 | 0.2764666111 |
| 959 | 7561 | 0.6272631844 | 0.2781973340 |
| 960 | 7573 | 0.6376411180 | 0.2885752676 |
| 961 | 7577 | 0.6410979928 | 0.2920321424 |
| 962 | 7583 | 0.6462810246 | 0.2972151742 |
| 963 | 7589 | 0.6514613230 | 0.3023954726 |
| 964 | 7591 | 0.6531874824 | 0.3041216320 |
| 965 | 7603 | 0.6635380768 | 0.3144722264 |
| 966 | 7607 | 0.6669858546 | 0.3179200042 |
| 967 | 7621 | 0.6790435673 | 0.3299777169 |
| 968 | 7639 | 0.6945246621 | 0.3454588117 |
| 969 | 7643 | 0.6979616021 | 0.3488957517 |
| 970 | 7649 | 0.7031147643 | 0.3540489139 |
| 971 | 7669 | 0.7202725339 | 0.3712066835 |
| 972 | 7673 | 0.7237005071 | 0.3746346567 |
| 973 | 7681 | 0.7305528811 | 0.3814870307 |
| 974 | 7687 | 0.7356890398 | 0.3866231895 |
| 975 | 7691 | 0.7391116610 | 0.3900458106 |
| 976 | 7699 | 0.7459533449 | 0.3968874945 |
| 977 | 7703 | 0.7493724097 | 0.4003065593 |
| 978 | 7717 | 0.7613298236 | 0.4122639732 |
| 979 | 7723 | 0.7664500025 | 0.4173841521 |
| 980 | 7727 | 0.7698619821 | 0.4207961317 |
| 981 | 7741 | 0.7817946458 | 0.4327287954 |
| 982 | 7753 | 0.7920111974 | 0.4429453471 |
| 983 | 7757 | 0.7954143719 | 0.4463485215 |
| 984 | 7759 | 0.7971155204 | 0.4480496700 |
| 985 | 7789 | 0.8225977412 | 0.4735318908 |
| 986 | 7793 | 0.8259904241 | 0.4769245737 |
| 987 | 7817 | 0.8463221809 | 0.4972563305 |
| 988 | 7823 | 0.8513986160 | 0.5023327656 |
| 989 | 7829 | 0.8564724561 | 0.5074066057 |
| 990 | 7841 | 0.8666123647 | 0.5175465143 |
| 991 | 7853 | 0.8767419329 | 0.5276760826 |
| 992 | 7867 | 0.8885467288 | 0.5394808784 |
| 993 | 7873 | 0.8936016399 | 0.5445357895 |
| 994 | 7877 | 0.8969701539 | 0.5479043035 |
| 995 | 7879 | 0.8986539834 | 0.5495881330 |
| 996 | 7883 | 0.9020207875 | 0.5529549371 |
| 997 | 7901 | 0.9171573284 | 0.5680914780 |
| 998 | 7907 | 0.9221977328 | 0.5731318824 |
| 999 | 7919 | 0.9322708973 | 0.5832050469 |
| 1000 | 7927 | 0.9389806882 | 0.5899148378 |
| 1001 | 7933 | 0.9440100693 | 0.5949442189 |
| 1002 | 7937 | 0.9473615814 | 0.5982957310 |
| 1003 | 7949 | 0.9574093663 | 0.6083435159 |
| 1004 | 7951 | 0.9590830138 | 0.6100171634 |
| 1005 | 7963 | 0.9691190094 | 0.6200531590 |
| 1006 | 7993 | 0.9941649645 | 0.6450991141 |
| 1007 | 8009 | 0.0074971893 | 0.3415686611 |
| 1008 | 8011 | 0.0091624685 | 0.3399033819 |
| 1009 | 8017 | 0.0141566438 | 0.3349092066 |
| 1010 | 8039 | 0.0324473301 | 0.3166185203 |
| 1011 | 8053 | 0.0440694893 | 0.3049963611 |
| 1012 | 8059 | 0.0490462914 | 0.3000195590 |
| 1013 | 8069 | 0.0573354751 | 0.2917303753 |
| 1014 | 8081 | 0.0672734604 | 0.2817923900 |
| 1015 | 8087 | 0.0722387639 | 0.2768270865 |
| 1016 | 8089 | 0.0738933193 | 0.2751725311 |
| 1017 | 8093 | 0.0772016121 | 0.2718642383 |
| 1018 | 8101 | 0.0838149289 | 0.2652509215 |
| 1019 | 8111 | 0.0920754550 | 0.2569903954 |
| 1020 | 8117 | 0.0970285122 | 0.2520373382 |
| 1021 | 8123 | 0.1019791291 | 0.2470867213 |
| 1022 | 8147 | 0.1217572544 | 0.2273085960 |
| 1023 | 8161 | 0.1332765618 | 0.2157892886 |

---


## Appendix O. Full scan: first 1024 primes, square-root fractional parts

Target $H=\pi/9\approx 0.3490658504$.

| i | p | frac(√p) | |frac(√p)−H| |
|---:|---:|---:|---:|
| 0 | 2 | 0.4142135624 | 0.0651477120 |
| 1 | 3 | 0.7320508076 | 0.3829849572 |
| 2 | 5 | 0.2360679775 | 0.1129978729 |
| 3 | 7 | 0.6457513111 | 0.2966854607 |
| 4 | 11 | 0.3166247904 | 0.0324410600 |
| 5 | 13 | 0.6055512755 | 0.2564854251 |
| 6 | 17 | 0.1231056256 | 0.2259602248 |
| 7 | 19 | 0.3588989435 | 0.0098330931 |
| 8 | 23 | 0.7958315233 | 0.4467656729 |
| 9 | 29 | 0.3851648071 | 0.0360989567 |
| 10 | 31 | 0.5677643628 | 0.2186985124 |
| 11 | 37 | 0.0827625303 | 0.2663033201 |
| 12 | 41 | 0.4031242374 | 0.0540583870 |
| 13 | 43 | 0.5574385243 | 0.2083726739 |
| 14 | 47 | 0.8556546004 | 0.5065887500 |
| 15 | 53 | 0.2801098893 | 0.0689559611 |
| 16 | 59 | 0.6811457479 | 0.3320798975 |
| 17 | 61 | 0.8102496759 | 0.4611838255 |
| 18 | 67 | 0.1853527719 | 0.1637130785 |
| 19 | 71 | 0.4261497732 | 0.0770839228 |
| 20 | 73 | 0.5440037453 | 0.1949378949 |
| 21 | 79 | 0.8881944173 | 0.5391285669 |
| 22 | 83 | 0.1104335791 | 0.2386322713 |
| 23 | 89 | 0.4339811321 | 0.0849152817 |
| 24 | 97 | 0.8488578018 | 0.4997919514 |
| 25 | 101 | 0.0498756211 | 0.2991902293 |
| 26 | 103 | 0.1488915651 | 0.2001742853 |
| 27 | 107 | 0.3440804328 | 0.0049854176 |
| 28 | 109 | 0.4403065089 | 0.0912406585 |
| 29 | 113 | 0.6301458127 | 0.2810799623 |
| 30 | 127 | 0.2694276696 | 0.0796381808 |
| 31 | 131 | 0.4455231423 | 0.0964572919 |
| 32 | 137 | 0.7046999107 | 0.3556340603 |
| 33 | 139 | 0.7898261226 | 0.4407602722 |
| 34 | 149 | 0.2065556157 | 0.1425102347 |
| 35 | 151 | 0.2882057274 | 0.0608601230 |
| 36 | 157 | 0.5299640861 | 0.1808982357 |
| 37 | 163 | 0.7671453348 | 0.4180794844 |
| 38 | 167 | 0.9228479833 | 0.5737821329 |
| 39 | 173 | 0.1529464380 | 0.1961194124 |
| 40 | 179 | 0.3790881603 | 0.0300223099 |
| 41 | 181 | 0.4536240471 | 0.1045581967 |
| 42 | 191 | 0.8202749611 | 0.4712091107 |
| 43 | 193 | 0.8924439894 | 0.5433781391 |
| 44 | 197 | 0.0356688476 | 0.3133970028 |
| 45 | 199 | 0.1067359797 | 0.2423298707 |
| 46 | 211 | 0.5258390463 | 0.1767731959 |
| 47 | 223 | 0.9331845231 | 0.5841186727 |
| 48 | 227 | 0.0665191733 | 0.2825466771 |
| 49 | 229 | 0.1327459504 | 0.2163199000 |
| 50 | 233 | 0.2643375225 | 0.0847283279 |
| 51 | 239 | 0.4596248337 | 0.1105589833 |
| 52 | 241 | 0.5241746963 | 0.1751088459 |
| 53 | 251 | 0.8429795178 | 0.4939136674 |
| 54 | 257 | 0.0312195419 | 0.3178463085 |
| 55 | 263 | 0.2172747402 | 0.1317911102 |
| 56 | 269 | 0.4012194669 | 0.0521536165 |
| 57 | 271 | 0.4620776332 | 0.1130117828 |
| 58 | 277 | 0.6433169771 | 0.2942511267 |
| 59 | 281 | 0.7630546142 | 0.4139887638 |
| 60 | 283 | 0.8226038413 | 0.4735379909 |
| 61 | 293 | 0.1172427686 | 0.2318230818 |
| 62 | 307 | 0.5214154679 | 0.1723496175 |
| 63 | 311 | 0.6351920885 | 0.2861262381 |
| 64 | 313 | 0.6918060130 | 0.3427401626 |
| 65 | 317 | 0.8044938148 | 0.4554279644 |
| 66 | 331 | 0.1934053987 | 0.1556604517 |
| 67 | 337 | 0.3575597507 | 0.0084939003 |
| 68 | 347 | 0.6279360102 | 0.2788701598 |
| 69 | 349 | 0.6815416923 | 0.3324758419 |
| 70 | 353 | 0.7882942281 | 0.4392283777 |
| 71 | 359 | 0.9472953215 | 0.5982294711 |
| 72 | 367 | 0.1572440607 | 0.1918217897 |
| 73 | 373 | 0.3132079158 | 0.0358579346 |
| 74 | 379 | 0.4679223339 | 0.1188564835 |
| 75 | 383 | 0.5703857908 | 0.2213199404 |
| 76 | 389 | 0.7230829233 | 0.3740170729 |
| 77 | 397 | 0.9248588452 | 0.5757929948 |
| 78 | 401 | 0.0249843945 | 0.3240814559 |
| 79 | 409 | 0.2237484162 | 0.1253174342 |
| 80 | 419 | 0.4694894905 | 0.1204236401 |
| 81 | 421 | 0.5182845287 | 0.1692186783 |
| 82 | 431 | 0.7605394920 | 0.4114736416 |
| 83 | 433 | 0.8086520467 | 0.4595861963 |
| 84 | 439 | 0.9523268398 | 0.6032609894 |
| 85 | 443 | 0.0475651798 | 0.3015006705 |
| 86 | 449 | 0.1896201004 | 0.1594457500 |
| 87 | 457 | 0.3775583264 | 0.0284924760 |
| 88 | 461 | 0.4709105536 | 0.1218447032 |
| 89 | 463 | 0.5174347914 | 0.1683689410 |
| 90 | 467 | 0.6101827850 | 0.2611169346 |
| 91 | 479 | 0.8860686282 | 0.5370027778 |
| 92 | 487 | 0.0680764907 | 0.2809893597 |
| 93 | 491 | 0.1585198062 | 0.1905460442 |
| 94 | 499 | 0.3383079037 | 0.0107579467 |
| 95 | 503 | 0.4276614920 | 0.0785956416 |
| 96 | 509 | 0.5610283454 | 0.2119624950 |
| 97 | 521 | 0.8254244210 | 0.4763585706 |
| 98 | 523 | 0.8691932521 | 0.5201274017 |
| 99 | 541 | 0.2594066992 | 0.0896591512 |
| 100 | 547 | 0.3880311271 | 0.0389652767 |
| 101 | 557 | 0.6008474424 | 0.2517815920 |
| 102 | 563 | 0.7276210354 | 0.3785551850 |
| 103 | 569 | 0.8537208838 | 0.5046550334 |
| 104 | 571 | 0.8956062907 | 0.5465404403 |
| 105 | 577 | 0.0208242989 | 0.3282415515 |
| 106 | 587 | 0.2280828792 | 0.1209829712 |
| 107 | 593 | 0.3515913238 | 0.0025254734 |
| 108 | 599 | 0.4744765010 | 0.1254106506 |
| 109 | 601 | 0.5153013443 | 0.1662354939 |
| 110 | 607 | 0.6373699895 | 0.2883041391 |
| 111 | 613 | 0.7588368063 | 0.4097709559 |
| 112 | 617 | 0.8394846967 | 0.4904188463 |
| 113 | 619 | 0.8797106092 | 0.5306447589 |
| 114 | 631 | 0.1197133742 | 0.2293524762 |
| 115 | 641 | 0.3179778023 | 0.0310880481 |
| 116 | 643 | 0.3574446662 | 0.0083788158 |
| 117 | 647 | 0.4361946840 | 0.0871288336 |
| 118 | 653 | 0.5538646784 | 0.2047988280 |
| 119 | 659 | 0.6709953060 | 0.3219294556 |
| 120 | 661 | 0.7099202644 | 0.3608544140 |
| 121 | 673 | 0.9422435421 | 0.5931776917 |
| 122 | 677 | 0.0192236625 | 0.3298421879 |
| 123 | 683 | 0.1342686907 | 0.2147971597 |
| 124 | 691 | 0.2868788562 | 0.0621869942 |
| 125 | 701 | 0.4764045897 | 0.1273387393 |
| 126 | 709 | 0.6270539114 | 0.2779880610 |
| 127 | 719 | 0.8141753556 | 0.4651095052 |
| 128 | 727 | 0.9629375254 | 0.6138716750 |
| 129 | 733 | 0.0739727414 | 0.2750931090 |
| 130 | 739 | 0.1845544381 | 0.1645114123 |
| 131 | 743 | 0.2580263409 | 0.0910395095 |
| 132 | 751 | 0.4043792121 | 0.0553133617 |
| 133 | 757 | 0.5136329844 | 0.1645671340 |
| 134 | 761 | 0.5862284483 | 0.2371625979 |
| 135 | 769 | 0.7308492477 | 0.3817833973 |
| 136 | 773 | 0.8028775489 | 0.4538116985 |
| 137 | 787 | 0.0535202782 | 0.2955455722 |
| 138 | 797 | 0.2311884270 | 0.1178774234 |
| 139 | 809 | 0.4429253067 | 0.0938594563 |
| 140 | 811 | 0.4780617318 | 0.1289958814 |
| 141 | 821 | 0.6530975638 | 0.3040317134 |
| 142 | 823 | 0.6879765756 | 0.3389107252 |
| 143 | 827 | 0.7576076891 | 0.4085418387 |
| 144 | 829 | 0.7923600978 | 0.4432942474 |
| 145 | 839 | 0.9654967159 | 0.6164308655 |
| 146 | 853 | 0.2061637330 | 0.1429021174 |
| 147 | 857 | 0.2745623366 | 0.0745035138 |
| 148 | 859 | 0.3087017795 | 0.0403640709 |
| 149 | 863 | 0.3768616431 | 0.0277957927 |
| 150 | 877 | 0.6141857899 | 0.2651199395 |
| 151 | 881 | 0.6816441593 | 0.3325783089 |
| 152 | 883 | 0.7153159162 | 0.3662500658 |
| 153 | 887 | 0.7825452237 | 0.4334793733 |
| 154 | 907 | 0.1164406928 | 0.2326251576 |
| 155 | 911 | 0.1827765456 | 0.1662893048 |
| 156 | 919 | 0.3150127824 | 0.0340530680 |
| 157 | 929 | 0.4795013083 | 0.1304354579 |
| 158 | 937 | 0.6104557300 | 0.2613898796 |
| 159 | 941 | 0.6757233004 | 0.3266574500 |
| 160 | 947 | 0.7733651069 | 0.4242992565 |
| 161 | 953 | 0.8706980809 | 0.5216322305 |
| 162 | 967 | 0.0966236109 | 0.2524422395 |
| 163 | 971 | 0.1608729018 | 0.1881929486 |
| 164 | 977 | 0.2569992162 | 0.0920666342 |
| 165 | 983 | 0.3528308132 | 0.0037649628 |
| 166 | 991 | 0.4801524774 | 0.1310866270 |
| 167 | 997 | 0.5753068077 | 0.2262409573 |
| 168 | 1009 | 0.7647603485 | 0.4156944981 |
| 169 | 1013 | 0.8276609257 | 0.4785950753 |
| 170 | 1019 | 0.9217793990 | 0.5727135486 |
| 171 | 1021 | 0.9530906173 | 0.6040247669 |
| 172 | 1031 | 0.1091887160 | 0.2398771344 |
| 173 | 1033 | 0.1403173600 | 0.2087484904 |
| 174 | 1039 | 0.2335229226 | 0.1155429278 |
| 175 | 1049 | 0.3882694814 | 0.0392036310 |
| 176 | 1051 | 0.4191301549 | 0.0700643045 |
| 177 | 1061 | 0.5729949498 | 0.2239290994 |
| 178 | 1063 | 0.6036807738 | 0.2546149234 |
| 179 | 1069 | 0.6955654485 | 0.3464995981 |
| 180 | 1087 | 0.9696830437 | 0.6206171933 |
| 181 | 1091 | 0.0302891298 | 0.3187767206 |
| 182 | 1093 | 0.0605505096 | 0.2885153408 |
| 183 | 1097 | 0.1209903234 | 0.2280755270 |
| 184 | 1103 | 0.2114438108 | 0.1376220396 |
| 185 | 1109 | 0.3016516107 | 0.0474142397 |
| 186 | 1117 | 0.4215499341 | 0.0724840837 |
| 187 | 1123 | 0.5111921602 | 0.1621263098 |
| 188 | 1129 | 0.6005952328 | 0.2515293824 |
| 189 | 1151 | 0.9263909074 | 0.5773250570 |
| 190 | 1153 | 0.9558536927 | 0.6067878423 |
| 191 | 1163 | 0.1027858100 | 0.2462800404 |
| 192 | 1171 | 0.2198772645 | 0.1291885859 |
| 193 | 1181 | 0.3656805549 | 0.0166147045 |
| 194 | 1187 | 0.4528663539 | 0.1038005035 |
| 195 | 1193 | 0.5398320783 | 0.1907662279 |
| 196 | 1201 | 0.6554469023 | 0.3063810519 |
| 197 | 1213 | 0.8281495345 | 0.4790836841 |
| 198 | 1217 | 0.8855270850 | 0.5364612346 |
| 199 | 1223 | 0.9714169001 | 0.6223510497 |
| 200 | 1229 | 0.0570962859 | 0.2919695645 |
| 201 | 1231 | 0.0856095857 | 0.2634562647 |
| 202 | 1237 | 0.1710107901 | 0.1780550603 |
| 203 | 1249 | 0.3411940941 | 0.0078717563 |
| 204 | 1259 | 0.4823899984 | 0.1333241480 |
| 205 | 1277 | 0.7351367704 | 0.3860709200 |
| 206 | 1279 | 0.7631094845 | 0.4140436341 |
| 207 | 1283 | 0.8189893771 | 0.4699235267 |
| 208 | 1289 | 0.9026461420 | 0.5535802916 |
| 209 | 1291 | 0.9304884464 | 0.5814225960 |
| 210 | 1297 | 0.0138862107 | 0.3351796397 |
| 211 | 1301 | 0.0693775937 | 0.2796882567 |
| 212 | 1303 | 0.0970912956 | 0.2519745548 |
| 213 | 1307 | 0.1524549651 | 0.1966108853 |
| 214 | 1319 | 0.3180395947 | 0.0310262557 |
| 215 | 1321 | 0.3455636908 | 0.0035021596 |
| 216 | 1327 | 0.4280112002 | 0.0789453498 |
| 217 | 1361 | 0.8917334914 | 0.5426676410 |
| 218 | 1367 | 0.9729630947 | 0.6238972443 |
| 219 | 1373 | 0.0540146273 | 0.2950512231 |
| 220 | 1381 | 0.1618083521 | 0.1872574983 |
| 221 | 1399 | 0.4032084185 | 0.0541425681 |
| 222 | 1409 | 0.5366487582 | 0.1875829078 |
| 223 | 1423 | 0.7226722277 | 0.3736063773 |
| 224 | 1427 | 0.7756535350 | 0.4265876846 |
| 225 | 1429 | 0.8021163429 | 0.4530504925 |
| 226 | 1433 | 0.8549864615 | 0.5059206111 |
| 227 | 1439 | 0.9341534768 | 0.5850876264 |
| 228 | 1447 | 0.0394532032 | 0.3096126472 |
| 229 | 1451 | 0.0919939095 | 0.2570719409 |
| 230 | 1453 | 0.1182371051 | 0.2308287453 |
| 231 | 1459 | 0.1968585096 | 0.1522073408 |
| 232 | 1471 | 0.3536178215 | 0.0045519711 |
| 233 | 1481 | 0.4837628098 | 0.1346969594 |
| 234 | 1483 | 0.5097390279 | 0.1606731775 |
| 235 | 1487 | 0.5616389693 | 0.2125731189 |
| 236 | 1489 | 0.5875627631 | 0.2384969128 |
| 237 | 1493 | 0.6393581727 | 0.2902923223 |
| 238 | 1499 | 0.7169213652 | 0.3678555148 |
| 239 | 1511 | 0.8715834512 | 0.5225176008 |
| 240 | 1523 | 0.0256326022 | 0.3234332482 |
| 241 | 1531 | 0.1279950930 | 0.2210707574 |
| 242 | 1543 | 0.2810386828 | 0.0680271676 |
| 243 | 1549 | 0.3573373083 | 0.0082714579 |
| 244 | 1553 | 0.4081209905 | 0.0590551401 |
| 245 | 1559 | 0.4841740448 | 0.1351081944 |
| 246 | 1567 | 0.5853508258 | 0.2362849754 |
| 247 | 1571 | 0.6358423652 | 0.2867765148 |
| 248 | 1579 | 0.7366329726 | 0.3875671222 |
| 249 | 1583 | 0.7869325282 | 0.4378666778 |
| 250 | 1597 | 0.9624824054 | 0.6134165550 |
| 251 | 1601 | 0.0124980475 | 0.3365678029 |
| 252 | 1607 | 0.0874045057 | 0.2616613447 |
| 253 | 1609 | 0.1123422403 | 0.2367236101 |
| 254 | 1613 | 0.1621712560 | 0.1868945944 |
| 255 | 1619 | 0.2367990775 | 0.1122667729 |
| 256 | 1621 | 0.2616442784 | 0.0874215720 |
| 257 | 1627 | 0.3360880602 | 0.0129777902 |
| 258 | 1637 | 0.4598566483 | 0.1107907979 |
| 259 | 1657 | 0.7062648741 | 0.3571990237 |
| 260 | 1663 | 0.7798970082 | 0.4308311578 |
| 261 | 1667 | 0.8289113252 | 0.4798454748 |
| 262 | 1669 | 0.8533964316 | 0.5043305812 |
| 263 | 1693 | 0.1460812229 | 0.2029846275 |
| 264 | 1697 | 0.1946598481 | 0.1544060023 |
| 265 | 1699 | 0.2189276910 | 0.1301381593 |
| 266 | 1709 | 0.3400532172 | 0.0090126332 |
| 267 | 1721 | 0.4849370254 | 0.1358711750 |
| 268 | 1723 | 0.5090351610 | 0.1599693106 |
| 269 | 1733 | 0.6293165930 | 0.2802507426 |
| 270 | 1741 | 0.7252920901 | 0.3762262397 |
| 271 | 1747 | 0.7971290880 | 0.4480632376 |
| 272 | 1753 | 0.8688428309 | 0.5197769805 |
| 273 | 1759 | 0.9404339510 | 0.5913681006 |
| 274 | 1777 | 0.1544778167 | 0.1945880337 |
| 275 | 1783 | 0.2255846614 | 0.1234811890 |
| 276 | 1787 | 0.2729227757 | 0.0761430747 |
| 277 | 1789 | 0.2965719651 | 0.0524938853 |
| 278 | 1801 | 0.4381903478 | 0.0891244974 |
| 279 | 1811 | 0.5558456619 | 0.2067798115 |
| 280 | 1823 | 0.6966040804 | 0.3475382300 |
| 281 | 1831 | 0.7901857907 | 0.4411199403 |
| 282 | 1847 | 0.9767378939 | 0.6276720435 |
| 283 | 1861 | 0.1393092202 | 0.2097566302 |
| 284 | 1867 | 0.2087954009 | 0.1402704495 |
| 285 | 1871 | 0.2550575078 | 0.0940083426 |
| 286 | 1873 | 0.2781700168 | 0.0708958336 |
| 287 | 1877 | 0.3243580449 | 0.0247078055 |
| 288 | 1879 | 0.3474336034 | 0.0016322470 |
| 289 | 1889 | 0.4626276242 | 0.1135617738 |
| 290 | 1901 | 0.6004587132 | 0.2513928628 |
| 291 | 1907 | 0.6692111218 | 0.3201452714 |
| 292 | 1913 | 0.7378554573 | 0.3887896069 |
| 293 | 1931 | 0.9431450854 | 0.5940792350 |
| 294 | 1933 | 0.9658958740 | 0.6168300236 |
| 295 | 1949 | 0.1474801093 | 0.2015857411 |
| 296 | 1951 | 0.1701256507 | 0.1789401997 |
| 297 | 1973 | 0.4184646290 | 0.0693987786 |
| 298 | 1979 | 0.4859528391 | 0.1368869887 |
| 299 | 1987 | 0.5757781760 | 0.2267123256 |
| 300 | 1993 | 0.6430285711 | 0.2939627207 |
| 301 | 1997 | 0.6878059430 | 0.3387400926 |
| 302 | 1999 | 0.7101778122 | 0.3611119618 |
| 303 | 2003 | 0.7548880012 | 0.4058221508 |
| 304 | 2011 | 0.8441746496 | 0.4951087992 |
| 305 | 2017 | 0.9110231458 | 0.5619572954 |
| 306 | 2027 | 0.0222167380 | 0.3268491124 |
| 307 | 2029 | 0.0444225182 | 0.3046433322 |
| 308 | 2039 | 0.1552876195 | 0.1937782309 |
| 309 | 2053 | 0.3100430368 | 0.0390228136 |
| 310 | 2063 | 0.4202597967 | 0.0711939463 |
| 311 | 2069 | 0.4862616622 | 0.1371958118 |
| 312 | 2081 | 0.6179789118 | 0.2689130614 |
| 313 | 2083 | 0.6398948290 | 0.2908289786 |
| 314 | 2087 | 0.6836951220 | 0.3346292716 |
| 315 | 2089 | 0.7055795281 | 0.3565136777 |
| 316 | 2099 | 0.8148447558 | 0.4657789054 |
| 317 | 2111 | 0.9456200306 | 0.5965541802 |
| 318 | 2113 | 0.9673797382 | 0.6183138878 |
| 319 | 2129 | 0.1410879802 | 0.2079778702 |
| 320 | 2131 | 0.1627555503 | 0.1863103001 |
| 321 | 2137 | 0.2276973253 | 0.1213685251 |
| 322 | 2141 | 0.2709412050 | 0.0781246454 |
| 323 | 2143 | 0.2925479964 | 0.0565178540 |
| 324 | 2153 | 0.4004310325 | 0.0513651821 |
| 325 | 2161 | 0.4865571967 | 0.1374913463 |
| 326 | 2179 | 0.6797600679 | 0.3306942175 |
| 327 | 2203 | 0.9361268108 | 0.5870609604 |
| 328 | 2207 | 0.9787185862 | 0.6296527358 |
| 329 | 2213 | 0.0425339454 | 0.3065319050 |
| 330 | 2221 | 0.1274866718 | 0.2215791786 |
| 331 | 2237 | 0.2969343615 | 0.0521314889 |
| 332 | 2239 | 0.3180726573 | 0.0309931931 |
| 333 | 2243 | 0.3603209449 | 0.0112550945 |
| 334 | 2251 | 0.4447046571 | 0.0956388067 |
| 335 | 2267 | 0.6130234285 | 0.2639575781 |
| 336 | 2269 | 0.6340214553 | 0.2849556049 |
| 337 | 2273 | 0.6759897642 | 0.3269239138 |
| 338 | 2281 | 0.7598157450 | 0.4107498946 |
| 339 | 2287 | 0.8225888049 | 0.4735229545 |
| 340 | 2293 | 0.8852795753 | 0.5362137249 |
| 341 | 2297 | 0.9270278653 | 0.5779620149 |
| 342 | 2309 | 0.0520551069 | 0.2970107435 |
| 343 | 2311 | 0.0728613669 | 0.2762044835 |
| 344 | 2333 | 0.3011387029 | 0.0479271475 |
| 345 | 2339 | 0.3632091574 | 0.0141433070 |
| 346 | 2341 | 0.3838816136 | 0.0348157632 |
| 347 | 2347 | 0.4458460552 | 0.0967802048 |
| 348 | 2351 | 0.4871116896 | 0.1380458392 |
| 349 | 2357 | 0.5489443758 | 0.1998785254 |
| 350 | 2371 | 0.6929152958 | 0.3438494454 |
| 351 | 2377 | 0.7544869730 | 0.4054211226 |
| 352 | 2381 | 0.7954915950 | 0.4464257446 |
| 353 | 2383 | 0.8159809898 | 0.4669151394 |
| 354 | 2389 | 0.8773976394 | 0.5283317890 |
| 355 | 2393 | 0.9182992345 | 0.5692333841 |
| 356 | 2399 | 0.9795875850 | 0.6305217346 |
| 357 | 2411 | 0.1019347888 | 0.2471310616 |
| 358 | 2417 | 0.1629942131 | 0.1860716373 |
| 359 | 2423 | 0.2239778970 | 0.1250879534 |
| 360 | 2437 | 0.3659801888 | 0.0169143384 |
| 361 | 2441 | 0.4064773081 | 0.0574114577 |
| 362 | 2447 | 0.4671608241 | 0.1180949737 |
| 363 | 2459 | 0.5883050729 | 0.2392392225 |
| 364 | 2467 | 0.6689037528 | 0.3198379024 |
| 365 | 2473 | 0.7292670366 | 0.3802011862 |
| 366 | 2477 | 0.7694685525 | 0.4204027021 |
| 367 | 2503 | 0.0299910054 | 0.3190748450 |
| 368 | 2521 | 0.2095608425 | 0.1395050079 |
| 369 | 2531 | 0.3090449124 | 0.0400209380 |
| 370 | 2539 | 0.3884907494 | 0.0394248990 |
| 371 | 2543 | 0.4281667325 | 0.0791008821 |
| 372 | 2549 | 0.4876222455 | 0.1385563951 |
| 373 | 2551 | 0.5074251967 | 0.1583593463 |
| 374 | 2557 | 0.5667875191 | 0.2177216687 |
| 375 | 2579 | 0.7838557024 | 0.4347898520 |
| 376 | 2591 | 0.9018663705 | 0.5528005201 |
| 377 | 2593 | 0.9215082259 | 0.5724423755 |
| 378 | 2609 | 0.0783711565 | 0.2706946939 |
| 379 | 2617 | 0.1566222497 | 0.1924436007 |
| 380 | 2621 | 0.1957029447 | 0.1533629057 |
| 381 | 2633 | 0.3127664427 | 0.0362994077 |
| 382 | 2647 | 0.4490038776 | 0.0999380272 |
| 383 | 2657 | 0.5460958754 | 0.1970300250 |
| 384 | 2659 | 0.5654923374 | 0.2164264870 |
| 385 | 2663 | 0.6042633898 | 0.2551975394 |
| 386 | 2671 | 0.6817182377 | 0.3326523873 |
| 387 | 2677 | 0.7397332811 | 0.3906674307 |
| 388 | 2683 | 0.7976833459 | 0.4486174955 |
| 389 | 2687 | 0.8362807308 | 0.4872148804 |
| 390 | 2689 | 0.8555686499 | 0.5065027995 |
| 391 | 2693 | 0.8941229813 | 0.5450571309 |
| 392 | 2699 | 0.9519008314 | 0.6028349810 |
| 393 | 2707 | 0.0288381573 | 0.3202276931 |
| 394 | 2711 | 0.0672641878 | 0.2818016626 |
| 395 | 2713 | 0.0864665724 | 0.2625992780 |
| 396 | 2719 | 0.1440312979 | 0.2050345525 |
| 397 | 2729 | 0.2398315464 | 0.1092343040 |
| 398 | 2731 | 0.2589705218 | 0.0900953286 |
| 399 | 2741 | 0.3545604508 | 0.0054946004 |
| 400 | 2749 | 0.4309069157 | 0.0818410653 |
| 401 | 2753 | 0.4690384894 | 0.1199726390 |
| 402 | 2767 | 0.6022813193 | 0.2532154690 |
| 403 | 2777 | 0.6972485050 | 0.3481826546 |
| 404 | 2789 | 0.8109837060 | 0.4619178556 |
| 405 | 2791 | 0.8299157675 | 0.4808499171 |
| 406 | 2797 | 0.8866712887 | 0.5376054383 |
| 407 | 2801 | 0.9244744896 | 0.5754086392 |
| 408 | 2803 | 0.9433659678 | 0.5943001174 |
| 409 | 2819 | 0.0942558098 | 0.2548100406 |
| 410 | 2833 | 0.2259335287 | 0.1231323217 |
| 411 | 2837 | 0.2634959423 | 0.0855699081 |
| 412 | 2843 | 0.3197899471 | 0.0292759033 |
| 413 | 2851 | 0.3947562968 | 0.0456904465 |
| 414 | 2857 | 0.4509120596 | 0.1018462092 |
| 415 | 2861 | 0.4883164813 | 0.1392506309 |
| 416 | 2879 | 0.6563137012 | 0.3072478508 |
| 417 | 2887 | 0.7308105280 | 0.3817446776 |
| 418 | 2897 | 0.8237865632 | 0.4747207128 |
| 419 | 2903 | 0.8794951721 | 0.5304293217 |
| 420 | 2909 | 0.9351462406 | 0.5860803902 |
| 421 | 2917 | 0.0092584656 | 0.3398073848 |
| 422 | 2927 | 0.1017559789 | 0.2473098715 |
| 423 | 2939 | 0.2125446737 | 0.1365211767 |
| 424 | 2953 | 0.3415126768 | 0.0075531736 |
| 425 | 2957 | 0.3783044973 | 0.0292386469 |
| 426 | 2963 | 0.4334456010 | 0.0843797506 |
| 427 | 2969 | 0.4885309033 | 0.1394650529 |
| 428 | 2971 | 0.5068802996 | 0.1578144492 |
| 429 | 2999 | 0.7631262804 | 0.4140604300 |
| 430 | 3001 | 0.7813836992 | 0.4323178488 |
| 431 | 3011 | 0.8725796733 | 0.5235138229 |
| 432 | 3019 | 0.9454274713 | 0.5963616209 |
| 433 | 3023 | 0.9818151756 | 0.6327493252 |
| 434 | 3037 | 0.1089829338 | 0.2400829166 |
| 435 | 3041 | 0.1452627158 | 0.2038031345 |
| 436 | 3049 | 0.2177507691 | 0.1313150813 |
| 437 | 3061 | 0.3263047745 | 0.0227610759 |
| 438 | 3067 | 0.3805019840 | 0.0314361336 |
| 439 | 3079 | 0.4887375960 | 0.1396717456 |
| 440 | 3083 | 0.5247692476 | 0.1757033972 |
| 441 | 3089 | 0.5787729264 | 0.2297070760 |
| 442 | 3109 | 0.7584074378 | 0.4093415874 |
| 443 | 3119 | 0.8480080218 | 0.4989421714 |
| 444 | 3121 | 0.8659108939 | 0.5168450435 |
| 445 | 3137 | 0.0089278598 | 0.3401379906 |
| 446 | 3163 | 0.2405547626 | 0.1085110878 |
| 447 | 3167 | 0.2761050536 | 0.0729607968 |
| 448 | 3169 | 0.2938717802 | 0.0551940702 |
| 449 | 3181 | 0.4003546088 | 0.0512887584 |
| 450 | 3187 | 0.4535207051 | 0.1044548547 |
| 451 | 3191 | 0.4889369700 | 0.1398711196 |
| 452 | 3203 | 0.5950527873 | 0.2459869369 |
| 453 | 3209 | 0.6480361531 | 0.2989703027 |
| 454 | 3217 | 0.7186036499 | 0.3695377996 |
| 455 | 3221 | 0.7538544947 | 0.4047886443 |
| 456 | 3229 | 0.8242905807 | 0.4752247303 |
| 457 | 3251 | 0.0175411606 | 0.3315246898 |
| 458 | 3253 | 0.0350769264 | 0.3139889240 |
| 459 | 3257 | 0.0701322935 | 0.2789335569 |
| 460 | 3259 | 0.0876519048 | 0.2614139456 |
| 461 | 3271 | 0.1926568713 | 0.1564089791 |
| 462 | 3299 | 0.4369219231 | 0.0878560727 |
| 463 | 3301 | 0.4543296889 | 0.1052638385 |
| 464 | 3307 | 0.5065213693 | 0.1574555189 |
| 465 | 3313 | 0.5586657246 | 0.2095998742 |
| 466 | 3319 | 0.6107628833 | 0.2616970329 |
| 467 | 3323 | 0.6454681653 | 0.2964023149 |
| 468 | 3329 | 0.6974869470 | 0.3484210966 |
| 469 | 3331 | 0.7148161220 | 0.3657502716 |
| 470 | 3343 | 0.8186821019 | 0.4696162515 |
| 471 | 3347 | 0.8532626565 | 0.5041968061 |
| 472 | 3359 | 0.9568805234 | 0.6078146730 |
| 473 | 3361 | 0.9741321625 | 0.6250663121 |
| 474 | 3371 | 0.0603134680 | 0.2887523824 |
| 475 | 3373 | 0.0775343829 | 0.2715314675 |
| 476 | 3389 | 0.2151183113 | 0.1339475391 |
| 477 | 3391 | 0.2322934462 | 0.1167724042 |
| 478 | 3407 | 0.3695125900 | 0.0204467397 |
| 479 | 3413 | 0.4208866759 | 0.0718208255 |
| 480 | 3433 | 0.5918083012 | 0.2427424508 |
| 481 | 3449 | 0.7281874401 | 0.3791215897 |
| 482 | 3457 | 0.7962583844 | 0.4471925340 |
| 483 | 3461 | 0.8302643203 | 0.4811984699 |
| 484 | 3463 | 0.8472599192 | 0.4981940688 |
| 485 | 3467 | 0.8812364001 | 0.5321705497 |
| 486 | 3469 | 0.8982172905 | 0.5491514401 |
| 487 | 3491 | 0.0846849869 | 0.2643808635 |
| 488 | 3499 | 0.1523456847 | 0.1967201657 |
| 489 | 3511 | 0.2536918681 | 0.0953739823 |
| 490 | 3517 | 0.3043000127 | 0.0447658377 |
| 491 | 3527 | 0.3885510852 | 0.0394852348 |
| 492 | 3529 | 0.4053869611 | 0.0563211107 |
| 493 | 3533 | 0.4390444069 | 0.0899785565 |
| 494 | 3539 | 0.4894948709 | 0.1404290205 |
| 495 | 3541 | 0.5063021872 | 0.1572363368 |
| 496 | 3547 | 0.5566956773 | 0.2076298269 |
| 497 | 3557 | 0.6405902050 | 0.2915243546 |
| 498 | 3559 | 0.6573549531 | 0.3082891027 |
| 499 | 3571 | 0.7578446733 | 0.4087788229 |
| 500 | 3581 | 0.8414572015 | 0.4923913511 |
| 501 | 3583 | 0.8581656919 | 0.5090998415 |
| 502 | 3593 | 0.9416382826 | 0.5925724322 |
| 503 | 3607 | 0.0583050044 | 0.2907608460 |
| 504 | 3613 | 0.1082357086 | 0.2408301418 |
| 505 | 3617 | 0.1414998150 | 0.2075660354 |
| 506 | 3623 | 0.1913615064 | 0.1577043440 |
| 507 | 3631 | 0.2577795807 | 0.0912862697 |
| 508 | 3637 | 0.3075451333 | 0.0415207171 |
| 509 | 3643 | 0.3572696533 | 0.0082038029 |
| 510 | 3659 | 0.4896685393 | 0.1406026889 |
| 511 | 3671 | 0.5887778388 | 0.2397119884 |
| 512 | 3673 | 0.6052802980 | 0.2562144476 |
| 513 | 3677 | 0.6382717432 | 0.2892058928 |
| 514 | 3691 | 0.7536007163 | 0.4045348659 |
| 515 | 3697 | 0.8029604542 | 0.4538946038 |
| 516 | 3701 | 0.8358446970 | 0.4867788466 |
| 517 | 3709 | 0.9015599143 | 0.5524940639 |
| 518 | 3719 | 0.9836043540 | 0.6345385036 |
| 519 | 3727 | 0.0491605184 | 0.2999053320 |
| 520 | 3733 | 0.0982814816 | 0.2507843688 |
| 521 | 3739 | 0.1473629848 | 0.2017028656 |
| 522 | 3761 | 0.3269924258 | 0.0220734246 |
| 523 | 3767 | 0.3758910322 | 0.0268251818 |
| 524 | 3769 | 0.3921819127 | 0.0431160623 |
| 525 | 3779 | 0.4735715572 | 0.1245057068 |
| 526 | 3793 | 0.5873363607 | 0.2382705103 |
| 527 | 3797 | 0.6198020120 | 0.2707361616 |
| 528 | 3803 | 0.6684684421 | 0.3194025917 |
| 529 | 3821 | 0.8142378421 | 0.4651719917 |
| 530 | 3823 | 0.8304132284 | 0.4813473780 |
| 531 | 3833 | 0.9112267687 | 0.5621609183 |
| 532 | 3847 | 0.0241888298 | 0.3248770206 |
| 533 | 3851 | 0.0564259364 | 0.2926399140 |
| 534 | 3853 | 0.0725382114 | 0.2765276390 |
| 535 | 3863 | 0.1530369330 | 0.1960289174 |
| 536 | 3877 | 0.2655603042 | 0.0835055462 |
| 537 | 3881 | 0.2976725087 | 0.0513933417 |
| 538 | 3889 | 0.3618473107 | 0.0127814603 |
| 539 | 3907 | 0.5059997120 | 0.1569338616 |
| 540 | 3911 | 0.5379884550 | 0.1889226046 |
| 541 | 3917 | 0.5859409133 | 0.2368750629 |
| 542 | 3919 | 0.6019169036 | 0.2528510532 |
| 543 | 3923 | 0.6338566592 | 0.2847908088 |
| 544 | 3929 | 0.6817357769 | 0.3326699265 |
| 545 | 3931 | 0.6976873577 | 0.3486215073 |
| 546 | 3943 | 0.7933117458 | 0.4442458954 |
| 547 | 3947 | 0.8251541980 | 0.4760883476 |
| 548 | 3967 | 0.9841249840 | 0.6350591336 |
| 549 | 3989 | 0.1585306986 | 0.1905351518 |
| 550 | 4001 | 0.2534584035 | 0.0956074469 |
| 551 | 4003 | 0.2692658405 | 0.0798000099 |
| 552 | 4007 | 0.3008688724 | 0.0481969780 |
| 553 | 4013 | 0.3482438588 | 0.0008219916 |
| 554 | 4019 | 0.3955834424 | 0.0465175920 |
| 555 | 4021 | 0.4113554500 | 0.0622895996 |
| 556 | 4027 | 0.4586479528 | 0.1095821024 |
| 557 | 4049 | 0.6317530797 | 0.2826872293 |
| 558 | 4051 | 0.6474665639 | 0.2984007135 |
| 559 | 4057 | 0.6945837572 | 0.3455179068 |
| 560 | 4073 | 0.8200595424 | 0.4709936920 |
| 561 | 4079 | 0.8670494073 | 0.5179835569 |
| 562 | 4091 | 0.9609255718 | 0.6118597214 |
| 563 | 4093 | 0.9765582069 | 0.6274923565 |
| 564 | 4099 | 0.0234332100 | 0.3256326404 |
| 565 | 4111 | 0.1170804076 | 0.2319854428 |
| 566 | 4127 | 0.2417309854 | 0.1073348650 |
| 567 | 4129 | 0.2572953057 | 0.0917705447 |
| 568 | 4133 | 0.2884126418 | 0.0606532086 |
| 569 | 4139 | 0.3350604259 | 0.0140054245 |
| 570 | 4153 | 0.4437739429 | 0.0947080925 |
| 571 | 4157 | 0.4748012793 | 0.1257354289 |
| 572 | 4159 | 0.4903093495 | 0.1412434991 |
| 573 | 4177 | 0.6297145282 | 0.2806486778 |
| 574 | 4201 | 0.8151216924 | 0.4660558420 |
| 575 | 4211 | 0.8922183316 | 0.5431524812 |
| 576 | 4217 | 0.9384323802 | 0.5893665298 |
| 577 | 4219 | 0.9538297562 | 0.6047639058 |
| 578 | 4229 | 0.0307619516 | 0.3183038988 |
| 579 | 4231 | 0.0461374718 | 0.3029283786 |
| 580 | 4241 | 0.1229606207 | 0.2261052297 |
| 581 | 4243 | 0.1383143779 | 0.2107514725 |
| 582 | 4253 | 0.2150289427 | 0.1340369077 |
| 583 | 4259 | 0.2610143960 | 0.0880514544 |
| 584 | 4261 | 0.2763356815 | 0.0727301689 |
| 585 | 4271 | 0.3528882300 | 0.0038223796 |
| 586 | 4273 | 0.3681879816 | 0.0191221312 |
| 587 | 4283 | 0.4446330878 | 0.0955672374 |
| 588 | 4289 | 0.4904573201 | 0.1413914697 |
| 589 | 4297 | 0.5515064663 | 0.2024406159 |
| 590 | 4327 | 0.7799361508 | 0.4308703004 |
| 591 | 4337 | 0.8559033041 | 0.5068374537 |
| 592 | 4339 | 0.8710862215 | 0.5220203711 |
| 593 | 4349 | 0.9469483752 | 0.5978825248 |
| 594 | 4357 | 0.0075753228 | 0.3414905276 |
| 595 | 4363 | 0.0530090155 | 0.2960568349 |
| 596 | 4373 | 0.1286624695 | 0.2204033809 |
| 597 | 4391 | 0.2646210281 | 0.0844448223 |
| 598 | 4397 | 0.3098786004 | 0.0391872500 |
| 599 | 4409 | 0.4003012041 | 0.0512353537 |
| 600 | 4421 | 0.4906008395 | 0.1415349891 |
| 601 | 4423 | 0.5056388587 | 0.1565730083 |
| 602 | 4441 | 0.6408283262 | 0.2917624758 |
| 603 | 4447 | 0.6858305789 | 0.3367647285 |
| 604 | 4451 | 0.7158152165 | 0.3667493661 |
| 605 | 4457 | 0.7607669219 | 0.4117010715 |
| 606 | 4463 | 0.8056883806 | 0.4566225302 |
| 607 | 4481 | 0.9402718847 | 0.5912060343 |
| 608 | 4483 | 0.9552089086 | 0.6061430582 |
| 609 | 4493 | 0.0298440995 | 0.3192217509 |
| 610 | 4507 | 0.1341939700 | 0.2148718804 |
| 611 | 4513 | 0.1788657243 | 0.1702001261 |
| 612 | 4517 | 0.2086303982 | 0.1404354522 |
| 613 | 4519 | 0.2235077930 | 0.1255580574 |
| 614 | 4523 | 0.2532527094 | 0.0958131410 |
| 615 | 4547 | 0.4314466699 | 0.0823808195 |
| 616 | 4549 | 0.4462749157 | 0.0972090653 |
| 617 | 4561 | 0.5351760196 | 0.1861101692 |
| 618 | 4567 | 0.5795827155 | 0.2305168651 |
| 619 | 4583 | 0.6978581641 | 0.3487923137 |
| 620 | 4591 | 0.7569184659 | 0.4078526155 |
| 621 | 4597 | 0.8011799307 | 0.4521140803 |
| 622 | 4603 | 0.8454125199 | 0.4963466695 |
| 623 | 4621 | 0.9779375974 | 0.6288717470 |
| 624 | 4637 | 0.0955211449 | 0.2535447055 |
| 625 | 4639 | 0.1102048154 | 0.2388610350 |
| 626 | 4643 | 0.1395626637 | 0.2095031867 |
| 627 | 4649 | 0.1835757349 | 0.1654901155 |
| 628 | 4651 | 0.1982404465 | 0.1508254039 |
| 629 | 4657 | 0.2422156733 | 0.1068501771 |
| 630 | 4663 | 0.2861625807 | 0.0629032697 |
| 631 | 4673 | 0.3593446429 | 0.0102787925 |
| 632 | 4679 | 0.4032162987 | 0.0541504483 |
| 633 | 4691 | 0.4908753047 | 0.1418094543 |
| 634 | 4703 | 0.5784222624 | 0.2293564120 |
| 635 | 4721 | 0.7095335452 | 0.3604676948 |
| 636 | 4723 | 0.7240860252 | 0.3750201748 |
| 637 | 4729 | 0.7677249878 | 0.4186591374 |
| 638 | 4733 | 0.7968022513 | 0.4477364009 |
| 639 | 4751 | 0.9274981412 | 0.5784322908 |
| 640 | 4759 | 0.9855057240 | 0.6364398736 |
| 641 | 4783 | 0.1592365487 | 0.1898293017 |
| 642 | 4787 | 0.1881492743 | 0.1609165761 |
| 643 | 4789 | 0.2026011072 | 0.1464647432 |
| 644 | 4793 | 0.2314957227 | 0.1175701277 |
| 645 | 4799 | 0.2748150485 | 0.0742508019 |
| 646 | 4801 | 0.2892488053 | 0.0598170451 |
| 647 | 4813 | 0.3757882838 | 0.0267224334 |
| 648 | 4817 | 0.4046107978 | 0.0555449474 |
| 649 | 4831 | 0.5053954740 | 0.1563296236 |
| 650 | 4861 | 0.7208720542 | 0.3718062038 |
| 651 | 4871 | 0.7925497457 | 0.4434838953 |
| 652 | 4877 | 0.8355210477 | 0.4864551973 |
| 653 | 4889 | 0.9213844257 | 0.5723185753 |
| 654 | 4903 | 0.0214252925 | 0.3276405579 |
| 655 | 4909 | 0.0642562224 | 0.2848096280 |
| 656 | 4919 | 0.1355829804 | 0.2134828700 |
| 657 | 4931 | 0.2210794562 | 0.1279863942 |
| 658 | 4933 | 0.2353187506 | 0.1137470998 |
| 659 | 4937 | 0.2637886824 | 0.0852771680 |
| 660 | 4943 | 0.3064719638 | 0.0425938866 |
| 661 | 4951 | 0.3633427290 | 0.0142768786 |
| 662 | 4957 | 0.4059656563 | 0.0568998059 |
| 663 | 4967 | 0.4769465854 | 0.1278807350 |
| 664 | 4969 | 0.4911341943 | 0.1420683439 |
| 665 | 4973 | 0.5195008491 | 0.1704349987 |
| 666 | 4987 | 0.6186944088 | 0.2696285584 |
| 667 | 4993 | 0.6611633077 | 0.3120974573 |
| 668 | 4999 | 0.7036066973 | 0.3545408469 |
| 669 | 5003 | 0.7318881411 | 0.3828222907 |
| 670 | 5009 | 0.7742891169 | 0.4252232665 |
| 671 | 5011 | 0.7884171316 | 0.4393512812 |
| 672 | 5021 | 0.8590149522 | 0.5099491018 |
| 673 | 5023 | 0.8731260775 | 0.5240602271 |
| 674 | 5039 | 0.9859140957 | 0.6368482453 |
| 675 | 5051 | 0.0703876449 | 0.2786782055 |
| 676 | 5059 | 0.1266476083 | 0.2224182421 |
| 677 | 5077 | 0.2530701093 | 0.0959957411 |
| 678 | 5081 | 0.2811335488 | 0.0679323016 |
| 679 | 5087 | 0.3232080041 | 0.0258578463 |
| 680 | 5099 | 0.4072825418 | 0.0582166914 |
| 681 | 5101 | 0.4212853427 | 0.0722194923 |
| 682 | 5107 | 0.4632772828 | 0.1142114324 |
| 683 | 5113 | 0.5052445629 | 0.1561787125 |
| 684 | 5119 | 0.5471872263 | 0.1981213759 |
| 685 | 5147 | 0.7425954367 | 0.3935295863 |
| 686 | 5153 | 0.7843994194 | 0.4353335690 |
| 687 | 5167 | 0.8818474999 | 0.5327816495 |
| 688 | 5171 | 0.9096655534 | 0.5605997030 |
| 689 | 5179 | 0.9652694013 | 0.6162035509 |
| 690 | 5189 | 0.0347138538 | 0.3143519966 |
| 691 | 5197 | 0.0902212509 | 0.2588445995 |
| 692 | 5209 | 0.1734023031 | 0.1756635473 |
| 693 | 5227 | 0.2979944397 | 0.0510714107 |
| 694 | 5231 | 0.3256524340 | 0.0234134164 |
| 695 | 5233 | 0.3394774656 | 0.0095883848 |
| 696 | 5237 | 0.3671196055 | 0.0180537551 |
| 697 | 5261 | 0.5327512232 | 0.1836853728 |
| 698 | 5273 | 0.6154253585 | 0.2663595081 |
| 699 | 5279 | 0.6567271490 | 0.3076612986 |
| 700 | 5281 | 0.6704891961 | 0.3214233457 |
| 701 | 5297 | 0.7804918917 | 0.4314260413 |
| 702 | 5303 | 0.8217000626 | 0.4726342122 |
| 703 | 5309 | 0.8628849278 | 0.5138190774 |
| 704 | 5323 | 0.9588925355 | 0.6098266851 |
| 705 | 5333 | 0.0273921210 | 0.3216737294 |
| 706 | 5347 | 0.1231837381 | 0.2258821123 |
| 707 | 5351 | 0.1505297315 | 0.1985361189 |
| 708 | 5381 | 0.3552997404 | 0.0062338900 |
| 709 | 5387 | 0.3961851870 | 0.0471193366 |
| 710 | 5393 | 0.4370478709 | 0.0879820205 |
| 711 | 5399 | 0.4778878303 | 0.1288219799 |
| 712 | 5407 | 0.5323058254 | 0.1832399750 |
| 713 | 5413 | 0.5730929077 | 0.2240270573 |
| 714 | 5417 | 0.6002717386 | 0.2512058882 |
| 715 | 5419 | 0.6138573911 | 0.2647915407 |
| 716 | 5431 | 0.6953187116 | 0.3462528612 |
| 717 | 5437 | 0.7360156233 | 0.3869497729 |
| 718 | 5441 | 0.7631344236 | 0.4140685732 |
| 719 | 5443 | 0.7766900857 | 0.4276242353 |
| 720 | 5449 | 0.8173421358 | 0.4682762854 |
| 721 | 5471 | 0.9662085009 | 0.6171426505 |
| 722 | 5477 | 0.0067564483 | 0.3423094021 |
| 723 | 5479 | 0.0202674948 | 0.3287983556 |
| 724 | 5483 | 0.0472821919 | 0.3017836585 |
| 725 | 5501 | 0.1687265632 | 0.1803392872 |
| 726 | 5503 | 0.1822081095 | 0.1668577409 |
| 727 | 5507 | 0.2091638546 | 0.1399019958 |
| 728 | 5519 | 0.2899724054 | 0.0590934450 |
| 729 | 5521 | 0.3034319530 | 0.0456338974 |
| 730 | 5527 | 0.3437959752 | 0.0052698752 |
| 731 | 5531 | 0.3706931526 | 0.0216273022 |
| 732 | 5557 | 0.5452882482 | 0.1962223978 |
| 733 | 5563 | 0.5855213832 | 0.2364555328 |
| 734 | 5569 | 0.6257328272 | 0.2766669768 |
| 735 | 5573 | 0.6525284234 | 0.3034625730 |
| 736 | 5581 | 0.7060907825 | 0.3570249321 |
| 737 | 5591 | 0.7729897757 | 0.4239239253 |
| 738 | 5623 | 0.9866654813 | 0.6375996309 |
| 739 | 5639 | 0.0932753314 | 0.2557905190 |
| 740 | 5641 | 0.1065909225 | 0.2424749279 |
| 741 | 5647 | 0.1465235390 | 0.2025423114 |
| 742 | 5651 | 0.1731334986 | 0.1759323518 |
| 743 | 5653 | 0.1864349467 | 0.1626309037 |
| 744 | 5657 | 0.2130307859 | 0.1360350645 |
| 745 | 5659 | 0.2263251794 | 0.1227406710 |
| 746 | 5669 | 0.2927619363 | 0.0563039141 |
| 747 | 5683 | 0.3856750318 | 0.0366091814 |
| 748 | 5689 | 0.4254598925 | 0.0763940421 |
| 749 | 5693 | 0.4519714786 | 0.1029056282 |
| 750 | 5701 | 0.5049667241 | 0.1559008737 |
| 751 | 5711 | 0.5711585196 | 0.2220926692 |
| 752 | 5717 | 0.6108457829 | 0.2617799325 |
| 753 | 5737 | 0.7429864740 | 0.3939206236 |
| 754 | 5741 | 0.7693869581 | 0.4203211077 |
| 755 | 5743 | 0.7825837511 | 0.4335179008 |
| 756 | 5749 | 0.8221603491 | 0.4730944987 |
| 757 | 5779 | 0.0197342800 | 0.3293315704 |
| 758 | 5783 | 0.0460386871 | 0.3030271633 |
| 759 | 5791 | 0.0986202240 | 0.2504456264 |
| 760 | 5801 | 0.1642960973 | 0.1847697531 |
| 761 | 5807 | 0.2036744521 | 0.1453913983 |
| 762 | 5813 | 0.2430324685 | 0.1060333819 |
| 763 | 5821 | 0.2954782408 | 0.0535876095 |
| 764 | 5827 | 0.3347889235 | 0.0142769269 |
| 765 | 5839 | 0.4133496190 | 0.0642837686 |
| 766 | 5843 | 0.4395185751 | 0.0904527247 |
| 767 | 5849 | 0.4787552200 | 0.1296893696 |
| 768 | 5851 | 0.4918296291 | 0.1427637787 |
| 769 | 5857 | 0.5310394546 | 0.1819736042 |
| 770 | 5861 | 0.5571681817 | 0.2081023313 |
| 771 | 5867 | 0.5963445603 | 0.2472787099 |
| 772 | 5869 | 0.6093989012 | 0.2603330508 |
| 773 | 5879 | 0.6746372668 | 0.3255714164 |
| 774 | 5881 | 0.6876782802 | 0.3386124298 |
| 775 | 5897 | 0.7919266590 | 0.4428608086 |
| 776 | 5903 | 0.8309833335 | 0.4819174831 |
| 777 | 5923 | 0.9610290991 | 0.6119632487 |
| 778 | 5927 | 0.9870118916 | 0.6379460412 |
| 779 | 5939 | 0.0649077077 | 0.2841581427 |
| 780 | 5953 | 0.1556867638 | 0.1933790866 |
| 781 | 5981 | 0.3369252039 | 0.0121406465 |
| 782 | 5987 | 0.3757067819 | 0.0266409315 |
| 783 | 6007 | 0.5048385586 | 0.1557727082 |
| 784 | 6011 | 0.5306391048 | 0.1815732544 |
| 785 | 6029 | 0.6466354712 | 0.2975696208 |
| 786 | 6037 | 0.6981338257 | 0.3490679753 |
| 787 | 6043 | 0.7367352029 | 0.3876693525 |
| 788 | 6047 | 0.7624588089 | 0.4133929585 |
| 789 | 6053 | 0.8010282708 | 0.4519624204 |
| 790 | 6067 | 0.8909494101 | 0.5418835597 |
| 791 | 6073 | 0.9294552785 | 0.5803894281 |
| 792 | 6079 | 0.9679421301 | 0.6188762797 |
| 793 | 6089 | 0.0320446996 | 0.3170211508 |
| 794 | 6091 | 0.0448588954 | 0.3042069550 |
| 795 | 6101 | 0.1088983407 | 0.2401675097 |
| 796 | 6113 | 0.1856764376 | 0.1633894128 |
| 797 | 6121 | 0.2368199763 | 0.1122458741 |
| 798 | 6131 | 0.3007024234 | 0.0483634270 |
| 799 | 6133 | 0.3134726596 | 0.0355931908 |
| 800 | 6143 | 0.3772926299 | 0.0282267795 |
| 801 | 6151 | 0.4283112148 | 0.0792453644 |
| 802 | 6163 | 0.5047769247 | 0.1557110743 |
| 803 | 6173 | 0.5684415017 | 0.2193756513 |
| 804 | 6197 | 0.7210264161 | 0.3719605657 |
| 805 | 6199 | 0.7337284777 | 0.3846626273 |
| 806 | 6203 | 0.7591264553 | 0.4100606049 |
| 807 | 6211 | 0.8098978555 | 0.4608320051 |
| 808 | 6217 | 0.8479549513 | 0.4988891009 |
| 809 | 6221 | 0.8733161468 | 0.5242502964 |
| 810 | 6229 | 0.9240140895 | 0.5749482391 |
| 811 | 6247 | 0.0379655609 | 0.3111002895 |
| 812 | 6257 | 0.1012010023 | 0.2478648481 |
| 813 | 6263 | 0.1391180138 | 0.2099478366 |
| 814 | 6269 | 0.1770168673 | 0.1720489831 |
| 815 | 6271 | 0.1896457878 | 0.1594200626 |
| 816 | 6277 | 0.2275204711 | 0.1215453793 |
| 817 | 6287 | 0.2906047398 | 0.0584611106 |
| 818 | 6299 | 0.3662396741 | 0.0171738237 |
| 819 | 6301 | 0.3788384899 | 0.0297726395 |
| 820 | 6311 | 0.4418025979 | 0.0927367475 |
| 821 | 6317 | 0.4795571201 | 0.1304912697 |
| 822 | 6323 | 0.5172937165 | 0.1682278661 |
| 823 | 6329 | 0.5550124128 | 0.2059465624 |
| 824 | 6337 | 0.6052762070 | 0.2562103566 |
| 825 | 6343 | 0.6429532350 | 0.2938873846 |
| 826 | 6353 | 0.7057087040 | 0.3566428536 |
| 827 | 6359 | 0.7433382798 | 0.3942724294 |
| 828 | 6361 | 0.7558775264 | 0.4068116760 |
| 829 | 6367 | 0.7934834432 | 0.4444175928 |
| 830 | 6373 | 0.8310716451 | 0.4820057947 |
| 831 | 6379 | 0.8686421570 | 0.5195763066 |
| 832 | 6389 | 0.9312204336 | 0.5821545832 |
| 833 | 6397 | 0.9812478022 | 0.6321819518 |
| 834 | 6421 | 0.1311425103 | 0.2179233401 |
| 835 | 6427 | 0.1685723959 | 0.1804934545 |
| 836 | 6449 | 0.3056660517 | 0.0433997987 |
| 837 | 6451 | 0.3181175078 | 0.0309483426 |
| 838 | 6469 | 0.4300938704 | 0.0810280200 |
| 839 | 6473 | 0.4549563420 | 0.1058904916 |
| 840 | 6481 | 0.5046582503 | 0.1555923999 |
| 841 | 6491 | 0.5667425182 | 0.2176766678 |
| 842 | 6521 | 0.7527089329 | 0.4036430825 |
| 843 | 6529 | 0.8022276921 | 0.4531618417 |
| 844 | 6547 | 0.9135340966 | 0.5644682462 |
| 845 | 6551 | 0.9382480660 | 0.5891822156 |
| 846 | 6553 | 0.9506022214 | 0.6015363710 |
| 847 | 6563 | 0.0123447383 | 0.3367211121 |
| 848 | 6569 | 0.0493676718 | 0.2996981786 |
| 849 | 6571 | 0.0617048920 | 0.2873609584 |
| 850 | 6577 | 0.0987052918 | 0.2503605586 |
| 851 | 6581 | 0.1233628494 | 0.2257030010 |
| 852 | 6599 | 0.2342292387 | 0.1148366117 |
| 853 | 6607 | 0.2834546510 | 0.0656111994 |
| 854 | 6619 | 0.3572369246 | 0.0081710742 |
| 855 | 6637 | 0.4677850442 | 0.1187191938 |
| 856 | 6653 | 0.5659242576 | 0.2168584072 |
| 857 | 6659 | 0.6026960339 | 0.2536301835 |
| 858 | 6661 | 0.6149496110 | 0.2658837606 |
| 859 | 6673 | 0.6884324736 | 0.3393666232 |
| 860 | 6679 | 0.7251491280 | 0.3760832776 |
| 861 | 6689 | 0.7863069224 | 0.4372410720 |
| 862 | 6691 | 0.7985329942 | 0.4494671438 |
| 863 | 6701 | 0.8596359630 | 0.5105701126 |
| 864 | 6703 | 0.8718510845 | 0.5227852341 |
| 865 | 6709 | 0.9084855189 | 0.5594196685 |
| 866 | 6719 | 0.9695065253 | 0.6204406749 |
| 867 | 6733 | 0.0548596976 | 0.2942061528 |
| 868 | 6737 | 0.0792300159 | 0.2698358345 |
| 869 | 6761 | 0.2253002427 | 0.1237656077 |
| 870 | 6763 | 0.2374610503 | 0.1116048001 |
| 871 | 6779 | 0.3346828499 | 0.0143830005 |
| 872 | 6781 | 0.3468275042 | 0.0022383462 |
| 873 | 6791 | 0.4075239283 | 0.0584580779 |
| 874 | 6793 | 0.4196578493 | 0.0705919989 |
| 875 | 6803 | 0.4803006784 | 0.1312348280 |
| 876 | 6823 | 0.6014527717 | 0.2523869213 |
| 877 | 6827 | 0.6256618733 | 0.2765960229 |
| 878 | 6829 | 0.6377637645 | 0.2886979141 |
| 879 | 6833 | 0.6619622317 | 0.3128963813 |
| 880 | 6841 | 0.7103379270 | 0.3612720766 |
| 881 | 6857 | 0.8070045346 | 0.4579386842 |
| 882 | 6863 | 0.8432254321 | 0.4941595817 |
| 883 | 6869 | 0.8794305000 | 0.5303646496 |
| 884 | 6871 | 0.8914953418 | 0.5424294914 |
| 885 | 6883 | 0.9638475482 | 0.6147816978 |
| 886 | 6899 | 0.0602191184 | 0.2888467320 |
| 887 | 6907 | 0.1083629968 | 0.2407028536 |
| 888 | 6911 | 0.1324244805 | 0.2166413699 |
| 889 | 6917 | 0.1685036537 | 0.1805621967 |
| 890 | 6947 | 0.3486652563 | 0.0004005941 |
| 891 | 6949 | 0.3606621855 | 0.0115963351 |
| 892 | 6959 | 0.4206209519 | 0.0715551015 |
| 893 | 6961 | 0.4326075345 | 0.0835416841 |
| 894 | 6967 | 0.4685569541 | 0.1194911037 |
| 895 | 6971 | 0.4925146345 | 0.1434487841 |
| 896 | 6977 | 0.5284382710 | 0.1793724206 |
| 897 | 6983 | 0.5643464643 | 0.2152806139 |
| 898 | 6991 | 0.6122000667 | 0.2631342163 |
| 899 | 6997 | 0.6480723030 | 0.2990064526 |
| 900 | 7001 | 0.6719785830 | 0.3229127326 |
| 901 | 7013 | 0.7436564762 | 0.3945906258 |
| 902 | 7019 | 0.7794724261 | 0.4304065757 |
| 903 | 7027 | 0.8272032219 | 0.4781373715 |
| 904 | 7039 | 0.8987485008 | 0.5496826504 |
| 905 | 7043 | 0.9225833730 | 0.5735175226 |
| 906 | 7057 | 0.0059521701 | 0.3431136803 |
| 907 | 7069 | 0.0773453434 | 0.2717205070 |
| 908 | 7079 | 0.1367933784 | 0.2122724720 |
| 909 | 7103 | 0.2792975766 | 0.0697682738 |
| 910 | 7109 | 0.3148859929 | 0.0341798575 |
| 911 | 7121 | 0.3860177992 | 0.0369519488 |
| 912 | 7127 | 0.4215612270 | 0.0724953766 |
| 913 | 7129 | 0.4334057112 | 0.0843398608 |
| 914 | 7151 | 0.5635855437 | 0.2145196933 |
| 915 | 7159 | 0.6108740057 | 0.2618081553 |
| 916 | 7177 | 0.7171765346 | 0.3681106842 |
| 917 | 7187 | 0.7761758987 | 0.4271100483 |
| 918 | 7193 | 0.8115558164 | 0.4624899660 |
| 919 | 7207 | 0.8940516173 | 0.5449857669 |
| 920 | 7211 | 0.9176071260 | 0.5685412756 |
| 921 | 7213 | 0.9293824303 | 0.5803165799 |
| 922 | 7219 | 0.9646985518 | 0.6156327014 |
| 923 | 7229 | 0.0235261560 | 0.3255396944 |
| 924 | 7237 | 0.0705589496 | 0.2785069008 |
| 925 | 7243 | 0.1058164875 | 0.2432493629 |
| 926 | 7247 | 0.1293134003 | 0.2197524501 |
| 927 | 7253 | 0.1645466142 | 0.1845192362 |
| 928 | 7283 | 0.3404944912 | 0.0085713592 |
| 929 | 7297 | 0.4224794770 | 0.0734136266 |
| 930 | 7307 | 0.4809920392 | 0.1319261888 |
| 931 | 7309 | 0.4926897460 | 0.1436238956 |
| 932 | 7321 | 0.5628424025 | 0.2137765521 |
| 933 | 7331 | 0.6212590424 | 0.2721931920 |
| 934 | 7333 | 0.6329375883 | 0.2838717379 |
| 935 | 7349 | 0.7263086806 | 0.3772428302 |
| 936 | 7351 | 0.7379729175 | 0.3889070671 |
| 937 | 7369 | 0.8428797280 | 0.4938138776 |
| 938 | 7393 | 0.9825563705 | 0.6334905201 |
| 939 | 7411 | 0.0871651293 | 0.2619007211 |
| 940 | 7417 | 0.1220064792 | 0.2270593712 |
| 941 | 7433 | 0.2148479092 | 0.1342179412 |
| 942 | 7451 | 0.3191751582 | 0.0298906922 |
| 943 | 7457 | 0.3539228987 | 0.0048570483 |
| 944 | 7459 | 0.3655023722 | 0.0164365218 |
| 945 | 7477 | 0.4696478540 | 0.1205820036 |
| 946 | 7481 | 0.4927742647 | 0.1437084143 |
| 947 | 7487 | 0.5274522912 | 0.1783864408 |
| 948 | 7489 | 0.5390085453 | 0.1899426949 |
| 949 | 7499 | 0.5967666833 | 0.2477008329 |
| 950 | 7507 | 0.6429454716 | 0.2938796212 |
| 951 | 7517 | 0.7006343691 | 0.3515685187 |
| 952 | 7523 | 0.7352292901 | 0.3861634397 |
| 953 | 7529 | 0.7698104181 | 0.4207445677 |
| 954 | 7537 | 0.8158971618 | 0.4668313114 |
| 955 | 7541 | 0.8389313615 | 0.4898655111 |
| 956 | 7547 | 0.8734712096 | 0.5244053592 |
| 957 | 7549 | 0.8849814410 | 0.5359155906 |
| 958 | 7559 | 0.9425097406 | 0.5934438902 |
| 959 | 7561 | 0.9540108333 | 0.6049449829 |
| 960 | 7573 | 0.0229854694 | 0.3260803810 |
| 961 | 7577 | 0.0459648691 | 0.3031009813 |
| 962 | 7583 | 0.0804225989 | 0.2686432515 |
| 963 | 7589 | 0.1148666991 | 0.2341991513 |
| 964 | 7591 | 0.1263450398 | 0.2227208106 |
| 965 | 7603 | 0.1951833532 | 0.1538824972 |
| 966 | 7607 | 0.2181173839 | 0.1309484665 |
| 967 | 7621 | 0.2983390449 | 0.0507268055 |
| 968 | 7639 | 0.4013729869 | 0.0523071365 |
| 969 | 7643 | 0.4242529279 | 0.0751870775 |
| 970 | 7649 | 0.4585616163 | 0.1094957659 |
| 971 | 7669 | 0.5728268357 | 0.2237609853 |
| 972 | 7673 | 0.5956619930 | 0.2465961426 |
| 973 | 7681 | 0.6413144584 | 0.2922486080 |
| 974 | 7687 | 0.6755382076 | 0.3264723572 |
| 975 | 7691 | 0.6983466207 | 0.3492807703 |
| 976 | 7699 | 0.7439456601 | 0.3948798097 |
| 977 | 7703 | 0.7667362957 | 0.4176704453 |
| 978 | 7717 | 0.8464569576 | 0.4973911072 |
| 979 | 7723 | 0.8806008172 | 0.5315349668 |
| 980 | 7727 | 0.9033560224 | 0.5542901720 |
| 981 | 7741 | 0.9829528943 | 0.6338870439 |
| 982 | 7753 | 0.0511215147 | 0.2979443357 |
| 983 | 7757 | 0.0738326633 | 0.2752331871 |
| 984 | 7759 | 0.0851860417 | 0.2638798087 |
| 985 | 7789 | 0.2553114549 | 0.0937543955 |
| 986 | 7793 | 0.2779700718 | 0.0710957786 |
| 987 | 7817 | 0.4137998279 | 0.0647339775 |
| 988 | 7823 | 0.4477246740 | 0.0986588236 |
| 989 | 7829 | 0.4816365129 | 0.1325706625 |
| 990 | 7841 | 0.5494212291 | 0.2003553787 |
| 991 | 7853 | 0.6171540956 | 0.2680882452 |
| 992 | 7867 | 0.6961103995 | 0.3470445491 |
| 993 | 7873 | 0.7299273075 | 0.3808614571 |
| 994 | 7877 | 0.7524647545 | 0.4033989041 |
| 995 | 7879 | 0.7637313321 | 0.4146654817 |
| 996 | 7883 | 0.7862601983 | 0.4371943479 |
| 997 | 7901 | 0.8875694347 | 0.5385035843 |
| 998 | 7907 | 0.9213135306 | 0.5722476802 |
| 999 | 7919 | 0.9887633356 | 0.6396974852 |
| 1000 | 7927 | 0.0337014843 | 0.3153643661 |
| 1001 | 7933 | 0.0673902166 | 0.2816756338 |
| 1002 | 7937 | 0.0898422942 | 0.2592235562 |
| 1003 | 7949 | 0.1571646027 | 0.1919012477 |
| 1004 | 7951 | 0.1683800458 | 0.1806858046 |
| 1005 | 7963 | 0.2356431030 | 0.1134227474 |
| 1006 | 7993 | 0.4035793467 | 0.0545134963 |
| 1007 | 8009 | 0.4930164873 | 0.1439506369 |
| 1008 | 8011 | 0.5041898461 | 0.1551239957 |
| 1009 | 8017 | 0.5377015564 | 0.1886357060 |
| 1010 | 8039 | 0.6604706657 | 0.3114048153 |
| 1011 | 8053 | 0.7385090137 | 0.3894431633 |
| 1012 | 8059 | 0.7719332531 | 0.4228674027 |
| 1013 | 8069 | 0.8276126812 | 0.4785468308 |
| 1014 | 8081 | 0.8943824719 | 0.5453166215 |
| 1015 | 8087 | 0.9277487764 | 0.5786829260 |
| 1016 | 8089 | 0.9388681272 | 0.5898022768 |
| 1017 | 8093 | 0.9611027056 | 0.6120368552 |
| 1018 | 8101 | 0.0055553841 | 0.3435104663 |
| 1019 | 8111 | 0.0610903776 | 0.2879754728 |
| 1020 | 8117 | 0.0943949422 | 0.2546709082 |
| 1021 | 8123 | 0.1276871999 | 0.2213786505 |
| 1022 | 8147 | 0.2607334338 | 0.0883324166 |
| 1023 | 8161 | 0.3382532486 | 0.0108126018 |

---


## Appendix A. Core Formulas

### A.1 BBP series

$$
\pi = \sum_{k=0}^{\infty} \frac{1}{16^k}
\left(\frac{4}{8k+1} - \frac{2}{8k+4} - \frac{1}{8k+5} - \frac{1}{8k+6}\right).
$$

### A.2 Digit extraction sketch

$$
d_n = \left\lfloor 16\,\{16^n\pi\}\right\rfloor.
$$

### A.3 SILR gate

$$
z_t=\frac{|\hat\alpha_t-\alpha^*|}{SE_t},\quad p_t=\frac{1}{1+e^{-\beta(z_t-z_0)}}.
$$

### A.4 Golden ratio

$$
\varphi=\frac{1+\sqrt{5}}{2}=\lim_{n\to\infty}\frac{F_{n+1}}{F_n}.
$$

### A.5 Fibonacci‑indexed $e$ approximation

$$
e_n=\left(1+\frac{1}{F_n}\right)^{F_n}\to e.
$$

### A.6 Residue grid

$$
r(a,b)=(53+4(a-1)+56(b-1))\bmod 100.
$$

---


## Appendix B. Code

### B.1 Fibonacci and $e_n$ “apples” table (Python)

```python
import math

def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

e = math.exp(1)

for n in range(1, 31):
    Fn = fibonacci(n)
    if Fn == 0:
        continue
    en = (1 + 1 / Fn) ** Fn
    error = abs(en - e)
    print(f"n={n:2d}  F_n={Fn:10d}  e_n={en:.15f}  error={error:.15e}")
```

### B.2 Residue grid generator (Python)

```python
def residue(a, b, seed=53, da=4, db=56, mod=100):
    return (seed + da * (a - 1) + db * (b - 1)) % mod

def print_grid(n=9, mask_sum=10):
    # prints residues as two-digit numbers, masked by a+b<=mask_sum
    for a in range(1, n + 1):
        row = []
        for b in range(1, n + 1):
            if a + b <= mask_sum:
                row.append(f"{residue(a,b):02d}")
            else:
                row.append("  ")
        print(" | ".join(row))

print_grid()
```

### B.3 ASCII projection (Python)

```python
def printable_char(x):
    return chr(x) if 33 <= x <= 126 else " "

def print_ascii(n=9, mask_sum=10):
    for a in range(1, n + 1):
        row = []
        for b in range(1, n + 1):
            if a + b <= mask_sum:
                row.append(printable_char(residue(a,b)))
            else:
                row.append(" ")
        print(" | ".join(row))

print_ascii()
```


## Appendix C. Tables

### C.1 “How about these apples?”: $e_n$ convergence with Fibonacci indices

Below is the provided run (n=1..30). This is a **deterministic convergence trace**: the engine doesn’t need an observer, only a clock (iteration count).

```text
n= 1  F_n=         1  e_n=2.000000000000000  error=7.182818284590451e-01
n= 2  F_n=         1  e_n=2.000000000000000  error=7.182818284590451e-01
n= 3  F_n=         2  e_n=2.250000000000000  error=4.682818284590451e-01
n= 4  F_n=         3  e_n=2.370370370370370  error=3.479114580886753e-01
n= 5  F_n=         5  e_n=2.488319999999999  error=2.299618284590457e-01
n= 6  F_n=         8  e_n=2.565784513950348  error=1.524973145086972e-01
n= 7  F_n=        13  e_n=2.620600887885731  error=9.768094057331433e-02
n= 8  F_n=        21  e_n=2.656263213926108  error=6.201861453293711e-02
n= 9  F_n=        34  e_n=2.679355428095767  error=3.892640036327766e-02
n=10  F_n=        55  e_n=2.693975012347579  error=2.430681611146568e-02
n=11  F_n=        89  e_n=2.703166201602155  error=1.511562685688972e-02
n=12  F_n=       144  e_n=2.708903037186260  error=9.378791272785403e-03
n=13  F_n=       233  e_n=2.712471461041542  error=5.810367417503404e-03
n=14  F_n=       377  e_n=2.714685423841387  error=3.596404617657978e-03
n=15  F_n=       610  e_n=2.716057071606022  error=2.224756853023369e-03
n=16  F_n=       987  e_n=2.716906063671805  error=1.375764787240552e-03
n=17  F_n=      1597  e_n=2.717431257862638  error=8.505705964072519e-04
n=18  F_n=      2584  e_n=2.717756031654547  error=5.257968044980466e-04
n=19  F_n=      4181  e_n=2.717956824154195  error=3.250043048499407e-04
n=20  F_n=      6765  e_n=2.718080947932234  error=2.008805268114422e-04
n=21  F_n=     10946  e_n=2.718157671040231  error=1.241574188139971e-04
n=22  F_n=     17711  e_n=2.718205092503898  error=7.673595514745557e-05
n=23  F_n=     28657  e_n=2.718234402089590  error=4.742636945520573e-05
n=24  F_n=     46368  e_n=2.718252516987778  error=2.931147126750133e-05
n=25  F_n=     75025  e_n=2.718263712838378  error=1.811562066666994e-05
n=26  F_n=    121393  e_n=2.718270632302497  error=1.119615654854300e-05
n=27  F_n=    196418  e_n=2.718274908848518  error=6.919610527233999e-06
n=28  F_n=    317811  e_n=2.718277551933405  error=4.276525639834716e-06
n=29  F_n=    514229  e_n=2.718279185283449  error=2.643175596173108e-06
n=30  F_n=    832040  e_n=2.718280194740024  error=1.633719021398861e-06
```

### C.2 Residue grid (9×9, mask $a+b\le 10$) residues

```text
53 | 09 | 65 | 21 | 77 | 33 | 89 | 45 | 01
57 | 13 | 69 | 25 | 81 | 37 | 93 | 49 |
61 | 17 | 73 | 29 | 85 | 41 | 97 |
65 | 21 | 77 | 33 | 89 | 45 |
69 | 25 | 81 | 37 | 93 |
73 | 29 | 85 | 41 |
77 | 33 | 89 |
81 | 37 |
85
```


---
## Appendix D. Source Notes (included for traceability)

These sections are imported from the working Nexus notes you supplied; they preserve phrasing and checkpoints so the paper remains “operational.”


### D.19 Excerpt from `Nexus_Engine_First_BBP_SILR_v3_with_Grid.md`

```text
# Nexus Notes v3: Engine-First Mathematics (BBP, π, SILR, e↔φ, and the +4/+56 Grid)

**Purpose.** This is the “engine first, name later” version:  
rules run; traces appear; *labels* come later. We keep the Nexus language (gap / fold / resonance / gate), but the math stays standard.

---

## 0) Two truths that can both be true

1. **Observerless computation is real.** A rule can run without anyone *recognizing* the output.
2. **Mathematical identity is also real.** A representation can equal a number *as an identity* even if the rule “doesn’t know the name”.

Those aren’t opposites. They’re different layers:
- **Engine layer:** “this recurrence / series / map produces a trace.”
- **Naming layer:** “this trace matches what we call π / e / etc.”

---

## 1) e↔φ via Fibonacci-indexed “breath”: why $e_n = (1 + 1/F_n)^{F_n} \to e$

### 1.1 Definitions

Fibonacci numbers:
$$
F_0 = 0,\quad F_1 = 1,\quad F_n = F_{n-1} + F_{n-2}\quad (n\ge 2).
$$

Define the “breath” approximation:
$$
e_n := \left(1 + \frac{1}{F_n}\right)^{F_n}.
$$

Claim:
$$
\lim_{n\to\infty} e_n = e.
$$

### 1.2 Why the limit holds (clean proof)

A standard theorem is:
$$
\lim_{m\to\infty}\left(1+\frac{1}{m}\right)^m = e.
$$

This limit holds for **any** integer sequence $m_n\to\infty$ (it does not need to be $m=n$).  
So it’s enough to show $F_n \to \infty$ (true), then substitute $m_n = F_n$:
$$
\lim_{n\to\infty}\left(1+\frac{1}{F_n}\right)^{F_n}
=
\lim_{m\to\infty}\left(1+\frac{1}{m}\right)^m
= e.
$$

That’s it.

### 1.3 The φ coupling is in the *rate* (this is the useful part)

Binet’s formula:
$$
F_n = \frac{\varphi^n - \psi^n}{\sqrt{5}}, \quad \varphi = \frac{1+\sqrt{5}}{2}, \quad \psi = \frac{1-\sqrt{5}}{2} = -\frac{1}{\varphi}.
$$

So for large $n$:
$$
F_n \sim \frac{\varphi^n}{\sqrt{5}}.
$$

Now use the log expansion:
$$
\ln\left(1+\frac{1}{m}\right) = \frac{1}{m} - \frac{1}{2m^2} + O\left(\frac{1}{m^3}\right).
$$

Multiply by $m$:
$$
m\ln\left(1+\frac{1}{m}\right) = 1 - \frac{1}{2m} + O\left(\frac{1}{m^2}\right).
$$

Exponentiate:
$$
\left(1+\frac{1}{m}\right)^m
= e\,\exp\left(-\frac{1}{2m} + O\left(\frac{1}{m^2}\right)\right)
= e\left(1 - \frac{1}{2m} + O\left(\frac{1}{m^2}\right)\right).
$$

So the error behaves like:
$$
\left|e - \left(1+\frac{1}{m}\right)^m\right| \approx \frac{e}{2m}.
$$

Substitute $m=F_n$:
$$
|e - e_n| \approx \frac{e}{2F_n}
\sim
\frac{e\sqrt{5}}{2}\,\varphi^{-n}.
$$

**This is the real “e↔φ echo”:** φ controls the growth of $F_n$, which controls the decay of the $e_n$ error.

---

## 2) “Do you like apples?” — the convergence dump (n=1..30)

Below is the exact numeric dump you provided (kept verbatim).

```text
n= 1  F_n=         1  e_n=2.000000000000000  error=7.182818284590451e-01
n= 2  F_n=         1  e_n=2.000000000000000  error=7.182818284590451e-01
n= 3  F_n=         2  e_n=2.250000000000000  error=4.682818284590451e-01
n= 4  F_n=         3  e_n=2.370370370370370  error=3.479114580886753e-01
n= 5  F_n=         5  e_n=2.488319999999999  error=2.299618284590457e-01
n= 6  F_n=         8  e_n=2.565784513950348  error=1.524973145086972e-01
n= 7  F_n=        13  e_n=2.620600887885731  error=9.768094057331433e-02
n= 8  F_n=        21  e_n=2.656263213926108  error=6.201861453293711e-02
n= 9  F_n=        34  e_n=2.679355428095767  error=3.892640036327766e-02
n=10  F_n=        55  e_n=2.693975012347579  error=2.430681611146568e-02
n=11  F_n=        89  e_n=2.703166201602155  error=1.511562685688972e-02
n=12  F_n=       144  e_n=2.708903037186260  error=9.378791272785403e-03
n=13  F_n=       233  e_n=2.712471461041542  error=5.810367417503404e-03
n=14  F_n=       377  e_n=2.714685423841387  error=3.596404617657978e-03
n=15  F_n=       610  e_n=2.716057071606022  error=2.224756853023369e-03
n=16  F_n=       987  e_n=2.716906063671805  error=1.375764787240552e-03
n=17  F_n=      1597  e_n=2.717431257862638  error=8.505705964072519e-04
n=18  F_n=      2584  e_n=2.717756031654547  error=5.257968044980466e-04
n=19  F_n=      4181  e_n=2.717956824154195  error=3.250043048499407e-04
n=20  F_n=      6765  e_n=2.718080947932234  error=2.008805268114422e-04
n=21  F_n=     10946  e_n=2.718157671040231  error=1.241574188139971e-04
n=22  F_n=     17711  e_n=2.718205092503898  error=7.673595514745557e-05
n=23  F_n=     28657  e_n=2.718234402089590  error=4.742636945520573e-05
n=24  F_n=     46368  e_n=2.718252516987778  error=2.931147126750133e-05
n=25  F_n=     75025  e_n=2.718263712838378  error=1.811562066666994e-05
n=26  F_n=    121393  e_n=2.718270632302497  error=1.119615654854300e-05
n=27  F_n=    196418  e_n=2.718274908848518  error=6.919610527233999e-06
n=28  F_n=    317811  e_n=2.718277551933405  error=4.276525639834716e-06
n=29  F_n=    514229  e_n=2.718279185283449  error=2.643175596173108e-06
n=30  F_n=    832040  e_n=2.718280194740024  error=1.633719021398861e-06
```

---

## 3) The +4/+56 residue grid: “hash-look” from a dead-simple affine rule

### 3.1 The rule (2D affine map mod $M$)

Define a residue field on integer coordinates $(a,b)$:

$$
r(a,b) = \big(s + \Delta_a(a-1) + \Delta_b(b-1)\big) \bmod M.
$$

For your grid:
- seed $s=53$
- vertical step $\Delta_a = 4$
- horizontal step $\Delta_b = 56$
- modulus $M=100$ (in the version you showed)

So:
$$
r(a,b) = \big(53 + 4(a-1) + 56(b-1)\big)\bmod 100.
$$

This is **not random**. It’s deterministic. It only looks hash-y because modular wrap + projection scrambles perception.

### 3.2 The “visibility window” is the gate (SILR-style)

A clean way to express the triangle window is:
$$
\text{show cell }(a,b)\ \text{iff } a+b \le K.
$$

That’s a literal gate. Same underlying field; different *projection*.

### 3.3 Why it’s good Nexus material

- It shows **frame rotation**: “random” becomes “obvious” once you spot steps.
- It shows **gate dependence**: meaning appears in a band, disappears outside it.
- It shows **observerless compute**: the residue field exists independent of the label “ASCII”.

### 3.4 Minimal code to reproduce

```python
def residue(a, b, seed=53, da=4, db=56, mod=100):
    return (seed + da*(a-1) + db*(b-1)) % mod

def gate(a, b, K=10):
    return (a + b) <= K

def printable_mod100(r):
    # For mod=100, r is 0..99, so "printable ASCII" really means 33..99
    return 33 <= r <= 99
```

---

## 4) The π/H story about 56: what’s real, what’s not, and what to test

You pasted a claim from Grok:

- $56 = 16\times 3.5$  
- interpret $16$ as “hex base”  
- interpret $3.5=7/2$ as “rough π”  
```


### D.20 Excerpt from `corrected_residue_grid_fibonacci_e_bbp.md`

```text
# Deterministic Residue Grids, Fibonacci–\(e\) Error, and BBP \(\pi\) Hex Synthesis  
*(Corrected, expanded, and formula-complete — Markdown + LaTeX)*

---

## Executive statement

This document consolidates and **corrects** three interlocked claims:

1. A 2D “random-looking” grid is generated by a **deterministic affine residue rule** with steps \(+4\) and \(+56\) from seed \(53\), with a triangular visibility window \(a+b\le N\).
2. A Fibonacci-indexed approximation \(e_N\) yields an error near \(1.6\times 10^{-6}\); this error is **not** “close to \(\varphi\)” as a number, but it **does** scale with \(\varphi\) through Fibonacci growth.
3. The BBP series supports extracting hexadecimal digits of \(\pi\) without computing all prior digits; convergence is guaranteed, but **normality** of \(\pi\) remains unproven.

Throughout, math statements are provided with precise inline \($\cdot$\) and block \($$\cdot$$\) tags.

---

## Part I — Residue grid generator (seed \(53\), steps \(+4\), \(+56\), modulus \(100\))

### 1. Indexing and generator

Let \(a,b\in\mathbb{Z}_{\ge 1}\) index a 2D grid. Define the residue:

$$
r(a,b)=\bigl(53 + 4(a-1) + 56(b-1)\bigr)\bmod 100.
$$

Interpretation:

- Moving “down” (increment \(a\)) adds \(4\).
- Moving “right” (increment \(b\)) adds \(56\).
- The modulus \(100\) enforces wrap-around in \(\{0,1,\dots,99\}\).

Because \(56=14\cdot 4\), the generator can be factored:

$$
r(a,b)=\bigl(53 + 4\,t(a,b)\bigr)\bmod 100,
\qquad
t(a,b)=(a-1)+14(b-1).
$$

This is a structural reduction: the 2D grid is an embedding of a **1D congruential walk** in the index \(t\).

---

### 2. Reachability constraints (why it *cannot* be “full scramble” mod 100)

Let \(M=100\). Since

$$
\gcd(4,100)=4
\quad\text{and}\quad
\gcd(56,100)=4,
$$

every increment is a multiple of \(4\), hence every residue is locked to a single congruence class modulo \(4\):

$$
r(a,b)\equiv 53\pmod 4.
$$

Because \(53\equiv 1\pmod 4\), it follows that

$$
r(a,b)\in\{1,5,9,\dots,97\}.
$$

Therefore the grid can hit **only 25 values** (not all 100). More formally, since

$$
r(a,b)=\bigl(53+4t\bigr)\bmod 100,
$$

and \(4\cdot 25=100\), the period in \(t\) is:

$$
t\mapsto t+25\quad\Rightarrow\quad r\text{ repeats}.
$$

So the reachable set size is:

$$
\#\{r(a,b)\}=\frac{100}{\gcd(100,4)}=25.
$$

**Correction note:** Any statement implying “coprime scrambling” for \(+4\) and \(+56\) mod \(100\) is false.

---

### 3. Visibility window (triangular band)

If you impose the triangular constraint

$$
a+b\le N,
$$

with \(a,b\ge 1\), the number of visible cells is:

$$
V(N)=\sum_{s=2}^N (s-1)=\frac{N(N-1)}{2}.
$$

Example: for \(N=10\),

$$
V(10)=\frac{10\cdot 9}{2}=45.
$$

If your *total* candidate-cell count is \(T\) (e.g., by embedding in a larger grid, or including blanked regions), the visibility ratio is

$$
\rho=\frac{V}{T}.
$$

One cited ratio is \(45/129\):

$$
\frac{45}{129}\approx 0.3488372093023256.
$$

Compare this to \(H=\pi/9\):

$$
H=\frac{\pi}{9}\approx 0.3490658503988659,
\qquad
\Delta = H-\frac{45}{129}\approx 0.0002286410965403.
$$

This refines “\(\Delta\approx 0.0003\)” into an explicit value.

---

### 4. Corrected “\(\pi\) echo” statement for the 14 ratio

The step ratio is:

$$
\frac{56}{4}=14.
$$

But

$$
14-\pi\approx 10.8584073464,
$$

so the small difference near \(0.358\) does **not** come from \(14-\pi\).

If you intended the quartered ratio \(14/4\), then:

$$
\frac{14}{4}-\pi = 3.5-\pi \approx 0.3584073464102069.
$$

This is the correct source of the \(\approx 0.3584\) quantity.

---

### 5. ASCII mapping (important modulus consequence)

If you map residues to ASCII, note:

- Mod \(100\) produces residues only in \(0\)–\(99\).
- The “printable ASCII” window \(33\)–\(126\) cannot be fully represented, because \(100\)–\(126\) are unreachable under \(\bmod 100\).

So for \(\bmod 100\), the printable set is at most:

$$
33\le r\le 99.
$$

If you want the full printable range \(33\)–\(126\), use a larger modulus such as \(256\) and then gate:

$$
r_{256}(a,b)=\bigl(53+4(a-1)+56(b-1)\bigr)\bmod 256,
$$

and display glyphs only when

$$
33\le r_{256}\le 126.
$$

---

### 6. General form (portability)

A general affine 2D residue field is:

$$
r(a,b)=(s + u(a-1) + v(b-1))\bmod M.
$$

A necessary condition to reach all \(M\) residues is:

$$
\gcd(u,v,M)=1.
$$

```


### D.21 Excerpt from `residue_grid_affine_lattice_corrections.md`

```text
# Residue Grid: Affine Modular Lattice (Corrected) — plus Fibonacci–$e$ and BBP context

This document consolidates and corrects the key claims about the “53-seed” residue grid and its interpretation. It also clarifies the separate Fibonacci–$e$ numeric check and the BBP (Bailey–Borwein–Plouffe) $\pi$-hex digit extractor context.

---

## 1) The grid definition (what is being generated)

We define a 2D residue field over integer coordinates $(a,b)$ using:

$$
R(a,b) \equiv \left(s + u(a-1) + v(b-1)\right) \bmod m
$$

with the concrete parameters:

- seed $s = 53$
- vertical step $u = 4$ (increment when $a \mapsto a+1$)
- horizontal step $v = 56$ (increment when $b \mapsto b+1$)
- modulus $m = 100$

So explicitly:

$$
R(a,b) \equiv \left(53 + 4(a-1) + 56(b-1)\right) \bmod 100.
$$

A common “visibility mask” used in the demo is:

$$
a+b \le 10
$$

which crops the infinite periodic lattice to a finite triangular window.

### Vector form (useful for reasoning)

Let $\Delta = \begin{bmatrix}a-1\\ b-1\end{bmatrix}$ and $w = \begin{bmatrix}u\\ v\end{bmatrix}$. Then

$$
R(a,b) \equiv (s + w^\top \Delta) \bmod m.
$$

This is an **affine linear form modulo $m$**—a modular lattice.

---

## 2) Correction: this is not a “true LCG” in the recursive sense

A standard (1D) linear congruential generator (LCG) is a **recurrence**:

$$
X_{n+1} \equiv (A X_n + C) \bmod m.
$$

The grid formula above **does not** depend on $R(a,b)$ to produce the next value. It is **direct evaluation** of a linear form in $(a,b)$.

### What is true (and still useful)

Along any straight path where you increment one coordinate by $1$ each step, the values *do* follow a simple modular recurrence—specifically an **additive congruential generator** (the special case $A=1$):

- Moving right: $(a,b)\mapsto(a,b+1)$
  $$
  R(a,b+1) \equiv R(a,b) + v \pmod m
  $$

- Moving down: $(a,b)\mapsto(a+1,b)$
  $$
  R(a+1,b) \equiv R(a,b) + u \pmod m
  $$

So: **the grid is an affine modular lattice; each row/column is an additive congruential sequence.** Calling it “LCG-like” is fine as intuition, but the mathematically precise label is:

> **2D affine congruential map** (linear form modulo $m$), with 1D additive congruential sequences along coordinate directions.

---

## 3) Period and reachable values (the key modular facts)

### 3.1 Axis periods

The period of repeated stepping by $k$ mod $m$ is:

$$
\text{period}(k;m) = \frac{m}{\gcd(k,m)}.
$$

Here:

- $\gcd(u,m) = \gcd(4,100) = 4$  
  $$
  \Rightarrow \text{period}(u;m) = \frac{100}{\gcd(u,m)} = 25
  $$

- $\gcd(v,m) = \gcd(56,100) = 4$  
  $$
  \Rightarrow \text{period}(v;m) = \frac{100}{\gcd(v,m)} = 25
  $$

So every fixed row repeats every $\text{period}(v;m)=25$ steps in $b$, and every fixed column repeats every $\text{period}(u;m)=25$ steps in $a$.

Equivalently:

$$
R(a+25,b) = R(a,b), \qquad R(a,b+25) = R(a,b).
$$

### 3.2 Only 25 distinct residues exist (global constraint)

Since both increments are multiples of $\gcd(u,v,m)=4$, we have:

$$
u(a-1) + v(b-1) \equiv 0 \pmod 4
$$

which implies:

$$
R(a,b) \equiv s \pmod 4.
$$

Because $s=53\equiv 1\pmod 4$, the grid can only ever hit residues congruent to 1 modulo $4$. That means **exactly $100/4 = 25$ residues are reachable** in the entire infinite grid.

This corrects any claim that the grid “scrambles across all 00–99.” It cannot; it lives on a 25-value coset.

---

## 4) Correction: row-major traversal is not a standard LCG

A claim like “if you traverse row-major it becomes a standard LCG with a combined step” is generally **false**.

If a row has width $W$, a row-major index $n$ maps to:

$$
a = \left\lfloor \frac{n}{W} \right\rfloor + 1, \qquad b = (n \bmod W) + 1.
$$

Substituting into the grid formula gives a **piecewise** expression involving both $\left\lfloor n/W\right\rfloor$ and $(n\bmod W)$:

$$
R(n) \equiv \left(s + u\left\lfloor \frac{n}{W} \right\rfloor + v(n \bmod W)\right) \bmod m,
$$

which is not of the LCG form $R(n+1)=AR(n)+C \bmod m$ with constant $A,C$.

If you want a true 1D recurrence, pick a **path with constant step vector** (e.g., diagonal). Example: along $(a,b)\mapsto(a+1,b+1)$, the step is $(u+v)\bmod m = (4+56)\bmod 100 = 60$:

$$
R(a+1,b+1) \equiv R(a,b) + (u+v) \pmod m.
$$

That is still additive (not multiplicative), and its period is:

$$
\frac{m}{\gcd(u+v,m)} = \frac{100}{\gcd(60,100)} = 5.
$$

So the diagonal repeats very quickly—another reason to avoid calling this “hash-like” without qualifiers.

---

## 5) Why it *looks* random in the cropped view

Even though the structure is linear, it can look “noisy” when:

1. You view only a small crop (e.g., $a+b\le 10$) rather than a full period tile.
2. You map values into a **nonlinear display predicate**, e.g. “print only when printable ASCII.”

A typical predicate for ASCII visibility is:

$$
\text{visible}(a,b) =
\begin{cases}
1,& 33 \le R(a,b) \le 126\\
0,& \text{otherwise}
\end{cases}
$$

This turns a smooth modular lattice into a **thresholded point field**, which can visually resemble “random scattering.” The “chaos” is in the *masking*, not in the generator.

### Correction on the “45/129” ratio

For the common $9\times 9$ window with mask $a+b\le 10$, the number of included cells is:

$$
\sum_{a=1}^{9} (10-a) = 45.
$$

If the underlying uncropped window is $9\times 9$, the total is $81$, so the ratio is:

$$
\frac{45}{81} = 0.555\ldots
$$

So the specific ratio $45/129\approx 0.3488$ cannot describe a $9\times 9$ crop. If “129” is a different denominator (e.g., a multi-layer count), it must be defined explicitly; otherwise it is inconsistent.

---

## 6) Correction: the $56/4$ “$\pi$-closeness” claim

```


### D.22 Excerpt from `residue_grid_period_and_classification_corrected.md`

```text
# Residue Grid: Corrected Algebra, Period, and Generator Classification

This note corrects two specific claims that commonly get mixed together:

1. **The grid generator is not an LCG in the usual sense** (it is an *additive/affine congruential* rule; if you insist on “LCG,” the multiplier is $1$).
2. **The “irrational-ish” ratio claim is incorrect**: $56/4 = 14$ is an integer; the apparent scrambling comes from modular reduction to $\mathbb{Z}_{25}$ where the step $14$ is a *unit* (invertible) and therefore permutes the residue class.

It also gives the precise **period** statements and a clean reduced form.

---

## 1. Definition (the actual generator)

You defined the grid value at integer coordinates $(a,b)$ as:

$$
r(a,b) \equiv 53 + 4(a-1) + 56(b-1) \pmod{100}.
$$

This is an **affine map** on the lattice $\mathbb{Z}^2 \to \mathbb{Z}_{100}$.

A useful factorization is:

$$
r(a,b) \equiv 53 + 4\big((a-1) + 14(b-1)\big) \pmod{100},
$$

since $56 = 4\cdot 14$.

---

## 2. Invariant class (why only 25 outputs exist)

Because $4(a-1)$ and $56(b-1)$ are multiples of $4$, the residue is locked to a single congruence class modulo $4$:

$$
r(a,b) \equiv 53 \equiv 1 \pmod 4.
$$

So **the grid can only ever hit the 25 values**
$$
\{1,5,9,\ldots,97\} \subset \mathbb{Z}_{100}.
$$

That is already enough to guarantee many repeats in any window larger than 25 cells (by pigeonhole).

---

## 3. Reduced coordinate: collapse to $\mathbb{Z}_{25}$

Since every value satisfies $r \equiv 1 \pmod 4$, write:

$$
r(a,b) = 1 + 4t(a,b),
$$

where $t(a,b) \in \mathbb{Z}_{25}$.

Compute $t$ by dividing out the factor 4:

$$
t(a,b) \equiv \frac{r(a,b)-1}{4} \pmod{25}.
$$

Substituting the definition of $r$:

$$
t(a,b) \equiv \frac{53-1}{4} + (a-1) + 14(b-1) \pmod{25}.
$$

Since $(53-1)/4 = 13$:

$$
t(a,b) \equiv 13 + (a-1) + 14(b-1) \pmod{25}.
$$

Equivalently:

$$
t(a,b) \equiv a + 14b - 2 \pmod{25}.
$$

This is the cleanest “truth form.” Everything else is display-layer.

---

## 4. Period (the exact statement)

The rule is additive in each coordinate, so the period is computed by the additive congruence fact:

> For $x_{n+1} = x_n + k \pmod m$, the period is $m/\gcd(k,m)$.

### Along the $a$ direction (vertical)

Fix $b$ and increment $a \mapsto a+1$:

$$
r(a+1,b) \equiv r(a,b) + 4 \pmod{100}.
$$

So the vertical period is:

$$
\frac{100}{\gcd(4,100)} = \frac{100}{4} = 25.
$$

### Along the $b$ direction (horizontal)

Fix $a$ and increment $b \mapsto b+1$:

$$
r(a,b+1) \equiv r(a,b) + 56 \pmod{100}.
$$

So the horizontal period is:

$$
\frac{100}{\gcd(56,100)} = \frac{100}{4} = 25.
$$

### 2D periodicity

Therefore the full function is periodic in both axes:

$$
r(a+25,b) = r(a,b), \quad r(a,b+25) = r(a,b).
$$

So a fundamental repeating domain is **a $25\times 25$ tile**.

---

## 5. Why it “looks random” in small windows (correct explanation)

The key point is *not* “irrational-ish ratios.” The ratio

$$
\frac{56}{4} = 14
$$

is exactly an integer.

The actual scrambling mechanism is visible in the reduced form over $\mathbb{Z}_{25}$:

- stepping $a$ adds $+1$ to $t$,
- stepping $b$ adds $+14$ to $t$.

Since

$$
\gcd(14,25) = 1,
$$

the step $+14$ generates a **full 25-cycle** in the additive group $\mathbb{Z}_{25}$.

So within a small cropped window (like your $a+b\le 10$ triangle), you see a **permutation-like jump** through the 25 allowed values. That is exactly the “pseudorandom” illusion: deterministic, linear, but well-mixed relative to the small viewport.

---

## 6. Window facts (your $a+b\le 10$ crop)

If you take $a,b\in\{1,\ldots,9\}$ with the constraint $a+b\le 10$, you get:

- **45 visible cells**
- **24 distinct residues** in that crop

The missing value from the full 25-value class is **5** (it first appears at $(a,b)=(1,18)$, outside your crop).

---

## 7. Classification: LCG vs affine/additive generator (corrected)

A standard **LCG** is:

$$
X_{n+1} \equiv (A X_n + C) \pmod m.
$$

Your grid does **not** use multiplication by the prior state; it is a direct affine mapping from $(a,b)$ into $\mathbb{Z}_{100}$.

If you force it into LCG form *along a line*, it is the special case $A=1$:

$$
X_{n+1} \equiv X_n + k \pmod m,
$$

which is best described as an **additive congruential generator** (still deterministic; still periodic; still linear—just simpler than a true LCG).

Also, the “full period” conditions you quoted (Hull–Dobell theorem) apply to the general multiplicative LCG; they are **not the right tool** for the purely additive step you are using here. For additive steps, the period is exactly $m/\gcd(k,m)$.

---

## 8. Separate correction: “error close to $\varphi$” (it is not)

You cited:

- $n=30$
- $F_n = 832040$
- $e_n = 2.718280194740024$
- absolute error $\varepsilon = 1.633719021398861\times 10^{-6}$
```


### D.23 Excerpt from `Nexus_e_phi_apples_convergence.md`

```text
# NEXUS ADDENDUM — *e* via Fibonacci Indices (φ-Driven Convergence)
**Δ-fold / ⊕-resonance / ↻-reflection**  
*(“Do you like apples? How about these apples?”)*

---

## 0. What this is (engine-first, observer-last)
We define an **observerless computation** that *runs* regardless of whether anyone recognizes the output:

- Fibonacci recursion generates an index ladder.
- A canonical exponential limit runs on that ladder.
- The output approaches **$e$** with a rate governed by **$\varphi$**.

Nothing here requires naming the limit “$e$” in order for the convergence to occur.

---

## 1. Definitions (the moving parts)

### Fibonacci engine
We use the Fibonacci numbers $(F_n)_{n\ge 0}$:

$$
F_0 = 0,\quad F_1 = 1,\quad F_n = F_{n-1} + F_{n-2}\ \ (n\ge 2).
$$

### The exponential breath on the ladder
Define the sequence:

$$
e_n \;=\; \left(1+\frac{1}{F_n}\right)^{F_n}\quad (n\ge 2,\ F_n\neq 0).
$$

### Golden steering ratio
The golden ratio is

$$
\varphi = \frac{1+\sqrt{5}}{2},
$$

and the Fibonacci ratios converge:

$$
\lim_{n\to\infty}\frac{F_{n+1}}{F_n} = \varphi.
$$

---

## 2. Convergence theorem (the simple proof)

### Step A — $F_n\to\infty$
From recursion and positivity: for $n\ge 2$, $F_n$ is increasing and unbounded.  
A quick growth bound (no closed form needed):

$$
F_{k+2} = F_{k+1}+F_k \ge 2F_k,
$$

so every two steps the sequence at least doubles, hence $F_n\to\infty$.

### Step B — the classic limit
A standard fact:

$$
\lim_{m\to\infty}\left(1+\frac{1}{m}\right)^m = e.
$$

### Step C — substitute $m=F_n$
Since $F_n\to\infty$, we can take $m_n=F_n$ and compose limits:

$$
\lim_{n\to\infty} e_n
=\lim_{n\to\infty}\left(1+\frac{1}{F_n}\right)^{F_n}
=\lim_{m\to\infty}\left(1+\frac{1}{m}\right)^m
=e.
$$

**Conclusion:**  
$$
e_n \to e \quad\text{as}\quad n\to\infty.
$$

---

## 3. Log expansion (kinetic view in math space)

Take logs:

$$
\ln e_n = F_n\ln\left(1+\frac{1}{F_n}\right).
$$

Use the series (for $|x|<1$):

$$
\ln(1+x)=x-\frac{x^2}{2}+\frac{x^3}{3}-\frac{x^4}{4}+\cdots
$$

with $x=\frac{1}{F_n}$:

$$
\ln e_n
=F_n\left(\frac{1}{F_n}-\frac{1}{2F_n^2}+\frac{1}{3F_n^3}-\cdots\right)
=1-\frac{1}{2F_n}+\frac{1}{3F_n^2}-\frac{1}{4F_n^3}+\cdots
\to 1.
$$

Exponentiate:

$$
e_n=\exp(\ln e_n)\to \exp(1)=e.
$$

This also shows the **shape** of the drift:

$$
\ln e_n = 1 - \frac{1}{2F_n} + O\!\left(\frac{1}{F_n^2}\right).
$$

---

## 4. Practical error bound (usable, not mystical)

A useful inequality (for $x>0$):

$$
x-\frac{x^2}{2}\ \le\ \ln(1+x)\ \le\ x-\frac{x^2}{2}+\frac{x^3}{3}.
$$

Let $x=\frac{1}{m}$ and multiply by $m$:

$$
1-\frac{1}{2m}\ \le\ m\ln\left(1+\frac{1}{m}\right)\ \le\ 1-\frac{1}{2m}+\frac{1}{3m^2}.
$$

Exponentiating gives:

$$
e\cdot e^{-\,\frac{1}{2m}}
\ \le\
\left(1+\frac{1}{m}\right)^m
\ \le\
e\cdot e^{-\,\frac{1}{2m}+\frac{1}{3m^2}}.
$$

So for $m$ large, the first-order error is sharp:

$$
e-\left(1+\frac{1}{m}\right)^m \approx \frac{e}{2m}.
$$

Substitute $m=F_n$:

$$
e-e_n \approx \frac{e}{2F_n}.
$$

---

## 5. Where φ enters (rate in **n**, not in **m**)

Binet (asymptotic form):

$$
F_n \sim \frac{\varphi^n}{\sqrt{5}}.
$$

Combine with $e-e_n \approx \frac{e}{2F_n}$:

$$
e-e_n \sim \frac{e}{2}\cdot \frac{\sqrt{5}}{\varphi^n}
=\left(\frac{e\sqrt{5}}{2}\right)\varphi^{-n}.
$$

So the error decays **exponentially in $n$**, with base $\varphi$:

$$
|e-e_n| = \Theta(\varphi^{-n}).
$$

That’s the “stacked echo”: **φ drives the ladder growth, ladder growth drives the breath convergence.**

---

## 6. 🍏 “Do you like apples? How about these apples?” (your computed run)

Below is the numeric trace you provided (kept verbatim).  
It shows the monotone approach from below toward $e=\exp(1)$.

```text
n= 1  F_n=         1  e_n=2.000000000000000  error=7.182818284590451e-01
n= 2  F_n=         1  e_n=2.000000000000000  error=7.182818284590451e-01
n= 3  F_n=         2  e_n=2.250000000000000  error=4.682818284590451e-01
n= 4  F_n=         3  e_n=2.370370370370370  error=3.479114580886753e-01
n= 5  F_n=         5  e_n=2.488319999999999  error=2.299618284590457e-01
n= 6  F_n=         8  e_n=2.565784513950348  error=1.524973145086972e-01
n= 7  F_n=        13  e_n=2.620600887885731  error=9.768094057331433e-02
n= 8  F_n=        21  e_n=2.656263213926108  error=6.201861453293711e-02
n= 9  F_n=        34  e_n=2.679355428095767  error=3.892640036327766e-02
n=10  F_n=        55  e_n=2.693975012347579  error=2.430681611146568e-02
```

