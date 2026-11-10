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

## Exact execution results

```json
{
  "scope": "New global rung construction for the original rings; exact mathematical finite-state audit, no physical interpretation. Compiling the map enumerates the finite field in this implementation.",
  "definition": "Pair each B-cycle A with C(A). Choose the least unhandled word a. Use q0=S_inverse(0) for the origin pair and q0=C(a) otherwise. Set M(B^j a)=B^j q0 in both directions.",
  "phase_convention_is_explicit_not_unique": true,
  "width_results": [
    {
      "n": 2,
      "N": 4,
      "all_state_matching_checks": true,
      "B_cycle_pair_lengths": {
        "2": 1
      },
      "prism_components": 1,
      "simple_graph_edges": 4,
      "graph_is_bipartite": true,
      "odd_prism_cycle_lengths": [],
      "C_paired_B_commuting_phase_choices": "2",
      "phase_choices_with_origin_rung_fixed": "1",
      "Frobenius_agreement": 0
    },
    {
      "n": 3,
      "N": 8,
      "all_state_matching_checks": true,
      "B_cycle_pair_lengths": {
        "4": 1
      },
      "prism_components": 1,
      "simple_graph_edges": 12,
      "graph_is_bipartite": true,
      "odd_prism_cycle_lengths": [],
      "C_paired_B_commuting_phase_choices": "4",
      "phase_choices_with_origin_rung_fixed": "1",
      "Frobenius_agreement": 0
    },
    {
      "n": 4,
      "N": 16,
      "all_state_matching_checks": true,
      "B_cycle_pair_lengths": {
        "8": 1
      },
      "prism_components": 1,
      "simple_graph_edges": 24,
      "graph_is_bipartite": true,
      "odd_prism_cycle_lengths": [],
      "C_paired_B_commuting_phase_choices": "8",
      "phase_choices_with_origin_rung_fixed": "1",
      "Frobenius_agreement": 0
    },
    {
      "n": 5,
      "N": 32,
      "all_state_matching_checks": true,
      "B_cycle_pair_lengths": {
        "16": 1
      },
      "prism_components": 1,
      "simple_graph_edges": 48,
      "graph_is_bipartite": true,
      "odd_prism_cycle_lengths": [],
      "C_paired_B_commuting_phase_choices": "16",
      "phase_choices_with_origin_rung_fixed": "1",
      "Frobenius_agreement": 0
    },
    {
      "n": 6,
      "N": 64,
      "all_state_matching_checks": true,
      "B_cycle_pair_lengths": {
        "16": 1,
        "8": 2
      },
      "prism_components": 3,
      "simple_graph_edges": 96,
      "graph_is_bipartite": true,
      "odd_prism_cycle_lengths": [],
      "C_paired_B_commuting_phase_choices": "1024",
      "phase_choices_with_origin_rung_fixed": "64",
      "Frobenius_agreement": 0
    },
    {
      "n": 7,
      "N": 128,
      "all_state_matching_checks": true,
      "B_cycle_pair_lengths": {
        "48": 1,
        "8": 2
      },
      "prism_components": 3,
      "simple_graph_edges": 192,
      "graph_is_bipartite": true,
      "odd_prism_cycle_lengths": [],
      "C_paired_B_commuting_phase_choices": "3072",
      "phase_choices_with_origin_rung_fixed": "64",
      "Frobenius_agreement": 0
    },
    {
      "n": 8,
      "N": 256,
      "all_state_matching_checks": true,
      "B_cycle_pair_lengths": {
        "85": 1,
        "8": 2,
        "27": 1
      },
      "prism_components": 4,
      "simple_graph_edges": 384,
      "graph_is_bipartite": false,
      "odd_prism_cycle_lengths": [
        27,
        85
      ],
      "C_paired_B_commuting_phase_choices": "146880",
      "phase_choices_with_origin_rung_fixed": "1728",
      "Frobenius_agreement": 0
    },
    {
      "n": 9,
      "N": 512,
      "all_state_matching_checks": true,
      "B_cycle_pair_lengths": {
        "233": 1,
        "8": 2,
        "7": 1
      },
      "prism_components": 4,
      "simple_graph_edges": 768,
      "graph_is_bipartite": false,
      "odd_prism_cycle_lengths": [
        7,
        233
      ],
      "C_paired_B_commuting_phase_choices": "104384",
      "phase_choices_with_origin_rung_fixed": "448",
      "Frobenius_agreement": 0
    },
    {
      "n": 10,
      "N": 1024,
      "all_state_matching_checks": true,
      "B_cycle_pair_lengths": {
        "468": 1,
        "8": 2,
        "14": 2
      },
      "prism_components": 5,
      "simple_graph_edges": 1536,
      "graph_is_bipartite": true,
      "odd_prism_cycle_lengths": [],
      "C_paired_B_commuting_phase_choices": "5870592",
      "phase_choices_with_origin_rung_fixed": "12544",
      "Frobenius_agreement": 0
    },
    {
      "n": 11,
      "N": 2048,
      "all_state_matching_checks": true,
      "B_cycle_pair_lengths": {
        "908": 1,
        "8": 4,
        "14": 2,
        "28": 2
      },
      "prism_components": 9,
      "simple_graph_edges": 3072,
      "graph_is_bipartite": true,
      "odd_prism_cycle_lengths": [],
      "C_paired_B_commuting_phase_choices": "571502231552",
      "phase_choices_with_origin_rung_fixed": "629407744",
      "Frobenius_agreement": 0
    },
    {
      "n": 12,
      "N": 4096,
      "all_state_matching_checks": true,
      "B_cycle_pair_lengths": {
        "2004": 1,
        "8": 2,
        "14": 2
      },
      "prism_components": 5,
      "simple_graph_edges": 6144,
      "graph_is_bipartite": true,
      "odd_prism_cycle_lengths": [],
      "C_paired_B_commuting_phase_choices": "25138176",
      "phase_choices_with_origin_rung_fixed": "12544",
      "Frobenius_agreement": 0
    },
    {
      "n": 13,
      "N": 8192,
      "all_state_matching_checks": true,
      "B_cycle_pair_lengths": {
        "3722": 1,
        "8": 2,
        "14": 2,
        "75": 1,
        "153": 1,
        "32": 2,
        "19": 2
      },
      "prism_components": 11,
      "simple_graph_edges": 12288,
      "graph_is_bipartite": false,
      "odd_prism_cycle_lengths": [
        19,
        19,
        75,
        153
      ],
      "C_paired_B_commuting_phase_choices": "198048823522099200",
      "phase_choices_with_origin_rung_fixed": "53210323353600",
      "Frobenius_agreement": 0
    },
    {
      "n": 14,
      "N": 16384,
      "all_state_matching_checks": true,
      "B_cycle_pair_lengths": {
        "796": 1,
        "855": 1,
        "8": 2,
        "1030": 2,
        "14": 2,
        "1028": 2,
        "903": 1,
        "429": 2,
        "197": 1,
        "423": 1
      },
      "prism_components": 15,
      "simple_graph_edges": 24576,
      "graph_is_bipartite": false,
      "odd_prism_cycle_lengths": [
        197,
        423,
        429,
        429,
        855,
        903
      ],
      "C_paired_B_commuting_phase_choices": "132551557387832447282672225427456000",
      "phase_choices_with_origin_rung_fixed": "166522057019890009149085710336000",
      "Frobenius_agreement": 0
    },
    {
      "n": 15,
      "N": 32768,
      "all_state_matching_checks": true,
      "B_cycle_pair_lengths": {
        "8483": 1,
        "855": 1,
        "8": 2,
        "1516": 2,
        "14": 2,
        "429": 2,
        "797": 1,
        "2013": 1,
        "90": 2,
        "61": 2
      },
      "prism_components": 16,
      "simple_graph_edges": 49152,
      "graph_is_bipartite": false,
      "odd_prism_cycle_lengths": [
        61,
        61,
        429,
        429,
        797,
        855,
        2013,
        8483
      ],
      "C_paired_B_commuting_phase_choices": "1860850138935214594815155859326976000",
      "phase_choices_with_origin_rung_fixed": "219362270297679428835925481472000",
      "Frobenius_agreement": 0
    },
    {
      "n": 16,
      "N": 65536,
      "all_state_matching_checks": true,
      "B_cycle_pair_lengths": {
        "30421": 1,
        "855": 1,
        "8": 2,
        "14": 2,
        "429": 2,
        "393": 1,
        "197": 1
      },
      "prism_components": 10,
      "simple_graph_edges": 98304,
      "graph_is_bipartite": false,
      "odd_prism_cycle_lengths": [
        197,
        393,
        429,
        429,
        855,
        30421
      ],
      "C_paired_B_commuting_phase_choices": "4648887183107718270720",
      "phase_choices_with_origin_rung_fixed": "152818355185816320",
      "Frobenius_agreement": 0
    }
  ],
  "state_checks": 131068,
  "first_nonbipartite_prism_width": 8,
  "examples": {
    "6": {
      "pairs": [
        {
          "seed": 0,
          "rung_seed": 1,
          "cycle_length": 16,
          "origin_pair": true,
          "anchor_rule": "S_inverse(0)",
          "A": [
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
          "Q": [
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
        },
        {
          "seed": 6,
          "rung_seed": 57,
          "cycle_length": 8,
          "origin_pair": false,
          "anchor_rule": "C(seed)",
          "A": [
            6,
            37,
            19,
            29,
            7,
            22,
            13,
            11
          ],
          "Q": [
            57,
            52,
            50,
            41,
            56,
            34,
            44,
            26
          ]
        },
        {
          "seed": 9,
          "rung_seed": 54,
          "cycle_length": 8,
          "origin_pair": false,
          "anchor_rule": "C(seed)",
          "A": [
            9,
            39,
            21,
            12,
            43,
            23,
            14,
            18
          ],
          "Q": [
            54,
            45,
            49,
            40,
            20,
            51,
            42,
            24
          ]
        }
      ],
      "rungs": [
        [
          0,
          1
        ],
        [
          2,
          59
        ],
        [
          3,
          17
        ],
        [
          4,
          61
        ],
        [
          5,
          55
        ],
        [
          6,
          57
        ],
        [
          7,
          56
        ],
        [
          8,
          58
        ],
        [
          9,
          54
        ],
        [
          10,
          47
        ],
        [
          11,
          26
        ],
        [
          12,
          40
        ],
        [
          13,
          44
        ],
        [
          14,
          42
        ],
        [
          15,
          35
        ],
        [
          16,
          53
        ],
        [
          18,
          24
        ],
        [
          19,
          50
        ],
        [
          20,
          43
        ],
        [
          21,
          49
        ],
        [
          22,
          34
        ],
        [
          23,
          51
        ],
        [
          25,
          27
        ],
        [
          28,
          48
        ],
        [
          29,
          41
        ],
        [
          30,
          31
        ],
        [
          32,
          33
        ],
        [
          36,
          38
        ],
        [
          37,
          52
        ],
        [
          39,
          45
        ],
        [
          46,
          60
        ],
        [
          62,
          63
        ]
      ],
      "M_table": [
        1,
        0,
        59,
        17,
        61,
        55,
        57,
        56,
        58,
        54,
        47,
        26,
        40,
        44,
        42,
        35,
        53,
        3,
        24,
        50,
        43,
        49,
        34,
        51,
        18,
        27,
        11,
        25,
        48,
        41,
        31,
        30,
        33,
        32,
        22,
        15,
        38,
        52,
        36,
        45,
        12,
        29,
        14,
        20,
        13,
        39,
        60,
        10,
        28,
        21,
        19,
        23,
        37,
        16,
        9,
        5,
        7,
        6,
        8,
        2,
        46,
        4,
        63,
        62
      ]
    },
    "8": {
      "pairs": [
        {
          "seed": 0,
          "rung_seed": 1,
          "cycle_length": 85,
          "origin_pair": true,
          "anchor_rule": "S_inverse(0)",
          "A": [
            0,
            254,
            192,
            8,
            135,
            69,
            60,
            187,
            119,
            13,
            44,
            171,
            103,
            89,
            215,
            47,
            110,
            29,
            2,
            126,
            3,
            34,
            97,
            223,
            55,
            14,
            141,
            75,
            42,
            105,
            24,
            151,
            85,
            51,
            10,
            137,
            71,
            38,
            90,
            57,
            183,
            115,
            9,
            16,
            142,
            205,
            236,
            154,
            164,
            98,
            225,
            144,
            76,
            202,
            169,
            232,
            230,
            148,
            82,
            209,
            176,
            108,
            235,
            250,
            132,
            64,
            190,
            128,
            56,
            182,
            116,
            243,
            234,
            153,
            229,
            212,
            48,
            174,
            237,
            220,
            194,
            161,
            224,
            4,
            131
          ],
          "Q": [
            1,
            255,
            124,
            251,
            31,
            94,
            61,
            35,
            18,
            81,
            207,
            43,
            26,
            102,
            21,
            12,
            139,
            73,
            199,
            127,
            65,
            191,
            123,
            5,
            20,
            147,
            79,
            46,
            173,
            107,
            25,
            23,
            86,
            53,
            179,
            111,
            30,
            157,
            91,
            101,
            19,
            50,
            113,
            239,
            246,
            140,
            72,
            198,
            165,
            217,
            184,
            118,
            245,
            204,
            170,
            104,
            231,
            150,
            213,
            180,
            114,
            241,
            200,
            32,
            158,
            221,
            252,
            129,
            253,
            226,
            145,
            208,
            40,
            166,
            152,
            84,
            211,
            242,
            136,
            68,
            195,
            186,
            120,
            247,
            63
          ]
        },
        {
          "seed": 6,
          "rung_seed": 249,
          "cycle_length": 8,
          "origin_pair": false,
          "anchor_rule": "C(seed)",
          "A": [
            6,
            133,
            67,
            125,
            7,
            70,
            37,
            59
          ],
          "Q": [
            249,
            196,
            218,
            185,
            248,
            130,
            188,
            122
          ]
        },
        {
          "seed": 11,
          "rung_seed": 244,
          "cycle_length": 27,
          "origin_pair": false,
          "anchor_rule": "C(seed)",
          "A": [
            11,
            74,
            41,
            167,
            99,
            17,
            143,
            77,
            203,
            39,
            22,
            149,
            83,
            49,
            175,
            109,
            27,
            58,
            121,
            15,
            78,
            45,
            28,
            155,
            87,
            54,
            117
          ],
          "Q": [
            244,
            138,
            201,
            168,
            100,
            227,
            210,
            177,
            240,
            134,
            197,
            228,
            146,
            80,
            206,
            172,
            106,
            233,
            216,
            52,
            178,
            112,
            238,
            156,
            88,
            214,
            181
          ]
        },
        {
          "seed": 33,
          "rung_seed": 222,
          "cycle_length": 8,
          "origin_pair": false,
          "anchor_rule": "C(seed)",
          "A": [
            33,
            159,
            93,
            36,
            163,
            95,
            62,
            66
          ],
          "Q": [
            222,
            189,
            193,
            160,
            92,
            219,
            162,
            96
          ]
        }
      ],
      "rungs": [
        [
          0,
          1
        ],
        [
          2,
          199
        ],
        [
          3,
          65
        ],
        [
          4,
          247
        ],
        [
          5,
          223
        ],
        [
          6,
          249
        ],
        [
          7,
          248
        ],
        [
          8,
          251
        ],
        [
          9,
          113
        ],
        [
          10,
          179
        ],
        [
          11,
          244
        ],
        [
          12,
          47
        ],
        [
          13,
          81
        ],
        [
          14,
          147
        ],
        [
          15,
          52
        ],
        [
          16,
          239
        ],
        [
          17,
          227
        ],
        [
          18,
          119
        ],
        [
          19,
          183
        ],
        [
          20,
          55
        ],
        [
          21,
          215
        ],
        [
          22,
          197
        ],
        [
          23,
          151
        ],
        [
          24,
          25
        ],
        [
          26,
          103
        ],
        [
          27,
          106
        ],
        [
          28,
          238
        ],
        [
          29,
          73
        ],
        [
          30,
          71
        ],
        [
          31,
          135
        ],
        [
          32,
          250
        ],
        [
          33,
          222
        ],
        [
          34,
          191
        ],
        [
          35,
          187
        ],
        [
          36,
          160
        ],
        [
          37,
          188
        ],
        [
          38,
          157
        ],
        [
          39,
          134
        ],
        [
          40,
          234
        ],
        [
          41,
          201
        ],
        [
          42,
          173
        ],
        [
          43,
          171
        ],
        [
          44,
          207
        ],
        [
          45,
          112
        ],
        [
          46,
          75
        ],
        [
          48,
          211
        ],
        [
          49,
          80
        ],
        [
          50,
          115
        ],
        [
          51,
          53
        ],
        [
          54,
          214
        ],
        [
          56,
          253
        ],
        [
          57,
          101
        ],
        [
          58,
          233
        ],
        [
          59,
          122
        ],
        [
          60,
          61
        ],
        [
          62,
          162
        ],
        [
          63,
          131
        ],
        [
          64,
          221
        ],
        [
          66,
          96
        ],
        [
          67,
          218
        ],
        [
          68,
          220
        ],
        [
          69,
          94
        ],
        [
          70,
          130
        ],
        [
          72,
          236
        ],
        [
          74,
          138
        ],
        [
          76,
          245
        ],
        [
          77,
          177
        ],
        [
          78,
          178
        ],
        [
          79,
          141
        ],
        [
          82,
          213
        ],
        [
          83,
          146
        ],
        [
          84,
          212
        ],
        [
          85,
          86
        ],
        [
          87,
          88
        ],
        [
          89,
          102
        ],
        [
          90,
          91
        ],
        [
          92,
          163
        ],
        [
          93,
          193
        ],
        [
          95,
          219
        ],
        [
          97,
          123
        ],
        [
          98,
          217
        ],
        [
          99,
          100
        ],
        [
          104,
          232
        ],
        [
          105,
          107
        ],
        [
          108,
          241
        ],
        [
          109,
          172
        ],
        [
          110,
          139
        ],
        [
          111,
          137
        ],
        [
          114,
          176
        ],
        [
          116,
          145
        ],
        [
          117,
          181
        ],
        [
          118,
          144
        ],
        [
          120,
          224
        ],
        [
          121,
          216
        ],
        [
          124,
          192
        ],
        [
          125,
          185
        ],
        [
          126,
          127
        ],
        [
          128,
          129
        ],
        [
          132,
          158
        ],
        [
          133,
          196
        ],
        [
          136,
          237
        ],
        [
          140,
          205
        ],
        [
          142,
          246
        ],
        [
          143,
          210
        ],
        [
          148,
          150
        ],
        [
          149,
          228
        ],
        [
          152,
          229
        ],
        [
          153,
          166
        ],
        [
          154,
          198
        ],
        [
          155,
          156
        ],
        [
          159,
          189
        ],
        [
          161,
          186
        ],
        [
          164,
          165
        ],
        [
          167,
          168
        ],
        [
          169,
          170
        ],
        [
          174,
          242
        ],
        [
          175,
          206
        ],
        [
          180,
          209
        ],
        [
          182,
          226
        ],
        [
          184,
          225
        ],
        [
          190,
          252
        ],
        [
          194,
          195
        ],
        [
          200,
          235
        ],
        [
          202,
          204
        ],
        [
          203,
          240
        ],
        [
          208,
          243
        ],
        [
          230,
          231
        ],
        [
          254,
          255
        ]
      ],
      "M_table": [
        1,
        0,
        199,
        65,
        247,
        223,
        249,
        248,
        251,
        113,
        179,
        244,
        47,
        81,
        147,
        52,
        239,
        227,
        119,
        183,
        55,
        215,
        197,
        151,
        25,
        24,
        103,
        106,
        238,
        73,
        71,
        135,
        250,
        222,
        191,
        187,
        160,
        188,
        157,
        134,
        234,
        201,
        173,
        171,
        207,
        112,
        75,
        12,
        211,
        80,
        115,
        53,
        15,
        51,
        214,
        20,
        253,
        101,
        233,
        122,
        61,
        60,
        162,
        131,
        221,
        3,
        96,
        218,
        220,
        94,
        130,
        30,
        236,
        29,
        138,
        46,
        245,
        177,
        178,
        141,
        49,
        13,
        213,
        146,
        212,
        86,
        85,
        88,
        87,
        102,
        91,
        90,
        163,
        193,
        69,
        219,
        66,
        123,
        217,
        100,
        99,
        57,
        89,
        26,
        232,
        107,
        27,
        105,
        241,
        172,
        139,
        137,
        45,
        9,
        176,
        50,
        145,
        181,
        144,
        18,
        224,
        216,
        59,
        97,
        192,
        185,
        127,
        126,
        129,
        128,
        70,
        63,
        158,
        196,
        39,
        31,
        237,
        111,
        74,
        110,
        205,
        79,
        246,
        210,
        118,
        116,
        83,
        14,
        150,
        228,
        148,
        23,
        229,
        166,
        198,
        156,
        155,
        38,
        132,
        189,
        36,
        186,
        62,
        92,
        165,
        164,
        153,
        168,
        167,
        170,
        169,
        43,
        109,
        42,
        242,
        206,
        114,
        77,
        78,
        10,
        209,
        117,
        226,
        19,
        225,
        125,
        161,
        35,
        37,
        159,
        252,
        34,
        124,
        93,
        195,
        194,
        133,
        22,
        154,
        2,
        235,
        41,
        204,
        240,
        202,
        140,
        175,
        44,
        243,
        180,
        143,
        48,
        84,
        82,
        54,
        21,
        121,
        98,
        67,
        95,
        68,
        64,
        33,
        5,
        120,
        184,
        182,
        17,
        149,
        152,
        231,
        230,
        104,
        58,
        40,
        200,
        72,
        136,
        28,
        16,
        203,
        108,
        174,
        208,
        11,
        76,
        142,
        4,
        7,
        6,
        32,
        8,
        190,
        56,
        255,
        254
      ],
      "odd_S_cycle_lengths": [
        27,
        27
      ],
      "global_rungs_leave_each_odd_S_orbit": true
    }
  },
  "seconds": 0.8110856519999743
}
```

