# Bitcoin Reverse Tension Probe — Complete Solution Draft

## Abstract

This document formalizes the current Bitcoin-header reverse-probe program as a **constraint-ranking problem on the SHA-256 predecessor fiber**, not as direct value guessing. The central result is that a candidate word is not judged by numerical proximity to the true schedule word, but by whether the predecessor state induced by that candidate reproduces the same **admissible side geometry** as the true run. In this framework, a **match** means geometric compatibility with the observed fold; a **failure** means scar inconsistency, often delayed and only exposed under chained reverse propagation.

The current empirical state is:

- exact one-step reverse closure is available once $W_r$ is supplied,
- a cold-score functional on admissible scars ranks the true Bitcoin chain first on real headers,
- multi-round coupling converts a local tension meter into a progressive binding sequence,
- best-first search shows that the previous 8-round failure was a **search bottleneck**, not disappearance of geometric signal.

This is **not yet** a full inversion proof for SHA-256 or Bitcoin. It is a formalization of the current phase: the search has moved from blind value guessing to **ranking admissible predecessor states by side-geometry residuals**.

---

## 1. Problem Statement

Let the SHA-256 compression state at round $r$ be

$$
x_r = 
\begin{bmatrix}
a_r \\
 b_r \\
 c_r \\
 d_r \\
 e_r \\
 f_r \\
 g_r \\
 h_r
\end{bmatrix}
\in (\mathbb Z/2^{32}\mathbb Z)^8.
$$

For a Bitcoin 80-byte block header, the mining-relevant uncertainty lives in the **second compression block of the first SHA pass**, where the seed words include the tail of the merkle root, timestamp, bits, and nonce. The reverse question is:

> Given a terminal state or derived observable package from late rounds, can one identify the lawful predecessor chain without exporting direct transport values?

The key point is that the reverse task is **not**:

$$
\text{guess a 32-bit value and hope it is right.}
$$

It is instead:

$$
\text{identify the unique predecessor chain whose induced side-geometry matches the observed fold.}
$$

---

## 2. The SHA-256 Die Equation

For one block, SHA-256 is a 64-step nonlinear recurrence

$$
x_{r+1} = \Phi_r(x_r, W_r), \qquad r = 0,\dots,63.
$$

Define the shift matrix

$$
P=
\begin{bmatrix}
0&0&0&0&0&0&0&0\\
1&0&0&0&0&0&0&0\\
0&1&0&0&0&0&0&0\\
0&0&1&0&0&0&0&0\\
0&0&0&1&0&0&0&0\\
0&0&0&0&1&0&0&0\\
0&0&0&0&0&1&0&0\\
0&0&0&0&0&0&1&0
\end{bmatrix},
$$

so that

$$
P x_r =
\begin{bmatrix}
0 \\
 a_r \\
 b_r \\
 c_r \\
 d_r \\
 e_r \\
 f_r \\
 g_r
\end{bmatrix}.
$$

Define the two nonlinear fold channels

$$
T1_r = h_r + \Sigma_1(e_r) + \operatorname{Ch}(e_r,f_r,g_r) + K_r + W_r,
$$

$$
T2_r = \Sigma_0(a_r) + \operatorname{Maj}(a_r,b_r,c_r).
$$

Let

$$
u_a=
\begin{bmatrix}
1\\0\\0\\0\\0\\0\\0\\0
\end{bmatrix},
\qquad
\nu_e=
\begin{bmatrix}
0\\0\\0\\0\\1\\0\\0\\0
\end{bmatrix}.
$$

Then the round map is

$$
\boxed{
x_{r+1} = P x_r + \nu_a (T1_r + T2_r) + \nu_e T1_r
}
$$

in $\mathbb Z/2^{32}\mathbb Z$.

This is the core die equation: the machine is mostly shift, with only **two nonlinear injections** per round.

---

## 3. Exact Reverse Closure for One Step

Because the shift structure is sparse, once a candidate word $g$ is supplied for round $r$, one can compute the candidate predecessor state

$$
x_r(g) = \Phi_r^{-1}(x_{r+1}; g)
$$

exactly.

