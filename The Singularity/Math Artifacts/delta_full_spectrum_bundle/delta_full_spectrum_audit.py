import numpy as np,math,json,time,csv,random
from fractions import Fraction

LUT=np.array([i.bit_count() for i in range(256)],dtype=np.int16)
def wt(x):return sum(LUT[(x>>(8*j))&255] for j in range(4))
def reverse_array(x,n):
 y=x.copy().astype(np.uint32);y=((y>>1)&0x55555555)|((y&0x55555555)<<1);y=((y>>2)&0x33333333)|((y&0x33333333)<<2)
 y=((y>>4)&0x0f0f0f0f)|((y&0x0f0f0f0f)<<4);y=((y>>8)&0x00ff00ff)|((y&0x00ff00ff)<<8);y=(y>>16)|(y<<16)
 return y>>(32-n)
def fwht(x):
 y=np.asarray(x,dtype=np.int64).copy();h=1
 while h<len(y):
  v=y.reshape(-1,2*h);a=v[:,:h].copy();b=v[:,h:].copy();v[:,:h]=a+b;v[:,h:]=a-b;h*=2
 return y

def comparator_from_reversed_mode(s,rs,n):
 d=s^rs
 if d.bit_count()!=2:return 0
 j=(d&-d).bit_length()-1
 width=n-2*j-2
 if width and ((s>>(j+1))&((1<<width)-1)):return 0
 sign=1 if (s>>(n-1-j))&1 else -1
 return sign*(1<<(n-j-1))

def comparator_coefficient(s,n):
 if not 0<=s<1<<n:raise ValueError('mode outside word width')
 rs=int(format(s,f'0{n}b')[::-1],2)
 return comparator_from_reversed_mode(s,rs,n)

def delta_coefficient(s,n):
 if n<1 or not 0<=s<1<<n:raise ValueError('invalid mode or width')
 N=1<<n
 if s==0:
  numerator=N*(4*N-3*n-4-(n&1));assert numerator%24==0
  return numerator//24
 rs=int(format(s,f'0{n}b')[::-1],2)
 if s.bit_count()%2:
  value=-comparator_from_reversed_mode(s,rs,n);assert value%2==0
  return value//2
 j=(s&-s).bit_length()-1
 value=-(1<<j)*comparator_from_reversed_mode(s^(1<<j),rs^(1<<(n-1-j)),n)
 for k in range(j):
  value+=(1<<k)*comparator_from_reversed_mode(s^(1<<k),rs^(1<<(n-1-k)),n)
 assert value%2==0
 return value//2

