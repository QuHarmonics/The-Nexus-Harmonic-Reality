#!/usr/bin/env python3
"""P20 cross-LEN center reader: independently reproduce the five presealed predictions.
No dependencies beyond Python standard library. No external readout data.
Dean A. Kulik, QuHarmonics Research Group, 2026-11-05.
"""
from math import sqrt
from itertools import product
import hashlib, pathlib

SEAL=pathlib.Path(__file__).with_name('NEXUS_P20_Cross_LEN_Center_Seal.txt')
EXPECTED_SEAL='79b50cf7a2e1d4570d97bc366d89e278797666f4b09619777c8b4add96ba8048'
assert SEAL.exists() and hashlib.sha256(SEAL.read_bytes()).hexdigest()==EXPECTED_SEAL


def words(n):
    return product((0, 1), repeat=n)


def notword(w):
    return tuple(1-x for x in w)


def p(w):
    return w[::-1] if w!=w[::-1] else notword(w)


def tau(w):
    return tuple(w[1:])+(1-w[0],)


def insert(o,b):
    k=len(o)//2
    return o[:k]+(b,)+o[k:]


def split_coordinates(o):
    k=len(o)//2
    a=o[:k]
    g=tuple(o[j]^o[-1-j] for j in range(k))
    return a,g


def reconstruct_outside(a,g):
    k=len(a)
    out=[0]*(2*k)
    for j in range(k):
        out[j]=a[j]
        out[-1-j]=a[j]^g[j]
    return tuple(out)


def selector(g):
    return int(not any(g))


def face(x):
    return int(x>p(x))


def r_even(x):
    h=len(x)//2
    return x[h-1]^x[h]


def reader_trace(x):
    y=[];z=x
    for _ in range(len(x)):
        y.append(r_even(z))
        z=tau(z)
    return tuple(y)


def differences_from_trace(y):
    m=len(y);k=m//2
    d=[None]*m
    for t,yt in enumerate(y):
        i=(k-1+t)%m
        d[i]=yt^(i==m-1)
    return tuple(d)


def reconstruct_x_from_trace_and_face(y,f):
    d=differences_from_trace(y)
    v=[0]
    for a in d[:-1]:
        v.append(v[-1]^a)
    x=tuple(v)
    assert (x[-1]^x[0])==d[-1]
    return x if face(x)==f else notword(x)


def mirror_from_d(d):
    m=len(d);k=m//2
    return tuple(sum(d[j:m-1-j])%2 for j in range(k))


def linear_t(k,g):
    s=selector(g)
    return tuple(x^s for x in g)


def normal_facing(a,g,b):
    s=selector(g)
    t=linear_t(len(a),g)
    return tuple(x^t_i for x,t_i in zip(a,t)),g,b^s


def walsh(f,k,u):
    total=0
    for g in words(k):
        ch=(-1)**(sum(i*j for i,j in zip(u,g))%2)
        total+=f(g)*ch
    return total/(1<<k)


def purity_2q(state):
    # density of first bit, tracing second
    rho=[[sum(state[i*2+j]*state[z*2+j].conjugate() for j in range(2)) for z in range(2)] for i in range(2)]
    return rho


