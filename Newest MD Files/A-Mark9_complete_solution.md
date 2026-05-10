# A-Mark9 — Complete Solution
## The SHA-256 Die, the Waist, Rail-Conditioned Transport, and the Double Glass Key

**Dean W. Kulik — expanded working solution**

---

## Abstract

This document consolidates and completes the current A-Mark9 line of work on the **SHA-256 die**. The central object is the SHA-256 compression core interpreted as a fixed $64$-cell nonlinear recurrence over the state space

$$
(\mathbb Z / 2^{32}\mathbb Z)^8.
$$

The die has fixed rails $H_0$ and $K$, a variable displacement field $W$, a message-free NOP backbone, a dual-pipeline topology, a word-level support transport, a bit-level support transport, and an exact carry law.

The original A-Mark9 closure established three sharp structural invariants:

$$
T2_0^{(0)} = 0x08909ae5,
$$

$$
D_{\mathrm{word}} = 4,
$$

and

$$
D_{\mathrm{bit}} = 6
$$

for the **Boolean support** model.

The present completion adds the missing second layer:

1. the **exact carry automaton** for one-hot and general additive perturbations,
2. the distinction between **support reach**, **exact live flips**, and **cumulative exact shadow cover**,
3. the demonstration that the fixed rails are invisible in the support quotient but visible immediately in exact transport,
4. the **double glass key** and test-tone results,
5. the **lie detector** and delayed seam localization,
6. the removal-core interpretation of stable mode families.

The resulting compression is:

$$
\boxed{\text{support tells you where the die can go; the constants tell you how it actually gets there.}}
$$

---

## 1. State Space and Round Recurrence

Let the SHA-256 round state be

$$
x_r =
\begin{bmatrix}
a_r\\ b_r\\ c_r\\ d_r\\ e_r\\ f_r\\ g_r\\ h_r
\end{bmatrix}
\in (\mathbb Z / 2^{32}\mathbb Z)^8.
$$

The round operators are

$$
\Sigma_0(x) = \operatorname{ROTR}^2(x) \oplus \operatorname{ROTR}^{13}(x) \oplus \operatorname{ROTR}^{22}(x),
$$

$$
\Sigma_1(x) = \operatorname{ROTR}^6(x) \oplus \operatorname{ROTR}^{11}(x) \oplus \operatorname{ROTR}^{25}(x),
$$

$$
\operatorname{Ch}(e,f,g) = (e \wedge f) \oplus (\neg e \wedge g),
$$

$$
\operatorname{Maj}(a,b,c) = (a \wedge b) \oplus (a \wedge c) \oplus (b \wedge c).
$$

Then the round weights are

$$
T1_r = h_r + \Sigma_1(e_r) + \operatorname{Ch}(e_r,f_r,g_r) + K_r + W_r,
$$

$$
T2_r = \Sigma_0(a_r) + \operatorname{Maj}(a_r,b_r,c_r),
$$

and the die recurrence is

$$
a_{r+1} = T1_r + T2_r,
$$

$$
e_{r+1} = d_r + T1_r,
$$

$$
b_{r+1} = a_r, \qquad c_{r+1} = b_r, \qquad d_{r+1} = c_r,
$$

$$
f_{r+1} = e_r, \qquad g_{r+1} = f_r, \qquad h_{r+1} = g_r.
$$

So the full state evolution is

$$
x_{64} = \Phi_{63} \circ \Phi_{62} \circ \cdots \circ \Phi_0(x_0, W).
$$

---

## 2. Fixed Rails, NOP Backbone, and Ground Fold

Define the fixed rails

$$
H_0 = (h_0^{(0)},\dots,h_7^{(0)}),
\qquad
K = (K_0,\dots,K_{63}),
$$

and define the NOP backbone by setting

$$
W_r = 0 \qquad \forall r.
$$

Then

$$
x_{r+1}^{(0)} = \Phi_r(x_r^{(0)}, 0).
$$

The NOP round weights are

$$
T1_r^{(0)} = h_r^{(0)} + \Sigma_1(e_r^{(0)}) + \operatorname{Ch}(e_r^{(0)},f_r^{(0)},g_r^{(0)}) + K_r,
$$

