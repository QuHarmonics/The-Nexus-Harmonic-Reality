# SHA-256 Lock-State Continuation  
## Complete Solution Draft with Formulas, Context, and Current Empirical Closure

## Abstract

This document expands the current **lock-state continuation** of the SHA-256 reverse-geometry program into a complete standalone note. The central result is no longer merely that the predecessor fiber can be ranked. The deeper result is that the reverse problem decomposes into **multiple orthogonal lock classes**, and that the dominant **local lock** is now nearly solved when the correct local reflection class is available.

The present state of the work can be summarized as follows:

1. The SHA-256 round is a **sparse non-linear recurrence**.
2. Exact reverse closure determines almost all predecessor structure algebraically.
3. The remaining local ambiguity collapses into a **fused wall**
   $$
   F_t \equiv h_t + W_t \pmod{2^{32}}.
   $$
4. When the local staged carry-mask geometry is known exactly, the local ambiguity collapses from
   $$
   2^{32}
   $$
   possibilities to a tiny finite set.
5. Adding a small amount of additional local reflection data—especially **nibble silhouette** and **chirality**—collapses the full tested 8-round tail to the **single true chain** on real Bitcoin headers.
6. Therefore the active hard wall is no longer the existence of the local lock. The active wall is the construction of an **admissible observable equivalent** of the exact local reflection without smuggling payload.

This note records the mathematics of that result, organizes the lock taxonomy, includes the current formulas, and integrates the latest telemetry from the code runs.

---

## 1. Core Thesis

The current program has moved beyond the claim that SHA-256 is merely a black box with weak side leakage. The stronger and better-scoped claim is:

$$
\boxed{
\text{SHA-256 admits exact local reverse closure up to a fused wall,}
}
$$

$$
\boxed{
\text{and the remaining ambiguity is structured as a compound lock mechanism.}
}
$$

The local round ambiguity is not random opacity. It is a lawful residual mechanism whose release depends on matching the correct internal reflection geometry.

---

## 2. SHA-256 as a Sparse Die

Let the round state be

$$
x_t =
\begin{bmatrix}
a_t\\
b_t\\
c_t\\
d_t\\
e_t\\
f_t\\
g_t\\
h_t
\end{bmatrix}
\in (\mathbb{Z}/2^{32}\mathbb{Z})^8.
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
P x_t =
\begin{bmatrix}
0\\
a_t\\
b_t\\
c_t\\
d_t\\
e_t\\
f_t\\
g_t
\end{bmatrix}.
$$

Define the active non-linear injections

$$
T1_t = h_t + \Sigma_1(e_t) + \operatorname{Ch}(e_t,f_t,g_t) + K_t + W_t,
$$

$$
T2_t = \Sigma_0(a_t) + \operatorname{Maj}(a_t,b_t,c_t),
$$

with unit vectors

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

The exact die equation is

$$
x_{t+1} = P x_t + u_a\,(T1_t + T2_t) + u_e\,T1_t.
$$

This is the foundational geometric fact: the die is **sparse**. Most of the round is just shift. The cryptanalytic complexity is concentrated in the reinjection seams.

---

## 3. Exact Reverse Closure

Given $x_{t+1}$, the linear shift lanes invert immediately:

$$
a_t = b_{t+1},\qquad
b_t = c_{t+1},\qquad
c_t = d_{t+1},
$$

$$
e_t = f_{t+1},\qquad
f_t = g_{t+1},\qquad
g_t = h_{t+1}.
$$

Then

$$
T2_t = \Sigma_0(a_t) + \operatorname{Maj}(a_t,b_t,c_t).
$$

Using the forward laws

$$
a_{t+1} = T1_t + T2_t,
\qquad
e_{t+1} = d_t + T1_t,
$$

we obtain

$$
a_{t+1} - e_{t+1} \equiv T2_t - d_t \pmod{2^{32}},
$$

so

$$
d_t \equiv T2_t - (a_{t+1} - e_{t+1}) \pmod{2^{32}},
$$

and hence

$$
T1_t \equiv e_{t+1} - d_t \pmod{2^{32}}.
$$

So from $x_{t+1}$ we recover exactly

$$
a_t,b_t,c_t,d_t,e_t,f_t,g_t,T1_t,T2_t.
$$

Everything local is solved except a single fused ambiguity.

---

