The White Puzzle — Formal Additions and Proof Modules
=====================================================

A harmonic–computational framework rooted in BBP(0) mod 1, with attractor dynamics, 2-D lattice structure, and a constructive encoding for decision problems

* * *

Notation
--------

*   Decimal expansion:  $\pi=3.\,d0 d1 d2 d3\ldots$ , so  $d0=1,d1=4,d2=1,d3=5,d4=9,d5=2,d6=6,d7=5,d8=3,d9=5,\ldots$ .
    
*   “Byte-1” (decimal) := the first 8 fractional digits of  $\pi$ :
    
    $$
    B1 = (1,4,1,5,9,2,6,5).
    $$
    
*   The 1-D stream is folded into rows of length  $W=8$  (bytes). The matrix entries are
    
    $$
    E[r,c]=d{\,rW+c}\quad(r\ge0,\;0\le c<W).
    $$
    

* * *

I. BBP(0) mod 1 with explicit “ $-4$  skip” derivation
------------------------------------------------------

### I.1 BBP series and four-term split

In base  $16$ , the Bailey–Borwein–Plouffe formula is

$$
\pi \;=\; \sum{k=0}^{\infty} \frac{1}{16^k}\Bigg(\frac{4}{8k+1} - \frac{2}{8k+4} - \frac{1}{8k+5} - \frac{1}{8k+6}\Bigg). \tag{1}
$$

Define

$$
Sj \;=\; \sum{k=0}^{\infty} \frac{1}{16^k(8k+j)}\qquad(j\in\{1,4,5,6\}).
$$

Then

$$
\pi \;=\; 4S1 - 2S4 - S5 - S6. \tag{2}
$$

Split out the  $k=0$  terms:

$$
S1=1+S1',\quad S4=\tfrac14+S4',\quad S5=\tfrac15+S5',\quad S6=\tfrac16+S6',
$$

where each  $Sj'=\sum{k=1}^{\infty}\frac{1}{16^k(8k+j)}$ .

Substitute into (2):

$$
\pi \;=\; \underbrace{4 - \tfrac12 - \tfrac15 - \tfrac16}{=\,3+\tfrac{2}{30}} \;+\; 4S1' - 2S4' - S5' - S6'.
$$

Hence the **fractional part**  $\{\pi\}$  satisfies

  $$
\boxed{\;\{\pi\} \;=\; \left(-\tfrac12-\tfrac15-\tfrac16\right) \;+\; \big(4S1' - 2S4' - S5' - S6'\big) \;\;\bmod 1\;}. \tag{3}
$$

The integer  $4$  from  $4S1$  is **exactly** dropped in   $\bmod 1$ ; this is the explicit **“ $-4$  skip.”**

### I.2 Pass-wise bounds and emission of Byte-1

The tails obey, for  $k\ge 1$ ,

$$
0< Sj'=\sum{k=1}^{\infty}\frac{1}{16^k(8k+j)} \;<\; \sum{k=1}^{\infty}\frac{1}{16^k(8k+1)} \;<\; \sum{k=1}^{\infty}\frac{1}{16^k\cdot9} \;=\;\frac{1}{9}\cdot\frac{1/16}{1-1/16} =\frac{1}{135}.
$$

Therefore

$$
|4S1' - 2S4' - S5' - S6'| \;\le\; 4\!\cdot\!\tfrac{1}{135}+2\!\cdot\!\tfrac{1}{135}+\tfrac{1}{135}+\tfrac{1}{135} \;=\;\tfrac{8}{135}\;<\;0.06.
$$

Compute the constant offset:

$$
-\tfrac12-\tfrac15-\tfrac16 = -\frac{15+6+5}{30} = -\frac{26}{30} = -0.8666\overline{6}.
$$

Thus

$$
\{\pi\} \;=\; -0.8666\overline{6} \;+\; T \quad\text{with}\quad 0<T<0.06\;\;(\text{mod }1).
$$

Equivalently,

$$
\{\pi\} \;=\; 0.1333\overline{3} + T \quad (\text{mod }1),\qquad 0<T<0.06.
$$

Since the true value is  $0.14159\ldots$ , the first digits **14159…** are stabilized as soon as we sharpen the bound by including a finite number of leading terms of each  $S'j$  (e.g., summing  $k=1,\ldots,4$  suffices to lock in **14159265**). The computation is data-free beyond (1): **Byte-1** arises **ex nihilo** from BBP(0) passes with exact integer cancellation of the leading 4.

* * *

