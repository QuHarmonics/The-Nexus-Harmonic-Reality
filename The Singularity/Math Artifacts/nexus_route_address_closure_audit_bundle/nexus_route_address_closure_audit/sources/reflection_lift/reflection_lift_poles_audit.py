import numpy as np,math,json,csv,hashlib,ast,time
from fractions import Fraction

def partner(word):
 r=word[::-1]
 return r if r!=word else ''.join('1' if b=='0' else '0' for b in word)
def canon(word):return min(word,partner(word))
def insert(word,m):
 h=len(word)//2
 return word[:h]+str(m)+word[h:]
def lift(odd,d):
 h=len(odd)//2;m=int(odd[h]);core=odd[:h]+odd[h+1:]
 return canon(str(m)+core+str(m)) if d==0 else '0'+(partner(core) if m else core)+'1'
def undo_even(word):
 inside=word[1:-1]
 if word!=word[::-1] and word[0]==word[-1]=='1':core=inside;m=1;d=0
 elif word==word[::-1] and word[:2]=='01':core=''.join('1' if b=='0' else '0' for b in inside);m=1;d=0
 elif word[0]==word[-1]=='0':core=inside;m=0;d=0
 elif word[0]=='0' and word[-1]=='1':
  m=int(inside!=canon(inside));core=partner(inside) if m else inside;d=1
 else:raise ValueError('noncanonical word')
 return insert(core,m),d

def encode(word):
 a=canon(word);side=int(a!=word);route=[]
 while len(a)>1:
  n=len(a)
  if n==2:route.append(a[1]);a='0'
  elif n%2:
   h=n//2;route.append(a[h]);a=a[:h]+a[h+1:]
  else:a,d=undo_even(a);route.append(str(d))
 return ''.join(reversed(route)),side

def rev_array(x,n):
 y=x.copy().astype(np.uint32);y=((y>>1)&0x55555555)|((y&0x55555555)<<1);y=((y>>2)&0x33333333)|((y&0x33333333)<<2)
 y=((y>>4)&0x0f0f0f0f)|((y&0x0f0f0f0f)<<4);y=((y>>8)&0x00ff00ff)|((y&0x00ff00ff)<<8);y=(y>>16)|(y<<16)
 return y>>(32-n)
def par_array(x,n):
 r=rev_array(x,n)
 return np.where(r!=x,r,x^((1<<n)-1)).astype(np.uint32)
