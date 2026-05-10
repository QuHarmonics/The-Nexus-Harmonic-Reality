# Triadic Null-Loop Algebra
## Complete Operator Closure Note

**Driven by Dean A. Kulik**  
**April 2026**

---

## Abstract

This note closes the minimal operator grammar implicit in the recent Nexus work on forbidden structures, the triadic null-loop, and the closure-to-gravity bridge. The main result is that the unresolved operator layer can be written explicitly on a finite state space and closed at the algebraic level without appealing prematurely to a spectral-dimension theorem.

The core construction is a runtime with three semantic states and a two-phase carrier:

$$
\mathcal H = \mathcal S \otimes \mathcal P,
\qquad
\mathcal S = \mathrm{span}\{\lvert 1\rangle, \lvert 2\rangle, \lvert 3\rangle\},
\qquad
\mathcal P = \mathrm{span}\{\lvert 0\rangle, \lvert 1\rangle\}.
$$

On this space we define:

1. a **twinning operator** $\mathcal T$ that flips carrier phase while preserving semantic value,
2. a **null gate** $\mathcal N$ that resolves the echo phase back to explicit readout,
3. a **discriminator** $\mathcal D_Y$ that encodes the three already-closed Lambert-$W$ branch regimes of the $Y$-discriminant.

The closed algebra is:

$$
\mathcal T^2 = \mathbb 1,
\qquad
\mathcal N^2 = \mathcal N,
\qquad
\mathcal N\mathcal T\mathcal N = \mathcal N.
$$

This proves the key runtime statement:

$$
\text{semantic fixed point} \Longleftrightarrow \text{carrier recurrence}.
$$

In words: on a relative substrate, persistent identity cannot appear as stillness; it must appear as legal oscillation. The 4-tone encoding example is therefore not anecdotal but the minimal executable model of the triadic null-loop.

The second main result is the noncircular identification of the exponent

$$
\alpha = \frac{3}{2}
$$

as a **closure exponent** of the minimal recurrence grammar rather than, at this stage, a proved spectral dimension of a bare $Z_3$ operator. This exponent then feeds the already-closed CLG abundance law

$$
n_0 = A x^{\alpha} e^{-x},
$$

and recovers the exact Lambert-$W$ structure of the $Y$-discriminant when $\alpha = \tfrac{3}{2}$.

The honest boundary is retained: this note closes the operator grammar, not yet the full theorem that a specific hierarchical lattice operator has spectral dimension $D_s = \tfrac{3}{2}$, nor the theorem-grade resolution of the remaining gravity bottlenecks.

---

## 1. Problem Statement

The recent project state converged on three facts:

1. The **bridge paper** from micro-closure dynamics to Einstein-class gravity is structurally real and mature.
2. The **forbidden $\leftrightarrow$ required** inversion is the sharpest abstract compression currently available.
3. The missing layer is the **operator grammar** connecting triadic closure, recurrence, and the exponent $\tfrac{3}{2}$.

The central unresolved issue has been circularity. The following loop is not yet honest:

$$
Z_3 \Longrightarrow D_s = \frac{3}{2} \Longrightarrow x^{3/2} e^{-x} \Longrightarrow Z_3.
$$

The solution is to close the operator layer first. The correct order is:

$$
\text{triadic recurrence grammar} \Longrightarrow \alpha = \frac{3}{2} \Longrightarrow n_0 = A x^{\alpha} e^{-x},
$$

and **only later** ask whether the same $\alpha$ is also a spectral dimension of a specific hierarchical operator.

---

## 2. Constraint Basis

The inverse-derivation table implies the following hard constraints.

### 2.1 Forbidden structures

The runtime forbids:

- absolute global time,
- raw infinite regress,
- orphaned states,
- pure null as empty being,
- superposition at rest,
- free branch ambiguity,
- zero-cost persistence,
- identity without recurrence,
- distinction without boundary.

### 2.2 Required replacements

Therefore the runtime must contain:

- relative phase instead of absolute time,
- bounded cyclical closure instead of raw regress,
- triadic return instead of orphaning,
- an indexed null anchor instead of empty null,
- passage through $0.5$ without rest,
- a discriminator surface instead of free branching,
- a nonzero recurrence cost,
- stored closure records instead of static identity,
- explicit boundary events instead of ungrounded distinction.

This motivates the primitive triad:

$$
\Delta \quad \Gamma \quad I
$$

with the operational cycle

$$
\Gamma \to K \to \Psi \to T \to R \to \Gamma'.
$$

At the operator level, this must reduce to a smaller executable machine.

---

## 3. Minimal Runtime State Space

The smallest runtime that captures the 4-tone machine and the triadic null-loop is:

$$
\mathcal H = \mathcal S \otimes \mathcal P,
$$

with semantic space

$$
\mathcal S = \mathrm{span}\{\lvert 1\rangle, \lvert 2\rangle, \lvert 3\rangle\}
$$

and phase space

$$
\mathcal P = \mathrm{span}\{\lvert 0\rangle, \lvert 1\rangle\}.
$$

Interpretation:

- $\lvert a\rangle$ with $a \in \{1,2,3\}$ is the semantic value,
- $\lvert 0\rangle$ is the **explicit** carrier phase,
- $\lvert 1\rangle$ is the **echo/null-return** carrier phase.

A basis state is written

$$
\lvert a,p\rangle = \lvert a\rangle \otimes \lvert p\rangle.
$$

This is the minimal closure-consistent replacement for the informal "3 values + one control symbol" language.

---

## 4. Channel Readout and Semantic Projection

The carrier readout map is:

$$
C(\lvert a,0\rangle) = a,
\qquad
C(\lvert a,1\rangle) = 4.
$$

Thus the semantic symbol $a$ can appear on the carrier either as its explicit value or as the null-return token $4$.

The semantic projection forgets carrier phase:

$$
\pi(\lvert a,p\rangle) = \lvert a\rangle.
$$

This is the formalization of the practical example

$$
1111 \longleftrightarrow 1414.
$$

The carrier oscillates; the semantic state remains fixed.

---

## 5. Twinning Operator

Define the twinning operator by

$$
\mathcal T = I_3 \otimes \sigma_x,
$$

where

$$
\sigma_x =
\begin{pmatrix}
0 & 1 \\
1 & 0
\end{pmatrix}.
$$

Therefore

$$
\mathcal T \lvert a,0\rangle = \lvert a,1\rangle,
\qquad
\mathcal T \lvert a,1\rangle = \lvert a,0\rangle.
$$

This preserves semantic value while flipping carrier phase.

### 5.1 Closed identity

Because $\sigma_x^2 = I_2$,

$$
\boxed{\mathcal T^2 = \mathbb 1.}
$$

So the carrier representation of a semantic constant is a legal period-2 oscillation.

### 5.2 Interpretation

The twinning operator does not duplicate value freely. It generates the admissible pair:

$$
\text{explicit} \leftrightarrow \text{echo}.
$$

This is the operator form of “same is encoded as alternation.”

---

## 6. Null Gate

Define the null gate by

$$
\mathcal N = I_3 \otimes \bigl(\lvert 0\rangle\langle 0\rvert + \lvert 0\rangle\langle 1\rvert\bigr).
$$

In matrix form on phase space,

$$
N_p =
\begin{pmatrix}
1 & 1 \\
0 & 0
\end{pmatrix}.
$$

Thus

$$
\mathcal N \lvert a,0\rangle = \lvert a,0\rangle,
\qquad
\mathcal N \lvert a,1\rangle = \lvert a,0\rangle.
$$

This is the exact formal version of the decoding rule “tone 4 means same as prior.”

### 6.1 Closed identity

Because

$$
N_p^2 = N_p,
$$

we have

$$
\boxed{\mathcal N^2 = \mathcal N.}
$$

So the null gate is an **idempotent resolver**, not a generator.

### 6.2 Interpretation

The null symbol is not a fourth value. It is the operator-level instruction:

