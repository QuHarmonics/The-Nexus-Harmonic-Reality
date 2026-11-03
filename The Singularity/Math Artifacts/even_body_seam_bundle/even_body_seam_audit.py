import numpy as np,math,json,csv,ast,time,random
from fractions import Fraction

def reverse_bits(x,h):return int(format(x,f'0{h}b')[::-1],2)
def reverse_array(x,n):
 y=x.copy().astype(np.uint32);y=((y>>1)&0x55555555)|((y&0x55555555)<<1);y=((y>>2)&0x33333333)|((y&0x33333333)<<2)
 y=((y>>4)&0x0f0f0f0f)|((y&0x0f0f0f0f)<<4);y=((y>>8)&0x00ff00ff)|((y&0x00ff00ff)<<8);y=(y>>16)|(y<<16)
 return y>>(32-n)
def partner_array(x,n):
 r=reverse_array(x,n);return np.where(r!=x,r,x^((1<<n)-1)).astype(np.uint32)
def ring(n):
 x=np.arange(1<<n,dtype=np.uint32);a=x[x<partner_array(x,n)];out=np.concatenate((a,partner_array(a,n)[::-1]));M=len(a)
 if n>1:out[M-1],out[M]=out[M],out[M-1]
 return out
LUT=np.array([i.bit_count() for i in range(256)],dtype=np.int16)
def wt(x):return sum(LUT[(x>>(8*k))&255] for k in range(4))

