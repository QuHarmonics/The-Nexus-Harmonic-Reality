# SHA-256 as a Geometric Trace Projector: Carry Topology, Pi-Phi Cone Apex Complementarity, and Mark-9 Fold-Pressure Phase

**Author:** Dean Kulik  
**Draft type:** Corrected preprint manuscript  
**Research branch:** SHA-GEOMETRY / PI-PHI / MARK-9  
**Linked branches:** FOLD-TOMO, PI-NINTH-LOOM, Nexus Fold Pressure  
**Date:** May 2026

---

## Abstract

SHA-256 is normally analyzed as a cryptographic compression function whose output is designed to behave like a pseudorandom digest. That abstraction is useful for security modeling, but it can obscure the fact that SHA-256 is also a fully deterministic 64-round operator field with a rigid internal topology. This paper develops a bounded structural model of SHA-256 as a geometric trace projector: the digest is treated as a boundary projection of a larger execution trace rather than as the full trace itself. The analysis separates carry-free `GF(2)` sum structure from nonlinear modular carry propagation, identifying the carry channel as a candidate shape or exhaust channel that records local correction history. The paper connects this carry topology to finite-cone XOR tomography, Pi-Phi apex complementarity, terminal dyadic checksum rows, and the Mark-9 phase interpretation of `H = pi/9`.

Several corrections are made relative to earlier drafts. First, Pi-Phi complementarity is stated only at the high-nibble apex: `pi_h` collapses to `0x0`, `phi_h` collapses to `0xf`, and their apex overlay reaches `0xf`. The internal cone trajectories are not claimed to be mirrored or element-wise complementary. Second, the Parity Law is added as a theorem: for an even-length finite XOR reconstruction system, all odd-indexed reconstruction levels are universally forced, so ambiguity can occur only at even-indexed levels. Third, even-level forcing such as `L16`, `L24`, and `L30` is treated as class-specific field geometry rather than a universal Nyquist law. Fourth, the terminal dyadic row at `N = 1024`, `ell = 1016` is corrected: the row has eight output channels, but each channel is a 128-point residue-class checksum, not an eight-point local probe. Finally, this paper does not claim a completed arbitrary SHA-256 preimage attack. It establishes a structural research program for locating residual address information inside deterministic cryptographic folds.

**Keywords:** SHA-256, carry topology, XOR tomography, Lucas theorem, Pi-Phi complementarity, Mark-9 phase, `H = pi/9`, finite-field geometry, cryptographic trace projection

---

## 1. Introduction

Cryptographic hash functions are usually modeled at the interface level. A message enters the function; a fixed-width digest leaves the function; the digest is expected to behave as if it were sampled from a pseudorandom distribution. For security proofs and adversarial reasoning, this viewpoint is appropriate. It abstracts away the implementation and asks whether an adversary can distinguish, invert, or collide the function efficiently.

The present work studies a different object. It does not treat SHA-256 only as an input-output oracle. It treats SHA-256 as a deterministic execution process with an internal trace. Under this viewpoint, the 256-bit digest is not the whole mathematical object. It is the final boundary projection of a structured sequence of scheduled rotations, Boolean gates, modular additions, carry propagations, constants, and state-register updates.

The central thesis is not that SHA-256 is insecure, nor that a complete practical preimage attack has been demonstrated. The central thesis is narrower: SHA-256 can be modeled as a deterministic geometric trace projector whose digest is a compressed boundary projection of a larger execution trace.

This claim shifts the analytical target. Instead of asking only whether the digest appears random, we ask what structural residues are preserved by the internal trace and whether these residues form useful constraints. The answer developed here is that several channels are structurally meaningful: the carry-free least-significant-bit anchor, the split between sum stream and carry stream, rank-deficient local windows, finite-cone parity tomography, and terminal dyadic checksum channels.

Earlier drafts of this paper overstated some conclusions. In particular, they sometimes treated structural invertibility, partial trace recovery, or analogy with finite XOR systems as if these implied full SHA-256 preimage recovery. This corrected version separates four claim classes: theorem, verified computation, model interpretation, and open problem. FOLD-TOMO proves parity tomography for finite XOR folds. SHA-GEOMETRY investigates whether analogous address residues survive in SHA carry and schedule topology. These are linked, but they are not the same theorem.

---

## 2. Claim Status Ledger

The corrected claim ledger is as follows.

