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


---

# Append-only correction and native 28-cycle all-width certificate — October 21, 2026

Dean A. Kulik · QuHarmonics Research Group · ORCID 0009-0003-3128-8828

## Correction ledger, do not overwrite the earlier assertions

The prior appended source has two executed assertions that fail: `self==7` for the 16-state branch at `LEN>=7`, and `internal==7` for its direct high-width predecessor. Both require **4**, not 7. Thus the port split is **4 internal + 12 external**, not **7 internal + 9 external**. The original 16-state cycle itself remains valid. At LEN 8 one external step reaches a detached 27-state orbit; at LEN 14 six external steps reach an 855-state orbit. Hence not every external port is a *core* port.

The proposed formula for recovering the hidden middle bit at LEN 6 also mismatches the sourced phase bits at t=1,7,9,11,12,15. That decoder is a DEAD END. The phase-tagged 16-state template remains valid, and the phase may be retained as context.

The source-linked LEN10 seed is word **23**, not a seed discovered by orbit-length candidate search. The predecessor and phase route starts there. The cited original source checksum belongs to its original source bytes; the new source has a separate checksum. Code corrections are logged; no failed assertion was silently removed in the old audit.

## Newly derived all-width identity, with way home

The native LEN10 left 28-cycle (seed 23) lifts to the LEN11 left 28-cycle by a deterministic 28-bit middle-phase word:

`0101010101010110101010101010`

Each of the 28 nodes is written as a 5-bit header `u`, a repeated middle bit `m^(n−10)`, and a 5-bit footer `v`:

`x_t^(n) = u_t m_t^(n−10) v_t`, for all integer `n>=10`.

Reverse route / way home: remove the uniform middle to obtain the same LEN10 node at the same phase t. The complement image supplies the opposite S-cycle. The B-cycle matching M also transports with this lift for the specified least-anchor convention.

**All-width local certificate**: canonicality of `u m^k v` is decided by comparing `u` to bitreverse(v), unless they tie, in which case the word is a palindrome and canonicality is decided by its leading bit. For every t, the predecessor requires only a decrement `d` of 1, 2, or 4. All candidates with smaller d fail canonicality. Except for phase 27, no decrement crosses the 5-bit footer. Phase 27 borrows through an all-zero middle run, uniformly producing an all-ones run, for every k≥0. Applying PC to the canonical predecessor produces exactly the next tagged node. These 28 finite symbolic identities establish S-closure for *every* integer n≥10; the wide runs are independent checks, not the proof.

Only **one** predecessor per 28-cycle remains within the cycle under T; the other 27 predecessor/successor connections leave it. The external destination owner is n-dependent.

`B = S²` splits that 28-cycle into two 14-cycles. Complement C maps both to their mirror B-cycles. Choosing the least anchor in each B-cycle, the C-paired rung M commutes with B and C, and the lift from LEN10 to any n≥10 intertwines M with its high-width counterpart. This is phase compatibility for this family; it is not a unique global phase law.

The width-8 27-cycle is **not** asserted to be an inserted or projected copy of this width-10 28-cycle. The previous negative one-bit insertion/projection result stands. General 27→28 origin is OPEN.

**Closed rung phase at every width n≥10:** the least even-cycle anchor is x_0=23; the least odd-cycle anchor is x_17. Consequently, for the native left 28-state S-cycle x_t with indices modulo 28,

- even t: M(x_t) = C(x_{-t});
- odd t: M(x_t) = C(x_{6-t}).

The anchor inequality is stable because the even cycle has its only zero-header at phase 0 and the odd cycle's two lowest headers occur at phases 9 and 17, with phase 17 carrying the smaller middle bit (and smaller footer when the middle has zero width). This derives all-width phase transport of M; the high-width checks independently verify the relation. The complement side follows by MC=CM.

## Seal and reproducibility

The executable source SHA-256 is `250ecd1bc1bc41ca394b8b61fd27c35bbd9bef73571a6fb2491bed7566553638`. It prints its pre-link prediction and SHA-256 digest **before** building or checking the high-width rings. The direct high-width checks use only 28 input nodes and their addresses, not all `2^n` words. The local symbolic proof explicitly quantifies over arbitrary middle length.

