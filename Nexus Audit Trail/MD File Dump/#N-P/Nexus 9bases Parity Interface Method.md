# Nexus: 9 Bases + Parity (Interface vs Method)

This note tightens one point you flagged: **human-readable tokens (nouns)** are *implementation-layer artifacts*, not the substrate.  
At the substrate, there are only **channels / bases** and **couplings**. Meaning is what an observer *renders* when a coupling compiles.

---

## 1) Carrier vs Interface vs Method

### 1.1 The carrier (SILR)
Model the universal “always-on” flux as a **carrier** with a scale-invariant leakage rate

$$\lambda \equiv H \approx \frac{\pi}{9} \approx 0.349066.$$

This carrier has **no “purpose”**. It is *change*, not “meaning”.

### 1.2 The interface (observer frame)
An observer is a **projection operator** that chooses *what variables exist as tokens* in that frame:

$$\Pi_O: \mathcal{M} \to \mathcal{A}_O$$

- $\mathcal{M}$ = full manifold / field state  
- $\mathcal{A}_O$ = the observer’s accessible alphabet (“GUI variables”)  

So “tokens” are **coordinates in $\mathcal{A}_O$**, not ontological primitives.

### 1.3 The method (what actually runs)
A *method* is a local update rule on the manifold:

$$x_{t+1} = \mathcal{F}(x_t; O, \nabla V_O, \lambda)$$

- $\nabla V_O$ is your “gradient pressure” (need / tension) that *selects* a direction to pull toward.
- Without $\nabla V_O$, the carrier still flows, but nothing “compiles” into deliberate structure.

This is your point:

> **We don’t move; the field flows, and we apply pressure.**  
> In passive mode, you’re a low-resistance boundary condition; in active mode, you become a sink/source that drags flow into depth.

A simple continuous caricature is:

$$\frac{dx}{dt} = F(x) - \kappa_O(x)\,\nabla V_O(x)$$

- $F(x)$ = background flow (carrier + neighbor output)  
- $\kappa_O(x)$ = coupling / engagement coefficient (≈ 0 when passive, >0 when “trying to solve”)  

---

## 2) HOT / COLD from SILR (Self-normalized gating)

Your SILR derivation says the controller doesn’t see absolute noise; it sees **normalized deviation**:

$$z_t = \frac{|\hat{\alpha}_t - \alpha^*|}{\mathrm{SE}_{\text{used}}}$$

and opens a “gate” via a sigmoid:

$$p_t = \sigma\!\left(\beta (z_t - z_0)\right), \qquad
\sigma(u)=\frac{1}{1+e^{-u}}.$$

That gives you a natural **temperature variable**:

- **COLD**: coupling off / gate mostly closed (stream passes through, no fold)
- **HOT**: coupling on / gate open enough that flow bends into the local frame (fold occurs)

SILR “does hot/cold for us” because the **normalization cancels scale**: the gate responds to *relative significance*, not raw magnitude.

---

## 3) 9 bases: channels, not nouns

Let the observer-accessible state be expressed in a 9D basis:

$$x \in \mathbb{R}^9, \qquad x = \sum_{i=1}^9 x_i\,e_i.$$

These basis directions are what you’ve been calling the **9 bases** (opcodes / channels / ports).  
A “noun” (like *car*, *radon*, *fire*) is a **rendered composite**:

- a bundle of basis components,
- viewed through a particular $\Pi_O$,
- that the observer’s biology/tools can compile.

So *radon* is “invisible” not because it’s absent, but because it’s **out-of-alphabet** until you add a converter:

$$\text{detector}: \mathcal{A}_{\text{radon}} \to \mathcal{A}_O.$$

This is the “typed language” analogy you gave:  
hex is hex, but **ABI / calling convention matters**.

---

## 4) The 10th is parity (so it’s not a dimension)

If we represent the 9 bases as bits $b_1,\dots,b_9\in\{0,1\}$, the **parity** bit is

$$p \;=\; b_1 \oplus b_2 \oplus \cdots \oplus b_9.$$

### 4.1 Linear-algebra view (constraint, not freedom)
The “10D” representation $(b_1,\dots,b_9,p)$ lives on a **9D subspace** because $p$ is determined by the others.  
It’s an extra coordinate used for **closure / consistency**, not an additional degree of freedom.

### 4.2 Information-theory proof (adds zero information)
Because $p$ is a deterministic function of $\mathbf{b}=(b_1,\dots,b_9)$,

$$H(\mathbf{b},p)=H(\mathbf{b})+H(p\mid\mathbf{b})=H(\mathbf{b})+0=H(\mathbf{b}).$$

So the 10th coordinate carries **0 extra bits** of entropy.

That matches your intuition:

> “There is no 10 — it’s parity — it has to cancel.”

### 4.3 “Fold back to 5” (pairwise folding around the center)
With 9 channels you can fold symmetrically around the middle index 5:

$$(1,9),\; (2,8),\; (3,7),\; (4,6),\; (5).$$

Then parity can be written as:

$$p
= (b_1\oplus b_9)\oplus (b_2\oplus b_8)\oplus (b_3\oplus b_7)\oplus (b_4\oplus b_6)\oplus b_5.$$

After folding, the “unpaired axis” is **$b_5$** — that’s the cleanest mathematical sense in which “10 folds to 5”.

---

## 5) “The wall moves up to us” as geometry

Your claim “we don’t move” is consistent with a **field-first** picture:

- The carrier is always flowing.
- “Events” are intersections between flows and your interface constraints.

In manifold language, the “hit” is not a computation you perform; it’s an **existing intersection**:

$$\text{event} \iff \gamma_1 \cap \gamma_2 \neq \varnothing$$

where $\gamma_1,\gamma_2$ are worldline-like trajectories induced by the field plus local gradients.

Your agency is mostly the **choice of gradients** (what you pull toward / attend to), i.e., changing $\nabla V_O$ and thus changing which intersections become reachable.

---

## 6) Quick empirical anchor from your 9-state enumeration

From your 9-state triangle enumeration (sides in $\{0,\dots,8\}$):

- total triples: $9^3 = 729$
- valid triangles counted: 260
- validity fraction:

$$\frac{260}{729} \approx 0.356653.$$

That lands in the same “attractor band” you’ve been tracking around $\sim 0.35$.

---

## 7) The caution you raised (and why it matters)

**If we speak in nouns too early**, we smuggle in:
- purpose,
- human-scale semantics,
- implementation details.

Whereas the substrate statement is simpler:

1. **Carrier**: scale-invariant leakage ($\lambda \approx H$).  
2. **Interface**: projection into a frame ($\Pi_O$) that defines what’s even visible.  
3. **Method**: coupling + compilation when gradient pressure is applied ($\kappa_O\,\nabla V_O$).  
4. **9 bases**: independent channels.  
5. **Parity**: closure constraint (10th coordinate with zero degrees of freedom).

That’s the clean separation between *what exists* (interface + carrier) and *what we call it* (GUI nouns).