| Statement | Status |
|---|---|
| The finite open-cone XOR fold satisfies `x^(ell) = (I + E)^ell x^(0)`. | Theorem |
| Lucas masks determine the surviving offsets `j subset ell`. | Theorem |
| For even `n`, odd reconstruction levels are universally forced. | Theorem |
| Terminal dyadic rows are residue-class parity checks. | Theorem |
| At `N = 1024`, `ell = 1016`, the row has 8 output cells, each a 128-point checksum. | Theorem |
| `pi_h -> 0x0` and `phi_h -> 0xf` at the high-nibble cone apex. | Verified computation, if reproduced by the supplied notebook |
| Pi and Phi are complementary at every internal cone level. | Not claimed; generally false |
| `L16`, `L24`, and `L30` are forced for the `pi` class. | Verified computation / class-specific field geometry |
| `L16`, `L24`, and `L30` are universally forced for all sequences. | Not claimed; false |
| SHA-256 has deterministic carry, schedule, and LSB-anchor structure. | Structural fact |
| Full arbitrary SHA-256 preimage recovery is solved. | Not claimed; open problem |
| `H = pi/9` is a Mark-9 phase hypothesis for eligible fold-pressure systems. | Model / hypothesis |
| `H = pi/9` appears automatically in every static number system. | Not claimed; false |

---

## 3. SHA-256 as a Deterministic Trace Projector

Let a one-block SHA-256 compression function be represented as

$$
\mathcal{S}:(M,H_{\mathrm{in}})\mapsto H_{\mathrm{out}},
$$

where `M` is the padded message block, `H_in` is the incoming chaining state, and `H_out` is the outgoing chaining state.

The standard interface view reads

$$
H_{\mathrm{out}}=\mathcal{S}(M,H_{\mathrm{in}})
$$

as a fixed-width digest. The trace-projector view inserts the internal execution trace:

$$
\Gamma_{\mathrm{exec}}=(X_0,X_1,\ldots,X_{64}),
$$

where each `X_t` contains the working registers, schedule word, round constant, and intermediate quantities at round `t`. The digest is then a projection:

$$
H_{\mathrm{out}}=\Pi_{\mathrm{digest}}(\Gamma_{\mathrm{exec}}).
$$

This statement is not cryptographically controversial. It simply says that the digest is the endpoint of a deterministic transition system. The research question is whether useful structural information can be recovered from the geometry of that transition system.

The SHA-256 working state is

$$
X_t=(a_t,b_t,c_t,d_t,e_t,f_t,g_t,h_t).
$$

The round transition can be written

$$
X_{t+1}=\mathcal{R}_t(X_t,W_t,K_t),
$$

and the full compression as

$$
X_{64}=\mathcal{R}_{63}\circ\cdots\circ\mathcal{R}_1\circ\mathcal{R}_0(X_0).
$$

The trace-projector model treats the round sequence `Gamma_exec` as the primary object and the digest as its boundary readout.

---

## 4. SHA-256 Round Structure

The SHA-256 round uses the Boolean functions

$$
Ch(e,f,g)=(e\land f)\oplus(\neg e\land g),
$$

$$
Maj(a,b,c)=(a\land b)\oplus(a\land c)\oplus(b\land c),
$$

and the large sigma functions

$$
\Sigma_0(a)=ROTR^2(a)\oplus ROTR^{13}(a)\oplus ROTR^{22}(a),
$$

$$
\Sigma_1(e)=ROTR^6(e)\oplus ROTR^{11}(e)\oplus ROTR^{25}(e).
$$

The round temporaries are

$$
T_1=h+\Sigma_1(e)+Ch(e,f,g)+K_t+W_t \pmod{2^{32}},
$$

$$
T_2=\Sigma_0(a)+Maj(a,b,c) \pmod{2^{32}}.
$$

The register update is

$$
h'=g,\quad g'=f,\quad f'=e,
$$

$$
e'=d+T_1\pmod{2^{32}},
$$

$$
d'=c,\quad c'=b,\quad b'=a,
$$

$$
a'=T_1+T_2\pmod{2^{32}}.
$$

The important structural point is that SHA-256 is not a monolithic random event. It is a deterministic composition of Boolean and modular operators. Any inversion or constraint-recovery program must respect that internal structure.

---

## 5. Sum Stream and Carry Stream

Modular addition is the main source of nonlinear coupling in SHA-256. To expose its structure, begin with ordinary binary addition.

For two operands `x` and `y`, the bitwise sum satisfies

$$
s_i=x_i\oplus y_i\oplus c_i,
$$

