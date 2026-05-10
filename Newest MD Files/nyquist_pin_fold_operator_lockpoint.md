# The Nyquist Pin of the Fold

## Parity Shadow, Dyadic Sampling, Branch Grammar, and Shape-Sufficient Inversion

---

## Abstract

This document records the current lock point of the fold investigation. The core discovery is that the decimal adjacent-difference reducer has an exact parity shadow: when decimal digits are projected modulo $2$, the absolute-difference fold becomes a binary XOR lattice. That lattice is not heuristic, approximate, or merely visual. It is the exact $GF(2)$ projection of the decimal fold.

The central operator is:

$$
x_i^{(\ell+1)} = x_i^{(\ell)} \oplus x_{i+1}^{(\ell)}.
$$

With the shift operator $E$ defined by:

$$
(E x)_i = x_{i+1},
$$

one fold step is:

$$
\delta = I+E,
$$

and level $\ell$ is:

$$
x^{(\ell)}=(I+E)^\ell x^{(0)}.
$$

Lucas's theorem exposes the hidden geometry:

$$
x_i^{(\ell)}
=
\bigoplus_{j\subseteq \ell}
x_{i+j}^{(0)}.
$$

Here $j\subseteq\ell$ means every binary $1$-bit of $j$ is also a $1$-bit of $\ell$. This turns every level of the fold into a precise algebraic sampling mask.

The lock point is:

$$
\boxed{
\text{forward fold}=\text{local deterministic compression}
}
$$

$$
\boxed{
\text{reverse fold}=\text{hidden branch variables}+\text{constraint propagation}
}
$$

This is the Nyquist pin: the point where the fold stops being a mysterious collapse and becomes a readable algebraic lattice. The same branch grammar appears in decimal Ducci-style reductions, Collatz dynamics, and cryptographic hash functions such as SHA-256, where hidden carries and schedule variables play the role of branch coordinates.

---

# 1. The Core Reduction

Let the original decimal digit stream be:

$$
D^{(0)}=(d_0^{(0)},d_1^{(0)},\ldots,d_{N_0-1}^{(0)}),
$$

where:

$$
d_i^{(0)}\in\{0,1,2,\ldots,9\}.
$$

The decimal adjacent-difference reducer is:

$$
d_i^{(\ell+1)}
=
\left|
d_{i+1}^{(\ell)}-d_i^{(\ell)}
\right|.
$$

The row length decreases by one each level:

$$
N_\ell=N_0-\ell.
$$

For a finite input of length $N_0$, the process terminates at:

$$
N_{N_0-1}=1.
$$

This is the visible finite cone.

---

# 2. The Parity Shadow

The key projection is parity:

$$
x_i^{(\ell)}=d_i^{(\ell)}\bmod 2.
$$

The decisive identity is:

$$
\left|a-b\right|\bmod 2
=
(a+b)\bmod 2.
$$

Since addition modulo $2$ is XOR:

$$
(a+b)\bmod2=a\oplus b,
$$

we obtain:

$$
x_i^{(\ell+1)}
=
x_i^{(\ell)}\oplus x_{i+1}^{(\ell)}.
$$

Therefore:

$$
\boxed{
\text{the XOR lattice is the exact parity projection of the decimal difference fold.}
}
$$

This is not an analogy. It is an exact shadow.

---

# 3. The Fold Operator Over $GF(2)$

Let $x^{(\ell)}$ denote the full binary row at level $\ell$.

Define:

$$
(Ix)_i=x_i
$$

and:

$$
(E x)_i=x_{i+1}.
$$

Then:

$$
x^{(\ell+1)}
=
(I+E)x^{(\ell)}.
$$

Over $GF(2)$:

$$
I+E
$$

means identity plus shift, with addition performed modulo $2$.

Thus:

$$
x^{(\ell)}
=
(I+E)^\ell x^{(0)}.
$$

This is the entire fold in one equation.

---

# 4. Binomial Expansion and the Pascal Mask

Expanding the operator:

$$
(I+E)^\ell
=
\sum_{j=0}^{\ell}
\binom{\ell}{j}E^j.
$$

