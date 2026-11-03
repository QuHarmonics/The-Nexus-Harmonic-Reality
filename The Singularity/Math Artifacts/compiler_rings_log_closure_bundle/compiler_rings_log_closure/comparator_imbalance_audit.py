import numpy as np,math,json,time,random,ast,csv
from fractions import Fraction

def reverse_bits(x,h):return int(format(x,f'0{h}b')[::-1],2) if h else 0

def rectangle(u,v,h):
    H=1<<h
    if u<=0 or v<=0:return 0
    if u>=H:return min(v,H)
    if v>=H:return min(u,H)
    total=0;rho=0
    for j in range(h):
        bit=(u>>(h-1-j))&1
        if bit:
            d=1<<(j+1);total+=(v-rho+d-1)//d;rho+=1<<j
    return total

def delta(p,n):
    if not 0<=p<=1<<n:raise ValueError('threshold out of range')
    if p in (0,1<<n):return 0
    h=n//2;H=1<<h;B=p&(H-1)
    if n%2==0:
        A=p>>h;base=A*(H-A)
    else:
        A=p>>(h+1);c=(p>>h)&1;base=2*A*(H-A)+c*(H-1-2*A)
    return base+B-2*rectangle(B,A,h)-int(reverse_bits(A,h)<B)

def sparse_comparator_spectrum(n):
    h=n//2;out={};outer=[0]
    for j in range(h):
        a=1<<(n-1-j);b=1<<j;coefficient=1<<(n-j-1)
        for s in outer:out[s|a]=coefficient;out[s|b]=-coefficient
        pair=a|b;outer+= [s|pair for s in outer]
    return out

def integrated_character(s,p):
    j=(s&-s).bit_length()-1;B=1<<(j+1);r=p&(B-1)
    sign=-1 if (s&p&~(B-1)).bit_count()%2 else 1
    return sign*min(r,B-r)

def delta_via_tents(p,n):
    numerator=sum(c*integrated_character(s,p) for s,c in sparse_comparator_spectrum(n).items())
    assert numerator%(1<<n)==0
    return numerator//(1<<n)

def reverse_array(x,n):
    y=x.copy().astype(np.uint32);y=((y>>1)&0x55555555)|((y&0x55555555)<<1);y=((y>>2)&0x33333333)|((y&0x33333333)<<2)
    y=((y>>4)&0x0f0f0f0f)|((y&0x0f0f0f0f)<<4);y=((y>>8)&0x00ff00ff)|((y&0x00ff00ff)<<8);y=(y>>16)|(y<<16)
    return y>>(32-n)
LUT=np.array([i.bit_count() for i in range(256)],dtype=np.int16)
def wt(x):return sum(LUT[(x>>(8*j))&255] for j in range(4))
def fwht(values):
    out=np.asarray(values,dtype=np.int64).copy();h=1
    while h<len(out):
        v=out.reshape(-1,2*h);a=v[:,:h].copy();b=v[:,h:].copy();v[:,:h]=a+b;v[:,h:]=a-b;h*=2
    return out