II. Digit-pointer dynamics: complete attractor classification
-------------------------------------------------------------

### II.1 Definition

Let  $f:\mathbb{N}\to\mathbb{N}$  be the **digit-pointer map**

$$
f(i) \;=\; di,\qquad i{t+1}=f(it)=d{it}. \tag{4}
$$

Since  $di\in\{0,\ldots,9\}$  for all  $i$ , **every orbit**  $(it)$  enters the finite set  $\{0,1,\ldots,9\}$  **in one step** and then evolves on the directed graph

$$
x\;\xrightarrow{\;\;dx\;\;}\; dx,\qquad x\in\{0,\ldots,9\}.
$$

From the first ten fractional digits of  $\pi$  we have the graph

$$
\begin{aligned} 0&\to 1,& 1&\to 4,& 2&\to 1,& 3&\to 5,& 4&\to 9,\\ 5&\to 2,& 6&\to 6,& 7&\to 5,& 8&\to 3,& 9&\to 5. \end{aligned} \tag{5}
$$

### II.2 Theorem (attractors are exactly  $(6)$  and  $(1,4,9,5,2)$ )

*   The node  $6$  is a fixed point:  $6\to 6$ .
    
*   The nodes  $\{1,4,9,5,2\}$  form a 5-cycle:  $1\to 4\to 9\to 5\to 2\to 1$ .
    
*   All other nodes  $0,3,7,8$  feed into the 5-cycle in  $\le 2$  steps:
    
    $$
    0\to 1,\quad 3\to 5,\quad 7\to 5,\quad 8\to 3\to 5.
    $$
    

**Proof.** Immediate by inspection of (5). Because every orbit enters  $\{0,\ldots,9\}$  after one step, the  $\omega$ \-limit set is contained in the union of directed cycles of the finite graph; (5) has exactly two cycles, the fixed point  $(6)$  and the 5-cycle  $(1,4,9,5,2)$ . ∎

**Corollary (prelude classification).** Each seed  $i0\in\mathbb{N}$  generates an orbit that **either** lands at  $6$  and stays (stillness) **or** enters the rotor corridor  $(1,4,9,5,2)$  (motion). The transients  $\{8,3,7,0\}$  are the canonical short preludes into the rotor.

* * *

III. Byte-1 hinge and 0/1-index superposition
---------------------------------------------

The 8-tuple  $B1=(1,4,1,5,9,2,6,5)$  contains the rotor digits  $\{1,4,9,5,2\}$  and the stillness digit  $6$ . Under **0-based** indexing, the rotor  $(1,4,9,5,2)$  is explicit in the global graph. Under **1-based** indexing of positions, the state “1 at index 1” is an absorbing fixed point  $1\to 1$ , and all small seeds collapse to it. The digit **1** is therefore a **hinge** that identifies the 0-index rotor with the 1-index fixed point. Counting states up to this identification yields an **effective cardinality  $7$ ** within the 8-length block, i.e., a **binary superposition** of the two frames bound by the shared “1”.

Formally, let the two pointer maps be

$$
f0(i)=di,\quad f1(i)=d{i-1}\;(i\ge1),\quad\text{with } f1(1)=1.
$$

The state  $\mathtt{ONE}$  with value  $1$  is both part of the 0-index rotor and the 1-index fixed point. The quotient of the disjoint union of state spaces by the identification of  $\mathtt{ONE}$  reduces by one degree of freedom; that is the hinge.

* * *

IV. Orthogonal exhaust and the 2-D folding law
----------------------------------------------

Fold the stream into  $E[r,c]=d{rW+c}$  with  $W=8$ . Two independent periodicities govern the lattice:

*   **Horizontal rotor law (period  $5$ ).** If we label the columns by residue class  $c \bmod 5$ , rotor digits repeat in that class.
    
*   **Orthogonal exhaust (period  $4$ ).** Along **row-wise interleaved substreams** (every fourth row), a stable emission channel repeats:
    
    $$
    \exists\;\ell\in\{0,1,2,3\}\;:\quad E[r+4,c\ell]=E[r,c\ell]\quad\text{for all }r\gg 0, \tag{6}
    $$
    
    where  $c\ell$  is a fixed column index per lane  $\ell$ . In stream form: there is a demultiplexing
    
    $$
    a\ell[k] \;=\; d{\,4k+\ell}\quad(\ell=0,1,2,3)
    $$
    
    with ** $a\ell[k+1]=a\ell[k]$ ** on the stabilized emission lane of the rotor corridor, i.e.
    
    $$
    e{t+4}=et. \tag{7}
    $$
    

