# NEXUS §189 — The registration interface, proved underdetermined
**Technical execution audit · October 29, 2026 · v02**

## Finding
The bacterial translation mechanism supplies an observable **one-codon progression**, but it does not supply the missing equation mapping that progression to the native-ring read address or to a distant structural partner. This audit proves the phase ambiguity constructively, then tests one fixed codon-based readout without fitting to solved creases. It fails the necessary phase-shift control.

## Inputs and provenance
- Input: `NEXUS_Fold_Compiler_Notebook (2).zip`, the `ecoli_chains.json` records bundled inside it; no external downloads or force-field fitting.
- SHA-256 of the extracted chain-data JSON: `f5266a447a4342955936966ff46df15823da5c55508540d78f316bf3f4d2e145`.
- 160 chain records; 19,329 independent resolved-residue-to-gene-index/identity agreements; 115 adjacency gaps in resolved-to-gene mapping.
- Observed targets: **143 antiparallel hairpins**, same coordinate-derived classifier as §188, 49 even-S and 94 odd-S. Native chain coordinates are accessed only after the prediction seal is written.
- Annotation: these tests are **retrospective against a previously discussed dataset**. Program-order sealing prevents within-run target leakage, but it is not an independent preregistration.

## 1. What physically advances
Bacterial initiation selects the start codon and reading frame. EF-G-assisted ribosomal translocation advances tRNAs and mRNA by one codon per elongation cycle, using GTP hydrolysis. This is a genuine physical clock for *residue index*, not evidence of one step on a native binary ring. The actual elongation time varies; a codon count is not a calibrated biochemical stopwatch.
References: [Belardinelli et al., 2016](https://pmc.ncbi.nlm.nih.gov/articles/PMC5207377/); [Milón & Rodnina, bacterial initiation](https://pmc.ncbi.nlm.nih.gov/articles/PMC4611024/).

## 2. Explicit non-identifiability of reader phase
Let `B` be a closed binary serialization of the native ring of length `M`. For any phase φ, a reader may sample `bφ(t)=B[(t+φ) mod M]`. Its window obeys the exact shift/carry identity `v_(t+1)=2v_t−(2^M−1)bφ(t)` for **every** φ. No stated native-ring identity or codon-progress equation contains φ. Thus φ is a free parameter of the interface, not determined by the provided rules.

The execution printed an explicit counterexample for the same 24-step input/clock:

```text
phase=0: [7, 10, 14, 17, 19, 21]
phase=1: [6, 9, 13, 16, 18, 20]
```

Both schedules obey the circular carry equation for the same R4 serialization; their crease predictions disagree. The protein input is unchanged. Even if a literal phase-0 convention is selected, the **molecular meaning** of that convention has not been derived.

## 3. The fixed codon-to-R6 *conditional* mapping
Unlike the previous chain-length-based serialized ring test, this experiment does not consume consecutive bits from an abstract ring traversal. A real input codon is interpreted through the already published two-bit alphabet `A=00, G=01, C=10, T=11`; it is a six-bit R6 word. Its **native address rank** is computed exactly, and the address hemisphere (`rank ≥ 32`) supplies a conditional one-bit readout. An adjacent `0→1` across consecutive true full-gene codons proposes a boundary between corresponding resolved residues.

This construction fixes an **encoding convention**, not a physical sensor. It is a testable alternative; there is currently no demonstrated biochemical event that reads the ring rank. Inversion of the hemisphere is another admissible representation with different structural results. Neither version was optimized.

- Prediction-manifest SHA-256: `cf98cda4f2ba62caef334ab33c4dd9892b02023d78dbaaec081cc2455e51b3e0`.
- Event proposals: **4,669** using the primary address hemisphere; **4,650** with the opposite hemisphere.

| Tolerance at crease centre | Codon→R6 candidate | Opposite hemisphere | Equal-count null mean | Phase-shift null mean | Synonymous shuffle mean |
|:--|--:|--:|--:|--:|--:|
| Exact S | 23/143 | 15/143 | 22.88 | 22.62 | 18.28 |
| ≤1 residue | 65/143 | 78/143 | 74.88 | 85.99 | 69.79 |
| ≤2 residues | 114/143 | 117/143 | 104.69 | 120.37 | 112.35 |

### Phase-shift and matched-count controls (3,000 each)
| Metric | Phase null 95% interval | P(null ≥ observed) | Equal-count 95% interval | P(null ≥ observed) |
|:--|:--|--:|:--|--:|
| Exact S | 15–31 | 0.5078 | 15–31 | 0.5425 |
| ≤1 residue | 75–97 | 1.0000 | 64–86 | 0.9620 |
| ≤2 residues | 112–129 | 0.9364 | 94–115 | 0.0467 |

The exact-match outcome **23/143** matches the phase and count controls; `P(null ≥ observed)` is 0.5078 and 0.5425 respectively. The `≤1 residue` outcome is *worse* than the phase null. The `≤2 residue` count superficially exceeds the equal-count null but not the phase null. The candidate is too dense for broad-tolerance match rates to establish precise crease prediction.

### Synonymous-codon control
A thousand independently shuffled sets of codons, with each gene retaining exactly its amino-acid sequence and its codon multiset per amino-acid class, yield an exact-match mean of 18.28, compared with 23 observed (one-sided unadjusted p≈0.041). This *one* exploratory raw comparison does not overcome the null phase result, the pre-existing hypothesis search, multiple tolerances, or the lack of a physical link. **No causal codon-to-crease claim is supported**.

## 4. Even-S creases: the frame does not determine the centre type
If a proposed crease is **between adjacent residues** e=i−1 and s=i, then `S=e+s=2i−1` is odd. A **residue-centred** reflection has `S=2c` even and passes through the diagonal cell `(c,c)` in the abstract pair square. These are both legal geometries of a reflection, not two experimentally established turn types. A diagonal contact `(c,c)` does **not** imply a physical backbone N_c−O_c hydrogen bond. The present boundary-only reader has exactly **0/49** even-S creases accessible by construction. The missing centre-type operator cannot be inferred from the ring reflection identity.

## 5. Distant partner non-identifiability
For a known local mirror sum S, a line `j=S−i` gives a potential partner conditional on choosing i. But S itself requires placing the ends e and s. Without a forward nucleation/contact mechanism, multiple distinct pairings satisfy every ring relation: on a 40-residue index set, `S=30` admits 14 distinct separated pairs `(i,30−i)` with `j−i>2`. Among them `(0,30)`, `(1,29)`, `(2,28)`, etc. They are combinatorially legal, **not** asserted to be physically stable folds. This directly shows that addressing is not partner selection.

## 6. Ledger
| Status | Exact scope |
|:--|:--|
| **STANDS** | Native-ring facing; circular carry update at arbitrary phase; proof of underdetermination of unconstrained phase; adjacent-residue boundary implies odd S. |
| **RUNS** | 160/160 chain records, 19,329 residue/codon-index agreements, 143 target hairpins, frozen conditional codon→R6 hypothesis and three null ensembles. |
| **DEAD END** | Claim that raw zero-phase serialized ring transitions or codon hemisphere transitions alone predict crease positions. |
| **OPEN** | Physical measurement realizing codon→ring address/hemisphere readout, registration and clock phase, residue-centred parity selection, local folding dynamics, distant-partner REACH. |

## 7. Execution trace — complete console output
```text
INPUT  | 160 chains; 19329 PDB-index/gene-sequence residue agreements; codon arrays match full gene length
INPUT  | chain-data SHA256: f5266a447a4342955936966ff46df15823da5c55508540d78f316bf3f4d2e145
RING   | R6 native facing verified for 64 words; ATG word=13 under published 2-bit encoding
PROOF  | identical 24-step input/clock; legal phase0 breaks=[7, 10, 14, 17, 19, 21] phase1 breaks=[6, 9, 13, 16, 18, 20]
PROOF  | identical 32-step input/clock; legal phase0 breaks=[7, 10, 14, 17, 19, 21, 25, 31] phase1 breaks=[6, 9, 13, 16, 18, 20, 24, 30]
PROOF  | circular end-around carry holds at all 64 positions at each of four phases; ring alone cannot select a phase
SEAL   | prediction SHA256 cf98cda4f2ba62caef334ab33c4dd9892b02023d78dbaaec081cc2455e51b3e0
SEAL   | per-chain conditional predictions written BEFORE accessing coordinate arrays
SEAL   | codon-address 0->1 events: 4669 | inverse-address events: 4650
TARGET | 160 chains, 143 hairpins, 49 even S and 94 odd S; identical §188 extraction
LAND   | R6 conditional codon-address hemisphere 0->1: {0: 23, 1: 65, 2: 114}
LAND   | inverse hemisphere orientation 0->1: {0: 15, 1: 78, 2: 117}
LAND   | even-S exact 0 (algebraically forbidden by boundary-only rule)
NULL   | equal_count          tol=0 observed= 23 mean= 22.88 95%=[15, 31] P(null>=obs)=0.5425
NULL   | equal_count          tol=1 observed= 65 mean= 74.88 95%=[64, 86] P(null>=obs)=0.9620
NULL   | equal_count          tol=2 observed=114 mean=104.69 95%=[94,115] P(null>=obs)=0.0467
NULL   | random_phase         tol=0 observed= 23 mean= 22.62 95%=[15, 31] P(null>=obs)=0.5078
NULL   | random_phase         tol=1 observed= 65 mean= 85.99 95%=[75, 97] P(null>=obs)=1.0000
NULL   | random_phase         tol=2 observed=114 mean=120.37 95%=[112,129] P(null>=obs)=0.9364
NULL   | synonymous_shuffle   tol=0 observed= 23 mean= 18.28 95%=[14, 23] P(null>=obs)=0.0410
NULL   | synonymous_shuffle   tol=1 observed= 65 mean= 69.79 95%=[62, 77] P(null>=obs)=0.9161
NULL   | synonymous_shuffle   tol=2 observed=114 mean=112.35 95%=[106,119] P(null>=obs)=0.3636
TIME   | three control ensembles 25.26 seconds
REACH  | same 40-residue prefix, local sum S=30 admits 14 distinct valid separated pairs; sample [(0, 30), (1, 29), (2, 28), (3, 27), (4, 26)] ; no partner selector follows from S
INDEX  | nonconsecutive full-gene indices among adjacent resolved residues: 115
LEDGER | STANDS: ring identities, phase invariance of carry, boundary odd-S algebra
LEDGER | RUNS: codon-word conditional candidate, 143 observed creases and three controls
LEDGER | DEAD END: an unregistered ring stream pretending to predict creases
LEDGER | OPEN: biochemical readout, even-S centres, distant partner REACH
FILES  | NEXUS_Registration_v02_Prediction_Seal.json NEXUS_Registration_v02_Results.json
```

The companion `NEXUS_Registration_v02_Results.json` records **all 160 chains**, all candidate `S` values, each observed hairpin and its matching status. The companion SHA-256 manifest contains the pre-target predictions.

## 8. Prompt for the following round
> Continue NEXUS §190 from the §189 registration-identifiability audit.
> 
> The physical bacterial elongation clock advances one codon per translocation, and initiation establishes the triplet frame. However, native-ring facing and end-around-carry identities do not specify the molecular interface linking codons to a ring address, hemisphere, phase or reflective crease.
> 
> The sealed, phase-free conditional candidate used the published A=00, G=01, C=10, T=11 encoding and native R6 address rank for each codon. Its 0→1 boundary events match 23/143 observed hairpins exactly, against 22.62 random-ring-phase and 22.88 matched-count expected. Within one residue it matches 65/143 against 85.99 under phase controls. All 49 even-S creases are structurally unreachable by the adjacent-boundary-only rule. A fixed reflection sum still does not determine which distant partner is reached.
> 
> Do not fit phase, crease sums, torsions, energy coefficients, or partner addresses to solved structures. Before doing another landing, identify an independently measurable molecular event that could distinguish the native-R6 hemisphere state from its complement and explain how a local run physically closes or persists. Treat native-ring identities as mathematical and the molecular interface as OPEN until experimentally supported.
> 
> Test distinguishability using a pair of synonymous codon variants and a pair of alternative partner registers that preserve the proposed input but differ in the outcome; work out what additional observable (time-resolved translation, nascent-chain conformation, solvent or contact state) could resolve them without target leakage. If possible devise a preregistered experiment with a prospective observable and matched controls; if not, prove non-identifiability and stop rather than adding more arbitrary rules.
> 
> Use the supplied NEXUS ZIP and the §189 code and results, produce one runnable Jupyter cell, all raw outputs, STANDS / RUNS / OPEN / DEAD END, and the next exact prompt.

## Appendix — Complete executable single-cell source
Copy the entire fenced code into **one Jupyter cell**; place `NEXUS_Fold_Compiler_Notebook (2).zip` beside the notebook. Dependencies: Python 3 and NumPy. Output: a sealed prediction JSON plus full results JSON. No other files, web access or reference structures are needed.

```python
"""NEXUS §189: reader-registration identifiability and conditional codon-address test.

Single-cell Jupyter compatible. Requires NumPy, standard library and the shipped
'NEXUS_Fold_Compiler_Notebook (2).zip'. No network, physical energy, fitted
thresholds, or structural targets enter the prediction stage.

This is a conditional test of codon-as-R6 input, NOT a derivation that real
ribosomes advance through native-ring addresses. The registration gap remains OPEN.
"""
from pathlib import Path
import math, json, zipfile, hashlib, collections, random, time, sys
import numpy as np

VERSION='NEXUS-REGISTRATION-IDENTIFIABILITY-2.0'
SEED=1892026
TRIALS=3000
SYNONYMOUS_TRIALS=1000
ZIPNAME='NEXUS_Fold_Compiler_Notebook (2).zip'
if '__file__' in globals():
    OUT=Path(__file__).resolve().parent
else:
    OUT=Path.cwd()
files=[OUT/ZIPNAME,Path.cwd()/ZIPNAME,Path('/mnt/data')/ZIPNAME]
ZIP=next((x for x in files if x.is_file()),None)
if ZIP is None: raise FileNotFoundError(f'Place {ZIPNAME} in the same folder as the notebook')
OUTPUT=OUT

# Ring operations. These are mathematical definitions, not molecular dynamics.
def reverse(x,w):return int(format(x,f'0{w}b')[::-1],2)
def partner(x,w):
    j=reverse(x,w)
    return j if j!=x else x^((1<<w)-1)
def native_ring(w):
    n=1<<w
    reps=[x for x in range(n) if x<partner(x,w)]
    m=reps[-1]
    r=reps[:-1]+[partner(m,w),m]+[partner(x,w) for x in reps[-2::-1]]
    assert sorted(r)==list(range(n))
    assert all(r[n-1-a]==partner(r[a],w) for a in range(n))
    return r

with zipfile.ZipFile(ZIP) as z:
    DATA=json.loads(z.read('NEXUS_Fold_Compiler_Notebook/data/ecoli_chains.json'))
    input_digest=hashlib.sha256(z.read('NEXUS_Fold_Compiler_Notebook/data/ecoli_chains.json')).hexdigest()
assert len(DATA)==160
assert all(len(d['codons'])==len(d['uniprot_sequence']) for d in DATA)
residue_checks=0
for d in DATA:
    for r in d['residues']:
        idx=r[0]
        assert isinstance(idx,int) and 0<=idx<len(d['codons'])
        assert d['uniprot_sequence'][idx]==r[1]
        residue_checks+=1
assert all(x==13 for d in DATA if d['uniprot_sequence'].startswith('M') for x in d['codons'][:1] if x==13) # sanity only
print('INPUT  |',len(DATA),'chains;',residue_checks,'PDB-index/gene-sequence residue agreements; codon arrays match full gene length')
print('INPUT  | chain-data SHA256:',input_digest)

R6=native_ring(6)
rank6={word:idx for idx,word in enumerate(R6)}
assert len(rank6)==64
assert all(rank6[partner(x,6)]==63-rank6[x] for x in range(64))
assert (0<<4)|(3<<2)|1==13  # published A=00,T=11,G=01 maps ATG to 001101=13
print('RING   | R6 native facing verified for 64 words; ATG word=13 under published 2-bit encoding')

# Explicit non-identifiability: two clock phase assignments satisfy the same circular carry law.
# This does NOT rotate or modify the actual native ring; only the unobserved read offset changes.
r4=native_ring(4)
bits=''.join(format(x,'04b') for x in r4)
M=len(bits);mask=(1<<M)-1
assert M==64
for phase in (0,1,7,19):
    v=int(bits[phase:]+bits[:phase],2)
    for k in range(M):
        b=int(bits[(phase+k)%M]); nxt=2*v-mask*b
        v=nxt
        assert v==int(bits[(phase+k+1)%M:]+bits[:(phase+k+1)%M],2) if ((phase+k+1)%M)!=0 else v==int(bits,2)
    assert v==int(bits[phase:]+bits[:phase],2)
# A tangible same-input, different-output example at fixed physical event indices.
for length in (24,32):
    schedules=[]
    for phase in (0,1):
        bs=''.join(bits[(phase+t)%M] for t in range(length))
        schedules.append([t for t in range(1,length) if bs[t-1:t+1]=='01'])
    assert schedules[0]!=schedules[1]
    print(f'PROOF  | identical {length}-step input/clock; legal phase0 breaks={schedules[0]} phase1 breaks={schedules[1]}')
print('PROOF  | circular end-around carry holds at all 64 positions at each of four phases; ring alone cannot select a phase')

# Conditional candidate: raw codon (published six-bit base word) selects its fixed address
# on R6. Read the native ring hemisphere bit, then 0->1 across adjacent *actual
# codon positions* (including full-gene numbering, no crystallographic gap steps).
# No fitted phase. HEMISPHERE IS AN ENCODING CONVENTION, NOT A BIOLOGICAL RULE.
PROTOCOL={
 'version':VERSION,'test':'conditional codon-word-to-R6-address hemisphere transition',
 'base_encoding':{'A':'00','G':'01','C':'10','T':'11'},
 'r6':'ascending lower representatives, last-pair crease swap, reflected remaining faces',
 'registration':'codon[t] is an R6 word, x[t]=rank_R6(codon[t]); one codon per translation step',
 'readout':'bit[t] = 1 iff rank_R6(codon[t]) >= 32',
 'event':'bit[t-1]=0 and bit[t]=1, with t and t-1 both matched to consecutive resolved residues',
 'predicted_sum':'S = (resolved_index[t-1] + resolved_index[t]) = 2*i-1, odd only',
 'controls':'same-count uniform-residue boundaries; random-phase shifting event positions; shuffled synonymous codons within each gene',
 'target':'same 143 as §188: N-O nearest <=3.5A, skip adjacent <=2, proline no donor, constant-S facing run >=3 with first-index increment <=2 and terminal gap<=8',
 'trials':TRIALS,'synonymous_trials':SYNONYMOUS_TRIALS,'seed':SEED,
 'qualification':'not a derived physical readout; no even-S or distant-partner prediction; data are public to the analyst; seal is program-order not external preregistration',
 'input_sha256':input_digest,
}

def boundary_events(d, codons, inverted=False):
    # Use full gene codon position; no structural information is needed except the
    # resolved-to-gene index map, required to project output for later evaluation.
    b=[int(rank6[int(c)]>=32)^int(inverted) for c in codons]
    indices=[r[0] for r in d['residues']]
    return [i for i in range(1,len(indices)) if indices[i-1]+1==indices[i]
            and b[indices[i]-1]==0 and b[indices[i]]==1]

manifest=[]
for idx,d in enumerate(DATA):
    ev=boundary_events(d,d['codons'])
    ev_inverse=boundary_events(d,d['codons'],inverted=True)
    manifest.append({'index':idx,'pdb':d['pdb'],'acc':d['acc'],'set':d['set'],
                     'resolved_L':len(d['residues']),'gene_L':len(d['codons']),
                     'breaks':ev,'inverse_breaks':ev_inverse,
                     'predicted_S':[2*i-1 for i in ev]})
seal_payload={'protocol':PROTOCOL,'predictions':manifest}
canonical=json.dumps(seal_payload,sort_keys=True,separators=(',',':')).encode()
seal_sha=hashlib.sha256(canonical).hexdigest()
seal_name='NEXUS_Registration_v02_Prediction_Seal.json'
(OUTPUT/seal_name).write_text(json.dumps({'sha256':seal_sha,'payload':seal_payload},indent=2)+'\n')
print('SEAL   | prediction SHA256',seal_sha)
print('SEAL   | per-chain conditional predictions written BEFORE accessing coordinate arrays')
print('SEAL   | codon-address 0->1 events:',sum(len(m['breaks']) for m in manifest),
      '| inverse-address events:',sum(len(m['inverse_breaks']) for m in manifest))

# Stage 2. Structural target uses only coordinates, not codons, as in earlier audit.
def target_hairpins(d):
    rr=d['residues'];n=len(rr)
    if n<30:return []
    seq=[r[1] for r in rr]
    nxyz=np.array([r[2] for r in rr],dtype=np.float64)
    oxyz=np.array([r[5] for r in rr],dtype=np.float64)
    dd=np.linalg.norm(nxyz[:,None,:]-oxyz[None,:,:],axis=2)
    ii=np.arange(n);dd[np.abs(ii[:,None]-ii[None,:])<=2]=np.inf
    closes=set()
    for i in range(1,n):
        if seq[i]=='P':continue
        j=int(dd[i].argmin())
        if dd[i,j]<=3.5:closes.add((i,j))
    bysum={}
    for i,j in closes:bysum.setdefault(i+j,[]).append((min(i,j),max(i,j)))
    out=[]
    for S,pts in bysum.items():
        pts=sorted(set(pts));run=[pts[0]]
        for p in pts[1:]+[None]:
            if p is not None and p[0]-run[-1][0]<=2:
                run.append(p);continue
            if len(run)>=3 and run[-1][1]-run[-1][0]<=8:
                out.append({'S':S,'arm_0':run[0][0],'arm_1':run[0][1],
                            'contacts':len(run),'axis':S/2,'parity':'even' if S%2==0 else 'odd'})
            if p is not None:run=[p]
    return sorted(out,key=lambda v:(v['S'],v['arm_0']))

observations=[target_hairpins(d) for d in DATA]
assert sum(len(o) for o in observations)==143
assert sum(v['S']%2==0 for arr in observations for v in arr)==49
print('TARGET | 160 chains, 143 hairpins, 49 even S and 94 odd S; identical §188 extraction')

def score(evs,obs=observations):
    return {t:sum(min((abs((2*i-1)-h['S']) for i in e),default=10**9)<=2*t
                  for e,arr in zip(evs,obs) for h in arr) for t in (0,1,2)}

main_events=[m['breaks'] for m in manifest]
inv_events=[m['inverse_breaks'] for m in manifest]
main=score(main_events);opposite=score(inv_events)
print('LAND   | R6 conditional codon-address hemisphere 0->1:',main)
print('LAND   | inverse hemisphere orientation 0->1:',opposite)
print('LAND   | even-S exact',sum(h['S']%2==0 and h['S'] in {2*i-1 for i in ev} for ev,arr in zip(main_events,observations) for h in arr),
      '(algebraically forbidden by boundary-only rule)')

rng=random.Random(SEED)
T=(0,1,2)
null={k:{j:[] for j in T} for k in ('equal_count','random_phase','synonymous_shuffle')}
start=time.perf_counter()
for trial in range(TRIALS):
    equal=[];phase=[]
    for m,events in zip(manifest,main_events):
        L=m['resolved_L'];k=len(events)
        equal.append(rng.sample(range(1,L),k) if k else [])
        delta=rng.randrange(L) if L else 0
        phase.append([(e+delta)%L for e in events if ((e+delta)%L)!=0])
    for key,arr in [('equal_count',equal),('random_phase',phase)]:
        s=score(arr)
        for j in T:null[key][j].append(s[j])
for trial in range(SYNONYMOUS_TRIALS):
    alt=[]
    for d in DATA:
        cods=list(d['codons'])
        # Shuffle codon identities only among positions encoding the same residue.
        groups=collections.defaultdict(list)
        for t,a in enumerate(d['uniprot_sequence']):groups[a].append(t)
        for positions in groups.values():
            vals=[cods[t] for t in positions]
            rng.shuffle(vals)
            for t,v in zip(positions,vals):cods[t]=v
        alt.append(boundary_events(d,cods))
    s=score(alt)
    for j in T:null['synonymous_shuffle'][j].append(s[j])

def summarize(v):
    a=np.asarray(v,dtype=float)
    return {'mean':round(float(a.mean()),4),'q025':float(np.quantile(a,.025)),
            'q975':float(np.quantile(a,.975)),
            'upper_tail_p':round(float((1+np.sum(a>=v_observed))/(len(a)+1)),6)}
results_null={}
for key in null:
    results_null[key]={}
    for j in T:
        v_observed=main[j]
        results_null[key][str(j)]=summarize(null[key][j])
        x=results_null[key][str(j)]
        print('NULL   | %-20s tol=%d observed=%3d mean=%6.2f 95%%=[%2d,%3d] P(null>=obs)=%.4f' %
             (key,j,main[j],x['mean'],int(x['q025']),int(x['q975']),x['upper_tail_p']))
print('TIME   | three control ensembles',round(time.perf_counter()-start,2),'seconds')

# Independent counterexample: for a local crease sum S, many register pairs possible.
S=30;L=40
pairs=[(i,S-i) for i in range(L) if 0<=S-i<L and (S-i)-i>2]
assert len(pairs)>2
print('REACH  | same 40-residue prefix, local sum S=30 admits',len(pairs),'distinct valid separated pairs; sample',pairs[:5],'; no partner selector follows from S')

# Account for spatially unresolved residues; quantify the limitation of gene->PDB mapping.
missing_adj=sum(sum(d['residues'][i][0]!=d['residues'][i-1][0]+1
                    for i in range(1,len(d['residues']))) for d in DATA)
print('INDEX  | nonconsecutive full-gene indices among adjacent resolved residues:',missing_adj)

per_chain=[]
for d,m,arr in zip(DATA,manifest,observations):
    es=set(m['predicted_S']);ev=m['breaks']
    per_chain.append({k:m[k] for k in ('index','pdb','acc','set','resolved_L','gene_L')}
                     | {'event_count':len(ev),'predicted_S':m['predicted_S'],
                        'observed_hairpins':arr,'exact':sum(h['S'] in es for h in arr),
                        'near1':sum(any(abs(2*i-1-h['S'])<=2 for i in ev) for h in arr)})
res={'version':VERSION,'sha256_seal':seal_sha,'input_sha256':input_digest,
     'total_hairpins':143,'even_S':49,'odd_S':94,'total_chains':160,
     'residue_agreements':residue_checks,'missing_adjacent_gene_indices':missing_adj,
     'model':'conditional codon R6 rank hemisphere; no physical registration law claimed',
     'events':sum(map(len,main_events)),'main':main,
     'inverse_events':sum(map(len,inv_events)),'inverse':opposite,
     'null':results_null,'per_chain':per_chain,
     'nonidentifiability':'legal ring phases give different breaks for identical inputs; no rule identifies R6 address hemisphere with molecular crease',
     'even_S_limitation':'boundary e,s=e+1 yields odd S only; even crease needs independent centre-selection rule',
     'reach_limitation':'fixed S still permits multiple different pairs (i,S-i)',
     'status':{'STANDS':['native facing law','end-around carry for each arbitrary phase','odd S for adjacent boundary'],
               'RUNS':['gene-to-residue indexing verified','conditional codon rank test','matched-count, phase and synonymous controls'],
               'DEAD_END':['unregistered serialized ring phase as structural predictor'],
               'OPEN':['physical codon->ring-phase/hemisphere coupling','even-S center rule','long-range REACH']}}
(OUTPUT/'NEXUS_Registration_v02_Results.json').write_text(json.dumps(res,indent=2)+'\n')
print('LEDGER | STANDS: ring identities, phase invariance of carry, boundary odd-S algebra')
print('LEDGER | RUNS: codon-word conditional candidate, 143 observed creases and three controls')
print('LEDGER | DEAD END: an unregistered ring stream pretending to predict creases')
print('LEDGER | OPEN: biochemical readout, even-S centres, distant partner REACH')
print('FILES  |',seal_name, 'NEXUS_Registration_v02_Results.json')
```