## Supplementary phase-family check

```json
{
  "scope": "C-paired phase-family enumeration at LEN=6, not all possible commuting matchings.",
  "distinct_matching_tables": 1024,
  "matching_tables_with_original_origin_rung_fixed": 64,
  "all_involution_B_commutation_C_commutation_checks": true
}
```


## Constructive proof of a global rung

Let C be the fixed-point-free complement involution and tau the index reflection with its two fixed endpoints. Let S=C tau and B=S^2. The relation C B C=B^(-1) sends any B-cycle to a B-cycle of the same length, with reversed orientation.

The missing condition is that the image cycle is distinct. This follows from the colored C/tau graph:

1. Ignore tau self-loops when drawing components, but retain them in the operators. There is one alternating path connecting the two tau-fixed vertices, plus alternating even cycles. C is a perfect matching, so the path has an even number of vertices.
2. On the path, S is one even cycle. Choose the tau-fixed origin a. Since S(a)=C(a), C sends S-index k to 1-k. Therefore C swaps the two B=S^2 parity cycles.
3. On an alternating closed component, S preserves each of the two alternating vertex classes, while C swaps those classes. Every B-cycle stays inside one class, so its C-image is distinct.

Thus every B-cycle has a distinct, equally long C-partner.

Choose a seed a in one cycle A. Choose q0 in C(A), fix its phase, and define

