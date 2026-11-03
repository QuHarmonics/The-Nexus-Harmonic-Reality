import itertools, numpy as np
from collections import defaultdict, Counter
ATOL=1e-9
def rank_abs(M):
    if M.size==0 or min(M.shape)==0: return 0
    return int((np.linalg.svd(M,compute_uv=False)>ATOL).sum())
def colspace(M):
    if M.size==0 or min(M.shape)==0: return np.zeros((M.shape[0],0))
    U,s,_=np.linalg.svd(M,full_matrices=False); return U[:,s>ATOL]
def nullspace(M, ncols):
    if M.size==0 or min(M.shape)==0: return np.eye(ncols)
    U,s,Vt=np.linalg.svd(M); r=int((s>ATOL).sum()); return Vt[r:].T
def meet(U,V):
    if U.shape[1]==0 or V.shape[1]==0: return 0
    return U.shape[1]+V.shape[1]-rank_abs(np.hstack([U,V]))
def autos(E,n):
    Es=set(map(tuple,map(sorted,E)));deg=defaultdict(int);adj=defaultdict(set)
    for u,v in Es: deg[u]+=1;deg[v]+=1;adj[u].add(v);adj[v].add(u)
    out,p,used=[],[None]*n,[False]*n
    def bt(i):
        if i==n: out.append(tuple(p));return
        for c in range(n):
            if used[c] or deg[c]!=deg[i]: continue
            if all((j in adj[i])==(p[j] in adj[c]) for j in range(i)):
                p[i]=c;used[c]=True;bt(i+1);used[c]=False
    bt(0);return out

class MArena:
    """K-token arena with per-site capacity; configurations are multisets (sorted tuples)."""
    def __init__(s,E,n,K,cap=None,allow=lambda S:True):
        s.n,s.K=n,K; cap=cap or {}; s.cap=[cap.get(v,1) for v in range(n)]
        s.E=sorted(set(map(tuple,map(sorted,E))))
        ok=lambda S: all(c<=s.cap[v] for v,c in Counter(S).items())
        s.verts=[S for S in itertools.combinations_with_replacement(range(n),K) if ok(S) and allow(S)]
        s.vi={S:i for i,S in enumerate(s.verts)}
        s.items=[]
        for e in s.E:
            for T in itertools.combinations_with_replacement(range(n),K-1):
                A=tuple(sorted(T+(e[0],))); B=tuple(sorted(T+(e[1],)))
                if A in s.vi and B in s.vi: s.items.append((e,T))
        s.idx={it:i for i,it in enumerate(s.items)}
    def ends(s,it):
        e,T=it; return tuple(sorted(T+(e[0],))), tuple(sorted(T+(e[1],)))
    def d0(s):
        D=np.zeros((len(s.items),len(s.verts)))
        for it in s.items:
            A,B=s.ends(it); D[s.idx[it],s.vi[B]]+=1; D[s.idx[it],s.vi[A]]-=1
        return D
    def comps(s): return len(s.verts)-rank_abs(s.d0())
    def proj(s,G):
        P=np.zeros((len(s.items),)*2)
        for g in G:
            for it in s.items:
                e,T=it; ge=(g[e[0]],g[e[1]])
                j=(tuple(sorted(ge)),tuple(sorted(g[x] for x in T)))
                sg=1.0 if ge[0]<ge[1] else -1.0
                P[s.idx[j],s.idx[it]]+=sg/len(G)
        return P
    def split(s,G):
        """returns (Inv basis, invariant-exact basis, residual basis)"""
        P=s.proj(G); Inv=colspace(P); Ex=colspace(P@colspace(s.d0()))
        R=colspace(Inv-Ex@(Ex.T@Inv)) if Ex.shape[1] else Inv
        return Inv,Ex,R

def contract_lab(E,n,a,b):
    lab,k={},0
    for v in range(n):
        if v==b: continue
        lab[v]=k;k+=1
    lab[b]=lab[a]; Ec=set()
    for u,v in map(tuple,map(sorted,E)):
        if {u,v}=={a,b}: continue
        x,y=sorted((lab[u],lab[v]))
        if (x,y) in Ec: raise ValueError("multi-edge")
        Ec.add((x,y))
    return sorted(Ec),n-1,lab

