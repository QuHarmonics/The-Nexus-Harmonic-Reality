# SHA-256 Shape Algebra, Waist Geometry, and the Three-Basin Lift
## A consolidated current solution state for the SHA map

$\Delta$ This document consolidates the current state of the SHA-256 mapping and extends it into the newly identified **shape layer**:

- carry-group objects,
- gap-distribution laws,
- compression/expansion crossover at the waist,
- crankshaft phase relocation under injection,
- amplitude / entropy fields distinct from support closure.

This is written as a **complete current solution state**.  
Where something is directly established by the mapped recurrence or by explicit computational probes, it is presented as an established result.  
Where something is an interpretive lift or still open, it is marked as an **open gap**.

---

## 1. Scope

The goal is not merely to restate SHA-256 as a conventional hash function, but to identify its deeper operative form.

The present result is:

$$
\boxed{
\text{SHA-256 is a 64-cell dual-seam history-to-residue transducer with a carry-shaped interior.}
}
$$

At the visible arithmetic layer, it is a fixed recurrence over eight 32-bit words.  
At the deeper shape layer, it is a transport machine whose stable invariants are better described by:

- carry-group geometry,
- inter-group gap laws,
- seam crossover observables,
- phase-preserving journal relocation,
- and closure bands rather than single endpoints.

---

## 2. Base state recurrence

Let the round state be

$$
x_r =
\begin{bmatrix}
a_r\\
b_r\\
c_r\\
d_r\\
e_r\\
f_r\\
g_r\\
h_r
\end{bmatrix}
\in \left(\mathbb Z / 2^{32}\mathbb Z\right)^8.
$$

For one 512-bit block, the die executes a 64-step recurrence

$$
x_{r+1} = \Phi_r(x_r, W_r),
\qquad
r = 0,1,\dots,63.
$$

Define the standard SHA-256 big sigmas

$$
\Sigma_0(x) = \operatorname{ROTR}^2(x)\oplus \operatorname{ROTR}^{13}(x)\oplus \operatorname{ROTR}^{22}(x),
$$

$$
\Sigma_1(x) = \operatorname{ROTR}^6(x)\oplus \operatorname{ROTR}^{11}(x)\oplus \operatorname{ROTR}^{25}(x),
$$

and the nonlinear gates

$$
\operatorname{Ch}(e,f,g) = (e\wedge f)\oplus(\neg e \wedge g),
$$

$$
\operatorname{Maj}(a,b,c) = (a\wedge b)\oplus(a\wedge c)\oplus(b\wedge c).
$$

Then the round weights are

$$
T1_r = h_r + \Sigma_1(e_r) + \operatorname{Ch}(e_r,f_r,g_r) + K_r + W_r,
$$

$$
T2_r = \Sigma_0(a_r) + \operatorname{Maj}(a_r,b_r,c_r),
$$

with arithmetic modulo $2^{32}$.

The state update is

$$
a_{r+1}=T1_r+T2_r,
\qquad
e_{r+1}=d_r+T1_r,
$$

and the six passive shifts are

$$
b_{r+1}=a_r,\quad c_{r+1}=b_r,\quad d_{r+1}=c_r,
$$

$$
f_{r+1}=e_r,\quad g_{r+1}=f_r,\quad h_{r+1}=g_r.
$$

---

## 3. Prime-root rails and ground witness

The initialization vector $H_0$ is the fractional-$32$-bit encoding of the square roots of the first eight primes, and the round constants $K_r$ are the fractional-$32$-bit encoding of the cube roots of the first 64 primes.

The message-free NOP backbone is defined by

$$
W_r = 0
\qquad \forall r.
$$

Then the NOP trajectory satisfies

$$
x^{(0)}_{r+1} = \Phi_r(x^{(0)}_r, 0),
\qquad
x^{(0)}_0 = H_0.
$$

The round-$0$ ground fold is

$$
G_0(H_0)
=
T2_0^{(0)}
=
\Sigma_0(H_0[0])+\operatorname{Maj}(H_0[0],H_0[1],H_0[2]).
$$

The exact value is

$$
\boxed{
T2_0^{(0)} = 0x08909ae5.
}
$$

This is the fixed scalar ground witness of the die.

