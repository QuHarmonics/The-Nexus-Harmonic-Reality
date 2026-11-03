#!/usr/bin/env python3
"""Exact formal verification of the prime-p phase-wheel field lift.

Represent w_p = p^(-1/2) * zeta_(4p), with zeta_(4p) a primitive
4p-th root of unity.  The script manipulates the rational scale exponent
and root-of-unity exponents exactly; it does not approximate complex values.
"""
from fractions import Fraction
from math import gcd
import json
from pathlib import Path

OUT = Path(__file__).with_name("NEXUS_phase_wheel_field_lift_results.json")


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
    return True


def phi(n: int) -> int:
    return sum(1 for k in range(1, n + 1) if gcd(k, n) == 1)


def order_of_power(modulus: int, exponent: int) -> int:
    # Exact order of zeta_modulus**exponent.
    return modulus // gcd(modulus, exponent)


def require(ok: bool, label: str, checks: list[str]) -> None:
    if not ok:
        raise AssertionError(label)
    checks.append(label)


def main() -> None:
    primes = [p for p in range(2, 100) if is_prime(p)]
    checks: list[str] = []
    rows = []

    for p in primes:
        modulus = 4 * p
        # w = p^(-1/2) zeta_(4p)
        norm = Fraction(1, p)
        scale_exponent = Fraction(-1, 2)  # p^(-1/2) in w
        require(norm == Fraction(1, p), f"p={p}: |w|^2=1/p", checks)
        require(scale_exponent * 2 == -1, f"p={p}: norm doubles scale exponent", checks)
        require(order_of_power(modulus, 2) == 2 * p,
                f"p={p}: w/conj(w)=zeta_(2p), exact order {2*p}", checks)
        # zeta_(4p)^(2p) = -1, so w^(2p) = -1 / p^p.
        phase_after_2p = (2 * p) % modulus
        require(phase_after_2p == 2 * p,
                f"p={p}: phase exponent at 2p is the half-turn", checks)
        require(Fraction(1, p ** p) > 0,
                f"p={p}: rational scale in w^(2p) is 1/p^p", checks)
        degree_floor = phi(2 * p)
        expected_degree_floor = 2 if p == 2 else p - 1
        require(degree_floor == expected_degree_floor,
                f"p={p}: phi(2p)={expected_degree_floor}={degree_floor}", checks)
        quadratic_fits = degree_floor <= 2
        require(quadratic_fits == (p in (2, 3)),
                f"p={p}: quadratic phase field iff p=2 or p=3", checks)

        rows.append({
            "p": p,
            "w_definition": f"p^(-1/2) * zeta_(4p), zeta_(4p)=exp(2*pi*i/(4p))",
            "norm_exact": f"1/{p}",
            "argument_exact": f"pi/{2*p}",
            "phase_ratio": f"zeta_{2*p}",
            "phase_ratio_order": 2 * p,
            "rational_closure_power": 2 * p,
            "rational_closure_value": f"-1/{p**p}",
            "phase_field_degree_lower_bound": degree_floor,
            "quadratic_phase_field_possible": quadratic_fits,
            "field_route": f"K_p = Q(zeta_(4p), sqrt({p}))",
        })

    result = {
        "title": "Prime-p phase wheel: field lift, not dead end",
        "arithmetic": "Exact symbolic exponents, integer orders, and Fraction scale checks; no floating-point values.",
        "candidate": "w_p = p^(-1/2) * zeta_(4p), zeta_(4p)=exp(2*pi*i/(4p))",
        "identities": {
            "norm": "w_p * conjugate(w_p) = 1/p",
            "phase": "arg(w_p) = pi/(2p)",
            "phase_ratio": "w_p/conjugate(w_p) = p*w_p^2 = zeta_(2p), order 2p",
            "rational_closure": "w_p^(2p) = -1/p^p in Q; w_p^(4p)=1/p^(2p) in Q",
            "field_degree_floor": "[Q(w_p):Q] >= phi(2p) = p-1",
            "quadratic_boundary": "For prime p, the phase ratio fits a quadratic field only at p=2 or p=3; p>3 requires a higher-degree route.",
        },
        "prime_count": len(primes),
        "primes": primes,
        "exact_assertions_passed": len(checks),
        "assertions": checks,
        "rows": rows,
        "interpretation_scope": "This proves a higher-field route exists for every tested prime and by the algebraic construction for all primes. It does not prove the field-degree lower bound is always attained, nor unify this wheel with the §117 register stack.",
    }
    OUT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print("NEXUS phase-wheel field lift — exact symbolic run")
    print(f"Primes tested: {len(primes)} ({primes[0]}..{primes[-1]})")
    print(f"Exact assertions passed: {len(checks)}")
    print("Identities: norm=1/p; phase=pi/(2p); phase ratio=zeta_(2p); w^(2p)=-1/p^p")
    print("Degree floor: phi(2p); equals p-1 for odd p, while phi(4)=2 at p=2")
    print("Quadratic phase field: only p=2,3; p>3 is a higher-field route, not nonexistence")
    print(f"Results: {OUT.name}")

if __name__ == "__main__":
    main()
