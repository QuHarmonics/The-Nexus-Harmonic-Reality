#!/usr/bin/env python3
"""Exact audit of the Walsh spectrum of comparator-prefix imbalance Delta."""
from __future__ import annotations
from fractions import Fraction
from hashlib import sha256
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PRED = ROOT / "even_delta_spectrum_prediction.txt"
SRC = Path(__file__).resolve()

def reverse_bits(x: int, n: int) -> int:
    y = 0
    for _ in range(n):
        y = (y << 1) | (x & 1)
        x >>= 1
    return y

def comparator(n: int, x: int) -> int:
    r = reverse_bits(x, n)
    return (r > x) - (r < x)

def fwht(values: list[int]) -> list[int]:
    a = values[:]
    length = 1
    while length < len(a):
        step = length * 2
        for base in range(0, len(a), step):
            for off in range(length):
                x = a[base + off]
                y = a[base + off + length]
                a[base + off] = x + y
                a[base + off + length] = x - y
        length = step
    return a

def predicted_delta_hat(s: int, n: int, chat: list[int]) -> Fraction:
    if s == 0:
        raise ValueError("zero mode is handled by its scalar formula")
    j = (s & -s).bit_length() - 1
    weight = s.bit_count()
    if weight & 1:
        return Fraction(-chat[s], 2)
    value = -Fraction(1 << j, 2) * chat[s ^ (1 << j)]
    for k in range(j):
        value += Fraction(1 << k, 2) * chat[s ^ (1 << k)]
    return value

def analytic_comparator_spectrum(n: int) -> list[int]:
    """Unnormalized Walsh coefficients from mirrored-pair expansion."""
    N = 1 << n
    h = n // 2
    out = [0] * N
    for j in range(h):
        coeff = Fraction(N, 1 << (j + 1))
        for subset in range(1 << j):
            paired_mask = 0
            for k in range(j):
                if (subset >> k) & 1:
                    paired_mask |= (1 << k) | (1 << (n - 1 - k))
            out[paired_mask | (1 << (n - 1 - j))] += int(coeff)
            out[paired_mask | (1 << j)] -= int(coeff)
    return out

def direct_kernel(n: int, s: int, t: int) -> Fraction:
    N = 1 << n
    acc = 0
    running = 0
    S = [0] * N
    for x in range(N):
        running += -1 if ((s & x).bit_count() & 1) else 1
        S[x] = running
    for x in range(N):
        acc += S[x] * (-1 if ((t & x).bit_count() & 1) else 1)
    return Fraction(acc, N)

def predicted_kernel(s: int, t: int) -> Fraction:
    j = (s & -s).bit_length() - 1
    if t == s:
        return Fraction(1, 2)
    if t == (s ^ (1 << j)):
        return Fraction(1 << j, 2)
    for k in range(j):
        if t == (s ^ (1 << k)):
            return -Fraction(1 << k, 2)
    return Fraction(0, 1)

def closed_zero_mode(n: int) -> Fraction:
    N = 1 << n
    h = n // 2
    if n % 2 == 0:
        return Fraction(N * (N - 1), 6) - Fraction(h * N, 4)
    return Fraction(N * (N - 2), 6) - Fraction(h * N, 4)

