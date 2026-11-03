import itertools
from collections import defaultdict, deque, Counter

def nbrs(c,dims):
    out=[]
    for i in range(len(dims)):
        for d in (1,-1):
            v=list(c); v[i]=(v[i]+d)%dims[i]; out.append(tuple(v))
    return out
def connected(S,dims):
    if not S: return False
    S=set(S); s=next(iter(S)); seen={s}; q=deque([s])
    while q:
        u=q.popleft()
        for v in nbrs(u,dims):
            if v in S and v not in seen: seen.add(v); q.append(v)
    return seen==S
def sign(s):
    n=len(s); sg=1; seen=[False]*n
    for i in range(n):
        if not seen[i]:
            L=0;j=i
            while not seen[j]: seen[j]=True;L+=1;j=s[j]
            if L%2==0: sg=-sg
    return sg

def census(parts, movefn, label):
    """FULL S_3 cover: ordered triples, no cyclic identification."""
    cover=sorted({p for b in parts for p in itertools.permutations(b)})
    cs=set(cover); adj=defaultdict(set)
    for v in cover:
        for w in movefn(v):
            if w in cs: adj[v].add(w); adj[w].add(v)
    base=sorted({frozenset(v) for v in cover}); bidx={b:i for i,b in enumerate(base)}
    badj=defaultdict(set)
    for v in cover:
        for w in adj[v]:
            badj[frozenset(v)].add(frozenset(w)); badj[frozenset(w)].add(frozenset(v))
    def lift(La,Q):
        for c in movefn(La):
            if frozenset(c)==Q: return c
        return None
    start=base[0]; L={start:tuple(sorted(start,key=lambda b:sorted(b)))}
    parent={start:None}; q=deque([start])
    while q:
        P=q.popleft()
        for Q in badj[P]:
            if Q in L: continue
            c=lift(L[P],Q)
            if c is None: continue
            L[Q]=c; parent[Q]=P; q.append(Q)
    tree={(min(bidx[c],bidx[parent[c]]),max(bidx[c],bidx[parent[c]])) for c in parent if parent[c]}
    perm=lambda La,Lb: tuple(Lb.index(La[k]) for k in range(3))
    rhos=[]
    for P in L:
        for Q in badj[P]:
            if Q not in L: continue
            key=(min(bidx[P],bidx[Q]),max(bidx[P],bidx[Q]))
            if key in tree or bidx[P]>bidx[Q]: continue
            c=lift(L[P],Q)
            if c: rhos.append(perm(c,list(L[Q])))
    nm={(0,1,2):'e',(1,2,0):'(123)',(2,0,1):'(132)',(0,2,1):'(23)',(2,1,0):'(13)',(1,0,2):'(12)'}
    V=len(L); E=sum(len(badj[b]&set(L)) for b in L)//2
    grp={(0,1,2)}
    ch=True
    while ch:
        ch=False
        for g in list(grp):
            for h in rhos:
                x=tuple(g[h[k]] for k in range(3))
                if x not in grp: grp.add(x); ch=True
    print(f"{label}")
    print(f"   V={V} E={E} beta_1={E-V+1}  cycles measured {len(rhos)}")
    print(f"   {dict(Counter(nm[r] for r in rhos))}")
    print(f"   odd {sum(1 for r in rhos if sign(r)==-1)}   subgroup order {len(grp)} "
          f"= {'A_3' if len(grp)==3 else 'S_3' if len(grp)==6 else len(grp)}")

# 1D arcs N=6
N=6
def arcs(N):
    out=[]
    for c in itertools.combinations(range(N),3):
        cs=sorted(c); a=[]
        for i in range(3):
            s,e=cs[i],cs[(i+1)%3]
            a.append(frozenset((s+t)%N for t in range((e-s)%N)))
        if all(len(x)>0 for x in a) and len(set().union(*a))==N: out.append(tuple(a))
    return out
def slide(v):
    out=[]
    for i in range(3):
        for j in range(3):
            if i==j or len(v[i])<2: continue
            for x in v[i]:
                if (x+1)%N in v[j] or (x-1)%N in v[j]:
                    n=list(v); n[i]=frozenset(v[i]-{x}); n[j]=frozenset(v[j]|{x})
                    if all(len(b)>0 for b in n): out.append(tuple(n))
    return out
census(arcs(N), slide, '1D contiguous arcs, Z_6')
print()

# 2D torus connected regions
dims=(3,3); cells=[(i,j) for i in range(3) for j in range(3)]
parts=[]
for k in range(1,8):
    for A in itertools.combinations(cells,k):
        if not connected(A,dims): continue
        rest=[c for c in cells if c not in A]
        for k2 in range(1,len(rest)):
            for Bb in itertools.combinations(rest,k2):
                if not connected(Bb,dims): continue
                C=tuple(c for c in rest if c not in Bb)
                if C and connected(C,dims): parts.append((frozenset(A),frozenset(Bb),frozenset(C)))
def transfer(v):
    out=[]
    for i,j in itertools.permutations(range(3),2):
        if len(v[i])<2: continue
        for x in v[i]:
            if not any(y in v[j] for y in nbrs(x,dims)): continue
            ni=frozenset(v[i]-{x}); nj=frozenset(v[j]|{x})
            if connected(ni,dims) and connected(nj,dims):
                out.append(tuple(nj if k==j else (ni if k==i else v[k]) for k in range(3)))
    return out
census(parts, transfer, '2D torus Z_3xZ_3, connected regions')
