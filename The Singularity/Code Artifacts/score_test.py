"""Scorer for the continuation-vs-retrieval test.

Usage:
    python3 score_test.py 324 36 8 288 4 3 5 4 1 0 1 0
    python3 score_test.py --self-check      # recompute ground truth from scratch

Ground truth is recomputed by brute force on request, so the key is not merely asserted.
"""
import sys, itertools
from itertools import permutations

KEY   = [324, 36, 8, 288, 4, 3, 5, 4, 1, 0, 1, 0]
LEVEL = ["classical"]*4 + ["horizon"]*4 + ["co-motion"]*4
CTRL  = {10, 12}          # answer 0; catch a system that always says "yes"

CASES = [
 (6,[(0,1,2),(3,4,5)],[1,2,3,4,5,0],None),
 (6,[(0,2,4),(1,3,5)],[1,2,3,4,5,0],None),
 (6,[(0,1),(2,3),(4,5)],[2,3,4,5,0,1],None),
 (7,[(0,1,2),(3,4),(5,6)],[1,2,3,4,5,6,0],None),
 (6,[(0,1,2),(3,4,5)],[1,2,3,4,5,0],None),
 (6,[(0,1),(2,3),(4,5)],[1,2,3,4,5,0],None),
 (6,[(0,),(1,),(2,3,4,5)],[1,2,3,4,5,0],None),
 (5,[(0,1),(2,3,4)],[1,2,3,4,0],None),
 (5,[(0,4),(1,2,3)],[1,2,3,4,0],[0,1,2,4,3]),
 (5,[(0,),(1,2,3,4)],[1,2,3,4,0],[0,1,2,3,4]),
 (6,[(0,3,4,5),(1,2)],[1,2,3,4,5,0],[0,1,3,4,2,5]),
 (5,[(0,1),(2,3,4)],[1,2,3,4,0],[1,0,2,3,4]),
]

def comp(a,b): return tuple(a[b[i]] for i in range(len(b)))
def inv(p):
    q=[0]*len(p)
    for i,v in enumerate(p): q[v]=i
    return tuple(q)
def LAB(P,n):
    L=[0]*n
    for i,b in enumerate(P):
        for x in b: L[x]=i
    return L
def itinT(t,L,T):
    n=len(t); out=[]
    for x in range(n):
        w=[]; y=x
        for _ in range(T): w.append(L[y]); y=t[y]
        out.append(tuple(w))
    return tuple(sorted(out))
def rec_running(t,L,pi,T):
    n=len(t); pin=inv(pi); pis=[tuple(range(n))]
    for _ in range(T): pis.append(comp(pin,pis[-1]))
    out=[]
    for x in range(n):
        w=[]; y=x
        for s in range(T): w.append(L[pis[s][y]]); y=t[y]
        out.append(tuple(w))
    return tuple(sorted(out))

def truth():
    out=[]
    for i,(n,P,s,pi) in enumerate(CASES,1):
        s=tuple(s); L=LAB(P,n); allp=list(permutations(range(n)))
        if i<=4:
            tgt=itinT(s,L,2)
            out.append(sum(1 for t in allp if itinT(t,L,2)==tgt))
        elif i<=8:
            sets=[set(t for t in allp if itinT(t,L,T)==itinT(s,L,T)) for T in range(1,3*n+1)]
            fin=sets[-1]
            out.append(next(T for T in range(1,3*n+1) if sets[T-1]==fin))
        else:
            pi=tuple(pi)
            out.append(1 if rec_running(s,L,pi,4*n)!=rec_running(inv(s),L,pi,4*n) else 0)
    return out

if "--self-check" in sys.argv:
    t=truth()
    print("recomputed:", t)
    print("matches stored key:", t==KEY)
    sys.exit(0)

ans=[int(x) for x in sys.argv[1:13]]
if len(ans)!=12:
    print(__doc__); sys.exit(1)
by={}
for i,(a,k,l) in enumerate(zip(ans,KEY,LEVEL),1):
    by.setdefault(l,[]).append((i,a,k,a==k))
print("  Q    level        given    true    ok")
for l in ["classical","horizon","co-motion"]:
    for i,a,k,ok in by[l]:
        tag=" [control]" if i in CTRL else ""
        print(f"  Q{i:02d}  {l:<11} {a:>7} {k:>7}    {'yes' if ok else 'NO '}{tag}")
print()
for l in ["classical","horizon","co-motion"]:
    c=sum(1 for _,_,_,ok in by[l] if ok)
    print(f"  {l:<11} {c}/4")
ctrl_ok=all(ok for i,_,_,ok in [x for v in by.values() for x in v] if i in CTRL)
print(f"  controls (Q10, Q12) passed: {ctrl_ok}")
cl=sum(1 for _,_,_,ok in by['classical'] if ok)
rest=sum(1 for l in ['horizon','co-motion'] for _,_,_,ok in by[l] if ok)
print()
print("  profile:", "retrieval-consistent (strong classical, weak rest)" if cl>=3 and rest<=3
      else "continuation-consistent (strong across levels)" if cl>=3 and rest>=6
      else "inconclusive — check the system understood the setup")
