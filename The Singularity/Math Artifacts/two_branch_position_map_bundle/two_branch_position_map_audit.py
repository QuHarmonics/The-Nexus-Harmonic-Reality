import numpy as np,json,hashlib,time,random
from functools import lru_cache

def reverse(x,L):return int(format(x,f'0{L}b')[::-1],2)
def partner(x,L):
 r=reverse(x,L)
 return r if r!=x else x^((1<<L)-1)
def rectangle(u,v,h):
 H=1<<h
 if u<=0 or v<=0:return 0
 if u>=H:return min(v,H)
 if v>=H:return min(u,H)
 U=format(u-1,f'0{h}b');V=format(v-1,f'0{h}b');states={(0,0):1}
 cmp=lambda a,b:(a>b)-(a<b)
 for j in range(h):
  new={}
  for (left,right),count in states.items():
   for bit in (0,1):
    key=(left or cmp(bit,int(U[j])),cmp(bit,int(V[h-1-j])) or right)
    new[key]=new.get(key,0)+count
  states=new
 return sum(n for (left,right),n in states.items() if left<=0 and right<=0)
def Q(z,L):
 h=L//2;H=1<<h;A=z>>h;B=z&(H-1);K1=2*H-1-A
 D1=K1*(K1-1)//2+(H-1-A)
 return D1+2*(H-1-B)-A+rectangle(B+1,A,h)
