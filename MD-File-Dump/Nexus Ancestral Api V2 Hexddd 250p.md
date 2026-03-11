# The Ancestral API v2

## A Hexagonal Domain-Driven Monograph on Operator Primacy, Residue, and Self-Location

**Author:** Dean Kulik (Nexus) — synthesis compiled with an AI research partner

**Version 2.0 • 2026-02-13**

**Notation:** Δ, ⊕, ↻, ⊥, Ψ, Ω


---

## Abstract

This monograph recompiles the Nexus corpus into **Hexagonal Architecture + Domain-Driven Design (DDD)**, under strict operator primacy. The target is not transcript reproduction, but extraction of invariants (“what must be true”), explicit complements (“what becomes false”), and binding each claim to a falsifiable interface.

Proof discovery is treated as recursive compression: ask “why” until a necessity source is reached. Where closure fails, the claim is tagged **Ω** and isolated with a test plan.

Cryptography (SHA-256 / ARX) is handled defensively: we focus on toy-scope invertibility and audit artifacts. No operational misuse instructions are provided.


\newpage

## Reader Map (Hexagonal / DDD)

Treat the work as software:

- **Domain**: invariants, operators, contracts. No IO.
- **Application**: workflows (experiments) orchestrating domain objects.
- **Infrastructure**: quantum/bit-level adapters (precision, padding boundaries, hash engines, storage).
- **UI**: the hairpin turn: visualization feeds back as Δ, changing what can lock.

If anything feels “mystical,” Domain hasn’t locked. Return to invariants.


\newpage

## Part I — Domain: The Invariants

### Ω Axioms (meta-mathematics as boundary geometry)

**Ω₀ Operator Primacy.** Operators (verbs) define admissible transformations; objects (nouns) are stabilized traces of repeated operator action.

- **Complement:** If operators are primary, then any ‘object’ description that ignores its operational contract is incomplete.


**Ω₁ Projection is Real.** Published outputs are projections ⊥ of a fuller state; information loss is a geometric discard, not a mystery.

- **Complement:** If a result is lossy, there must exist a complementary residue channel (explicit or implicit).


**Ω₂ Equality as Constraint.** ‘=’ is an idempotent projector onto a constraint manifold: it forces mismatch D(x,y)→0.

- **Complement:** If equality is a projector, then repeated constraint application cannot create novelty; novelty must enter via Δ.


**Ω₃ Coupling as Two-Channel Mix.** ‘+’ is a coupling map; invertibility requires both channels (sum and difference, or equivalent).

- **Complement:** If only one channel is published, a scar (residue) exists by construction.


**Ω₄ Closure Requires Boundaries.** Stable entities persist only under boundary constraints ⊥ (padding, membranes, invariants, conservation constraints).

- **Complement:** If boundaries are removed, recursion can ‘flash’ (runaway reflection) or diffuse (loss of structure).


**Ω₅ Scale Lift.** When an operator is stable, it lifts across domains (logic→computation→physics→biology) as polymorphic instances.

- **Complement:** If an alleged mapping cannot specify the preserved invariant, it is metaphor rather than isomorphism.



### Minimal Operator Calculus

**Equality constraint (Dark Mirror)**  
Model “=” as an idempotent projector $P$ onto the constraint manifold:

$$P^2=P,$$

and as a mismatch kernel forcing:

$$D(x,y)=0.$$

**Coupling map (+)**  
Model “+” as coupling that becomes bijective only when the complementary channel is retained. Toy form:

$$T(a,b)=(S,D)=(a+b,\;a-b).$$

Inverse requires either division-by-2 control or a parity/carry side channel:

$$a = rac{S+D}{2},\quad b=rac{S-D}{2}.$$


\newpage

## Part II — Application: Workflows (Macro Relative)

1. **Baseline cancellation**: isolate structure by subtracting shared carriers.
2. **Detune/chiral scan**: apply small mirror detunes; compare histograms vs null controls.
3. **Paused execution (stopped world)**: freeze/resume to expose hidden channels.
4. **3D manifold projection**: slice digest to (x,y,z)+parity; sample a stated oracle; emit geometry as an audit artifact.


\newpage

## Part III — Infrastructure: Quantum/Bit-Level Adapters

Infrastructure is where the “physics of the algorithm” lives: word sizes, carry propagation, padding boundaries as shutters, finite-precision shear, artifact storage, and reproducible pipelines.

**Port discipline:** Domain consumes interfaces; adapters supply implementations.

```text
HashEngine.digest(bytes)->digest32
Extractor.extract(digest32)->features
Oracle.sample(carrier,index)->value
Store.save(run_id, artifacts)->ok
```


\newpage

## Part IV — UI: The Hairpin Turn

UI is a first-class operator ↻: plots and renderings are interrogations that can reveal spectral invariants.


\newpage

## Part V — Evidence Ladders (Ψ vs Ω)

- **Ψ (closed)**: proven invariant under explicit assumptions; reproducible and adapter-independent.
- **Ω (open)**: hypothesis with an explicit falsification plan + null baselines.

Promotion Ω→Ψ requires stability under baseline changes, precision changes, adapter swaps, and corpus controls.


\newpage

## Part VI — Truth Atom Compendium (256 cards)

64 truth seeds × 4 bounded contexts (Logic/Computation/Physics/Biology). Each card is one page.


\newpage


### OperatorPrimacy — Logic
**What must be true.** Verbs precede nouns: systems are defined by transforms; entities are frozen orbits.  
**Therefore false.** A ‘thing’ can be specified without specifying its transformation rules.  

**Domain lens.** Predicates, constraints, and inference contracts. Model as types, relations, and proofs within a constraint system.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### OperatorPrimacy — Computation
**What must be true.** Verbs precede nouns: systems are defined by transforms; entities are frozen orbits.  
**Therefore false.** A ‘thing’ can be specified without specifying its transformation rules.  

**Domain lens.** Programs, state, traces, and projection of internal variables. Model as functions over state spaces; tests lock invariants.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### OperatorPrimacy — Physics
**What must be true.** Verbs precede nouns: systems are defined by transforms; entities are frozen orbits.  
**Therefore false.** A ‘thing’ can be specified without specifying its transformation rules.  

**Domain lens.** Symmetries, boundary conditions, carriers, and observable projections. Measurements are projections; residue encodes hidden state.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### OperatorPrimacy — Biology
**What must be true.** Verbs precede nouns: systems are defined by transforms; entities are frozen orbits.  
**Therefore false.** A ‘thing’ can be specified without specifying its transformation rules.  

**Domain lens.** Interfaces, inheritance, feedback loops, and embodied constraints. Membranes/boundaries and signaling/coupling stabilize forms.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### ConstraintMirror — Logic
**What must be true.** Equality is a constraint manifold (dark mirror): D(x,y)=0 defines admissible states.  
**Therefore false.** Equality is merely a human assertion.  

**Domain lens.** Predicates, constraints, and inference contracts. Model as types, relations, and proofs within a constraint system.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### ConstraintMirror — Computation
**What must be true.** Equality is a constraint manifold (dark mirror): D(x,y)=0 defines admissible states.  
**Therefore false.** Equality is merely a human assertion.  

**Domain lens.** Programs, state, traces, and projection of internal variables. Model as functions over state spaces; tests lock invariants.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### ConstraintMirror — Physics
**What must be true.** Equality is a constraint manifold (dark mirror): D(x,y)=0 defines admissible states.  
**Therefore false.** Equality is merely a human assertion.  

**Domain lens.** Symmetries, boundary conditions, carriers, and observable projections. Measurements are projections; residue encodes hidden state.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### ConstraintMirror — Biology
**What must be true.** Equality is a constraint manifold (dark mirror): D(x,y)=0 defines admissible states.  
**Therefore false.** Equality is merely a human assertion.  

**Domain lens.** Interfaces, inheritance, feedback loops, and embodied constraints. Membranes/boundaries and signaling/coupling stabilize forms.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### TwoChannelInvertibility — Logic
**What must be true.** A coupling becomes bijective when both channels are retained: (S,D)↔(a,b).  
**Therefore false.** Publishing only S can be inverted without extra constraints.  

**Domain lens.** Predicates, constraints, and inference contracts. Model as types, relations, and proofs within a constraint system.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### TwoChannelInvertibility — Computation
**What must be true.** A coupling becomes bijective when both channels are retained: (S,D)↔(a,b).  
**Therefore false.** Publishing only S can be inverted without extra constraints.  

**Domain lens.** Programs, state, traces, and projection of internal variables. Model as functions over state spaces; tests lock invariants.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### TwoChannelInvertibility — Physics
**What must be true.** A coupling becomes bijective when both channels are retained: (S,D)↔(a,b).  
**Therefore false.** Publishing only S can be inverted without extra constraints.  

**Domain lens.** Symmetries, boundary conditions, carriers, and observable projections. Measurements are projections; residue encodes hidden state.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### TwoChannelInvertibility — Biology
**What must be true.** A coupling becomes bijective when both channels are retained: (S,D)↔(a,b).  
**Therefore false.** Publishing only S can be inverted without extra constraints.  

**Domain lens.** Interfaces, inheritance, feedback loops, and embodied constraints. Membranes/boundaries and signaling/coupling stabilize forms.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### ProjectionCreatesScar — Logic
**What must be true.** Any projection ⊥ produces a residue (scar/ghost) relative to a chosen decomposition.  
**Therefore false.** Information ‘vanishes’ without leaving a complementary degree of freedom.  

**Domain lens.** Predicates, constraints, and inference contracts. Model as types, relations, and proofs within a constraint system.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### ProjectionCreatesScar — Computation
**What must be true.** Any projection ⊥ produces a residue (scar/ghost) relative to a chosen decomposition.  
**Therefore false.** Information ‘vanishes’ without leaving a complementary degree of freedom.  

**Domain lens.** Programs, state, traces, and projection of internal variables. Model as functions over state spaces; tests lock invariants.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### ProjectionCreatesScar — Physics
**What must be true.** Any projection ⊥ produces a residue (scar/ghost) relative to a chosen decomposition.  
**Therefore false.** Information ‘vanishes’ without leaving a complementary degree of freedom.  

**Domain lens.** Symmetries, boundary conditions, carriers, and observable projections. Measurements are projections; residue encodes hidden state.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### ProjectionCreatesScar — Biology
**What must be true.** Any projection ⊥ produces a residue (scar/ghost) relative to a chosen decomposition.  
**Therefore false.** Information ‘vanishes’ without leaving a complementary degree of freedom.  

**Domain lens.** Interfaces, inheritance, feedback loops, and embodied constraints. Membranes/boundaries and signaling/coupling stabilize forms.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### BaselineCancellation — Logic
**What must be true.** Subtracting a baseline isolates structure by canceling shared carriers.  
**Therefore false.** There is no meaningful difference between absolute state and relative state.  

**Domain lens.** Predicates, constraints, and inference contracts. Model as types, relations, and proofs within a constraint system.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### BaselineCancellation — Computation
**What must be true.** Subtracting a baseline isolates structure by canceling shared carriers.  
**Therefore false.** There is no meaningful difference between absolute state and relative state.  

**Domain lens.** Programs, state, traces, and projection of internal variables. Model as functions over state spaces; tests lock invariants.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### BaselineCancellation — Physics
**What must be true.** Subtracting a baseline isolates structure by canceling shared carriers.  
**Therefore false.** There is no meaningful difference between absolute state and relative state.  