M(B^j a)=B^j q0,
M(B^j q0)=B^j a.

Equal cycle lengths make the definition consistent. The cycles are disjoint, so M is fixed-point-free. Advancing j proves M B=B M and M^2=I. Writing q0=B^r C(a) also proves M C=C M. This construction works for odd cycle lengths as well: it pairs two distinct cycles, rather than trying to alternate pairs around an odd cycle.

## Convention used in the execution

For each unprocessed C-pair, choose its least word a. In the origin pair use q0=S_inverse(0), preserving the previous LEN=3/4 rung. For detached pairs use q0=C(a). These are explicit anchors, not a claim that the algebra singles out one global matching.

The new rule agrees exactly with the earlier matching on all states at LEN=3 and LEN=4. It remains x xor 001 at LEN=3, and retains the masks 1,1,5,3,8,8,3,5 at LEN=4.

## Exact LEN=6 result

Global B-plus-M graph components:

- One C16 square K2 prism, 32 vertices and 48 edges, on the spinal component.
- Two C8 square K2 prisms, 16 vertices and 24 edges each, inside the detached component.

Total: 64 vertices, 96 edges, every vertex degree three. All states have one rung and exact return. Example detached anchors are 6<->57 and 9<->54; every other rung follows by applying the same B power to both ends. Full cycle and rung lists are in the result section above.

