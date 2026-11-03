import sys, math
import mpmath as mp
from measure import shells, rank_int
from valcor import valuation_corank

b, n, mc = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
dps = int(n * math.log10(mc)) + 130
vdps = dps + 150
print(f"({b},{n}) maxcoeff={mc:.3g} dps={dps} vdps={vdps}", flush=True)

S  = shells(b, n, dps)
Sh = shells(b, n, vdps)
active = list(range(n)); found = []
while len(active) > 1:
    mp.mp.dps = dps
    try:
        r = mp.pslq([S[i] for i in active], tol=mp.mpf(10)**(-(dps-60)),
                    maxcoeff=mc, maxsteps=80000)
    except Exception as ex:
        print("pslq exception:", ex, flush=True); r = None
    if not r or all(x == 0 for x in r):
        print("no further relation", flush=True); break
    e = [0]*n
    for k,i in enumerate(active): e[i] = int(r[k])
    mp.mp.dps = vdps
    res = abs(sum(mp.mpf(e[i])*Sh[i] for i in range(n)))
    if res > mp.mpf(10)**(-(vdps-80)):
        print("REJECTED (failed replication), residual", mp.nstr(res,6), flush=True); break
    found.append(tuple(e))
    print(f"  rel {len(found)}: maxc={max(abs(x) for x in e)} res={mp.nstr(res,6)}", flush=True)
    print(f"      {e}", flush=True)
    active.remove(max((i for i in active if e[i]!=0), key=lambda i: abs(e[i])))

cor,_,_ = valuation_corank(b, n)
d = rank_int(found)
print(f"RESULT ({b},{n}): dim={d} corank={cor} delta={d-cor}", flush=True)
