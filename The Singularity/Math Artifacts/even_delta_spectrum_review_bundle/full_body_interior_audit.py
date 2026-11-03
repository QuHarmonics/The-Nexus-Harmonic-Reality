import numpy as np,math,json,time,ast,random,csv

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
 if p in (0,1<<n):return 0
 h=n//2;H=1<<h;B=p&(H-1)
 if n%2==0:A=p>>h;base=A*(H-A)
 else:
  A=p>>(h+1);middle=(p>>h)&1;base=2*A*(H-A)+middle*(H-1-2*A)
 return base+B-2*rectangle(B,A,h)-int(reverse_bits(A,h)<B)

def palindrome_from_prefix(u,n):
 m=(n+1)//2
 return (u<<m)|reverse_bits(u,m) if n%2==0 else (u<<(m-1))|reverse_bits(u>>1,m-1)
def palindrome_count_below(p,n):
 if p<=0:return 0
 if p>=1<<n:return 1<<((n+1)//2)
 m=(n+1)//2;u=p>>(n-m)
 return u+int(palindrome_from_prefix(u,n)<p)
def rank_below(p,n):
 pi=palindrome_count_below(p,n);T=min(pi,1<<((n+1)//2-1))
 value=p-pi+delta(p,n);assert value%2==0
 return value//2+T

def partner(word,n):
 r=reverse_bits(word,n)
 return r if r!=word else word^((1<<n)-1)
def location(word,n):
 p=partner(word,n);a=min(word,p);r=rank_below(a,n);N=1<<n;M=N//2;i=r if a==word else N-1-r
 return N-1-i if n>1 and i in (M-1,M) else i

def reverse_order_select(S,i):
 residue=0
 for j in range((S-1).bit_length()):
  count0=max(0,(S-1-residue)//(1<<(j+1))+1)
  if i>=count0:i-=count0;residue+=1<<j
 assert i==0 and residue<S
 return residue

def word_at(i,n):
 if n==1:return i
 N=1<<n;M=N//2
 if not 0<=i<N:raise ValueError('ring position out of range')
 q=i-M if i>=M else M-1-i;h=n//2;H=1<<h;nu=1 if n%2==0 else 2;Q=q//nu;boundary=(H//2)*(H//2-1)//2
 if Q<boundary:K=(1+math.isqrt(1+8*Q))//2
 else:K=(math.isqrt(1+8*(Q+H//2))-1)//2
 e=int(K>=H//2);S=K+e;D=K*(K-1)//2+max(0,K-H//2);offset=q-nu*D
 if nu==1:middle=None;inside=offset
 else:middle=int(offset<S);inside=offset if middle else offset-S
 r=reverse_order_select(S,inside);A=H-1-K;B=H-1-reverse_bits(r,h)
 a=(A<<h)|B if middle is None else (A<<(h+1))|(middle<<h)|B
 canonical_on_right=q==0
 return a if ((i>=M)==canonical_on_right) else partner(a,n)

def body_at(i,n):
 x=word_at(i,n)
 return 0 if x==reverse_bits(x,n) else 2*x.bit_count()-n

def popcount_sum(S):
 total=0
 for j in range(S.bit_length()):
  half=1<<j;period=2*half;total+=(S//period)*half+max(0,S%period-half)
 return total

def reverse_array(x,n):
 y=x.copy().astype(np.uint32);y=((y>>1)&0x55555555)|((y&0x55555555)<<1);y=((y>>2)&0x33333333)|((y&0x33333333)<<2)
 y=((y>>4)&0x0f0f0f0f)|((y&0x0f0f0f0f)<<4);y=((y>>8)&0x00ff00ff)|((y&0x00ff00ff)<<8);y=(y>>16)|(y<<16)
 return y>>(32-n)
def partner_array(x,n):
 r=reverse_array(x,n);return np.where(r!=x,r,x^((1<<n)-1)).astype(np.uint32)
LUT=np.array([i.bit_count() for i in range(256)],dtype=np.int16)
def wt(x):return sum(LUT[(x>>(8*j))&255] for j in range(4))
def rectangle_array(u,v,h):
 total=np.zeros_like(u,dtype=np.int64);rho=np.zeros_like(u,dtype=np.int64)
 for j in range(h):
  bit=(u>>(h-1-j))&1;d=1<<(j+1);total+=bit*((v-rho+d-1)//d);rho+=bit<<j
 return total

def delta_array(p,n):
 h=n//2;H=1<<h;B=(p&(H-1)).astype(np.int64)
 if n%2==0:A=(p>>h).astype(np.int64);base=A*(H-A)
 else:
  A=(p>>(h+1)).astype(np.int64);middle=((p>>h)&1).astype(np.int64);base=2*A*(H-A)+middle*(H-1-2*A)
 return base+B-2*rectangle_array(B,A,h)-(reverse_array(A.astype(np.uint32),h)<B).astype(np.int64)

def independent_rank(p,n):
 if p<=0:return 0
 if p>=1<<n:return 1<<(n-1)
 bound=format(p-1,f'0{n}b');states={(0,0,0,-1):1};cmp=lambda a,b:(a>b)-(a<b)
 for j in range(n//2):
  new={}
  for (left,right,mirror,first),count in states.items():
   for a in (0,1):
    for b in (0,1):
     key=(left or cmp(a,int(bound[j])),cmp(b,int(bound[n-1-j])) or right,mirror or cmp(a,b),a if j==0 else first)
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

def run():
 start=time.perf_counter();original={};tree=ast.parse(open('pairs_forced.py').read())
 exec(compile(ast.Module(body=[n for n in tree.body if isinstance(n,ast.FunctionDef) and n.name in ('partner','grow')],type_ignores=[]),'original','exec'),original)
 checks=[];blockrows=[];counter=None
 for n in range(2,21):
  N=1<<n;M=N//2;h=n//2;H=1<<h;nu=1 if n%2==0 else 2;m=(n+1)//2
  p=np.arange(N,dtype=np.uint32);P=partner_array(p,n);can=p<P;a=p[can];ring=np.concatenate((a,P[a][::-1]));ring[M-1],ring[M]=ring[M],ring[M-1]
  if n<=10:assert [format(int(x),f'0{n}b') for x in ring]==original['grow'](n)
  u=p>>(n-m)
  pal=(u<<m)|reverse_array(u,m) if n%2==0 else (u<<(m-1))|reverse_array(u>>1,m-1)
  pi=u.astype(np.int64)+(pal<p).astype(np.int64);T=np.minimum(pi,1<<(m-1));Dlt=delta_array(p,n)
  predicted_rank=(p.astype(np.int64)-pi+Dlt)//2+T;true_rank=np.concatenate(([0],np.cumsum(can.astype(np.int64))))[:-1]
  assert np.array_equal(predicted_rank,true_rank)
  naive=(p.astype(np.int64)+pi+Dlt)//2;bad=int(np.count_nonzero(naive[can]!=true_rank[can]))
  canonical_predictions=[];body_predictions=[];blocks=0;pal_blocks=0
  for K in range(1,H):
   e=int(K>=H//2);S=K+e;startq=K*(K-1)//2+max(0,K-H//2)
   rr=np.arange(S,dtype=np.uint32);rr=rr[np.argsort(reverse_array(rr,h),kind='stable')];A=H-1-K;B=H-1-reverse_array(rr,h)
   core_zero=K.bit_count()+wt(rr);block_values=[];block_body=[];canonical_zero=0
   for middle in ((None,) if nu==1 else (1,0)):
    words=(A<<h)|B if middle is None else (A<<(h+1))|(middle<<h)|B
    zeros=core_zero if middle is None else core_zero+1-middle
    bodies=np.where(rr==K,0,n-2*zeros)
    canonical_predictions.extend(words.tolist());body_predictions.extend(bodies.tolist());canonical_zero+=int(zeros.sum())
    block_body.extend(bodies.tolist())
   Zcan=nu*(S*K.bit_count()+popcount_sum(S))+(nu-1)*S
   assert canonical_zero==Zcan
   body_deficit=Zcan+nu*e*(h-2*K.bit_count())
   actual_twice_deficit=nu*S*n-sum(block_body)
   assert actual_twice_deficit==2*body_deficit
   blockrows.append({'n':n,'K':K,'palindrome_entry':e,'parent_block_size':S,'canonical_zero_sum':Zcan,'body_deficit_sum':body_deficit,'body_sample_count':nu*S})
   blocks+=1;pal_blocks+=e
  predicted=np.array(canonical_predictions,dtype=np.uint32);assert np.array_equal(predicted,a[::-1])
  right=partner_array(predicted,n);right[0]=predicted[0];left=predicted.copy();left[0]=partner_array(predicted[:1],n)[0]
  assert np.array_equal(np.concatenate((left[::-1],right)),ring)
  Z=2*wt(ring)-n;pal_mask=ring==reverse_array(ring,n);body=np.where(pal_mask,0,Z)
  assert np.array_equal(body[M:],np.array(body_predictions)) and np.array_equal(body[:M][::-1],np.array(body_predictions))
  if n<=10:assert all(word_at(i,n)==int(x) for i,x in enumerate(ring))
  checks.append({'n':n,'all_rank_thresholds':N,'all_ring_words_predicted':N,'blocks':blocks,'palindrome_containing_blocks':pal_blocks,'uncorrected_rank_failures_on_canonical_words':bad,'full_body_prediction':True,'all_block_sums':True})
  if n==4:
   x=11;counter={'n':4,'representative':'1011','pi':int(pi[x]),'T':int(T[x]),'Delta':int(Dlt[x]),'uncorrected_rank':int(naive[x]),'actual_rank':int(true_rank[x]),'physical_center_position':8}
 rng=random.Random(20261020);wide=[]
 for n in (63,64,127,128,255,256,511,512,1023,1024):
  N=1<<n;M=N//2;positions=[0,1,M-1,M,N-2,N-1]+[rng.randrange(N) for _ in range(6)]
  for i in positions:
   x=word_at(i,n);assert location(x,n)==i
   pal=x==reverse_bits(x,n);actual=0 if pal else 2*x.bit_count()-n;assert body_at(i,n)==actual
  thresholds=[0,1,M,N-1,N]+[rng.randrange(N) for _ in range(4)]
  for p in thresholds:assert rank_below(p,n)==independent_rank(p,n)
  wide.append({'n':n,'direct_word_address_cases':len(positions),'independent_rank_thresholds':len(thresholds)})
 report={'scope':'Full rank, full canonical block decomposition and exact Walsh-even body. Source is a new independent audit; external scripts and seals are not claimed as verified.','checks':checks,'total_rank_thresholds':sum(t['all_rank_thresholds'] for t in checks),'total_predicted_ring_words':sum(t['all_ring_words_predicted'] for t in checks),'total_blocks':sum(t['blocks'] for t in checks),'total_palindrome_containing_blocks':sum(t['palindrome_containing_blocks'] for t in checks),'rank_correction_example':counter,'wide_checks':wide,'seconds':time.perf_counter()-start}
 with open('output/full_body_interior_results.json','w') as f:json.dump(report,f,indent=2)
 with open('output/full_body_block_sums.csv','w',newline='') as f:
  w=csv.DictWriter(f,fieldnames=blockrows[0]);w.writeheader();w.writerows(blockrows)
 print(json.dumps({'all_rank_thresholds':report['total_rank_thresholds'],'all_ring_words':report['total_predicted_ring_words'],'all_blocks':report['total_blocks'],'palindrome_blocks':report['total_palindrome_containing_blocks'],'rank_correction':counter,'largest_case':checks[-1],'wide_word_cases':sum(r['direct_word_address_cases'] for r in wide),'wide_rank_cases':sum(r['independent_rank_thresholds'] for r in wide),'seconds':report['seconds']},indent=2))
if __name__=='__main__':run()
