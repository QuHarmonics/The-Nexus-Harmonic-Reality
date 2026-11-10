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

## Exact execution results

```json
{
  "scope": "Independent exact finite ring/operator/graph audit. No unseen source files, physical mechanism or all-width topology assertion is claimed.",
  "width_results": [
    {
      "n": 2,
      "N": 4,
      "Frobenius_agreement_count": 0,
      "S_cycle_length_counts": {
        "4": 1
      },
      "B_cycle_length_counts": {
        "2": 2
      },
      "spine_vertices": 4,
      "spine_fraction": "4/4",
      "detached_components": 0,
      "S_fixed_points": 0,
      "PC_adjacent_forward_edges": 0
    },
    {
      "n": 3,
      "N": 8,
      "Frobenius_agreement_count": 0,
      "S_cycle_length_counts": {
        "8": 1
      },
      "B_cycle_length_counts": {
        "4": 2
      },
      "spine_vertices": 8,
      "spine_fraction": "8/8",
      "detached_components": 0,
      "S_fixed_points": 0,
      "PC_adjacent_forward_edges": 0
    },
    {
      "n": 4,
      "N": 16,
      "Frobenius_agreement_count": 0,
      "S_cycle_length_counts": {
        "16": 1
      },
      "B_cycle_length_counts": {
        "8": 2
      },
      "spine_vertices": 16,
      "spine_fraction": "16/16",
      "detached_components": 0,
      "S_fixed_points": 0,
      "PC_adjacent_forward_edges": 0
    },
    {
      "n": 5,
      "N": 32,
      "Frobenius_agreement_count": 0,
      "S_cycle_length_counts": {
        "32": 1
      },
      "B_cycle_length_counts": {
        "16": 2
      },
      "spine_vertices": 32,
      "spine_fraction": "32/32",
      "detached_components": 0,
      "S_fixed_points": 0,
      "PC_adjacent_forward_edges": 0
    },
    {
      "n": 6,
      "N": 64,
      "Frobenius_agreement_count": 0,
      "S_cycle_length_counts": {
        "32": 1,
        "16": 2
      },
      "B_cycle_length_counts": {
        "16": 2,
        "8": 4
      },
      "spine_vertices": 32,
      "spine_fraction": "32/64",
      "detached_components": 1,
      "S_fixed_points": 0,
      "PC_adjacent_forward_edges": 0
    },
    {
      "n": 7,
      "N": 128,
      "Frobenius_agreement_count": 0,
      "S_cycle_length_counts": {
        "96": 1,
        "16": 2
      },
      "B_cycle_length_counts": {
        "48": 2,
        "8": 4
      },
      "spine_vertices": 96,
      "spine_fraction": "96/128",
      "detached_components": 1,
      "S_fixed_points": 0,
      "PC_adjacent_forward_edges": 0
    },
    {
      "n": 8,
      "N": 256,
      "Frobenius_agreement_count": 0,
      "S_cycle_length_counts": {
        "170": 1,
        "16": 2,
        "27": 2
      },
      "B_cycle_length_counts": {
        "85": 2,
        "8": 4,
        "27": 2
      },
      "spine_vertices": 170,
      "spine_fraction": "170/256",
      "detached_components": 2,
      "S_fixed_points": 0,
      "PC_adjacent_forward_edges": 0
    },
    {
      "n": 9,
      "N": 512,
      "Frobenius_agreement_count": 0,
      "S_cycle_length_counts": {
        "466": 1,
        "16": 2,
        "7": 2
      },
      "B_cycle_length_counts": {
        "233": 2,
        "8": 4,
        "7": 2
      },
      "spine_vertices": 466,
      "spine_fraction": "466/512",
      "detached_components": 2,
      "S_fixed_points": 0,
      "PC_adjacent_forward_edges": 0
    },
    {
      "n": 10,
      "N": 1024,
      "Frobenius_agreement_count": 0,
      "S_cycle_length_counts": {
        "936": 1,
        "16": 2,
        "28": 2
      },
      "B_cycle_length_counts": {
        "468": 2,
        "8": 4,
        "14": 4
      },
      "spine_vertices": 936,
      "spine_fraction": "936/1024",
      "detached_components": 2,
      "S_fixed_points": 0,
      "PC_adjacent_forward_edges": 0
    },
    {
      "n": 11,
      "N": 2048,
      "Frobenius_agreement_count": 0,
      "S_cycle_length_counts": {
        "1816": 1,
        "16": 4,
        "28": 2,
        "56": 2
      },
      "B_cycle_length_counts": {
        "908": 2,
        "8": 8,
        "14": 4,
        "28": 4
      },
      "spine_vertices": 1816,
      "spine_fraction": "1816/2048",
      "detached_components": 4,
      "S_fixed_points": 0,
      "PC_adjacent_forward_edges": 0
    },
    {
      "n": 12,
      "N": 4096,
      "Frobenius_agreement_count": 0,
      "S_cycle_length_counts": {
        "4008": 1,
        "16": 2,
        "28": 2
      },
      "B_cycle_length_counts": {
        "2004": 2,
        "8": 4,
        "14": 4
      },
      "spine_vertices": 4008,
      "spine_fraction": "4008/4096",
      "detached_components": 2,
      "S_fixed_points": 0,
      "PC_adjacent_forward_edges": 0
    },
    {
      "n": 13,
      "N": 8192,
      "Frobenius_agreement_count": 0,
      "S_cycle_length_counts": {
        "7444": 1,
        "16": 2,
        "28": 2,
        "75": 2,
        "153": 2,
        "64": 2,
        "38": 2
      },
      "B_cycle_length_counts": {
        "3722": 2,
        "8": 4,
        "14": 4,
        "75": 2,
        "153": 2,
        "32": 4,
        "19": 4
      },
      "spine_vertices": 7444,
      "spine_fraction": "7444/8192",
      "detached_components": 6,
      "S_fixed_points": 0,
      "PC_adjacent_forward_edges": 0
    },
    {
      "n": 14,
      "N": 16384,
      "Frobenius_agreement_count": 0,
      "S_cycle_length_counts": {
        "1592": 1,
        "855": 2,
        "16": 2,
        "2060": 2,
        "28": 2,
        "2056": 2,
        "903": 2,
        "858": 2,
        "197": 2,
        "423": 2
      },
      "B_cycle_length_counts": {
        "796": 2,
        "855": 2,
        "8": 4,
        "1030": 4,
        "14": 4,
        "1028": 4,
        "903": 2,
        "429": 4,
        "197": 2,
        "423": 2
      },
      "spine_vertices": 1592,
      "spine_fraction": "1592/16384",
      "detached_components": 9,
      "S_fixed_points": 0,
      "PC_adjacent_forward_edges": 0
    },
    {
      "n": 15,
      "N": 32768,
      "Frobenius_agreement_count": 0,
      "S_cycle_length_counts": {
        "16966": 1,
        "855": 2,
        "16": 2,
        "3032": 2,
        "28": 2,
        "858": 2,
        "797": 2,
        "2013": 2,
        "180": 2,
        "122": 2
      },
      "B_cycle_length_counts": {
        "8483": 2,
        "855": 2,
        "8": 4,
        "1516": 4,
        "14": 4,
        "429": 4,
        "797": 2,
        "2013": 2,
        "90": 4,
        "61": 4
      },
      "spine_vertices": 16966,
      "spine_fraction": "16966/32768",
      "detached_components": 9,
      "S_fixed_points": 0,
      "PC_adjacent_forward_edges": 0
    },
    {
      "n": 16,
      "N": 65536,
      "Frobenius_agreement_count": 0,
      "S_cycle_length_counts": {
        "60842": 1,
        "855": 2,
        "16": 2,
        "28": 2,
        "858": 2,
        "393": 2,
        "197": 2
      },
      "B_cycle_length_counts": {
        "30421": 2,
        "855": 2,
        "8": 4,
        "14": 4,
        "429": 4,
        "393": 2,
        "197": 2
      },
      "spine_vertices": 60842,
      "spine_fraction": "60842/65536",
      "detached_components": 6,
      "S_fixed_points": 0,
      "PC_adjacent_forward_edges": 0
    }
  ],
  "first_detached_component_width": 6,
  "first_nonzero_Frobenius_agreement_width": null,
  "LEN6": {
    "ring": [
      0,
      1,
      2,
      3,
      4,
      5,
      6,
      7,
      9,
      10,
      11,
      12,
      13,
      14,
      15,
      17,
      18,
      19,
      21,
      22,
      23,
      25,
      27,
      29,
      30,
      31,
      35,
      37,
      39,
      43,
      47,
      59,
      55,
      61,
      53,
      57,
      41,
      49,
      62,
      33,
      46,
      54,
      38,
      58,
      26,
      42,
      50,
      45,
      34,
      60,
      28,
      44,
      51,
      52,
      20,
      36,
      56,
      24,
      40,
      8,
      48,
      16,
      32,
      63
    ],
    "origin": 0,
    "seam": 55,
    "spine_path": [
      0,
      63,
      1,
      62,
      35,
      28,
      15,
      48,
      4,
      59,
      61,
      2,
      32,
      31,
      33,
      30,
      46,
      17,
      60,
      3,
      16,
      47,
      53,
      10,
      36,
      27,
      38,
      25,
      58,
      5,
      8,
      55
    ],
    "components": [
      {
        "origin_component": true,
        "vertices": [
          0,
          1,
          2,
          3,
          4,
          5,
          8,
          10,
          15,
          16,
          17,
          25,
          27,
          28,
          30,
          31,
          32,
          33,
          35,
          36,
          38,
          46,
          47,
          48,
          53,
          55,
          58,
          59,
          60,
          61,
          62,
          63
        ],
        "binary_vertices": [
          "000000",
          "000001",
          "000010",
          "000011",
          "000100",
          "000101",
          "001000",
          "001010",
          "001111",
          "010000",
          "010001",
          "011001",
          "011011",
          "011100",
          "011110",
          "011111",
          "100000",
          "100001",
          "100011",
          "100100",
          "100110",
          "101110",
          "101111",
          "110000",
          "110101",
          "110111",
          "111010",
          "111011",
          "111100",
          "111101",
          "111110",
          "111111"
        ],
        "tau_poles": [
          0,
          55
        ],
        "S_cycles": [
          [
            0,
            63,
            62,
            28,
            48,
            59,
            2,
            31,
            30,
            17,
            3,
            47,
            10,
            27,
            25,
            5,
            55,
            8,
            58,
            38,
            36,
            53,
            16,
            60,
            46,
            33,
            32,
            61,
            4,
            15,
            35,
            1
          ]
        ],
        "B_cycles": [
          [
            0,
            62,
            48,
            2,
            30,
            3,
            10,
            25,
            55,
            58,
            36,
            16,
            46,
            32,
            4,
            35
          ],
          [
            1,
            63,
            28,
            59,
            31,
            17,
            47,
            27,
            5,
            8,
            38,
            53,
            60,
            33,
            61,
            15
          ]
        ]
      },
      {
        "origin_component": false,
        "vertices": [
          6,
          7,
          9,
          11,
          12,
          13,
          14,
          18,
          19,
          20,
          21,
          22,
          23,
          24,
          26,
          29,
          34,
          37,
          39,
          40,
          41,
          42,
          43,
          44,
          45,
          49,
          50,
          51,
          52,
          54,
          56,
          57
        ],
        "binary_vertices": [
          "000110",
          "000111",
          "001001",
          "001011",
          "001100",
          "001101",
          "001110",
          "010010",
          "010011",
          "010100",
          "010101",
          "010110",
          "010111",
          "011000",
          "011010",
          "011101",
          "100010",
          "100101",
          "100111",
          "101000",
          "101001",
          "101010",
          "101011",
          "101100",
          "101101",
          "110001",
          "110010",
          "110011",
          "110100",
          "110110",
          "111000",
          "111001"
        ],
        "tau_poles": [],
        "S_cycles": [
          [
            6,
            23,
            37,
            14,
            19,
            18,
            29,
            9,
            7,
            39,
            22,
            21,
            13,
            12,
            11,
            43
          ],
          [
            20,
            52,
            51,
            50,
            42,
            41,
            24,
            56,
            54,
            34,
            45,
            44,
            49,
            26,
            40,
            57
          ]
        ],
        "B_cycles": [
          [
            6,
            37,
            19,
            29,
            7,
            22,
            13,
            11
          ],
          [
            9,
            39,
            21,
            12,
            43,
            23,
            14,
            18
          ],
          [
            20,
            51,
            42,
            24,
            54,
            45,
            49,
            40
          ],
          [
            26,
            57,
            52,
            50,
            41,
            56,
            34,
            44
          ]
        ]
      }
    ],
    "T_TC_agreement_states": []
  },
  "small_prism_graphs": [
    {
      "n": 3,
      "A": [
        0,
        6,
        3,
        5
      ],
      "Q": [
        1,
        7,
        2,
        4
      ],
      "rung_masks": [
        1,
        1,
        1,
        1
      ],
      "prism_edges": 12,
      "literal_binary_cube_edges_in_prism": 4,
      "abstract_gray_embedding_into_Qn": true,
      "gray_relabeling": {
        "0": 0,
        "1": 4,
        "6": 1,
        "7": 5,
        "3": 3,
        "2": 7,
        "5": 2,
        "4": 6
      },
      "missing_cube_edges_after_gray_relabeling": [],
      "single_bit_edges_in_T_union_TC": {
        "0": 4,
        "1": 0,
        "2": 2
      }
    },
    {
      "n": 4,
      "A": [
        0,
        14,
        7,
        5,
        11,
        12,
        9,
        13
      ],
      "Q": [
        1,
        15,
        2,
        6,
        3,
        4,
        10,
        8
      ],
      "rung_masks": [
        1,
        1,
        5,
        3,
        8,
        8,
        3,
        5
      ],
      "prism_edges": 24,
      "literal_binary_cube_edges_in_prism": 8,
      "abstract_gray_embedding_into_Qn": true,
      "gray_relabeling": {
        "0": 0,
        "1": 8,
        "14": 1,
        "15": 9,
        "7": 3,
        "2": 11,
        "5": 2,
        "6": 10,
        "11": 6,
        "3": 14,
        "12": 7,
        "4": 15,
        "9": 5,
        "10": 13,
        "13": 4,
        "8": 12
      },
      "missing_cube_edges_after_gray_relabeling": [
        [
          0,
          2
        ],
        [
          1,
          5
        ],
        [
          3,
          7
        ],
        [
          4,
          6
        ],
        [
          8,
          10
        ],
        [
          9,
          13
        ],
        [
          11,
          15
        ],
        [
          12,
          14
        ]
      ],
      "single_bit_edges_in_T_union_TC": {
        "0": 6,
        "1": 0,
        "2": 0,
        "3": 2
      }
    }
  ],
  "differential_quotient": {
    "A": [
      0,
      14,
      7,
      5,
      11,
      12,
      9,
      13
    ],
    "Q": [
      1,
      15,
      2,
      6,
      3,
      4,
      10,
      8
    ],
    "dA": [
      0,
      1,
      4,
      7,
      6,
      2,
      5,
      3
    ],
    "dQ": [
      1,
      0,
      3,
      5,
      2,
      6,
      7,
      4
    ],
    "source_prism_edges": 24,
    "image_distinct_edges": 10,
    "image_degrees": {
      "0": 2,
      "1": 2,
      "2": 2,
      "3": 3,
      "4": 3,
      "5": 3,
      "6": 2,
      "7": 3
    },
    "edge_image_multiplicities": {
      "(0, 1)": 4,
      "(0, 3)": 2,
      "(1, 4)": 2,
      "(2, 5)": 2,
      "(2, 6)": 4,
      "(3, 4)": 2,
      "(3, 5)": 2,
      "(4, 7)": 2,
      "(5, 7)": 2,
      "(6, 7)": 2
    },
    "non_Hamming_cube_edge_examples": [
      {
        "source_edge": [
          0,
          13
        ],
        "image": [
          0,
          3
        ],
        "xor_mask": 3
      },
      {
        "source_edge": [
          1,
          8
        ],
        "image": [
          1,
          4
        ],
        "xor_mask": 5
      },
      {
        "source_edge": [
          2,
          6
        ],
        "image": [
          3,
          5
        ],
        "xor_mask": 6
      },
      {
        "source_edge": [
          2,
          7
        ],
        "image": [
          3,
          4
        ],
        "xor_mask": 7
      },
      {
        "source_edge": [
          2,
          15
        ],
        "image": [
          3,
          0
        ],
        "xor_mask": 3
      }
    ],
    "is_cover_of_standard_simple_Q3": false
  },
  "projected_operator_label_checks": [
    {
      "label": "M3",
      "projected_edge": [
        0,
        1
      ],
      "actual_operator_image": 1,
      "matches": true
    },
    {
      "label": "B3_squared",
      "projected_edge": [
        4,
        7
      ],
      "actual_operator_image": 7,
      "matches": true
    },
    {
      "label": "P3C3",
      "projected_edge": [
        6,
        2
      ],
      "actual_operator_image": 4,
      "matches": false
    },
    {
      "label": "P3",
      "projected_edge": [
        5,
        3
      ],
      "actual_operator_image": 2,
      "matches": false
    }
  ],
  "seconds": 0.43398399400000187
}
```

