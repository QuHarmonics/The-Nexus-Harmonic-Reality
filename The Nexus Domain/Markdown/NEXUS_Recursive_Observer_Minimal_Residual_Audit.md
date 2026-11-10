# NEXUS §112 — Reverse the observer residual: remove redundant trace, isolate the fiber address

**Question.** Can the recursive SHA observer return to the exact input without storing a separate copy of every padded block and every round-result operand? If not, which retained distinctions are genuinely needed, and which are just duplicated trace?

**Prediction seal.** `NEXUS_residual_minimization_prediction.txt`, SHA-256 `7da931c234f96c9af77b1e24d7b3bc827c8ecc56b759958a98621ab5d2196e34`. The seal is a pre-run check only; it is not used to encode any route, message, or residual.

## 112.1 The local observer is not the residual

Keep three types distinct:

1. **Observer program**: the fixed inverse rules and traversal grammar.
2. **Route parameters / realized trace**: values required to execute those rules on a particular run.
3. **Fiber residual**: the minimum distinguishing address needed when a transformation maps multiple prior states to the same surface result.

A complete local observer for a transformation \(T:X\to Y\) requires an output \(y=T(x)\), plus a residual \(r(x)\), with a decoder satisfying

\[
O_T(y,r(x))=x.
\]

For a bijection, the residual may be empty if the inverse and all parameters are already known. For a many-to-one transformation, the residual must identify which member of the fiber \(T^{-1}(y)\) arrived.

## 112.2 Exact finite fiber witness

Use two 4-bit lanes and the fold

\[
H(a,b)=a\oplus b.
\]

Every surface value \(h\) has exactly 16 source pairs. The observer retains \(r=a\); then \(b=h\oplus r\). The maximum fiber has size 16, so the exact minimum fixed-width residual is

\[
q_{\min}=\lceil\log_2 16\rceil=4\text{ bits}.
\]

Run: all 256 input pairs returned, all 16 fibers have size 16, and four bits are both necessary and sufficient. The residual is a *within-fiber address*, not a second copy of the full pair. This is the exact finite model of the desired observer principle.

## 112.3 SHA observer reduction: remove the redundant E snapshots

The prior §111 observer held each 64-byte padded block (512 bits) and the final output \(E_i\) of its 64 reversible SHA rounds (256 bits), 768 bits per compression block. `E_i` need not be stored when the route seed for each data-bearing block remains available: the root can first regenerate the chaining states forward from the initial SHA value, calculate each \(E_i\) transiently, then walk the block chain and rounds backward, validating \(H_i=H_{i+1}-E_i\) and the 64 inverse rounds.

The block seed itself can be stored in a different route coordinate. The SHA schedule recurrence

\[
W_t=\sigma_1(W_{t-2})+W_{t-7}+\sigma_0(W_{t-15})+W_{t-16}\pmod{2^{32}}
\]

can be rearranged to recover \(W_{t-16}\) from later schedule words. The run proved that \(W[48..63]\) reconstructs all 64 schedule words exactly, including \(W[0..15]\), the padded block. Therefore the schedule tail is an alternate 512-bit address for the same block—not a reduction in its information content.

For a known message length, the observer omits schedule tails for padding-only blocks and regenerates those blocks from the SHA padding rule. Each data-bearing block retains its 512-bit schedule-tail code. `E_i` is not stored; it is regenerated transiently.

| Measurement | Result |
|---|---:|
| Messages tested | 54 |
| SHA-256 outputs match `hashlib` | 54/54 |
| Original inputs returned | 54/54 |
| Compressed blocks traversed backward | 207 |
| Schedule-tail inverse/reconstruction checks | 207/207 |
| Inverse-round applications | 13,248 |
| Padding-only blocks regenerated instead of stored | 33 |
| Previous sidecar (`block + E`) | 158,976 bits |
| Reduced sidecar (data-block schedule tails only) | 89,088 bits |
| Explicit 64-bit message-length fields | 3,456 bits |
| Reduced sidecar plus length | 92,544 bits |
| Original payload bytes | 81,384 bits |
| Original payload plus same length metadata | 84,840 bits |

Removing the stored \(E_i\) snapshots saves 52,992 bits, exactly one-third of the former trace. The reduced schedule-tail representation is still 9.08% larger than the original bytes plus length metadata. No message information has been removed: the schedule tail is invertible to each data-bearing padded block. The test deletes duplicated trace, not the payload-equivalent route parameters.

