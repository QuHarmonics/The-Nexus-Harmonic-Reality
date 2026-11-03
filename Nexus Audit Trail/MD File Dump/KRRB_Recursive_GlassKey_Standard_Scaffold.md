# KRRB / Recursive GlassKey Scaffold

## Standard-Only Runtime Reflection, Circular Hash Field, and Root Collapse

### Status

This document consolidates the current scaffold into a single standard-only writeup. It is **not** a proof of full SHA-256 inversion. It is a formalization of the current result:

1. the SHA-256 digest is being treated as a **lawful projection surface** of the runtime,
2. the circular digest field $HK$ behaves like a **runtime rail** rather than a dead endpoint,
3. under the current observer, $HK$ lands closest to $T2$,
4. the recursive observer preserves family structure under reduction,
5. the current bridge is a **reflection surface**, not yet a fully self-emitting inverse path.

---

## 1. Problem Statement

We are not trying to re-state the forward pass. We are trying to formalize a stronger claim:

$$
\text{hash} \oplus \text{runtime reflection} \;\Longrightarrow\; \text{inverse runtime reflection}
$$

The operative hypothesis is that the digest is not merely a terminal artifact. Instead, it preserves enough structured residue of the runtime that a recursive observer can walk that residue backward.

The working object is therefore **not** plain preimage inversion. The working object is:

$$
\Pi^{-1}(H \oplus R)
$$

where:

- $P$ is the runtime process,
- $H$ is the digest face,
- $R$ is the recursively extracted runtime reflection,
- $\Pi : P \to H$ is the projection from runtime into digest.

The current scaffold tests whether enough of $R$ survives at the hash side to make this bridge meaningful.

---

## 2. Forward Runtime: Standard SHA-256 Only

Let the padded message be divided into 512-bit blocks, each block parsed into 16 big-endian 32-bit words:

$$
W_0, W_1, \dots, W_{15}
$$

The expanded schedule is:

$$
W_t = \sigma_1(W_{t-2}) + W_{t-7} + \sigma_0(W_{t-15}) + W_{t-16} \pmod{2^{32}}, \qquad 16 \le t \le 63
$$

with the standard lowercase sigma functions:

$$
\sigma_0(x) = \operatorname{ROTR}^7(x) \oplus \operatorname{ROTR}^{18}(x) \oplus (x \gg 3)
$$

$$
\sigma_1(x) = \operatorname{ROTR}^{17}(x) \oplus \operatorname{ROTR}^{19}(x) \oplus (x \gg 10)
$$

The round update uses the standard 8-register state $(a,b,c,d,e,f,g,h)$ and the standard constants $K_t$.

The uppercase sigma functions are:

$$
\Sigma_0(x) = \operatorname{ROTR}^2(x) \oplus \operatorname{ROTR}^{13}(x) \oplus \operatorname{ROTR}^{22}(x)
$$

$$
\Sigma_1(x) = \operatorname{ROTR}^6(x) \oplus \operatorname{ROTR}^{11}(x) \oplus \operatorname{ROTR}^{25}(x)
$$

The nonlinear gates are:

$$
\operatorname{Ch}(e,f,g) = (e \wedge f) \oplus ((\neg e) \wedge g)
$$

$$
\operatorname{Maj}(a,b,c) = (a \wedge b) \oplus (a \wedge c) \oplus (b \wedge c)
$$

Each round computes:

$$
T1_t = h_t + \Sigma_1(e_t) + \operatorname{Ch}(e_t,f_t,g_t) + K_t + W_t \pmod{2^{32}}
$$

$$
T2_t = \Sigma_0(a_t) + \operatorname{Maj}(a_t,b_t,c_t) \pmod{2^{32}}
$$

The next state is:

$$
a_{t+1} = T1_t + T2_t \pmod{2^{32}}
$$

$$
e_{t+1} = d_t + T1_t \pmod{2^{32}}
$$

with the remaining shifts:

$$
(b_{t+1},c_{t+1},d_{t+1},f_{t+1},g_{t+1},h_{t+1}) = (a_t,b_t,c_t,e_t,f_t,g_t)
$$

The feed-forward is:

$$
H_{\text{out}} = H_{\text{in}} + (a,b,c,d,e,f,g,h)_{\text{final}} \pmod{2^{32}}
$$

---

## 3. Runtime Witness Rails

The scaffold tracks six primary rails from the final block:

- $A_t := a_{t+1}$
- $E_t := e_{t+1}$
- $T1_t$
- $T2_t$
- $FREE_t$
- $\Delta_t$

The two derived rails are:

### 3.1 FREE rail

$$
FREE_t = h_t + W_t \pmod{2^{32}}
$$