## Supplementary checks

```json
{
  "T_crosses_spine_detached_boundary_edges": [
    [
      5,
      6
    ],
    [
      9,
      10
    ],
    [
      10,
      11
    ],
    [
      14,
      15
    ],
    [
      17,
      18
    ],
    [
      20,
      36
    ],
    [
      23,
      25
    ],
    [
      27,
      29
    ],
    [
      28,
      44
    ],
    [
      29,
      30
    ],
    [
      34,
      60
    ],
    [
      35,
      37
    ],
    [
      36,
      56
    ],
    [
      40,
      8
    ],
    [
      43,
      47
    ],
    [
      46,
      54
    ],
    [
      49,
      62
    ],
    [
      53,
      57
    ],
    [
      54,
      38
    ],
    [
      58,
      26
    ]
  ],
  "T_crossing_edge_count": 20,
  "T_still_single_64_cycle": true,
  "LEN8_S_odd_cycle_lengths": [
    27
  ],
  "LEN4_literal_single_bit_counts": {
    "0": 6,
    "1": 0,
    "2": 0,
    "3": 2
  }
}
```


## Findings and corrections

### LEN=6: exact breakup

The first detached component occurs at n=6 in this audit. The C/tau graph has a 32-vertex Origin-to-Seam path and one detached 32-vertex alternating cycle. The seam is 55=110111, not the complement pole 63=111111. The complement pole belongs to the spinal component, while the two tau-fixed vertices are 0 and 55.