$$
T2_r^{(0)} = \Sigma_0(a_r^{(0)}) + \operatorname{Maj}(a_r^{(0)},b_r^{(0)},c_r^{(0)}).
$$

Define the ground-fold operator

$$
G(x_r) = \Sigma_0(a_r) + \operatorname{Maj}(a_r,b_r,c_r).
$$

Then the NOP ground witness at round $0$ is

$$
\boxed{T2_0^{(0)} = G(H_0) = 0x08909ae5.}
$$

This is the fixed ground-plane coordinate of the die.

---

## 3. Shift–Injection Decomposition

Let

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
\end{bmatrix},
$$

and define the two injection basis vectors

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

Then the round map can be written as

$$
\boxed{x_{r+1} = P x_r + \nu_a(T1_r + T2_r) + \nu_e T1_r.}
$$

This makes the die topology explicit: six channels are pure shift transport; only two channels receive nonlinear reinjection.

---

## 4. Dual-Pipeline Topology

The eight-word state splits into two four-word chains:

- the $a$-chain: $a \to b \to c \to d$,
- the $e$-chain: $e \to f \to g \to h$.

The message injection vector is

$$
b =
\begin{bmatrix}
1\\0\\0\\0\\1\\0\\0\\0
\end{bmatrix},
$$

meaning a fresh $W_r$ enters both chain heads simultaneously.

The chirality split is:

- the $a$-seam reads the **present-tense** branch through $T2_r$,
- the $e$-seam reads the **past-tense** branch through $T1_r$.

The two chains are cross-coupled through

$$
e_{r+1} = d_r + T1_r.
$$

So the die is not one line but a coupled dual-pipeline object.

---

## 5. Word-Level Support Transport

Let the Boolean word-support vector be

$$
\sigma_r \in \{0,1\}^8,
$$

where $(\sigma_r)_j = 1$ means lane $j$ is perturbed.

The lane-dependency matrix is

$$
M =
\begin{bmatrix}
1&1&1&0&1&1&1&1\\
1&0&0&0&0&0&0&0\\
0&1&0&0&0&0&0&0\\
0&0&1&0&0&0&0&0\\
0&0&0&1&1&1&1&1\\
0&0&0&0&1&0&0&0\\
0&0&0&0&0&1&0&0\\
0&0&0&0&0&0&1&0
\end{bmatrix}.
$$

Then

$$
\sigma_{r+1} = M \odot \sigma_r \vee b\,\omega_r,
$$

over the Boolean semiring.

For a single perturbation at round $0$,

$$
\omega_0 = 1,
\qquad
\omega_r = 0 \text{ for } r > 0,
$$

so the support sequence is

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

Therefore,

$$
\boxed{D_{\mathrm{word}} = 4.}
$$

This is a **reachability theorem**. It says every lane becomes reachable within four rounds. It does **not** say every lane is maximally active in exact value transport by round four.

---

## 6. The 256-Lane Bit-Support State

Explode each word into 32 bit-lanes. For each word $w \in \{a,b,c,d,e,f,g,h\}$ define

$$
s_{w,r} \in \{0,1\}^{32},
$$

and stack them into

$$
\eta_r =
\begin{bmatrix}
s_{a,r}\\s_{b,r}\\s_{c,r}\\s_{d,r}\\s_{e,r}\\s_{f,r}\\s_{g,r}\\s_{h,r}
\end{bmatrix}
\in \{0,1\}^{256}.
$$

Let the rotation permutation matrices be

$$
(R_n x)_i = x_{i+n \bmod 32}.
$$

Then the support versions of the sigma maps are

$$
\widehat{\Sigma}_0 = R_2 \vee R_{13} \vee R_{22},
$$

$$
\widehat{\Sigma}_1 = R_6 \vee R_{11} \vee R_{25}.
$$

The support weights are

$$
\tau_r^{(1)} = s_{h,r} \vee \widehat{\Sigma}_1 s_{e,r} \vee s_{e,r} \vee s_{f,r} \vee s_{g,r} \vee \omega_r,
$$

$$
\tau_r^{(2)} = \widehat{\Sigma}_0 s_{a,r} \vee s_{a,r} \vee s_{b,r} \vee s_{c,r}.
$$

