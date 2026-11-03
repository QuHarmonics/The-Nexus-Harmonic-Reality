# §124. The same difference stack runs the BBP lane fold and the SHA-256 round

**Run date:** 17 October 2026  
**Source engine:** `compiler_space.py`, §123, with the first-run fuse `(A,B) → (A,A XOR B)`  
**Executable:** `nexus_bbp_sha_difference_engine.py`  
**Prediction seal:** `NEXUS_BBP_SHA_difference_engine_prediction_2026-10-17.txt`  
**Prediction SHA-256:** `6f79721b0f6477069092816766f9832cbeae06d5a835bcc9b8e2a4e924a85332`  
**Carry-type follow-up seal:** `NEXUS_BBP_carry_type_prediction_2026-10-17.txt`  
**Carry-type prediction SHA-256:** `8374fc30ad192492443cd81a31bb42ce612134b79add6fde27e9f49355288d8b`

## The compile operation

The engine takes a vector-valued truth table over `LEN = n` Boolean coordinates and applies the same recursive mixer stack:

\[
 a_S=\bigoplus_{T\subseteq S}f(T)
       =\left(\prod_{i\in S}D_i f\right)(0),
 \qquad M(M(f))=f.
\]

A table entry may pack several output bits; XOR acts componentwise. The coefficients are not merely counted: their ANF evaluation is used to execute the actual BBP lane-fold inputs and the local SHA gate operations.

## A. BBP: compile the four rational lanes before folding the columns

For one layer, take the four base-16 lane digits `q1,q4,q5,q6` as a 16-bit word and compile the weighted contribution

\[
 (q_1,q_4,q_5,q_6)\longmapsto 4q_1-2q_4-q_5-q_6
\]

as a signed 7-bit output. All \(16^4=65,536\) input tuples are included in the difference table; applying the stack a second time returns every weighted output. The coefficient program was then executed on 2,926 actual rational-ring layer/column tuples, drawn from 2,271 distinct tuples. Those compiled contributions were accumulated by column and propagated through the base-16 normalization carry. The resulting 64 hexadecimal digits agree exactly with the independent Machin computation:

```text
3.243f6a8885a308d313198a2e03707344a4093822299f31d0082efa98ec4e6c89
```

The local weighted-fold ANF has maximum degree 13 in its 16 input coordinates. Its nonzero coefficient-vector counts by degree are 1:16, 2:109, 3:480, 4:1306, 5:2471, 6:3577, 7:4127, 8:3609, 9:2260, 10:1019, 11:336, 12:74, 13:8. Degrees 14–16 are empty. This is the transformation table of the signed lane fold, not a list of π digits.

### Carry ownership correction

The run separates two values that WP5's prose had put under the same name.

1. **Layer-local carry** \(J_k(m)\), from *The Form of the BBP Digit Machine*, is defined per rational-ring layer and satisfies

   \[
   J_k(m)=\left\lfloor16^mV_k\right\rfloor-
          \sum_j c_j\left\lfloor\frac{16^m}{8k+j}\right\rfloor\in\{-4,-3,\ldots,3\},
   \]

   together with \(H_k(m)=w_k(m)+16J_k(m)-J_k(m+1)\). The exact recurrence and the bound were checked on all 2,850 layer/age pairs used here; observed range: \([-4,3]\).

2. **Global column-normalization carry** is the quotient propagated right-to-left while adding the contributions from many layers into each output column. In the finite WP5 configuration \(N=64,G=12\), its observed range is **\([-23,37]\)**.

The second value is not the first. WP5's sentence that “the carry from the right stays in \([-4,3]\)” is valid only when “carry” means the layer-local \(J_k\). Read as the global carry of its own column-normalization code, it is false. The correction is to name the owner: the bound belongs to \(J_k(m)\), not to the global column carry. The matching π digits survive the correction.

## B. SHA-256: compile the bit operators, then compose the round

The engine compiles complete three-input truth tables for `Ch`, `Maj`, a full adder and a full subtractor. Their recovered ANFs are:

\[
\begin{aligned}
\operatorname{Ch}(x,y,z)&=xy\oplus z\oplus xz,\\
\operatorname{Maj}(x,y,z)&=xy\oplus xz\oplus yz,\\
\operatorname{FA}_{sum}(x,y,c)&=x\oplus y\oplus c,\\
\operatorname{FA}_{carry}(x,y,c)&=xy\oplus xc\oplus yc,\\
\operatorname{FS}_{borrow}(x,y,b)&=y\oplus xy\oplus b\oplus xb\oplus yb.
\end{aligned}
\]

