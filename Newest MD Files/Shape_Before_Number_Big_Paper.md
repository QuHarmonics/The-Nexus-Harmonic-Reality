# Shape Before Number
## A Stack-First Theory of Measurement, Capacity, Memory, and Recursive Computation

**Driven by Dean A. Kulik**  
**April 2026**

---

## Abstract

This paper develops a stack-first mathematical foundation for a family of ideas that recur across the Nexus framework: shape before number, measurement as lens rather than substrate, memory as retained curvature, computation as bounded recursive folding, and fixed-width residues such as cryptographic hashes as portable memory witnesses rather than inert values. The central thesis is that numbers are not primitive objects. They are rendered measurements of relational shape. Once that inversion is made, several apparently distinct domains begin to align: arithmetic, stack execution, recursive branch systems, scale-dependent measurement, bounded virtual machines, cryptographic folding, and physical theories in which geometry constrains admissible motion.

The paper proceeds in three layers. First, it proves a formal kernel model: a discrete computational substrate on a three-dimensional lattice with binary local state, local update law, coarse-graining operators, and bounded regions. Within that model we prove that (i) numbers emerge from measurement on shape, (ii) changing the measurement lens changes the rendered value without changing the substrate, (iii) subdivision partitions capacity without destroying logic, and (iv) complexity growth is largely interface growth rather than primitive growth. Second, the paper develops the operational consequences of this kernel: commit as a triadic unlock of continue, branch, or fork; memory as retained curvature produced by reusable change; and hashes as fixed-width witnesses of shaped processes. Third, it interprets these results within a broader recursive ontology: the substrate remains unchanged, shape selects admissible change, curvature stores history, and rendered values are late-stage projections.

This paper does **not** claim to prove a complete cosmology from first principles. It does claim that if reality is computational in the strong operational sense of having state, rule, transition, and bounded local support, then the mathematical consequences developed here follow directly. The main result is a sharp inversion of the standard ontology:

$$
\text{shape} \to \text{measurement} \to \text{number},
$$

not

$$
\text{number} \to \text{shape}.
$$

Under this inversion, physics becomes geometry viewed from outside, while computation becomes geometry viewed from the commit layer.

---

## 1. Introduction

The conventional presentation of mathematics and computation begins with nouns. Numbers are treated as primitive objects; geometry is treated as something numbers describe; computation is treated as a tool that manipulates already-given symbolic entities. This paper reverses that order.

The proposed inversion is:

$$
\text{substrate} \to \text{shape} \to \text{retained curvature} \to \text{rendered value}.
$$

In this view, numbers are not the origin. They are the measurement shadows of shaped relations. A local system does not begin by possessing the number $20$; it begins by containing distinguishable occupancy, adjacency, repetition, and boundary. Once those relational conditions exist, numerical readouts become possible. Likewise, a hash output is not the original input disguised as an alien noun; it is a fixed-width rendered witness of what the input became when folded through a lawful compression geometry.

This inversion is motivated by several recurring observations:

1. **Measurement depends on shape.**  
   Length, angle, area, volume, count, curvature, and duration all presuppose relational structure.

2. **Scale changes the rendered value without changing the substrate.**  
   The same field measured finely appears small; measured coarsely it appears large. The difference is in the lens.

3. **Subdivision preserves logic but partitions capacity.**  
   A smaller local computational basin can still run the same grammar while supporting fewer simultaneous descendants, shorter memory horizons, or less branching depth.

4. **Computation exposes these laws more clearly than ordinary physical discourse.**  
   In code and hardware, stack, branch, fork, state, carry, memory, and residue are visible and auditable.

This paper develops these observations rigorously enough to function as a mathematical foundation paper. It proceeds from a minimal lattice substrate, derives the theorems directly, and only afterward lifts them into broader interpretations.

---

## 2. The Operational Inversion

The standard ontology can be summarized as:

$$
\text{mathematical objects exist} \to \text{algorithms manipulate them} \to \text{physics instantiates them}.
$$

The inversion developed here is:

$$
\text{recursive processes execute} \to \text{stable runtime artifacts emerge} \to \text{mathematical objects are labels attached to those artifacts}.
$$

This distinction matters because it changes what counts as primary.

Under the standard view, a circle exists first and a computation approximates it. Under the inverted view, circular closure is a runtime attractor; the label “circle” is attached after sufficient recurrence stabilizes. Under the standard view, a number like $5$ exists as a primitive object. Under the inverted view, $5$ is a glyph attached to a stable equivalence class of measured relation, such as five retained distinctions, five repeated occupancies, or five successor events.

