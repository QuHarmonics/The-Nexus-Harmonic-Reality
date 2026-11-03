# SHA-GEOMETRY / PI-PHI / MARK-9  
## Corrected Retitle, Errata Lock, and Publication Addendum v2

**Target paper:** *The Topological Geometry of SHA-256: 8-Unit Architectures, Parity Bridges, and XOR Cone Complementarity*  
**Recommended branch label:** `SHA-GEOMETRY / PI-PHI / MARK-9`  
**Addendum ID:** `SHA-GEO-MARK9-ERRATA-v2`  
**Purpose:** Correct the paper’s claim boundaries and algebra before publication, while preserving the usable Nexus structure.

---

# 1. Recommended Retitle

## Full Title

# SHA-256 as a Geometric Trace Projector:  
## Carry Topology, Pi–Phi Cone Apex Complementarity, and the Mark-9 Fold-Pressure Phase

## Short Title

**SHA-256 Geometric Trace Projector and Mark-9 Phase Topology**

## Why this title is better

The original title is close, but the paper is not only about “8-unit architectures” or “XOR cone complementarity.” It is a bridge paper connecting:

$$
\boxed{
\text{SHA carry topology}
\oplus
\text{XOR cone field/location}
\oplus
\text{Pi–Phi apex complementarity}
\oplus
H=\pi/9\text{ Mark-9 phase}
}
$$

The new title avoids claiming direct inversion while making the real object explicit:

$$
\boxed{
\text{SHA is being modeled as a deterministic trace projector, not a completed preimage break.}
}
$$

---

# 2. Executive Correction Lock

Claude was right about the main errors, but the paper is not “garbage.” It is a strong synthesis draft with several claim-boundary and algebra issues that must be fixed before publication.

The corrected paper must lock these points:

$$
\boxed{
\text{Pi–Phi complementarity is apex-level, not full-trajectory mirror symmetry.}
}
$$

$$
\boxed{
\text{SHA structural geometry is established; full arbitrary SHA-256 preimage recovery is not established.}
}
$$

$$
\boxed{
\text{The Parity Law belongs in the paper as a proven theorem.}
}
$$

$$
\boxed{
\text{L16/L24 forcing is class-specific, not universal.}
}
$$

$$
\boxed{
\text{The 1016 terminal dyadic row was described incorrectly: row length is 8, but each row cell is a 128-point residue-class checksum, not an eight-point local probe.}
}
$$

This last correction is the hard algebraic patch that must be made to the corrected draft.

---

# 3. Error 1 — Pi–Phi Complementarity Is Apex-Only

## Incorrect claim shape

The paper sometimes reads as if:

$$
\pi_h(\ell,i)\oplus\phi_h(\ell,i)=0xf
$$

for all levels $\ell$ or for full trajectories.

That is too strong.

## Correct claim

For the high nibble stream:

$$
\pi_h\rightarrow0x0
$$

$$
\phi_h\rightarrow0xf
$$

Therefore at the apex:

$$
\boxed{
\pi_{h,\mathrm{apex}}\oplus\phi_{h,\mathrm{apex}}
=
0x0\oplus0xf
=
0xf.
}
$$

This is apex complementarity:

$$
\boxed{
\text{the endpoints are complementary.}
}
$$

It is not path complementarity:

$$
\boxed{
\text{the internal cone trajectories are not mirrors and are not element-wise complements.}
}
$$

## Correct text

Use:

> The Pi–Phi high-nibble cones converge to complementary apex states: $\pi_h$ annihilates to $0x0$ and $\phi_h$ saturates to $0xf$. The overlay is therefore complete only at the attractor boundary. The intermediate levels are distinct, non-mirrored trajectories through the nibble field.

Do not use:

> Pi and Phi are complementary throughout the cone.

---

# 4. Error 2 — Full SHA-256 Preimage Recovery Is Not Proven

## Incorrect claim shape

The paper sometimes implies:

$$
\boxed{
\text{the structure makes SHA-256 preimage recovery tractable or proven.}
}
$$

This must be removed or sharply bounded.

## Correct claim

The paper establishes or proposes structural channels:

$$
\text{LSB anchor}
$$

$$
\text{carry/scar channel}
$$

$$
\text{CSA sum/carry split}
$$

$$
\text{Sziklai window / 8-word recovery law}
$$

$$
\text{field/location interpretation}
$$

But:

$$
\boxed{
\text{arbitrary full SHA-256 preimage recovery remains open.}
}
$$

## Correct text