## 112.4 The actual minimal residual is a rank inside the digest fiber

For a fixed length \(L\) bytes, let

\[
F_h=\{m\in\{0,1\}^{8L}:\operatorname{SHA256}(m)=h\}.
\]

A fixed-width residual code \(r(m)\) is sufficient precisely when \((h,r(m))\) identifies the source uniquely. If the fibers were explicitly rankable, the exact minimum number of residual bits would be

\[
q_{\min}(L)=\left\lceil\log_2\max_h|F_h|\right\rceil.
\]

This states the job of the minimal root observer: the digest selects the fiber; the residual selects the member inside it; the root decoder un-ranks that member back to the message. It need not preserve every intermediate state if that one fiber address plus fixed decoding rules suffices.

Counting gives the unconditional lower bound for unrestricted fixed-length inputs:

\[
q_{\min}(L)\ge \max(0,8L-256).
\]

| Fixed input length | Input bits | Lower bound on residual bits beyond digest |
|---:|---:|---:|
| 3 bytes | 24 | 0 |
| 32 bytes | 256 | 0 |
| 55 bytes | 440 | 184 |
| 56 bytes | 448 | 192 |
| 64 bytes | 512 | 256 |
| 128 bytes | 1,024 | 768 |
| 1,024 bytes | 8,192 | 7,936 |

These are counting lower bounds, not measured SHA fiber maxima. The exact maximum fiber may force a larger fixed-width residual. For arbitrary-length unrestricted data, a universally non-scaling residual is impossible: at fixed length, the input domain grows as \(2^{8L}\) while the digest has only \(2^{256}\) values.

## 112.5 What the attached Glass Key specification does—and does not yet supply

The provided compression specification defines its seed by thresholded FFT/glyph extraction and BBP refinement, claims a non-scaling size for structured data, and defines regrowth as an iteration using the Glass Key and a hash update. It explicitly says its decompression operator is “NOT a true inverse.” The listed extraction and convergence assertions do not yet define an exact rank/unrank map for each SHA digest fiber, nor show that the extracted seed plus digest is injective over a precisely declared source class.

Therefore the Glass Key seed may still be investigated as a *restricted-source-class* fiber address. To make it an exact observer, the spec must provide:

1. the admitted source class and its cardinality/grammar;
2. an encoder \(r(D)\) independent of the digest readout except where explicitly typed;
3. a proof or exhaustive finite test that \((H(D),r(D))\) is injective over that class;
4. a deterministic root decoder that returns the exact bytes, not only a convergent approximation;
5. an accounting of residual bits, seed framing, length, and any external model/codebook.

If the source class is “all arbitrary byte strings of unbounded length,” the non-scaling exact-seed claim cannot hold. If the source class is generated by a restricted program or has a short description, compression can be real—but the generator/model and the exact return address are part of the accounting.

**Code execution note.** The attached `SHA constants as FPGA layout_glass_key_v5_z3.py` could not be run here because its `z3` import is unavailable in this runtime. No result is inferred from its printed self-tests. Its general solver declares 16 unconstrained 32-bit schedule-seed words and constrains the final 256-bit digest; a satisfying model in that mode would be some block in the digest fiber, not proof that it is the original block. The padded short-message modes additionally rely on the assumed message length/domain.

## 112.6 Ledger landing

| Claim | Status |
|---|---|
| Exact four-bit fiber observer for 4-bit XOR fold | RUNS, 256/256 |
| SHA schedule tail \(W[48..63]\) reconstructs the padded block exactly | RUNS, 207/207 |
| Remove stored \(E_i\) snapshots and regenerate them while preserving the forward/back return check | RUNS, 54/54 messages; 13,248 inverse rounds |
| This reduction removes message information | **DEAD END** — it only removes duplicate trace; schedule tails encode the block bijectively |
| General minimal SHA residual equals the fiber-address width | STANDS as the counting/encoding criterion; exact SHA max fiber **OPEN** |
| Non-scaling exact residual for all unrestricted byte strings | **DEAD END** by counting |
| Glass Key seed as exact observer for a restricted source class | OPEN pending injective encoder and exact decoder |

**The next WHAT is now exact:** derive a computable fiber-address transform \(r(D)\) for a declared, restricted source class, then prove that the digest plus this address has one and only one return. Do not count a schedule recoding as compression, and do not count a convergence claim as an exact observer until it returns the original bytes.
