exec(open('arena_contraction.py').read().split('C=lambda')[0])
C=lambda m:[(i,(i+1)%m) for i in range(m)]
P=lambda m:[(i,i+1) for i in range(m-1)]
Q3=[(v,v^(1<<i)) for v in range(8) for i in range(3) if v<v^(1<<i)]
Pet=[(i,(i+1)%5) for i in range(5)]+[(i,i+5) for i in range(5)]+[(5+i,5+(i+2)%5) for i in range(5)]
def comps(Ar):
    import numpy as np
    return len(Ar.verts)-rank_abs(Ar.d0())
for name,Ep,npr,e0 in [("C7",C(7),7,(0,1)),("C8",C(8),8,(0,1)),("C9",C(9),9,(0,1)),("P7",P(7),7,(2,3)),("Q3",Q3,8,(0,1)),("Pet",Pet,10,(0,1))]:
    a,b=e0; K=3
    Ap=Arena(Ep,npr,K); A0=Arena(Ep,npr,K,allow=lambda S:not {a,b}<=S)
    Rm=np.zeros((len(A0.items),len(Ap.items)))
    for it,i in A0.idx.items(): Rm[i,Ap.idx[it]]=1
    I1=[tuple(range(npr))]
    RP=Ap.residual(I1); R0=A0.residual(I1)
    rr=rank_abs(R0.T@Rm@RP)
    dI=len(Ap.items)-len(A0.items); dV=len(Ap.verts)-len(A0.verts); dc=comps(A0)-comps(Ap)
    # full Aut channel of X' : does it survive collision deletion?
    Gp=autos(Ep,npr); stab=[g for g in Gp if {g[a],g[b]}=={a,b}]
    RPa=Ap.residual(Gp); R0s=A0.residual(stab)
    fa=rank_abs(R0s.T@Rm@RPa) if RPa.shape[1] else 0
    # kernel support: items of ker rho (trivial group) touching a collision config
    M=R0.T@Rm@RP; U,s,Vt=np.linalg.svd(M); kerb=Vt[(s>ATOL).sum():].T if M.shape[1]>rank_abs(M) else np.zeros((RP.shape[1],0))
    # choose representative orthogonal to exact... measure mass on removed items after subtracting best exact fit on A0 part
    print(f"{name}: trivial-group collision loss={RP.shape[1]-rr}  removed items-verts+dcomp={dI-dV+dc}  (removed configs {dV}, items {dI})   full-Aut X' channels {RPa.shape[1]} surviving deletion {fa}")
print("--- do surviving full-Aut channels of X' come from X (lie in im q*)?")
for name,Ep,npr,e0 in [("C7",C(7),7,(0,1)),("C8",C(8),8,(0,1)),("C9",C(9),9,(0,1)),("Q3",Q3,8,(0,1)),("Pet",Pet,10,(0,1))]:
    a,b=e0;K=3
    E,n,lab=contract(Ep,npr,a,b)
    Ap=Arena(Ep,npr,K);A0=Arena(Ep,npr,K,allow=lambda S:not {a,b}<=S);A=Arena(E,n,K)
    Q=np.zeros((len(A.items),len(A0.items)))
    for it in A0.items:
        e,T=it
        if set(e)=={a,b}: continue
        As,Bs=A0.ends(it);qA=frozenset(lab[x] for x in As);qB=frozenset(lab[x] for x in Bs)
        j=(frozenset(lab[x] for x in e),frozenset(lab[x] for x in T));jA,jB=A.ends(j)
        Q[A.idx[j],A0.idx[it]]+=1.0 if (jA,jB)==(qA,qB) else -1.0
    Rm=np.zeros((len(A0.items),len(Ap.items)))
    for it,i in A0.idx.items(): Rm[i,Ap.idx[it]]=1
    Gp=autos(Ep,npr);stab=[g for g in Gp if {g[a],g[b]}=={a,b}]
    Gd=[]
    for g in stab:
        h=[None]*n
        for v in range(npr): h[lab[v]]=lab[g[v]]
        Gd.append(tuple(h))
    RX=A.residual(Gd);R0=A0.residual(stab);RPa=Ap.residual(Gp)
    Iq=colspace(R0@(R0.T@Q.T@RX)); Ia=colspace(R0@(R0.T@Rm@RPa))
    tot=rank_abs(np.hstack([Iq,Ia]))
    print(f"{name}: full-Aut survivors {Ia.shape[1]}, inside im q* {Iq.shape[1]+Ia.shape[1]-tot}")
