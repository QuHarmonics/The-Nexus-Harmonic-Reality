"""
Direct measurement of dim K_{b,n} -- ground truth, independent of any selector.

S_r = b * int_0^1 t^(r-1)/(b - t^n) dt,  r = 1..n

Closed form (derived, then checked against quadrature):
    b - t^n = -prod_j (t - alpha_j),  alpha_j = rho * zeta^j,  rho = b^(1/n)
    1/(b - t^n) = -sum_j alpha_j / (n b (t - alpha_j))
    int_0^1 t^(r-1)/(t-alpha) dt = sum_{i=0}^{r-2} alpha^(r-2-i)/(i+1) + alpha^(r-1) ln(1-1/alpha)
    the polynomial part sums to  sum_j alpha_j^s = n rho^s [n | s]  which VANISHES for
    1 <= s <= n-1, so it drops out entirely, leaving

    S_r = -(1/n) sum_j alpha_j^r ln(1 - 1/alpha_j)

Branch is safe: rho > 1 so |zeta^-j / rho| < 1, hence Re(1 - zeta^-j/rho) > 0 and
every beta_j sits in the right half plane -- principal log, no cut crossing.

Detector calibration (from the session instrument log: five failures, all detector):
  - exact integer LLL, no floating Gram-Schmidt
  - REPLICATION at two precisions; a relation counts only if it survives both
  - acceptance requires the residual to SHRINK with precision (a true relation's
    residual tracks the precision floor; a lattice artifact does not)
"""
from fractions import Fraction
import mpmath as mp


# ---------- shell integrals ----------

def shells(b, n, dps):
    mp.mp.dps = dps
    rho = mp.mpf(b) ** (mp.mpf(1) / n)
    out = []
    for r in range(1, n + 1):
        tot = mp.mpc(0)
        for j in range(n):
            a = rho * mp.e ** (2j * mp.pi * j / n)
            tot += a**r * mp.log(1 - 1 / a)
        out.append(-tot / n)
    # imaginary parts must cancel
    assert max(abs(mp.im(v)) for v in out) < mp.mpf(10) ** (-(dps - 20)), "complex leak"
    return [mp.re(v) for v in out]


def check_against_quadrature(b, n, dps=40):
    mp.mp.dps = dps
    cf = shells(b, n, dps)
    ok = True
    for r in range(1, n + 1):
        q = b * mp.quad(lambda t: t ** (r - 1) / (b - t**n), [0, 1])
        if abs(q - cf[r - 1]) > mp.mpf(10) ** (-(dps - 10)):
            ok = False
    return ok


# ---------- exact integer LLL ----------

def lll(basis, delta=Fraction(99, 100)):
    B = [list(map(int, row)) for row in basis]
    n_ = len(B)

    def gso(B):
        Bs, mu = [], [[Fraction(0)] * n_ for _ in range(n_)]
        for i in range(n_):
            v = [Fraction(x) for x in B[i]]
            for j in range(i):
                den = sum(x * x for x in Bs[j])
                if den == 0:
                    mu[i][j] = Fraction(0)
                    continue
                mu[i][j] = sum(Fraction(B[i][k]) * Bs[j][k] for k in range(len(v))) / den
                v = [v[k] - mu[i][j] * Bs[j][k] for k in range(len(v))]
            Bs.append(v)
        return Bs, mu

    Bs, mu = gso(B)
    k = 1
    while k < n_:
        for j in range(k - 1, -1, -1):
            if abs(mu[k][j]) > Fraction(1, 2):
                q = int(mu[k][j] + Fraction(1, 2)) if mu[k][j] > 0 else -int(-mu[k][j] + Fraction(1, 2))
                if q:
                    B[k] = [B[k][i] - q * B[j][i] for i in range(len(B[k]))]
                    Bs, mu = gso(B)
        nk = sum(x * x for x in Bs[k])
        nk1 = sum(x * x for x in Bs[k - 1])
        if nk >= (delta - mu[k][k - 1] ** 2) * nk1:
            k += 1
        else:
            B[k], B[k - 1] = B[k - 1], B[k]
            Bs, mu = gso(B)
            k = max(k - 1, 1)
    return B


def find_relations(S, dps, guard=30, maxcoeff=10**7):
    """Integer vectors e with sum e_r S_r ~ 0.  Returns (vector, residual) list."""
    n_ = len(S)
    mp.mp.dps = dps
    N = mp.mpf(10) ** (dps - guard)
    rows = []
    for i in range(n_):
        row = [0] * n_ + [int(mp.nint(N * S[i]))]
        row[i] = 1
        rows.append(row)
    red = lll(rows)
    out = []
    for row in red:
        e = row[:n_]
        if all(x == 0 for x in e):
            continue
        if max(abs(x) for x in e) > maxcoeff:
            continue
        res = abs(sum(mp.mpf(e[i]) * S[i] for i in range(n_)))
        out.append((tuple(e), res))
    return out


def rank_int(vs):
    if not vs:
        return 0
    rows = [[Fraction(x) for x in v] for v in vs]
    r, cols = 0, len(rows[0])
    for c in range(cols):
        p = next((i for i in range(r, len(rows)) if rows[i][c] != 0), None)
        if p is None:
            continue
        rows[r], rows[p] = rows[p], rows[r]
        pv = rows[r][c]
        for i in range(len(rows)):
            if i != r and rows[i][c] != 0:
                f = rows[i][c] / pv
                rows[i] = [rows[i][k] - f * rows[r][k] for k in range(cols)]
        r += 1
        if r == len(rows):
            break
    return r


def measure_dim(b, n, dps_lo=140, dps_hi=220):
    """Replicated measurement: keep only relations confirmed at BOTH precisions
    with residuals that shrink as precision rises."""
    S_lo = shells(b, n, dps_lo)
    S_hi = shells(b, n, dps_hi)
    cand_lo = find_relations(S_lo, dps_lo)
    keep = []
    mp.mp.dps = dps_hi
    for e, res_lo in cand_lo:
        res_hi = abs(sum(mp.mpf(e[i]) * S_hi[i] for i in range(n)))
        floor_lo = mp.mpf(10) ** (-(dps_lo - 40))
        floor_hi = mp.mpf(10) ** (-(dps_hi - 40))
        if res_lo < floor_lo and res_hi < floor_hi:
            keep.append(e)
    return rank_int(keep), keep


if __name__ == "__main__":
    print("quadrature cross-check of the closed form:")
    for b, n in [(64, 6), (16, 8), (64, 12)]:
        print(f"  ({b},{n}): {check_against_quadrature(b, n)}")

    print("\nknown-answer checks:")
    mp.mp.dps = 60
    S6 = shells(64, 6, 60)
    z6 = (16, -24, -8, -6, 1, 0)
    print(f"  z6.S for (64,6)     = {mp.nstr(sum(z6[i]*S6[i] for i in range(6)), 8)}  (want 0)")
    S8 = shells(16, 8, 60)
    v8 = (4, 0, 0, -2, -1, -1, 0, 0)
    print(f"  BBP.S for (16,8)    = {mp.nstr(sum(v8[i]*S8[i] for i in range(8)), 20)}")
    print(f"  pi                  = {mp.nstr(mp.pi, 20)}")