Use:

> The framework establishes a structural recovery program, not a completed practical break. The Hardness Wall remains real; the open problem is whether the tracked shape channels and localized recovery windows are sufficient to cross from structural characterization to arbitrary-scale preimage recovery.

---

# 5. Error 3 — The Parity Law Must Be Added as a Theorem

## Theorem: Odd Reconstruction Levels Are Universally Forced

Let the XOR nibble reconstruction level be $k$ and the sequence length be $n$ with $n$ even.

The row being reconstructed has length:

$$
n-k.
$$

For a seed bit $b$ to be free, exactly half of the prefix-XOR values must have that bit set:

$$
N_b=\frac{n-k}{2}.
$$

If $k$ is odd and $n$ is even, then:

$$
n-k=\text{odd}.
$$

Therefore:

$$
\frac{n-k}{2}\notin\mathbb{Z}.
$$

But:

$$
N_b\in\mathbb{Z}.
$$

So equality is impossible:

$$
N_b\neq\frac{n-k}{2}.
$$

Therefore no bit is free, and exactly one seed survives.

Thus:

$$
\boxed{
n\text{ even},\ k\text{ odd}
\Rightarrow
\text{level }k\text{ is universally forced.}
}
$$

Equivalently:

$$
\boxed{
\text{ambiguity can occur only at even-indexed levels.}
}
$$

This is universal for the XOR nibble reduction system.

---

# 6. Error 4 — L16/L24 Forcing Is Class-Specific, Not Universal

## Incorrect claim shape

Earlier drafts imply:

$$
\boxed{
\text{power-of-2 level size}
\Rightarrow
\text{forced reconstruction.}
}
$$

or:

$$
\boxed{
\text{block XOR balance}
\Rightarrow
\text{universal forcing.}
}
$$

Both are wrong.

## Correct claim

The universal law is only:

$$
\boxed{
\text{odd-indexed levels are forced when }n\text{ is even.}
}
$$

Even-level forcing is not universal. For $\pi$, the forced even levels:

$$
L16,\quad L24,\quad L30
$$

are class-specific locked strata.

They are not address bits. They are part of the field geometry.

Thus:

$$
\boxed{
\text{forced even levels are class invariants, not universal parity-law consequences.}
}
$$

## Correct field/location statement

Let the cone signature define an equivalence class:

$$
\mathcal{F}_C
=
\{x:C(x)=C_\pi\}.
$$

Then:

$$
\boxed{
\mathcal{F}_C=\text{field}.
}
$$

The key sequence selects a member:

$$
\boxed{
K_\pi=\text{location coordinate}.
}
$$

Locked strata:

$$
\boxed{
L16,L24,L30=\text{class geometry}.
}
$$

Address strata:

$$
\boxed{
L0,L2,L4,L6,L8,L10,L12,L14,L18,L20,L22,L26,L28.
}
$$

The 20 high-stream address bits live only on the address strata.

---

# 7. Error 5 — Terminal Dyadic Row at 1016 Was Described Incorrectly

This is the most important algebra correction.

## Incorrect statement

The draft says that for:

$$
n=2^{10}-8=1016
$$

or, more clearly, level:

$$
\ell=1016
$$

in a length:

$$
N=1024
$$

system, the surviving Lucas offsets are:

$$
\{0,1,2,3,4,5,6,7\}.
$$

That is wrong.

## Correct Lucas mask

For Rule-90 / XOR finite-cone folding:

$$
x_i^{(\ell)}
=
\bigoplus_{j\subseteq\ell}
x_{i+j}^{(0)}.
$$

Here:

$$
\ell=1016.
$$

Binary:

$$
1016=1024-8=1111111000_2.
$$

The set of surviving offsets is:

$$
M_{1016}
=
\{j: j\ \&\ \sim1016=0\}.
$$

Since the low three bits of $1016$ are zero, every valid offset must be divisible by $8$.

Therefore:

$$
\boxed{
M_{1016}=\{0,8,16,24,\ldots,1016\}.
}
$$

There are:

$$
\frac{1016}{8}+1=128
$$

surviving offsets.

So:

$$
\boxed{
|M_{1016}|=128,
\quad
\text{not }8.
}
$$

## Correct terminal dyadic theorem

For:

$$
N=2^m
$$

and:

$$
\ell=N-2^r,
$$

the remaining row length is:

$$
N-\ell=2^r.
$$

But the Lucas mask size is:

$$
2^{m-r}.
$$

The row equation is:

