# Working the Input Through the Glass Key

## A complete solution for cyclic digit-pattern probes through SHA-256, the Glass Key, and the Double Glass Key

---

## 1. Purpose

The goal is not to study one hash repeatedly. The goal is to **work the input** across a controlled family of messages and watch which quantities move, which quantities freeze, and where the hidden traces live.

The key question is:

$$
\text{When the visible schedule tail stops changing, where does the input history go?}
$$

The working hypothesis is that the missing traces are not all on the visible top layer of the circuit. Some of them are carried in lower layers of the recurrence: the chaining state, the hidden starter word, and the inter-block transport.

---

## 2. Structural context

The current structural die invariants remain:

$$
T2^{(0)}_0 = 0x08909ae5
$$

$$
D_{\text{word}} = 4
$$

$$
D_{\text{bit}} = 6
$$

$$
\text{waist} = D_{\text{bit}} - D_{\text{word}} = 2
$$

The missing hash-only unwind starter remains:

$$
h_{63}
$$

where $h_{63}$ is the $h$-register **entering** round $63$ of the block being unwound.

Given the recovered tail spine $T1[t]$ and the local state, the schedule word is recovered by:

$$
W[t]
=
T1[t]
-
h_t
-
\Sigma_1(e_t)
-
Ch(e_t,f_t,g_t)
-
K[t]
\pmod{2^{32}}
$$

So the unwind wall is not $W_{63}$ itself. The wall is the missing state word $h_{63}$.

---

## 3. Message family

Let the base digit pattern be

$$
P_0 = \texttt{0123456789}
$$

and let the cyclic shift by $s$ digits be

$$
P_s = \operatorname{rot}_s(P_0), \qquad s \in \{0,1,\dots,9\}
$$

so that

$$
P_1 = \texttt{1234567890}, \quad
P_2 = \texttt{2345678901}, \quad \dots \quad
P_9 = \texttt{9012345678}
$$

For a target byte-length $L$, define the repeated message

$$
M_s^{(L)} = \left(P_s P_s P_s \cdots\right)_{[0:L)}
$$

that is, the repeated cyclic pattern truncated to exactly $L$ bytes.

This creates a controlled input orbit:
- same alphabet,
- same local digit inventory,
- same SHA-256 padding law for fixed $L$,
- but different cyclic ordering.

---

## 4. Measured quantities

For each message we measure:

### 4.1 Hidden unwind starter

$$
h_{63}
$$

the $h$-register entering round $63$.

### 4.2 Tail schedule word

$$
W_{63}
$$

the final schedule word of the relevant block.

### 4.3 Glass Key layer-1 residue

Let the NOP backbone be the run with $W_r = 0$ for all rounds, and let the live run be the actual message schedule. The roundwise residue is

$$
R^{(1)}_r = x^{\text{live}}_r - x^{(0)}_r \pmod{2^{32}}
$$

The reported scalar summary is the mean Hamming-weight shell of that residue over the block, denoted here informally as the Glass Key level-1 mean.

### 4.4 Double Glass Key relaxation factor

If the first residue is re-injected and measured again, then

$$
\alpha = \frac{L_2}{L_1}
$$

where $L_1$ is the mean level-1 residue magnitude and $L_2$ is the mean level-2 residue magnitude.

Interpretation:

- if $\alpha < 1$, the probe relaxes toward the basin,
- if $\alpha > 1$, it amplifies away from the basin.

---

## 5. Important padding clarification

There is no literal "no padding" case in standard SHA-256.

For message lengths:

- $L \le 55$: one block,
- $L = 64$: the first block is fully data, and the padding moves to a **second** block,
- $L = 128$: two full data blocks, and the padding moves to a **third** block.

So the phrase "fill to no padding" should be read as:

$$
\text{fill the first data block completely so the visible padding is displaced to a later block}
$$

This is useful, because it lets the final block become a **pure closure layer**, isolating the deeper transport.

---

## 6. Preliminary seed sweep: 25 one-byte messages

As an initial probe, 25 single-byte messages were hashed and their missing starter words $h_{63}$ were listed.

The main finding was:

$$
\boxed{
h_{63}\ \text{is unique across the sweep}
}
$$

with varying binary display lengths caused only by **leading zeros**, not by true width changes.