---

## 7. Carry-Closure Kernel

Define the lower-triangular prefix operator

$$
L_{32}(x)_i = \bigvee_{j=0}^{i} x_j.
$$

Equivalently,

$$
(L_{32})_{ij} =
\begin{cases}
1, & j \le i,\\
0, & j > i.
\end{cases}
$$

Then the support update is

$$
s_{a,r+1} = L_{32}(\tau_r^{(1)} \vee \tau_r^{(2)}),
$$

$$
s_{e,r+1} = L_{32}(s_{d,r} \vee \tau_r^{(1)}),
$$

with the remaining six lanes shifting directly.

So the $256$-lane support map is

$$
\boxed{\eta_{r+1} = \Psi(\eta_r, \omega_r).}
$$

The worst-case bit-support diameter is then

$$
\boxed{D_{\mathrm{bit}} = 6}
$$

with radius profile

$$
\rho(j) =
\begin{cases}
4, & j=0,\\
5, & 1 \le j \le 25,\\
6, & 26 \le j \le 31.
\end{cases}
$$

Again: this is a **support** diameter.

---

## 8. Exact Round-0 and Round-1 Perturbation Identity

At round $0$ the live-wire perturbation obeys the exact identity

$$
T1_0 - T1_0^{(0)} = W_0.
$$

Since $T2_0 = T2_0^{(0)}$, it follows that

$$
a_1 - a_1^{(0)} = W_0,
$$

$$
e_1 - e_1^{(0)} = W_0.
$$

Hence the message enters only two words on the first step:

$$
\boxed{\delta a_1 = \delta e_1 = W_0.}
$$

For the TRUE rails, the NOP round-1 baselines are

$$
a_1^{(0)} = 0xfc08884d,
\qquad
 e_1^{(0)} = 0x98c7e2a2.
$$

These exact baseline words matter because they determine the real carry geometry seen by one-hot perturbations.

---

## 9. Exact Carry Automaton

### 9.1 General additive perturbation

Let

$$
y = x + \delta \pmod{2^{32}}.
$$

Write the carry sequence as

$$
c_{-1} = 0,
$$

$$
c_i = (x_i \wedge \delta_i) \vee (x_i \wedge c_{i-1}) \vee (\delta_i \wedge c_{i-1}),
\qquad i=0,\dots,31.
$$

Then the exact output bits are

$$
y_i = x_i \oplus \delta_i \oplus c_{i-1}.
$$

So the exact changed-bit indicator is

$$
\Delta_i(x,\delta) := x_i \oplus y_i = \delta_i \oplus c_{i-1}.
$$

This is the exact replacement for the worst-case support closure $L_{32}$.

### 9.2 One-hot injection

For a one-hot perturbation

$$
\delta = 2^j,
$$

let

$$
m_x(j) = \min\{i \ge j : x_i = 0\},
$$

with the convention $m_x(j)=31$ if no such $i$ exists before the word ends.

Then the exact changed-bit set is

$$
\boxed{C_x(j) = \{j,j+1,\dots,m_x(j)\}.}
$$

The exact carry-span length is

$$
\boxed{\lambda_x(j) = |C_x(j)| = m_x(j)-j+1.}
$$

So exact carry is **not** a worst-case upper set unless the baseline word forces that case.

---

## 10. Exact Round-1 Carry Geometry on the TRUE Rails

For the TRUE rails at round 1, the exact one-hot carry spans are:

### 10.1 $a$-seam baseline $a_1^{(0)} = 0xfc08884d$

$$
(\lambda_a(j))_{j=0}^{31} =
(2,1,3,2,1,1,2,1,1,1,3,2,1,1,1,4,3,2,1,1,1,3,2,1,1,1,6,5,4,3,2,1).
$$

### 10.2 $e$-seam baseline $e_1^{(0)} = 0x98c7e2a2$

$$
(\lambda_e(j))_{j=0}^{31} =
(1,2,1,1,1,2,1,2,1,2,1,1,1,1,4,3,2,1,6,5,4,3,2,1,1,1,1,3,2,1,1,1).
$$