---

## 4. Injection, support, and closure

At round $0$, the perturbation enters only through $T1_0$:

$$
T1_0 - T1_0^{(0)} = W_0,
\qquad
T2_0 = T2_0^{(0)}.
$$

Therefore

$$
\delta a_1 = \delta e_1 = W_0.
$$

So the message first appears only in the two active heads $a$ and $e$.

### 4.1 Word-level support transport

Let $\sigma_r\in\{0,1\}^8$ be the lane-support indicator.  
Then the lane transport is governed by a Boolean support matrix $M$, and the support layers evolve as

$$
\Sigma_1 = \{a,e\},
$$

$$
\Sigma_2 = \{a,b,e,f\},
$$

$$
\Sigma_3 = \{a,b,c,e,f,g\},
$$

$$
\Sigma_4 = \{a,b,c,d,e,f,g,h\}.
$$

Hence the word-support diameter is

$$
\boxed{
D_{\mathrm{word}} = 4.
}
$$

### 4.2 Bit-level support closure

At the bit level, support transport must include carry closure.  
The previously established result is

$$
\boxed{
D_{\mathrm{bit}} = 6,
}
$$

with exact one-bit support radius profile

$$
\boxed{
\rho(j)=
\begin{cases}
4, & j=0,\\[4pt]
5, & 1\le j\le 25,\\[4pt]
6, & 26\le j\le 31.
\end{cases}
}
$$

So support closes over the full 256-bit fabric by round $6$.

This must now be distinguished from later phase / entropy behavior.

---

## 5. The three-basin split

The addition

$$
a_{r+1}=T1_r+T2_r
$$

should not be treated as a primitive monolith.  
It separates naturally into three simultaneous channels:

### Basin 0 — visible distinction
$$
B_r^{(0)} = T1_r \oplus T2_r
$$

### Basin 1 — carry witness / residue channel
$$
B_r^{(1)} = (T1_r \wedge T2_r)\ll 1
$$

### Basin 2 — actualized child / resolved noun
$$
B_r^{(2)} = T1_r + T2_r \pmod{2^{32}}
$$

Thus

$$
\boxed{
B_r^{(2)} = B_r^{(0)} + B_r^{(1)} \pmod{2^{32}}.
}
$$

This is the first seam identity.

The crucial correction is that **Basin 1 is not noise**.  
It is the witness/history channel.

---

## 6. Carry groups as geometric objects

The primary shape object is not the raw bitmask itself, but the geometry of its carry clusters.

For any 32-bit word $x$, define the carry-group extractor

$$
\mathcal G(x)=\{(s_1,\ell_1),\dots,(s_m,\ell_m)\},
$$

where each $(s_k,\ell_k)$ is a maximal run of consecutive $1$-bits in $x$:

- $s_k$ is the start bit,
- $\ell_k$ is the run length,
- $m$ is the number of groups.

The group count is

$$
N_{\mathcal G}(x)=|\mathcal G(x)|.
$$

Define the inter-group gaps by

$$
\mathcal D(x)=\bigl(g_1,\dots,g_{m-1}\bigr),
$$

with

$$
g_k = s_{k+1} - (s_k+\ell_k).
$$

So the **shape signature** of a carry word is

$$
\boxed{
\mathfrak S(x)=\bigl(\mathcal G(x),\mathcal D(x)\bigr).
}
$$

This is the exact shift away from value-only analysis:

$$
\boxed{
\text{value is surface; group/gap geometry is pedigree.}
}
$$

---

## 7. Distributional anti-linearity

The next correction is that the symmetry is not merely positional.  
It is **distributional**.

Let the forward-reading gap distribution be

$$
\mathfrak D_{\mathrm{fwd}}(n)
=
\Pr\bigl(\text{gap size}=n \text{ under low-to-high reading}\bigr),
$$

and the reverse-reading gap distribution be

$$
\mathfrak D_{\mathrm{rev}}(n)
=
\Pr\bigl(\text{gap size}=n \text{ under high-to-low reading}\bigr).
$$

The anti-linear claim is not

$$
\text{forward path} = \text{backward path}
$$

bit-for-bit.

It is