That is, the reverse ambiguity is not in the algebra of the step itself. The ambiguity is in the unknown injected schedule word. Therefore the real reverse object is not the value $g$ by itself, but the induced predecessor state $x_r(g)$.

This yields the first crucial distinction:

$$
\text{candidate word} \longrightarrow \text{candidate predecessor state} \longrightarrow \text{candidate scar geometry}.
$$

---

## 4. Ground Geometry and the NOP Backbone

Set all message schedule words to zero:

$$
W_r = 0 \qquad \forall r.
$$

Then the backbone trajectory is

$$
x_{r+1}^{(0)} = \Phi_r(x_r^{(0)}, 0).
$$

This is the **message-free backbone** or ground manifold.

At round $0$, the ground fold is universal:

$$
T2_0^{(0)} = \Sigma_0(H_{0,a}) + \operatorname{Maj}(H_{0,a}, H_{0,b}, H_{0,c}) = 0x08909ae5.
$$

This is a fixed substrate coordinate, not a property of any particular message.

A useful derived perturbation form is

$$
\delta x_r = x_r - x_r^{(0)} \pmod{2^{32}}.
$$

The NOP backbone is therefore the clean reference against which message-induced geometry is measured.

---

## 5. The Sziklai Differential Invariant

A central exact identity of the die is

$$
a_{r+1} - e_{r+1} \equiv T2_r - d_r \pmod{2^{32}}.
$$

This follows directly from

$$
a_{r+1} = T1_r + T2_r,
$$

$$
e_{r+1} = d_r + T1_r.
$$

Subtracting gives

$$
a_{r+1} - e_{r+1} = (T1_r + T2_r) - (d_r + T1_r) = T2_r - d_r.
$$

This is important because it is **$T1$-blind**. It removes the shared emitter and leaves a differential constraint tied only to the top-half geometry.

Because the register shift implies

$$
d_r = a_{r-3},
$$

this differential relation spans multiple rounds and is a natural candidate for future cross-round admissible observables.

---

## 6. What a “Match” Means

A candidate does **not** match because its numeric bits are close to the true schedule word.

A candidate matches when the predecessor state it induces reproduces the same exported side geometry as the true run.

Let $B_r^{\text{obs}}$ be the observed admissible geometry bundle for round $r$, exported from the forward pass. Let $B_r(g)$ denote the same bundle recomputed from the candidate predecessor state $x_r(g)$.

Then a match at round $r$ means

$$
B_r(g) = B_r^{\text{obs}}.
$$

A failure means

$$
B_r(g) \neq B_r^{\text{obs}}.
$$

But because the bundle may be thin or partially degenerate, a false candidate can still satisfy a weak local equality and fail only after recursive chaining.

So the stronger notion is **chain match**:

$$
B_C(\mathbf g) = B_C^{\text{obs}}
$$

for a chain of rounds $C$ and a candidate vector $\mathbf g = (g_{r_0},\dots,g_{r_1})$.

---

## 7. The Admissible Geometry Bundle

The practical probe deliberately uses **side scars**, not transported values. The current admissible family includes the following observable classes.

### 7.1 Staged carry masks

For the staged construction of $T1_r$, define carry masks at each internal addition stage. The full 32-bit masks are stronger than mere Hamming weights.

### 7.2 Carry-mask Hamming weights

For a carry mask $C$, define

$$
\operatorname{hw}(C) = \sum_{j=0}^{31} C_j.
$$

This is coarser than the full mask but still useful as a side observable.

### 7.3 Chirality splits

To separate even and odd bit-position contributions, define

$$
\chi_0(x) = \operatorname{hw}(x \mathbin{\&} 0x55555555),
$$

$$
\chi_1(x) = \operatorname{hw}(x \mathbin{\&} 0xAAAAAAAA).
$$

These are admissible because they expose directional asymmetry of the carry geometry without revealing direct schedule words.

### 7.4 Nibble silhouette of $h$

Partition a 32-bit word into 8 nibbles. For the reconstructed register $h_r$, define the nibble Hamming silhouette