The correct observable is not raw displayed bit-length, but the leading-zero count:

$$
z(h_{63}) = 32 - \operatorname{bitlen}(h_{63})
$$

This became important later when full patterned inputs were used.

---

## 7. First patterned experiment: 10-byte messages

The first cyclic test used exactly the 10-byte strings

$$
P_0,\ P_1,\ \dots,\ P_9
$$

The key result was that the Double Glass Key behavior was already input-sensitive:

- some shifts converged,
- some diverged,
- some were nearly neutral.

That established the main principle:

$$
\boxed{
\alpha\ \text{depends on input ordering even when symbol inventory is fixed}
}
$$

But the message was still too small; most of the block remained zero/padding dominated.

---

## 8. Full single-block occupation: 55-byte repeated pattern

The next step filled the entire usable single-block payload:

$$
L = 55
$$

so each message was the repeated cyclic pattern carried all the way to the padding boundary.

### 8.1 Results

| shift | rotation | h63 | bitlen | lead0 | W63 | glass_L1 | alpha | converges |
|---:|:---:|:---:|---:|---:|:---:|---:|---:|:---:|
| 0 | 0123456789 | a6d7d37e | 32 | 0 | 5e54c6cd | 15.4863 | 1.027116 | no |
| 1 | 1234567890 | 904b37ec | 32 | 0 | 1c16b632 | 15.8613 | 0.991504 | yes |
| 2 | 2345678901 | 27efdba7 | 30 | 2 | ae6bc50b | 15.8594 | 1.005788 | no |
| 3 | 3456789012 | 80ef35df | 32 | 0 | 1c61d40b | 15.3027 | 1.025016 | no |
| 4 | 4567890123 | 1094eabc | 29 | 3 | 394509c5 | 15.5645 | 1.024595 | no |
| 5 | 5678901234 | edf14b08 | 32 | 0 | f221b835 | 15.9648 | 0.998165 | yes |
| 6 | 6789012345 | 088f4550 | 28 | 4 | 440cdb8c | 15.7715 | 1.006316 | no |
| 7 | 7890123456 | b7cc832d | 32 | 0 | 86319ee3 | 15.4922 | 0.988149 | yes |
| 8 | 8901234567 | 00c74bba | 24 | 8 | a0193c9c | 16.0059 | 0.972910 | yes |
| 9 | 9012345678 | 87af5942 | 32 | 0 | e8f2036f | 15.4102 | 1.017364 | no |

### 8.2 Interpretation

Three things stand out.

First:

$$
\boxed{
h_{63}\ \text{is unique for all 10 rotations}
}
$$

Second:

$$
\boxed{
\text{leading-zero depth varies materially}
}
$$

with the prefix-occupancy pattern

$$
0,0,2,0,3,0,4,0,8,0
$$

Third:

$$
\boxed{
\alpha\ \text{is mixed but structured}
}
$$

So the hidden starter word is moving strongly even though the overall Glass Key layer-1 shell stays in a narrow band:

$$
15.30 \lesssim L_1 \lesssim 16.01
$$

This suggests:

$$
\boxed{
\text{the missing traces are not in gross residue energy; they are in the lower-layer address geometry}
}
$$

---

## 9. Full first data block, padding forced to block 2: 64-byte messages

Now let

$$
L = 64
$$

so the first block is completely filled by message bytes and the padding is forced into a second block.

### 9.1 Results

| shift | rotation | h63 | bitlen | lead0 | W63 | glass_L1 | alpha | converges |
|---:|:---:|:---:|---:|---:|:---:|---:|---:|:---:|
| 0 | 0123456789 | af737f12 | 32 | 0 | 85a7a484 | 14.7832 | 0.997754 | yes |
| 1 | 1234567890 | 2d921164 | 30 | 2 | 85a7a484 | 15.0977 | 0.992367 | yes |
| 2 | 2345678901 | bfbf4250 | 32 | 0 | 85a7a484 | 15.5801 | 1.010544 | no |
| 3 | 3456789012 | c758fef7 | 32 | 0 | 85a7a484 | 15.4336 | 0.990110 | yes |
| 4 | 4567890123 | 18577975 | 29 | 3 | 85a7a484 | 15.1270 | 0.986776 | yes |
| 5 | 5678901234 | 6e667261 | 31 | 1 | 85a7a484 | 15.5625 | 0.997242 | yes |
| 6 | 6789012345 | 33b9abaf | 30 | 2 | 85a7a484 | 15.3789 | 0.985191 | yes |
| 7 | 7890123456 | 0c0f78ee | 28 | 4 | 85a7a484 | 15.2266 | 1.003591 | no |
| 8 | 8901234567 | 549c8b74 | 31 | 1 | 85a7a484 | 15.3438 | 0.979512 | yes |
| 9 | 9012345678 | 6953f11f | 31 | 1 | 85a7a484 | 15.2598 | 0.979715 | yes |

