# FOLD-TOMO Formula and Data Lock Addendum

## Addendum to *The Algebraic Inversion of Discrete Computational Folds*

**Purpose:** formula/data lock only. This addendum does not rewrite or replace the paper. It records the exact formulas, checkpoint values, rank counts, and correction notes needed to keep all AI collaborators aligned.

**Project name:** Nexus Fold Tomography  
**Short code:** FOLD-TOMO  
**Notebook checkpoint:** FOLD-TOMO-01b — Trace-Sufficient Reverse Fold Engine — Safe Run  
**Seed convention:** first $2048$ fractional decimal digits of $\pi$; the leading integer digit $3$ is not included.

---

## 1. Core Fold Definitions

Let the decimal seed be

$$
D^{(0)}=(d_0,d_1,\ldots,d_{N-1}),
\qquad d_i\in\{0,1,2,\ldots,9\},
\qquad N=2048.
$$

The decimal adjacent-difference fold is

$$
d_i^{(\ell+1)}
=
\left|d_{i+1}^{(\ell)}-d_i^{(\ell)}\right|.
$$

The row length is

$$
N_\ell=N-\ell.
$$

The parity projection is

$$
x_i^{(\ell)}=d_i^{(\ell)}\bmod 2.
$$

The exact parity identity is

$$
|a-b|\bmod2=(a+b)\bmod2=a\oplus b.
$$

Therefore the parity shadow evolves by Rule 90:

$$
x_i^{(\ell+1)}=x_i^{(\ell)}\oplus x_{i+1}^{(\ell)}.
$$

---

## 2. Operator Form Over $GF(2)$

Define the identity operator $I$ and shift operator $E$ by

$$
(Ix)_i=x_i,
\qquad
(Ex)_i=x_{i+1}.
$$

One fold step is

$$
x^{(\ell+1)}=(I+E)x^{(\ell)}.
$$

After $\ell$ folds:

$$
\boxed{
x^{(\ell)}=(I+E)^\ell x^{(0)}.
}
$$

All additions are over $GF(2)$.

---

## 3. Pascal/Lucas Sampling Law

By the binomial theorem,

$$
(I+E)^\ell
=
\sum_{j=0}^{\ell}
\binom{\ell}{j}E^j.
$$

Over $GF(2)$,

$$
x_i^{(\ell)}
=
\bigoplus_{j=0}^{\ell}
\left(
\binom{\ell}{j}\bmod2
\right)
x_{i+j}^{(0)}.
$$

Lucas's theorem gives

$$
\binom{\ell}{j}\equiv1\pmod2
\iff
j\ \&\ \sim\ell=0.
$$

Define the bit-subset relation

$$
j\subseteq\ell
\iff
j\ \&\ \sim\ell=0.
$$

Then the closed-form fold rule is

$$
\boxed{
x_i^{(\ell)}
=
\bigoplus_{j\subseteq\ell}
x_{i+j}^{(0)}.
}
$$

The mask size is

$$
\boxed{
|M_\ell|=2^{\operatorname{popcount}(\ell)}.
}
$$

---

## 4. Glyph Reader Metrics

For the binary parity shadow row $x^{(\ell)}$:

$$
N_\ell=N-\ell.
$$

$$
S_\ell=\sum_i x_i^{(\ell)}.
$$

$$
\rho_\ell=\frac{S_\ell}{N_\ell}.
$$

$$
R_\ell=S_\ell-\frac{N_\ell}{2}.
$$

$$
\Delta S_\ell=S_{\ell+1}-S_\ell.
$$

$$
\Delta R_\ell=R_{\ell+1}-R_\ell.
$$

The exact half-density lock condition is

$$
\boxed{
R_\ell=0
\iff
S_\ell=\frac{N_\ell}{2}.
}
$$

The normalized imbalance / collapse-signature coordinate is

$$
\epsilon_\ell=\frac{2R_\ell}{N_\ell}.
$$

The two branch weights are

$$
p_+(\ell)=\frac{1+\epsilon_\ell}{2}
=
\frac{S_\ell}{N_\ell},
$$