## Exact LEN=8 result

B-plus-M components are C85 square K2, C27 square K2 and two C8 square K2 prisms: 170+54+16+16=256 vertices, 384 edges. The two odd S-orbits of length 27 are matched across to each other, so the former odd-cycle pairing obstruction is repaired.

This graph is not bipartite because B already contains odd cycles of length 85 and 27. Therefore it cannot be an edge-preserving subgraph of any hypercube under any relabeling. The earlier cube/prism coincidence at LEN=3 and the Gray embedding at LEN=4 do not extend to an all-width hypercube claim. LEN=8 here means an eight-bit word field of 256 states, not the eight-slot serialized R2 orbit.

## How many anchors

Within the fixed C-pairing, a pair of B-cycles of length m admits m phase-preserving rung alignments. Therefore this family has product(m) matchings. At LEN=6 this is 16*8*8=1024. Pinning the original origin rung leaves 8*8=64 detached alignments. All 1024 tables were additionally enumerated and checked below. This does not count matchings using other cycle pairings.

The selected code fixes these phases deterministically before runtime. It does not select them using payload values.

## What the audit establishes

All 131,068 states across LEN=2,...,16 passed M^2=I, M(x)!=x, M B=B M and M C=C M. Each component had the expected prism edges. LEN=2 is the simple-graph degenerate case with degree two. LEN>=3 had degree three and 3N/2 edges. The first odd-cycle/nonbipartite case in this audited ladder was LEN=8.

