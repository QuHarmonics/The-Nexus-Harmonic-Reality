#!/usr/bin/env python3
"""
NEXUS Depth Engine (S4)
Dean Kulik, QuHarmonics.  ORCID 0009-0003-3128-8828

Runs the depth ladder instead of another surface statistic.

  Substrate is complete. Resolution lives in the reader. Depth is entering
  the closed loop, not scanning wider. Each level's STATES are the previous
  level's TRANSITIONS -- vertices, then edges, then edges-of-edges.

At every level it reports:
  * the slot table  -- the enumerated addressable objects at that depth.
                       This is the carved space. Save it; the next run
                       starts on the far side of it.
  * H              -- bits per symbol at that depth
  * fold           -- bits folded away relative to the level below
  * leak           -- I(C_{t+1} ; C_{t-1} | C_t), against a shuffle floor.
                       leak == floor : level is CLOSED. It continues on its
                                       own. This is the clock face.
                       leak >  floor : level is OPEN. It cannot continue
                                       without the level beneath it. This is
                                       where Fix has to enter.

USAGE
  python3 depth_engine.py                       # defaults, ~30 s
  python3 depth_engine.py --n 40000000 --levels 6
  python3 depth_engine.py --substrate sha       # sha | uniform | pi | file
  python3 depth_engine.py --substrate file --path mydata.hex
  python3 depth_engine.py --slots slots.json    # write the slot table out

Only numpy required. mpmath only if --substrate pi.
"""
import argparse, hashlib, json, math, os, sys
import numpy as np

HEX = "0123456789abcdef"
bar = lambda c="-": print(c * 78)


# ---------------------------------------------------------------------------
# substrates
# ---------------------------------------------------------------------------
def sub_uniform(n, seed):
    return np.random.default_rng(seed).integers(0, 16, n).astype(np.int64)

def sub_sha(n, seed):
    """concatenated sha-256 digests, hex nibbles"""
    out = bytearray()
    ctr = seed * 10**9
    need = (n + 63) // 64
    for i in range(need):
        out += hashlib.sha256(str(ctr + i).encode()).digest()
    a = np.frombuffer(bytes(out), np.uint8)
    hi, lo = a >> 4, a & 0xF
    return np.stack([hi, lo], 1).ravel()[:n].astype(np.int64)

def sub_pi(n, seed):
    import mpmath
    mpmath.mp.prec = int(4 * n + 128)
    v = mpmath.mpf(mpmath.pi) - 3
    d = np.empty(n, np.int64)
    for i in range(n):
        v *= 16
        k = int(v)
        d[i] = k
        v -= k
    return d

def sub_file(n, path):
    raw = open(path, "rb").read()
    txt = raw.decode("ascii", "ignore").lower()
    keep = np.array([c in HEX for c in txt])
    if keep.mean() > 0.9:
        lut = np.full(256, -1, np.int64)
        for i, c in enumerate(HEX):
            lut[ord(c)] = i
        d = lut[np.frombuffer(txt.encode(), np.uint8)]
        d = d[d >= 0]
    else:
        a = np.frombuffer(raw, np.uint8)
        d = np.stack([a >> 4, a & 0xF], 1).ravel().astype(np.int64)
    return d[:n]


# ---------------------------------------------------------------------------
# information tools, fully vectorised
# ---------------------------------------------------------------------------
def entropy(seq, K):
    p = np.bincount(seq, minlength=K).astype(float)
    p = p[p > 0] / p.sum()
    return float(-(p * np.log2(p)).sum())

def cmi(seq, K):
    """I(C_{t+1} ; C_{t-1} | C_t), plug-in, vectorised."""
    if seq.size < 100:
        return 0.0
    x, y, z = seq[:-2], seq[1:-1], seq[2:]
    idx = (x * K + y) * K + z
    J = np.bincount(idx, minlength=K**3).astype(float).reshape(K, K, K)
    J /= J.sum()
    pxy = J.sum(2)[:, :, None]
    pyz = J.sum(0)[None, :, :]
    py = J.sum((0, 2))[None, :, None]
    with np.errstate(divide="ignore", invalid="ignore"):
        t = J * np.log2((J * py) / (pxy * pyz))
    return float(np.nansum(np.where(J > 0, t, 0.0)))

def floor_cmi(seq, K, rng):
    s = seq.copy()
    rng.shuffle(s)
    return cmi(s, K)


# ---------------------------------------------------------------------------
# LEVEL 1 reader: geometric admissibility of sliding triples
# ---------------------------------------------------------------------------
L1_NAMES = ["NULL-SIDE", "IMPOSSIBLE", "DEGENERATE", "SCALENE",
            "RIGHT", "ISOSCELES", "EQUILATERAL"]

def read_shape(d, stride=1):
    a, b, c = d[:-2], d[1:-1], d[2:]
    s = a + b + c
    mx = np.maximum(np.maximum(a, b), c)
    mn = np.minimum(np.minimum(a, b), c)
    rest = s - mx
    md = s - mx - mn
    out = np.empty(a.size, np.int64)
    ns = mn == 0
    im = (~ns) & (mx > rest)
    dg = (~ns) & (mx == rest)
    lv = ~(ns | im | dg)
    eq = lv & (mn == mx)
    rt = lv & (~eq) & (mn * mn + md * md == mx * mx)
    iso = lv & (~eq) & (~rt) & ((a == b) | (b == c) | (a == c))
    sc = lv & (~eq) & (~rt) & (~iso)
    out[ns], out[im], out[dg] = 0, 1, 2
    out[sc], out[rt], out[iso], out[eq] = 3, 4, 5, 6
    return out[::stride], 7, L1_NAMES


