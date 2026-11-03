import itertools, numpy as np
from collections import defaultdict
ATOL=1e-9
def rank_abs(M):
    if M.size==0 or min(M.shape)==0: return 0
    return int((np.linalg.svd(M,compute_uv=False)>ATOL).sum())
def colspace(M):
    if M.size==0 or min(M.shape)==0: return np.zeros((M.shape[0],0))
    U,s,_=np.linalg.svd(M,full_matrices=False); return U[:,s>ATOL]
def autos(E,n):
    Es=set(map(tuple,map(sorted,E))); deg=defaultdict(int); adj=defaultdict(set)
    for u,v in Es: deg[u]+=1;deg[v]+=1;adj[u].add(v);adj[v].add(u)
    out,p,used=[],[None]*n,[False]*n
    def bt(i):
        if i==n: out.append(tuple(p));return
        for c in range(n):
            if used[c] or deg[c]!=deg[i]: continue
            if all((j in adj[i])==(p[j] in adj[c]) for j in range(i)):
                p[i]=c;used[c]=True;bt(i+1);used[c]=False
    bt(0);return out
class Arena:
    def __init__(s,E,n,K,allow=lambda S:True):
        s.n,s.K=n,K; s.E=sorted(set(map(tuple,map(sorted,E))))
        s.verts=[frozenset(S) for S in itertools.combinations(range(n),K) if allow(frozenset(S))]
        s.vi={S:i for i,S in enumerate(s.verts)}
        s.items=[]
        for e in s.E:
            for T in itertools.combinations([x for x in range(n) if x not in e],K-1):
                T=frozenset(T)
                if T|{e[0]} in s.vi and T|{e[1]} in s.vi: s.items.append((frozenset(e),T))
        s.idx={it:i for i,it in enumerate(s.items)}
    def ends(s,it):
        e,T=it;u,w=sorted(e);return T|{u},T|{w}
    def d0(s):
        D=np.zeros((len(s.items),len(s.verts)))
        for it in s.items:
            A,B=s.ends(it);D[s.idx[it],s.vi[B]]+=1;D[s.idx[it],s.vi[A]]-=1
        return D
    def proj(s,G):
        P=np.zeros((len(s.items),)*2)
        for g in G:
            for it in s.items:
                e,T=it;u,w=sorted(e)
                j=(frozenset(g[i] for i in e),frozenset(g[i] for i in T))
                ju,jw=sorted(j[0]); sg=1.0 if (g[u],g[w])==(ju,jw) else -1.0
                P[s.idx[j],s.idx[it]]+=sg/len(G)
        return P
    def residual(s,G):
        P=s.proj(G);Inv=colspace(P);Ex=colspace(P@colspace(s.d0()))
        return colspace(Inv-Ex@(Ex.T@Inv)) if Ex.shape[1] else Inv

def contract(E,n,a,b):              # merge b into a, a<b
    lab={}; k=0
    for v in range(n):
        if v==b: continue
        lab[v]=k;k+=1
    lab[b]=lab[a]
    Ec=set()
    for u,v in map(tuple,map(sorted,E)):
        if {u,v}=={a,b}: continue
        x,y=sorted((lab[u],lab[v])); 
        if (x,y) in Ec: raise ValueError("multi-edge")
        Ec.add((x,y))
    return sorted(Ec),n-1,lab