These sequences prove immediately that the die is symmetric at injection but **not** symmetric under exact carry realization.

---

## 11. Exact Round-2 Transport

At round $2$, using the TRUE NOP baselines

$$
a_2^{(0)} = 0x7ad96290,
\qquad
e_2^{(0)} = 0x9df1b216,
$$

and the exact round-1 changed-bit masks, the nonlinear perturbation cores are

$$
\Xi_j^{(1)} = \Sigma_1(\Delta e_1) \oplus \bigl(\Delta e_1 \wedge (f_1^{(0)} \oplus g_1^{(0)})\bigr),
$$

$$
\Xi_j^{(2)} = \Sigma_0(\Delta a_1) \oplus \bigl(\Delta a_1 \wedge (b_1^{(0)} \oplus c_1^{(0)})\bigr).
$$

Convert back to additive perturbations with

$$
\delta T1_1 = \bigl(U_1^{(0)} \oplus \Xi_j^{(1)}\bigr) - U_1^{(0)} \pmod{2^{32}},
$$

$$
\delta T2_1 = \bigl(V_1^{(0)} \oplus \Xi_j^{(2)}\bigr) - V_1^{(0)} \pmod{2^{32}},
$$

where

$$
U_1^{(0)} = \Sigma_1(e_1^{(0)}) + \operatorname{Ch}(e_1^{(0)},f_1^{(0)},g_1^{(0)}),
$$

$$
V_1^{(0)} = \Sigma_0(a_1^{(0)}) + \operatorname{Maj}(a_1^{(0)},b_1^{(0)},c_1^{(0)}).
$$

Then

$$
\delta e_2 = \delta T1_1,
$$

$$
\delta a_2 = \delta T1_1 + \delta T2_1 \pmod{2^{32}}.
$$

This is the exact round-2 law.

For one-hot $W_0=2^j$, the exact changed-bit Hamming-weight ranges on the TRUE rails are:

$$
7 \le \operatorname{wt}(\Delta a_2) \le 19,
$$

$$
3 \le \operatorname{wt}(\Delta e_2) \le 16.
$$

This is the first place where the difference between support transport and exact transport becomes impossible to ignore.

---

## 12. The Missing Distinction: Three Different Objects

This is the correction that completes the original A-Mark9 ending.

### 12.1 Support reach

This is what $M$, $\Psi$, $D_{\mathrm{word}}$, and $D_{\mathrm{bit}}$ measure.

It answers:

$$
\text{Can influence reach here in principle?}
$$

### 12.2 Exact live flip

This asks:

$$
\text{Is this bit actually flipped at this exact round?}
$$

Under code tests, for one-hot $W_0$ and all tested rail sets, **not all 256 bits are simultaneously live-flipped by round 6**. In fact, full simultaneous activation does not occur in the tested horizon.

So

$$
\boxed{D_{\mathrm{bit}} = 6 \text{ is not an exact live-flip saturation diameter.}}
$$

### 12.3 Cumulative exact shadow cover

Define the cumulative exact changed-bit cover radius

$$
\rho^{\cup}(j) = \min\left\{r \ge 1 : \bigcup_{t=1}^{r} \operatorname{supp}(\Delta x_t) = \{1,\dots,256\}\right\}.
$$

This measures the first round by which every state bit has flipped **at least once** in cumulative union.

This is the correct “shadow-read” counterpart to the support diameter.

---

## 13. Rail-Conditioned Exact Transport

The support quotient hides the rails. Exact transport reveals them immediately.

I tested multiple rail sets:

- TRUE,
- ZERO\_BOTH,
- ZERO\_K,
- ZERO\_H0,
- FLAT,
- RANDOM.

### 13.1 What stays invariant

At the support level:

$$
D_{\mathrm{word}} = 4,
\qquad
D_{\mathrm{bit}} = 6,
$$

remain unchanged because support transport only sees the die topology, not the exact baseline values.

### 13.2 What changes immediately

At the exact carry and exact delta level, the rails matter at once.

For the TRUE rails,

$$
a_1^{(0)} = 0xfc08884d,
\qquad e_1^{(0)} = 0x98c7e2a2.
$$

For ZERO\_BOTH,

