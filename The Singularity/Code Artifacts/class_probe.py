"""Per-class probe: does residue class c mod q carry a relation?

Observed on every subdivision frame so far, relations are CLASS-PURE -- each
relation is supported entirely inside one residue class r = c (mod q).  So the
question "does class c close?" can be asked on the n/q shells of that class alone
instead of on all n.

That drops the PSLQ dimension from n to n/q, which is the difference between a
dimension-40 run at 410 digits (kept getting killed) and a dimension-8 run where
a 1e12 coefficient bound is cheap.  This directly discharges the bound caveat on
(16,40): the earlier maxcoeff=1e5 is replaced by 1e12 on the classes that matter.

Limitation, stated: this cannot see relations spanning several classes.  Class
purity holds for the observed SUBDIVISION frames; it does NOT hold for winding
frames like (4096,24), whose relations spread across positions.  So this probe is
valid for subdivision frames only, and full-dimension PSLQ remains the arbiter.
"""
import mpmath as mp
from measure import shells


def class_probe(b, n, q, dps=320, maxcoeff=10**12):
    """For each residue class mod q, test the sub-vector of shells for a relation."""
    S = shells(b, n, dps)
    Sv = shells(b, n, dps + 140)
    out = {}
    for c in range(q):
        idx = [r - 1 for r in range(1, n + 1) if r % q == c % q]
        mp.mp.dps = dps
        vals = [S[i] for i in idx]
        try:
            r = mp.pslq(vals, tol=mp.mpf(10) ** (-(dps - 50)),
                        maxcoeff=maxcoeff, maxsteps=60000)
        except Exception:
            r = None
        if r and any(r):
            mp.mp.dps = dps + 140
            res = abs(sum(mp.mpf(r[k]) * Sv[idx[k]] for k in range(len(idx))))
            ok = res < mp.mpf(10) ** (-(dps + 140 - 70))
            out[c] = (tuple(int(x) for x in r), ok, res)
        else:
            out[c] = (None, False, None)
    return out


CASES = [
    ("oct q=3 -> (16,24)", 16, 24, 3, "classes 0,1,2 should ALL carry"),
    ("hex q=4 -> (64,24)", 64, 24, 4, "class 0 only"),
    ("oct q=4 -> (16,32)", 16, 32, 4, "unknown"),
    ("oct q=5 -> (16,40)", 16, 40, 5, "THE DISCRIMINATOR"),
    ("hex q=3 -> (64,18)", 64, 18, 3, "class 0 only"),
]

for name, b, n, q, expect in CASES:
    res = class_probe(b, n, q)
    carry = sorted(c for c, (v, ok, _) in res.items() if ok)
    print(f"{name:>22}  classes carrying: {carry}   [{expect}]", flush=True)
    for c in sorted(res):
        v, ok, rr = res[c]
        if ok:
            print(f"      class {c}: maxc={max(abs(x) for x in v):>7}  {v}", flush=True)
    print(flush=True)
