import math
import mpmath as mp
from measure import shells, rank_int
from valcor import valuation_corank

def kdim(b, n, mc=None):
    mc = mc or max(10**7, 1000*b)
    dps = int(n*math.log10(mc)) + 130; vdps = dps + 150
    S, Sh = shells(b,n,dps), shells(b,n,vdps)
    active, found = list(range(n)), []
    while len(active) > 1:
        mp.mp.dps = dps
        try: r = mp.pslq([S[i] for i in active], tol=mp.mpf(10)**(-(dps-60)),
                         maxcoeff=mc, maxsteps=80000)
        except Exception: r = None
        if not r or all(x==0 for x in r): break
        e=[0]*n
        for k,i in enumerate(active): e[i]=int(r[k])
        mp.mp.dps = vdps
        if abs(sum(mp.mpf(e[i])*Sh[i] for i in range(n))) > mp.mpf(10)**(-(vdps-80)): break
        found.append(tuple(e))
        active.remove(max((i for i in active if e[i]!=0), key=lambda i: abs(e[i])))
    return rank_int(found), found

# Existing subdivision frames: seed (b,m) -> (b, q*m), same radix b
CASES = [("hex q=2", 64, 12, 2), ("hex q=3", 64, 18, 3),
         ("hex q=4", 64, 24, 4), ("oct q=3", 16, 24, 3)]
for name, b, n, q in CASES:
    d, rels = kdim(b, n)
    cor,_,_ = valuation_corank(b, n)
    classes = sorted({ (i+1) % q for r in rels for i,x in enumerate(r) if x })
    print(f"{name:>9} ({b},{n}): dim={d} corank={cor} delta={d-cor}  "
          f"classes mod {q} carrying relations: {classes}", flush=True)
