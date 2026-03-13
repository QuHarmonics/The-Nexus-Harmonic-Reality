#!/usr/bin/env python3
# ==============================================================
# BytesOfPI "Disassembler" — full run (not snippets)
# - Reads BytesOfPI.xlsm
# - Extracts raw header bytes (default: first 96 bytes of the file)
# - Produces a simple opcode-style disassembly over the byte stream
# - Saves CSV + plots + extracts vbaProject.bin (if present) for
#   external VBA decompilation (olevba / pcodedmp)
#
# NOTE:
# This does NOT claim to recover true CPU assembly from an .xlsm.
# It is a Nexus-style "behavioral disassembly": mapping byte-to-byte
# transitions into a small instruction set (verbs).
#
# If you want the actual VBA source:
#   pip install oletools
#   olevba xl/vbaProject.bin (or the .xlsm directly)
# ==============================================================

import os, zipfile, math, csv, hashlib
from dataclasses import dataclass
from typing import List, Dict, Tuple, Optional

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# -----------------------------
# Config
# -----------------------------
XLSM_PATH = "BytesOfPI.xlsm"          # put in same folder as this script
OUTDIR    = "bytesofpi_disasm_out"
N_HEADER_BYTES = 88                   # your prior run shows 87 rows; 88 bytes -> 87 transitions


# -----------------------------
# Helpers
# -----------------------------
def ensure_outdir(outdir: str):
    os.makedirs(outdir, exist_ok=True)

def read_file_bytes(path: str, n: int) -> np.ndarray:
    with open(path, "rb") as f:
        b = f.read(n)
    return np.frombuffer(b, dtype=np.uint8)

def extract_vba_project(xlsm_path: str, outdir: str) -> Optional[str]:
    """
    Extract xl/vbaProject.bin from the .xlsm if present.
    Returns path to extracted file or None.
    """
    try:
        with zipfile.ZipFile(xlsm_path, "r") as zf:
            cand = None
            for name in zf.namelist():
                if name.lower().endswith("vbaProject.bin".lower()):
                    cand = name
                    break
            if cand is None:
                return None
            outpath = os.path.join(outdir, "vbaProject.bin")
            with zf.open(cand) as src, open(outpath, "wb") as dst:
                dst.write(src.read())
            return outpath
    except Exception:
        return None

def disassemble_bytes(header: np.ndarray) -> pd.DataFrame:
    """
    Build a small opcode set over consecutive byte pairs.
    Opcodes are "verbs" about how state changes from t-1 to t.

    Opcodes:
      HOLD:   b[t] == b[t-1]
      PUSH:   first element (no previous)
      DIFF2:  delta = b[t]-b[t-1] (signed) and abs(delta) is small-ish (<=32)
      ADD2:   looks like modular addition step (b[t] == (b[t-1] + k) % 256 with k in {1..7})
      XOR2:   looks like XOR with a small mask (b[t] == b[t-1] XOR m with m in {1,2,4,8,16,32,64,128})
      SUM_mod16:      (b[t] + b[t-1]) % 16 == 0
      DIFFSUM_mod16:  (b[t] - b[t-1]) % 16 == 0
    """
    rows = []
    prev = None
    for t, b in enumerate(header):
        if prev is None:
            rows.append(dict(t=t, byte=int(b), prev=np.nan, delta=np.nan, opcode="PUSH", arg=np.nan))
            prev = int(b)
            continue

        cur = int(b)
        delta = cur - prev

        opcode = None
        arg = None

        # Priority: exact equality
        if cur == prev:
            opcode, arg = "HOLD", 0
        else:
            # mod-16 constraints
            if ((cur + prev) % 16) == 0:
                opcode, arg = "SUM_mod16", (cur + prev) % 16
            if ((cur - prev) % 16) == 0:
                # if both hit, mark the stronger (DIFFSUM_mod16)
                opcode, arg = "DIFFSUM_mod16", (cur - prev) % 16

            # XOR with power-of-two mask
            for m in (1,2,4,8,16,32,64,128):
                if cur == (prev ^ m):
                    opcode, arg = "XOR2", m
                    break

            # small modular add
            if opcode is None:
                for k in range(1,8):
                    if cur == ((prev + k) & 0xFF):
                        opcode, arg = "ADD2", k
                        break

            # small difference
            if opcode is None and abs(delta) <= 32:
                opcode, arg = "DIFF2", delta

            # fallback
            if opcode is None:
                opcode, arg = "DIFF2", delta  # default verb: delta step

        rows.append(dict(t=t, byte=cur, prev=prev, delta=delta, opcode=opcode, arg=arg))
        prev = cur

    df = pd.DataFrame(rows)
    return df

def compute_header_repeats(header: np.ndarray) -> pd.DataFrame:
    """
    For each index i, find next j>i where header[j]==header[i].
    Record the repeat gap (j-i).
    """
    vals = header.astype(int).tolist()
    positions: Dict[int, List[int]] = {}
    for i, v in enumerate(vals):
        positions.setdefault(v, []).append(i)

    events = []
    for v, idxs in positions.items():
        if len(idxs) < 2:
            continue
        for a, b in zip(idxs[:-1], idxs[1:]):
            events.append(dict(value=v, i=a, j=b, gap=b-a))
    return pd.DataFrame(events).sort_values(["gap","value","i"]).reset_index(drop=True)

