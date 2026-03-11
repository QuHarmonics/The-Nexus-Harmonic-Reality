# Axioms and Falsification Tests
## Ontic Mixing vs Epistemic Separation

_Last updated: 2026-02-24_

This document is a **testable specification** of the claim:

- **Epistemic separation** (layers / modules / types / abstractions) is a *projection* used by bounded agents to communicate and compress.
- **Ontic mixing** (coupled nodes with history) is a *structural requirement* for any system that:
  1) runs for all inputs (no fatal “halt” state),
  2) supports stable trajectories (not pure jitter),
  3) supports meaning transfer (reuse) without recomputing the world from scratch.

The question here is not “is separation useful?” (it is).  
The question is: **what must be true underneath** for separation to be possible at all.

---

## 0. Symbols and setup

We work in discrete time (a sampled view) because it makes falsification explicit; continuous-time analogs follow by letting the tick size $\Delta t\to 0$.

- $t\in\mathbb{Z}$ indexes ticks.
- $S_t$ is the **full internal state** of the substrate at tick $t$ (the thing that actually updates).
- $O_t$ is an **observation / rendered projection** of $S_t$ (what an agent sees).
- $U_t$ is an **exogenous input** (what is injected / perturbs at tick $t$).
- $F$ is the update rule.

### Total transition (no crash)

A runnable universe requires a **total** update map:

$$
S_{t+1} = F(S_t, U_t) \quad \text{is defined for all } (S_t, U_t).
$$

No “undefined state” is permitted (no fatal exception).  
This is weaker than determinism; it only says *a next state exists* for every current state and input.

### Markov vs non-Markov

A process is **Markov** (order-1) if

$$
P(S_{t+1}\mid S_t, S_{t-1},\dots)=P(S_{t+1}\mid S_t).
$$

A process is **non-Markov** if history matters beyond $S_t$ in the representation being used.

A **representation-invariant** way to test this is the conditional mutual information:

$$
I(S_{t+1}; S_{t-1} \mid S_t) > 0.
$$

If this holds robustly above a null baseline, then the substrate is not order-1 Markov in the state you’re measuring. (If you later expand the state to include enough history, you can make it Markov again—but then that history is literally part of the state.)

---

## 1. The core thesis in one line

**Separation is a compression of a coupled system; coupling is what makes compression stable.**

Formally, if an agent uses a projection $\Pi$ to define “layers”:

$$
O_t = \Pi(S_t),
$$

then “separation” is the *claim* that $\Pi$ factorizes the dynamics into independent pieces.

The falsifiable question is:

> Does there exist any factorization of $S_t$ into independent sub-states that preserves predictive power without importing hidden history?

---

## 2. Axioms (what must be true)

### A0 — Total transition
As above: $F$ is total.

### A1 — Finite bandwidth observers
Any agent has bounded bandwidth and must compress:

$$
\Pi: \mathcal{S}\to\mathcal{O},\quad \dim(\mathcal{O})\ll\dim(\mathcal{S}).
$$

This is why layers, nouns, types, and “objects” exist as interface artifacts.

### A2 — Memory is required for trajectory
To define a trajectory you need curvature, and curvature requires multiple past points.

Discrete velocity and acceleration:

$$
v_t = S_t - S_{t-1},\qquad a_t = v_t - v_{t-1} = S_t - 2S_{t-1} + S_{t-2}.
$$

If $S_{t-1}$ and $S_{t-2}$ are not functionally present in the update (explicitly or implicitly), you cannot compute $a_t$ and you cannot stabilize against jitter.

### A3 — Stability requires filtering (history integration)
A minimal stability mechanism is a low-pass filter that integrates history:

Exponential moving average (EMA):

$$
M_t = (1-\alpha)M_{t-1}+\alpha X_t,\qquad 0<\alpha<1.
$$

Variance reduction (“peace”) is:

$$
\mathrm{Var}(M_t) < \mathrm{Var}(X_t) \quad \text{for high-frequency } X_t.
$$

A universe that “cannot crash” but also “cannot remember” would be forced into maximal sensitivity (jitter).

### A4 — Meaning requires reuse (invariants)
Meaning transfer requires invariants (stable equivalence classes).  
An invariant $I$ satisfies:

$$
I(S_{t+1}) = I(S_t) \quad \text{(exact)} \qquad \text{or} \qquad I(S_{t+1})\approx I(S_t) \text{ (robust)}.
$$