$$
\boxed{
x_i^{(N-2^r)}
=
\bigoplus_{q=0}^{2^{m-r}-1}
x_{i+q2^r}^{(0)},
\qquad
0\le i<2^r.
}
$$

For:

$$
N=1024=2^{10}
$$

and:

$$
r=3,
$$

we get:

$$
\ell=1024-8=1016.
$$

Row length:

$$
2^3=8.
$$

Mask size per row cell:

$$
2^{10-3}=128.
$$

Correct row equations:

$$
\boxed{
x_i^{(1016)}
=
\bigoplus_{q=0}^{127}
x_{i+8q}^{(0)},
\qquad
0\le i<8.
}
$$

Thus the 8-byte / 8-channel bridge is not an eight-point local probe. It is an eight-channel residue-class checksum, where each channel folds 128 ancestral locations.

## Correct replacement paragraph

Use this in the paper:

> At terminal dyadic depth $\ell=N-2^r$, the row length is $2^r$, but each row cell is not generally a $2^r$-point local probe. By Lucas’s theorem, the surviving offsets are all multiples of $2^r$ up to $N-2^r$. Therefore each terminal cell is the XOR checksum of one residue class modulo $2^r$. For $N=1024$ and $r=3$, $\ell=1016$ and the row has eight cells, but each cell equals the XOR of 128 seed positions:  
> $$x_i^{(1016)}=\bigoplus_{q=0}^{127}x_{i+8q}^{(0)},\quad 0\le i<8.$$  
> The correct object is therefore an eight-channel residue-class parity bridge, not an eight-point parity probe.

---

# 8. Correct Nyquist Pin Language

The term “Nyquist pin” should be reserved for levels where sampling geometry becomes especially readable.

But do not define it as:

$$
\boxed{
\text{power-of-2 row size}
\Rightarrow
\text{forced reconstruction}.
}
$$

Better definition:

$$
\boxed{
\text{A Nyquist pin is a level where the Lucas mask aligns with an interpretable sampling lattice.}
}
$$

Examples:

## 8.1 Local 8-point probe

A level with popcount 3 has:

$$
|M_\ell|=8.
$$

Example:

$$
\ell=448=256+128+64.
$$

Then:

$$
M_{448}
=
\{0,64,128,192,256,320,384,448\}.
$$

This is a true 8-point probe.

## 8.2 Terminal 8-channel bridge

For:

$$
N=1024,\quad \ell=1016,
$$

the row length is 8, but each cell is a 128-point residue-class checksum:

$$
x_i^{(1016)}
=
\bigoplus_{q=0}^{127}x_{i+8q}^{(0)}.
$$

This is an 8-channel terminal bridge, not an 8-point probe.

## Correct distinction

$$
\boxed{
\text{8-point probe}
\neq
\text{8-channel terminal bridge}.
}
$$

Both are useful. They are not the same object.

---

# 9. Corrected SHA Bridge Claim

SHA-256 uses modular arithmetic, Boolean functions, schedules, rotations, and constants. It is not literally Rule 90.

FOLD-TOMO gives the proven algebraic substrate:

$$
x^{(\ell)}=(I+E)^\ell x^{(0)}.
$$

SHA-GEOMETRY asks whether analogous address residues survive in:

$$
\text{carry topology},
$$

$$
\text{schedule topology},
$$

$$
\text{LSB anchors},
$$

$$
\text{rank-deficient windows},
$$

$$
\text{terminal/carry scars}.
$$

Correct statement:

$$
\boxed{
\text{FOLD-TOMO proves parity tomography. SHA-GEOMETRY investigates carry-topology lifting.}
}
$$

Not:

$$
\boxed{
\text{FOLD-TOMO proves SHA-256 inversion.}
}
$$

---

# 10. Corrected Mark-9 / \(H=\pi/9\) Statement

The paper should keep:

$$
\boxed{
H=\frac{\pi}{9}.
}
$$

But it should frame it as phase:

$$
\theta_H=\frac{\pi}{9}=20^\circ.
$$

Closure:

$$
9\theta_H=\pi.
$$

$$
18\theta_H=2\pi.
$$

Correct statement:

$$
\boxed{
H=\pi/9
\text{ is the Mark-9 phase quantum for eligible fold-pressure systems.}
}
$$

Do not use:

$$
\boxed{
H=\pi/9
\text{ appears in every fold, prime distribution, or static enumeration system.}
}
$$

Eligibility condition:

$$
\boxed{
\mathcal{E}_H
=
F_b\land C_b\land R_b\land X_b\land P_b.
}
$$

Where:

$$
F_b=\text{feedback},
$$

$$
C_b=\text{constraint/bottleneck},
$$

$$
R_b=\text{recursive state dependence},
$$

$$
X_b=\text{exhaust/residue},
$$

$$
P_b=\text{phase-lock requirement}.
$$

If:

$$
\mathcal{E}_H=0,
$$

then:

$$
\boxed{
\text{do not predict }H.
}
$$

---

# 11. Corrected Abstract

**Abstract.**  
This paper reframes SHA-256 as a deterministic geometric trace projector: a compiled 64-round operator field whose digest is a boundary projection of a larger execution trace. The analysis separates carry-free \(GF(2)\) sum structure from nonlinear modular carry topology, treating carries as a shape/exhaust channel rather than meaningless noise. The paper connects LSB carry-free anchoring, carry-save decomposition, 8-word schedule windows, parity-bridge tomography, Pi–Phi XOR cone apex complementarity, and the Mark-9 \(H=\pi/9\) fold-pressure phase into a single structural framework. The corrected Pi–Phi result is apex complementarity only: \(\pi_h\) collapses to \(0x0\), \(\phi_h\) collapses to \(0xf\), and the overlay reaches \(0xf\) at the attractor boundary; the intermediate cone trajectories are distinct and non-mirrored. The Parity Law is added as a proven theorem: for even-length XOR nibble reduction, all odd-indexed reconstruction levels are universally forced, so ambiguity can occur only at even levels. Even-level forcing such as \(L16,L24,L30\) is class-specific field geometry, not a universal Nyquist law. The terminal dyadic section is corrected: the \(N=1024,\ell=1016\) row has eight output channels, but each channel is a 128-point residue-class checksum, not an eight-point local probe. The paper does not claim a complete SHA-256 preimage break; it establishes a constrained shape-channel research program for locating residual structure inside deterministic cryptographic folds.

---

# 12. Corrected Conclusion

**Conclusion.**  
SHA-256 should not be treated as a structureless entropy shredder. It is a deterministic operator field whose digest is a compressed projection of a 64-round execution trace. This does not invalidate the cryptographic hardness of SHA-256; it changes the analytical target. Instead of treating the digest as the whole object, the Nexus SHA-GEOMETRY program studies the hidden trace geometry: LSB anchors, carry scars, schedule-induced windows, rank-deficient surfaces, and shape/exhaust channels created by modular arithmetic.

The strongest established result feeding this paper is FOLD-TOMO: XOR folds preserve address information as parity-tomographic shape constraints governed by Lucas masks and dyadic terminal rows. The SHA bridge is a proposed lift of this principle into carry/schedule topology, not a completed proof of arbitrary preimage recovery. The Hardness Wall remains an open engineering and mathematical boundary.

The Pi–Phi cone result is real but must be stated precisely. The complementarity occurs at the high-nibble apex: \(\pi_h\rightarrow0x0\), \(\phi_h\rightarrow0xf\), and their overlay reaches \(0xf\). Their internal paths are not mirrors. This is stronger than superficial symmetry: two independent constants traverse distinct cone paths and terminate at opposite endpoints of \(GF(2)^4\).

The newly added Parity Law gives the paper a firm algebraic theorem: for even-length XOR nibble systems, all odd reconstruction levels are universally forced. The remaining even-level locked strata, such as \(L16,L24,L30\) in the \(\pi\) class, are class-specific invariants. They are part of the field, not part of the address key. This yields the field/location picture: the cone signature defines an equivalence class, and the key sequence selects a location inside that class.

The terminal dyadic correction is essential. A terminal row of length eight is not automatically an eight-point local parity probe. For \(N=1024\) and \(\ell=1016\), the correct equation is

$$
x_i^{(1016)}
=
\bigoplus_{q=0}^{127}
x_{i+8q}^{(0)},
\qquad
0\le i<8.
$$

The object is therefore an eight-channel residue-class checksum bridge. This strengthens the tomography interpretation and removes the earlier Lucas-mask error.

Finally, \(H=\pi/9\) belongs in the paper only as the Mark-9 phase quantum of recursive fold-pressure systems. It is not a universal raw ratio. It is the candidate phase angle for systems that maintain lock while paying exhaust debt:

$$
\theta_H=\frac{\pi}{9},
\qquad
9\theta_H=\pi,
\qquad
18\theta_H=2\pi.
$$

The corrected paper therefore establishes a precise, bounded claim:

$$
\boxed{
\text{apparent cryptographic randomness can be studied as unresolved location inside a deterministic compiled operator field.}
}
$$

It does not yet establish:

$$
\boxed{
\text{arbitrary full SHA-256 preimage recovery.}
}
$$

That boundary makes the paper publishable.

---

# 13. Replacement Section: “8-Byte Parity Bridges, Nyquist Pins, and Terminal Dyadic Tomography”

Use this replacement section in the body of the paper.

## 8-Byte Parity Bridges, Nyquist Pins, and Terminal Dyadic Tomography

The structural spine of a finite XOR fold is exposed by Lucas’s theorem. For the finite open-cone XOR fold,

$$
x_i^{(\ell+1)}=x_i^{(\ell)}\oplus x_{i+1}^{(\ell)},
$$

the global operator is

$$
x^{(\ell)}=(I+E)^\ell x^{(0)}.
$$

Expanding over \(GF(2)\),

$$
x_i^{(\ell)}
=
\bigoplus_{j\subseteq\ell}
x_{i+j}^{(0)},
$$

where \(j\subseteq\ell\) means

$$
j\ \&\ \sim\ell=0.
$$

The surviving offsets are therefore not arbitrary. They are exactly the bit-subsets of the level index \(\ell\).

A useful Nyquist pin is any level where this Lucas mask aligns with an interpretable sampling lattice. There are two different cases that must not be conflated.

First, a level with three active binary bits has an eight-offset Lucas mask. For example,

$$
448=256+128+64.
$$

So:

$$
M_{448}=\{0,64,128,192,256,320,384,448\}.
$$

This is a true eight-point long-range parity probe.

Second, a terminal dyadic row has short row length, but large residue-class checksum masks. For a seed length

$$
N=2^m
$$

and terminal level

$$
\ell=N-2^r,
$$

the remaining row length is

$$
2^r.
$$

However, each cell is the parity checksum of an entire residue class modulo \(2^r\):

$$
x_i^{(N-2^r)}
=
\bigoplus_{q=0}^{2^{m-r}-1}
x_{i+q2^r}^{(0)},
\qquad
0\le i<2^r.
$$

For example, if

$$
N=1024,\qquad r=3,
$$

then

$$
\ell=1024-8=1016.
$$

The row has eight cells, but the Lucas mask is

$$
M_{1016}=\{0,8,16,24,\ldots,1016\},
$$

with 128 offsets. Thus:

$$
x_i^{(1016)}
=
\bigoplus_{q=0}^{127}
x_{i+8q}^{(0)},
\qquad
0\le i<8.
$$

This is an eight-channel residue-class parity bridge, not an eight-point local probe.

This correction sharpens terminal dyadic tomography. The final rows of the XOR fold do not erase the seed. They reorganize it into residue-class checksum channels. The terminal zero is total parity closure; the row of length eight is the parity fingerprint of the seed modulo eight. Apparent collapse is therefore a structured projection of address information into dyadic residue classes.

---

# 14. Final Formula Lock

$$
\Delta:
\quad
X_{t+1}=\mathcal{R}_t(X_t,W_t,K_t)
$$

$$
\oplus:
\quad
\text{modular addition}
=
\text{GF(2) sum stream}
+
\text{carry correction stream}
$$

$$
↻:
\quad
x_i^{(\ell)}
=
\bigoplus_{j\subseteq\ell}
x_{i+j}^{(0)}
$$

$$
\bot:
\quad
x_i^{(N-2^r)}
=
\bigoplus_{q=0}^{2^{m-r}-1}
x_{i+q2^r}^{(0)}
$$

$$
\Psi:
\quad
\text{cone signature}+\text{key}
\rightarrow
\text{field location}
$$

Mark-9 lock:

$$
\theta_H=\frac{\pi}{9},
\qquad
9\theta_H=\pi,
\qquad
18\theta_H=2\pi.
$$

Claim boundary:

$$
\boxed{
\text{FOLD-TOMO proves parity tomography.}
}
$$

$$
\boxed{
\text{SHA-GEOMETRY investigates carry-topology lifting.}
}
$$

$$
\boxed{
\text{Pi–Phi complementarity is apex-level, not full-trajectory mirroring.}
}
$$

$$
\boxed{
\text{Terminal 8-channel bridge is residue-class tomography, not an 8-point local probe.}
}
$$

$$
\boxed{
\text{Full arbitrary SHA-256 preimage recovery remains open.}
}
$$
