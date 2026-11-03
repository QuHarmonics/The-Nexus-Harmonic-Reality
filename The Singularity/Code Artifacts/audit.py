import itertools, sys, numpy as np
from collections import defaultdict
from math import factorial

def int_partitions(n, maxp=None):
    if maxp is None: maxp = n
    if n == 0: yield (); return
    for k in range(min(n, maxp), 0, -1):
        for rest in int_partitions(n-k, k): yield (k,)+rest

def ctype(p):
    n=len(p); seen=[0]*n; out=[]
    for i in range(n):
        if not seen[i]:
            L=0; j=i
            while not seen[j]: seen[j]=1; j=p[j]; L+=1
            out.append(L)
    return tuple(sorted(out, reverse=True))

class UF:
    def __init__(s,n): s.p=list(range(n))
    def f(s,x):
        while s.p[x]!=x: s.p[x]=s.p[s.p[x]]; x=s.p[x]
        return x
    def u(s,a,b):
        a,b=s.f(a),s.f(b)
        if a!=b: s.p[a]=b
    def count(s): return len({s.f(i) for i in range(len(s.p))})

def run(n):
    perms=list(itertools.permutations(range(n))); idx={p:i for i,p in enumerate(perms)}; N=len(perms)
    inv=[idx[tuple(np.argsort(p))] for p in perms]
    lam=[ctype(p) for p in perms]
    tot=dict(orb=0, orb_inv=0, key=set(), skey=set(), vals=set(), keyM={}, split_inv=0,
             dc_mismatch=0, orb_splits_key=0, ninv_asym=0, cells=0)
    for mu in int_partitions(n):
        m=len(mu); b=[]; blocks=[]; s=0
        for i,k in enumerate(mu): b+= [i]*k; blocks.append(list(range(s,s+k))); s+=k
        # labeled contingency table T[i][j] = #{x in B_i : sigma(x) in B_j}
        T=np.zeros((N,m,m),dtype=np.int8)
        for si,p in enumerate(perms):
            for x in range(n): T[si,b[x],b[p[x]]]+=1
        Tb=[T[si].tobytes() for si in range(N)]
        # |M| via (labeled T, lambda) grouping  [double coset <-> T]
        grp=defaultdict(int)
        for si in range(N): grp[(Tb[si],lam[si])]+=1
        Mval=[grp[(Tb[si],lam[si])] for si in range(N)]
        # check double coset <-> T by brute force for small |K|
        Ksz=int(np.prod([factorial(k) for k in mu]))
        if Ksz<=48:
            K=[]
            for q in perms:
                if all(b[q[x]]==b[x] for x in range(n)): K.append(q)
            for si in range(0,N,max(1,N//60)):
                p=perms[si]
                dc={tuple(k1[p[k2[x]]] for x in range(n)) for k1 in K for k2 in K}
                same={perms[t] for t in range(N) if Tb[t]==Tb[si]}
                if dc!=same: tot['dc_mismatch']+=1
        # generators of Stab(P0): within-block adjacent transpositions, swaps of consecutive equal blocks
        gens=[]
        for B in blocks:
            for a,c in zip(B,B[1:]):
                g=list(range(n)); g[a],g[c]=c,a; gens.append(g)
        for i in range(m-1):
            if mu[i]==mu[i+1]:
                g=list(range(n))
                for a,c in zip(blocks[i],blocks[i+1]): g[a],g[c]=c,a
                gens.append(g)
        uf=UF(N); uf2=UF(N)
        for si,p in enumerate(perms):
            for g in gens:
                gi=[0]*n
                for x in range(n): gi[g[x]]=x
                c=tuple(g[p[gi[x]]] for x in range(n)); ci=idx[c]
                uf.u(si,ci); uf2.u(si,ci)
            uf2.u(si,inv[si])
        tot['orb']+=uf.count(); tot['orb_inv']+=uf2.count()
        # key: (T up to size-preserving simultaneous block relabel, lambda)
        bperms=[]
        for q in itertools.permutations(range(m)):
            if all(mu[q[i]]==mu[i] for i in range(m)): bperms.append(q)
        BP=np.array(bperms)
        uniqT={}
        for si in range(N): uniqT.setdefault(Tb[si],si)
        canon={}
        for tb,si in uniqT.items():
            A=T[si]
            X=A[BP[:,:,None],BP[:,None,:]].reshape(len(BP),-1)
            Y=A.T[BP[:,:,None],BP[:,None,:]].reshape(len(BP),-1)
            cx=min(r.tobytes() for r in X); cy=min(r.tobytes() for r in Y)
            canon[tb]=(mu,cx,min(cx,cy),cx!=cy)
        keyof=[]; 
        for si in range(N):
            mu_,cx,cs,asym=canon[Tb[si]]
            k=(mu_,cx,lam[si]); ks=(mu_,cs,lam[si]); keyof.append(k)
            tot['key'].add(k); tot['skey'].add(ks); tot['vals'].add(Mval[si])
            if k in tot['keyM'] and tot['keyM'][k]!=Mval[si]: tot['keyM'][k]=-1
            else: tot['keyM'].setdefault(k,Mval[si])
            if asym: tot['ninv_asym']+=1
        tot['cells']+=N
        # key invariance under conjugation: constant on uf orbits
        rep=defaultdict(set); repM=defaultdict(set); rep2=defaultdict(set)
        for si in range(N):
            rep[uf.f(si)].add(keyof[si]); repM[uf2.f(si)].add(Mval[si]); rep2[uf2.f(si)].add(keyof[si])
        tot['orb_splits_key']+=sum(len(v)>1 for v in rep.values())
        tot['split_inv']+=sum(len(v)>1 for v in rep2.values())
        assert all(len(v)==1 for v in repM.values()), "M not constant on conj+inv orbits"
    amb=sum(1 for v in tot['keyM'].values() if v==-1)
    print(f"n={n}: cells {tot['cells']}  |X/S_n| {tot['orb']}  |X/(S_n x C2)| {tot['orb_inv']}  "
          f"key {len(tot['key'])} (ambiguous {amb}, conj-orbits splitting key {tot['orb_splits_key']})  "
          f"sym-key {len(tot['skey'])}  values {len(tot['vals'])}  "
          f"conj+inv orbits split by key {tot['split_inv']}  cells with T not ~ T^t {tot['ninv_asym']}  "
          f"double-coset<->T mismatches {tot['dc_mismatch']}")
for n in map(int,sys.argv[1:]): run(n)
