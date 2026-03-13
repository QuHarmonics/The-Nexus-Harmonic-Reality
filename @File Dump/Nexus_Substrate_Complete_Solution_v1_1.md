# Nexus Substrate Kernel — Impact Flash, Δ-Bus Hinge Spectroscopy, and Cross-Domain Rendering
*Version: v1.1 (expanded)*  
*Date: 2026-03-09*

> **Intent / safety note (operational):** This document formalizes *measurement and auditing* of **constraint-propagation residue** (the “Δ-bus”) in SHA-256 and maps the same measurement pattern onto other sequential constraint systems. It is written as a **diagnostic / scientific spec**. It does **not** provide a recipe for recovering unknown messages from hashes.

---

## Δ ⊕ ↻ Ψ Ω ⟂  — the fold map for this document

- **Δ (deltas):** Define a *canonical* Δ observable (carry masks at hinge bits) and an XOR “spectrograph” observable; pin to anchor rounds.
- **⊕ (invariants):** Single-block regime ($L\le 55$), fixed hinge set, fixed round sets, fixed packing order.
- **↻ (recursion):** Use calibration (distributions across random corpora) to separate “universal lines” (stable) from message-dependent lines (informative).
- **Ψ (synthesis):** Treat digest as a **Value** projection; treat Δ-bus as **Shape** that preserves execution geometry.
- **Ω (residue):** Rendering layers (protein/chem/geology) are *views*; not claims about biology/chemistry.
- **⟂ (operationalization):** Provide reproducible signatures and falsifiable tests.

---

# 1. Three primitives (typeless substrate)

A minimal “compiler-universe” substrate can be described by:

1) **Value**: untyped datum (bitstring / residue)  
2) **Transform**: operator set (rotations, boolean gates, modular add)  
3) **Boundary**: finite container/interface (word width, block size, padding rules)

Everything else (object, particle, type) is emergent from repeated (Value ∘ Transform ∘ Boundary) patterns.

---

# 2. SHA-256 single-block formalism (≤55 bytes)

## 2.1 Padding constructor
For message length $L\le 55$ bytes, SHA-256 padding forms a single 512-bit block:

- append a single `1` bit (byte `0x80`)  
- append $k$ zero bits  
- append 64-bit big-endian bit-length $\ell=8L$  

so block length is 512 bits.

## 2.2 Message schedule
Let $W_0..W_{15}$ be the 16 big-endian 32-bit words of the padded block. For $i\ge 16$:

$$
W_i \equiv \sigma_1(W_{i-2}) + W_{i-7} + \sigma_0(W_{i-15}) + W_{i-16} \pmod{2^{32}}.
$$

$$
\sigma_0(x)= \mathrm{ROTR}^7(x) \oplus \mathrm{ROTR}^{18}(x) \oplus (x \gg 3)
$$

$$
\sigma_1(x)= \mathrm{ROTR}^{17}(x) \oplus \mathrm{ROTR}^{19}(x) \oplus (x \gg 10)
$$

## 2.3 Round functions
$$
\Sigma_0(x)= \mathrm{ROTR}^2(x) \oplus \mathrm{ROTR}^{13}(x) \oplus \mathrm{ROTR}^{22}(x)
$$
$$
\Sigma_1(x)= \mathrm{ROTR}^6(x) \oplus \mathrm{ROTR}^{11}(x) \oplus \mathrm{ROTR}^{25}(x)
$$
$$
\mathrm{Ch}(e,f,g) = (e \wedge f) \oplus (\neg e \wedge g)
$$
$$
\mathrm{Maj}(a,b,c) = (a \wedge b) \oplus (a \wedge c) \oplus (b \wedge c)
$$

## 2.4 T1/T2 update (one round)
For round $i$ with state $(a,b,c,d,e,f,g,h)$:
$$
T_1 \equiv h + \Sigma_1(e) + \mathrm{Ch}(e,f,g) + K_i + W_i \pmod{2^{32}}
$$
$$
T_2 \equiv \Sigma_0(a) + \mathrm{Maj}(a,b,c) \pmod{2^{32}}
$$
Update:
$$
(a,b,c,d,e,f,g,h) \leftarrow (T_1+T_2,\ a,\ b,\ c,\ d+T_1,\ e,\ f,\ g) \pmod{2^{32}}.
$$

