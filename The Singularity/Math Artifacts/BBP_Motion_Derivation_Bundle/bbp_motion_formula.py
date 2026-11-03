#!/usr/bin/env python3
"""Motion-derived hexadecimal digit generator from the BBP lane recurrence.

This is a compact executable companion to the paper. It does not store or
replay previous pi digits. It seeds the exact-rational accumulator with a
finite BBP partial sum and a rigorous tail interval, then generates each
subsequent digit from persistent reciprocal-lane remainders and the crossing
recurrence F_(n+1) = 16 F_n - C_n.

The finite-seed version is a transparent reference implementation of the
formula. The separate PendingField implementation is the empty-field,
open/widen/certify realization.
"""
from __future__ import annotations
import argparse
import csv
from fractions import Fraction as Q
from pathlib import Path

BASE = 16
WEIGHTS = {1: 4, 4: -2, 5: -1, 6: -1}
HEX = "0123456789ABCDEF"


def floor_q(x: Q) -> int:
    return x.numerator // x.denominator


def bbp_term(k: int) -> Q:
    return Q(1, BASE**k) * (
        Q(4, 8*k+1) - Q(2, 8*k+4) - Q(1, 8*k+5) - Q(1, 8*k+6)
    )


def initial_seed(terms: int) -> tuple[Q, Q]:
    """Return center for F_0 = pi-4 and a rigorous bound on its error."""
    partial = sum((bbp_term(k) for k in range(terms)), Q(0))
    center = partial - 4
    # For k >= terms, the weighted bracket has absolute value <= 8/(8k+1).
    # Summing the geometric envelope gives this bound for the omitted tail.
    error = Q(128, 15 * (8*terms + 1) * BASE**terms)
    return center, error


def generate(count: int, guard: int = 96, trace_path: str | None = None):
    if count < 1:
        raise ValueError("count must be positive")
    if guard < 8:
        raise ValueError("guard must be at least 8 terms")

    terms = count + guard
    F, err = initial_seed(terms)
    # Each lane is (k, j, denominator, coefficient, current remainder).
    lanes: list[list[int]] = []
    rows = []
    out = []

    for n in range(count):
        # OPEN: a fresh layer of four local instructions, no output digits stored.
        for j, c in WEIGHTS.items():
            d = 8*n + j
            lanes.append([n, j, d, c, 1 % d])

        # Digit is read from the current enclosure; do not guess if it straddles
        # a hexadecimal boundary.
        lo, hi = F - err, F + err
        qlo, qhi = floor_q(BASE * lo), floor_q(BASE * hi)
        if qlo != qhi:
            raise ArithmeticError(
                f"digit {n} is not certified with {terms} seed terms; increase guard"
            )
        digit = qlo % BASE
        I_n_lo, I_n_hi = floor_q(lo), floor_q(hi)
        if I_n_lo != I_n_hi:
            raise ArithmeticError(f"integer boundary not certified at n={n}")
        I_n = I_n_lo

        # READ/TICK: each local lane makes one long-division transition.
        C = 0
        q_sums = {j: 0 for j in WEIGHTS}
        for L in lanes:
            k, j, d, c, r = L
            q, r_next = divmod(BASE * r, d)
            C += c * q
            q_sums[j] += q
            L[4] = r_next

        # ACCUMULATE: the entire aggregate update is one integer crossing
        # subtraction, while the certified uncertainty expands by exactly 16.
        F_next = BASE * F - C
        err_next = BASE * err
        nlo, nhi = F_next - err_next, F_next + err_next
        I_next_lo, I_next_hi = floor_q(nlo), floor_q(nhi)
        if I_next_lo != I_next_hi:
            raise ArithmeticError(f"next carry boundary not certified at n={n}")
        I_next = I_next_lo
        carry = I_next - BASE * I_n
        if digit != C + carry:
            raise AssertionError(f"motion formula failed at n={n}")

        out.append(HEX[digit])
        rows.append({
            "n_zero_based": n,
            "opened_lanes": len(lanes),
            "q_sum_j1": q_sums[1],
            "q_sum_j4": q_sums[4],
            "q_sum_j5": q_sums[5],
            "q_sum_j6": q_sums[6],
            "crossing_sum_C_n": C,
            "carry_I_next_minus_16I": carry,
            "digit_hex": HEX[digit],
            "certified": True,
            "seed_terms": terms,
            "error_bound_bits_denominator": err.denominator.bit_length(),
        })
        F, err = F_next, err_next

    if trace_path:
        path = Path(trace_path)
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
            w.writeheader()
            w.writerows(rows)
    return "".join(out), rows


def independent_pi_hex(count: int, decimal_guard: int = 80) -> str:
    """Independent numerical regression reference; not used by the generator."""
    from mpmath import mp, pi
    mp.dps = int(count * 1.21) + decimal_guard
    x = pi - 3
    digits = []
    for _ in range(count):
        x *= 16
        d = int(x)
        digits.append(HEX[d])
        x -= d
    return "".join(digits)


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--digits", type=int, default=96)
    p.add_argument("--guard", type=int, default=96)
    p.add_argument("--trace", default="bbp_motion_formula_trace.csv")
    p.add_argument("--verify", action="store_true")
    a = p.parse_args()
    digits, rows = generate(a.digits, a.guard, a.trace)
    print(f"digits: {len(digits)}")
    print(f"seed BBP terms: {a.digits + a.guard} (finite rational center + rigorous tail bound)")
    print(f"trace rows: {len(rows)} -> {a.trace}")
    print(f"hex: {digits}")
    if a.verify:
        ref = independent_pi_hex(a.digits)
        matches = sum(x == y for x, y in zip(digits, ref))
        print(f"independent mpmath match: {matches}/{a.digits}")
        if matches != a.digits:
            raise SystemExit(1)


if __name__ == "__main__":
    main()
