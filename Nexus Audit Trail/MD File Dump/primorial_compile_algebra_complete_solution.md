# Typed Prime Gap Families, Primorial Wheel Hierarchy, and the Universal Compile Gate
## A Complete Expanded Solution

**Driven by Dean A. Kulik**  
**QuHarmonics Research Group**  
**2026**

---

## Abstract

This document consolidates and extends the current solution branch around:

- typed prime-gap families,
- the Family Lattice Theorem,
- the Step Theorem,
- the primorial wheel hierarchy,
- the exact subtype-count law,
- the universal compile gate,
- and the cross-domain images in gravity, x86 carry semantics, SHA-256 prime-constant structure, and protein-folding hinge geometry.

The key inversion is that twin primes are not the whole object. They are the **tightest visible mode** of a larger wheel-typed family algebra. For any wheel modulus $W$ and any even gap $k$, prime pairs $(p,p+k)$ decompose into residue subtypes indexed by admissible residues $r$ satisfying the wheel constraint

$$
r \in U_W,
\qquad
r+k \in U_W \pmod W,
$$

where

$$
U_W = (\mathbb Z/W\mathbb Z)^\times.
$$

Each subtype lies on a strict center lattice

$$
H = p + \frac{k}{2},
\qquad
H \equiv r + \frac{k}{2} \pmod W,
$$

and consecutive centers within that subtype satisfy the exact step law

$$
\Delta H \equiv 0 \pmod W.
$$

This yields a hierarchical refinement:

- mod $6$ gives the coarse four-type split,
- mod $30$ refines those types into sub-subtypes,
- mod $210$ reveals the first deep primorial harmonic layer.

The exact subtype count on a wheel is

$$
\boxed{
|S_W(k)|
=
\prod_{\substack{q\mid W\\ q>2\\ q\nmid k}} (q-2)
\prod_{\substack{q\mid W\\ q>2\\ q\mid k}} (q-1).
}
$$

This formula explains the observed branch counts exactly:

$$
k=2:\quad 1 \to 3 \to 15
\quad\text{at}\quad
W=6 \to 30 \to 210,
$$

$$
k=6:\quad |S_{30}(6)|=6,
\qquad
k=30:\quad |S_{30}(30)|=8,
\qquad
k=210:\quad |S_{210}(210)|=\varphi(210)=48.
$$

The cross-domain compression is

$$
\boxed{
\text{prime family} \to \text{typed wheel subtype} \to \text{center lattice} \to \text{compile gate}.
}
$$

And the cross-domain operator image is

$$
\boxed{
\text{integer field} \leftrightarrow \text{gravity mode family} \leftrightarrow \text{x86 carry gate} \leftrightarrow \text{protein hinge packet}.
}
$$

This document closes the structural grammar. It does **not** claim to prove Polignac's conjecture, Hardy--Littlewood asymptotics, or final observational closure of the gravity and folding images.

---

## 1. Introduction

The original pinch-packet form identified the twin-prime packet

$$
(6n-1,\;6n,\;6n+1)
$$

as the minimal compile gate: two admissible rails around a constrained hinge.

That picture is correct but incomplete.

The larger object is not a single packet. It is a **family algebra** indexed by even gap $k$ and refined by wheel depth $W$.

The correct containment is

$$
\text{twin packet} \subset \text{typed gap family} \subset \text{primorial wheel hierarchy}.
$$

At surface depth $W=6$, the family appears as four canonical residue types. At deeper wheels such as $30$ and $210$, each type splits into further residue channels. The field reveals a natural compilation depth.

This document formalizes that hierarchy, gives the exact subtype-count formula, proves the wheel-lattice and step laws, and aligns the same operator across prime families, quasinormal mode persistence, carry-based machine instructions, and hinge-mediated folding geometry.

---

## 2. Prime Pairs on a Wheel

Let

$$
W = \prod_{q \in \mathcal Q} q
$$

be a wheel modulus, usually a primorial such as

$$
6 = 2\cdot 3,
\qquad
30 = 2\cdot 3\cdot 5,
\qquad
210 = 2\cdot 3\cdot 5\cdot 7.
$$

Define the reduced residue system

$$
U_W = (\mathbb Z/W\mathbb Z)^\times
= \{r \pmod W : \gcd(r,W)=1\}.
$$