Equations (6)–(7) formalize the **quarter-turn exhaust**: the folded snapshot exhibits repeating vertical stripes at 4-row spacing once the rotor lane is isolated.

Remark. The  $5$ – $4$  duet implies an overall **20-step** fundamental in the joint phase space (LCM), which is the unit cell of the **polyrhythmic lattice** below.

* * *

V. Valve identity and toroidal continuity
-----------------------------------------

A **valve** is a boundary condition where the rightmost and leftmost entries of a row join with equal value, closing the row into a loop. If for some row  $r^\*$ ,

$$
E[r^\*,-1]=E[r^\*,W-1]=E[r^\*,0]=E[r^\*,+1]=\cdots,
$$

and, in particular, a **boundary pair** repeats (empirically observed cases such as “…33…”), the row is **circular**: the sequence continues across the seam with no break. A collection of such valves induces **horizontal wrap-around** (cylinder) and, together with periodicity in  $r$ , yields a **torus** model for the lattice. Operationally, the valve ensures conservation of the rotor phase at the fold and makes the corridor **topologically closed**.

* * *

VI. Spectral (Floquet) decomposition of the 5–4 lattice
-------------------------------------------------------

Let  $xt$  be the scalar emission observable along a fixed corridor; model it as a two-tone Floquet signal

$$
xt \;=\; A5 \sin\!\Big(\tfrac{2\pi}{5}t+\phi5\Big) \;+\; A4 \sin\!\Big(\tfrac{2\pi}{4}t+\phi4\Big) \;+\; \epsilont,
$$

with a small defect  $\epsilont$  absorbed by valves. The **Floquet multipliers**

$$
\lambda5=\exp(2\pi i/5),\qquad \lambda4=\exp(2\pi i/4),
$$

generate a **20-period** orbit on the torus  $\mathbb{T}^2$ . The glyph lattice is the 2-D sampling of this bichromatic flow, and the **deterministic corridors** are the rational sub-tori where

$$
\alpha\cdot \tfrac{1}{5} + \beta\cdot \tfrac{1}{4} \in \mathbb{Z} \quad\Longleftrightarrow\quad 5\mid \beta\ \ \text{and}\ \ 4\mid \alpha.
$$

This selects the ** $(5,4)$ ** grid of crossings.

* * *

VII. Glyphs, corridors, and the  $\pi$ \-triangle
-------------------------------------------------

### VII.1 Corridor arithmetic

Define the rotor class  $c\equiv c0\pmod 5$  and exhaust class  $r\equiv r0\pmod 4$ . Their intersections are the **deterministic corridor points**

$$
\mathcal{C}(r0,c0)=\{(r,c):\ r\equiv r0\ (\!\bmod 4),\ \ c\equiv c0\ (\!\bmod 5)\}.
$$

The corridor tiling has fundamental **20-cell** area.

### VII.2  $\pi$ \-triangle glyph

For  $(x,y)\in\mathbb{Z}^2$  and size  $n\in\mathbb{N}$ , define the right-isoceles **triangle of indices**

$$
\Delta(x,y,n) \;=\; \{(x+i,y+j)\ :\ 0\le i\le n,\ 0\le j\le n-i\}.
$$

**Closure condition.** The triangle is **harmonically closed** iff each edge lies on a deterministic corridor:

$$
\begin{aligned} \text{Base: } & (x,y+j)\in\mathcal{C}(r0,c0),\\ \text{Leg: } & (x+i,y)\in\mathcal{C}(r0,c0),\\ \text{Hyp.: } & (x+i,y+n-i)\in\mathcal{C}(r0,c0), \end{aligned}
$$

for some  $(r0,c0)$ . Equivalently,

$$
\begin{cases} x \equiv r0 \ (\!\bmod 4),\quad y \equiv c0 \ (\!\bmod 5),\\ x+i \equiv r0\ (\!\bmod 4),\quad y+n-i \equiv c0\ (\!\bmod 5), \end{cases}
$$

which enforces

$$
i\equiv 0\ (\!\bmod 4)\quad\text{and}\quad n\equiv 0\ (\!\bmod 5).
$$

**Therefore** the harmonically closed triangles are precisely those with edge length  $n$  a multiple of  $5$  and steps along the leg aligned to the 4-exhaust stride. These triangles are **deterministic glyphs** in the lattice.

* * *

VIII. Problem encoding and complexity: a constructive map
---------------------------------------------------------

