# NEXUS §196 — The face-coherence reader and the missing sheet plane

**Dean A. Kulik · QuHarmonics Research Group · ORCID 0009-0003-3128-8828**  
**30 October 2026 · Continuation of the running audit, §195**  
**Status: DATA LINKED · COMPLETE RE-EXECUTION.** The §196 sequence-coherence rule was sealed before the original experimental hairpin locations were read. The v2 ring ISA provenance takes precedence over v1: the frame lemma, centre nesting and ℓ(n) are recovered from the prior record; the §195 additions were the step-mirror channel split and one-transposition seam step. The parallel v2 ring section also bears the number §196; this document is the sequence-face-coherence companion, not a renumbering of the ring work.

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

The sequence algorithm was executed on exact synthetic controls **and** subsequently on the original 160-chain E. coli corpus; its original synthetic witnesses are:

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

## 196.7 DATA LINKED — the empirical landing, with all failures

The corrected Google Drive mount supplied the **original** `QUHarmonics/Json Artifacts/ecoli_chains.json` (160 chains; 19,329 amino-acid records) and `ecoli_water.json`. Only the chain file was used for sequence scoring and for the structural hairpin read-back. The water file was deliberately **not** opened by the scoring cell. Source identity is sealed by raw SHA-256:

`f5266a447a4342955936966ff46df15823da5c55508540d78f316bf3f4d2e145`

The rule remains exactly the one sealed in the previous UNLINKED draft, including the fixed nine-row aperture, widths 3–8, score normalization and control designs:

- **Rule SHA-256:** `d98925c95f2b01c4818eb7894f91e80ce01a84146642fcf2df69b4e79530ff9a`.
- **Stage A, sequence-only score-ledger SHA-256:** `ef20a128123d1e20460a0821865f4f162799e76f84f41e9be2859b247750758c`.
- Stage A constructed **95,496** `(S,w,Q,D₃…D₈)` rows and **32,464** best-centre scores, then sealed them *before executing any coordinate-based hairpin detector*.
- Stage B reproduced **143** structure-detected hairpins, **49** with even `S`, from the unchanged §188 nearest N–O detector.

| Reading | Executed result |
|---|---:|
| True centres with all nine rows in at least one legal width | **132 / 143** |
| No valid true-centre score (UNLINKED, not assigned zero) | **11 / 143** |
| True centres uniquely ranked first in ±8 | **12 / 132** |
| True centres ranked within top three | **38 / 132** |
| Mean normalized rank advantage, valid centres | **0.634060** |
| Chain-composition shuffle null, 200 repeats | **0.498424**; SD 0.024366; difference +0.135636; empirical p 0.00498 |
| Same-parity shifted-centre null, 200 repeats | **0.513876**; SD 0.021895; difference +0.120183; empirical p 0.00498 |
| Matched detector-negative composition decoys | **0.475469**; paired difference +0.158591 |
| Chain-block bootstrap, 88 chains, 2,000 replicates | observed advantage 95% interval **[0.580149, 0.680745]** |
| Bootstrap on difference from shuffles | **[0.085370, 0.181190]** |
| Bootstrap on difference from shifted centres | **[0.074031, 0.163233]** |
| Bootstrap on difference from matched decoys | **[0.100506, 0.217230]** |

The mean centre rank is separated from all three controls under this fixed reader, including a full-chain resampling interval above zero for each paired difference. **This is a RUNS sequence-only preference for *candidate-centre rank*, not a solved crease-address compiler.** Only 12 of 132 evaluable true centres land uniquely first. The signal is distributed: a true centre can be enriched relative to controls without being the top address in its local 17-centre window.

**Failures, not edited out:** 11/143 true centres cannot be evaluated by the predetermined nine-row requirement; 94/132 evaluable centres are outside the top three; 120/132 are not uniquely first; 78/132 sequence-selected best widths disagree with the structure-derived inner-pair width; 7/143 trace rows reverse the signed contrast at some prefix; no detected true score was zero. The full ledger below prints **each individual failure and every candidate in its ±8 window**. True-centre width labels and observed locations were not used to choose the winning width in Stage A. The control p-values have a resolution floor of 1/201; they are not claims about untested datasets.

The score engine was optimized **after** discovering that the 200 full shuffled-sequence rounds exceeded the execution limit. The vectorized engine uses precisely the same integer formula; explicit equivalence checks against the original reference implementation passed on four independent test strings. **The rule and its prior rule SHA-256 did not change.** The original reference scorer still produces the sealed Stage A dataset ledger; only shuffled-control execution uses the equivalent vectorized route. Both changes and the initial timeout are logged here.

## 196.8 Full runnable *single Jupyter cell* — sequence score, controls, geometry and slip read-back

Run the entire Python block below as one Jupyter cell. Python 3 and NumPy only. The original `ecoli_chains.json` must be local (alongside the notebook, in `/mnt/data` or at `NEXUS_DATA`), or the original ZIP can be supplied; files read from Google Drive must first be made available to the notebook's runtime. The source chain is read twice in a deliberately ordered manner: **first only amino-acid letters**, then after the complete score hash is printed, the structural N/O positions. This is a post-seal landing, not a fit.

The slip section is a **separate, ring-sealed diagnostic within the same cell**. It reads the same original chain JSON. Its TP/PT mapping has a different rule SHA-256 and a separate 41-event trace; it does not alter the face-coherence score. No water coordinates or physical plane normal are used in either prediction.

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

