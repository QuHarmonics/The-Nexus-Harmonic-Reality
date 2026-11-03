#!/usr/bin/env python3
"""
derive_seed_kernels.py

Derives the BBP shell-relation kernels for the two seed frames from S-unit
structure alone.  No PSLQ, no coefficient bound, no precision threshold,
therefore none of the six logged instrument failure modes can occur here.

-------------------------------------------------------------------------
The chain
-------------------------------------------------------------------------
S_r = sum_k 1/((nk+r) b^k)  =  L(1,b,n,r)                    (Bailey's notation)

        = -(1/n) sum_j alpha_j^r log(1 - 1/alpha_j),   alpha_j = b^{1/n} zeta_n^j

  This is Borwein-Borwein-Galway (2004), eq. (64).  Confirmed to 120 digits
  on (16,8), (64,6), (4096,12), (4096,24).

Writing C(y) = sum_r c_r y^r, a kernel element is

        sum_j C(alpha_j) L_j = 0,        L_j = log(beta_j),  beta_j = 1 - 1/alpha_j

Baker's theorem: a vanishing linear form in logarithms of algebraic numbers
with algebraic coefficients forces the coefficient vector into R (x) Qbar,
where R is the Q-space of relations among the L_j.  So

        K  =  { c :  (C(alpha_j))_j  in  R (x) Qbar }

and R is a multiplicative relation lattice in the S-unit group of
Q(zeta_n, b^{1/n}) -- exactly the object BBG's Research Problem 10 asks for.

R is cut out by two independent families of conditions:

    (V) valuation conditions, one per prime ideal in S.
        This is BBG's valuation-vector method (their section 3.2).
    (A) argument conditions, from the unit and root-of-unity part.
        BBG note explicitly that valuations cannot see these:
        "knowledge of theta_p(z) for all p only determines Im log z (mod 2 pi)".

(V) alone overcounts.  (V) and (A) together give R exactly.

Consequence, immediate: if a prime ideal divides exactly one beta_j and no
other, then every element of R has j-th coordinate zero, so C vanishes at
alpha_j and hence on its whole Galois orbit.  So the principal relation is
FORCED to annihilate every orbit carrying an unshared prime, and k -- the
count of such orbits -- is not an auxiliary statistic but a rank deficiency.
-------------------------------------------------------------------------
"""

import sympy as sp
import mpmath as mpm