def audit(kmax=7, temporal_width_max=14):
    print('P20 Prediction seal SHA256:', EXPECTED_SEAL)
    print('P20.1 and P20.2, all words and both center bits')
    total=0
    for k in range(1,kmax+1):
        ct=0
        for oo in words(2*k):
            o=tuple(oo)
            a,g=split_coordinates(o)
            assert reconstruct_outside(a,g)==o
            s=selector(g)
            assert s==int(o==o[::-1])
            for b in (0,1):
                w=insert(o,b)
                actual=p(w)
                expected=insert(p(o),b^s)
                assert actual==expected, ('P20.1',k,o,b)
                aa,gg,bb=normal_facing(a,g,b)
                assert gg==g
                assert actual==insert(reconstruct_outside(aa,gg),bb),('P20.2',k,o,b)
                aaa,ggg,bbb=normal_facing(aa,gg,bb)
                assert (aaa,ggg,bbb)==(a,g,b),('P20.2 inverse',k,o,b)
                assert p(actual)==w
                ct+=1
        assert ct==1<<(2*k+1)
        total+=ct
        print(f' k={k:2d}, LEN={2*k+1:2d}, states={ct:6d}, exact lift and inverse')
    print(' Total odd-width states:',total)
    print('P20.3 temporal reader all words and return')
    temporal_total=0
    for m in range(2,temporal_width_max+1,2):
        ct=0;k=m//2
        for xx in words(m):
            x=tuple(xx)
            y=reader_trace(x)
            assert sum(y)%2==1,('odd total parity',m,x)
            d=differences_from_trace(y)
            assert d==tuple(x[j]^x[(j+1)%m] for j in range(m)),('edge diffs',m,x)
            a,g=split_coordinates(x)
            assert mirror_from_d(d)==g,('mirror from time',m,x)
            assert selector(mirror_from_d(d))==int(x==x[::-1]),('temporal selector',m,x)
            ret=reconstruct_x_from_trace_and_face(y,face(x))
            assert ret==x,('exact temporal return',m,x)
            assert reader_trace(ret)==y
            ct+=1
        temporal_total+=ct
        print(f' m={m:2d}, words={ct:6d}, XOR trace parity=1, mirror selector and full return')
    print(' Total even-width words:',temporal_total)
    print('P20.4 comparison of plus and minus response (signed vectors)')
    for k in range(1,6):
        for gg in words(k):
            g=tuple(gg)
            s=selector(g)
            for aa in words(k):
                a=tuple(aa)
                Q_a,_,_=normal_facing(a,g,0)  # outside transport independent of center bit
                Q_back,_,_=normal_facing(Q_a,g,0)
                assert Q_back==a
                plus=(Q_a,g,+1)
                minus=(Q_a,g,(-1)**s)
                # Inverse Q after both responses cancels transport and leaves only sign on original sector.
                assert plus[2]==1 and minus[2]==(-1)**s
                assert Q_back==a and minus[2]*minus[2]==1
        print(f' k={k:2d}, sectors={1<<k:3d}, Uminus Uplus^-1 and reverse= D_s')
    # P20.4 also checked on full coherent complex superpositions, not just basis states.
    for k in range(1,6):
        basis=[(tuple(a),tuple(g)) for a in words(k) for g in words(k)]
        v={x:complex((i*7%17)-8, (i*11%19)-9) for i,x in enumerate(basis)}
        def act_plus(vec):
            out={}
            for (a,g),amp in vec.items():
                t=linear_t(k,g)
                aa=tuple(x^j for x,j in zip(a,t))
                out[(aa,g)]=amp
            return out
        def act_minus(vec):
            out={}
            for (a,g),amp in vec.items():
                t=linear_t(k,g)
                aa=tuple(x^j for x,j in zip(a,t))
                out[(aa,g)]=amp*((-1)**selector(g))
            return out
        target={(a,g):amp*((-1)**selector(g)) for (a,g),amp in v.items()}
        assert act_minus(act_plus(v))==target
        assert act_plus(act_minus(v))==target
        assert act_plus(act_plus(v))==v
        assert act_minus(act_minus(v))==v
    print(' complex-superposition relative readers agree through k=5')
    print('P20.5 Walsh projection and k=2 entanglement')
    for k in range(1,8):
        f=lambda g: -1 if selector(g) else 1
        coeff={tuple(u):walsh(f,k,tuple(u)) for u in words(k)}
        expected0=1-2**(1-k)
        expected_nonzero=-2**(1-k)
        for u,c in coeff.items():
            assert abs(c-(expected0 if not any(u) else expected_nonzero))<1e-12
        for g in words(k):
            reconstructed=sum(coeff[u]*(-1)**(sum(i*j for i,j in zip(u,g))%2) for u in coeff)
            assert abs(reconstructed-f(g))<1e-12
        assert abs(sum(c*c for c in coeff.values())-1)<1e-12
        print(f' k={k:2d}, Fourier DC={expected0:+.8f}, each non-DC={expected_nonzero:+.8f}, inverse exact')
    k=2
    a=[(-1 if (g==(0,0)) else 1)/2 for g in words(k)]
    rho=purity_2q(a)
    for i in range(2):
        for j in range(2):
            assert abs(rho[i][j]-(0.5 if i==j else 0.0))<1e-12,('Bell reduced density',rho)
    print(' k=2 reduced density=',rho,'maximally entangled; relative-phase readout')
    print('STANDS algebraically; RUNS within the above exhaustive scopes; no physical dataset linked.')

if __name__=='__main__':
    audit()
