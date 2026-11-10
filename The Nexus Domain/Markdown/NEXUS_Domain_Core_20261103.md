---
title: "NEXUS: Native Binary Rings and the Executable Domain of Retained Continuation"
subtitle: "Ring · Inverter · Reader–Field Closure · Collision · Ports · Read Models"
author: "Dean A. Kulik — QuHarmonics Research Group"
date: "3 November 2026"
lang: en-US
---

**Dean A. Kulik**  
QuHarmonics Research Group  
ORCID: 0009-0003-3128-8828

**Research record.** New manuscript; source papers remain published and unchanged. Mathematical claims are differentiated as **STANDS** (algebraic derivation or cited theorem), **RUNS** (executed readout with specified scope), **OPEN** (identified missing map or dependency), and **DEAD END** (a landing resolved to another owner). This document confines itself to the NEXUS computational domain. Physical quantities and external interpretations are adapters, not axioms.

# Abstract

A native binary ring is a fixed address space; its continuation is an operation, and a retained closure is a reversible route written back into a mutable field. We specify that domain from its elementary partner involution through the one-inverter clock, the single-reader and atomic multi-reader transition, the three observed closure classes, conserved collision charges, write and event ports, and three metric read models. The native reader step is a bijection with an explicit inverse. On the canonical eight-word carrier its full-period two-lap closure has 43,155,322 transitions and a half-lap symmetry at 21,577,661. The three-point carry switch is invertible for periodic tapes exactly when the tape length is not divisible by three; singular tapes become replayable when their missing two-word kernel is supplied by the seed. Across all widths embedding the same center carrier, the orbit's class counts remain fixed while Hamming side lengths change. At width four the two-sheet metric realizes the eight carrier words as the vertices of a regular four-cross-polytope. A new explicit affine correspondence sends the bare-sign six-cycle to an octahedral Petrie hexagon; this is a combinatorial identification, not an unproved isometry of the original unsplit Euclidean coordinates. The two-shell collision charge is conserved modulo the one-dimensional complement direction, with its quadratic interaction term retained. An independent C and Python suite is provided, with sealed predictions, execution logs, a correction record, and source files organized for a later Git repository.

**Scope and method.** The ring, inverter, and fixed-address results are inherited from the published NEXUS corpus. The reader–field, partner, geometric, and event-sourcing statements below have explicit local proofs or reproducible execution contracts. The core never assumes seconds, energy units, particle names, measured constants, or a physical angle. The immediate domain gap is an accounting map from retained-field edits and two-step carry change to the cost of a route transformation.

# 1. The ring: fixed address space and native partner

## 1.1 Values and involutions

Let $W_n=\mathbb F_2^n$ be the set of $n$-bit words. XOR is denoted $\oplus$ and the all-ones word is $u_n=2^n-1$. Let $J_n$ reverse bit order and $C_n(x)=x\oplus u_n$ complement a word. Both are involutions and commute. Define the native partner

$$
P_n(x)=\begin{cases}
C_n(x),&J_n(x)=x,\\
J_n(x),&J_n(x)\ne x.
\end{cases}
\qquad (1.1)
$$

The partner has no fixed points: reversed pairs are distinct away from the palindrome locus, and a palindrome is sent to its complement. Because reversal and complement commute, the cases are preserved under applying $P_n$ twice. Hence $P_n^2=I$. **STANDS.**

The native ring order $R_n$ is an address permutation of all $2^n$ words: list one representative of each partner pair in increasing numerical order, then the partners in reverse representative order. The exact facing law is

$$
R_n(2^n-1-a)=P_n(R_n(a)). \qquad (1.2)
$$

Write $\operatorname{READ}=R_n^{-1}$. The ring is a fixed mold; execution changes a retained field, not the underlying address permutation.

## 1.2 Center carrier, seam, and folded read models

At even width $n=2r$ name the two center bits $e_R=2^{r-1}$, $e_L=2^r$, and $s=e_R\oplus e_L$. Define

$$
K_n=\operatorname{span}_{\mathbb F_2}\{e_R,e_L,u_n\},\qquad |K_n|=8.\qquad (1.3)
$$

