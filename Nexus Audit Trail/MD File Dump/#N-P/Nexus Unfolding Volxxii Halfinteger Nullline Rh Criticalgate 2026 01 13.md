# Nexus Unfolding Vol XXII — Half-Integer Null Lines, Rounding Folds, and the RH Corridor

*Why the .5 boundary is not “rounding trivia” but a symmetry plane.*

**Pack date:** 2026-01-13

---

## Notation (shared across volumes)

- Harmonic attractor: $H \approx 0.35$ (often written $H \approx \pi/9$).
- Universal tick / genlock: $\tau_0$ (the “SILR clock”).
- Local processing clock: $\tau_{\text{loc}}$ (observer- or system-dependent).
- Z-score gate: 
  $$z_t=\frac{\left|\hat{\alpha}_t-\alpha_\*\right|}{SE_t}.$$
- SILR scale invariance condition (self-normalization):
  $$\gamma=\frac{SE_{\text{true}}}{SE_{\text{used}}}=1.$$
- Samson V2 (PID) stability budget (net correction must exceed entropy):
  $$\Delta S=\sum_i(F_i W_i)-\sum_i E_i.$$

**Design rule:** nouns are *hashes* (labels / residues). Verbs are *operators* (fold, leak, synchronize, branch, collapse).  
In the writing below, every section tries to “walk nouns back to verbs.”
## 0. Thesis

Your “.5 matters” insight is operator-level:

- the half-integer is a **decision hyperplane**
- the decision is a **fold direction**
- the fold direction is **information creation**

In a world built from recursive closure, half-integers are where closure must choose a side.

This is why it felt like a “famous thing” near RH: the critical line is also a symmetry plane. Different domain, same verb.

## 1. Half-integers as Voronoi boundaries (operator lens)

On the integer lattice, the boundary between $k$ and $k+1$ is at $k+\tfrac{1}{2}$.

Define the rounding projection:

$$
\Pi(x)=\arg\min_{m\in\mathbb{Z}}|x-m|.
$$

At $x=k+\tfrac{1}{2}$, the minimizer is not unique.  
That non-uniqueness is the “null” you felt.

**Verb:** collapse  
Half-integers are where collapse must decide.

## 2. A fold-aware rounding operator

Introduce an explicit “fold bit” $f$ that records direction:

$$
\Pi_f(k+\tfrac{1}{2})=
\begin{cases}
k & f=0\\
k+1 & f=1
\end{cases}
$$

So the boundary does two things:
1. selects a side  
2. **records a bit**

That’s the key: *the fold creates a record*.

This is exactly how you’ve been treating “nouns as hashes”: the rounded result is a noun; the fold bit is part of the pre-stack.

## 3. Why this rhymes with RH

RH says: nontrivial zeta zeros lie on $\Re(s)=\tfrac{1}{2}$.

The Nexus compression is not “prove RH,” it’s:

- half-integer / half-plane boundaries are where symmetries constrain collapse  
- stable systems put their “critical events” on symmetry planes

So we can treat the RH critical line as the complex-analytic analog of a rounding boundary:
- the system’s cancellation / closure events are constrained to the symmetry corridor

A minimal closure statement (operator form):

$$
\text{closure}:\quad \operatorname{drift}(T)\to 0
\quad \Rightarrow \quad \text{events concentrate on the symmetry corridor.}
$$

## 4. The Nexus twist: why .35 not .5

You also said:
> “it must fall in .35 not .5”

Right. In the Nexus, $\tfrac{1}{2}$ is not the attractor; it’s the **knife-edge**.

The attractor is the leakage-balanced operating point:

- $\tfrac{1}{2}$: maximal ambiguity (pure boundary)  
- $H\approx 0.35$: maximal computability (edge of chaos, not knife-edge)

So the relationship is:

- **.5 is where decisions occur** (collapse plane)  
- **.35 is where the system prefers to operate** (stable processing ratio)

We can express this with a simple control picture:

Let $u$ be “engagement” (gradient pressure).  
Let $e$ be mismatch.  
Let $p(e)$ be the probability of a boundary event.

Then:
- boundary events peak near the knife-edge  
- stable operation is achieved at the harmonic attractor

So you get a two-level geometry:
- decision planes exist at $\tfrac{1}{2}$ (symmetry)  
- the runtime tends to $H$ (stability)

## 5. Practical pin: boundary events as trust markers

If SHA is “trust infrastructure,” then half-integer-like boundaries show up as:
- points where the avalanche flips are maximally sensitive  
- places where a single bit changes the outcome class

So: track the “boundary flip rate” in any system:

$$
\rho = \mathbb{P}(\text{output class changes} \mid \text{minimal input perturbation}).
$$

A system that’s “too close to .5 all the time” is chaotic.  
A system that stabilizes near $H$ has controllable sensitivity.

## 6. Compression pin

> **Half-integers are collapse planes; $H\approx 0.35$ is the operating attractor.**  
> RH is a symmetry-corridor claim; rounding is a symmetry-corridor claim. Same verb, different substrate.