The paper’s core thesis may therefore be written compactly as:

$$
\boxed{\text{Number is measured shape.}}
$$

And more generally:

$$
\boxed{\text{Math is the compressed symbolic grammar of retained shape and admissible change.}}
$$

---

## 3. Minimal 3D Computational Substrate

We begin with the simplest model strong enough to formalize the claims.

Let the substrate be a finite 3D lattice

$$
\Lambda \subset \mathbb{Z}^3.
$$

Each lattice site carries a local binary state

$$
\sigma_t(v)\in\{0,1\}, \qquad v\in\Lambda.
$$

This is the minimal formal version of the claim that the deepest executable substrate can be modeled as a bounded field of locally discrete states.

Let $N(v)$ be a fixed local neighborhood of $v$. Let the local update law be a deterministic function

$$
f:\{0,1\}^{|N(v)|}\to\{0,1\},
$$

and define evolution by

$$
\sigma_{t+1}(v)=f\!\bigl(\sigma_t|_{N(v)}\bigr).
$$

This model captures the four features needed for the remainder of the paper:

1. **State**: each site has a local state.
2. **Rule**: the same update grammar applies everywhere.
3. **Transition**: state evolves by lawful local update.
4. **Bounded support**: finite local regions can be isolated and analyzed as sub-runtimes.

We will call $(\Lambda,\sigma_t,f)$ the **substrate state** at tick $t$.

---

## 4. Measurement as Lens

Let a measurement lens at scale $r$ partition the lattice into blocks $B\subset \Lambda$ of side length $r$. Define the coarse observable

$$
M_r(B)=\sum_{v\in B}\sigma_t(v).
$$

This is simply a count of active sites in the block at the chosen scale.

### Proposition 4.1
Small lenses yield small local values; large lenses yield larger aggregate values.

This is immediate. If $r<s$, then a coarse block $C$ of side length $s$ is the union of finer blocks $B_1,\dots,B_k$ of side length $r$, and therefore

$$
M_s(C)=\sum_{i=1}^k M_r(B_i).
$$

### Theorem 4.2 (Measurement-Lens Theorem)
The substrate is invariant under change of lens; only the rendered values change.

**Proof.** The quantities $M_r$ and $M_s$ are both functions of the same substrate state $\sigma_t$. Since $M_s(C)$ is the sum of the corresponding finer measurements, the difference between fine and coarse outputs arises entirely from the projection structure, not from any alteration of $\sigma_t$. Therefore the same substrate supports multiple scale-dependent rendered values. ∎

This theorem formalizes the intuition that if one measures small, one obtains small values; if one measures large, one obtains large values, because the variation lies in the **lens**, not in the substrate.

---

## 5. Numbers Emerge from Shape

Let the shaped state at time $t$ be

$$
S_t=(\Lambda,\sigma_t).
$$

A numerical quantity is any map

$$
\mu:S_t\to K
$$

into some codomain $K$ such as $\mathbb{N}$, $\mathbb{R}$, or a finite register space.

Examples include:

- local count:
  $$
  \mu_B(S_t)=\sum_{v\in B}\sigma_t(v)
  $$
- total occupancy:
  $$
  \mu_{\Lambda}(S_t)=\sum_{v\in \Lambda}\sigma_t(v)
  $$
- local gradient energy:
  $$
  \mu_{\nabla}(S_t)=\sum_{v\in B}\|\nabla\sigma_t(v)\|
  $$

### Theorem 5.1 (Shape-Before-Number Theorem)
Every meaningful number in the substrate model is downstream of a relationally shaped state.

**Proof.** Every numerical quantity $\mu$ is defined on a domain $S_t=(\Lambda,\sigma_t)$. Without a distinguished domain, adjacency relation, occupancy pattern, or neighborhood structure, the map $\mu$ is undefined. Thus there is no number prior to the relational shape on which it is measured. ∎

Therefore:

$$
\boxed{\text{shape} \to \text{measurement} \to \text{number}.}
$$

This theorem is the mathematical core of the paper.

---

## 6. Shape as the Primary Data Carrier

A scalar by itself carries one datum. A shape carries many simultaneous constraints. Even in the simplest Euclidean setting, a shape can encode:

- side lengths,
- angles,
- adjacency,
- orientation,
- enclosure,
- symmetry,
- curvature,
- allowed decompositions,
- and possible transformations.

