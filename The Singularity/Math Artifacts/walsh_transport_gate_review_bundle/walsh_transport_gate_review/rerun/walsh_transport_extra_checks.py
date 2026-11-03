import numpy as np,json
from walsh_transport_audit import ring,reverse,wt,fwht

def run():
    r=ring(5);positions=np.flatnonzero(r==reverse(r,5));u=np.arange(8,dtype=np.int64)
    a=1-(u&1);b=(u>>1)&1;c=(u>>2)&1;majority=(a&b)^(a&c)^(b&c)
    assert np.array_equal(positions,4*u+2*c+majority)
    out=[]
    for n in (10,11,19,20):
        m=(n+1)//2;N=1<<n;M=1<<m;r=ring(n);pal=r==reverse(r,n);idx=np.flatnonzero(pal);u=np.arange(M,dtype=np.uint32)
        Z=(2*wt(r)-n).astype(np.int64);F=fwht(Z);A=np.empty((N,m),dtype=np.int64)
        for j in range(m):
            f=np.zeros(N,dtype=np.int64);f[idx]=1-2*((u>>j)&1).astype(np.int64);A[:,j]=fwht(f)
        numerators=A.T@F;denominator=N*M
        assert np.all(numerators%denominator==0)
        coefficients=numerators//denominator
        assert np.array_equal(coefficients,[-1 if n%2 and j==0 else -2 for j in range(m)])
        assert np.array_equal(A@coefficients,fwht(np.where(pal,Z,0)))
        out.append({'n':n,'coefficients':coefficients.tolist(),'exact':True})
    return out
if __name__=='__main__':print(json.dumps(run(),indent=2))
