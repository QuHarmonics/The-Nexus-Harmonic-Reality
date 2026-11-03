"""
Omega-2: Is the Galois group used by the branch selector the ACTUAL Galois group?

Two independent computations per frame (b, n), b = 2^m:

(A) TRUE DEGREE  [K:Q] where K = Q(zeta_n, b^(1/n)) is the splitting field of b - t^n.
    Exact, from theory:
      rho = 2^(m/n); g = gcd(m,n); n' = n/g;  Q(rho) = Q(2^(1/n')).
      K = Q(zeta_n, 2^(1/n')).  Since n' | n, mu_{n'} subset Q(zeta_n), so the
      extension is Kummer:
        [K : Q(zeta_n)] = n' / e,  e = largest divisor of n' with 2 in Q(zeta_n)^{*e}.
      For odd prime p:  2^(1/p) in Q(zeta_n) would put the non-Galois field
        Q(2^(1/p)) inside an abelian field -> impossible.  So e is a power of 2.
      2^(1/4) likewise generates a non-Galois quartic -> not in any cyclotomic field.
      sqrt(2) in Q(zeta_n)  <=>  8 | n.
      Hence e = 2 if (8 | n and 2 | n') else 1.
      [K:Q] = phi(n) * n'/e.

(B) FILTER GROUP  the necessary-condition group the session actually used:
    every Q-automorphism sends root alpha_j = rho*zeta_n^j to alpha_{a*j+c},
    a in (Z/n)*, c in Z/n.  Galois must preserve each irreducible Q-factor's
    root set SETWISE.  Collect all affine (a,c) that do.  |Aff| = n*phi(n).

If |G_filter| > [K:Q] the filter is too permissive: it admits maps that are not
field automorphisms, and any selector filtered by "all sigma in G" was over-
constraining with phantom elements.  If equal, the filter is exact.
"""
from sympy import Poly, factor_list, symbols, totient, gcd, ZZ
import mpmath as mp

mp.mp.dps = 80
t = symbols('t')


def true_degree(m, n):
    """[Q(zeta_n, 2^(m/n)) : Q], exact."""
    g = int(gcd(m, n))
    nprime = n // g
    e = 2 if (n % 8 == 0 and nprime % 2 == 0) else 1
    return int(totient(n)) * (nprime // e), nprime, e


def root_index_orbits(b, n):
    """Partition {0..n-1} by which irreducible Q-factor of b - t^n owns alpha_j."""
    rho = mp.mpf(b) ** (mp.mpf(1) / n)
    roots = [rho * mp.e ** (2j * mp.pi * j / n) for j in range(n)]
    _, facs = factor_list(Poly(b - t**n, t, domain=ZZ))
    orbits = []
    for f, mult in facs:
        p = Poly(f, t)
        coeffs = [mp.mpf(int(c)) for c in p.all_coeffs()]
        members = []
        for j, r in enumerate(roots):
            val = mp.mpf(0)
            for c in coeffs:
                val = val * r + c
            if abs(val) < mp.mpf(10) ** (-40) * max(1, abs(rho) ** p.degree()):
                members.append(j)
        assert len(members) == p.degree(), (f, len(members), p.degree())
        orbits.append(frozenset(members))
    assert sum(len(o) for o in orbits) == n
    return orbits


def filter_group(b, n):
    """All affine (a,c) on Z/n preserving every factor root-set setwise."""
    orbits = root_index_orbits(b, n)
    units = [a for a in range(1, n) if int(gcd(a, n)) == 1]
    G = []
    for a in units:
        for c in range(n):
            if all(frozenset((a * j + c) % n for j in o) == o for o in orbits):
                G.append((a, c))
    return G, orbits


FRAMES = [
    (64, 6), (16, 8), (1024, 10), (32, 10), (64, 12), (256, 16),
    (64, 18), (262144, 18), (1048576, 20),
    (16, 24), (64, 24), (4096, 24), (16777216, 24),
]

print(f"{'frame (b,n)':>18} {'m':>3} {'n-prime':>8} {'e':>2} "
      f"{'|Aff|':>7} {'[K:Q]':>7} {'|G_filt|':>9} {'verdict':>10}")
print("-" * 78)

rows = []
for b, n in FRAMES:
    m = b.bit_length() - 1
    assert 2**m == b
    deg, nprime, e = true_degree(m, n)
    G, orbits = filter_group(b, n)
    aff = n * int(totient(n))
    if len(G) == deg:
        verdict = "EXACT"
    elif len(G) > deg:
        verdict = f"TOO BIG x{len(G)//deg if deg and len(G)%deg==0 else '?'}"
    else:
        verdict = "TOO SMALL"
    rows.append((b, n, m, nprime, e, aff, deg, len(G), verdict, orbits))
    print(f"{str((b,n)):>18} {m:>3} {nprime:>8} {e:>2} "
          f"{aff:>7} {deg:>7} {len(G):>9} {verdict:>10}")

print()
print("orbit degree profiles (irreducible Q-factors of b - t^n):")
for b, n, m, nprime, e, aff, deg, gf, verdict, orbits in rows:
    prof = sorted(len(o) for o in orbits)
    print(f"  {str((b,n)):>18}  {len(orbits)} orbits, degrees {prof}")
