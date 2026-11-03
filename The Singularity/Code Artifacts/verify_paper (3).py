"""Companion verification for: What a Reader Recovers.
Reproduces every number in the paper. No randomness; every census stated as
exhaustive enumerates its full domain.  Runtime ~2 min on one core.
"""
import itertools, time
from math import factorial, log2
from itertools import permutations, combinations
from collections import Counter, deque

# ---------- permutation utilities ----------
def comp(a,b): return tuple(a[b[i]] for i in range(len(b)))
def inv(p):
    q=[0]*len(p)
    for i,v in enumerate(p): q[v]=i
    return tuple(q)
def ctype(p):
    n=len(p); seen=[False]*n; c=[]
    for i in range(n):
        if seen[i]: continue
        l=0; j=i
        while not seen[j]: seen[j]=True; j=p[j]; l+=1
        c.append(l)
    return tuple(sorted(c,reverse=True))
def order(p):
    n=len(p); e=tuple(range(n)); q=p; k=1
    while q!=e: q=comp(p,q); k+=1
    return k
def class_size(lam,n):
    cnt=Counter(lam); d=1
    for l,m in cnt.items(): d*=(l**m)*factorial(m)
    return factorial(n)//d
def rep_of(lam,n):
    p=[0]*n; i=0
    for L in lam:
        for j in range(L): p[i+j]=i+(j+1)%L
        i+=L
    return tuple(p)
def parts_of(n):
    def go(n,mx):
        if n==0: yield (); return
        for k in range(min(n,mx),0,-1):
            for t in go(n-k,k): yield (k,)+t
    return list(go(n,n))

# ---------- partitions and Young subgroups ----------
def young(P):
    r=1
    for b in P: r*=factorial(len(b))
    return r
def young_group(P,n):
    B=[list(b) for b in P]; out=[]
    for cb in itertools.product(*[permutations(b) for b in B]):
        q=[0]*n
        for b,img in zip(B,cb):
            for s,d in zip(b,img): q[s]=d
        out.append(tuple(q))
    return out
def blockgens(P,n):
    g=[]
    for b in P:
        b=sorted(b)
        for x,y in zip(b,b[1:]):
            q=list(range(n)); q[x],q[y]=y,x; g.append(tuple(q))
    return g
def dcoset(s,gens):
    """KsK by BFS under left/right multiplication by block transpositions."""
    I={s}; q=deque([s])
    while q:
        p=q.popleft()
        for g in gens:
            for r in (comp(g,p), comp(p,g)):
                if r not in I: I.add(r); q.append(r)
    return I
def setparts(el):
    el=list(el)
    if not el: yield []; return
    f,rest=el[0],el[1:]
    for r in setparts(rest):
        for i in range(len(r)): yield r[:i]+[tuple(sorted((f,)+r[i]))]+r[i+1:]
        yield [(f,)]+r
def uparts(el,size):
    el=list(el)
    if not el: yield []; return
    f=el[0]
    for rest in combinations(el[1:],size-1):
        blk=(f,)+rest; rem=[e for e in el[1:] if e not in rest]
        for t in uparts(rem,size): yield [tuple(sorted(blk))]+t
def meet(P,Q):
    c={}
    for b in P:
        for x in b: c[x]=[frozenset(b)]
    for b in Q:
        for x in b: c[x].append(frozenset(b))
    g={}
    for x,(p,q) in c.items(): g.setdefault((p,q),[]).append(x)
    return [tuple(sorted(v)) for v in g.values()]
def imgP(P,s): return [tuple(sorted(s[x] for x in b)) for b in P]
def aligned(P,s): return set(map(frozenset,P))==set(map(frozenset,imgP(P,s)))
def lab(P,n):
    L=[0]*n
    for i,b in enumerate(P):
        for x in b: L[x]=i
    return L

# ---------- reader records ----------
def record_R1(t,L,P):
    return tuple(tuple(sorted(Counter(L[t[x]] for x in b).items())) for b in P)
