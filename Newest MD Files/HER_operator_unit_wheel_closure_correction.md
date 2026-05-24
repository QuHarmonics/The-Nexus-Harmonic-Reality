# NEXUS-RH HER Operator Correction — Unit Wheel Closure Test

## Result

The local Euler module

\[
S_{210}=\langle2,3,5,7\rangle
\]

cannot be represented as ordinary multiplication inside only the unit group

\[
G=(\mathbb Z/210\mathbb Z)^\times.
\]

For \(p\in\{2,3,5,7\}\), multiplication sends every unit residue to a nonunit residue:

\[
r\in G
\quad\Rightarrow\quad
pr \notin G.
\]

Therefore the HER operator cannot be implemented as

\[
T_n:(u,r)\mapsto(u-\log n,rn\bmod210)
\]

on \(G\) alone once the local Euler module is added.

## Correction

There are two valid implementations.

### Option A — Expanded Residue Ring

Use the full residue ring

\[
\mathbb Z/210\mathbb Z
\]

instead of only its unit group. Then the local Euler multipliers \(2,3,5,7\) are legal transformations.

### Option B — Separate Local Euler Fibers

Keep the coprime wheel backbone

\[
(m,210)=1
\]

on \(G\), but attach separate dilation fibers

\[
D_2,D_3,D_5,D_7
\]

acting on the Nyman address coordinate:

\[
D_p:\rho\!\left(\frac{1}{mx}\right)
\mapsto
\rho\!\left(\frac{1}{pmx}\right).
\]

Then the corrected algebra is

\[
\boxed{
\operatorname{Alg}
\left(
K_L^{\mathrm{prime}},
D_2,D_3,D_5,D_7
\right)
}
\]

not merely \(K_L^{\mathrm{prime}}\) on \(G\).

## Consequence for the next run

The next HER spectral scan must not use a unit-only residue state space if it includes the Euler module.

The correct next numerical operator is either:

\[
\mathcal R_{s,L}^{\mathrm{HER,ring}}
=
J_R(1-s)K_{s,L}^{\mathrm{ring}}J_R(s)K_{1-s,L}^{\mathrm{ring}},
\]

with full \(210\)-residue state space, or

\[
\mathcal R_{s,L}^{\mathrm{HER,fiber}}
=
J_R(1-s)K_{s,L}^{\mathrm{prime+EulerFibers}}J_R(s)K_{1-s,L}^{\mathrm{prime+EulerFibers}}.
\]

## Collapse

\[
\boxed{
\Psi:
\text{the Euler module correction is real.}
}
\]

\[
\boxed{
\Delta:
\text{adding }D_2,D_3,D_5,D_7\text{ forces residue-space enlargement or fiber separation.}
}
\]

\[
\boxed{
\Omega:
\text{run spectral exclusion on the expanded/fibered HER operator.}
}
\]