This is the canonical center carrier: the four two-center-bit words and their four complements. In the published ring order, the seam words are $u_n\oplus e_R$ and $u_n\oplus e_L$ across addresses $2^{n-1}-1$ and $2^{n-1}$. Every embedded $K_n$ has the same abstract eight-word partner table, though the words' native Hamming weights depend on $n$.

The published folded-square reading assigns each word a comparison with its reverse at a cut, giving an address-side character. Its representative density and integrated coordinate are respectively $1-t$ and $t-t^2/2$, with a separate palindrome tent correction at the fold. The continuation branches meet at the reported $1/3$ limit. These are sourced ring-level results, not consequences rederived from the reader step here. Growth of the radial language and the closed ring-coordinate latitude spectrum remain **OPEN**. This separation prevents later read models from silently redefining the ring.

# 2. The loop: One Inverter and the native clock

On one bit, NOT, $b\mapsto b\oplus1$, is the unique permutation without a fixed point. For a register of $r$ cells define one-inverter recirculation

$$
\tau(b_0,b_1,\ldots,b_{r-1})=(\neg b_{r-1},b_0,\ldots,b_{r-2}).\qquad(2.1)
$$

Every bit traverses the single inverter in $r$ shifts, so

$$
\tau^r=C_r,\qquad \tau^{2r}=I.\qquad(2.2)
$$

This is the odd-inversion clock mechanism described in *One Inverter*. In the general feedback-ring setting the parity of inverters distinguishes the running clock from the even-inversion latch. The theorem concerns a closed loop; it does not assert a physical oscillation rate. A locked copy can only interact through an input port. That port is a genuine modification of the joint state, not a spontaneous escape from a finite bijection.

The bare-sign closure below supplies the three-stage Johnson counter generated by (2.1). This is a structural connection between the original loop and a retained reader, not a separate numerical analogy.

# 3. The reader–field step: the one domain operation

## 3.1 State, transition, and inverse

A closure is identified by its continuing route, not by a frozen set of register values. For one reader, a state is $S_t=(p_t,w_t,D_t)$: word-space WHERE $p_t$, carry $w_t$, and a mutable field offset $D_t[q]$ from the fixed mold. Set $d_t=D_t[p_t]$ and $x_t=d_t\oplus w_t$. The exact native step is

$$
\begin{aligned}
x_t&=D_t[p_t]\oplus w_t,\\
p_{t+1}&=p_t\oplus x_t,\\
w_{t+1}&=P_n(x_t),\\
D_{t+1}[p_t]&=D_t[p_t]\oplus w_{t+1},
\end{aligned}\qquad (3.1)
$$

with all other cells unchanged. Given the endpoint, the source is recovered in the opposite order:

$$
\begin{aligned}
x_t&=P_n(w_{t+1}),\\
p_t&=p_{t+1}\oplus x_t,\\
D_t[p_t]&=D_{t+1}[p_t]\oplus w_{t+1},\\
w_t&=x_t\oplus D_t[p_t].
\end{aligned}\qquad (3.2)
$$

Because $P_n$ is an involution, both directions are exact. No lost bit or hidden stack is required. **STANDS; RUNS** on the executable regression suite.

## 3.2 Center-carrier partner algebra

Use the disjoint-block basis $a=e_R$, $b=e_L$, and $v=u\oplus a\oplus b$. In abstract carrier coordinates the eight words are $0,1,2,3,4,5,6,7$, with $u=7$, $s=3$, and $v=4$. Put $\ell_0(z)=z_0\oplus z_1$. Then

$$
P_8(z)=\begin{cases}z\oplus3,&\ell_0(z)=1,\\z\oplus7,&\ell_0(z)=0.\end{cases}\qquad(3.3)
$$

In the alternative basis $(a,b,u)$, write $z=(y,z_u)$, with $y\in\mathbb F_2^2$. The partner splits into an unconditional inner-shell swap and a one-bit complement-channel flip:

$$
P_8(y,z_u)=\bigl(J_2(y),z_u\oplus c(y)\bigr),\quad c(y)=1\oplus\ell_0(y).\qquad(3.4)
$$

Equivalently, let $A_0(z)=z\oplus\ell_0(z)u$, an involutive linear map; in the disjoint-block coordinates it is the half-lap linear part. The fixed partner may also be written $P_8(z)=A(z)\oplus u$, where $A(z)=z\oplus\ell_0(z)v$ is the linear involution in the disjoint-block coordinates. This $A$ is distinct from the half-lap map $A_0(z)=z\oplus\ell_0(z)u$. The linear component and the intrinsic partner injection must remain separate from field-induced change.