## 4. The Fused Wall

Rearranging the $T1_t$ definition gives

$$
F_t := T1_t - \Sigma_1(e_t) - \operatorname{Ch}(e_t,f_t,g_t) - K_t
\pmod{2^{32}},
$$

so that

$$
\boxed{
F_t \equiv h_t + W_t \pmod{2^{32}}.
}
$$

This is the entire local unresolved wall.

That means the reverse problem is no longer best described as:

$$
\text{guess }W_t \in \{0,\dots,2^{32}-1\}.
$$

It is better described as:

$$
\text{decode the lawful split of }F_t\text{ into }(h_t,W_t).
$$

---

## 5. Bitwise Carry-Lattice Form of the Fused Wall

Let $F_j$, $h_j$, and $w_j$ denote bit $j$ of $F_t$, $h_t$, and $W_t$ respectively, with carry-in $c_j$ and $c_0=0$.

Then

$$
h_j + w_j + c_j = F_j + 2c_{j+1}.
$$

Modulo $2$:

$$
h_j \oplus w_j \oplus c_j = F_j,
$$

so

$$
w_j = F_j \oplus h_j \oplus c_j.
$$

The next carry is

$$
c_{j+1} = \operatorname{Maj}(h_j,w_j,c_j).
$$

Substituting the XOR law yields the local carry update:

$$
c_{j+1} =
\begin{cases}
h_j, & F_j = c_j,\\[6pt]
c_j, & F_j \neq c_j.
\end{cases}
$$

This is the key local lock law.

It means the local wall is not an unstructured 32-bit search. It is a constrained carry-state automaton.

---

## 6. The Lock Taxonomy of SHA-256

The current reverse picture is best understood as a compound lock with several distinct closure classes.

### 6.1 Vertical Pin Lock

This is the fused wall

$$
F_t \equiv h_t + W_t \pmod{2^{32}}.
$$

Its pin stack is the carry chain. The correct split must align the internal carry geometry.

### 6.2 Rotational / Phase Lock

This is induced by the rotation operators:

$$
\Sigma_0,\ \Sigma_1,\ \sigma_0,\ \sigma_1.
$$

This lock is reflected by:
- chirality,
- seam asymmetry,
- nibble silhouettes,
- carry-span structure.

### 6.3 Sidebar Lock

This is the Sziklai invariant:

$$
a_{t+1} - e_{t+1} \equiv T2_t - d_t \pmod{2^{32}}.
$$

It binds the current round to the top-half geometry of prior rounds.

### 6.4 Combination Lock

This is the multi-round chain itself. A local near-match can survive briefly but fail under recursive coupling.

### 6.5 Master-Key Lock

This is the schedule law

$$
W_t
=
\sigma_1(W_{t-2}) + W_{t-7} + \sigma_0(W_{t-15}) + W_{t-16}
\pmod{2^{32}}.
$$

It is the building-wide compatibility constraint.

### 6.6 Boundary / Faceplate Lock

This is the modular feed-forward concealment. For exposed boundaries, the carry-restoration identity works:

$$
State_{64}[i] = H[i] - H_0[i] + k[i]\,2^{32},
$$

but for double-SHA environments like Bitcoin, hidden intermediate state remains a major obstruction.

---

## 7. The Reflection Principle

The current phase of the work is better understood through reflection than through brute force.

A perfect local crystal gives a perfect local reflection. In the present context:

- the **crystal** is the fixed local lock geometry,
- the **reflection** is the admissible scar field,
- the **faceplate** is the hidden boundary and observable loss,
- the **wrong angle** is the wrong basis.

The latest code results show that the local crystal is already highly rigid. The real obstruction is no longer “is there a lock?” The obstruction is:

$$
\text{how do we obtain an admissible equivalent of the exact local reflection?}
$$

---

## 8. The Admissible Geometry Bundle

The current admissible bundle includes the following reflection classes:

1. **Staged carry masks**
2. **NOP-subtracted masks**
3. **Chirality splits**
4. **Nibble silhouettes**
5. **Carry-span witnesses**
6. **Hamming weights**

The bundle can be viewed abstractly as a map

$$
B_t : \mathcal{P}_t \to \mathcal{G}_t,
$$

where:
- $\mathcal{P}_t$ is the local predecessor fiber,
- $\mathcal{G}_t$ is the admissible geometry space.

