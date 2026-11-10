# Running audit — hemisphere coupling and persistent branch transport

One append-ready Markdown entry: source, results and interpretation. No prior log is overwritten.

Pre-execution SHA-256 of the exact UTF-8 Python source block (including its final newline): `d8221144ea9a1e56181065177792eeec2c70550ee1aa2bdf6abec943982018b4`.

This seals this independent audit block, not a claim that the final appended Markdown file has an unchanged file checksum. Unknown topology and port destinations are measured rather than assumed. The core is the S-orbit containing zero, never a hardcoded sorted-cycle index.

## Executable source

```python
import math,json,time,itertools,collections,ast

TEMPLATE=[(0,0,6),(2,1,7),(4,0,5),(1,1,6),(2,0,3),(2,0,2),(3,1,5),(1,0,1),(0,0,7),(4,1,7),(2,0,6),(2,1,5),(1,0,5),(1,0,4),(1,1,3),(5,0,3)]
def J(x,n):return int(format(x,f'0{n}b')[::-1],2)
def C(x,n):return x^((1<<n)-1)
def P(x,n):
 y=J(x,n);return y if y!=x else C(x,n)
def PC(x,n):return P(C(x,n),n)
def ring(n):
 a=[x for x in range(1<<n) if x<P(x,n)];r=a+[P(x,n) for x in reversed(a)]
 if n>1:r[len(a)-1],r[len(a)]=r[len(a)],r[len(a)-1]
 return r

def cycles(perm):
 seen=set();out=[]
 for x in range(len(perm)):
  if x in seen:continue
  seq=[];y=x
  while y not in seen:seen.add(y);seq.append(y);y=perm[y]
  assert y==seq[0];out.append(seq)
 return out

def maps(n):
 r=ring(n);N=len(r);T=[0]*N;Ti=[0]*N
 for i,x in enumerate(r):T[x]=r[(i+1)%N];Ti[x]=r[(i-1)%N]
 K=[PC(x,n) for x in range(N)];TC=[C(T[C(x,n)],n) for x in range(N)];S=[K[Ti[x]] for x in range(N)];Si=[0]*N
 for x,y in enumerate(S):Si[y]=x
 cs=cycles(S);owner=[0]*N
 for i,seq in enumerate(cs):
  for x in seq:owner[x]=i
 return {'n':n,'R':r,'T':T,'Ti':Ti,'K':K,'TC':TC,'S':S,'Si':Si,'cycles':cs,'owner':owner,'core':owner[0]}

def embed(t,n,header=3):
 u,m,v=t;k=n-2*header
 if k<0:raise ValueError('negative middle width')
 return (u<<(n-header))|((((1<<k)-1) if m else 0)<<header)|v

def prev_bounded(x,n,limit=4):
 for d in range(1,limit+1):
  y=x-d
  if y<P(y,n):return y,d
 raise AssertionError('predecessor exceeded declared bound')

def pattern_rep(t):
 u,m,v=t;r=J(v,3)
 return u<r if u!=r else u<4

def subtract_pattern(t,d):
 u,m,v=t
 if v>=d:return u,m,v-d
 if m==0 and u>0:return u-1,1,v-d+8
 raise AssertionError('unsupported middle borrow in certificate')

def pc_pattern(t):
 u,m,v=t
 return t if u==J(v,3) else (7-J(v,3),1-m,7-J(u,3))

def symbolic_certificate():
 rows=[]
 for phase,t in enumerate(TEMPLATE):
  assert pattern_rep(t)
  candidates=[]
  for d in range(1,5):
   p=subtract_pattern(t,d);valid=pattern_rep(p);candidates.append({'decrement':d,'pattern':p,'canonical':valid})
   if valid:break
  assert candidates[-1]['canonical'] and all(not r['canonical'] for r in candidates[:-1])
  assert pc_pattern(p)==TEMPLATE[(phase+1)%16]
  rows.append({'phase':phase,'source':t,'predecessor':p,'decrement':d,'PC_predecessor':pc_pattern(p),'earlier_candidates':candidates[:-1]})
 return rows

def project(x,n,positions):return sum(((x>>p)&1)<<j for j,p in enumerate(positions))
def core_destination_summary(data,branch):
 n=data['n'];owner=data['owner'];core=data['core'];U=owner[branch[0]];V=owner[C(branch[0],n)]
 counts=collections.Counter(owner[data['T'][x]] for x in branch)
 destinations=[]
 for i,count in sorted(counts.items(),key=lambda item:(item[0]!=core,min(data['cycles'][item[0]]))):
  destinations.append({'orbit_min':min(data['cycles'][i]),'orbit_length':len(data['cycles'][i]),'is_core':i==core,'is_self':i==U,'is_complement_partner':i==V,'edges':count})
 return {'core':counts[core],'self':counts[U],'mirror':counts[V],'other_detached':sum(c for i,c in counts.items() if i not in (core,U,V)),'destinations':destinations}

def left_cycle(data,length):
 return next((c for c in data['cycles'] if len(c)==length and all(x<P(x,data['n']) for x in c)),None)

def cyclic_equal(a,b):
 return len(a)==len(b) and any(a==b[k:]+b[:k] for k in range(len(b)))

def run():
 start=time.perf_counter();symbolic=symbolic_certificate();data={};width_rows=[];branch16=[];matrix6=None
 for n in range(2,17):
  d=maps(n);data[n]=d;N=1<<n;owner=d['owner'];core=d['core'];K=d['K'];S=d['S'];Si=d['Si'];T=d['T'];TC=d['TC']
  rep=[x<P(x,n) for x in range(N)]
  assert all(rep[x]==rep[K[x]] for x in range(N))
  assert all(T[x]==Si[K[x]] and TC[x]==S[K[x]] for x in range(N))
  assert all(owner[T[x]]==owner[TC[x]]==owner[K[x]] for x in range(N))
  assert all(all(rep[x] for x in c) or not any(rep[x] for x in c) for i,c in enumerate(d['cycles']) if i!=core)
  mat=collections.Counter((owner[x],owner[T[x]]) for x in range(N))
  assert all(mat[i,j]==mat[j,i] for i in range(len(d['cycles'])) for j in range(len(d['cycles'])))
  for i,ci in enumerate(d['cycles']):
   for j,cj in enumerate(d['cycles']):
    if i!=core and j!=core and rep[ci[0]]!=rep[cj[0]]:assert mat[i,j]==0
  assert all({C(x,n) for x in c}==set(d['cycles'][owner[C(c[0],n)]]) for c in d['cycles'])
  width_rows.append({'n':n,'core_length':len(d['cycles'][core]),'largest_S_cycle':max(map(len,d['cycles'])),'core_is_largest':len(d['cycles'][core])==max(map(len,d['cycles'])),'all_hemisphere_and_port_identities':True})
  if n>=6:
   branch=[embed(t,n) for t in TEMPLATE]
   assert all(S[x]==branch[(j+1)%16] for j,x in enumerate(branch))
   ports=core_destination_summary(d,branch)
   assert ports['self']==(11 if n==6 else 7) and ports['mirror']==0
   branch16.append({'n':n,'template_closes':True,'ports':ports})
   if n==6:
    ids=[core,owner[branch[0]],owner[C(branch[0],n)]];matrix6=[[mat[i,j] for j in ids] for i in ids]
 projection=[];U6=[embed(t,6) for t in TEMPLATE]
 for ps in itertools.combinations(range(6),4):
  buckets=collections.defaultdict(list)
  for x in U6:buckets[project(x,6,ps)].append(x)
  witness=next((v[:2] for v in buckets.values() if len(v)>1),None)
  assert len(buckets)<16 and witness is not None
  projection.append({'bit_positions_LSB':ps,'distinct_outputs':len(buckets),'collision_witness':witness})
 # Test the proposed hidden middle-bit decoder literally.
 middle_decoder=[]
 for phase,(u,m,v) in enumerate(TEMPLATE):
  x=U6[phase];previous_word=U6[(phase-1)%16];previous_rep,_=prev_bounded(previous_word,6)
  claimed=0 if x==J(x,6) else 1-((previous_rep&7)>>2)
  if claimed!=m:middle_decoder.append({'phase':phase,'word':x,'previous_branch_word':previous_word,'its_previous_rep':previous_rep,'claimed_middle':claimed,'template_middle':m})
 wide=[]
 for n in (64,128,256,512,1024,2048):
  branch=[embed(t,n) for t in TEMPLATE];members=set(branch);decrements=[]
  for phase,x in enumerate(branch):
   assert x<P(x,n);prev,dd=prev_bounded(x,n);assert PC(prev,n)==branch[(phase+1)%16];decrements.append(dd)
   assert embed(TEMPLATE[(phase+1)%16],n+1)==PC(prev_bounded(embed(TEMPLATE[phase],n+1),n+1)[0],n+1)
  internal=sum(prev_bounded(x,n)[0] in members for x in branch)
  assert internal==7
  wide.append({'n':n,'all_16_S_steps':True,'self_T_edges':internal,'outside_branch_edges':16-internal,'maximum_predecessor_decrement':max(decrements),'destination_component_of_outside_edges':'not classified without an additional component-address proof'})
 # The 28-state left branch: test the suggested outer-4 versus outer-5 descriptions.
 base=left_cycle(data[10],28);assert base is not None;base_index={x:i for i,x in enumerate(base)}
 outer4=[];outer5=[];labels=None
 for n in range(10,17):
  cyc=left_cycle(data[n],28);assert cyc is not None
  for h,target in ((4,outer4),(5,outer5)):
   k=n-2*h
   mids=[(x>>h)&((1<<k)-1) for x in cyc] if k else [0]*len(cyc)
   uniform=sum(m in (0,(1<<k)-1) for m in mids)
   row={'n':n,'outer_width':h,'middle_width':k,'uniform_middle_states':uniform,'total':28}
   if h==5:
    proj=[((x>>(n-5))<<5)|(x&31) for x in cyc]
    row['delete_middle_recovers_base10']=set(proj)==set(base) and len(set(proj))==28
    row['phase_intertwining']=row['delete_middle_recovers_base10'] and all((base_index[proj[(i+1)%28]]-base_index[proj[i]])%28==1 for i in range(28))
    if n==11 and row['delete_middle_recovers_base10']:
     bybase={((x>>(n-5))<<5)|(x&31):(x>>5)&1 for x in cyc}
     labels=[(x>>5,bybase[x],x&31) for x in base]
   target.append(row)
 extracted_checks=[]
 if labels is not None:
  for n in range(10,17):
   proposed=[embed(t,n,5) for t in labels];S=data[n]['S'];exact=all(S[x]==proposed[(j+1)%28] for j,x in enumerate(proposed))
   extracted_checks.append({'n':n,'outer5_template_closes':exact})
 projected8=[((x>>6)<<4)|(x&15) for x in base];U8=left_cycle(data[8],27);duplicate={str(x):[j for j,y in enumerate(projected8) if y==x] for x in set(projected8) if projected8.count(x)>1}
 contracted=[]
 for x in projected8:
  if not contracted or contracted[-1]!=x:contracted.append(x)
 if len(contracted)>1 and contracted[0]==contracted[-1]:contracted.pop()
 collapse8={'base_width':10,'outer4_projection_distinct':len(set(projected8)),'matches_LEN8_left_27_vertex_set':set(projected8)==set(U8),'duplicate_phases':duplicate,'after_adjacent_duplicate_contraction_length':len(contracted),'matches_LEN8_cycle_order':cyclic_equal(contracted,U8),'matches_LEN8_inverse_order':cyclic_equal(contracted,list(reversed(U8)))}
 width9=[]
 for bit in (4,5):
  values=[((x>>(bit+1))<<bit)|(x&((1<<bit)-1)) for x in base];cnt=collections.Counter(data[9]['owner'][x] for x in values)
  width9.append({'deleted_base10_bit_LSB':bit,'distinct_9bit_images':len(set(values)),'component_membership_with_multiplicity':[{'length':len(data[9]['cycles'][i]),'is_core':i==data[9]['core'],'images':count} for i,count in sorted(cnt.items())]})
 result={'scope':'Exact coupling and template audit. Infinite-width template claim is supported by the explicit finite pattern certificate; full component destinations are only classified where complete rings were built.','widths':width_rows,'LEN6_matrix_core_left_right':matrix6,'16_template_symbolic_certificate':symbolic,'16_template_ports':branch16,'four_of_six_projection_checks':projection,'proposed_middle_decoder_failures':middle_decoder,'wide_template_checks':wide,'28_branch_outer4_uniformity':outer4,'28_branch_outer5_extraction':outer5,'28_branch_extracted_outer5_template':labels,'28_branch_outer5_closure_tests':extracted_checks,'28_to_27_projection':collapse8,'width9_intermediate_projection':width9,'seconds':time.perf_counter()-start}
 print(json.dumps(result,indent=2))
 return result
```
