# §103 candidate — nuclear spin–orbit coefficient: exact factor, sign condition, and identifiability

**Route from §102.** The atomic Thomas–Fermi gate is a non-fitted threshold within its stated nonrelativistic TF model. The nuclear branch is not yet a matching parameter-free gate: the angular algebra determines the multiplier, but it does not determine the interaction coefficient.

## Exact angular factor

Fix the convention

\[
H_{\rm so}=\kappa\,\mathbf L\cdot\mathbf S,\qquad s=\tfrac12.
\]

Using

\[
\langle\mathbf L\cdot\mathbf S\rangle_{\ell j}
=\frac{j(j+1)-\ell(\ell+1)-s(s+1)}2,
\]

we obtain

\[
\begin{aligned}
j=\ell+\tfrac12 &: \quad \langle L\cdot S\rangle=+\ell/2,\\
j=\ell-\tfrac12 &: \quad \langle L\cdot S\rangle=-(\ell+1)/2.
\end{aligned}
\]

Thus

\[
E_{\ell,+}-E_{\ell,-}=\kappa\,\frac{2\ell+1}{2}
=\kappa(\ell+\tfrac12).
\]

For this convention, the aligned branch is lower exactly when \(\kappa<0\). The aligned branch's shift relative to the doublet centroid, however, is \(\kappa\ell/2\), not \(\kappa(\ell+1/2)\); the latter is the **splitting** between branches. This is a type correction to any wording that calls \(\ell+1/2\) the aligned-branch lowering itself.

The aligned branch has degeneracy \(2\ell+2\), so a lowered high-\(j\) intruder contributes that many states at the next closure. The counting part is discrete and exact; whether the branch is low enough is an energy-ordering question.

## What is and is not identifiable

A schematic level model is

\[
E_{n\ell j}=\epsilon_{n\ell}+\kappa_{n\ell}\langle L\cdot S\rangle_{\ell j},
\]

where \(\epsilon_{n\ell}\) is the central-field level and \(\kappa_{n\ell}\) may include a radial matrix element. A closure constrains whether a candidate level sits below competing levels. It does not, by itself, supply the gap \(\Delta_\ell\), a radial matrix element, or an energy unit.

There is a simple scale non-identifiability: multiplying every level energy, every competing gap, and \(\kappa\) by the same positive factor preserves every ordering and shell count. Therefore closure positions alone cannot determine a dimensionful \(\kappa\). They may constrain a dimensionless ratio such as \(|\kappa|/\Delta\) after the model has defined what \(\Delta\) and \(\kappa\) mean.

The sign has a narrower conditional result: if the Hamiltonian convention above is fixed and the observed/modelled ordering places \(j=\ell+1/2\) below its partner, then \(\kappa<0\). That is a correct phenomenological inference from the branch ordering. It is not yet an independent compiler-side derivation of the sign, because the current compiler primitives do not specify a signed map from their orientations/routes to the physical \(\mathbf L\cdot\mathbf S\) interaction.

This distinction matters in modern nuclear theory: single-particle potentials and their shell spectra depend on the resolution/representation used for the nuclear interaction; they are not themselves observables. A 2026 *Physical Review Letters* calculation connects magic-number structure to chiral EFT two- and three-nucleon forces through resolution evolution, and reports the microscopic origin of the effective spin/pseudospin structure as resolution-dependent. That is a concrete physical route beyond fitting one universal \(\kappa\), but it is not yet a mapping from NEXUS's six-verb compiler to the nuclear Hamiltonian. Source: [Ding et al., *Physical Review Letters* 136, 052501 (2026)](https://doi.org/10.1103/8lzc-j1lx); [APS synopsis](https://physics.aps.org/articles/v19/11).

## Atomic 5g scope note

The \(Z\simeq114.7\) result is the onset of the specified **nonrelativistic Thomas–Fermi gate**, not an unconditional lower bound on every relativistic atomic calculation. Relativistic calculations differ: Umemoto and Saito (1996) report g-electron occupation beginning at \(Z=126\), while a 2024 calculation predicts an occupied 5g spinor for hypothetical element 125. Both place it near the TF gate, but the element has not been experimentally established. Sources: [J. Phys. Soc. Japan 65, 3175 (1996)](https://doi.org/10.1143/jpsj.65.3175); [AIP/PubMed report (2024)](https://pubmed.ncbi.nlm.nih.gov/39115167/).

## Ledger status proposal

| Claim | Status |
|---|---|
| \(\langle L\cdot S\rangle=\ell/2,-(\ell+1)/2\), splitting factor \(\ell+1/2\) | RUNS (exact angular algebra) |
| In the convention \(H_{\rm so}=\kappa L\cdot S\), lower aligned branch implies \(\kappa<0\) | STANDS conditionally on the branch ordering |
| Magic-number counts alone identify the magnitude of \(\kappa\) | DEAD END — scale and gap are not identified |
| Compiler primitives presently derive the physical sign of \(\kappa\) | OPEN — signed map to the physical interaction is not specified |
| A universal, model-independent measured \(\kappa\) exists | OPEN / ill-posed until Hamiltonian and radial normalization are fixed |
| Microscopic nuclear-force calculation provides a route to the effective ordering | STANDS as an external physical route; NEXUS mapping remains OPEN |

**Next discriminating run.** Do not fit \(\kappa\) to the magic numbers alone. First declare the nuclear Hamiltonian and normalization; then (a) use a measured same-\(\ell\) spin–orbit doublet to test the sign convention, and (b) track the branch splitting and relevant shell gaps under a microscopic interaction/resolution sweep. The compiler-side test is whether an independently specified route rule predicts the *sign and ordering before reading the observed closures*, not whether a sign can be reverse-inferred from them afterward.