S has cycle lengths 32,16,16. B=S^2 has cycle lengths 16,16,8,8,8,8. Thus half the 64 states belong to the spinal component and half to the detached component. All exact state lists and cycle orders are in the JSON above.

Detachment is relative to the chosen generated operations C and tau (and hence S and B). It is not detachment from T: the original T remains a single 64-cycle and crosses between these components. The supplementary edge list below makes that distinction explicit.

### What is a theorem, and what is a measured topology

PTP=T_inverse and PC=CP imply K=PC is an involution, T_C=K T_inverse K, and B=T_C T_inverse=(K T_inverse)^2. Hence S^2=B is an algebraic identity.

The two tau-fixed vertices force one alternating path connecting those endpoints when tau-self-loops are ignored in the path drawing. They do not force that path to contain all vertices. Additional alternating cycles are allowed and first appear at n=6 here.

For permutation matrices, Frobenius agreement equals #Fix(B)=#Fix(S^2). Therefore zero agreement requires S to have no cycles of length one or two. The supplied no-adjacent-PC argument rules out fixed points of S, but does not by itself rule out its two-cycles. Agreement was zero at every n=2,...,16; an all-width proof still needs that second exclusion or another valid argument.

The proposed global rung rule M=S_inverse on even S-steps and S on odd S-steps is valid on the even spinal orbit. It is not automatically a global rule on all later components. At n=8 there are odd S-cycles of length 27, so an alternating neighboring-S pairing cannot be defined on every such orbit. A broader matching would need an additional construction.