$$
\sigma(h_r) = \big(\operatorname{hw}(h_r^{(0)}),\operatorname{hw}(h_r^{(1)}),\dots,\operatorname{hw}(h_r^{(7)})\big),
$$

where each $h_r^{(k)}$ is a 4-bit nibble.

### 7.5 Carry-span witnesses

If a carry begins at bit $j$ and propagates through a maximal contiguous cascade, define its span length

$$
\lambda_x(j) = \text{maximum carry cascade length starting at bit } j.
$$

The maximal span or span profile is a stronger admissible scar than weight alone.

### 7.6 NOP-subtracted masks

Given a staged carry mask $C_r$ and its NOP counterpart $C_r^{(0)}$, define the message-only interference pattern

$$
\Delta C_r = C_r \oplus C_r^{(0)}.
$$

This isolates message-induced geometry relative to the pure substrate.

---

## 8. Residual Score Functional

Let $d(\cdot,\cdot)$ be a nonnegative mismatch functional on bundles. Then the local round score is

$$
R_r(g) = d\big(B_r(g), B_r^{\text{obs}}\big).
$$

The cumulative chain score over a round set $C$ is

$$
\boxed{
R_C(\mathbf g) = \sum_{r\in C} d\big(B_r(x_r(g_r), g_r), B_r^{\text{obs}}\big)
}
$$

with the true chain satisfying

$$
R_C(\mathbf g^\star) = 0.
$$

False chains satisfy

$$
R_C(\mathbf g) > 0
$$

unless the current bundle is still degenerate enough to admit counterfeit minima.

This is the key change of viewpoint:

$$
\text{we are not searching for values; we are minimizing a geometric residual on the predecessor fiber.}
$$

---

## 9. Why a False Candidate Can Look Cold Locally

A false candidate can score well in one round because the observable map

$$
g \mapsto B_r(g)
$$

need not be injective for fixed $x_{r+1}$.

That means multiple candidates can produce the same thin projection, such as equal carry weight or equal coarse silhouette.

However, once that candidate is used to construct a predecessor state and the process is repeated, the wrong predecessor poisons the next round. Therefore the map

$$
\mathbf g \mapsto B_C(\mathbf g)
$$

becomes progressively sharper as the chain grows.

This is the mathematical form of the lock-picking analogy:

- one tumbler = one local residual,
- full lock = recursively coupled residual chain.

---

## 10. Best-First Search on the Predecessor Fiber

Let a partial chain of guesses be denoted by a node $n$. Define the accumulated cost

$$
g(n) = \sum_{r \in C(n)} R_r.
$$

A conservative best-first or uniform-cost strategy ranks nodes by

$$
f(n) = g(n).
$$

A future A*-style refinement would add a lower-bound estimate of remaining unavoidable residual,

$$
f(n) = g(n) + h(n),
$$

with $h(n)$ admissible in the sense that it never overestimates the minimum remaining mismatch.

At present, the grounded search result is that replacing fixed-width beam truncation by best-first expansion was sufficient to recover the true chain at greater depth on real Bitcoin data. That indicates the previous deeper failures were caused by **search policy**, not disappearance of the geometric signal.

---

## 11. Bitcoin-Specific Interpretation

For an 80-byte Bitcoin block header, the first SHA pass spans two 512-bit compression blocks. The mining-relevant action is in the second block of the first SHA pass, where the schedule seed words contain:

- merkle-root tail,
- timestamp,
- bits,
- nonce.

The experiments target late rounds in that block. The current interpretation is:

1. the true chain remains the unique zero-residual path under the tested admissible bundle,
2. false chains can survive locally but destabilize under recursive coupling,
3. deeper recovery depends both on bundle richness and search policy.

So the current claim is:

$$
\boxed{
\text{true Bitcoin candidate chains are progressively isolatable by admissible side-geometry residuals.}
}
$$

This is stronger than “there is some signal,” but weaker than full inversion.

---

## 12. What Is Different in the Math Between a Match and a Failure?

The question is not value vs. value. It is **lawful predecessor geometry vs. counterfeit predecessor geometry**.

### 12.1 Match

A match is a candidate chain $\mathbf g$ such that

$$
x_r(\mathbf g) \in \mathcal F_r^{\text{obs}}
$$