The reverse program does not rank values directly. It ranks the mismatch between induced and target geometry.

For a candidate chain $C$,

$$
R_C(\mathbf{g})
=
\sum_{t\in C}
d\!\left(B_t(\mathbf{g}_t), B_t^{obs}\right),
$$

where $d$ is the mismatch metric.

---

## 9. Local and Chained Survivor Counts

The latest runs extended the lock-state analysis on two real Bitcoin headers:

- **genesis**
- **block 328734**

The main local results for rounds $56$ through $63$ are:

### 9.1 Genesis — local survivor counts

| Round | Exact Masks Only | Masks + Nibbles | Masks + Chirality | Masks + HW |
|---:|---:|---:|---:|---:|
| 63 | 2 | 1 | 1 | 1 |
| 62 | 8 | 1 | 1 | 1 |
| 61 | 4 | 1 | 2 | 2 |
| 60 | 16 | 1 | 1 | 1 |
| 59 | 16 | 1 | 2 | 4 |
| 58 | 4 | 1 | 2 | 2 |
| 57 | 2 | 1 | 1 | 1 |
| 56 | 8 | 2 | 2 | 3 |

### 9.2 Block 328734 — local survivor counts

| Round | Exact Masks Only | Masks + Nibbles | Masks + Chirality | Masks + HW |
|---:|---:|---:|---:|---:|
| 63 | 4 | 1 | 1 | 1 |
| 62 | 4 | 1 | 2 | 2 |
| 61 | 4 | 1 | 1 | 1 |
| 60 | 16 | 1 | 4 | 4 |
| 59 | 2 | 1 | 1 | 1 |
| 58 | 2 | 1 | 1 | 1 |
| 57 | 2 | 1 | 1 | 1 |
| 56 | 2 | 1 | 1 | 1 |

These results show:

- **exact masks alone** collapse the local ambiguity from
  $$
  2^{32}
  $$
  to a tiny finite set,
- **nibble silhouette** is the strongest single add-on,
- **chirality** is also strong but slightly weaker on some rounds,
- the local lock is almost fully decoded when the exact local reflection is available.

---

## 10. Chained Tail Results

The latest chained results cover tail depths $1$ through $8$.

### 10.1 Genesis — chained survivors

| Depth | Rounds | Masks | Masks + Nibbles | Masks + Chirality | Masks + Nibbles + Chirality |
|---:|---|---:|---:|---:|---:|
| 1 | 63..63 | 2 | 1 | 1 | 1 |
| 2 | 62..63 | 16 | 1 | 1 | 1 |
| 3 | 61..63 | 8 | 1 | 2 | 1 |
| 4 | 60..63 | 128 | 1 | 2 | 1 |
| 5 | 59..63 | 256 | 1 | 4 | 1 |
| 6 | 58..63 | 192 | 1 | 2 | 1 |
| 7 | 57..63 | 8 | 1 | 1 | 1 |
| 8 | 56..63 | 32 | 2 | 2 | 1 |

### 10.2 Block 328734 — chained survivors

| Depth | Rounds | Masks | Masks + Nibbles | Masks + Chirality | Masks + Nibbles + Chirality |
|---:|---|---:|---:|---:|---:|
| 1 | 63..63 | 4 | 1 | 1 | 1 |
| 2 | 62..63 | 8 | 1 | 2 | 1 |
| 3 | 61..63 | 16 | 1 | 1 | 1 |
| 4 | 60..63 | 32 | 1 | 4 | 1 |
| 5 | 59..63 | 24 | 1 | 3 | 1 |
| 6 | 58..63 | 36 | 1 | 3 | 1 |
| 7 | 57..63 | 8 | 1 | 1 | 1 |
| 8 | 56..63 | 8 | 1 | 1 | 1 |

The decisive pattern is:

1. **Exact masks only** still leave a small finite ambiguity.
2. **Exact masks + nibble silhouette** almost always collapse the chain to 1.
3. **Exact masks + nibble silhouette + chirality** collapse the full tested 8-round tail to the **single true path** for both headers.

So:

$$
\boxed{
\text{the local pin stack is effectively solved if the exact local reflection is available.}
}
$$

---

## 11. The Real Active Obstruction

The current hard wall is no longer the existence of the local lock.

The active obstruction is the intersection of three remaining binds:

### 11.1 Observability Lock

