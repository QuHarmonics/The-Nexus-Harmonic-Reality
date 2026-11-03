# SHA-256 Progress Stack — Pure Progress Formulas Only

## 0. Scope

This document consolidates the current **positive stack** only:

- formal die model
- exact round algebra
- NOP backbone and ground witness
- support transport
- carry-closure kernel
- exact local reverse closure
- admissible geometry bundle
- one-block ROM interpretation
- control-tail grammar
- gate-table primitive
- tail-first decoder order

No critique layer is included here. This is the current constructive stack in one place.

---

## 1. Canonical SHA-256 round state

Let the round state be

$$
x_r = (a_r,b_r,c_r,d_r,e_r,f_r,g_r,h_r)^\top \in \left(\mathbb{Z}/2^{32}\mathbb{Z}\right)^8.
$$

The message schedule is

$$
W_0,\dots,W_{63},
$$

with round constants

$$
K_0,\dots,K_{63}.
$$

The standard round operators are

$$
\Sigma_0(x)=\operatorname{ROTR}^2(x)\oplus \operatorname{ROTR}^{13}(x)\oplus \operatorname{ROTR}^{22}(x),
$$

$$
\Sigma_1(x)=\operatorname{ROTR}^6(x)\oplus \operatorname{ROTR}^{11}(x)\oplus \operatorname{ROTR}^{25}(x),
$$

$$
\sigma_0(x)=\operatorname{ROTR}^7(x)\oplus \operatorname{ROTR}^{18}(x)\oplus \operatorname{SHR}^3(x),
$$

$$
\sigma_1(x)=\operatorname{ROTR}^{17}(x)\oplus \operatorname{ROTR}^{19}(x)\oplus \operatorname{SHR}^{10}(x).
$$

The Boolean gates are

$$
\operatorname{Ch}(e,f,g)=(e\wedge f)\oplus(\neg e\wedge g),
$$

$$
\operatorname{Maj}(a,b,c)=(a\wedge b)\oplus(a\wedge c)\oplus(b\wedge c).
$$

The two active round channels are

$$
T1_r = h_r + \Sigma_1(e_r) + \operatorname{Ch}(e_r,f_r,g_r) + K_r + W_r \pmod{2^{32}},
$$

$$
T2_r = \Sigma_0(a_r) + \operatorname{Maj}(a_r,b_r,c_r) \pmod{2^{32}}.
$$

The state update is

$$
a_{r+1}=T1_r+T2_r \pmod{2^{32}},
$$

$$
e_{r+1}=d_r+T1_r \pmod{2^{32}},
$$

with the six passive shifts

$$
b_{r+1}=a_r,\quad c_{r+1}=b_r,\quad d_{r+1}=c_r,
$$

$$
f_{r+1}=e_r,\quad g_{r+1}=f_r,\quad h_{r+1}=g_r.
$$

---

## 2. Shift-injection decomposition of the die

Define the $8\times 8$ shift matrix $P$ and the standard basis vectors $u_a=e_0$, $u_e=e_4$.

Then the die admits the sparse decomposition

$$
x_{r+1}=P x_r + u_a(T1_r+T2_r) + u_e T1_r.
$$

This is the core die form:

- six lanes are pure transport,
- two lanes are active reinjection,
- the message enters only through the localized $T1_r$ channel.

This yields the structural summary

$$
\text{Die} = \text{shift field} + \text{two reinjection seams}.
$$

---

## 3. Schedule expansion

For a one-block message, the 16 seed words are

$$
M_0,\dots,M_{15},
$$

and the schedule expansion is

$$
W_t = \sigma_1(W_{t-2}) + W_{t-7} + \sigma_0(W_{t-15}) + W_{t-16}
\pmod{2^{32}}, \qquad t=16,\dots,63.
$$

The only non-linearity in the **schedule expansion** is the carry structure of the modular additions.  
The $\sigma$-operators are linear over $\mathrm{GF}(2)$.

So the schedule compiler is