def rect_array(u,v,h):
    total=np.zeros_like(u,dtype=np.int64);rho=np.zeros_like(u,dtype=np.int64)
    for j in range(h):
        bit=(u>>(h-1-j))&1;d=1<<(j+1);total+=bit*((v-rho+d-1)//d);rho+=bit<<j
    return total

def delta_array(p,n):
    h=n//2;H=1<<h;B=(p&(H-1)).astype(np.int64)
    if n%2==0:A=(p>>h).astype(np.int64);base=A*(H-A)
    else:
        A=(p>>(h+1)).astype(np.int64);c=((p>>h)&1).astype(np.int64);base=2*A*(H-A)+c*(H-1-2*A)
    return base+B-2*rect_array(B,A,h)-(reverse_array(A.astype(np.uint32),h)<B).astype(np.int64)

def independent_signed_prefix(p,n):
    if p<=0 or p>=1<<n:return 0
    bound=format(p-1,f'0{n}b');states={(0,0,0):1};cmp=lambda a,b:(a>b)-(a<b)
    for i in range(n//2):
        new={}
        for (left,right,mirror),count in states.items():
            for a in (0,1):
                for b in (0,1):
                    key=(left or cmp(a,int(bound[i])),cmp(b,int(bound[n-1-i])) or right,mirror or cmp(a,b))
                    new[key]=new.get(key,0)+count
        states=new
    result=0
    for (left,right,mirror),count in states.items():
        for c in ((0,1) if n%2 else (None,)):
            order=left
            if n%2:order=order or cmp(c,int(bound[n//2]))
            if (order or right)<=0:result-=mirror*count
    return result

def run():
    start=time.perf_counter();records=[];degree_rows=[];pal_checks=0
    for h in range(1,6):
        H=1<<h
        for u in range(H+1):
            for v in range(H+1):assert rectangle(u,v,h)==sum(reverse_bits(b,h)<v for b in range(u))
    for n in range(2,21):
        N=1<<n;h=n//2;M=1<<h;x=np.arange(N,dtype=np.uint32);r=reverse_array(x,n)
        c=(r>x).astype(np.int64)-(r<x).astype(np.int64);D=np.concatenate(([0],np.cumsum(c)))
        predicted=delta_array(x,n);assert np.array_equal(predicted,D[:-1]);assert D[-1]==0 and np.all(D>=0)
        assert np.array_equal(D,D[::-1]) and np.array_equal(D[:-1][::-1],D[:-1]+c)
        C=fwht(c);DF=fwht(D[:-1]);expected=np.zeros(N,dtype=np.int64);sparse=sparse_comparator_spectrum(n)
        for s,v in sparse.items():expected[s]=v
        assert np.array_equal(C,expected)
        degrees=wt(x);odd=degrees%2==1
        assert np.all(C[~odd]==0) and np.array_equal(C[reverse_array(x,n)],-C)
        assert np.array_equal(2*DF[odd],-C[odd])
        assert np.count_nonzero(C)==2*((1<<h)-1)
        for k in range(h):assert np.count_nonzero(C[degrees==2*k+1])==2*math.comb(h,k+1)
        energy=Fraction(int(np.dot(C,C)),N*N);assert energy==1-Fraction(1,1<<h)
        # Test the posted palindrome-address formula on the actual ring layout.
        P=np.where(r!=x,r,x^(N-1)).astype(np.uint32);a=x[x<P];ring=np.concatenate((a,P[a][::-1]));half=len(a);ring[half-1],ring[half]=ring[half],ring[half-1]
        inverse=np.empty(N,dtype=np.int64);inverse[ring]=np.arange(N)
        pals=x[r==x];lower=pals[pals<N//2].astype(np.int64);u=lower>>(n-(n+1)//2)
        address=(lower+u+D[lower])//2
        assert np.array_equal(inverse[lower],address) and np.array_equal(inverse[N-1-lower],N-1-address)
        pal_checks+=len(pals)
        if n<=12:
            numerator=np.zeros(N,dtype=np.int64);p=x.astype(np.int64)
            for s,coefficient in sparse.items():
                j=(s&-s).bit_length()-1;B=1<<(j+1);rr=p&(B-1);sign=1-2*(wt((x&(s&~(B-1))).astype(np.uint32))%2).astype(np.int64)
                numerator+=coefficient*sign*np.minimum(rr,B-rr)
            assert np.array_equal(numerator,N*D[:-1])
        if n<=16:
            bxy=np.zeros(N,dtype=np.uint32);byx=np.zeros(N,dtype=np.uint32)
            for j in range(n):
                a0=(x>>j)&1;b0=(r>>j)&1;na=1-a0;nb=1-b0
                bxy=(na&b0)^(na&bxy)^(b0&bxy)
                byx=(nb&a0)^(nb&byx)^(a0&byx)
            assert np.array_equal(bxy.astype(np.int64)-byx.astype(np.int64),c)
        records.append({'n':n,'prefix_thresholds_checked':N+1,'nonzero_comparator_Walsh_coefficients':len(sparse),'comparator_spectral_energy':str(energy),'closed_delta_matches_direct_prefix_sum':True,'palindrome_addresses':len(pals),'odd_Delta_spectrum_is_minus_half_comparator':True,'borrow_gate_check':n<=16,'full_tent_check':n<=12})
        for d in range(n+1):
            values=C[degrees==d];degree_rows.append({'n':n,'degree':d,'nonzero_coefficients':int(np.count_nonzero(values)),'integer_spectral_energy':int(np.dot(values,values))})
    rng=random.Random(20261020);wide=[]
    for n in (63,64,127,128,255,256,511,512,1023,1024):
        points=[0,1,(1<<n)//2,(1<<n)-1,1<<n]+[rng.getrandbits(n) for _ in range(4)]
        for p in points:assert delta(p,n)==independent_signed_prefix(p,n)
        wide.append({'n':n,'scalar_thresholds_checked':len(points)})
    for _ in range(64):
        p=rng.randrange((1<<20)+1);assert delta_via_tents(p,20)==delta(p,20)
    report={'scope':'Independent sealed comparator/imbalance audit. User-reported seals and external /tmp scripts are not independently verified. SHA remains parked.','width_checks':records,'total_finite_thresholds':sum(r['prefix_thresholds_checked'] for r in records),'palindrome_address_checks':pal_checks,'wide_scalar_checks':wide,'n20_scalar_tent_checks':64,'seconds':time.perf_counter()-start}
    with open('output/comparator_imbalance_results.json','w') as f:json.dump(report,f,indent=2)
    with open('output/comparator_walsh_degrees.csv','w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=degree_rows[0]);w.writeheader();w.writerows(degree_rows)
    print(json.dumps({'total_thresholds':report['total_finite_thresholds'],'palindrome_addresses':pal_checks,'largest_case':records[-1],'wide_scalar_cases':sum(r['scalar_thresholds_checked'] for r in wide),'seconds':report['seconds']},indent=2))
if __name__=='__main__':run()