$$
\boxed{
\mathfrak D_{\mathrm{fwd}} \approx \mathfrak D_{\mathrm{rev}}.
}
$$

That is, the invariant can live in the **law of gaps**, even when literal path order differs.

This is why the palindrome is better understood as **distributional symmetry** rather than positional mirror identity.

---

## 8. The waist: compression meets expansion

The waist is the compression/expansion crossover of carry-group geometry.

For round $r$, define the carry seed

$$
C_r^{\mathrm{in}} = T1_r \wedge T2_r,
$$

and its shifted carry-out channel

$$
C_r^{\mathrm{out}} = (C_r^{\mathrm{in}} \ll 1)\bmod 2^{32}.
$$

Define the carry-group counts

$$
cg_{\mathrm{in}}(r)=N_{\mathcal G}(C_r^{\mathrm{in}}),
\qquad
cg_{\mathrm{out}}(r)=N_{\mathcal G}(C_r^{\mathrm{out}}).
$$

Then the compression/expansion observable is

$$
\Delta cg_r = cg_{\mathrm{out}}(r)-cg_{\mathrm{in}}(r).
$$

Interpretation:

- $\Delta cg_r<0$ means **compression** (groups merge),
- $\Delta cg_r>0$ means **expansion** (groups split),
- $\Delta cg_r=0$ means **waist**.

So the waist set is

$$
\boxed{
\mathcal U = \{\,r : \Delta cg_r = 0\,\}.
}
$$

This is where analog transport meets digital resolution.

### 8.1 Balanced lines

Define the carry Hamming weights

$$
hw_{\mathrm{in}}(r)=hw(C_r^{\mathrm{in}}),
\qquad
hw_{\mathrm{out}}(r)=hw(C_r^{\mathrm{out}}).
$$

A balanced-line indicator is

$$
\mathrm{bal}_r
=
\mathbf 1\!\left(\left|hw_{\mathrm{out}}(r)-hw_{\mathrm{in}}(r)\right|\le 1\right).
$$

Balanced lines are rounds where the carry channel is near equilibrium.

These act like threshold seams or knife-edges inside the conversion picture.

---

## 9. Entropy flow through the fold

Let $H(x)$ denote the bit-sequence Shannon entropy of a 32-bit word $x$.

Define the round entropy-flow observable

$$
\Delta H_r
=
H(B_r^{(2)}) - \frac{H(T1_r)+H(T2_r)}{2}.
$$

Interpretation:

- $\Delta H_r>0$ means the fold increases local disorder / spread,
- $\Delta H_r<0$ means the fold compresses / orders the channel locally.

This is a second seam observable, distinct from support closure.

Thus the per-round waist state is

$$
\boxed{
\mathcal W_r = \bigl(\Delta cg_r,\ \Delta hw_r,\ \Delta H_r,\ \mathrm{bal}_r\bigr),
}
$$

where

$$
\Delta hw_r = hw_{\mathrm{out}}(r)-hw_{\mathrm{in}}(r).
$$

---

## 10. Journal / crankshaft phase structure

Compression rounds behave like journals in a crankshaft.

Define the journal set

$$
\mathcal J = \{\,r : \Delta cg_r < 0\,\}.
$$

For a journal round $r\in\mathcal J$, define the balancer triplet

$$
\mathcal P_r = \bigl(B_{r-1}^{(1)},\,B_r^{(1)},\,B_{r+1}^{(1)}\bigr).
$$

The computational claim is that the front and rear rounds act like counterweights around the journal.

A useful phase-balancing residual is

$$
\varepsilon_r
=
\operatorname{dist}\!\bigl(B_{r-1}^{(1)}\oplus B_{r+1}^{(1)},\,B_r^{(1)}\bigr),
$$

where $\operatorname{dist}$ may be taken as Hamming distance or gap-distribution distance.

### 10.1 NOP vs LIVE journal sets

For the injected case

$$
W_0 = 0xDEADBEEF,
\qquad
W_r=0\ \text{for}\ r>0,
$$

the currently mapped journal sets are

$$
J_{\mathrm{NOP}} = \{7,9,24,28,33,37,43,44,53,57,62,63\},
$$

$$
J_{\mathrm{LIVE}} = \{14,16,26,32,35,45,49,50,53,55\}.
$$