def reverse_order_select(K,i):
 if not 0<=i<K:raise ValueError('within-block index out of range')
 residue=0
 for j in range((K-1).bit_length()):
  d=1<<(j+1);count0=max(0,(K-1-residue)//d+1)
  if i>=count0:i-=count0;residue+=1<<j
 assert residue<K and i==0
 return residue

def seam_profile(n,q):
 h=n//2;H=1<<h
 if n%2==0:
  K=(1+math.isqrt(1+8*q))//2;i=q-K*(K-1)//2;mu=None
 else:
  K=(1+math.isqrt(1+4*q))//2;t=q-K*(K-1);mu=1 if t<K else 0;i=t if mu else t-K
 if not 1<=K<H//2:raise ValueError('outside declared nonpalindromic block region')
 r=reverse_order_select(K,i);A=H-1-K;B=H-1-reverse_bits(r,h)
 canonical=A*H+B if n%2==0 else (A<<(h+1))+(mu<<h)+B
 word=canonical if q==0 else int(format(canonical,f'0{n}b')[::-1],2)
 deficit=K.bit_count()+r.bit_count()+(0 if mu is None else 1-mu)
 assert word.bit_count()==n-deficit
 return {'K':K,'i':i,'r':r,'middle':mu,'word':word,'deficit':deficit,'twice_body':n-2*deficit}

def popcount_sum(K):
 total=0
 for j in range(K.bit_length()):
  half=1<<j;period=2*half;total+=(K//period)*half+max(0,K%period-half)
 return total

def rank_below(t,n):
 if t<=0:return 0
 if t>=1<<n:return 1<<(n-1)
 bound=format(t-1,f'0{n}b');states={(0,0,0,-1):1};cmp=lambda a,b:(a>b)-(a<b)
 for i in range(n//2):
  new={}
  for (left,right,mirror,first),count in states.items():
   for a in (0,1):
    for b in (0,1):
     key=(left or cmp(a,int(bound[i])),cmp(b,int(bound[n-1-i])) or right,mirror or cmp(a,b),a if i==0 else first)
     new[key]=new.get(key,0)+count
  states=new
 total=0
 for (left,right,mirror,first),count in states.items():
  for c in ((0,1) if n%2 else (None,)):
   order=left
   if n%2:order=order or cmp(c,int(bound[n//2]))
   order=order or right;lead=c if n==1 else first
   if order<=0 and(mirror<0 or(mirror==0 and lead==0)):total+=count
 return total

def location(word,n):
 rev=int(format(word,f'0{n}b')[::-1],2);p=rev if rev!=word else word^((1<<n)-1);a=min(word,p)
 r=rank_below(a,n);N=1<<n;M=N//2;i=r if word==a else N-1-r
 return N-1-i if n>1 and i in (M-1,M) else i

def run():
 start=time.perf_counter();original={};tree=ast.parse(open('pairs_forced.py').read())
 exec(compile(ast.Module(body=[n for n in tree.body if isinstance(n,ast.FunctionDef) and n.name in ('partner','grow')],type_ignores=[]),'original','exec'),original)
 for n in range(1,11):assert [format(int(x),f'0{n}b') for x in ring(n)]==original['grow'](n)
 records=[];closures=[];plots={};cross_width=0;previous={};power_cases=[]
 for n in range(2,21):
  r=ring(n);N=len(r);M=N//2;pal=r==reverse_array(r,n);Z=(2*wt(r)-n).astype(np.int64);body=np.where(pal,0,Z)
  assert np.array_equal(body,body[::-1])
  assert body[0]==body[-1]==0 and body[1]==body[-2]==2-n
  closures.append({'n':n,'endpoint_twice_body':0,'adjacent_twice_body':2-n,'normalized_adjacent_jump':str(Fraction(n-2,n)),'angular_step_over_2pi':str(Fraction(1,N))})
  h=n//2;H=1<<h;predicted=[];word_pred=[]
  for K in range(1,H//2):
   rr=np.arange(K,dtype=np.uint32);rr=rr[np.argsort(reverse_array(rr,h),kind='stable')]
   assert sum(int(x).bit_count() for x in rr)==popcount_sum(K)
   ds=K.bit_count()+wt(rr)
   assert int(ds.max())<=2*K.bit_length()-1
   for mu in ((None,) if n%2==0 else (1,0)):
    A=H-1-K;B=H-1-reverse_array(rr,h)
    c=A*H+B if mu is None else (A<<(h+1))+(mu<<h)+B
    dd=ds if mu is None else ds+1-mu
    words=reverse_array(c,n);word_pred.extend(words.tolist());predicted.extend((n-2*dd).tolist())
  if predicted:
   word_pred[0]=seam_profile(n,0)['word'];pred=np.array(predicted,dtype=np.int64);words=np.array(word_pred,dtype=np.uint32);length=len(pred)
   assert np.array_equal(body[M:M+length],pred) and np.array_equal(r[M:M+length],words)
   assert np.array_equal(body[M-length:M][::-1],pred)
   if n-2 in previous:
    old=previous[n-2];assert np.array_equal(pred[:len(old)],old+2);cross_width+=len(old)
   previous[n]=pred
   records.append({'n':n,'clean_center_depths':length,'both_faces_match':True,'all_word_and_deficit_predictions':True,'upper_deficit_bound':True})
   if n==12:plots={'seam_depths':list(range(128)),'seam_deficits':((n-body[M:M+128])//2).tolist(),'closure_slots':list(range(17)),'closure_twice_body':body[:17].tolist()}
   for t in range(1,12):
    K=1<<t;q=K*(K-1)//2
    if K<H//2 and n%2==0:
     assert seam_profile(n,q)['deficit']==1
     q2=1<<(2*t-1);assert seam_profile(n,q2)['deficit']==2
     power_cases.append({'n':n,'K':K,'triangular_depth':q,'triangular_deficit':1,'dyadic_depth':q2,'dyadic_deficit':2})
 counter=seam_profile(10,64);assert counter['deficit']==5 and format(counter['word'],'010b')=='1110000101'
 scalar=[]
 for n in (64,65,256,257,512,513,1024,1025):
  depths=[0,1,2,4,8,16,32,64,128,512,1024,1<<20]
  for q in depths:
   info=seam_profile(n,q);assert location(info['word'],n)==(1<<(n-1))+q
   scalar.append({'n':n,'depth':q,'deficit':info['deficit'],'exact_address':True})
 result={'scope':'Exact zero-filled Walsh-even latitude body; finite sample smoothness criterion, not an arbitrary smoothing of omitted sites.','profile_checks':records,'clean_depths_checked':sum(r['clean_center_depths'] for r in records),'both_face_samples_checked':2*sum(r['clean_center_depths'] for r in records),'cross_width_deficit_stability_samples':cross_width,'closure_checks':closures,'triangular_and_dyadic_families':power_cases,'raw_dyadic_counterexample':{'n':10,'depth':64,'absolute_position':576,'word':format(counter['word'],'010b'),'zeros':5},'wide_scalar_cases':len(scalar),'wide_scalar_details':scalar,'plot_data':plots,'seconds':time.perf_counter()-start}
 with open('output/even_body_seam_results.json','w') as f:json.dump(result,f,indent=2)
 print(json.dumps({'clean_depths':result['clean_depths_checked'],'both_faces':result['both_face_samples_checked'],'stability_samples':cross_width,'counterexample':result['raw_dyadic_counterexample'],'wide_cases':len(scalar),'closure_n20':closures[-1],'seconds':result['seconds']},indent=2))
if __name__=='__main__':run()