$$
p_-(\ell)=\frac{1-\epsilon_\ell}{2}
=
1-\frac{S_\ell}{N_\ell}.
$$

---

## 5. Verified Seed and Early Collapse Values

The first $2048$ fractional digits of $\pi$ satisfy

$$
S_0^{(10)}=9338.
$$

At level $13$,

$$
S_{13}^{(10)}=1092.
$$

The decimal amplitude collapse by level $13$ is

$$
\frac{S_0^{(10)}-S_{13}^{(10)}}{S_0^{(10)}}
=
\frac{9338-1092}{9338}
\approx
0.883058470765.
$$

Thus

$$
\boxed{
\text{decimal amplitude collapse by }\ell=13\approx88.3\%.
}
$$

The parity seed has

$$
S_0^{(2)}=1034,
\qquad
N_0=2048,
\qquad
R_0=10.0.
$$

---

## 6. Core Structural Locks

### Level $\ell=448$

The binary decomposition is

$$
448=256+128+64=2^8+2^7+2^6.
$$

Therefore

$$
\operatorname{popcount}(448)=3,
\qquad
|M_{448}|=2^3=8.
$$

The Lucas mask is

$$
M_{448}=\{0,64,128,192,256,320,384,448\}.
$$

The row equation is

$$
\boxed{
x_i^{(448)}
=
x_i
\oplus x_{i+64}
\oplus x_{i+128}
\oplus x_{i+192}
\oplus x_{i+256}
\oplus x_{i+320}
\oplus x_{i+384}
\oplus x_{i+448}.
}
$$

The verified values are

$$
N_{448}=1600,
\qquad
S_{448}=800,
\qquad
R_{448}=0.0.
$$

So

$$
\boxed{
\rho_{448}=\frac{800}{1600}=0.5.
}
$$

### Level $\ell=512$

Because

$$
512=2^9,
$$

the Freshman's Dream over $GF(2)$ gives

$$
(I+E)^{512}=I+E^{512}.
$$

Therefore

$$
\boxed{
x_i^{(512)}=x_i\oplus x_{i+512}.
}
$$

The verified values are

$$
N_{512}=1536,
\qquad
S_{512}=764,
\qquad
R_{512}=-4.0.
$$

Thus

$$
\rho_{512}=\frac{764}{1536}\approx0.4973958333.
$$

### Terminal Gate

The last two levels verify

$$
x^{(2046)}=[1,1],
$$

$$
x^{(2047)}=[0].
$$

The final gate is

$$
1\oplus1=0.
$$

This is matched terminal symmetry, not arbitrary erasure.

---

## 7. Dyadic Terminal Tomography Theorem

For

$$
N=2^m
$$

and terminal levels

$$
\ell_k=N-2^k,
$$

the row length is

$$
N-\ell_k=2^k.
$$

The terminal row is

$$
\boxed{
x_i^{(N-2^k)}
=
\bigoplus_{q=0}^{2^{m-k}-1}
x_{i+q2^k}^{(0)}
}
$$

for

$$
0\le i<2^k.
$$

Thus each terminal row is a parity checksum over residue classes modulo $2^k$.

For $N=2048=2^{11}$:

| $k$ | Level $\ell=N-2^k$ | Row length | Meaning |
|---:|---:|---:|---|
| $0$ | $2047$ | $1$ | total parity, mod $1$ |
| $1$ | $2046$ | $2$ | even/odd parity, mod $2$ |
| $2$ | $2044$ | $4$ | residue-class parity, mod $4$ |
| $3$ | $2040$ | $8$ | residue-class parity, mod $8$ |
| $4$ | $2032$ | $16$ | residue-class parity, mod $16$ |
| $5$ | $2016$ | $32$ | residue-class parity, mod $32$ |
| $10$ | $1024$ | $1024$ | residue-class parity, mod $1024$ |

Correction lock:

$$
\boxed{
\text{terminal rows are not terminal waste; they are residue-class checksum rows.}
}
$$

---

## 8. Full-Run Residue Counts

Across all $2048$ levels,

