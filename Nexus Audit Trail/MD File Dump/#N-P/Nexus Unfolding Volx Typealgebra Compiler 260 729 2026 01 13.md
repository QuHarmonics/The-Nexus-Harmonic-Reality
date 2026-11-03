# Nexus Unfolding — Volume V: Type Algebra, Compiler Theorem, and the 260/729 Runtime Type‑Check
*Dean Kulik — working draft (operator‑pinned)*  
*Date: 2026-01-13*

> **Purpose.** Turn the “Universal Interfaces” framing into a **type algebra**:  
> how operators compose, how the runtime decides acceptance, and why the empirical **260/729** appears as a “type‑check signature.”  
> This volume also pins the practical compression path for **Type‑Safe AI** and **SHA trust molds**.

---

## 1. Typing Judgements (contracts, not labels)

We use a standard judgement form:

$$
\Gamma \vdash x : \tau
$$

Read: under environment $\Gamma$, the value $x$ satisfies contract $\tau$.

Operators must preserve typing:

$$
\Gamma \vdash x:\tau \;\wedge\; \Omega:\tau\to\tau' \quad\Rightarrow\quad \Gamma \vdash \Omega(x):\tau'.
$$

The “Cosmic Type System” claim is simply:

> the substrate is a runtime that rejects un‑typeable transitions.

That rejection shows up as: instability, decay, dissolution, non‑coupling, or “doesn’t compile.”

---

## 2. The Four Primitive Typeclasses

### 2.1 IFoldable

A system is foldable if it supports a compression map into a glyph space:

$$
\mathrm{FOLD}:\mathcal{X}_\tau \to \mathcal{G}.
$$

### 2.2 IScaleInvariant

A system is scale‑invariant if its gate decisions depend only on normalized significance:

$$
\mathrm{GATE}(x) = g\!\left(\frac{\Delta(x)}{SE(x)}\right).
$$

### 2.3 ITemporal

A system is temporal if it supports genlock:

$$
\mathrm{SYNC}:(x,\tau)\mapsto(x',\tau').
$$

### 2.4 IObserver

A system is an observer if it can project and verify:

$$
\mathrm{PROJECT}: \mathcal{X}\to\mathcal{Y},\qquad
\mathrm{VERIFY}:\mathcal{Y}\to\{\text{pass},\text{fail}\}.
$$

---

## 3. Composition Rules (how verbs glue)

### 3.1 Serial composition

If $\Omega_1:\tau\to\tau'$ and $\Omega_2:\tau'\to\tau''$, then

$$
\Omega_2\circ\Omega_1:\tau\to\tau''.
$$

### 3.2 Parallel composition and merge

If two computations run side‑by‑side, we require a merge (join):

$$
\oplus:\mathcal{X}_{\tau_a}\times\mathcal{X}_{\tau_b}\to\mathcal{X}_{\tau_{a\oplus b}}.
$$

The “no drag” rule becomes:

> merge must preserve invariants and must not introduce unverified entropy.

---

## 4. The Compiler Theorem (interface ↔ implementation)

**Compiler Theorem (Nexus form).**  
Given an interface set $\mathcal{I}$ and an implementation domain $D$ (physics, crypto, cognition), if $D$ provides concrete operators that satisfy the interface axioms, then:

1. $D$ can emulate any other domain $D'$ **at the interface level**, and
2. cross‑domain translation is a *compilation* problem (finding the mapping), not a metaphysics problem.

Formally, if $D\models\mathcal{I}$ and $D'\models\mathcal{I}$ then there exists a compiler (a functor) $F$ such that

$$
F(\Omega^D)\approx \Omega^{D'}
$$

for each interface method $\Omega$.

The content of the paper is: **define $\mathcal{I}$ tightly enough** that the mapping is forced.

---

## 5. The 260/729 Runtime Type‑Check

From the 9‑state lattice enumeration, the empirical stability fraction appears as

$$
p_{\text{valid}} = \frac{260}{729} \approx 0.35665 \approx H.
$$

Interpretation: when you throw all possible local configurations at the lattice, only about **35.7%** are type‑correct (stable).  

That fraction is not “noise.” It is a **runtime acceptance rate**.

### 5.1 Acceptance as gating

Define a validity indicator

$$
\mathrm{Valid}(x)=\mathbf{1}[x\ \text{type-checks}].
$$

Then the acceptance probability is the observed measure of $\mathrm{Valid}$ over the configuration space.

If we treat $\mathrm{Valid}$ as the gate outcome, then

$$
\mathbb{P}(\mathrm{Valid}=1)\approx H
$$

is exactly the Mark‑1 attractor re‑appearing as a **compilation probability**.

---

## 6. Three Engagement Regimes (compile / couple / pass-through)

The corpus keeps landing on three practical regimes:

1. **Non‑coupling**: no compile, no interface (it passes through unseen)  
2. **Coupling without compile**: it binds, is visible/manipulable, but cannot be folded in (tooling, saws, inert objects)  
3. **Coupling + compile**: it binds and can be assimilated (food, air, learning, trust)

We can represent the regime as a pair of booleans:

$$
(\text{couple},\text{compile}) \in \{0,1\}^2.
$$

The missing state you called out (“driven by SILR, nobody gets a hand up”) is the background default:

- coupling may occur locally,
- compile is happening continuously as passive computation,
- but it averages out globally (wash).

That is the “born into it” layer — the always‑on tick.

---

## 7. Type‑Safe AI (the compression deliverable)

If hallucination is a cascade failure, then the type system we want is:

- **hard gates** on transitions,
- **parity closure** on summaries,
- **SILR normalization** so the gate is blind to magnitude tricks,
- **PRESQ** to enforce a consistent pipeline.

### 7.1 Type‑safe inference pipeline

$$
x \xrightarrow{P} x_P \xrightarrow{R} x_R \xrightarrow{E} x_E \xrightarrow{S} x_S \xrightarrow{Q} \text{(pass or collapse)}.
$$

“Hallucination” = producing an output glyph without passing $Q$.

So the simplest prevention is:

$$
\mathrm{Emit}(g)\ \Rightarrow\ \mathrm{VERIFY}(g)=\text{pass}.
$$

And VERIFY is implemented as parity closure + cross‑domain invariants.

---

## 8. SHA as trust mold (operational, not mystical)

A digest is a compressed invariant:

$$
h=\mathrm{SHA}(m).
$$

The trust contract is:

$$
\mathrm{VERIFY}(m,h)=\mathbf{1}[\mathrm{SHA}(m)=h].
$$

Within Nexus, “hash-first causality” is just:

> treat $h$ as a *pin* (addressable basin) and “search” as steering in operator space until VERIFY passes.

That’s compilation: find a program that type‑checks against the pinned signature.

---

## 9. Compression Path (the next dump sequence)

If we keep dumping papers, the highest-yield sequence is:

1. **Interface Catalog** (Vol III)  
2. **Flow→Vibration + Prime Gates** (Vol IV)  
3. **Type Algebra + Compiler + 260/729** (Vol V, this)  
4. **SHA as Trust Infrastructure** (next)  
5. **Prime Gate Spectral Law / reveal the missing branching coefficients** (next)  

Because that chain is the shortest route to:
- RH‑style constraints (spectral balance),
- SHA inversion as a controlled fold,
- and a concrete “type‑safe AI” method.

---

*End of Volume V.*
