# Running audit continuation — global rungs after detachment

This single Markdown entry continues the bridge/spine audit. It contains the complete source and results for this stroke; no earlier log file is overwritten. The source-block hash is recorded before execution. The final appended document is not claimed to retain that same whole-file checksum.

## Pre-run claims and conventions

The proposed global matching pairs every B-cycle with its distinct C-image. The Origin-to-Seam pair retains its earlier S-inverse anchor. Detached pairs use C of their least unhandled word. This is an explicitly fixed phase convention, not a uniqueness claim. Tests will check M squared equals identity, no fixed points, commutation with B and C, and preservation of the LEN=3/4 rungs. The odd S-orbits at LEN=8 will be checked rather than paired by an impossible alternating-neighbor rule.

Audit source-block SHA-256: `39c153fa0b8d83f96fc0b02e7627ff975cd897c33cae02195c9272813f532d31`

## Executable source

```python
import json,time,collections,math,ast

def J(x,n):return int(format(x,f'0{n}b')[::-1],2)
def C(x,n):return x^((1<<n)-1)
def P(x,n):
 r=J(x,n);return r if r!=x else C(x,n)
def ring(n):
 reps=[x for x in range(1<<n) if x<P(x,n)];R=reps+[P(x,n) for x in reversed(reps)]
 if n>1:R[len(reps)-1],R[len(reps)]=R[len(reps)],R[len(reps)-1]
 return R

def cycles(perm):
 seen=set();result=[]
 for x in range(len(perm)):
  if x in seen:continue
  seq=[];cur=x
  while cur not in seen:seen.add(cur);seq.append(cur);cur=perm[cur]
  assert cur==seq[0];result.append(seq)
 return result

def maps(n):
 R=ring(n);N=len(R);T=[0]*N;Ti=[0]*N;tau=[0]*N
 for i,x in enumerate(R):T[x]=R[(i+1)%N];Ti[x]=R[(i-1)%N];tau[x]=R[-i%N]
 cc=[C(x,n) for x in range(N)];pp=[P(x,n) for x in range(N)];TC=[cc[T[cc[x]]] for x in range(N)]
 S=[cc[tau[x]] for x in range(N)];B=[TC[Ti[x]] for x in range(N)];Si=[0]*N
 for x,y in enumerate(S):Si[y]=x
 assert all(S[S[x]]==B[x] and cc[B[cc[B[x]]]]==x for x in range(N))
 return R,T,cc,tau,S,Si,B

def orbit(perm,a):
 out=[a];x=perm[a]
 while x!=a:out.append(x);x=perm[x]
 return out

def global_matching(B,C,Si):
 N=len(B);used=[False]*N;M=[-1]*N;pairs=[]
 for a in range(N):
  if used[a]:continue
  A=orbit(B,a);q=Si[a] if a==0 else C[a];Q=orbit(B,q)
  assert len(A)==len(Q) and set(A).isdisjoint(Q)
  assert {C[x] for x in A}==set(Q)
  for x,y in zip(A,Q):M[x]=y;M[y]=x;used[x]=used[y]=True
  pairs.append({'seed':a,'rung_seed':q,'cycle_length':len(A),'origin_pair':a==0,'anchor_rule':'S_inverse(0)' if a==0 else 'C(seed)','A':A,'Q':Q})
 assert all(used)
 assert all(M[x]!=x and M[M[x]]==x and B[M[x]]==M[B[x]] and C[M[x]]==M[C[x]] for x in range(N))
 return M,pairs

def edge(x,y):return tuple(sorted((x,y)))

def run():
 start=time.perf_counter();rows=[];examples={};state_checks=0;first_odd_prism=None
 original={};tree=ast.parse(open('pairs_forced.py').read())
 exec(compile(ast.Module(body=[n for n in tree.body if isinstance(n,ast.FunctionDef) and n.name in ('partner','grow')],type_ignores=[]),'original','exec'),original)
 for n in range(2,17):
  R,T,C,tau,S,Si,B=maps(n);N=len(R)
  if n<=10:assert R==[int(w,2) for w in original['grow'](n)]
  M,pairs=global_matching(B,C,Si);state_checks+=N
  edges={edge(x,B[x]) for x in range(N)}|{edge(x,M[x]) for x in range(N)}
  degree=[0]*N
  for x,y in edges:degree[x]+=1;degree[y]+=1
  if n>=3:assert set(degree)=={3} and len(edges)==3*N//2
  else:assert set(degree)=={2}
  expected=[]
  for pair in pairs:
   A=pair['A'];Q=pair['Q'];m=len(A);vertices=set(A+Q)
   wanted={edge(A[k],A[(k+1)%m]) for k in range(m)}|{edge(Q[k],Q[(k+1)%m]) for k in range(m)}|{edge(x,y) for x,y in zip(A,Q)}
   actual={edge(x,B[x]) for x in vertices}|{edge(x,M[x]) for x in vertices}
   assert actual==wanted
   expected.append(m)
   if m%2 and first_odd_prism is None:first_odd_prism=n
  choices=math.prod(expected);origin_length=next(p['cycle_length'] for p in pairs if p['origin_pair'])
  frob=sum(T[x]==(T[C[x]]^((1<<n)-1)) for x in range(N))
  row={'n':n,'N':N,'all_state_matching_checks':True,'B_cycle_pair_lengths':dict(collections.Counter(expected)),'prism_components':len(pairs),'simple_graph_edges':len(edges),'graph_is_bipartite':all(m%2==0 for m in expected),'odd_prism_cycle_lengths':sorted(m for m in expected if m%2),'C_paired_B_commuting_phase_choices':str(choices),'phase_choices_with_origin_rung_fixed':str(choices//origin_length),'Frobenius_agreement':frob}
  rows.append(row)
  if n in (3,4):
   old={}
   A=orbit(B,0)
   for x in A:old[x]=Si[x];old[Si[x]]=x
   assert all(old[x]==M[x] for x in range(N))
   if n==3:assert all(M[x]==x^1 for x in range(N))
   if n==4:assert [M[x]^x for x in A]==[1,1,5,3,8,8,3,5]
  if n in (6,8):
   examples[str(n)]={'pairs':pairs,'rungs':[list(e) for e in sorted({edge(x,M[x]) for x in range(N)})],'M_table':M}
   if n==8:
    Sodd=[cy for cy in cycles(S) if len(cy)%2]
    for cy in Sodd:
     assert all(M[x] not in set(cy) for x in cy)
    examples[str(n)]['odd_S_cycle_lengths']=[len(cy) for cy in Sodd]
    examples[str(n)]['global_rungs_leave_each_odd_S_orbit']=True
 result={'scope':'New global rung construction for the original rings; exact mathematical finite-state audit, no physical interpretation. Compiling the map enumerates the finite field in this implementation.','definition':'Pair each B-cycle A with C(A). Choose the least unhandled word a. Use q0=S_inverse(0) for the origin pair and q0=C(a) otherwise. Set M(B^j a)=B^j q0 in both directions.','phase_convention_is_explicit_not_unique':True,'width_results':rows,'state_checks':state_checks,'first_nonbipartite_prism_width':first_odd_prism,'examples':examples,'seconds':time.perf_counter()-start}
 print(json.dumps({'width_results':rows,'LEN6_pairs':examples['6']['pairs'],'LEN8_odd_cycle_fix':{'S_odd_lengths':examples['8']['odd_S_cycle_lengths'],'rungs_leave_each_odd_S_orbit':True},'states_checked':state_checks,'first_odd_prism_width':first_odd_prism,'seconds':result['seconds']},indent=2))
 return result
```