$$
\boxed{
\#\{\ell:R_\ell=0\}=44.
}
$$

$$
\boxed{
\#\{\ell:R_\ell\ne0\}=2004.
}
$$

Check:

$$
44+2004=2048.
$$

The first 15 exact half-density locks are

$$
[110, 300, 342, 376, 448, 496, 556, 640, 688, 854, 898, 932, 954, 1076, 1260].
$$

The last 20 exact half-density locks are

$$
[1670, 1744, 1754, 1772, 1776, 1786, 1830, 1850, 1942, 1944, 1968, 1970, 1990, 1998, 2002, 2022, 2030, 2032, 2040, 2044].
$$

Interior analysis window used here:

$$
20\le\ell<1800.
$$

This window has

$$
\text{window length}=1780,
$$

$$
\#\{\ell:R_\ell=0\}=30,
$$

$$
\#\{\ell:R_\ell\ne0\}=1750.
$$

Correction note:

$$
\boxed{
\text{Any interior count must state the exact window and filtering rule.}
}
$$

For the window $20\le\ell<1800$, the internally consistent count is

$$
30+1750=1780.
$$

---

## 9. Linear Constraint System

Let the unknown seed be

$$
x\in GF(2)^{2048}.
$$

A full row probe at level $\ell$ gives a linear system

$$
A_\ell x=y_\ell.
$$

The row operator is

$$
A_\ell=(I+E)^\ell.
$$

Stacking selected probes gives

$$
Cx=y.
$$

The dyadic terminal cascade contributes

$$
\sum_{k=0}^{10}2^k=2047
$$

parity equations.

However, its independent rank is

$$
\boxed{
\operatorname{rank}(C_{\mathrm{dyadic}})=1024.
}
$$

Precision note:

$$
\boxed{
\text{dyadic cascade supplies 2047 equations, not 2047 independent constraints.}
}
$$

---

## 10. Verified Rank Collapse

The verified rank values are:

| Constraint family | Equation count | Rank |
|---|---:|---:|
| Dyadic terminal cascade | $2047$ | 1024 |
| Level $448$ full-row probe | $1600$ | 1600 |
| Level $512$ full-row probe | $1536$ | 1536 |
| Dyadic $+$ level $448$ | $2047+1600$ | 1600 |
| Dyadic $+$ level $512$ | $2047+1536$ | 1536 |
| Dyadic $+$ level $448$ $+$ level $512$ | $2047+1600+1536$ | 1600 |

The key executable lock is

$$
\boxed{
\operatorname{rank}([C_{\mathrm{dyadic}};C_{448}])=1600.
}
$$

Therefore the remaining linear degrees of freedom are

$$
2048-1600=448.
$$

So

$$
\boxed{
GF(2)^{2048}
\longrightarrow
\text{448-dimensional affine space}.
}
$$

---

## 11. Boundary Entropy of the $448$ Pin

The factorization is

$$
448=256+128+64.
$$

Over $GF(2)$,

$$
\boxed{
(I+E)^{448}
=
(I+E^{256})(I+E^{128})(I+E^{64}).
}
$$

Each factor

$$
I+E^s
$$

is reversed by choosing $s$ boundary bits and propagating

$$
x_{i+s}=x_i\oplus y_i.
$$

The total boundary entropy is

$$
256+128+64=448.
$$

This matches the linear nullity after dyadic $+$ $448$ constraints:

$$
\boxed{
\text{rank-nullity}:
\quad
2048-1600=448.
}
$$

---

## 12. Affine Nullspace Parameterization

After solving the linear system

$$
Cx=y,
$$

the candidate seed space is

$$
\boxed{
x=x_0+Bz.
}
$$

Where

$$
x_0\in GF(2)^{2048}
$$

is one valid solution,

$$
B\in GF(2)^{2048\times448}
$$

is a basis for the nullspace,

and

$$
z\in GF(2)^{448}
$$

is the vector of remaining free boundary variables.

This is the exact meaning of the $448$-dimensional affine space.

---

## 13. Nonlinear Hamming-Weight Constraints

