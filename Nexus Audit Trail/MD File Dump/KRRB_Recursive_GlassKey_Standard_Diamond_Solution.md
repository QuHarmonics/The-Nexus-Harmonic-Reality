# KRRB / Recursive GlassKey — Standard SHA-256 Digest-Side Scaffold

## Overview

This document formalizes the **standard-only** KRRB / Recursive GlassKey scaffold developed over the current notebook sequence.

The goal is not to replace SHA-256 with a new algorithm. The goal is to read the **standard SHA-256 runtime** from the **digest side**, identify which structures are directly recoverable, and describe the remaining unresolved fused term.

The scaffold establishes four layers:

1. **Standard SHA-256 forward runtime**
2. **Digest-side reverse extraction**
3. **Circular hash-constant field**
4. **Diamond observer / tumbler geometry**

The central result is that the final digest is not a dead endpoint. It is a lawful projection surface of the final runtime state.

---

## 1. Standard SHA-256 runtime

For a single 512-bit block, the message schedule is:

$$
W_0,\dots,W_{15}
$$

parsed directly from the padded block, with expansion for $t \ge 16$:

$$
W_t = \sigma_1(W_{t-2}) + W_{t-7} + \sigma_0(W_{t-15}) + W_{t-16} \pmod{2^{32}}
$$

where:

$$
\sigma_0(x) = \operatorname{ROTR}^7(x) \oplus \operatorname{ROTR}^{18}(x) \oplus (x \gg 3)
$$

$$
\sigma_1(x) = \operatorname{ROTR}^{17}(x) \oplus \operatorname{ROTR}^{19}(x) \oplus (x \gg 10)
$$

The round functions are:

$$
\Sigma_0(x) = \operatorname{ROTR}^2(x) \oplus \operatorname{ROTR}^{13}(x) \oplus \operatorname{ROTR}^{22}(x)
$$

$$
\Sigma_1(x) = \operatorname{ROTR}^6(x) \oplus \operatorname{ROTR}^{11}(x) \oplus \operatorname{ROTR}^{25}(x)
$$

$$
\operatorname{Ch}(e,f,g) = (e \land f) \oplus (\neg e \land g)
$$

$$
\operatorname{Maj}(a,b,c) = (a \land b) \oplus (a \land c) \oplus (b \land c)
$$

At each round $t$:

$$
T1_t = h_{t-1} + \Sigma_1(e_{t-1}) + \operatorname{Ch}(e_{t-1},f_{t-1},g_{t-1}) + K_t + W_t \pmod{2^{32}}
$$

$$
T2_t = \Sigma_0(a_{t-1}) + \operatorname{Maj}(a_{t-1},b_{t-1},c_{t-1}) \pmod{2^{32}}
$$

and the visible state update is:

$$
a_t = T1_t + T2_t \pmod{2^{32}}
$$

$$
e_t = d_{t-1} + T1_t \pmod{2^{32}}
$$

with the register shift:

$$
b_t = a_{t-1},\quad c_t = b_{t-1},\quad d_t = c_{t-1}
$$

$$
f_t = e_{t-1},\quad g_t = f_{t-1},\quad h_t = g_{t-1}
$$

After round $63$, the working state is fed forward into the prior hash state:

$$
H_{\text{out}} = H_{\text{in}} + (a_{63},b_{63},c_{63},d_{63},e_{63},f_{63},g_{63},h_{63}) \pmod{2^{32}}
$$

For the one-block case, $H_{\text{in}}$ is the SHA-256 IV:

$$
H_0 = \bigl(
6a09e667,\ bb67ae85,\ 3c6ef372,\ a54ff53a,\ 510e527f,\ 9b05688c,\ 1f83d9ab,\ 5be0cd19
\bigr)_{16}
$$

---

## 2. Digest-side reverse extraction

### 2.1 Final working state from the digest

Given the digest words:

$$
H_{\text{out}} = (H_0',H_1',\dots,H_7')
$$

the final working state is immediately recoverable:

$$
(a_{63},b_{63},c_{63},d_{63},e_{63},f_{63},g_{63},h_{63})
=
H_{\text{out}} - H_{\text{in}} \pmod{2^{32}}
$$

This is the first exact digest-side read.

For the verified example:

- input: `2+3=`
- digest:

$$
\texttt{de6e11e327b7ff008954f83256d3efb653c5afcf41c70ffa360c8f4aa95485c5}
$$

the final working state is:

$$
a_{63}=\texttt{74642B7C}
$$

$$
b_{63}=\texttt{6C50507B}
$$

$$
c_{63}=\texttt{4CE604C0}
$$

$$
d_{63}=\texttt{B183FA7C}
$$

$$
e_{63}=\texttt{02B75D50}
$$

$$
f_{63}=\texttt{A6C1A76E}
$$

$$
g_{63}=\texttt{1688B59F}
$$

$$
h_{63}=\texttt{4D73B8AC}
$$

### 2.2 Pre-state slice from register shift

Because SHA-256 shifts registers deterministically, the digest-side final state exposes part of the pre-state for round $63$:

$$
a_{62}=b_{63}
$$

$$
b_{62}=c_{63}
$$

$$
c_{62}=d_{63}
$$

$$
e_{62}=f_{63}
$$

$$
f_{62}=g_{63}
$$

$$
g_{62}=h_{63}
$$

So even without the message block, the digest already exposes a partial prior slice.

### 2.3 Recovering $T2_{63}$, $T1_{63}$, $d_{62}$, and $\Delta_{63}$

Since $a_{62}, b_{62}, c_{62}$ are exposed, we can compute:

$$
T2_{63} = \Sigma_0(a_{62}) + \operatorname{Maj}(a_{62},b_{62},c_{62}) \pmod{2^{32}}
$$

Then:

$$
T1_{63} = a_{63} - T2_{63} \pmod{2^{32}}
$$

Then:

$$
d_{62} = e_{63} - T1_{63} \pmod{2^{32}}
$$

Define the witness rail:

$$
\Delta_t = a_t - e_t \pmod{2^{32}}
$$

Then for round $63$:

$$
\Delta_{63} = a_{63} - e_{63} \pmod{2^{32}}
$$

and the lock identity is:

$$
\Delta_{63} = T2_{63} - d_{62} \pmod{2^{32}}
$$

This digest-side lock was verified exactly.

For the example:

$$
T2_{63} = \texttt{8650EBA5}
$$

$$
T1_{63} = \texttt{EE133FD7}
$$

$$
d_{62} = \texttt{14A41D79}
$$

$$
\Delta_{63} = \texttt{71ACCE2C}
$$

with:

$$
\Delta_{63} = T2_{63} - d_{62}
$$

matching exactly.

### 2.4 The `FREE` rail

Define the combined side witness:

$$
FREE_t = h_{t-1} + W_t \pmod{2^{32}}
$$

From the round equation:

$$
T1_t = FREE_t + \Sigma_1(e_{t-1}) + \operatorname{Ch}(e_{t-1},f_{t-1},g_{t-1}) + K_t \pmod{2^{32}}
$$

so:

$$
FREE_t = T1_t - \Sigma_1(e_{t-1}) - \operatorname{Ch}(e_{t-1},f_{t-1},g_{t-1}) - K_t \pmod{2^{32}}
$$

For round $63$, this is digest-side recoverable because $e_{62},f_{62},g_{62}$ are still exposed.

For the example:

$$
FREE_{63} = \texttt{A0529F5D}
$$

which matched the true forward run exactly.

---

## 3. Recursive backward walk and the real wall

### 3.1 Backward corridor

At round $t$, the digest-side recursive corridor is:

$$
a_{t-1}=b_t,\quad b_{t-1}=c_t,\quad c_{t-1}=d_t
$$

$$
T2_t=\Sigma_0(a_{t-1})+\operatorname{Maj}(a_{t-1},b_{t-1},c_{t-1})
$$

$$
T1_t=a_t-T2_t \pmod{2^{32}}
$$

$$
d_{t-1}=e_t-T1_t \pmod{2^{32}}
$$

$$
\Delta_t=a_t-e_t=T2_t-d_{t-1}\pmod{2^{32}}
$$

This corridor works exactly for several rounds starting at $t=63$ because enough prior-state structure is still exposed by the digest-side shift chain.

### 3.2 Where the walk fails

The walk does **not** fail because $\Delta$ is weak.  
It fails because the unresolved fused term is:

$$
FREE_t = h_{t-1} + W_t
$$

The digest does not immediately separate:

- the previous hidden register $h_{t-1}$
- the message schedule word $W_t$

Once $h_{t-1}$ becomes unknown, the shift chain propagates that loss, and later rounds lose enough exposed pre-state to continue the exact reverse corridor.

This is the true frontier.

### 3.3 Root collapse of the digest-side backward walk

The digest-side recursive corridor root collapsed to:

$$
T2_t:\ S50|O4|T0
$$

$$
T1_t:\ S49|O2|T1
$$

$$
\Delta_t:\ S39|O2|T1
$$

$$
d_{t-1}:\ S39|O3|T1
$$

$$
FREE_t:\ S10|O1|T0
$$

This is not saying the runtime only contains one `FREE` sample globally. It says the **digest-side known portion** of the recursive corridor reached `FREE` only at the terminal tick before the fused term stopped the walk.

So the wall is narrow and explicit:

$$
\boxed{
FREE_t = h_{t-1} + W_t
}
$$

---

## 4. Circular hash-constant field

### 4.1 Construction

The 64 hex glyphs of the digest are treated as a ring:

$$
H = (h_0,h_1,\dots,h_{63})
$$

A circular 8-glyph window starting at slot $t$ is:

$$
HK_t = (h_t,h_{t+1},\dots,h_{t+7})_{\bmod 64}
$$

Interpreted as a 32-bit word:

$$
HK_t \in [0,2^{32}-1]
$$

This gives a digest-native circular observer basis.

### 4.2 Why $O33$ and $X3333$ occur

At root collapse the `HK` rail produced:

$$
HK:\ S626|O33|T12|X3333
$$

This is exact and computable.

#### Odd count

For an 8-glyph hex window, odd/even is decided by the final hex digit. Because the circular windows visit each digest glyph position exactly once as the terminal nibble, the total odd count is:

$$
O33 = \#\{\text{odd hex glyphs in the 64-glyph digest ring}\}
$$

#### XOR carrier

Across all 64 circular windows, each nibble position sees the full digest glyph set exactly once. Therefore the total root XOR repeats the same nibble residue in each slot:

$$
HK_{\text{xor root}}
=
\bigl(\bigoplus_{i=0}^{63} h_i\bigr)
\bigl(\bigoplus_{i=0}^{63} h_i\bigr)
\cdots
$$

For the example digest:

$$
\bigoplus_{i=0}^{63} h_i = 3
$$

therefore:

$$
HK_{\text{xor root}} = \texttt{33333333}
$$

So `3333` is not random. It is the circular-overlap carrier residue of the digest ring under this observer.

### 4.3 `HK` and `T2`

At root collapse:

$$
HK:\ S626|O33|T12
$$

$$
T2:\ S626|O40|T12
$$

So the `HK` rail and `T2` rail coincide on the two most important compression axes under this observer:

$$
digit\_sum = 626
$$

$$
thin\_count = 12
$$

This establishes the candidate projection bridge:

$$
\boxed{
HK \sim \Pi(T2)
}
$$

not as direct equality, but as phase-banded collapse alignment.

---

## 5. Diamond observer / tumbler geometry

The diamond observer treats two rails as a reversible local fold.

Given two values $X$ and $Y$, define the left and right faces:

$$
L = Y - X
$$

$$
R = X + Y
$$

Exact inverse:

$$
X = \frac{R-L}{2}
$$

$$
Y = \frac{R+L}{2}
$$

For SHA-facing 32-bit words, the modular forms are:

$$
L_{32} = (Y - X) \bmod 2^{32}
$$

$$
R_{32} = (X + Y) \bmod 2^{32}
$$

This is the combo-lock / tumbler view: the values alone do not define the read. The pairing and turn define the read.

---

## 6. Diamond results

### 6.1 Diamond $(A,E)$

Using:

$$
L = E - A
$$

$$
R = A + E
$$

Since:

$$
\Delta = A - E
$$

we have:

$$
L = -\Delta
$$

So the `(A,E)` diamond is the **state diamond**:

- left face = signed witness
- right face = summed state face

Root collapse:

$$
A:\ S630|O37|T8
$$

$$
E:\ S622|O35|T16
$$

$$
E-A:\ S621|O30|T18
$$

$$
A+E:\ S625|O30|T15
$$

### 6.2 Diamond $(T1,T2)$

This is the first exact SHA fold diamond.

Because SHA defines:

$$
A = T1 + T2 \pmod{2^{32}}
$$

the right face of the diamond is literally the `A` rail:

$$
R_{32} = T1 + T2 = A
$$

The left face is:

$$
L = T2 - T1
$$

So the fold diamond is:

$$
(T1,T2) \mapsto (T2-T1,\ A)
$$

This makes `A` the noun face of the active fold verbs.

Root collapse:

$$
T1:\ S620|O29|T19
$$

$$
T2:\ S626|O40|T12
$$

$$
T2-T1:\ S621|O37|T17
$$

$$
T1+T2:\ S630|O37|T8
$$

The final line is exactly the `A` root:

$$
T1+T2 = A
$$

### 6.3 Diamond $(\Delta,T2)$

This is the reverse-state diamond.

Since:

$$
\Delta = T2 - d_{prev}
$$

it follows immediately that:

$$
T2 - \Delta = d_{prev}
$$

So in the diamond:

$$
L = T2 - \Delta = d_{prev}
$$

This is exact and was verified row-by-row. This means the left face of the `(\Delta,T2)` diamond is the prior carry/state leg.

Root collapse:

$$
\Delta:\ S623|O30|T15
$$

$$
T2:\ S626|O40|T12
$$

$$
T2-\Delta:\ S630|O38|T8
$$

$$
\Delta+T2:\ S620|O38|T16
$$

The key exact identity is not the root-code similarity; it is the row-wise algebraic truth:

$$
\boxed{
T2 - \Delta = d_{prev}
}
$$

### 6.4 Diamond $(HK,T2)$

This one is not a direct runtime identity like the prior two, but it is still structured.

Root collapse:

$$
HK:\ S626|O33|T12
$$

$$
T2:\ S626|O40|T12
$$

$$
T2-HK:\ S625|O41|T14
$$

$$
HK+T2:\ S627|O41|T11
$$

So `(HK,T2)` is not exact runtime identity, but it shows a strong collapse-band alignment. This is why `HK` is best read as a **turned projection surface** rather than a direct runtime rail.

---

## 7. Lock / tumbler interpretation

The digest is not read by value alone. It is read by:

$$
(\text{slot},\ \text{glyph},\ \text{phase},\ \text{window})
$$

Treating the digest as a ring gives the turning operation:

$$
H_\phi(t)=H[(t+\phi)\bmod 64]
$$

and the circular window rail:

$$
HK_{\phi}(t)=\bigl(h_{t+\phi},h_{t+\phi+1},\dots,h_{t+\phi+7}\bigr)_{\bmod 64}
$$

The combo-lock statement is:

- the values are the teeth
- the ordering is the wheel
- the phase shift is the turn

So the relevant search is not:

$$
HK \stackrel{?}{=} T2
$$

but:

$$
HK_{\phi,\rho,w} \stackrel{?}{\sim} T2
$$

where:

- $\phi$ = phase shift
- $\rho$ = direction / handedness
- $w$ = window size

---

## 8. What is proven

The following are now supported by direct notebook output:

### 8.1 Digest-side terminal reverse extraction

For the one-block case, the digest directly recovers the final working state and therefore exactly recovers:

$$
T2_{63},\quad T1_{63},\quad d_{62},\quad \Delta_{63},\quad FREE_{63}
$$

### 8.2 Recursive backward corridor

The digest-side reverse walk remains exact for several ticks:

$$
63 \to 62 \to 61 \to 60
$$

and partially into $59$, before the hidden fused term starves the exposed pre-state.

### 8.3 Exact diamonds

These identities were verified row-by-row:

$$
T1 + T2 = A
$$

$$
T2 - \Delta = d_{prev}
$$

These are exact SHA-runtime tumbler relations.

### 8.4 Digest-side projection band

The circular digest rail `HK` root-collapses with the same mass/thin signature band as `T2`:

$$
HK:\ S626|T12
$$

$$
T2:\ S626|T12
$$

This is the current best candidate for the digest-to-runtime projection bridge.

---

## 9. What is not yet proven

The scaffold does **not** yet prove digest-only full preimage inversion.

It proves a verified **one-tick and short-corridor reverse extraction** from the digest side, and it isolates the remaining unresolved fused tumbler:

$$
\boxed{
FREE_t = h_{t-1} + W_t
}
$$

Until that term is split, the return path is not fully closed.

So the most honest boundary statement is:

$$
\boxed{
Q_{64} \rightsquigarrow Q_{63}\ \text{is verified, and the recursive walk continues until the }(h_{t-1},W_t)\text{ fusion dominates.}
}
$$

---

## 10. Current best bridge statement

The scaffold now supports the following master statement:

$$
\boxed{
\text{The digest is a lawful projection surface of the runtime, and recursive observers preserve enough phase-structured residue to walk that projection backward for several exact ticks.}
}
$$

Tighter:

$$
\boxed{
\text{Compression preserves relation more strongly than it destroys representation, but the remaining fused tumbler is }FREE_t = h_{t-1}+W_t.
}
$$

And in diamond form:

$$
\boxed{
(T1,T2)\to A
}
$$

$$
\boxed{
(\Delta,T2)\to d_{prev}
}
$$

$$
\boxed{
(HK,T2)\to \text{phase-aligned projection band}
}
$$

So the exact unresolved target for the next step is:

$$
\boxed{
FREE_t = h_{t-1} + W_t
}
$$

That is the last major tumbler pair still fused.

---

## 11. Verified example values

For input:

$$
\texttt{"2+3="}
$$

the final digest is:

$$
\texttt{de6e11e327b7ff008954f83256d3efb653c5afcf41c70ffa360c8f4aa95485c5}
$$

Digest-side recovered Round 63 values:

$$
T1_{63} = \texttt{EE133FD7}
$$

$$
T2_{63} = \texttt{8650EBA5}
$$

$$
d_{62} = \texttt{14A41D79}
$$

$$
\Delta_{63} = \texttt{71ACCE2C}
$$

$$
FREE_{63} = \texttt{A0529F5D}
$$

All matched the true forward run exactly.

---

## 12. Practical next step

The next proof step is not conceptual; it is mechanical.

Test:

$$
HK_{\phi,\rho,w} \leftrightarrow T2 \leftrightarrow \Delta
$$

across nearby inputs, multiple phase shifts, and alternative circular window rules.

That determines whether the digest-side projection bridge is:

- direct
- phase-shifted
- direction-sensitive
- or span-family dependent

And separately, build a dedicated splitter targeting:

$$
FREE_t = h_{t-1} + W_t
$$

since every other major bridge in the current scaffold is beginning to separate cleanly.