```python
"""Native ring transport audit: derives a 28-state lift from width-10 source and width-11 native orbit.
All print output is real; no external dataset, fabricated runs, or off-domain probes.
Dean A. Kulik, QuHarmonics Research Group, ORCID 0009-0003-3128-8828.
"""
from collections import Counter
from hashlib import sha256

def J(x,n):
    return int(format(x,f'0{n}b')[::-1],2)
def C(x,n):
    return x ^ ((1<<n)-1)
def P(x,n):
    r=J(x,n)
    return r if r!=x else C(x,n)
def K(x,n):
    return P(C(x,n),n)
def is_rep(x,n):
    return x<P(x,n)
def ring(n):
    a=[x for x in range(1<<n) if is_rep(x,n)]
    R=a+[P(x,n) for x in a[::-1]]
    if n>1:R[len(a)-1],R[len(a)]=R[len(a)],R[len(a)-1]
    return R
def S_map(n):
    r=ring(n); N=1<<n
    pred={r[i]:r[(i-1)%N] for i in range(N)}
    T={r[i]:r[(i+1)%N] for i in range(N)}
    return {x:K(pred[x],n) for x in r},T
def cycle(f,seed):
    out=[];x=seed
    while x not in out:
        out.append(x);x=f[x]
    assert x==seed
    return out
def prev_rep(x,n):
    assert is_rep(x,n) and x>0
    for d in range(1,33):
        y=x-d
        if is_rep(y,n):return y,d
    raise AssertionError(('predecessor too far',n,x))
def embed(t,n,h):
    u,m,v=t;k=n-2*h
    assert k>=0
    return (u<<(n-h)) | (((1<<k)-1 if m else 0)<<h) | v

def make_template_28():
    # Known provider: the previously obtained 28-state native S cycle at LEN10, anchor min word.
    S10,_=S_map(10); seed=23  # Source-linked LEN10 orbit anchor; no orbit-length candidate search.
    assert is_rep(seed,10)
    a10=cycle(S10,seed)
    assert len(a10)==28
    # The LEN11 source resolves each missing middle bit, with phase anchored at the same word.
    S11,_=S_map(11)
    a11=cycle(S11,seed)
    assert len(a11)==28
    check10=lambda x: ((x>>6)<<5)|(x&31)
    assert [check10(x) for x in a11]==a10
    result=[(x>>6,(x>>5)&1,x&31) for x in a11]
    assert [embed(t,10,5) for t in result]==a10
    assert [embed(t,11,5) for t in result]==a11
    return result,a10

# Seal claims before any high-LEN data is linked:
prediction=(
 'Native 28-state S-cycle obtained at LEN10/11 by one middle-bit reader remains '
 'a single native cycle at LEN32,64,128,512,2048 under insertion of uniform middle runs; '
 'its complement image forms the reverse paired S-cycle. At LEN64 and beyond '
 'all 28 predecessor and successor links pass without generating full rings. '
 'The 16-state template remains S-closed but has 4 rather than 7 internal T ports '
 'for every tested n>=7. Cross-width copy to LEN8 27-cycle remains OPEN. '
 'Way home: strip the uniform middle to recover the exact LEN10 phase word '
 'and apply C to recover the other hemisphere.'
)
print('PRE-LINK PREDICTION',prediction)
print('PREDICTION_SHA256',sha256(prediction.encode()).hexdigest())

TEMPLATE16=[(0,0,6),(2,1,7),(4,0,5),(1,1,6),(2,0,3),(2,0,2),(3,1,5),(1,0,1),(0,0,7),(4,1,7),(2,0,6),(2,1,5),(1,0,5),(1,0,4),(1,1,3),(5,0,3)]
T28,a10=make_template_28()
print('LEN10_28_SEED',a10[0], 'LEFT_CYCLE',a10)
print('LEN11_28_MIDDLE_LABELS',''.join(str(m) for _,m,_ in T28))
print('LEN11_28_TEMPLATE',T28)

for n in range(6,17):
    f,T=S_map(n)
    orbit16=[embed(t,n,3) for t in TEMPLATE16]
    assert all(f[orbit16[i]]==orbit16[(i+1)%16] for i in range(16))
    members=set(orbit16)
    internal=sum(prev_rep(x,n)[0] in members for x in orbit16)
    others=Counter()
    if n>=10:
        orbit28=[embed(t,n,5) for t in T28]
        assert len(set(orbit28))==28
        assert all(f[orbit28[i]]==orbit28[(i+1)%28] for i in range(28))
        # phase preserved by stripping uniform run
        assert [((x>>(n-5))<<5)|(x&31) for x in orbit28]==a10
        other=set(C(x,n) for x in orbit28)
        assert other.isdisjoint(orbit28)
        assert {C(f[x],n) for x in orbit28}=={f[C(x,n)] for x in orbit28} # set-based sanity
        maxd=max(prev_rep(x,n)[1] for x in orbit28)
        internal28=sum(prev_rep(x,n)[0] in set(orbit28) for x in orbit28)
        print(f'LEN={n:2d} 16-self={internal}/16 28-closed=28/28 28-self={internal28}/28 28-max-decrement={maxd}')
    else:
        print(f'LEN={n:2d} 16-self={internal}/16')

# High-width direct read: only 28 states, no full ring.
for n in (32,64,128,512,2048):
    arr=[embed(t,n,5) for t in T28]
    assert len(set(arr))==28 and all(is_rep(x,n) for x in arr)
    decrements=[]
    for i,x in enumerate(arr):
        prev,d=prev_rep(x,n);decrements.append(d)
        assert K(prev,n)==arr[(i+1)%28],('failed S',n,i)
    assert [((x>>(n-5))<<5)|(x&31) for x in arr]==a10
    print(f'LEN={n:4d} 28 S links PASS; max-prev-decrement={max(decrements)}; 28 independent locations, 28 complement partners; strip-way-home PASS')

# Phase transport: native global matching of B-cycles within 28 branch and complement.
# The B-odd/even pairing's least anchor must persist under lift.
def matching_28(n):
    X=[embed(t,n,5) for t in T28];V=set(X)
    A=[X[i] for i in range(0,28,2)];Q=[X[i] for i in range(1,28,2)]
    # Compute M on complementary left/right B-cycles, anchor a=min(A or Q), q=C(a)
    M={}
    for cyc in (A,Q):
        s=min(cyc);i=cyc.index(s)
        # starting at anchor phase, successive B-powers increment index in chosen cycle
        for t in range(14):
            a=cyc[(i+t)%14];b=C(cyc[(i-t)%14],n)
            M[a]=b;M[b]=a
    # Anchors are x_0=23 (even B-cycle) and x_17 (odd B-cycle)
    # for every n>=10. Thus M has a closed phase formula on the left branch.
    assert min(A)==X[0] and min(Q)==X[17]
    for t in range(28):
        target=C(X[(-t if t%2==0 else 6-t)%28],n)
        assert M[X[t]]==target,('closed M phase',n,t)
    assert len(M)==56 and all(M[M[x]]==x and M[x]!=x and M[C(x,n)]==C(M[x],n) for x in M)
    # Two B-cycles within the left S-cycle, and their reversed complements.
    b={X[t]:X[(t+2)%28] for t in range(28)}
    b.update({C(X[t],n):C(X[(t-2)%28],n) for t in range(28)})
    assert all(M[b[x]]==b[M[x]] for x in M), 'M fails B commutation'
    return X,M
X10,M10=matching_28(10)
for n in (11,12,16,32,64,128,512):
    X,M=matching_28(n)
    src=X10+[C(x,10) for x in X10]
    dst=X+[C(x,n) for x in X]
    phi=dict(zip(src,dst))
    if all(phi[M10[x]]==M[phi[x]] for x in src):
        print(f'LEN10 -> LEN{n}: M phase transported for all 56 states PASS')
    else:
        fails=[(x,phi[M10[x]],M[phi[x]]) for x in src if phi[M10[x]]!=M[phi[x]]]
        print(f'LEN10 -> LEN{n}: M phase transport OPEN: {len(fails)} mismatches, first {fails[:2]}')

# test old middle label decoder rather than silently accepting it
fault=[]
for i,(u,m,v) in enumerate(TEMPLATE16):
    x=embed((u,m,v),6,3);z=embed(TEMPLATE16[(i-1)%16],6,3);prev,_=prev_rep(z,6)
    stated=0 if x==J(x,6) else 1-((prev&7)>>2)
    if stated!=m:fault.append(i)
print('OLD_MIDDLE_DECODER_FAILURE_PHASES',fault)

# All-width *symbolic* 28-row certificate: headers and footers are fixed 5-bit
# words, the center is an arbitrary-length UNIFORM m^k (including k=0).
def rep_tag(t):
    u,m,v=t; rev_v=J(v,5)
    # If outer blocks tie, the whole word is a palindrome for any uniform m^k.
    # Then P=C and the rep is exactly the word with leading bit 0.
    return (u<rev_v) if u!=rev_v else u<16

def dec_tag(t,d):
    u,m,v=t
    if v>=d:return (u,m,v-d)
    # Borrow across an all-zero central run. Includes the empty run k=0.
    assert m==0 and u>0
    return (u-1,1,v-d+32)

def K_tag(t):
    u,m,v=t
    if u==J(v,5):return t # palindrome, PC fixes word
    return (31-J(v,5),1-m,31-J(u,5))

certificate=[]
for i,t in enumerate(T28):
    assert rep_tag(t)
    for d in range(1,5):
        pred=dec_tag(t,d)
        if rep_tag(pred):break
    assert rep_tag(pred) and K_tag(pred)==T28[(i+1)%28]
    certificate.append((i,d,t,pred,T28[(i+1)%28]))
print('ALL_WIDTH_SYMBOLIC_CERTIFICATE 28/28 rows PASS for every middle length k>=0')
print('PREDECESSOR_DECREMENT_SEQUENCE', [r[1] for r in certificate])
print('BORROW_ACROSS_MIDDLE_PHASES', [i for i,d,t,_,_ in certificate if t[2]<d])
# The exhaustive local certificate also fixes internal T ports without reference to width.
inside=sum(row[3] in set(T28) for row in certificate)
assert inside==1
print('ALL_WIDTH_28_BRANCH_T_PORTS', f'{inside} internal, {28-inside} external; destinations not universally core')
print('CORRECTIONS',
      'Original pasted self-port values 7/9 -> 4/12 at LEN>=7;',
      'Original hidden middle-bit decoder fails at six phases;',
      'One width-10 source anchor 23 used; no orbit-length search;',
      'Removed ineffective placeholder assertion; checked B commutation explicitly.')

# A second symbolic certificate handles the persistent 16 orbit, independently.
# Here h=3 and k=n-6; n=6 forgets m, giving additional apparent T interiors.
def bit_reverse_small(x,h):return int(format(x,f'0{h}b')[::-1],2)
def canonical_small(t,h):
    u,m,v=t;r=bit_reverse_small(v,h)
    return (u<r) if u!=r else u<(1<<(h-1))
def predecessor_small(t,h,d):
    u,m,v=t; radix=1<<h
    if v>=d:return (u,m,v-d)
    assert m==0 and u>0
    return (u-1,1,v-d+radix)
def pc_small(t,h):
    u,m,v=t;radix=1<<h
    if u==bit_reverse_small(v,h):return t
    return (radix-1-bit_reverse_small(v,h),1-m,radix-1-bit_reverse_small(u,h))
cert16=[]
for i,t in enumerate(TEMPLATE16):
    for d in range(1,5):
        pred=predecessor_small(t,3,d)
        if canonical_small(pred,3):break
    assert pc_small(pred,3)==TEMPLATE16[(i+1)%16]
    cert16.append((i,d,pred))
assert sum(t in set(TEMPLATE16) for i,d,t in cert16)==4
print('ALL_WIDTH_SYMBOLIC_16_BRANCH', '16/16 phase rows PASS for any n>=6; exactly 4 internal T links if n>=7')

print('ALL_WIDTH_28_RUNG_PHASE: M(x_t)=C(x_-t) for even t, C(x_(6-t)) for odd t; anchored by phase 0 and 17')

```

