from mpmath import mp
import json

COUNT = {
    'words': lambda L: 1<<L,
    'pairs': lambda L: 1<<(L-1),
    'palindromes': lambda L: 1<<((L+1)//2),
    'slices': lambda L: L*(1<<L),
    'roots': lambda L: (1 if L==1 else 2 if L==2 else 3*(1<<(L-3))),
}

def series(kind,z,dps):
    q=2*abs(z)
    if not 0<q<1:raise ValueError('require 0<abs(z)<1/2')
    N=1;threshold=mp.power(10,-dps-20)
    while q**(N+1)*((N+1)-N*q)/(1-q)**2 >= threshold:N+=1
    return mp.fsum(mp.mpf(COUNT[kind](L))*z**L for L in range(1,N+1))

def point(which):
    return mp.pi/20 if which=='pi' else mp.e/20

def basis(kind,dps,which='pi'):
    z=point(which);A=series(kind,z,dps)
    if kind=='pairs':return mp.matrix([A,z*A,z])
    if kind=='palindromes':return mp.matrix([A,z*z*A,z,z*z])
    if kind=='slices':return mp.matrix([A,z*A,z*z*A,z])
    if kind=='roots':return mp.matrix([A,z*A,z,z**3])
    raise ValueError(kind)

def search(kind,dps=100,maxcoeff=1000):
    with mp.workdps(dps):
        rel=mp.pslq(basis(kind,dps),tol=mp.power(10,-dps+15),maxcoeff=maxcoeff,maxsteps=10000)
        if rel is not None and next(c for c in rel if c)!=abs(next(c for c in rel if c)):
            rel=[-c for c in rel]
    return rel

def validate(kind,rel,dps,which):
    with mp.workdps(dps):
        v=basis(kind,dps,which)
        residual=abs(mp.fsum(mp.mpf(c)*x for c,x in zip(rel,v)))
        return {'dps':dps,'point':which+'/20','absolute_residual':mp.nstr(residual,12),
                'passed':bool(residual<mp.power(10,-dps+8))}

def run():
    expected={'pairs':[1,-2,-1],'palindromes':[1,-2,-2,-2],
              'slices':[1,-4,4,-2],'roots':[1,-2,-1,1]}
    result={}
    for kind in expected:
        rel=search(kind)
        assert rel==expected[kind],(kind,rel)
        tests=[validate(kind,rel,dps,p) for dps in (100,200,300) for p in ('pi','e')]
        assert all(x['passed'] for x in tests)
        result[kind]={'relation':rel,'validation':tests}
    with mp.workdps(100):
        s=mp.mpc(mp.mpf(1)/2,mp.mpf(1)/2)
        constants={'norm_squared':(s*mp.conj(s)).real,'eighth_power_real':(s**8).real,
                   'limiting_mean_depth':mp.fsum(mp.power(4,-d) for d in range(1,240)),
                   'base4_count_series':mp.fsum(mp.mpf(k)*mp.power(4,-k-1) for k in range(240))}
        controls={}
        for name,value in constants.items():
            rel=mp.pslq(mp.matrix([mp.mpf(1),value]),tol=mp.mpf('1e-85'),maxcoeff=1000,maxsteps=10000)
            if rel[0]<0:rel=[-c for c in rel]
            controls[name]={'value':mp.nstr(value,30),'relation_on_1_value':rel}
        result['fold_controls']=controls
    return result

if __name__=='__main__':
    print(json.dumps(run(),indent=2))
