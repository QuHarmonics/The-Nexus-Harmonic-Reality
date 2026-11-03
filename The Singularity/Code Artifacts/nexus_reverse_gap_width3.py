#!/usr/bin/env python3
"""Reverse the width-three gap through the NEXUS transformation compiler.

This does not generate or scan candidate maps. It verifies one compiler-derived
composition against its sealed WHAT and proves the lower-width boundary by
counting the affine group and permutation group exactly.
"""
from __future__ import annotations
from hashlib import sha256
from itertools import combinations
from math import factorial
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parent
PREDICTION = ROOT / "NEXUS_reverse_gap_width3_prediction_2026-10-17.txt"
SEAL_FILE = ROOT / "NEXUS_reverse_gap_width3_prediction_2026-10-17.sha256"
actual_seal = sha256(PREDICTION.read_bytes()).hexdigest()
expected_seal = SEAL_FILE.read_text().split()[0]
assert actual_seal == expected_seal, (actual_seal, expected_seal)

# A = F_2^n. |AGL(n,2)| = 2^n |GL(n,2)|.
def gl_order(n: int) -> int:
    out = 1
    for i in range(n):
        out *= (2**n - 2**i)
    return out

def agl_order(n: int) -> int:
    return (2**n) * gl_order(n)

lower_width = []
for n in (1, 2):
    perm_count = factorial(2**n)
    affine_bijection_count = agl_order(n)
    assert affine_bijection_count == perm_count
    lower_width.append({
        "width": n,
        "bijections": perm_count,
        "invertible_affine_maps": affine_bijection_count,
        "all_bijections_affine": True,
    })

# Bit order in tuples is (a,b,c), with a as bit 0 and c as bit 2.
def unpack(x: int) -> tuple[int, int, int]:
    return (x & 1, (x >> 1) & 1, (x >> 2) & 1)

def pack(a: int, b: int, c: int) -> int:
    return (a & 1) | ((b & 1) << 1) | ((c & 1) << 2)

def T(x: int) -> int:
    """Toffoli: (a,b,c) -> (a,b,c xor (a&b)); T^2 = identity."""
    a, b, c = unpack(x)
    return pack(a, b, c ^ (a & b))

def X(x: int) -> int:
    """Affine free involution: (a,b,c) -> (a xor c,b xor 1,c)."""
    a, b, c = unpack(x)
    return pack(a ^ c, b ^ 1, c)

def F(x: int) -> int:
    """Conjugated exchange F = T o X o T; its way home is the same route."""
    return T(X(T(x)))

def xor_all(values) -> int:
    out = 0
    for v in values:
        out ^= v
    return out

def anf_coefficients(bit_values: list[int], n: int) -> list[int]:
    """Mobius/ANF coefficients c_S = XOR_{U subset S} f(U)."""
    coeff = []
    for S in range(1 << n):
        vals = []
        U = S
        while True:
            vals.append(bit_values[U])
            if U == 0:
                break
            U = (U - 1) & S
        coeff.append(xor_all(vals))
    return coeff

def monomial_name(S: int, n: int) -> str:
    names = [chr(ord('a') + i) for i in range(n)]
    if S == 0:
        return "1"
    return "".join(names[i] for i in range(n) if (S >> i) & 1)

# Verify the input exchange itself and the conjugated output path.
inputs = list(range(8))
T_involution = all(T(T(x)) == x for x in inputs)
X_involution = all(X(X(x)) == x for x in inputs)
X_fixed_point_free = all(X(x) != x for x in inputs)
F_image = [F(x) for x in inputs]
F_bijective = len(set(F_image)) == 8
F_involution = all(F(F(x)) == x for x in inputs)
F_fixed_point_free = all(F(x) != x for x in inputs)
assert T_involution and X_involution and X_fixed_point_free
assert F_bijective and F_involution and F_fixed_point_free

coord_data = []
for bit_index, coordinate in enumerate(("a'", "b'", "c'")):
    vals = [(F(x) >> bit_index) & 1 for x in inputs]
    coeff = anf_coefficients(vals, 3)
    terms = [monomial_name(S, 3) for S, c in enumerate(coeff) if c]
    degree = max((S.bit_count() for S, c in enumerate(coeff) if c), default=-1)
    assert coeff[7] == 0, "A full cubic abc term is not permitted in the output of this route"
    coord_data.append({
        "coordinate": coordinate,
        "truth_table_in_canonical_input_order": vals,
        "anf_terms": terms,
        "degree": degree,
        "full_width_abc_coefficient": coeff[7],
    })

quadratic_terms = [
    {"coordinate": d["coordinate"], "term": term}
    for d in coord_data for term in d["anf_terms"]
    if len(term) == 2
]
assert quadratic_terms