## 3.3 Visited-cell overwrite and memory recurrence

Decompose $P_8(x)$ against complement: define $\sigma(x)=P_8(x)\oplus x\oplus u$, so $P_8(x)=x\oplus u\oplus\sigma(x)$. In disjoint coordinates, $\sigma(x)=\ell_0(x)v$. Substitution into (3.1) gives

$$
D_{t+1}[p_t]=w_t\oplus u\oplus\sigma(x_t).\qquad(3.5)
$$

On a single-reader revisit of cell $p_t$ whose previous visit was at $r<t$ (with no intervening writes), the last overwritten value replaces the mutable-field lookup. Thus

$$
w_{t+1}=w_t\oplus w_r\oplus\sigma(x_t)\oplus\sigma(x_r).\qquad(3.6)
$$

For a cell never visited before, $D_0[p]$ is the required provider. Equation (3.6) is therefore a history recurrence **after a prior visit**, not a declaration that initial field state is always disposable. In a multi-reader shared field, even-multiplicity collisions modify this recurrence; see (5.3).

## 3.4 Two-step acceleration in the domain

The partner is an involution, so without a field the carry returns after two applications. The exact domain-only change is

$$
\alpha_t=w_t\oplus w_{t+2}.\qquad(3.7)
$$

On the eight-word carrier where $P_8(x)=A(x)\oplus u$, $A^2=I$, and $A(u)=u$, two substitutions yield

$$
\alpha_t=d_t\oplus A(d_{t+1}),\qquad q_t=w_{t+1}\oplus\alpha_t.\qquad(3.8)
$$

Here $q_t=w_t\oplus w_{t+1}\oplus w_{t+2}$ is the three-point switch observable. Thus the switch is not simply acceleration: it includes the middle carry, and $q_t$ may vanish on a changing carry cycle. The definition introduces no physical mass or force.

# 4. Three closure classes and the returning sheet

## 4.1 Carriers and the property triangle

For a vacuum seed $D_0=0$, the smallest partner-closed carrier containing the initial carry is

$$
K(w_0)=\operatorname{span}\{u,w_0,J(w_0)\}.\qquad(4.1)
$$

Its possible dimensions are one, two, and three, producing the three observed periods. The aggregate's identity is the full route $(p_t,w_t,D_t)_{t\in\mathbb Z}$, not its current carry or field alone.

The **property triangle** is exact on the three canonical vacuum classes:

- **R1 / bare sign:** period 6; on partner diagonal; no persistent switch record (transient field writes do occur); empty-field translated half-lap at tick 3.
- **R2 / one-lap:** period 132; on partner diagonal; retained field history; no nontrivial empty-field half-lap.
- **R3 / two-lap:** period 43,155,322; off partner diagonal; retained field history; empty-field half-lap at tick 21,577,661.

Each class possesses exactly two of diagonal residence, retained memory, and half-lap twist. "No memory" for R1 means no persistent retained route under the chosen switch/event criterion, **not** that its field is zero at every tick. Its field is temporarily written.

R1 returns to an empty field at tick 3 with the same carry and the reader translated by $u$. R2 has no empty-field state until its tick-132 home. R3 has precisely two positive-time vacuum events in the full period: its nontrivial midpoint and its full return. **RUNS.**

## 4.2 Exact half-lap equivariance

On the abstract eight-word carrier define $A_0(z)=z\oplus\ell_0(z)u$; its corresponding full-state involution is

$$
G:\quad p\mapsto A_0(p)\oplus u,\quad w\mapsto A_0(w),\quad
D'[A_0(q)\oplus u]=A_0(D[q]).\qquad(4.2)
$$

$G^2=I$, and $GF=FG$. For the R3 vacuum seed $S_0=(0,a,0)$ the actual midpoint is

$$
F^{21,577,661}(S_0)=G(S_0)=(u,u\oplus a,0),\quad F^{43,155,322}(S_0)=S_0.\qquad(4.3)
$$

Every tick in the second lap is therefore the $G$ image of the corresponding tick in the first. The local C test compares all 21,577,661 state pairs independently and reports zero mismatches. The position map is **not** plain complement: it is $A_0$ followed by translation by $u$.