where `c_i` is the incoming carry at bit `i`. The carry recurrence is

$$
c_{i+1}=(x_i\land y_i)\lor(x_i\land c_i)\lor(y_i\land c_i).
$$

At the least significant bit,

$$
c_0=0.
$$

Therefore,

$$
s_0=x_0\oplus y_0.
$$

For multi-operand addition, the least-significant bit still has no incoming carry. The LSB is therefore the carry-free anchor of the addition.

This gives a useful split:

$$
\text{modular addition}=\text{carry-free }GF(2)\text{ sum stream}+\text{carry correction stream}.
$$

The sum stream is the linear scaffold. The carry stream is the nonlinear correction required to make the addition valid over `Z / 2^32 Z`. In the Nexus terminology used in earlier work, the carry stream is a candidate shape or exhaust channel: it records the correction debt paid by modular arithmetic.

This does not make SHA-256 linear. It means that part of its structure can be separated into a linear component and a nonlinear correction component.

---

## 6. Carry-Save Decomposition as Structural Unbraiding

Carry-save addition gives a hardware-level way to separate sum and carry components. For three operands `x`, `y`, and `z`, define

$$
s=x\oplus y\oplus z,
$$

and

$$
c=(x\land y)\lor(x\land z)\lor(y\land z).
$$

Then

$$
x+y+z=s+2c.
$$

The shifted carry term `2c` is the nonlinear correction. The term `s` is the carry-free `GF(2)` scaffold.

This decomposition is valuable because it prevents the linear channel from being immediately conflated with the carry channel. A solver or analysis method can use the `GF(2)` scaffold for linear constraints while separately tracking carries as branch variables or correction variables. This is the foundation of the structural recovery program proposed here.

---

## 7. Relation to FOLD-TOMO

FOLD-TOMO is the stronger algebraic root branch. It studies finite open-cone XOR folds, not SHA-256 directly.

The finite XOR fold is

$$
x_i^{(\ell+1)}=x_i^{(\ell)}\oplus x_{i+1}^{(\ell)}.
$$

Let `E` be the shift operator, `(Ex)_i = x_{i+1}`, and `I` the identity. Then

$$
x^{(\ell)}=(I+E)^\ell x^{(0)}.
$$

Expanding over `GF(2)`,

$$
x_i^{(\ell)}=\bigoplus_{j=0}^{\ell}\left(\binom{\ell}{j}\bmod2\right)x_{i+j}^{(0)}.
$$

Lucas's theorem gives

$$
\binom{\ell}{j}\equiv1\pmod2\iff j\ \&\ \sim\ell=0.
$$

Define `j subset ell` to mean that every binary 1-bit of `j` is also a binary 1-bit of `ell`. Then

$$
x_i^{(\ell)}=\bigoplus_{j\subseteq\ell}x_{i+j}^{(0)}.
$$

This is the key FOLD-TOMO theorem: every row is a structured parity probe of the seed.

The SHA bridge is not that SHA-256 is literally Rule 90. It is that FOLD-TOMO supplies a rigorous model of address displacement into shape constraints, while SHA-GEOMETRY investigates whether related address residues survive in SHA carry topology, schedule topology, LSB anchors, rank-deficient windows, and terminal/carry scars.

---

## 8. The Parity Law for Reconstruction Levels

The reconstruction problem asks which seed choices remain possible at each inverse level of an XOR nibble cone. The following theorem separates universal forcing from class-specific forcing.

### Theorem 1. Odd reconstruction levels are universally forced for even-length sequences.

Let the original sequence length `n` be even. At reconstruction level `k`, the row length is

$$
n-k.
$$

For a seed bit `b` to remain free, exactly half of the relevant prefix-XOR values must have that bit set:

$$
N_b=\frac{n-k}{2}.
$$

If `k` is odd and `n` is even, then `n-k` is odd. Therefore,

$$
\frac{n-k}{2}\notin\mathbb{Z}.
$$

But `N_b` is an integer. Thus equality is impossible:

$$
N_b\neq\frac{n-k}{2}.
$$

Therefore no bit is free and exactly one seed survives at that reconstruction level. Consequently,

$$
n\text{ even},\quad k\text{ odd}\quad\Rightarrow\quad\text{level }k\text{ is forced}.
$$

Equivalently, ambiguity can occur only at even-indexed reconstruction levels.

This theorem is universal for the finite XOR nibble system. It does not prove that all even levels are ambiguous or that all even forcing is universal. Even-level forcing is class-specific.