def score_sequence_fast(seq):
    """Vectorized scorer for null replicates; identical integer rule, no changed predictions."""
    v=np.fromiter((WET[a] for a in seq),dtype=np.int64,count=len(seq))
    L=len(v); best={}
    for w in range(3,9):
        e=np.arange(MAX_H,L-w-MAX_H,dtype=np.int64)
        if not len(e): continue
        s=e+w
        rows=np.stack([v[e-t]+v[s+t] for t in range(MAX_H+1)])
        even=np.zeros(len(e),dtype=np.int64); odd=np.zeros(len(e),dtype=np.int64)
        ec=oc=0; ds=[]
        for h in range(MAX_H+1):
            if h%2==0:even+=rows[h];ec+=1
            else:odd+=rows[h];oc+=1
            if h>=3:
                denom=2*ec*oc
                ds.append((even*oc-odd*ec)*(1440//denom))
        D=np.stack(ds).T; Q=np.abs(D.sum(axis=1)); S=2*e+w
        for j in range(len(e)):
            ss=int(S[j]); qq=int(Q[j]);
            if ss not in best or qq>best[ss][2] or (qq==best[ss][2] and w<best[ss][1]):
                best[ss]=(ss,w,qq,tuple(map(int,D[j])))
    return [],best

# Check the optimized route before linking structural outcomes or using it in controls.
for test_seq in ('AR'*35,'A'*70, 'GSPDNIVWYH'*10, 'ACDEFGHIKLMNPQRSTVWY'*6):
    assert score_sequence(test_seq)[1]==score_sequence_fast(test_seq)[1]
print('SCORE ENGINE equivalence: vectorized and reference rules identical on 4 independent inputs')

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
            _,b=score_sequence_fast(''.join(a));shuffled[ci]=b
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

# ----------------------------- §196 slip diagnostic, same Jupyter cell; independent ring rule.
import json, numpy as np, collections, hashlib
from pathlib import Path
RULE=('NEXUS slip/readback v1; ring address a in Z_2^n, P(a)=N-1-a, T(a)=a+1; '
      'S+1 pairs on sum N => TP=T o P, fixed {0,N/2}; '
      'S-1 pairs on sum N-2 => PT=P o T, fixed {N/2-1,N-1}; '
      'no intrinsic sign multiplicity predicted by two conjugate reflections; '
      'readback: original 188 nearest N to O detector, 193 emitted bonds v2, '
      'only D\\E in each hairpin window, classify stored i+j-S in {+1,-1}, '
      'one row per stored slip; source hash and all failures reported.')
print('RULE',RULE)
print('RULE SHA256',hashlib.sha256(RULE.encode()).hexdigest())
# Independence from any observed chain, test fixed sets for every tested width.
for n in range(2,15):
    N=1<<n
    P=lambda a:(N-1-a)%N
    T=lambda a:(a+1)%N
    tp=lambda a:T(P(a));pt=lambda a:P(T(a))
    assert [a for a in range(N) if tp(a)==a]==[0,N//2]
    assert [a for a in range(N) if pt(a)==a]==[N//2-1,N-1]
    assert all(tp(a)==T(pt((a-1)%N)) for a in range(N))
print('STANDS RING identity fixed point and conjugacy n=2..14 PASS')
print('WAY HOME dataset S=e+s observed from detector; classify missing bonds by (i+j-S) after generator readback')
raw=Path('/mnt/data/ecoli_chains.json').read_bytes()
print('DATA raw SHA256',hashlib.sha256(raw).hexdigest())
chs=json.loads(raw)
def closures(ent):
 r=ent['residues'];L=len(r);seq=[x[1] for x in r]; N=np.array([x[2] for x in r]); O=np.array([x[5] for x in r]);
 dd=np.linalg.norm(N[:,None,:]-O[None,:,:],axis=2); ix=np.arange(L);dd[np.abs(ix[:,None]-ix[None,:])<=2]=np.inf;out=set()
 for i in range(1,L):
  if seq[i]=='P':continue
  j=int(dd[i].argmin())
  if dd[i,j]<=3.5:out.add((i,j))
 return out
def hps(directed,L):
 und={(min(a,b),max(a,b)) for a,b in directed};byS=collections.defaultdict(list)
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
def zipv2(e,s,k):
 ret=s if s-e==3 else s-1
 out={(e,s),(ret,e)}
 for t in range(1,k+1):
  if t%2==0:out|={(e-t,s+t),(s+t,e-t)}
 return out
slips=[]; counts=collections.Counter();missingN=0
hpsall=[]
for ci,ent in enumerate(chs):
 R=ent['residues'];L=len(R)
 if L<30:continue
 D=closures(ent)
 for e,s,k,S in hps(D,L):
  hpsall.append((ci,e,s,k,S))
  stored={(i,j) for i,j in D if e-k<=i<=s+k and e-k<=j<=s+k}
  emitted=zipv2(e,s,k)
  for i,j in sorted(stored-emitted):
   offset=i+j-S
   counts[offset if abs(offset)<=1 else 'other']+=1
   missingN+=1
   if offset in (-1,1):
    slips.append({'chain':ci,'pdb':ent['pdb'],'e':e,'s':s,'k':k,'S':S,'donor':i,'acceptor':j,'sum':i+j,'offset':offset,'reflection':'TP' if offset==1 else 'PT',
       'row':None if not (min(e-k,s+k)<=i<=max(e,s)) else 'within_window'})
print('HAIRPINS',len(hpsall),'MISSING',missingN, 'OFFSETS',counts)
print('SLIPS',len(slips),'TP',sum(x['offset']==1 for x in slips),'PT',sum(x['offset']==-1 for x in slips))
print('TRACE CSV: ci,pdb,e,s,k,S,donor,acceptor,sum,delta,reflection')
for x in slips:
 print(','.join(str(x[v]) for v in ['chain','pdb','e','s','k','S','donor','acceptor','sum','offset','reflection']))
```

## 196.9 Complete observed stdout — stage order, statistics, 143 hairpin traces and 41 slips

The following is the verbatim saved stdout of the two executed sections, in exactly the order of the single cell above. Every candidate-window score and individual failure is printed. The full return includes all 143 hairpins (including 11 UNLINKED centres), not only selected successful cases.

```text
NEXUS §196   SEQUENCE FACE COHERENCE / LOCAL PLANE NON-IDENTIFIABILITY
AUTHOR Dean A. Kulik | QuHarmonics Research Group | ORCID 0009-0003-3128-8828
RULE SHA-256 d98925c95f2b01c4818eb7894f91e80ce01a84146642fcf2df69b4e79530ff9a
SCORE UNIT Q/60480, with D_h = 1440 * Delta_h (integer)
STANDS/RUNS ADDRESS: (f,delta) inverse n=2,3,4,6; off-diagonal P(i||J(j))=j||J(i), diagonal -> C(i)||J(C(i)) on n=4: PASS
OPS KEEP SEPARATE: transposition (i,j)->(j,i); parity t&1; value b=1[WET>0]; orientation sign[n_sheet dot (CB-CA)] UNLINKED until geometry
SCORE ENGINE equivalence: vectorized and reference rules identical on 4 independent inputs
RUNS TOY 70-residue planted alternating arms, e=22 s=27 width=5: Q= 60480 /60480; D3..8= (-10080, -10080, -10080, -10080, -10080, -10080) ; persistence= (6, 0)
RUNS FAILURE homogeneous A*70: all 101 candidate centres have Q=0; no centre is identifiable
RUNS FAILURE repeating AR*35: global max Q= 60480 shared by 50 distinct centres (first 12: [20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42] )
STANDS GEOMETRY: same N CA C CB and nonzero handed volume 2.494784;
  counterexample I: tangent [1.0, 0.0, 0.0] across [0.0, 1.0, 0.0] normal [0.0, 0.0, 1.0] n.CB = -1.205
  counterexample II: same local atoms, across [0.0, 0.0, -1.0] normal [-0.0, 1.0, 0.0] n.CB = 0.780
  sheet normals orthogonal, side-chain face sign reverses; local tetrahedron cannot choose sheet plane.
  required geometric link: independent cross-strand vector plus strand tangent; solvent/burial requires surrounding occupancy.
STAGE A ONLY-SEQUENCE DATA SOURCE ('json', '/mnt/data/ecoli_chains.json', None) raw SHA-256 f5266a447a4342955936966ff46df15823da5c55508540d78f316bf3f4d2e145 chains 160
STAGE A SCORES SEALED (BEFORE ANY COORDINATE-DERIVED LOCATIONS ARE COMPUTED)
  raw (S,w,Q,D3..8) candidate rows 95496 valid centre scores 32464 SHA-256 ef20a128123d1e20460a0821865f4f162799e76f84f41e9be2859b247750758c
STAGE B observed hairpins 143 (historical benchmark 143; report mismatch, do not force) even S 49
STAGE C TRUE SCORES: 132 of 143 evaluable; excluded 11
  TRUE  rank=1 12 top3 38 mean advantage 0.634060
  DIRECTION SIGN FLIPS 7 ZERO SCORES 0 WIDTH MISMATCH 78
  COMPOSITION SHUFFLE (200): n 132 null mean 0.498424 sd 0.024366 obs_same_subset 0.634060 delta 0.135636 P(null>=obs) 0.00498
  SHIFTED CENTRE same parity (200): n 132 null mean 0.513876 sd 0.021895 obs_same_subset 0.634060 delta 0.120183 P(null>=obs) 0.00498
  MATCHED NON-HAIRPIN DECOY: n 132 mean 0.475469 obs_same_subset 0.634060 delta 0.158591
  CHAIN-BLOCK BOOTSTRAP true advantage : mean 0.634060 95% CI [0.580149, 0.680745], chains 88 hairpins 132
  CHAIN-BLOCK BOOTSTRAP true minus shuffle : mean 0.135636 95% CI [0.085370, 0.181190], chains 88 hairpins 132
  CHAIN-BLOCK BOOTSTRAP true minus shifted : mean 0.120183 95% CI [0.074031, 0.163233], chains 88 hairpins 132
  CHAIN-BLOCK BOOTSTRAP true minus decoy : mean 0.158591 95% CI [0.100506, 0.217230], chains 88 hairpins 132
TRACE: 1 row for EVERY detected hairpin; D is signed exact-scale row-contrast sequence (h=3..8).
ID | chain | pdb | e,s,k,S | true_w | best_w | Q/60480 | D3..8 | stable,flip | rank,adv,nwin | shuffle_mean | shift_mean | decoy_S,decoy_adv | window [S:Q] | FAILURES
001 |   1 | 2F1F | 36,41,6,77 | 5 | 7 | 15528 | (-2880, -3480, -3840, -2700, -1440, -1188) | 6,0 | 5.0,0.75000,17 | 0.50562 | 0.67031 | 57,0.00000 | [69:10392,70:8040,71:4752,72:9168,73:7776,74:5880,75:8736,76:10152,77:15528,78:9480,79:20136,80:12600,81:18408,82:6600,83:19776,84:1632,85:18000] | TRUE_NOT_TOP3;TRUE_NOT_FIRST;BEST_WIDTH_DIFFERS
002 |   3 | 5WQV | 18,22,4,40 | 4 | 6 | 3624 | (-720, -1800, -480, 240, -360, -504) | 5,1 | 17.0,0.00000,17 | 0.53266 | 0.41219 | 22,0.27273 | [32:5304,33:23112,34:5544,35:21360,36:6624,37:20088,38:4776,39:22488,40:3624,41:17616,42:12624,43:14976,44:15216,45:10104,46:18240,47:3912,48:17544] | TRUE_NOT_TOP3;TRUE_NOT_FIRST;DELTA_SIGN_REVERSAL;BEST_WIDTH_DIFFERS
003 |   3 | 5WQV | 37,40,12,77 | 3 | 7 | 4152 | (360, -240, -960, -1800, -360, -1152) | 5,1 | 14.0,0.18750,17 | 0.48797 | 0.47719 | 95,0.25000 | [69:20280,70:11256,71:14592,72:13128,73:17424,74:10248,75:7608,76:4128,77:4152,78:8112,79:10656,80:11952,81:3840,82:14496,83:5064,84:13416,85:3984] | TRUE_NOT_TOP3;TRUE_NOT_FIRST;DELTA_SIGN_REVERSAL;BEST_WIDTH_DIFFERS
004 |   3 | 5WQV | 78,81,6,159 | 3 | 7 | 14424 | (2160, 3840, 2640, 2220, 1620, 1944) | 6,0 | 5.0,0.71429,15 | 0.53000 | 0.68885 | 135,0.12500 | [151:18048,152:14352,153:18408,154:12264,155:16704,156:9912,157:16056,158:9456,159:14424,160:6432,161:12312,162:2856,163:9480,164:1104,165:6888] | TRUE_NOT_TOP3;TRUE_NOT_FIRST;BEST_WIDTH_DIFFERS
005 |   4 | 7WW6 | 74,77,6,151 | 3 | 5 | 18984 | (4680, 3960, 3120, 2220, 2700, 2304) | 6,0 | 2.0,0.93750,17 | 0.53312 | 0.63094 | 131,1.00000 | [143:3840,144:7416,145:7152,146:3456,147:10920,148:10200,149:15936,150:6432,151:18984,152:3288,153:20328,154:3672,155:17520,156:6864,157:14856,158:2016,159:11664] | TRUE_NOT_FIRST;BEST_WIDTH_DIFFERS
006 |   7 | 1FS0 | 7,15,4,22 | 8 | 6 | 16104 | (3600, 3120, 2400, 3060, 2340, 1584) | 6,0 | 1.0,1.00000,12 | 0.45636 | 0.45630 | 128,0.93750 | [19:7944,20:13224,21:5496,22:16104,23:2592,24:12576,25:14064,26:7464,27:10536,28:4008,29:11424,30:9000] | BEST_WIDTH_DIFFERS
007 |   7 | 1FS0 | 26,29,4,55 | 3 | 3 | 22368 | (-4680, -4680, -4560, -3660, -2520, -2268) | 6,0 | 3.0,0.87500,17 | 0.50859 | 0.50156 | 73,0.25000 | [47:3048,48:24552,49:9264,50:18792,51:19776,52:12432,53:24456,54:1464,55:22368,56:6336,57:21288,58:10968,59:14208,60:12696,61:12480,62:15648,63:4248] | TRUE_NOT_FIRST
008 |   7 | 1FS0 | 53,57,6,110 | 4 | 6 | 13680 | (2520, 2280, 2880, 2400, 2160, 1440) | 6,0 | 6.0,0.68750,17 | 0.53859 | 0.60406 | 88,0.68750 | [102:5616,103:11544,104:8520,105:14112,106:8424,107:16344,108:13392,109:11952,110:13680,111:9816,112:17280,113:9456,114:16920,115:1296,116:16200,117:7680,118:7944] | TRUE_NOT_TOP3;TRUE_NOT_FIRST;BEST_WIDTH_DIFFERS
009 |   7 | 1FS0 | 71,74,6,145 | 3 | 3 | 24552 | (6480, 4320, 4320, 4140, 3060, 2232) | 6,0 | 2.0,0.93750,17 | 0.50781 | 0.56844 | 85,0.50000 | [137:7848,138:22056,139:7944,140:20328,141:13512,142:16656,143:19704,144:11904,145:24552,146:4992,147:22536,148:7728,149:22536,150:8880,151:25896,152:5520,153:21288] | TRUE_NOT_FIRST
010 |   9 | 1XEO | 111,115,6,226 | 4 | 8 | 34392 | (-7200, -7200, -6720, -5820, -4140, -3312) | 6,0 | 1.0,1.00000,17 | 0.47219 | 0.60500 | 198,0.12500 | [218:13680,219:13344,220:9840,221:14424,222:13152,223:16824,224:24360,225:3600,226:34392,227:7728,228:30432,229:11280,230:28800,231:22032,232:24168,233:20592,234:13368] | BEST_WIDTH_DIFFERS
011 |  10 | 1JKE | 12,20,11,32 | 8 | 4 | 25200 | (-5040, -5040, -5040, -4500, -3240, -2340) | 6,0 | 5.0,0.75000,17 | 0.48187 | 0.76247 | 154,0.62500 | [24:24120,25:17952,26:24312,27:11472,28:27600,29:7080,30:26304,31:2952,32:25200,33:3672,34:26904,35:8352,36:24888,37:16152,38:25632,39:18912,40:19200] | TRUE_NOT_TOP3;TRUE_NOT_FIRST;BEST_WIDTH_DIFFERS
012 |  10 | 1JKE | 56,60,3,116 | 4 | 4 | 19680 | (2880, 4200, 4080, 3480, 3060, 1980) | 6,0 | 7.0,0.62500,17 | 0.49609 | 0.69125 | 98,0.43750 | [108:18600,109:24528,110:21384,111:14424,112:19944,113:12864,114:19464,115:11664,116:19680,117:11232,118:22728,119:6024,120:25368,121:3576,122:24984,123:11640,124:18720] | TRUE_NOT_TOP3;TRUE_NOT_FIRST
013 |  11 | 4KEH | 146,154,4,300 | 8 | 8 | 15216 | (-4680, -3840, -1920, -1860, -1260, -1656) | 6,0 | 11.0,0.37500,17 | 0.52125 | 0.58729 | 280,0.50000 | [292:26760,293:7080,294:30000,295:3600,296:27168,297:14232,298:19320,299:19296,300:15216,301:14976,302:11184,303:16776,304:12696,305:20472,306:17112,307:24360,308:15528] | TRUE_NOT_TOP3;TRUE_NOT_FIRST
014 |  12 | 1ETO | 6,11,4,17 | 5 | None | None | None | None,None | UNLINKED | UNLINKED | UNLINKED | 35,0.56250 | [19:96,20:10944,21:5376,22:8544,23:6576,24:10176,25:10608] | NO_VALID_TRUE_SCORE
015 |  14 | 9H45 | 40,46,4,86 | 6 | 4 | 5616 | (1080, 840, 720, 1500, 1080, 396) | 6,0 | 6.0,0.68750,17 | 0.48641 | 0.72313 | 66,1.00000 | [78:5496,79:2712,80:7296,81:3528,82:6336,83:2808,84:4416,85:1584,86:5616,87:4536,88:9096,89:5304,90:7128,91:3912,92:7536,93:1680,94:5592] | TRUE_NOT_TOP3;TRUE_NOT_FIRST;BEST_WIDTH_DIFFERS
016 |  15 | 1OWF | 62,67,4,129 | 5 | 7 | 10608 | (1800, 2280, 1920, 2520, 1080, 1008) | 6,0 | 9.0,0.50000,17 | 0.51547 | 0.26359 | 147,0.68750 | [121:4608,122:8928,123:12096,124:7128,125:7560,126:14112,127:2520,128:14688,129:10608,130:11328,131:7560,132:12960,133:7320,134:12912,135:7632,136:13152,137:10872] | TRUE_NOT_TOP3;TRUE_NOT_FIRST;BEST_WIDTH_DIFFERS
017 |  16 | 1OWF | 61,66,4,127 | 5 | 7 | 21504 | (3960, 3000, 3840, 4260, 3600, 2844) | 6,0 | 1.0,1.00000,17 | 0.46984 | 0.51844 | 161,0.50000 | [119:7368,120:9696,121:2832,122:2976,123:3528,124:11184,125:11328,126:15384,127:21504,128:12024,129:20688,130:16944,131:15768,132:19176,133:18288,134:13176,135:20136] | BEST_WIDTH_DIFFERS
018 |  17 | 2HZA | 89,93,6,182 | 4 | 6 | 18264 | (4680, 3840, 3840, 2880, 1800, 1224) | 6,0 | 4.0,0.81250,17 | 0.53719 | 0.59625 | 200,0.87500 | [174:9984,175:8352,176:9624,177:6672,178:11496,179:5568,180:16464,181:6168,182:18264,183:11448,184:23544,185:9648,186:17904,187:19968,188:16344,189:19200,190:6576] | TRUE_NOT_TOP3;TRUE_NOT_FIRST;BEST_WIDTH_DIFFERS
019 |  19 | 4PYA | 67,72,8,139 | 5 | 5 | 42816 | (8640, 8160, 7440, 6300, 6120, 6156) | 6,0 | 2.0,0.93750,17 | 0.47609 | 0.75813 | 121,0.93750 | [131:17928,132:16752,133:27120,134:9384,135:33840,136:6480,137:40296,138:3792,139:42816,140:6720,141:43104,142:12552,143:35328,144:13848,145:30648,146:14232,147:24936] | TRUE_NOT_FIRST
020 |  20 | 6SYM | 82,85,8,167 | 3 | 7 | 24504 | (3960, 5280, 5520, 4200, 2880, 2664) | 6,0 | 2.0,0.93750,17 | 0.53469 | 0.68437 | 147,0.43750 | [159:18096,160:4992,161:23088,162:8832,163:17976,164:11232,165:20808,166:15600,167:24504,168:12768,169:27336,170:13320,171:21504,172:12552,173:14448,174:11328,175:11328] | TRUE_NOT_FIRST;BEST_WIDTH_DIFFERS
021 |  20 | 6SYM | 124,129,4,253 | 5 | None | None | None | None,None | UNLINKED | UNLINKED | UNLINKED | 235,0.75000 | [245:16800,246:9960,247:17328] | NO_VALID_TRUE_SCORE
022 |  23 | 5LS7 | 22,27,6,49 | 5 | 7 | 17640 | (5040, 3720, 2880, 2580, 2160, 1260) | 6,0 | 1.0,1.00000,17 | 0.49703 | 0.41719 | 27,0.62500 | [41:9576,42:11136,43:6096,44:10512,45:6816,46:11496,47:15696,48:7152,49:17640,50:12408,51:10440,52:15864,53:10440,54:6744,55:6936,56:7944,57:6192] | BEST_WIDTH_DIFFERS
023 |  24 | 2AU7 | 9,12,3,21 | 3 | 5 | 13536 | (3960, 2640, 1440, 1680, 1980, 1836) | 6,0 | 5.0,0.60000,11 | 0.46350 | 0.22420 | 39,0.25000 | [19:2856,20:7296,21:13536,22:17832,23:9936,24:14448,25:6120,26:15168,27:11544,28:19368,29:11832] | TRUE_NOT_TOP3;TRUE_NOT_FIRST;BEST_WIDTH_DIFFERS
024 |  24 | 2AU7 | 32,37,6,69 | 5 | 5 | 15192 | (2520, 3240, 3600, 2880, 1620, 1332) | 6,0 | 7.0,0.62500,17 | 0.51719 | 0.63500 | 87,0.37500 | [61:12600,62:19200,63:7032,64:13632,65:6912,66:12072,67:16752,68:8976,69:15192,70:5136,71:19464,72:3624,73:21624,74:3336,75:22512,76:7056,77:17832] | TRUE_NOT_TOP3;TRUE_NOT_FIRST
025 |  24 | 2AU7 | 94,97,6,191 | 3 | 7 | 6960 | (2520, 1320, 1680, 1080, 0, 360) | 5,0 | 11.0,0.37500,17 | 0.51797 | 0.24219 | 173,0.37500 | [183:10560,184:19512,185:6408,186:13200,187:5520,188:13152,189:2352,190:19032,191:6960,192:17136,193:11232,194:13968,195:4944,196:11640,197:3624,198:8400,199:6144] | TRUE_NOT_TOP3;TRUE_NOT_FIRST;BEST_WIDTH_DIFFERS
026 |  25 | 1JL1 | 23,26,8,49 | 3 | 5 | 15264 | (4320, 3240, 2880, 1800, 1620, 1404) | 6,0 | 8.0,0.56250,17 | 0.46813 | 0.64312 | 25,0.28571 | [41:22008,42:8712,43:18144,44:7608,45:13320,46:13128,47:3696,48:11328,49:15264,50:7920,51:21432,52:9168,53:21264,54:12408,55:25992,56:19800,57:19416] | TRUE_NOT_TOP3;TRUE_NOT_FIRST;BEST_WIDTH_DIFFERS
027 |  26 | 1HJR | 8,11,8,19 | 3 | 3 | 4440 | (-360, -960, -240, -540, -1440, -900) | 6,0 | 7.0,0.25000,9 | 0.36219 | 0.15142 | 85,0.00000 | [19:4440,20:16512,21:6024,22:14448,23:3960,24:17376,25:3360,26:18888,27:7752] | TRUE_NOT_TOP3;TRUE_NOT_FIRST
028 |  26 | 1HJR | 20,23,4,43 | 3 | 7 | 19200 | (2520, 2760, 3120, 3060, 3240, 4500) | 6,0 | 3.0,0.87500,17 | 0.51375 | 0.65094 | 61,0.37500 | [35:13128,36:17064,37:14928,38:12624,39:17304,40:13680,41:22752,42:10992,43:19200,44:10464,45:12216,46:1080,47:13248,48:9696,49:18528,50:8040,51:22248] | TRUE_NOT_FIRST;BEST_WIDTH_DIFFERS
029 |  27 | 3HVV | 5,8,4,13 | 3 | None | None | None | None,None | UNLINKED | UNLINKED | UNLINKED | 31,0.25000 | [19:13920,20:21096,21:13920] | NO_VALID_TRUE_SCORE
030 |  27 | 3HVV | 30,34,4,64 | 4 | 4 | 10176 | (-2880, -3240, -2640, -1020, -180, -216) | 6,0 | 4.0,0.81250,17 | 0.52109 | 0.47625 | 46,0.18750 | [56:9744,57:6144,58:4344,59:6384,60:2856,61:6672,62:9936,63:3792,64:10176,65:2808,66:13248,67:8088,68:2856,69:12840,70:5664,71:8712,72:11136] | TRUE_NOT_TOP3;TRUE_NOT_FIRST
031 |  29 | 1NU0 | 9,12,4,21 | 3 | 3 | 11904 | (2880, 1920, 1920, 1980, 1080, 2124) | 6,0 | 3.0,0.80000,11 | 0.44850 | 0.54476 | 151,0.75000 | [19:11040,20:7872,21:11904,22:11352,23:13152,24:10080,25:9696,26:3816,27:12648,28:3096,29:11784] | TRUE_NOT_FIRST
032 |  29 | 1NU0 | 19,24,4,43 | 5 | 5 | 19944 | (5400, 3600, 3600, 2700, 2160, 2484) | 6,0 | 3.0,0.87500,17 | 0.51906 | 0.38125 | 61,0.93750 | [35:16392,36:21864,37:17832,38:19128,39:14376,40:17688,41:21024,42:14736,43:19944,44:15912,45:17712,46:16200,47:7440,48:17280,49:2040,50:14280,51:7152] | TRUE_NOT_FIRST
033 |  30 | 1Q5X | 145,148,4,293 | 3 | 3 | 9696 | (2880, 3360, 960, 1020, 1080, 396) | 6,0 | 6.0,0.64286,15 | 0.52768 | 0.60650 | 29,0.25000 | [285:12264,286:10704,287:10464,288:9504,289:6144,290:10176,291:696,292:5064,293:9696,294:5184,295:8568,296:5976,297:7848,298:3096,299:11160] | TRUE_NOT_TOP3;TRUE_NOT_FIRST
034 |  32 | 4K4C | 104,112,6,216 | 8 | 8 | 14112 | (3240, 1680, 2160, 2640, 1980, 2412) | 6,0 | 5.0,0.75000,17 | 0.48906 | 0.68156 | 234,0.12500 | [208:22512,209:8232,210:22464,211:11448,212:17472,213:7320,214:14424,215:5208,216:14112,217:5592,218:7992,219:7392,220:13080,221:4080,222:9768,223:10776,224:9768] | TRUE_NOT_TOP3;TRUE_NOT_FIRST
035 |  37 | 1MJC | 56,59,4,115 | 3 | 5 | 5976 | (-1800, -960, -720, -660, -1080, -756) | 6,0 | 9.0,0.20000,11 | 0.47450 | 0.32289 | 97,0.68750 | [107:7464,108:10488,109:3888,110:15120,111:6936,112:20400,113:8568,114:18768,115:5976,116:12288,117:2016] | TRUE_NOT_TOP3;TRUE_NOT_FIRST;BEST_WIDTH_DIFFERS
036 |  38 | 8XYF | 54,57,4,111 | 3 | 5 | 7728 | (-1800, -1200, -1200, -1260, -1260, -1008) | 6,0 | 10.0,0.10000,11 | 0.47175 | 0.54652 | 81,0.50000 | [103:21120,104:9312,105:19608,106:19344,107:19320,108:26064,109:13800,110:25512,111:7728,112:13512,113:6072] | TRUE_NOT_TOP3;TRUE_NOT_FIRST;BEST_WIDTH_DIFFERS
037 |  40 | 3CCD | 34,37,4,71 | 3 | 5 | 20904 | (4320, 4800, 3360, 2700, 3060, 2664) | 6,0 | 1.0,1.00000,17 | 0.49969 | 0.60234 | 53,0.93750 | [63:6648,64:9768,65:4920,66:10848,67:12552,68:8880,69:17952,70:5640,71:20904,72:6000,73:19824,74:7440,75:19824,76:6720,77:16872,78:8592,79:15672] | BEST_WIDTH_DIFFERS
038 |  42 | 1R94 | 32,36,8,68 | 4 | 8 | 15456 | (1440, 3480, 3840, 2700, 1980, 2016) | 6,0 | 9.0,0.50000,17 | 0.51187 | 0.48531 | 46,0.37500 | [60:7608,61:15312,62:6096,63:20688,64:9384,65:24168,66:11016,67:20160,68:15456,69:19368,70:15816,71:14928,72:17760,73:8616,74:22248,75:1776,76:16008] | TRUE_NOT_TOP3;TRUE_NOT_FIRST;BEST_WIDTH_DIFFERS
039 |  42 | 1R94 | 56,59,6,115 | 3 | 5 | 15744 | (2880, 4320, 3120, 2580, 1800, 1044) | 6,0 | 3.0,0.87500,17 | 0.50219 | 0.47469 | 95,0.75000 | [107:9744,108:19176,109:1032,110:16968,111:6936,112:14208,113:13344,114:12768,115:15744,116:7056,117:13056,118:4416,119:14928,120:3336,121:13848,122:6144,123:6936] | TRUE_NOT_FIRST;BEST_WIDTH_DIFFERS
040 |  42 | 1R94 | 81,84,6,165 | 3 | 3 | 9984 | (720, 1440, 2400, 2760, 1800, 864) | 6,0 | 7.0,0.62500,17 | 0.51406 | 0.40067 | 147,0.68750 | [157:2664,158:8040,159:7368,160:9264,161:14088,162:8544,163:9696,164:10080,165:9984,166:11160,167:9384,168:10032,169:10824,170:13632,171:1416,172:4224,173:2256] | TRUE_NOT_TOP3;TRUE_NOT_FIRST
041 |  43 | 2DXA | 51,57,8,108 | 6 | 4 | 5856 | (1800, 840, 1200, 1260, 360, 396) | 6,0 | 12.0,0.31250,17 | 0.51234 | 0.35281 | 126,0.87500 | [100:13776,101:5424,102:12168,103:5496,104:5616,105:7056,106:936,107:10056,108:5856,109:13128,110:5064,111:19416,112:11352,113:16824,114:9960,115:16872,116:12432] | TRUE_NOT_TOP3;TRUE_NOT_FIRST;BEST_WIDTH_DIFFERS
042 |  43 | 2DXA | 129,134,4,263 | 5 | 5 | 26040 | (-5760, -5760, -4560, -4560, -3420, -1980) | 6,0 | 1.0,1.00000,17 | 0.49141 | 0.64469 | 245,0.18750 | [255:5232,256:5112,257:9912,258:8088,259:18024,260:8496,261:23520,262:4944,263:26040,264:6384,265:20136,266:8208,267:21264,268:12336,269:15768,270:13464,271:9624] | NONE
043 |  45 | 4HR7 | 43,46,4,89 | 3 | 3 | 13200 | (-1800, -2160, -1920, -1920, -2700, -2700) | 6,0 | 7.0,0.62500,17 | 0.50344 | 0.53187 | 71,0.43750 | [81:7608,82:6024,83:5880,84:9600,85:5208,86:11760,87:7560,88:17328,89:13200,90:19944,91:21384,92:12648,93:25152,94:12336,95:22680,96:11352,97:19680] | TRUE_NOT_TOP3;TRUE_NOT_FIRST
044 |  54 | 1F9Z | 33,38,4,71 | 5 | 3 | 4440 | (0, -600, -960, -1800, -720, -360) | 5,0 | 17.0,0.00000,17 | 0.53187 | 0.28781 | 49,0.00000 | [63:5088,64:13632,65:5832,66:11592,67:5952,68:11064,69:5520,70:12792,71:4440,72:9984,73:7872,74:15144,75:7800,76:11976,77:8592,78:12696,79:9912] | TRUE_NOT_TOP3;TRUE_NOT_FIRST;BEST_WIDTH_DIFFERS
045 |  54 | 1F9Z | 114,118,6,232 | 4 | 6 | 16944 | (4680, 3120, 1920, 2580, 2340, 2304) | 6,0 | 1.0,1.00000,12 | 0.48318 | 0.46346 | 104,0.31250 | [224:9264,225:12936,226:6144,227:8016,228:10536,229:9744,230:10656,231:8784,232:16944,233:8376,234:9144,235:15432] | BEST_WIDTH_DIFFERS
046 |  55 | 1MUL | 54,59,8,113 | 5 | 3 | 11136 | (-1440, -2400, -1680, -2160, -1800, -1656) | 6,0 | 13.0,0.25000,17 | 0.52938 | 0.24406 | 93,0.37500 | [105:9288,106:21360,107:2280,108:25344,109:5904,110:20856,111:8112,112:23064,113:11136,114:27168,115:12312,116:26976,117:14712,118:25056,119:16584,120:27816,121:14424] | TRUE_NOT_TOP3;TRUE_NOT_FIRST;BEST_WIDTH_DIFFERS
047 |  56 | 1DM9 | 54,57,6,111 | 3 | 5 | 20976 | (3960, 2520, 3360, 3540, 3960, 3636) | 6,0 | 6.0,0.68750,17 | 0.50531 | 0.64187 | 135,0.87500 | [103:21216,104:17064,105:21696,106:18144,107:19872,108:18072,109:17736,110:22200,111:20976,112:22272,113:26256,114:15384,115:17448,116:9960,117:10032,118:4296,119:6000] | TRUE_NOT_TOP3;TRUE_NOT_FIRST;BEST_WIDTH_DIFFERS
048 |  57 | 1XS0 | 43,46,4,89 | 3 | 3 | 6696 | (-2160, -1920, -720, -960, -540, -396) | 6,0 | 8.0,0.56250,17 | 0.47641 | 0.60797 | 71,0.12500 | [81:11832,82:5784,83:4632,84:9120,85:7344,86:8136,87:4248,88:5832,89:6696,90:4944,91:9096,92:1128,93:8208,94:7248,95:6576,96:4536,97:3360] | TRUE_NOT_TOP3;TRUE_NOT_FIRST
049 |  57 | 1XS0 | 55,62,6,117 | 7 | 3 | 5160 | (-360, -1680, -960, -1260, -720, -180) | 6,0 | 13.0,0.25000,17 | 0.51516 | 0.39609 | 19,0.50000 | [109:4536,110:12096,111:1752,112:15048,113:8472,114:8760,115:9240,116:11400,117:5160,118:10512,119:7752,120:13992,121:9960,122:9240,123:7680,124:3960,125:2880] | TRUE_NOT_TOP3;TRUE_NOT_FIRST;BEST_WIDTH_DIFFERS
050 |  57 | 1XS0 | 69,74,8,143 | 5 | 5 | 13824 | (3240, 1680, 2160, 3180, 1980, 1584) | 6,0 | 2.0,0.93750,17 | 0.55656 | 0.57531 | 21,0.60000 | [135:12288,136:5904,137:10800,138:5304,139:12240,140:3456,141:15240,142:4896,143:13824,144:7872,145:9144,146:5184,147:3504,148:5064,149:3936,150:1296,151:2616] | TRUE_NOT_FIRST
051 |  57 | 1XS0 | 83,88,6,171 | 5 | 5 | 7704 | (2880, 1680, 2160, 1020, 180, -216) | 5,1 | 9.0,0.50000,17 | 0.46891 | 0.23563 | 189,0.31250 | [163:4920,164:10512,165:3648,166:8472,167:3936,168:8880,169:7296,170:3288,171:7704,172:7848,173:5808,174:8928,175:3048,176:10944,177:5184,178:13944,179:7824] | TRUE_NOT_TOP3;TRUE_NOT_FIRST;DELTA_SIGN_REVERSAL
052 |  58 | 4P1M | 6,9,6,15 | 3 | None | None | None | None,None | UNLINKED | UNLINKED | UNLINKED | 33,0.43750 | [19:29112,20:3456,21:31584,22:8256,23:22896] | NO_VALID_TRUE_SCORE
053 |  60 | 9PME | 14,18,6,32 | 4 | 4 | 11928 | (1800, 2160, 2400, 2580, 1800, 1188) | 6,0 | 7.0,0.62500,17 | 0.46937 | 0.39224 | 50,0.37500 | [24:7680,25:14784,26:3552,27:7440,28:11952,29:4848,30:15840,31:6648,32:11928,33:16128,34:8304,35:10344,36:5448,37:16272,38:9576,39:16392,40:9528] | TRUE_NOT_TOP3;TRUE_NOT_FIRST
054 |  60 | 9PME | 53,60,4,113 | 7 | 5 | 15312 | (2880, 3120, 3120, 3240, 1800, 1152) | 6,0 | 2.0,0.93750,17 | 0.50578 | 0.50469 | 95,0.93750 | [105:7416,106:10776,107:3528,108:4080,109:6792,110:4080,111:11112,112:8400,113:15312,114:6624,115:20712,116:12024,117:13344,118:10824,119:12072,120:12912,121:10248] | TRUE_NOT_FIRST;BEST_WIDTH_DIFFERS
055 |  61 | 1MVF | 34,37,6,71 | 3 | None | None | None | None,None | UNLINKED | UNLINKED | UNLINKED | 51,0.06250 | [63:29160,64:3168,65:27840,66:288,67:27984] | NO_VALID_TRUE_SCORE
056 |  64 | 1QU9 | 21,24,4,45 | 3 | 7 | 14664 | (1800, 2760, 3120, 2160, 2340, 2484) | 6,0 | 6.0,0.68750,17 | 0.51313 | 0.64375 | 67,0.75000 | [37:10992,38:14784,39:8448,40:17880,41:14232,42:11904,43:17328,44:7488,45:14664,46:6216,47:13848,48:11616,49:12336,50:15144,51:15576,52:13512,53:14640] | TRUE_NOT_TOP3;TRUE_NOT_FIRST;BEST_WIDTH_DIFFERS
057 |  65 | 2OUG | 37,40,8,77 | 3 | 3 | 9864 | (-1080, -2160, -2160, -1800, -1080, -1584) | 6,0 | 14.0,0.18750,17 | 0.49812 | 0.35000 | 57,0.81250 | [69:4872,70:18600,71:5688,72:18120,73:12768,74:10368,75:16488,76:17280,77:9864,78:13176,79:14928,80:15720,81:8976,82:16296,83:12576,84:15576,85:11544] | TRUE_NOT_TOP3;TRUE_NOT_FIRST
058 |  66 | 1UMU | 58,61,6,119 | 3 | 3 | 12336 | (2880, 2640, 1920, 2160, 1440, 1296) | 6,0 | 13.0,0.25000,17 | 0.53750 | 0.65469 | 137,0.75000 | [111:26784,112:12696,113:27144,114:8448,115:22176,116:7416,117:17616,118:11712,119:12336,120:13584,121:3384,122:20256,123:13152,124:22824,125:24792,126:18120,127:33312] | TRUE_NOT_TOP3;TRUE_NOT_FIRST
059 |  68 | 1QYN | 42,46,12,88 | 4 | 8 | 18096 | (720, 2640, 3360, 3600, 3960, 3816) | 6,0 | 6.0,0.68750,17 | 0.52203 | 0.40813 | 68,0.18750 | [80:19800,81:15720,82:15456,83:9624,84:15192,85:3192,86:15744,87:9024,88:18096,89:18576,90:11496,91:22248,92:14544,93:19008,94:14496,95:20208,96:16896] | TRUE_NOT_TOP3;TRUE_NOT_FIRST;BEST_WIDTH_DIFFERS
060 |  68 | 1QYN | 57,65,12,122 | 8 | 8 | 22032 | (-3240, -3480, -5040, -4260, -2880, -3132) | 6,0 | 3.0,0.87500,17 | 0.51313 | 0.68281 | 142,0.75000 | [114:14808,115:22728,116:18480,117:21000,118:19272,119:16704,120:18192,121:15264,122:22032,123:11880,124:21192,125:10080,126:22392,127:2976,128:15576,129:4512,130:9888] | TRUE_NOT_FIRST
061 |  69 | 1ESO | 13,16,8,29 | 3 | 7 | 27840 | (5040, 5280, 5280, 4500, 3960, 3780) | 6,0 | 1.0,1.00000,17 | 0.51516 | 0.67330 | 47,0.37500 | [21:15096,22:3264,23:17256,24:6696,25:20688,26:9696,27:27408,28:7896,29:27840,30:13032,31:21912,32:17664,33:18432,34:17640,35:16320,36:15120,37:13800] | BEST_WIDTH_DIFFERS
062 |  70 | 1QVC | 87,94,6,181 | 7 | 7 | 6768 | (360, 720, 1440, 720, 1980, 1548) | 6,0 | 14.0,0.18750,17 | 0.49734 | 0.20156 | 155,0.31250 | [173:17424,174:31752,175:16152,176:31824,177:11304,178:31632,179:13176,180:25872,181:6768,182:22584,183:2568,184:18384,185:5616,186:17256,187:5040,188:12072,189:6792] | TRUE_NOT_TOP3;TRUE_NOT_FIRST
063 |  71 | 4LW4 | 69,73,8,142 | 4 | 8 | 13728 | (1080, 2040, 1680, 3060, 2520, 3348) | 6,0 | 9.0,0.50000,17 | 0.54844 | 0.68875 | 164,0.00000 | [134:18840,135:2256,136:20352,137:7344,138:15072,139:7176,140:12168,141:6672,142:13728,143:11376,144:15696,145:14232,146:11856,147:14760,148:13656,149:16800,150:18528] | TRUE_NOT_TOP3;TRUE_NOT_FIRST;BEST_WIDTH_DIFFERS
064 |  73 | 7EYJ | 7,10,5,17 | 3 | None | None | None | None,None | UNLINKED | UNLINKED | UNLINKED | 57,0.12500 | [19:5688,20:3168,21:11232,22:3600,23:14304,24:6624,25:16344] | NO_VALID_TRUE_SCORE
065 |  73 | 7EYJ | 18,22,8,40 | 4 | 6 | 18552 | (4680, 3840, 3120, 2520, 2160, 2232) | 6,0 | 6.0,0.68750,17 | 0.50359 | 0.43312 | 58,0.81250 | [32:4008,33:22296,34:9840,35:20928,36:13872,37:20568,38:20064,39:15456,40:18552,41:13944,42:18984,43:13224,44:13056,45:7296,46:13296,47:7536,48:16632] | TRUE_NOT_TOP3;TRUE_NOT_FIRST;BEST_WIDTH_DIFFERS
066 |  74 | 4FXI | 64,69,4,133 | 5 | 7 | 5112 | (-720, -360, -1440, -1260, -1080, -252) | 6,0 | 12.0,0.31250,17 | 0.50687 | 0.43719 | 161,0.60000 | [125:8256,126:3672,127:8712,128:8232,129:8712,130:7272,131:7440,132:9792,133:5112,134:11664,135:2376,136:6432,137:2856,138:4272,139:8280,140:2496,141:7080] | TRUE_NOT_TOP3;TRUE_NOT_FIRST;BEST_WIDTH_DIFFERS
067 |  75 | 1QWI | 11,15,7,26 | 4 | 6 | 23352 | (4320, 4560, 4080, 4200, 3420, 2772) | 6,0 | 3.0,0.86667,16 | 0.54950 | 0.69792 | 44,0.18750 | [19:9360,20:22752,21:2256,22:30672,23:5664,24:30960,25:9624,26:23352,27:10032,28:19200,29:10536,30:12696,31:6696,32:8184,33:2376,34:11016] | TRUE_NOT_FIRST;BEST_WIDTH_DIFFERS
068 |  75 | 1QWI | 86,89,4,175 | 3 | 7 | 15528 | (2880, 2760, 3120, 2700, 1800, 2268) | 6,0 | 9.0,0.50000,17 | 0.51922 | 0.60875 | 153,0.81250 | [167:25320,168:10416,169:23736,170:13944,171:23976,172:15816,173:17256,174:16584,175:15528,176:17328,177:12792,178:16752,179:6624,180:14928,181:8784,182:7296,183:11376] | TRUE_NOT_TOP3;TRUE_NOT_FIRST;BEST_WIDTH_DIFFERS
069 |  76 | 1SLU | 54,59,6,113 | 5 | 5 | 4992 | (-2520, -2400, -480, 120, 540, -252) | 4,2 | 16.0,0.06250,17 | 0.50516 | 0.61000 | 177,0.81250 | [105:21792,106:9312,107:15504,108:12144,109:8904,110:10824,111:5304,112:10728,113:4992,114:3144,115:13752,116:6960,117:14376,118:11664,119:11904,120:13680,121:12408] | TRUE_NOT_TOP3;TRUE_NOT_FIRST;DELTA_SIGN_REVERSAL
070 |  78 | 5XU7 | 75,79,6,154 | 4 | 8 | 30744 | (6840, 6240, 5040, 4380, 4680, 3564) | 6,0 | 4.0,0.81250,17 | 0.49047 | 0.60437 | 172,0.56250 | [146:11136,147:15168,148:21768,149:17640,150:32448,151:14760,152:35568,153:19296,154:30744,155:22416,156:27864,157:30960,158:20496,159:25344,160:15768,161:20136,162:13608] | TRUE_NOT_TOP3;TRUE_NOT_FIRST;BEST_WIDTH_DIFFERS
071 |  78 | 5XU7 | 107,110,8,217 | 3 | 3 | 13776 | (1800, 2040, 2640, 2220, 2160, 2916) | 6,0 | 5.0,0.60000,11 | 0.50225 | 0.75202 | 197,0.18750 | [209:19512,210:2880,211:22104,212:3576,213:20256,214:1536,215:20760,216:9120,217:13776,218:5784,219:4152] | TRUE_NOT_TOP3;TRUE_NOT_FIRST
072 |  79 | 1TT8 | 78,85,8,163 | 7 | 7 | 7944 | (-4320, -1920, -480, -720, -540, 36) | 5,1 | 15.0,0.12500,17 | 0.50938 | 0.30438 | 181,0.56250 | [155:13056,156:25080,157:9960,158:19464,159:12984,160:13944,161:10608,162:14424,163:7944,164:13392,165:3912,166:15768,167:4680,168:17808,169:9720,170:22416,171:16104] | TRUE_NOT_TOP3;TRUE_NOT_FIRST;DELTA_SIGN_REVERSAL
073 |  79 | 1TT8 | 131,134,6,265 | 3 | 7 | 9624 | (720, 960, 960, 2340, 2700, 1944) | 6,0 | 14.0,0.18750,17 | 0.49219 | 0.51969 | 247,0.68750 | [257:10272,258:12768,259:3312,260:12360,261:4128,262:11952,263:11088,264:3096,265:9624,266:10392,267:13320,268:25008,269:22896,270:21480,271:23280,272:23088,273:25416] | TRUE_NOT_TOP3;TRUE_NOT_FIRST;BEST_WIDTH_DIFFERS
074 |  79 | 1TT8 | 143,146,8,289 | 3 | 3 | 16920 | (-3960, -3600, -4320, -2520, -1080, -1440) | 6,0 | 10.0,0.43750,17 | 0.52063 | 0.41993 | 209,0.68750 | [281:21600,282:7128,283:12912,284:9240,285:9240,286:14880,287:9456,288:18456,289:16920,290:22200,291:20712,292:24720,293:21240,294:25800,295:19008,296:27048,297:14856] | TRUE_NOT_TOP3;TRUE_NOT_FIRST
075 |  80 | 8IWI | 34,37,4,71 | 3 | 5 | 28008 | (-5040, -5280, -5760, -4440, -3780, -3708) | 6,0 | 2.0,0.93750,17 | 0.47563 | 0.72031 | 51,0.75000 | [63:17904,64:19320,65:24120,66:10488,67:23952,68:7968,69:26280,70:9696,71:28008,72:9264,73:29808,74:15456,75:26328,76:17256,77:19920,78:21288,79:13440] | TRUE_NOT_FIRST;BEST_WIDTH_DIFFERS
076 |  80 | 8IWI | 42,46,4,88 | 4 | 4 | 11040 | (-2160, -2520, -2640, -1560, -1620, -540) | 6,0 | 9.0,0.50000,17 | 0.52953 | 0.39594 | 54,0.62500 | [80:18480,81:7512,82:12720,83:7512,84:5040,85:11544,86:6336,87:8568,88:11040,89:11304,90:17496,91:11688,92:10872,93:12072,94:9912,95:13848,96:2280] | TRUE_NOT_TOP3;TRUE_NOT_FIRST
077 |  80 | 8IWI | 53,58,4,111 | 5 | 5 | 9552 | (3600, 1560, 1680, 1740, 900, 72) | 6,0 | 5.0,0.75000,17 | 0.47500 | 0.64250 | 53,0.50000 | [103:6072,104:6960,105:14040,106:7632,107:9432,108:5592,109:12672,110:7920,111:9552,112:6480,113:288,114:6816,115:9456,116:8136,117:14664,118:6408,119:10224] | TRUE_NOT_TOP3;TRUE_NOT_FIRST
078 |  80 | 8IWI | 63,66,4,129 | 3 | 7 | 21096 | (-4320, -3960, -2880, -3240, -3960, -2736) | 6,0 | 2.0,0.93750,17 | 0.51250 | 0.68469 | 169,0.87500 | [121:15264,122:5736,123:12432,124:1440,125:14400,126:1104,127:14976,128:5592,129:21096,130:6240,131:20520,132:12936,133:17472,134:17736,135:15528,136:21600,137:10608] | TRUE_NOT_FIRST;BEST_WIDTH_DIFFERS
079 |  80 | 8IWI | 73,76,4,149 | 3 | 3 | 13656 | (3240, 3600, 1680, 960, 1800, 2376) | 6,0 | 8.0,0.56250,17 | 0.50516 | 0.49594 | 167,0.43750 | [141:5976,142:8496,143:2184,144:9864,145:5016,146:9768,147:9696,148:9144,149:13656,150:13824,151:13680,152:16416,153:16272,154:13320,155:18336,156:15192,157:23016] | TRUE_NOT_TOP3;TRUE_NOT_FIRST
080 |  84 | 1FM0 | 121,124,4,245 | 3 | 7 | 10608 | (-360, -2160, -1920, -1920, -2340, -1908) | 6,0 | 10.0,0.43750,17 | 0.50156 | 0.51656 | 263,0.75000 | [237:23040,238:6984,239:21816,240:3480,241:18312,242:2784,243:15864,244:7608,245:10608,246:7152,247:12432,248:14976,249:13776,250:23112,251:4296,252:28824,253:6144] | TRUE_NOT_TOP3;TRUE_NOT_FIRST;BEST_WIDTH_DIFFERS
081 |  86 | 1RYA | 37,41,4,78 | 4 | 4 | 15120 | (4320, 1920, 2880, 1680, 2160, 2160) | 6,0 | 6.0,0.68750,17 | 0.48078 | 0.56281 | 98,0.12500 | [70:19800,71:8184,72:23760,73:8352,74:16248,75:5376,76:15888,77:7272,78:15120,79:6504,80:5880,81:14424,82:6120,83:9576,84:11760,85:7584,86:19200] | TRUE_NOT_TOP3;TRUE_NOT_FIRST
082 |  87 | 1X8D | 45,50,4,95 | 5 | 5 | 14880 | (2880, 2400, 1680, 2880, 2520, 2520) | 6,0 | 6.0,0.68750,17 | 0.46422 | 0.70625 | 73,0.37500 | [87:6744,88:6696,89:8112,90:2736,91:9336,92:5424,93:13008,94:12912,95:14880,96:5352,97:19440,98:5016,99:22992,100:13320,101:18168,102:17136,103:15408] | TRUE_NOT_TOP3;TRUE_NOT_FIRST
083 |  88 | 4QAK | 78,83,4,161 | 5 | 3 | 7848 | (2880, 1440, 720, 1260, 540, 1008) | 6,0 | 13.0,0.25000,17 | 0.51313 | 0.65094 | 143,0.00000 | [153:27168,154:13416,155:21480,156:8064,157:18528,158:6120,159:11280,160:9192,161:7848,162:9984,163:7752,164:11304,165:10680,166:4368,167:15888,168:6792,169:22800] | TRUE_NOT_TOP3;TRUE_NOT_FIRST;BEST_WIDTH_DIFFERS
084 |  88 | 4QAK | 154,157,6,311 | 3 | 3 | 8088 | (2880, 1560, 1920, 720, 360, 648) | 6,0 | 15.0,0.12500,17 | 0.47594 | 0.30160 | 293,0.31250 | [303:13440,304:36384,305:11880,306:32472,307:10800,308:26160,309:12408,310:21504,311:8088,312:13584,313:4800,314:18672,315:7056,316:14616,317:15672,318:23232,319:12960] | TRUE_NOT_TOP3;TRUE_NOT_FIRST
085 |  90 | 5LS7 | 41,49,6,90 | 8 | 4 | 11760 | (-2520, -1800, -2640, -1560, -1800, -1440) | 6,0 | 11.0,0.37500,17 | 0.50297 | 0.51375 | 72,0.06250 | [82:6432,83:28128,84:6792,85:26088,86:5760,87:23208,88:12648,89:18672,90:11760,91:15240,92:20352,93:9504,94:25824,95:6960,96:28440,97:6624,98:35928] | TRUE_NOT_TOP3;TRUE_NOT_FIRST;BEST_WIDTH_DIFFERS
086 |  90 | 5LS7 | 56,59,4,115 | 3 | 3 | 21552 | (3960, 5520, 4800, 3420, 2340, 1512) | 6,0 | 4.0,0.81250,17 | 0.47391 | 0.33687 | 141,0.62500 | [107:9696,108:10752,109:15336,110:9240,111:18456,112:11544,113:21048,114:18360,115:21552,116:21240,117:15552,118:27408,119:10392,120:31008,121:2832,122:32160,123:10104] | TRUE_NOT_TOP3;TRUE_NOT_FIRST
087 |  91 | 1U5W | 79,82,8,161 | 3 | 3 | 9288 | (720, 1440, 2160, 1260, 1620, 2088) | 6,0 | 13.5,0.21875,17 | 0.52891 | 0.35156 | 141,0.31250 | [153:4032,154:24432,155:1968,156:21240,157:9288,158:15792,159:7416,160:12552,161:9288,162:15792,163:10656,164:13272,165:14976,166:15624,167:19008,168:15600,169:15528] | TRUE_NOT_TOP3;TRUE_NOT_FIRST
088 |  91 | 1U5W | 91,94,6,185 | 3 | 5 | 24936 | (6120, 6240, 4800, 3240, 2520, 2016) | 6,0 | 2.0,0.93750,17 | 0.47641 | 0.33516 | 81,0.12500 | [177:4344,178:24888,179:10584,180:25656,181:14184,182:24000,183:18528,184:20400,185:24936,186:18600,187:18264,188:15408,189:11592,190:11592,191:8376,192:6912,193:10728] | TRUE_NOT_FIRST;BEST_WIDTH_DIFFERS
089 |  92 | 1OI4 | 43,48,4,91 | 5 | 3 | 24792 | (5040, 4800, 4080, 3780, 3420, 3672) | 6,0 | 1.0,1.00000,17 | 0.46813 | 0.71156 | 67,0.50000 | [83:24408,84:9840,85:22464,86:11664,87:21504,88:10824,89:24144,90:7800,91:24792,92:7584,93:21912,94:6360,95:19464,96:10392,97:16032,98:12648,99:8448] | BEST_WIDTH_DIFFERS
090 |  93 | 4MAK | 60,65,6,125 | 5 | 3 | 8496 | (-720, -1680, -2160, -2100, -1080, -756) | 6,0 | 4.5,0.56250,9 | 0.33844 | 0.42572 | 107,0.37500 | [117:3864,118:15840,119:7416,120:13248,121:8496,122:6360,123:15288,124:432,125:8496] | TRUE_NOT_TOP3;TRUE_NOT_FIRST;BEST_WIDTH_DIFFERS
091 |  95 | 3QMQ | 42,48,6,90 | 6 | 6 | 19632 | (3600, 3720, 3120, 3000, 3060, 3132) | 6,0 | 7.0,0.62500,17 | 0.49641 | 0.65063 | 48,0.31250 | [82:43608,83:6408,84:41568,85:9888,86:35136,87:9480,88:28392,89:6312,90:19632,91:4800,92:20712,93:9624,94:15768,95:14304,96:13056,97:21456,98:9336] | TRUE_NOT_TOP3;TRUE_NOT_FIRST
092 |  96 | 4NTK | 108,112,4,220 | 4 | None | None | None | None,None | UNLINKED | UNLINKED | UNLINKED | 92,0.50000 | [212:5520,213:7224,214:3000,215:6672,216:1200,217:3168,218:6840,219:3072] | NO_VALID_TRUE_SCORE
093 |  99 | 2A6Q | 30,34,4,64 | 4 | 4 | 14328 | (3960, 2280, 2160, 1860, 1620, 2448) | 6,0 | 6.0,0.68750,17 | 0.46672 | 0.37812 | 30,0.75000 | [56:10728,57:15528,58:11592,59:16392,60:13320,61:19584,62:8160,63:14424,64:14328,65:10224,66:8040,67:3936,68:7320,69:5376,70:13080,71:7272,72:15000] | TRUE_NOT_TOP3;TRUE_NOT_FIRST
094 | 101 | 1F3Z | 62,66,6,128 | 4 | 6 | 20784 | (4680, 3840, 3120, 3060, 2700, 3384) | 6,0 | 2.0,0.93750,17 | 0.45906 | 0.73313 | 110,0.50000 | [120:10872,121:3648,122:11664,123:3648,124:14904,125:6048,126:18624,127:4176,128:20784,129:4344,130:21744,131:5304,132:16824,133:4704,134:16272,135:4992,136:12744] | TRUE_NOT_FIRST;BEST_WIDTH_DIFFERS
095 | 103 | 5Z38 | 13,17,4,30 | 4 | 4 | 13320 | (-3960, -2760, -1440, -1740, -2340, -1080) | 6,0 | 4.0,0.81250,17 | 0.53250 | 0.51002 | 70,0.81250 | [22:5112,23:6552,24:15432,25:13872,26:12456,27:12312,28:14064,29:9312,30:13320,31:6480,32:9432,33:10584,34:2880,35:6120,36:7272,37:4272,38:5832] | TRUE_NOT_TOP3;TRUE_NOT_FIRST
096 | 103 | 5Z38 | 22,30,4,52 | 8 | 4 | 23832 | (4320, 3600, 3600, 4140, 4140, 4032) | 6,0 | 3.0,0.87500,17 | 0.52109 | 0.54844 | 72,0.93750 | [44:11208,45:15072,46:22080,47:4776,48:27720,49:7608,50:26352,51:10368,52:23832,53:19080,54:19152,55:17424,56:12336,57:23640,58:9696,59:16824,60:6168] | TRUE_NOT_FIRST;BEST_WIDTH_DIFFERS
097 | 104 | 5E1L | 12,17,4,29 | 5 | 5 | 21696 | (3600, 4440, 4800, 3960, 2700, 2196) | 6,0 | 3.0,0.87500,17 | 0.50594 | 0.66801 | 111,0.50000 | [21:14736,22:11616,23:19656,24:7200,25:21816,26:3384,27:22968,28:5448,29:21696,30:6384,31:17856,32:7728,33:11064,34:7464,35:9648,36:12360,37:3408] | TRUE_NOT_FIRST
098 | 104 | 5E1L | 22,26,4,48 | 4 | 4 | 22824 | (-4320, -3360, -5040, -4560, -3420, -2124) | 6,0 | 2.0,0.93750,17 | 0.49734 | 0.53156 | 66,0.12500 | [40:8184,41:11064,42:6384,43:14976,44:13752,45:11928,46:17664,47:7896,48:22824,49:5664,50:27744,51:5976,52:18624,53:16656,54:7848,55:13824,56:5376] | TRUE_NOT_FIRST
099 | 104 | 5E1L | 115,120,6,235 | 5 | 3 | 14760 | (2880, 3000, 3600, 2400, 1800, 1080) | 6,0 | 3.0,0.87500,17 | 0.48109 | 0.47437 | 217,0.68750 | [227:4752,228:12192,229:4416,230:13200,231:7176,232:12264,233:9648,234:13152,235:14760,236:8352,237:18960,238:10032,239:15312,240:8208,241:7992,242:6168,243:7272] | TRUE_NOT_FIRST;BEST_WIDTH_DIFFERS
100 | 104 | 5E1L | 127,135,4,262 | 8 | 6 | 6936 | (2520, 1680, 480, 960, 360, 936) | 6,0 | 15.0,0.12500,17 | 0.48984 | 0.41500 | 154,0.68750 | [254:13128,255:15816,256:10200,257:18000,258:3672,259:15480,260:10848,261:11568,262:6936,263:6600,264:10056,265:9168,266:10008,267:12288,268:8928,269:12360,270:11808] | TRUE_NOT_TOP3;TRUE_NOT_FIRST;BEST_WIDTH_DIFFERS
101 | 104 | 5E1L | 145,148,4,293 | 3 | 7 | 12912 | (-3600, -2640, -1200, -1620, -1800, -2052) | 6,0 | 6.0,0.68750,17 | 0.45359 | 0.20312 | 311,0.10000 | [285:3696,286:19560,287:1584,288:20400,289:3744,290:22560,291:10248,292:14712,293:12912,294:10920,295:8616,296:12096,297:5208,298:12240,299:11856,300:15336,301:7440] | TRUE_NOT_TOP3;TRUE_NOT_FIRST;BEST_WIDTH_DIFFERS
102 | 105 | 2FS2 | 99,107,8,206 | 8 | 8 | 26904 | (5040, 4920, 5280, 4320, 3600, 3744) | 6,0 | 4.0,0.81250,17 | 0.51078 | 0.77219 | 224,0.12500 | [198:18960,199:10488,200:18288,201:18096,202:22008,203:20016,204:27816,205:17304,206:26904,207:13176,208:28416,209:14088,210:30096,211:9288,212:26592,213:9984,214:17592] | TRUE_NOT_TOP3;TRUE_NOT_FIRST
103 | 106 | 1MZG | 59,63,8,122 | 4 | 8 | 28776 | (5400, 5040, 4560, 4920, 4680, 4176) | 6,0 | 4.0,0.81250,17 | 0.50344 | 0.82844 | 92,0.43750 | [114:24240,115:12048,116:23808,117:10248,118:25296,119:10320,120:24720,121:9672,122:28776,123:13800,124:30840,125:9912,126:29496,127:5712,128:32400,129:6600,130:26688] | TRUE_NOT_TOP3;TRUE_NOT_FIRST;BEST_WIDTH_DIFFERS
104 | 107 | 2G2N | 26,29,4,55 | 3 | 3 | 25224 | (-4320, -4680, -4800, -4440, -3600, -3384) | 6,0 | 4.0,0.81250,17 | 0.52391 | 0.65094 | 37,0.06250 | [47:23328,48:9432,49:29184,50:6456,51:31992,52:3048,53:27384,54:4728,55:25224,56:6384,57:24096,58:10080,59:19584,60:16224,61:9264,62:22248,63:2376] | TRUE_NOT_TOP3;TRUE_NOT_FIRST
105 | 109 | 2VB2 | 62,65,4,127 | 3 | 5 | 1656 | (-720, -480, 720, 480, 540, 1116) | 4,2 | 11.0,0.00000,11 | 0.43750 | 0.37265 | 109,0.31250 | [119:15984,120:20136,121:10176,122:19128,123:5328,124:15936,125:8064,126:9528,127:1656,128:7368,129:2184] | TRUE_NOT_TOP3;TRUE_NOT_FIRST;DELTA_SIGN_REVERSAL;BEST_WIDTH_DIFFERS
106 | 110 | 1NJK | 76,84,8,160 | 8 | 8 | 11688 | (1800, 960, 1920, 2040, 2520, 2448) | 6,0 | 9.0,0.50000,17 | 0.52687 | 0.31000 | 142,0.25000 | [152:4440,153:19344,154:6720,155:18936,156:12288,157:12576,158:16440,159:12384,160:11688,161:11064,162:11808,163:9648,164:10344,165:11088,166:7824,167:12768,168:6984] | TRUE_NOT_TOP3;TRUE_NOT_FIRST
107 | 111 | 1VH5 | 103,111,6,214 | 8 | 8 | 12888 | (1440, 1680, 2160, 2640, 1980, 2988) | 6,0 | 7.0,0.62500,17 | 0.49484 | 0.26469 | 232,0.87500 | [206:10728,207:24000,208:7488,209:19488,210:12600,211:12864,212:12264,213:5016,214:12888,215:6240,216:12960,217:14160,218:9240,219:14328,220:10824,221:17568,222:5736] | TRUE_NOT_TOP3;TRUE_NOT_FIRST
108 | 112 | 3O9X | 21,24,4,45 | 3 | 5 | 3408 | (0, 1200, 1200, 360, 360, 288) | 5,0 | 16.0,0.06250,17 | 0.48141 | 0.50469 | 27,0.78125 | [37:16920,38:27264,39:17136,40:19848,41:14112,42:11952,43:7872,44:8856,45:3408,46:3048,47:11424,48:11064,49:13152,50:12072,51:21912,52:17448,53:21336] | TRUE_NOT_TOP3;TRUE_NOT_FIRST;BEST_WIDTH_DIFFERS
109 | 113 | 3HI2 | 74,77,6,151 | 3 | 3 | 33960 | (-7920, -7200, -5280, -4560, -4500, -4500) | 6,0 | 1.0,1.00000,17 | 0.46047 | 0.64125 | 133,0.87500 | [143:12168,144:22656,145:10416,146:22656,147:20808,148:21288,149:27384,150:11928,151:33960,152:5928,153:29328,154:7224,155:27528,156:9816,157:20760,158:6768,159:16464] | NONE
110 | 113 | 3HI2 | 86,89,6,175 | 3 | None | None | None | None,None | UNLINKED | UNLINKED | UNLINKED | 111,0.43750 | [167:13032,168:15816,169:13680,170:18336,171:12144,172:17808,173:9840] | NO_VALID_TRUE_SCORE
111 | 114 | 4Q2U | 61,65,6,126 | 4 | 8 | 7392 | (-360, -1560, -1680, -1020, -1080, -1692) | 6,0 | 13.0,0.25000,17 | 0.48750 | 0.55406 | 92,0.81250 | [118:20088,119:9864,120:13440,121:4008,122:10344,123:6096,124:7032,125:7248,126:7392,127:14496,128:10632,129:15816,130:15960,131:15096,132:16440,133:16608,134:18144] | TRUE_NOT_TOP3;TRUE_NOT_FIRST;BEST_WIDTH_DIFFERS
112 | 114 | 4Q2U | 72,75,4,147 | 3 | 5 | 16440 | (-4320, -3000, -1920, -2160, -2520, -2520) | 6,0 | 3.0,0.87500,17 | 0.50266 | 0.57482 | 85,0.37500 | [139:20112,140:2112,141:19032,142:9360,143:15144,144:10392,145:15000,146:14088,147:16440,148:11616,149:14400,150:9192,151:9288,152:6384,153:7728,154:3984,155:4080] | TRUE_NOT_FIRST;BEST_WIDTH_DIFFERS
113 | 116 | 8K6G | 134,138,10,272 | 4 | 8 | 21816 | (2520, 3240, 3600, 3960, 4140, 4356) | 6,0 | 7.0,0.62500,17 | 0.48125 | 0.77875 | 250,0.06250 | [264:28992,265:10008,266:22464,267:10944,268:20064,269:8928,270:21288,271:2664,272:21816,273:9384,274:23256,275:6144,276:28464,277:3624,278:24696,279:5784,280:28656] | TRUE_NOT_TOP3;TRUE_NOT_FIRST;BEST_WIDTH_DIFFERS
114 | 118 | 1VSR | 20,27,3,47 | 7 | 5 | 23088 | (4320, 3960, 4560, 4020, 3420, 2808) | 6,0 | 4.0,0.81250,17 | 0.52547 | 0.52875 | 29,0.87500 | [39:20328,40:21480,41:27768,42:15672,43:29376,44:9312,45:31608,46:13992,47:23088,48:14352,49:13248,50:13584,51:7320,52:8952,53:7032,54:7944,55:10488] | TRUE_NOT_TOP3;TRUE_NOT_FIRST;BEST_WIDTH_DIFFERS
115 | 118 | 1VSR | 32,35,3,67 | 3 | 3 | 20736 | (3600, 3360, 2880, 3660, 3960, 3276) | 6,0 | 5.0,0.75000,17 | 0.46328 | 0.73578 | 85,0.12500 | [59:20760,60:12792,61:26040,62:14592,63:23928,64:20760,65:19608,66:20232,67:20736,68:17568,69:16296,70:12552,71:16848,72:10584,73:12384,74:3528,75:13512] | TRUE_NOT_TOP3;TRUE_NOT_FIRST
116 | 118 | 1VSR | 125,128,4,253 | 3 | None | None | None | None,None | UNLINKED | UNLINKED | UNLINKED | 235,0.81250 | [245:15504,246:792,247:7776] | NO_VALID_TRUE_SCORE
117 | 120 | 3A7L | 18,22,6,40 | 4 | 4 | 12888 | (4320, 2640, 2160, 2040, 900, 828) | 6,0 | 11.0,0.37500,17 | 0.47203 | 0.58250 | 22,0.09091 | [32:7368,33:20064,34:9864,35:13704,36:13368,37:5712,38:11424,39:3672,40:12888,41:10680,42:15936,43:13560,44:20304,45:14304,46:21888,47:18624,48:22848] | TRUE_NOT_TOP3;TRUE_NOT_FIRST
118 | 120 | 3A7L | 61,64,4,125 | 3 | 5 | 12432 | (2520, 2520, 1680, 1680, 2160, 1872) | 6,0 | 6.0,0.68750,17 | 0.51875 | 0.51156 | 147,0.75000 | [117:6504,118:9168,119:9264,120:8280,121:8976,122:7560,123:12792,124:10800,125:12432,126:11016,127:19992,128:8256,129:14952,130:13248,131:11472,132:13152,133:8616] | TRUE_NOT_TOP3;TRUE_NOT_FIRST;BEST_WIDTH_DIFFERS
119 | 121 | 4FYY | 123,126,6,249 | 3 | 3 | 23712 | (5760, 4200, 4080, 3840, 3060, 2772) | 6,0 | 2.0,0.93750,17 | 0.50266 | 0.44719 | 225,0.37500 | [241:8832,242:8040,243:5616,244:6336,245:11496,246:8112,247:20064,248:7632,249:23712,250:11280,251:22176,252:17472,253:21696,254:20712,255:18168,256:26112,257:11112] | TRUE_NOT_FIRST
120 | 121 | 4FYY | 131,136,4,267 | 5 | 3 | 17376 | (3960, 2760, 2640, 3300, 2880, 1836) | 6,0 | 4.0,0.78571,15 | 0.53089 | 0.37069 | 229,0.75000 | [259:5904,260:26616,261:7080,262:19656,263:11688,264:17664,265:14376,266:11568,267:17376,268:8328,269:16656,270:7272,271:13584,272:5136,273:5328] | TRUE_NOT_TOP3;TRUE_NOT_FIRST;BEST_WIDTH_DIFFERS
121 | 125 | 2H09 | 63,67,4,130 | 4 | 8 | 17568 | (2880, 3600, 2880, 2880, 2520, 2808) | 6,0 | 5.0,0.75000,17 | 0.50156 | 0.50500 | 102,0.50000 | [122:7344,123:10056,124:5544,125:12384,126:6648,127:12264,128:13368,129:8616,130:17568,131:6720,132:20448,133:11640,134:20568,135:14448,136:19128,137:22560,138:14688] | TRUE_NOT_TOP3;TRUE_NOT_FIRST;BEST_WIDTH_DIFFERS
122 | 129 | 9SV1 | 37,41,6,78 | 4 | 8 | 21432 | (3960, 3840, 3840, 3780, 2880, 3132) | 6,0 | 5.0,0.75000,17 | 0.51094 | 0.59344 | 96,0.06250 | [70:22992,71:7632,72:26472,73:4512,74:27984,75:10800,76:24504,77:12504,78:21432,79:17640,80:10104,81:14568,82:5424,83:9648,84:3840,85:6744,86:7944] | TRUE_NOT_TOP3;TRUE_NOT_FIRST;BEST_WIDTH_DIFFERS
123 | 130 | 3MPY | 34,38,4,72 | 4 | 8 | 15120 | (2880, 3600, 2880, 2880, 1800, 1080) | 6,0 | 9.0,0.50000,17 | 0.50234 | 0.30031 | 54,0.18750 | [64:11952,65:11688,66:8280,67:16320,68:3000,69:13608,70:6312,71:13800,72:15120,73:20688,74:13680,75:23088,76:15768,77:23088,78:16536,79:23856,80:16608] | TRUE_NOT_TOP3;TRUE_NOT_FIRST;BEST_WIDTH_DIFFERS
124 | 131 | 4MTD | 75,80,4,155 | 5 | 3 | 10896 | (3600, 1680, 1920, 1500, 1080, 1116) | 6,0 | 1.0,1.00000,17 | 0.51016 | 0.53156 | 137,0.25000 | [147:6696,148:3168,149:7368,150:8808,151:3744,152:10656,153:4416,154:7536,155:10896,156:4512,157:7776,158:3720,159:9288,160:5232,161:6696,162:4584,163:8520] | BEST_WIDTH_DIFFERS
125 | 131 | 4MTD | 99,104,4,203 | 5 | 5 | 4416 | (-720, -120, -480, -540, -1260, -1296) | 6,0 | 12.0,0.31250,17 | 0.48094 | 0.48750 | 221,0.12500 | [195:2736,196:3120,197:6216,198:4632,199:8328,200:7368,201:7464,202:6408,203:4416,204:4104,205:5736,206:3360,207:11880,208:7416,209:3912,210:9984,211:4824] | TRUE_NOT_TOP3;TRUE_NOT_FIRST
126 | 135 | 5YPP | 37,42,6,79 | 5 | 3 | 9120 | (2520, 1440, 1680, 780, 1260, 1440) | 6,0 | 12.0,0.31250,17 | 0.54578 | 0.24031 | 97,0.25000 | [71:13920,72:9672,73:13920,74:11280,75:9840,76:16200,77:5640,78:13968,79:9120,80:15480,81:4560,82:17568,83:5400,84:14544,85:8400,86:9840,87:8208] | TRUE_NOT_TOP3;TRUE_NOT_FIRST;BEST_WIDTH_DIFFERS
127 | 138 | 4DT4 | 102,106,6,208 | 4 | 6 | 6960 | (1440, 480, 960, 1740, 1080, 1260) | 6,0 | 4.0,0.81250,17 | 0.46797 | 0.43438 | 186,0.12500 | [200:6360,201:12360,202:7368,203:5664,204:6192,205:6552,206:5448,207:6216,208:6960,209:2616,210:10368,211:5256,212:5928,213:2832,214:2832,215:6288,216:6840] | TRUE_NOT_TOP3;TRUE_NOT_FIRST;BEST_WIDTH_DIFFERS
128 | 140 | 3BMB | 62,67,6,129 | 5 | 3 | 15360 | (-3600, -3720, -3360, -2160, -1260, -1260) | 6,0 | 10.0,0.43750,17 | 0.50438 | 0.27781 | 147,0.62500 | [121:9744,122:34056,123:8256,124:37608,125:9576,126:42816,127:8016,128:40968,129:15360,130:35688,131:16152,132:24744,133:16320,134:19296,135:9840,136:14784,137:4224] | TRUE_NOT_TOP3;TRUE_NOT_FIRST;BEST_WIDTH_DIFFERS
129 | 140 | 3BMB | 109,113,6,222 | 4 | 4 | 13920 | (-2160, -2760, -3360, -2760, -1620, -1260) | 6,0 | 3.5,0.84375,17 | 0.50000 | 0.46766 | 192,0.12500 | [214:5568,215:4224,216:5208,217:4560,218:7968,219:6024,220:8400,221:9000,222:13920,223:7320,224:15000,225:6240,226:13920,227:5544,228:10368,229:14280,230:4992] | TRUE_NOT_TOP3;TRUE_NOT_FIRST
130 | 142 | 4HF0 | 57,63,4,120 | 6 | 4 | 11136 | (3600, 2040, 2400, 2160, 540, 396) | 6,0 | 10.0,0.43750,17 | 0.50875 | 0.42812 | 102,0.37500 | [112:15672,113:21888,114:9432,115:17856,116:9072,117:14712,118:6720,119:10104,120:11136,121:8184,122:16176,123:9792,124:11976,125:16704,126:11256,127:16704,128:9456] | TRUE_NOT_TOP3;TRUE_NOT_FIRST;BEST_WIDTH_DIFFERS
131 | 143 | 2UYK | 21,24,4,45 | 3 | 7 | 13944 | (1800, 2760, 3120, 2160, 2340, 1764) | 6,0 | 5.0,0.75000,17 | 0.50469 | 0.66297 | 63,0.68750 | [37:14112,38:12096,39:11136,40:14760,41:14232,42:9216,43:17328,44:8208,45:13944,46:6216,47:11328,48:9096,49:8016,50:10824,51:8568,52:10512,53:6816] | TRUE_NOT_TOP3;TRUE_NOT_FIRST;BEST_WIDTH_DIFFERS
132 | 145 | 4XB6 | 52,57,4,109 | 5 | 7 | 25608 | (6840, 5760, 4560, 3120, 2880, 2448) | 6,0 | 4.0,0.81250,17 | 0.47594 | 0.27844 | 89,0.50000 | [101:10488,102:16224,103:12888,104:21552,105:15888,106:22032,107:21288,108:20424,109:25608,110:28344,111:17856,112:30624,113:15168,114:24624,115:5568,116:25704,117:2928] | TRUE_NOT_TOP3;TRUE_NOT_FIRST;BEST_WIDTH_DIFFERS
133 | 145 | 4XB6 | 73,77,8,150 | 4 | 6 | 17544 | (2520, 3480, 3120, 2880, 2700, 2844) | 6,0 | 7.0,0.62500,17 | 0.48656 | 0.65031 | 168,0.12500 | [142:22008,143:9144,144:7608,145:13464,146:3288,147:21720,148:10176,149:17376,150:17544,151:14712,152:24624,153:6120,154:25464,155:5640,156:28128,157:9312,158:25848] | TRUE_NOT_TOP3;TRUE_NOT_FIRST;BEST_WIDTH_DIFFERS
134 | 146 | 8VRG | 5,8,4,13 | 3 | None | None | None | None,None | UNLINKED | UNLINKED | UNLINKED | 31,0.43750 | [19:1296,20:3696,21:3888] | NO_VALID_TRUE_SCORE
135 | 148 | 1NP6 | 54,57,6,111 | 3 | 3 | 9960 | (2880, 2880, 1200, 1200, 1260, 540) | 6,0 | 3.0,0.87500,17 | 0.50469 | 0.24594 | 93,0.81250 | [103:5040,104:14304,105:5400,106:15624,107:2520,108:9144,109:3840,110:7416,111:9960,112:5832,113:2592,114:2472,115:1992,116:4488,117:3744,118:4368,119:8640] | TRUE_NOT_FIRST
136 | 150 | 6OD1 | 69,77,6,146 | 8 | 8 | 26064 | (3960, 5040, 5040, 4140, 4140, 3744) | 6,0 | 1.0,1.00000,17 | 0.55359 | 0.53312 | 128,0.37500 | [138:7632,139:17880,140:15408,141:14856,142:20712,143:10704,144:25464,145:6072,146:26064,147:9864,148:24768,149:13200,150:17544,151:18408,152:12936,153:19416,154:9264] | NONE
137 | 150 | 6OD1 | 98,101,4,199 | 3 | None | None | None | None,None | UNLINKED | UNLINKED | UNLINKED | 179,0.81250 | [191:10080] | NO_VALID_TRUE_SCORE
138 | 154 | 7N0J | 28,32,4,60 | 4 | 4 | 13200 | (3960, 2880, 1920, 1920, 900, 1620) | 6,0 | 10.0,0.43750,17 | 0.51203 | 0.31469 | 30,0.87500 | [52:7704,53:14016,54:4440,55:16008,56:4368,57:15240,58:8688,59:19008,60:13200,61:16488,62:15000,63:21888,64:7800,65:26568,66:8160,67:18480,68:11688] | TRUE_NOT_TOP3;TRUE_NOT_FIRST
139 | 154 | 7N0J | 37,42,4,79 | 5 | 7 | 4320 | (1800, 2040, 0, -780, 0, 1260) | 3,1 | 13.0,0.25000,17 | 0.53859 | 0.36406 | 97,0.12500 | [71:6984,72:3864,73:5328,74:3528,75:3888,76:5976,77:7440,78:7320,79:4320,80:12096,81:4344,82:12432,83:8736,84:12216,85:5856,86:12792,87:3336] | TRUE_NOT_TOP3;TRUE_NOT_FIRST;DELTA_SIGN_REVERSAL;BEST_WIDTH_DIFFERS
140 | 156 | 6KML | 62,65,7,127 | 3 | 3 | 22488 | (6120, 4080, 3360, 3240, 2880, 2808) | 6,0 | 3.0,0.87500,17 | 0.49016 | 0.74000 | 107,0.18750 | [119:11664,120:7296,121:17424,122:12696,123:17160,124:14592,125:22560,126:9552,127:22488,128:7248,129:19536,130:5160,131:23088,132:6504,133:15840,134:3816,135:17808] | TRUE_NOT_FIRST
141 | 156 | 6KML | 73,78,4,151 | 5 | 7 | 17712 | (-3600, -2640, -2880, -2940, -3240, -2412) | 6,0 | 2.0,0.93750,17 | 0.47531 | 0.58906 | 169,0.93750 | [143:11352,144:20376,145:11952,146:12024,147:15624,148:8256,149:17640,150:3912,151:17712,152:5256,153:17040,154:3336,155:14520,156:6576,157:14592,158:17016,159:11856] | TRUE_NOT_FIRST;BEST_WIDTH_DIFFERS
142 | 157 | 6HPC | 9,13,4,22 | 4 | 6 | 11328 | (-2880, -3240, -1920, -660, -1260, -1368) | 6,0 | 5.0,0.63636,12 | 0.46523 | 0.58493 | 40,0.96875 | [19:4560,20:10968,21:10920,22:11328,23:7608,24:11640,25:9936,26:14424,27:9624,28:12960,29:14136,30:8448] | TRUE_NOT_TOP3;TRUE_NOT_FIRST;BEST_WIDTH_DIFFERS
143 | 159 | 1NAQ | 45,48,6,93 | 3 | 5 | 14016 | (-2880, -2400, -1680, -2520, -2160, -2376) | 6,0 | 8.0,0.56250,17 | 0.49859 | 0.45312 | 111,0.06250 | [85:10392,86:19464,87:13056,88:14424,89:17016,90:13368,91:14424,92:8256,93:14016,94:9168,95:10416,96:10056,97:14904,98:14448,99:8304,100:19848,101:4776] | TRUE_NOT_TOP3;TRUE_NOT_FIRST;BEST_WIDTH_DIFFERS
ALL FAILURES (no suppression):
  HP 001: TRUE_NOT_TOP3; TRUE_NOT_FIRST; BEST_WIDTH_DIFFERS
  HP 002: TRUE_NOT_TOP3; TRUE_NOT_FIRST; DELTA_SIGN_REVERSAL; BEST_WIDTH_DIFFERS
  HP 003: TRUE_NOT_TOP3; TRUE_NOT_FIRST; DELTA_SIGN_REVERSAL; BEST_WIDTH_DIFFERS
  HP 004: TRUE_NOT_TOP3; TRUE_NOT_FIRST; BEST_WIDTH_DIFFERS
  HP 005: TRUE_NOT_FIRST; BEST_WIDTH_DIFFERS
  HP 006: BEST_WIDTH_DIFFERS
  HP 007: TRUE_NOT_FIRST
  HP 008: TRUE_NOT_TOP3; TRUE_NOT_FIRST; BEST_WIDTH_DIFFERS
  HP 009: TRUE_NOT_FIRST
  HP 010: BEST_WIDTH_DIFFERS
  HP 011: TRUE_NOT_TOP3; TRUE_NOT_FIRST; BEST_WIDTH_DIFFERS
  HP 012: TRUE_NOT_TOP3; TRUE_NOT_FIRST
  HP 013: TRUE_NOT_TOP3; TRUE_NOT_FIRST
  HP 014: NO_VALID_TRUE_SCORE
  HP 015: TRUE_NOT_TOP3; TRUE_NOT_FIRST; BEST_WIDTH_DIFFERS
  HP 016: TRUE_NOT_TOP3; TRUE_NOT_FIRST; BEST_WIDTH_DIFFERS
  HP 017: BEST_WIDTH_DIFFERS
  HP 018: TRUE_NOT_TOP3; TRUE_NOT_FIRST; BEST_WIDTH_DIFFERS
  HP 019: TRUE_NOT_FIRST
  HP 020: TRUE_NOT_FIRST; BEST_WIDTH_DIFFERS
  HP 021: NO_VALID_TRUE_SCORE
  HP 022: BEST_WIDTH_DIFFERS
  HP 023: TRUE_NOT_TOP3; TRUE_NOT_FIRST; BEST_WIDTH_DIFFERS
  HP 024: TRUE_NOT_TOP3; TRUE_NOT_FIRST
  HP 025: TRUE_NOT_TOP3; TRUE_NOT_FIRST; BEST_WIDTH_DIFFERS
  HP 026: TRUE_NOT_TOP3; TRUE_NOT_FIRST; BEST_WIDTH_DIFFERS
  HP 027: TRUE_NOT_TOP3; TRUE_NOT_FIRST
  HP 028: TRUE_NOT_FIRST; BEST_WIDTH_DIFFERS
  HP 029: NO_VALID_TRUE_SCORE
  HP 030: TRUE_NOT_TOP3; TRUE_NOT_FIRST
  HP 031: TRUE_NOT_FIRST
  HP 032: TRUE_NOT_FIRST
  HP 033: TRUE_NOT_TOP3; TRUE_NOT_FIRST
  HP 034: TRUE_NOT_TOP3; TRUE_NOT_FIRST
  HP 035: TRUE_NOT_TOP3; TRUE_NOT_FIRST; BEST_WIDTH_DIFFERS
  HP 036: TRUE_NOT_TOP3; TRUE_NOT_FIRST; BEST_WIDTH_DIFFERS
  HP 037: BEST_WIDTH_DIFFERS
  HP 038: TRUE_NOT_TOP3; TRUE_NOT_FIRST; BEST_WIDTH_DIFFERS
  HP 039: TRUE_NOT_FIRST; BEST_WIDTH_DIFFERS
  HP 040: TRUE_NOT_TOP3; TRUE_NOT_FIRST
  HP 041: TRUE_NOT_TOP3; TRUE_NOT_FIRST; BEST_WIDTH_DIFFERS
  HP 043: TRUE_NOT_TOP3; TRUE_NOT_FIRST
  HP 044: TRUE_NOT_TOP3; TRUE_NOT_FIRST; BEST_WIDTH_DIFFERS
  HP 045: BEST_WIDTH_DIFFERS
  HP 046: TRUE_NOT_TOP3; TRUE_NOT_FIRST; BEST_WIDTH_DIFFERS
  HP 047: TRUE_NOT_TOP3; TRUE_NOT_FIRST; BEST_WIDTH_DIFFERS
  HP 048: TRUE_NOT_TOP3; TRUE_NOT_FIRST
  HP 049: TRUE_NOT_TOP3; TRUE_NOT_FIRST; BEST_WIDTH_DIFFERS
  HP 050: TRUE_NOT_FIRST
  HP 051: TRUE_NOT_TOP3; TRUE_NOT_FIRST; DELTA_SIGN_REVERSAL
  HP 052: NO_VALID_TRUE_SCORE
  HP 053: TRUE_NOT_TOP3; TRUE_NOT_FIRST
  HP 054: TRUE_NOT_FIRST; BEST_WIDTH_DIFFERS
  HP 055: NO_VALID_TRUE_SCORE
  HP 056: TRUE_NOT_TOP3; TRUE_NOT_FIRST; BEST_WIDTH_DIFFERS
  HP 057: TRUE_NOT_TOP3; TRUE_NOT_FIRST
  HP 058: TRUE_NOT_TOP3; TRUE_NOT_FIRST
  HP 059: TRUE_NOT_TOP3; TRUE_NOT_FIRST; BEST_WIDTH_DIFFERS
  HP 060: TRUE_NOT_FIRST
  HP 061: BEST_WIDTH_DIFFERS
  HP 062: TRUE_NOT_TOP3; TRUE_NOT_FIRST
  HP 063: TRUE_NOT_TOP3; TRUE_NOT_FIRST; BEST_WIDTH_DIFFERS
  HP 064: NO_VALID_TRUE_SCORE
  HP 065: TRUE_NOT_TOP3; TRUE_NOT_FIRST; BEST_WIDTH_DIFFERS
  HP 066: TRUE_NOT_TOP3; TRUE_NOT_FIRST; BEST_WIDTH_DIFFERS
  HP 067: TRUE_NOT_FIRST; BEST_WIDTH_DIFFERS
  HP 068: TRUE_NOT_TOP3; TRUE_NOT_FIRST; BEST_WIDTH_DIFFERS
  HP 069: TRUE_NOT_TOP3; TRUE_NOT_FIRST; DELTA_SIGN_REVERSAL
  HP 070: TRUE_NOT_TOP3; TRUE_NOT_FIRST; BEST_WIDTH_DIFFERS
  HP 071: TRUE_NOT_TOP3; TRUE_NOT_FIRST
  HP 072: TRUE_NOT_TOP3; TRUE_NOT_FIRST; DELTA_SIGN_REVERSAL
  HP 073: TRUE_NOT_TOP3; TRUE_NOT_FIRST; BEST_WIDTH_DIFFERS
  HP 074: TRUE_NOT_TOP3; TRUE_NOT_FIRST
  HP 075: TRUE_NOT_FIRST; BEST_WIDTH_DIFFERS
  HP 076: TRUE_NOT_TOP3; TRUE_NOT_FIRST
  HP 077: TRUE_NOT_TOP3; TRUE_NOT_FIRST
  HP 078: TRUE_NOT_FIRST; BEST_WIDTH_DIFFERS
  HP 079: TRUE_NOT_TOP3; TRUE_NOT_FIRST
  HP 080: TRUE_NOT_TOP3; TRUE_NOT_FIRST; BEST_WIDTH_DIFFERS
  HP 081: TRUE_NOT_TOP3; TRUE_NOT_FIRST
  HP 082: TRUE_NOT_TOP3; TRUE_NOT_FIRST
  HP 083: TRUE_NOT_TOP3; TRUE_NOT_FIRST; BEST_WIDTH_DIFFERS
  HP 084: TRUE_NOT_TOP3; TRUE_NOT_FIRST
  HP 085: TRUE_NOT_TOP3; TRUE_NOT_FIRST; BEST_WIDTH_DIFFERS
  HP 086: TRUE_NOT_TOP3; TRUE_NOT_FIRST
  HP 087: TRUE_NOT_TOP3; TRUE_NOT_FIRST
  HP 088: TRUE_NOT_FIRST; BEST_WIDTH_DIFFERS
  HP 089: BEST_WIDTH_DIFFERS
  HP 090: TRUE_NOT_TOP3; TRUE_NOT_FIRST; BEST_WIDTH_DIFFERS
  HP 091: TRUE_NOT_TOP3; TRUE_NOT_FIRST
  HP 092: NO_VALID_TRUE_SCORE
  HP 093: TRUE_NOT_TOP3; TRUE_NOT_FIRST
  HP 094: TRUE_NOT_FIRST; BEST_WIDTH_DIFFERS
  HP 095: TRUE_NOT_TOP3; TRUE_NOT_FIRST
  HP 096: TRUE_NOT_FIRST; BEST_WIDTH_DIFFERS
  HP 097: TRUE_NOT_FIRST
  HP 098: TRUE_NOT_FIRST
  HP 099: TRUE_NOT_FIRST; BEST_WIDTH_DIFFERS
  HP 100: TRUE_NOT_TOP3; TRUE_NOT_FIRST; BEST_WIDTH_DIFFERS
  HP 101: TRUE_NOT_TOP3; TRUE_NOT_FIRST; BEST_WIDTH_DIFFERS
  HP 102: TRUE_NOT_TOP3; TRUE_NOT_FIRST
  HP 103: TRUE_NOT_TOP3; TRUE_NOT_FIRST; BEST_WIDTH_DIFFERS
  HP 104: TRUE_NOT_TOP3; TRUE_NOT_FIRST
  HP 105: TRUE_NOT_TOP3; TRUE_NOT_FIRST; DELTA_SIGN_REVERSAL; BEST_WIDTH_DIFFERS
  HP 106: TRUE_NOT_TOP3; TRUE_NOT_FIRST
  HP 107: TRUE_NOT_TOP3; TRUE_NOT_FIRST
  HP 108: TRUE_NOT_TOP3; TRUE_NOT_FIRST; BEST_WIDTH_DIFFERS
  HP 110: NO_VALID_TRUE_SCORE
  HP 111: TRUE_NOT_TOP3; TRUE_NOT_FIRST; BEST_WIDTH_DIFFERS
  HP 112: TRUE_NOT_FIRST; BEST_WIDTH_DIFFERS
  HP 113: TRUE_NOT_TOP3; TRUE_NOT_FIRST; BEST_WIDTH_DIFFERS
  HP 114: TRUE_NOT_TOP3; TRUE_NOT_FIRST; BEST_WIDTH_DIFFERS
  HP 115: TRUE_NOT_TOP3; TRUE_NOT_FIRST
  HP 116: NO_VALID_TRUE_SCORE
  HP 117: TRUE_NOT_TOP3; TRUE_NOT_FIRST
  HP 118: TRUE_NOT_TOP3; TRUE_NOT_FIRST; BEST_WIDTH_DIFFERS
  HP 119: TRUE_NOT_FIRST
  HP 120: TRUE_NOT_TOP3; TRUE_NOT_FIRST; BEST_WIDTH_DIFFERS
  HP 121: TRUE_NOT_TOP3; TRUE_NOT_FIRST; BEST_WIDTH_DIFFERS
  HP 122: TRUE_NOT_TOP3; TRUE_NOT_FIRST; BEST_WIDTH_DIFFERS
  HP 123: TRUE_NOT_TOP3; TRUE_NOT_FIRST; BEST_WIDTH_DIFFERS
  HP 124: BEST_WIDTH_DIFFERS
  HP 125: TRUE_NOT_TOP3; TRUE_NOT_FIRST
  HP 126: TRUE_NOT_TOP3; TRUE_NOT_FIRST; BEST_WIDTH_DIFFERS
  HP 127: TRUE_NOT_TOP3; TRUE_NOT_FIRST; BEST_WIDTH_DIFFERS
  HP 128: TRUE_NOT_TOP3; TRUE_NOT_FIRST; BEST_WIDTH_DIFFERS
  HP 129: TRUE_NOT_TOP3; TRUE_NOT_FIRST
  HP 130: TRUE_NOT_TOP3; TRUE_NOT_FIRST; BEST_WIDTH_DIFFERS
  HP 131: TRUE_NOT_TOP3; TRUE_NOT_FIRST; BEST_WIDTH_DIFFERS
  HP 132: TRUE_NOT_TOP3; TRUE_NOT_FIRST; BEST_WIDTH_DIFFERS
  HP 133: TRUE_NOT_TOP3; TRUE_NOT_FIRST; BEST_WIDTH_DIFFERS
  HP 134: NO_VALID_TRUE_SCORE
  HP 135: TRUE_NOT_FIRST
  HP 137: NO_VALID_TRUE_SCORE
  HP 138: TRUE_NOT_TOP3; TRUE_NOT_FIRST
  HP 139: TRUE_NOT_TOP3; TRUE_NOT_FIRST; DELTA_SIGN_REVERSAL; BEST_WIDTH_DIFFERS
  HP 140: TRUE_NOT_FIRST
  HP 141: TRUE_NOT_FIRST; BEST_WIDTH_DIFFERS
  HP 142: TRUE_NOT_TOP3; TRUE_NOT_FIRST; BEST_WIDTH_DIFFERS
  HP 143: TRUE_NOT_TOP3; TRUE_NOT_FIRST; BEST_WIDTH_DIFFERS
LEDGER: STANDS binary pair/address identities and geometric non-identifiability; RUNS toy exact score and all observed tests above; DEAD END retained §195 value mirror; OPEN physical face without nonlocal geometry and sequence-only centre unless controls separate.
RULE NEXUS slip/readback v1; ring address a in Z_2^n, P(a)=N-1-a, T(a)=a+1; S+1 pairs on sum N => TP=T o P, fixed {0,N/2}; S-1 pairs on sum N-2 => PT=P o T, fixed {N/2-1,N-1}; no intrinsic sign multiplicity predicted by two conjugate reflections; readback: original 188 nearest N to O detector, 193 emitted bonds v2, only D\E in each hairpin window, classify stored i+j-S in {+1,-1}, one row per stored slip; source hash and all failures reported.
RULE SHA256 4c95489dee5c731649f60fed669b81b606ef9a7876d59c11440782a6515b2264
STANDS RING identity fixed point and conjugacy n=2..14 PASS
WAY HOME dataset S=e+s observed from detector; classify missing bonds by (i+j-S) after generator readback
DATA raw SHA256 f5266a447a4342955936966ff46df15823da5c55508540d78f316bf3f4d2e145
HAIRPINS 143 MISSING 136 OFFSETS Counter({0: 62, 'other': 33, 1: 30, -1: 11})
SLIPS 41 TP 30 PT 11
TRACE CSV: ci,pdb,e,s,k,S,donor,acceptor,sum,delta,reflection
7,1FS0,7,15,4,22,9,12,21,-1,PT
7,1FS0,7,15,4,22,12,9,21,-1,PT
10,1JKE,12,20,11,32,14,17,31,-1,PT
10,1JKE,12,20,11,32,17,14,31,-1,PT
10,1JKE,56,60,3,116,54,63,117,1,TP
10,1JKE,56,60,3,116,63,54,117,1,TP
11,4KEH,146,154,4,300,148,151,299,-1,PT
11,4KEH,146,154,4,300,151,148,299,-1,PT
24,2AU7,9,12,3,21,9,13,22,1,TP
24,2AU7,9,12,3,21,13,9,22,1,TP
32,4K4C,104,112,6,216,105,112,217,1,TP
32,4K4C,104,112,6,216,107,110,217,1,TP
32,4K4C,104,112,6,216,112,105,217,1,TP
60,9PME,14,18,6,32,9,22,31,-1,PT
68,1QYN,57,65,12,122,59,62,121,-1,PT
68,1QYN,42,46,12,88,43,46,89,1,TP
68,1QYN,42,46,12,88,46,43,89,1,TP
86,1RYA,37,41,4,78,42,35,77,-1,PT
90,5LS7,41,49,6,90,43,46,89,-1,PT
90,5LS7,41,49,6,90,46,43,89,-1,PT
96,4NTK,108,112,4,220,112,109,221,1,TP
103,5Z38,22,30,4,52,25,28,53,1,TP
103,5Z38,22,30,4,52,28,25,53,1,TP
103,5Z38,22,30,4,52,30,23,53,1,TP
104,5E1L,127,135,4,262,128,135,263,1,TP
104,5E1L,127,135,4,262,130,133,263,1,TP
104,5E1L,127,135,4,262,135,128,263,1,TP
105,2FS2,99,107,8,206,100,107,207,1,TP
105,2FS2,99,107,8,206,102,105,207,1,TP
105,2FS2,99,107,8,206,107,100,207,1,TP
110,1NJK,76,84,8,160,77,84,161,1,TP
110,1NJK,76,84,8,160,79,82,161,1,TP
110,1NJK,76,84,8,160,82,79,161,1,TP
110,1NJK,76,84,8,160,84,77,161,1,TP
111,1VH5,103,111,6,214,104,111,215,1,TP
111,1VH5,103,111,6,214,106,109,215,1,TP
111,1VH5,103,111,6,214,111,104,215,1,TP
114,4Q2U,61,65,6,126,62,65,127,1,TP
114,4Q2U,61,65,6,126,65,62,127,1,TP
130,3MPY,34,38,4,72,38,35,73,1,TP
142,4HF0,57,63,4,120,62,59,121,1,TP
```

## 196.10 The ring-only TP/PT assignment and the 41-slip read-back

This follows the revised §196 ring audit in `running-audit-6` and `nexus-methods-v2`, not v1's incorrect claim of first discovering the frame law. For **native ring addresses**, not arbitrary sequence indices, define `P(a)=N−1−a` and `T(a)=a+1 (mod N)`. Composition is right-to-left:

$$
TP(a)=N-a\pmod N,\qquad PT(a)=N-2-a\pmod N.
$$

Thus native mirror pairs normally have address sum `N−1`; an upper sum slip to `N` is **TP**, and a lower sum slip to `N−2` is **PT**. The two cases possess two self-facing *addresses* each:

$$
\operatorname{Fix}(TP)=\{0,N/2\},\qquad \operatorname{Fix}(PT)=\{N/2-1,N-1\}.
$$

In the native `R_n` order, these are respectively `0ⁿ` and the crease representative `m`; or `P(m)` and `1ⁿ`. This is a **ring address statement**. Identifying `m` with an actual residue position would require the local chain-to-ring address map; the abstract equation alone cannot locate a physical self-facing residue along a real turn.

Crucially, `TP=T(PT)T^{-1}`. These are conjugate reflections with the **same number and types of fixed sites**. Therefore the ring-only symmetry supplies **no prediction of unequal sign counts**. A 30:11 excess cannot be forced by those two conjugate reflections alone. The missing dependency is the *chain interface's signed registration/occupancy of the crease and its NH/O directed interactions*. The experimental observation does not retroactively supply a ring prediction. This is **OPEN**, not a fitted physical energy or extra bit.

The read-back used precisely the §188 donor-to-nearest-O closure and §193 v2 zipper. From the 143 hairpin windows it found **1,023 stored bonds**, of which **136** were un-emitted: 62 on `S`, 33 on other sums, **30 on `S+1` and 11 on `S−1`**. All 41 are classified by the sealed rule, and their original `(chain, PDB, e, s, k, S, NH donor, O acceptor)` are printed in §196.9.

But these are **41 directed stored bonds, not 41 statistically independent hairpins**. They occupy **20 hairpins in 18 chains**, with **26 distinct undirected residue pairs** (19 positive, 7 negative). Across the negative slips, 9/11 donors lie in the loop interior; across positives, 16/30 donors lie in the loop. Consequently, the descriptor *β-bulge* has been used too broadly in the prior audit: a bond on `S±1` is a row-register deviation, but **it is not automatically a cross-strand β-bulge**. The missing classifier is whether its actual donor/acceptor geometry attaches the opposite arms or only closes the turn. No classification has been back-filled by convention.

The comparison's provenance is separate:

- **Slip rule SHA-256:** `4c95489dee5c731649f60fed669b81b606ef9a7876d59c11440782a6515b2264` (printed before coordinates were read).
- Native fixed-set and conjugacy checks **RUNS n=2…14**; identities **STANDS for even N**.
- Original data **RUNS: 143 hairpins, 136 stored-but-unemitted, 30 TP-labelled and 11 PT-labelled offsets**.
- Physical assignment of individual self-facing cells, and a forced 30:11 multiplicity, remain **OPEN**.

## 196.11 Ledger — no retrospective repairs

| Object | Status | Owner / way home |
|---|---|---|
| `R_{n+2}` centre nesting, frame lemma, ℓ(n), lamps | **STANDS (recovered)** | Earlier frame law, §135, *Native Binary Rings* eq.14; v2 correction takes precedence over v1's novelty claim |
| Pair-square address transposition and inverse face/shape encoding | **STANDS** | The binary address space; not dependent on protein data |
| One-centred-transposition seam step and mirrored step-program with face flags | **STANDS**, earlier §195 | The ring's native ISA, preserving shape/value separation |
| Sequence-only face-coherence rule and candidate ledger | **RUNS** | Pre-sealed `d98925…`; candidate-score ledger `ef20a1…`; 95,496 raw candidate rows |
| Preferential candidate-centre ranking on actual proteins | **RUNS** | 0.634060 mean versus shuffle 0.498424, shift 0.513876, decoy 0.475469; chain-block intervals above zero |
| Unique sequence-only crease location | **OPEN** | 12/132 first; 94/132 outside top three; more registration information needed |
| True centres excluded by nine-row aperture | **OPEN / UNLINKED** | 11/143; not guessed, not assigned zero |
| Sequence-selected turn width | **DEAD END as an exact width call** | 78/132 mismatches; contrast can be high at another width |
| Individual value mirror as a crease locator (§195) | **DEAD END** | 10/143 first, 0.5299 mean advantage versus nulls; not resurrected |
| Local N–Cα–C–Cβ tetrahedron as sheet-plane locator | **DEAD END** | Explicit equal-local-geometry counterexamples with opposing face signs; needs opposite-arm transverse vector |
| `TP`/`PT` ring reflection classification | **STANDS · RUNS** | Native address sums, fixed points n=2–14; separately sealed |
| 30 `S+1`, 11 `S−1` un-emitted stored bonds | **RUNS** | Original 143 hairpins; 41 directed events, 20 hairpins, 18 chains |
| All `S±1` bonds are physical β-bulges | **DEAD END as a blanket identification** | Many bonds remain within turn interior; interface/registration classification is missing |
| Why TP should outnumber PT and where its fixed point sits on the actual chain | **OPEN** | Two conjugate ring reflections are unbiased by themselves; missing chain-to-ring register/oriented strand geometry |
| Physical dry face from finished sheet normal | **RUNS previously, conditional** | 112/141 in §195; physical orientation is not sequence prediction |

## 196.12 Next precise prompt — §197

> Continue NEXUS using the v2 ring ISA, the sequence-only face-coherence ledger sealed `ef20a128…`, and the original 143-hairpin/41-slip read-back. **Do not invent any new bit, fitted energy, or global ring phase.** The face-coherence score preferentially ranks true centres (132 evaluable; advantage 0.634060 against the controls), yet only 12 rank first. The two native cell reflections are `TP(a)=−a` and `PT(a)=N−2−a`, conjugate by `T`, so the ring alone cannot derive the 30/11 orientation imbalance. Reverse the missing address: establish whether local sequence-only turn/strand route tokens, existing ring shell lamps, or an independently derived chain-to-ring registration can supply the displaced-reader identity *before* the N/O data are opened. First name each candidate provider, its native inverse, and the specific observable it returns through. Do not choose between providers by scanning observed bonds. Seal the exact provider-selection rule, predicted individual true centres, and signed slip classifications before opening any structural coordinates. Preserve the 11 UNLINKED centres and the 41 trace records. Separate cross-strand register changes from turn-internal contacts. Then run chain-block controls and output every false address, with STANDS / RUNS / OPEN / DEAD END and a complete single-cell verifier. If no unique provider exists, label the dependency OPEN and state precisely which geometry/registration link is absent.

**Attribution:** Dean A. Kulik · QuHarmonics Research Group · ORCID 0009-0003-3128-8828.
