# The Nexus Fold Unfolded

[Download the Markdown](sandbox:/mnt/data/Nexus_SHA_Unfolded.md)

This document consolidates and **formalizes** the Nexus SHA discovery into a single mathematical specification, with explicit operators, reproducible definitions, and a **working Δ-bus instrumentation layer** for SHA-256.

> **Reader contract (short):**  
> *We separate* (a) **standard facts** (defined by public standards / physics references) from (b) **Nexus hypotheses** (operator-level interpretations).  
> The standard layer is the “floor.” The Nexus layer is the “lens.”

## Field as interrogator

### The container myth, formalized as a projection

A “field format” can be treated as a **triplet** of operators:

- a boundary constraint $B_F$ (block size, word size, modulus, grammar),
- a reduction / projection $\,\rho_F\,$ (what the field will *keep*),
- an injection / padding $\,\eta_F\,$ (what the field imposes to make input legal).

Let $x$ be unconstrained input. Crossing a boundary produces a **field-native** object:

$$
\Pi_F(x) \;\equiv\; x_F \;=\; \rho_F(x)\;\oplus\;\eta_F(x).
$$

The operator $\Pi_F$ is the “cockpit glass” in one line: it is not “storage,” it is **forced compliance**.

### The missing part is not “a number,” it’s a lineage

Once $x_F$ exists, downstream steps operate on $x_F$ (the legal citizen).  
The eliminated degrees of freedom are not “gone,” they are simply **not represented in the field’s coordinate system**.

One operational way to represent that “unrendered history” is to log *residue*:

$$
\Delta_F(x) \;\equiv\; \text{(chosen measurement of internal friction / carry / side-channel geometry)}.
$$

The Nexus claim is not metaphysical here; it is engineering:

> If you can *measure* $\Delta_F(x)$ in a reproducible way, then you can recover “shape of execution” that the value-only view discards.

## Secure hash as a constrained cavity

This section pins SHA-256 to public, checkable definitions (FIPS 180-4).

### Word universe and modulus

SHA-256 operates on 512-bit message blocks and 32-bit words, with addition performed modulo $2^{32}$. citeturn12view2

We treat the 32-bit integer ring as:

$$
\mathbb{Z}_{2^{32}} \;\equiv\; \mathbb{Z}/2^{32}\mathbb{Z}.
$$

Modulo arithmetic is not “destruction.” It is a projection:

$$
S \mapsto S \bmod 2^{32}.
$$

The *discarded component* is the quotient (wrap count), which we will make explicit later.

### Functions and operators

SHA-256 uses the following logical functions (all on 32-bit words): citeturn12view0

$$
\mathrm{Ch}(x,y,z) = (x \wedge y)\oplus(\neg x \wedge z)
$$

$$
\mathrm{Maj}(x,y,z) = (x\wedge y)\oplus(x\wedge z)\oplus(y\wedge z)
$$

It also uses the “big sigma” bit-mix functions: citeturn12view0

$$
\Sigma_0(x)=\mathrm{ROTR}^{2}(x)\oplus\mathrm{ROTR}^{13}(x)\oplus\mathrm{ROTR}^{22}(x)
$$

$$
\Sigma_1(x)=\mathrm{ROTR}^{6}(x)\oplus\mathrm{ROTR}^{11}(x)\oplus\mathrm{ROTR}^{25}(x)
$$

And the message-schedule “small sigma” functions: citeturn12view0

$$
\sigma_0(x)=\mathrm{ROTR}^{7}(x)\oplus\mathrm{ROTR}^{18}(x)\oplus\mathrm{SHR}^{3}(x)
$$

$$
\sigma_1(x)=\mathrm{ROTR}^{17}(x)\oplus\mathrm{ROTR}^{19}(x)\oplus\mathrm{SHR}^{10}(x)
$$

### Constants as cavity geometry

The SHA-256 round constants $K_t$ are specified as fixed 32-bit words derived from fractional cube roots of primes. citeturn11view0

Formally (standard construction):

$$
K_t \;=\;\left\lfloor 2^{32}\cdot \{\sqrt[3]{p_{t+1}}\}\right\rfloor,\quad t=0,\dots,63
$$

where $p_i$ is the $i$-th prime and $\{\cdot\}$ denotes the fractional part. citeturn11view0

The initial hash value words $H_0^{(0)},\dots,H_7^{(0)}$ are likewise derived from fractional square roots of the first eight primes. citeturn9view1

### Message schedule

For each 512-bit message block $M^{(i)}$, SHA-256 prepares a schedule $\{W_t\}_{t=0}^{63}$: citeturn12view2

