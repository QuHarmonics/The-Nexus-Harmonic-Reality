---

## § 126. Odd-prime fold wheels: the half-turn exists for every prime; the phase-rich exception is p = 3 — `nexus_odd_prime_fold_wheel.py`

**Query, reversed from § 125.** § 117 says the register stack's inherited LEN chain is the prime-2 chain. § 125 says the nontrivial norm-halving wheel in \(\mathbb Q(i)\) gives the π/4 amplitude phase and π/2 doubled phase. Ask whether every odd prime fails to admit a nested wheel when the field is generalized to \(\mathbb Q(\sqrt{-d})\), with \(N(w)=|w|^2=1/p\) and \(w^k\in\mathbb Q\).

Prediction sealed before run: `NEXUS_odd_prime_fold_wheel_prediction_2026-10-17.txt`, SHA-256 `c5a2af3800437bd528014a87f8a1f0f99a6881abb06b53149ab71fff988cf212`.

### 126.1 Literal nesting does not exclude odd primes

For every prime \(p\), set

\[
w_p=\frac{\sqrt{-p}}{p}=\frac{i}{\sqrt p}\in\mathbb Q(\sqrt{-p}).
\]

Then, exactly,

\[
N(w_p)=w_p\bar w_p=\frac1p,\qquad w_p^2=-\frac1p\in\mathbb Q.
\]

Therefore the literal condition \(N(w)=1/p\) and \(w^k\in\mathbb Q\) has a solution for every prime. It is the pure-imaginary half-turn (phase \(\pi/2\)), not the phase-rich wheel of § 125. Exact rational arithmetic verifies the formula for 24 odd primes, 3 through 97.

### 126.2 The phase-rich wheel has an odd-prime exception

The matched nontrivial phase is \(\pi/(2p)\):

- \(p=2\): \(s=(1+i)/2\), \(N(s)=1/2\), \(\arg(s)=\pi/4\), \(s^4=-1/4\), \(s^8=1/16\).
- \(p=3\): \(t=(3+\sqrt{-3})/6\), \(N(t)=1/3\), \(\arg(t)=\pi/6\), \(t^2=(1+\sqrt{-3})/6\), \(t^3=\sqrt{-3}/9\), \(t^6=-1/27\), \(t^{12}=1/729\).

These are exact quadratic-field identities. The second is the odd-prime counterexample to “every odd base fails”: the Eisenstein field \(\mathbb Q(\sqrt{-3})\) carries a sixth-root phase and the required scale simultaneously.

### 126.3 Why no further nontrivial phase wheel occurs

If \(w^k\in\mathbb Q\), then

\[
\left(\frac{w}{\bar w}\right)^k=1,
\]

so \(w/\bar w\) is a root of unity in its imaginary quadratic field. Such a field has roots of unity only \(\{\pm1\}\), except \(\mathbb Q(i)\), which has \(\mu_4\), and \(\mathbb Q(\sqrt{-3})\), which has \(\mu_6\).

A wheel at phase \(\pi/(2p)\) has \(w/\bar w=e^{i\pi/p}\), a primitive \(2p\)-th root of unity. For an odd prime, its degree over \(\mathbb Q\) is \(\varphi(2p)=p-1\). A quadratic field can contain it only if \(p-1\le2\), hence \(p=3\). The case \(p=2\) is the Gaussian wheel already in § 125. For odd \(p>3\), the phase-rich \(\pi/(2p)\) wheel is impossible under these conditions, although the trivial pure-imaginary half-turn \(w_p\) remains available.

### 126.4 Exact run

`nexus_odd_prime_fold_wheel.py` uses `fractions.Fraction` and exact multiplication in \(a+b\sqrt{-d}\); no floating-point arithmetic is involved. **83 exact assertions pass**, covering the p=2 and p=3 special wheels and the generic half-turn for 24 odd primes. Machine-readable results and the console transcript are bundled with the report.

| claim | status |
|---|---|
| \(N(w)=1/p\) and some \(w^k\in\mathbb Q\) exists for every prime | **RUNS**; explicit construction, all primes by formula, 24 odd-prime instances executed |
| the \(p=3\) phase wheel in \(\mathbb Q(\sqrt{-3})\) | **RUNS**, exact |
| no phase-\(\pi/(2p)\) wheel for odd \(p>3\) in any imaginary quadratic field | **STANDS** by the root-of-unity degree argument |
| § 117's prime-2 register-stack boundary and § 125's phase-wheel boundary are one theorem | **OPEN**; the \(p=3\) exception must be explained by any proposed unification |