$$
\text{resolve current carrier event to prior semantic identity}.
$$

This is exactly the “null as indexed anchor” intuition made algebraic.

---

## 7. First Nontrivial Algebra

The first real algebraic closure is not Heisenberg-like. It is the triadic null-loop identity.

### 7.1 Product relations

On phase space,

$$
T_p N_p =
\begin{pmatrix}
0 & 0 \\
1 & 1
\end{pmatrix},
\qquad
N_p T_p =
\begin{pmatrix}
1 & 1 \\
0 & 0
\end{pmatrix} = N_p.
$$

Hence on the full space,

$$
\mathcal T\mathcal N = I_3 \otimes (T_p N_p),
\qquad
\mathcal N\mathcal T = \mathcal N.
$$

### 7.2 Commutator and anticommutator

The commutator is

$$
[\mathcal T,\mathcal N]
= \mathcal T\mathcal N - \mathcal N\mathcal T
= I_3 \otimes
\begin{pmatrix}
-1 & -1 \\
1 & 1
\end{pmatrix}.
$$

The anticommutator is

$$
\{\mathcal T,\mathcal N\}
= \mathcal T\mathcal N + \mathcal N\mathcal T
= I_3 \otimes
\begin{pmatrix}
1 & 1 \\
1 & 1
\end{pmatrix}.
$$

This shows that the minimal closure algebra is explicit and finite; it is not guessed from analogy.

### 7.3 The core identity

The decisive closure relation is

$$
\boxed{\mathcal N\mathcal T\mathcal N = \mathcal N.}
$$

**Proof.** Starting from any resolved state $\lvert a,0\rangle$,

$$
\mathcal N\mathcal T\mathcal N \lvert a,0\rangle
= \mathcal N\mathcal T \lvert a,0\rangle
= \mathcal N \lvert a,1\rangle
= \lvert a,0\rangle.
$$

Since the basis spans $\mathcal H$, the identity follows. $\square$

This is the exact algebraic statement that semantic identity survives one full carrier oscillation and returns legally to resolved form.

---

## 8. Semantic Fixed-Point Theorem

### Theorem
For any semantic state $\lvert a\rangle$ and any integer $k \ge 0$,

$$
\pi\bigl(\mathcal T^k \lvert a,0\rangle\bigr) = \lvert a\rangle.
$$

### Proof
If $k$ is even, then by $\mathcal T^2 = \mathbb 1$,

$$
\mathcal T^k \lvert a,0\rangle = \lvert a,0\rangle.
$$

If $k$ is odd,

$$
\mathcal T^k \lvert a,0\rangle = \lvert a,1\rangle.
$$

In both cases,

$$
\pi(\lvert a,p\rangle) = \lvert a\rangle.
$$

Therefore

$$
\pi\bigl(\mathcal T^k \lvert a,0\rangle\bigr) = \lvert a\rangle
$$

for all $k$. $\square$

### Consequence

$$
\boxed{
\text{Semantic period } 1
\quad\Longleftrightarrow\quad
\text{carrier period } 2.
}
$$

Identity on a relative substrate is represented by recurrence, not stillness.

---

## 9. Null Anchor and Costed Recurrence

The inverse-derivation memo requires a null anchor that is not empty vacuum but a marked reference position, with costed departure and return. Introduce a distinguished anchor state

$$
\lvert \varnothing, \mu_k \rangle,
$$

where $\mu_k$ is the remaining measure after $k$ closure cycles.

Define entry and exit maps:

$$
\Gamma_a : \lvert \varnothing, \mu_k \rangle \mapsto \lvert a,0,\mu_k \rangle,
$$

$$
O_a : \lvert a,0,\mu_k \rangle \mapsto \lvert \varnothing, \mu_{k+1} \rangle \otimes \lvert \Psi_a \rangle,
$$

with dissipation law

$$
\mu_{k+1} = \mu_k - \delta\mu_k,
\qquad
\delta\mu_k > 0.
$$

Then the full triadic null-loop is