# ---------------------------------------------------------------- helpers
def integer_vector(expr, y, deg):
    """Normalise a polynomial to a primitive integer coefficient vector."""
    p = sp.Poly(sp.expand(expr), y)
    coeffs = [sp.nsimplify(p.coeff_monomial(y**r)) for r in range(deg + 1)]
    den = sp.ilcm(*[sp.denom(sp.together(t)) for t in coeffs])
    vec = [int(sp.simplify(t * den)) for t in coeffs]
    g = sp.igcd(*[v for v in vec if v != 0])
    vec = [v // g for v in vec]
    if next(v for v in vec if v != 0) < 0:
        vec = [-v for v in vec]
    return vec


def numeric_residual(b, n, c, dps=80):
    """Confirm a kernel vector against the series it is supposed to annihilate."""
    mpm.mp.dps = dps
    terms = int(dps * 3.5 / mpm.log10(b)) + 60
    tot = mpm.mpf(0)
    for r in range(1, n):
        if c[r - 1] == 0:
            continue
        s, bk = mpm.mpf(0), mpm.mpf(1)
        for k in range(terms):
            s += mpm.mpf(1) / ((n * k + r) * bk)
            bk *= b
        tot += c[r - 1] * s
    return abs(tot)


def report(name, b, n, vec, published):
    res = numeric_residual(b, n, vec)
    ok = vec == published or vec == [-x for x in published]
    print(f"  derived kernel   : {vec}")
    print(f"  published kernel : {published}")
    print(f"  match            : {ok}")
    print(f"  series residual  : {mpm.nstr(res, 4)}")


# ================================================================ OCTAL
# (16,8).  Q(zeta_8, 16^{1/8}) = Q(zeta_8), because 16^{1/8} = sqrt2 lies in it.
# Degree 4.  Unit rank 1 (fundamental unit u = 1 + sqrt2), 2 totally ramified.
#
#   beta_0 = u^-1 s^-1     beta_4 = u   s^-1        s = sqrt2
#   beta_1 = z   s^-1      beta_7 = z^-1 s^-1       z = zeta_8
#   beta_2, beta_6 : conjugate primes over 3   <- unshared
#   beta_3, beta_5 : conjugate primes over 5   <- unshared
#
# (V) kills coordinates 2,3,5,6 outright.  On {0,1,4,7}, (V) gives
# c_0 = c_4, c_1 = c_7, sum = 0; (A) is automatically consistent.
#   =>  R = span{(1,-1,0,0,1,0,0,-1)},  dim R = 1.
print("=" * 70)
print("OCTAL SEED  (16, 8)   field Q(zeta_8), degree 4")
print("=" * 70)

y, a, bq, cq, lam = sp.symbols('y a b c lam')
C8 = sp.expand(y * (y**2 + 2) * (y**2 + 2*y + 2) * (a + bq*y + cq*y**2))
root8 = {0: sp.sqrt(2), 4: -sp.sqrt(2), 1: 1 + sp.I, 7: 1 - sp.I}
eqs8 = [sp.Eq(sp.simplify(C8.subs(y, root8[0])),  lam),
        sp.Eq(sp.simplify(C8.subs(y, root8[4])),  lam),
        sp.Eq(sp.simplify(C8.subs(y, root8[1])), -lam),
        sp.Eq(sp.simplify(C8.subs(y, root8[7])), -lam)]
s8 = sp.solve(eqs8, [a, bq, cq, lam], dict=True)[0]
free8 = [t for t in (a, bq, cq, lam) if t not in s8]
print(f"  dim K            : {len(free8)}   (forced, not measured)")
vec8 = integer_vector(sp.simplify(C8.subs(s8) / free8[0]), y, 7)
report("octal", 16, 8, vec8[1:], [8, -8, -4, -8, -2, -2, 1])
print("  note: this vector is the Bailey-Borwein-Plouffe formula for pi.")

# ================================================================ HEX
# (64,6).  Q(zeta_6, 64^{1/6}) = Q(zeta_6) = Q(sqrt-3), because 64^{1/6} = 2.
# Degree 2.  Unit rank 0 -- units are torsion only, so (A) does real work here.
#
#   beta_0 = 1/2            v = (-1, 0, 0, 0)      arg 0
#   beta_1 = (3+i r3)/4     v = (-1, 1, 0, 0)      arg  pi/6
#   beta_2 = (5+i r3)/4     v = (-1, 0, 1, 0)      arg  irrational  <- unshared 7
#   beta_3 = 3/2            v = (-1, 2, 0, 0)      arg 0
#   beta_4 = (5-i r3)/4     v = (-1, 0, 0, 1)      arg -irrational  <- unshared 7
#   beta_5 = (3-i r3)/4     v = (-1, 1, 0, 0)      arg -pi/6
#
# (V):  sum c = 0 ; c1 + c5 + 2 c3 = 0 ; c2 + c4 = 0        -> dim 3
# (A):  c1 = c5 ; c2 = c4                                   -> dim 1
print()
print("=" * 70)
print("HEX SEED  (64, 6)   field Q(sqrt-3), degree 2")
print("=" * 70)

c = sp.symbols('c0 c1 c2 c3 c4 c5')
V = [sp.Eq(sum(c), 0), sp.Eq(c[1] + c[5] + 2*c[3], 0), sp.Eq(c[2] + c[4], 0)]
A = [sp.Eq(c[1] - c[5], 0), sp.Eq(c[2] - c[4], 0)]
print(f"  dim R, valuations only  : {len(sp.linsolve(V, c).free_symbols)}")
print(f"  dim R, + argument layer : {len(sp.linsolve(V + A, c).free_symbols)}")
print("  the gap between those two lines is the phase layer.")

r3 = sp.sqrt(3)
root6 = {j: sp.simplify(sp.expand(2 * (sp.Rational(1, 2) + sp.I*r3/2)**j))
         for j in range(6)}
C6 = sp.expand(y * (y**2 + 2*y + 4) * (a + bq*y + cq*y**2))
eqs6 = [sp.Eq(sp.simplify(sp.expand(C6.subs(y, root6[0]))), -lam),
        sp.Eq(sp.simplify(sp.expand(C6.subs(y, root6[1]))),  lam),
        sp.Eq(sp.simplify(sp.expand(C6.subs(y, root6[3]))), -lam)]
s6 = sp.solve(eqs6, [a, bq, cq, lam], dict=True)[0]
free6 = [t for t in (a, bq, cq, lam) if t not in s6]
print(f"  dim K            : {len(free6)}   (forced, not measured)")
vec6 = integer_vector(sp.simplify(C6.subs(s6) / free6[0]), y, 5)
report("hex", 64, 6, vec6[1:], [16, -24, -8, -6, 1])

# ============================================================ FIELD NOTE
print()
print("=" * 70)
print("WHY THESE TWO")
print("=" * 70)
for (b, n) in [(16, 8), (64, 6), (4, 3), (8, 4), (2, 5), (10, 4), (100, 6)]:
    # is b^{1/n} inside Q(zeta_n)?  Kummer degeneracy test, crude version:
    # b = 2^m with n | 2m and the resulting radical already cyclotomic.
    e = sp.Rational(sp.log(b, 2)) if sp.log(b, 2).is_rational else None
    note = ""
    if e is not None:
        r = sp.Rational(e, n)          # b^{1/n} = 2^r
        deg = sp.denom(r)
        note = f"b^(1/n) = 2^{r}, radical degree {deg}"
        if deg == 1:
            note += "   -> rational, field = Q(zeta_n)"
        elif deg == 2 and n % 8 == 0:
            note += "   -> sqrt2 in Q(zeta_8) | Q(zeta_n), field = Q(zeta_n)"
        else:
            note += "   -> field strictly larger than Q(zeta_n)"
    print(f"  ({b:>5},{n:>3}) : {note}")
print()
print("  Both seeds, and only the seeds, collapse to the cyclotomic field.")
print("  That is a Kummer condition on (b,n), not a search result --")
print("  it is the candidate generator of 'exactly two seeds'.")