Therefore:

$$
x_i^{(\ell)}
=
\bigoplus_{j=0}^{\ell}
\left(
\binom{\ell}{j}\bmod2
\right)
x_{i+j}^{(0)}.
$$

Only odd binomial coefficients survive.

This is the Pascal mask. The visible Sierpinski or Rule-90 structure is the geometry of Pascal's triangle modulo $2$.

---

# 5. Lucas's Theorem and Bit-Subset Sampling

Lucas's theorem implies that:

$$
\binom{\ell}{j}\equiv1\pmod2
$$

if and only if every binary $1$-bit of $j$ is also a binary $1$-bit of $\ell$.

Write:

$$
j\subseteq\ell
$$

for this bit-subset relation.

Then:

$$
\boxed{
x_i^{(\ell)}
=
\bigoplus_{j\subseteq\ell}
x_{i+j}^{(0)}.
}
$$

This is the exact sampling law of the fold.

It says that every cell at level $\ell$ is a checksum over the initial row, but not over all positions. It samples only offsets whose binary pattern is contained inside the binary pattern of $\ell$.

The number of surviving terms is:

$$
2^{\operatorname{popcount}(\ell)},
$$

where $\operatorname{popcount}(\ell)$ is the number of $1$-bits in $\ell$.

Thus:

$$
\boxed{
\text{fold depth controls sampling geometry.}
}
$$

---

# 6. The 448 Lock: A 64-Grid Nyquist Pin

The observed level:

$$
\ell=448
$$

is not arbitrary.

Its binary decomposition is:

$$
448=256+128+64
$$

or:

$$
448=2^8+2^7+2^6.
$$

Therefore:

$$
\operatorname{popcount}(448)=3.
$$

The number of surviving offsets is:

$$
2^3=8.
$$

The valid subset offsets are:

$$
j\in
\{0,64,128,192,256,320,384,448\}.
$$

Therefore:

$$
x_i^{(448)}
=
x_i
\oplus x_{i+64}
\oplus x_{i+128}
\oplus x_{i+192}
\oplus x_{i+256}
\oplus x_{i+320}
\oplus x_{i+384}
\oplus x_{i+448}.
$$

This means:

$$
\boxed{
\ell=448\text{ is an eight-point parity probe on a }64\text{-grid.}
}
$$

If the row has:

$$
N_{448}=1600
$$

and:

$$
S_{448}=800,
$$

then:

$$
R_{448}
=
S_{448}-\frac{N_{448}}{2}
=
800-800
=
0.
$$

Thus level $448$ is an exact half-density lock:

$$
\boxed{
N_{448}=1600,\quad S_{448}=800,\quad R_{448}=0.
}
$$

This is the Nyquist pin of the current discovery: it samples the fold at exactly the scale where a deep binary mask becomes a clean long-range parity grid.

---

# 7. The 512 Lock: Long-Range Lag Probe

At:

$$
\ell=512=2^9,
$$

the Freshman's Dream identity over $GF(2)$ gives:

$$
(I+E)^{512}
=
I+E^{512}.
$$

Therefore:

$$
x_i^{(512)}
=
x_i\oplus x_{i+512}.
$$

This is not local texture. It is a long-range parity separation.

For the measured row:

$$
N_{512}=1536,
$$

$$
S_{512}=764,
$$

so:

$$
R_{512}
=
764-\frac{1536}{2}
=
764-768
=
-4.
$$

Thus:

$$
\boxed{
\ell=512\text{ reads a direct }512\text{-lag parity comparison.}
}
$$

The row is nearly balanced:

$$
764\text{ ones},\quad772\text{ zeros}.
$$

This is a long-range internal symmetry probe.

---

# 8. The Final Bit as Terminal Checksum

For a seed length:

$$
N_0=2048=2^{11},
$$

the final level is:

$$
\ell=2047=2^{11}-1.
$$

Binary:

$$
2047=11111111111_2.
$$

Every integer $j$ from $0$ to $2047$ is a bit-subset of $2047$.

Therefore:

$$
x_0^{(2047)}
=
\bigoplus_{j=0}^{2047}
x_j^{(0)}.
$$