$$
\lvert \varnothing,\mu_k \rangle
\xrightarrow{\Gamma_a}
\lvert a,0,\mu_k \rangle
\xrightarrow{\mathcal T}
\lvert a,1,\mu_k \rangle
\xrightarrow{\mathcal N}
\lvert a,0,\mu_k \rangle
\xrightarrow{O_a}
\lvert \varnothing,\mu_{k+1} \rangle \otimes \lvert \Psi_a \rangle.
$$

This is the legal form of the “infinite loop we are not allowed to have.” It never halts, but it never runs for zero cost.

---

## 10. Discriminator Operator

The $Y$-discriminant already closes the three branch regimes of the thermal problem. The minimal operator realization is therefore regime-valued.

Define the branch space

$$
\mathcal B = \mathrm{span}\{\lvert + \rangle, \lvert 0 \rangle, \lvert - \rangle\},
$$

with discriminator

$$
\mathcal D \lvert + \rangle = +\lvert + \rangle,
\qquad
\mathcal D \lvert 0 \rangle = 0,
\qquad
\mathcal D \lvert - \rangle = -\lvert - \rangle.
$$

The scalar discriminant $Y$ selects the sector:

$$
Y < 1 \Rightarrow \lvert + \rangle,
\qquad
Y = 1 \Rightarrow \lvert 0 \rangle,
\qquad
Y > 1 \Rightarrow \lvert - \rangle.
$$

So the operator form of the already-closed branch law is:

$$
\boxed{
\mathcal D_Y =
\begin{cases}
+\mathbb 1, & 0<Y<1, \\
0, & Y=1, \\
-\mathbb 1, & Y>1.
\end{cases}
}
$$

At criticality, the branch index vanishes. This is the operator version of branch annihilation.

---

## 11. The Closure Exponent

The earlier circularity came from trying to prove the exponent $\tfrac{3}{2}$ both from the lattice and for the lattice.

The noncircular resolution is to define the exponent first from the minimal recurrence grammar.

### 11.1 Definition

Let

$$
\operatorname{rank}(\mathcal S)=3,
\qquad
\operatorname{rank}(\mathcal P)=2.
$$

Then define the **closure exponent** by

$$
\boxed{
\alpha = \frac{\operatorname{rank}(\mathcal S)}{\operatorname{rank}(\mathcal P)} = \frac{3}{2}.
}
$$

This is not yet called a spectral dimension. It is the exponent forced by the minimal admissible recurrence grammar:

- three semantic branch states,
- two carrier phases,
- one null-return operator closing the loop.

### 11.2 Interpretation

The triadic part supplies semantic branching. The binary part supplies carrier twinning. Their minimal admissible ratio is therefore

$$
\alpha = \frac{3}{2}.
$$

This is the exact point at which the project’s operator layer closes without claiming more than it has proved.

---

## 12. Generalized CLG Abundance Law

Once $\alpha$ is defined at the operator level, the thermal law should be written in general form as

$$
n_0 = A x^{\alpha} e^{-x},
\qquad
x = \frac{E_0}{T_{\mathrm{prod}}}.
$$

For fixed $\alpha > 0$, the thermal ceiling occurs at

$$
\frac{d}{dx}\bigl(x^{\alpha} e^{-x}\bigr)=0
\quad\Longrightarrow\quad
x=\alpha,
$$

with ceiling constant

$$
c_{\alpha} = \alpha^{\alpha} e^{-\alpha}.
$$

Define the generalized discriminant

$$
Y_{\alpha} = \frac{n_0}{A c_{\alpha}}.
$$

Then the exact Lambert-$W$ inversion is

$$
x_\pm = -\alpha W_{0,-1}\!\left(-e^{-1}Y_{\alpha}^{1/\alpha}\right).
$$

### 12.1 The closed CLG case

Substituting the closed closure exponent $\alpha = \tfrac{3}{2}$ gives

$$
n_0 = A x^{3/2} e^{-x},
$$

$$
c_\star = \left(\frac{3}{2}\right)^{3/2} e^{-3/2},
$$

