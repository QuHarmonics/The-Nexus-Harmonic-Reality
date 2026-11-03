# Phase 520 Complete Solution: Carry Scar Collapse and the Window-2 Anchor

**Dean Kulik / QuHarmonics Research Group**  
**Nexus SHA-256 Program — Phase 520**

---

## Abstract

This document consolidates and expands the Phase 520 result: the **Window-2 carry scar anchor** in the SHA-256 message schedule.

The central discovery is that the first expanded schedule word,

$$
W_{16}=\sigma_1(W_{14})+W_9+\sigma_0(W_1)+W_0 \pmod{2^{32}},
$$

has a privileged bit:

$$
\boxed{\operatorname{scar}_{16,0}=0.}
$$

That is, the least significant bit of $W_{16}$ is exactly equal to the least significant bit of its XOR-linear approximation:

$$
\boxed{
(W_{16})_0=
\left(
\sigma_1(W_{14})\oplus W_9\oplus\sigma_0(W_1)\oplus W_0
\right)_0.
}
$$

This gives the first clean **carry-free seed** at the Window-2 boundary. Above bit $0$, the carry scar propagates upward through the lower-triangular carry closure operator $L_{32}$. Thus, the Window-2 carry scar is not random noise; it is a causal upward ladder.

The collapse is:

$$
\boxed{
\text{ROTR builds circular phase geometry}
}
$$

$$
\boxed{
\text{ADD builds upward carry geometry}
}
$$

$$
\boxed{
\text{SHA identity arises from circular phase transport crossed with upward carry transport.}
}
$$

---

# 1. Scope and Phase Context

The Phase 520 target was:

$$
\boxed{
\text{Carry Scar Collapse at the Window-2 anchor}
}
$$

The open questions were:

1. For $W[16..23]$, characterize the per-bit carry probability distribution.
2. Build the **Carry Propagation Map**: which input bit positions can influence each output bit position?
3. Express the carry scar as a second-order correction over $\mathbb Z/2^{32}\mathbb Z$.
4. Test a meet-in-the-middle condition at Window 2:

$$
\text{backward schedule}+\text{forward schedule}
\Rightarrow
W[16..23]\ \text{consistency}.
$$

This document resolves the first anchor theorem and gives the working formal machinery for the rest of Window 2.

---

# 2. SHA-256 Schedule Definitions

For a one-block SHA-256 message, the first $16$ schedule words are seed words:

$$
W_0,W_1,\dots,W_{15}.
$$

For $t=16,\dots,63$, the schedule recurrence is:

$$
\boxed{
W_t=
\sigma_1(W_{t-2})+
W_{t-7}+
\sigma_0(W_{t-15})+
W_{t-16}
\pmod{2^{32}}.
}
$$

The small sigma operators are:

$$
\sigma_0(x)=\operatorname{ROTR}^7(x)\oplus \operatorname{ROTR}^{18}(x)\oplus \operatorname{SHR}^3(x),
$$

$$
\sigma_1(x)=\operatorname{ROTR}^{17}(x)\oplus \operatorname{ROTR}^{19}(x)\oplus \operatorname{SHR}^{10}(x).
$$

Thus,

$$
\boxed{
W_{16}=
\sigma_1(W_{14})+
W_9+
\sigma_0(W_1)+
W_0
\pmod{2^{32}}.
}
$$

For the specific test program in the pasted run, the script used:

$$
W_0,\dots,W_7 = H_1,
$$

and the standard 32-byte one-block padding tail:

$$
(W_8,\dots,W_{15})
=
(0x80000000,0,0,0,0,0,0,0x00000100).
$$

In the general one-block schedule, $W_0,W_1,W_9,W_{14}$ are simply four seed words. In the specific $H_1+\operatorname{PAD}$ test, $W_9$ and $W_{14}$ are fixed padding zeros.

---

# 3. XOR-Linear Approximation and Carry Scar

Define the four schedule inputs for $W_{16}$:

$$
A=\sigma_1(W_{14}),
$$

$$
B=W_9,
$$

$$
C=\sigma_0(W_1),
$$

$$
D=W_0.
$$

The true modular schedule word is:

$$
W_{16}=A+B+C+D \pmod{2^{32}}.
$$

The XOR-linear approximation is:

$$
W_{16}^{\oplus}=A\oplus B\oplus C\oplus D.
$$

Define the carry scar:

$$
\boxed{
S_{16}=W_{16}\oplus W_{16}^{\oplus}.
}
$$