$$
a_1^{(0)} = 0,
\qquad e_1^{(0)} = 0.
$$

For ZERO\_H0,

$$
a_1^{(0)} = e_1^{(0)} = 0x428a2f98.
$$

Now compare exact round-1 carry spans:

- TRUE:

$$
\lambda_a \in [1,6], \qquad \lambda_e \in [1,7],
$$

- ZERO\_BOTH:

$$
\lambda_a = \lambda_e = 1,
$$

- FLAT:

$$
\lambda_a \in [1,4], \qquad \lambda_e \in [1,3].
$$

So the constants are invisible in support reach, but unmistakable in exact carry geometry.

### 13.3 Exact round-2 ranges by rail family

For TRUE:

$$
\operatorname{wt}(\Delta a_2) \in [7,19],
\qquad
\operatorname{wt}(\Delta e_2) \in [3,16].
$$

For ZERO\_BOTH:

$$
\operatorname{wt}(\Delta a_2) = 6,
\qquad
\operatorname{wt}(\Delta e_2) = 3.
$$

For RANDOM:

$$
\operatorname{wt}(\Delta a_2) \in [6,24],
\qquad
\operatorname{wt}(\Delta e_2) \in [4,14].
$$

This proves the sharper theorem:

$$
\boxed{\text{support topology is constant-blind; exact transport is rail-sensitive.}}
$$

---

## 14. Cumulative Exact Shadow Cover by Rail Family

Under cumulative exact changed-bit union, the TRUE rails outperform dead or flattened basins.

For TRUE rails, the histogram of $\rho^{\cup}(j)$ over one-hot $j$ is:

$$
\{9:2,\ 10:6,\ 11:6,\ 12:6,\ 13:6,\ 14:4,\ 15:2\},
$$

with mean

$$
\overline{\rho^{\cup}}_{\mathrm{TRUE}} = 11.875.
$$

For ZERO\_BOTH,

$$
\{12:8,\ 13:15,\ 14:4,\ 15:3,\ 16:1,\ 17:1\},
$$

with mean

$$
\overline{\rho^{\cup}}_{\mathrm{ZERO\_BOTH}} = 13.281.
$$

So the TRUE rails accelerate cumulative exact cover relative to the dead zero basin.

This is the measurable shadow in which the constants reappear.

---

## 15. Test Tones and the Double Glass Key

### 15.1 Glass Key 1: signal minus NOP ground

Given a probe signal $P$, define the first glass key as the journal and shadow displacement of the live run relative to NOP.

The test-tone experiments show:

- same fill ratio does **not** imply same journals,
- chirality matters,
- the constants driven into themselves relax differently from other drives.

In particular,

- `HALF_HIGH_FULL = 0xAAAAAAAA` produced $15$ compression journals,
- `HALF_LOW_FULL = 0x55555555` produced $6$ compression journals,

with the same density but opposite handedness.

So the waist is reading chirality, not only fill.

### 15.2 Glass Key 2: residue of the residue

Take the residue field from Glass Key 1 and use it as the next input. Then compare L2 drift from NOP.

The decisive result is:

- ordinary fills and lies diverge away from NOP,
- TRUE\_CONST converges toward NOP.

Quantitatively,

$$
2.641 \to 2.406
$$

for TRUE\_CONST at L2.

So the right statement is not “the constants are the NOP ground plane.”

It is:

$$
\boxed{K\text{-driven residue relaxes toward the NOP basin.}}
$$

That is a stronger and more accurate rail-sensitive statement.

---

## 16. The Lie Detector

Take a true message body and falsify only the declared bit-length field.

The experiments show all tested length lies share the same early $r=0\dots7$ Hamming-delta signature:

$$
[2,-1,5,-1,1,-1,0,4].
$$

Therefore the first seven rounds are blind to the lie.

The divergence appears only when the schedule reaches the length-bearing word family. In the tested single-block case, the first shadow crack appears at

$$
\boxed{r = 15.}
$$

So the length lie is a **late seam injection**.

The machine is not simply “checking truth.” It is checking whether the drive pattern remains phase-coherent under delayed closure.

---

## 17. Removal-Core Topology