So the terminal bit is the total parity of the original seed.

If:

$$
S_0=1034,
$$

then:

$$
1034\bmod2=0,
$$

and:

$$
x_0^{(2047)}=0.
$$

Thus:

$$
\boxed{
\text{the final zero is not absence; it is total parity closure.}
}
$$

The system has not destroyed all information. It has preserved one global invariant exactly.

---

# 9. Sum Spine, Density, and Residue

At every level define:

$$
S_\ell=\sum_{i=0}^{N_\ell-1}x_i^{(\ell)}.
$$

This is binary occupancy mass.

Define density:

$$
\rho_\ell=\frac{S_\ell}{N_\ell}.
$$

Define residue from half-density:

$$
R_\ell=S_\ell-\frac{N_\ell}{2}.
$$

Define first difference:

$$
\Delta S_\ell=S_{\ell+1}-S_\ell.
$$

Define residue velocity:

$$
\Delta R_\ell=R_{\ell+1}-R_\ell.
$$

The trace stack is:

$$
\boxed{
\left(
S_\ell,\rho_\ell,R_\ell,\Delta S_\ell,\Delta R_\ell
\right).
}
$$

The half-density lock set is:

$$
\mathcal{L}
=
\{\ell:R_\ell=0\}.
$$

The fold fingerprint is:

$$
\mathcal{F}(D,F)
=
\left(
\mathcal{L},
R_\ell,
\Delta R_\ell,
\widehat R(f),
T_{\text{terminal}},
\Theta_{\text{shape}}
\right).
$$

Where:

$$
\widehat R(f)=\mathcal{F}_{\text{Fourier}}\{R_\ell\}
$$

is the spectrum of the residue wave.

This is the shape hash.

---

# 10. Shape-Value-by-Location

A raw bit is not the full unit of meaning.

The full cell is:

$$
\mathcal{C}_{\ell,i}
=
\left(
x_i^{(\ell)},\ell,i,F
\right).
$$

Here:

- $x_i^{(\ell)}$ is value,
- $\ell$ is recursive depth,
- $i$ is position,
- $F$ is the operator constraint.

Thus:

$$
\boxed{
\text{meaning}=\text{value}+\text{location}+\text{constraint}.
}
$$

Or:

$$
\boxed{
\text{shape is value after recursion gives it location.}
}
$$

This is the core Nexus translation.

---

# 11. Random Controls and the Universal Carrier

Random input still forms the cone.

That matters.

It means the visible finite cone is not caused by $\pi$, $e$, or any special constant.

The cone is the universal carrier:

$$
C_{N,F,Q}.
$$

The source-specific signal is the modulation:

$$
P_F(D).
$$

The rendered image is:

$$
I(D)=C_{N,F,Q}+P_F(D)+\epsilon.
$$

Where:

- $C_{N,F,Q}$ is the carrier from length, operator, frame, font, and alignment,
- $P_F(D)$ is source-specific payload modulation,
- $\epsilon$ is render/read noise.

Thus:

$$
\boxed{
\text{random working proves the medium, not the message.}
}
$$

The task is to subtract the universal carrier and isolate the payload modulation.

---

# 12. Reversing One XOR Row

The forward row relation is:

$$
y_i=x_i\oplus x_{i+1}.
$$

To reverse, choose one boundary bit:

$$
x_0=b,
$$

where:

$$
b\in\{0,1\}.
$$

Then propagate:

$$
x_{i+1}=x_i\oplus y_i.
$$

Thus one XOR row has exactly two binary preimages.

If:

$$
y=[1,0,1],
$$

and:

$$
x_0=0,
$$

then:

$$
x_1=0\oplus1=1,
$$

$$
x_2=1\oplus0=1,
$$

$$
x_3=1\oplus1=0.
$$

So:

$$
x=[0,1,1,0].
$$

If:

$$
x_0=1,
$$

then:

$$
x=[1,0,0,1].
$$

The two preimages are complements.

Therefore:

$$
\boxed{
\text{one-step reverse}=\text{choose boundary bit, then integrate.}
}
$$

---