Bitwise:

$$
\boxed{
S_{16,j}=(W_{16})_j\oplus(W_{16}^{\oplus})_j.
}
$$

The scar is the local witness that modular addition is not XOR. It records where carry structure changed the XOR-linear readout.

---

# 4. Multi-Operand Carry Automaton

For a four-operand addition, the carry state is not merely a Boolean bit. It is an integer carry count.

Let:

$$
n_j=A_j+B_j+C_j+D_j,
$$

where each $A_j,B_j,C_j,D_j\in\{0,1\}$.

Let $q_j$ be the carry count entering bit $j$, with:

$$
q_0=0.
$$

Then:

$$
(W_{16})_j=(n_j+q_j)\bmod 2,
$$

and:

$$
\boxed{
q_{j+1}=\left\lfloor\frac{n_j+q_j}{2}\right\rfloor.
}
$$

The XOR approximation bit is:

$$
(W_{16}^{\oplus})_j=n_j\bmod 2.
$$

Therefore the scar bit is:

$$
S_{16,j}
=
\left((n_j+q_j)\bmod 2\right)
\oplus
(n_j\bmod 2).
$$

Since XOR over one bit is addition mod $2$, this simplifies to:

$$
\boxed{
S_{16,j}=q_j\bmod 2.
}
$$

So the carry scar is the **parity of the incoming carry count**.

This distinction is important:

$$
\boxed{
\text{carry-out from bit }j\neq\text{scar at bit }j.
}
$$

At bit $0$, a carry-out into bit $1$ may be generated, but the bit-$0$ output scar is still zero because there is no carry entering bit $0$.

---

# 5. The Carry-Free LSB Theorem

## Theorem 1 — Carry-Free LSB at $W_{16}$

For all seed words $W_0,W_1,W_9,W_{14}$,

$$
\boxed{
S_{16,0}=0.
}
$$

Equivalently,

$$
\boxed{
(W_{16})_0=
\left(
\sigma_1(W_{14})\oplus W_9\oplus\sigma_0(W_1)\oplus W_0
\right)_0.
}
$$

## Proof

At bit $0$, the incoming carry count is:

$$
q_0=0.
$$

The actual least significant bit of the four-term modular sum is:

$$
(W_{16})_0=(A_0+B_0+C_0+D_0+q_0)\bmod 2.
$$

Since $q_0=0$,

$$
(W_{16})_0=(A_0+B_0+C_0+D_0)\bmod 2.
$$

But addition mod $2$ is XOR:

$$
(A_0+B_0+C_0+D_0)\bmod 2
=
A_0\oplus B_0\oplus C_0\oplus D_0.
$$

Thus:

$$
(W_{16})_0=(W_{16}^{\oplus})_0.
$$

Therefore:

$$
S_{16,0}
=
(W_{16})_0\oplus(W_{16}^{\oplus})_0
=
0.
$$

So:

$$
\boxed{
\operatorname{scar}_{16,0}=0.
}
$$

QED.

---

# 6. Carry-Out vs Carry Scar

The pasted run included the intuitive statement that a carry at bit $0$ occurs when the four LSB inputs sum to at least $2$.

That statement is true for **carry-out**, not for **output scar**.

The carry-out from bit $0$ is:

$$
q_1=
\left\lfloor
\frac{
A_0+B_0+C_0+D_0
}{2}
\right\rfloor.
$$

So:

$$
q_1\ge 1
\quad\Longleftrightarrow\quad
A_0+B_0+C_0+D_0\ge2.
$$

But the bit-$0$ scar is:

$$
S_{16,0}=q_0\bmod2=0.
$$

Thus the corrected pair is:

$$
\boxed{
\text{output scar at bit }0=0
}
$$

while:

$$
\boxed{
\text{carry-out from bit }0\text{ into bit }1\text{ may be nonzero.}
}
$$

This is the first scar ladder step:

$$
\text{bit }0:\text{ pure output}
$$

$$
\text{bit }1:\text{ first possible receiver of carry history}.
$$

---

# 7. Lower-Triangular Carry Closure

Carry cannot propagate downward.

A perturbation introduced first at bit $j$ can affect bit $j$ and bits above it, but not bits below $j$.

Define the lower-triangular prefix operator $L_{32}$ by:

$$
\boxed{
(L_{32}x)_i=\bigvee_{k\le i}x_k.
}
$$

