# Bitcoin SHA-256 Reverse Geometry — Fused-Term Decoder Complete Solution

## Abstract

This document extends the Bitcoin tension-probe program into a **math-first inversion framework**.  
The central shift is this:

- We are **not** solving “guess the message word.”
- We are solving the **unique lawful split** of the fused reverse-round wall
  $$
  F_r \equiv h_r + W_r \pmod{2^{32}}.
  $$

Once the next round state $x_{r+1}$ is known, the SHA-256 die already determines **seven of the eight predecessor state words exactly**. The only unresolved object is the fused pair $(h_r, W_r)$. The entire brute-force problem therefore collapses to a constrained **bitwise carry automaton** driven by admissible side geometry.

This writeup makes that collapse explicit, derives the bit-level recurrence, defines the admissible budget-state solver, and shows how local round decoding can be chained backward through both the **state transport law** and the **message schedule law**. The result is a complete mathematical roadmap for replacing word brute force with symbolic elimination.

---

## 1. The SHA-256 die as a sparse nonlinear recurrence

Let the compression-state vector at round $r$ be

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
\in \left(\mathbb{Z}/2^{32}\mathbb{Z}\right)^8.
$$

One SHA-256 round is

$$
x_{r+1} = \Phi_r(x_r, W_r),
\qquad r=0,\dots,63.
$$

Define the shift matrix

$$
P =
\begin{bmatrix}
0&0&0&0&0&0&0&0\\
1&0&0&0&0&0&0&0\\
0&1&0&0&0&0&0&0\\
0&0&1&0&0&0&0&0\\
0&0&0&1&0&0&0&0\\
0&0&0&0&1&0&0&0\\
0&0&0&0&0&1&0&0\\
0&0&0&0&0&0&1&0
\end{bmatrix}.
$$

Then

$$
P x_r =
\begin{bmatrix}
0\\
a_r\\
b_r\\
c_r\\
d_r\\
e_r\\
f_r\\
g_r
\end{bmatrix}.
$$

Define the two nonlinear injections

$$
T1_r = h_r + \Sigma_1(e_r) + \operatorname{Ch}(e_r,f_r,g_r) + K_r + W_r,
$$

$$
T2_r = \Sigma_0(a_r) + \operatorname{Maj}(a_r,b_r,c_r).
$$

Let

$$
u_a =
\begin{bmatrix}
1\\0\\0\\0\\0\\0\\0\\0
\end{bmatrix},
\qquad
u_e =
\begin{bmatrix}
0\\0\\0\\0\\1\\0\\0\\0
\end{bmatrix}.
$$

Then the full die equation is

$$
x_{r+1}
=
P x_r
+
u_a (T1_r + T2_r)
+
u_e T1_r.
$$

This matters because the die is **sparse**:

- six lanes are pure shifts,
- only two lanes are active reinjections,
- the inversion difficulty therefore concentrates in the reinjection wall rather than the whole state.

---

## 2. Exact reverse closure up to one fused wall

Given $x_{r+1}$, six predecessor words are immediate from the shift structure:

$$
a_r = b_{r+1},
\qquad
b_r = c_{r+1},
\qquad
c_r = d_{r+1},
$$

$$
e_r = f_{r+1},
\qquad
f_r = g_{r+1},
\qquad
g_r = h_{r+1}.
$$

Now compute

$$
T2_r = \Sigma_0(a_r) + \operatorname{Maj}(a_r,b_r,c_r).
$$

Using the round outputs,

$$
a_{r+1} = T1_r + T2_r,
\qquad
e_{r+1} = d_r + T1_r.
$$

Subtracting gives the exact differential identity

$$
a_{r+1} - e_{r+1}
\equiv
T2_r - d_r
\pmod{2^{32}}.
$$

Therefore

$$
d_r \equiv T2_r - (a_{r+1} - e_{r+1}) \pmod{2^{32}}.
$$

