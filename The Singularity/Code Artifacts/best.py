import itertools, numpy as np
from collections import defaultdict, Counter
from math import factorial, prod
from fractions import Fraction
from audit import int_partitions, ctype, UF

def det_int(M):
    M=[[Fraction(x) for x in r] for r in M]; n=len(M); d=Fraction(1)
    for c in range(n):
        p=next((r for r in range(c,n) if M[r][c]!=0),None)
        if p is None: return 0
        if p!=c: M[c],M[p]=M[p],M[c]; d=-d
        d*=M[c][c]
        for r in range(c+1,n):
            f=M[r][c]/M[c][c]
            for k in range(c,n): M[r][k]-=f*M[c][k]
    return int(d)

def best_ncycles(T,d):
    m=len(d)
    L=[[(sum(T[i]) if i==j else 0)-(T[i][j] if i!=j else 0) for j in range(m)] for i in range(m)]
    # loops: remove from degree too for Laplacian
    for i in range(m): L[i][i]-=T[i][i]
    tw=det_int([r[1:] for r in L[1:]]) if m>1 else 1
    ec=tw*prod(factorial(x-1) for x in d)
    return Fraction(ec*prod(factorial(x) for x in d), prod(factorial(int(v)) for r in T for v in r))

def ts_spectrum(T,d):
    # enumerate transition systems on labeled-arc multigraph; return Counter of trail-length multisets
    m=len(d); arcs=[]
    for i in range(m):
        for j in range(m):
            for _ in range(T[i][j]): arcs.append((i,j))
    A=len(arcs)
    inc=[[a for a in range(A) if arcs[a][1]==v] for v in range(m)]
    out=[[a for a in range(A) if arcs[a][0]==v] for v in range(m)]
    C=Counter()
    for choice in itertools.product(*[itertools.permutations(out[v]) for v in range(m)]):
        nxt=[0]*A
        for v in range(m):
            for a,bb in zip(inc[v],choice[v]): nxt[a]=bb
        C[ctype(nxt)]+=1
    return C

for n in (5,6,7):
    perms=list(itertools.permutations(range(n))); N=len(perms)
    lam=[ctype(p) for p in perms]
    bad_best=0; checked_best=0; bad_ts=0; checked_ts=0; key_uf_total=0; key_uf_inv_total=0
    for mu in int_partitions(n):
        m=len(mu); b=[]
        for i,k in enumerate(mu): b+=[i]*k
        groups=defaultdict(list)
        for si,p in enumerate(perms):
            T=[[0]*m for _ in range(m)]
            for x in range(n): T[b[x]][b[p[x]]]+=1
            groups[tuple(map(tuple,T))].append(si)
        for Tt,members in groups.items():
            T=[list(r) for r in Tt]
            cnt=Counter(lam[s] for s in members)
            pred=best_ncycles(T,mu); got=cnt.get((n,),0)
            checked_best+=1
            if pred!=got: bad_best+=1
            if prod(factorial(x) for x in mu)<=5040:
                C=ts_spectrum(T,mu); scale=Fraction(prod(factorial(x) for x in mu),prod(factorial(v) for r in T for v in r))
                checked_ts+=1
                if any(Fraction(C[l])*scale!=cnt.get(l,0) for l in set(C)|set(cnt)): bad_ts+=1
    print(f"n={n}: BEST closed form for |M| at lambda=(n): {checked_best-bad_best}/{checked_best} tables exact;"
          f"  transition-system spectrum == |M| for all lambda: {checked_ts-bad_ts}/{checked_ts}")
