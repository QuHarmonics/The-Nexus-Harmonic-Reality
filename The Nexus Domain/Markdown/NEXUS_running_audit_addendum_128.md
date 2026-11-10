---

## § 128. Phase-wheel continuation: the quadratic route reaches its boundary, the transformation lifts — `nexus_phase_wheel_field_lift.py`

**Dean's correction applied:** there are no dead-end transformations. A field-limited result marks the boundary of that route; the same structure may continue in a different direction. The §126 proof must not be read as global nonexistence.

### 128.1 The lifted multiplier

For every prime p, take

\[
\zeta_{4p}=e^{i\pi/(2p)},\qquad w_p=\frac{\zeta_{4p}}{\sqrt p}
\]

inside \(K_p=\mathbb Q(\zeta_{4p},\sqrt p)\). The same one-step multiplier now runs in a field whose degree can grow with the required phase. Exactly:

\[
|w_p|^2=\frac1p,\quad \arg w_p=\frac{\pi}{2p},\quad
\frac{w_p}{\bar w_p}=\zeta_{2p},\quad
w_p^{2p}=-\frac1{p^p},\quad w_p^{4p}=\frac1{p^{2p}}.
\]

The scale, phase, and rational nesting coexist for every prime in this extended field route.

### 128.2 The degree is the route selector

Since \(\bar w_p=1/(p w_p)\), \(\zeta_{2p}=p w_p^2\in\mathbb Q(w_p)\). Therefore

\[
[\mathbb Q(w_p):\mathbb Q]\ge\varphi(2p).
\]

For odd primes, \(\varphi(2p)=p-1\); for p=2, \(\varphi(4)=2\). The p=2 and p=3 wheels can lie in quadratic fields; p>3 cannot carry this phase ratio within a quadratic field and must lift to a higher-degree route. The explicit field \(K_p\) gives that route.

The exact symbolic test represents root-of-unity exponents modulo \(4p\) and scale factors as rational exponents; it avoids floating-point phase guesses. It checked primes 2 through 97, 25 primes, with 175 assertions passing. The universal claim rests on the identities and cyclotomic degree formula, not on the finite sweep alone.

**Harness correction:** the first run incorrectly used \(\varphi(2p)=p-1\) for p=2. This was corrected to the exact exception \(\varphi(4)=2\), and the prediction seal wording updated before the successful run.

### 128.3 Ledger correction

The statement in §126.3 is retained only with its scope explicit: **the nontrivial phase wheel does not fit inside an imaginary quadratic field for odd p>3**. It does not mean that the transformation is absent. Its phase requires a field with degree at least \(p-1\), and the higher-field construction supplies one.

| Claim | Status |
|---|---|
| A phase/norm wheel exists in \(K_p\) for every prime p | RUNS: explicit construction; exact symbolic sweep p≤97 |
| Rational closure \(w_p^{2p}=-1/p^p\), \(w_p^{4p}=1/p^{2p}\) | STANDS: direct identity |
| Minimum field degree at least \(\varphi(2p)\) | STANDS: phase ratio \(\zeta_{2p}\) is inside \(\mathbb Q(w_p)\) |
| Quadratic-field boundary at p=2,3 | STANDS, scoped to that route |
| Single theorem connecting the §117 prime-2 register stack to these field-lift routes | OPEN; continuation across routes still to be derived |

No DEAD END is assigned. The boundary of one route is used as the selector for the next transformation direction.