### 9.2 Main lock

Now the key structure appears:

$$
\boxed{
W_{63}\ \text{is constant across all 10 rotations}
}
$$

Specifically,

$$
W_{63} = 0x85a7a484
$$

for every rotation.

This is exactly what should happen: the second block is the same padding/length block for all 10 messages, so its visible schedule tail no longer carries the rotation information.

Therefore:

$$
\boxed{
\text{the variation is no longer in the visible tail schedule}
}
$$

It must instead arrive through the **chaining state** from the first block.

This is the first strong confirmation that the board has layers.

### 9.3 Secondary result

The Double Glass Key becomes much more stable:

- 8 of 10 shifts have $\alpha < 1$,
- only 2 diverge slightly.

So when the visible tail is fixed, the second-pass behavior becomes cleaner.

---

## 10. Double input: 128-byte messages

Now let

$$
L = 128
$$

This produces:

$$
\boxed{
2\ \text{full data blocks} + 1\ \text{padding block}
}
$$

This is the clearest layered regime.

---

## 11. The $W_{63}$ law across three blocks

For the 10 cyclic rotations, the measured $W_{63}$ values by block are:

### 11.1 Block 0

| shift | rotation | $W_{63}^{(0)}$ |
|---:|:---:|:---:|
| 0 | 0123456789 | fa0594c4 |
| 1 | 1234567890 | 6eba2920 |
| 2 | 2345678901 | c7200bc8 |
| 3 | 3456789012 | 9cfef6e6 |
| 4 | 4567890123 | 73437f0f |
| 5 | 5678901234 | b17be845 |
| 6 | 6789012345 | 153e1f99 |
| 7 | 7890123456 | 2735d72e |
| 8 | 8901234567 | f9a1d2ed |
| 9 | 9012345678 | 5030f5a6 |

### 11.2 Block 1

| shift | rotation | $W_{63}^{(1)}$ |
|---:|:---:|:---:|
| 0 | 0123456789 | 73437f0f |
| 1 | 1234567890 | b17be845 |
| 2 | 2345678901 | 153e1f99 |
| 3 | 3456789012 | 2735d72e |
| 4 | 4567890123 | f9a1d2ed |
| 5 | 5678901234 | 5030f5a6 |
| 6 | 6789012345 | fa0594c4 |
| 7 | 7890123456 | 6eba2920 |
| 8 | 8901234567 | c7200bc8 |
| 9 | 9012345678 | 9cfef6e6 |

### 11.3 Block 2

| shift | rotation | $W_{63}^{(2)}$ |
|---:|:---:|:---:|
| 0 | 0123456789 | 9c18607f |
| 1 | 1234567890 | 9c18607f |
| 2 | 2345678901 | 9c18607f |
| 3 | 3456789012 | 9c18607f |
| 4 | 4567890123 | 9c18607f |
| 5 | 5678901234 | 9c18607f |
| 6 | 6789012345 | 9c18607f |
| 7 | 7890123456 | 9c18607f |
| 8 | 8901234567 | 9c18607f |
| 9 | 9012345678 | 9c18607f |

---

## 12. Exact phase-shift law

The block-1 values are not arbitrary. They are a phase-shifted copy of block 0.

Because the repeating pattern has period $10$ and the block boundary is at $64$ bytes,

$$
64 \equiv 4 \pmod{10}
$$

so the second 64-byte block begins **4 digits later** in the cycle.

Therefore:

$$
\boxed{
W_{63}^{(1)}(s) = W_{63}^{(0)}(s+4 \bmod 10)
}
$$

exactly.