def input_coordinates(x,L):
 h=L//2;H=1<<h;A=x>>h;B=x&(H-1);K=H-1-A
 D=K*(K-1)//2+max(0,K-H//2)
 count=sum(1 for b in range(B+1,H) if reverse(b,h)>A or (reverse(b,h)==A and A<H//2))
 return K,count,D+count

def physical_position(q,n):
 M=1<<(n-1)
 return M if q==0 else M-1-q

def direct_target_offsets(x,L,j=None):
 assert L%2==0 and x<partner(x,L)
 h=L//2;H=1<<h;A=x>>h;B=x&(H-1);K=H-1-A
 if j is None:_,_,j=input_coordinates(x,L)
 s=max(0,K-H//2)+int(A<H//2 and reverse(A,h)>B)
 p=partner(x,L);qx=Q(x,L);qp=Q(p,L)
 return {'E0':qx+1,'G0':qx,'E1':j-s if x!=reverse(x,L) else qp+1,'G1':qp}

def reverse_array(x,L):
 y=x.copy().astype(np.uint32)
 y=((y>>1)&0x55555555)|((y&0x55555555)<<1)
 y=((y>>2)&0x33333333)|((y&0x33333333)<<2)
 y=((y>>4)&0x0f0f0f0f)|((y&0x0f0f0f0f)<<4)
 y=((y>>8)&0x00ff00ff)|((y&0x00ff00ff)<<8)
 y=(y>>16)|(y<<16)
 return y>>(32-L)
def partner_array(x,L):
 r=reverse_array(x,L)
 return np.where(r!=x,r,x^((1<<L)-1)).astype(np.uint32)
def reps(L):
 x=np.arange(1<<L,dtype=np.uint32)
 return x[x<partner_array(x,L)]
def rectangle_table(h):
 H=1<<h;table=np.zeros((H+1,H+1),dtype=np.int64)
 a=np.arange(H,dtype=np.uint32);table[a+1,reverse_array(a,h)+1]=1
 return table.cumsum(0).cumsum(1)
def Q_array(z,L,table):
 h=L//2;H=1<<h;A=(z>>h).astype(np.int64);B=(z&(H-1)).astype(np.int64);K1=2*H-1-A
 return K1*(K1-1)//2+(H-1-A)+2*(H-1-B)-A+table[B+1,A]

# A separate mirrored-pair rank counter validates wide scalar queries.
def rank_below(t,L):
 if t<=0:return 0
 if t>=1<<L:return 1<<(L-1)
 b=format(t-1,f'0{L}b');states={(0,0,0,-1):1};cmp=lambda a,b:(a>b)-(a<b)
 for i in range(L//2):
  new={}
  for (cl,cr,cj,first),n in states.items():
   for a in (0,1):
    for c in (0,1):
     key=(cl or cmp(a,int(b[i])),cmp(c,int(b[L-1-i])) or cr,cj or cmp(a,c),a if i==0 else first)
     new[key]=new.get(key,0)+n
  states=new
 return sum(n for (cl,cr,cj,first),n in states.items() if (cl or cr)<=0 and(cj<0 or(cj==0 and first==0)))

def run():
 start=time.perf_counter();checks=[];examples=[]
 for h in range(1,5):
  T=rectangle_table(h)
  assert all(rectangle(u,v,h)==int(T[u,v]) for u in range((1<<h)+1) for v in range((1<<h)+1))
 for L in range(2,19,2):
  h=L//2;H=1<<h;x=reps(L)[::-1].copy();p=partner_array(x,L);n=L+2
  target=reps(n)[::-1].copy();inv=np.full(1<<n,-1,dtype=np.int32);inv[target]=np.arange(len(target))
  odds=reps(L+1)[::-1].copy();oddinv=np.full(1<<(L+1),-1,dtype=np.int32);oddinv[odds]=np.arange(len(odds))
  j=np.arange(len(x),dtype=np.int64);A=(x>>h).astype(np.int64);B=(x&(H-1)).astype(np.int64);K=H-1-A
  D=K*(K-1)//2+np.maximum(0,K-H//2);size=K+(K>=H//2).astype(np.int64);i=j-D
  assert np.all((i>=0)&(i<size))
  for m in (0,1):
   child=((x>>h)<<(h+1))|(m<<h)|(x&(H-1));pred=2*D+i+(1-m)*size
   assert np.array_equal(oddinv[child],pred)
  table=rectangle_table(h);qx=Q_array(x,L,table);qp=Q_array(p,L,table)
  pal=x==reverse_array(x,L);s=np.maximum(0,K-H//2)+((A<H//2)&(reverse_array(A.astype(np.uint32),h)>B)).astype(np.int64)
  E0=x<<1;raw1=(1<<(L+1))|(x<<1)|1;E1=np.minimum(raw1,partner_array(raw1,n));G0=(x<<1)|1;G1=(p<<1)|1
  predicted={'E0':qx+1,'G0':qx,'E1':np.where(pal,qp+1,j-s),'G1':qp}
  actual={'E0':E0,'E1':E1,'G0':G0,'G1':G1}
  assert np.array_equal(np.sort(np.concatenate(list(actual.values()))),np.sort(target))
  for name,words in actual.items():
   q=predicted[name];assert np.array_equal(inv[words],q)
   M=1<<(n-1);absolute=np.where(q==0,M,M-1-q)
   ascending=target[::-1];full=np.concatenate((ascending,partner_array(ascending,n)[::-1]));full[M-1],full[M]=full[M],full[M-1]
   assert np.array_equal(full[absolute],words)
   assert np.array_equal(full[(1<<n)-1-absolute],partner_array(words,n))
  checks.append({'source_width':L,'target_width':n,'canonical_parents':len(x),'E_G_outputs_checked':4*len(x),'odd_middle_offset_formulas':True,'E_G_offset_formulas':True,'physical_seam_and_partner_positions':True,'all_target_representatives_covered_once':True})
  if L==4:
   for xx in (0,1,6,11):
    jj=int(np.where(x==xx)[0][0]);out=direct_target_offsets(xx,L,jj)
    e1=min((1<<5)|(xx<<1)|1,partner((1<<5)|(xx<<1)|1,6));targets={'E0':xx<<1,'G0':(xx<<1)|1,'E1':e1,'G1':(partner(xx,4)<<1)|1}
    examples.append({'parent':format(xx,'04b'),'parent_descending_offset':jj,'targets':{key:{'word':format(targets[key],'06b'),'descending_offset':out[key],'absolute_ring_position':physical_position(out[key],6)} for key in out}})
 rng=random.Random(20261020);wide=[]
 for L in (64,256,512):
  for _ in range(8):
   z=rng.getrandbits(L);x=min(z,partner(z,L));j=(1<<(L-1))-1-rank_below(x,L)
   predicted=direct_target_offsets(x,L,j);raw1=(1<<(L+1))|(x<<1)|1
   outputs={'E0':x<<1,'G0':(x<<1)|1,'E1':min(raw1,partner(raw1,L+2)),'G1':(partner(x,L)<<1)|1}
   for name,y in outputs.items():
    q=(1<<(L+1))-1-rank_below(y,L+2)
    assert predicted[name]==q
  wide.append({'source_width':L,'scalar_parents':8,'target_offsets_checked':32,'no_ring_arrays_used':True})
 return {'scope':'Independent unsealed mathematical derivation; audit source checksum sealed before this execution. User-reported ab543c... seal not independently verified because its source file was not supplied.','coordinate':'Descending canonical representative offset q, then explicit physical center-swap conversion.','exhaustive':checks,'wide_scalar_queries':wide,'examples':examples,'seconds':time.perf_counter()-start}

if __name__=='__main__':
 result=run()
 with open('output/two_branch_position_map_results.json','w') as f:json.dump(result,f,indent=2)
 print(json.dumps(result,indent=2))