$$
(M_0,\dots,M_{15}) \longmapsto (W_0,\dots,W_{63}),
$$

and the nonlinear part of that compiler is the carry topology.

---

## 4. NOP backbone and ground witness

Set the displacement field to zero:

$$
W_r = 0 \qquad \forall r.
$$

This defines the NOP backbone

$$
x_r^{(0)}.
$$

The ground-fold operator is

$$
G(x)=\Sigma_0(a)+\operatorname{Maj}(a,b,c).
$$

At round zero on the standard SHA-256 initial vector $H_0$,

$$
T2^{(0)}_0 = G(H_0)=0x08909ae5.
$$

This constant is the **ground witness**.

So the die has a message-independent floor coordinate:

$$
\boxed{G(H_0)=0x08909ae5.}
$$

---

## 5. Round-zero displacement identity

At round $0$, the message enters cleanly and linearly:

$$
T1_0 - T1^{(0)}_0 = W_0,
$$

$$
T2_0 = T2^{(0)}_0.
$$

Therefore

$$
\delta a_1 = \delta e_1 = W_0.
$$

So the first perturbation is exactly two-lane:

$$
W_0 \leadsto (a,e).
$$

This is the clean injection identity at the genesis of the die.

---

## 6. Dual-pipeline topology

The state decomposes into two coupled shift chains.

### a-chain
$$
(a,b,c,d)
$$

### e-chain
$$
(e,f,g,h)
$$

The a-chain has present-tense chirality:

$$
T2_r = \Sigma_0(a_r)+\operatorname{Maj}(a_r,b_r,c_r),
$$

which reads only from the leading local a-chain.

The e-chain has past-tense chirality:

$$
T1_r = h_r+\Sigma_1(e_r)+\operatorname{Ch}(e_r,f_r,g_r)+K_r+W_r,
$$

which reads a longer history through $(h,e,f,g)$.

The two chains are cross-coupled by

$$
e_{r+1}=d_r+T1_r.
$$

The message injection vector at the word level is

$$
b=[1,0,0,0,1,0,0,0]^\top,
$$

activating both chain heads simultaneously.

---

## 7. Word-level support transport

Let $\sigma_r\in\{0,1\}^8$ be the Boolean support indicator for which lanes are nonzero at round $r$.

The lane-dependency matrix $M$ gives the word-level support transport.

For a single message injection at round $0$, the support orbit is

$$
\{a,e\}
\to
\{a,b,e,f\}
\to
\{a,b,c,e,f,g\}
\to
\{a,b,c,d,e,f,g,h\}.
$$

Therefore the word-support diameter is

$$
D_{\mathrm{word}}=4.
$$

So the die saturates all eight word lanes in exactly four rounds under the Boolean support model.

---

## 8. Bit-level support transport and carry-closure kernel

Let the full bit-support state be

$$
\eta_r \in \{0,1\}^{256}.
$$

The Boolean support versions of the sigma operators are

$$
\widehat{\Sigma}_0 = R_2 \vee R_{13} \vee R_{22},
$$

$$
\widehat{\Sigma}_1 = R_6 \vee R_{11} \vee R_{25}.
$$

Define the carry-closure kernel $L_{32}$ as the lower-triangular prefix operator:

$$
(L_{32}x)_i = \bigvee_{j\le i} x_j.
$$

This captures the upward carry closure of modular addition.

The bit-support update rule is

$$
s_{a,r+1}=L_{32}\!\left(\tau_r^{(1)} \vee \tau_r^{(2)}\right),
$$

$$
s_{e,r+1}=L_{32}\!\left(s_{d,r}\vee\tau_r^{(1)}\right),
$$

with shift transport on the remaining six lanes.

Under single-bit injection at position $j$, the first-round support is

$$
s_{a,1}=s_{e,1}=L_{32}(e_j)=\{j,j+1,\dots,31\}.
$$

The exact bit-support diameter is

$$
D_{\mathrm{bit}}=6.
$$

