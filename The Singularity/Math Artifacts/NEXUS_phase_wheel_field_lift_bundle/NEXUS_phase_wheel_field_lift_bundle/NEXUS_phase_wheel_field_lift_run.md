# §128 — The phase wheel continues in a larger field; quadratic closure is a route boundary

**Date:** 17 October 2026  
**Executable:** `nexus_phase_wheel_field_lift.py`  
**Prediction seal:** `NEXUS_phase_lift_prediction_2026-10-17.txt` (SHA-256 recorded in companion `.sha256`)  
**Input:** §126 odd-prime wheel result; user's correction that route-bounded nonexistence is not global absence.

## Query

When the phase-π/(2p), norm-1/p wheel cannot be represented in an imaginary quadratic field, does the transformation cease to exist, or must it be read through a different field route?

## Construction

For every prime p, let

\[
\zeta_{4p}=e^{2\pi i/(4p)}=e^{i\pi/(2p)},\qquad
w_p=\frac{\zeta_{4p}}{\sqrt p}.
\]

This is one multiplier. It lives in the larger field

\[
K_p=\mathbb Q(\zeta_{4p},\sqrt p),
\]

rather than requiring that every p use an imaginary quadratic field.

## Exact identities

All four identities follow symbolically from the definition:

\[
\begin{aligned}
w_p\overline{w_p}&=1/p,\\
\arg(w_p)&=\pi/(2p),\\
\frac{w_p}{\overline{w_p}}&=\zeta_{2p},\\
w_p^{2p}&=-1/p^p\in\mathbb Q,\\
w_p^{4p}&=1/p^{2p}\in\mathbb Q.
\end{aligned}
\]

So every prime has a phase wheel with the prescribed scale and a rational power, if the field is allowed to grow with p.

## Why the quadratic route has a boundary

Since \(w_p\overline{w_p}=1/p\), the conjugate is \(\overline{w_p}=1/(p w_p)\), hence

\[
\zeta_{2p}=\frac{w_p}{\overline{w_p}}=p w_p^2\in\mathbb Q(w_p).
\]

Consequently,

\[
[\mathbb Q(w_p):\mathbb Q]\ge [\mathbb Q(\zeta_{2p}):\mathbb Q]
=\varphi(2p).
\]

For odd prime p, \(\varphi(2p)=p-1\); for p=2, \(\varphi(4)=2\). Thus a quadratic field can carry this phase ratio only for p=2 or p=3. For p>3 the same phase-and-scale transformation requires a higher-degree field route. The result is a field-type boundary, not a claim that the wheel does not exist.

The quadratic cases line up with the recorded wheels:

- p=2: \(w_2=(1+i)/2\), phase \(\pi/4\), norm \(1/2\).
- p=3: \(w_3=(3+\sqrt{-3})/6\), phase \(\pi/6\), norm \(1/3\).

## Run details

The executable uses exact rational scale arithmetic and exact root-of-unity exponents modulo \(4p\), not floating-point complex approximations. It checked every prime from 2 through 97 (25 primes): 175 assertions passed. The claims for all primes follow from the displayed algebraic identities and the standard cyclotomic degree formula, rather than from the finite sweep alone.

Harness correction: the first run's assertion accidentally generalized \(\varphi(2p)=p-1\) to p=2. The corrected statement is \(\varphi(2p)=p-1\) for odd prime p, while \(\varphi(4)=2\). The assertion and prediction seal wording were corrected before the successful run. This is a test-harness correction, not a counterexample to the mathematical prediction.

## Audit correction and status

Section §126 remains correct only when read with its field restriction explicit: **no phase-\(\pi/(2p)\) wheel for odd p>3 inside an imaginary quadratic field**. It must not be read as universal nonexistence. The next transformation is the field lift above.

| Claim | Status |
|---|---|
| The scale-1/p phase wheel exists in \(K_p=\mathbb Q(\zeta_{4p},\sqrt p)\) for every prime p | RUNS as an explicit algebraic construction; 25-prime exact symbolic sweep |
| \(w_p^{2p}=-1/p^p\) and \(w_p^{4p}=1/p^{2p}\) | STANDS by direct identity |
| Required phase field degree is at least \(\varphi(2p)\) | STANDS by \(\zeta_{2p}\in\mathbb Q(w_p)\) |
| Quadratic-field wheel only for p=2,3 under this phase constraint | STANDS; retained as a route boundary |
| The register stack's prime-2 route (§117) and the lifted phase wheel are one theorem | OPEN; not a dead end, but a cross-route linkage still to derive |

No DEAD END is assigned here. The quadratic-field result is the endpoint/readout of that route and the entry condition for a higher-degree route.

## Artifacts

- `nexus_phase_wheel_field_lift.py`
- `NEXUS_phase_wheel_field_lift_results.json`
- `NEXUS_phase_wheel_field_lift_console.log`
- `NEXUS_phase_lift_prediction_2026-10-17.txt` and `.sha256`
- `NEXUS_running_audit_addendum_128.md`
- `running-audit (13).md`
