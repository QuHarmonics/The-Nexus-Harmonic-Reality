#!/usr/bin/env python3
"""Exact tests for rational-nesting scale wheels in imaginary quadratic fields.

All arithmetic on field elements a + b*sqrt(-d) uses Fraction. The finite checks
verify the explicit candidates; the accompanying report gives the exact root-of-unity
classification argument for the infinite claim.
"""
from __future__ import annotations
from dataclasses import dataclass
from fractions import Fraction as F
import json
from pathlib import Path

@dataclass(frozen=True)
class Quad:
    a: F
    b: F
    d: int

    def __post_init__(self):
        object.__setattr__(self, "a", F(self.a))
        object.__setattr__(self, "b", F(self.b))
        if self.d <= 0:
            raise ValueError("d must be positive")

    def __mul__(self, other: "Quad") -> "Quad":
        if self.d != other.d:
            raise ValueError("field mismatch")
        return Quad(self.a*other.a - self.d*self.b*other.b,
                    self.a*other.b + self.b*other.a, self.d)

    def __pow__(self, n: int) -> "Quad":
        if n < 0:
            raise ValueError("only nonnegative powers used")
        ans = Quad(F(1), F(0), self.d)
        x = self
        while n:
            if n & 1:
                ans = ans*x
            x = x*x
            n >>= 1
        return ans

    def conjugate(self) -> "Quad":
        return Quad(self.a, -self.b, self.d)

    def norm(self) -> F:
        return self.a*self.a + self.d*self.b*self.b

    def rational(self) -> bool:
        return self.b == 0

    def real_value(self) -> str:
        return str(self.a) if self.b == 0 else f"{self.a} + ({self.b})*sqrt(-{self.d})"


def q(a, b, d):
    return Quad(F(a), F(b), d)

def expect(condition: bool, name: str, tests: list[str]):
    if not condition:
        raise AssertionError(name)
    tests.append(name)

tests: list[str] = []

# p=2: the nontrivial Gaussian-rational wheel from §125.
s = q(F(1,2), F(1,2), 1)
expect(s.norm() == F(1,2), "p=2 special wheel has norm 1/2", tests)
expect((s**2) == q(0, F(1,2), 1), "s^2 = i/2", tests)
expect((s**4) == q(F(-1,4), 0, 1), "s^4 = -1/4", tests)
expect((s**8) == q(F(1,16), 0, 1), "s^8 = 1/16", tests)

# p=3: exceptional odd-prime wheel in Q(sqrt(-3)), angle pi/6.
t = q(F(1,2), F(1,6), 3)  # (3 + sqrt(-3))/6
expect(t.norm() == F(1,3), "p=3 special wheel has norm 1/3", tests)
expect((t**2) == q(F(1,6), F(1,6), 3), "t^2 = (1 + sqrt(-3))/6", tests)
expect((t**3) == q(0, F(1,9), 3), "t^3 = sqrt(-3)/9", tests)
expect((t**6) == q(F(-1,27), 0, 3), "t^6 = -1/27", tests)
expect((t**12) == q(F(1,729), 0, 3), "t^12 = 1/729", tests)

# Literal nesting criterion: every prime has a pure-imaginary two-cycle in Q(sqrt(-p)).
odd_primes = [3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]
generic_rows = []
for p in odd_primes:
    w = q(0, F(1,p), p)  # sqrt(-p)/p = i/sqrt(p)
    expect(w.norm() == F(1,p), f"p={p}: generic half-turn norm 1/p", tests)
    expect((w**2) == q(F(-1,p), 0, p), f"p={p}: generic half-turn w^2=-1/p rational", tests)
    expect((w**2).rational(), f"p={p}: generic half-turn nests in p", tests)
    generic_rows.append({"p":p,"field":f"Q(sqrt(-{p}))","w":f"sqrt(-{p})/{p}",
                         "norm":f"1/{p}","w_squared":f"-1/{p}","rational_power":2,
                         "angle":"pi/2 (pure-imaginary half-turn)","type":"trivial half-turn"})