---

## 9. Field, Location, and Class-Specific Forced Strata

Let `C(x)` be the cone signature of a sequence `x`. It may include apex value, row-sum trajectory, rebound pattern, terminal parity, or other trace features, depending on the experiment. The associated field is the equivalence class

$$
\mathcal{F}_{C}=\{y:C(y)=C(x)\}.
$$

The key sequence selects a member of that field:

$$
K_x=\text{location coordinate inside }\mathcal{F}_{C}.
$$

The corrected interpretation is:

$$
\text{cone signature}\rightarrow\text{field},
$$

$$
\text{key}\rightarrow\text{location}.
$$

Some reconstruction levels are branchable and contribute address bits. Other levels are forced and belong to the field geometry itself.

For the `pi` high-nibble class, the levels

$$
L16,\quad L24,\quad L30
$$

are treated as class-specific locked strata. They should not be described as universal consequences of the Parity Law. The universal theorem forces odd-indexed levels for even `n`. The even forced levels are additional invariants of the particular cone class.

This distinction prevents a common error: interpreting every forced level as a universal law. The correct picture is that universal parity constraints define part of the reconstruction grammar, while class-specific forcing defines the geometry of the particular field.

---

## 10. Nyquist Pins and Lucas Masks

A Nyquist pin is a level where the Lucas mask aligns with an interpretable sampling lattice. The term should not mean that every power-of-two row length is automatically forced or that every short terminal row is an eight-point local probe.

For example,

$$
448=256+128+64.
$$

Thus

$$
M_{448}=\{0,64,128,192,256,320,384,448\}.
$$

This is an eight-point long-range parity probe. Each output cell at level `448` samples eight ancestral locations separated by 64.

The important distinction is that an eight-point probe is not the same thing as an eight-channel terminal row. The former is controlled by the popcount of the level. The latter is controlled by terminal dyadic residue classes.

---

## 11. Terminal Dyadic Tomography

The terminal dyadic rows of a finite XOR fold are exactly describable.

### Theorem 2. Terminal dyadic rows are residue-class parity checks.

Let

$$
N=2^m
$$

and let

$$
\ell=N-2^r.
$$

Then the remaining row length is

$$
N-\ell=2^r.
$$

For each output index `0 <= i < 2^r`,

$$
x_i^{(N-2^r)}=\bigoplus_{q=0}^{2^{m-r}-1}x_{i+q2^r}^{(0)}.
$$

Thus each terminal row cell is the parity checksum of one residue class modulo `2^r`.

### Correction for `N = 1024`, `ell = 1016`

Let

$$
N=1024=2^{10},
$$

and

$$
\ell=1016=1024-8.
$$

Then `r = 3`, and the row length is

$$
2^3=8.
$$

However, each row cell is not an eight-point local probe. Since

$$
1016=1111111000_2,
$$

the surviving offsets are all multiples of 8:

$$
M_{1016}=\{0,8,16,24,\ldots,1016\}.
$$

There are

$$
\frac{1016}{8}+1=128
$$

surviving offsets. Therefore,

$$
x_i^{(1016)}=\bigoplus_{q=0}^{127}x_{i+8q}^{(0)},\qquad0\le i<8.
$$

The corrected interpretation is that level `1016` is an 8-channel residue-class bridge, not an 8-point local probe. This correction strengthens the tomography interpretation. The row of length eight is not weak; it is a compact residue-class checksum of the entire seed.

---

## 12. Pi-Phi Cone Apex Complementarity

Earlier drafts overextended the Pi-Phi result. The corrected statement is apex-level only.

For the high-nibble stream, the verified endpoint behavior is

$$
\pi_h\rightarrow0x0,
$$

$$
\phi_h\rightarrow0xf.
$$

Therefore, at the apex,

$$
\pi_{h,\mathrm{apex}}\oplus\phi_{h,\mathrm{apex}}=0x0\oplus0xf=0xf.
$$

This is apex complementarity.

It does not imply

$$
\pi_h(\ell,i)\oplus\phi_h(\ell,i)=0xf
$$

for every internal level `ell` and index `i`. The internal paths are distinct and should not be described as mirrored.

The corrected interpretation is that `pi` and `phi` traverse different cone trajectories and terminate at opposite endpoints of the high-nibble field.

---

## 13. Mark-9 Phase and `H = pi/9`

The corrected Mark-9 statement treats `H` as a phase quantity before treating it as a measured ratio.

Define