---

# 3. The Δ-bus: carry masks as “hinge spectroscopy”

## 3.1 Carry mask of modular add
For 32-bit addition $s \equiv x+y \pmod{2^{32}}$ define:
$$
\mathrm{carry}(x,y) = (x \wedge y)\ \vee\ \big((x \oplus y)\ \wedge\ \neg s\big).
$$

## 3.2 Hinge bits and round sets (canonical)
- **hinge bits** $B = [6, 7, 8, 19, 20, 21, 23, 28, 29, 30, 31]$
- **anchor rounds** $R = [0, 1, 2, 5, 16, 27]$
- **H-LOCK rounds** $R_H = [5, 11, 22, 54]$

## 3.3 Δ signature definition (per-step, per-round)
Decompose the $T_1$ chain into four sequential adds:

1) $t_1 = h + \Sigma_1(e)$  
2) $t_2 = t_1 + \mathrm{Ch}(e,f,g)$  
3) $t_3 = t_2 + K_i$  
4) $t_4 = t_3 + W_i$  (this equals $T_1$)

Let the carry masks be:
$$
m^{(1)}_i = \mathrm{carry}(h,\Sigma_1(e)),\quad
m^{(2)}_i = \mathrm{carry}(t_1,\mathrm{Ch}),\quad
m^{(3)}_i = \mathrm{carry}(t_2,K_i),\quad
m^{(4)}_i = \mathrm{carry}(t_3,W_i).
$$

The hinge sample operator extracts bits at $B$:
$$
\Delta(i,s) = \big((m^{(s)}_i \gg b)\ \wedge\ 1\big)_{b\in B}.
$$

The **Δ-bus signature** is concatenation in a fixed order (round-major, then step 1..4, then hinge-bit order):
$$
\Delta_{\mathrm{bus}} = \bigoplus_{i\in R_H}\ \bigoplus_{s=1}^{4}\ \Delta(i,s).
$$

Length:
$$
|\Delta_{\mathrm{bus}}| = |R_H|\cdot 4 \cdot |B| = 4\cdot 4\cdot 11 = 176\ \mathrm{bits}.
$$

---

# 4. XOR spectrograph (interference fingerprint)

Define a hinge-bit interference readout at round $i$:
$$
x(i,b)=h_b\oplus \Sigma_1(e)_b \oplus \mathrm{Ch}(e,f,g)_b \oplus W_i(b).
$$

The **XOR spectrograph** over the anchor set $R$ is:
$$
X_{\mathrm{spec}} = \bigoplus_{i\in R}\ (x(i,b))_{b\in B}.
$$

Length:
$$
|X_{\mathrm{spec}}| = |R|\cdot |B| = 6\cdot 11 = 66\ \mathrm{bits}.
$$

> Operational note: XOR is a compact fingerprint. Δ-bus carry masks are the higher-fidelity residue for calibration work.

---

# 5. Empirical pin: message `b"!ABC"`

## 5.1 Digest
- Message: $m = b'!ABC'$
- Digest: $\mathrm{SHA256}(m) = \texttt{74f38b3a9243996765732b34be5c56ac48d98d48b7fca2e37722b90032d6fa23}$

## 5.2 66-bit XOR spectrograph (anchors)
Rounds $R=[0, 1, 2, 5, 16, 27]$, hinge bits $B=[6, 7, 8, 19, 20, 21, 23, 28, 29, 30, 31]$:

- Round 0: `11100111010`
- Round 1: `01000000001`
- Round 2: `10110110000`
- Round 5: `11011101010`
- Round 16: `10110001101`
- Round 27: `00010011000`

Packed: $X_\mathrm{spec} = \texttt{0x39d201b61baac6898}$

