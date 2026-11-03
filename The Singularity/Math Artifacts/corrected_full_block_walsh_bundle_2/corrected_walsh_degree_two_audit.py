import numpy as np,math,ast,json,csv,time
from fractions import Fraction

def rev_bits(x,h):return int(format(x,f'0{h}b')[::-1],2) if h else 0
def partner_int(x,n):
 r=rev_bits(x,n);return r if r!=x else x^((1<<n)-1)
def select_reversal(S,i):
 residue=0
 for j in range((S-1).bit_length()):
  count0=max(0,(S-1-residue)//(1<<(j+1))+1)
  if i>=count0:i-=count0;residue+=1<<j
 assert i==0 and residue<S
 return residue

def word_at(i,n):
 if n==1:return i
 M=1<<(n-1);h=n//2;H=1<<h;nu=1 if n%2==0 else 2;q=i-M if i>=M else M-1-i;Q=q//nu
 boundary=(H//2)*(H//2-1)//2
 K=(1+math.isqrt(1+8*Q))//2 if Q<boundary else (math.isqrt(1+8*(Q+H//2))-1)//2
 S=K+int(K>=H//2);D=K*(K-1)//2+max(0,K-H//2);offset=q-nu*D
 if nu==1:middle=None;local=offset
 else:middle=int(offset<S);local=offset if middle else offset-S
 r=select_reversal(S,local);A=H-1-K;B=H-1-rev_bits(r,h)
 a=A*H+B if middle is None else (2*A+middle)*H+B
 return a if ((i>=M)==(q==0)) else partner_int(a,n)

def radial(u,n):
 x=u*(1<<n);i=x.numerator//x.denominator;f=x-i;k=n*f.numerator//f.denominator
 w=word_at(i,n)
 return (w>>(n-1-k))&1,i,k,w

def rev_array(x,n):
 y=x.copy().astype(np.uint32);y=((y>>1)&0x55555555)|((y&0x55555555)<<1);y=((y>>2)&0x33333333)|((y&0x33333333)<<2)
 y=((y>>4)&0x0f0f0f0f)|((y&0x0f0f0f0f)<<4);y=((y>>8)&0x00ff00ff)|((y&0x00ff00ff)<<8);y=(y>>16)|(y<<16)
 return y>>(32-n)
def partner_array(x,n):
 r=rev_array(x,n);return np.where(r!=x,r,x^((1<<n)-1)).astype(np.uint32)
def ring(n):
 x=np.arange(1<<n,dtype=np.uint32);p=partner_array(x,n);a=x[x<p];out=np.concatenate((a,p[a][::-1]));M=len(a)
 if n>1:out[M-1],out[M]=out[M],out[M-1]
 return out
LUT=np.array([i.bit_count() for i in range(256)],dtype=np.int16)
def wt(x):return sum(LUT[(x>>(8*j))&255] for j in range(4))
def fwht(values):
 out=np.asarray(values,dtype=np.int64).copy();h=1
 while h<len(out):
  v=out.reshape(-1,2*h);a=v[:,:h].copy();b=v[:,h:].copy();v[:,:h]=a+b;v[:,h:]=a-b;h*=2
 return out

def run():
 start=time.perf_counter();original={};tree=ast.parse(open('pairs_forced.py').read())
 exec(compile(ast.Module(body=[n for n in tree.body if isinstance(n,ast.FunctionDef) and n.name in ('partner','grow')],type_ignores=[]),'original','exec'),original)
 for n in range(1,11):
  expected=original['grow'](n)
  assert all(word_at(i,n)==int(w,2) for i,w in enumerate(expected))
  assert [format(int(x),f'0{n}b') for x in ring(n)]==expected
 records=[];degree_rows=[];counter=None;block_example=[]
 for n in range(2,21):
  N=1<<n;M=N//2;h=n//2;H=1<<h;R=ring(n);pal=R==rev_array(R,n);Z=(2*wt(R)-n).astype(np.int64);body=np.where(pal,0,Z)
  qpred=[];badq=np.zeros(M,dtype=np.int64)
  for K in range(1,H):
   S=K+int(K>=H//2);D=K*(K-1)//2+max(0,K-H//2)
   rr=np.arange(S,dtype=np.uint32);rr=rr[np.argsort(rev_array(rr,h),kind='stable')]
   for mu in ((None,) if n%2==0 else (1,0)):
    deficits=K.bit_count()+wt(rr)+(0 if mu is None else 1-mu)
    value=np.where(rr==K,0,n-2*deficits);qpred.extend(value.tolist())
   if n%2==0:
    compressed=np.arange(K,dtype=np.uint32);compressed=compressed[np.argsort(rev_array(compressed,h),kind='stable')]
    badq[D:D+K]=n-2*K.bit_count()-2*wt(compressed)
   if n==6 and K==4:
    for local,r in enumerate(rr):
     a=((H-1-K)<<h)|(H-1-int(rev_array(np.array([r],dtype=np.uint32),h)[0]))
     block_example.append({'local_i':local,'label_r':int(r),'canonical_word':format(a,'06b'),'center_depth':D+local,'mask':int(r<K),'even_body_z':0 if r==K else (n-2*K.bit_count()-2*int(r).bit_count())/2})
  B=np.array(qpred,dtype=np.int64);assert len(B)==M and np.array_equal(body,np.concatenate((B[::-1],B)))
  F=fwht(Z);E=fwht(body);G=fwht(B);q=np.arange(M,dtype=np.uint32);dq=wt(q);s_even=q|((dq%2).astype(np.uint32)<<(n-1))
  predicted=np.zeros(N,dtype=np.int64);predicted[s_even]=2*(1-2*(dq%2).astype(np.int64))*G
  assert np.array_equal(predicted,E)
  degrees=wt(np.arange(N,dtype=np.uint32));power=F*F;epower=E*E
  total=int(power.sum());body_energy=int(epower.sum());e2=int(epower[degrees==2].sum());e1=int(power[degrees==1].sum())
  q1=int(np.dot(G[dq==1],G[dq==1]));q2=int(np.dot(G[dq==2],G[dq==2]));assert e2==4*(q1+q2)
  energies=[]
  for d in range(n+1):
   full_energy=int(power[degrees==d].sum());even_energy=int(epower[degrees==d].sum());energies.append(full_energy)
   degree_rows.append({'n':n,'degree':d,'full_twice_latitude_spectral_energy':full_energy,'body_twice_latitude_spectral_energy':even_energy,'full_energy_share':str(Fraction(full_energy,total))})
  bad_mismatches=None
  if n%2==0:
   badF=fwht(np.concatenate((badq[::-1],badq)));even=(degrees%2==0);bad_mismatches=int(np.count_nonzero(badF[even]!=E[even]))
   if bad_mismatches and counter is None:
    s=int(np.flatnonzero((badF!=E)&even)[0]);counter={'n':n,'mode':s,'bits':format(s,f'0{n}b'),'actual_coefficient':int(E[s])//2,'unmasked_formula_coefficient':int(badF[s])//2}
  records.append({'n':n,'full_coefficients_checked':N,'corrected_block_formula_exact':True,'center_out_degree_mapping_exact':True,'degree_two_share_full':str(Fraction(e2,total)),'degree_two_share_full_percent':100*e2/total,'degree_two_share_body':str(Fraction(e2,body_energy)) if body_energy else None,'degree_two_share_body_percent':100*e2/body_energy if body_energy else None,'degree_one_share_full_percent':100*e1/total,'largest_full_energy_degree':int(np.argmax(energies)),'full_nonzero_coefficients':int(np.count_nonzero(F)),'body_nonzero_coefficients':int(np.count_nonzero(E)),'participation_ratio_full_approx':float(total)**2/float(np.dot(power.astype(float),power.astype(float))),'center_out_degree_one_share_body_percent':100*4*q1/body_energy if body_energy else None,'center_out_degree_two_share_body_percent':100*4*q2/body_energy if body_energy else None,'unmasked_even_formula_mismatches':bad_mismatches})
 u=Fraction(49,128);b,i,k,w=radial(u,4)
 assert b==0 and k==0 and u>Fraction(3,8)
 front={'u':str(u),'L':4,'scaled_u':str(16*u),'address':i,'fractional_part':'1/8','slice':k,'word':format(w,'04b'),'actual_bit':b,'tau':'1-sqrt(15)/8','tau_first_bit':1}
 certificates=[]
 for D in range(13,97):
  p=2*D//3+1;u=Fraction(1,2)+Fraction(1,1<<p)+Fraction(2,3*(1<<(D-1)));target='100'+'1'*(D-5)+'00';failure=None
  for L in range(1,D+1):
   b,i,k,w=radial(u,L)
   if b!=int(target[L-1]) and failure is None:failure={'L':L,'address':str(i),'slice':k,'word':format(w,f'0{L}b'),'actual':b,'expected':int(target[L-1])}
  certificates.append({'D':D,'residue':D%3,'pass':failure is None,'first_failure':failure})
 report={'scope':'Corrected full-block formulas and finite degree-energy measurements; no proof of asymptotic degree-two dominance, radial nonregularity, or physical quantum interpretation.','normalization':'Unnormalized Walsh transforms. Energies computed exactly from twice-latitude; ratios equal those for z. Participation ratio is approximate and explicitly defined.','records':records,'all_coefficients_checked':sum(r['full_coefficients_checked'] for r in records),'block_hole_example':block_example,'first_unmasked_counterexample':counter,'square_root_counterexample':front,'certificate_summary':{str(r):{'tested':sum(t['residue']==r for t in certificates),'passed':sum(t['residue']==r and t['pass'] for t in certificates)} for r in range(3)},'certificate_cases':certificates,'seconds':time.perf_counter()-start}
 with open('output/corrected_walsh_degree_two_results.json','w') as f:json.dump(report,f,indent=2)
 with open('output/corrected_walsh_degree_energy.csv','w',newline='') as f:
  writer=csv.DictWriter(f,fieldnames=degree_rows[0]);writer.writeheader();writer.writerows(degree_rows)
 print(json.dumps({'selected_results':[r for r in records if r['n'] in (6,8,10,12,16,20)],'first_unmasked_counterexample':counter,'block_example':block_example,'certificate_summary':report['certificate_summary'],'seconds':report['seconds']},indent=2))
if __name__=='__main__':run()