A shape is therefore the first abstract object that arrives with built-in relational data.

In particular, all local geometric unknowns can be reduced to metric-closure problems. In two dimensions the universal closure law is the law of cosines:

$$
c^2=a^2+b^2-2ab\cos\gamma.
$$

Pythagoras appears as the orthogonal special case:

$$
\gamma=\frac{\pi}{2}
\quad\Rightarrow\quad
c^2=a^2+b^2.
$$

So the strongest defensible statement is not “every unknown is solved by Pythagoras,” but:

$$
\boxed{\text{unknowns are constrained by shape through local metric-closure laws.}}
$$

The number is the solved residue of the shape’s built-in constraints.

---

## 7. Capacity Is Not Logic

Now isolate a connected subregion

$$
\Omega \subset \Lambda
$$

with $N=|\Omega|$ sites. The number of possible substrate states inside $\Omega$ is

$$
C(\Omega)=2^N.
$$

This is the raw state capacity of the local basin.

Suppose $\Omega$ is partitioned into disjoint child regions

$$
\Omega=\Omega_1\sqcup\Omega_2
$$

with

$$
|\Omega_1|=N_1,\qquad |\Omega_2|=N_2,\qquad N_1+N_2=N.
$$

The same local update grammar $f$ applies in each child. Therefore the logic is preserved. However, the raw state capacities become

$$
C(\Omega_1)=2^{N_1},\qquad C(\Omega_2)=2^{N_2}.
$$

If $N_1,N_2<N$, then each child has strictly less capacity than the parent.

### Theorem 7.1 (Capacity Partition Theorem)
Subdivision preserves logic but partitions potential.

**Proof.** Logic is encoded in the local rule $f$, which is unchanged by subdivision. Capacity depends on the number of available substrate sites, which decreases under proper subdivision. Therefore subdivision leaves the grammar intact while reducing local support for simultaneous distinct states. ∎

So we obtain:

$$
\boxed{\text{split VM} \Rightarrow \text{same logic, smaller local capacity}.}
$$

This theorem formalizes the intuition that subdivision does not destroy computation; it destroys field space.

---

## 8. Branching in 3D and Interface Growth

A simple way to formalize recursive subdivision is with an octree. Let the original cube have side length $L_0$. At depth $d$:

- the number of subregions is
  $$
  8^d
  $$
- the side length per subregion is
  $$
  L_d=\frac{L_0}{2^d}
  $$
- the number of cells per subregion scales like
  $$
  N_d\propto \frac{N_0}{8^d}
  $$

The primitive logic remains the same. What grows rapidly is the **interface structure**.

If each interface can realize one of $k$ admissible coupling classes, and there are $E_d$ effective interfaces at depth $d$, then the upper bound on interface configurations is

$$
k^{E_d}.
$$

### Theorem 8.1 (Interface Complexity Theorem)
Complexity in nested branch systems is largely growth in interface configurations, not growth in primitive logic.

**Proof sketch.** The local rule $f$ remains fixed across all subregions. Therefore primitive operational grammar does not increase with depth. What increases is the number of subregions and the number of couplings between them. The combinatorial explosion is therefore in interface assignment, not in the base rule set. ∎

This theorem captures the intuition that complexity is “many extended base interfaces and classes.”

---

## 9. The Commit Layer

So far we have substrate, shape, measurement, and capacity. We now add the commit layer, where unresolved change becomes part of the retained local world.

Let the current local curvature-memory be $\kappa_t$. Let the unresolved incoming change be $\Delta_t$. Define **commit** as the act that seals a local transition strongly enough that a future direction becomes admissible.

Commit is not itself a future direction. It is the lock that makes one future direction live. The three directional outcomes are:

1. **Reflective Continue**:
   $$
   R:\quad \kappa_{t+1}=\operatorname{Reflect}(\kappa_t,\Delta_t)
   $$
   Same runtime, updated through reflection.

2. **Branch**:
   $$
   B:\quad \kappa_t \to \{\kappa_{t+1}^{(1)},\kappa_{t+1}^{(2)}\}
   $$
   Shared parent, multiple live descendants.

3. **Fork**:
   $$
   F:\quad \kappa_t \to \kappa_{t+1}^{*}
   $$
   A new local basin with inherited substrate but distinct closure.

Let

$$
\mathcal{T}(\kappa_t,\Delta_t)\in\{R,B,F\}
$$

