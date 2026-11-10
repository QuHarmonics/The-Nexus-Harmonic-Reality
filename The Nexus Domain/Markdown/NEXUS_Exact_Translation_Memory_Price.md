# NEXUS — The missing carrier handoff: exact translation and its retained-field price

**Driven by Dean A. Kulik**  
QuHarmonics Research Group · ORCID 0009-0003-3128-8828  
Audit: 2026-11-02. Independent C and Python implementations, prediction sealed before execution.  
SHA-256 prediction: `c823e96a046c6465d3d9385177cbdd63ce8dfa52b2dc96c43b2606038628682f`

## 1. Name the hole

The earlier next-shell result established a live eight-word carrier with a full **43,155,322-step** two-lap return. A carry-only external bit applied after 4,096 steps enlarged the visited footprint to 32 words; applied at a field-vacuum return it remained confined to eight. The missing relationship is not another candidate value. It is the operation that changes the **WHERE of an already populated eight-word return** while transporting its **retained field history** and preserving its return identity.

The coupled rule acts on the entire n-bit word domain, not on a sliced or hand-selected ring:

\[
 x=D[p]\oplus w,\quad
 p'=p\oplus x,\quad
 w'=P_n(x),\quad
 D'[p]=D[p]\oplus w'.
\]

The exact inverse remains