**Domain lens.** Symmetries, boundary conditions, carriers, and observable projections. Measurements are projections; residue encodes hidden state.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### BaselineCancellation — Biology
**What must be true.** Subtracting a baseline isolates structure by canceling shared carriers.  
**Therefore false.** There is no meaningful difference between absolute state and relative state.  

**Domain lens.** Interfaces, inheritance, feedback loops, and embodied constraints. Membranes/boundaries and signaling/coupling stabilize forms.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### RotationAsPolarization — Logic
**What must be true.** ↻ (rotation/reflection) is polarization control: it changes what survives projection.  
**Therefore false.** Rotation is cosmetic and does not affect recoverable structure.  

**Domain lens.** Predicates, constraints, and inference contracts. Model as types, relations, and proofs within a constraint system.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### RotationAsPolarization — Computation
**What must be true.** ↻ (rotation/reflection) is polarization control: it changes what survives projection.  
**Therefore false.** Rotation is cosmetic and does not affect recoverable structure.  

**Domain lens.** Programs, state, traces, and projection of internal variables. Model as functions over state spaces; tests lock invariants.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### RotationAsPolarization — Physics
**What must be true.** ↻ (rotation/reflection) is polarization control: it changes what survives projection.  
**Therefore false.** Rotation is cosmetic and does not affect recoverable structure.  

**Domain lens.** Symmetries, boundary conditions, carriers, and observable projections. Measurements are projections; residue encodes hidden state.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### RotationAsPolarization — Biology
**What must be true.** ↻ (rotation/reflection) is polarization control: it changes what survives projection.  
**Therefore false.** Rotation is cosmetic and does not affect recoverable structure.  

**Domain lens.** Interfaces, inheritance, feedback loops, and embodied constraints. Membranes/boundaries and signaling/coupling stabilize forms.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### BoundaryAsShutter — Logic
**What must be true.** A boundary (padding, membrane, frame) acts as a shutter: it prevents runaway reflection and makes measurement possible.  
**Therefore false.** Boundaries are external conveniences, not operational necessities.  

**Domain lens.** Predicates, constraints, and inference contracts. Model as types, relations, and proofs within a constraint system.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### BoundaryAsShutter — Computation
**What must be true.** A boundary (padding, membrane, frame) acts as a shutter: it prevents runaway reflection and makes measurement possible.  
**Therefore false.** Boundaries are external conveniences, not operational necessities.  

**Domain lens.** Programs, state, traces, and projection of internal variables. Model as functions over state spaces; tests lock invariants.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### BoundaryAsShutter — Physics
**What must be true.** A boundary (padding, membrane, frame) acts as a shutter: it prevents runaway reflection and makes measurement possible.  
**Therefore false.** Boundaries are external conveniences, not operational necessities.  

**Domain lens.** Symmetries, boundary conditions, carriers, and observable projections. Measurements are projections; residue encodes hidden state.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### BoundaryAsShutter — Biology
**What must be true.** A boundary (padding, membrane, frame) acts as a shutter: it prevents runaway reflection and makes measurement possible.  
**Therefore false.** Boundaries are external conveniences, not operational necessities.  

**Domain lens.** Interfaces, inheritance, feedback loops, and embodied constraints. Membranes/boundaries and signaling/coupling stabilize forms.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### ComputationByLocation — Logic
**What must be true.** Some computations are navigation: the query is an address in a pre-existing lattice.  
**Therefore false.** All computation must be temporal generation from scratch.  

**Domain lens.** Predicates, constraints, and inference contracts. Model as types, relations, and proofs within a constraint system.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### ComputationByLocation — Computation
**What must be true.** Some computations are navigation: the query is an address in a pre-existing lattice.  
**Therefore false.** All computation must be temporal generation from scratch.  

**Domain lens.** Programs, state, traces, and projection of internal variables. Model as functions over state spaces; tests lock invariants.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### ComputationByLocation — Physics
**What must be true.** Some computations are navigation: the query is an address in a pre-existing lattice.  
**Therefore false.** All computation must be temporal generation from scratch.  

**Domain lens.** Symmetries, boundary conditions, carriers, and observable projections. Measurements are projections; residue encodes hidden state.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### ComputationByLocation — Biology
**What must be true.** Some computations are navigation: the query is an address in a pre-existing lattice.  
**Therefore false.** All computation must be temporal generation from scratch.  

**Domain lens.** Interfaces, inheritance, feedback loops, and embodied constraints. Membranes/boundaries and signaling/coupling stabilize forms.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### AddressableConstants — Logic
**What must be true.** Constants behave like addressable ROM under the right access law; digits can be ‘looked up’ by index.  
**Therefore false.** Digits exist only as a sequential process; random access is impossible in principle.  

**Domain lens.** Predicates, constraints, and inference contracts. Model as types, relations, and proofs within a constraint system.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### AddressableConstants — Computation
**What must be true.** Constants behave like addressable ROM under the right access law; digits can be ‘looked up’ by index.  
**Therefore false.** Digits exist only as a sequential process; random access is impossible in principle.  

**Domain lens.** Programs, state, traces, and projection of internal variables. Model as functions over state spaces; tests lock invariants.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### AddressableConstants — Physics
**What must be true.** Constants behave like addressable ROM under the right access law; digits can be ‘looked up’ by index.  
**Therefore false.** Digits exist only as a sequential process; random access is impossible in principle.  

**Domain lens.** Symmetries, boundary conditions, carriers, and observable projections. Measurements are projections; residue encodes hidden state.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### AddressableConstants — Biology
**What must be true.** Constants behave like addressable ROM under the right access law; digits can be ‘looked up’ by index.  
**Therefore false.** Digits exist only as a sequential process; random access is impossible in principle.  

**Domain lens.** Interfaces, inheritance, feedback loops, and embodied constraints. Membranes/boundaries and signaling/coupling stabilize forms.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### ScarLedger — Logic
**What must be true.** Residues can be logged as a ledger: signatures of discarded degrees of freedom.  
**Therefore false.** Residues are noise with no informational value.  

**Domain lens.** Predicates, constraints, and inference contracts. Model as types, relations, and proofs within a constraint system.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### ScarLedger — Computation
**What must be true.** Residues can be logged as a ledger: signatures of discarded degrees of freedom.  
**Therefore false.** Residues are noise with no informational value.  

**Domain lens.** Programs, state, traces, and projection of internal variables. Model as functions over state spaces; tests lock invariants.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### ScarLedger — Physics
**What must be true.** Residues can be logged as a ledger: signatures of discarded degrees of freedom.  
**Therefore false.** Residues are noise with no informational value.  

**Domain lens.** Symmetries, boundary conditions, carriers, and observable projections. Measurements are projections; residue encodes hidden state.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### ScarLedger — Biology
**What must be true.** Residues can be logged as a ledger: signatures of discarded degrees of freedom.  
**Therefore false.** Residues are noise with no informational value.  

**Domain lens.** Interfaces, inheritance, feedback loops, and embodied constraints. Membranes/boundaries and signaling/coupling stabilize forms.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### DetuneRevealsHandedness — Logic
**What must be true.** Small detunes can steer coherent structures while leaving nulls statistically flat (handedness test).  
**Therefore false.** Structured and random inputs respond identically to detune.  

**Domain lens.** Predicates, constraints, and inference contracts. Model as types, relations, and proofs within a constraint system.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### DetuneRevealsHandedness — Computation
**What must be true.** Small detunes can steer coherent structures while leaving nulls statistically flat (handedness test).  
**Therefore false.** Structured and random inputs respond identically to detune.  

**Domain lens.** Programs, state, traces, and projection of internal variables. Model as functions over state spaces; tests lock invariants.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### DetuneRevealsHandedness — Physics
**What must be true.** Small detunes can steer coherent structures while leaving nulls statistically flat (handedness test).  
**Therefore false.** Structured and random inputs respond identically to detune.  

**Domain lens.** Symmetries, boundary conditions, carriers, and observable projections. Measurements are projections; residue encodes hidden state.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### DetuneRevealsHandedness — Biology
**What must be true.** Small detunes can steer coherent structures while leaving nulls statistically flat (handedness test).  
**Therefore false.** Structured and random inputs respond identically to detune.  

**Domain lens.** Interfaces, inheritance, feedback loops, and embodied constraints. Membranes/boundaries and signaling/coupling stabilize forms.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### LaneSelectionInvariant — Logic
**What must be true.** Winner lanes emerge from invariant geometry, not from labels.  
**Therefore false.** Lane wins are arbitrary artifacts of representation.  

**Domain lens.** Predicates, constraints, and inference contracts. Model as types, relations, and proofs within a constraint system.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### LaneSelectionInvariant — Computation
**What must be true.** Winner lanes emerge from invariant geometry, not from labels.  
**Therefore false.** Lane wins are arbitrary artifacts of representation.  

**Domain lens.** Programs, state, traces, and projection of internal variables. Model as functions over state spaces; tests lock invariants.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### LaneSelectionInvariant — Physics
**What must be true.** Winner lanes emerge from invariant geometry, not from labels.  
**Therefore false.** Lane wins are arbitrary artifacts of representation.  

**Domain lens.** Symmetries, boundary conditions, carriers, and observable projections. Measurements are projections; residue encodes hidden state.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### LaneSelectionInvariant — Biology
**What must be true.** Winner lanes emerge from invariant geometry, not from labels.  
**Therefore false.** Lane wins are arbitrary artifacts of representation.  

**Domain lens.** Interfaces, inheritance, feedback loops, and embodied constraints. Membranes/boundaries and signaling/coupling stabilize forms.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### OddEvenCarrierSplit — Logic
**What must be true.** Odd/even (or parity) partitions can isolate action-like degrees from structure-like degrees.  
**Therefore false.** Parity carries no operational significance.  

**Domain lens.** Predicates, constraints, and inference contracts. Model as types, relations, and proofs within a constraint system.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### OddEvenCarrierSplit — Computation
**What must be true.** Odd/even (or parity) partitions can isolate action-like degrees from structure-like degrees.  
**Therefore false.** Parity carries no operational significance.  

**Domain lens.** Programs, state, traces, and projection of internal variables. Model as functions over state spaces; tests lock invariants.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### OddEvenCarrierSplit — Physics
**What must be true.** Odd/even (or parity) partitions can isolate action-like degrees from structure-like degrees.  
**Therefore false.** Parity carries no operational significance.  

**Domain lens.** Symmetries, boundary conditions, carriers, and observable projections. Measurements are projections; residue encodes hidden state.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### OddEvenCarrierSplit — Biology
**What must be true.** Odd/even (or parity) partitions can isolate action-like degrees from structure-like degrees.  
**Therefore false.** Parity carries no operational significance.  

**Domain lens.** Interfaces, inheritance, feedback loops, and embodied constraints. Membranes/boundaries and signaling/coupling stabilize forms.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### TriplexCarrier — Logic
**What must be true.** π, φ, e behave as a triad of carriers (cyclic/recursive/exponential) useful for coordinate embeddings.  
**Therefore false.** No stable triad exists; any triple is as good as any other.  

**Domain lens.** Predicates, constraints, and inference contracts. Model as types, relations, and proofs within a constraint system.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### TriplexCarrier — Computation
**What must be true.** π, φ, e behave as a triad of carriers (cyclic/recursive/exponential) useful for coordinate embeddings.  
**Therefore false.** No stable triad exists; any triple is as good as any other.  