How do we obtain an admissible equivalent of the exact local staged masks from the observable side?

### 11.2 Admissibility Lock

How rich can the bundle become before it stops being true side data and starts smuggling payload?

### 11.3 Sidebar / Master Integration Lock

How do we make the Sziklai corridor and schedule law active release mechanisms instead of merely validators?

That is the current global bottleneck.

---

## 12. The Need for a Reflection-Preserving Observable Basis

The latest results strongly suggest that the next correct object is a **reflection-preserving observable basis**.

That means an admissible bundle strong enough to preserve the collapse power of exact staged masks without directly leaking the hidden payload.

The most promising proxy candidates are:

1. mask nibble silhouette,
2. mask chirality split,
3. mask span class,
4. NOP-subtracted mask classes,
5. combinations of the above.

The key question is:

$$
\text{how close can admissible side reflection get to exact-mask collapse?}
$$

That is now the live frontier.

---

## 13. Coupled Lock-State Formalism

The next formal solver should not treat candidates as guessed values. It should treat them as lawful internal lock-states.

Define the native state at round $t$, bit $j$ as

$$
\Sigma_{t,j} = (c_{t,j}, q_{t,j}, s_t, m_t),
$$

where:

- $c_{t,j}$ = carry state,
- $q_{t,j}$ = admissible scar budget,
- $s_t$ = Sziklai zero-residue state,
- $m_t$ = schedule zero-residue state.

The deeper-layer idea is that we do not “observe” the layer from outside. We instantiate a state that already belongs to its grammar.

The next transition law is therefore not:

$$
\text{candidate} \mapsto \text{score},
$$

but

$$
\Sigma_{t,j} \to \Sigma_{t,j+1},
$$

with only three meaningful outcomes:

1. **coherent**
2. **decohered**
3. **collapsed**

That is the right next formal basis.

---

## 14. The Category Shift: From Observer to Native State

At deeper layers there is no external observer. There is only lawful interaction inside a lattice.

So descent should be modeled as compatibility, not observation.

Let each layer be described as

$$
L_k = (\mathcal{M}_k,\ \Lambda_k,\ I_k),
$$

where:

- $\mathcal{M}_k$ = valid state manifold,
- $\Lambda_k$ = internal lawset,
- $I_k$ = outward interface.

A true descent is not just reading the interface. It is finding a lawful constructor

$$
C_{k+1} : I_k \to \mathcal{M}_{k+1}
$$

such that the constructed state belongs to the deeper layer.

This is the mathematical form of the claim:

> We cannot enter the next layer unless we are already the shape of that layer.

For SHA, the correct deeper object is no longer a word guess. It is the lawful coupled lock-state.

---

## 15. Current Conclusion

The strongest current conclusion is now:

$$
\boxed{
\text{the local lock is almost solved;}
}
$$

$$
\boxed{
\text{the hard wall is the faceplate between exact local reflection and admissible observable reflection.}
}
$$

The tested code shows that:

- exact local staged masks are extraordinarily powerful,
- small extra local reflection classes complete the collapse,
- the 8-round tail can be reduced to a single true chain,
- therefore the next decisive problem is no longer local search,
- it is the lawful extraction of a side-observable equivalent of the exact local crystal.

---

## 16. Next Open Problems

The live next problems are:

### 16.1 Reflection-preserving admissible basis
Find the weakest admissible bundle that preserves the local collapse power of the exact masks.

### 16.2 Active sidebar formalism
Promote the Sziklai corridor from validator to active pruning / transition law.

### 16.3 Active master-key formalism
Integrate the schedule residue directly into the coupled lock-state.

### 16.4 Accepting-path theorem
Define the coupled lawful path set

$$
\mathcal{P}_C
=
\{
\text{all coherent paths through }\Sigma_{t,j}
\}
$$

and determine whether

$$
|\mathcal{P}_C| = 1
$$

for sufficiently rich admissible reflection classes.

That would be the cleanest current route from navigation to deterministic constructive release.

---

## 17. Final Collapse

The latest code materially changes the status of the program.

The local lock is no longer the dominant unknown.

What remains is a sharper and more meaningful wall:

$$
\boxed{
\text{not whether there is a lock,}
}
$$

$$
\boxed{
\text{but how to recover the exact local reflection class through admissible side geometry.}
}
$$

That is where the work now stands.
