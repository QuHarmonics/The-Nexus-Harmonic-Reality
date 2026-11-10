# NEXUS — Closed-Route Reversal, Facing and the Reader Seam

**Dean A. Kulik · QuHarmonics Research Group · ORCID 0009-0003-3128-8828**  
**Independent interface-side audit · 5 November 2026**

**Source:** *Facing, Composition and the Center in Native Binary Rings*, §§3, 6–8, 11, 14, and the accompanying `NEXUS_Facing_Manual_scripts.zip`. The source manuscript and scripts are unchanged.

## Result in one sentence

The binary contact wheel's complete closed-route space admits an **exact, all-LEN reversal decomposition**; the native conditional partner `P` does **not** descend to unbased closed routes unless the reader's seam/starting phase is supplied. These are different operations and must not be conflated.

## 1. Domain objects, before readout

Let `B(n)` be the binary de Bruijn contact wheel:

- Vertex/contact face space `V_n`: all `n`-bit faces (`2^n` vertices).
- Edge/contact space `E_n`: all `(n+1)`-bit contacts (`2^(n+1)` edges).
- An edge `e=b_0...b_n` has `IN(e)=b_0...b_{n-1}` and `OUT(e)=b_1...b_n`.
- Its binary boundary is `∂e = IN(e)+OUT(e)` in the vector space on vertices over `F_2`.
- The closed-route (binary cycle) space is `Z_n=ker ∂`. As `B(n)` is connected, `dim Z_n=2^(n+1)-2^n+1=2^n+1`.

This counts **independent mod-2 route directions**, not the number of distinct simple cycles, and not an implementation's observed times.

Let `J_E` reverse `(n+1)`-bit edge words and `J_V` reverse `n`-bit vertex words. Then

`∂ J_E = J_V ∂`.

Hence `J_E` maps closed routes to closed routes, and `J_E^2=I` on `Z_n`.

## 2. All-LEN closed-route reversal theorem — STANDS

Define

\[
V=2^n,\qquad p_n=2^{\lceil n/2\rceil},\qquad q_n=2^{\lceil(n+1)/2\rceil}.
\]

`p_n` counts palindrome vertices and `q_n` counts palindrome edges.

The reversal-invariant edge-chain space has dimension `(2V+q_n)/2`: each palindrome edge is fixed, and each nonpalindrome pair contributes its sum.

**Boundary-image lemma:**

\[
\partial(E_n^{J_E})=\operatorname{im}(I+J_V).
\]

*Proof, inclusion:* the boundary of a palindrome edge is `v+J_V(v)` and the boundary of an edge pair `e+J_E(e)` is `(I+J_V)∂e`; both lie in `im(I+J_V)`.

*Proof, reverse inclusion:* for any vertex `v`, choose a route `c` from `v` to the palindrome vertex `0^n` (the de Bruijn wheel is connected, in fact strongly connected). Then `c+J_E(c)` is a reversal-invariant edge chain with boundary `v+J_V(v)`. Every generator of `im(I+J_V)` is represented. QED.

Therefore the fixed closed-route subspace has dimension

\[
\boxed{\dim Z_n^{J_E}=\frac{2^n+p_n+q_n}{2}.}
\]

Because `J_E^2=I` over `F_2`, its representation is a direct sum of 1-dimensional identity blocks and 2-dimensional exchanged blocks. Write `t_n` for the number of 1-blocks and `r_n` for the number of 2-blocks. Then

\[
\boxed{t_n=p_n+q_n-1,\qquad
r_n=\frac{2^n+2-p_n-q_n}{2},\qquad t_n+2r_n=2^n+1.}
\]

**Terminology:** A swapped two-dimensional block also has a one-dimensional invariant sum. Thus the *entire* fixed subspace has dimension `t_n+r_n`, not merely `t_n`.

| LEN n | Cycle-space dimension | Fixed-subspace dimension | Identity 1-blocks | Exchanged 2-blocks |
|---:|---:|---:|---:|---:|
| 1 | 3 | 3 | 3 | 0 |
| 2 | 5 | 5 | 5 | 0 |
| 3 | 9 | 8 | 7 | 1 |
| 4 | 17 | 14 | 11 | 3 |
| 5 | 33 | 24 | 15 | 9 |
| 6 | 65 | 44 | 23 | 21 |
| 7 | 129 | 80 | 31 | 49 |
| 8 | 257 | 152 | 47 | 105 |
| 9 | 513 | 288 | 63 | 225 |