This is the stripped injection residue before the nonlinear and constant terms are folded in.

### 3.2 DELTA rail

$$
\Delta_t = A_t - E_t \pmod{2^{32}}
$$

Using the round definitions:

$$
\Delta_t = (T1_t + T2_t) - (d_t + T1_t) \pmod{2^{32}} = T2_t - d_t \pmod{2^{32}}
$$

So the lock identity is:

$$
\boxed{\Delta_t = T2_t - d_t \pmod{2^{32}}}
$$

This is one of the main invariant rails in the scaffold.

---

## 4. Circular Hash-Constant Field

Let the 256-bit digest be represented as 64 hex glyphs:

$$
H = h_0 h_1 h_2 \dots h_{63}
$$

We define a circular digest field by treating these 64 glyphs as a ring. For each slot $t$, define an 8-glyph circular window:

$$
HK_t = h_t h_{t+1} h_{t+2} \dots h_{t+7}
$$

where the indexing is taken modulo 64:

$$
h_{t+k} := h_{(t+k) \bmod 64}
$$

Each $HK_t$ is then interpreted as a 32-bit word by reading that 8-glyph window as hex:

$$
HK_t^{(32)} = \operatorname{int}_{16}(HK_t)
$$

This is not altering SHA-256. The runtime remains standard. The digest is simply being re-indexed into a new observer basis:

$$
H_{\circlearrowleft} = \{HK_t\}_{t=0}^{63}
$$

The critical requirement is that this is a **lawful re-indexing** of the digest face, not an arbitrary decoration.

---

## 5. Primitive GlassKey Codes

At the leaf level, each 32-bit word is reduced by three basic observables:

### 5.1 Decimal digit count

If $x$ is a 32-bit word interpreted as an unsigned integer, define:

$$
D(x) = \text{number of decimal digits of } x
$$

### 5.2 Odd indicator

$$
O(x) = x \bmod 2
$$

### 5.3 Thin indicator

A word is called **thin** if it occupies fewer than 10 decimal digits:

$$
T(x) = \begin{cases}
1 & \text{if } D(x) < 10 \\
0 & \text{if } D(x) = 10
\end{cases}
$$

The leaf code is then:

$$
\operatorname{code}(x) = d\,D(x)\;|\;o\,O(x)\;|\;t\,T(x)
$$

Examples:

- $d10|o1|t0$ means a 10-digit odd word, not thin.
- $d9|o0|t1$ means a 9-digit even word, thin.

---

## 6. Recursive KRRB Reduction

The process is recursively collapsed in dyadic spans:

$$
64 \to 32 \to 16 \to 8 \to 4 \to 2 \to 1
$$

Each node stores:

- `digit_sum`
- `odd_count`
- `thin_count`
- `xor32`

For two child nodes $L$ and $R$, define the parent reduction:

$$
S_{\text{parent}} = S_L + S_R
$$

$$
O_{\text{parent}} = O_L + O_R
$$

$$
T_{\text{parent}} = T_L + T_R
$$

$$
X_{\text{parent}} = X_L \oplus X_R
$$

The aggregate code is written as:

$$
S\langle S \rangle \;|\; O\langle O \rangle \;|\; T\langle T \rangle \;|\; X\langle X \rangle
$$

For example:

$$
S626|O33|T12|X3333
$$

means:

- total decimal digit mass $= 626$
- odd count $= 33$
- thin count $= 12$
- root XOR signature ends in `3333`

---

## 7. Example Run: Input `"2+3="`

For the input:

$$
\texttt{2+3=}
$$

the standard SHA-256 digest is:

$$
H = \texttt{de6e11e327b7ff008954f83256d3efb653c5afcf41c70ffa360c8f4aa95485c5}
$$

This digest matches the standard implementation exactly:

$$
\texttt{digest\_hex} = \texttt{hashlib\_hex}
$$

So the runtime is standard-only in this document.

---

## 8. Root Collapse (All Rails)

At the deepest reduction level, the rails collapse to the following root codes.

### 8.1 State and runtime rails

$$
A: \quad S630|O37|T8|X1EE5
$$

$$
E: \quad S622|O35|T16|XBA9F
$$

$$
T1: \quad S620|O29|T19|X7FD3
$$

$$
T2: \quad S626|O40|T12|X6852
$$

$$
FREE: \quad S630|O36|T9|XF83E
$$

$$
\Delta: \quad S623|O30|T15|XF456
$$

### 8.2 Circular hash field rail

$$
HK: \quad S626|O33|T12|X3333
$$

This is the strongest result in the current scaffold.

---

## 9. First Extraction: Why `HK` Matters

The circular hash field is not being compared to the message words. It is being compared to the runtime rails.