**Domain lens.** Programs, state, traces, and projection of internal variables. Model as functions over state spaces; tests lock invariants.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### TriplexCarrier — Physics
**What must be true.** π, φ, e behave as a triad of carriers (cyclic/recursive/exponential) useful for coordinate embeddings.  
**Therefore false.** No stable triad exists; any triple is as good as any other.  

**Domain lens.** Symmetries, boundary conditions, carriers, and observable projections. Measurements are projections; residue encodes hidden state.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### TriplexCarrier — Biology
**What must be true.** π, φ, e behave as a triad of carriers (cyclic/recursive/exponential) useful for coordinate embeddings.  
**Therefore false.** No stable triad exists; any triple is as good as any other.  

**Domain lens.** Interfaces, inheritance, feedback loops, and embodied constraints. Membranes/boundaries and signaling/coupling stabilize forms.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### HAttractor — Logic
**What must be true.** A stable attractor H (e.g., π/9) can act as a phase-lock for multi-domain alignment experiments.  
**Therefore false.** Any H works; attractors are after-the-fact fits.  

**Domain lens.** Predicates, constraints, and inference contracts. Model as types, relations, and proofs within a constraint system.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### HAttractor — Computation
**What must be true.** A stable attractor H (e.g., π/9) can act as a phase-lock for multi-domain alignment experiments.  
**Therefore false.** Any H works; attractors are after-the-fact fits.  

**Domain lens.** Programs, state, traces, and projection of internal variables. Model as functions over state spaces; tests lock invariants.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### HAttractor — Physics
**What must be true.** A stable attractor H (e.g., π/9) can act as a phase-lock for multi-domain alignment experiments.  
**Therefore false.** Any H works; attractors are after-the-fact fits.  

**Domain lens.** Symmetries, boundary conditions, carriers, and observable projections. Measurements are projections; residue encodes hidden state.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### HAttractor — Biology
**What must be true.** A stable attractor H (e.g., π/9) can act as a phase-lock for multi-domain alignment experiments.  
**Therefore false.** Any H works; attractors are after-the-fact fits.  

**Domain lens.** Interfaces, inheritance, feedback loops, and embodied constraints. Membranes/boundaries and signaling/coupling stabilize forms.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### OOPAsSubstrate — Logic
**What must be true.** OOP is a lens for reality: interfaces, inheritance, polymorphism correspond to stable contracts across scales.  
**Therefore false.** OOP is purely human convention with no structural counterpart.  

**Domain lens.** Predicates, constraints, and inference contracts. Model as types, relations, and proofs within a constraint system.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### OOPAsSubstrate — Computation
**What must be true.** OOP is a lens for reality: interfaces, inheritance, polymorphism correspond to stable contracts across scales.  
**Therefore false.** OOP is purely human convention with no structural counterpart.  

**Domain lens.** Programs, state, traces, and projection of internal variables. Model as functions over state spaces; tests lock invariants.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### OOPAsSubstrate — Physics
**What must be true.** OOP is a lens for reality: interfaces, inheritance, polymorphism correspond to stable contracts across scales.  
**Therefore false.** OOP is purely human convention with no structural counterpart.  

**Domain lens.** Symmetries, boundary conditions, carriers, and observable projections. Measurements are projections; residue encodes hidden state.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### OOPAsSubstrate — Biology
**What must be true.** OOP is a lens for reality: interfaces, inheritance, polymorphism correspond to stable contracts across scales.  
**Therefore false.** OOP is purely human convention with no structural counterpart.  

**Domain lens.** Interfaces, inheritance, feedback loops, and embodied constraints. Membranes/boundaries and signaling/coupling stabilize forms.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### BoundedContexts — Logic
**What must be true.** Clarity requires bounded contexts: each domain owns its language and invariants; translations need anti-corruption layers.  
**Therefore false.** One language can safely describe all levels without loss.  

**Domain lens.** Predicates, constraints, and inference contracts. Model as types, relations, and proofs within a constraint system.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### BoundedContexts — Computation
**What must be true.** Clarity requires bounded contexts: each domain owns its language and invariants; translations need anti-corruption layers.  
**Therefore false.** One language can safely describe all levels without loss.  

**Domain lens.** Programs, state, traces, and projection of internal variables. Model as functions over state spaces; tests lock invariants.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### BoundedContexts — Physics
**What must be true.** Clarity requires bounded contexts: each domain owns its language and invariants; translations need anti-corruption layers.  
**Therefore false.** One language can safely describe all levels without loss.  

**Domain lens.** Symmetries, boundary conditions, carriers, and observable projections. Measurements are projections; residue encodes hidden state.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### BoundedContexts — Biology
**What must be true.** Clarity requires bounded contexts: each domain owns its language and invariants; translations need anti-corruption layers.  
**Therefore false.** One language can safely describe all levels without loss.  

**Domain lens.** Interfaces, inheritance, feedback loops, and embodied constraints. Membranes/boundaries and signaling/coupling stabilize forms.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### PortsAndAdapters — Logic
**What must be true.** Truth claims must be testable through explicit ports and adapters; IO is separated from invariants.  
**Therefore false.** Systems can be validated without separating domain from infrastructure.  

**Domain lens.** Predicates, constraints, and inference contracts. Model as types, relations, and proofs within a constraint system.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### PortsAndAdapters — Computation
**What must be true.** Truth claims must be testable through explicit ports and adapters; IO is separated from invariants.  
**Therefore false.** Systems can be validated without separating domain from infrastructure.  

**Domain lens.** Programs, state, traces, and projection of internal variables. Model as functions over state spaces; tests lock invariants.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### PortsAndAdapters — Physics
**What must be true.** Truth claims must be testable through explicit ports and adapters; IO is separated from invariants.  
**Therefore false.** Systems can be validated without separating domain from infrastructure.  

**Domain lens.** Symmetries, boundary conditions, carriers, and observable projections. Measurements are projections; residue encodes hidden state.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### PortsAndAdapters — Biology
**What must be true.** Truth claims must be testable through explicit ports and adapters; IO is separated from invariants.  
**Therefore false.** Systems can be validated without separating domain from infrastructure.  

**Domain lens.** Interfaces, inheritance, feedback loops, and embodied constraints. Membranes/boundaries and signaling/coupling stabilize forms.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### EntropyAsDiscard — Logic
**What must be true.** What we call ‘entropy increase’ often presents as progressive projection and loss of recoverable channels.  
**Therefore false.** Entropy is an intrinsic substance, not a bookkeeping effect.  

**Domain lens.** Predicates, constraints, and inference contracts. Model as types, relations, and proofs within a constraint system.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### EntropyAsDiscard — Computation
**What must be true.** What we call ‘entropy increase’ often presents as progressive projection and loss of recoverable channels.  
**Therefore false.** Entropy is an intrinsic substance, not a bookkeeping effect.  

**Domain lens.** Programs, state, traces, and projection of internal variables. Model as functions over state spaces; tests lock invariants.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### EntropyAsDiscard — Physics
**What must be true.** What we call ‘entropy increase’ often presents as progressive projection and loss of recoverable channels.  
**Therefore false.** Entropy is an intrinsic substance, not a bookkeeping effect.  

**Domain lens.** Symmetries, boundary conditions, carriers, and observable projections. Measurements are projections; residue encodes hidden state.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### EntropyAsDiscard — Biology
**What must be true.** What we call ‘entropy increase’ often presents as progressive projection and loss of recoverable channels.  
**Therefore false.** Entropy is an intrinsic substance, not a bookkeeping effect.  

**Domain lens.** Interfaces, inheritance, feedback loops, and embodied constraints. Membranes/boundaries and signaling/coupling stabilize forms.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### FalsifiabilityAsInterface — Logic
**What must be true.** A truth claim is a callable interface: it must define inputs, outputs, invariants, and failure modes.  
**Therefore false.** Truth claims can remain unfalsifiable and still be useful.  

**Domain lens.** Predicates, constraints, and inference contracts. Model as types, relations, and proofs within a constraint system.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### FalsifiabilityAsInterface — Computation
**What must be true.** A truth claim is a callable interface: it must define inputs, outputs, invariants, and failure modes.  
**Therefore false.** Truth claims can remain unfalsifiable and still be useful.  

**Domain lens.** Programs, state, traces, and projection of internal variables. Model as functions over state spaces; tests lock invariants.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### FalsifiabilityAsInterface — Physics
**What must be true.** A truth claim is a callable interface: it must define inputs, outputs, invariants, and failure modes.  
**Therefore false.** Truth claims can remain unfalsifiable and still be useful.  

**Domain lens.** Symmetries, boundary conditions, carriers, and observable projections. Measurements are projections; residue encodes hidden state.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### FalsifiabilityAsInterface — Biology
**What must be true.** A truth claim is a callable interface: it must define inputs, outputs, invariants, and failure modes.  
**Therefore false.** Truth claims can remain unfalsifiable and still be useful.  

**Domain lens.** Interfaces, inheritance, feedback loops, and embodied constraints. Membranes/boundaries and signaling/coupling stabilize forms.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### HashAsProjection — Logic
**What must be true.** A digest is a projection of a fuller computational trace; security rests on which channels are kept private.  
**Therefore false.** A digest is an intrinsically one-way ontological object.  

**Domain lens.** Predicates, constraints, and inference contracts. Model as types, relations, and proofs within a constraint system.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### HashAsProjection — Computation
**What must be true.** A digest is a projection of a fuller computational trace; security rests on which channels are kept private.  
**Therefore false.** A digest is an intrinsically one-way ontological object.  

**Domain lens.** Programs, state, traces, and projection of internal variables. Model as functions over state spaces; tests lock invariants.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### HashAsProjection — Physics
**What must be true.** A digest is a projection of a fuller computational trace; security rests on which channels are kept private.  
**Therefore false.** A digest is an intrinsically one-way ontological object.  

**Domain lens.** Symmetries, boundary conditions, carriers, and observable projections. Measurements are projections; residue encodes hidden state.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### HashAsProjection — Biology
**What must be true.** A digest is a projection of a fuller computational trace; security rests on which channels are kept private.  
**Therefore false.** A digest is an intrinsically one-way ontological object.  

**Domain lens.** Interfaces, inheritance, feedback loops, and embodied constraints. Membranes/boundaries and signaling/coupling stabilize forms.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### ARXAsGeometry — Logic
**What must be true.** Add-Rotate-XOR is geometry on word lattices: coupling + polarization + selection.  
**Therefore false.** ARX is a bag of tricks with no geometric interpretation.  

**Domain lens.** Predicates, constraints, and inference contracts. Model as types, relations, and proofs within a constraint system.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### ARXAsGeometry — Computation
**What must be true.** Add-Rotate-XOR is geometry on word lattices: coupling + polarization + selection.  
**Therefore false.** ARX is a bag of tricks with no geometric interpretation.  

**Domain lens.** Programs, state, traces, and projection of internal variables. Model as functions over state spaces; tests lock invariants.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### ARXAsGeometry — Physics
**What must be true.** Add-Rotate-XOR is geometry on word lattices: coupling + polarization + selection.  
**Therefore false.** ARX is a bag of tricks with no geometric interpretation.  

**Domain lens.** Symmetries, boundary conditions, carriers, and observable projections. Measurements are projections; residue encodes hidden state.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### ARXAsGeometry — Biology
**What must be true.** Add-Rotate-XOR is geometry on word lattices: coupling + polarization + selection.  
**Therefore false.** ARX is a bag of tricks with no geometric interpretation.  