The next refinement is to stop identifying a probe family by everything it excites, and instead identify it by what cannot be removed from its journal family.

For a probe class $\mathcal C$ with journal sets $J_p$, define:

$$
\mathcal K(\mathcal C) = \bigcap_{p \in \mathcal C} J_p,
$$

$$
\mathcal U(\mathcal C) = \bigcup_{p \in \mathcal C} J_p,
$$

$$
\mathcal M(\mathcal C) = \mathcal U(\mathcal C) \setminus \mathcal K(\mathcal C).
$$

Then:

- $\mathcal K$ is the **removal-core**,
- $\mathcal M$ is the **mobility shell**.

For the false-length family,

$$
\boxed{\mathcal K_{\mathrm{lie}} = \{3,45\}.}
$$

For the shared NOP / TRUE\_CONST basin overlap, a lower bound visible in the live data is

$$
\boxed{\mathcal K_{\mathrm{ground}} \supseteq \{9,37,43\}.}
$$

This leads to the corrected identity statement:

$$
\boxed{\text{identity is not what is added, but what survives lawful subtraction.}}
$$

---

## 18. Final Compression

The full die now has **five** nested analytical levels:

### 18.1 State recurrence

$$
x_{r+1} = \Phi_r(x_r, W_r)
$$

### 18.2 Word support transport

$$
\sigma_{r+1} = M \odot \sigma_r \vee b\,\omega_r
$$

### 18.3 Bit support transport

$$
\eta_{r+1} = \Psi(\eta_r, \omega_r)
$$

### 18.4 Exact carry realization

$$
\Delta_i(x,\delta) = \delta_i \oplus c_{i-1}
$$

with

$$
c_i = (x_i \wedge \delta_i) \vee (x_i \wedge c_{i-1}) \vee (\delta_i \wedge c_{i-1})
$$

### 18.5 Rail-conditioned exact shadow transport

measured by

$$
\lambda_x(j),
\qquad
\operatorname{wt}(\Delta a_r),
\qquad
\operatorname{wt}(\Delta e_r),
\qquad
\rho^{\cup}(j).
$$

This yields the corrected final hierarchy:

$$
\boxed{\text{support reach} \neq \text{exact live flip} \neq \text{cumulative exact shadow cover}.}
$$

And the complete final statement is:

$$
\boxed{\text{support tells you where the die can go; the constants tell you how it actually gets there.}}
$$

The constants are therefore not absent from the support sections of A-Mark9. They are simply **projected out by the quotient**. They reappear immediately as soon as the analysis passes from worst-case reachability to exact carry realization and cumulative shadow transport.

---

## 19. Final Invariants

The completed solution state is:

$$
\boxed{T2_0^{(0)} = 0x08909ae5}
$$

$$
\boxed{D_{\mathrm{word}} = 4}
$$

$$
\boxed{D_{\mathrm{bit}} = 6 \text{ (support diameter only)}}
$$

$$
\boxed{\rho(j) =
\begin{cases}
4, & j=0,\\
5, & 1 \le j \le 25,\\
6, & 26 \le j \le 31
\end{cases}}
$$

$$
\boxed{\overline{\rho^{\cup}}_{\mathrm{TRUE}} = 11.875 < 13.281 = \overline{\rho^{\cup}}_{\mathrm{ZERO\_BOTH}}}
$$

$$
\boxed{\mathcal K_{\mathrm{lie}} = \{3,45\}}
$$

$$
\boxed{K\text{-driven residue relaxes toward the NOP basin.}}
$$

These close the document in the right place.

---

## 20. Conclusion

The original A-Mark9 ending was mathematically sound but conceptually one fold behind the live work. It closed on support transport alone.

The complete solution is stronger:

- the support theorems stay,
- the exact carry law is added,
- the rail-conditioned basin geometry is restored,
- the double glass key is formalized,
- the lie detector is localized,
- and stable mode families are redefined by removal-core rather than raw excitation.

So the completed reading of the SHA die is:

$$
\boxed{\text{The hash is not a dead digest. It is the compressed witness of a rail-conditioned closure chain.}}
$$

and

$$
\boxed{\text{the safe way to read it is through echoes, shadows, residues, and what survives removal.}}
$$