def audit() -> dict:
    source_hash_before = sha256(SRC.read_bytes()).hexdigest()
    prediction_hash = sha256(PRED.read_bytes()).hexdigest()
    width_rows = []
    total_masks = 0
    total_nonzero_matches = 0
    total_comparator_spectrum_matches = 0
    zero_mode_checks = 0
    zero_mode_values = {}
    max_abs_hat_delta = 0

    for n in range(2, 21):
        N = 1 << n
        prefix = 0
        delta_sum = 0
        h = n // 2
        stored_c: list[int] | None = [] if n <= 12 else None
        stored_delta: list[int] | None = [] if n <= 12 else None
        for x in range(N):
            c = comparator(n, x)
            delta_sum += prefix  # Delta(p) at p=x
            if stored_c is not None:
                stored_c.append(c)
                stored_delta.append(prefix)
            prefix += c
        assert prefix == 0, f"comparator does not sum to zero, n={n}"
        pred0 = closed_zero_mode(n)
        assert pred0.denominator == 1
        assert delta_sum == int(pred0), ("zero mode", n, delta_sum, pred0)
        zero_mode_checks += 1
        zero_mode_values[str(n)] = int(pred0)
        max_abs_hat_delta = max(max_abs_hat_delta, abs(delta_sum))

        width_row = {"n": n, "N": N, "zero_mode": int(pred0), "zero_mode_match": True}
        if stored_c is not None and stored_delta is not None:
            chat = fwht(stored_c)
            dhat_direct = fwht(stored_delta)
            analytic_chat = analytic_comparator_spectrum(n)
            assert chat == analytic_chat, f"comparator spectrum mismatch n={n}"
            total_comparator_spectrum_matches += N
            for s in range(1, N):
                pred = predicted_delta_hat(s, n, chat)
                assert pred.denominator == 1, ("noninteger predicted coefficient", n, s, pred)
                assert int(pred) == dhat_direct[s], ("Delta spectrum mismatch", n, s, int(pred), dhat_direct[s])
                total_nonzero_matches += 1
                max_abs_hat_delta = max(max_abs_hat_delta, abs(dhat_direct[s]))
            assert dhat_direct[0] == delta_sum
            width_row["nonzero_walsh_modes_checked"] = N - 1
            width_row["comparator_modes_checked"] = N
        else:
            width_row["nonzero_walsh_modes_checked"] = 0
            width_row["comparator_modes_checked"] = 0
        width_rows.append(width_row)

    # Verify the sparse kernel itself by direct Walsh transforms of prefix sums.
    kernel_pairs = 0
    for n in range(2, 9):
        N = 1 << n
        for s in range(1, N):
            S = []
            running = 0
            for x in range(N):
                running += -1 if ((s & x).bit_count() & 1) else 1
                S.append(running)
            direct = fwht(S)
            for t in range(N):
                want = predicted_kernel(s, t)
                got = Fraction(direct[t], N)
                assert got == want, ("kernel mismatch", n, s, t, got, want)
                kernel_pairs += 1

    source_hash_after = sha256(SRC.read_bytes()).hexdigest()
    assert source_hash_before == source_hash_after, "source changed while audit was running"
    return {
        "status": "PASS",
        "source_sha256_before": source_hash_before,
        "source_sha256_after": source_hash_after,
        "prediction_sha256": prediction_hash,
        "scope": {
            "direct_delta_walsh_widths": "2..12",
            "direct_zero_mode_widths": "2..20",
            "direct_kernel_widths": "2..8",
            "direct_comparator_spectrum_widths": "2..12"
        },
        "counts": {
            "zero_mode_checks": zero_mode_checks,
            "nonzero_delta_walsh_coefficients_checked": total_nonzero_matches,
            "comparator_walsh_coefficients_checked": total_comparator_spectrum_matches,
            "kernel_pairs_checked": kernel_pairs
        },
        "zero_mode_values": zero_mode_values,
        "width_rows": width_rows,
        "max_abs_direct_delta_coefficient": max_abs_hat_delta,
        "notes": [
            "All Walsh transforms are unnormalized exact integer transforms.",
            "Nonzero Delta coefficient formula was checked against direct FWHT of Delta.",
            "Zero-mode formula was checked against direct sum_p Delta(p) through n=20.",
            "Sparse kernel was checked directly for every nonzero s and every t at n=2..8."
        ]
    }

if __name__ == "__main__":
    result = audit()
    out = ROOT / "even_delta_spectrum_results.json"
    out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({
        "status": result["status"],
        "counts": result["counts"],
        "source_sha256": result["source_sha256_after"],
        "prediction_sha256": result["prediction_sha256"],
        "zero_mode_checks": result["counts"]["zero_mode_checks"]
    }, indent=2))
