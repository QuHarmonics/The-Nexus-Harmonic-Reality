import itertools, numpy as np
from collections import defaultdict
from audit import int_partitions, ctype, UF
for n in (5,6,7):
    perms=list(itertools.permutations(range(n))); idx={p:i for i,p in enumerate(perms)}; N=len(perms)
    inv=[idx[tuple(int(v) for v in np.argsort(p))] for p in perms]; lam=[ctype(p) for p in perms]
    c1=c2=0
    for mu in int_partitions(n):
        m=len(mu); b=[]; blocks=[]; s=0
        for i,k in enumerate(mu): b+=[i]*k; blocks.append(list(range(s,s+k))); s+=k
        gens=[]
        for B in blocks:
            for a,c in zip(B,B[1:]): g=list(range(n)); g[a],g[c]=c,a; gens.append(g)
        for i in range(m-1):
            if mu[i]==mu[i+1]:
                g=list(range(n))
                for a,c in zip(blocks[i],blocks[i+1]): g[a],g[c]=c,a
                gens.append(g)
        cell=defaultdict(list)
        for si,p in enumerate(perms):
            T=[0]*(m*m)
            for x in range(n): T[b[x]*m+b[p[x]]]+=1
            cell[(tuple(T),lam[si])].append(si)
        u1=UF(N); u2=UF(N)
        for mem in cell.values():
            for s_ in mem[1:]: u1.u(mem[0],s_); u2.u(mem[0],s_)
        for si,p in enumerate(perms):
            for g in gens:
                gi=[0]*n
                for x in range(n): gi[g[x]]=x
                ci=idx[tuple(g[p[gi[x]]] for x in range(n))]; u1.u(si,ci); u2.u(si,ci)
            u2.u(si,inv[si])
        c1+=u1.count(); c2+=u2.count()
    print(f"n={n}: classes under conjugation + [tau in M(P,sigma)]: {c1}   ... + inversion: {c2}")