### Cube and quotient qualifications

At n=3, the B-plus-rung graph is abstractly Q3. At n=4 it is the octagonal prism with 16 vertices and 24 edges. An explicit Gray relabeling in the results embeds that prism as a spanning subgraph of Q4, leaving eight cube edges. Under the original word labels, only eight prism edges are literal single-bit cube edges. The relabeling is necessary for the hypercube-subgraph statement.

The differential d(x)=(x xor (x>>1))&7 has kernel {0,15}, is complement-invariant, and maps each of A4 and Q4 bijectively to eight three-bit labels. Those vertex facts pass.

It does not give a graph covering onto the standard simple Q3. The 24 prism edges have only ten distinct image edges, and image vertices 0,1,2,6 have degree two rather than three. Some image edges differ in multiple bits. For example 14->7 maps to 1->4, which is not a Hamming-cube edge. Retaining multiplicity gives a multigraph with parallel edges, not the simple cube claimed.

Two projected operator labels fail under the stated native definitions: P3 C3 sends 6 to 4, not 2; P3 sends 5 to 2, not 3. The four projected edges have the stated XOR differences, but that alone does not identify them with those global operators.

The actual single-bit edge counts in E(T4) union E(T_C4), with undirected duplicate edges removed, are {0:6,1:0,2:0,3:2}, not {0:6,1:3,2:2,3:1}. The rung-mask list 1,1,5,3,8,8,3,5 does pass.

### Ledger scope

- Square-root bridge factorization: exact algebra; RUNS independently n=2,...,16.
- Origin-to-Seam path plus detached loops: RUNS with exact components and cycle orders.
- First detachment at n=6: RUNS in the audited ladder.
- Frobenius zero through n=16: RUNS; supplied all-width proof argument incomplete.
- Q3/prism identities: RUNS as abstract graphs, with explicit coordinate relabeling.
- Differential map as complement quotient on vertices: RUNS.
- Differential map as a cover of the simple Q3 graph: DEAD END for this map; vertex surjectivity does not preserve the needed edges.
- Global adjacent-S rung rule at every width: not established; odd S-cycle obstruction appears at n=8.

This is a mathematical operator audit. No physical identification is inferred from the term internal loop or vortex.