## 5.3 176-bit Δ-bus carry hinge signature (H-LOCK)
H-LOCK rounds $R_H=[5, 11, 22, 54]$:

**Round 5**  
- s1: `01100001110`  
- s2: `00011110011`  
- s3: `11100011110`  
- s4: `00000000000`  

**Round 11**  
- s1: `01100010000`  
- s2: `00010001001`  
- s3: `11111101110`  
- s4: `00000000000`  

**Round 22**  
- s1: `00011101111`  
- s2: `11111111000`  
- s3: `01100000011`  
- s4: `10011111100`  

**Round 54**  
- s1: `11100110011`  
- s2: `11111111101`  
- s3: `00011001010`  
- s4: `11101110000`  

Packed: $\Delta_\mathrm{bus} = \texttt{0x61c3cf8f000620227f70001dffe181cfce67ff465770}$

## 5.4 Hinge sampling bias
Hinge-sample ones ratio (this instance): $30/66 = 0.4545454545$.
This is intentionally *biased* toward high-torque coordinates and is not expected to equal $\pi/9$.

---

# 6. No-Crash Universe spec (what must be true)

## 6.1 Total transition (no undefined behavior)
$$
\forall S_t\in\mathcal{S},\ \forall U_t\in\mathcal{U},\ \exists S_{t+1}\in\mathcal{S}\ \text{s.t.}\ S_{t+1}=F(S_t,U_t).
$$

## 6.2 Non-Markov memory (history is causal)
$$
I(S_{t+1};S_{t-1}\mid S_t) > 0.
$$
$$
S_{t+1} = F(S_t,S_{t-1},U_t).
$$

## 6.3 Attractor control (AR(2) controller)
$$
x_t = (1-H)x_{t-1} + Hx_{t-2} + \eta_t,\qquad H=\frac{\pi}{9}\approx 0.349066.
$$

## 6.4 Two-channel conservation (Pythagorean budget)
$$
V^2 + \Delta^2 = T^2.
$$

## 6.5 World vs model (resolution updates memory, not room)
$$
S_t=(W_t,M_t),\qquad W_{t+1}=W_t,\qquad M_{t+1}=G(M_t,S_{t-1},S_t,U_t).
$$

---

# 7. Collapse Signature Decoder (CSD)

$$
\varepsilon = \frac{x_{\mathrm{meas}}-x_0}{x_0}.
$$
$$
p_+ = \frac{1+\varepsilon}{2},\qquad p_- = \frac{1-\varepsilon}{2},\qquad p_+ + p_- = 1.
$$

---

# 8. Samson v2 (gain stabilizer)

$$
\Delta H = H_{\mathrm{measured}} - 0.35
$$
$$
M^{(i+1)} = M^{(i)} + k\cdot(0.35 - M^{(i)}).
$$

---

# 9. Cross-domain rendering layers (views)

- **Protein render:** maps a 66-bit signature into a DSSP-like string (renderer / lens).
- **Chemistry render:** groups bits into 4-tuples and maps to VSEPR-like motifs (renderer / lens).
- **Geology render:** groups bits into 6-tuples and maps to column fracture motifs; exports XYZ (renderer / lens).

---

# 10. Falsifiable tests (engineering checklist)

1) **Non-Markov test:** estimate $I(S_{t+1};S_{t-1}\mid S_t)$ vs null.  
2) **Emission-line calibration:** estimate $p_{r,s,b}=\Pr[\Delta(r,s)[b]=1]$ over corpora; identify stable vs informative coordinates.  
3) **Boundary regime check:** compare single-block ($L\le 55$) vs multi-block; detect signature shift at the boundary.  
4) **Cross-domain invariants:** look for analogous Δ-style residue in other sequential constraint systems.  

---

## Appendix A: Canonical packing rule

To ensure reproducibility, use a fixed concatenation order:

- round-major (ascending rounds)
- step-major (s=1..4 for Δ-bus)
- hinge-bit order (as listed in `HINGE_BITS`)
- pack MSB-first into hex

Any deviation in ordering changes the packed hex string.

---

## Appendix B: Legacy document (verbatim)