$$
\theta_H=\frac{\pi}{9}.
$$

Then

$$
\theta_H=20^\circ,
$$

$$
9\theta_H=\pi,
$$

and

$$
18\theta_H=2\pi.
$$

Thus `H = pi/9` is interpreted as the phase quantum of a nine-step half-turn correction loom.

This should not be confused with a universal raw percentage. The observed correction-pressure ratio must be defined separately. Let

$$
R_t=\text{retained structure},
$$

and

$$
C_t=\text{correction or update pressure}.
$$

Then

$$
H_{\mathrm{obs}}=\frac{\|C_t\|}{\|R_t\|+\|C_t\|+\epsilon}.
$$

The Mark-9 hypothesis predicts

$$
H_{\mathrm{obs}}\approx\frac{\pi}{9}
$$

only for systems that satisfy the `H`-eligibility condition.

---

## 14. H-Eligibility

A system is `H`-eligible only when it has feedback, constraint, recursive state dependence, exhaust or residue, and a phase-lock requirement. Define

$$
\mathcal{E}_H=F_b\land C_b\land R_b\land X_b\land P_b.
$$

Here,

$$
F_b=\text{feedback},
$$

$$
C_b=\text{constraint or bottleneck},
$$

$$
R_b=\text{recursive state dependence},
$$

$$
X_b=\text{exhaust or residue},
$$

and

$$
P_b=\text{phase-lock requirement}.
$$

If

$$
\mathcal{E}_H=0,
$$

then `H` should not be predicted.

This prevents `H = pi/9` from being incorrectly attached to static enumeration systems or arbitrary ratios. In the SHA setting, `H` is not predicted from raw digest bits. It is a candidate fold-pressure phase for carry/correction dynamics, solver feedback loops, or other recursive constraint systems that must pay exhaust debt while maintaining phase-lock.

---

## 15. Exhaust Debt and Carry Topology

A stable recursive system does not maintain phase-lock by eliminating all error. It maintains phase-lock by paying correction debt fast enough that residue does not accumulate beyond tolerance.

Let

$$
\phi_t=\text{phase error},
$$

$$
E_{\mathrm{exhaust}}(t)=\text{available residue removal or correction dissipation},
$$

and

$$
C_{\mathrm{correction}}(t)=\text{cost of correction}.
$$

A stable lock requires

$$
|\phi_t|<\epsilon
$$

while

$$
E_{\mathrm{exhaust}}(t)\ge C_{\mathrm{correction}}(t).
$$

In SHA-256, carry bits are a natural candidate for local exhaust debt. They are generated when the `GF(2)` scaffold is lifted into modular arithmetic. They are not arbitrary noise; they are the correction required to make addition consistent in `Z / 2^32 Z`.

This does not mean that the carry channel alone reveals the preimage. It means that the carry channel is structurally meaningful and should be modeled as part of the execution trace.

---

## 16. The 8-Unit Geometry as Modeling Scaffold

The paper uses 8-unit geometry because SHA-256 has eight working state words,

$$
(a,b,c,d,e,f,g,h),
$$

and because eight-direction plus rest-state models such as D2Q9 provide an intuitive scaffold:

$$
8\text{ directions}+1\text{ rest state}=9\text{ local modes}.
$$

This should be presented as a modeling analogy, not as proof that SHA-256 is literally a fluid system. The safe statement is that the 8-unit model is a useful geometric scaffold for reasoning about directional propagation, register rotation, carry flow, and rest-state anchoring.

The unsafe statement is that SHA-256 is proven to be a hydrodynamic lattice. The scientific version keeps the analogy but ties all claims back to executable algebra, trace logs, or testable predictions.

---

## 17. Implications for SHA Inversion Research

The corrected paper supports a structural research program. It does not complete that program.

The research targets are:

1. Identify rank-deficient windows in Booleanized SHA circuits.
2. Separate carry-free `GF(2)` constraints from nonlinear carry constraints.
3. Measure whether carry topology provides solver advantage over blind search.
4. Track LSB-anchor propagation through schedule and round equations.
5. Compare carry-scar statistics against random controls.
6. Test whether Pi-Phi cone signatures classify boundary conditions or merely visualize them.
7. Determine whether Mark-9 phase metrics appear in eligible correction-pressure traces.

The open inversion question can be stated as follows: Can carry topology, LSB anchoring, rank-deficient windows, and trace-shape constraints reduce SHA-256 preimage recovery beyond random-oracle search in a reproducible, scalable way?