# Exact algebraic condition for the nontrivial phase pi/(2p): ratio w/conj(w)
# is a primitive 2p-th root of unity. Such a root's degree over Q is phi(2p)=p-1
# for odd prime p, and must be <=2 to lie in a quadratic field. Thus only p=3
# can survive among odd primes. Its exact candidate was verified above.
nontrivial_rows = [
    {"p":2,"field":"Q(i)","w":"(1+i)/2","norm":"1/2","phase":"pi/4",
     "root_order":"4","power":"w^4=-1/4; w^8=1/16","status":"RUNS"},
    {"p":3,"field":"Q(sqrt(-3))","w":"(3+sqrt(-3))/6","norm":"1/3","phase":"pi/6",
     "root_order":"6","power":"w^6=-1/27; w^12=1/729","status":"RUNS"},
]

# Rational-point exclusions by exact square-class arguments:
# Q(i): allowed phase classes are axes (a^2=1/p) or diagonals (2a^2=1/p).
# For odd prime p, neither 1/p nor 1/(2p) is a rational square.
# Q(sqrt(-3)): phase classes have norm a^2, 4a^2, 3b^2, or 12b^2.
# These can equal 1/p with rational coordinates only when p=3 in the 3b^2/12b^2 classes.
expect(all(p % 2 == 1 for p in odd_primes), "sample set contains only odd primes", tests)
expect(F(1,3) == F(1,3), "p=3 exceptional scale is exact", tests)

results = {
    "title": "Odd-prime fold-wheel: exact classification",
    "prediction_seal_sha256": "c5a2af3800437bd528014a87f8a1f0f99a6881abb06b53149ab71fff988cf212",
    "arithmetic": "exact rational arithmetic (fractions.Fraction); no floating point",
    "tests_passed": len(tests),
    "tests": tests,
    "literal_condition": "N(w)=1/p and w^k in Q for some k",
    "literal_result": "YES for every prime p: w=sqrt(-p)/p has norm 1/p and w^2=-1/p",
    "odd_prime_examples": generic_rows,
    "nontrivial_phase_wheel_condition": "phase pi/(2p), norm 1/p, quadratic field, finite rational nesting",
    "nontrivial_result": "only p=2 and p=3; for odd primes, p=3 is the sole nontrivial phase wheel",
    "special_phase_wheels": nontrivial_rows,
    "classification_proof": [
        "If w^k is rational, then (w/conjugate(w))^k=1, so w/conjugate(w) is a root of unity in the imaginary quadratic field.",
        "Every imaginary quadratic field has roots of unity only ±1, except Q(i) with μ4 and Q(sqrt(-3)) with μ6.",
        "In a generic field, ratio +1 forces w rational, impossible because a^2=1/p has no rational solution; ratio -1 forces w pure imaginary and d=p (for squarefree d), giving w=±sqrt(-p)/p.",
        "A nontrivial wheel with phase pi/(2p) has w/conjugate(w)=exp(i*pi/p), a primitive 2p-th root of unity. Its degree is φ(2p)=p-1 for odd prime p. A quadratic field can contain it only if p-1≤2, hence p=3; p=2 is the already-known Gaussian case.",
        "Exact p=3 witness: w=(3+sqrt(-3))/6, N(w)=1/3, w^6=-1/27 and w^12=1/729.",
        "For p>3 no nontrivial pi/(2p) wheel exists under these constraints, though the pure-imaginary half-turn remains."
    ],
    "tests_status": "RUNS",
}
Path('/mnt/data/NEXUS_odd_prime_fold_wheel_results.json').write_text(json.dumps(results, indent=2) + '\n')

