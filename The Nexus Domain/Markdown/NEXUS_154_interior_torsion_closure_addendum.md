# §154 — Interior torsion closure: neighboring axes versus matched collinear boundary axes

**Dean A. Kulik — QuHarmonics Research Group — ORCID 0009-0003-3128-8828**  
**Date:** 23 October 2026  
**Status:** Standalone addendum; not inserted into the published Paper I ledger. Source computations are self-contained.

## The hole and its required type

§153 provides a 3D synchronous way to realize an end turn-bit flip. If the same pair of **neighboring, noncollinear** bond-axis half-turns is applied to an **interior** bit, its endpoint is legal and the operation is reversible, but the entire downstream exterior rotates: it does not satisfy the required fixed-exterior boundary conditions.

The missing interface is therefore a path in the configuration space with all three conditions: (a) a nontrivial interior change; (b) both exterior portions remain fixed in **position and orientation at every instant**; (c) an explicit inverse. This is an **SE(3) closure condition**, not a missing endpoint turn word.

## Result 1 — Adjacent noncollinear axes cannot close the exterior

Two proper rotations about distinct, noncollinear axes cannot compose to the identity unless both rotations are trivial modulo 2π: if \(R_v(\beta)R_u(\alpha)=I\), then \(R_v(\beta)=R_u(-\alpha)\), which for nontrivial rotations requires the same rotation axis. (At π the axis is unoriented, but still unique.) Thus two neighboring noncollinear torsions cannot realize a nontrivial move that returns the **full downstream exterior pose**.

**Computational readout.** Input word `0101010101` at 10 turn bits, interior flip at \(j=5\), target `0101000101`. Two adjacent π torsions land on the precise target word but rotate the five downstream vertices through **+120°** around the hinge. Inverse execution in reverse order restores the original 3D coordinates (max float discrepancy 5.329e-15). The source geometry is self-avoiding at both ends. The result is a **valid nonlocal pivot**, not a fixed-exterior local move.

**Seal** SHA-256: `f8ee06df528edd5e56bac5acf96bf1906adb66e3dd770a3f5e428d593fd6802d` (test prepared before execution; input and the defining algebra already known).

## Result 2 — The local 1001 ↔ 0110 move has the correct two-axis interface

Consider any existing legal hexagon rewrite with turn substring `1001` or `0110` beginning at position \(i\). Let the chain have vertices \(p_0,\ldots,p_{m+1}\). The three-bond arc from \(p_{i+1}\) to \(p_{i+4}\) contains precisely two moving internal vertices \(p_{i+2},p_{i+3}\). **Its opening and closing exterior bonds**, \((p_i,p_{i+1})\) and \((p_{i+4},p_{i+5})\), lie on the **same straight line** as the fixed endpoint chord \(p_{i+1}p_{i+4}\). This follows from the heading sequence associated with `1001` or `0110`.

Define an instruction using only backbone bond axes:

1. Rotate the downstream chain around the left exterior bond axis by \(+\theta\).
2. In synchrony, rotate the still-distal chain around the right exterior bond axis by \(-\theta\).

Because the two axes are **collinear**, they implement opposite rotations about the same line. Their actions on the entire distal exterior cancel for every \(\theta\), not only at \(\theta=\pi\). Everything outside the two internal arc vertices stays fixed. The two internal vertices undergo a rigid rotation around the chord. At \(\theta=\pi\), they occupy the opposite side of the hexagon, producing exactly `1001 ↔ 0110`. Reverse \(\theta\) or repeat the π half-turn for the way home.

**All fixed-length, fixed-angle kinematics are preserved.** The arc is rigid, and both exterior bonds are themselves aligned with the rotation axis, so the boundary valence-angle cosines remain unchanged along the entire route.

**Ideal zero-thickness collision theorem.** Every moving and fixed bond point begins in the same plane and ends in that plane. For a moving point \(p\), fixed point \(q\), and rotation \(R_\theta\) about the chord axis,