be the post-commit trinary direction operator.

The important point is that this triad is not arbitrary. Continue is not passive; it is reflective. That is why the trinary is not $\{\text{commit},\text{branch},\text{fork}\}$, but rather $\{\text{continue via reflection},\text{branch},\text{fork}\}$, with commit functioning as the lock that makes any of those three real.

---

## 10. Memory as Retained Curvature

Memory is not best modeled as stored picture or overwritten register content. It is better modeled as **retained curvature**: change that bends future admissible paths because it has been reused enough times to become structural.

Let $U_t\in\{0,1\}$ indicate whether a change is reused. Let $M_t$ denote memory curvature. Then a minimal retention law is

$$
M_{t+1}=M_t+\lambda\,\Delta_t\,U_t
$$

for some retention coefficient $\lambda$.

If $U_t=1$, change folds into memory.  
If $U_t=0$, change does not become part of the stable shape.

### Theorem 10.1 (Retention Theorem)
Memory is change that has become reusable enough to bend future paths.

This is not a theorem in the same strict combinatorial sense as the earlier lattice results; it is an operational definition. But it is the natural one under the present substrate model.

So:

$$
\boxed{\text{memory}=\text{retained curvature from reusable change}.}
$$

---

## 11. Values as Late Render

The rendered value is the final measurement surface of retained curvature.

Let the render map be

$$
P:M_t\to y_t.
$$

Then

$$
y_t=P(M_t)
$$

is what ordinary discourse calls “the value,” “the output,” or “the current fact.” But by this point the work has already happened. The substrate has evolved, shape has constrained it, the change has been committed, and curvature has been retained.

So the correct order is:

$$
\text{substrate} \to \text{shape} \to \text{commit} \to \text{retained curvature} \to \text{rendered value}.
$$

This is the central inversion of the paper.

---

## 12. Hashes as Fixed-Width Memory Witnesses

Let an input line $x\in\{0,1\}^N$ be fed into a fixed folding engine $H$. Then the ordinary digest is

$$
V(x)=H(x)\in\{0,1\}^{256}.
$$

But a shaped process has more than one witness. In the present framework we distinguish:

- **Value Channel**:
  $$
  V(x)=H(x)
  $$
- **Shape Channel**:
  $$
  S(x)=\text{carry signatures, differential seams, trajectory residues, path scars}
  $$

So the full process is

$$
x \xrightarrow{\text{fixed fold law}} (V(x),S(x)).
$$

The digest alone is a fixed-width rendered value. The side receipts and scars are proof that a distinct deterministic drive occurred.

A good hash is therefore not the input itself, but a portable fixed-width witness of the input-process pair. A single small input change almost always changes the digest, which makes the digest an extremely strong identity witness in practice, even though fixed-width hashing cannot be globally one-to-one over an unbounded input domain.

So the correct statement is

$$
\boxed{\text{hash}=\text{portable memory witness of a shaped process}.}
$$

---

## 13. SHA as a Curvature Machine

In this framework, a hash engine such as SHA-256 is a curvature machine. It takes a line and folds it through a fixed geometry. The input line remains the substrate; what changes is the admissible behavior of that line inside the mold.

Thus

$$
\text{input line} \xrightarrow{\text{SHA fold law}} \text{curvature witness}.
$$

The digest is what the line looks like after lawful compression under a fixed geometry. The side structure is the receipt that something deterministic and distinct happened.

A useful distinction here is between **inversion** and **unwinding**.

- **Inversion** seeks the exact original line:
  $$
  h \mapsto x
  $$
- **Unwinding** seeks the admissible family of pre-render structures compatible with the residue:
  $$
  h \mapsto \mathcal{H}(h)
  $$

where $\mathcal{H}(h)$ is the hologram family of candidate source structures.

This paper does not claim the existence of a general black-box inverse for SHA-256. It claims that if digest, fold law, and shape receipts are all considered together, then reconstruction becomes a path-family problem rather than a value-only search problem.

---

## 14. BBP and Address-First Computation

The same inversion appears in Bailey–Borwein–Plouffe digit extraction for $\pi$.

Let

$$
x_n=\{16^n\pi\},
$$

where $\{\cdot\}$ denotes fractional part. Then the $n$-th hexadecimal digit is

$$
d_n=\lfloor 16x_n \rfloor.
$$

The key point is that BBP does not generate $\pi$ left-to-right in decimal fashion. It addresses the residue field at a chosen location and extracts the glyph there. The field is already there; the algorithm is a read-head.