All values are consequences of the formulas, not fitted outputs.

## 3. Native facing P and unbased closed routes — OPEN link identified

The manuscript defines native facing at LEN `L` as

\[
P_L(w)=\begin{cases}J_L(w),&w\neq J_L(w),\\C_L(w),&w=J_L(w).\end{cases}
\]

`J_L` gives an unambiguous reverse reading of a **cyclic route** even if we choose a different starting point, because reversal takes rotations to rotations. `P_L` can switch branches when a cyclic route is re-addressed at another starting phase.

A five-contact cyclic word has two equivalent presentations:

- `00100` (palindrome), so `P(00100)=11011` (NOT),
- `00001` (a cyclic rotation), so `P(00001)=10000` (reversal).

The resulting strings have different Hamming weights, 4 and 1, and are **not cyclic rotations** of each other. Thus `P_L` does not induce a well-defined operation on *unbased* cyclic words.

This does **not** contradict `P_L^2=I` on individual **based** words, nor the manuscript's complete-contact theorems. It names a dependency that matters for §14: to face an unbased closed route using the native conditional P, the reader must provide an origin/seam or the domain must derive a canonical seam. Otherwise classify the well-defined bare reversal `J` first.

### Seam requirement

`OPEN`: identify the native interface property which fixes a reading origin on every closed route or gives a seam-independent replacement of conditional facing. The manuscript's ring-center seam belongs to the **native word-order ring**; an arbitrary closed route of the de Bruijn contact wheel has no proven equivalent distinguished seam.

## 4. Isolated motion is an incomplete interface fingerprint

From the manuscript's own LEN-3 affine catalog: `C_3` (bitwise NOT) and `P_3` (native partner) are both fixed-point-free involutions. Each has exactly four 2-cycles, so isolated orbit lengths, number of fixed words and order cannot distinguish them.

But they differ *as contacts with other transformations*. Define translation `T_t(x)=x⊕t`.

For every `t`, `C_3 T_t = T_t C_3`. For `P_3`, choose `t=001` and `x=000`:

- `P_3(T_t(000))=P_3(001)=100`;
- `T_t(P_3(000))=T_t(111)=110`.

These are unequal. So the interaction (commutator) separates the interfaces without using a histogram of returned values or relying on their isolated orbit clocks.

This refines manuscript procedure P8: comparing solitary orbit spectra can reject an implementation, but passing the isolated-motion test does not determine an affine conjugacy class. To identify an interface, compare its **relations with other available operations** (contact-compatible compositions, commutators, orientation, return). This follows the user's constraint that the domain consists of what contracts *do*.

## 5. Ledger and seal

**STANDS:** `∂J=J∂`, cycle rank, invariant-chain boundary lemma, all-LEN reversal decomposition, native P phase obstruction, `C_3` versus `P_3` interaction distinction.

**RUNS:** `nexus_facing.py`, `audit.py`, `seam.py`, `degree.py` from the user's script archive all completed with all their asserted checks passing. Independent `NEXUS_Closed_Route_Facing_Audit.py` computed ranks through LEN 9 and checked the phase and interaction witnesses with all assertions passing.

**OPEN:** canonical route-seam/phase-owner for conditional native P; upgrade the motion reader's interface test from isolated motion to a complete contact-algebra signature. These remain domain-side requirements, not a request to fit an implementation output.

**Seal (before running the independent audit):** SHA-256 of `NEXUS_Closed_Route_Facing_Seal.txt` is

`cb051adbb1718851e6560e3e6af2f0050779105db054a47f63fe021ca4ee89e4`.

The way home is the path-plus-reversed-path construction in §2. This is an independent mathematical proof with a subsequent finite audit, not an external forward-landing claim.

## Files

- `NEXUS_Closed_Route_Facing_Audit.py` — single-file standard-library checker.
- `NEXUS_Closed_Route_Facing_Seal.txt` — complete pre-run prediction text and way home.

The original DOCX and ZIP remain unchanged.