\[
\|R_\theta p-q\|^2=\frac{1+\cos\theta}{2}\|p-q\|^2+\frac{1-\cos\theta}{2}\|R_\pi p-q\|^2.
\]

Both coefficients are nonnegative on \([0,\pi]\). Thus the separation between **any nonincident moving/fixed bond pair** at intermediate times is at least the smaller of its two planar endpoint separations. Endpoints are required to be self-avoiding lattice chains; for the planar honeycomb, nonincident bonds do not intersect at either endpoint. Moving arc bonds rotate rigidly, so the interior cannot self-intersect. Incident terminal bonds share their intended hinge vertex and cannot overlap because the nonzero boundary bond angle remains fixed. Hence every existing legal hexagon-rewrite edge admits this continuous **3D torsional realization** in the idealized zero-thickness fixed-angle chain.

**Finite execution:** exact target coordinates and explicit inverse checked at even turn widths 4,6,8,10,12,14.

| Turn bits | Valid conformations | Audited legal hexagon edges |
|---:|---:|---:|
| 4 | 16 | 1 |
| 6 | 58 | 12 |
| 8 | 216 | 76 |
| 10 | 776 | 396 |
| 12 | 2,796 | 1,864 |
| 14 | 9,964 | 8,242 |
| **Total** | | **10,591** |

The max sampled bond-length/adjacent-angle dot-product discrepancy is 7.33e-15; the 3D half-turn lands on the target canonical coordinates and the inverse returns to the origin for every audited edge.

**Prediction seals:** `21b9add8cc19a85aa80db90f252e3d62d67034b2b9dc9c138d8fb0b7da780869` for the chord-axis half-turn (preceded finite audit); `32bd2f151e4ed7e4a61398d8c21be9b71eab05be021bff3e3f8385476459f112` for the collinear dual torsions (sealed after observing the chord relation, explicitly **not** an independent blind prediction).

## Interpretation for §153 figure and Paper II

- **Do not label [0, π]² as the full control torus.** It is a patch of the two-angle periodic space. The counter-rotating schedule \((\theta,-\theta)\) lies outside this displayed patch except at endpoints (it can be rendered with \(\phi_2=2\pi-\theta\) in a full-period chart). The white diagonal in the current panel depicts **co-rotation**, not counter-rotation.
- The 0.93954 clearance bound quoted for serial-failing gates pertains to a **selected counter-rotating schedule** and requires its appropriate angular speed bound. Initial-axis-radius sums alone do not bound the co-rotating speed: a direct numerical derivative on the chosen `01011110101101011101011110` witness reaches approximately 5.19615 bond lengths/radian in the co-rotating schedule, greater than its initial-radius sum of 3.46410. The older 0.75565 conservative certificate remains available for those earlier selected paths.
- The discovered 3D route for the local **hex** transformation does **not** establish global ergodicity. An isolated word with no endpoint-legal hex replacement stays isolated under this exact move vocabulary. The next substantive hole is a geometrically defined *new* locally closing mechanism for those configurations, or an explicit physical route through non-lattice intermediates—not assigning rates to missing edges.

## Ledger status

**STANDS:** The closure obstruction for noncollinear adjacent-axis rotations; the chord/collinear-axis factorization of each `1001 ↔ 0110` hexagon step; ideal zero-thickness continuous nonintersection under the stated geometry.

**RUNS:** 10,591 exhaustive finite legal hexagon edges through m=14 with reversible 3D kinematics; an interior nonlocal counterexample and reverse route.

**OPEN:** Molecular steric thickness, permitted dihedral torsions and chemical angle constraints, energy barriers, rates, fully connected physical folding dynamics, and a lawful local escape for components left disconnected by the hexagon-only graph.

## Reproducibility

- `NEXUS_154_interior_SE3_closure_audit.py` / `_output.txt`
- `NEXUS_154_hexagon_3D_local_return.py` / `_output.txt`
- `NEXUS_154_collinear_dual_torsion.py` / `_output.txt`

No external data, packages beyond NumPy, or hidden notebook state are required.
