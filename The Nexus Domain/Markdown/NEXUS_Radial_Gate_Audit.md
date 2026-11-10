# §102. One radial field, two gates: the common route-selection law

**Scope.** This entry continues §101 of `running-audit.md`. It uses the orbital-collapse and nuclear-intruder observations recorded there; the original `screened.py` and `collapse.py` scratchpad scripts were not attached to this run, so §101's numerical spectra are not claimed as independently re-executed here. The exact angular-momentum identities below were independently checked by `nexus_radial_gate_audit.py` with rational arithmetic.

## 102.1 The correction that opens the route

The two cases do **not** use one identical physical term. The atom's delayed inward localization in §101 was produced by a changing screened central field opposed by the centrifugal barrier. The nucleus's early intruder is produced by a strong, inverted spin–orbit splitting. Calling these the same force would erase the mechanism that distinguishes their timing.

What is common is the **radial eigenroute**: separate the central-field problem into angular channels, calculate the admissible radial states, and order those states by their resulting spectrum. A channel moves inward or becomes the next occupied state when the relevant radial branch becomes energetically preferred. The two systems use different field profiles and different terms to reach that crossing.

## 102.2 The shared effective radial operator

A common Schrödinger-like comparison form is

\[
H_{X,\ell j}= -\frac{\hbar^2}{2m_X}\frac{d^2}{dr^2}
+\frac{\hbar^2\ell(\ell+1)}{2m_Xr^2}
+V_X(r)
+\lambda_X W_X(r)\langle\mathbf L\!\cdot\!\mathbf S\rangle_{\ell j},
\]

where \(X\) identifies atom or nucleus. The spin–orbit term can be negligible or omitted in a nonrelativistic atomic screening model; in a nuclear mean-field model its coefficient is strong and has the sign that lowers the aligned \(j=\ell+\tfrac12\) branch. This is a comparison family, not a claim that the scalar atomic Thomas–Fermi run already contained a nuclear spin–orbit term.

For spin \(s=\tfrac12\), the exact angular factors are

\[
\langle\mathbf L\!\cdot\!\mathbf S\rangle_{j=\ell+1/2}=\frac{\ell}{2},\qquad
\langle\mathbf L\!\cdot\!\mathbf S\rangle_{j=\ell-1/2}=-\frac{\ell+1}{2}.
\]

Thus the branch-splitting factor is \((2\ell+1)/2\); the centrifugal factor is \(\ell(\ell+1)\). The angular dependence is related, but **not equal**. With the same radial prefactor, their ratio is

\[
\frac{(2\ell+1)/2}{\ell(\ell+1)}=\frac{2\ell+1}{2\ell(\ell+1)},
\]

which decreases approximately as \(1/\ell\). This is only a ratio of angular factors—not a physical energy ratio—because the radial expectation values, masses, gradients, and couplings differ.

## 102.3 The common crossing predicate

The useful common law is not “spin–orbit equals centrifugal.” It is:

> **A route changes rank when its field-dependent radial energy crosses the competing route's energy.**

For the atomic case, the field parameter is the nuclear charge and its self-consistent screening profile. The measured signature is inward localization of the nodeless high-\(\ell\) radial state (the audit's \(\langle r\rangle\) collapse), together with the resulting level order. For the nuclear case, the decisive term is the spin–orbit shift; the aligned high-\(j\) level crosses below the competing shell states when its lowering exceeds the original shell gap.

A diagnostic threshold can be written in each domain as a drive-to-gap ratio:

\[
\Gamma_A(Z)=\frac{\text{screened-well advantage of the inward branch}}
{\text{centrifugal/localization penalty}},\qquad
\Gamma_N=\frac{|\Delta E_{so}(j_+)|}{\Delta E_{shell}}.
\]

The transition is expected when the relevant ratio reaches order one. But the numerators and denominators are domain-specific observables in this definition. **A shared threshold form is not yet a parameter-free universal law.** The open theorem is whether both ratios can be derived from one common radial functional with no independently fitted selector.

## 102.4 The discriminator to run next

1. **Atomic continuation:** for every \(Z\) in a dense sweep, retain the full radial eigenfunction, eigenvalue, \(\langle r\rangle\), and inner probability \(P_{in}(r_c)=\int_0^{r_c}|u(r)|^2dr\). Do not classify collapse from \(\langle r\rangle\) alone. Repeat over the screening-profile parameter to separate a genuine localization transition from grid/parameter artifacts.
2. **Nuclear continuation:** hold the central mean field fixed and scale the spin–orbit term by \(\eta\in[0,1]\). Track \(E_{j+}(\eta)\), \(E_{j-}(\eta)\), their radial localization, and the crossing against the shell gap. The predicted critical scale is \(\eta_c\) satisfying \(|\Delta E_{so}(\eta_c)|=\Delta E_{shell}\).
3. **Fit neither threshold to the desired orbital.** Calculate the dimensionless ratios from the radial integrals, then test whether the atomic localization change and nuclear level crossing occur at the same parameter-free criterion. Include neighboring \(\ell\) channels as controls.
4. **Route every mismatch back.** If atomic transition thresholds shift with screening parameters but the nuclear crossings shift independently with \(\eta\), the common result is the radial eigenvalue-selection rule—not a deeper conversion of centrifugal barrier into spin–orbit coupling. If a shared functional predicts both without extra fitted constants, that is the stronger result.

## 102.5 Current ledger

| Claim | Status |
|---|---|
| Centrifugal angular factor \(\ell(\ell+1)\) and spin–orbit factors \(\ell/2\), \(- (\ell+1)/2\) | **STANDS** (exact angular-momentum algebra) |
| Both cases can be represented as radial channels whose energy/localization determines route ranking | **STANDS** (common spectral framework) |
| Atomic Thomas–Fermi/Latter run gives the reported delayed localization and directions | **RUNS in §101 as reported**; not re-executed here because scripts were not attached |
| Nuclear spin–orbit lowers the aligned high-\(j\) intruder and produces shell reordering | **STANDS** in established nuclear shell-model physics |
| Same nodeless/no-partner address identifies the exceptional member in both tables | **RUNS under the declared mapping** in §§100–101 |
| One parameter-free law converts atomic centrifugal gating into nuclear spin–orbit advancement | **OPEN** |

## Reproducibility

Run `python nexus_radial_gate_audit.py`. It verifies the exact angular identities for \(\ell=0\ldots8\) and writes `nexus_radial_gate_results.json`. It does not model atomic or nuclear radial potentials and makes no claim to reproduce the §101 energy or radius data.