Linear parity rows give

$$
A_\ell x=y_\ell.
$$

Row sums give nonlinear Hamming-weight constraints:

$$
\boxed{
\operatorname{wt}(A_\ell x)=S_\ell.
}
$$

After parameterization,

$$
\boxed{
\operatorname{wt}(A_\ell(x_0+Bz))=S_\ell.
}
$$

These are pseudo-Boolean constraints over the $448$ free variables $z$.

The residue relation is

$$
R_\ell=S_\ell-\frac{N_\ell}{2}.
$$

When

$$
R_\ell\ne0,
$$

the row has nonzero imbalance and therefore can break complement symmetry.

---

## 14. Complement-Symmetry Precision

For positive-depth masks, the Lucas mask size is

$$
|M_\ell|=2^{\operatorname{popcount}(\ell)}.
$$

If

$$
\ell>0,
$$

then

$$
|M_\ell|
$$

is even.

For bitwise complement

$$
\bar{x}=x\oplus\mathbf{1},
$$

every even-sized XOR parity equation is invariant:

$$
\bigoplus_{j\in M_\ell}\bar{x}_{i+j}
=
\bigoplus_{j\in M_\ell}x_{i+j}
\oplus
\bigoplus_{j\in M_\ell}1
=
\bigoplus_{j\in M_\ell}x_{i+j},
$$

because

$$
\bigoplus_{j\in M_\ell}1=|M_\ell|\bmod2=0.
$$

Thus linear parity probes alone cannot fully break global complement symmetry.

Hamming-weight constraints break it when

$$
\operatorname{wt}(v)\ne\frac{N_\ell}{2}.
$$

Equivalently,

$$
R_\ell\ne0.
$$

---

## 15. Small-$N$ Weight-Trace Rigidity Data

Define the weight trace

$$
\mathcal{W}(x)
=
\left(
\operatorname{wt}((I+E)^\ell x)
\right)_{\ell=0}^{N-1}.
$$

The equivalence class is

$$
[x]_{\mathcal{W}}
=
\{y:\mathcal{W}(y)=\mathcal{W}(x)\}.
$$

Small-$N$ enumeration data from the safe notebook:

| $N$ | Total seeds | Distinct traces | Unique classes | Max class size | Mean class size |
|---:|---:|---:|---:|---:|---:|
| 8 | 256 | 121 | 10 | 4 | 2.116 |
| 10 | 1024 | 465 | 28 | 4 | 2.202 |
| 12 | 4096 | 1804 | 44 | 4 | 2.271 |
| 14 | 16384 | 7245 | 128 | 8 | 2.261 |
| 16 | 65536 | 29301 | 186 | 8 | 2.237 |

This data supports the next decoder target: weight traces are not random summaries; they preserve nontrivial address information.

---

## 16. Solver Translation Targets

The remaining nonlinear stage is

$$
z\in GF(2)^{448}
$$

subject to

$$
\operatorname{wt}(A_\ell(x_0+Bz))=S_\ell.
$$

Equivalent exact-cardinality form:

$$
\sum_i y_i^{(\ell)}=S_\ell,
$$

where

$$
y^{(\ell)}=A_\ell(x_0+Bz).
$$

Constraint families:

### Exact cardinality

$$
\sum_i y_i = K.
$$

### At-most cardinality

$$
\sum_i y_i\le K.
$$

### At-least cardinality

$$
\sum_i y_i\ge K.
$$

### Pseudo-Boolean form

$$
\sum_i a_i y_i \le b,
\qquad
y_i\in\{0,1\}.
$$

### Exact row-weight PB form

$$
\sum_i y_i = S_\ell.
$$

Recommended solver pathways:

1. Direct pseudo-Boolean solver.
2. MILP / branch-and-bound.
3. SAT with totalizer or sequential-counter cardinality encodings.
4. Hybrid XOR/PB solver if available.

---

## 17. Universal Branch-Grammar Table