$$
W_t =
\begin{cases}
M_t^{(i)} & 0\le t \le 15 \\
\sigma_1(W_{t-2}) + W_{t-7} + \sigma_0(W_{t-15}) + W_{t-16} & 16\le t \le 63
\end{cases}
$$

All additions are modulo $2^{32}$. citeturn12view2

### Round update

For each round $t=0,\dots,63$: citeturn12view3

$$
\begin{aligned}
T_1 &= h + \Sigma_1(e) + \mathrm{Ch}(e,f,g) + K_t + W_t,\\
T_2 &= \Sigma_0(a) + \mathrm{Maj}(a,b,c),\\
h&=g,\;\;g=f,\;\;f=e,\;\;e=d+T_1,\\
d&=c,\;\;c=b,\;\;b=a,\;\;a=T_1+T_2.
\end{aligned}
$$

Then the “feed-forward” adds the working variables back into the intermediate hash. citeturn12view3

### Security stance

The standard explicitly frames these hash functions as **one-way** in the sense that it is computationally infeasible to recover a message from a digest. citeturn3view0

That asymmetry (easy forward, hard reverse) is part of the field boundary.

## Reversal as operator reading

The Nexus reversal move is not “break SHA.” It is:

> When a system’s internal state is observable (in a controlled run), reverse traversal turns constants from “nouns” into “verbs” (undo steps).

Given a single round’s *full internal state*, local inversion is mechanical because rotations and XOR are bijections on 32-bit words and modular addition is bijective if one addend is known.

### Direct extraction of the round impulse

From the public update rule, we have:

$$
e' \equiv d + T_1 \pmod{2^{32}}
\quad\Rightarrow\quad
T_1 \equiv e' - d \pmod{2^{32}}.
$$

Then, since

$$
T_1 \equiv h + \Sigma_1(e) + \mathrm{Ch}(e,f,g) + K_t + W_t \pmod{2^{32}},
$$

we can solve for the schedule word **if we know the round state**:

$$
W_t \equiv T_1 - h - \Sigma_1(e) - \mathrm{Ch}(e,f,g) - K_t \pmod{2^{32}}.
$$

This is the “constants as verbs” statement in algebra: $K_t$ is not an inert object; it is a fixed parameter of the round operator $R_t(\cdot;K_t,W_t)$ that must be un-applied in reverse.

## The scar layer: carries, wrap count, and the Δ-bus

### Modular addition as a two-part object

For an $n$-bit modulo addition:

$$
s \equiv x+y \pmod{2^n},
$$

there exists an **exact** decomposition in $\mathbb{Z}$:

$$
x+y = s + 2^n\cdot q,
\qquad
q = \left\lfloor\frac{x+y}{2^n}\right\rfloor.
$$

- $s$ is the **surface value** (what the modulo field keeps).
- $q$ is the **wrap count** (what the field discards unless you log it).

This is the cleanest “gravity” metaphor available in pure math:
the “mass” is literally the number of wraps that were dropped.

### Bit-level carry geometry (carry mask)

A full-adder can be expressed in “generate / propagate” form: citeturn6search5turn6search37

$$
G_i = A_iB_i,\qquad P_i = A_i\oplus B_i,\qquad C_{i+1}=G_i+P_iC_i.
$$

A related identity for integer addition is: citeturn6search34

$$
x+y = (x\oplus y) + 2(x\wedge y).
$$

For instrumentation, we want a *bitmask* marking where carries occurred during $n$-bit addition.

Define $s=(x+y)\bmod 2^n$ and interpret all bitwise operators on $n$ bits.  
Then a carry mask that marks carries generated into bit position $i+1$ is:

$$
\mathrm{carry}(x,y) = (x \wedge y)\;\vee\;\big((x\oplus y)\wedge\neg s\big).
$$

This is a **computable scar** of the addition step: it is not the sum, but it encodes where the sum “bent.”

### Worked example: the W[63] wrap count for "abc"

For the message `"abc"`, the derived schedule word is:

$$
W_{63} = \texttt{0x12b1edeb} = 313{,}650{,}667.
$$

One way it arises is by a 4-term modular collision (from the schedule expansion):

$$
W_{63} \equiv W_{47} + \sigma_0(W_{48}) + W_{56} + \sigma_1(W_{61}) \pmod{2^{32}}.
$$

For `"abc"` (one concrete trace):