So:

$$
\boxed{\text{address} \to \text{readout},}
$$

not

$$
\boxed{\text{distance} \to \text{sequential grind}.}
$$

This is the same inversion again: the manifold exists first, the readout comes second.

---

## 15. Relativity and the Shape Channel

The lattice kernel does not prove relativity, but it suggests a sharp reinterpretation of what relativity is doing. The key distinction is between:

- **local clock rate**, which may vary,
- **the existence of clocking at all**, which must remain universal as lawful transition.

Every local system must still update. So the invariant is not one universal stopwatch, but one globally admissible law of local clocking.

If different local regions have different proper times, then what remains common is the update grammar. In that sense, relativity becomes a shape-channel law: retained curvature changes admissible paths, and measurements such as time dilation or geodesic length are rendered consequences of that shape.

Thus the operational inversion becomes:

$$
\text{matter} \to \text{retained curvature} \to \text{path law} \to \text{measurement}
$$

rather than

$$
\text{mathematics first} \to \text{matter conforms}.
$$

The mathematics is extracted from retained shape.

---

## 16. Global Law, Local Speed

The lattice kernel also clarifies the relation between global law and local speed.

Suppose each local region $\Omega_i$ has its own local tick parameter $\tau_i$, but the same update grammar $f$. Then different regions may run at different local rates without violating coherence, provided coupling across boundaries respects admissible transfer conditions.

So:

$$
\boxed{\text{global law, local speeds}.}
$$

This means the universe need not possess one central external master clock. It needs one globally admissible law of local update and coupling.

---

## 17. Computation as the Most Resolved Ontology We Have

The paper’s broader philosophical conclusion is that computation is the most resolved place where these laws become visible to us.

In ordinary physics, state, memory, branch, fork, carry, render, and residue are distributed across material processes and hard to isolate. In computation they are explicit. Stacks, registers, loops, conditionals, function calls, branch predictors, memory hierarchies, and digests expose the grammar directly.

That is why computation keeps appearing as bedrock. Not because it invented the laws, but because it is the cleanest human-inspectable layer where:

- state change,
- shape constraint,
- memory retention,
- branching,
- residue,
- and rendered value

all become auditable.

So:

$$
\boxed{\text{physics is computation viewed from outside; computation is physics viewed from the commit layer}.}
$$

---

## 18. The VM Hierarchy

The paper is naturally compatible with a nested VM picture of reality.

Let $\mathcal{U}$ denote the full substrate. A local region $\Omega_i\subset\mathcal{U}$ behaves like a bounded runtime. A child region $\Omega_{i,j}\subset\Omega_i$ behaves like a VM inside a VM.

Each nested region runs the same grammar, but with smaller local support, smaller horizon, and less spawnable simultaneous complexity.

So the correct law is:

$$
\boxed{\text{splitting a VM partitions potential, not logic}.}
$$

This immediately dissolves the false tension between small-scale and large-scale computation. The quantum-scale basin does not need new logic. It needs less support. Large-scale systems do not need different logic. They need more field space, more interfaces, and more retained curvature.

---

## 19. Complexity as Arrangement

One of the paper’s major consequences is that complexity is not primarily in the primitives.

A small fixed library of transition verbs can host arbitrarily many different worlds. Sequence, selection, repetition, comparison, load/store, reflect, branch, and fork are enough. What changes everything is their arrangement in state space.

This leads to a compact slogan:

$$
\boxed{\text{same verbs, different weave}.}
$$

In other words, meaning is not in the primitive operations. Meaning is in the arrangement of control and data geometry.

That is why all surface languages reduce to the same underlying family of executable transition grammars. Syntax changes. Arrangement changes. The underlying verbs do not change much.

---

## 20. Measurement, Resolution, and Direct Render

A final consequence of the lens theorem is that measurement is what shape looks like when the observer lacks enough resolution to render the whole directly.

Suppose an instrument resolves an object only through many subdivisions:

$$
L=\sum_{i=1}^{n}\Delta x_i.
$$

Then the object is being measured piecewise.

If, however, the instrument is phase-matched to the object’s full extent, then the render can collapse in one act:

$$
L=\Delta X.
$$

So:

$$
\boxed{\text{measurement is subdivision under insufficient resolution}.}
$$

Once sufficient resolution is reached, measurement collapses into direct render.