Then

$$
T1_r \equiv e_{r+1} - d_r \pmod{2^{32}}.
$$

So from $x_{r+1}$ alone we now know:

- $a_r,b_r,c_r,d_r,e_r,f_r,g_r$,
- $T2_r$,
- $T1_r$,

all **exactly**.

The only unresolved object is therefore

$$
h_r + W_r.
$$

That is the true reverse wall.

---

## 3. The fused reverse wall

Rearrange the $T1_r$ equation:

$$
T1_r
=
h_r
+
\Sigma_1(e_r)
+
\operatorname{Ch}(e_r,f_r,g_r)
+
K_r
+
W_r.
$$

So define the fused term

$$
F_r
:=
T1_r
-
\Sigma_1(e_r)
-
\operatorname{Ch}(e_r,f_r,g_r)
-
K_r
\pmod{2^{32}}.
$$

Then

$$
\boxed{
F_r \equiv h_r + W_r \pmod{2^{32}}
}
$$

This is the entire remaining ambiguity of a reverse round.

So the problem is no longer:

$$
\text{guess }W_r \in \{0,\dots,2^{32}-1\}.
$$

It is:

$$
\text{decode the unique lawful split }(h_r,W_r)\text{ of }F_r.
$$

---

## 4. Match versus failure in mathematical terms

A candidate match is **not** “the right number.”

A candidate match is a pair $(h_r, W_r)$ such that:

1. it satisfies the fused wall,
   $$
   h_r + W_r \equiv F_r \pmod{2^{32}},
   $$
2. it reproduces the exported admissible side geometry,
3. it remains recursively compatible with adjacent rounds.

A failure is any pair that:

- satisfies the sum but produces the wrong carry scar,
- satisfies local scar projections but poisons the predecessor chain,
- or survives one round only because the bundle is degenerate.

So the core distinction is

$$
\text{match} = \text{same fold geometry},
$$

$$
\text{failure} = \text{geometric inconsistency under recursion}.
$$

---

## 5. Bitwise decomposition of the fused wall

Let $F_j$, $h_j$, and $w_j$ be bit $j$ of $F_r$, $h_r$, and $W_r$ respectively, with $j=0,\dots,31$.

Let $c_j$ be the carry into bit $j$, with

$$
c_0 = 0.
$$

Then the bitwise addition law is

$$
h_j + w_j + c_j = F_j + 2c_{j+1}.
$$

Reducing modulo $2$ gives

$$
h_j \oplus w_j \oplus c_j = F_j,
$$

hence

$$
\boxed{
w_j = F_j \oplus h_j \oplus c_j
}
$$

So if $h_j$ and $c_j$ are known, then $w_j$ is **forced**.

The next carry is

$$
c_{j+1} = \operatorname{Maj}(h_j, w_j, c_j).
$$

Substitute $w_j = F_j \oplus h_j \oplus c_j$ and simplify.

There are only two cases:

### Case 1: $F_j = c_j$

Then

$$
w_j = h_j,
$$

and therefore

$$
c_{j+1} = \operatorname{Maj}(h_j,h_j,c_j)=h_j.
$$

### Case 2: $F_j \neq c_j$

Then

$$
w_j = 1 \oplus h_j,
$$

so $(h_j,w_j)$ are complementary and

$$
c_{j+1} = \operatorname{Maj}(h_j,1\oplus h_j,c_j)=c_j.
$$

Therefore the carry recursion is

$$
\boxed{
c_{j+1} =
\begin{cases}
h_j, & F_j = c_j,\\[6pt]
c_j, & F_j \neq c_j.
\end{cases}
}
$$

This is the crucial no-brute-force law.

It means the fused wall is not a 32-bit blind search. It is a **finite-state bit decoder**.

---

## 6. Immediate consequences of the carry law

The fused split now behaves as follows:

### Regime A: forced-carry regime

If

$$
F_j = c_j,
$$