LUT=np.array([i.bit_count() for i in range(256)],dtype=np.int16)
def wt(x):return sum(LUT[(x>>(8*j))&255] for j in range(4))
def palindrome_count(n,w):
 if n%2==0:return math.comb(n//2,w//2) if w%2==0 else 0
 return math.comb(n//2,w//2)
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
  for center in ((0,1) if n%2 else (None,)):
   order=left
   if n%2:order=order or cmp(center,int(bound[n//2]))
   order=order or right;leading=center if n==1 else first
   if order<=0 and (mirror<0 or (mirror==0 and leading==0)):total+=count
 return total

def location(word):
 n=len(word);a=canon(word);r=rank_below(int(a,2),n);N=1<<n;M=N//2;i=r if word==a else N-1-r
 return N-1-i if n>1 and i in (M-1,M) else i

def route_trace(name,message):
 digest=hashlib.sha256(message).digest();word=format(int.from_bytes(digest,'big'),'0256b');route,side=encode(word)
 a='0';Z=-1;rows=[]
 def record(step,bit='',m='',d='',sign=1):
  n=len(a);w=a.count('1');assert Z==2*w-n
  row={'digest':name,'radius':n,'step':step,'route_bit':bit,'middle_m':m,'outer_xor_d':d,'sign_reflection':sign,'weight':w,'twice_z':Z,'normalized_height':str(Fraction(Z,n)),'transverse_radius_squared':n*n-Z*Z,'radius_increment':0 if step in ('base','partner_face') else 1}
  if n<=8 or n in (16,32,64,128,256):row['ring_position']=str(location(a))
  else:row['ring_position']=''
  rows.append(row)
 record('base')
 for bit in route:
  b=int(bit);n=len(a)
  if n==1:a='0'+bit;Z+=2*b-1;record('base_to_two',bit,m=b)
  elif n%2==0:a=insert(a,b);Z+=2*b-1;record('middle_insertion',bit,m=b)
  else:
   h=n//2;m=int(a[h]);core=a[:h]+a[h+1:];s=-1 if m==1 and core==core[::-1] else 1
   Z=s*(Z+(2*m-1)*(-1 if b else 1));a=lift(a,b);record('E' if b==0 else 'G',bit,m,b,s)
 if side:
  s=-1 if a==a[::-1] else 1;Z*=s;a=partner(a);record('partner_face',sign=s)
 assert a==word
 return rows,{'digest':name,'sha256':digest.hex(),'route_bits':len(route),'side':side,'radius_start':1,'radius_end':len(a),'outward_steps':len(route),'latitude_updates_verified':True,'final_twice_z':Z,'final_weight':a.count('1'),'digest_reconstructed':True}

def run():
 start=time.perf_counter();bands=[];band_checks=[]
 for n in range(2,21):
  x=np.arange(1<<n,dtype=np.uint32);p=par_array(x,n);w=wt(x);wp=wt(p);pal=x==rev_array(x,n)
  assert np.array_equal(wp,np.where(pal,n-w,w))
  a=x[x<p];full=np.concatenate((a,par_array(a,n)[::-1]));M=len(a);full[M-1],full[M]=full[M],full[M-1]
  inverse=np.empty(1<<n,dtype=np.int64);inverse[full]=np.arange(1<<n)
  assert np.array_equal(inverse[p],(1<<n)-1-inverse[x])
  assert not np.any(inverse[p]==((inverse[x]+M)%(1<<n)))
  pc=np.bincount(w[pal],minlength=n+1);counts=np.bincount(w,minlength=n+1)
  for k in range(n+1):
   assert int(counts[k])==math.comb(n,k) and int(pc[k])==palindrome_count(n,k)
   bands.append({'n':n,'weight':k,'twice_z':2*k-n,'word_count':int(counts[k]),'palindrome_count':int(pc[k]),'nonpalindrome_same_band':int(counts[k]-pc[k]),'palindrome_target_weight':n-k})
  band_checks.append({'n':n,'words':len(x),'all_weight_bands':True,'reflection_address':True,'half_turn_matches':0})
 covariance=[];lift_checks=[]
 for L in range(2,19,2):
  x=np.arange(1<<L,dtype=np.uint32);p=par_array(x,L);pal=x==rev_array(x,L);h=L//2;mask=(1<<h)-1
  for m in (0,1):
   child=((x>>h)<<(h+1))|(m<<h)|(x&mask);mp=np.where(pal,1-m,m).astype(np.uint32)
   expected=((p>>h)<<(h+1))|(mp<<h)|(p&mask)
   assert np.array_equal(par_array(child,L+1),expected)
   equal=(m<<(L+1))|(x<<1)|m
   eq_expected=(mp<<(L+1))|(p<<1)|mp
   assert np.array_equal(par_array(equal,L+2),eq_expected)
   mixed=((p if m else x)<<1)|1
   # P(0 P^m(x) 1) = 1 J(P^m(x)) 0.
   mix_expected=(1<<(L+1))|(rev_array(p if m else x,L)<<1)
   assert np.array_equal(par_array(mixed,L+2),mix_expected)
  covariance.append({'source_width':L,'all_source_words':len(x),'middle_insertion_cases':2*len(x),'equal_frame_cases':2*len(x),'mixed_frame_cases':2*len(x),'all_partner_covariance_identities':True})
  x=x[x<p];p=par_array(x,L);pal=x==rev_array(x,L);w=wt(x);flips=0
  for m in (0,1):
   Zodd=2*w+2*m-L-1;s=np.where(pal & (m==1),-1,1)
   for d in (0,1):
    if d==0:
     raw=(m<<(L+1))|(x<<1)|m;y=np.minimum(raw,par_array(raw,L+2))
    else:y=((p if m else x)<<1)|1
    expected=s*(Zodd+(2*m-1)*(-1 if d else 1));actual=2*wt(y)-(L+2)
    assert np.array_equal(actual,expected)
    py=par_array(y,L+2);outpal=y==rev_array(y,L+2)
    assert np.array_equal(2*wt(py)-(L+2),np.where(outpal,-actual,actual))
    if d==1:assert not np.any(outpal)
    else:assert np.array_equal(outpal,pal)
    flips+=int(np.count_nonzero(s==-1))
  lift_checks.append({'source_width':L,'target_width':L+2,'canonical_outputs':4*len(x),'sign_reflected_steps':flips,'all_latitude_and_partner_face_checks':True})
 poles=[]
 for n in (32,64,128,256,512,1024,2048,4096):
  zero='0'*n;one='1'*n;assert partner(zero)==one and partner(one)==zero
  assert location(zero)==0 and location(one)==(1<<n)-1
  for m in (0,1):
   for d in (0,1):
    odd=insert(zero,m);y=lift(odd,d);Z=2*y.count('1')-(n+2)
    expected_Z={'00':-(n+2),'01':-n,'10':n-2,'11':n}[str(m)+str(d)]
    assert Z==expected_Z
    poles.append({'source_width':n,'target_width':n+2,'m':m,'d':d,'target_weight':y.count('1'),'target_twice_z':Z,'normalized_height':str(Fraction(Z,n+2)),'transverse_radius_squared':(n+2)**2-Z*Z,'partner_returns':partner(partner(y))==y})
 rows=[];traces=[]
 for name,message in [('empty',b''),('ovaltine',b'Dont forget to drink your Ovaltine')]:
  rr,summary=route_trace(name,message);rows.extend(rr);traces.append(summary)
 report={'scope':'Independent exact finite operator checks and wide pole queries, not a physical-spin or SHA-preimage claim.','sphere_convention':'Physical radius r=n; height Z=2z=2w-n; rho=sqrt(n*n-Z*Z); theta=2*pi*((i+1/2)/2^n-1/2).','band_checks':band_checks,'operator_covariance':covariance,'lift_and_output_partner_checks':lift_checks,'wide_pole_profiles':poles,'full_digest_radius_traces':traces,'seconds':time.perf_counter()-start}
 with open('output/reflection_lift_poles_results.json','w') as f:json.dump(report,f,indent=2)
 with open('output/all_weight_band_actions.csv','w',newline='') as f:
  writer=csv.DictWriter(f,fieldnames=bands[0]);writer.writeheader();writer.writerows(bands)
 with open('output/full_digest_radius_latitude_trace.csv','w',newline='') as f:
  writer=csv.DictWriter(f,fieldnames=rows[0]);writer.writeheader();writer.writerows(rows)
 print(json.dumps({'all_band_words':sum(c['words'] for c in band_checks),'weight_bands':len(bands),'covariance_cases_per_identity':sum(c['middle_insertion_cases'] for c in covariance),'lift_outputs':sum(c['canonical_outputs'] for c in lift_checks),'maximum_pole_source_width':4096,'traces':traces,'seconds':report['seconds']},indent=2))

if __name__=='__main__':run()