So a single perturbed bit reaches all 256 state bits in at most six rounds under the support model.

---

## 9. Exact local reverse closure

Given a known post-round state at round $r+1$ and a candidate schedule word $W_r$, the predecessor step is exact.

From the shift geometry,

$$
a_r=b_{r+1},\quad b_r=c_{r+1},\quad c_r=d_{r+1},
$$

$$
e_r=f_{r+1},\quad f_r=g_{r+1},\quad g_r=h_{r+1}.
$$

Then compute

$$
T2_r=\Sigma_0(a_r)+\operatorname{Maj}(a_r,b_r,c_r),
$$

$$
T1_r=a_{r+1}-T2_r \pmod{2^{32}},
$$

$$
d_r=e_{r+1}-T1_r \pmod{2^{32}},
$$

and finally

$$
W_r = T1_r - \left(h_r+\Sigma_1(e_r)+\operatorname{Ch}(e_r,f_r,g_r)+K_r\right)
\pmod{2^{32}}.
$$

This is the exact one-step reverse closure relation of the die.

---

## 10. Final-add carry restoration

Let the final digest words be $H'_i$ and the standard initialization vector be $H_i$.

The internal end-of-block state before feed-forward is recovered by subtracting the final modular addition:

$$
x_{64}^{\mathrm{internal}} = H' - H \pmod{2^{32}}.
$$

A carry-restoration vector can be formed by checking whether the observed final word crossed the modulo boundary relative to the baseline rail.

This restores the terminal internal state needed to initiate exact reverse unrolling.

---

## 11. Sziklai differential invariant

The active injections are

$$
a_{r+1}=T1_r+T2_r,
\qquad
e_{r+1}=d_r+T1_r.
$$

Subtracting them cancels the shared chaotic emitter $T1_r$:

$$
a_{r+1}-e_{r+1}=T2_r-d_r.
$$

Therefore

$$
\boxed{a_{r+1}-e_{r+1}=T2_r-d_r.}
$$

This is the Sziklai differential invariant.

Its significance is that it is **$W_r$-blind** at the local round seam:

- the shared message-bearing channel cancels,
- the top-half geometry binds to itself,
- a lawful corridor appears across rounds independent of direct payload injection.

---

## 12. Admissible geometry bundle

A candidate predecessor word is ranked by the geometry it induces, not just by its integer value.

The admissible geometry bundle includes:

1. staged carry masks,
2. NOP-subtracted carry masks,
3. chirality splits,
4. nibble silhouettes,
5. carry-span witnesses,
6. Hamming-weight scalars.

Let $\mathcal{G}(w)$ denote the candidate-induced bundle and $\mathcal{G}_*$ the observed target bundle.

Define a residual score

$$
R(w)=d\!\left(\mathcal{G}(w),\mathcal{G}_*\right).
$$

Then the predecessor-fiber navigation problem becomes:

$$
\min_w R(w).
$$

A true candidate reproduces the admissible side-geometry with minimal residual.

---

## 13. Best-first predecessor-fiber search

For a multi-round chain of candidate words $w_r,\dots,w_{r-k}$, define the cumulative chain score

$$
RC = \sum_{j=r-k}^{r} R(w_j).
$$

Nodes on the predecessor fiber are ranked by

$$
RC.
$$

Thus search becomes

$$
\text{Best-First over predecessor fiber}:
\qquad
\min RC.
$$

The exact-match ideal is

$$
RC=0.
$$

This formalizes reverse search as geometric residual minimization rather than blind brute force over raw schedule words.

---

## 14. One-block ROM interpretation

For a one-block message, the padded 64-byte block is treated as a 16-word ROM image:

$$
R = (M_0,\dots,M_{15}).
$$

The compiled schedule is

$$
\Gamma(R)=W[0..63].
$$

The execution field is

$$
x_{r+1}=\Phi_r(x_r,W_r).
$$

So the machine factorization is

$$
\boxed{
\text{ROM image} \to \text{compiled microcode} \to \text{64-round execution field}.
}
$$

