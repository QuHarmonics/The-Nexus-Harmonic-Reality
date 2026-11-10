# NEXUS §196 — The face-coherence reader and the missing sheet plane

**Dean A. Kulik · QuHarmonics Research Group · ORCID 0009-0003-3128-8828**  
**30 October 2026 · Continuation of the running audit, §195**  
**Status: the sequence rule is sealed and executable; the original 143-hairpin data is UNLINKED in this session. No observed centre rankings are represented as new runs.**

## 196.1 What §195 already owns

The ring's instruction set is in its differences. The address transposition in the pair square is exact, and the value/shape split is invertible. These are not new hypotheses in §196. The seam is one centred transposition; the wrap is complement, acting on the value channel without changing the shape. The step program's mirror is exact in the shape channel, with its palindrome corrections carried in the face channel. Those identities determine what this next reader is allowed to ask.

The observed hairpin audit has already supplied two distinct objects. The local Cα construction gives **801/822** physically corresponding paired rows and **1,370/1,404** side-chain face alternations. With the physical sheet normal **read from the completed structure**, the approximate sequence slot-density reader calls the more buried physical face in **112/141 evaluable hairpins**. That is *structure-conditioned decompilation*. It does not locate a fold from an unseen sequence. The methods-v1 record also retains a related, differently evaluated earlier dry-face tally, **111/143**; those denominators must not be merged.

The attempted sequence-only value mirror is a DEAD END: **10/143** true centres first within ±8 and normalized mean-rank advantage **0.5299**, against about **0.4985** for composition-preserving shuffles and **0.5014** for shifted centres in the running audit. Those are prior recorded measurements, not §196 rerun results. A value bit need not equal its partner value for both residues to belong to a consistent physical face. The old reader demanded equality of individual values where the shape channel supplies an address transposition and the value channel contributes a *contrast of groups*.

This section therefore changes exactly one question: **Does a candidate crease organize the sequence into two alternating rows whose water-facing slot-density difference remains coherent as the hypothetical paired arms extend?** No physical face normal enters the prediction, and no observed crease or arm length enters the sequence score.

## 196.2 The four operations remain separate

The common operand is a binary word. For an $n$-bit word $x=(b_0,\ldots,b_{n-1})$, with $b_0$ most significant, define

$$
f(x)=b_0,\qquad \delta_i(x)=b_i\oplus b_{i+1},\qquad
b_{i+1}=b_i\oplus\delta_i.
$$

The split $(f,\delta)$ is invertible. $C(x)=x\oplus 1^n$ flips $f$ and leaves $\delta$ unchanged. The native $P$ reverses $\delta$, including its complement branch at palindromes. The residue-address square uses

$$
W_n(i,j)=i\parallel J(j),\qquad
P_{2n}(W_n(i,j))=W_n(j,i)\quad(i\ne j).
$$

On the diagonal, $W_n(i,i)$ is a palindrome, so the fixed-point-free partner selects **complement**, $P(W_n(i,i))=W_n(C(i),C(i))$, not a fixed transposition. That exception must remain in the ISA.

The physical chain then exposes four different operations, which cannot be collapsed by renaming them:

| Operation | Input → output | What is known at prediction time? |
|---|---|---|
| **Address transposition** | paired residue addresses $(i,j)\mapsto(j,i)$; sum address $S=i+j$ | exact abstract address operation; not an observed bond |
| **Shape parity** | hypothesized row index $t\mapsto t\bmod2$ from a candidate crease | computable from the candidate geometry in index space; the absolute face sign is free |
| **Side-chain value** | amino-acid symbol $a\mapsto v(a)=\mathrm{WET}(a)\in\{0,2,3,5,7\}$; optional already-defined $b(a)=\mathbf1[v(a)>0]$ | sequence alone; *Reading Proteins* §5 table retained without alteration |
| **Physical orientation** | local frame plus opposite-arm geometry $\mapsto$ sheet normal $\hat n$ and oriented Cβ projection | **not** available from sequence or one local tetrahedron; read only after construction/structure |

Here $t\bmod2$ is a local alternation at a *candidate* crease. It is not a newly selected universal ring phase. No new physical bit, energy term, fitted coefficient, learned parameter or global phase is introduced.

## 196.3 Seal the sequence reader before reading the crease

For every chain sequence and each candidate sum address $S$, examine each integer candidate turn width $w\in\{3,4,5,6,7,8\}$ for which

$$
e=(S-w)/2,\qquad s=(S+w)/2
$$

are integer indices with all hypothetical paired residues $e-t$ and $s+t$ present for $t=0,\ldots,8$. The widths of the wrong parity cannot be paired with $S$; no residue is inserted to make them fit. The sequence-only reader is

$$
r_t(S,w)=\frac{v(a_{e-t})+v(a_{s+t})}{2},\qquad t=0,\ldots,8.
$$

It does **not** require $v(a_{e-t})=v(a_{s+t})$. Instead, for each prefix $h\in\{3,4,5,6,7,8\}$, compare the two alternating row means:

$$
\Delta_h(S,w)=\frac{\sum_{0\le t\le h,\ t\ \mathrm{even}} r_t}{\#\{0\le t\le h:t\ \mathrm{even}\}}
-\frac{\sum_{0\le t\le h,\ t\ \mathrm{odd}} r_t}{\#\{0\le t\le h:t\ \mathrm{odd}\}}.
$$

This asks whether a contrast persists while adding successive hypothetical rows. It does not assign either row to the outward, inward, dry, wet, upper or lower *physical* face. Reversing which abstract row is named A changes the sign, not the score.

The six prefixes are fixed before seeing structural centres. Since the original slot table is integral, the contrast can be encoded exactly:

$$
D_h=1440\Delta_h\in\mathbb Z,\qquad
Q(S,w)=\left|\sum_{h=3}^{8}D_h(S,w)\right|,\quad 0\le Q\le 60480.
$$

The integer $1440$ is the least common multiple of the six row-mean denominators, not a tuned coefficient. $60480=6\cdot7\cdot1440$ is the full-range normalization. A sign reversal across prefixes cancels part of the sum; consistently signed large contrasts persist. The trace also reports how many of the six nonzero $D_h$ agree with the sign of their total, and how many oppose it. The primary score is fixed: $Q(S)=\max_w Q(S,w)$; a tie chooses the **smallest admissible width**. This optimizes over unknown *turn-width labels* for every candidate equally, never over the known structure.

The score readout's **way home** is fixed too: only after a canonical SHA-256 seal of **every** $(S,w,Q,D_3,\ldots,D_8)$ sequence score does the old §188 nearest N→O detector read coordinates and supply true $(e,s,k,S)$. The true centre $S$ is ranked against valid candidate scores in $[S-8,S+8]$ by midrank. If the centre lacks a valid 8-row candidate, it is **UNLINKED**, not filled, given zero, or silently dropped. Report it in the 143-row trace.

The rule text itself has a SHA-256 seal, including the read-back path and controls. The exact rule seal from the executed cell is:

`d98925c95f2b01c4818eb7894f91e80ce01a84146642fcf2df69b4e79530ff9a`

A score seal for the original 143-hairpin experiment cannot be printed here because the original sequence file was not among the attachments. Inventing that hash would violate the seal.

## 196.4 The controls, with the right unit of uncertainty

A local high contrast is not automatically a crease. The controls ask whether the *observed* crease receives an unusual score relative to the alternatives it competes with:

1. **Composition-preserving shuffled chains.** Permute the amino acids within each chain, recompute every candidate score with the identical width and prefix rules, and rank the real centre locations *without using structure in the score*. Make 200 independent replicates, seeded as written in the rule. The null is not a new source of residues.
2. **Shifted centres.** Hold the actual sequence scores fixed; displace each observed centre by one of $\pm2,\pm4,\pm6,\pm8$ when evaluable. Retaining parity prevents a width-class change from masquerading as a centre-position effect. Run 200 seeded replicates and rank each shifted location in its own ±8 window.
3. **Matched detector-negative decoys.** In the same chain, require centre parity equality and exclusion from ±16 of **all** detected hairpin centres, so the ranked windows cannot share a detected true centre. Match the composition of a fixed 25-residue neighbourhood by the L1 distance of the 20 amino-acid counts, breaking ties by centre index and avoiding reuse until necessary. These are *detector-negative* controls, not guaranteed proof of non-hairpin secondary structure.

The rank statistic is $A=(m-r)/(m-1)$ for $m$ valid candidates in the centre's window and midrank $r$, so $A=1$ is a unique first-place landing and $A\approx0.5$ is an unprivileged position. Every source hairpin has a ledger row including the real width, sequence-selected width, all six signed prefix contrasts, contrast-reversal count, rank, mean shuffled/shifted advantage, matched decoy, competing window scores, and every failed condition. The empirical tail count is $(1+\#\{A_{\rm null}\ge A_{\rm true}\})/201$ for 200 null replicates.

The 143 hairpins are *not* 143 independent observations. The code also resamples complete **chains** with replacement (2,000 chain-block bootstrap draws) and reports 95% percentile intervals on mean observed advantage and the paired differences from each control. A one-chain input yields **UNLINKED** uncertainty rather than a fictitious zero-width confidence interval. Invalid or missing predictions are explicitly counted, and paired comparisons use only hairpins evaluable in both arms of the comparison.

This is a preregistered comparison, not a post-result choice of the width, threshold, sign, contrast weight, or best-performing null.

## 196.5 What the rule can and cannot identify, before structural data

The sequence algorithm has been executed on exact synthetic controls, not on substitute experimental proteins:

- With a planted pair of nine alternating rows at $(e,s)=(22,27)$ in a 70-residue sequence, each $D_h=-10080$; $Q=60480$, and **all six prefixes retain the same direction**. The operator detects the intended *coherent difference*, rather than residue-to-residue equality being a requirement.
- On a homogeneous 70-residue sequence, all **101** evaluable centre scores are zero. No sequence-only face contrast can locate a crease there.
- On the repeating sequence `AR` repeated 35 times, **50 distinct centres** attain the same maximum $Q=60480$. Even perfect coherence does **not** supply a unique address. The repetition carries a face-periodic shape but leaves the crease location **AMBIGUOUS**.

These failures are constraints on the reader. A wet/dry periodicity is not an address by itself. If the original true centres do not outrank the controls, the next missing provider is **registration of the opposite arm**, not an added hydrophobic bit or a fitted score. This is the exact place to reverse the gap: hold the type of the missing information fixed (which two index-space arms bind) rather than search new coefficients.

## 196.6 The sheet-normal gap: a constructive no-go result

The covalent fragment $(N,C_\alpha,C,C_\beta)$ can establish a **local chiral frame**, because the signed volume

$$
\chi=\det\bigl[N-C_\alpha,\ C-C_\alpha,\ C_\beta-C_\alpha\bigr]
$$

is nonzero for a nondegenerate Cβ tetrahedron. That is not the same as identifying a β-sheet plane. A sheet plane requires a second independent direction transverse to the strand. No partner-arm position occurs in these four local covalent coordinates.

The executed counterexample fixes the same atoms in both constructions (Ångström-like coordinates are used solely as a geometric witness):

$$
N=(-1.458,0,0),\quad C_\alpha=(0,0,0),\quad C=(0.550,1.420,0),\quad C_\beta=(-0.535,0.780,-1.205).
$$

Even granting the local reader a **supplied** strand tangent $u=(1,0,0)$, consider two possible transverse directions of a later partner arm:

$$
\begin{aligned}
w_1&=(0,1,0), & n_1=u\times w_1&=(0,0,1), & n_1\cdot(C_\beta-C_\alpha)&=-1.205;\\
w_2&=(0,0,-1), & n_2=u\times w_2&=(0,1,0), & n_2\cdot(C_\beta-C_\alpha)&=+0.780.
\end{aligned}
$$

Both use **identical N, Cα, C, Cβ**, identical bond geometry and identical nonzero chirality $\chi=2.494784$. Yet the candidate sheet normals are orthogonal and the Cβ face sign reverses. The points of the other arm can be placed along the corresponding transverse direction at suitable separation; the local coordinates give no rule for preferring one direction. This is a counterexample to *geometric identifiability from that local fragment*, not a claim that these abstract placements already satisfy the complete β-sheet hydrogen-bond network.

In fact, the no-go result is stronger than needed: an unoriented sheet plane cannot be selected, much less its oriented normal. Supplying more precise local bond lengths or the correct L-amino-acid chirality cannot identify the absent nonlocal vector. A strand tangent together with **one independent cross-strand correspondence** (another-arm Cα displacement or an explicitly identified hydrogen-bond partner direction) supplies the missing plane geometrically, as long as the two vectors are not collinear. The choice of normal sign then requires an orientation convention; to call a face *more buried* also requires surrounding occupancy or solvent information. A fixed local Cβ vector does not carry that environmental readout.

This is why the prior 801/822 correspondence and 1,370/1,404 alternation, which use the completed structure, are fully compatible with a sequence-only crease reader remaining OPEN. The local geometric machinery can decompile an already-formed sheet; it does not supply an unseen partner-arm address.

## 196.7 Result of this execution and data boundary

The supplied attachments were the §195 running audit, methods manuscript, methods notebook and AI-writing-failure record. Their code references the original **`ecoli_chains.json`** and optional **`NEXUS_Fold_Compiler_Notebook (2).zip`**, but neither raw data file was supplied in the current artifact set. Searching the connected Drive by those exact names also found no matching file. The earlier audit's aggregate numbers cannot be inverted into residue sequences, coordinate-derived closure sets, 143 valid score vectors or independent null distributions.

Consequently, the **actual §196 centre rankings, 200-replicate controls, chain-block intervals and 143 per-hairpin traces are OPEN / UNLINKED here**. They are implemented, but no run on those structures is claimed. The cell's score seal is produced *before* it computes any hairpins whenever the original data becomes accessible, and it refuses to substitute or fabricate records. It also prints a mismatch rather than manipulating the detector to force 143 observations.

**Precisely what ran:** the binary address identities, exact integer score and persistence on the planted example, two sequence-level ambiguity controls, the geometric counterexample, the missing-data path, and an additional private smoke test exercising the detector, nulls and complete per-hairpin trace on one explicitly synthetic chain. That smoke test is software testing only and is not presented as an observed protein landing. Its one-chain bootstrap is correctly marked UNLINKED.

## 196.8 Full single-cell Jupyter implementation

Run the following as **one cell**. Requires Python 3.8+ and NumPy. The only optional input is the original `ecoli_chains.json` or its original compiler ZIP, in the current directory, `/mnt/data`, or a path supplied by environment variable `NEXUS_DATA`. The program prints the exact rule hash and, when data is linked, hashes the **complete integer candidate-score ledger before reading the observed locations**. The final trace prints **every** detected hairpin and every failure; no other repository modules, fitted parameters, new datasets, or network calls are used.

```python
# NEXUS §196 — one-cell, no imported NEXUS modules; Python 3 + NumPy.
# Stage A uses only sequence strings; Stage B is unreachable until A and its score hash are printed.
import os, json, math, hashlib, random, collections, zipfile
from pathlib import Path
import numpy as np

AUTHOR = 'Dean A. Kulik | QuHarmonics Research Group | ORCID 0009-0003-3128-8828'
WET = {'G':0,'A':0,'V':0,'L':0,'I':0,'F':0,'P':0,'C':2,'M':2,'W':2,
       'S':3,'T':3,'Y':3,'H':3,'K':3,'N':5,'Q':5,'D':5,'E':5,'R':7}
MAX_H = 8
RULE = ('NEXUS196/v1; sequence WET table from Reading Proteins s5 as recorded s195; '
        'candidate width w=3..8; e=(S-w)/2,s=(S+w)/2 integers; full t=0..8; '
        'r_t=(WET[e-t]+WET[s+t])/2; for h=3..8 let Delta_h=mean_even_rows_0..h(r)-mean_odd_rows_0..h(r); '
        'D_h=1440*Delta_h exact integer; Q(S,w)=abs(sum_h D_h) integer in [0,60480]; '
        'Q(S)=max_w Q(S,w), ties smaller w; physical A/B orientation deliberately unknown; '
        'way home: original s188 N-to-nearest-O hairpin detector run only after candidate score seal, observed S=e+s and true ranks; '
        'midrank +-8 among valid candidate centres; chain composition shuffles seed 196 200 reps; '
        'shift +-2,+-4,+-6,+-8 with matching parity; decoy same chain, centre parity, '
        'outside +-16 of every hairpin centre, 25-position 20aa-composition L1 minimum, then centre ascending; '
        'chain block bootstrap seed 196196 2000 reps; no fitted weights, energy, or ring phase.')
sha = lambda v: hashlib.sha256(v).hexdigest()
def canon(x): return json.dumps(x,sort_keys=True,separators=(',',':'),ensure_ascii=True).encode()
print('NEXUS §196   SEQUENCE FACE COHERENCE / LOCAL PLANE NON-IDENTIFIABILITY')
print('AUTHOR',AUTHOR)
print('RULE SHA-256',sha(RULE.encode()))
print('SCORE UNIT Q/60480, with D_h = 1440 * Delta_h (integer)')

# ------------------------------ Common binary address base: no physical meanings smuggled into addresses.
def J(x,n): return int(format(x,f'0{n}b')[::-1],2)
def C(x,n): return x^((1<<n)-1)
def P(x,n): return C(x,n) if J(x,n)==x else J(x,n)
def pairword(i,j,n): return (i<<n)|J(j,n)
def shape(x,n): return (x^(x>>1))&((1<<(n-1))-1)
def unsplit(f,d,n):
    b=[f]
    for k in range(n-1): b.append(b[-1]^((d>>(n-2-k))&1))
    return int(''.join(map(str,b)),2)
for n in (2,3,4,6):
    assert all(unsplit(x>>(n-1),shape(x,n),n)==x for x in range(1<<n))
for i in range(16):
    for j in range(16):
        q=pairword(i,j,4)
        if i!=j: assert P(q,8)==pairword(j,i,4)
        else: assert P(q,8)==pairword(C(i,4),C(i,4),4)
print('STANDS/RUNS ADDRESS: (f,delta) inverse n=2,3,4,6; off-diagonal P(i||J(j))=j||J(i), diagonal -> C(i)||J(C(i)) on n=4: PASS')
print('OPS KEEP SEPARATE: transposition (i,j)->(j,i); parity t&1; value b=1[WET>0]; orientation sign[n_sheet dot (CB-CA)] UNLINKED until geometry')

# ------------------------------ Exact integer score and deterministic candidate ledger.
def score_sequence(seq):
    v=np.fromiter((WET[a] for a in seq),dtype=np.int64,count=len(seq))
    L=len(v); entries=[]; best={}
    for w in range(3,9):
        e=np.arange(MAX_H,L-w-MAX_H,dtype=np.int64)
        if len(e)==0: continue
        s=e+w
        rows=np.stack([v[e-t]+v[s+t] for t in range(MAX_H+1)])
        even=np.zeros(len(e),dtype=np.int64); odd=np.zeros(len(e),dtype=np.int64)
        ec=oc=0; ds=[]
        for h in range(MAX_H+1):
            if h%2==0: even+=rows[h]; ec+=1
            else: odd+=rows[h]; oc+=1
            if h>=3:
                # Delta_h = even/(2ec) - odd/(2oc), and 2ecoc always divides 1440.
                denom=2*ec*oc
                assert 1440%denom==0
                ds.append((even*oc-odd*ec)*(1440//denom))
        D=np.stack(ds).T
        Q=np.abs(D.sum(axis=1))
        for j in range(len(e)):
            S=int(e[j]*2+w); d=tuple(map(int,D[j])); q=int(Q[j]);
            row=(S,w,q,d)
            entries.append(row)
            if S not in best or q>best[S][2] or (q==best[S][2] and w<best[S][1]): best[S]=row
    entries.sort(key=lambda z:(z[0],z[1]))
    return entries,best

def rank(S,best):
    win=[(a,best[a][2]) for a in range(S-8,S+9) if a in best]
    if S not in best or len(win)<2:return None
    q=best[S][2]; gt=sum(x>q for _,x in win); eq=sum(x==q for _,x in win)
    rk=1+gt+(eq-1)/2
    return (rk,(len(win)-rk)/(len(win)-1),len(win))

def delta_persistence(d):
    s=sum(d)
    if not s:return 0,0
    sg=1 if s>0 else -1
    return sum(int(x*sg>0) for x in d),sum(int(x*sg<0) for x in d)

toy=['G']*70; e0=22; w0=5; s0=e0+w0
for t in range(9):
    aa='A' if t%2==0 else 'R'
    toy[e0-t]=aa; toy[s0+t]=aa
et,bt=score_sequence(''.join(toy))
q=next(row for row in et if row[0]==e0+s0 and row[1]==w0)
assert q[2]==60480 and q[3]==(-10080,)*6, q
print('RUNS TOY 70-residue planted alternating arms, e=22 s=27 width=5: Q=',q[2],'/60480; D3..8=',q[3],'; persistence=',delta_persistence(q[3]))
# Required failure demonstrations: contrast-free sequences and multiple equally coherent creases.
_,uniform_best=score_sequence('A'*70)
assert len(uniform_best)>0 and all(r[2]==0 for r in uniform_best.values())
print('RUNS FAILURE homogeneous A*70: all',len(uniform_best),'candidate centres have Q=0; no centre is identifiable')
_,repeat_best=score_sequence('AR'*35)
top=max(v[2] for v in repeat_best.values())
topcentres=sorted(S for S,row in repeat_best.items() if row[2]==top)
assert top==60480 and len(topcentres)>1
print('RUNS FAILURE repeating AR*35: global max Q=',top,'shared by',len(topcentres),'distinct centres (first 12:',topcentres[:12],')')

# ------------------------------ Independent geometry counterexample: identical local covalent coordinates.
N=np.array([-1.458,0.,0.]); CA=np.array([0.,0.,0.]); CC=np.array([0.550,1.420,0.]); CB=np.array([-0.535,0.780,-1.205])
tangent=np.array([1.,0.,0.]); across1=np.array([0.,1.,0.]); across2=np.array([0.,0.,-1.])
normal1=np.cross(tangent,across1);normal2=np.cross(tangent,across2)
sgn1=float(np.dot(normal1,CB-CA));sgn2=float(np.dot(normal2,CB-CA))
chiral=float(np.linalg.det(np.stack([N-CA,CC-CA,CB-CA],axis=0)))
assert sgn1*sgn2<0 and abs(np.dot(normal1,normal2))<1.e-12 and abs(chiral)>1.e-6
assert abs(np.linalg.norm(N-CA)-1.458)<1.e-12
print('STANDS GEOMETRY: same N CA C CB and nonzero handed volume %.6f;'%chiral)
print('  counterexample I: tangent',tangent.tolist(),'across',across1.tolist(),'normal',normal1.tolist(),'n.CB = %.3f'%sgn1)
print('  counterexample II: same local atoms, across',across2.tolist(),'normal',normal2.tolist(),'n.CB = %.3f'%sgn2)
print('  sheet normals orthogonal, side-chain face sign reverses; local tetrahedron cannot choose sheet plane.')
print('  required geometric link: independent cross-strand vector plus strand tangent; solvent/burial requires surrounding occupancy.')

# ------------------------------ Optional original data, deliberately not replaced by a different corpus.
def open_data_sequences_and_source():
    roots=[]
    arg=os.environ.get('NEXUS_DATA','').strip()
    if arg:roots.append(Path(arg).expanduser())
    roots.extend([Path.cwd(),Path('/mnt/data')])
    seen=set()
    for r in roots:
        if str(r) in seen:continue
        seen.add(str(r))
        fs=[r] if r.is_file() else [r/'ecoli_chains.json'] if r.is_dir() else []
        for f in fs:
            if f.is_file() and f.suffix.lower()=='.json' and (f.name=='ecoli_chains.json' or f==Path(arg)):
                raw=f.read_bytes(); obj=json.loads(raw)
                seqs=[''.join(row[1] for row in ent['residues']) for ent in obj]
                return seqs,('json',str(f),None),sha(raw)
        zips=([r] if r.is_file() and r.suffix.lower()=='.zip' else
              [r/'NEXUS_Fold_Compiler_Notebook (2).zip'] if r.is_dir() else [])
        for z in zips:
            if not z.is_file():continue
            with zipfile.ZipFile(z) as zz:
                hits=[n for n in zz.namelist() if n=='ecoli_chains.json' or n.endswith('/ecoli_chains.json')]
                if len(hits)!=1:raise ValueError('Expected one ecoli_chains.json in '+str(z))
                buf=zz.read(hits[0]); obj=json.loads(buf)
                seqs=[''.join(row[1] for row in ent['residues']) for ent in obj]
                return seqs,('zip',str(z),hits[0]),sha(buf)
    return None,None,None

def load_full_from_source(src):
    kind,path,member=src
    if kind=='json':return json.loads(Path(path).read_bytes())
    with zipfile.ZipFile(path) as z:return json.loads(z.read(member))

seqs,source,source_hash=open_data_sequences_and_source()
if seqs is None:
    print('OPEN DATA UNLINKED: ecoli_chains.json / original NEXUS_Fold_Compiler_Notebook (2).zip not supplied.')
    print('NO 143-HAIRPIN SCORES OR RANKS CLAIMED. No invented data, controls, or per-hairpin outcomes.')
    print('RUN COMMAND: set NEXUS_DATA to the original JSON or ZIP path, then run this unchanged single cell.')
else:
    print('STAGE A ONLY-SEQUENCE DATA SOURCE',source,'raw SHA-256',source_hash,'chains',len(seqs))
    bad=sorted({a for s in seqs for a in s if a not in WET})
    if bad:raise ValueError('UNLINKED residue letter(s); stop rather than fill by convention: '+repr(bad))
    ledger=[]; bests=[]; nc=0
    for ci,seq in enumerate(seqs):
        entries,best=score_sequence(seq); bests.append(best)
        ledger.append({'chain':ci,'sequence_sha256':sha(seq.encode()),'candidates':entries})
        nc+=len(entries)
    score_hash=sha(canon({'rule_hash':sha(RULE.encode()),'score_ledger':ledger}))
    print('STAGE A SCORES SEALED (BEFORE ANY COORDINATE-DERIVED LOCATIONS ARE COMPUTED)')
    print('  raw (S,w,Q,D3..8) candidate rows',nc,'valid centre scores',sum(map(len,bests)),'SHA-256',score_hash)
    del ledger

    # ---- STAGE B: only here are C=O and N coordinates loaded and hairpin labels computed.
    original=load_full_from_source(source)
    def closures(ent):
        r=ent['residues']; L=len(r); seq=[x[1] for x in r]
        n=np.array([x[2] for x in r],dtype=float)
        o=np.array([x[5] for x in r],dtype=float)
        dd=np.linalg.norm(n[:,None,:]-o[None,:,:],axis=2)
        ix=np.arange(L);dd[np.abs(ix[:,None]-ix[None,:])<=2]=np.inf
        out=set()
        for i in range(1,L):
            if seq[i]=='P':continue
            j=int(dd[i].argmin())
            if dd[i,j]<=3.5:out.add((i,j))
        return out
    def hairpins(directed,L):
        und={(min(i,j),max(i,j)) for i,j in directed}
        byS=collections.defaultdict(list)
        for a,b in und:byS[a+b].append((a,b))
        out=[]
        for S,pts in byS.items():
            pts=sorted(set(pts));run=[pts[0]]
            for p in pts[1:]+[None]:
                if p is not None and p[0]-run[-1][0]<=2:run.append(p);continue
                if len(run)>=3 and run[-1][1]-run[-1][0]<=8:
                    e,s=run[-1];out.append((e,s,min(e-run[0][0],e,L-1-s),S))
                if p is not None:run=[p]
        return out
    hp=[]
    for ci,ent in enumerate(original):
        if len(ent['residues'])>=30:
            hp.extend([(ci,e,s,k,S) for e,s,k,S in hairpins(closures(ent),len(ent['residues']))])
    hp.sort(key=lambda a:(a[0],a[4],a[1],a[2]))
    print('STAGE B observed hairpins',len(hp),'(historical benchmark 143; report mismatch, do not force)', 'even S',sum(S%2==0 for ci,e,s,k,S in hp))
    if len(hp)!=143: print('FAILURE BENCHMARK COUNTS: expected 143 from §195, observed',len(hp),'; source or detector differs.')
    # Decoy library: same chain, same parity, away from ±16 of every observed centre, composition-matched locally.
    hcent=collections.defaultdict(list)
    for ci,e,s,k,S in hp:hcent[ci].append(S)
    ALPH='ACDEFGHIKLMNPQRSTVWY'
    def hist25(seq,S):
        center=S//2; lo=max(0,center-12);hi=min(len(seq),center+13)
        c=collections.Counter(seq[lo:hi]);return tuple(c[a] for a in ALPH)
    decoy_used=collections.defaultdict(set)
    def decoy(ci,S):
        tar=hist25(seqs[ci],S); H=hcent[ci]
        cand=[c for c in bests[ci] if c%2==S%2 and all(abs(c-q)>16 for q in H)]
        if not cand:return None
        # A decoy can be reused only once all uniquely usable candidates have been taken.
        unique=[c for c in cand if c not in decoy_used[ci]]
        if unique:cand=unique
        obj=lambda c:(sum(abs(x-y) for x,y in zip(hist25(seqs[ci],c),tar)),c)
        v=min(cand,key=obj); decoy_used[ci].add(v)
        return v
    results=[]
    for num,(ci,e,s,k,S) in enumerate(hp,1):
        bc=bests[ci]; r=rank(S,bc); dS=decoy(ci,S)
        dr=rank(dS,bc) if dS is not None else None
        w=bc[S][1] if S in bc else None
        q=bc[S][2] if S in bc else None
        d=bc[S][3] if S in bc else None
        persist,flip=delta_persistence(d) if d is not None else (None,None)
        failures=[]
        if r is None:failures.append('NO_VALID_TRUE_SCORE')
        else:
            if r[0]>3:failures.append('TRUE_NOT_TOP3')
            if r[0]!=1:failures.append('TRUE_NOT_FIRST')
        if flip is not None and flip:failures.append('DELTA_SIGN_REVERSAL')
        if q==0:failures.append('ZERO_CONTRAST')
        if w is not None and w!=s-e:failures.append('BEST_WIDTH_DIFFERS')
        if dr is None:failures.append('DECOY_UNLINKED')
        results.append({'num':num,'ci':ci,'e':e,'s':s,'k':k,'S':S,'width_true':s-e,
                        'w_pred':w,'Q':q,'D':d,'persist':persist,'flip':flip,'rank':r,
                        'decoy_S':dS,'decoy_rank':dr,'failures':failures})
    usable=[x for x in results if x['rank'] is not None]
    print('STAGE C TRUE SCORES:',len(usable),'of',len(results),'evaluable; excluded',len(results)-len(usable))
    print('  TRUE  rank=1',sum(x['rank'][0]==1 for x in usable),'top3',sum(x['rank'][0]<=3 for x in usable),
          'mean advantage',format(np.mean([x['rank'][1] for x in usable]),'.6f') if usable else 'UNLINKED')
    print('  DIRECTION SIGN FLIPS',sum((x['flip'] or 0)>0 for x in results),'ZERO SCORES',sum(x['Q']==0 for x in results),
          'WIDTH MISMATCH',sum(x['w_pred'] is not None and x['w_pred']!=x['width_true'] for x in results))
    # Per-rep nulls track per-hairpin paired outcomes for proper chain-block CIs.
    rng=np.random.default_rng(196); NR=200
    sh_reps=[];shift_reps=[]
    for rep in range(NR):
        shuffled={}
        for ci in sorted(set(x['ci'] for x in usable)):
            a=np.array(list(seqs[ci]),dtype='U1');rng.shuffle(a)
            _,b=score_sequence(''.join(a));shuffled[ci]=b
        shvals={};stvals={}
        for x in usable:
            ci,S=x['ci'],x['S'];rr=rank(S,shuffled[ci]);
            if rr:shvals[x['num']]=rr[1]
            options=[q for off in (-8,-6,-4,-2,2,4,6,8) if (q:=S+off) in bests[ci] and rank(q,bests[ci]) is not None]
            if options:
                v=int(rng.choice(options));stvals[x['num']]=rank(v,bests[ci])[1]
        sh_reps.append(shvals);shift_reps.append(stvals)
    def common_reps(reps):
        common=set(x['num'] for x in usable)
        for r in reps:common &= set(r)
        return sorted(common)
    # Null mean computed on the same common subset; if missing, print coverage.
    def null_summary(reps,title):
        keys=common_reps(reps)
        if not keys:return {},'UNLINKED'
        obs_by={x['num']:x['rank'][1] for x in usable}
        obs=float(np.mean([obs_by[i] for i in keys]))
        dist=np.array([np.mean([r[i] for i in keys]) for r in reps])
        p=(1+int(np.count_nonzero(dist>=obs)))/(len(dist)+1)
        base={i:float(np.mean([r[i] for r in reps])) for i in keys}
        print('  '+title+': n',len(keys),'null mean %.6f sd %.6f obs_same_subset %.6f delta %.6f P(null>=obs) %.5f'%(dist.mean(),dist.std(),obs,obs-dist.mean(),p))
        return base,(obs,float(dist.mean()),p,len(keys))
    shbase,shsum=null_summary(sh_reps,'COMPOSITION SHUFFLE (200)')
    stbase,stsum=null_summary(shift_reps,'SHIFTED CENTRE same parity (200)')
    decbase={x['num']:x['decoy_rank'][1] for x in usable if x['decoy_rank'] is not None}
    if decbase:
        obs_dec=np.mean([x['rank'][1] for x in usable if x['num'] in decbase]); dec_avg=np.mean(list(decbase.values()))
        print('  MATCHED NON-HAIRPIN DECOY: n',len(decbase),'mean',format(dec_avg,'.6f'),'obs_same_subset',format(obs_dec,'.6f'), 'delta',format(obs_dec-dec_avg,'.6f'))
    else:print('  MATCHED NON-HAIRPIN DECOY: UNLINKED')
    # Chain block resampling; each chain's full set of hairpins travels as a block.
    rngB=np.random.default_rng(196196); NB=2000
    obs_by={x['num']:x['rank'][1] for x in usable}
    bychain=collections.defaultdict(list)
    for x in usable:bychain[x['ci']].append(x['num'])
    ckeys=sorted(bychain)
    def block_ci(baseline):
        keys=[i for i in obs_by if baseline is None or i in baseline]
        keyed=collections.defaultdict(list)
        for ci in ckeys:
            for i in bychain[ci]:
                if i in keys:keyed[ci].append(obs_by[i]-(baseline[i] if baseline else 0.0))
        groups=[np.array(v,dtype=float) for v in keyed.values() if v]
        if len(groups)<2:return None  # no defensible chain-block interval from a single chain
        B=[]
        for rep in range(NB):
            indexes=rngB.integers(0,len(groups),size=len(groups))
            q=np.concatenate([groups[k] for k in indexes]);B.append(float(q.mean()))
        return np.mean(np.concatenate(groups)),np.quantile(B,[.025,.975]).tolist(),len(groups),sum(map(len,groups))
    for label,baseline in [('true advantage',None),('true minus shuffle',shbase),('true minus shifted',stbase),('true minus decoy',decbase)]:
        ci=block_ci(baseline)
        print('  CHAIN-BLOCK BOOTSTRAP',label,':',('mean %.6f 95%% CI [%.6f, %.6f], chains %d hairpins %d'%(ci[0],*ci[1],ci[2],ci[3])) if ci else 'UNLINKED (fewer than 2 independent chain blocks or missing paired values)')
    # Complete diagnostic per-hairpin ledger; including failures, not only hits.
    print('TRACE: 1 row for EVERY detected hairpin; D is signed exact-scale row-contrast sequence (h=3..8).')
    print('ID | chain | pdb | e,s,k,S | true_w | best_w | Q/60480 | D3..8 | stable,flip | rank,adv,nwin | shuffle_mean | shift_mean | decoy_S,decoy_adv | window [S:Q] | FAILURES')
    for x in results:
        ci,S=x['ci'],x['S'];ent=original[ci];pdb=ent.get('pdb',ent.get('acc','NA'))
        win=[str(i)+':'+str(bests[ci][i][2]) for i in range(S-8,S+9) if i in bests[ci]]
        rankval=('UNLINKED' if x['rank'] is None else ('%.1f,%.5f,%d'%x['rank']))
        dav='UNLINKED' if x['decoy_rank'] is None else format(x['decoy_rank'][1],'.5f')
        hm=lambda d: 'UNLINKED' if x['num'] not in d else format(d[x['num']],'.5f')
        print('%03d | %3d | %s | %d,%d,%d,%d | %s | %s | %s | %s | %s,%s | %s | %s | %s | %s,%s | [%s] | %s'%(
            x['num'],ci,pdb,x['e'],x['s'],x['k'],S,x['width_true'],x['w_pred'],x['Q'],
            x['D'],x['persist'],x['flip'],rankval,hm(shbase),hm(stbase),x['decoy_S'],dav,','.join(win),
            ';'.join(x['failures']) if x['failures'] else 'NONE'))
    print('ALL FAILURES (no suppression):')
    for x in results:
        if x['failures']:print('  HP %03d: %s'%(x['num'],'; '.join(x['failures'])))
    print('LEDGER: STANDS binary pair/address identities and geometric non-identifiability; '
          'RUNS toy exact score and all observed tests above; DEAD END retained §195 value mirror; '
          'OPEN physical face without nonlocal geometry and sequence-only centre unless controls separate.')

```

## 196.9 Complete saved output of the execution with the supplied attachments

This is the **complete stdout of the current run**. There are no per-hairpin rows because the original structure/sequence source is UNLINKED; no fabricated 143-row table is substituted. With the original data, the same cell prints Stage A seal, Stage B structural read-back, all three controls, chain-block uncertainty, all per-hairpin traces, all failures and the ledger.

```text
NEXUS §196   SEQUENCE FACE COHERENCE / LOCAL PLANE NON-IDENTIFIABILITY
AUTHOR Dean A. Kulik | QuHarmonics Research Group | ORCID 0009-0003-3128-8828
RULE SHA-256 d98925c95f2b01c4818eb7894f91e80ce01a84146642fcf2df69b4e79530ff9a
SCORE UNIT Q/60480, with D_h = 1440 * Delta_h (integer)
STANDS/RUNS ADDRESS: (f,delta) inverse n=2,3,4,6; off-diagonal P(i||J(j))=j||J(i), diagonal -> C(i)||J(C(i)) on n=4: PASS
OPS KEEP SEPARATE: transposition (i,j)->(j,i); parity t&1; value b=1[WET>0]; orientation sign[n_sheet dot (CB-CA)] UNLINKED until geometry
RUNS TOY 70-residue planted alternating arms, e=22 s=27 width=5: Q= 60480 /60480; D3..8= (-10080, -10080, -10080, -10080, -10080, -10080) ; persistence= (6, 0)
RUNS FAILURE homogeneous A*70: all 101 candidate centres have Q=0; no centre is identifiable
RUNS FAILURE repeating AR*35: global max Q= 60480 shared by 50 distinct centres (first 12: [20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42] )
STANDS GEOMETRY: same N CA C CB and nonzero handed volume 2.494784;
  counterexample I: tangent [1.0, 0.0, 0.0] across [0.0, 1.0, 0.0] normal [0.0, 0.0, 1.0] n.CB = -1.205
  counterexample II: same local atoms, across [0.0, 0.0, -1.0] normal [-0.0, 1.0, 0.0] n.CB = 0.780
  sheet normals orthogonal, side-chain face sign reverses; local tetrahedron cannot choose sheet plane.
  required geometric link: independent cross-strand vector plus strand tangent; solvent/burial requires surrounding occupancy.
OPEN DATA UNLINKED: ecoli_chains.json / original NEXUS_Fold_Compiler_Notebook (2).zip not supplied.
NO 143-HAIRPIN SCORES OR RANKS CLAIMED. No invented data, controls, or per-hairpin outcomes.
RUN COMMAND: set NEXUS_DATA to the original JSON or ZIP path, then run this unchanged single cell.
```

## 196.10 STANDS / RUNS / OPEN / DEAD END ledger

| Object and readout | Status | Exact boundary |
|---|---|---|
| Residue-address transposition on off-diagonal pair words; complement branch on the diagonal | **STANDS**; **RUNS** exhaustive $n=4$ pair-square check | The ring identity is not itself an observed hydrogen bond. |
| Invertible $(f,\delta)$ split, complement face-only, local row parity kept distinct | **STANDS**; **RUNS** widths 2, 3, 4, 6 | No physical sheet sign assigned in sequence stage. |
| $Q(S,w)$ exact face-coherence score, widths 3–8, prefixes 3–8 | **RUNS** on sequence unit tests; rule **SEALED** | An executable readout, not an observed true-centre success. |
| Planted nine-row alternating-arm contrast | **RUNS** | $Q=60480$, six of six signed prefixes agree. |
| Homogeneous-sequence centre | **DEAD END** for this reader | 101 evaluable centres all score zero. |
| Repeating alternating sequence as unique crease address | **DEAD END** | 50 centres share perfect coherence; location remains AMBIGUOUS. |
| Determining an oriented sheet plane from one local N–Cα–C–Cβ fragment | **DEAD END**; constructive counterexample **STANDS** | Identical covalent atoms allow distinct normals with opposite Cβ projections. |
| Independent cross-strand displacement and strand tangent as geometric provider of an unoriented plane | **STANDS** in nondegenerate Euclidean geometry | Absolute burial still requires environment. |
| §195 equality of mirrored sequence values as crease predictor | **DEAD END** (record) | 10/143 first, mean advantage 0.5299; not rerun here. |
| §195 structural face correspondence and burial tallies | **RUNS** (supplied historical audit) | 801/822, 1,370/1,404 and 112/141 conditional on physical sheet normal. |
| §196 actual scores for the 143 E. coli hairpins, null comparisons and chain-block confidence intervals | **OPEN — DATA UNLINKED** | Original `ecoli_chains.json` / compiler ZIP absent. No invented P values, seals or trace rows. |
| Sequence-only arm registration and a unique crease address | **OPEN — missing dependency** | A coherent face-periodic value channel does not by itself select an address. |

## 196.11 Next precise prompt — §197

> Continue NEXUS from §196 using the **unchanged sealed face-coherence rule**, SHA-256 `d98925c95f2b01c4818eb7894f91e80ce01a84146642fcf2df69b4e79530ff9a`. Link the **original** `ecoli_chains.json` or its named compiler ZIP; do not replace missing entries or select a new protein corpus. Run Stage A on sequence alone, print the complete score seal, and only then compute the §188 observed hairpins. Require the historical 143 count or report the detector/source mismatch. Print **all** per-hairpin traces, 200 composition-shuffle nulls, 200 parity-matched shifted-centre nulls, composition-matched detector-negative decoys, and chain-block bootstrap intervals, including every exclusion, tie and failure. Keep the value score's sign unassigned to a physical face until after the structure is read.
>
> If face coherence does not outrank its controls, **do not tune the score**. Resolve the compiler dependency: which earlier sequence-accessible operation, if any, supplies *opposite-arm registration* rather than just alternating face value? Derive its required input/output type and its inverse/way home in the same binary address base; identify the owner as **BOUND**, **AMBIGUOUS** or **UNBOUND**. Preserve the local N–Cα–C–Cβ counterexamples: covalent chirality is not a sheet normal. Seal any genuinely new WHAT and its independent readout **before** structural labels. If no provider exists in the present chain, mark the specific missing link **OPEN**. Do not invent a bit, fit an energy, choose a global phase, or search candidate rules until one happens to land.

**§196 ends with one sharp separation:** the exact mirror and address transposition belong to the shape operator; sequence slot density can identify coherent *alternating contrast*; physical orientation requires a second geometric direction. The only sequence-only crease claim left to test is whether that contrast supplies a sufficiently unique address against the sealed controls. The original data has not yet been linked, so the ledger leaves that claim OPEN.