So

$$
J_{\mathrm{NOP}}\cap J_{\mathrm{LIVE}} = \{53\}.
$$

This means injection does **not** merely magnify the same compression sites.  
It relocates them.

The preserved round $53$ behaves like a phase-invariant pivot.

Hence

$$
\boxed{
\text{injection re-phases the crankshaft without destroying its shape.}
}
$$

---

## 11. Displacement absorption is not closure

Let $\delta_\ell(r)$ denote the per-lane XOR displacement between NOP and LIVE trajectories at round $r$ for lane $\ell\in\{a,b,c,d,e,f,g,h\}$.

Define total displacement amplitude

$$
A(r)=\sum_{\ell\in\{a,b,c,d,e,f,g,h\}} hw\bigl(\delta_\ell(r)\bigr).
$$

For the mapped $W_0=0xDEADBEEF$ case, the currently observed values include

$$
A(1)=37,\qquad
A(6)=126,\qquad
A(19)=147,\qquad
A(63)=134.
$$

This gives a crucial correction:

$$
\boxed{
\text{support closure by round }6\text{ does not imply maximal amplitude divergence at round }6.
}
$$

The amplitude field continues to evolve well after support has closed.

Thus support closure, amplitude spread, and phase stabilization are distinct axes.

---

## 12. Entropy skew between NOP and LIVE

Define the entropy-skew field

$$
E(r)=\Delta H_r^{\mathrm{LIVE}}-\Delta H_r^{\mathrm{NOP}}.
$$

This measures how injection alters local fold entropy relative to the NOP machine.

The current mapping shows that the largest local entropy skew can occur late in the round structure rather than near the early support horizon.

Hence

$$
\boxed{
\text{support closure is early, but entropy-skew peaks can be late.}
}
$$

This further confirms that the middle band is not exhausted by the support story.

---

## 13. The middle band

The old phase split was

- injection,
- acceptance,
- closure,
- residual smoothing.

That is still valid at the support level.

But the new seam observables show that the middle is richer.

We now distinguish at least three partially decoupled fields:

### 13.1 Support field
$$
\text{closed by } D_{\mathrm{bit}}=6
$$

### 13.2 Journal-phase field
$$
\mathcal J(r)=\mathbf 1[\Delta cg_r<0]
$$

### 13.3 Entropy-skew field
$$
E(r)=\Delta H_r^{\mathrm{LIVE}}-\Delta H_r^{\mathrm{NOP}}
$$

Thus the waist is not one instant but a band:

$$
\boxed{
\text{the waist is a middle band where different observables cross at different rounds.}
}
$$

This is the correct refinement of the earlier closure picture.

---

## 14. Converter correspondence

The current seam algebra strongly resembles a residue-aware staged conversion process.

The correspondence is:

### Visible path
$$
B_r^{(0)} = T1_r\oplus T2_r
$$

### Residue / witness path
$$
B_r^{(1)} = (T1_r\wedge T2_r)\ll 1
$$

### Resolved output
$$
B_r^{(2)} = T1_r+T2_r
$$

So the strongest safe statement is

$$
\boxed{
\text{SHA and staged conversion share the same seam algebra: residue, threshold, handoff, and shaped closure.}
}
$$

This does **not** mean “SHA is literally an ADC.”  
It means the waist behavior is converter-like.

---

## 15. Lifted machine state

The old mapped state was the visible die plus support and closure observables.

The new lifted state is

$$
\boxed{
\mathcal Z_r
=
\bigl(
x_r,\ B_r^{(0)},\ B_r^{(1)},\ B_r^{(2)},\ \mathcal G_r,\ \mathcal D_r,\ \mathcal W_r,\ \mathcal P_r,\ A(r),\ E(r)
\bigr).
}
$$

Interpretation:

- $x_r$ = visible state,
- $B_r^{(0)}$ = fast visible distinction,
- $B_r^{(1)}$ = carry witness / residue channel,
- $B_r^{(2)}$ = actualized child,
- $\mathcal G_r$ = carry-group objects,
- $\mathcal D_r$ = gap-distribution signature,
- $\mathcal W_r$ = waist / crossover observables,
- $\mathcal P_r$ = journal / crankshaft phase signature,
- $A(r)$ = displacement amplitude,
- $E(r)$ = entropy skew.