def run(name,Ep,npr,K,e0):
    a,b=sorted(e0)
    E,n,lab=contract(Ep,npr,a,b)
    Ap=Arena(Ep,npr,K)                                    # X'
    A0=Arena(Ep,npr,K,allow=lambda S:not {a,b}<=S)        # collision-free X'_0
    A =Arena(E,n,K)                                       # X = X'/e
    # q : C_*(A0) -> C_*(A)
    Q=np.zeros((len(A.items),len(A0.items))); QV=np.zeros((len(A.verts),len(A0.verts)))
    for S,i in A0.vi.items(): QV[A.vi[frozenset(lab[x] for x in S)],i]=1
    degen=0
    for it in A0.items:
        e,T=it
        if set(e)=={a,b}: degen+=1; continue
        As,Bs=A0.ends(it); qA=frozenset(lab[x] for x in As); qB=frozenset(lab[x] for x in Bs)
        qe=frozenset(lab[x] for x in e); qT=frozenset(lab[x] for x in T)
        j=(qe,qT); jA,jB=A.ends(j)
        sg=1.0 if (jA,jB)==(qA,qB) else -1.0
        Q[A.idx[j],A0.idx[it]]+=sg
    err=np.abs(A.d0().T@Q-QV@A0.d0().T).max()
    # restriction C^1(A') -> C^1(A0)
    Rm=np.zeros((len(A0.items),len(Ap.items)))
    for it,i in A0.idx.items(): Rm[i,Ap.idx[it]]=1
    Gp=autos(Ep,npr); GX=autos(E,n)
    stab=[g for g in Gp if {g[a],g[b]}=={a,b}]
    Gd=[]
    for g in stab:
        h=[None]*n
        for v in range(npr): h[lab[v]]=lab[g[v]]
        Gd.append(tuple(h))
    assert all(h in set(GX) for h in Gd)
    RX=A.residual(Gd); R0=A0.residual(stab); RP=Ap.residual(stab)
    RXa=A.residual(GX); RPa=Ap.residual(Gp)
    M_q=R0.T@(Q.T@RX); M_r=R0.T@(Rm@RP)
    rq=rank_abs(M_q); rr=rank_abs(M_r)
    # joint: image of q* and image of rho inside R0
    Iq=colspace(R0@M_q) if rq else np.zeros((R0.shape[0],0))
    Ir=colspace(R0@M_r) if rr else np.zeros((R0.shape[0],0))
    both=rank_abs(np.hstack([Iq,Ir])) if (rq or rr) else 0
    inter=rq+rr-both
    print(f"\n### {name} K={K} contract {e0}  |E'|={len(Ep)} -> |E|={len(E)}")
    print(f"  configs X'={len(Ap.verts)} X'_0={len(A0.verts)} X={len(A.verts)}  items X'={len(Ap.items)} X'_0={len(A0.items)} (degenerate {degen}) X={len(A.items)}")
    print(f"  chain map q on X'_0: max|dq-qd|={err:.1e}")
    print(f"  |Aut X'|={len(Gp)} |Aut X|={len(GX)} |stab|={len(stab)}")
    print(f"  dim R: X'@Aut={RPa.shape[1]} X'@stab={RP.shape[1]} X'_0@stab={R0.shape[1]} X@stab={RX.shape[1]} X@Aut={RXa.shape[1]}")
    print(f"  q*_R  : R_X({RX.shape[1]}) -> R_X'0({R0.shape[1]})  rank={rq} ker={RX.shape[1]-rq}")
    print(f"  rho_R : R_X'({RP.shape[1]}) -> R_X'0({R0.shape[1]})  rank={rr} ker(collision loss)={RP.shape[1]-rr}")
    print(f"  in R_X'0: im q* ∩ im rho = {inter}   im q*+im rho = {both}   uncovered = {R0.shape[1]-both}")
    return dict(RX=RX.shape[1],R0=R0.shape[1],RP=RP.shape[1],rq=rq,rr=rr,inter=inter,both=both,err=err)

C=lambda m:[(i,(i+1)%m) for i in range(m)]
P=lambda m:[(i,i+1) for i in range(m-1)]
Q3=[(v,v^(1<<i)) for v in range(8) for i in range(3) if v<v^(1<<i)]
Pet=[(i,(i+1)%5) for i in range(5)]+[(i,i+5) for i in range(5)]+[(5+i,5+(i+2)%5) for i in range(5)]
K33=[(i,j) for i in range(3) for j in range(3,6)]
Q3s=[e for e in Q3 if e!=(0,1)]+[(0,8),(1,8)]
import sys
run("C7 -> C6",C(7),7,3,(0,1))
run("C8 -> C7",C(8),8,3,(0,1))
run("C9 -> C8",C(9),9,3,(0,1))
run("P7 -> P6",P(7),7,3,(2,3))
run("Q3' -> Q3 (undo subdivision)",Q3s,9,3,(0,8))
run("Q3 -> Q3/e",Q3,8,3,(0,1))
run("K33 -> K33/e",K33,6,3,(0,3))
run("Petersen -> Pet/e",Pet,10,3,(0,1))