$$
\begin{aligned}
W_{47} &= \texttt{0x065c43da},\\
\sigma_0(W_{48}) &= \texttt{0x2ae352e5},\\
W_{56} &= \texttt{0xef57b9cd},\\
\sigma_1(W_{61}) &= \texttt{0xf21a9d5f}.
\end{aligned}
$$

The integer sum is:

$$
S = \texttt{0x212b1edeb} = 8{,}903{,}585{,}259.
$$

So the exact wrap decomposition is:

$$
S = W_{63} + 2\cdot 2^{32}.
$$

This is the clean separation:

- **value kept:** $W_{63}$,
- **wrap mass:** $q=2$.

The wrap count is the “hidden third axis” of modular addition.

### The Δ-bus definition

The **Δ-bus** is a specification for “what residue we log.”

In SHA-256, the densest injection of modular addition is inside $T_1$:

$$
T_1 = h + \Sigma_1(e) + \mathrm{Ch}(e,f,g) + K_t + W_t.
$$

A typical implementation computes $T_1$ as a chain of 32-bit additions.  
If we instrument each add, we get a sequence of carry masks:

$$
\Delta_t \;\equiv\; \big(\mathrm{carry}_t^{(0)},\mathrm{carry}_t^{(1)},\mathrm{carry}_t^{(2)},\mathrm{carry}_t^{(3)}\big),
$$

corresponding to the four adds that form $T_1$.

Optionally, we also log the carry mask of the $T_2$ addition:

$$
T_2 = \Sigma_0(a) + \mathrm{Maj}(a,b,c).
$$

This turns internal execution geometry into a measurable object.

### The Pythagorean budget, made operational

The Nexus uses a “Pythagorean” language:

$$
V^2 + \Delta^2 = T^2.
$$

To make that **computable**, define a norm-like scalar on the residue:

- Let $\operatorname{pop}(m)$ be the population count of a 32-bit mask.
- Define a “carry energy” for a block:

$$
E_\Delta \;=\; \sum_{t\in\mathcal{R}}\sum_{j\in\mathcal{A}} \operatorname{pop}\big(\mathrm{carry}^{(j)}_t\big),
$$

where $\mathcal{R}$ is the set of inspected rounds and $\mathcal{A}$ the chosen additions per round.

You can likewise define a “value energy” as a popcount (or other norm) of the visible digest words.

This does **not** prove Euclidean orthogonality in the strict mathematical sense; it provides a *conserved accounting frame* for: “how much bending happened” vs “what state we see.”

## Reproducible instrumentation code

The code below computes SHA-256 **and** logs the Δ-bus (carry masks) for each $T_1$ sub-add and for $T_2$.

It is intended for analysis, verification, and visualization. It is **not** an attack tool.