\[
 x=P_n(w'),\quad p=p'\oplus x,\quad
 D[p]=D'[p]\oplus w',\quad w=x\oplus D[p].
\]

## 2. The filled slot: translate WHERE **and** the live field

For an arbitrary fixed word difference \(h\in\mathbb F_2^n\), define

\[
 \boxed{H_h(p,w,D)=\left(p\oplus h,\ w,\ q\mapsto D[q\oplus h]\right).}
\]

This is a real, reversible state change relative to a *fixed* native mold: the reader changes word location and the offset field is readdressed; the mold itself is not shifted. It carries the stored return relationships to their new addresses, rather than leaving them behind.

### The exact commutative square

\[
 \boxed{F\circ H_h=H_h\circ F,\qquad H_h^2=I,\qquad H_aH_b=H_{a\oplus b}=H_bH_a.}
\]

**Proof.** In the shifted state the active offset at the shifted reader is
\(D_h[p\oplus h]=D[p]\). The next difference therefore remains \(x=D[p]\oplus w\); the next carry remains \(P_n(x)\); the reader advances to \((p\oplus h)\oplus x=(p\oplus x)\oplus h\), and the one field update is the original update at the translated address. This is valid for *all* n, p, w, live fields D, and h. The inverse is the same translation because XOR by h is an involution.

**Corollary.** Any complete two-lap orbit of period \(T\) is transported to an orbit of *exactly the same* period T. Its internal return history is not copied from a new generator; it is the same route at another WHERE.

## 3. Locations are affine carrier cosets

For an even-width ring \(n=2r\), let

\[
 u=1^n,\quad e_R=2^{r-1},\quad e_L=2^r,\quad
 L=\operatorname{span}_{\mathbb F_2}\{u,e_R,e_L\}.
\]

The one-break reader returns within the affine eight-word carrier \(A=m_*\oplus L\). Every \(A+h\) is another exact carrier: the collection of all such locations is the quotient

\[
 \boxed{\mathcal B_n/L\cong\mathbb F_2^{n-3},\qquad 2^{n-3}\text{ distinct eight-word placements}.}
\]

The next-shell mirror pair \(o_R=2^{r-2},\ o_L=J(o_R)=2^{r+1}\) adds two independent quotient directions. Their four pre-existing carrier cosets form a square:

\[
 A,\quad A+o_R,\quad A+o_L,\quad A+o_R+o_L.
\]

**This is the exact next-shell transport geometry:** one direction moves to a new eight-word carrier; its partner moves in the orthogonal quotient direction. Their composition closes without adding a location outside the fixed field. Neither a physical Euclidean distance nor a force law is assumed.

## 4. What the three previous kicks were missing

All rows begin from the original one-break seed, with native partner P; the t=4096 rows share the same nonzero field configuration before the handoff. Footprints are over the next 100,000 steps. An original full period was rerun at each width.

| Handoff | Action | Visited word locations | Return ownership |
|---|---|---:|---|
| No kick | Original F | 8 | Two-lap period 43,155,322 |
| Carry only at t=4096 | \(w\leftarrow w\oplus o_R\) | 32 | Route visits all four quotient cosets; original field remains |
| Reader WHERE only at t=4096 | \(p\leftarrow p\oplus o_R\) | **2** | Exact **6-step** loop; seven original field cells remain stranded |
| Complete translation at t=4096 | \(H_{o_R}(p,w,D)\) | **8** | Original **43,155,322-step** identity retained |
| Reader WHERE only at half-lap vacuum | \(p\leftarrow p\oplus o_R\), \(D=0\) | **8** | Exactly \(H_{o_R}\) at that instant; full two-lap identity retained |

The newly discovered **two-location, six-step** result from an isolated WHERE kick is important. It is a valid, reversible landing of the reader in an unpopulated carrier coset, while the seven old field writes are left at the original WHERE. It is not a relocated one-break object. This identifies why the original carry-only expansion also failed to produce translation: it changed an operand without carrying the registered history.

### Vacuum return as a zero-field-handoff gate

At exactly t=21,577,661:
\[
 p=m_*\oplus u,\quad w=e_R\oplus u,\quad D=0.
\]

At this state, \(H_{o_R}\) reduces exactly to the one-word location update \(p\leftarrow p\oplus o_R\). The same signed reader and two-lap continuation are preserved. After another 21,577,661 steps, the reader is at the translated starting WHERE \(m_*\oplus o_R\), with carry \(e_R\) and empty field; after a second half-cycle, it returns to its translated complemented state. This full translated cycle was executed at n=6,8,10,12.

The original period contains **only two field-vacuum arrivals** (halfway and full return). Thus there are exactly two phases per complete period when a WHERE-only kick performs an *instantaneous* full translation without changing any stored field cells. It is a phase gate, not a permanently available free relocation operation.

## 5. The price is an exact field gradient

A translation changes the field according to \(D_h[q]=D[q\oplus h]\). The exact number of live-field cell values that must change to produce this state is

\[
 \boxed{C_{\rm cell}(D;h)=\sum_q [D(q)\ne D(q\oplus h)].}
\]

The more granular bitwise change count is

\[
 \boxed{C_{\rm bit}(D;h)=\sum_q\operatorname{popcount}(D(q)\oplus D(q\oplus h)).}
\]

These are **discrete gradients of the retained field** along the translation h. When h leaves the original carrier L (as oR does), the original and translated supports are disjoint, and if k cells are nonzero,

\[
 \boxed{C_{\rm cell}=2k,\qquad C_{\rm bit}=2\sum_q\operatorname{popcount}(D(q)).}
\]

At t=4096, k=7, so **14 field cell values change** (equivalently seven disjoint swaps, plus the one reader WHERE XOR). At half-lap k=0, so **zero field cell values change**. These are necessary differences between the specified initial and translated states; execution cost in machine instructions or physical energy is a separate matter.

| Width | Shift h | Old → translated anchor (word) | Old → translated native address | Cell changes at 4096 | Changed field bits at 4096 |
|---|---|---|---|---:|---:|
| 6 | 0x02 | 0x23 → 0x21 | 26 → 39 | 14 | 28 |
| 8 | 0x04 | 0xC7 → 0xC3 | 122 → 201 | 14 | 36 |
| 10 | 0x08 | 0x38F → 0x387 | 506 → 909 | 14 | 44 |
| 12 | 0x10 | 0xF1F → 0xF0F | 2042 → 3861 | 14 | 52 |

The XOR shift is one bit in the chosen next-shell word coordinate, but the corresponding address gap in the native ring is not constant. The quotient shell graph provides a precise relational step distance; ordinary spatial lengths require an additional coordinate reading.

### Exact complete-cycle burden

A full 43,155,322-step n=6 cycle gives the number of phase ticks with k active field locations:

| Active k | Number of ticks |
|---:|---:|
| 0 | 2 |
| 1 | 106 |
| 2 | 3,212 |
| 3 | 50,576 |
| 4 | 475,298 |
| 5 | 2,738,622 |
| 6 | 9,409,712 |
| 7 | 17,402,406 |
| 8 | 13,075,388 |

The exact mean is \(\bar{k}=6.919906147380849\), so the mean instantaneous field-cell mismatch for a move outside L is \(2\bar{k}=13.839812294761698\). The field has k=7 or 8 on 70.6235% of phase ticks. This is a **compiler-defined resistance to instantaneous carrier readdressing**, not yet mass in SI units or a demonstrated dynamical law of inertia.

## 6. Status and the remaining actual link

**STANDS** — Exact full-field translation symmetry \(H_hF=FH_h\); invertibility; quotient location geometry \(\mathcal B_n/L\); exact field-gradient mismatch formula; period preservation under H; vacuum-field collapse of H to a WHERE-only XOR.

**RUNS** — Complete original 43,155,322-step native partner cycle at n=6,8,10,12; 43,155,322-step translated populated orbit at n=6; full translated half-vacuum 43,155,322-step orbit at all four widths; exact six-step reader-only populated-field landing at all four widths; 32-word carry-only expansion; 14-cell/28–52-bit gradient at t=4096; 1,250 independent random conjugacy/inverse tests and native address/quotient checks.

**DEAD END** — A carry-only perturbation of a populated field is not translation; a WHERE-only perturbation of a populated field is not translation. Both are correct computations, with distinct owners: enlarged relational reach and a detached six-step packet, respectively.

**OPEN** — Which interaction in the self-contained reader–field dynamics selects h and executes the paired offset relocation as an *endogenous*, local handoff, rather than an externally applied symmetry? The operator and its state gradient are fixed. A physical inertia/mass and acceleration law requires an operational clock, permitted transport scheduling, and spatial/energetic calibration derived within the same field, not attached by numeric analogy. The NESTED -1 ownership remains to be derived.

### Reproduction and correction log

1. The seal text was written and SHA-256 committed before the new C and independent Python readouts.
2. The first C compilation printed format warnings because `PRIu64` expected a platform `uint64_t` but `ULL` literals were passed. This was corrected with explicit casts; all numerical results were unchanged.
3. The first C test found that a populated-field WHERE-only kick visits **two**, rather than 8 or 32, sites. It was retained and the full six-step phase-state return added to the assertions, which passed.
4. The corrected full C audit and independent Python tests both pass as shipped; no manual trimming of the generator was used.

**Files:** `NEXUS_Translation_Handoff_Audit.c` and its execution trace; `NEXUS_Translation_Handoff_Independent.py` and its trace; `NEXUS_Translation_Handoff_Prediction.json` and `.sha256`.