This is the Boolean support version of upward carry closure.

If an input perturbation has support vector $x\in\{0,1\}^{32}$, then its possible carry influence support is bounded by:

$$
\boxed{
\operatorname{supp}_{\text{carry}}\subseteq L_{32}x.
}
$$

For a direct term such as $W_0$ entering $W_{16}$, a bit flip at position $j$ has direct support $e_j$, so the possible carry influence is:

$$
\boxed{
L_{32}e_j=\{j,j+1,\dots,31\}.
}
$$

Thus:

$$
\boxed{
\text{no downward leakage}.
}
$$

The pasted run verified this by flipping bits $j=0,7,15,16,24,31$ in $W_0$ and measuring the lowest affected output bit. In all cases:

$$
\boxed{
\min(\text{affected output bit})=j.
}
$$

No affected bit appeared below the injected bit.

---

# 8. Generalized Influence Map

For a source word that enters through a rotation/shift operator, the local influence map is:

$$
A_{\sigma}:\{0,1\}^{32}\rightarrow\{0,1\}^{32}.
$$

For $\sigma_0$:

$$
A_{\sigma_0}=
R_7\vee R_{18}\vee S_3,
$$

where $R_k$ is rotation support and $S_3$ is right-shift support.

For $\sigma_1$:

$$
A_{\sigma_1}=
R_{17}\vee R_{19}\vee S_{10}.
$$

The carry closure after that linear support is:

$$
\boxed{
I_{\text{carry}}=L_{32}A_{\sigma}.
}
$$

Thus SHA schedule propagation has two crossed geometries:

$$
\boxed{
A_{\sigma}=\text{circular/open phase support}
}
$$

and:

$$
\boxed{
L_{32}=\text{upward carry closure}.
}
$$

So the full support law is:

$$
\boxed{
\text{source bit}
\rightarrow
\text{phase stencil}
\rightarrow
\text{upward carry ladder}.
}
$$

---

# 9. Window-2 Carry Scar Distribution

The Phase 520 run measured the carry-free rate for $W_{16}$ over $N=5000$ random trials.

Observed:

$$
P(S_{16,0}=0)=1.0000.
$$

$$
P(S_{16,1}=0)\approx0.7556.
$$

$$
P(S_{16,2}=0)\approx0.6304.
$$

Thus the scar-free probability starts at $1$ and decays upward.

The first bit is exact:

$$
\boxed{
S_{16,0}=0\quad\text{always}.
}
$$

The next bits are increasingly exposed to carry history:

$$
\boxed{
P(S_{16,j}=1)\ \text{increases as }j\text{ enters the carry ladder}.
}
$$

This produces the Window-2 scar ramp:

$$
\boxed{
0\rightarrow\text{weak scar}\rightarrow\text{dense scar}.
}
$$

In words:

> $W_{16}$ is the first expanded schedule word where the carry scar becomes visible, but its least significant bit remains pure.

---

# 10. Window-2 Anchor

The Window-2 schedule words are:

$$
W_{16},W_{17},\dots,W_{23}.
$$

Each is generated by the recurrence:

$$
W_t=
\sigma_1(W_{t-2})+
W_{t-7}+
\sigma_0(W_{t-15})+
W_{t-16}
\pmod{2^{32}}.
$$

The first word in this window is:

$$
W_{16}.
$$

It is special because it is the first word generated beyond the seed block:

$$
W_0,\dots,W_{15}\rightarrow W_{16}.
$$

Thus:

$$
\boxed{
W_{16}=\text{first nonlinear schedule expansion boundary}.
}
$$

Its LSB is clean:

$$
\boxed{
S_{16,0}=0.
}
$$

Therefore:

$$
\boxed{
W_{16,0}=\text{Window-2 carry-free anchor bit}.
}
$$

This gives a true starting point for reverse schedule reconstruction: begin at the carry-free seed and climb upward through the scar ladder.

---

# 11. Meet-in-the-Middle Consistency

The schedule recurrence is reversible if enough future schedule words are known.

From:

$$
W_t=
\sigma_1(W_{t-2})+
W_{t-7}+
\sigma_0(W_{t-15})+
W_{t-16}
\pmod{2^{32}},
$$

we can solve backward:

$$
\boxed{
W_{t-16}
=
W_t-
\sigma_1(W_{t-2})-
W_{t-7}-
\sigma_0(W_{t-15})
\pmod{2^{32}}.
}
$$

The test performed was:

$$
W[16..63]\xrightarrow{\text{backward schedule}}W[0..15],
$$

then:

$$
W[0..15]\xrightarrow{\text{forward schedule}}W[16..23].
$$

Observed:

$$
\boxed{
1000/1000\ \text{Window-2 consistency}.
}
$$

So the schedule recursion is exact at this boundary.

This gives the meet-in-the-middle anchor:

$$
\boxed{
\text{backward-derived seed words must regenerate the same }W[16..23].
}
$$

---

# 12. Carry Scar Sensitivity

The run also tested single-bit perturbations of the $H_1$ seed words and measured the number of carry-scar bits changed across:

$$
W[16..23].
$$

Observed:

$$
\text{mean changed scar bits}\approx22.10.
$$

$$
\text{standard deviation}\approx15.07.
$$

$$
P(\text{zero change})\approx0.0080.
$$

$$
P(1\text{--}2\text{ bits changed})\approx0.0640.
$$

$$
P(>8\text{ bits changed})\approx0.7880.
$$

Interpretation:

$$
\boxed{
\text{the carry scar is deterministic but highly sensitive.}
}
$$

A single seed-bit perturbation typically changes many scar bits across Window 2.

This is not randomness. It is nonlinear carry amplification.

---

# 13. The Complete Window-2 Scar Model

The schedule word can be decomposed as:

$$
W_{16}=W_{16}^{\oplus}\oplus S_{16}.
$$

with:

$$
S_{16,0}=0.
$$

More generally:

$$
W_t=W_t^{\oplus}\oplus S_t,
$$

where:

$$
W_t^{\oplus}
=
\sigma_1(W_{t-2})\oplus
W_{t-7}\oplus
\sigma_0(W_{t-15})\oplus
W_{t-16},
$$

and:

$$
S_t
=
W_t\oplus W_t^{\oplus}.
$$

For every expanded word $t\ge16$:

$$
\boxed{
S_{t,j}=q_{t,j}\bmod2
}
$$

where $q_{t,j}$ is the integer carry count entering bit $j$ during the multi-operand addition that creates $W_t$.

Thus:

$$
\boxed{
\text{schedule nonlinearity}=\text{carry-scar parity field}.
}
$$

The Window-2 anchor is the first place this field appears.

---

# 14. Rotation Geometry vs Carry Geometry

The previous phase-geometry work established:

$$
\boxed{
\operatorname{ROTR}=\text{phase transport on }\mathbb Z_{32}.
}
$$

Rotations create circular locality.

For example:

$$
\Sigma_0(x)=R_2x\oplus R_{13}x\oplus R_{22}x
$$

builds a triangular phase stencil with offsets:

$$
(2,13,22).
$$

The carry result adds the second geometry:

$$
\boxed{
+ \pmod{2^{32}}=\text{upward carry transport}.
}
$$

Therefore SHA combines:

$$
\boxed{
\text{circular phase transport}
}
$$

with:

$$
\boxed{
\text{linear upward carry transport}.
}
$$

That cross-product creates a lattice:

$$
\boxed{
\mathcal L_{\text{SHA}}
=
\mathbb Z_{32}^{\text{phase}}
\oplus
L_{32}^{\text{carry}}.
}
$$

This is the deeper geometry of schedule identity.

---

# 15. Interpretation: Why This Matters for Reversal

A value-only view sees:

$$
W_{16}
$$

as a 32-bit word.

A shape view sees:

$$
W_{16}
=
W_{16}^{\oplus}\oplus S_{16}.
$$

The XOR approximation is the linear face.

The carry scar is the hidden nonlinear history.

Since:

$$
S_{16,0}=0,
$$

the least significant bit gives a clean entry point.

Then the reconstruction can proceed upward:

$$
j=0\rightarrow1\rightarrow2\rightarrow\cdots\rightarrow31.
$$

At each step:

$$
q_{j+1}=\left\lfloor\frac{n_j+q_j}{2}\right\rfloor.
$$

Thus, if candidate low-bit assignments are known, the carry state can be propagated upward deterministically.

This turns carry scar collapse into a prefix-decoding problem:

$$
\boxed{
\text{recover low bits}
\rightarrow
\text{propagate carry}
\rightarrow
\text{constrain high bits}.
}
$$

---

# 16. Window-2 Reverse Strategy

A schedule-reversal engine should use the Window-2 anchor as follows:

1. Compute or hypothesize:

$$
W_{16}^{\oplus}
=
\sigma_1(W_{14})\oplus W_9\oplus\sigma_0(W_1)\oplus W_0.
$$

2. Lock the carry-free bit:

$$
(W_{16})_0=(W_{16}^{\oplus})_0.
$$

3. Track integer carry counts:

$$
q_0=0,
$$

$$
q_{j+1}=
\left\lfloor
\frac{
A_j+B_j+C_j+D_j+q_j
}{2}
\right\rfloor.
$$

4. Compute scar parity:

$$
S_{16,j}=q_j\bmod2.
$$

5. Enforce:

$$
(W_{16})_j=(W_{16}^{\oplus})_j\oplus S_{16,j}.
$$

6. Extend to $W[17..23]$ using the same automaton.

7. Apply meet-in-the-middle consistency:

$$
\text{backward}(W[16..63])\Rightarrow W[0..15]
$$

and:

$$
\text{forward}(W[0..15])\Rightarrow W[16..23].
$$

The anchor is:

$$
\boxed{
W_{16,0}.
}
$$

The ladder is:

$$
\boxed{
L_{32}.
}
$$

The boundary check is:

$$
\boxed{
W[16..23]\ \text{regeneration}.
}
$$

---

# 17. Experimental Summary

The pasted Phase 520 run produced the following results:

| Test | Result |
|---|---:|
| $P(S_{16,0}=0)$ | $1.0000$ |
| $P(S_{16,1}=0)$ | $0.7556$ |
| $P(S_{16,2}=0)$ | $0.6304$ |
| Downward leakage under direct $W_0$ bit flips | $0$ |
| Window-2 backward/forward consistency | $1000/1000$ |
| Carry-free LSB theorem verification | $10000/10000$ |
| Mean scar bits changed under single-bit seed perturbation | $22.10$ |
| $P(>8\text{ scar bits changed})$ | $0.7880$ |

The stable empirical conclusion is:

$$
\boxed{
W_{16,0}\text{ is carry-free, while higher bits enter an upward carry scar field.}
}
$$

---

# 18. Final Theorem Stack

## Theorem A — XOR LSB Theorem

For any multi-operand addition modulo $2^{32}$,

$$
\left(\sum_m X_m\right)_0
=
\bigoplus_m (X_m)_0.
$$

Therefore the LSB has no output scar.

---

## Theorem B — Window-2 Anchor

For SHA-256,

$$
W_{16}=
\sigma_1(W_{14})+
W_9+
\sigma_0(W_1)+
W_0
\pmod{2^{32}},
$$

and:

$$
\boxed{
S_{16,0}=0.
}
$$

---

## Theorem C — Upward Carry Causality

For direct bit injection at position $j$ into an addition term,

$$
\boxed{
\delta_j\Rightarrow\operatorname{supp}(\delta W)\subseteq\{j,j+1,\dots,31\}.
}
$$

No bit below $j$ can be affected by carry propagation.

---

## Theorem D — Carry Scar Parity

For four-operand addition with carry count $q_j$,

$$
\boxed{
S_j=q_j\bmod2.
}
$$

---

## Theorem E — Window-2 Meet-in-the-Middle Consistency

The recurrence admits exact backward recovery:

$$
W_{t-16}
=
W_t-
\sigma_1(W_{t-2})-
W_{t-7}-
\sigma_0(W_{t-15})
\pmod{2^{32}}.
$$

Thus any candidate $W[16..63]$ must regenerate the same $W[16..23]$ after backward schedule recovery.

---

# 19. Phase 520 Stable Collapse

The complete Phase 520 result is:

$$
\boxed{
\text{Window 2 begins with a carry-free LSB anchor and an upward carry scar ladder.}
}
$$

The direct formula is:

$$
\boxed{
W_{16,0}
=
\left(
\sigma_1(W_{14})\oplus W_9\oplus\sigma_0(W_1)\oplus W_0
\right)_0.
}
$$

The structural geometry is:

$$
\boxed{
\text{ROTR builds circular phase}
}
$$

$$
\boxed{
\text{ADD builds upward scar}
}
$$

$$
\boxed{
\text{Schedule recurrence propagates both into ancestry}
}
$$

The inversion implication is:

$$
\boxed{
\text{do not attack }W_{16}\text{ as a flat word; climb it from the carry-free LSB upward.}
}
$$

---

# Appendix A — Reproducible Python Script