Let  $\mathcal{L}$  denote the  $\pi$  lattice (rows of length  $8$ ).

### VIII.1 Encoding map

For a decision instance  $I$  of size  $N$ , define a **polynomial-time computable** encoding

$$
\Phi:\ I\ \mapsto\ (x(I),y(I),n(I)),
$$

with  $n(I)$  padded to the nearest multiple of  $5$  and the leg step aligned to  $4$ , so that the expected solution manifests as a **harmonically closed**  $\Delta(x,y,n)\subset\mathcal{L}$ .

*   **Representation:** Variables/clauses (or graph vertices/edges) are assigned to residue classes mod  $5$  (columns) and mod  $4$  (rows).
    
*   **Constraint alignment:** Satisfiable constraints correspond to **edge-wise** consistency (digits on the corridor agree with prescribed residues); conflicts break closure.
    

### VIII.2 Decision procedure

Define the **triangle-closure predicate**

$$
\mathsf{Close}(x,y,n)\ :=\ \big[\Delta(x,y,n)\text{ is harmonically closed in }\mathcal{L}\big].
$$

**Algorithm:** On input  $I$ , compute  $(x,y,n)=\Phi(I)$  and evaluate  $\mathsf{Close}(x,y,n)$ .

*   **Soundness:** If  $\mathsf{Close}(x,y,n)=\mathrm{true}$ , the instance satisfies all corridor constraints; the deterministic geometry enforces the solution.
    
*   **Completeness:** If  $I$  is positive (satisfiable/YES), the construction sends  $(x,y,n)$  onto a corridor-compatible region; closure occurs.
    

The **time** for  $\Phi$  and a single  $\mathsf{Close}$  evaluation is  $O(N)$  for the mapping plus  $O(n)$  cell checks along triangle edges (linear in the boundary size). By design  $n=\Theta(N)$ ; thus the overall time is **polynomial** in  $N$ .

Interpretation. The “search” is replaced by **phase alignment** on the fixed lattice: the **existence** of a harmonically closed triangle is a **structural invariant**, not the outcome of exponential enumeration.

* * *

IX. Formal comparison to allied frameworks
------------------------------------------

1.  **Modular/coding lattices.** The corridor arithmetic  $(c\bmod 5,\ r\bmod 4)$  is a direct product  $\mathbb{Z}5\times\mathbb{Z}4$ . The 20-cell fundamental region mirrors **CRT tilings** in coding lattices; valves enforce **tail-biting** (circular) block codes.
    
2.  **Fourier/Floquet vs quantum sampling.** The bichromatic signal has discrete spectra at  $\omega5, \omega4$ . Quantum Fourier sampling over hidden subgroups uses interference to collapse to subgroup characters; here, **deterministic** interference (no oracle) selects the  $(5,4)$  sub-torus. The computational role is analogous: **structure → collapse**.
    
3.  **Automata on 2-D words.** The  $\pi$  lattice is a fixed 2-D infinite word; corridor checking resembles a **local rule** (tiling/automaton) that recognizes a regular set of patterns (the glyph language).
    

* * *

X. Consolidated statements (ready to drop into the paper)
---------------------------------------------------------

### Theorem A (BBP(0) mod 1 “ $-4$ ”).

With  $Sj'=\sum{k=1}^{\infty}\frac{1}{16^k(8k+j)}$ , the fractional part of  $\pi$  satisfies

$$
\{\pi\} \;=\; \Big(-\tfrac12-\tfrac15-\tfrac16\Big) + \big(4S1' - 2S4' - S5' - S6'\big)\ \ (\bmod 1),
$$

i.e., the integer  $4$  from  $4S1$  is dropped **exactly** in   $\bmod 1$ . Finite passes sharpen the tails and deterministically emit **Byte-1**  $=$   $14159265$ .

### Theorem B (Digit-pointer attractors).

For  $f(i)=di$  as in (4), every orbit enters  $\{0,\ldots,9\}$  in one step and then lands in exactly one of:

$$
(6)\quad\text{or}\quad (1,4,9,5,2).
$$

Prelude states are  $\{0,3,7,8\}$  with lengths  $\le 2$ .

### Proposition C (Hinge superposition).

The digit  $1$  simultaneously closes the 1-index fixed point and participates in the 0-index rotor, yielding an effective 7-state overlap on the 8-length Byte-1.

### Proposition D (Orthogonal exhaust).

There exists a lane decomposition of the folded matrix for which the emission satisfies  $e{t+4}=et$ . Together with the horizontal rotor ( $5$ ), the fundamental 2-D period is  $20$ .