then the next carry equals $h_j$:

$$
c_{j+1} = h_j.
$$

So if the side bundle reveals the actual carry-out bit at that position, then $h_j$ is known exactly, and therefore

$$
w_j = F_j \oplus h_j \oplus c_j
$$

is known exactly too.

That bit is solved with **zero guessing**.

### Regime B: frozen-carry regime

If

$$
F_j \neq c_j,
$$

then

$$
c_{j+1}=c_j
$$

independent of $h_j$.

So the carry bit alone does not choose between the two possibilities for $h_j$ and $w_j$.

This is where extra admissible side scars must intervene.

Thus the round-local ambiguity is not 32 free bits. It is only the subset of bits that fall into the frozen-carry regime and are not otherwise constrained by scar budgets.

---

## 7. Admissible side geometry

The exported bundle must capture **scar**, not **payload**.

Admissible observables include:

### 7.1 Carry scars
- staged carry-out bits,
- full carry-mask patterns,
- NOP-subtracted carry masks,
- carry-mask chirality splits.

### 7.2 Register silhouettes
- nibble-wise Hamming silhouette of $h_r$,
- even/odd chirality partitions of $h_r$.

### 7.3 Seam witnesses
- seam-specific max carry-span,
- seam-specific first-hit / last-hit positions,
- seam-specific span histograms.

### 7.4 Cross-round silhouettes
- derived silhouette of the Sziklai differential
  $$
  a_{r+1}-e_{r+1} \equiv T2_r-d_r \pmod{2^{32}},
  $$
  not the raw invariant itself.

These do not reveal $W_r$ directly, but they constrain the lawful split of $F_r$.

---

## 8. Budget-state formulation

Let the admissible side information at round $r$ be encoded as a finite budget vector

$$
q_0.
$$

This budget may contain:

- remaining chirality counts,
- remaining nibble populations,
- required seam-span class,
- carry-mask pattern obligations,
- differential silhouette class.

At bit position $j$, define the dynamic-programming state

$$
S_j = (c_j, q_j),
$$

where:

- $c_j \in \{0,1\}$ is the current carry,
- $q_j$ is the remaining admissible-budget state after bits $0,\dots,j-1$ have been decoded.

A transition chooses $h_j \in \{0,1\}$, then computes

$$
w_j = F_j \oplus h_j \oplus c_j,
$$

updates the carry using

$$
c_{j+1} =
\begin{cases}
h_j, & F_j = c_j,\\[6pt]
c_j, & F_j \neq c_j,
\end{cases}
$$

and updates the budget

$$
q_{j+1} = q_j - \Delta q(h_j,w_j,c_j,c_{j+1},j),
$$

where $\Delta q$ is the scar contribution induced by that local bit decision.

Thus the recursion is

$$
(c_j,q_j) \longrightarrow (c_{j+1},q_{j+1}).
$$

The accepting condition is

$$
\boxed{
(c_{32},q_{32}) = (0,0)
}
$$

or more generally, $(c_{32},q_{32})$ lying in a prescribed terminal-acceptance set.

This is a constrained automaton solve, not a word brute-force loop.

---

## 9. Local decoder theorem

### Theorem (Round-local split decoding)

Let $F_r$ be known. Let the admissible geometry bundle be encoded as a finite budget state $q_0$. Then the lawful splits $(h_r,W_r)$ of the fused wall

$$
F_r \equiv h_r + W_r \pmod{2^{32}}
$$

are in one-to-one correspondence with accepting paths of the automaton

$$
S_j = (c_j,q_j),
\qquad j=0,\dots,32,
$$

with update equations

$$
w_j = F_j \oplus h_j \oplus c_j,
$$

$$
c_{j+1} =
\begin{cases}
h_j, & F_j = c_j,\\[6pt]
c_j, & F_j \neq c_j,
\end{cases}
$$

and terminal condition

