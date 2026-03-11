# Nexus Phase–Closure Lens v2  
## Twin primes: single-orbit vs chained-orbit phase mechanics (and why SHA reads like a “difference oracle”)

> **Status note (important):** This document **does not claim** a completed Clay-style proof of the Twin Prime Conjecture or \(P = NP\).  
> It **does** turn the work so far into a *complete, reproducible mathematical specification* with:
> - explicit definitions,
> - explicit formulas,
> - clear “what is assumed vs what is observed,”
> - testable propositions,
> - and a clean bridge back to the Nexus idea: **ask the right question, get the remainder**.

---

## 0) Core Nexus stance (so we don’t mis-attribute “value” to SHA)

A hash is not “truth.” It is an **interface** that enforces a **difference invariant**:

- If \(x=y\), then \(h(x)=h(y)\).
- If \(x\neq y\), then typically \(h(x)\neq h(y)\) (for SHA-256, collision probability is negligible in practice).

Formally, for a hash \(h:\{0,1\}^\*\to \{0,1\}^{256}\),
\[\
x=y \implies h(x)=h(y).
\]
\[\
x\ne y \implies \Pr[h(x)=h(y)] \approx 2^{-256}\ \text{(under standard assumptions)}.
\]

So SHA is best treated as a **granular difference engine** and a **validation oracle**: it doesn’t explain meaning, it enforces identity under re-check.

That matches your “pre-stack” language:
> The hash isn’t the value; it’s the **brick wall filter** that says “this input is still itself.”

---

## 1) Harmonic anchor

Define the harmonic entry angle:
\[\
H \stackrel{\mathrm{def}}{=} \frac{\pi}{9}\approx 0.3490658504\ \text{radians}\approx 20^\circ.
\]

Define the base phase unit:
\[\
\omega \stackrel{\mathrm{def}}{=} 2H = \frac{2\pi}{9}\approx 0.6981317008\ \text{radians}\approx 40^\circ.
\]

Everything below is a **phase-map lens** built on \(\omega\).  
The point is not “\(\omega\) must be cosmic.” The point is: *if you choose this lens*, certain closure/non-closure structures become visible and testable.

---

## 2) Twin primes and indexing

Let the \(k\)-th twin prime pair be:
\[\
(p_k,\ p_k+2),
\]
with \(p_k\) prime and \(p_k+2\) prime, ordered by increasing \(p_k\).

Let the twin prime counting function be:
\[\
\pi_2(x) = \#\{k:\ p_k \le x\}.
\]

We will use **two “time axes”**:

- the **internal axis** \(k\): “twin index time,”
- the **external axis** \(x\): “integer-line time.”

Most confusion comes from collapsing these two into one.

---

## 3) Model A: the **single-orbit** (constant-step) phase map

### 3.1 Definition
Define cumulative phase:
\[\
\Theta_A(k) \stackrel{\mathrm{def}}{=} k\omega,
\qquad
\theta_A(k) \stackrel{\mathrm{def}}{=} \Theta_A(k)\bmod 2\pi.
\]

### 3.2 Local closure (period-9 portal)
Then:
\[\
\theta_A(k)=0 \iff k\omega \equiv 0 \pmod{2\pi}
\iff k\cdot \frac{2\pi}{9} \equiv 0 \pmod{2\pi}
\iff k\equiv 0 \pmod 9.
\]

So **local closure** is exact in Model A:
\[\
\theta_A(9m)=0\quad (m\in\mathbb{N}).
\]

### 3.3 The “global non-closure” move
If you view closure along the integer line \(x\), you substitute \(k=\pi_2(x)\) and get:
\[\
\theta_A(\pi_2(x))=0 \iff \pi_2(x)\equiv 0 \pmod 9.
\]

If \(\pi_2(x)\bmod 9\) keeps drifting (empirically it does in your plots/runs), then closure is **visited** but not **locked**.

> **Nexus phrasing:** local closure exists (platforms), global lock never arrives (no final wall).

This is the first “eye of the storm” statement:
\[\
\textbf{Local closure in }k\ \textbf{does not imply global closure in }x.
\]

---

## 4) Non-closure metrics (what the plots are actually computing)

Define circular distance-to-closure:
\[\
d(\theta) \stackrel{\mathrm{def}}{=} \min\{\theta,\ 2\pi-\theta\}.
\]

