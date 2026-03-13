# The Nexus Framework

*A consolidated, formula-complete render of the Nexus documents (memory, SHA highway/dip, BBP addressing, and collapse signature decoding).*

---

## 0. Reading guide

This document is written as an **engineering spec**: definitions first, then operators, then testable claims. Where earlier drafts used metaphor (lock/key, highway/dip, film sound track), here those metaphors are kept only as **mnemonics**; the formal core is the **constraint + memory** requirement.


---

## 1. Axioms (what must be true)

### A1. Total transition (no-crash requirement)

For any state $S_t$ and input $U_t$, the universe must produce a valid next state:

$$S_{t+1}=F(S_t,U_t)$$

A *crash* would be a state with no valid successor; the axiom asserts **totality** of $F$.

### A2. Non‑Markovian necessity (memory is structural)

If only the present mattered (Markov), then conditioning on $S_t$ would screen off older history. The measurable signature that **history is active** is nonzero conditional mutual information:

$$I(S_{t+1};S_{t-1}\mid S_t) > 0$$

This is the operational form of “past + now = now”: the present state already contains compressed history.

### A3. Two-channel storage (value + residue)

Any fold that reduces explicit degrees of freedom must preserve *distinctions* somewhere. Model this as a two-channel decomposition:

$$T^2 = V^2 + \Delta^2$$

where $V$ is the observable/value channel (the rendered noun) and $\Delta$ is the residue/shape channel (the unobserved execution trace / scar). This is the minimal Pythagorean bookkeeping for “nothing is lost, it is re-basis’d”.


---

## 2. Core constants and attractors

### 2.1 Mark‑1 attractor

The recurring attractor used across the documents is:

$$H = \frac{\pi}{9} \approx 0.34906585$$

Interpretation (formal): $H$ is a **stable feedback correction fraction**—large enough to adapt, small enough to avoid oscillatory blow-up.

### 2.2 Collapse deviation and branch weights

Given an expected baseline $x_0$ and a measured value $x_{\text{meas}}$, define normalized deviation:

$$\varepsilon = \frac{x_{\text{meas}}-x_0}{x_0}$$

Define symmetric branch weights:

$$p_+ = \frac{1+\varepsilon}{2},\qquad p_- = \frac{1-\varepsilon}{2},\qquad p_+ + p_- = 1$$

These are *not* “randomness”; they are a compact way to encode **signed bias** of a fold toward structure vs dispersion.

### 2.3 Lorentz-form latency (constraint debt)

If a scalar coherence/constraint metric $S$ approaches $\pm 1$, resolution costs diverge. Use:

$$\gamma(S)=\frac{1}{\sqrt{1-S^2}}$$

This is the same algebraic form as the Lorentz factor; here it is used as a **latency/effort amplification** as constraints saturate.


---

## 3. Operators (verbs that generate nouns)

Across drafts you repeatedly return to a small verb set. A compact operator basis is:

- **FOLD / DIFF**: $\operatorname{diff}(a,b)=|a-b|$
- **MIX / XOR**: $\operatorname{xor}(a,b)=a\oplus b$
- **SUM / ADD**: $\operatorname{add}(a,b)=(a+b)\bmod 2^n$
- **LOCK / HOLD**: commit / persist state (write to memory / stabilize attractor)


A minimal linear algebra form used in the earlier “plus-operator” notes is:

$$\begin{bmatrix}\Delta\\\Sigma\end{bmatrix} = \begin{bmatrix}1&-1\\1&1\end{bmatrix}\begin{bmatrix}a\\b\end{bmatrix}$$

with $\Delta=a-b$ and $\Sigma=a+b$. This makes explicit that “difference” and “sum” are just a basis change.


---

## 4. SHA‑256 rendered as a constraint fold

### 4.1 Standard round equations (ground truth)

For each round $t\in\{0,\dots,63\}$ the SHA‑256 compression uses:

$$T1_t = h_t + \Sigma_1(e_t) + \operatorname{Ch}(e_t,f_t,g_t) + K_t + W_t \pmod{2^{32}}$$

$$T2_t = \Sigma_0(a_t) + \operatorname{Maj}(a_t,b_t,c_t) \pmod{2^{32}}$$

with updates:

$$a_{t+1}=T1_t+T2_t,\; e_{t+1}=d_t+T1_t,\; \text{and the remaining registers shift}$$

where

$$\operatorname{Ch}(x,y,z)=(x\wedge y)\oplus(\neg x\wedge z),\qquad \operatorname{Maj}(x,y,z)=(x\wedge y)\oplus(x\wedge z)\oplus(y\wedge z)$$

and the big sigmas are rotations:

$$\Sigma_0(x)=\operatorname{ROTR}^2(x)\oplus\operatorname{ROTR}^{13}(x)\oplus\operatorname{ROTR}^{22}(x)$$

