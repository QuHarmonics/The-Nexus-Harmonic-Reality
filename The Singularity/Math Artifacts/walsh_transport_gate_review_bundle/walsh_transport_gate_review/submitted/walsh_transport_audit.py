import numpy as np,math,json,ast,time,csv
from fractions import Fraction

def reverse(x,n):
 y=x.copy().astype(np.uint32);y=((y>>1)&0x55555555)|((y&0x55555555)<<1);y=((y>>2)&0x33333333)|((y&0x33333333)<<2)
 y=((y>>4)&0x0f0f0f0f)|((y&0x0f0f0f0f)<<4);y=((y>>8)&0x00ff00ff)|((y&0x00ff00ff)<<8);y=(y>>16)|(y<<16)
 return y>>(32-n)
def partner(x,n):
 r=reverse(x,n)
 return np.where(r!=x,r,x^((1<<n)-1)).astype(np.uint32)
def ring(n):
 x=np.arange(1<<n,dtype=np.uint32);a=x[x<partner(x,n)];out=np.concatenate((a,partner(a,n)[::-1]));M=len(a)
 if n>1:out[M-1],out[M]=out[M],out[M-1]
 return out
LUT=np.array([i.bit_count() for i in range(256)],dtype=np.int16)
def wt(x):return sum(LUT[(x>>(8*j))&255] for j in range(4))
def fwht(x):
 y=np.asarray(x,dtype=np.int64).copy();h=1
 while h<len(y):
  v=y.reshape(-1,2*h);a=v[:,:h].copy();b=v[:,h:].copy();v[:,:h]=a+b;v[:,h:]=a-b;h*=2
 return y

def run():
 start=time.perf_counter();original={};tree=ast.parse(open('pairs_forced.py').read())
 exec(compile(ast.Module(body=[n for n in tree.body if isinstance(n,ast.FunctionDef) and n.name in ('partner','grow')],type_ignores=[]),'original','exec'),original)
 for n in range(1,11):assert [format(int(x),f'0{n}b') for x in ring(n)]==original['grow'](n)
 complete=[];singletons=[];first_mixing=None;degree_rows=[]
 for n in range(2,21):
  m=(n+1)//2;N=1<<n;M=1<<m;r=ring(n);pal=r==reverse(r,n);positions=np.flatnonzero(pal);u=np.arange(M,dtype=np.uint32)
  assert len(positions)==M and np.array_equal(r[pal]>>(n-m),u)
  assert np.array_equal(positions[::-1],N-1-positions)
  degrees=wt(np.arange(N,dtype=np.uint32));small_degrees=wt(u)
  if n<=12:
   C=np.empty((N,M),dtype=np.int16)
   for t in range(M):
    f=np.zeros(N,dtype=np.int64);f[positions]=1-2*(wt(u&t)%2).astype(np.int64);C[:,t]=fwht(f)
   bad=(degrees[:,None]%2)!=(small_degrees[None,:]%2)
   assert not np.any(C[bad])
   C64=C.astype(np.int64);gram=C64.T@C64
   assert np.array_equal(gram,N*M*np.eye(M,dtype=np.int64))
   nonzero=np.count_nonzero(C,axis=1)
   if first_mixing is None and np.any(nonzero>1):
    s=int(np.flatnonzero(nonzero>1)[0]);ts=np.flatnonzero(C[s])
    first_mixing={'n':n,'half_width':m,'full_character_index':s,'full_character_bits':format(s,f'0{n}b'),'full_character_degree':s.bit_count(),'compressed_terms':[{'index':int(t),'bits':format(int(t),f'0{m}b'),'degree':int(t).bit_count(),'coefficient':str(Fraction(int(C[s,t]),M))} for t in ts]}
   complete.append({'n':n,'matrix_rows':N,'matrix_columns':M,'all_parity_forbidden_entries_zero':True,'exact_integer_gram_is_NM_identity':True,'characters_with_multiple_compressed_terms':int(np.count_nonzero(nonzero>1)),'maximum_terms_per_pulled_back_character':int(nonzero.max())})
   del C,C64,gram,bad
  cols=np.empty((N,m),dtype=np.int16);prediction=np.zeros(N,dtype=np.int64)
  for j in range(m):
   f=np.zeros(N,dtype=np.int64);f[positions]=1-2*((u>>j)&1).astype(np.int64);col=fwht(f);cols[:,j]=col
   assert np.all(col[degrees%2==0]==0)
   coefficient=-1 if n%2 and j==0 else -2
   prediction+=coefficient*col
  twice_z=(2*wt(r)-n).astype(np.int64);carrier=np.where(pal,twice_z,0);direct=fwht(carrier)
  assert np.array_equal(prediction,direct)
  A=cols.astype(np.int64);assert np.array_equal(A.T@A,N*M*np.eye(m,dtype=np.int64))
  singletons.append({'n':n,'half_width':m,'basis_columns_used':m,'all_carrier_coefficients_reconstructed':N,'exact_reconstruction':True,'singleton_columns_orthogonal':True,'direct_carrier_nonzero_coefficients':int(np.count_nonzero(direct))})
  for d in range(n+1):
   values=direct[degrees==d];energy=int(np.dot(values,values));degree_rows.append({'n':n,'degree':d,'carrier_integer_spectral_energy':energy})
  del A,cols
 report={'scope':'Original-ring palindrome character transport; not a SHA inversion or a physical interpretation.','normalization':'C_st=sum_u (-1)^(s dot i_n(u)+t dot u). T=C/sqrt(2^n*2^m).','complete_matrix_checks':complete,'singleton_carrier_checks':singletons,'first_degree_mixing_example':first_mixing,'seconds':time.perf_counter()-start}
 with open('output/walsh_transport_results.json','w') as f:json.dump(report,f,indent=2)
 with open('output/walsh_transport_degree_energy.csv','w',newline='') as f:
  w=csv.DictWriter(f,fieldnames=degree_rows[0]);w.writeheader();w.writerows(degree_rows)
 print(json.dumps({'complete_matrices':complete,'first_mixing':first_mixing,'largest_singleton_case':singletons[-1],'seconds':report['seconds']},indent=2))
if __name__=='__main__':run()
