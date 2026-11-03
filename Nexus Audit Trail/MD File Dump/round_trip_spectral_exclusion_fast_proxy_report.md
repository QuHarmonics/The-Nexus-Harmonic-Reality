# NEXUS-RH Round-Trip Spectral Exclusion — Fast Proxy Run

## Tested object

\[
\mathcal R_s=J_R(1-s)K_sJ_R(s)K_{1-s}.
\]

The corrected target is:

\[
1
otin \operatorname{Spec}(\mathcal R_s),
\]

equivalently:

\[
-1
otin \operatorname{Spec}(\mathcal A_s).
\]

## Fast finite model

- \(L=12\)
- \(N=28\) Buchstab bins
- \(t=14.135\)
- \(\sigma=0.50,\ldots,0.80\)
- \(K_s\): killed-Buchstab finite proxy with phase
- \(J_R(1-s)\): enforced inverse of \(J_R(s)\)

## Result

Minimum distance from forbidden round-trip eigenvalue:

\[
\min |\lambda(\mathcal R_s)-1|
=
0.59797.
\]

Minimum distance from forbidden two-fiber eigenvalue:

\[
\min |\lambda(\mathcal A_s)+1|
=
0.359726.
\]

Maximum round-trip spectral radius:

\[
\max ho(\mathcal R_s)
=
0.446315.
\]

## Interpretation

This finite proxy found no \(1\)-eigenvalue in the round-trip spectrum and no \(-1\)-mode in the two-fiber block spectrum.

This supports the corrected search target: spectral exclusion, not one-step norm contraction.

## Caution

This does not prove RH. It is not yet the full signed Hall operator with Euler-module restoration. The next run must replace the proxy \(K_s\) with the actual Hall/Euler-restored operator.