def itinerary(t,L,T):
    n=len(t); out=[]
    for x in range(n):
        s=[]; y=x
        for _ in range(T): s.append(L[y]); y=t[y]
        out.append(tuple(s))
    return tuple(sorted(out))

T0=time.time()
print("="*74)
print("SECTION 3.  R1 consistent set = the double coset KsK   (brute force, S_6)")
n=6; allp=list(permutations(range(n)))
for P,k in [([(0,1,2),(3,4,5)],1),([(0,3),(1,4),(2,5)],1),([(0,1),(2,3),(4,5)],2),
            ([(0,1,2),(3,4,5)],3),([(0,2,4),(1,3,5)],1)]:
    s=tuple((x+k)%n for x in range(n)); L=lab(P,n)
    cons=[t for t in allp if record_R1(t,L,P)==record_R1(s,L,P)]
    I=dcoset(s,blockgens(P,n))
    cf=young(P)**2//young(meet(P,imgP(P,s)))
    print(f"   P={P} sigma=+{k}:  |consistent|={len(cons):4d}  |KsK|={len(I):4d}  "
          f"closed form={cf:4d}  match={len(cons)==len(I)==cf}")

print("\n"+"="*74)
print("SECTION 4.  the ladder  G <= R3 <= R2 <= R1   (class reps x all set partitions)")
print("   n   configs   |R2|<|R1|   |R3|<|R2|      R3==G        R1==G")
for n in (4,5,6):
    allp=list(permutations(range(n))); allP=list(setparts(range(n)))
    tot=s21=s32=eqG=r1G=0; mult=Counter()
    for lam in parts_of(n):
        s=rep_of(lam,n); T=order(s)
        pw=[]; q=s
        for _ in range(T): pw.append(q); q=comp(s,q)
        for P in allP:
            K=young_group(P,n); L=lab(P,n); gens=blockgens(P,n)
            R1=dcoset(s,gens)
            pc=[dcoset(p,gens) for p in pw]
            R2=set()
            for t in R1:
                q=t; ok=True
                for i in range(T):
                    if q not in pc[i]: ok=False; break
                    q=comp(t,q)
                if ok: R2.add(t)
            tgt=itinerary(s,L,2*n)
            R3=set(t for t in R2 if itinerary(t,L,2*n)==tgt)
            G=set(comp(k,comp(s,inv(k))) for k in K)
            assert G<=R3<=R2<=R1
            tot+=1
            s21+= len(R2)<len(R1); s32+= len(R3)<len(R2)
            eqG+= R3==G; r1G+= R1==G
            mult[len(R3)//len(G) if len(R3)%len(G)==0 else -1]+=1
    print(f"   {n} {tot:8d} {s21:10d} {s32:11d}   {eqG:5d} ({100*eqG/tot:4.1f}%) {r1G:8d}")
    if n==6:
        print(f"        |R3|/|G| multiplicities: {dict(sorted(mult.items()))}  (no non-integer ratios: {-1 not in mult})")

print("\n"+"="*74)
print("SECTION 5.  R1 floor = log2|K|, attained exactly on aligned partitions (Z/12)")
N=12
for k in (1,2,3):
    s=[(x+k)%N for x in range(N)]
    for bs in (6,4,3,2):
        rows=[(log2(young(P)**2//young(meet(P,imgP(P,s)))), aligned(P,s)) for P in uparts(range(N),bs)]
        rows.sort(); K=log2(young([tuple(range(bs))]*(N//bs)))
        al=[r[0] for r in rows if r[1]]
        ok = abs(rows[0][0]-K)<1e-9 and min(al)==max(al)==rows[0][0]
        print(f"   sigma=+{k} labels={N//bs}: floor={K:7.3f} min={rows[0][0]:7.3f} "
              f"median={rows[len(rows)//2][0]:7.3f} worst={rows[-1][0]:7.3f} aligned-attains={ok}")

print("\n"+"="*74)
print("SECTION 6.  passive observation: consistent set vs the group-based figure (Z/12)")
import math
for k in (1,2,3):
    G=12//math.gcd(12,k); sizes=[G]*(12//G); a=1; h=1
    for z in sizes: a*=factorial(z); h*=factorial(z-1)
    a//=G
    print(f"   <+{k}> orbits {sizes}: group-based {a:>9} ({log2(a):6.3f} b)   "
          f"consistent {h:>9} ({log2(h):6.3f} b)   ratio {a/h:.1f}x")
print(f"   transitive coincidence: 12!/12 = 11! = {factorial(12)//12 == factorial(11)}")

print("\n"+"="*74)
print("SECTION 7.  joint reader census S_4..S_7, and the extremal family")
print("   n   configs   gain   max excess   aligned among gainers")
for n in (4,5,6,7):
    allP=list(setparts(range(n))); tot=sup=alsup=0; mx=-9
    for lam in parts_of(n):
        s=rep_of(lam,n); Cl=class_size(lam,n); d=log2(factorial(n)/Cl)
        for P in allP:
            I=dcoset(s,blockgens(P,n)); M=sum(1 for p in I if ctype(p)==lam)
            e=log2(len(I))-log2(M)-d; tot+=1
            if e>1e-9:
                sup+=1
                if aligned(P,s): alsup+=1
            mx=max(mx,e)
    print(f"   {n} {tot:8d} {sup:6d}    {mx:+.4f}          {alsup}")
print("   extremal family lambda=(4,1^(n-4)), P={1,3}|rest,  gain=(n-2)(n-3)/4")
for n in (6,7,8,9):
    lam=(4,)+(1,)*(n-4); s=rep_of(lam,n); Cl=class_size(lam,n)
    P=[(1,3),tuple(x for x in range(n) if x not in (1,3))]
    I=dcoset(s,blockgens(P,n)); M=sum(1 for p in I if ctype(p)==lam)
    R=(len(I)*Cl/factorial(n))/M
    print(f"     n={n}: |KsK| {factorial(n-2)**2//factorial(n-4):>7}/{len(I):<7} "
          f"|M| {(n-2)*(n-3):>3}/{M:<3} gain {(n-2)*(n-3)/4:7.3f}/{R:<7.3f} excess {log2(R):+.4f} b")

print("\n"+"="*74)
print("SECTION 8.  families of readers, and the orientation floor")
def twoblocks(n):
    out=set()
    for k in range(1,n):
        for A in combinations(range(n),k):
            B=tuple(x for x in range(n) if x not in A)
            out.add(frozenset([A,B]))
    return [sorted(map(tuple,f)) for f in out]
for n in (5,6,7):
    allp=list(permutations(range(n))); s=tuple((x+1)%n for x in range(n))
    tb=twoblocks(n); cap=set(allp)
    for P in tb: cap&=dcoset(s,blockgens(P,n))
    print(f"   n={n}: complete binary family {len(tb)} readers (= 2^(n-1)-1 = {2**(n-1)-1}) "
          f"-> {len(cap)} candidates; == {{sigma, sigma^-1}}: {cap=={s,inv(s)}}")
for n in (5,6):
    allp=list(permutations(range(n))); s=tuple((x+1)%n for x in range(n))
    cap=set(allp)
    for P in twoblocks(n): cap&=dcoset(s,blockgens(P,n))
    three=[P for P in setparts(range(n)) if len(P)==3]
    kills=sum(1 for P in three if len(cap & dcoset(s,blockgens(P,n)))==1)
    props=[P for P in setparts(range(n)) if 1<len(P)<n]
    cos=[dcoset(s,blockgens(P,n)) for P in props]
    best=None
    for m in (1,2):
        for cb in combinations(range(len(props)),m):
            I=set(allp)
            for i in cb: I&=cos[i]
            if len(I)==1: best=(m,[props[i] for i in cb]); break
        if best: break
    print(f"   n={n}: 3-block readers breaking the tie: {kills}/{len(three)};  "
          f"minimum proper partitions for exact recovery = {best[0]}")
    print(f"        witness: {best[1]}")



# ================= additional sections for the expanded paper =================
def contingency(P,s):
    m=len(P); idx={}
    for i,b in enumerate(P):
        for x in b: idx[x]=i
    N=[[0]*m for _ in range(m)]
    for i,b in enumerate(P):
        for x in b: N[i][idx[s[x]]]+=1
    return tuple(tuple(r) for r in N)
def prodfac(N):
    r=1
    for row in N:
        for v in row: r*=factorial(v)
    return r
def undirected(s): return frozenset(frozenset((x,s[x])) for x in range(len(s)))
def necklaces(k):
    return {min(tuple(w[i:]+w[:i]) for i in range(k)) for w in itertools.product((0,1),repeat=k)}
def bracelets(k):
    out=set()
    for w in itertools.product((0,1),repeat=k):
        r=tuple(reversed(w))
        out.add(min([tuple(w[i:]+w[:i]) for i in range(k)]+[tuple(r[i:]+r[:i]) for i in range(k)]))
    return out
def twoblocks(n):
    out=set()
    for kk in range(1,n):
        for A in combinations(range(n),kk):
            B=tuple(x for x in range(n) if x not in A)
            out.add(frozenset([A,B]))
    return [sorted(map(tuple,f)) for f in out]

print("\n"+"="*74)
print("SECTION 3 / 4A.  the record IS the contingency table; product formula")
ok=True; checked=0
for n in (4,5):
    for P in setparts(range(n)):
        base_=1
        for b in P: base_*=factorial(len(b))
        for s in permutations(range(n)):
            N=contingency(P,s)
            if base_*base_//prodfac(N) != len(dcoset(s,blockgens(P,n))): ok=False
            checked+=1
print(f"   |KsK| = (prod|B|!)^2 / prod N_ij!  in all {checked} pairs at n=4,5 : {ok}")
n=6; s=tuple((x+1)%6 for x in range(6))
for P,name in [([(0,1,2),(3,4,5)],"A"),([(0,2,4),(1,3,5)],"B")]:
    N=contingency(P,s); K=1
    for b in P: K*=factorial(len(b))
    print(f"   worked example reader {name}: N={N}  |K|={K}  |KsK|={K*K//prodfac(N)}")

print("\n"+"="*74)
print("SECTION 4.  inversion criterion:  sigma^-1 in KsK  <=>  N(P,sigma) symmetric")
bad=tot=sym2=tot2=0
for n in (4,5,6):
    for P in setparts(range(n)):
        for s in permutations(range(n)):
            N=contingency(P,s); m=len(N)
            symm=all(N[i][j]==N[j][i] for i in range(m) for j in range(m))
            if symm != (inv(s) in dcoset(s,blockgens(P,n))): bad+=1
            tot+=1
            if m<=2:
                tot2+=1; sym2+= symm
print(f"   {tot} triples at n=4,5,6 : counterexamples = {bad}")
print(f"   of {tot2} triples with |P|<=2, table symmetric in {sym2} (100% expected)")

print("\n"+"="*74)
print("SECTION 9.  complete binary family recovers the undirected graph; |cap| = 2^c")
for n in (4,5,6,7):
    allp=list(permutations(range(n))); tb=twoblocks(n); allok=True
    for lam in parts_of(n):
        s=rep_of(lam,n); cap=set(allp)
        for P in tb: cap&=dcoset(s,blockgens(P,n))
        c=sum(1 for L in lam if L>=3)
        allok &= (len(cap)==2**c) and (cap=={t for t in allp if undirected(t)==undirected(s)})
    print(f"   n={n} ({len(tb)} binary readers, {len(parts_of(n))} cycle types): |cap| = 2^c and cap = orientations : {allok}")

print("\n"+"="*74)
print("SECTION 10.  handedness threshold")
for n in (5,6,7):
    s=tuple((x+1)%n for x in range(n)); T=order(s); allsym=True
    for P in twoblocks(n):
        q=s
        for t in range(T):
            N=contingency(P,q)
            if N[0][1]!=N[1][0]: allsym=False
            q=comp(s,q)
    print(f"   n={n}: N(P,sigma^t) symmetric for every power and every binary reader: {allsym}")
print("   k   necklaces  bracelets  chiral?   R3 binary family on a k-cycle")
for kk in range(3,8):
    n=kk; allp=list(permutations(range(n))); s=tuple((x+1)%n for x in range(n))
    cap=set(allp)
    for P in twoblocks(n):
        L=[0]*n
        for i,b in enumerate(P):
            for x in b: L[x]=i
        tgt=itinerary(s,L,2*n)
        cap&={t for t in allp if itinerary(t,L,2*n)==tgt}
    Nn=len(necklaces(kk)); Bb=len(bracelets(kk))
    print(f"   {kk}   {Nn:8d}  {Bb:9d}  {str(Nn>Bb):7s}  |cap|={len(cap)}  exact={cap=={s}}")

print("\n"+"="*74)
print("SECTION 11 / 11A.  families: minimum size, pair density, and the m-block dichotomy")
for n in (5,6):
    allp=list(permutations(range(n)))
    props=[P for P in setparts(range(n)) if 1<len(P)<n]
    mins=set(); dens=[]
    for lam in parts_of(n):
        s=rep_of(lam,n)
        cos=[dcoset(s,blockgens(P,n)) for P in props]
        singles=sum(1 for c in cos if len(c)==1)
        good=tot=0
        for i in range(len(props)):
            for j in range(i+1,len(props)):
                tot+=1; good+= len(cos[i]&cos[j])==1
        mins.add((singles==0, good>0)); dens.append((lam,good,tot))
    print(f"   n={n}: single reader never suffices and some pair always does: {mins=={(True,True)}}")
    print(f"        pair success rate by cycle type: " + ", ".join(f"{l}:{100*g/t:.1f}%" for l,g,t in dens[:4]) + " ...")
    for m in (2,3,4):
        fam=[P for P in setparts(range(n)) if len(P)==m]
        exact=all(len({t for t in allp} & set.intersection(*[dcoset(rep_of(lam,n),blockgens(P,n)) for P in fam]))==1
                  for lam in parts_of(n))
        print(f"        complete {m}-block family ({len(fam):3d} readers): exact for every cycle type = {exact}")
print(f"\nall sections reproduced in {time.time()-T0:.0f}s")

print("\n"+"="*74)
print("SUPERSEDED (kept as Problem-6 data): equal vs unequal K-class sizes inside R3")
print("   n   configs   Case A   Case B   |R3|=|K| in B   divisibility failures")
for n in (4,5,6):
    allP=list(setparts(range(n))); A=B=Bok=viol=0
    for lam in parts_of(n):
        s=rep_of(lam,n); T=order(s)
        pw=[]; q=s
        for _ in range(T): pw.append(q); q=comp(s,q)
        for P in allP:
            K=young_group(P,n); L=lab(P,n); gens=blockgens(P,n)
            R1=dcoset(s,gens); pc=[dcoset(p,gens) for p in pw]
            R2=set()
            for t in R1:
                q=t; ok=True
                for i in range(T):
                    if q not in pc[i]: ok=False; break
                    q=comp(t,q)
                if ok: R2.add(t)
            tgt=itinerary(s,L,2*n)
            R3=set(t for t in R2 if itinerary(t,L,2*n)==tgt)
            G=set(comp(kk,comp(s,inv(kk))) for kk in K)
            rem=set(R3); sizes=[]
            while rem:
                t=next(iter(rem))
                cl=set(comp(kk,comp(t,inv(kk))) for kk in K)
                sizes.append(len(cl)); rem-=cl
            if len(set(sizes))==1 and sizes[0]==len(G): A+=1
            else:
                B+=1
                if len(R3)==len(K): Bok+=1
            if len(R3)%len(G)!=0: viol+=1
    print(f"   {n} {A+B:8d} {A:8d} {B:8d} {Bok:13d} {viol:20d}")

print("\n"+"="*74)
print("THEOREM 5.1.  |R3| = |K| for every sigma and P;  Corollaries 5.2, 5.3;  Prop 5.4")
def imgP(P,s): return [tuple(sorted(s[x] for x in b)) for b in P]
def alignedP(P,s): return set(map(frozenset,P))==set(map(frozenset,imgP(P,s)))
for n in (4,5,6):
    allP=list(setparts(range(n)))
    tot=idok=termok=c2=c4=triv=0
    for lam in parts_of(n):
        s=rep_of(lam,n); T=order(s)
        pw=[]; q=s
        for _ in range(T): pw.append(q); q=comp(s,q)
        for P in allP:
            K=young_group(P,n); L=lab(P,n); gens=blockgens(P,n)
            R1=dcoset(s,gens); pc=[dcoset(p,gens) for p in pw]
            R2=set()
            for t in R1:
                q=t; ok=True
                for i in range(T):
                    if q not in pc[i]: ok=False; break
                    q=comp(t,q)
                if ok: R2.add(t)
            H=2*n; tgt=itinerary(s,L,H)
            R3=set(t for t in R2 if itinerary(t,L,H)==tgt)
            G=set(comp(kk,comp(s,inv(kk))) for kk in K)
            CK=set(kk for kk in K if comp(kk,s)==comp(s,kk))
            words=Counter()
            for x in range(n):
                w=[]; y=x
                for _ in range(H): w.append(L[y]); y=s[y]
                words[tuple(w)]+=1
            assign=1
            for i,b in enumerate(P):
                den=1
                for w,m in words.items():
                    if w[0]==i: den*=factorial(m)
                assign*= factorial(len(b))//den
            bij=1
            for w,m in words.items(): bij*=factorial(m)
            tot+=1
            idok += len(R3)==len(K)
            termok += assign*bij==len(K)==len(R3)
            c2 += (R3==G)==(len(CK)==1)
            a=alignedP(P,s)
            c4 += (a==(len(R1)==len(K))==(R2==R1)==(R3==R1))
            triv += len(CK)==1
    print(f"   n={n}: {tot:5d} configs   |R3|=|K|: {idok}   proof terms match: {termok}"
          f"   Cor 5.3 holds: {c2}   Prop 5.4 holds: {c4}   C_K(sigma) trivial: {triv} ({100*triv/tot:.1f}%)")

print("\n"+"="*74)
print("THEOREM 5.5 / COROLLARY 5.6.  structure of R3 from the word-class shift orbits")
def conj_classes_of_Sm(m):
    out=[]
    def pr(n,mx):
        if n==0: yield (); return
        for kk in range(min(n,mx),0,-1):
            for t in pr(n-kk,kk): yield (kk,)+t
    for lam in pr(m,m):
        c=Counter(lam); d=1
        for l,mu in c.items(): d*=(l**mu)*factorial(mu)
        out.append(factorial(m)//d)
    return out
def pcount(m,mx=None):
    mx=m if mx is None else mx
    if m==0: return 1
    return sum(pcount(m-kk,kk) for kk in range(min(m,mx),0,-1))
for n in (4,5,6):
    allP=list(setparts(range(n))); tot=sz=cnt=corr=0
    for lam in parts_of(n):
        s=rep_of(lam,n); T=order(s)
        pw=[]; q=s
        for _ in range(T): pw.append(q); q=comp(s,q)
        for P in allP:
            K=young_group(P,n); L=lab(P,n); gens=blockgens(P,n)
            R1=dcoset(s,gens); pc=[dcoset(p,gens) for p in pw]
            R2=set()
            for t in R1:
                q=t; ok=True
                for i in range(T):
                    if q not in pc[i]: ok=False; break
                    q=comp(t,q)
                if ok: R2.add(t)
            H=2*n; tgt=itinerary(s,L,H)
            R3=set(t for t in R2 if itinerary(t,L,H)==tgt)
            rem=set(R3); obs=[]
            while rem:
                t=next(iter(rem))
                cl=set(comp(kk,comp(t,inv(kk))) for kk in K)
                obs.append(len(cl)); rem-=cl
            word={}
            for x in range(n):
                w=[]; y=x
                for _ in range(H): w.append(L[y]); y=s[y]
                word[x]=tuple(w)
            cls={}
            for x in range(n): cls.setdefault(word[x],[]).append(x)
            nxt={w: word[s[cls[w][0]]] for w in cls}
            seen=set(); ms=[]
            for w in cls:
                if w in seen: continue
                y=w
                while y not in seen: seen.add(y); y=nxt[y]
                ms.append(len(cls[w]))
            pred=[]
            for combo in itertools.product(*[conj_classes_of_Sm(m) for m in ms]):
                cent=1
                for cs,m in zip(combo,ms): cent*= factorial(m)//cs
                pred.append(len(K)//cent)
            tot+=1
            sz += sorted(obs)==sorted(pred)
            npred=1
            for m in ms: npred*=pcount(m)
            cnt += len(obs)==npred
            corr += (len(set(obs))==1)==(max(ms)<=2)
    print(f"   n={n}: {tot:5d} configs   class-size multiset predicted: {sz}   class count = prod p(m): {cnt}"
          f"   equal sizes iff all word-classes <= 2: {corr}")

print("\n"+"="*74)
print("PROOF STEPS FOR THEOREM 5.5 (holonomy argument)")
print("   S1: K transitive on assignments, stabiliser = prod of symmetric groups on word-classes")
print("   S2: C_K(tau) <= Stab(A_tau)   (tau's own word-classes, not sigma's)")
for n in (4,5,6):
    allP=list(setparts(range(n))); tot=s1=s2=s2wrong=0
    for lam in parts_of(n):
        s=rep_of(lam,n); T=order(s)
        pw=[]; q=s
        for _ in range(T): pw.append(q); q=comp(s,q)
        for P in allP:
            K=young_group(P,n); L=lab(P,n); gens=blockgens(P,n)
            R1=dcoset(s,gens); pc=[dcoset(p,gens) for p in pw]
            R2=set()
            for t in R1:
                q=t; ok=True
                for i in range(T):
                    if q not in pc[i]: ok=False; break
                    q=comp(t,q)
                if ok: R2.add(t)
            H=2*n; tgt=itinerary(s,L,H)
            R3=set(t for t in R2 if itinerary(t,L,H)==tgt)
            def words_of(t):
                d={}
                for x in range(n):
                    w=[]; y=x
                    for _ in range(H): w.append(L[y]); y=t[y]
                    d[x]=tuple(w)
                return d
            ws=words_of(s); cls={}
            for x in range(n): cls.setdefault(ws[x],[]).append(x)
            fib=[kk for kk in K if all(ws[kk[x]]==ws[x] for x in range(n))]
            exp=1
            for w,v in cls.items(): exp*=factorial(len(v))
            assign=1
            for i,b in enumerate(P):
                den=1
                for w,v in cls.items():
                    if w[0]==i: den*=factorial(len(v))
                assign*=factorial(len(b))//den
            tot+=1
            if len(fib)==exp and len(K)//len(fib)==assign: s1+=1
            okc=okw=True
            for t in R3:
                wt=words_of(t)
                for kk in K:
                    if comp(kk,t)==comp(t,kk):
                        if any(wt[kk[x]]!=wt[x] for x in range(n)): okc=False
                        if any(ws[kk[x]]!=ws[x] for x in range(n)): okw=False
            s2+=okc; s2wrong+= not okw
    print(f"   n={n}: {tot:5d} configs   S1: {s1}   S2 (tau's classes): {s2}"
          f"   configs where the sigma-version of S2 fails: {s2wrong}")