# Record a canonical explicit route table only as the return/readout for this WHAT.
route_rows = []
for x in inputs:
    y = F(x)
    back = F(y)
    assert back == x
    a, b, c = unpack(x)
    ap, bp, cp = unpack(y)
    route_rows.append({
        "input_abc": [a, b, c],
        "output_a_prime_b_prime_c_prime": [ap, bp, cp],
        "return_after_same_route": list(unpack(back)),
        "changed_state": y != x,
    })

results = {
    "status": "RUNS",
    "prediction_sha256": actual_seal,
    "gap": "minimum binary register width for a reversible, fixed-point-free nonlinear exchange",
    "formalization": {
        "binary_domain": "GF(2)^n",
        "no_escape": "bijection / return route exists",
        "cannot_hold_still": "fixed-point-free state map",
        "nonlinear_interaction": "at least one ANF monomial of degree >= 2",
    },
    "lower_width_proof": lower_width,
    "width_three": {
        "construction": "F = T o X o T",
        "T": "(a,b,c) -> (a,b,c xor ab)",
        "X": "(a,b,c) -> (a xor c,b xor 1,c)",
        "T_involution": T_involution,
        "X_involution": X_involution,
        "X_fixed_point_free": X_fixed_point_free,
        "F_bijective": F_bijective,
        "F_involution": F_involution,
        "F_fixed_point_free": F_fixed_point_free,
        "output_anf": coord_data,
        "quadratic_interaction_terms": quadratic_terms,
        "full_cubic_coefficient_zero_in_all_coordinates": all(d["full_width_abc_coefficient"] == 0 for d in coord_data),
        "way_home": "F^{-1}=F; F(F(x))=x",
        "readback_rows": route_rows,
    },
    "conclusion": "Width 3 is the first width permitting a nonlinear exchange that is both reversible and fixed-point-free under the declared binary-register typing.",
    "degree_correction": "At width 3, the highest nonlinear degree of the constructed permutation is 2=n-1; the cubic abc coefficient is zero. Do not call this a nonzero degree-3 coefficient.",
    "scope": "One compiler-composed route plus exact lower-width group counts; no candidate maps or new datasets were searched.",
}

(ROOT / "NEXUS_reverse_gap_width3_results.json").write_text(json.dumps(results, indent=2) + "\n")
report = [
    "# NEXUS reverse-the-gap — width-three exchange run",
    "",
    f"**Prediction SHA-256:** `{actual_seal}`",
    "**Status:** RUNS",
    "",
    "## Binding chain",
    "- WHAT: the minimum binary register width for a reversible, fixed-point-free nonlinear exchange.",
    "- WHERE/type: bijections on GF(2)^n; fixed-point-free means F(x) != x for every address; nonlinear means a nonzero ANF term of degree at least 2.",
    "- Width 1: |AGL(1,2)| = 2 = 2!, so every bijection is affine.",
    "- Width 2: |AGL(2,2)| = 24 = 4!, so every bijection is affine.",
    "- Width 3: the composed route below supplies the missing map; no candidate scan is required.",
    "",
    "## Bound provider",
    "T(a,b,c) = (a,b,c xor ab), with T^2 = I.",
    "X(a,b,c) = (a xor c,b xor 1,c), with X^2 = I and no fixed states.",
    "F = T o X o T. Since T is bijective, F is conjugate to X; therefore F^2 = I and F has no fixed states. Since T contributes the quadratic interaction and X shears c into a, the compiled map keeps nonlinear ANF terms.",
    "",
    "## Compiled output ANF",
]
for d in coord_data:
    report.append(f"- {d['coordinate']} = `{' xor '.join(d['anf_terms'])}`; degree {d['degree']}.")
report += [
    "",
    "## Way home",
    "Applying the same F route twice returns all 8 input addresses exactly. The exact output/input return table is in the JSON artifact. No fixed point occurs.",
    "",
    "## Degree correction",
    "The surviving nonlinear terms are quadratic, degree 2 = n−1. The full cubic coefficient `abc` is zero in all three output coordinates. Thus the width-three collision stands for the first nonlinear reversible exchange, not for a nonzero degree-n coefficient in a permutation.",
    "",
    "## Ledger",
    "- **STANDS:** the group counts prove widths 1 and 2 cannot contain nonlinear bijections.",
    "- **RUNS:** the width-three composed route is reversible, fixed-point-free, and nonlinear; the way-home check is exact.",
    "- **OPEN:** interpreting this binary compiler law as a physical law requires a separate typed map to physical observables; this run closes the Boolean/compiler gap only.",
    "",
    "Scope: one explicit compiler-derived transformation and exact group-order proof; no candidate maps or new datasets were searched.",
]
(ROOT / "NEXUS_reverse_gap_width3_run_2026-10-17.md").write_text("\n".join(report) + "\n")
print("\n".join(report))
