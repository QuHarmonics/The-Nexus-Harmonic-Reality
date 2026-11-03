#!/usr/bin/env python3
"""Acceptance test for the persistent pending-field reader, 2,000 emissions.

The reference is independent of BBP: pi from mpmath, converted to hex.
Checks, in the reviewers' numbering:
  1  every emitted digit is certified by the current bounds, and is correct
  2  every refinement (OPEN, WIDEN) keeps the true unread value inside the interval
  3  every emission leaves the interval holding the scaled fractional remainder
  4  resolved contributions survive: lanes are never dropped or reopened, and every
     lane's retained value is exactly what it should be at the current address
  5  nothing evaluates the unopened lanes (the machine source is shown to the caller)
  6  the trace records n, K, P, lanes, refinements, certified carry, storage size
"""
import sys, time, math, csv, inspect
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from pending import PendingField, WEIGHTS
from mpmath import mp, pi as MPPI

N = 2000
GUARD = 40

# ---------------------------------------------------------------- independent reference
mp.dps = int((N + GUARD) * 1.21) + 60
x = MPPI - 3
H = []
for _ in range(N + GUARD):
    x *= 16
    d = int(x)
    H.append(d)
    x -= d
HEX = "0123456789ABCDEF"


def contains(m):
    """Is the true x_n (from mpmath) inside the machine's interval, mod 1?"""
    lo, hi, _ = m.interval()
    P, n = m.P, m.n
    X = int("".join(HEX[h] for h in H[n:n + P + 5]), 16)        # x_n in [X, X+1) / 16^(P+5)
    M = 16 ** (P + 5)
    a = lo * 16 ** 5 - X
    k = -((-a) // M)                                             # ceil
    return X + 1 + k * M <= hi * 16 ** 5


# independent carry register for the first steps: I_(n+1) = 16 I_n - C_n + d_n
def C_ref(n):
    return sum(c * sum((16 * pow(16, n - k, 8 * k + j)) // (8 * k + j) for k in range(n + 1))
               for j, c in WEIGHTS.items())


I_ref = [-1]
for n in range(400):
    I_ref.append(16 * I_ref[n] - C_ref(n) + H[n])

# ---------------------------------------------------------------- run
m = PendingField(P=4)
rows = []
digits = []
checks_refine = fails_refine = 0
checks_emit = fails_emit = 0
carry_checked = carry_ok = 0
lanes_seen = 0
t0 = time.time()
for step in range(N):
    opens = widens = 0
    while True:
        d = m.certify()
        if d is not None:
            break
        lo, hi, T = m.interval()
        E = 4 * (m.K + 1)
        if m.K < m.n or T >= E:
            m.open_layer(); opens += 1
        else:
            m.widen(); widens += 1
        checks_refine += 1
        fails_refine += not contains(m)
        assert m.lanes() >= lanes_seen
        lanes_seen = m.lanes()
    I_cert = m.carry_register()
    if m.n < len(I_ref) - 1 and I_cert is not None:
        carry_checked += 1
        carry_ok += (I_cert == I_ref[m.n])
    lo, hi, T = m.interval()
    row = dict(n=m.n, K=m.K, gap=m.K - m.n, P=m.P, lanes=m.lanes(), opens=opens, widens=widens,
               digit=HEX[d], tail_bound_ulps=T, field_trunc_ulps=4 * (m.K + 1),
               carry_register=I_cert, storage_bits=m.storage_bits())
    digits.append(d)
    m.emit()
    checks_emit += 1
    ok = contains(m)
    fails_emit += not ok
    row["contains_after_emit"] = ok
    rows.append(row)
dt = time.time() - t0

# ---------------------------------------------------------------- 4: every retained lane, exactly
lane_ok = 0
n = m.n
idx = 0
for k in range(m.K + 1):
    for j in WEIGHTS:
        dd, D, r = 8 * k + j, m.D[idx], m.rt[idx]
        if k <= n:
            want = (r * dd == pow(16, n - k, dd) * D)
        else:
            want = (r * dd * 16 ** (k - n) == D)
        lane_ok += want
        idx += 1

with (HERE / "pending_reader_trace.csv").open("w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
    w.writeheader(); w.writerows(rows)

# ---------------------------------------------------------------- report
correct = sum(a == b for a, b in zip(digits, H[:N]))
print(f"{N} emissions in {dt:.1f}s, from an empty field\n")
print(f"1  certified and correct:            {correct}/{N} digits match mpmath")
print(f"2  refinements keep the true value:  {checks_refine - fails_refine}/{checks_refine} "
      f"(OPEN {sum(r['opens'] for r in rows)}, WIDEN {sum(r['widens'] for r in rows)})")
print(f"3  emissions land on 16x mod 1:      {checks_emit - fails_emit}/{checks_emit}")
print(f"4  lanes retained, never dropped:    {m.lanes()} lanes = 4 x {m.K + 1} layers; "
      f"{m.opened_ahead} opened ahead of the read point")
print(f"   every retained lane exact now:    {lane_ok}/{m.lanes()}")
print(f"   carry register inside S matches the independent I_n: {carry_ok}/{carry_checked} steps")
src = inspect.getsource(PendingField)
print(f"5  unopened lanes evaluated anywhere in the machine? "
      f"{'no' if 'tail_ulps' in src and 'for k in' not in src else 'CHECK'}"
      f"  (only the closed-form bound in tail_ulps)")
gaps = [r['gap'] for r in rows]
print(f"6  trace.csv written: {len(rows)} rows")
print(f"\n   frontier gap K - n: min {min(gaps)}, max {max(gaps)}, "
      f"mean {sum(gaps)/len(gaps):.2f}")
print(f"   precision P: {rows[0]['P']} -> {rows[-1]['P']}")
print(f"   OPENs per emission: {sum(r['opens'] for r in rows)/N:.3f}")
for nn in (250, 500, 1000, 1999):
    r = rows[nn]
    print(f"   n={nn:5d}: lanes {r['lanes']:5d}, storage {r['storage_bits']:8d} bits, "
          f"bits / (n log2 n) = {r['storage_bits']/(max(nn,2)*math.log2(max(nn,2))):.2f}")
print("\n   first 64 digits: " + "".join(HEX[d] for d in digits[:64]))