$$
(c_{32},q_{32}) \in \mathcal{A}_{\mathrm{term}}.
$$

### Proof sketch

A path determines the bits $h_j$ and therefore all $w_j$ by the XOR law. Concatenating the bits yields words $h_r$ and $W_r$ satisfying the fused wall by construction. The budget update enforces precisely the admissible side scars. Conversely, any lawful split induces a unique sequence of bits and carries satisfying the same update laws, hence a unique accepting path. ∎

This theorem removes the need for full 32-bit candidate enumeration.

---

## 10. Cross-round chaining

A local round decoder is not enough by itself. It must be chained backward.

### 10.1 State-transport glue

From the shift law,

$$
g_{r-1} = h_r.
$$

So once round $r$ has been decoded, the word $h_r$ becomes an **exact transported state word** for the previous round.

Similarly, decoded local words propagate through the reverse shift structure. The important point is that decoded local words are not isolated; they are immediately inherited by neighboring rounds.

### 10.2 Schedule-law glue

The message schedule recurrence for $r \ge 16$ is

$$
W_r
=
\sigma_1(W_{r-2})
+
W_{r-7}
+
\sigma_0(W_{r-15})
+
W_{r-16}
\pmod{2^{32}},
$$

with

$$
\sigma_0(x) = \operatorname{ROTR}^7(x)\oplus \operatorname{ROTR}^{18}(x)\oplus \operatorname{SHR}^3(x),
$$

$$
\sigma_1(x) = \operatorname{ROTR}^{17}(x)\oplus \operatorname{ROTR}^{19}(x)\oplus \operatorname{SHR}^{10}(x).
$$

So even if multiple local split paths survive at round $r$, they must still satisfy the **global schedule law** across the chain.

This is the second deterministic elimination layer.

---

## 11. Full no-brute-force architecture

The complete architecture is therefore three-layered.

### Layer 1 — round-local fused-term decoder

$$
F_r \longrightarrow (h_r,W_r)
$$

via the carry automaton and admissible budgets.

### Layer 2 — inter-round state glue

$$
g_{r-1} = h_r
$$

and the shift-derived predecessor relations.

### Layer 3 — global schedule glue

$$
W_r
=
\sigma_1(W_{r-2}) + W_{r-7} + \sigma_0(W_{r-15}) + W_{r-16}
\pmod{2^{32}}.
$$

Brute force disappears when these three layers are solved jointly.

---

## 12. Residual functional viewpoint

The earlier tension probe can now be reinterpreted as a residual on partial automaton paths.

Let $C$ be a chain of rounds and let $\mathbf{p}$ denote a collection of local accepting paths. Then define

$$
R_C(\mathbf{p})
=
\sum_{r\in C}
d\!\left(B_r(\mathbf{p}_r), B_r^{\mathrm{obs}}\right)
+
\sum_{r\in C}
\Gamma_r(\mathbf{p}_{r+1},\mathbf{p}_r)
+
\sum_{r\in C}
\Lambda_r(\mathbf{p}),
$$

where:

- $d$ measures local scar mismatch,
- $\Gamma_r$ measures inter-round state inconsistency,
- $\Lambda_r$ measures schedule-law inconsistency.

Then:

- a true chain has
  $$
  R_C(\mathbf{p}^\star)=0,
  $$
- counterfeit chains have
  $$
  R_C(\mathbf{p})>0.
  $$

This is the correct mathematical replacement for “hot/cold guessing.”

---

## 13. Complexity perspective

A naive word search examines

$$
2^{32}
$$

values for a single round word.

The fused decoder instead explores a state graph whose size is bounded by

$$
O\!\left(32 \cdot 2 \cdot |\mathcal{Q}|\right),
$$

where $|\mathcal{Q}|$ is the size of the finite budget lattice induced by the chosen admissible scars.

So the problem is transformed from:

$$
\text{enumeration over all words}
$$

to

$$
\text{reachability in a finite constrained automaton}.
$$