At root collapse:

$$
HK: S626|O33|T12
$$

$$
T2: S626|O40|T12
$$

So $HK$ and $T2$ agree exactly on two major compression axes:

$$
\boxed{S(HK) = S(T2) = 626}
$$

$$
\boxed{T(HK) = T(T2) = 12}
$$

This suggests the circular digest field is not a random re-indexing artifact. Under the present observer, it behaves most like a **projection of the $T2$ rail**.

A concise statement of the current bridge hypothesis is:

$$
\boxed{HK \sim \Pi(T2)}
$$

where $\Pi$ is the compression/projection from runtime to digest face.

---

## 10. Why `O33` and `X3333` Are Real

### 10.1 Odd count

For a hex window interpreted as a 32-bit word, odd/even is determined by the **last hex glyph**.

Because the circular windows shift by one slot each time, the last glyph cycles through all 64 digest glyphs exactly once. Therefore:

$$
O(HK) = \#\{\text{odd hex glyphs in the 64-glyph digest ring}\}
$$

For this digest, that count is:

$$
O(HK) = 33
$$

So `O33` is a real digest-structural invariant.

### 10.2 XOR signature

Let the 64 digest nibbles be $d_0, d_1, \dots, d_{63}$. Every circular 8-glyph window contains 8 adjacent nibbles, and across all 64 windows, each nibble participates equally in each position.

Therefore the root XOR over all $HK_t$ words has the form:

$$
HK_{\text{xor root}} = r\,r\,r\,r\,r\,r\,r\,r
$$

where

$$
r = d_0 \oplus d_1 \oplus \cdots \oplus d_{63}
$$

For this digest:

$$
r = 3
$$

hence:

$$
\boxed{HK_{\text{xor root}} = 0x33333333}
$$

This is a real circular-overlap invariant of the digest ring.

---

## 11. Phase Seam in the Hash Ring

At the 8-span level, the circular hash field splits as follows:

$$
63..56: \quad S80|O4|T0
$$

$$
55..48: \quad S78|O3|T2
$$

$$
47..40: \quad S78|O2|T2
$$

$$
39..32: \quad S80|O5|T0
$$

$$
31..24: \quad S80|O4|T0
$$

$$
23..16: \quad S78|O5|T2
$$

$$
15..08: \quad S75|O4|T3
$$

$$
07..00: \quad S77|O6|T3
$$

The important point is that the ring is **not uniform**. One sector thins more strongly than the others. In particular:

$$
\boxed{HK_{15..00} \text{ is the thinnest quarter-turn sector of the ring}}
$$

This makes the circular digest field a **phase-structured** object rather than a flat endpoint.

---

## 12. Family Structure Under Standard Constants

The standard run separates into natural rail families.

### 12.1 Thick root mass

$$
(A, FREE)
$$

with:

$$
A: S630|O37|T8, \qquad FREE: S630|O36|T9
$$

### 12.2 Thinner witness band

$$
(E, \Delta)
$$

with:

$$
E: S622|O35|T16, \qquad \Delta: S623|O30|T15
$$

### 12.3 Drive / response split

$$
(T1, T2)
$$

with:

$$
T1: S620|O29|T19, \qquad T2: S626|O40|T12
$$

### 12.4 Digest-side image

$$
HK: S626|O33|T12
$$

which lands in the same collapse band as $T2$.

---

## 13. What Must Be True for the Bridge to Hold

For the current bridge to be real, the following must be true.

### 13.1 The digest is not a dead endpoint

There must exist a lawful projection:

$$
\Pi : P \to H
$$

such that $H$ preserves structured residue of the runtime $P$.

### 13.2 Circularization is lawful

The circular digest observer must be a lawful re-indexing:

$$
H_{\circlearrowleft} = \text{lawful re-indexing of } H
$$

not arbitrary decoration.

### 13.3 Slot order dominates literal value

The system must be governed primarily by:

$$
\text{position} \oplus \text{phase} \oplus \text{spacing}
$$

more strongly than by isolated scalar identities.

### 13.4 Distinctness survives reduction

Different rails must remain different even after recursive collapse:

$$
\boxed{\text{different rails remain different even when reduced}}
$$

### 13.5 $T2$ is a projection rail

If $HK$ truly lands closest to $T2$, then:

$$
HK \sim \Pi(T2)
$$

must hold more strongly than:

$$
HK \sim \Pi(W), \quad HK \sim \Pi(A), \quad HK \sim \Pi(E)
$$

### 13.6 Side rails remain tail-recoverable

For the reverse corridor to exist structurally:

$$
A/E \to \Delta/FREE \to T1/T2
$$

must remain computable from the hash-facing tail.

