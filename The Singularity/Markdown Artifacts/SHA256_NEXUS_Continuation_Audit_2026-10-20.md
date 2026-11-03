# NEXUS SHA-256 Continuation Audit

**Run date:** 20 October 2026  
**Focus:** exact coordinate binding, constant-indexed reverse-round fields, symbolic inverse DAGs, and ROBDD closure.

## 1. Corrected coordinate binding for `OK`

The 65,536-row closure residual table `sha_OK_closure_residual_16bit.npy` is indexed by the natural 16-bit message value. The ring word table `sha_OK_ring_words_16bit.npy` is indexed by ring address. The correct binding is therefore

\[
\operatorname{residual}_{\mathrm{address}}[i]
=\operatorname{residual}_{\mathrm{message}}[R_{16}[i]].
\]

This was applied explicitly in the rerun. The checks pass:

- Natural message value: `0x4F4B` (`OK`) = 20,299.
- Ring address: 17,194; `R_16[17194] = 0x4F4B`.
- The exact 256-bit return-state residual is zero for exactly one of the 65,536 messages: `OK`.
- The target region survives every sound exclusion test, as it must.

**Important distinction:** the region tests below start from the complete, already-computed residual table. They test whether a region admits an exclusion certificate after its leaves have been evaluated. They do **not** yet compute the certificate directly from the region prefix without evaluating its leaves.

## 2. Region-level certificate results

For a region, a *common-one certificate* exists when at least one of the 256 residual bits is 1 on every leaf. An *affine-one certificate* exists when there is a GF(2) linear functional that evaluates to 1 on every residual vector in that region. Either condition soundly excludes the region because a valid preimage has residual zero.

| Coordinate partition | Prefix depth | Regions rejected by common-one | Fraction of domain covered |
|---|---:|---:|---:|
| Ring-address MSB prefix | 12 | 13 / 4,096 | 0.317% |
| Natural message MSB prefix | 12 | 9 / 4,096 | 0.220% |
| Folded square `(f, reverse(g))` | 12 | 16 / 4,096 | 0.391% |
| Outer-frame inward | 12 | 17 / 4,096 | 0.415% |
| Ring-address MSB prefix | 13 | 5,187 / 8,192 | 63.318% |
| Natural message MSB prefix | 13 | 5,150 / 8,192 | 62.866% |
| Folded square `(f, reverse(g))` | 13 | 5,157 / 8,192 | 62.952% |
| Outer-frame inward | 13 | 5,272 / 8,192 | 64.355% |

At depths 14–16, common-one certificates reject every non-target region in this finite test. The affine-one diagnostic finds certificates for 8,191 of 8,192 regions at depth 13 in each tested partition; the target region is the only one excluded from that count. This high rate is an *after-the-fact existence result*, not evidence that an inexpensive prefix-only selector has been found. The certificate may depend on the residual values of all leaves.

### Constant-driven route-state stability

The exact carry archive contains 14,336 retained intermediate carry/borrow fields: seven arithmetic stages × 64 reverse rounds × 32 bit boundaries. The table below counts fields that are constant across every candidate in the region containing `OK`.

| Partition | 8-bit prefix (256 words) | 12-bit prefix (16 words) | 13-bit prefix (8 words) | 14-bit prefix (4 words) | 15-bit prefix (2 words) |
|---|---:|---:|---:|---:|---:|
| Ring address | 1,303 / 14,336 (9.09%) | 1,587 (11.07%) | 1,973 (13.76%) | 3,698 (25.80%) | 8,231 (57.42%) |
| Natural message prefix | 1,302 (9.08%) | 1,603 (11.18%) | 1,974 (13.77%) | 3,759 (26.22%) | 8,284 (57.78%) |
| Folded square `(f, reverse(g))` | 1,302 (9.08%) | 1,613 (11.25%) | 1,945 (13.57%) | 3,695 (25.77%) | 8,369 (58.38%) |
| Outer frame inward | 1,311 (9.15%) | 1,616 (11.27%) | 1,984 (13.84%) | 3,685 (25.70%) | 8,369 (58.38%) |
| Carry-frame inward | 1,311 (9.15%) | 1,616 (11.27%) | 1,998 (13.94%) | 3,685 (25.70%) | 8,234 (57.44%) |

A second, more focused test selected 512 fields specifically from the `sub_K` and `sub_W` stages (borrow boundaries 8, 16, 24, and 31 in each reverse round). For the target region, folded-square order has the largest fixed share at depth 12 (114/512 = 22.27%), while carry-frame-inward order is strongest at depths 13–15 (158/512 = 30.86%; 221/512 = 43.16%; 359/512 = 70.12%). There is no single partition that wins at every depth. These fields remain separately indexed by stage, reverse-round index, and bit boundary; neither `K_t` nor `W_t` has been averaged away.

## 3. Shared symbolic XOR/AND inverse DAG: `Q` and `GO`

I built a separate shared Boolean DAG using the exact SHA-256 IV and indexed round constants, the source-dependent message schedule, known one-block padding, and all 64 reverse rounds. The source interface is symbolic; candidate messages are not used to construct the intermediate graph. Every residual bit compares the recovered initial state with `H0`.

An independent constant-table comparison against `reverse64_verified.py` confirms that all 64 constants and all eight IV words match. In particular, **`K[42] = 0xC24B8B70`**; a transcription error in the first prototype was caught by the true-source replay and corrected before these results were retained.