**Domain lens.** Interfaces, inheritance, feedback loops, and embodied constraints. Membranes/boundaries and signaling/coupling stabilize forms.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### CarryIsHiddenState — Logic
**What must be true.** Carry is a hidden state channel: modular add publishes sum but discards carry history.  
**Therefore false.** Carry is irrelevant once modded.  

**Domain lens.** Predicates, constraints, and inference contracts. Model as types, relations, and proofs within a constraint system.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### CarryIsHiddenState — Computation
**What must be true.** Carry is a hidden state channel: modular add publishes sum but discards carry history.  
**Therefore false.** Carry is irrelevant once modded.  

**Domain lens.** Programs, state, traces, and projection of internal variables. Model as functions over state spaces; tests lock invariants.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### CarryIsHiddenState — Physics
**What must be true.** Carry is a hidden state channel: modular add publishes sum but discards carry history.  
**Therefore false.** Carry is irrelevant once modded.  

**Domain lens.** Symmetries, boundary conditions, carriers, and observable projections. Measurements are projections; residue encodes hidden state.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### CarryIsHiddenState — Biology
**What must be true.** Carry is a hidden state channel: modular add publishes sum but discards carry history.  
**Therefore false.** Carry is irrelevant once modded.  

**Domain lens.** Interfaces, inheritance, feedback loops, and embodied constraints. Membranes/boundaries and signaling/coupling stabilize forms.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### UIHairpinTurn — Logic
**What must be true.** UI is a reflection operator: visualization is a new Δ that changes what the system can lock onto.  
**Therefore false.** UI is decoration and should not affect inference.  

**Domain lens.** Predicates, constraints, and inference contracts. Model as types, relations, and proofs within a constraint system.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### UIHairpinTurn — Computation
**What must be true.** UI is a reflection operator: visualization is a new Δ that changes what the system can lock onto.  
**Therefore false.** UI is decoration and should not affect inference.  

**Domain lens.** Programs, state, traces, and projection of internal variables. Model as functions over state spaces; tests lock invariants.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### UIHairpinTurn — Physics
**What must be true.** UI is a reflection operator: visualization is a new Δ that changes what the system can lock onto.  
**Therefore false.** UI is decoration and should not affect inference.  

**Domain lens.** Symmetries, boundary conditions, carriers, and observable projections. Measurements are projections; residue encodes hidden state.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### UIHairpinTurn — Biology
**What must be true.** UI is a reflection operator: visualization is a new Δ that changes what the system can lock onto.  
**Therefore false.** UI is decoration and should not affect inference.  

**Domain lens.** Interfaces, inheritance, feedback loops, and embodied constraints. Membranes/boundaries and signaling/coupling stabilize forms.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### SpectrumNotScalar — Logic
**What must be true.** Many invariants are spectral (distributions, histograms, eigenmodes), not single numbers.  
**Therefore false.** Single-point metrics are sufficient to characterize complex systems.  

**Domain lens.** Predicates, constraints, and inference contracts. Model as types, relations, and proofs within a constraint system.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### SpectrumNotScalar — Computation
**What must be true.** Many invariants are spectral (distributions, histograms, eigenmodes), not single numbers.  
**Therefore false.** Single-point metrics are sufficient to characterize complex systems.  

**Domain lens.** Programs, state, traces, and projection of internal variables. Model as functions over state spaces; tests lock invariants.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### SpectrumNotScalar — Physics
**What must be true.** Many invariants are spectral (distributions, histograms, eigenmodes), not single numbers.  
**Therefore false.** Single-point metrics are sufficient to characterize complex systems.  

**Domain lens.** Symmetries, boundary conditions, carriers, and observable projections. Measurements are projections; residue encodes hidden state.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### SpectrumNotScalar — Biology
**What must be true.** Many invariants are spectral (distributions, histograms, eigenmodes), not single numbers.  
**Therefore false.** Single-point metrics are sufficient to characterize complex systems.  

**Domain lens.** Interfaces, inheritance, feedback loops, and embodied constraints. Membranes/boundaries and signaling/coupling stabilize forms.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### ChiralResidue — Logic
**What must be true.** Residue can encode chirality (handedness) when symmetry is slightly broken.  
**Therefore false.** Residue is symmetric and cannot carry handedness.  

**Domain lens.** Predicates, constraints, and inference contracts. Model as types, relations, and proofs within a constraint system.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### ChiralResidue — Computation
**What must be true.** Residue can encode chirality (handedness) when symmetry is slightly broken.  
**Therefore false.** Residue is symmetric and cannot carry handedness.  

**Domain lens.** Programs, state, traces, and projection of internal variables. Model as functions over state spaces; tests lock invariants.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### ChiralResidue — Physics
**What must be true.** Residue can encode chirality (handedness) when symmetry is slightly broken.  
**Therefore false.** Residue is symmetric and cannot carry handedness.  

**Domain lens.** Symmetries, boundary conditions, carriers, and observable projections. Measurements are projections; residue encodes hidden state.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### ChiralResidue — Biology
**What must be true.** Residue can encode chirality (handedness) when symmetry is slightly broken.  
**Therefore false.** Residue is symmetric and cannot carry handedness.  

**Domain lens.** Interfaces, inheritance, feedback loops, and embodied constraints. Membranes/boundaries and signaling/coupling stabilize forms.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### ParityBitAsSpin — Logic
**What must be true.** The leftover bit in a coordinate slicing can be treated as spin/parity to select a handed branch.  
**Therefore false.** Leftover bits are meaningless waste.  

**Domain lens.** Predicates, constraints, and inference contracts. Model as types, relations, and proofs within a constraint system.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### ParityBitAsSpin — Computation
**What must be true.** The leftover bit in a coordinate slicing can be treated as spin/parity to select a handed branch.  
**Therefore false.** Leftover bits are meaningless waste.  

**Domain lens.** Programs, state, traces, and projection of internal variables. Model as functions over state spaces; tests lock invariants.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### ParityBitAsSpin — Physics
**What must be true.** The leftover bit in a coordinate slicing can be treated as spin/parity to select a handed branch.  
**Therefore false.** Leftover bits are meaningless waste.  

**Domain lens.** Symmetries, boundary conditions, carriers, and observable projections. Measurements are projections; residue encodes hidden state.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### ParityBitAsSpin — Biology
**What must be true.** The leftover bit in a coordinate slicing can be treated as spin/parity to select a handed branch.  
**Therefore false.** Leftover bits are meaningless waste.  

**Domain lens.** Interfaces, inheritance, feedback loops, and embodied constraints. Membranes/boundaries and signaling/coupling stabilize forms.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### MeshAsAuditArtifact — Logic
**What must be true.** Geometry outputs (meshes) are audit artifacts: they preserve a structural fingerprint useful for comparison.  
**Therefore false.** Meshes are arbitrary renderings unrelated to the underlying computation.  

**Domain lens.** Predicates, constraints, and inference contracts. Model as types, relations, and proofs within a constraint system.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### MeshAsAuditArtifact — Computation
**What must be true.** Geometry outputs (meshes) are audit artifacts: they preserve a structural fingerprint useful for comparison.  
**Therefore false.** Meshes are arbitrary renderings unrelated to the underlying computation.  

**Domain lens.** Programs, state, traces, and projection of internal variables. Model as functions over state spaces; tests lock invariants.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### MeshAsAuditArtifact — Physics
**What must be true.** Geometry outputs (meshes) are audit artifacts: they preserve a structural fingerprint useful for comparison.  
**Therefore false.** Meshes are arbitrary renderings unrelated to the underlying computation.  

**Domain lens.** Symmetries, boundary conditions, carriers, and observable projections. Measurements are projections; residue encodes hidden state.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### MeshAsAuditArtifact — Biology
**What must be true.** Geometry outputs (meshes) are audit artifacts: they preserve a structural fingerprint useful for comparison.  
**Therefore false.** Meshes are arbitrary renderings unrelated to the underlying computation.  

**Domain lens.** Interfaces, inheritance, feedback loops, and embodied constraints. Membranes/boundaries and signaling/coupling stabilize forms.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### InvariantFirstDesign — Logic
**What must be true.** Architecture should start from invariants: define what must be true before building workflows and adapters.  
**Therefore false.** Workflows can come first; invariants can be ‘filled in’ later.  

**Domain lens.** Predicates, constraints, and inference contracts. Model as types, relations, and proofs within a constraint system.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### InvariantFirstDesign — Computation
**What must be true.** Architecture should start from invariants: define what must be true before building workflows and adapters.  
**Therefore false.** Workflows can come first; invariants can be ‘filled in’ later.  

**Domain lens.** Programs, state, traces, and projection of internal variables. Model as functions over state spaces; tests lock invariants.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### InvariantFirstDesign — Physics
**What must be true.** Architecture should start from invariants: define what must be true before building workflows and adapters.  
**Therefore false.** Workflows can come first; invariants can be ‘filled in’ later.  

**Domain lens.** Symmetries, boundary conditions, carriers, and observable projections. Measurements are projections; residue encodes hidden state.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### InvariantFirstDesign — Biology
**What must be true.** Architecture should start from invariants: define what must be true before building workflows and adapters.  
**Therefore false.** Workflows can come first; invariants can be ‘filled in’ later.  

**Domain lens.** Interfaces, inheritance, feedback loops, and embodied constraints. Membranes/boundaries and signaling/coupling stabilize forms.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### WhyChain — Logic
**What must be true.** Proof discovery is a ‘why’ chain: recurse until you find the constraint that makes the claim necessary.  
**Therefore false.** Proof is a matter of authority or convention.  

**Domain lens.** Predicates, constraints, and inference contracts. Model as types, relations, and proofs within a constraint system.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### WhyChain — Computation
**What must be true.** Proof discovery is a ‘why’ chain: recurse until you find the constraint that makes the claim necessary.  
**Therefore false.** Proof is a matter of authority or convention.  

**Domain lens.** Programs, state, traces, and projection of internal variables. Model as functions over state spaces; tests lock invariants.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### WhyChain — Physics
**What must be true.** Proof discovery is a ‘why’ chain: recurse until you find the constraint that makes the claim necessary.  
**Therefore false.** Proof is a matter of authority or convention.  

**Domain lens.** Symmetries, boundary conditions, carriers, and observable projections. Measurements are projections; residue encodes hidden state.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### WhyChain — Biology
**What must be true.** Proof discovery is a ‘why’ chain: recurse until you find the constraint that makes the claim necessary.  
**Therefore false.** Proof is a matter of authority or convention.  

**Domain lens.** Interfaces, inheritance, feedback loops, and embodied constraints. Membranes/boundaries and signaling/coupling stabilize forms.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### Localization — Logic
**What must be true.** Information flow can localize under certain operator regimes (Anderson-like), producing stable pockets of structure.  
**Therefore false.** Information always diffuses uniformly in large systems.  

**Domain lens.** Predicates, constraints, and inference contracts. Model as types, relations, and proofs within a constraint system.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### Localization — Computation
**What must be true.** Information flow can localize under certain operator regimes (Anderson-like), producing stable pockets of structure.  
**Therefore false.** Information always diffuses uniformly in large systems.  

**Domain lens.** Programs, state, traces, and projection of internal variables. Model as functions over state spaces; tests lock invariants.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### Localization — Physics
**What must be true.** Information flow can localize under certain operator regimes (Anderson-like), producing stable pockets of structure.  
**Therefore false.** Information always diffuses uniformly in large systems.  