Then define (for any phase sequence \(\theta(k)\)):

- pointwise distance:
  \[\
  d(k)=d(\theta(k));
  \]
- cumulative non-closure sum:
  \[\
  S(N)=\sum_{k=1}^{N} d(k);
  \]
- winding number:
  \[\
  W(N)=\frac{\Theta(N)}{2\pi}.
  \]

These are diagnostics: they describe whether the process repeatedly returns near the same phase (closure) or drifts.

---

## 5) Why Model A isn’t the whole story (what you spotted)

Model A assumes **one circle** and **one constant step**.

Your newer plots are pointing at a different geometry:

> Each twin pair behaves like its own *local orbit* (ellipse), and the observed trajectory is the **chain** of those orbits.

That is not “one rotation sampled.” It is a **linked-orbit process** with a small alphabet of step sizes (“gears”).

---

## 6) Model B: the **chained-orbit** (three-gear) phase map

### 6.1 What is meant by “chain link”

We define a **chain-link value** \(\ell_k\) that represents the “step descriptor” between the \(k\)-th and \((k+1)\)-th twin pair under your construction.

Your plots label this as something like:
\[\
\ell = 6n-2
\]
for an integer \(n\). This form forces \(\ell\equiv 4\pmod 6\), so any “mod 6” statistic on \(\ell\) is **structural**, not a discovery by itself.

To keep the model honest, we define:
\[\
n_k \stackrel{\mathrm{def}}{=} \frac{\ell_k+2}{6} \in \mathbb{Z}.
\]

The informative residue class is then \(n_k\bmod 3\), not \(\ell_k\bmod 6\).

### 6.2 The three gears (phase increments)

Empirical claim from your chained-orbit analysis (to be treated as an observed pattern under your mapping):

There are **three** dominant increments, corresponding to fractions of \(2\pi\) with denominator \(9\):

- gear 1: \(\frac{2}{9}\cdot 2\pi = \frac{4\pi}{9} = 80^\circ\),
- gear 2: \(\frac{5}{9}\cdot 2\pi = \frac{10\pi}{9} = 200^\circ\),
- gear 3: \(\frac{8}{9}\cdot 2\pi = \frac{16\pi}{9} = 320^\circ\).

Define the gear-map \(g:\mathbb{Z}\to\{2,5,8\}\) by:
\[\
g(n)=
\begin{cases}
2,& n\equiv 1\pmod 3,\\
5,& n\equiv 2\pmod 3,\\
8,& n\equiv 0\pmod 3.
\end{cases}
\]

Then define the chained phase increment:
\[\
\Delta\theta_k \stackrel{\mathrm{def}}{=} g(n_k)\cdot \frac{2\pi}{9}.
\]

### 6.3 The chained cumulative phase

Define:
\[\
\Theta_B(K) \stackrel{\mathrm{def}}{=} \sum_{k=1}^{K} \Delta\theta_k,
\qquad
\theta_B(K) \stackrel{\mathrm{def}}{=} \Theta_B(K)\bmod 2\pi.
\]

This is a **finite-alphabet rotation** on the circle: each step is one of three rotations.

### 6.4 Closure in the chained model

A closure event is:
\[\
\theta_B(K)=0 \iff \Theta_B(K)\equiv 0\pmod{2\pi}.
\]

Since each \(\Delta\theta_k\) is a multiple of \(2\pi/9\), write:
\[\
\Theta_B(K)=\frac{2\pi}{9}\sum_{k=1}^{K} g(n_k).
\]

So closure becomes a modular sum constraint:
\[\
\sum_{k=1}^{K} g(n_k) \equiv 0 \pmod 9.
\]

This is the key: **closure becomes a constraint satisfaction condition on the gear sequence** \(\{g(n_k)\}\).

That is why you see “preferred closure points” (e.g., sums mod \(18\) appearing more often than uniform would predict): the gear alphabet is small, and the sequence is not independent uniform.

> **Nexus phrasing:** this is a real “set collapse” mechanism: you don’t search the full space, you collapse onto modular constraints.

---

## 7) The Markov/transition layer (what your heatmap implies)

If the observed process has constrained transitions, you can model the gear-state as a Markov chain.

