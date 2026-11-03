"""Independent recomputation of the radial-profile language through depth 16.
Exact: atoms of the common refinement of all slice boundaries j/(L 2^L), L <= Dmax, over one integer
denominator Q = lcm(L 2^L). Each atom has one profile. Counts R_d, new exclusions E_d = 2R_{d-1}-R_d,
minimal DFA sizes of the horizon languages L_<=H (prefix-closed, all members accepting, plus one sink),
and the number of depth-11 classes distinguished by continuations up to horizon H."""
import sys, math, time
import numpy as np
sys.path.insert(0, "/home/claude/space/rings")
from ringlib import grow

Dmax = int(sys.argv[1]) if len(sys.argv) > 1 else 16
t0 = time.time()
S = {L: L * (1 << L) for L in range(1, Dmax + 1)}
Q = 1
for L in S: Q = Q * S[L] // math.gcd(Q, S[L])
# all boundaries as integers over Q
bnd = np.unique(np.concatenate([np.arange(S[L], dtype=np.int64) * (Q // S[L]) for L in S]))
print(f"Dmax={Dmax}: Q={Q}  atoms={len(bnd)}  ({time.time()-t0:.1f}s)", flush=True)
prof = np.zeros(len(bnd), dtype=np.uint32)
for L in range(1, Dmax + 1):
    tape = np.frombuffer("".join(grow(L)).encode(), dtype=np.uint8) - 48
    j = (bnd * S[L]) // Q                    # slice of ring L containing the atom's left end
    prof |= tape[j].astype(np.uint32) << (Dmax - L)
print(f"profiles read ({time.time()-t0:.1f}s)", flush=True)
uniq = np.unique(prof)
R = {d: len(np.unique(uniq >> (Dmax - d))) for d in range(1, Dmax + 1)}
print("\n d   R_d     E_d=2R_{d-1}-R_d")
for d in range(1, Dmax + 1):
    E = 2 * R[d - 1] - R[d] if d > 1 else 0
    print(f"{d:2d}  {R[d]:6d}   {E:5d}")

# trie of reachable prefixes, as sets of integers per depth
P = {d: set((uniq >> (Dmax - d)).tolist()) for d in range(0, Dmax + 1)}

def dfa_size(H):
    """minimal DFA states of L_<=H: distinct right languages of members, plus sink."""
    sig = {}
    ids = {}
    for d in range(H, -1, -1):
        for p in P[d] if d <= Dmax else ():
            if d == H: key = ("end",)
            else:
                c0 = sig.get((d + 1, p << 1)); c1 = sig.get((d + 1, (p << 1) | 1))
                key = (c0, c1)
            if key not in ids: ids[key] = len(ids)
            sig[(d, p)] = ids[key]
    return len(ids) + 1, sig

print("\n H   minimal DFA states of L_<=H")
for H in range(8, Dmax + 1):
    n, _ = dfa_size(H)
    print(f"{H:2d}  {n}")

print("\n H   distinct continuation classes among depth-11 prefixes (continuations to depth H)")
for H in range(11, Dmax + 1):
    _, sig = dfa_size(H)
    print(f"{H:2d}  {len({sig[(11, p)] for p in P[11]})}")
print(f"\n({time.time()-t0:.1f}s)")