**Domain lens.** Symmetries, boundary conditions, carriers, and observable projections. Measurements are projections; residue encodes hidden state.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### Localization — Biology
**What must be true.** Information flow can localize under certain operator regimes (Anderson-like), producing stable pockets of structure.  
**Therefore false.** Information always diffuses uniformly in large systems.  

**Domain lens.** Interfaces, inheritance, feedback loops, and embodied constraints. Membranes/boundaries and signaling/coupling stabilize forms.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### TransferMatrix — Logic
**What must be true.** Transfer matrices track how operators move amplitude/structure through layers; they are natural for ‘gap’ analysis.  
**Therefore false.** Layer-by-layer propagation is not modelable in matrix terms.  

**Domain lens.** Predicates, constraints, and inference contracts. Model as types, relations, and proofs within a constraint system.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### TransferMatrix — Computation
**What must be true.** Transfer matrices track how operators move amplitude/structure through layers; they are natural for ‘gap’ analysis.  
**Therefore false.** Layer-by-layer propagation is not modelable in matrix terms.  

**Domain lens.** Programs, state, traces, and projection of internal variables. Model as functions over state spaces; tests lock invariants.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### TransferMatrix — Physics
**What must be true.** Transfer matrices track how operators move amplitude/structure through layers; they are natural for ‘gap’ analysis.  
**Therefore false.** Layer-by-layer propagation is not modelable in matrix terms.  

**Domain lens.** Symmetries, boundary conditions, carriers, and observable projections. Measurements are projections; residue encodes hidden state.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### TransferMatrix — Biology
**What must be true.** Transfer matrices track how operators move amplitude/structure through layers; they are natural for ‘gap’ analysis.  
**Therefore false.** Layer-by-layer propagation is not modelable in matrix terms.  

**Domain lens.** Interfaces, inheritance, feedback loops, and embodied constraints. Membranes/boundaries and signaling/coupling stabilize forms.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### DualClock — Logic
**What must be true.** Systems can have two clocks: internal recursion rate and external observation rate; mismatch generates drift.  
**Therefore false.** All clocks are equivalent under scaling.  

**Domain lens.** Predicates, constraints, and inference contracts. Model as types, relations, and proofs within a constraint system.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### DualClock — Computation
**What must be true.** Systems can have two clocks: internal recursion rate and external observation rate; mismatch generates drift.  
**Therefore false.** All clocks are equivalent under scaling.  

**Domain lens.** Programs, state, traces, and projection of internal variables. Model as functions over state spaces; tests lock invariants.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### DualClock — Physics
**What must be true.** Systems can have two clocks: internal recursion rate and external observation rate; mismatch generates drift.  
**Therefore false.** All clocks are equivalent under scaling.  

**Domain lens.** Symmetries, boundary conditions, carriers, and observable projections. Measurements are projections; residue encodes hidden state.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### DualClock — Biology
**What must be true.** Systems can have two clocks: internal recursion rate and external observation rate; mismatch generates drift.  
**Therefore false.** All clocks are equivalent under scaling.  

**Domain lens.** Interfaces, inheritance, feedback loops, and embodied constraints. Membranes/boundaries and signaling/coupling stabilize forms.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### DriftAsSignal — Logic
**What must be true.** Drift is not error; it is a steering signal indicating a mismatch between frames/transforms.  
**Therefore false.** Drift is noise and should be ignored.  

**Domain lens.** Predicates, constraints, and inference contracts. Model as types, relations, and proofs within a constraint system.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### DriftAsSignal — Computation
**What must be true.** Drift is not error; it is a steering signal indicating a mismatch between frames/transforms.  
**Therefore false.** Drift is noise and should be ignored.  

**Domain lens.** Programs, state, traces, and projection of internal variables. Model as functions over state spaces; tests lock invariants.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### DriftAsSignal — Physics
**What must be true.** Drift is not error; it is a steering signal indicating a mismatch between frames/transforms.  
**Therefore false.** Drift is noise and should be ignored.  

**Domain lens.** Symmetries, boundary conditions, carriers, and observable projections. Measurements are projections; residue encodes hidden state.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### DriftAsSignal — Biology
**What must be true.** Drift is not error; it is a steering signal indicating a mismatch between frames/transforms.  
**Therefore false.** Drift is noise and should be ignored.  

**Domain lens.** Interfaces, inheritance, feedback loops, and embodied constraints. Membranes/boundaries and signaling/coupling stabilize forms.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### SignedResidue — Logic
**What must be true.** Residues are signed; the sign is ‘which-path’ information (branch choice) under symmetric potentials.  
**Therefore false.** Only magnitude matters; sign is arbitrary.  

**Domain lens.** Predicates, constraints, and inference contracts. Model as types, relations, and proofs within a constraint system.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### SignedResidue — Computation
**What must be true.** Residues are signed; the sign is ‘which-path’ information (branch choice) under symmetric potentials.  
**Therefore false.** Only magnitude matters; sign is arbitrary.  

**Domain lens.** Programs, state, traces, and projection of internal variables. Model as functions over state spaces; tests lock invariants.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### SignedResidue — Physics
**What must be true.** Residues are signed; the sign is ‘which-path’ information (branch choice) under symmetric potentials.  
**Therefore false.** Only magnitude matters; sign is arbitrary.  

**Domain lens.** Symmetries, boundary conditions, carriers, and observable projections. Measurements are projections; residue encodes hidden state.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### SignedResidue — Biology
**What must be true.** Residues are signed; the sign is ‘which-path’ information (branch choice) under symmetric potentials.  
**Therefore false.** Only magnitude matters; sign is arbitrary.  

**Domain lens.** Interfaces, inheritance, feedback loops, and embodied constraints. Membranes/boundaries and signaling/coupling stabilize forms.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### PhaseLocking — Logic
**What must be true.** Phase locking is a computational primitive: align carriers to reduce effective search dimensionality.  
**Therefore false.** Alignment is post-hoc patterning without causal force.  

**Domain lens.** Predicates, constraints, and inference contracts. Model as types, relations, and proofs within a constraint system.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### PhaseLocking — Computation
**What must be true.** Phase locking is a computational primitive: align carriers to reduce effective search dimensionality.  
**Therefore false.** Alignment is post-hoc patterning without causal force.  

**Domain lens.** Programs, state, traces, and projection of internal variables. Model as functions over state spaces; tests lock invariants.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### PhaseLocking — Physics
**What must be true.** Phase locking is a computational primitive: align carriers to reduce effective search dimensionality.  
**Therefore false.** Alignment is post-hoc patterning without causal force.  

**Domain lens.** Symmetries, boundary conditions, carriers, and observable projections. Measurements are projections; residue encodes hidden state.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### PhaseLocking — Biology
**What must be true.** Phase locking is a computational primitive: align carriers to reduce effective search dimensionality.  
**Therefore false.** Alignment is post-hoc patterning without causal force.  

**Domain lens.** Interfaces, inheritance, feedback loops, and embodied constraints. Membranes/boundaries and signaling/coupling stabilize forms.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### WeirdMachine — Logic
**What must be true.** Non-obvious interpreter paths (weird machines) arise when constraints create unintended computation channels.  
**Therefore false.** Execution is fully described by the stated program semantics.  

**Domain lens.** Predicates, constraints, and inference contracts. Model as types, relations, and proofs within a constraint system.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### WeirdMachine — Computation
**What must be true.** Non-obvious interpreter paths (weird machines) arise when constraints create unintended computation channels.  
**Therefore false.** Execution is fully described by the stated program semantics.  

**Domain lens.** Programs, state, traces, and projection of internal variables. Model as functions over state spaces; tests lock invariants.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### WeirdMachine — Physics
**What must be true.** Non-obvious interpreter paths (weird machines) arise when constraints create unintended computation channels.  
**Therefore false.** Execution is fully described by the stated program semantics.  

**Domain lens.** Symmetries, boundary conditions, carriers, and observable projections. Measurements are projections; residue encodes hidden state.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### WeirdMachine — Biology
**What must be true.** Non-obvious interpreter paths (weird machines) arise when constraints create unintended computation channels.  
**Therefore false.** Execution is fully described by the stated program semantics.  

**Domain lens.** Interfaces, inheritance, feedback loops, and embodied constraints. Membranes/boundaries and signaling/coupling stabilize forms.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### MinimalOperators — Logic
**What must be true.** A small operator basis (+, =, ↻, ⊥) can generate large classes of behavior via composition.  
**Therefore false.** You need domain-specific primitives for each phenomenon.  

**Domain lens.** Predicates, constraints, and inference contracts. Model as types, relations, and proofs within a constraint system.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### MinimalOperators — Computation
**What must be true.** A small operator basis (+, =, ↻, ⊥) can generate large classes of behavior via composition.  
**Therefore false.** You need domain-specific primitives for each phenomenon.  

**Domain lens.** Programs, state, traces, and projection of internal variables. Model as functions over state spaces; tests lock invariants.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### MinimalOperators — Physics
**What must be true.** A small operator basis (+, =, ↻, ⊥) can generate large classes of behavior via composition.  
**Therefore false.** You need domain-specific primitives for each phenomenon.  

**Domain lens.** Symmetries, boundary conditions, carriers, and observable projections. Measurements are projections; residue encodes hidden state.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### MinimalOperators — Biology
**What must be true.** A small operator basis (+, =, ↻, ⊥) can generate large classes of behavior via composition.  
**Therefore false.** You need domain-specific primitives for each phenomenon.  

**Domain lens.** Interfaces, inheritance, feedback loops, and embodied constraints. Membranes/boundaries and signaling/coupling stabilize forms.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### PrecisionBoundary — Logic
**What must be true.** Finite precision introduces a boundary that can alias axes; robust invariants survive shear.  
**Therefore false.** Precision limits make all results meaningless.  

**Domain lens.** Predicates, constraints, and inference contracts. Model as types, relations, and proofs within a constraint system.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### PrecisionBoundary — Computation
**What must be true.** Finite precision introduces a boundary that can alias axes; robust invariants survive shear.  
**Therefore false.** Precision limits make all results meaningless.  

**Domain lens.** Programs, state, traces, and projection of internal variables. Model as functions over state spaces; tests lock invariants.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### PrecisionBoundary — Physics
**What must be true.** Finite precision introduces a boundary that can alias axes; robust invariants survive shear.  
**Therefore false.** Precision limits make all results meaningless.  

**Domain lens.** Symmetries, boundary conditions, carriers, and observable projections. Measurements are projections; residue encodes hidden state.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### PrecisionBoundary — Biology
**What must be true.** Finite precision introduces a boundary that can alias axes; robust invariants survive shear.  
**Therefore false.** Precision limits make all results meaningless.  

**Domain lens.** Interfaces, inheritance, feedback loops, and embodied constraints. Membranes/boundaries and signaling/coupling stabilize forms.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### RecursiveDepth — Logic
**What must be true.** Depth (recursion/continued fraction) is a coordinate distinct from distance; it can be measured when distance aliases.  
**Therefore false.** All coordinates reduce to distance under scaling.  

**Domain lens.** Predicates, constraints, and inference contracts. Model as types, relations, and proofs within a constraint system.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### RecursiveDepth — Computation
**What must be true.** Depth (recursion/continued fraction) is a coordinate distinct from distance; it can be measured when distance aliases.  
**Therefore false.** All coordinates reduce to distance under scaling.  

