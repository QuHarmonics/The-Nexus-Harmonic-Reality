# Running audit — bridge square root, folded spine, and LEN=6

This is one append-ready Markdown record containing source, checks, results, and interpretation. No prior running-log entry is overwritten. The code is an independent audit of the supplied formulas; it records topology and orthogonality rather than assuming every proposed global conclusion.

Pre-run source-block SHA-256: `441c05587431ab2e16a815a9cd869e8fad5b6cca5062a92dabecd926508174d8`

Hash policy: UTF-8 bytes of the Python source string below, including its final newline. This source-block seal is not a claim that the final appended Markdown file has an unchanged checksum.

## Executable source

```python
import math,json,time,collections,ast

def J(x,n):return int(format(x,f'0{n}b')[::-1],2)
def C(x,n):return x^((1<<n)-1)
def P(x,n):
 r=J(x,n);return r if r!=x else C(x,n)
def ring(n):
 N=1<<n;reps=[x for x in range(N) if x<P(x,n)];R=reps+[P(x,n) for x in reversed(reps)]
 if n>1:R[N//2-1],R[N//2]=R[N//2],R[N//2-1]
 return R

def cycles(perm):
 seen=set();out=[]
 for x in range(len(perm)):
  if x in seen:continue
  seq=[];cur=x
  while cur not in seen:seen.add(cur);seq.append(cur);cur=perm[cur]
  assert cur==seq[0];out.append(seq)
 return out

def maps(n):
 R=ring(n);N=len(R);T=[0]*N;Ti=[0]*N;tau=[0]*N
 for i,x in enumerate(R):T[x]=R[(i+1)%N];Ti[x]=R[(i-1)%N];tau[x]=R[-i%N]
 pp=[P(x,n) for x in range(N)];cc=[C(x,n) for x in range(N)];K=[pp[cc[x]] for x in range(N)]
 TC=[cc[T[cc[x]]] for x in range(N)];S=[cc[tau[x]] for x in range(N)];B=[TC[Ti[x]] for x in range(N)]
 assert all(pp[T[pp[x]]]==Ti[x] and pp[cc[x]]==cc[pp[x]] for x in range(N))
 assert all(TC[x]==K[Ti[K[x]]] and S[x]==K[Ti[x]] and S[S[x]]==B[x] for x in range(N))
 return R,T,Ti,pp,cc,K,tau,TC,S,B

def graph_components(cc,tau):
 seen=set();out=[]
 for x in range(len(cc)):
  if x in seen:continue
  todo=[x];component=[];seen.add(x)
  while todo:
   y=todo.pop();component.append(y)
   for z in (cc[y],tau[y]):
    if z not in seen:seen.add(z);todo.append(z)
  out.append(sorted(component))
 return out

def edge(a,b):return tuple(sorted((a,b)))
def degrees(edges,vertices):
 d={v:0 for v in vertices}
 for a,b in edges:d[a]+=1;d[b]+=1
 return d

def make_prism(n):
 R,T,Ti,pp,cc,K,tau,TC,S,B=maps(n);N=len(R);Si=[0]*N
 for x,y in enumerate(S):Si[y]=x
 orbit=[];x=0
 while not orbit or x!=0:orbit.append(x);x=S[x]
 assert len(orbit)==N
 A=orbit[::2];Q=[Si[x] for x in A];rungs={}
 for a,q in zip(A,Q):rungs[a]=q;rungs[q]=a
 assert len(rungs)==N and all(rungs[rungs[x]]==x and B[rungs[x]]==rungs[B[x]] for x in R)
 edges={edge(x,B[x]) for x in R}|{edge(x,rungs[x]) for x in R}
 assert set(degrees(edges,R).values())=={3}
 # Explicit abstract embedding, not an assumption about literal word coordinates.
 labels={}
 for k,(a,q) in enumerate(zip(A,Q)):
  gray=k^(k>>1);labels[a]=gray;labels[q]=gray|(1<<(n-1))
 assert len(set(labels.values()))==N
 relabeled={edge(labels[a],labels[b]) for a,b in edges};cube={edge(x,x^(1<<j)) for x in range(N) for j in range(n)}
 assert relabeled<=cube
 return {'A':A,'Q':Q,'rung_masks':[a^q for a,q in zip(A,Q)],'edges':edges,'labels':labels,'cube_edges':cube,'relabeled_edges':relabeled,'B':B,'P':pp,'C':cc,'K':K,'T':T,'TC':TC,'rungs':rungs}

def run():
 start=time.perf_counter();rows=[];len6=None;first_detachment=None;first_agreement=None
 original={};tree=ast.parse(open('pairs_forced.py').read())
 exec(compile(ast.Module(body=[n for n in tree.body if isinstance(n,ast.FunctionDef) and n.name in ('partner','grow')],type_ignores=[]),'original','exec'),original)
 for n in range(2,17):
  R,T,Ti,pp,cc,K,tau,TC,S,B=maps(n);N=len(R)
  if n<=10:assert R==[int(w,2) for w in original['grow'](n)]
  assert [x for x in R if tau[x]==x]==[R[0],R[N//2]]
  sc=cycles(S);bc=cycles(B);components=graph_components(cc,tau);spinal=next(c for c in components if 0 in c)
  assert R[N//2] in spinal
  spine=[0];cur=0
  for _ in range(N+1):
   cur=cc[cur];spine.append(cur)
   if tau[cur]==cur:break
   cur=tau[cur];spine.append(cur)
  else:raise AssertionError('spine did not reach the other pole')
  assert spine[-1]==R[N//2] and len(set(spine))==len(spine) and set(spine)==set(spinal)
  frob=sum(T[x]==TC[x] for x in R);Bfixed=sum(B[x]==x for x in R);assert frob==Bfixed
  if len(spinal)<N and first_detachment is None:first_detachment=n
  if frob and first_agreement is None:first_agreement=n
  rows.append({'n':n,'N':N,'Frobenius_agreement_count':frob,'S_cycle_length_counts':dict(collections.Counter(map(len,sc))),'B_cycle_length_counts':dict(collections.Counter(map(len,bc))),'spine_vertices':len(spine),'spine_fraction':str(len(spine))+'/'+str(N),'detached_components':len(components)-1,'S_fixed_points':sum(S[x]==x for x in R),'PC_adjacent_forward_edges':sum(T[x]==K[x] for x in R)})
  if n==6:
   details=[]
   for component in components:
    members=set(component)
    details.append({'origin_component':0 in members,'vertices':component,'binary_vertices':[format(x,'06b') for x in component],'tau_poles':[x for x in component if tau[x]==x],'S_cycles':[c for c in sc if c[0] in members],'B_cycles':[c for c in bc if c[0] in members]})
   len6={'ring':R,'origin':0,'seam':R[N//2],'spine_path':spine,'components':details,'T_TC_agreement_states':[x for x in R if T[x]==TC[x]]}
 prisms={n:make_prism(n) for n in (3,4)};g=prisms[4];d=lambda x:(x^(x>>1))&7
 projected=collections.Counter(edge(d(a),d(b)) for a,b in g['edges']);qdegree=degrees(set(projected),range(8))
 noncube=[{'source_edge':[a,b],'image':[d(a),d(b)],'xor_mask':d(a)^d(b)} for a,b in sorted(g['edges']) if (d(a)^d(b)).bit_count()!=1]
 assert all(d(x)==d(x^15) for x in range(16)) and [x for x in range(16) if d(x)==0]==[0,15]
 assert all(d(J(x,4))==J(d(x),3) for x in range(16))
 assert sorted(map(d,g['A']))==list(range(8)) and sorted(map(d,g['Q']))==list(range(8))
 project_report={'A':g['A'],'Q':g['Q'],'dA':list(map(d,g['A'])),'dQ':list(map(d,g['Q'])),'source_prism_edges':len(g['edges']),'image_distinct_edges':len(projected),'image_degrees':qdegree,'edge_image_multiplicities':{str(k):v for k,v in sorted(projected.items())},'non_Hamming_cube_edge_examples':noncube[:5],'is_cover_of_standard_simple_Q3':False}
 p3=prisms[3];dA=list(map(d,g['A']));checks=[]
 for k,name in zip((0,2,4,6),('M3','B3_squared','P3C3','P3')):
  x,y=dA[k],dA[k+1]
  actual=p3['rungs'][x] if name=='M3' else p3['B'][p3['B'][x]] if name=='B3_squared' else p3['K'][x] if name=='P3C3' else p3['P'][x]
  checks.append({'label':name,'projected_edge':[x,y],'actual_operator_image':actual,'matches':actual==y})
 prism_report=[]
 for n,h in prisms.items():
  traversal={edge(x,h['T'][x]) for x in range(1<<n)}|{edge(x,h['TC'][x]) for x in range(1<<n)}
  counts={j:sum(edge(x,x^(1<<j)) in traversal for x in range(1<<n))//2 for j in range(n)}
  prism_report.append({'n':n,'A':h['A'],'Q':h['Q'],'rung_masks':h['rung_masks'],'prism_edges':len(h['edges']),'literal_binary_cube_edges_in_prism':sum((a^b).bit_count()==1 for a,b in h['edges']),'abstract_gray_embedding_into_Qn':True,'gray_relabeling':h['labels'],'missing_cube_edges_after_gray_relabeling':[list(e) for e in sorted(h['cube_edges']-h['relabeled_edges'])],'single_bit_edges_in_T_union_TC':counts})
 result={'scope':'Independent exact finite ring/operator/graph audit. No unseen source files, physical mechanism or all-width topology assertion is claimed.','width_results':rows,'first_detached_component_width':first_detachment,'first_nonzero_Frobenius_agreement_width':first_agreement,'LEN6':len6,'small_prism_graphs':prism_report,'differential_quotient':project_report,'projected_operator_label_checks':checks,'seconds':time.perf_counter()-start}
 print(json.dumps({'width_results':rows,'first_detachment':first_detachment,'first_nonzero_agreement':first_agreement,'LEN6':len6,'prisms':prism_report,'differential_quotient':project_report,'projected_labels':checks,'seconds':result['seconds']},indent=2))
 return result
```