def plot_all(header: np.ndarray, df_dis: pd.DataFrame, repeats: pd.DataFrame, outdir: str):
    # 1) Header byte trace
    plt.figure(figsize=(14,5))
    plt.plot(np.arange(len(header)), header.astype(int))
    plt.xlabel("t (byte index)")
    plt.ylabel("Header byte value")
    plt.title("Header byte trace")
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(os.path.join(outdir, "header_byte_trace.png"), dpi=160)
    plt.close()

    # 2) Match-over-time (matched = opcode != fallback DIFF2 large?)
    # Here: "matched" means opcode is one of the named structured ops.
    structured = {"HOLD","PUSH","ADD2","XOR2","SUM_mod16","DIFFSUM_mod16"}
    matched = df_dis["opcode"].isin(structured).astype(int).values

    plt.figure(figsize=(14,4))
    plt.plot(df_dis["t"].values, matched)
    plt.ylim(-0.05, 1.05)
    plt.xlabel("t")
    plt.ylabel("Matched (1=yes)")
    plt.title("Match-over-time (structured opcode hits)")
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(os.path.join(outdir, "match_over_time.png"), dpi=160)
    plt.close()

    # 3) Opcode counts
    counts = df_dis["opcode"].value_counts().reset_index()
    counts.columns = ["opcode","count"]
    plt.figure(figsize=(10,4))
    plt.bar(counts["opcode"], counts["count"])
    plt.xticks(rotation=35, ha="right")
    plt.ylabel("Count")
    plt.title("Opcode counts")
    plt.grid(True, axis="y", alpha=0.3)
    plt.tight_layout()
    plt.savefig(os.path.join(outdir, "opcode_counts.png"), dpi=160)
    plt.close()

    # 4) Repeat gap histogram
    if len(repeats) > 0:
        plt.figure(figsize=(10,4))
        plt.hist(repeats["gap"].values, bins=25)
        plt.xlabel("Repeat gap (steps)")
        plt.ylabel("Count")
        plt.title("Repeat gap histogram")
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        plt.savefig(os.path.join(outdir, "repeat_gap_hist.png"), dpi=160)
        plt.close()


def write_summary(df_dis: pd.DataFrame, repeats: pd.DataFrame, outdir: str):
    structured = {"HOLD","PUSH","ADD2","XOR2","SUM_mod16","DIFFSUM_mod16"}
    matched_rate = float(df_dis["opcode"].isin(structured).mean())
    unique_headers = int(df_dis["byte"].nunique())

    most_common_gap = None
    med_gap = None
    if len(repeats) > 0:
        med_gap = float(np.median(repeats["gap"].values))
        most_common_gap = int(repeats["gap"].value_counts().idxmax())

    lines = []
    lines.append(f"Rows disassembled: {len(df_dis)}")
    lines.append(f"Matched: {matched_rate*100:.1f}%")
    lines.append("Opcode counts:")
    for k, v in df_dis["opcode"].value_counts().items():
        lines.append(f"  {k}: {int(v)}")
    lines.append(f"Unique headers: {unique_headers}")
    lines.append(f"Repeat events: {len(repeats)}")
    if med_gap is not None:
        lines.append(f"Median repeat gap: {med_gap}")
    if most_common_gap is not None:
        lines.append(f"Most common gap: {most_common_gap}")

    outpath = os.path.join(outdir, "summary.txt")
    with open(outpath, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))


def main():
    ensure_outdir(OUTDIR)

    if not os.path.exists(XLSM_PATH):
        raise FileNotFoundError(f"Can't find {XLSM_PATH}. Put it next to this script or edit XLSM_PATH.")

    # Extract VBA project (for true macro analysis later)
    vba_path = extract_vba_project(XLSM_PATH, OUTDIR)

    # "Header" bytes = first N bytes of the container file (you can change this)
    header = read_file_bytes(XLSM_PATH, N_HEADER_BYTES)

    df_dis = disassemble_bytes(header)
    repeats = compute_header_repeats(header)

    # Save artifacts
    df_dis.to_csv(os.path.join(OUTDIR, "pi_header_disassembly.csv"), index=False)
    repeats.to_csv(os.path.join(OUTDIR, "header_repeats.csv"), index=False)
    df_dis["opcode"].value_counts().to_csv(os.path.join(OUTDIR, "opcode_counts.csv"))

    plot_all(header, df_dis, repeats, OUTDIR)
    write_summary(df_dis, repeats, OUTDIR)

    print("DONE")
    print("OUTDIR:", OUTDIR)
    if vba_path:
        print("Extracted vbaProject.bin to:", vba_path)
        print("For VBA source, run (outside Python):")
        print("  pip install oletools")
        print("  olevba BytesOfPI.xlsm  # or olevba bytesofpi_disasm_out/vbaProject.bin")
    else:
        print("No vbaProject.bin found (workbook may contain no macros).")


if __name__ == "__main__":
    main()