These invariants are what agents name (“king cobra”) and transmit.

### A5 — Orthogonal bookkeeping (value vs residue)
If the system is total and stable, changes must be conserved across channels: what doesn’t remain as *value* must remain as *residue* (shape / exhaust).

A compact bookkeeping identity is a Pythagorean norm:

$$
V_t^2 + \Delta_t^2 = T^2,
$$

where $V_t$ is “rendered value” (what you measure as a noun), and $\Delta_t$ is “unrendered residue” (what remains to be carried as phase/history).

### A6 — Coupling is primary, separation is secondary
Nodes interact; “layers” are partitions of the interaction graph.  
Let $G=(\mathcal{N},\mathcal{E})$ be the node-edge graph of dependencies. Then:

- Ontic: dynamics on $G$ are coupled.
- Epistemic: we draw module boundaries as a partition $\mathcal{N}=\bigsqcup_k \mathcal{N}_k$.

Separation is successful only if boundary-crossing information is low, but **never zero** for a live system.

---

## 3. Derived propositions

### P1 — “Peace” is measurable variance reduction
If an agent’s internal state is a filter $M_t$ over inputs $X_t$, then “peace/silence” corresponds to reduced high-frequency energy:

Let $\widehat{X}(\omega)$ be the Fourier transform. For EMA, the frequency response is:

$$
H(\omega)=\frac{\alpha}{1-(1-\alpha)e^{-i\omega}}.
$$

High $\omega$ components are damped: $|H(\omega)|$ decreases as $\omega$ increases.

### P2 — Non-Markovian signature is unavoidable for stable agents
If an agent uses acceleration/curvature for control, it must depend on at least two past points. Therefore, in the agent’s effective state:

$$
I(S_{t+1};S_{t-1}\mid S_t) > 0
$$

should hold whenever the environment drives nontrivial dynamics.

### P3 — “Context missing → revert to shape” is optimal compression
When semantic labels are missing, the best fallback is geometry / morphology: i.e., use invariants of motion and boundary conditions.

Operationally: if you can’t decode the symbol, decode the **likelihood of threat** from shape features $\phi$:

$$
P(\text{danger}\mid\phi) \propto P(\phi\mid\text{danger})P(\text{danger}).
$$

This is not philosophy; it’s Bayes under limited context.

---

## 4. Falsification tests (what would kill the claim)

Each test below is designed so that a *single robust failure* breaks a corresponding axiom.

### T1 — Total transition test (no crash)
**Claim:** for any input $U_t$, the system yields a defined $S_{t+1}$.

**Operational proxy:** if a supposed “substrate ISA” has invalid opcodes / fatal halts for generic inputs, it cannot be the substrate. A real substrate must interpret every pattern as some valid state update (even if it is “do nothing,” saturate, leak, or re-route).

### T2 — Non-Markov conditional mutual information
Compute:

$$
I(S_{t+1};S_{t-1}\mid S_t)
= \sum_{s_{t+1},s_t,s_{t-1}} p\,\log\frac{p(s_{t+1},s_{t-1}\mid s_t)}{p(s_{t+1}\mid s_t)p(s_{t-1}\mid s_t)}.
$$

**Falsification:** if this is indistinguishable from a Markov null **across** domains where “memory” is claimed (e.g., internal SHA traces, structured biological chains), then “memory is required” is wrong.

### T3 — Layer-separation test (graph cut)
Given a candidate partition (layers), measure boundary information flow by mutual information between partitions:

$$
I(\mathcal{N}_A;\mathcal{N}_B).
$$

**Falsification:** if a partition exists with boundary information consistently ~0 while preserving prediction accuracy, then ontic mixing is not required.

### T4 — Stability requires history (jitter vs trajectory)
Take a signal $X_t$ and compare one-step controller vs two-step controller.

- Markov controller: $u_t=f(X_t)$
- Non-Markov controller: $u_t=f(X_t,X_{t-1},X_{t-2})$

Measure closed-loop variance of controlled variable $Y_t$.

**Falsification:** if the Markov controller matches or dominates the non-Markov controller for stability in systems that claim trajectory, then “memory is required for peace” fails.

### T5 — Orthogonal channels (value/residue)
Estimate whether “rendered” and “residue” channels are linearly uncorrelated but informationally coupled:

- Pearson: $\rho(V,\Delta)\approx 0$
- Mutual information: $I(V;\Delta)>0$

