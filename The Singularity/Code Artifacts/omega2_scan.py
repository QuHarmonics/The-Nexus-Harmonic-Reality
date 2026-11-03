"""How often does the orbit filter over-count?  Scan b = 2^m, n over a wide grid."""
from sympy import totient, gcd
from omega2_group import true_degree, filter_group
from omega2_cause import true_group

rows = []
for n in range(4, 31):
    for m in range(1, 31):
        b = 2**m
        if b - 1 > 10**12:
            continue
        try:
            deg, nprime, e = true_degree(m, n)
            G_true, G_filt, orbits, _ = true_group(b, n)
        except Exception:
            continue
        rows.append((n, m, e, deg, len(G_filt), len(G_true)))

over = [r for r in rows if r[4] != r[3]]
badtrue = [r for r in rows if r[5] != r[3]]

print(f"frames scanned: {len(rows)}")
print(f"orbit filter over/under-counts: {len(over)}  ({100*len(over)/len(rows):.1f}%)")
print(f"corrected group mismatches:     {len(badtrue)}")
print()

if badtrue:
    print("CORRECTED GROUP STILL WRONG ON:")
    for n, m, e, deg, gf, gt in badtrue[:40]:
        print(f"  n={n:>3} m={m:>3} (b=2^{m}) e={e} [K:Q]={deg} |G_true|={gt}")
else:
    print("Corrected group matches [K:Q] on every scanned frame.")

print()
print("frames where the ORBIT FILTER alone is wrong (the trap):")
print(f"{'n':>4} {'m':>4} {'e':>2} {'[K:Q]':>7} {'|G_filt|':>9} {'ratio':>6}")
for n, m, e, deg, gf, gt in over[:60]:
    print(f"{n:>4} {m:>4} {e:>2} {deg:>7} {gf:>9} {gf/deg:>6.2f}")

# characterise the trap
print()
trap_n = sorted(set(r[0] for r in over))
print("n values where over-counting occurs:", trap_n)
print("all satisfy 8|n :", all(n % 8 == 0 for n in trap_n))
nprimes = sorted(set(r[0] // int(gcd(r[1], r[0])) for r in over))
print("n' values in the trap:", nprimes)
