#!/usr/bin/env python3
"""
gearbox_lab.py — Constant Gearbox Lab

π(64) is treated as a read-only wheel.
Two overlapping samplers (phase0, phase1) carve teeth (0/1) on a 64-slot ring.
Meshing is simulated as contact pulses under a relative rotation step based on H = π/9.

Outputs:
- pi64_gearbox_xray.png
- pi64_gear_pulses.csv
- pi64_gear_A.svg, pi64_gear_B.svg, pi64_gear_X.svg
"""

import numpy as np, math, pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

pi64 = "1415926525897922846264882795028841971699975105820974944592078164"
digits = np.array([int(ch) for ch in pi64], dtype=np.uint8)

def bytes_overlap(digs, start=0):
    return np.array([(int(digs[i])<<4) | int(digs[i+1]) for i in range(start, len(digs)-1)], dtype=np.uint8)

def to_len(arr, L):
    reps = (L + len(arr) - 1)//len(arr)
    return np.tile(arr, reps)[:L].astype(np.uint8)

def bytes_to_bits(byte_arr):
    bits = np.zeros(len(byte_arr)*8, dtype=np.uint8)
    k = 0
    for b in byte_arr:
        for j in range(8):
            bits[k] = (int(b) >> (7-j)) & 1
            k += 1
    return bits

phase0 = bytes_overlap(digits, 0)
phase1 = bytes_overlap(digits, 1)
C0 = to_len(phase0, 64)
C1 = to_len(phase1, 64)
CX = (C0 ^ C1).astype(np.uint8)

bits0 = bytes_to_bits(C0)
bits1 = bytes_to_bits(C1)
bitsX = bytes_to_bits(CX)

def gear_teeth(bits, N=64, offset=0):
    return np.roll(bits, -offset)[:N].astype(np.uint8)

N = 64
A = gear_teeth(bits0, N)
B = gear_teeth(bits1, N)
X = gear_teeth(bitsX, N)

H = math.pi/9
r_idx = N * H / (2*math.pi)  # N/18

def mesh_pulses(ta, tb, steps=2048, phase=0.0, r=r_idx):
    N = len(ta)
    acc = float(phase)
    pulses = np.zeros(steps, dtype=np.uint8)
    idx_a = 0
    for t in range(steps):
        idx_b = int(math.floor(acc)) % N
        pulses[t] = 1 if (ta[idx_a] & tb[idx_b]) else 0
        idx_a = (idx_a + 1) % N
        acc = (acc + r) % N
    return pulses

p_AB = mesh_pulses(A, B)

pd.DataFrame({"t": np.arange(len(p_AB)), "AB": p_AB}).to_csv("pi64_gear_pulses.csv", index=False)
plt.figure(figsize=(10,4)); plt.plot(p_AB[:256])
plt.title("Contact pulses (A↔B), first 256 ticks"); plt.xlabel("t"); plt.ylabel("contact")
plt.savefig("pi64_gear_pulses.png", dpi=160, bbox_inches="tight"); plt.close()
print("Saved: pi64_gear_pulses.csv and pi64_gear_pulses.png")