# 13. Reversing Arbitrary Depth

For arbitrary depth:

$$
x^{(\ell)}=(I+E)^\ell x^{(0)}.
$$

Factor the operator by binary digits:

$$
(I+E)^\ell
=
\prod_{k:\ell_k=1}
(I+E^{2^k}).
$$

Each factor has the form:

$$
y_i=x_i\oplus x_{i+s}.
$$

To reverse:

1. choose the first $s$ boundary bits,
2. propagate using:

$$
x_{i+s}=x_i\oplus y_i.
$$

For:

$$
\ell=448=256+128+64,
$$

we have:

$$
(I+E)^{448}
=
(I+E^{256})(I+E^{128})(I+E^{64}).
$$

A staged reverse unroll is:

$$
(I+E^{256})^{-1},
$$

then:

$$
(I+E^{128})^{-1},
$$

then:

$$
(I+E^{64})^{-1}.
$$

Each stage injects boundary variables and propagates constraints.

Thus:

$$
\boxed{
\text{deep reverse}=\text{dyadic factorization}+\text{boundary seeds}+\text{constraint propagation}.
}
$$

---

# 14. Underdetermination and Trace-Sufficient Inversion

A single final bit gives only one equation:

$$
\bigoplus_{i=0}^{N-1}x_i=b.
$$

That leaves:

$$
2^{N-1}
$$

valid preimages.

A full row at depth $\ell$ gives:

$$
A_\ell x=y_\ell,
$$

where:

$$
A_\ell=(I+E)^\ell.
$$

If:

$$
A_\ell:\{0,1\}^{N}\rightarrow\{0,1\}^{N-\ell},
$$

then its kernel has dimension:

$$
\dim\ker A_\ell=\ell.
$$

Therefore one full row at depth $\ell$ leaves:

$$
2^\ell
$$

candidate ancestors.

So uniqueness is not automatic.

The correct inversion target is:

$$
\boxed{
\text{recover the seed by intersecting many independent fold constraints.}
}
$$

Use:

$$
A_{\ell_1}x=y_{\ell_1},
$$

$$
A_{\ell_2}x=y_{\ell_2},
$$

$$
A_{\ell_3}x=y_{\ell_3},
$$

and so on.

If only row sums are known:

$$
\sum_i(A_\ell x)_i=S_\ell,
$$

these are weaker cardinality constraints.

If exact rows are known, they are linear $GF(2)$ constraints.

If lock locations are known:

$$
R_\ell=0,
$$

then:

$$
\sum_i(A_\ell x)_i=\frac{N_\ell}{2}.
$$

The shape decoder is:

$$
\boxed{
x\in
\bigcap_{\ell\in\Lambda}
\mathcal{P}_\ell
}
$$

where $\mathcal{P}_\ell$ is the preimage set consistent with level $\ell$.

The remaining question is:

$$
\boxed{
\text{how much of the trace is sufficient to reconstruct the seed?}
}
$$

This is the engineering target.

---

# 15. Decimal Reverse: Lifting Parity Back to Amplitude

The decimal rule is:

$$
y_i=|d_{i+1}-d_i|.
$$

To reverse it:

$$
d_{i+1}=d_i+\sigma_i y_i,
$$

where:

$$
\sigma_i\in\{-1,+1\}.
$$

Digits must remain valid:

$$
0\leq d_i\leq9.
$$

So decimal reverse is a constrained walk:

$$
d_0\in\{0,1,\ldots,9\},
$$

$$
\sigma_i\in\{-1,+1\},
$$

$$
d_{i+1}=d_i+\sigma_i y_i,
$$

with:

$$
0\leq d_{i+1}\leq9.
$$

The parity skeleton constrains the decimal lift because:

$$
d_{i+1}\bmod2
=
d_i\bmod2
\oplus
y_i\bmod2.
$$

Thus the correct reverse order is:

$$
\boxed{
\text{reverse parity shape first, then solve decimal amplitudes.}
}
$$

---

# 16. Collatz as a Reverse Fold Tree

The compressed odd Collatz map is:

$$
T(n)
=
\frac{3n+1}{2^{v_2(3n+1)}}.
$$