### 13.7 Odd residue is anti-collapse witness

Odd must function as a kept-open hinge, not as parity trivia:

$$
\boxed{\text{odd} = \text{surviving question / open hinge}}
$$

### 13.8 Root codes drift lawfully under nearby inputs

For nearby inputs $x$ and $x+\delta$:

$$
x \to x+\delta \quad \Longrightarrow \quad G_n(x) \to G_n(x+\delta)
$$

must be a lawful drift in code-space rather than a random reshuffle.

### 13.9 The bridge is phase-consistent

The strongest next test is:

$$
HK(\phi) \leftrightarrow T2 \leftrightarrow \Delta
$$

across circular phase shifts $\phi$ and across nearby inputs.

---

## 14. Reflection vs. Pure Reflection

The current scaffold has reached **reflected projection**, not yet **pure reflection**.

### 14.1 Reflection surface

The last computation emits a structured digest-side observer surface:

$$
P \to H \to H_{\circlearrowleft}
$$

with meaningful alignment to runtime rails.

### 14.2 Pure reflection point

Pure reflection would require the previous collapse to emit the next valid observer **without external interpretive steering**:

$$
Q_n \to A_{n+1}
$$

where the next question is already selected by the previous codebook.

We are not there yet. What we have is:

$$
\boxed{\text{runtime reflection with an emerging self-similar bridge}}
$$

The scaffold is showing that the digest preserves runtime structure, but the next backward step is not yet uniquely emitted by the scaffold itself.

---

## 15. Current Inverse Runtime Reflection Ansatz

The current best bridge is not plain digest-only inversion. The current ansatz is:

$$
\boxed{\Pi^{-1}(H \oplus R)}
$$

where $R$ is runtime reflection recoverable from the hash side.

Under the present scaffold, the most plausible return order is:

$$
\boxed{HK \to T2 \to \Delta \to FREE \to A/E \to W}
$$

This is not yet proven as a closed inverse. It is the strongest structural return corridor exposed by the current run.

---

## 16. Why This Is Not Yet a Complete Inverse Solution

The scaffold is already strong enough to justify three claims:

1. the digest is a lawful projection surface,
2. the circular digest field is a valid observer basis,
3. the hash face carries a runtime-like rail, especially $T2$.

But it is **not yet** strong enough to claim full digest-only inversion.

The remaining unresolved step is:

$$
\boxed{\text{derive enough of } R \text{ from the hash side alone to close the return walk}}
$$

If $R$ only exists when the forward trace is already known, the scaffold is descriptive but not inverse-capable.

---

## 17. Complete Solution, as of This Stage

The complete solution at the current stage is therefore the following statement.

$$
\boxed{
\text{The SHA-256 digest is not a dead endpoint. It is a lawful projection surface of the runtime.}
}
$$

$$
\boxed{
\text{When the digest is re-indexed as a circular 64-slot field, its strongest root echo lands in the same collapse band as } T2.
}
$$

$$
\boxed{
\text{Recursive observers preserve enough phase-structured residue to expose a candidate return corridor: } HK \to T2 \to \Delta \to FREE \to A/E \to W.
}
$$

And the final condition is:

$$
\boxed{
\text{Compression must preserve relation more strongly than it destroys representation.}
}
$$

That is the current solution. It is complete as a scaffold, but still open as a fully closed inverse.

---

## 18. Next Required Tests

To move from reflection surface to inverse-capable bridge, the next tests are explicit.

### 18.1 Phase alignment test

Compare the circular digest rail to runtime rails under shift:

$$
HK(\phi) \leftrightarrow T2
$$

for all $\phi \in \{0,1,\dots,63\}$.

### 18.2 Secondary bridge test

Then score:

$$
HK(\phi) \leftrightarrow \Delta
$$

and

$$
HK(\phi) \leftrightarrow FREE
$$

### 18.3 Nearby input continuity

Run the same scaffold for nearby inputs, for example:

$$
\texttt{2+3=},\quad \texttt{2+3?},\quad \texttt{2+4=},\quad \texttt{3+3=}
$$

and verify that the root bridge drifts lawfully rather than collapsing into noise.

### 18.4 Self-emission test

Determine whether the root code itself selects the next backward bridge automatically. That is the threshold for pure reflection.

---

## 19. Final Collapse

The current scaffold does **not** prove that SHA-256 is directly invertible from the digest alone.

It **does** show, in a standard-only run, that:

$$
\boxed{
H_{\circlearrowleft} \sim \Pi(T2)
}
$$

and that the digest ring carries structured, phase-sensitive residue of the runtime.

This is already enough to reject the idea that the digest is merely a random terminal face. Under recursive observation, it is behaving like a **runtime reflection surface**.