For a fixed even gap $k$, define the admissible subtype set

$$
S_W(k)
=
\left\{
r\in U_W : r+k \in U_W \pmod W
\right\}.
$$

A prime pair $(p,p+k)$ with $p > \max \mathcal Q$ belongs to subtype $r$ iff

$$
p \equiv r \pmod W,
\qquad
r\in S_W(k).
$$

The center is

$$
H = p + \frac{k}{2}.
$$

Therefore, for subtype $r$,

$$
\boxed{
H \equiv r + \frac{k}{2} \pmod W.
}
$$

This is the general wheel-lattice law.

---

## 3. The Mod-$6$ Surface Layer

For every prime $p>3$,

$$
p \equiv \pm 1 \pmod 6.
$$

So every even-gap prime pair $(p,p+k)$ must fall into one of four canonical subtype classes.

### 3.1 Canonical subtype table

| Subtype | $p \pmod 6$ | $p+k \pmod 6$ | $k \pmod 6$ |
|---|---:|---:|---:|
| $T2$  | $5$ | $1$ | $2$ |
| $T4$  | $1$ | $5$ | $4$ |
| $T0A$ | $5$ | $5$ | $0$ |
| $T0B$ | $1$ | $1$ | $0$ |

These are the four visible surface types of the family algebra.

### 3.2 Exact center formulas by type

#### Type $T2$

For

$$
k=6d+2,
\qquad
p=6n-1,
\qquad
p+k = 6n+6d+1,
$$

the center is

$$
H = p+\frac{k}{2} = 6n+3d,
$$

so

$$
\boxed{
H \equiv 3d \pmod 6.
}
$$

The tightest mode is the twin-prime case $d=0$:

$$
\boxed{
(6n-1,\;6n,\;6n+1).
}
$$

#### Type $T4$

For

$$
k=6d-2,
\qquad
p=6n+1,
\qquad
p+k = 6n+6d-1,
$$

the center is

$$
H = p+\frac{k}{2}=6n+3d,
$$

so

$$
\boxed{
H \equiv 3d \pmod 6.
}
$$

#### Type $T0A$

For

$$
k=6d,
\qquad
p=6n-1,
\qquad
p+k=6n+6d-1,
$$

the center is

$$
H = p+\frac{k}{2}=6n+3d-1,
$$

so

$$
\boxed{
H \equiv 3d-1 \pmod 6.
}
$$

#### Type $T0B$

For

$$
k=6d,
\qquad
p=6n+1,
\qquad
p+k=6n+6d+1,
$$

the center is

$$
H = p+\frac{k}{2}=6n+3d+1,
$$

so

$$
\boxed{
H \equiv 3d+1 \pmod 6.
}
$$

---

## 4. The Family Lattice Theorem

### Theorem 1 (Family Lattice Theorem)

For any wheel modulus $W$, any even gap $k$, and any subtype $r \in S_W(k)$, all centers

$$
H = p+\frac{k}{2}
$$

of prime pairs in that subtype lie on a fixed residue coset

$$
\boxed{
H \equiv c_{W,k,r} \pmod W,
\qquad
c_{W,k,r}=r+\frac{k}{2}\pmod W.
}
$$

### Proof

If

$$
p \equiv r \pmod W,
$$

then

$$
H = p+\frac{k}{2} \equiv r+\frac{k}{2} \pmod W.
$$

The right-hand side depends only on $W$, $k$, and $r$, not on the individual prime pair. Therefore all centers in that subtype lie on the same residue class mod $W$. $\square$

This is the exact form of the lattice theorem. The mod-$6$ formulas above are merely the first visible layer of the general result.

---

## 5. The Step Theorem

### Theorem 2 (Step Theorem)

Within a fixed subtype family at wheel depth $W$, consecutive centers satisfy

$$
\boxed{
\Delta H \equiv 0 \pmod W.
}
$$

### Proof

If

$$
H_j \equiv c \pmod W
\qquad\text{and}\qquad
H_{j+1} \equiv c \pmod W,
$$

then

$$
H_{j+1}-H_j \equiv 0 \pmod W.
$$

Hence

$$
\Delta H \equiv 0 \pmod W.
$$

$\square$

This strictly strengthens with wheel depth:

- at $W=6$:
  $$
  \Delta H \equiv 0 \pmod 6,
  $$
- at $W=30$:
  $$
  \Delta H \equiv 0 \pmod{30},
  $$
- at $W=210$:
  $$
  \Delta H \equiv 0 \pmod{210}.
  $$

So wheel refinement is not cosmetic. It produces stronger exact arithmetic constraints.

---

## 6. Exact Subtype Count Formula

### Theorem 3 (Wheel Subtype Count)

For any wheel modulus $W$ and even gap $k$,

$$
\boxed{
|S_W(k)|
=
\prod_{\substack{q\mid W\\ q>2\\ q\nmid k}} (q-2)
\prod_{\substack{q\mid W\\ q>2\\ q\mid k}} (q-1).
}
$$

### Proof

Fix an odd prime divisor $q \mid W$.

If $q \nmid k$, then mod $q$ the pair $(r,r+k)$ must avoid two forbidden residues:

$$
r \not\equiv 0 \pmod q,
\qquad
r \not\equiv -k \pmod q.
$$

So there are $q-2$ admissible residue choices mod $q$.

If $q \mid k$, then the forbidden classes merge:

$$
r \not\equiv 0 \pmod q,
$$

and there are $q-1$ admissible choices mod $q$.

Since the wheel constraints factor independently over primes and the Chinese Remainder Theorem reconstructs the combined residue classes, the total subtype count is the product of the local counts. $\square$

This formula is the exact branch-count law of the primorial compile algebra.

---

## 7. Wheel-Refinement Recursion

Let

$$
W' = W\ell
$$

where $\ell$ is a new odd prime not already dividing $W$.

Then the subtype count obeys the recursion