**Domain lens.** Programs, state, traces, and projection of internal variables. Model as functions over state spaces; tests lock invariants.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### RecursiveDepth — Physics
**What must be true.** Depth (recursion/continued fraction) is a coordinate distinct from distance; it can be measured when distance aliases.  
**Therefore false.** All coordinates reduce to distance under scaling.  

**Domain lens.** Symmetries, boundary conditions, carriers, and observable projections. Measurements are projections; residue encodes hidden state.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### RecursiveDepth — Biology
**What must be true.** Depth (recursion/continued fraction) is a coordinate distinct from distance; it can be measured when distance aliases.  
**Therefore false.** All coordinates reduce to distance under scaling.  

**Domain lens.** Interfaces, inheritance, feedback loops, and embodied constraints. Membranes/boundaries and signaling/coupling stabilize forms.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### CombinatorialAxis — Logic
**What must be true.** Factorial/combinatorial growth is an axis distinct from linear growth; it captures arrangement-state.  
**Therefore false.** Combinatorics is just ‘big numbers’ with no geometric role.  

**Domain lens.** Predicates, constraints, and inference contracts. Model as types, relations, and proofs within a constraint system.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### CombinatorialAxis — Computation
**What must be true.** Factorial/combinatorial growth is an axis distinct from linear growth; it captures arrangement-state.  
**Therefore false.** Combinatorics is just ‘big numbers’ with no geometric role.  

**Domain lens.** Programs, state, traces, and projection of internal variables. Model as functions over state spaces; tests lock invariants.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### CombinatorialAxis — Physics
**What must be true.** Factorial/combinatorial growth is an axis distinct from linear growth; it captures arrangement-state.  
**Therefore false.** Combinatorics is just ‘big numbers’ with no geometric role.  

**Domain lens.** Symmetries, boundary conditions, carriers, and observable projections. Measurements are projections; residue encodes hidden state.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### CombinatorialAxis — Biology
**What must be true.** Factorial/combinatorial growth is an axis distinct from linear growth; it captures arrangement-state.  
**Therefore false.** Combinatorics is just ‘big numbers’ with no geometric role.  

**Domain lens.** Interfaces, inheritance, feedback loops, and embodied constraints. Membranes/boundaries and signaling/coupling stabilize forms.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### CarrierSeparation — Logic
**What must be true.** Separating carrier vs baseband is key: K constants as carrier; message as baseband; digest as modulated output.  
**Therefore false.** There is no carrier; everything is mixed beyond separation.  

**Domain lens.** Predicates, constraints, and inference contracts. Model as types, relations, and proofs within a constraint system.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### CarrierSeparation — Computation
**What must be true.** Separating carrier vs baseband is key: K constants as carrier; message as baseband; digest as modulated output.  
**Therefore false.** There is no carrier; everything is mixed beyond separation.  

**Domain lens.** Programs, state, traces, and projection of internal variables. Model as functions over state spaces; tests lock invariants.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### CarrierSeparation — Physics
**What must be true.** Separating carrier vs baseband is key: K constants as carrier; message as baseband; digest as modulated output.  
**Therefore false.** There is no carrier; everything is mixed beyond separation.  

**Domain lens.** Symmetries, boundary conditions, carriers, and observable projections. Measurements are projections; residue encodes hidden state.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### CarrierSeparation — Biology
**What must be true.** Separating carrier vs baseband is key: K constants as carrier; message as baseband; digest as modulated output.  
**Therefore false.** There is no carrier; everything is mixed beyond separation.  

**Domain lens.** Interfaces, inheritance, feedback loops, and embodied constraints. Membranes/boundaries and signaling/coupling stabilize forms.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### QuantizationGrid — Logic
**What must be true.** Certain operator regimes act as quantization grids (‘autotune’) that snap states onto stable lanes.  
**Therefore false.** Quantization is an artifact of measurement only.  

**Domain lens.** Predicates, constraints, and inference contracts. Model as types, relations, and proofs within a constraint system.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### QuantizationGrid — Computation
**What must be true.** Certain operator regimes act as quantization grids (‘autotune’) that snap states onto stable lanes.  
**Therefore false.** Quantization is an artifact of measurement only.  

**Domain lens.** Programs, state, traces, and projection of internal variables. Model as functions over state spaces; tests lock invariants.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### QuantizationGrid — Physics
**What must be true.** Certain operator regimes act as quantization grids (‘autotune’) that snap states onto stable lanes.  
**Therefore false.** Quantization is an artifact of measurement only.  

**Domain lens.** Symmetries, boundary conditions, carriers, and observable projections. Measurements are projections; residue encodes hidden state.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### QuantizationGrid — Biology
**What must be true.** Certain operator regimes act as quantization grids (‘autotune’) that snap states onto stable lanes.  
**Therefore false.** Quantization is an artifact of measurement only.  

**Domain lens.** Interfaces, inheritance, feedback loops, and embodied constraints. Membranes/boundaries and signaling/coupling stabilize forms.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### HolographicBoundary — Logic
**What must be true.** A boundary can store a compressed signature of the bulk (holographic principle as design pattern).  
**Therefore false.** Boundaries cannot carry information about the bulk.  

**Domain lens.** Predicates, constraints, and inference contracts. Model as types, relations, and proofs within a constraint system.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### HolographicBoundary — Computation
**What must be true.** A boundary can store a compressed signature of the bulk (holographic principle as design pattern).  
**Therefore false.** Boundaries cannot carry information about the bulk.  

**Domain lens.** Programs, state, traces, and projection of internal variables. Model as functions over state spaces; tests lock invariants.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### HolographicBoundary — Physics
**What must be true.** A boundary can store a compressed signature of the bulk (holographic principle as design pattern).  
**Therefore false.** Boundaries cannot carry information about the bulk.  

**Domain lens.** Symmetries, boundary conditions, carriers, and observable projections. Measurements are projections; residue encodes hidden state.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### HolographicBoundary — Biology
**What must be true.** A boundary can store a compressed signature of the bulk (holographic principle as design pattern).  
**Therefore false.** Boundaries cannot carry information about the bulk.  

**Domain lens.** Interfaces, inheritance, feedback loops, and embodied constraints. Membranes/boundaries and signaling/coupling stabilize forms.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### ResidueAsReceipt — Logic
**What must be true.** A residue is a receipt proving computation occurred: it records the work done by projection/coupling.  
**Therefore false.** You can’t tell whether computation happened from outputs.  

**Domain lens.** Predicates, constraints, and inference contracts. Model as types, relations, and proofs within a constraint system.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### ResidueAsReceipt — Computation
**What must be true.** A residue is a receipt proving computation occurred: it records the work done by projection/coupling.  
**Therefore false.** You can’t tell whether computation happened from outputs.  

**Domain lens.** Programs, state, traces, and projection of internal variables. Model as functions over state spaces; tests lock invariants.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### ResidueAsReceipt — Physics
**What must be true.** A residue is a receipt proving computation occurred: it records the work done by projection/coupling.  
**Therefore false.** You can’t tell whether computation happened from outputs.  

**Domain lens.** Symmetries, boundary conditions, carriers, and observable projections. Measurements are projections; residue encodes hidden state.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### ResidueAsReceipt — Biology
**What must be true.** A residue is a receipt proving computation occurred: it records the work done by projection/coupling.  
**Therefore false.** You can’t tell whether computation happened from outputs.  

**Domain lens.** Interfaces, inheritance, feedback loops, and embodied constraints. Membranes/boundaries and signaling/coupling stabilize forms.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### SafetyByDesign — Logic
**What must be true.** Operational claims about cryptographic inversion must be boxed into toy scopes and defensive evaluation.  
**Therefore false.** Any claim can be published as an ‘idea’ regardless of misuse.  

**Domain lens.** Predicates, constraints, and inference contracts. Model as types, relations, and proofs within a constraint system.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### SafetyByDesign — Computation
**What must be true.** Operational claims about cryptographic inversion must be boxed into toy scopes and defensive evaluation.  
**Therefore false.** Any claim can be published as an ‘idea’ regardless of misuse.  

**Domain lens.** Programs, state, traces, and projection of internal variables. Model as functions over state spaces; tests lock invariants.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### SafetyByDesign — Physics
**What must be true.** Operational claims about cryptographic inversion must be boxed into toy scopes and defensive evaluation.  
**Therefore false.** Any claim can be published as an ‘idea’ regardless of misuse.  

**Domain lens.** Symmetries, boundary conditions, carriers, and observable projections. Measurements are projections; residue encodes hidden state.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### SafetyByDesign — Biology
**What must be true.** Operational claims about cryptographic inversion must be boxed into toy scopes and defensive evaluation.  
**Therefore false.** Any claim can be published as an ‘idea’ regardless of misuse.  

**Domain lens.** Interfaces, inheritance, feedback loops, and embodied constraints. Membranes/boundaries and signaling/coupling stabilize forms.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### EvidenceLadders — Logic
**What must be true.** Claims must be organized by evidence ladders: Ψ-closed theorems vs Ω-open hypotheses with tests.  
**Therefore false.** All claims are equal; style can substitute for evidence.  

**Domain lens.** Predicates, constraints, and inference contracts. Model as types, relations, and proofs within a constraint system.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### EvidenceLadders — Computation
**What must be true.** Claims must be organized by evidence ladders: Ψ-closed theorems vs Ω-open hypotheses with tests.  
**Therefore false.** All claims are equal; style can substitute for evidence.  

**Domain lens.** Programs, state, traces, and projection of internal variables. Model as functions over state spaces; tests lock invariants.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### EvidenceLadders — Physics
**What must be true.** Claims must be organized by evidence ladders: Ψ-closed theorems vs Ω-open hypotheses with tests.  
**Therefore false.** All claims are equal; style can substitute for evidence.  

**Domain lens.** Symmetries, boundary conditions, carriers, and observable projections. Measurements are projections; residue encodes hidden state.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### EvidenceLadders — Biology
**What must be true.** Claims must be organized by evidence ladders: Ψ-closed theorems vs Ω-open hypotheses with tests.  
**Therefore false.** All claims are equal; style can substitute for evidence.  

**Domain lens.** Interfaces, inheritance, feedback loops, and embodied constraints. Membranes/boundaries and signaling/coupling stabilize forms.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### Polymorphism — Logic
**What must be true.** Cross-domain mapping must preserve an interface (invariant); everything else is adapter code.  
**Therefore false.** Any similarity implies deep identity.  

**Domain lens.** Predicates, constraints, and inference contracts. Model as types, relations, and proofs within a constraint system.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### Polymorphism — Computation
**What must be true.** Cross-domain mapping must preserve an interface (invariant); everything else is adapter code.  
**Therefore false.** Any similarity implies deep identity.  

**Domain lens.** Programs, state, traces, and projection of internal variables. Model as functions over state spaces; tests lock invariants.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### Polymorphism — Physics
**What must be true.** Cross-domain mapping must preserve an interface (invariant); everything else is adapter code.  
**Therefore false.** Any similarity implies deep identity.  

**Domain lens.** Symmetries, boundary conditions, carriers, and observable projections. Measurements are projections; residue encodes hidden state.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### Polymorphism — Biology
**What must be true.** Cross-domain mapping must preserve an interface (invariant); everything else is adapter code.  
**Therefore false.** Any similarity implies deep identity.  

**Domain lens.** Interfaces, inheritance, feedback loops, and embodied constraints. Membranes/boundaries and signaling/coupling stabilize forms.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### AntiCorruptionLayer — Logic
**What must be true.** Metaphor-to-math translation is an ACL: it prevents conceptual bleed-through.  
**Therefore false.** Metaphors can be treated as proofs.  