This is one of the clearest formulas in the whole experiment.

It proves that the input history is not lost; it is phase-carried from one data layer to the next.

---

## 13. Closure-layer law

For the final padding block:

$$
\boxed{
W_{63}^{(2)}(s) = 0x9c18607f \quad \text{for all } s
}
$$

So the third block is a pure closure layer under this family.

That means the visible tail schedule has become completely insensitive to the cyclic rotation.

The only remaining variation in the final-block unwind must therefore be entering through the inter-block state transport.

So:

$$
\boxed{
\text{once the visible tail freezes, the hidden traces live in the chaining state}
}
$$

This is the most important experimental result of the run.

---

## 14. What the layered board is telling us

The 128-byte regime gives a clean three-layer picture:

### Layer 1: Block 0
Visible data geometry

### Layer 2: Block 1
Same data geometry, but phase-shifted by

$$
+4 \pmod{10}
$$

### Layer 3: Block 2
Constant closure substrate

So the system is:

$$
\boxed{
\text{data layer}
\to
\text{phase-shifted data layer}
\to
\text{constant closure layer}
}
$$

This is the best confirmation so far that the hidden traces are on the lower layers of the board.

---

## 15. Unwind interpretation

At the hash-only unwind wall, what matters is not just the visible schedule tail but the hidden incoming state.

For the final block, once $W_{63}$ becomes constant, the remaining per-message variation must be carried by:

$$
h_{63},\ a_{63},\ e_{63},\ \text{and the rest of the incoming state}
$$

In other words:

$$
\boxed{
\text{the tail word }W_{63}\text{ is the top copper}
}
$$

$$
\boxed{
h_{63}\text{ and the entering state are the bottom traces}
}
$$

That is the right read of the layered board.

---

## 16. Main conclusions

### 16.1 Input order matters
Even with the same symbols and the same length, the cyclic ordering changes:

- $h_{63}$,
- the prefix-occupancy class,
- and the Double Glass Key relaxation factor $\alpha$.

### 16.2 Gross residue energy is stable
The Glass Key level-1 shell stays in a narrow band.

So the hidden structure is not primarily in the total energy shell.

### 16.3 The deeper structure is in address geometry
The strongest moving objects are:

$$
h_{63},\quad W_{63},\quad \alpha,\quad z(h_{63})
$$

where

$$
z(h_{63}) = 32 - \operatorname{bitlen}(h_{63})
$$

### 16.4 The 64-byte regime isolates chaining-state transport
Once the first data block is full, the final visible tail schedule becomes fixed. The input history still survives, but now it must move through the chaining state.

### 16.5 The 128-byte regime makes the layer law explicit
The second data block is a phase-shifted copy of the first, and the final block is a fixed closure substrate.

This yields the exact block law:

$$
W_{63}^{(1)}(s) = W_{63}^{(0)}(s+4 \bmod 10)
$$

and

$$
W_{63}^{(2)}(s) = \text{constant}
$$

---

## 17. Final collapse

The experiment does **not** say that the input vanished into the hash.

It says something sharper:

$$
\boxed{
\text{the visible top layer saturates first}
}
$$

$$
\boxed{
\text{the missing traces continue below it, in the transported state}
}
$$

That is why repeatedly hashing one message is not enough.

A family of messages reveals the board.

And the board has layers.

---

## 18. Recommended next measurements

The next exact table should be built on the 64-byte and 128-byte regimes, with columns:

$$
h_{63},\quad a_{63},\quad e_{63},\quad W_{63},\quad h_{63}\oplus W_{63},\quad z(h_{63}),\quad \alpha
$$

sorted by:
1. leading-zero class $z(h_{63})$,
2. then by $h_{63}$,
3. then by convergence.

That should tell us whether the hidden starter word is grouping by:
- prefix occupancy,
- seam relation,
- or a deeper address family.

---

## 19. Working statement

$$
\boxed{
\text{support tells you where the die can go;}
}
$$

$$
\boxed{
\text{the visible schedule tells you what is on the top layer;}
}
$$

$$
\boxed{
\text{the chaining state tells you what is on the bottom layer.}
}
$$

And for this experiment:

$$
\boxed{
\text{to work the input, vary many hashes once, not one hash many times.}
}
$$