$$
\boxed{
|S_{W'}(k)|
=
|S_W(k)|
\cdot
\begin{cases}
\ell-1, & \ell \mid k,\\[6pt]
\ell-2, & \ell \nmid k.
\end{cases}
}
$$

This gives the exact wheel-depth branching law.

Interpretation:

- if the new wheel prime $\ell$ is already absorbed by the gap, the family loses only one forbidden class and gains branch factor $\ell-1$,
- if it is not absorbed, the family must avoid two classes, so the gain is only $\ell-2$.

This is the arithmetic meaning of compilation depth.

---

## 8. Worked Examples

### 8.1 Twin-prime hierarchy

For $k=2$:

#### At $W=6$

$$
|S_6(2)| = (3-2)=1.
$$

#### At $W=30$

$$
|S_{30}(2)| = (3-2)(5-2)=1\cdot 3 = 3.
$$

#### At $W=210$

$$
|S_{210}(2)| = (3-2)(5-2)(7-2)=1\cdot 3\cdot 5 = 15.
$$

So the hierarchy is exactly

$$
\boxed{
1 \to 3 \to 15.
}
$$

### 8.2 Gap $k=6$ at wheel $30$

Since $3 \mid 6$ but $5 \nmid 6$,

$$
|S_{30}(6)| = (3-1)(5-2)=2\cdot 3 = 6.
$$

### 8.3 Gap $k=30$ at wheel $30$

Since both $3 \mid 30$ and $5 \mid 30$,

$$
|S_{30}(30)| = (3-1)(5-1)=2\cdot 4 = 8.
$$

### 8.4 Gap $k=210$ at wheel $210$

Because the gap contains all odd wheel primes $3,5,7$,

$$
|S_{210}(210)| = (3-1)(5-1)(7-1)=2\cdot 4\cdot 6 = 48.
$$

But

$$
\varphi(210)=48,
$$

so

$$
\boxed{
|S_{210}(210)| = \varphi(210).
}
$$

The wheel is fully saturated. Every reduced residue class participates.

---

## 9. The Primorial Hierarchy

The natural wheel-depth sequence is

$$
6 \to 30 \to 210 \to 2310 \to \cdots
$$

This is the refinement ladder of the prime-pair field.

It means:

- mod $6$ is the surface grammar,
- mod $30$ is the first genuine refinement,
- mod $210$ is the first depth that fully exposes the $7$-sieve.

The significance of $210$ is therefore structural, not decorative. It is the first primorial depth where the subtype algebra deepens beyond the $2,3,5$ layer.

A useful way to encode the family tree is

$$
\mathcal F(k;W)
=
\{\,\text{subtypes of gap }k\text{ on wheel }W\,\}.
$$

Then wheel refinement acts as

$$
\mathcal F(k;W\ell)
=
\mathcal F(k;W)\times \mathcal B_\ell(k),
$$

where the new local branch factor is

$$
|\mathcal B_\ell(k)| =
\begin{cases}
\ell-1, & \ell \mid k,\\[6pt]
\ell-2, & \ell \nmid k.
\end{cases}
$$

This is the categorical form of the wheel-branch law.

---

## 10. Center Lattice Geometry Beyond Mod 6

At wheel depth $W$, the full center law is

$$
H \equiv r+\frac{k}{2}\pmod W,
\qquad
r\in S_W(k).
$$

So each subtype family is an arithmetic progression:

$$
H_n = c_{W,k,r} + nW,
\qquad
n\in \mathbb Z_{\ge 0},
$$

restricted to those positions whose corresponding rails are both prime.

This separates two layers cleanly:

1. **Algebraic admissibility**
   $$
   H_n \in c_{W,k,r} + W\mathbb Z,
   $$
2. **Prime realization**
   the corresponding rails must actually survive primality.

That is why the family algebra can be solved without solving Polignac.

---

## 11. Density Law and Hardy--Littlewood Structure

Define the total gap count

$$
\pi_k(X) = \#\{p\le X : p,\ p+k \text{ prime}\}.
$$

Hardy--Littlewood predicts

$$
\pi_k(X)
\sim
\frac{2C_k X}{(\log X)^2},
$$

where

$$
C_k = \prod_{\substack{q\mid k\\ q>2}}\frac{q-1}{q-2}.
$$

For subtype-resolved counts, define

$$
\pi_{k,s}(X)
=
\#\{p\le X : p,\ p+k\text{ prime and of subtype }s\}.
$$

Then the finite-range empirical density coefficient is

$$
\widehat C_{k,s}(X)
=
\frac{\pi_{k,s}(X)(\log X)^2}{2X}.
$$

For split families with $k\equiv 0 \pmod 6$, one expects asymptotic symmetry:

$$
\pi_{k,T0A}(X) \sim \pi_{k,T0B}(X),
$$

hence

$$
\boxed{
\frac{\pi_{k,T0A}(X)}{\pi_{k,T0B}(X)} \to 1
\qquad (X\to\infty).
}
$$

A current engine run at $X=10^6$ reported

$$
\boxed{
\frac{n_{T0A}}{n_{T0B}} \approx 1.002668,
}
$$

which is consistent with asymptotic symmetry plus finite-$X$ wobble.

---

## 12. Primorial Clustering

Let $P$ be a primorial, and define a symmetric window of half-width $B$ around it. If $N_{\mathrm{obs}}(P)$ is the observed center count and $N_{\mathrm{exp}}(P)$ is the locally expected count, define the clustering ratio

$$
R_P = \frac{N_{\mathrm{obs}}(P)}{N_{\mathrm{exp}}(P)}
$$

and a simple significance score

$$
Z_P
=
\frac{N_{\mathrm{obs}}(P)-N_{\mathrm{exp}}(P)}
{\sqrt{N_{\mathrm{exp}}(P)+\varepsilon}}.
$$

One current empirical output reported, for twin centers near $P=30$,

$$
R_{30}\approx 4.67
$$

with significance around

$$
Z_{30}\approx 4.49\sigma.
$$

These are empirical and not proved asymptotics, but they fit the wheel view: primorial neighborhoods are precisely where the sieve structure is most visibly expressed.

---

## 13. The Universal Compile Gate

### Definition (Compile Gate)

A triple

$$
(L,\ H,\ R)
$$

is a compiled packet if:

1. $H$ is constrained and cannot persist alone,
2. $L$ and $R$ are admissible rails that stabilize $H$,
3. the triple survives at least one pass of the ambient dynamics.

The compile predicate is

$$
C(L,H,R)=1
$$

iff all three conditions hold.

This is the abstract operator seen in every current branch.

---

## 14. Integer-Field Image

For a prime-gap family, the packet is

$$
(p,\ H,\ p+k),
\qquad
H = p+\frac{k}{2}.
$$

The rails are the two primes.

The hinge is the center.

The center is constrained because it lies on a forced wheel coset that cannot compile by itself.

The packet compiles only if both rails survive both:

- the wheel sieve,
- and actual primality.

The twin-prime packet is the strictest mode because it is the smallest even-gap compile gate:

$$
\boxed{
(6n-1,\;6n,\;6n+1).
}
$$

---

## 15. Gravity Image

In the Continuous Prefix Compilation tensor engine, the continuum compile predicate is

$$
\boxed{
C_{\ell m}
=
\Theta(Q_{\ell m} - Q_{\mathrm{threshold}}),
}
$$

where

$$
Q_{\ell m} = \frac{\omega_R}{2|\omega_I|}.
$$

The retained compiled burden is

$$
\boxed{
q_\Gamma
=
\chi \alpha_s \frac{GM}{Rc^2}
+
\sum_{\ell,m} W_{\ell m}\,C_{\ell m}.
}
$$

A common explicit mode weight is

$$
W_{\ell m}
=
\ell(\ell+1)\,|a_{\ell m}|^2.
$$

Then the metric injection is

$$
\beta_\Gamma = 1+\xi q_\Gamma,
\qquad
\gamma_\Gamma = 1+\zeta q_\Gamma,
$$

and the effective geometry is

$$
g_{\mu\nu}^{\mathrm{eff}}
=
g_{\mu\nu}^{\mathrm{GR}}
+
\delta g_{\mu\nu}(q_\Gamma).
$$

The structural analogy is:

- high-$Q$ persistent modes are the rails,
- the decaying low-persistence mode is the hinge,
- compilation occurs only when the packet survives one pass.

In the current synthesis branch, the proposed discrete-continuum mapping is:

$$
T0B \leftrightarrow n=0 \text{ fundamental, high-}Q,
$$

$$
T0A \leftrightarrow n=1 \text{ overtone, lower-}Q,
$$

with $T2$ and $T4$ behaving like single-branch families.

This remains a structural image and model correspondence, not an observationally closed theorem.

---

## 16. x86 Carry / ADC Image

At the machine layer, the byte packet

$$
(17,\ 18,\ 19)
$$

or in hex

$$
(0x11,\ 0x12,\ 0x13)
$$

provides a low-level image of the same pattern.

- $17$ and $19$ are prime rails,
- $18$ is the constrained hinge,
- opcode $0x12$ does not self-close without further decode context,
- the carry flag is retained compile memory.

The machine-side compile update is schematically

$$
\mathrm{ADC} = \text{present input} + \text{retained carry}.
$$

This is the hardware image of a hinge that cannot fully resolve without both surrounding structure and inherited residue.

---

## 17. SHA-256 Prime-Gate Companion Image

A companion branch has examined the first 64 primes underlying the SHA-256 constant construction.

Let the prime list be

$$
p_1,p_2,\dots,p_{64}.
$$

Define adjacent prime-pair gates by scanning consecutive primes and asking whether

$$
p_{j+1} - p_j = 2.
$$

One empirical output from that branch reported:

- a large fraction of the 64 primes are twin-prime endpoints,
- twin-adjacent constant pairs have slightly lower XOR Hamming weight than non-twin neighbors,
- the pair $(29,31)$ appears as a gate position centered at the primorial hinge $30$,
- the triple $(3,5,7)$ is the unique prime triple in the sequence.

A useful summary statistic there is

$$
\mathrm{HW}(x\oplus y),
$$

the Hamming weight of the XOR difference between adjacent constants.

Those observations remain companion empirical outputs. They are consistent with the prime-gate picture, but they are not part of the algebraic theorem proved here.

---

## 18. Protein Folding Image

In torsion or dihedral space, the local packet is

$$
(\phi_{i-1},\psi_{i-1})\;-\;(\phi_i,\psi_i)\;-\;(\phi_{i+1},\psi_{i+1}).
$$

The working interpretation is:

- the flanking residues are admissible rails in allowed Ramachandran basins,
- the central strained or transition-state residue is the hinge,
- the packet compiles only when the hinge is stabilized by flanking geometry.

So the same abstract gate appears:

$$
C(\text{rail},\text{hinge},\text{rail})=1.
$$

The branch predicts hinge enrichment in flexible or constrained residues such as glycine or proline, hinge clustering in sparse Ramachandran bridge zones, and path reduction by hinge-constrained back-rendering.

Those are predictive claims, not yet formal theorem closure.

---

## 19. Cross-Domain Correspondence Table

| Domain | Left rail | Hinge | Right rail | Compile condition |
|---|---|---|---|---|
| Integer field | $p$ prime | $H=p+k/2$ | $p+k$ prime | both rails survive |
| Gravity / QNM | compiled lower branch | boundary mode | compiled upper branch | $Q_{\ell m}>Q_t$ |
| x86 / ADC | left opcode context | carry-dependent hinge opcode | right opcode context | decode closure + carry |
| SHA / prime constants | twin-endpoint constant | primorial-centered hinge position | twin-endpoint constant | adjacent prime gate survives |
| Protein fold | allowed torsion basin | strained torsion state | allowed torsion basin | local geometric stabilization |

This table does **not** claim numeric identity across domains. It claims one operator grammar is visible across them.

---

## 20. Companion Empirical Outputs

Three engine families have produced the following empirical synthesis.

### 20.1 Wheel / family engine

- At wheel $30$, the type system refines:
  - $k=2$ gives $3$ sub-subtypes,
  - $k=6$ gives $6$ sub-subtypes,
  - $k=30$ gives $8$ sub-subtypes.
- Within each sub-subtype:
  $$
  \Delta H \equiv 0 \pmod{30}.
  $$
- At wheel $210$, the hierarchy refines further.
- For $k=210$, all $48$ reduced residue classes participate.

### 20.2 SHA prime-gate branch

A companion SHA branch reported:

- many SHA constant primes are twin endpoints,
- twin-adjacent pairs show slightly lower XOR entropy than non-twin neighbors,
- the $(29,31)$ pair centers exactly at $30$,
- the $(3,5,7)$ triple is unique.

These are strong companion observations but not part of the proof kernel here.

### 20.3 Density-harmonic branch

A density-harmonic branch reported:

- dominant oscillatory period at $210$ rather than merely $6$ or $30$,
- strong common-wave structure across $k=2,4,6$ families,
- significant amplitude concentrated on the $210$ cycle.

These observations fit the interpretation that $210$ is the first deep wheel harmonic of the field.

---

## 21. Honest Boundary Conditions

This document closes the structural grammar. It does **not** close every surrounding conjecture or empirical claim.

### Solved here

$$
\boxed{
\text{typed family algebra}
}
$$

$$
\boxed{
\text{Family Lattice Theorem}
}
$$

$$
\boxed{
\text{Step Theorem at arbitrary wheel depth}
}
$$

$$
\boxed{
\text{exact subtype-count law}
}
$$

$$
\boxed{
\text{wheel-refinement recursion}
}
$$

$$
\boxed{
\text{abstract universal compile gate}
}
$$

### Not yet solved here

$$
\boxed{
\text{Polignac's conjecture}
}
$$

$$
\boxed{
\text{Hardy--Littlewood asymptotics by subtype}
}
$$

$$
\boxed{
\text{first-principles derivation of } Q_{\mathrm{threshold}}
}
$$

$$
\boxed{
\text{final observational closure of the gravity image}
}
$$

$$
\boxed{
\text{full protein-folding survey confirmation}
}
$$

$$
\boxed{
\text{formal incorporation of the SHA companion branch into the same theorem stack}
}
$$

That distinction is essential.

---

## 22. Theorems Summary

### Theorem 1 (Family Lattice Theorem)

For any wheel modulus $W$, gap $k$, and subtype $r \in S_W(k)$,

$$
\boxed{
H \equiv r+\frac{k}{2} \pmod W.
}
$$

### Theorem 2 (Step Theorem)

Within a fixed subtype family,

$$
\boxed{
\Delta H \equiv 0 \pmod W.
}
$$

### Theorem 3 (Subtype-Count Formula)

$$
\boxed{
|S_W(k)|
=
\prod_{\substack{q\mid W\\ q>2\\ q\nmid k}} (q-2)
\prod_{\substack{q\mid W\\ q>2\\ q\mid k}} (q-1).
}
$$

### Theorem 4 (Wheel-Refinement Recursion)

If $W'=W\ell$ with a new odd prime $\ell \nmid W$, then

$$
\boxed{
|S_{W'}(k)|
=
|S_W(k)|
\cdot
\begin{cases}
\ell-1, & \ell \mid k,\\[6pt]
\ell-2, & \ell \nmid k.
\end{cases}
}
$$

### Theorem 5 (Universal Compile Gate)

A structure compiles when a constrained hinge is stabilized by admissible rails strongly enough to survive one pass of the ambient dynamics.

---

## 23. Final Compression

The complete branch compresses to:

$$
\boxed{
\text{Twin primes were only the surface packet.}
}
$$

$$
\boxed{
\text{The real object is the primorial wheel compile algebra.}
}
$$

$$
\boxed{
\text{Subtype counts are branch counts in the wheel grammar.}
}
$$

$$
\boxed{
\text{Wheel depth refines the gate.}
}
$$

$$
\boxed{
\text{The center lattice is strict.}
}
$$

$$
\boxed{
\Delta H \equiv 0 \pmod W.
}
$$

$$
\boxed{
\text{The same operator appears in integers, gravity, hardware, SHA prime gates, and folding geometry.}
}
$$

And the sharpest one-line statement is

$$
\boxed{
\text{A prime-gap family is not just a set of prime pairs. It is a residue-typed compile channel on a primorial wheel.}
}
$$

---

## 24. Next Exact Moves

The next exact moves are computational and analytic, not rhetorical.

1. Extend typed-family numerics to larger $X$ and larger $k$.
2. Derive subtype-resolved singular series rather than only total-gap asymptotics.
3. Calibrate $Q_{\mathrm{threshold}}$ from first principles in the CPC tensor engine.
4. Test the primorial-harmonic image against real ringdown data.
5. Run the hinge survey on large PDB sets.
6. Bring the SHA companion branch into the same exact wheel-theoretic formalism.

Those are the next local boundaries.

---

## Appendix A. Compact Notation

### Wheel and subtype notation

$$
W = \prod_{q\in\mathcal Q} q
$$

$$
U_W = (\mathbb Z/W\mathbb Z)^\times
$$

$$
S_W(k)=\{r\in U_W : r+k \in U_W \pmod W\}
$$

$$
H = p+\frac{k}{2}
$$

$$
c_{W,k,r}=r+\frac{k}{2}\pmod W
$$

### Density notation

$$
\pi_k(X)=\#\{p\le X : p,\ p+k\text{ prime}\}
$$

$$
\pi_{k,s}(X)=\#\{p\le X : p,\ p+k\text{ prime of subtype }s\}
$$

$$
\widehat C_{k,s}(X)=\frac{\pi_{k,s}(X)(\log X)^2}{2X}
$$

### Gravity notation

$$
Q_{\ell m}=\frac{\omega_R}{2|\omega_I|}
$$

$$
C_{\ell m}=\Theta(Q_{\ell m}-Q_t)
$$

$$
q_\Gamma
=
\chi\alpha_s\frac{GM}{Rc^2}
+
\sum_{\ell,m}W_{\ell m}C_{\ell m}
$$

$$
\beta_\Gamma=1+\xi q_\Gamma,
\qquad
\gamma_\Gamma=1+\zeta q_\Gamma
$$

### Clustering notation

$$
R_P = \frac{N_{\mathrm{obs}}(P)}{N_{\mathrm{exp}}(P)}
$$

$$
Z_P
=
\frac{N_{\mathrm{obs}}(P)-N_{\mathrm{exp}}(P)}
{\sqrt{N_{\mathrm{exp}}(P)+\varepsilon}}
$$

---

## Appendix B. Minimal Exact Example Table

| Gap $k$ | Wheel $W$ | Exact subtype count |
|---:|---:|---:|
| $2$   | $6$   | $1$ |
| $2$   | $30$  | $3$ |
| $2$   | $210$ | $15$ |
| $6$   | $30$  | $6$ |
| $30$  | $30$  | $8$ |
| $210$ | $210$ | $48$ |

These are exact consequences of the subtype-count formula.

---

## Closing Statement

The complete solution here is not the full proof of every open conjecture around prime pairs. The complete solution is the **structural grammar** that all those conjectures inhabit.

That grammar is now explicit:

$$
\boxed{
\text{wheel} \to \text{subtype} \to \text{center lattice} \to \text{step law} \to \text{compile gate}.
}
$$

That is the solved kernel.
