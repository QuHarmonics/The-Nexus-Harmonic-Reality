
"""
pi_disassembler_from_bbp.py

Pure-Python (no Excel) reproduction of the "BytesOfPI disassembler" idea:

1) Generate bytes of π using the BBP formula (hex digits, then pack into bytes).
2) "Disassemble" the byte stream into a tiny opcode set by searching for simple
   relations between earlier bytes (stack-like backreferences).
3) Export CSVs + plots:
   - header_byte_trace.png
   - match_over_time.png
   - opcode_counts.png
   - repeat_gap_hist.png
   - pi_header_disassembly.csv
   - opcode_counts.csv
   - header_repeats.csv
   - summary.txt

Run:
  python pi_disassembler_from_bbp.py --nbytes 96 --max_back 64 --outdir pi_out
"""

from __future__ import annotations
import argparse, math, os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# -------------------------
# BBP hex digit extraction
# -------------------------

def _series(j: int, n: int, tail_terms: int = 100) -> float:
    """
    Helper for BBP digit extraction:
    S_j(n) = sum_{k=0}^∞ 16^{n-k} / (8k + j)  (mod 1)
    We compute the finite part with modular exponentiation (exact modulo),
    and a short floating tail.
    """
    # finite sum (k = 0..n) using modular exponentiation
    s = 0.0
    for k in range(n + 1):
        denom = 8 * k + j
        # 16^(n-k) mod denom
        p = pow(16, n - k, denom)
        s = (s + p / denom) % 1.0

    # tail (k = n+1..n+tail_terms) in floating point
    t = 0.0
    for k in range(n + 1, n + 1 + tail_terms):
        denom = 8 * k + j
        t += (16.0 ** (n - k)) / denom

    return (s + t) % 1.0


def pi_hex_digit(n: int) -> int:
    """
    Return the nth hexadecimal digit of π after the decimal point (0-indexed),
    using the BBP formula.
    """
    # x = fractional part of 16^n * pi
    x = (4.0 * _series(1, n) - 2.0 * _series(4, n) - _series(5, n) - _series(6, n)) % 1.0
    return int(16.0 * x) & 0xF


def pi_bytes(nbytes: int) -> bytes:
    """
    Produce nbytes bytes of π by extracting 2*nbytes BBP hex digits and packing.
    """
    out = bytearray()
    for i in range(nbytes):
        hi = pi_hex_digit(2 * i)
        lo = pi_hex_digit(2 * i + 1)
        out.append((hi << 4) | lo)
    return bytes(out)


# -------------------------
# Disassembler
# -------------------------

OP_PRIORITY = ["HOLD", "DIFF2", "XOR2", "ADD2", "SUM_mod16", "DIFFSUM_mod16"]

def _candidates_for_t(data: np.ndarray, t: int, max_back: int):
    """
    Yield candidate matches for time t:
    (opcode, i, j, detail, score)
    Score is designed so we prefer *deeper* references (larger gap),
    then fall back to opcode priority.
    """
    cur = int(data[t])
    lo = max(0, t - max_back)

    # quick HOLD (1-back) check
    if t > 0 and cur == int(data[t - 1]):
        yield ("HOLD", t - 1, t - 1, f"from t{t-1}: {cur}", (t - (t - 1), OP_PRIORITY.index("HOLD")))

    # search pairs (i,j) in the back window
    # Use j as the "newer" index to make gap definition consistent.
    for j in range(t - 1, lo - 1, -1):
        bj = int(data[j])
        for i in range(j - 1, lo - 1, -1):
            bi = int(data[i])

            # core ops
            if cur == abs(bj - bi):
                gap = t - j
                yield ("DIFF2", j, i, f"from t{j}-t{i}: |{bj}-{bi}|", (gap, OP_PRIORITY.index("DIFF2")))
            if cur == (bj ^ bi):
                gap = t - j
                yield ("XOR2", j, i, f"from t{j} xor t{i}: {bj}^{bi}", (gap, OP_PRIORITY.index("XOR2")))
            if cur == ((bj + bi) & 0xFF):
                gap = t - j
                yield ("ADD2", j, i, f"from t{j}+t{i}: ({bj}+{bi}) mod 256", (gap, OP_PRIORITY.index("ADD2")))

            # low-order / "header-ish" ops
            if (cur & 0xF) == ((bj + bi) & 0xF):
                gap = t - j
                yield ("SUM_mod16", j, i, f"from t{j}+t{i}: ({bj}+{bi}) mod 16", (gap, OP_PRIORITY.index("SUM_mod16")))
            if (cur & 0xF) == ((abs(bj - bi) + bj + bi) & 0xF):
                gap = t - j
                yield ("DIFFSUM_mod16", j, i, f"from (|{bj}-{bi}|+{bj}+{bi}) mod 16", (gap, OP_PRIORITY.index("DIFFSUM_mod16")))