**Domain lens.** Predicates, constraints, and inference contracts. Model as types, relations, and proofs within a constraint system.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### AntiCorruptionLayer — Computation
**What must be true.** Metaphor-to-math translation is an ACL: it prevents conceptual bleed-through.  
**Therefore false.** Metaphors can be treated as proofs.  

**Domain lens.** Programs, state, traces, and projection of internal variables. Model as functions over state spaces; tests lock invariants.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### AntiCorruptionLayer — Physics
**What must be true.** Metaphor-to-math translation is an ACL: it prevents conceptual bleed-through.  
**Therefore false.** Metaphors can be treated as proofs.  

**Domain lens.** Symmetries, boundary conditions, carriers, and observable projections. Measurements are projections; residue encodes hidden state.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### AntiCorruptionLayer — Biology
**What must be true.** Metaphor-to-math translation is an ACL: it prevents conceptual bleed-through.  
**Therefore false.** Metaphors can be treated as proofs.  

**Domain lens.** Interfaces, inheritance, feedback loops, and embodied constraints. Membranes/boundaries and signaling/coupling stabilize forms.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### ExecutableGlossary — Logic
**What must be true.** Glossaries should be executable: each term binds to a test or a type signature.  
**Therefore false.** Glossaries are descriptive only.  

**Domain lens.** Predicates, constraints, and inference contracts. Model as types, relations, and proofs within a constraint system.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### ExecutableGlossary — Computation
**What must be true.** Glossaries should be executable: each term binds to a test or a type signature.  
**Therefore false.** Glossaries are descriptive only.  

**Domain lens.** Programs, state, traces, and projection of internal variables. Model as functions over state spaces; tests lock invariants.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### ExecutableGlossary — Physics
**What must be true.** Glossaries should be executable: each term binds to a test or a type signature.  
**Therefore false.** Glossaries are descriptive only.  

**Domain lens.** Symmetries, boundary conditions, carriers, and observable projections. Measurements are projections; residue encodes hidden state.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### ExecutableGlossary — Biology
**What must be true.** Glossaries should be executable: each term binds to a test or a type signature.  
**Therefore false.** Glossaries are descriptive only.  

**Domain lens.** Interfaces, inheritance, feedback loops, and embodied constraints. Membranes/boundaries and signaling/coupling stabilize forms.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### UnitTestsAsProof — Logic
**What must be true.** In engineered domains, unit tests are the operational form of proof under specified assumptions.  
**Therefore false.** Testing is inferior to proof and cannot participate in rigor.  

**Domain lens.** Predicates, constraints, and inference contracts. Model as types, relations, and proofs within a constraint system.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### UnitTestsAsProof — Computation
**What must be true.** In engineered domains, unit tests are the operational form of proof under specified assumptions.  
**Therefore false.** Testing is inferior to proof and cannot participate in rigor.  

**Domain lens.** Programs, state, traces, and projection of internal variables. Model as functions over state spaces; tests lock invariants.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### UnitTestsAsProof — Physics
**What must be true.** In engineered domains, unit tests are the operational form of proof under specified assumptions.  
**Therefore false.** Testing is inferior to proof and cannot participate in rigor.  

**Domain lens.** Symmetries, boundary conditions, carriers, and observable projections. Measurements are projections; residue encodes hidden state.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### UnitTestsAsProof — Biology
**What must be true.** In engineered domains, unit tests are the operational form of proof under specified assumptions.  
**Therefore false.** Testing is inferior to proof and cannot participate in rigor.  

**Domain lens.** Interfaces, inheritance, feedback loops, and embodied constraints. Membranes/boundaries and signaling/coupling stabilize forms.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### MeshTopologyHypothesis — Logic
**What must be true.** If message topology maps to mesh topology, the invariant must be stated (knot class, homology, etc.).  
**Therefore false.** Visual similarity is sufficient proof of topology equivalence.  

**Domain lens.** Predicates, constraints, and inference contracts. Model as types, relations, and proofs within a constraint system.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### MeshTopologyHypothesis — Computation
**What must be true.** If message topology maps to mesh topology, the invariant must be stated (knot class, homology, etc.).  
**Therefore false.** Visual similarity is sufficient proof of topology equivalence.  

**Domain lens.** Programs, state, traces, and projection of internal variables. Model as functions over state spaces; tests lock invariants.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### MeshTopologyHypothesis — Physics
**What must be true.** If message topology maps to mesh topology, the invariant must be stated (knot class, homology, etc.).  
**Therefore false.** Visual similarity is sufficient proof of topology equivalence.  

**Domain lens.** Symmetries, boundary conditions, carriers, and observable projections. Measurements are projections; residue encodes hidden state.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### MeshTopologyHypothesis — Biology
**What must be true.** If message topology maps to mesh topology, the invariant must be stated (knot class, homology, etc.).  
**Therefore false.** Visual similarity is sufficient proof of topology equivalence.  

**Domain lens.** Interfaces, inheritance, feedback loops, and embodied constraints. Membranes/boundaries and signaling/coupling stabilize forms.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### CoordinateNormalization — Logic
**What must be true.** Coordinate slicing requires normalization and bijective mapping choices; these are part of the claim.  
**Therefore false.** Any normalization yields the same geometry.  

**Domain lens.** Predicates, constraints, and inference contracts. Model as types, relations, and proofs within a constraint system.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### CoordinateNormalization — Computation
**What must be true.** Coordinate slicing requires normalization and bijective mapping choices; these are part of the claim.  
**Therefore false.** Any normalization yields the same geometry.  

**Domain lens.** Programs, state, traces, and projection of internal variables. Model as functions over state spaces; tests lock invariants.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### CoordinateNormalization — Physics
**What must be true.** Coordinate slicing requires normalization and bijective mapping choices; these are part of the claim.  
**Therefore false.** Any normalization yields the same geometry.  

**Domain lens.** Symmetries, boundary conditions, carriers, and observable projections. Measurements are projections; residue encodes hidden state.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### CoordinateNormalization — Biology
**What must be true.** Coordinate slicing requires normalization and bijective mapping choices; these are part of the claim.  
**Therefore false.** Any normalization yields the same geometry.  

**Domain lens.** Interfaces, inheritance, feedback loops, and embodied constraints. Membranes/boundaries and signaling/coupling stabilize forms.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### ParitySteersBranch — Logic
**What must be true.** Parity/spin can select between mirrored branches, resolving ambiguities introduced by projection.  
**Therefore false.** Branch selection is arbitrary and cannot be controlled.  

**Domain lens.** Predicates, constraints, and inference contracts. Model as types, relations, and proofs within a constraint system.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### ParitySteersBranch — Computation
**What must be true.** Parity/spin can select between mirrored branches, resolving ambiguities introduced by projection.  
**Therefore false.** Branch selection is arbitrary and cannot be controlled.  

**Domain lens.** Programs, state, traces, and projection of internal variables. Model as functions over state spaces; tests lock invariants.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### ParitySteersBranch — Physics
**What must be true.** Parity/spin can select between mirrored branches, resolving ambiguities introduced by projection.  
**Therefore false.** Branch selection is arbitrary and cannot be controlled.  

**Domain lens.** Symmetries, boundary conditions, carriers, and observable projections. Measurements are projections; residue encodes hidden state.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### ParitySteersBranch — Biology
**What must be true.** Parity/spin can select between mirrored branches, resolving ambiguities introduced by projection.  
**Therefore false.** Branch selection is arbitrary and cannot be controlled.  

**Domain lens.** Interfaces, inheritance, feedback loops, and embodied constraints. Membranes/boundaries and signaling/coupling stabilize forms.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### DetuneProtocol — Logic
**What must be true.** A detune protocol is a controlled perturbation; results must be compared against null baselines.  
**Therefore false.** Any perturbation proves something if it produces a pattern.  

**Domain lens.** Predicates, constraints, and inference contracts. Model as types, relations, and proofs within a constraint system.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### DetuneProtocol — Computation
**What must be true.** A detune protocol is a controlled perturbation; results must be compared against null baselines.  
**Therefore false.** Any perturbation proves something if it produces a pattern.  

**Domain lens.** Programs, state, traces, and projection of internal variables. Model as functions over state spaces; tests lock invariants.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### DetuneProtocol — Physics
**What must be true.** A detune protocol is a controlled perturbation; results must be compared against null baselines.  
**Therefore false.** Any perturbation proves something if it produces a pattern.  

**Domain lens.** Symmetries, boundary conditions, carriers, and observable projections. Measurements are projections; residue encodes hidden state.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### DetuneProtocol — Biology
**What must be true.** A detune protocol is a controlled perturbation; results must be compared against null baselines.  
**Therefore false.** Any perturbation proves something if it produces a pattern.  

**Domain lens.** Interfaces, inheritance, feedback loops, and embodied constraints. Membranes/boundaries and signaling/coupling stabilize forms.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### StoppedWorld — Logic
**What must be true.** Paused execution is a technique: freeze the system, expose hidden state, then resume.  
**Therefore false.** Systems cannot be meaningfully paused without changing them.  

**Domain lens.** Predicates, constraints, and inference contracts. Model as types, relations, and proofs within a constraint system.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### StoppedWorld — Computation
**What must be true.** Paused execution is a technique: freeze the system, expose hidden state, then resume.  
**Therefore false.** Systems cannot be meaningfully paused without changing them.  

**Domain lens.** Programs, state, traces, and projection of internal variables. Model as functions over state spaces; tests lock invariants.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### StoppedWorld — Physics
**What must be true.** Paused execution is a technique: freeze the system, expose hidden state, then resume.  
**Therefore false.** Systems cannot be meaningfully paused without changing them.  

**Domain lens.** Symmetries, boundary conditions, carriers, and observable projections. Measurements are projections; residue encodes hidden state.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### StoppedWorld — Biology
**What must be true.** Paused execution is a technique: freeze the system, expose hidden state, then resume.  
**Therefore false.** Systems cannot be meaningfully paused without changing them.  

**Domain lens.** Interfaces, inheritance, feedback loops, and embodied constraints. Membranes/boundaries and signaling/coupling stabilize forms.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### ObserverResolution — Logic
**What must be true.** Observer resolution limits what can be seen; increasing resolution reveals pre-existing structure rather than creating it.  
**Therefore false.** Structure is created by observation.  

**Domain lens.** Predicates, constraints, and inference contracts. Model as types, relations, and proofs within a constraint system.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### ObserverResolution — Computation
**What must be true.** Observer resolution limits what can be seen; increasing resolution reveals pre-existing structure rather than creating it.  
**Therefore false.** Structure is created by observation.  

**Domain lens.** Programs, state, traces, and projection of internal variables. Model as functions over state spaces; tests lock invariants.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### ObserverResolution — Physics
**What must be true.** Observer resolution limits what can be seen; increasing resolution reveals pre-existing structure rather than creating it.  
**Therefore false.** Structure is created by observation.  

**Domain lens.** Symmetries, boundary conditions, carriers, and observable projections. Measurements are projections; residue encodes hidden state.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### ObserverResolution — Biology
**What must be true.** Observer resolution limits what can be seen; increasing resolution reveals pre-existing structure rather than creating it.  
**Therefore false.** Structure is created by observation.  