```python
import random
from collections import defaultdict

MASK = 0xFFFFFFFF

PAD = [
    0x80000000,
    0,
    0,
    0,
    0,
    0,
    0,
    0x00000100,
]

def rotr(x, n):
    return ((x >> n) | (x << (32 - n))) & MASK

def s0(w):
    return rotr(w, 7) ^ rotr(w, 18) ^ (w >> 3)

def s1(w):
    return rotr(w, 17) ^ rotr(w, 19) ^ (w >> 10)

def expand(W16):
    W = list(W16) + [0] * 48
    for i in range(16, 64):
        W[i] = (s1(W[i-2]) + W[i-7] + s0(W[i-15]) + W[i-16]) & MASK
    return W

def backward_schedule(W_full):
    W = list(W_full)
    for i in range(63, 15, -1):
        W[i-16] = (W[i] - s1(W[i-2]) - W[i-7] - s0(W[i-15])) & MASK
    return W[:16]

# Carry-free LSB theorem verification
N = 10000
holds = 0

for _ in range(N):
    H1 = [random.randint(0, MASK) for _ in range(8)]
    W = expand(H1 + PAD)

    w16_xor_lsb = (s1(W[14]) ^ W[9] ^ s0(W[1]) ^ W[0]) & 1
    w16_actual_lsb = W[16] & 1

    if w16_xor_lsb == w16_actual_lsb:
        holds += 1

print(f"Carry-free LSB theorem: {holds}/{N}")

# Carry-free rates
N = 5000
carry_free_bits = [0] * 32

for _ in range(N):
    H1 = [random.randint(0, MASK) for _ in range(8)]
    W = expand(H1 + PAD)

    w16_actual = W[16]
    w16_xor = s1(W[14]) ^ W[9] ^ s0(W[1]) ^ W[0]
    scar = w16_actual ^ w16_xor

    for bit in range(32):
        if not ((scar >> bit) & 1):
            carry_free_bits[bit] += 1

print("Carry-free bit rates at W[16]:")
for bit in range(32):
    p = carry_free_bits[bit] / N
    if p > 0.6:
        print(bit, p)

# No downward leakage test for direct W0 injection
for j in [0, 7, 15, 16, 24, 31]:
    affected = defaultdict(float)

    for _ in range(1000):
        H1_base = [random.randint(0, MASK) for _ in range(8)]
        H1_pert = list(H1_base)
        H1_pert[0] ^= (1 << j)

        W_base = expand(H1_base + PAD)
        W_pert = expand(H1_pert + PAD)

        diff = W_base[16] ^ W_pert[16]

        for b in range(32):
            if (diff >> b) & 1:
                affected[b] += 1 / 1000

    bits = [b for b in range(32) if affected[b] > 0.01]
    lowest = min(bits) if bits else None
    downward = [b for b in bits if b < j]

    print(
        f"j={j}: lowest affected={lowest}, "
        f"downward leakage bits={len(downward)}, "
        f"P(affects j)={affected.get(j, 0):.3f}"
    )

# Window-2 meet-in-the-middle consistency
N = 1000
success = 0

for _ in range(N):
    H1 = [random.randint(0, MASK) for _ in range(8)]
    W_full = expand(H1 + PAD)

    recovered = backward_schedule(W_full)
    W_check = expand(recovered + PAD)

    ok = all(W_full[r] == W_check[r] for r in range(16, 24))
    if ok:
        success += 1

print(f"Window-2 consistency: {success}/{N}")
```

---

# Appendix B — Correct Terminology

Use these distinctions consistently:

| Term | Meaning |
|---|---|
| carry count $q_j$ | integer carry entering bit $j$ |
| carry-out $q_{j+1}$ | carry count passed upward into bit $j+1$ |
| XOR approximation $W^\oplus$ | schedule word computed with XOR instead of modular addition |
| carry scar $S$ | $W\oplus W^\oplus$ |
| scar bit $S_j$ | parity of incoming carry count, $q_j\bmod2$ |
| carry-free bit | bit where $S_j=0$ for all inputs |
| Window-2 anchor | $W_{16,0}$ |

---

# Final Statement

$$
\boxed{
\text{The carry scar does not begin as chaos. It begins as a pure bit.}
}
$$

$$
\boxed{
W_{16,0}\text{ is the first clean rung of the Window-2 ladder.}
}
$$

$$
\boxed{
\text{From there, SHA's schedule nonlinearity climbs upward through }L_{32}.
}
$$