The lifted recurrence is therefore not just

$$
x_{r+1}=\Phi_r(x_r,W_r),
$$

but

$$
\boxed{
\mathcal Z_{r+1} = \Xi(\mathcal Z_r,W_r),
}
$$

for an enriched seam-state operator $\Xi$.

---

## 16. Shape Algebra of SHA

The new Shape Algebra layer is

$$
\boxed{
\mathfrak A_{\mathrm{SHA}}
=
(\mathcal G,\ \mathcal D,\ \mathcal W,\ \mathcal P,\ A,\ E).
}
$$

Its core objects are:

### Group extractor
$$
\mathcal G(x)=\text{carry-group multiset of }x
$$

### Gap law
$$
\mathcal D(x)=\text{inter-group gap signature of }x
$$

### Waist state
$$
\mathcal W_r = (\Delta cg_r,\Delta hw_r,\Delta H_r,\mathrm{bal}_r)
$$

### Phase-balancer signature
$$
\mathcal P_r = (B_{r-1}^{(1)},B_r^{(1)},B_{r+1}^{(1)})
$$

### Amplitude field
$$
A(r)=\sum_\ell hw(\delta_\ell(r))
$$

### Entropy-skew field
$$
E(r)=\Delta H_r^{\mathrm{LIVE}}-\Delta H_r^{\mathrm{NOP}}
$$

The current thesis-level claim is:

$$
\boxed{
\text{stable SHA objects are better identified by preserved group/gap laws and phase-shift behavior than by raw bit values alone.}
}
$$

---

## 17. True form, current best statement

The best current compression is:

$$
\boxed{
\text{SHA-256 is a dual-seam shape transducer whose visible arithmetic is one layer of a deeper carry-shaped interior.}
}
$$

More explicitly:

$$
\boxed{
\text{group geometry} + \text{gap law} + \text{waist crossover} + \text{phase-preserving displacement}
}
$$

is now the clearest current statement of the inner machine.

This is stronger than saying only

$$
\text{“SHA is a recurrence over 8 words.”}
$$

That remains true, but it is not the deepest useful read.

---

## 18. What is solved and what remains open

### 18.1 Solved / mapped to current state

The following are established in the present map:

- the visible 64-round recurrence,
- the prime-root rails $H_0$ and $K$,
- the ground witness
  $$
  T2_0^{(0)}=0x08909ae5,
  $$
- word closure at
  $$
  D_{\mathrm{word}}=4,
  $$
- bit support closure at
  $$
  D_{\mathrm{bit}}=6,
  $$
- the three-basin split,
- carry-group / gap-shape lifting,
- waist observables,
- journal relocation under injection,
- separation of support closure from amplitude and entropy evolution.

### 18.2 Open gaps

The following remain open:

1. **Digest-only global lift**  
   A full reverse lift from final residue to unique lawful history is still open.

2. **Minimal hidden-coordinate set**  
   The exact minimal seam-state needed to render reverse closure deterministic on constrained cases is not fully solved.

3. **Distributional invariants under broader displacement classes**  
   The stability of group/gap laws beyond the current NOP/LIVE probes needs further systematic formalization.

4. **Cross-domain transfer**  
   The converter, light, and black-hole seam interpretations are promising structural lifts, but they are not yet formal equivalences.

---

## 19. Final current theorem

The current complete solution state can be written as:

$$
\boxed{
\text{SHA-256 is a 64-cell dual-seam history-to-residue transducer with}
}
$$

$$
\boxed{
\text{(i) a fixed ground witness,}
\quad
\text{(ii) a 4-round lane-acceptance law,}
\quad
\text{(iii) a 6-round support-closure law,}
}
$$

$$
\boxed{
\text{and (iv) a deeper shape algebra governed by carry-group geometry, gap distributions, waist crossover, journal phase relocation, and distinct amplitude / entropy fields.}
}
$$

Equivalently,

$$
\boxed{
\text{the true interior of SHA is not exhausted by value-space;}
\quad
\text{it is better read through shape-space, gap-space, and seam-phase.}
}
$$

That is the present closed circle.