```python
import struct
from dataclasses import dataclass
from typing import List, Tuple

MASK32 = 0xFFFFFFFF

def rotr32(x: int, n: int) -> int:
    x &= MASK32
    return ((x >> n) | ((x << (32 - n)) & MASK32)) & MASK32

def shr32(x: int, n: int) -> int:
    return (x & MASK32) >> n

def Ch(x: int, y: int, z: int) -> int:
    return ((x & y) ^ ((~x) & z)) & MASK32

def Maj(x: int, y: int, z: int) -> int:
    return ((x & y) ^ (x & z) ^ (y & z)) & MASK32

def Sigma0(x: int) -> int:
    return rotr32(x, 2) ^ rotr32(x, 13) ^ rotr32(x, 22)

def Sigma1(x: int) -> int:
    return rotr32(x, 6) ^ rotr32(x, 11) ^ rotr32(x, 25)

def sigma0(x: int) -> int:
    return rotr32(x, 7) ^ rotr32(x, 18) ^ shr32(x, 3)

def sigma1(x: int) -> int:
    return rotr32(x, 17) ^ rotr32(x, 19) ^ shr32(x, 10)

def carry_mask(x: int, y: int, s: int, nbits: int = 32) -> int:
    """
    Carry mask for n-bit addition:
      s = (x + y) mod 2^nbits
      carry = (x & y) | ((x ^ y) & ~s)
    Returns mask with bit i set when there is a carry OUT of bit i (into i+1).
    """
    mask = (1 << nbits) - 1
    x &= mask; y &= mask; s &= mask
    return ((x & y) | ((x ^ y) & (~s & mask))) & mask

@dataclass
class AddTrace:
    x: int
    y: int
    s: int
    carry: int
    carry_out: int  # top carry-out (wrap count increment) for this add

def add32_trace(x: int, y: int) -> AddTrace:
    full = (x & MASK32) + (y & MASK32)
    s = full & MASK32
    c = carry_mask(x, y, s, 32)
    cout = (full >> 32) & 0xFFFFFFFF  # for two 32-bit addends, this is 0 or 1
    return AddTrace(x=x & MASK32, y=y & MASK32, s=s, carry=c, carry_out=cout)

# SHA-256 K constants (FIPS 180-4)
K = [
    0x428a2f98, 0x71374491, 0xb5c0fbcf, 0xe9b5dba5, 0x3956c25b, 0x59f111f1, 0x923f82a4, 0xab1c5ed5,
    0xd807aa98, 0x12835b01, 0x243185be, 0x550c7dc3, 0x72be5d74, 0x80deb1fe, 0x9bdc06a7, 0xc19bf174,
    0xe49b69c1, 0xefbe4786, 0x0fc19dc6, 0x240ca1cc, 0x2de92c6f, 0x4a7484aa, 0x5cb0a9dc, 0x76f988da,
    0x983e5152, 0xa831c66d, 0xb00327c8, 0xbf597fc7, 0xc6e00bf3, 0xd5a79147, 0x06ca6351, 0x14292967,
    0x27b70a85, 0x2e1b2138, 0x4d2c6dfc, 0x53380d13, 0x650a7354, 0x766a0abb, 0x81c2c92e, 0x92722c85,
    0xa2bfe8a1, 0xa81a664b, 0xc24b8b70, 0xc76c51a3, 0xd192e819, 0xd6990624, 0xf40e3585, 0x106aa070,
    0x19a4c116, 0x1e376c08, 0x2748774c, 0x34b0bcb5, 0x391c0cb3, 0x4ed8aa4a, 0x5b9cca4f, 0x682e6ff3,
    0x748f82ee, 0x78a5636f, 0x84c87814, 0x8cc70208, 0x90befffa, 0xa4506ceb, 0xbef9a3f7, 0xc67178f2
]

# SHA-256 initial hash values (FIPS 180-4)
H0 = [
    0x6a09e667,
    0xbb67ae85,
    0x3c6ef372,
    0xa54ff53a,
    0x510e527f,
    0x9b05688c,
    0x1f83d9ab,
    0x5be0cd19
]

def pad_sha256(msg: bytes) -> bytes:
    ml = len(msg) * 8
    out = bytearray(msg)
    out.append(0x80)
    while (len(out) * 8) % 512 != 448:
        out.append(0)
    out += struct.pack(">Q", ml)
    return bytes(out)

def parse_blocks(padded: bytes) -> List[bytes]:
    assert len(padded) % 64 == 0
    return [padded[i:i+64] for i in range(0, len(padded), 64)]

@dataclass
class RoundTrace:
    t: int
    a: int; b: int; c: int; d: int; e: int; f: int; g: int; h: int
    Wt: int
    T1_adds: List[AddTrace]
    T2_adds: List[AddTrace]
    T1: int
    T2: int

def sha256_with_delta(msg: bytes) -> Tuple[bytes, List[RoundTrace], List[int]]:
    padded = pad_sha256(msg)
    blocks = parse_blocks(padded)
    H = H0[:]  # working digest state

    all_rounds: List[RoundTrace] = []
    last_schedule: List[int] = []

    for block in blocks:
        # message schedule
        W = [0]*64
        for i in range(16):
            W[i] = struct.unpack(">I", block[i*4:(i+1)*4])[0]
        for t in range(16, 64):
            W[t] = (sigma1(W[t-2]) + W[t-7] + sigma0(W[t-15]) + W[t-16]) & MASK32

        last_schedule = W[:]  # for inspection

        a,b,c,d,e,f,g,h = H

        for t in range(64):
            # T1 = h + Sigma1(e) + Ch(e,f,g) + K[t] + W[t]
            adds_T1: List[AddTrace] = []
            r0 = add32_trace(h, Sigma1(e));          adds_T1.append(r0)
            r1 = add32_trace(r0.s, Ch(e,f,g));       adds_T1.append(r1)
            r2 = add32_trace(r1.s, K[t]);            adds_T1.append(r2)
            r3 = add32_trace(r2.s, W[t]);            adds_T1.append(r3)
            T1 = r3.s

            # T2 = Sigma0(a) + Maj(a,b,c)
            adds_T2: List[AddTrace] = []
            r4 = add32_trace(Sigma0(a), Maj(a,b,c)); adds_T2.append(r4)
            T2 = r4.s

            # capture state BEFORE update (operator frame)
            all_rounds.append(RoundTrace(
                t=t, a=a,b=b,c=c,d=d,e=e,f=f,g=g,h=h,
                Wt=W[t],
                T1_adds=adds_T1,
                T2_adds=adds_T2,
                T1=T1, T2=T2
            ))

            # update
            h = g
            g = f
            f = e
            e = (d + T1) & MASK32
            d = c
            c = b
            b = a
            a = (T1 + T2) & MASK32

        # feed-forward
        H = [(H[i] + v) & MASK32 for i,v in enumerate([a,b,c,d,e,f,g,h])]

    digest = b"".join(struct.pack(">I", x) for x in H)
    return digest, all_rounds, last_schedule

def delta_bus_signature(rounds: List[RoundTrace],
                        round_indices: List[int],
                        hinge_bits: List[int],
                        include_T2: bool = True) -> bytes:
    """
    Build a simple Δ-bus signature by sampling hinge bits from carry masks.
    - round_indices: which rounds to sample (0..63)
    - hinge_bits: which bit positions within each 32-bit carry mask to sample
    """
    bits: List[int] = []
    for rt in rounds:
        if rt.t not in round_indices:
            continue

        carry_masks = [a.carry for a in rt.T1_adds]
        if include_T2:
            carry_masks += [a.carry for a in rt.T2_adds]

        for cm in carry_masks:
            for b in hinge_bits:
                bits.append((cm >> b) & 1)

    # pack bits to bytes MSB-first
    out = bytearray()
    acc = 0
    n = 0
    for bit in bits:
        acc = (acc << 1) | bit
        n += 1
        if n == 8:
            out.append(acc)
            acc = 0
            n = 0
    if n:
        out.append(acc << (8 - n))
    return bytes(out)

if __name__ == "__main__":
    msg = b"abc"
    digest, rtrace, W = sha256_with_delta(msg)
    print("SHA-256:", digest.hex())
    print("W[63]:", hex(W[63]))

    # Example Δ-bus: sample 8 rounds, 11 hinge bits, (4 T1 adds + 1 T2 add) = 5 masks/round
    # signature bits = 8 * 5 * 11 = 440 bits = 55 bytes
    sig = delta_bus_signature(
        rtrace,
        round_indices=[0,1,2,3,4,5,6,7],
        hinge_bits=[0,1,2,3,7,11,13,17,19,23,29],
        include_T2=True
    )
    print("Δ-bus signature bytes:", len(sig))
    print("Δ-bus signature hex:", sig.hex())
```