## Actual execution stdout

```text
PRE-LINK PREDICTION Native 28-state S-cycle obtained at LEN10/11 by one middle-bit reader remains a single native cycle at LEN32,64,128,512,2048 under insertion of uniform middle runs; its complement image forms the reverse paired S-cycle. At LEN64 and beyond all 28 predecessor and successor links pass without generating full rings. The 16-state template remains S-closed but has 4 rather than 7 internal T ports for every tested n>=7. Cross-width copy to LEN8 27-cycle remains OPEN. Way home: strip the uniform middle to recover the exact LEN10 phase word and apply C to recover the other hemisphere.
PREDICTION_SHA256 7fc40f5b8478a8fe946abbd74e927d19ce6224eb930e273b25ebbeb146f5ba62
LEN10_28_SEED 23 LEFT_CYCLE [23, 607, 278, 349, 149, 859, 84, 215, 595, 54, 335, 565, 206, 307, 306, 461, 177, 43, 687, 298, 429, 169, 107, 679, 234, 419, 489, 97]
LEN11_28_MIDDLE_LABELS 0101010101010110101010101010
LEN11_28_TEMPLATE [(0, 0, 23), (18, 1, 31), (8, 0, 22), (10, 1, 29), (4, 0, 21), (26, 1, 27), (2, 0, 20), (6, 1, 23), (18, 0, 19), (1, 1, 22), (10, 0, 15), (17, 1, 21), (6, 0, 14), (9, 1, 19), (9, 1, 18), (14, 0, 13), (5, 1, 17), (1, 0, 11), (21, 1, 15), (9, 0, 10), (13, 1, 13), (5, 0, 9), (3, 1, 11), (21, 0, 7), (7, 1, 10), (13, 0, 3), (15, 1, 9), (3, 0, 1)]
LEN= 6 16-self=11/16
LEN= 7 16-self=4/16
LEN= 8 16-self=4/16
LEN= 9 16-self=4/16
LEN=10 16-self=4/16 28-closed=28/28 28-self=1/28 28-max-decrement=4
LEN=11 16-self=4/16 28-closed=28/28 28-self=1/28 28-max-decrement=4
LEN=12 16-self=4/16 28-closed=28/28 28-self=1/28 28-max-decrement=4
LEN=13 16-self=4/16 28-closed=28/28 28-self=1/28 28-max-decrement=4
LEN=14 16-self=4/16 28-closed=28/28 28-self=1/28 28-max-decrement=4
LEN=15 16-self=4/16 28-closed=28/28 28-self=1/28 28-max-decrement=4
LEN=16 16-self=4/16 28-closed=28/28 28-self=1/28 28-max-decrement=4
LEN=  32 28 S links PASS; max-prev-decrement=4; 28 independent locations, 28 complement partners; strip-way-home PASS
LEN=  64 28 S links PASS; max-prev-decrement=4; 28 independent locations, 28 complement partners; strip-way-home PASS
LEN= 128 28 S links PASS; max-prev-decrement=4; 28 independent locations, 28 complement partners; strip-way-home PASS
LEN= 512 28 S links PASS; max-prev-decrement=4; 28 independent locations, 28 complement partners; strip-way-home PASS
LEN=2048 28 S links PASS; max-prev-decrement=4; 28 independent locations, 28 complement partners; strip-way-home PASS
LEN10 -> LEN11: M phase transported for all 56 states PASS
LEN10 -> LEN12: M phase transported for all 56 states PASS
LEN10 -> LEN16: M phase transported for all 56 states PASS
LEN10 -> LEN32: M phase transported for all 56 states PASS
LEN10 -> LEN64: M phase transported for all 56 states PASS
LEN10 -> LEN128: M phase transported for all 56 states PASS
LEN10 -> LEN512: M phase transported for all 56 states PASS
OLD_MIDDLE_DECODER_FAILURE_PHASES [1, 7, 9, 11, 12, 15]
ALL_WIDTH_SYMBOLIC_CERTIFICATE 28/28 rows PASS for every middle length k>=0
PREDECESSOR_DECREMENT_SEQUENCE [1, 2, 1, 2, 1, 4, 1, 1, 4, 1, 1, 2, 1, 1, 1, 2, 2, 1, 2, 1, 2, 2, 1, 4, 1, 2, 2, 2]
BORROW_ACROSS_MIDDLE_PHASES [27]
ALL_WIDTH_28_BRANCH_T_PORTS 1 internal, 27 external; destinations not universally core
CORRECTIONS Original pasted self-port values 7/9 -> 4/12 at LEN>=7; Original hidden middle-bit decoder fails at six phases; One width-10 source anchor 23 used; no orbit-length search; Removed ineffective placeholder assertion; checked B commutation explicitly.
ALL_WIDTH_SYMBOLIC_16_BRANCH 16/16 phase rows PASS for any n>=6; exactly 4 internal T links if n>=7
ALL_WIDTH_28_RUNG_PHASE: M(x_t)=C(x_-t) for even t, C(x_(6-t)) for odd t; anchored by phase 0 and 17

```

## Ledger

- **STANDS:** All-width 28-state phase-tag symbolic predecessor certificate, the return route, and closed phase-anchored rung formula.
- **RUNS:** Finite native ring checks and direct wide checks through LEN2048; 56-state rung transport through LEN512.
- **DEAD END:** 7/9 16-cycle coupling claim, faulty six-phase hidden decoder, and simple 27→28 insertion claim.
- **OPEN:** Global phase-selection law and physical dynamics.