**Domain lens.** Interfaces, inheritance, feedback loops, and embodied constraints. Membranes/boundaries and signaling/coupling stabilize forms.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### ReversePath — Logic
**What must be true.** If a path exists forward, the reverse path exists in principle given missing channels; irreversibility is missing state.  
**Therefore false.** Forward paths do not imply any reverse capability.  

**Domain lens.** Predicates, constraints, and inference contracts. Model as types, relations, and proofs within a constraint system.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### ReversePath — Computation
**What must be true.** If a path exists forward, the reverse path exists in principle given missing channels; irreversibility is missing state.  
**Therefore false.** Forward paths do not imply any reverse capability.  

**Domain lens.** Programs, state, traces, and projection of internal variables. Model as functions over state spaces; tests lock invariants.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### ReversePath — Physics
**What must be true.** If a path exists forward, the reverse path exists in principle given missing channels; irreversibility is missing state.  
**Therefore false.** Forward paths do not imply any reverse capability.  

**Domain lens.** Symmetries, boundary conditions, carriers, and observable projections. Measurements are projections; residue encodes hidden state.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### ReversePath — Biology
**What must be true.** If a path exists forward, the reverse path exists in principle given missing channels; irreversibility is missing state.  
**Therefore false.** Forward paths do not imply any reverse capability.  

**Domain lens.** Interfaces, inheritance, feedback loops, and embodied constraints. Membranes/boundaries and signaling/coupling stabilize forms.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### NeedAsSource — Logic
**What must be true.** A ‘why’ chain ends at a need: the constraint that makes a behavior inevitable.  
**Therefore false.** All behaviors are arbitrary and need no necessity source.  

**Domain lens.** Predicates, constraints, and inference contracts. Model as types, relations, and proofs within a constraint system.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### NeedAsSource — Computation
**What must be true.** A ‘why’ chain ends at a need: the constraint that makes a behavior inevitable.  
**Therefore false.** All behaviors are arbitrary and need no necessity source.  

**Domain lens.** Programs, state, traces, and projection of internal variables. Model as functions over state spaces; tests lock invariants.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### NeedAsSource — Physics
**What must be true.** A ‘why’ chain ends at a need: the constraint that makes a behavior inevitable.  
**Therefore false.** All behaviors are arbitrary and need no necessity source.  

**Domain lens.** Symmetries, boundary conditions, carriers, and observable projections. Measurements are projections; residue encodes hidden state.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### NeedAsSource — Biology
**What must be true.** A ‘why’ chain ends at a need: the constraint that makes a behavior inevitable.  
**Therefore false.** All behaviors are arbitrary and need no necessity source.  

**Domain lens.** Interfaces, inheritance, feedback loops, and embodied constraints. Membranes/boundaries and signaling/coupling stabilize forms.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### LibraryOfShapes — Logic
**What must be true.** Index spaces can be reinterpreted as libraries of shapes: addresses select renderings under a consistent rule.  
**Therefore false.** Addresses have no geometric meaning; shape is imposed by the renderer.  

**Domain lens.** Predicates, constraints, and inference contracts. Model as types, relations, and proofs within a constraint system.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### LibraryOfShapes — Computation
**What must be true.** Index spaces can be reinterpreted as libraries of shapes: addresses select renderings under a consistent rule.  
**Therefore false.** Addresses have no geometric meaning; shape is imposed by the renderer.  

**Domain lens.** Programs, state, traces, and projection of internal variables. Model as functions over state spaces; tests lock invariants.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### LibraryOfShapes — Physics
**What must be true.** Index spaces can be reinterpreted as libraries of shapes: addresses select renderings under a consistent rule.  
**Therefore false.** Addresses have no geometric meaning; shape is imposed by the renderer.  

**Domain lens.** Symmetries, boundary conditions, carriers, and observable projections. Measurements are projections; residue encodes hidden state.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### LibraryOfShapes — Biology
**What must be true.** Index spaces can be reinterpreted as libraries of shapes: addresses select renderings under a consistent rule.  
**Therefore false.** Addresses have no geometric meaning; shape is imposed by the renderer.  

**Domain lens.** Interfaces, inheritance, feedback loops, and embodied constraints. Membranes/boundaries and signaling/coupling stabilize forms.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### OperatorPrimacy_v1 — Logic
**What must be true.** Verbs precede nouns: systems are defined by transforms; entities are frozen orbits.  
**Therefore false.** A ‘thing’ can be specified without specifying its transformation rules.  

**Domain lens.** Predicates, constraints, and inference contracts. Model as types, relations, and proofs within a constraint system.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### OperatorPrimacy_v1 — Computation
**What must be true.** Verbs precede nouns: systems are defined by transforms; entities are frozen orbits.  
**Therefore false.** A ‘thing’ can be specified without specifying its transformation rules.  

**Domain lens.** Programs, state, traces, and projection of internal variables. Model as functions over state spaces; tests lock invariants.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### OperatorPrimacy_v1 — Physics
**What must be true.** Verbs precede nouns: systems are defined by transforms; entities are frozen orbits.  
**Therefore false.** A ‘thing’ can be specified without specifying its transformation rules.  

**Domain lens.** Symmetries, boundary conditions, carriers, and observable projections. Measurements are projections; residue encodes hidden state.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### OperatorPrimacy_v1 — Biology
**What must be true.** Verbs precede nouns: systems are defined by transforms; entities are frozen orbits.  
**Therefore false.** A ‘thing’ can be specified without specifying its transformation rules.  

**Domain lens.** Interfaces, inheritance, feedback loops, and embodied constraints. Membranes/boundaries and signaling/coupling stabilize forms.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### ConstraintMirror_v1 — Logic
**What must be true.** Equality is a constraint manifold (dark mirror): D(x,y)=0 defines admissible states.  
**Therefore false.** Equality is merely a human assertion.  

**Domain lens.** Predicates, constraints, and inference contracts. Model as types, relations, and proofs within a constraint system.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### ConstraintMirror_v1 — Computation
**What must be true.** Equality is a constraint manifold (dark mirror): D(x,y)=0 defines admissible states.  
**Therefore false.** Equality is merely a human assertion.  

**Domain lens.** Programs, state, traces, and projection of internal variables. Model as functions over state spaces; tests lock invariants.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### ConstraintMirror_v1 — Physics
**What must be true.** Equality is a constraint manifold (dark mirror): D(x,y)=0 defines admissible states.  
**Therefore false.** Equality is merely a human assertion.  

**Domain lens.** Symmetries, boundary conditions, carriers, and observable projections. Measurements are projections; residue encodes hidden state.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### ConstraintMirror_v1 — Biology
**What must be true.** Equality is a constraint manifold (dark mirror): D(x,y)=0 defines admissible states.  
**Therefore false.** Equality is merely a human assertion.  

**Domain lens.** Interfaces, inheritance, feedback loops, and embodied constraints. Membranes/boundaries and signaling/coupling stabilize forms.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### TwoChannelInvertibility_v1 — Logic
**What must be true.** A coupling becomes bijective when both channels are retained: (S,D)↔(a,b).  
**Therefore false.** Publishing only S can be inverted without extra constraints.  

**Domain lens.** Predicates, constraints, and inference contracts. Model as types, relations, and proofs within a constraint system.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### TwoChannelInvertibility_v1 — Computation
**What must be true.** A coupling becomes bijective when both channels are retained: (S,D)↔(a,b).  
**Therefore false.** Publishing only S can be inverted without extra constraints.  

**Domain lens.** Programs, state, traces, and projection of internal variables. Model as functions over state spaces; tests lock invariants.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### TwoChannelInvertibility_v1 — Physics
**What must be true.** A coupling becomes bijective when both channels are retained: (S,D)↔(a,b).  
**Therefore false.** Publishing only S can be inverted without extra constraints.  

**Domain lens.** Symmetries, boundary conditions, carriers, and observable projections. Measurements are projections; residue encodes hidden state.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### TwoChannelInvertibility_v1 — Biology
**What must be true.** A coupling becomes bijective when both channels are retained: (S,D)↔(a,b).  
**Therefore false.** Publishing only S can be inverted without extra constraints.  

**Domain lens.** Interfaces, inheritance, feedback loops, and embodied constraints. Membranes/boundaries and signaling/coupling stabilize forms.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### ProjectionCreatesScar_v1 — Logic
**What must be true.** Any projection ⊥ produces a residue (scar/ghost) relative to a chosen decomposition.  
**Therefore false.** Information ‘vanishes’ without leaving a complementary degree of freedom.  

**Domain lens.** Predicates, constraints, and inference contracts. Model as types, relations, and proofs within a constraint system.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### ProjectionCreatesScar_v1 — Computation
**What must be true.** Any projection ⊥ produces a residue (scar/ghost) relative to a chosen decomposition.  
**Therefore false.** Information ‘vanishes’ without leaving a complementary degree of freedom.  

**Domain lens.** Programs, state, traces, and projection of internal variables. Model as functions over state spaces; tests lock invariants.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### ProjectionCreatesScar_v1 — Physics
**What must be true.** Any projection ⊥ produces a residue (scar/ghost) relative to a chosen decomposition.  
**Therefore false.** Information ‘vanishes’ without leaving a complementary degree of freedom.  

**Domain lens.** Symmetries, boundary conditions, carriers, and observable projections. Measurements are projections; residue encodes hidden state.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage


### ProjectionCreatesScar_v1 — Biology
**What must be true.** Any projection ⊥ produces a residue (scar/ghost) relative to a chosen decomposition.  
**Therefore false.** Information ‘vanishes’ without leaving a complementary degree of freedom.  

**Domain lens.** Interfaces, inheritance, feedback loops, and embodied constraints. Membranes/boundaries and signaling/coupling stabilize forms.

**Formalization (minimal).**
- Operators: Δ, ⊕, ↻, ⊥, Ψ, Ω
- Constraint: $D(x,y)=0$ (when applicable)
- Projection: $\perp: \mathcal{S}\to\mathcal{O}$; residue $\rho := \mathcal{S}\ominus \mathcal{O}$

**Test hook (falsifiable).**
- Define a port $P$ returning observable $o$ under perturbation $\Delta$.
- Prediction: $o$ changes coherently for structured inputs; null baselines follow the null model.

**Failure mode.** If the effect vanishes under baseline changes, precision increases, or adapter swaps, reclassify as $\Omega$ and isolate the coupling that created it.


\newpage

## Part VII — Novel Code Modules (Isolated)

**Note:** modules below are toy-safe scaffolding (no operational cryptographic inversion).

### Module A — Dual-Channel Coupling (Toy)
```python
MASK = 0xffffffff
def mix(a,b):
    return (a+b)&MASK, (a-b)&MASK
```

### Module B — Detune Scan Harness (Histogram scaffolding)
```python
def detune_scan(corpus, score_fn, detunes):
    return {d:[score_fn(x, *d) for x in corpus] for d in detunes}
```

### Module C — Hash Slice → (x,y,z)+parity (Rendering adapter)
```python
def slice256_to_xyz_parity(digest_bytes):
    h=int.from_bytes(digest_bytes,'big'); parity=h&1; h>>=1
    m=(1<<85)-1
    z=h&m; h>>=85; y=h&m; h>>=85; x=h&m
    denom=float(1<<85)
    return (x/denom,y/denom,z/denom,parity)
```


\newpage

## Appendix — Reproducibility Checklist

1) Record versions and seeds. 2) Keep Domain pure. 3) Always run null baselines. 4) Prefer spectral evidence. 5) Promote Ω→Ψ only after adapter swaps and baseline changes.