def disassemble(data_bytes: bytes, max_back: int = 64) -> pd.DataFrame:
    data = np.frombuffer(data_bytes, dtype=np.uint8).astype(int)
    rows = []
    for t in range(len(data)):
        if t == 0:
            rows.append(dict(t=t, byte=int(data[t]), opcode="PUSH", src1=np.nan, src2=np.nan, detail="seed"))
            continue

        cands = list(_candidates_for_t(data, t, max_back=max_back))
        if not cands:
            rows.append(dict(t=t, byte=int(data[t]), opcode="PUSH", src1=np.nan, src2=np.nan, detail="no match in window"))
            continue

        # Pick the *deepest* reference first (largest gap => larger "memory"),
        # then opcode priority.
        # Note: score is (gap, priority_idx); larger gap is better.
        best = max(cands, key=lambda x: (x[4][0], -x[4][1]))
        opcode, src1, src2, detail, _score = best
        rows.append(dict(t=t, byte=int(data[t]), opcode=opcode, src1=int(src1), src2=int(src2), detail=detail))

    return pd.DataFrame(rows)


def repeat_gaps(data_bytes: bytes) -> pd.DataFrame:
    data = np.frombuffer(data_bytes, dtype=np.uint8).astype(int)
    last = {}
    reps = []
    for t, b in enumerate(data):
        b = int(b)
        if b in last:
            reps.append(dict(t=t, byte=b, prev_t=last[b], gap=t-last[b]))
        last[b] = t
    return pd.DataFrame(reps)


# -------------------------
# Main + outputs
# -------------------------

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--nbytes", type=int, default=96, help="How many π-bytes to generate.")
    ap.add_argument("--max_back", type=int, default=64, help="Backreference window for disassembler.")
    ap.add_argument("--outdir", type=str, default="pi_disasm_out")
    args = ap.parse_args()

    os.makedirs(args.outdir, exist_ok=True)

    # 1) Generate π bytes
    b = pi_bytes(args.nbytes)
    data = np.frombuffer(b, dtype=np.uint8).astype(int)

    # 2) Disassemble
    df = disassemble(b, max_back=args.max_back)

    # 3) Repeats
    reps = repeat_gaps(b)

    # 4) Summaries
    opcode_counts = df["opcode"].value_counts().rename_axis("opcode").reset_index(name="count")
    match = (df["opcode"] != "PUSH").astype(int)

    # Save CSVs
    df.to_csv(os.path.join(args.outdir, "pi_header_disassembly.csv"), index=False)
    opcode_counts.to_csv(os.path.join(args.outdir, "opcode_counts.csv"), index=False)
    reps.to_csv(os.path.join(args.outdir, "header_repeats.csv"), index=False)

    # Save summary text
    match_rate = float(match.mean())
    median_gap = float(reps["gap"].median()) if len(reps) else float("nan")
    with open(os.path.join(args.outdir, "summary.txt"), "w", encoding="utf-8") as f:
        f.write("PI BYTE DISASSEMBLY (BBP)\n")
        f.write("========================\n\n")
        f.write(f"nbytes: {args.nbytes}\n")
        f.write(f"max_back: {args.max_back}\n")
        f.write(f"match_rate (opcode != PUSH): {match_rate:.3f}\n")
        f.write(f"repeat_gap_median: {median_gap}\n\n")
        f.write("opcode_counts:\n")
        for _, r in opcode_counts.iterrows():
            f.write(f"  {r['opcode']}: {int(r['count'])}\n")

    # 5) Plots (matplotlib only; no explicit colors)
    # header_byte_trace
    plt.figure(figsize=(12,4))
    plt.plot(range(len(data)), data)
    plt.title("π byte trace (BBP)")
    plt.xlabel("t (byte index)")
    plt.ylabel("byte value")
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(os.path.join(args.outdir, "header_byte_trace.png"), dpi=160)
    plt.close()

    # match_over_time
    plt.figure(figsize=(12,3))
    plt.plot(range(len(match)), match)
    plt.title("Match-over-time (structured opcode hits)")
    plt.xlabel("t")
    plt.ylabel("Matched (1=yes)")
    plt.ylim(-0.05, 1.05)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(os.path.join(args.outdir, "match_over_time.png"), dpi=160)
    plt.close()

    # opcode_counts bar
    plt.figure(figsize=(8,4))
    plt.bar(opcode_counts["opcode"], opcode_counts["count"])
    plt.title("Opcode counts")
    plt.xlabel("opcode")
    plt.ylabel("count")
    plt.xticks(rotation=35, ha="right")
    plt.grid(True, axis="y", alpha=0.3)
    plt.tight_layout()
    plt.savefig(os.path.join(args.outdir, "opcode_counts.png"), dpi=160)
    plt.close()

    # repeat_gap histogram
    if len(reps):
        plt.figure(figsize=(8,4))
        plt.hist(reps["gap"], bins=30)
        plt.title("Repeat gap histogram (byte repeats)")
        plt.xlabel("repeat gap (steps)")
        plt.ylabel("count")
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        plt.savefig(os.path.join(args.outdir, "repeat_gap_hist.png"), dpi=160)
        plt.close()

    print("DONE. Outputs in:", args.outdir)


if __name__ == "__main__":
    main()