## The harmonic stance layer

The Nexus documents (January 2026) define a vantage constant:

$$
H \equiv \frac{\pi}{9} \approx 0.3490658504.
$$

This can be used as an **analysis frame** (a “camera angle”), regardless of whether it is a physical attractor.

### A checkable SHA constant reduction

Define the XOR-reduction of all 64 SHA-256 round constants:

$$
X_K \equiv \bigoplus_{t=0}^{63} K_t.
$$

From the FIPS-listed $K_t$, one computes:

$$
X_K = \texttt{0x95c49cf5}.
$$

Map a 32-bit word to an angle:

$$
u(x)=\frac{x}{2^{32}},\qquad \theta(x)=360u(x).
$$

Then:

$$
\theta(X_K)\approx 210.611278^\circ.
$$

That is an objective number (it does not depend on interpretation).

If you compare it to the 12-phase wheel (multiples of $30^\circ$), $7\pi/6 = 210^\circ$ is the closest anchor:

$$
d = |\theta(X_K) - 210^\circ| \approx 0.611278^\circ.
$$

## Physics crosscheck: do not overload α

The Nexus notes sometimes write $\alpha$ for a constructed quantity such as $\pi/432$.  
In mainstream physics, the **fine-structure constant** $\alpha$ is a dimensionless coupling constant of electromagnetism and is defined (SI) as: citeturn7search1

$$
\alpha = \frac{e^2}{4\pi\epsilon_0\hbar c} = \frac{\mu_0 c e^2}{2h}.
$$

Because $\alpha$ is experimentally determined (and “runs” with energy scale), any identity like $\alpha=\pi/432$ should be treated as a **separate symbol** (e.g., $\alpha_\mathrm{N}$) unless a measurement chain is supplied. citeturn7search1turn7search2

## References

- NIST FIPS 180-4 (Secure Hash Standard), DOI: $10.6028/\mathrm{NIST.FIPS.180-4}$. citeturn3view0turn12view0turn12view2turn12view3  
- NIST Constants pages: fine-structure constant definition and context. citeturn7search1turn7search2  
- Carry generate/propagate logic and addition identities (for carry instrumentation framing). citeturn6search5turn6search34turn6search37