This remains open.

---

## 18. Methods Required for Publication-Grade Validation

To make the framework publication-grade, the following must be attached as executable notebooks or scripts.

### 18.1 FOLD-TOMO algebra notebook

This notebook must verify

$$
x_i^{(\ell)}=\bigoplus_{j\subseteq\ell}x_{i+j}^{(0)}.
$$

It must include the terminal dyadic theorem and the corrected `1016` case.

### 18.2 Pi-Phi cone notebook

This notebook must verify

$$
\pi_h\rightarrow0x0,
$$

$$
\phi_h\rightarrow0xf,
$$

and must explicitly test that internal paths are not assumed to be mirrors.

### 18.3 Carry topology notebook

This notebook must compute LSB anchors and carry constraints on actual SHA round equations.

### 18.4 Rank / solver notebook

This notebook must report rank, nullity, and solver advantage relative to controls.

### 18.5 Mark-9 phase notebook

This notebook must test 18-phase residue organization against random controls and other constants.

Without these notebooks, the paper should be treated as a structural hypothesis paper rather than a completed proof paper.

---

## 19. Discussion

The corrected paper preserves the valuable central idea: cryptographic randomness may be studied as unresolved location inside a deterministic operator field. A digest is not the entire trace. It is a final projection. If structural information survives in the trace, then inversion research should not be limited to blind preimage guessing.

The main danger is overstatement. SHA-256 is deliberately designed so that digest-level statistics are pseudorandom and preimage recovery is computationally infeasible by known methods. A structural model does not overturn that fact by itself. It becomes significant only when it produces reproducible constraints, solver advantage, or exact recovery in reduced or controlled settings.

FOLD-TOMO provides a genuine algebraic proof branch because Rule-90 cones are exactly governed by Lucas masks. The SHA case is harder because SHA includes rotations, Boolean nonlinearities, message expansion, modular addition, and carries. The correct scientific move is to use FOLD-TOMO as the algebraic template and then test whether SHA has analogous recoverable trace channels.

The Pi-Phi apex result is interesting because it suggests endpoint complementarity between two constants under a cone projection. However, the result must be kept at the apex unless full-level complementarity is proven. This makes the result more credible, not less. A precise endpoint complementarity is publishable; an unsupported full-trajectory symmetry is not.

The Mark-9 `H = pi/9` interpretation is also useful if kept in its correct category. It is a phase hypothesis for fold-pressure systems with feedback, constraint, residue, and phase-lock. It should not be used as a universal pattern-matching constant.

---

## 20. Conclusion

SHA-256 is a deterministic 64-round operator field. Its digest is a boundary projection of a richer execution trace. This paper develops a corrected structural model in which the trace is analyzed through carry topology, `GF(2)` sum scaffolds, terminal dyadic tomography, Pi-Phi cone apex complementarity, and Mark-9 fold-pressure phase.

The strongest theorem-level results come from the finite XOR fold. Lucas's theorem gives an exact parity-sampling law, and terminal dyadic rows are exact residue-class checksum channels. The corrected `N = 1024`, `ell = 1016` case is decisive: the row has eight output channels, but each channel folds 128 ancestral positions. This is terminal tomography, not an eight-point local probe.

The Pi-Phi result is retained as apex complementarity: `pi_h` collapses to `0x0`, `phi_h` collapses to `0xf`, and the overlay reaches `0xf` at the attractor boundary. The internal trajectories are not claimed to be mirrors.

The SHA claim is bounded. FOLD-TOMO proves parity tomography. SHA-GEOMETRY investigates carry-topology lifting. Full arbitrary SHA-256 preimage recovery remains open.

The corrected final claim is therefore this: apparent cryptographic randomness can be studied as unresolved location inside a deterministic compiled operator field, but structural trace analysis must be distinguished from completed cryptographic inversion.

---

## References and Source Notes

This corrected manuscript is prepared as an internal preprint draft for the Nexus SHA-GEOMETRY / PI-PHI / MARK-9 branch. It is designed to replace prose that overstates inversion claims or conflates distinct algebraic objects.

Primary linked internal branches:

1. FOLD-TOMO finite-cone XOR tomography and dyadic terminal rows.
2. Pi-Phi cone apex complementarity experiments.
3. SHA carry topology and LSB anchor analysis.
4. Mark-9 `H = pi/9` fold-pressure phase notes.
5. Projection Diode / shape-channel residual methodology.

Formal bibliographic entries should be normalized before external publication.