$$\Sigma_1(x)=\operatorname{ROTR}^6(x)\oplus\operatorname{ROTR}^{11}(x)\oplus\operatorname{ROTR}^{25}(x)$$

The message schedule is:

$$W_t = \begin{cases}M_t,&0\le t<16\\ \gamma_1(W_{t-2})+W_{t-7}+\gamma_0(W_{t-15})+W_{t-16},&16\le t<64\end{cases}$$

where

$$\gamma_0(x)=\operatorname{ROTR}^7(x)\oplus\operatorname{ROTR}^{18}(x)\oplus(x\gg 3),\quad \gamma_1(x)=\operatorname{ROTR}^{17}(x)\oplus\operatorname{ROTR}^{19}(x)\oplus(x\gg 10)$$

### 4.2 The “highway / dip” split as orthogonal bookkeeping

Define Highway as the schedule stream $W_t$ (message-derived) and Dip as the evolving working state (e.g., $e_t$ or $T1_t$). A practical test of “orthogonal channels but coupled constraints” is:

- low linear correlation $\rho(W_t,e_t)\approx 0$
- but nonzero mutual information $I(W_t;e_t) > 0$

This is exactly what you expect if the system is not trivially reducible but still deterministic.

### 4.3 What must be true for ‘unfolding without a forward pass’

In standard cryptography, the digest alone does not uniquely determine the preimage (many-to-one). For the **Nexus-style ‘resume’** idea to be literally true, *extra constraints must be available* besides the final digest.


Formally: you need an additional observable $\Delta$ such that

$$\text{Given }(H,\Delta)\text{ the preimage }M\text{ is uniquely determined (or sharply constrained).}$$

A concrete example of such an added observable is a traced internal sequence (a “scar”), e.g. the $T1_t$ series. From the round equation, if you know $T1_t$ and the working-state terms, you can algebraically recover $W_t$:

$$W_t = T1_t - h_t - \Sigma_1(e_t) - \operatorname{Ch}(e_t,f_t,g_t) - K_t \pmod{2^{32}}$$

So: **unfoldability requires access to internal constraints**, not just the final 256 bits.


---

## 5. BBP as constraint-as-input addressing

The Bailey–Borwein–Plouffe (BBP) formula for hexadecimal digits of $\pi$ is:

$$\pi = \sum_{k=0}^{\infty}\frac{1}{16^k}\left(\frac{4}{8k+1}-\frac{2}{8k+4}-\frac{1}{8k+5}-\frac{1}{8k+6}\right)$$

The key property: the $n$-th hex digit can be computed without all prior digits by working modulo powers of 16. In the Nexus language, this is “**addressing**” rather than “sequential generation”.


---

## 6. Helix → cross diffraction (Photo 51 as reciprocal constraint readout)

A helix with radius $r$ and pitch $P$ has a Fourier transform with Bessel-function structure. A standard form for scattering amplitude from a continuous helix can be written (schematically) as:

$$A(\mathbf{q}) \propto \sum_{n=-\infty}^{\infty} J_n(q_\perp r)\,\delta\!\left(q_z-\frac{2\pi n}{P}\right)$$

The $
$-indexed layer lines (the $\delta$ conditions) produce the ‘cross’ when intersected with the Ewald sphere. This makes Photo 51 a physical example of “shape is history”: the helix constraint prints as a reciprocal-space scar.


---

## 7. Memory, stability, and ‘peace’ as variance reduction

A minimal formalization of your “peace = trajectory stability” point is that memory acts as a low-pass integrator. One canonical model is an exponential moving average:

$$m_t = (1-\alpha)m_{t-1}+\alpha x_t,\qquad 0<\alpha<1$$

If the raw input $x_t$ contains high-frequency jitter, then $m_t$ reduces variance (and therefore perceived ‘noise’). This is a direct mechanism by which a non-Markov system can be stable.


---

## 8. Falsifiable tests (what would break the framework)

1. **Markov refutation**: If in a domain you claim is Nexus-governed, measurements consistently give

$$I(S_{t+1};S_{t-1}\mid S_t)\approx 0$$

then “history as active constraint” fails for that domain.


2. **No attractor**: If estimated $H$ (from control/feedback fits) does not cluster near $\pi/9$, then the proposed universal attractor is not universal.


3. **Unfold without scars**: If you can uniquely reconstruct messages from SHA-256 digests alone at nontrivial lengths, that would contradict standard complexity expectations—and must be demonstrated with reproducible experiments.


4. **Helix control**: Replace a helical fiber with an amorphous polymer (rings) or a crystal (Bragg spots). If the cross persists, the helix → cross claim is wrong.


---

## 9. Compact glossary

- **Constraint / lock**: a predicate on states that admits/forbids transitions.
- **Key**: a boundary condition that satisfies the predicate; formally not a force but a member of the admissible set.
- **Scar / residue**: additional observable left by execution; enables partial inversion when combined with output.
- **Highway/Dip**: two coupled-but-distinct channels (schedule vs working-state) used to test orthogonality.
