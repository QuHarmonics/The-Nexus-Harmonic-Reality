#!/usr/bin/env python3
"""
Trace decimal digit deletion from the SHA-256 empty-string digest.

Three traces are produced:
  1. remove one digit from the END each step
  2. remove one digit from the START each step
  3. remove the CENTER digit each step

For even-length strings, the center trace removes the LEFT-of-center digit.
Change CENTER_MODE to "right" to remove the right-of-center digit instead.
"""

import csv
from pathlib import Path

HEX = "1a14bbc855b4cbea992eaf922d5669309678aede7b2cf38e685211349175cd1d"
DECIMAL = str(int(HEX, 16))

CENTER_MODE = "left"  # "left" or "right"


def trace_decimal_digits(s: str, mode: str) -> list[dict]:
    rows = [{
        "step": 0,
        "removed_index": "",
        "removed_digit": "",
        "remaining_decimal": s,
        "value": int(s),
    }]

    step = 0
    while len(s) > 1:
        n = len(s)

        if mode == "end":
            idx = n - 1
        elif mode == "start":
            idx = 0
        elif mode == "center":
            if n % 2 == 1:
                idx = n // 2
            elif CENTER_MODE == "left":
                idx = n // 2 - 1
            else:
                idx = n // 2
        else:
            raise ValueError("mode must be end, start, or center")

        removed = s[idx]
        s = s[:idx] + s[idx + 1:]
        step += 1

        rows.append({
            "step": step,
            "removed_index": idx,
            "removed_digit": removed,
            "remaining_decimal": s,
            "value": int(s),
        })

    return rows


def main() -> None:
    traces = {
        "from_end": trace_decimal_digits(DECIMAL, "end"),
        "from_start": trace_decimal_digits(DECIMAL, "start"),
        "from_center": trace_decimal_digits(DECIMAL, "center"),
    }

    print("SHA-256 empty-string digest:")
    print(HEX)
    print()
    print("Decimal:")
    print(DECIMAL)
    print()

    output = Path("empty_hash_decimal_deletion_traces.csv")
    with output.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([
            "trace",
            "step",
            "removed_index",
            "removed_digit",
            "remaining_decimal",
            "value",
        ])

        for name, rows in traces.items():
            print(f"=== {name} ===")
            for row in rows:
                print(
                    row["step"],
                    row["removed_digit"],
                    row["remaining_decimal"],
                    row["value"],
                    sep="\t",
                )
                writer.writerow([
                    name,
                    row["step"],
                    row["removed_index"],
                    row["removed_digit"],
                    row["remaining_decimal"],
                    row["value"],
                ])
            print()

    print(f"CSV written to: {output.resolve()}")


if __name__ == "__main__":
    main()