Each local map has eight inputs; its table is transformed to difference coefficients, then its ANF is evaluated over every local input. The resulting gate tables drive each bit of the real 32-bit SHA adders, subtractors, `Ch`, and `Maj`. Rotations and XORs are the linear wiring between those compiled local transformations.

Results:

- 1,000 random `(state, W_t, K_t)` round tests match the independent SHA-256 implementation; every compiled round is inverted back to its parent state.
- The compiled one-block path for `NEXUS difference engine` produces the exact `hashlib.sha256` digest `74f4227aab1097a2f87a499bc55e21cdb8ff2400908ee29f5b1e10e6136405df`.
- For 256 initial chaining states formed by the eight independent reader directions (bit 0 of each of the eight 32-bit words), the compiled 64-round path returns all 256 seeds when the actual message schedule and round constants are retained. Feed-forward reverses with the incoming chaining state retained.

## C. The per-round difference table: progression, not a selected endpoint

For one fixed padded block, the complete actual state map is restricted to the declared `LEN=8` affine reader slice. The state output is 256 bits. Its table is compiled with the same stack after every round, at all depths 0–64, and once more after feed-forward. Every table is evaluated back from its coefficients at every one of its 256 reader addresses.

The progression has a sharp sequence:

- At round 0, the map is affine: 9 active monomial addresses (constant plus eight degree-1 directions), with \(H(D_aF)=0\).
- At round 1, the highest degree is 4; 48 of 256 monomial addresses are active.
- At round 2, degree 8 is present, but only 235 of 256 monomial addresses are active.
- At round 3, all 256 monomial addresses are active; derivative diversity is still short of its ceiling (mean \(H(D_aF)=6.964199859\), with 99–128 distinct derivative vectors depending on direction).
- At round 4, every one of the 255 nonzero reader directions has exactly 128 distinct derivative outputs, each appearing twice across the 256 addresses. Thus \(H(D_aF)=7\) for every direction and the mean is exactly 7 bits. This is the first full-support, maximum-derivative-diversity layer on this slice.
- Rounds 5–64 and feed-forward continue to change the individual coefficient vectors even though this support and entropy statistic remains saturated.

The seven-bit derivative entropy has a precise combinatorial ceiling here: \(D_aF(x)=F(x)\oplus F(x\oplus a)\) is identical for the paired addresses \(x\) and \(x\oplus a\); at most 128 distinct derivative outputs can occur for a fixed nonzero direction in a 256-address domain. The run reaches that ceiling at round 4. This is an exact result for this explicitly defined reader slice, not an assertion that a whole 256-bit SHA truth table was enumerated.

## Ledger

| Claim | Status |
|---|---|
| Boolean difference table is compiled by the first-run mixer stack and is its own inverse | RUNS; Möbius/ANF transform STANDS |
| BBP four-lane weighted-fold coefficients generate the actual finite rational-ring column contributions | RUNS |
| First 64 BBP hex digits match independent Machin computation | RUNS, 64/64 |
| Layer-local BBP carry recurrence and \([-4,3]\) bound | RUNS, 2,850/2,850 |
| Global column-normalization carry in the same finite run has range \([-23,37]\) | RUNS; different owner from \(J_k\) |
| SHA local gates compiled from difference tables drive the 32-bit word operators | RUNS |
| Compiled SHA round equals the reference and is reversible when \(W_t,K_t\) are known | RUNS, 1,000/1,000 randomized cases |
| Restricted SHA state map has full difference support by round 3 and saturated derivative diversity by round 4 | RUNS on the declared `LEN=8` slice |
| Unrestricted digest-only inverse and minimal root observer | OPEN |

## Artifacts

- `nexus_bbp_sha_difference_engine.py` — executable difference-stack compiler and run.
- `NEXUS_BBP_SHA_difference_engine_results.json` — all 65 round-layer profiles plus feed-forward, coefficient support, and run records.
- `NEXUS_BBP_SHA_difference_engine_run.md` — compact run report.
- `NEXUS_BBP_SHA_difference_engine_console.log` — terminal summary.
- Both pre-run prediction seals and `sha256_bidirectional_audit.py` — reproducibility inputs.