The implementation constructs tables by enumerating the finite state field once; subsequent M queries follow the stored map. No claim that compilation cost vanishes or that this is a physical matter model is made. The earlier differential map to three-bit labels remains a vertex quotient, not a repaired covering of the simple Q3 graph.

## Remaining orthogonality hole

For the original ring, <T,T_C>_F=#Fix(B)=#Fix(S^2). On a detached alternating component with 2m vertices, S has two m-cycles. Fixed points of B can therefore occur only for detached components with 2 or 4 vertices (or a two-vertex path, which the original n>=2 origin/seam geometry excludes). The all-width orthogonality proof is now a local exclusion problem: prove that those tiny detached alternating components cannot occur in the original representative order. Zero agreement still passed through LEN=16, but is not promoted to a proof merely from that finite run.

## Ledger update

- Global C-paired rung existence: constructive proof under the stated involution/graph assumptions; RUNS at every state through LEN=16.
- Preservation of earlier LEN=3/4 rungs: RUNS.
- Handling detached odd S-orbits: RUNS at LEN=8 and all larger audited widths.
- Uniqueness of a global rung without phase anchors: not claimed; phase choices are explicit.
- Global hypercube interpretation: fails once the fixed B graph contains odd cycles; first audited instance LEN=8.
- All-width Frobenius orthogonality: finite RUNS retained; tiny-cycle exclusion remains OPEN.

The source-block checksum still matches the pre-run record. Results and proof are appended to the same Markdown entry; the entire evolving document is not described as having an unchanged checksum.