**Falsification:** if either (a) they are fully redundant ($\rho$ large) or (b) fully independent ($I\approx 0$) in domains where “two-channel storage” is claimed, the dual-channel model fails.

---

## 5. Domain anchoring (how to apply tests to your artifacts)

This section is intentionally concrete. It’s not claiming new physics; it’s specifying *measurements* you can do on the data you already generated.

### 5.1 SHA-256 traces (internal rounds)
For a single block, the round relation:

$$
T1_t = h_t + \Sigma_1(e_t) + Ch(e_t,f_t,g_t) + K_t + W_t \pmod{2^{32}}.
$$

Rearranged:

$$
W_t \equiv T1_t - h_t - \Sigma_1(e_t) - Ch(e_t,f_t,g_t) - K_t \pmod{2^{32}}.
$$

**Test hooks:**
- Treat $S_t$ as the 8-word working state $(a,b,c,d,e,f,g,h)$.
- Compute $I(S_{t+1};S_{t-1}\mid S_t)$ over $t$ across many inputs.
- Compare to a Markov null built by permuting $t$ within each run.

### 5.2 BBP-style “addressing”
The BBP digit extraction formula (base 16) is:

$$
\pi = \sum_{k=0}^{\infty} \frac{1}{16^k}
\left(
\frac{4}{8k+1}-\frac{2}{8k+4}-\frac{1}{8k+5}-\frac{1}{8k+6}
\right).
$$

Operational point: some structures behave like *addressable manifolds* (query by index without enumerating all prior indices).  
The falsifiable part here is **not** “pi is a ROM”; it is: “addressing exists as a mechanism.”

### 5.3 Protein folding metric (Sarrus-style coherence)
Your coherence proxy (as described in your drafts) can be expressed as a differential of lag autocorrelations:

Let $\rho(\ell)$ be autocorrelation at lag $\ell$ of a transformed sequence signal.

Helix proxy:
$$
H = \frac{\rho(3)+\rho(4)}{2}.
$$

Sheet proxy:
$$
S = \rho(2).
$$

Differential (“Sarrus”):
$$
\Delta_{HS}=Z_H-Z_S.
$$

Then your latency model used a Lorentz-like form over a normalized progress variable $\sigma$:

$$
\gamma(\sigma)=\frac{1}{\sqrt{1-\sigma^2}}.
$$

The **testable** statement is “non-Markov + stability improves prediction,” not any metaphysical interpretation.

---

## 6. What must be true (compressed answer)

If *all code must run no matter what* (no crash), and *meaning/trajectory exists*, then at minimum:

1) **A total transition exists:** $S_{t+1}=F(S_t,U_t)$ for all inputs.  
2) **State contains or induces memory:** otherwise trajectory and stability are impossible.  
3) **Compression exists:** observers use $\Pi(S_t)$ to name and transmit invariants.  
4) **The substrate is coupled:** separation is an observer partition of a dependency graph, not the graph itself.

---

## 7. Minimal “lock/key” formalization (optional, but crisp)

Let $L$ be a constraint (lock), and $k$ a candidate boundary condition (key).  
Define a predicate that means “admitted”:

$$
C_L(k)=1 \iff \text{the trajectory under }F\text{ reaches an admissible fixed point / orbit}.
$$

The key does not “force” the lock; it is simply the boundary condition that satisfies the lock’s predicate.

In other words: **the verbs are in $C_L$; the key is a frozen waveform passed through $C_L$.**

---

## 8. Reporting template (drop-in for a paper)

When you run tests, report:

- sample size (N runs, lengths, domains),
- statistic (CMI, MI, AIC, etc.),
- null construction,
- effect size (ratio over null),
- confidence intervals.

Example for the non-Markov test:

$$
\text{Non-Markov Score} = \frac{I(S_{t+1};S_{t-1}\mid S_t)}{I_{\text{null}}}
$$

---

## Appendix A — Useful identities

Bitwise add decomposition (for intuition about “parity vs carry”):

$$
a+b = (a\oplus b) + 2(a\wedge b).
$$

Quadrature / 90° partner (Hilbert transform):

Given $x(t)$,
$$
z(t)=x(t)+i\,\mathcal{H}\{x(t)\},\quad
\phi(t)=\arg z(t).
$$

These are tools for measuring “orthogonal components” in data—nothing more is assumed.