def chain(Asrc,Atgt,lab):
    """q: C_*(Asrc)->C_*(Atgt) by relabelling; degenerate items -> 0. Returns Q, error."""
    Q=np.zeros((len(Atgt.items),len(Asrc.items))); QV=np.zeros((len(Atgt.verts),len(Asrc.verts)))
    for S,i in Asrc.vi.items(): QV[Atgt.vi[tuple(sorted(lab[x] for x in S))],i]=1
    for it in Asrc.items:
        e,T=it; ge=(lab[e[0]],lab[e[1]])
        if ge[0]==ge[1]: continue
        j=(tuple(sorted(ge)),tuple(sorted(lab[x] for x in T)))
        Q[Atgt.idx[j],Asrc.idx[it]]+=1.0 if ge[0]<ge[1] else -1.0
    err=np.abs(Atgt.d0().T@Q-QV@Asrc.d0().T).max()
    return Q,err

def restr(Asub,Abig):
    Rm=np.zeros((len(Asub.items),len(Abig.items)))
    for it,i in Asub.idx.items(): Rm[i,Abig.idx[it]]=1
    return Rm

def run(name,Ep,npr,K,e0,verbose=True):
    a,b=sorted(e0); E,n,lab=contract_lab(Ep,npr,a,b); m=lab[a]
    Xp =MArena(Ep,npr,K)
    X0 =MArena(Ep,npr,K,allow=lambda S: not (a in S and b in S))
    X1 =MArena(E,n,K)                      # capacity 1 at m
    X2 =MArena(E,n,K,cap={m:2})            # capacity 2 at m
    Q2,e2=chain(Xp,X2,lab); Q1,e1=chain(X0,X1,lab)
    Rm=restr(X0,Xp); Sm=restr(X1,X2)
    sq=np.abs(Rm@Q2.T - Q1.T@Sm).max()     # cochain square rho q2* = q1* sigma
    Gp=autos(Ep,npr); stab=[g for g in Gp if {g[a],g[b]}=={a,b}]
    Gd=[]
    for g in stab:
        h=[None]*n
        for v in range(npr): h[lab[v]]=lab[g[v]]
        Gd.append(tuple(h))
    assert all(h in set(autos(E,n)) for h in Gd)
    _,_,RP=Xp.split(stab); _,_,R0=X0.split(stab); _,_,R1=X1.split(Gd); _,_,R2=X2.split(Gd)
    q2=RP.T@Q2.T@R2; q1=R0.T@Q1.T@R1; rho=R0.T@Rm@RP; sig=R1.T@Sm@R2
    Kr=nullspace(rho,RP.shape[1]); Ks=nullspace(sig,R2.shape[1])     # coordinates
    Kr_c=RP@Kr; Ks_img=RP@(q2@Ks)                                    # in C^1(X')
    im_q2=colspace(RP@q2)
    out=dict(name=name,e1=e1,e2=e2,sq=sq,
        V=(len(Xp.verts),len(X0.verts),len(X1.verts),len(X2.verts)),
        I=(len(Xp.items),len(X0.items),len(X1.items),len(X2.items)),
        R=(RP.shape[1],R0.shape[1],R1.shape[1],R2.shape[1]),
        rq2=rank_abs(q2), rq1=rank_abs(q1), kr=Kr.shape[1], ks=Ks.shape[1],
        sq_ker=rank_abs(Ks_img), ker_meet=meet(colspace(Ks_img),Kr_c) if Ks_img.size else 0,
        kr_in_imq2=meet(Kr_c,im_q2),
        cokq2=RP.shape[1]-rank_abs(q2),
        dc=(X0.comps()-Xp.comps(), X1.comps()-X2.comps()))
    # trivial-group counts vs Euler, both sides
    I1p=[tuple(range(npr))]; I1d=[tuple(range(n))]
    _,_,a_=Xp.split(I1p); _,_,b_=X0.split(I1p); _,_,c_=X1.split(I1d); _,_,d_=X2.split(I1d)
    out['kr1']=a_.shape[1]-rank_abs(b_.T@Rm@a_); out['ks1']=d_.shape[1]-rank_abs(c_.T@Sm@d_)
    out['eul_up']=len(Xp.items)-len(X0.items)-(len(Xp.verts)-len(X0.verts))
    out['eul_dn']=len(X2.items)-len(X1.items)-(len(X2.verts)-len(X1.verts))
    # support: kernel of rho realised by cochains supported on removed items (mod exact, invariant)
    Inv,Ex,_=Xp.split(stab)
    rem=[Xp.idx[it] for it in Xp.items if it not in X0.idx]
    Sup=np.zeros((len(Xp.items),len(rem)))
    for k,i in enumerate(rem): Sup[i,k]=1
    Pg=Xp.proj(stab); SupInv=colspace(Pg@Sup)
    cls=colspace(SupInv-Ex@(Ex.T@SupInv)) if Ex.shape[1] else SupInv
    out['sup_dim']=cls.shape[1]; out['sup_eq_ker']=meet(cls,Kr_c)
    if verbose:
        o=out
        print(f"\n### {name}  contract {e0} -> site {m} ")
        print(f"  configs X'={o['V'][0]} X'_0={o['V'][1]} X(cap1)={o['V'][2]} X(cap2)={o['V'][3]}   items {o['I']}")
        print(f"  chain maps: q1 {e1:.1e}  q2 {e2:.1e}   square rho∘q2* = q1*∘sigma (cochains) {sq:.1e}")
        print(f"  dim R (stab): X'={o['R'][0]} X'_0={o['R'][1]} X_cap1={o['R'][2]} X_cap2={o['R'][3]}   Δcomp up/down {o['dc']}")
        print(f"  cap2  q2*_R: R_X2({o['R'][3]}) -> R_X'({o['R'][0]}) rank={o['rq2']} ker={o['R'][3]-o['rq2']} coker={o['cokq2']}")
        print(f"  cap1  q1*_R: R_X1({o['R'][2]}) -> R_X'0({o['R'][1]}) rank={o['rq1']} ker={o['R'][2]-o['rq1']}")
        print(f"  ker rho (upstairs collision) = {o['kr']}    ker sigma (downstairs exclusion) = {o['ks']}")
        print(f"  q2* on ker sigma: rank {o['sq_ker']}, lands inside ker rho: {o['ker_meet']}")
        print(f"  ker rho inside im q2* : {o['kr_in_imq2']} of {o['kr']}")
        print(f"  ker rho = classes supported on removed items: support classes {o['sup_dim']}, meet {o['sup_eq_ker']}")
        print(f"  trivial group: ker rho={o['kr1']} (Euler up {o['eul_up']})   ker sigma={o['ks1']} (Euler down {o['eul_dn']})")
    return out

C=lambda m:[(i,(i+1)%m) for i in range(m)]
P=lambda m:[(i,i+1) for i in range(m-1)]
Q3=[(v,v^(1<<i)) for v in range(8) for i in range(3) if v<v^(1<<i)]
Q3s=[e for e in Q3 if e!=(0,1)]+[(0,8),(1,8)]
K33=[(i,j) for i in range(3) for j in range(3,6)]
Pet=[(i,(i+1)%5) for i in range(5)]+[(i,i+5) for i in range(5)]+[(5+i,5+(i+2)%5) for i in range(5)]
cases=[("C7 -> C6",C(7),7,(0,1)),("C8 -> C7",C(8),8,(0,1)),("C9 -> C8",C(9),9,(0,1)),
       ("P7 -> P6",P(7),7,(2,3)),("Q3' -> Q3",Q3s,9,(0,8)),("Q3 -> Q3/e",Q3,8,(0,1)),
       ("K33 -> K33/e",K33,6,(0,3)),("Petersen -> Pet/e",Pet,10,(0,1))]
if __name__=="__main__":
    res=[run(nm,E,n,3,e0) for nm,E,n,e0 in cases]