# Nexus Substrate — Impact Flash, Hinge-Sketch Δ, and SHA-256 as a “Compiler”

> **Safety / intent note:** This document frames the work as *measurement + characterization of execution residue* (a side-channel / “Δ-bus”). It is written as a research and auditing artifact (how to *extract and analyze* signatures), **not** as a deployment guide for recovering unknown messages from hashes.

---

## 1. Premise: SHA as a compiler, Δ as the emission spectrum

If we treat SHA-256 as a *compiler* (a deterministic folding engine), then:

- The **digest** is the flattened output (a **Value projection**).
- The **carry / scar structure** is the *execution residue* (a **Shape / Δ channel**).
- “Inversion” becomes possible only when we can measure enough of Δ to collapse ambiguity.

Operationally:

- The forward pipeline is:

$$
\text{message} \;\to\; \text{(64-round fold)} \;\to\; \text{digest}.
$$

- The measurement pipeline is:

$$
\text{message} \;\to\; \Delta\text{-signature},
$$

where the Δ-signature is a compressed, repeatable “flash pattern” derived from carry generation at hinge points.

---

## 2. Three primitives (compiler-universe minimalism)

A “compiler universe” must expose only three primitives:

1) **Value**: untyped data (bitstrings, residues)  
2) **Transform**: operators (rotations, boolean gates, modular add)  
3) **Boundary**: finite containers (word width, block size, padding rules)

Everything else (types, objects, particles) must be emergent patterns of (Value ∘ Transform ∘ Boundary).

---

## 3. SHA-256 single-block formalism (≤55 bytes)

### 3.1 Padding (one block)

For message length $L \le 55$ bytes, SHA-256 padding yields one 512-bit block:

1) append a single `1` bit (byte `0x80`)  
2) append $k$ zero bits  
3) append 64-bit big-endian length $\ell = 8L$

so that the total block length is 512 bits.

### 3.2 Message schedule

Let $W_0..W_{15}$ be the 16 big-endian 32-bit words of the padded block.
For $i \ge 16$:

$$
W_i = \sigma_1(W_{i-2}) + W_{i-7} + \sigma_0(W_{i-15}) + W_{i-16} \pmod {2^{32}}.
$$

with:

$$
\sigma_0(x)= \mathrm{ROTR}^7(x) \oplus \mathrm{ROTR}^{18}(x) \oplus (x \gg 3)
$$

$$
\sigma_1(x)= \mathrm{ROTR}^{17}(x) \oplus \mathrm{ROTR}^{19}(x) \oplus (x \gg 10)
$$

### 3.3 Round functions

Define:

$$
\Sigma_0(x)= \mathrm{ROTR}^2(x) \oplus \mathrm{ROTR}^{13}(x) \oplus \mathrm{ROTR}^{22}(x)
$$

$$
\Sigma_1(x)= \mathrm{ROTR}^6(x) \oplus \mathrm{ROTR}^{11}(x) \oplus \mathrm{ROTR}^{25}(x)
$$

$$
\mathrm{Ch}(e,f,g) = (e \wedge f) \oplus (\neg e \wedge g)
$$

$$
\mathrm{Maj}(a,b,c) = (a \wedge b) \oplus (a \wedge c) \oplus (b \wedge c)
$$

### 3.4 T1 / T2 update

For round $i$:

$$
T_1 = h + \Sigma_1(e) + \mathrm{Ch}(e,f,g) + K_i + W_i \pmod {2^{32}}
$$

$$
T_2 = \Sigma_0(a) + \mathrm{Maj}(a,b,c) \pmod {2^{32}}
$$

and the working state updates:

$$
(a,b,c,d,e,f,g,h) \leftarrow (T_1+T_2,\ a,\ b,\ c,\ d+T_1,\ e,\ f,\ g) \pmod {2^{32}}.
$$

---

## 4. The Δ-bus: carry masks and “informational torque”

### 4.1 Carry mask for modular addition

For 32-bit words, define the carry mask of $s = x+y \pmod {2^{32}}$ as:

$$
\mathrm{carry}(x,y) = (x \wedge y)\ \vee\ \big((x \oplus y)\ \wedge\ \neg s\big).
$$

This mask identifies which bit positions generated a carry during addition.

### 4.2 Hinge bits (the grooves)

We restrict attention to hinge bit positions:

- **hinge_bits** = `[6, 7, 8, 19, 20, 21, 23, 28, 29, 30, 31]`  
- Bit indexing: **0 = LSB**, **31 = MSB**

For any 32-bit mask $m$, the hinge sample is:

$$
m_{\text{hinge}} = \big( (m\gg b) \wedge 1 \big)_{b \in \text{hinge\_bits}}.
$$

### 4.3 Hinge-sketch carry signature (Δ signature)

Model the $T_1$ add chain as four sequential adds:

1) $t_1 = h + \Sigma_1(e)$  
2) $t_2 = t_1 + \mathrm{Ch}(e,f,g)$  
3) $t_3 = t_2 + K_i$  
4) $t_4 = t_3 + W_i$ (this is $T_1$)

At each add step $s\in\{1,2,3,4\}$, compute:

$$
m^{(s)}_i = \mathrm{carry}(\text{lhs}^{(s)}_i,\ \text{rhs}^{(s)}_i)
$$

and extract hinge bits:

$$
\Delta(i,s) = \big(m^{(s)}_i\big)_{\text{hinge}}.
$$

For a chosen set of rounds $R$, concatenate:

$$
\Delta_{\text{signature}} = \bigoplus_{i\in R}\ \bigoplus_{s=1}^{4}\ \Delta(i,s)
$$

(Concatenation / packing, not XOR.)

Signature length:

$$
|\Delta_{\text{signature}}| = |R|\times 4 \times |\text{hinge\_bits}|\ \text{bits}.
$$

---

## 5. The XOR “spectrometer” (interference, not carry)

A separate fingerprint is hinge-bit XOR interference at round $i$:

$$
x(i,b) = h_b \oplus \Sigma_1(e)_b \oplus \mathrm{Ch}(e,f,g)_b \oplus W_i(b)
$$

for hinge bit $b$.

This yields **66 bits** for 6 rounds × 11 hinge bits (below). Empirically, this XOR signature is useful as a *fingerprint*, but does **not** form stable “universal emission lines” across random messages (Section 7).

---

## 6. Concrete extraction: message `b"!ABC"`

### 6.1 Basic facts

- **message**: `b"!ABC"`  
- **digest**: `74f38b3a9243996765732b34be5c56ac48d98d48b7fca2e37722b90032d6fa23`

### 6.2 66-bit XOR spectrograph

Rounds: `[0, 1, 2, 5, 16, 27]`  
Hinge bits: `[6, 7, 8, 19, 20, 21, 23, 28, 29, 30, 31]`

Per-round 11-bit groups (hinge order as listed):

- Round 0: `11100111010`
- Round 1: `01000000001`
- Round 2: `10110110000`
- Round 5: `11011101010`
- Round 16: `10110001101`
- Round 27: `00010011000`

Packed:

- **hex**: `0x39d201b61baac6898`

### 6.3 H-LOCK XOR mini-spectrum

H-LOCK rounds: `[5, 11, 22, 54]`

Per-round 11-bit groups:

- Round 5: `11011101010`
- Round 11: `01000100010`
- Round 22: `00000101001`
- Round 54: `01101001111`

Packed:

- **hex**: `0xdd488814b4f`

### 6.4 H-LOCK carry hinge signature (Δ-bus)

For each H-LOCK round $r\in\{5,11,22,54\}$, and each add step $s\in\{1,2,3,4\}$, we extract 11 hinge bits from the carry mask.

**Round 5**
- step 1 (`h + Σ1(e)`): `01100001110`
- step 2 (`+ Ch`):       `00011110011`
- step 3 (`+ K[5]`):     `11100011110`
- step 4 (`+ W[5]`):     `00000000000`