def sparse_comparator(n):
 result={};outer=[0]
 for j in range(n//2):
  high=1<<(n-1-j);low=1<<j;v=1<<(n-j-1)
  for mask in outer:result[mask|high]=v;result[mask|low]=-v
  outer += [mask|high|low for mask in outer]
 return result

def direct_kernel(n):
 N=1<<n;x=np.arange(N,dtype=np.uint32);count=0
 for s in range(1,N):
  char=1-2*(wt(x&s)%2).astype(np.int64);prefix=np.cumsum(char);Knum=2*fwht(prefix)
  assert np.all(Knum%N==0)
  actual=Knum//N;expected=np.zeros(N,dtype=np.int64);j=(s&-s).bit_length()-1
  expected[s]=1;expected[s^(1<<j)]=1<<j
  for k in range(j):expected[s^(1<<k)]=-(1<<k)
  assert np.array_equal(actual,expected);count+=1
 return count

def independent_mode_from_tents(s,n):
 N=1<<n;answer=Fraction(0)
 for t,coefficient in sparse_comparator(n).items():
  l=(t&-t).bit_length()-1;B=1<<(l+1)
  if (s>>(l+1))!=(t>>(l+1)):continue
  # Inclusive interval integration is evaluated directly on one dyadic block.
  block=sum(min(r,B-r)*(1 if (s&r).bit_count()%2==0 else -1) for r in range(B))
  answer+=Fraction(coefficient*block,B)
 assert answer.denominator==1
 return int(answer)

def run():
 start=time.perf_counter();records=[];kernel_rows=0;examples=[];degree_rows=[]
 for n in range(2,21):
  N=1<<n;x=np.arange(N,dtype=np.uint32);r=reverse_array(x,n);c=(r>x).astype(np.int64)-(r<x).astype(np.int64)
  D=np.concatenate(([0],np.cumsum(c)))[:-1];C=fwht(c);F=fwht(D)
  sparse=np.zeros(N,dtype=np.int64)
  for s,v in sparse_comparator(n).items():sparse[s]=v
  assert np.array_equal(C,sparse)
  degrees=wt(x);odd=degrees%2==1;expected2=np.zeros(N,dtype=np.int64);expected2[odd]=-C[odd]
  for j in range(n):
   idx=np.arange(1<<j,N,1<<(j+1),dtype=np.int64);idx=idx[degrees[idx]%2==0]
   expected2[idx]=-(1<<j)*C[idx^(1<<j)]
   for k in range(j):expected2[idx]+=(1<<k)*C[idx^(1<<k)]
  dc=delta_coefficient(0,n);expected2[0]=2*dc
  assert np.array_equal(expected2,2*F)
  # DC is checked independently as pair distances, direct prefix area, and singleton moment.
  pair_area=int(np.sum((r[x<r]-x[x<r]).astype(np.int64)))
  singleton_moment=Fraction(0)
  for k in range(n):singleton_moment+=Fraction(1<<k,2)*int(C[1<<k])
  assert pair_area==int(D.sum())==dc==singleton_moment
  assert dc==Fraction(N*N,6)*(1-Fraction(1,4**(n//2)))-Fraction(N*(n//2),4)
  if n<=10:kernel_rows+=direct_kernel(n)
  # Exhaustive scalar evaluator checks through n=12; deterministic selection afterward.
  modes=list(range(N)) if n<=12 else [0,1,2,3,N-1,N//2]+list(sparse_comparator(n))[:32]
  for s in modes:
   assert comparator_coefficient(s,n)==int(C[s]) and delta_coefficient(s,n)==int(F[s])
  records.append({'n':n,'all_Delta_modes_checked':N,'nonzero_Delta_modes':int(np.count_nonzero(F)),'DC':dc,'DC_four_forms_agree':True,'scalar_modes_checked':len(modes),'nonzero_comparator_modes':int(np.count_nonzero(C))})
  if n in (2,3,4):examples.append({'n':n,'comparator_spectrum':C.tolist(),'Delta_spectrum':F.tolist()})
  for d in range(n+1):
   v=F[degrees==d];degree_rows.append({'n':n,'degree':d,'nonzero_Delta_coefficients':int(np.count_nonzero(v))})
 # A nontrivial audit of the coefficient reader without a full-width spectrum.
 wide=[];rng=random.Random(20261020)
 for n in (32,64,128,256,512,1024):
  for _ in range(12):
   j=rng.randrange(n//2);mask=0
   for k in range(j):
    if rng.randrange(2):mask|=(1<<k)|(1<<(n-1-k))
   t=mask|(1<<(n-1-j));v=1<<(n-j-1)
   assert comparator_coefficient(t,n)==v
   assert delta_coefficient(t,n)==-v//2
   # Force an even mode with least bit 0: it must read t through the half coefficient.
   if not t&1:
    assert delta_coefficient(t^1,n)==-v//2
  wide.append({'n':n,'constructed_nonzero_odd_modes':12,'no_full_array':True})
 # Compare against a separate direct dyadic-tent integration on manageable but wider cases.
 for n in (13,14):
  modes=[0]+[rng.randrange(1<<n) for _ in range(24)]
  for s in modes:assert delta_coefficient(s,n)==independent_mode_from_tents(s,n)
 report={'scope':'Exact unnormalized Walsh spectrum of the reversal comparator prefix sum. No claim about physical spectra or SHA inversion.','normalization':'hat f(s)=sum_x f(x)(-1)^(s dot x).','records':records,'complete_Delta_modes':sum(r['all_Delta_modes_checked'] for r in records),'complete_nonzero_kernel_rows':kernel_rows,'kernel_row_widths':[2,10],'small_spectra':examples,'wide_scalar_checks':wide,'independent_tent_mode_checks':50,'seconds':time.perf_counter()-start}
 with open('output/delta_full_spectrum_results.json','w') as f:json.dump(report,f,indent=2)
 with open('output/delta_full_spectrum_degree_counts.csv','w',newline='') as f:
  w=csv.DictWriter(f,fieldnames=degree_rows[0]);w.writeheader();w.writerows(degree_rows)
 print(json.dumps({'all_modes_checked':report['complete_Delta_modes'],'kernel_rows':kernel_rows,'largest_case':records[-1],'small_spectra':examples[:2],'seconds':report['seconds']},indent=2))
if __name__=='__main__':run()