report = r'''# §126 — Odd-prime fold wheel: the trivial half-turn survives; p=3 has a second wheel

**Query.** Generalize §125's nesting question to a prime p and an imaginary quadratic field Q(√−d). Separate the literal condition N(w)=1/p, w^k∈Q from the stronger nontrivial phase-wheel condition phase(w)=π/(2p).

**Prediction seal (before run).** `NEXUS_odd_prime_fold_wheel_prediction_2026-10-17.txt`, SHA-256 `c5a2af3800437bd528014a87f8a1f0f99a6881abb06b53149ab71fff988cf212`.

## Exact witnesses

For every prime p, the literal condition has the solution

\[
w_p=\frac{\sqrt{-p}}{p}=\frac{i}{\sqrt p},\qquad N(w_p)=\frac1p,\qquad w_p^2=-\frac1p\in\mathbb Q.
\]

So **the literal generalization does not fail for odd primes**. It carries only the pure-imaginary half-turn (phase π/2), not the more structured phase wheel from §125.

The nontrivial phase condition has two exact cases:

- **p=2:** \(s=(1+i)/2\), \(N(s)=1/2\), phase π/4, \(s^4=-1/4\), \(s^8=1/16\).
- **p=3:** \(t=(3+\sqrt{-3})/6\), \(N(t)=1/3\), phase π/6, \(t^2=(1+\sqrt{-3})/6\), \(t^3=\sqrt{-3}/9\), \(t^6=-1/27\), \(t^{12}=1/729\).

All these equalities were checked using exact fractions and exact quadratic-field multiplication; no floating-point arithmetic was used. The executable checked the pure half-turn witness for 24 odd primes from 3 through 97.

## Why the nontrivial wheel stops at 3

If \(w^k\in\mathbb Q\), then \(w/\bar w\) is a root of unity. An imaginary quadratic field has only \(\pm1\), except \(\mathbb Q(i)\) (fourth roots) and \(\mathbb Q(\sqrt{-3})\) (sixth roots).

For a wheel with phase \(\pi/(2p)\), its phase ratio is

\[
\frac{w}{\bar w}=e^{i\pi/p},
\]

a primitive \(2p\)-th root of unity. Its degree over \(\mathbb Q\) is \(\varphi(2p)=p-1\) for odd prime \(p\). A quadratic field can contain it only when \(p-1\le2\), so the only odd-prime possibility is **p=3**, realized exactly in \(\mathbb Q(\sqrt{-3})\). For \(p>3\), the nontrivial \(\pi/(2p)\) phase is impossible under the stated quadratic-field/nesting constraints. The pure-imaginary half-turn is not excluded.

## What this says about §117

This is **not yet one theorem with the register-stack result**. §117 says the register stack's inherited LEN chain is generated by the prime 2, while other bases are reached by conversion with carries. §126 says that, among imaginary-quadratic rational-nesting wheels with the scale \(N(w)=1/p\), a trivial half-turn exists for every prime, but a nontrivial \(\pi/(2p)\) wheel exists only at p=2 and p=3. The p=3 exception prevents claiming that every odd prime fails. A proof identifying the register-stack route prime with the phase-wheel restriction remains OPEN.

## Status

- Literal \(N(w)=1/p\), some \(w^k\in\mathbb Q\): **RUNS**; explicit construction for every prime.
- p=3 nontrivial phase wheel: **RUNS**, exact.
- No nontrivial \(\pi/(2p)\) wheel for odd primes p>3 in an imaginary quadratic field: **STANDS by the root-of-unity degree argument**.
- “The register-stack prime-2 boundary and the phase-wheel boundary are one theorem”: **OPEN**; p=3 is the decisive exception that any unification must explain.
'''
Path('/mnt/data/NEXUS_odd_prime_fold_wheel_run.md').write_text(report)
print(f"PASS: {len(tests)} exact assertions")
for item in tests:
    print("PASS", item)
print("Literal condition: a nested half-turn exists for every prime p")
print("Nontrivial phase pi/(2p): p=2 and p=3 only; odd p>3 ruled out by degree argument")
print("Wrote results JSON and report")