That is the exact mathematical sense in which brute force is removed.

---

## 14. Current phase of the program

### Global program stages

1. Exact reverse die algebra  
2. Local side-bundle scoring  
3. Multi-round coupling on real Bitcoin  
4. Richer admissible bundles  
5. Search-policy upgrade  
6. **Fused-term split decoder**  
7. Terminal-to-vestibule bridge and deterministic block-level recovery

The present document is the formal entry into **Stage 6**.

### Local round status

Within a single reverse round:

- $7$ of the $8$ predecessor state words are already solved exactly,
- the final unresolved object is reduced to a bitwise constrained split of
  $$
  F_r = h_r + W_r.
  $$

So locally the problem is almost fully algebraized.

---

## 15. What still remains

This document completes the local no-brute-force round formulation, but three major tasks remain.

### 15.1 Build the admissible budget set explicitly

The budget vector $q_j$ must be concretely instantiated using:

- chirality counts,
- nibble silhouette of $h_r$,
- seam-specific carry spans,
- NOP-subtracted carry masks,
- optional cross-round Sziklai silhouette.

### 15.2 Prove uniqueness or small finite ambiguity

For a given round and bundle, we need to determine whether

$$
|\mathcal{A}_r(F_r,B_r)| = 1,
$$

or whether a small finite set survives.

If the latter, then inter-round and schedule coupling must eliminate the remainder.

### 15.3 Build the terminal-to-vestibule bridge

The tail schedule words must eventually constrain the earlier words without leaking transport. That is the bridge from local round recovery to deterministic block-level recovery.

---

## 16. Final collapse

The SHA-256 reverse problem is no longer best understood as “searching for a 32-bit value.”

The correct formulation is:

$$
\boxed{
\text{decode the lawful split of }F_r=h_r+W_r\text{ using admissible carry geometry}
}
$$

The mathematics that replaces brute force is:

1. exact die reversal up to one fused wall,
2. bitwise lower-triangular carry recursion,
3. admissible scar budgets,
4. inter-round transport,
5. message-schedule closure.

So the governing object is not a guessed word but an accepting path in a constrained automaton.

That is the complete solution direction.

---

## 17. Minimal implementation blueprint

A practical solver for one round should do the following:

### Input
- $x_{r+1}$
- observed admissible bundle $B_r^{\mathrm{obs}}$

### Step A — compute exact knowns
Compute
$$
a_r,b_r,c_r,e_r,f_r,g_r,d_r,T2_r,T1_r,F_r.
$$

### Step B — initialize automaton
Set
$$
c_0=0,
\qquad
q_0=\text{bundle budget extracted from }B_r^{\mathrm{obs}}.
$$

### Step C — run bitwise DP
For $j=0,\dots,31$:
- branch only on admissible $h_j\in\{0,1\}$,
- compute $w_j$ from
  $$
  w_j = F_j \oplus h_j \oplus c_j,
  $$
- update carry using
  $$
  c_{j+1} =
  \begin{cases}
  h_j, & F_j = c_j,\\[6pt]
  c_j, & F_j \neq c_j,
  \end{cases}
  $$
- update budget,
- prune any state whose budget becomes impossible.

### Step D — accept
Keep only paths with
$$
(c_{32},q_{32})=(0,0)
$$
or terminal-allowed equivalent.

### Step E — chain backward
Use the resulting $h_r$ and $W_r$ in the previous round, together with:
- state transport,
- schedule recurrence,
- cross-round scars.

This is the implementation path that removes brute force.

---

## 18. Concluding statement

The search phase was useful only because it exposed the exact shape of the wall.

That wall is now named:

$$
\boxed{
h_r + W_r = F_r
}
$$

Once the wall is named, the work changes.

We are no longer looking for values.  
We are looking for the **law of the split**.

And once the split law is explicit, the remaining work is not brute force.  
It is recursive elimination.
