"""Scorer for the continuation-vs-retrieval test.

Works from a notebook, a REPL, or the command line.

    NOTEBOOK / REPL
        from score_test import score, self_check
        self_check()                                  # recompute the key by brute force
        score([324, 36, 8, 288, 4, 3, 5, 4, 1, 0, 1, 0])
        score("Q01: 324\nQ02: 36 ...")                # paste a model's raw reply
        score(open("model_reply.txt").read())

    COMMAND LINE
        python3 score_test.py 324 36 8 288 4 3 5 4 1 0 1 0
        python3 score_test.py --self-check
        cat model_reply.txt | python3 score_test.py

score() accepts a list of 12 ints, a whitespace-separated string, or arbitrary text
containing lines of the form "Q01: 324" (case-insensitive, any separator).
"""
import sys, re
from itertools import permutations

KEY   = [324, 36, 8, 288, 4, 3, 5, 4, 1, 0, 1, 0]
LEVEL = ["classical"]*4 + ["horizon"]*4 + ["co-motion"]*4
CTRL  = {10, 12}

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

def _comp(a,b): return tuple(a[b[i]] for i in range(len(b)))
def _inv(p):
    q=[0]*len(p)
    for i,v in enumerate(p): q[v]=i
    return tuple(q)
def _lab(P,n):
    L=[0]*n
    for i,b in enumerate(P):
        for x in b: L[x]=i
    return L
def _itin(t,L,T):
    n=len(t); out=[]
    for x in range(n):
        w=[]; y=x
        for _ in range(T): w.append(L[y]); y=t[y]
        out.append(tuple(w))
    return tuple(sorted(out))
def _run(t,L,pi,T):
    n=len(t); pin=_inv(pi); pis=[tuple(range(n))]
    for _ in range(T): pis.append(_comp(pin,pis[-1]))
    out=[]
    for x in range(n):
        w=[]; y=x
        for s in range(T): w.append(L[pis[s][y]]); y=t[y]
        out.append(tuple(w))
    return tuple(sorted(out))

def truth():
    """Recompute the key by brute force. Slowest case is n=7 (5040 rules)."""
    out=[]
    for i,(n,P,s,pi) in enumerate(CASES,1):
        s=tuple(s); L=_lab(P,n); allp=list(permutations(range(n)))
        if i<=4:
            tgt=_itin(s,L,2)
            out.append(sum(1 for t in allp if _itin(t,L,2)==tgt))
        elif i<=8:
            sets=[set(t for t in allp if _itin(t,L,T)==_itin(s,L,T)) for T in range(1,3*n+1)]
            fin=sets[-1]
            out.append(next(T for T in range(1,3*n+1) if sets[T-1]==fin))
        else:
            pi=tuple(pi)
            out.append(1 if _run(s,L,pi,4*n)!=_run(_inv(s),L,pi,4*n) else 0)
    return out

def self_check(verbose=True):
    t=truth()
    if verbose:
        print("recomputed:", t)
        print("matches stored key:", t==KEY)
    return t==KEY

def parse(x):
    """Accept a list of ints, a whitespace string, or raw model text with Qnn: v lines."""
    if isinstance(x,(list,tuple)):
        return [int(v) for v in x]
    text=str(x)
    tagged=re.findall(r'(?im)^\s*Q?\s*0*(\d{1,2})\s*[:.\)\-]\s*(-?\d+)', text)
    if len(tagged)>=12:
        d={int(q):int(v) for q,v in tagged}
        missing=[q for q in range(1,13) if q not in d]
        if missing: raise ValueError(f"missing answers for {missing}")
        return [d[q] for q in range(1,13)]
    nums=re.findall(r'-?\d+', text)
    if len(nums)==12: return [int(v) for v in nums]
    raise ValueError(f"could not read 12 answers (found {len(nums)} numbers, "
                     f"{len(tagged)} tagged). Pass a list of 12 ints.")

def score(answers, key=None):
    key = key or KEY
    ans = parse(answers)
    rows=[(i,a,k,LEVEL[i-1],a==k) for i,(a,k) in enumerate(zip(ans,key),1)]
    print("  Q    level        given    true    ok")
    for i,a,k,l,ok in rows:
        tag=" [control]" if i in CTRL else ""
        print(f"  Q{i:02d}  {l:<11} {a:>7} {k:>7}    {'yes' if ok else 'NO '}{tag}")
    print()
    per={}
    for l in ["classical","horizon","co-motion"]:
        c=sum(1 for i,a,k,ll,ok in rows if ll==l and ok)
        per[l]=c
        print(f"  {l:<11} {c}/4")
    ctrl=all(ok for i,a,k,l,ok in rows if i in CTRL)
    print(f"  controls (Q10, Q12) passed: {ctrl}")
    cl=per["classical"]; rest=per["horizon"]+per["co-motion"]
    if cl>=3 and rest>=6 and ctrl:
        p="continuation-consistent (strong across levels, controls held)"
    elif cl>=3 and rest<=3:
        p="retrieval-consistent (strong classical, weak rest)"
    else:
        p="inconclusive - check the system understood the setup"
    print("\n  profile:", p)
    return {"answers":ans,"per_level":per,"controls":ctrl,"profile":p}

def _argv_ints():
    return [t for t in sys.argv[1:] if re.fullmatch(r'-?\d+', t)]

if __name__ == "__main__":
    if "--self-check" in sys.argv:
        self_check()
    else:
        got=_argv_ints()
        if len(got)==12:
            score(got)
        elif not sys.stdin.isatty():
            score(sys.stdin.read())
        else:
            print(__doc__)