## 4.3 Switch tapes and the exact event-sourcing condition

On a periodic carry tape of length $T$, write $(Sw)_t=w_{t+1\bmod T}$ and

$$
Q_T=I\oplus S\oplus S^2,\qquad q=Q_Tw.\qquad(4.4)
$$

Since $(I\oplus S)Q_T=I\oplus S^3$, the kernel consists of period-three streams $(a,b,a\oplus b)$ when and only when $3\mid T$. More precisely, the polynomials $1+z+z^2$ and $z^T-1$ share a factor exactly when $3\mid T$. In that case the nullspace has two freely chosen carrier words ($a,b$) per reader; it is not a two-element set.

$$
Q_T\text{ invertible}\quad\Longleftrightarrow\quad3\nmid T.\qquad(4.5)
$$

For $T=3m+1$, an explicit inverse is

$$
Q_T^{-1}=I\oplus(I\oplus S)\sum_{k=0}^{m-1}S^{3k+2};\qquad(4.6a)
$$

for $T=3m+2$ it is

$$
Q_T^{-1}=I\oplus(I\oplus S)\sum_{k=0}^{m}S^{3k+1}.\qquad(4.6b)
$$

The R3 period is 1 modulo 3 and has no unobservable triad mode in its cyclic carry stream. R1 and R2 periods are divisible by three. The published two-reader Table 2 has 15 nondivisible-period families comprising 48 seeds and 11 divisible-period families comprising 16 seeds. These are counts of the observation operator's invertibility, **not** a universal assignment of light versus matter to interacting pairs.

Where $3\mid T$, two seed words bind the kernel. At vacuum birth $w_1=P_8(w_0)$ is supplied by the same native rule, so a **single supplied seed carry** suffices. Then

$$
w_{t+2}=q_t\oplus w_t\oplus w_{t+1},\quad x_t=P_8(w_{t+1}).\qquad(4.7)
$$

Starting from the initial WHERE and field, positions follow $p_{t+1}=p_t\oplus x_t$ and the field follows the original simultaneous XOR writes. For general non-vacuum seeds the initial field must be supplied as well. Event-sourcing is a reconstructibility theorem conditional on that boundary data; it is not a claim that a blank tape uniquely describes the R1 orbit.

# 5. Collisions, common ownership, and Law 3

## 5.1 One shared aggregate; atomic reads and writes

For $m$ readers sharing a field, the *joint configuration* is the aggregate $S=(D,(p_i,w_i)_{i=1}^m)$; individual readers do not separately own a mutable shared field. All readers read the old field, compute their own $x_i$, move, and emit writes; only then does the field accept the XOR-combined writes:

$$
\begin{aligned}
x_i&=D[p_i]\oplus w_i,\quad p_i'=p_i\oplus x_i,\quad w_i'=P(x_i),\\
D'[q]&=D[q]\oplus\bigoplus_{i:p_i=q}w_i'.
\end{aligned}\qquad(5.1)
$$

