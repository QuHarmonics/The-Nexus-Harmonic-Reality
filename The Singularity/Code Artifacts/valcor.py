from sympy import Poly, factor_list, symbols, ZZ, factorint, Rational
from measure import rank_int

t = symbols('t')


def valuation_corank(b, n):
    """Rows = irreducible Q-orbits of b - t^n, cols = primes, entries = ord_p(g(1)/g(0))."""
    _, facs = factor_list(Poly(b - t**n, t, domain=ZZ))
    norms = []
    for f, mult in facs:
        p = Poly(f, t)
        norms.append(Rational(int(p.eval(1)), int(p.eval(0))))
    primes = set()
    for q in norms:
        primes |= set(factorint(q.p)) | set(factorint(q.q))
    primes = sorted(primes)
    M = []
    for q in norms:
        fp, fq = factorint(q.p), factorint(q.q)
        M.append([fp.get(pr, 0) - fq.get(pr, 0) for pr in primes])
    return len(M) - rank_int(M), norms, primes
