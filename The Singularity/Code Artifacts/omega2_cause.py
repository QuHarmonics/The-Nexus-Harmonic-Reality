"""
Where do the phantom elements at (64,24) come from, and what is the correct group?

rho = b^(1/n) = 64^(1/24) = 2^(1/4).  So rho^2 = sqrt(2), and sqrt(2) ALREADY LIVES
IN Q(zeta_24)  (sqrt2 = zeta_8 + zeta_8^-1 = zeta_24^3 + zeta_24^21).

That is a relation BETWEEN the radical and the cyclotomic part.  The orbit filter
never sees it: it only checks that j -> a*j+c permutes each factor's roots.  But a
genuine automorphism must send sqrt(2) to the same place whether you compute it
as rho^2 or as zeta_24^3 + zeta_24^21.  Those two routes must agree.

  route 1 (radical):  sigma(rho^2) = (rho*zeta^c)^2 = sqrt2 * zeta_n^(2c)
  route 2 (cyclotomic): sigma(sqrt2) = zeta_8^a + zeta_8^-a = chi(a)*sqrt2,
                        chi(a) = +1 if a = +-1 mod 8, -1 if a = +-3 mod 8

  => constraint   zeta_n^(2c) = chi(a)

Generally: e=2 exactly when 8|n and n'=n/gcd(m,n) is even.  Then m'=m/gcd is odd,
u = rho^(n'/2) = 2^((m'-1)/2) * sqrt2 is a rational multiple of sqrt2, and the
same two-route argument gives

  zeta_n^(c*n'/2) = chi(a).
"""
from sympy import totient, gcd, Poly, factor_list, symbols, ZZ
import mpmath as mp
from omega2_group import true_degree, filter_group

mp.mp.dps = 60
t = symbols('t')


def chi(a):
    """sigma_a(sqrt2)/sqrt2 for sigma_a: zeta_8 -> zeta_8^a."""
    return 1 if a % 8 in (1, 7) else -1


def true_group(b, n):
    """Affine pairs surviving orbit preservation AND the radical/cyclotomic
    compatibility relation when one exists (e=2)."""
    m = b.bit_length() - 1
    g = int(gcd(m, n))
    nprime = n // g
    e = 2 if (n % 8 == 0 and nprime % 2 == 0) else 1
    G_filt, orbits = filter_group(b, n)
    if e == 1:
        return G_filt, G_filt, orbits, e
    k = nprime // 2                      # exponent making rho^k ~ sqrt2
    G_true = []
    for (a, c) in G_filt:
        # zeta_n^(c*k) must equal chi(a) exactly (as +-1)
        ang = (c * k) % n
        if ang == 0 and chi(a) == 1:
            G_true.append((a, c))
        elif ang * 2 == n and chi(a) == -1:   # zeta_n^(n/2) = -1
            G_true.append((a, c))
    return G_true, G_filt, orbits, e


FRAMES = [
    (64, 6), (16, 8), (1024, 10), (32, 10), (64, 12), (256, 16),
    (64, 18), (262144, 18), (1048576, 20),
    (16, 24), (64, 24), (4096, 24), (16777216, 24),
]

print(f"{'frame':>18} {'e':>2} {'[K:Q]':>7} {'|G_filt|':>9} {'|G_true|':>9} {'match':>8}")
print("-" * 62)
bad = []
for b, n in FRAMES:
    m = b.bit_length() - 1
    deg, nprime, e = true_degree(m, n)
    G_true, G_filt, orbits, e2 = true_group(b, n)
    ok = (len(G_true) == deg)
    if not ok:
        bad.append((b, n, deg, len(G_true)))
    print(f"{str((b,n)):>18} {e:>2} {deg:>7} {len(G_filt):>9} {len(G_true):>9} "
          f"{'yes' if ok else 'NO':>8}")

print()
if bad:
    print("MISMATCHES:", bad)
else:
    print("Corrected group order matches the exact field degree on every frame.")

# Exhibit the phantom elements at (64,24) explicitly.
print("\n--- (64,24): the phantom coset ---")
G_true, G_filt, orbits, e = true_group(64, 24)
phantom = sorted(set(G_filt) - set(G_true))
print(f"|G_filt| = {len(G_filt)}, |G_true| = {len(G_true)}, phantom = {len(phantom)}")
print("phantom (a,c) pairs:", phantom)
print()
# show one phantom failing concretely
a, c = phantom[0]
rho = mp.mpf(64) ** (mp.mpf(1) / 24)
z = mp.e ** (2j * mp.pi / 24)
lhs = (rho * z**c) ** 2           # sigma(rho)^2  -- route 1
rhs = z**(3 * a) + z**(21 * a)    # sigma(sqrt2)  -- route 2
print(f"phantom (a,c)=({a},{c}):")
print(f"  sigma(rho)^2      = {mp.nstr(lhs, 12)}")
print(f"  sigma(zeta+zeta^-1)= {mp.nstr(rhs, 12)}")
print(f"  disagree by       = {mp.nstr(abs(lhs-rhs), 12)}   <- not a field automorphism")