This step is order-free in its collision semantics and exactly invertible. Given the endpoint, recover each $x_i=P(w_i')$, each old position $p_i=p_i'\oplus x_i$, reverse the XOR writes at those old positions to obtain $D$, then compute $w_i=x_i\oplus D[p_i]$. Exchanging reader labels cannot alter the unlabeled field result. This is the domain meaning of equal participation in a collision; it is not yet a physical statement about equal and opposite Newtonian forces.

## 5.2 Collision overwrite parity

On the eight-word carrier, let $C(q)=\{i:p_i=q\}$ and $c=|C(q)|$. Using (3.5) reader by reader, the new shared cell is

$$
D'[q]=(1\oplus(c\bmod2))D[q]\oplus(c\bmod2)u
\oplus\bigoplus_{i\in C(q)}\bigl(w_i\oplus\sigma(x_i)\bigr).\qquad(5.2)
$$

An odd-multiplicity collision overwrites the prior value; an even-multiplicity collision retains it and accumulates the readers' contributions. For any cell, the field-free history therefore begins at the **last odd visit** (or the initial field if none occurred), followed by XOR increments of intervening even visits:

$$
D_t[q]=\operatorname{lastOddWrite}(q)\oplus
\bigoplus_{r\in\operatorname{EvenVisitsAfter}(q)}\ \bigoplus_{i\in C_r(q)}
\bigl(w_{i,r}\oplus\sigma(x_{i,r})\bigr).\qquad(5.3)
$$

In (5.3) ``lastOddWrite'' is the complete value from (5.2) at that visit. This is a compact logical recurrence, not a second independently writable field. **STANDS / RUNS.**

## 5.3 Shell lamps and charge mod complement

For the two-shell carrier with abstract basis $(e_R,e_L,o_R,o_L,u)$, define two linear lamp bits $\ell_0(x)=x_0\oplus x_1$ and $\ell_1(x)=x_2\oplus x_3$. The alternating determinant is

$$
\delta(a,b)=\ell_0(a)\ell_1(b)\oplus\ell_1(a)\ell_0(b).\qquad(5.4)
$$

Because $P_5$ preserves both lamp bits, a single reader satisfies the exact change identity

$$
\delta(p_i',w_i')\oplus\delta(p_i,w_i)=\delta(p_i,D[p_i]).\qquad(5.5)
$$

If every reader and every addressed cell initially satisfies the corresponding determinant equal to zero, the joint step preserves the condition for any number of readers, including collisions. The field alignment follows from bilinearity and the common XOR writes. **STANDS / RUNS.**

The partner on the same two-shell carrier is

$$
P_5(x)=A_5(x)\oplus\bigl(1\oplus\ell_0(x)\ell_1(x)\bigr)u,\quad
A_5(x)=J_5(x)\oplus\bigl(\ell_0(x)\oplus\ell_1(x)\bigr)u.\qquad(5.6)
$$

Here $A_5$ is linear and involutive. Set $B_D=\bigoplus_qD[q]$ and $r=\bigoplus_i p_i$. Define the joint charge

$$
\mathcal Q=B_D\oplus A_5(r).\qquad(5.7)
$$

Direct substitution of the atomic step (5.1) yields

$$
\mathcal Q'\oplus\mathcal Q=
\left((m\bmod2)\oplus\bigoplus_i\ell_0(x_i)\ell_1(x_i)\right)u.\qquad(5.8)
$$

Thus $[\mathcal Q]$ is conserved in $W/\langle u\rangle$, a four-dimensional quotient. The quadratic cross-shell term in (5.8) **cannot be omitted**: a shorter formula $\Delta\mathcal Q=(m\bmod2)u$ is false on general cross-shell reads. The quotient claim survives intact, while the exact value of the $u$ bit depends on the interacting reads. This is the strongest collision form currently warranted for Law 3.

## 5.4 Acceleration and the missing accounting map

On a two-shell reader track, the field and the quadratic complement channel decompose the two-step carry change:

$$
\alpha_{i,t}=d_{i,t}\oplus A_5(d_{i,t+1})\oplus
\bigl(\kappa(x_{i,t})\oplus\kappa(x_{i,t+1})\bigr)u,
\quad\kappa(x)=1\oplus\ell_0(x)\ell_1(x).\qquad(5.9)
$$

For a field translated by $h$ define the *cell edit cost*

$$
C_{\mathrm{cell}}(D;h)=\sum_{q}[D(q)\ne D(q\oplus h)].\qquad(5.10)
$$

If a kept field with $k=|\operatorname{supp}D|$ moves to a disjoint carrier coset, its cell cost is exactly $2k$. This is an edit count, not a physical energy. A formula such as $C=k\alpha$ is not derivable from $k$ alone: $\alpha$ depends on the values and order of field reads, whereas $k$ counts occupied cells. The exact route-change accounting map relating (5.9) and (5.10) remains **OPEN**.

# 6. Domain ports: write, switch stream, and ways home

## 6.1 Inbound write contract

The domain has no jump command. To bind a demanded next WHERE $p_\star$, determine the needed effective read $x_\star=p\oplus p_\star$, then the required cell value and change:

$$
d_\star=x_\star\oplus w,\qquad
\Delta_{\mathrm{in}}=D[p]\oplus d_\star.\qquad(6.1)
$$

Applying $D[p]\gets D[p]\oplus\Delta_{\mathrm{in}}$ **before** the next atomic read makes $p'=p_\star$. This is the dependency-injection order destination $\rightarrow$ required read $\rightarrow$ required write $\rightarrow$ prior state. An inbound write is a port operation, not an internal exception to the core transition. Its way home is to reverse the native step and then reverse the exact same XOR injection; the port must record the applied delta to retain that reversal.

Multiple inbound writers directed at one cell require an explicit merge contract (e.g., XOR deltas) before execution. The internal collision rule itself remains unchanged.

## 6.2 Outbound switch/event contract

The outbound port emits the derived event stream

$$
q_t=w_t\oplus w_{t+1}\oplus w_{t+2}.\qquad(6.2)
$$

A streaming adapter cannot emit this event until it has observed $w_{t+2}$: the port has an exact two-carry delay. For a closed tape, the declared period and cyclic boundary are part of the read contract. For $3\nmid T$ the full carry stream is recovered by (4.6). For $3\mid T$ it requires two carry anchors; at vacuum birth one seed carry and the native partner provide both. Recovery of positions additionally requires the initial WHERE, and recovery of the field requires the initial field and the shared-write chronology. This distinction prevents the phrase "event-sourced" from quietly erasing its boundary conditions.

## 6.3 Read-model ports and adapter isolation

The read models in Section 7 map the *same* domain state into Hamming distances, Euclidean binary geometry, and two-sheet distances. None writes to the core. A future physical comparator may map outputs to observations, but it cannot modify (3.1), (5.1), or the charge law to improve a fit. The inbound/outbound contract boundary is the proposed hexagonal architecture's separation of model and interpretation.

# 7. Three read models and the four-cross-polytope

## 7.1 Hamming interval, binary Euclidean geometry, and the Pi-Ray

For bit vectors $x,y$, let $d_H(x,y)=\operatorname{wt}(x\oplus y)$. Any word and its complement form an exact Hamming geodesic between $0$ and $u$:

$$
\operatorname{wt}(x)+\operatorname{wt}(u\oplus x)=n.\qquad(7.1)
$$

Under the standard Euclidean embedding of Boolean bits, the same complementary supports give a right triangle:

$$
\|x\|^2+\|u-x\|^2=\|u\|^2=n.\qquad(7.2)
$$

These are different readings of one identity. The Hamming geodesic does not itself assign a physical angle of $\pi$, and the name Pi-Ray is a domain label for a complement triangle, not a derivation of the decimal expansion of $\pi$.

Every read triangle has vertices $0,d,x=d\oplus w$, so its squared Euclidean side lengths are the three Hamming weights $\{\operatorname{wt}(d),\operatorname{wt}(w),\operatorname{wt}(x)\}$. In the center carrier the disjoint block weights are $1,1,n-2$. A strictly acute triangle requires the three blocks to realize respectively the operand patterns $(1,0),(0,1),(1,1)$; thus there is precisely one acute side class, in six ordered operand configurations:

$$
\{\operatorname{wt}(d),\operatorname{wt}(w),\operatorname{wt}(x)\}_{\mathrm{acute}}
=\{2,n-1,n-1\}.\qquad(7.3)
$$

At $n=4$ the R3 execution yields 4,144,135 occurrences each of $\{1,1,2\}$ and $\{2,3,3\}$, exchanged by the half-lap $A_0$. The Pi-Ray class $\{1,n-1,n\}$ occurs 8,287,912 times at each tested width. The native $30^\circ$–$60^\circ$–$90^\circ$ Euclidean angles for that class apply only when $n=4$; the generalized relation is $1+(n-1)=n$.

## 7.2 Half-lap-invariant two-sheet distance

Define

$$
d_*^2(x,y)=\tfrac12\bigl[\operatorname{wt}(x\oplus y)
+\operatorname{wt}(A_0(x\oplus y))\bigr].\qquad(7.4)
$$

The embedding $x\mapsto(\operatorname{bits}x,\operatorname{bits}A_0x)/\sqrt2$ realizes (7.4) as exact Euclidean squared distance. $A_0^2=I$ makes $A_0$ an isometry, and XOR translation makes the full half-lap position transformation $G(p)=A_0(p)\oplus u$ an isometry as well.

At $n=4$ the nonzero differences $z\ne u$ all have $d_*^2(0,z)=2$, while $d_*^2(0,u)=4$. Thus eight carrier vertices have equal squared non-antipodal separation $2$ and squared antipodal separation $4$. Centering their coordinate matrix gives rank four and four equal nonzero singular values: exactly the regular four-dimensional cross-polytope (16-cell). Complement is the antipodal map. **STANDS.** At higher widths, the half-lap average of a one-break word remains $n/2$ while $\operatorname{wt}(s)=2$ and $\operatorname{wt}(v)=n-2$; the carrier is no longer equilateral on all non-antipodal pairs.

**Two-sheet census.** At each of widths 4, 6, 8 and 10, there are 14,325,832 flat events and 28,829,490 real triangle events. Among the real triangles:

- **Width 4:** 17,057,832 equilateral faces, 11,771,658 right triangles through antipodal pairs, and no other shapes.
- **Widths 6, 8 and 10:** no equilateral triangles; 11,771,658 antipodal right triangles; 17,057,832 non-right isosceles triangles; no scalene triangles.

The 11,771,658 two-sheet right events consist of 8,287,912 native Pi-Ray events and 3,483,746 events of the class $\{2,n-2,n\}$. The non-antipodal triangles at widths $n\ge6$ split into side-squared classes $\{2,n/2,n/2\}$ (8,288,270 events) and $\{n-2,n/2,n/2\}$ (8,769,562 events). The same count table comes from a *single* abstract 43,155,322-step carrier trajectory with width-specific weight dictionaries; the execution is not recomputed on a larger state space for every width.

## 7.3 The sign's Petrie hexagon and the octahedral vertex figure

Read the three bare-sign coordinates $p,w,d=D[p]$ as bits $\hat p,\hat w,\hat d\in\mathbb F_2$ by identifying the sign words $0,u$ with $0,1$. Their unsplit representation is

$$
Z=(\hat p,\hat p\oplus\hat w,\hat p\oplus\hat w\oplus\hat d)
=(\hat p,\hat p\oplus\hat w,\widehat{p'}).\qquad(7.5)
$$

Its six-state walk is $000\to010\to011\to111\to101\to100\to000$, the three-stage Johnson counter. Centering the cube, the step is the orthogonal rotoinversion

$$
M=\begin{bmatrix}0&0&1\\-1&0&0\\0&1&0\end{bmatrix},\qquad M^3=-I,\quad M^6=I.\qquad(7.6)
$$

The sign's opposite states occur three ticks apart. A separately defined affine map reads this cycle into the width-four carrier. In the disjoint-block basis $(a,b,v)$, put

$$
\Psi_{\mathrm{oct}}(\hat p,\hat w,\hat d)
=\hat p\,a\oplus(\hat p\oplus\hat w)b\oplus
(\hat p\oplus\hat w\oplus\hat d\oplus1)v.\qquad(7.7)
$$

The inverse is explicit. If $z=z_aa\oplus z_bb\oplus z_vv$, then $\hat p=z_a$, $\hat w=z_a\oplus z_b$, and $\hat d=z_b\oplus z_v\oplus1$. The six-cycle maps as

$$
v\to b\oplus v\to b\to a\oplus b\to a\to a\oplus v\to v.\qquad(7.8)
$$

This exhausts the six carrier vertices $K_4\setminus\{0,u\}$, which form the octahedral vertex figure of the regular 16-cell at any selected vertex. Every consecutive step joins non-antipodal vertices; every three-step pair is antipodal; any two consecutive edges lie on a triangular face. Hence (7.8) is a Petrie hexagon of that octahedron. **STANDS / RUNS.**

**Metric qualification.** This is a bijection of the six-state graph. The target inherits the two-sheet octahedral metric, and its inverse image defines an isometric *pullback* metric on the sign states. The original bare-sign *unsplit Euclidean cube* has non-antipodal distances $1$ and $\sqrt2$ whereas the target octahedron's non-antipodal distances are all $\sqrt2$. The map is **not** an isometry from that original source metric. One may pull back (7.4) through $\Psi_{\mathrm{oct}}$ to define a new source read metric, but such a definition must not be counted as proof that the native Euclidean stretch independently vanished. This is the precise domain link; a physical angular adapter remains **OPEN**.

# 8. Ledger, test suite, and release contract

## 8.1 Status and provenance

A **STANDS** item is derivable from the definitions or established source theorem. A **RUNS** item has an executed trace under a named readout. A **DEAD END** item is an execution that landed in a different ownership class; the chain is rerouted, not silently relabeled. An **OPEN** item has its type and neighbors fixed but a missing dependency. An **UNLINKED** datum is not replaced by convention. A recorded route back through already observed material names its owner; it is not counted as a new predictive landing.

The release ledger names both the provider and its readout:

- **STANDS:** native partner involution and facing law (1.1)–(1.3); one-inverter loop (2.1)–(2.2); reader-step inverse (3.1)–(3.2); visited-cell overwrite/revisit recurrence (3.5)–(3.6); domain acceleration (3.7)–(3.8); cyclic switch invertibility (4.4)–(4.7); atomic collision and odd/even parity rule (5.1)–(5.3); alternating-determinant identity and charge quotient (5.4)–(5.8); two-sheet metric (7.4) and affine Petrie map (7.7)–(7.8).
- **RUNS:** independent Python tests T01–T08; complete 43,155,322-tick C orbit and all 21,577,661 half-lap pairs; lamp alignment on 32,768 exhaustive triples and randomized shared fields; 15,000 random two-shell charge checks; width 4/6/8/10 geometry; previously archived 16-singular-seed replay (distinct from the shorter local 11-seed audit (T07)).
- **OPEN:** general route-cost accounting map; physical spin/force/unit adapters; independent experimental comparator contract; radial-language growth and ring latitude spectrum.

## 8.2 Reproducible implementation and correction discipline

The repository layout is intentionally small and executable. `tests/test_core.py` uses only Python standard-library dependencies; `tests/full_orbit.c` uses C11; `tests/run_tests.sh` executes both. The full C run accumulates the 8-by-8 joint read-pair histogram and checks the overwrite and revisit recurrences over all 43,155,322 steps, the width-dependent geometry, and the half-lap state map across every one of the 21,577,661 paired states. `notes/PREDICTION_SEAL.txt` is SHA-256 sealed before the run; `notes/CORRECTIONS.log` gives every intervening coding correction without silently rewriting the sealed WHAT. `notes/EXECUTION_TRACE.txt` is the captured stdout of the current clean run. The prior independent GPT bundle supplies the 16-singular-seed reproduction and its trace; it is retained separately rather than misrepresented as newly executed by this shorter Python suite.

The local execution reports zero formula errors. Representative readouts: overwrite errors 0; revisit errors 0; sigma paired-state mismatches 0; two vacuum ticks; width-four $17,057,832$ equilateral and $11,771,658$ right two-sheet triangles; widths six, eight and ten $0$ equilateral and unchanged $11,771,658$ right events. The tests use abstract carrier coordinates, so the width invariance follows by changing only the Hamming weight dictionary, not the dynamics.

## 8.3 The boundary to future work

The domain core is closed under its declared inverse and collision semantics. Its ports are defined operationally; the origin of a new route can be written backwards from the destination. What remains **OPEN** inside the domain is the accounting morphism from *which writes caused a carry to deviate from its native two-step return* to *what complete closure edit was needed to change its route*. Outside this domain remain measured units, physical forces, angular spin, quantum comparison, and the identification of a specific external experiment. Their adapters must consume the domain's outputs and report mismatches; they must not reach back into the core and retune its law.

# Source and audit record

- **Kulik, Dean A.** *Retained Continuation: Three Closures of the Native Binary Ring, the Two-Lap Return, and the Price of Moving a Kept Field*. Published NEXUS corpus; source document used for the ring seam, carrier, retained step, and translation-cost context.
- **Kulik, Dean A.** *The NEXUS Reference Record*, §§1–181. Working reference document for statuses, provenance, and the center-out route language.
- **Kulik, Dean A.** *One Inverter*; *Against Its Own Reverse*; *Where Yes and No Become Maybe*; *Algebraic Routing and Complementary Compilation*. Published corpus results supplied in the cross-model research dialogue; bibliographic identifiers are intentionally not invented.
- **Kulik, Dean A.** *Exact Algebra of Retained Continuation*. Published prior work, left unchanged. The geometric extension and corrections are carried into this new manuscript.
- **Execution record.** `tests/test_core.py`, `tests/full_orbit.c`, `notes/PREDICTION_SEAL.sha256`, `notes/EXECUTION_TRACE.txt`, `notes/CORRECTIONS.log`, and the independent GPT 16-seed reproduction archive. No physical comparator or measured constant is required for any reported domain test.