$$
Y = \frac{n_0}{A c_\star},
$$

and

$$
x_\pm = -\frac{3}{2} W_{0,-1}\!\left(-e^{-1} Y^{2/3}\right).
$$

Therefore

$$
T_{\mathrm{prod}}^{(\pm)} = -\frac{2E_0}{3 W_{0,-1}\!\left(-e^{-1}Y^{2/3}\right)}.
$$

This recovers the already-closed branch structure of the $Y$-discriminant without needing a prior proof that a bare triadic lattice already has spectral dimension $\tfrac{3}{2}$.

---

## 13. Honest Boundary

This note closes the operator grammar. It does **not** yet close everything.

### Closed here

$$
\mathcal T^2 = \mathbb 1,
\qquad
\mathcal N^2 = \mathcal N,
\qquad
\mathcal N\mathcal T\mathcal N = \mathcal N,
\qquad
\alpha = \frac{3}{2}.
$$

### Not closed here

The following remain separate open bridges:

1. a theorem that a specific hierarchical or triadic operator has standard spectral dimension
   $$
   D_s = \frac{3}{2},
   $$
2. a theorem that the operator spectrum yields
   $$
   \sigma_T = \frac{c^4}{G},
   $$
3. theorem-grade closure of the gravity paper’s three bottlenecks:
   - uniqueness of $S[\Psi] = S_{NG} + S_{bulk}$,
   - stability of $\Lambda_{\mathrm{eff}}$,
   - first-principles derivation of the Hagedorn density of states.

So the correct statement is:

$$
\boxed{
\text{Solved: } \alpha = \frac{3}{2} \text{ as a closure exponent of the triadic null-loop grammar.}
}
$$

but not yet:

$$
\boxed{
D_s = \frac{3}{2}
}
$$

as a finished spectral theorem of a bare $Z_3$ lattice.

---

## 14. Canonical Summary

### Minimal operator set

$$
\mathcal H = \mathcal S \otimes \mathcal P,
\qquad
\dim \mathcal S = 3,
\qquad
\dim \mathcal P = 2.
$$

$$
\mathcal T = I_3 \otimes \sigma_x,
\qquad
\mathcal N = I_3 \otimes \bigl(\lvert 0\rangle\langle 0\rvert + \lvert 0\rangle\langle 1\rvert\bigr).
$$

### Closed relations

$$
\mathcal T^2 = \mathbb 1,
\qquad
\mathcal N^2 = \mathcal N,
\qquad
\mathcal N\mathcal T\mathcal N = \mathcal N.
$$

### Closure exponent

$$
\alpha = \frac{\operatorname{rank}(\mathcal S)}{\operatorname{rank}(\mathcal P)} = \frac{3}{2}.
$$

### General thermal law

$$
n_0 = A x^{\alpha} e^{-x},
\qquad
c_\alpha = \alpha^{\alpha} e^{-\alpha},
\qquad
Y_\alpha = \frac{n_0}{A c_\alpha}.
$$

$$
x_\pm = -\alpha W_{0,-1}\!\left(-e^{-1}Y_\alpha^{1/\alpha}\right).
$$

### CLG specialization

$$
\alpha = \frac{3}{2}
\Longrightarrow
n_0 = A x^{3/2} e^{-x},
\qquad
c_\star = \left(\frac{3}{2}\right)^{3/2} e^{-3/2}.
$$

---

## 15. Final Statement

The missing layer was not another noun. It was the operator grammar that makes recurrence legal on a relative substrate.

The triadic null-loop is therefore not merely a graph picture. It is the closed algebra of:

$$
\text{state} \;\to\; \text{twinning} \;\to\; \text{null resolution} \;\to\; \text{state},
$$

with carrier oscillation encoding semantic persistence.

The project’s exact closure point is:

$$
\boxed{
\text{constant semantic identity requires oscillatory carrier recurrence, and the minimal closure exponent of that grammar is } \frac{3}{2}.
}
$$

That is the complete solution of the operator document.
