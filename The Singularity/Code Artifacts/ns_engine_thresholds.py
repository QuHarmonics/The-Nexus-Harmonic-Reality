import numpy as np, time, json, sys

def run(N, Re, T=10.0, cfl=0.4, nsamp=11, verbose=False):
    nu=1.0/Re
    k1=np.fft.fftfreq(N,1.0/N)
    kz=np.fft.rfftfreq(N,1.0/N)
    KX,KY,KZ=np.meshgrid(k1,k1,kz,indexing='ij')
    K2=KX**2+KY**2+KZ**2; K2i=1.0/np.where(K2==0,1,K2); K2i[0,0,0]=0
    kmax=N//3
    mask=(np.abs(KX)<kmax)&(np.abs(KY)<kmax)&(np.abs(KZ)<kmax)
    x=np.linspace(0,2*np.pi,N,endpoint=False)
    X,Y,Z=np.meshgrid(x,x,x,indexing='ij')
    u=np.sin(X)*np.cos(Y)*np.cos(Z)
    v=-np.cos(X)*np.sin(Y)*np.cos(Z)
    w=np.zeros_like(u)
    AX=(0,1,2)
    F=lambda f: np.fft.rfftn(f,axes=AX); Fi=lambda f: np.fft.irfftn(f,s=(N,N,N),axes=AX)
    U=[F(u),F(v),F(w)]
    def project(A):
        div=KX*A[0]+KY*A[1]+KZ*A[2]
        return [A[0]-KX*div*K2i, A[1]-KY*div*K2i, A[2]-KZ*div*K2i]
    U=project(U)
    def curlF(A):
        return [1j*(KY*A[2]-KZ*A[1]), 1j*(KZ*A[0]-KX*A[2]), 1j*(KX*A[1]-KY*A[0])]
    def nonlin(A):
        ua=[Fi(a) for a in A]; W=curlF(A); wa=[Fi(a) for a in W]
        cx=ua[1]*wa[2]-ua[2]*wa[1]
        cy=ua[2]*wa[0]-ua[0]*wa[2]
        cz=ua[0]*wa[1]-ua[1]*wa[0]
        C=[F(cx)*mask,F(cy)*mask,F(cz)*mask]
        return project(C), ua, wa
    def diag(A):
        ua=[Fi(a) for a in A]; W=curlF(A); wa=[Fi(a) for a in W]
        G=np.empty((N,N,N,3,3))
        for i in range(3):
            for j in range(3):
                G[...,i,j]=Fi(1j*[KX,KY,KZ][j]*A[i])
        S=0.5*(G+np.swapaxes(G,-1,-2))
        lam,vec=np.linalg.eigh(S)          # ascending
        l3,l2,l1=lam[...,0],lam[...,1],lam[...,2]
        e3,e2,e1=vec[...,0],vec[...,1],vec[...,2]
        om=np.stack(wa,axis=-1); w2=np.sum(om**2,axis=-1)
        nrm=np.sqrt(np.maximum(w2,1e-30))
        c1=np.abs(np.sum(om*e1,axis=-1))/nrm
        c2=np.abs(np.sum(om*e2,axis=-1))/nrm
        c3=np.abs(np.sum(om*e3,axis=-1))/nrm
        Sw=np.einsum('...ij,...j->...i',S,om)
        prod=np.sum(om*Sw,axis=-1)
        P=prod.mean(); Plock=(l1*w2).mean()
        ens=0.5*w2.mean()
        # exhaust: nu * <|grad omega|^2>.  irfftn returns a real field, so f**2 is |f|**2.
        exh=0.0
        for a in wa:
            Wa=F(a)
            g=Fi(1j*KX*Wa)**2+Fi(1j*KY*Wa)**2+Fi(1j*KZ*Wa)**2
            exh+=g.mean()
        exh*=nu
        locked=(w2*(c1>0.9)).sum()/w2.sum()
        Lthr={f'L{int(th*100)}':float((w2*(c1>th)).sum()/w2.sum()) for th in (0.70,0.75,0.80,0.85,0.90,0.95,0.98)}
        ke=0.5*sum((q**2).mean() for q in ua)
        divmax=float(np.abs(Fi(1j*(KX*A[0]+KY*A[1]+KZ*A[2]))).max())
        eps=nu*w2.mean()
        eta=(nu**3/max(eps,1e-30))**0.25
        return dict(**Lthr,ens=float(ens),ke=float(ke),div=divmax,P=float(P),Plock=float(Plock),
                    D=float(P/Plock) if Plock>0 else 0.0,
                    EXH=float(exh), PEXH=float(P/exh) if exh>0 else 0.0,
                    c1=float((w2*c1).sum()/w2.sum()),
                    c2=float((w2*c2).sum()/w2.sum()),
                    c3=float((w2*c3).sum()/w2.sum()),
                    locked=float(locked), trS=float(np.abs(np.trace(S,axis1=-2,axis2=-1)).max()),
                    kmax_eta=float(kmax*eta), eps=float(eps))
    samples=np.linspace(0,T,nsamp); si=0; out=[]
    t=0.0; t0=time.time()
    while t<T-1e-12:
        ua=[Fi(a) for a in U]
        umax=max(np.abs(a).max() for a in ua)
        dt=min(cfl*(2*np.pi/N)/max(umax,1e-9), 0.05, T-t)
        if si<nsamp and t>=samples[si]-1e-9:
            d=diag(U); d['t']=t; out.append(d); si+=1
            if verbose: print(f"  t={t:5.2f} ens={d['ens']:.4f} D={d['D']:.4f} lock={d['locked']:.4f} kmax*eta={d['kmax_eta']:.2f}",flush=True)
        IF=np.exp(-nu*K2*dt)              # exact viscous integrating factor
        Nl,_,_=nonlin(U)
        U1=[IF*(U[i]+dt*Nl[i]) for i in range(3)]
        Nl1,_,_=nonlin(U1)
        U=[IF*(U[i]+0.5*dt*Nl[i])+0.5*dt*Nl1[i] for i in range(3)]
        t+=dt
    d=diag(U); d['t']=t; out.append(d)
    if verbose: print(f"  t={t:5.2f} ens={d['ens']:.4f} D={d['D']:.4f} lock={d['locked']:.4f}",flush=True)
    return out, time.time()-t0

if __name__=="__main__":
    N=int(sys.argv[1]); Re=float(sys.argv[2])
    o,el=run(N,Re,verbose=True)
    print(f"N={N} Re={Re} elapsed {el:.1f}s")
    json.dump(o,open(f"dns_N{N}_Re{int(Re)}.json","w"))
