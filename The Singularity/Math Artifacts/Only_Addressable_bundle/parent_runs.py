"""Recompute: minimal unreadable extensions through depth 12, and how many runs of the other bit's region
(maximal runs of consecutive slices of ring k+1 holding bit 1-b) each parent's location set meets."""
import sys, math
import numpy as np
from ringlib import grow
Dmax = 12
S = {L: L * (1 << L) for L in range(1, Dmax + 1)}
Q = 1
for L in S: Q = Q * S[L] // math.gcd(Q, S[L])
bnd = np.unique(np.concatenate([np.arange(S[L], dtype=np.int64) * (Q // S[L]) for L in S]))
tapes = {L: np.frombuffer("".join(grow(L)).encode(), dtype=np.uint8) - 48 for L in S}
sl = {L: (bnd * S[L]) // Q for L in S}                     # slice index of each atom on ring L
prof = np.zeros(len(bnd), dtype=np.int64)
for L in range(1, Dmax + 1): prof |= tapes[L][sl[L]].astype(np.int64) << (Dmax - L)
from collections import Counter
hist = Counter(); total = 0
for k in range(1, Dmax):
    pk = prof >> (Dmax - k)                                 # depth-k prefix per atom
    nxt = tapes[k + 1][sl[k + 1]]                          # ring k+1 bit per atom
    # run id on ring k+1: consecutive slices with equal bit form one run
    t = tapes[k + 1]; run_id = np.concatenate([[0], np.cumsum(t[1:] != t[:-1])])
    rid = run_id[sl[k + 1]]
    for p in np.unique(pk):
        m = pk == p; bits = np.unique(nxt[m])
        if len(bits) == 1:                                  # child (p, 1-bits) is unreadable
            total += 1; hist[len(np.unique(rid[m]))] += 1
print(f"minimal unreadable extensions through depth {Dmax}: {total}")
print("parents meeting 1/2/3/... runs of the surviving bit:", dict(sorted(hist.items())))
print("meeting more than one run:", sum(v for kk, v in hist.items() if kk > 1))