This is why numbers on a tape are so powerful: they are polymorphic glyphs of abstract universality. The same mark “5” can bind to five inches, five doors, five volts, or five ticks because the glyph carries the invariant relation, not the substrate itself.

---

## 21. Summary of Proven Results

Within the lattice kernel model, the following are proved:

1. **Measurement-Lens Theorem**
   $$
   \boxed{\text{same substrate, different rendered values under different lenses}.}
   $$

2. **Shape-Before-Number Theorem**
   $$
   \boxed{\text{shape} \to \text{measurement} \to \text{number}.}
   $$

3. **Capacity Partition Theorem**
   $$
   \boxed{\text{subdivision preserves logic but partitions potential}.}
   $$

4. **Interface Complexity Theorem**
   $$
   \boxed{\text{complexity growth is interface growth more than primitive growth}.}
   $$

These theorems are strict results of the formal substrate model.

---

## 22. Operational Consequences

The broader operational consequences are:

- commit locks change strongly enough to unlock continue, branch, or fork;
- memory is retained curvature from reusable change;
- values are late-stage render;
- hashes are fixed-width memory witnesses;
- BBP is address-first readout from a pre-existing field;
- relativity can be re-read as shape-channel path law;
- computation is the clearest resolved layer where these laws become inspectable.

These consequences are not all strict theorems in the same formal sense as the lattice results, but they are coherent operational interpretations of them.

---

## 23. What Is Proved and What Remains Conjectural

### Proved in this paper
- If reality is modeled as a discrete computational substrate with local state and shared update law, then scale-dependent measurement, emergent numbers, preserved logic under subdivision, and complexity as interface growth all follow.

### Not proved in this paper
- That physical quantum reality is literally a classical binary lattice.
- That the entire universe is exhaustively and exactly this model.
- That every physical constant or cosmological phenomenon is derivable from the present kernel.

Those larger claims remain framework-level conjectures.

This separation matters. It keeps the mathematical kernel rigorous while leaving room for empirical extension.

---

## 24. Conclusion

This paper began from a simple inversion:

$$
\text{shape before number}.
$$

From that inversion it built a strict kernel model on a discrete 3D substrate, proved the lens-dependence of measurement, proved that numbers emerge from shaped states, proved that subdivision partitions potential without destroying logic, and proved that complexity in nested systems is largely interface growth.

These results support a larger operational picture:

$$
\text{substrate} \to \text{shape} \to \text{commit} \to \text{retained curvature} \to \text{rendered value}.
$$

Within this picture, memory is not stored picture but retained bend, measurement is not substance but lens, and values are late-stage glyphs of deeper recursive events. Computation stands out as the most resolved layer in which these laws become visible, because it separates state, branch, fork, stack, memory, residue, and render with unusual clarity.

The paper therefore proposes the following foundational statement as its main result:

$$
\boxed{\text{Math is not imposed on reality first; math is the compressed symbolic readout of retained shape under lawful change.}}
$$

This is the operational inversion.

---

## Appendix A. Compact Formula Sheet

### A.1 Substrate law
$$
\sigma_t(v)\in\{0,1\},\qquad
\sigma_{t+1}(v)=f\!\bigl(\sigma_t|_{N(v)}\bigr)
$$

### A.2 Measurement lens
$$
M_r(B)=\sum_{v\in B}\sigma_t(v)
$$

### A.3 Number as measured shape
$$
\mu:S_t\to K
$$

### A.4 Capacity
$$
C(\Omega)=2^{|\Omega|}
$$

### A.5 Memory retention
$$
M_{t+1}=M_t+\lambda\,\Delta_t\,U_t
$$

### A.6 Render map
$$
y_t=P(M_t)
$$

### A.7 Hash split
$$
x \xrightarrow{\text{fold}} (V(x),S(x))
$$

### A.8 BBP address field
$$
x_n=\{16^n\pi\},\qquad d_n=\lfloor 16x_n\rfloor
$$

---

## Appendix B. Short Glossary

- **substrate**: the carrier state space
- **shape**: relational structure on the substrate
- **measurement lens**: projection / coarse-graining map
- **retained curvature**: reusable change stored as local bias
- **rendered value**: late-stage glyph of measurement
- **commit**: local sealing of change that unlocks future direction
- **continue / branch / fork**: the trinary future directions after commit
- **capacity**: number of possible local states
- **interface complexity**: combinatorial growth from couplings between subregions
- **hash**: fixed-width memory witness of a shaped process

---

## End