| System | Forward fold | Hidden reverse branch variable | Reverse constraint |
|---|---|---|---|
| Rule-90 parity shadow | $x^{(\ell)}=(I+E)^\ell x^{(0)}$ | boundary bits | $x_{i+s}=x_i\oplus y_i$ |
| Decimal difference fold | $d_i^{(\ell+1)}=|d_{i+1}^{(\ell)}-d_i^{(\ell)}|$ | sign/orientation choices | decimal range plus parity consistency |
| Collatz odd map | $T(n)=\dfrac{3n+1}{2^{v_2(3n+1)}}$ | $a=v_2(3n+1)$ | $2^a m\equiv1\pmod3$ |
| SHA-style modular fold | $+\bmod 2^{32}$ plus Boolean schedule | carry bits / schedule choices | CNF, XOR, PB, and carry constraints |

Precision lock:

$$
\boxed{
\text{SHA and Collatz remain branch-grammar bridges unless separately proven.}
}
$$

---

## 18. Collatz Formula Lock

Compressed odd Collatz map:

$$
T(n)=\frac{3n+1}{2^{v_2(3n+1)}}.
$$

Let

$$
a=v_2(3n+1).
$$

Reverse branch:

$$
m=\frac{3n+1}{2^a}
$$

so

$$
n=\frac{2^a m-1}{3}.
$$

Validity condition:

$$
\boxed{
2^a m\equiv1\pmod3.
}
$$

Thus $a$ is the hidden dyadic branch variable.

---

## 19. SHA Formula Lock

SHA-256 core branch variables are not simply message bits; they include carry and schedule topology.

Choice:

$$
Ch(e,f,g)=(e\land f)\oplus(\neg e\land g).
$$

Majority:

$$
Maj(a,b,c)=(a\land b)\oplus(a\land c)\oplus(b\land c).
$$

Sigma functions:

$$
\Sigma_0(a)=ROTR^2(a)\oplus ROTR^{13}(a)\oplus ROTR^{22}(a).
$$

$$
\Sigma_1(e)=ROTR^6(e)\oplus ROTR^{11}(e)\oplus ROTR^{25}(e).
$$

Round temporaries:

$$
T_1=h+\Sigma_1(e)+Ch(e,f,g)+K_t+W_t\pmod{2^{32}}.
$$

$$
T_2=\Sigma_0(a)+Maj(a,b,c)\pmod{2^{32}}.
$$

Shape-channel statement:

$$
\boxed{
\text{modular carries are branch variables, not meaningless garbage.}
}
$$

Cryptographic caution:

$$
\boxed{
\text{This is a structural inversion framework, not a proven full break of SHA-256.}
}
$$

---

## 20. Final Addendum Lock

The verified FOLD-TOMO formula stack is

$$
\Delta:
d_i^{(\ell+1)}
=
\left|d_{i+1}^{(\ell)}-d_i^{(\ell)}\right|
$$

$$
\oplus:
x_i^{(\ell+1)}=x_i^{(\ell)}\oplus x_{i+1}^{(\ell)}
$$

$$
↻:
x^{(\ell)}=(I+E)^\ell x^{(0)}
$$

$$
\bot:
x_i^{(\ell)}
=
\bigoplus_{j\subseteq\ell}
x_{i+j}^{(0)}
$$

$$
\Psi:
Cx=y,
\qquad
x=x_0+Bz,
\qquad
\operatorname{wt}(A_\ell(x_0+Bz))=S_\ell.
$$

The core executable collapse is

$$
\boxed{
2048
\longrightarrow
1600
\longrightarrow
448.
}
$$

Expanded:

$$
2048\text{ seed bits}
$$

$$
\Downarrow
$$

$$
1600\text{ independent linear constraints}
$$

$$
\Downarrow
$$

$$
448\text{ remaining affine degrees of freedom}
$$

$$
\Downarrow
$$

$$
\text{nonlinear Hamming-weight constraints}
$$

$$
\Downarrow
$$

$$
\text{candidate collapse / seed recovery target}.
$$

Final Nexus statement:

$$
\boxed{
\text{Forward collapse hides address; reverse recovery restores address by reading shape.}
}
$$