The forward step is:

1. grow:

$$
3n+1,
$$

2. fold by binary depth:

$$
2^{v_2(3n+1)}.
$$

The reverse equation for child $m$ is:

$$
m=
\frac{3n+1}{2^a}.
$$

So:

$$
3n+1=2^a m,
$$

and:

$$
n=\frac{2^a m-1}{3}.
$$

Valid reverse branches require:

$$
2^a m\equiv1\pmod3.
$$

The hidden branch variable is:

$$
a=v_2(3n+1).
$$

Thus:

$$
\boxed{
\text{Collatz reverse}=\text{choose dyadic exponent }a,\text{ then test congruence.}
}
$$

This matches the XOR reverse grammar:

$$
\boxed{
\text{XOR reverse}=\text{choose boundary bit, then propagate.}
}
$$

And the decimal reverse grammar:

$$
\boxed{
\text{decimal reverse}=\text{choose sign variables and boundary digit, then propagate.}
}
$$

Same branch grammar:

$$
\boxed{
\text{forward fold is many-to-one; reverse fold is a constrained tree.}
}
$$

---

# 17. SHA as a Fold Carrier

SHA-256 has a fixed carrier:

$$
C_{\text{SHA}}
=
(H_0,K_t,\Sigma_0,\Sigma_1,\sigma_0,\sigma_1,Ch,Maj,+\bmod2^{32}).
$$

The message modulates the carrier through the message schedule:

$$
M\rightarrow W_t.
$$

The digest is the final residue:

$$
H(M)=\text{residue of }M\text{ on }C_{\text{SHA}}.
$$

So:

$$
\boxed{
\text{SHA works because every input modulates a universal fold lattice into a stable residue.}
}
$$

In XOR, hidden variables are boundary bits.

In Collatz, hidden variables are dyadic exponents.

In SHA, hidden variables include:

$$
\text{carry bits},
$$

$$
\text{schedule choices},
$$

$$
\text{round-state constraints}.
$$

The SHA reverse problem is not solved by the XOR model alone. But the branch grammar is the same:

$$
\boxed{
\text{recover hidden branch variables, then propagate constraints backward.}
}
$$

This is why carry residues matter.

They are not discarded noise. They are the shape channel.

---

# 18. The Unresolved Location Principle

If two objects share a base class, they share inherited logic.

Let an object be:

$$
O=(B,\Delta,S,L),
$$

where:

- $B$ is base class,
- $\Delta$ is override or mutation,
- $S$ is state,
- $L$ is location or address.

If two objects share:

$$
B,
$$

then their shared operator grammar is still present.

Apparent randomness arises when the observer lacks location:

$$
\Omega_L=\text{unresolved location}.
$$

So:

$$
\boxed{
\text{random}=\text{logic without resolved address.}
}
$$

In the XOR lattice:

$$
x_i^{(\ell)}
=
\bigoplus_{j\subseteq\ell}
x_{i+j}^{(0)}.
$$

If $i$ and $j$ are known, the cell is deterministic.

If the address is lost, the result appears random.

Thus:

$$
\boxed{
\text{somewhere is what makes things random.}
}
$$

The inverse operation is:

$$
\boxed{
\text{recover the somewhere.}
}
$$

That is the fold decoder.

---

# 19. The Nyquist Pin

The Nyquist pin is the level where the system reveals that the apparent randomness is actually sampled structure.

For this fold, level $448$ is the pin because it exposes a clean $64$-grid:

$$
448=7\cdot64.
$$

The mask is:

$$
\{0,64,128,192,256,320,384,448\}.
$$

This is eight-point sampling.

The lock:

$$
N_{448}=1600,\quad S_{448}=800,\quad R_{448}=0
$$

shows exact half-density balance across those checksums.

Thus:

$$
\boxed{
\ell=448\text{ is a Nyquist pin for the }2048\text{-cell parity fold.}
}
$$

It is not the whole proof.

It is the point where the structure becomes undeniable.

---

# 20. Complete Reverse Blueprint

The fold inversion method is:

## Step 1: Identify the projection

For decimal folds:

$$
d_i\bmod2=x_i.
$$

For SHA:

$$
\text{extract shape/carry channels}.
$$

For Collatz:

$$
\text{extract dyadic depth }v_2.
$$

## Step 2: Identify the local operator

For parity:

$$
F(a,b)=a\oplus b.
$$

For decimal:

$$
F(a,b)=|a-b|.
$$

For Collatz:

$$
F(n)=\frac{3n+1}{2^{v_2(3n+1)}}.
$$

For SHA:

$$
F=\text{round function}.
$$

## Step 3: Factor the global operator

For XOR:

$$
(I+E)^\ell
=
\prod_{k:\ell_k=1}(I+E^{2^k}).
$$

## Step 4: Identify hidden branch variables

XOR:

$$
b=\text{boundary bit}.
$$

Decimal:

$$
\sigma_i=\text{sign choice}.
$$

Collatz:

$$
a=v_2(3n+1).
$$

SHA:

$$
c_i=\text{carry and schedule branch states}.
$$

## Step 5: Propagate constraints backward

Use:

$$
x_{i+s}=x_i\oplus y_i.
$$

Use:

$$
d_{i+1}=d_i+\sigma_i y_i.
$$

Use:

$$
n=\frac{2^a m-1}{3}.
$$

Use SHA round equations with carry constraints.

## Step 6: Intersect trace constraints

Use:

$$
S_\ell,
$$

$$
R_\ell,
$$

$$
\mathcal{L},
$$

$$
\Delta R_\ell,
$$

$$
\widehat R(f),
$$

$$
T_{\text{terminal}}.
$$

The target is not:

$$
\text{invert one final value}.
$$

The target is:

$$
\boxed{
\text{recover the branch history consistent with the whole trace.}
}
$$

---

# 21. What This Solves and What Remains Open

## Solved

The fold law for the parity shadow is solved:

$$
\boxed{
x^{(\ell)}=(I+E)^\ell x^{(0)}.
}
$$

The sampling law is solved:

$$
\boxed{
x_i^{(\ell)}
=
\bigoplus_{j\subseteq\ell}
x_{i+j}^{(0)}.
}
$$

The $448$ lock is solved:

$$
\boxed{
448=256+128+64
}
$$

and:

$$
\boxed{
x_i^{(448)}
=
\bigoplus_{m=0}^{7}
x_{i+64m}^{(0)}.
}
$$

The $512$ lag probe is solved:

$$
\boxed{
x_i^{(512)}=x_i\oplus x_{i+512}.
}
$$

The final bit is solved:

$$
\boxed{
x_0^{(2047)}
=
\bigoplus_{j=0}^{2047}
x_j^{(0)}.
}
$$

The reverse mechanism is solved:

$$
\boxed{
\text{choose boundary variables, then propagate constraints.}
}
$$

## Open

The open engineering problem is trace sufficiency:

$$
\boxed{
\text{which subset of the trace uniquely reconstructs the seed?}
}
$$

The open Collatz problem is branch-frequency control:

$$
\boxed{
\text{can the dyadic branch tree be shown to always pay its heat debt?}
}
$$

The open SHA problem is shape-channel extraction:

$$
\boxed{
\text{can enough carry/schedule branch variables be recovered to make inversion practical?}
}
$$

---

# 22. Final Collapse

$$
\Delta:
\text{decimal difference exposes parity shadow}
$$

$$
\oplus:
\text{parity shadow becomes XOR / Rule-90 lattice}
$$

$$
↻:
\text{Lucas subset law reveals exact sampling geometry}
$$

$$
\bot:
\ell=448\text{ pins the fold as a }64\text{-grid resonance}
$$

$$
\Psi:
\boxed{
\text{the fold is algebraic, reversible as a constrained branch tree, and readable as shape.}
}
$$

This is the lock point.

This is the Nyquist pin.

The short form:

$$
\boxed{
\text{forward collapse hides information by losing address;}
\quad
\text{reverse recovery restores address by reading shape.}
}
$$

And the final statement:

$$
\boxed{
\text{shape is memory, and location is the missing branch variable.}
}
$$
