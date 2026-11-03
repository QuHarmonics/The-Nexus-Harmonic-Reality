import math,ast,json,time,csv
from fractions import Fraction
import numpy as np
import sympy as sp

def reverse_bits(x,h):return int(format(x,f'0{h}b')[::-1],2) if h else 0
def partner(x,n):
 r=reverse_bits(x,n);return r if r!=x else x^((1<<n)-1)
def select_reversal(S,i):
 residue=0
 for j in range((S-1).bit_length()):
  c=max(0,(S-1-residue)//(1<<(j+1))+1)
  if i>=c:i-=c;residue+=1<<j
 assert i==0 and residue<S
 return residue

def word_at(i,n):
 if n==1:return i
 N=1<<n;M=N//2;q=i-M if i>=M else M-1-i;h=n//2;H=1<<h;nu=1 if n%2==0 else 2;Q=q//nu;boundary=(H//2)*(H//2-1)//2
 K=(1+math.isqrt(1+8*Q))//2 if Q<boundary else (math.isqrt(1+8*(Q+H//2))-1)//2
 S=K+int(K>=H//2);D=K*(K-1)//2+max(0,K-H//2);t=q-nu*D
 if nu==1:middle=None;local=t
 else:middle=int(t<S);local=t if middle else t-S
 r=select_reversal(S,local);A=H-1-K;B=H-1-reverse_bits(r,h)
 a=A*H+B if middle is None else (2*A+middle)*H+B
 return a if ((i>=M)==(q==0)) else partner(a,n)

def radial(u,L):
 value=u*(1<<L);i=value.numerator//value.denominator;frac=value-i;k=(L*frac.numerator)//frac.denominator
 word=word_at(i,L);bit=(word>>(L-1-k))&1
 return bit,i,k,word

def fwht(x):
 y=np.asarray(x,dtype=np.int64).copy();h=1
 while h<len(y):
  v=y.reshape(-1,2*h);a=v[:,:h].copy();b=v[:,h:].copy();v[:,:h]=a+b;v[:,h:]=a-b;h*=2
 return y

def run():
 start=time.perf_counter();original={};tree=ast.parse(open('pairs_forced.py').read())
 exec(compile(ast.Module(body=[n for n in tree.body if isinstance(n,ast.FunctionDef) and n.name in ('partner','grow')],type_ignores=[]),'original','exec'),original)
 for n in range(1,11):assert all(word_at(i,n)==int(w,2) for i,w in enumerate(original['grow'](n)))
 # An exact algebraic test of the displayed root product.
 z=sp.symbols('z');roots=[sp.cos(2*sp.pi*k/8)+sp.I*sp.sin(2*sp.pi*k/8) for k in range(8)]
 product=sp.simplify(sp.expand(sp.prod(z-r for r in roots)))
 assert product==z**8-1
 root_report={'standard_zeta_definition':'exp(2*pi*i/n)','n':8,'p':2,'actual_product':int(product.subs(z,2)),'claimed_product':2**4-1,'product_polynomial':str(product),'p3_unit_distance_lower_bound':2,'p2_m1_n8_squared_distance':str(sp.simplify(abs(2-roots[1])**2))}
 # Exact front-bit counterexample, avoiding square-root floating-point arithmetic.
 u=Fraction(49,128);bit,i,k,word=radial(u,4)
 predicted=int(u>Fraction(3,8));assert k<2 and bit==0 and predicted==1
 front={'L':4,'u':str(u),'address':i,'slice':k,'word':format(word,'04b'),'actual_bit':bit,'tau_expression':'1-sqrt(15)/8','tau_first_bit':predicted,'strictly_above_tau_half_threshold':True}
 block_tests=[];first_failure=None
 for n in (4,6,8,10,12):
  H=1<<(n//2);M=1<<(n-1);N=1<<n;actual=np.zeros(N,dtype=np.int64);bad=np.zeros(N,dtype=np.int64);fixed=np.zeros(N,dtype=np.int64)
  for pos in range(N):
   w=word_at(pos,n)
   actual[pos]=0 if w==reverse_bits(w,n) else 2*w.bit_count()-n
  for K in range(1,H):
   D=K*(K-1)//2+max(0,K-H//2)
   compressed=sorted(range(K),key=lambda r:reverse_bits(r,n//2))
   for j,r in enumerate(compressed):
    Z=n-2*K.bit_count()-2*r.bit_count();rank=M-1-(D+j)
    bad[rank]=Z;bad[N-1-rank]=Z
   S=K+int(K>=H//2);full=sorted(range(S),key=lambda r:reverse_bits(r,n//2))
   for j,r in enumerate(full):
    if r==K:continue
    Z=n-2*K.bit_count()-2*r.bit_count();rank=M-1-(D+j)
    fixed[rank]=Z;fixed[N-1-rank]=Z
  F=fwht(actual);B=fwht(bad);C=fwht(fixed);assert np.array_equal(C,F)
  even=[s for s in range(N) if s.bit_count()%2==0];wrong=[s for s in even if B[s]!=F[s]]
  if wrong and first_failure is None:
   s=wrong[0];first_failure={'n':n,'mode':s,'mode_bits':format(s,f'0{n}b'),'degree':s.bit_count(),'actual_Walsh_z_body':int(F[s])//2,'displayed_compressed_block_formula':int(B[s])//2,'corrected_block_formula':int(C[s])//2}
  block_tests.append({'n':n,'even_modes_checked':len(even),'displayed_formula_mismatches':len(wrong),'palindrome_masked_full_block_formula_mismatches':0})
 certificates=[]
 for D in range(13,97):
  p=(2*D)//3+1;angle=Fraction(1,2)+Fraction(1,1<<p)+Fraction(2,3*(1<<(D-1)))
  target='100'+'1'*(D-5)+'00';observed=[];detail=[]
  for L in range(1,D+1):
   b,ii,kk,ww=radial(angle,L);observed.append(str(b))
   if b!=int(target[L-1]):detail.append({'L':L,'expected':int(target[L-1]),'actual':b,'word_address':str(ii),'slice':kk,'word':format(ww,f'0{L}b')})
  certificates.append({'D':D,'residue_mod_3':D%3,'p':p,'angle':str(angle),'matches_full_target':not detail,'first_mismatch':detail[0] if detail else None})
 # Standard quantum-state distinction at the same classical parity readout.
 phi=sp.Matrix([1,0,0,1])/sp.sqrt(2);rho=phi*phi.T;mixture=sp.diag(sp.Rational(1,2),0,0,sp.Rational(1,2))
 assert list(rho.diagonal())==list(mixture.diagonal()) and rho!=mixture
 def pt(matrix):
  out=sp.zeros(4)
  for a in (0,1):
   for b in (0,1):
    for c in (0,1):
     for d in (0,1):out[2*a+d,2*c+b]=matrix[2*a+b,2*c+d]
  return out
 bell={'identical_computational_populations':[str(x) for x in rho.diagonal()],'Bell_offdiagonal_00_11':str(rho[0,3]),'mixture_offdiagonal_00_11':str(mixture[0,3]),'Bell_partial_transpose_eigenvalues':{str(k):v for k,v in pt(rho).eigenvals().items()},'mixture_partial_transpose_eigenvalues':{str(k):v for k,v in pt(mixture).eigenvals().items()}}
 report={'scope':'Audit of formulas visible in the draft; not an execution of unprovided corpus scripts or an audit of truncated final sections.','root_product':root_report,'finite_square_root_counterexample':front,'body_spectrum_block_checks':block_tests,'first_body_spectrum_counterexample':first_failure,'radial_certificate_checks':certificates,'certificate_summary':{str(r):{'tested':sum(c['residue_mod_3']==r for c in certificates),'passed':sum(c['residue_mod_3']==r and c['matches_full_target'] for c in certificates)} for r in range(3)},'Bell_pair_vs_mixture':bell,'seconds':time.perf_counter()-start}
 with open('output/quantum_closure_draft_audit_results.json','w') as f:json.dump(report,f,indent=2)
 print(json.dumps({'root_product':root_report,'front_counterexample':front,'body_counterexample':first_failure,'certificate_summary':report['certificate_summary'],'first_certificate_failures':[c for c in certificates if not c['matches_full_target']][:4],'Bell_vs_mixture':bell,'seconds':report['seconds']},indent=2))
if __name__=='__main__':run()