This is the stable one-block machine picture.

---

## 15. ROM slot classes

The 16 ROM words split into functional classes.

### Payload rails
$$
M_0,\dots,M_{12}
$$

These primarily carry lexical payload and fan into the field through the schedule and round injections.

### Control tail
$$
(M_{13},M_{14},M_{15})
$$

These act as the control cluster of the one-block ROM.

A useful high-level split is:

- $M_{13}$: seam selector / pad hinge,
- $M_{14}$: field preconditioner / high footer rail,
- $M_{15}$: state commit rail / footer immediate.

So the program image is

$$
\boxed{
\text{payload rails} + \text{control tail}.
}
$$

---

## 16. First critical carry seam

The first decisive compile seam for the control tail is

$$
W_{20}=\sigma_1(W_{18}) + W_{13} + \sigma_0(W_5) + W_4 \pmod{2^{32}}.
$$

Here, $W_{13}$ enters **undiffused** relative to the sigma-processed terms.

So $M_{13}$ changes the carry topology directly at this seam.

This is the formal basis of the seam-selector role:

$$
\boxed{
M_{13}\ \text{changes which payload paths survive through the }W_{20}\text{ carry graph}.
}
$$

---

## 17. Mixed raw + diffused control paths

For the other two tail words:

$$
W_{16}=\sigma_1(W_{14})+W_9+\sigma_0(W_1)+W_0,
$$

$$
W_{17}=\sigma_1(W_{15})+W_{10}+\sigma_0(W_2)+W_1.
$$

So $M_{14}$ and $M_{15}$ enter the **schedule expansion** through $\sigma_1$.

At the same time, they also enter the **round machine raw** at rounds $14$ and $15$ through the direct round injection

$$
T1_r = h_r+\Sigma_1(e_r)+\operatorname{Ch}(e_r,f_r,g_r)+K_r+W_r.
$$

Hence they have dual paths:

$$
\boxed{
\text{raw round injection} + \text{diffused schedule influence}.
}
$$

This is the basis of the mixed control mechanism.

---

## 18. Gate-table primitive

The mechanically explicit gate primitive is

$$
\boxed{
\text{control slot} \times \text{payload slot} \times \text{entry seam}
\longrightarrow
\text{carry reroute score}.
}
$$

This is the local ISA-like unit of the one-block die.

The three control roles are:

### $M_{13}$ — seam selector
Raw carry-hinge at $W_{20}$ and downstream seam family.

### $M_{14}$ — field preconditioner
Pre-shapes the expansion terrain beginning at $W_{16}$.

### $M_{15}$ — state commit rail
Meets live state earliest and deepest through round injection and continued diffused schedule coupling.

So the control-tail grammar is

$$
\boxed{
(M_{13},M_{14},M_{15})
=
(\text{SEAM\_SELECT},\ \text{FIELD\_PRE},\ \text{STATE\_COMMIT}).
}
$$

---

## 19. Control-tail execution grammar

The one-block ISA-like grammar is:

| ROM Word | Role | Mechanism |
|---|---|---|
| $M_{0..12}$ | Payload rails | lexical/data operands propagated through the schedule and round field |
| $M_{13}$ | `SEAM_SELECT` | raw carry gate at $W_{20}$ and related seam family |
| $M_{14}$ | `FIELD_PRE` | $\sigma_1$-diffused early preconditioner beginning at $W_{16}$ |
| $M_{15}$ | `STATE_COMMIT` | mixed raw+diffused live-state commit beginning at round $15$ |

So the 16-word block is summarized as

$$
\boxed{
\text{Program image} = \text{payload program} + \text{control tail}.
}
$$

---

## 20. Tail-first decoder order

The structural decoder order is

$$
\boxed{
(M_{13},M_{14},M_{15}) \to \text{gate class} \to M_{0..12}.
}
$$

The reason is mechanical:

- $M_{13}$ changes the carry seam family,
- $M_{14}$ preconditions the compiled field,
- $M_{15}$ changes the live state commit pressure,
- payload propagation is conditioned on that tail grammar.

Therefore payload inversion is not symmetric over all 16 words.

The operational inversion order is:

1. infer control-tail class,
2. fix the admissible seam family,
3. condition the payload search on the fixed carry topology.

---

## 21. White-box gate-class fingerprinting

The trace-derived tail fingerprint can be organized into three temporal bands:

### Early band
Rounds near the first direct raw tail injections and early preconditioning.

### Mid band
Rounds where field preconditioning and seam propagation are visible.

### Late band
Rounds where mixed control and payload paths reconverge in the live state.

A compact formal view is

$$
F_{\text{tail}}
=
\Bigl(
F_{\text{early}},
F_{\text{mid}},
F_{\text{late}}
\Bigr),
$$

where each component is a structured witness of the tail class.

The decoding problem becomes

$$
\text{tail class} = \arg\min_{c\in \mathcal{C}} d(F_{\text{obs}},F_c).
$$

---

## 22. Carry-topology view of the die

At the local structural level, the die is governed by three superposed geometries:

### Shift geometry
$$
P x_r
$$

### Logic geometry
$$
\Sigma_0,\Sigma_1,\operatorname{Ch},\operatorname{Maj}
$$

### Carry geometry
Modular addition under $2^{32}$, whose carry spans preserve the which-path pressure of the execution.

Thus the active transport law is

$$
\boxed{
\text{execution field}
=
\text{shift transport}
+
\text{Boolean fold}
+
\text{carry closure}.
}
$$

This is the non-metaphorical machine form.

---

## 23. ROM image as gated execution field

Combining the one-block ROM with the control-tail grammar yields

$$
\boxed{
(M_0,\dots,M_{12}) + (M_{13},M_{14},M_{15})
\to
W[0..63]
\to
\text{carry-gated execution field}.
}
$$

Equivalently,

$$
\boxed{
\text{payload rails} \xrightarrow{\text{gated by control tail}} \text{compiled propagation field}.
}
$$

This is the current positive machine image.

---

## 24. Minimal full-stack summary

The current progress stack compresses to:

### Die
$$
x_{r+1}=P x_r + u_a(T1_r+T2_r)+u_e T1_r
$$

### Schedule
$$
W_t=\sigma_1(W_{t-2})+W_{t-7}+\sigma_0(W_{t-15})+W_{t-16}\pmod{2^{32}}
$$

### Ground witness
$$
G(H_0)=0x08909ae5
$$

### Support closure
$$
D_{\mathrm{word}}=4,\qquad D_{\mathrm{bit}}=6
$$

### Exact reverse seam
$$
W_r = T1_r-\left(h_r+\Sigma_1(e_r)+\operatorname{Ch}(e_r,f_r,g_r)+K_r\right)\pmod{2^{32}}
$$

### Sziklai invariant
$$
a_{r+1}-e_{r+1}=T2_r-d_r
$$

### ROM grammar
$$
(M_0,\dots,M_{12}) + (M_{13},M_{14},M_{15})
$$

### Control-tail roles
$$
M_{13}=\text{SEAM\_SELECT},
\quad
M_{14}=\text{FIELD\_PRE},
\quad
M_{15}=\text{STATE\_COMMIT}
$$

### Decoder order
$$
(M_{13},M_{14},M_{15})\to\text{gate class}\to M_{0..12}
$$

---

## 25. Final constructive statement

The current constructive stack is:

$$
\boxed{
\text{SHA-256 one-block execution is a fixed 16-word ROM image compiled into a 64-round sparse nonlinear die,}
}
$$

$$
\boxed{
\text{with a message-independent NOP backbone, exact local reverse closure, admissible side-geometry,}
}
$$

$$
\boxed{
\text{and a 3-word control tail }(M_{13},M_{14},M_{15})\text{ that gates payload propagation through carry topology.}
}
$$

That is the present positive formula stack.