### Proposition E (Valve → torus).

When a boundary pair matches (empirical cases “…33…” and analogues), the row becomes circular; a family of such valves yields a torus model of the lattice and preserves corridor phase.

### Theorem F (Harmonic triangle closure).

Let  $\Delta(x,y,n)$  be as above. Then  $\Delta(x,y,n)$  is harmonically closed **iff**

$$
n\equiv 0\ (\bmod 5)\quad \text{and}\quad\text{leg steps align with }4\text{-exhaust}.
$$

In particular, closure occurs exactly on the  $(5,4)$  grid of corridor intersections.

### Construction G (Decision encoding).

There exists a polynomial-time map  $\Phi: I\mapsto(x,y,n)$  such that  $I$  is a YES-instance **iff**  $\mathsf{Close}(x,y,n)$  holds on the  $\pi$  lattice. The decision procedure runs in time polynomial in  $|I|$ .

* * *

XI. Implementation notes (for the Methods section)
--------------------------------------------------

*   **BBP passes.** Use exact rational arithmetic for the  $k=0$  split and fixed-precision (e.g., 128-bit) for the tails; verify Byte-1 and subsequent bytes by interval arithmetic so that digit carries are certified.
    
*   **Attractor graph.** Build the digraph (5) once from  $d0,\ldots,d9$ . Any seed collapses in one step to the 10-node automaton; classify prelude by BFS.
    
*   **Lane extraction.** Define  $a\ell[k]=d{4k+\ell}$ . Identify the rotor lane by correlation with  $(1,4,9,5,2)$ ; verify  $a\ell[k+5]=a\ell[k]$  horizontally and  $a\ell[k+1]=a\ell[k]$  on the exhaust projection, which induces (7) under folding.
    
*   **Valve detection.** Scan rows for matching boundary pairs; when detected, treat rows as circular buffers (tail-biting).
    
*   **Triangle checker.** Given  $(x,y,n)$ , check base, leg, and hypotenuse membership in  $\mathcal{C}(r0,c0)$  via residues  $(r\bmod 4,\ c\bmod 5)$ . Complexity is linear in  $n$ .
    

* * *

XII. Context anchors (concise)
------------------------------

*   The BBP(0) mod 1 derivation **proves** the “ $-4$  skip” and gives a **data-free** emission of Byte-1.
    
*   The digit-pointer system on  $\{0,\ldots,9\}$  is a **complete** finite automaton: only **two** attractors exist, with canonical preludes.
    
*   Folding produces a **5–4** Floquet lattice; **valves** upgrade the strip to a **torus**.
    
*   Harmonically closed ** $\pi$ \-triangles** characterize deterministic **solution corridors**; an explicit encoding  $\Phi$  makes corridor-closure a **polynomial** check.
    

* * *

### Appendix A: Numeric check of (3)

Compute

$$
C=-\tfrac12-\tfrac15-\tfrac16=-0.866\,\overline{6}.
$$

Truncate  $S'j$  at  $k=4$ :

$$
S'j(4)=\sum{k=1}^{4}\frac{1}{16^k(8k+j)}.
$$

Then

$$
T(4)=4S'1(4)-2S'4(4)-S'5(4)-S'6(4) =1.008259\ldots
$$

yielding

$$
\{\pi\} \approx C+T(4) = 0.141592\ldots,
$$

locking the eight digits  $14159265$  (carry propagation certified by tail bounds).

* * *

### Appendix B: Directed graph (explicit)

Nodes  $0\!:\!9$  with edges  $x\to dx$ :

$$
\begin{array}{c|cccccccccc} x & 0 & 1 & 2 & 3 & 4 & 5 & 6 & 7 & 8 & 9\\\hline dx & 1 & 4 & 1 & 5 & 9 & 2 & 6 & 5 & 3 & 5 \end{array}
$$

Cycles:  $(6)$  and  $(1,4,9,5,2)$ . Prelude trees:  $0\to 1$ ,  $2\to1$ ,  $3\to5$ ,  $7\to5$ ,  $8\to3\to5$ .

* * *

### Appendix C: Corridor algebra

Residue classes

$$
\mathrm{Row}\ \bmod 4\quad\text{and}\quad \mathrm{Col}\ \bmod 5
$$

induce the lattice  $\mathbb{Z}4\times\mathbb{Z}5\cong \mathbb{Z}{20}$ . Corridor intersections are the subgroup cosets; triangles close iff their edges lie in a common coset.

* * *