# ---------------------------------------------------------------------------
# LEVEL n>1 reader: the STATES here are the EDGES down there.
# Enter the closed loop: read what the level below does between its states,
# not what its states are.
# ---------------------------------------------------------------------------
def read_edges(seq, K, names=None):
    """symbol at t encodes the ordered pair (seq[t], seq[t+1]) collapsed to
       the structural move it represents:
         0 HOLD        stayed in the same state
         1 OPEN        moved into a state with more freedom (higher class idx)
         2 CLOSE       moved into a state with less freedom
         3 CROSS-BDY   either endpoint is the boundary state (DEGENERATE-like)
       plus the identity of the destination, so the alphabet is 4*K but only
       the reachable cells are slots."""
    a, b = seq[:-1], seq[1:]
    move = np.where(a == b, 0, np.where(b > a, 1, 2))
    bdy = (a == 2) | (b == 2)          # index 2 is the boundary class at L1
    move = np.where(bdy, 3, move)
    sym = move * K + b
    used = np.unique(sym)
    remap = np.full(4 * K, -1, np.int64)
    remap[used] = np.arange(used.size)
    nm = []
    for u in used:
        mv = ["HOLD", "OPEN", "CLOSE", "BDY"][u // K]
        dst = u % K
        dn = names[dst] if names and dst < len(names) else f"s{dst}"
        nm.append(f"{mv}->{dn}")
    return remap[sym], int(used.size), nm


# ---------------------------------------------------------------------------
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--n", type=int, default=4_000_000, help="substrate symbols")
    ap.add_argument("--levels", type=int, default=5)
    ap.add_argument("--substrate", default="uniform",
                    choices=["uniform", "sha", "pi", "file"])
    ap.add_argument("--path", default=None)
    ap.add_argument("--seed", type=int, default=1)
    ap.add_argument("--stride", type=int, default=1,
                    help="1 = sliding (overlapping reader); 3 = disjoint")
    ap.add_argument("--slots", default=None, help="write slot table json here")
    ap.add_argument("--max-alpha", type=int, default=64,
                    help="stop if a level's alphabet exceeds this")
    A = ap.parse_args()

    rng = np.random.default_rng(A.seed + 777)
    if A.substrate == "uniform":
        d = sub_uniform(A.n, A.seed)
    elif A.substrate == "sha":
        d = sub_sha(A.n, A.seed)
    elif A.substrate == "pi":
        d = sub_pi(A.n, A.seed)
    else:
        if not A.path:
            sys.exit("--substrate file needs --path")
        d = sub_file(A.n, A.path)

    print(f"NEXUS DEPTH ENGINE   substrate={A.substrate}  symbols={d.size:,}"
          f"  stride={A.stride}")
    bar("=")

    slot_table = {}
    seq, K, names = d, 16, [f"{c}" for c in HEX]
    H_prev = entropy(seq, K)
    print(f"LEVEL 0  (substrate)   alphabet {K}   H = {H_prev:.5f} bits/sym")
    bar()

    for lvl in range(1, A.levels + 1):
        if lvl == 1:
            seq, K, names = read_shape(seq, A.stride)
        else:
            seq, K, names = read_edges(seq, K, names)
        if K > A.max_alpha:
            print(f"LEVEL {lvl}: alphabet {K} exceeds --max-alpha; stopping.")
            break
        if seq.size < 1000:
            print(f"LEVEL {lvl}: stream exhausted ({seq.size} symbols); stopping.")
            break

        H = entropy(seq, K)
        lk = cmi(seq, K)
        fl = floor_cmi(seq, K, rng)
        pop = np.bincount(seq, minlength=K)
        closed = lk <= fl * 1.5 + 1e-9

        print(f"LEVEL {lvl}   alphabet {K:3d}   symbols {seq.size:,}")
        print(f"   H        = {H:9.5f} bits/sym      fold from above = "
              f"{H_prev - H:+.5f}")
        print(f"   leak     = {lk:9.6f} bits         shuffle floor   = {fl:.6f}")
        print(f"   verdict  = {'CLOSED  (runs on its own -- clock face)' if closed else 'OPEN    (needs the level beneath -- Fix enters here)'}")
        print(f"   slot table ({K} addressable objects):")
        rows = sorted(zip(names, pop), key=lambda r: -r[1])
        for nm, ct in rows[:12]:
            print(f"        {nm:<26s} {ct:>12,}  p={ct/seq.size:.6f}")
        if K > 12:
            print(f"        ... {K-12} more")
        slot_table[f"level{lvl}"] = {
            "alphabet": int(K), "H": H, "leak": lk, "floor": fl,
            "closed": bool(closed),
            "slots": [{"name": nm, "count": int(ct)} for nm, ct in zip(names, pop)],
        }
        H_prev = H
        bar()

    if A.slots:
        json.dump(slot_table, open(A.slots, "w"), indent=1)
        print(f"slot table written to {A.slots} -- next run starts on the far "
              f"side of these.")

    print("\nREAD: a CLOSED level is a valid alias. It is closed under RUN only.")
    print("An OPEN level is where the surface stops being sufficient, i.e. where")
    print("repair requires the interior. Without Fix a system has two states.")
    bar("=")


if __name__ == "__main__":
    main()