Let the state be \(s_k = n_k \bmod 3 \in \{0,1,2\}\).  
Or equivalently \(s_k = g(n_k)\in\{2,5,8\}\).

A Markov model would define:
\[\
P_{ij} = \Pr(s_{k+1}=j\mid s_k=i).
\]

Then closure statistics become properties of additive functionals over the chain:
\[\
\Sigma_K \stackrel{\mathrm{def}}{=} \sum_{k=1}^{K} g(n_k) \pmod 9.
\]

This is now a **random walk on \(\mathbb{Z}_9\)** driven by a (possibly) Markov source.

If the source were uniform i.i.d. over \(\{2,5,8\}\), closure frequency would be near \(1/9\).  
If it’s structured, some residues can be hit more often — that’s exactly the “preferred closure points” effect you noted.

---

## 8) Why this is structurally different from Model A

- **Model A**: one fixed step \(\omega\). Closure every 9 steps is built-in.
- **Model B**: steps come from a **three-element alphabet**, closure is a **modular-sum constraint** over a driven sequence.

In Model B, there is no single “orbit.” There is a **gear train**.

That matches your “weird machine depth” idea: not a linear computation, but a collective computation where the substrate determines which transitions exist.

---

## 9) What this does *and does not* say about twin primes

### 9.1 What it *does* say (cleanly)
You’ve built a mapping in which:

- There exist **local closure gates** (modular portals).
- The embedding into external time \(x\) shows **global drift**.
- In the chained model, closure corresponds to a modular constraint:
  \[\
  \sum g(n_k)\equiv 0\pmod 9,
  \]
  making the problem “set-like” (constraint collapse) rather than “path-like.”

### 9.2 What it *does not* yet say (and what would be required)
It does **not** yet prove:
- infinitude of twin primes,
- or any Clay-class statement,
because the mapping must be connected to established number-theoretic control of the sequence \(\{n_k\}\) (or whichever canonical statistic \(\ell_k\) is computed from).

To move toward “proof,” you would need:

1. a **canonical** definition of \(\ell_k\) in terms of primes/twins (not just a plotting recipe);
2. a theorem that the induced gear sequence \(\{g(n_k)\}\) has certain recurrence / non-locking properties;
3. a bridge from those properties back to a statement about \(\pi_2(x)\) (twin counts).

---

## 10) The “right question” in math form

You said: *the pre-stack is the remainder.*  
Here is the general form of that idea:

Let \(F\) be a constraint function and define solution set:
\[\
\mathcal{S} = \{z:\ F(z)=0\}.
\]

“Searching” is enumerating candidates \(z\).  
“Right-questioning” is choosing coordinates so \(\mathcal{S}\) collapses to a singleton (or a low-dimensional manifold).

In the chained model, the “right question” is literally:
\[\
\text{Find }K\text{ such that } \sum_{k=1}^{K} g(n_k)\equiv 0\pmod 9.
\]

That’s a remainder constraint. The answer is whatever survives it.

---

## 11) Appendix: formula reference

### Harmonic anchor
- \(H=\pi/9\)
- \(\omega=2H=2\pi/9\)

### Model A (single orbit)
\[\
\Theta_A(k)=k\omega,\quad \theta_A(k)=\Theta_A(k)\bmod 2\pi.
\]
\[\
\theta_A(k)=0 \iff k\equiv 0\pmod 9.
\]

### Model B (chained orbits / three gears)
\[\
n_k = \frac{\ell_k+2}{6}.
\]
\[\
g(n)=\begin{cases}
2,& n\equiv 1\pmod 3\\
5,& n\equiv 2\pmod 3\\
8,& n\equiv 0\pmod 3
\end{cases}
\qquad
\Delta\theta_k = g(n_k)\cdot \frac{2\pi}{9}.
\]
\[\
\Theta_B(K)=\sum_{k=1}^{K}\Delta\theta_k,\quad \theta_B(K)=\Theta_B(K)\bmod 2\pi.
\]
\[\
\theta_B(K)=0 \iff \sum_{k=1}^{K} g(n_k)\equiv 0\pmod 9.
\]

### Distance / non-closure diagnostics
\[\
d(\theta)=\min\{\theta,\ 2\pi-\theta\},\quad S(N)=\sum_{k=1}^{N} d(k).
\]

---

**End.**