for all rounds in the tested chain, where $\mathcal F_r^{\text{obs}}$ is the admissible predecessor fiber consistent with the observed bundle.

Equivalent residual statement:

$$
R_C(\mathbf g)=0.
$$

### 12.2 Failure

A failure is a chain whose induced predecessor exits the observed fiber:

$$
x_r(\mathbf g) \notin \mathcal F_r^{\text{obs}}
$$

for at least one round in the chain, producing

$$
R_C(\mathbf g)>0.
$$

So in structural terms:

$$
\text{match} = \text{same fold geometry},
$$

$$
\text{failure} = \text{geometric inconsistency, often delayed}.
$$

---

## 13. Where We Are in Steps

There are two natural step counts.

### 13.1 Operational round depth

The current Bitcoin program has successfully tracked from round

$$
63 \rightarrow 56
$$

in the target compression block, i.e. **8 rounds deep out of 64** for that block.

So in the local block sense, the current operational depth is

$$
\frac{8}{64}.
$$

### 13.2 Research-program phase

A reasonable seven-step map is:

1. exact one-step reverse closure given $W_r$,
2. local admissible bundle and cold score,
3. multi-round coupling on real Bitcoin headers,
4. search-policy correction showing deeper failure was algorithmic, not geometric,
5. stronger cross-round admissible invariants or lower-bound heuristic,
6. tail-to-vestibule bridge from late-round scars to earlier schedule structure,
7. deterministic block-level recovery, then full Bitcoin double-SHA pipeline.

On that scale, the current phase is approximately

$$
\boxed{4/7}
$$

— well past “is there a signal?” but not yet at “the inverse law is closed.”

---

## 14. The Current Missing $\Delta$

The next missing pieces are now sharply defined.

### 14.1 Injectivity of the chained bundle

We need either proof or strong evidence that the chained bundle map

$$
\mathbf g \mapsto B_C(\mathbf g)
$$

is injective on the admissible predecessor fiber, at least for practically relevant chain lengths.

### 14.2 A true lower-bound heuristic

Best-first search worked, but a real A*-style step requires a nontrivial admissible estimate

$$
h(n)
$$

for remaining unavoidable residual.

### 14.3 Tail-to-vestibule bridge

Current recovery is still tail-first. We need a law that constrains earlier schedule structure using late-round scars without leaking transport.

### 14.4 Stronger cross-round scars

Candidates include:

- differential silhouettes derived from the Sziklai invariant,
- seam-specific carry-span witnesses,
- longer-range chirality profiles,
- support-closure or span-consistency observables across multiple rounds.

---

## 15. Complete Current Solution Statement

The present complete solution is not a proof of SHA-256 inversion. It is the following formal statement.

### Theorem-like current state

Let $C$ be a tested reverse round chain on a real Bitcoin SHA-256 compression block. Let $B_C^{\text{obs}}$ be the exported admissible side-geometry bundle over that chain. Let

$$
R_C(\mathbf g) = \sum_{r\in C} d\big(B_r(x_r(g_r), g_r), B_r^{\text{obs}}\big).
$$

Then, empirically for the tested real Bitcoin headers and tested search budgets:

1. the true chain $\mathbf g^\star$ satisfies

$$
R_C(\mathbf g^\star)=0,
$$

2. false chains satisfy

$$
R_C(\mathbf g)>0,
$$

within the observed top-ranked search basin,

3. replacing beam truncation by best-first search preserves the true chain to greater depth,

4. therefore the current barrier is no longer “absence of structure,” but the transition from a ranking functional to a genuine inverse law.

---

## 16. Final Collapse

The deepest current conclusion is:

$$
\boxed{
\text{A match is not “the right 32-bit value.” A match is the unique candidate whose induced predecessor remains on the same recursive scar manifold.}
}
$$

That is why the next move is not “more guessing.” The next move is to find the next invariant that turns

$$
\text{ranking} \longrightarrow \text{elimination}.
$$

Until then, the program is correctly understood as **geometric reverse ranking on the predecessor fiber of the SHA die**, currently demonstrated on real Bitcoin header data.
