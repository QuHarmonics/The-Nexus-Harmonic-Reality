import numpy as np,math,json,ast,time,csv
from fractions import Fraction

def rev(x,n):
 y=x.copy().astype(np.uint32);y=((y>>1)&0x55555555)|((y&0x55555555)<<1);y=((y>>2)&0x33333333)|((y&0x33333333)<<2)
 y=((y>>4)&0x0f0f0f0f)|((y&0x0f0f0f0f)<<4);y=((y>>8)&0x00ff00ff)|((y&0x00ff00ff)<<8);y=(y>>16)|(y<<16)
 return y>>(32-n)
def partner(x,n):
 r=rev(x,n)
 return np.where(r!=x,r,x^((1<<n)-1)).astype(np.uint32)
def ring(n):
 x=np.arange(1<<n,dtype=np.uint32);a=x[x<partner(x,n)];r=np.concatenate((a,partner(a,n)[::-1]));M=len(a)
 if n>1:r[M-1],r[M]=r[M],r[M-1]
 return r
LUT=np.array([i.bit_count() for i in range(256)],dtype=np.int16)
def wt(x):return sum(LUT[(x>>(8*j))&255] for j in range(4))
def fwht(values):
 out=np.asarray(values,dtype=np.int64).copy();h=1
 while h<len(out):
  a=out.reshape(-1,2*h);left=a[:,:h].copy();right=a[:,h:].copy();a[:,:h]=left+right;a[:,h:]=left-right;h*=2
 return out

def run():
 start=time.perf_counter();original={};tree=ast.parse(open('pairs_forced.py').read())
 exec(compile(ast.Module(body=[n for n in tree.body if isinstance(n,ast.FunctionDef) and n.name in ('partner','grow')],type_ignores=[]),'original','exec'),original)
 for n in range(1,11):assert [format(int(x),f'0{n}b') for x in ring(n)]==original['grow'](n)
 records=[];examples=[];energy_rows=[]
 for n in range(2,21):
  r=ring(n);N=len(r);m=(n+1)//2;pal=r==rev(r,n);u=(r[pal]>>(n-m)).astype(np.uint32)
  assert np.array_equal(u,np.arange(1<<m,dtype=np.uint32))
  half=ring(m);literal=np.array_equal(u,half);assert literal==(n==2)
  Z=(2*wt(r)-n).astype(np.int64);body=np.where(pal,0,Z);carrier=np.where(pal,Z,0)
  assert np.array_equal(body,body[::-1]) and np.array_equal(carrier,-carrier[::-1])
  F=fwht(Z);Fc=fwht(carrier);degrees=wt(np.arange(N,dtype=np.uint32));even=degrees%2==0
  assert np.all(Fc[even]==0) and np.all((F-Fc)[~even]==0)
  assert np.array_equal(Fc,np.where(even,0,F))
  total=int(np.dot(Z,Z));palenergy=int(np.dot(carrier,carrier));share=Fraction(palenergy,total)
  if n%2==0:expected=Fraction(2,1<<(n//2))
  else:
   h=n//2;expected=Fraction(4*h+1,(2*h+1)*(1<<h))
  assert share==expected
  naturalZ=(4*wt(u)-2*m) if n%2==0 else (4*wt(u)-2*(u&1).astype(np.int16)-(2*m-1))
  assert np.array_equal(Z[pal],naturalZ)
  native_half_Z=(2*wt(half)-m).astype(np.int64)
  readdressed=naturalZ[half]
  predicted=2*native_half_Z if n%2==0 else 2*native_half_Z+1-2*(half&1).astype(np.int16)
  assert np.array_equal(readdressed,predicted)
  compressed=fwht(naturalZ);small_degree=wt(np.arange(1<<m,dtype=np.uint32))
  assert np.all(compressed[small_degree!=1]==0)
  full_degrees=[]
  for d in range(n+1):
   energy=int(np.dot(Fc[degrees==d],Fc[degrees==d]))
   if energy:full_degrees.append(d)
   energy_rows.append({'n':n,'Walsh_degree':d,'unnormalized_palindrome_carrier_spectral_energy':energy})
  # Native small-ring partner and parent-palindrome complement induce distinct maps in general.
  small_inverse=np.empty(1<<m,dtype=np.int64);small_inverse[half]=np.arange(1<<m)
  complement_reader=small_inverse[half^((1<<m)-1)]
  native_partner_reader=(1<<m)-1-np.arange(1<<m)
  mismatch=int(np.count_nonzero(complement_reader!=native_partner_reader))
  records.append({'n':n,'half_width':m,'palindromes':int(pal.sum()),'natural_halfword_order_ascending':True,'literal_order_matches_smaller_ring':bool(literal),'energy_fraction':str(share),'expected_energy_fraction':str(expected),'full_carrier_nonzero_Walsh_degrees':full_degrees,'compressed_halfword_Walsh_support_degree_one_only':True,'readdressed_waveform_identity':True,'complement_vs_native_half_partner_mismatches':mismatch})
  if n in (3,4,6):
   examples.append({'n':n,'palindrome_words':[format(int(x),f'0{n}b') for x in r[pal]],'halfword_values':u.tolist(),'smaller_ring_order':half.tolist(),'palindrome_twice_z':Z[pal].tolist(),'complement_reader_permutation':complement_reader.tolist(),'native_partner_reader_permutation':native_partner_reader.tolist()})
 report={'scope':'Independent finite audit from original grow/partner ordering. The two given /tmp/r4 files and their seal were not supplied.','convention':'Integer twice-latitude Z=2w-n; unnormalized Walsh transform; energy fractions unaffected by this scaling.','checks':records,'examples':examples,'seconds':time.perf_counter()-start}
 with open('output/palindrome_half_width_results.json','w') as f:json.dump(report,f,indent=2)
 with open('output/palindrome_walsh_degree_energy.csv','w',newline='') as f:
  w=csv.DictWriter(f,fieldnames=energy_rows[0]);w.writeheader();w.writerows(energy_rows)
 print(json.dumps({'records':records,'small_examples':examples[:2],'seconds':report['seconds']},indent=2))
if __name__=='__main__':run()