| Target | Unknown source bits | DAG nodes including input variables | XOR gates | AND gates | Internal nodes bound by local propagation | Source bits bound locally |
|---|---:|---:|---:|---:|---:|---:|
| `Q` (`0x51`) | 8 | 98,031 | 60,846 | 37,177 | 2,422 | 0 |
| `GO` (`0x474F`) | 16 | 98,799 | 61,408 | 37,375 | 2,042 | 0 |

Doubling the unknown input interface from 8 to 16 bits increases this implementation's total shared-DAG node count by 768 nodes, or about **0.783%**. These counts depend on the selected gate basis and complement-edge representation; do not equate them directly with another compiler's raw-node counts.

Replay of the declared source succeeds exactly: all 256 returned-state residual bits are zero for both `Q` and `GO`, and the closure evaluates true. The all-zero and all-one control inputs do not close. The local propagator uses the two-known XOR rule and standard AND forcing rules; it binds zero source bits in both cases. This is consistent with the reconvergent-dependency limitation described in the project note. **For `GO`, this DAG/replay result does not by itself prove that `GO` is the only 16-bit preimage.**

## 4. Exact ROBDD closure for the one-byte `Q` control

A direct ROBDD compilation then reverses the same target digest with the full symbolic schedule and indexed `K_t`, and intersects the 256 exact conditions that the recovered initial state equals `H0`. Four variable orderings give the same single satisfying assignment, `0x51 = Q`; each final closure root has eight reachable BDD decision nodes and a satisfying-assignment count of one.

| Source-variable order | Canonical BDD nodes allocated during compilation | Final closure nodes | Satisfying assignments | Time |
|---|---:|---:|---:|---:|
| MSB source order | 1,672,107 | 8 | 1 | 8.20 s |
| LSB source order | 1,673,285 | 8 | 1 | 8.31 s |
| Outside inward | 1,672,527 | 8 | 1 | 8.94 s |
| Even then odd | 1,672,979 | 8 | 1 | 8.47 s |

The aggregate allocated-node count varies by about 0.071% across these orders. **Metric definition:** these counts include all canonical nodes allocated during the run, including temporary intermediate functions; they are not the peak live/reachable-node metric reported by a different implementation.

The exact returned-state closure sequence, with initial-state word 0 tested from bit 0 upward, is:

\[
256\to131\to56\to28\to12\to6\to3\to1.
\]

The first seven constraints isolate the unique source; the remaining 249 returned-state checks leave that source unchanged. This is an exact one-byte closure result, not a general SHA-256 inversion formula for arbitrary message lengths.

## 5. Ring binding of `Q`

The width-8 ring generator independently places `Q = 01010001` at address 70, between `0x4F` at 69 and `0x53` at 71. Its normalized angle is

\[
u=\frac{70}{256}=\frac{35}{128}.
\]

The reflected address is `255 - 70 = 185`, which contains the conditional partner `P_8(Q) = reverse(Q) = 10001010`. Thus the symbolic inverse closure and the ring address/partner map agree for this target.

## 6. Ledger and next exact link

**RUNS:** corrected `OK` coordinate binding; full finite-domain residual uniqueness for the declared 2-byte class; region-certificate existence counts; 14,336-field carry/borrow stability comparisons; shared inverse DAGs for `Q` and `GO`; exact local-propagation test; one-byte `Q` ROBDD closure under four variable orders; ring address 70 and reflected partner address 185.

**OPEN:** derive a region exclusion certificate directly from the retained region coordinates and the indexed `K_t/W_t` drivers, without first evaluating every leaf. The next scaling target is to couple schedule-tail recurrence and `PadValid` constraints to the cofactor procedure, then test whether an outer-frame/ring-address subtree can be rejected before expanding its individual messages. The 512-bit tail bijection is an address transformation, not extra digest information; for the 55-byte class the historical-source selector lower bound remains 184 bits by the pigeonhole argument.

The ring partition comparison supplies guidance but not the missing selector: outer-frame/carry-frame orders improve a few local stability scores, while other depths favor folded square or direct ring order. The next algorithm must preserve the tuple `(ring address, W_t, K_t, state_t, carry/borrow fields_t)` and prove every prune sound under exact cofactor semantics.

## Reproducibility files

- `sha_OK_folded_square_region_pruning.py` and its JSON output: finite-domain residual-region certificates.
- `sha_OK_frame_borrow_uniformity.py` and its JSON output: 512 selected exact driver/borrow fields over all regions.
- `sha_OK_target_frame_all_carry_stability.py` and its JSON output: all 14,336 fields on the target region.
- `sha_OK_target_region_driver_stability.py` and its JSON output: focused `K_t/W_t` borrow fields.
- `sha_OK_closure_bit_ordering_diagnostic.json/.csv`: canonical versus oracle-guided closure-bit ordering for `OK`.
- `sha_symbolic_gate_dag.py` and `sha_symbolic_gate_dag_Q_GO_results.json`: shared gate DAG and local propagation.
- `sha_symbolic_robdd_inverse.py` and `sha_symbolic_robdd_Q_results.json`: exact one-byte closure with four orderings and the per-return-bit trace.

The region scripts consume the existing exact mask/residual arrays from the working directory; the compact package includes the scripts and summarized output, not the 99 MB raw carry archive.