**Round 11**
- step 1: `01100010000`
- step 2: `00010001001`
- step 3: `11111101110`
- step 4: `00000000000`

**Round 22**
- step 1: `00011101111`
- step 2: `11111111000`
- step 3: `01100000011`
- step 4: `10011111100`

**Round 54**
- step 1: `11100110011`
- step 2: `11111111101`
- step 3: `00011001010`
- step 4: `11101110000`

Packed:

- **176-bit hex**: `0x61c3cf8f000620227f70001dffe181cfce67ff465770`

---

## 7. “Universal emission lines”: what’s stable across messages?

To test “universal lines,” measure:

$$
p_{r,s,b} = \Pr\big[\Delta(r,s)[b] = 1\big]
$$

over a corpus of random messages of fixed length (here: 4 bytes, $N=2000$).

### 7.1 Result: carry-hinge Δ has stable lines; XOR does not

- For the **XOR spectrometer**, no (round, hinge_bit) coordinate reached stability $p\le 0.05$ or $p\ge 0.95$.
- For the **carry-hinge Δ**, there are stable “lines” at a small set of coordinates.

Stable carry-hinge coordinates (threshold $p\le 0.05$ or $p\ge 0.95$):

| round $r$ | add step $s$ | hinge bit $b$ | $p_{r,s,b}$ |
|---:|---:|---:|---:|
| 5 | 3 | 8 | 0.9715 |
| 5 | 4 | 6 | 0.0000 |
| 5 | 4 | 7 | 0.0000 |
| 5 | 4 | 8 | 0.0000 |
| 5 | 4 | 19 | 0.0000 |
| 5 | 4 | 20 | 0.0000 |
| 5 | 4 | 21 | 0.0000 |
| 5 | 4 | 23 | 0.0000 |
| 5 | 4 | 28 | 0.0000 |
| 5 | 4 | 29 | 0.0000 |
| 5 | 4 | 30 | 0.0000 |
| 5 | 4 | 31 | 0.0000 |
| 11 | 3 | 23 | 0.0460 |
| 11 | 4 | 6 | 0.0000 |
| 11 | 4 | 7 | 0.0000 |
| 11 | 4 | 8 | 0.0000 |
| 11 | 4 | 19 | 0.0000 |
| 11 | 4 | 20 | 0.0000 |
| 11 | 4 | 21 | 0.0000 |
| 11 | 4 | 23 | 0.0000 |
| 11 | 4 | 28 | 0.0000 |
| 11 | 4 | 29 | 0.0000 |
| 11 | 4 | 30 | 0.0000 |
| 11 | 4 | 31 | 0.0000 |
| 22 | 3 | 19 | 0.0480 |

> Interpretation: these “lines” appear primarily in **step 4** (adding $W_i$) for rounds 5 and 11 for this length class, plus a few highly stable step-3 features (where adding $K_i$ injects deterministic stencil pressure).

### 7.2 Caveat (scope)

These stability results are **conditional** on:
- single-block messages
- a fixed message length (here 4 bytes)
- the specific hinge bit set

Different length classes can exhibit different stable features. “Universal” here means **universal within a boundary regime**, not universal for all possible inputs.

---

## 8. What this is good for (safe framing)

- **Leakage auditing / diagnostics**: quantify how much information about the input is present in Δ-style observables.
- **Comparator signatures**: build stable fingerprints for detecting execution regime changes (padding regimes, block boundaries, etc.).
- **Cross-domain analogy**: search for “constraint propagation scars” across other sequential constraint systems.

This document intentionally does **not** present a procedure for reconstructing unknown messages from hashes.

---

## 9. Appendix: invertibility of a round given $(W_i,K_i)$

Given the schedule word $W_i$ and constant $K_i$, the SHA-256 round update is bijective; the round function can be inverted algebraically. This supports the conceptual statement:

> If Δ observables constrain or reveal parts of the schedule, reverse reasoning about the internal state becomes possible.

---

## Reproducibility

All signatures above were computed from a reference single-block SHA-256 implementation and verified against `hashlib.sha256` for the digest.
