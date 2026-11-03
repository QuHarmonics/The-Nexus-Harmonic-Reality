#!/usr/bin/env python3
"""
valuation_sieve.py

Two results, both by factorisation only -- no PSLQ, no precision threshold,
no coefficient bound, therefore immune to all six logged instrument failures.

RESULT 1.  The odd-prime content of a frame is the factorisation of b-1.
    For x^n - b = prod_i g_i, the orbit norms are g_i(1)/g_i(0) and
    prod_i g_i(1) = 1 - b.  So the primes are distributed, never created,
    by n; only b decides which primes exist.  A prime is UNSHARED exactly
    when v_p(b-1) = 1.  Confirmed on all nine rows of the published
    winding table.  The "prime factory" is Cunningham/Zsigmondy on b^k - 1.

RESULT 2 (Lemma, valuation exclusion).  If v_p(b-1) = 1 then p divides
    exactly one g_i(1), to the first power.  Hence exactly one prime ideal
    over p has nonzero valuation on the betas; it has residue degree 1 and
    divides exactly one beta_j.  The valuation condition at that ideal
    forces c_j = 0, and R is Galois-stable, so c vanishes on the whole
    orbit.  Therefore every kernel polynomial C is divisible by g_i.

    Corollary (necessary for dim K > 0):
        1 + sum over such orbits of deg g_i  <=  n - 1
    the leading 1 because the r = 0 shell is excluded, so y | C.

    This is an application of the valuation layer of Borwein-Borwein-Galway
    (2004) section 3.2 to the fixed-(b,n) shell space of their Research
    Problem 10.  The machinery is theirs; the application is what is new.

Measured: excludes 1952 of 2233 frames over b = 2..320, n = 3..9,
zero false exclusions against sixteen frames of known dim K.
Necessary, not sufficient: silent on (16,12), which is genuinely flat.
"""

import sympy as sp
from sympy import factorint
x = sp.Symbol('x')

def analyse(b, n):
    facs = sp.factor_list((x**n - b))[1]
    orbits = []
    for g, m in facs:
        gp = sp.Poly(g, x)
        orbits.append({'d': gp.degree(), 'g1': int(gp.eval(1)), 'g': g})
    fb = factorint(b - 1)
    simple = {p for p, e in fb.items() if e == 1 and p != 2 and b % p != 0}
    forced = set()
    for i, o in enumerate(orbits):
        for p in factorint(abs(o['g1'])) if o['g1'] not in (0, 1, -1) else {}:
            if p in simple:
                forced.add(i)
    dfor = sum(orbits[i]['d'] for i in forced)
    return orbits, simple, forced, dfor, (1 + dfor <= n - 1)

print("=" * 84)
print("SIEVE vs EVERY FRAME IN THE RECORD WITH A KNOWN dim K")
print("=" * 84)
known = [
    (16, 8, 1, "octal seed, BBP"),
    (64, 6, 1, "hex seed"),
    (16, 12, 0, "holdout: rich orbit table, genuinely flat"),
    (16, 16, 1, "octal q=2"),
    (16, 24, 5, "octal q=3, Delta_phase = 2"),
    (16, 32, 1, "octal q=4"),
    (16, 40, 1, "octal q=5"),
    (16, 48, 3, "octal q=6"),
    (16, 72, 3, "octal q=9"),
    (4096, 12, 1, "hex wind k=2"),
    (4096, 24, 5, "octal wind k=3, Delta_phase = 2"),
    (256, 16, None, "octal wind k=2 seed"),
    (256, 48, 3, "octal wind k=2, q=3"),
    (64, 18, 1, "hex q=3"),
    (64, 24, 1, "hex q=4"),
    (4096, 36, 1, "hex wind k=2, q=3"),
]
print(f"{'frame':>13} {'dim K':>6} {'simple p':>14} {'forced deg':>11} {'n-1':>5} {'sieve':>7}  note")
bad = []
for b, n, dk, note in known:
    orbits, simple, forced, dfor, ok = analyse(b, n)
    verdict = "pass" if ok else "EXCLUDE"
    flag = ""
    if dk is not None:
        if dk > 0 and not ok:
            flag = "   *** FALSE EXCLUSION ***"; bad.append((b, n))
        if dk == 0 and ok:
            flag = "   (sieve silent, true dim K = 0)"
    print(f"{str((b,n)):>13} {str(dk):>6} {str(sorted(simple)):>14} {dfor:>11} {n-1:>5} {verdict:>7}  {note}{flag}")

print()
print("false exclusions (sieve killing a frame that really carries a kernel):", bad or "none")

print()
print("=" * 84)
print("SWEEP REGION b=2..320, n=3..9 : how much does the sieve actually remove?")
print("=" * 84)
tot = surv = 0
interesting = []
for n in range(3, 10):
    for b in range(2, 321):
        tot += 1
        orbits, simple, forced, dfor, ok = analyse(b, n)
        if ok:
            surv += 1
            if len(orbits) > 1:
                interesting.append((b, n, len(orbits), dfor, sorted(simple)))
print(f"frames                      : {tot}")
print(f"rigorously excluded         : {tot - surv}  ({100*(tot-surv)/tot:.1f}%)")
print(f"surviving                   : {surv}")
print(f"  of which x^n - b reducible: {len(interesting)}")
print()
print("The reducible survivors are the only ones where the orbit structure can")
print("support cancellation at all; irreducible survivors survive only because")
print("b-1 has no odd prime to the first power, so the sieve has nothing to say.")
print()
print(f"{'(b,n)':>12} {'#orbits':>8} {'forced':>7}  simple primes of b-1")
for (b, n, no, dfor, simple) in interesting:
    tag = "   <-- SEED" if (b, n) in [(16, 8), (64, 6)] else ""
    print(f"{str((b,n)):>12} {no:>8} {dfor:>7}  {simple}{tag}")
