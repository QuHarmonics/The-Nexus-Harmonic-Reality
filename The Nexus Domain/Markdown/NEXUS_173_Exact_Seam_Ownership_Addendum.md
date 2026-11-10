# NEXUS §173 — SHA-256 Reduced Boundary: Exact Seam Ownership

**Dean A. Kulik — QuHarmonics Research Group — ORCID 0009-0003-3128-8828**  
**Date:** 2026-10-24  
**Companion verifier:** `NEXUS_173_reduced_seam_verifier.py`; stdlib-only, fully printed output.

## Scope and input

This is a constraint audit of the supplied §172 SHA-256 calculation, *not* a claim of a solved SHA-256 preimage problem. SHA-256 follows its ordinary standard 64-round single-block implementation. The IV, round constants, padding and schedule are held exactly as defined. For a block with a known message length, the unknown message bytes are **UNLINKED** until independently supplied or derived.

The supplied work has correctly shown:

1. A 64-round working trajectory can be encoded by one scalar stream `(a_1,...,a_64)`, using its companion coboundary to determine `e`, and the round equations to determine its `W`.
2. A single-block digest determines eight terminal `a`-words `a_57,...,a_64` by algebraic cancellation without needing the message.
3. The 56 trajectory variables `a_1,...,a_56` can be parametrized by the first eight input words when `W_8,...,W_15` are fixed, since the round dynamics and schedule propagate forward. The remaining eight constraints are the terminal seam equations.

## 1. The digest is *exactly equivalent* to the last eight a-words

Subtract the public IV from the eight digest words to obtain

\[
H_{64}=(a_{64},a_{63},a_{62},a_{61},e_{64},e_{63},e_{62},e_{61}).
\]

Use the exact hemisphere cancellation

\[
e_{t+1}\equiv a_{t+1}-\Sigma_0(a_t)-\operatorname{Maj}(a_t,a_{t-1},a_{t-2})+a_{t-3}\pmod{2^{32}}.
\]

It returns `a_60,a_59,a_58,a_57` consecutively. Conversely, given those eight `a` words (`a_57..a_64`), the same relation gives `e_61..e_64` and therefore the original eight digest words. This is a **bijective 256-bit coordinate change** on the terminal working state: no independent information has been recovered beyond the digest.

**STANDS** by triangular algebra; **RUNS** for the empty message, `abc`, and `GlassKey`.

## 2. Identify the final seam residual exactly

Define two quantities read directly from the digest and IV:

\[
A(D)=a_{60}-\Sigma_0(a_{59})-\operatorname{Maj}(a_{59},a_{58},a_{57}),
\]

\[
B(D)=a_{64}-\Sigma_0(a_{63})-\operatorname{Maj}(a_{63},a_{62},a_{61})
-\Sigma_1(e_{63})-\operatorname{Ch}(e_{63},e_{62},e_{61})-K_{63},
\]

all modulo `2^32`.

The first is `e_60-a_56`; the second is `e_60+W_63`. Thus the digest alone fixes

\[
\boxed{q(D)=B(D)-A(D)\equiv a_{56}+W_{63}\pmod{2^{32}}.}
\]

The final (`t=63`) equation of the eight-word seam is **exactly**

\[
\boxed{r_{63}=q(D)-a_{56}-W_{63}=0\pmod{2^{32}}.}
\]

It is not a ninth constraint and does not add information to the other seven residuals. It makes the owner of the last boundary equation explicit.

For `abc`: `a56=0x38cc9913`, `W63=0x12b1edeb`, `q(D)=0x4b7e86fe`.

## 3. What the complete eight-word seam means

Let `W(W_0,...,W_7)` be the actual standard message schedule with fixed `W_8,...,W_15` where the message-length assumptions permit that. Compute the 56-round forward state with the IV, and the 8-round backward state with the digest and **the same** late schedule words:

\[
\boxed{H_{56}^{\rm fwd}(W)=F_{56:63}^{-1}(H_{64}(D); W_{56},\dots,W_{63}).}
\]

This is equivalent to simultaneous satisfaction of all eight terminal schedule/state residual words. The equivalence follows from exact invertibility of the SHA working-state round when its schedule word is known.

The `t=63` equation binds `a_56` once `W_63` is linked. The earlier `t=62,...,56` equations bind successively earlier elements of the a-trajectory when the corresponding schedule words are known. This is an **inverse route**, not a digest-only assignment to the schedule.

**RUNS:** on all seven tests, the correct schedule yields equal boundary states and eight zero residuals. A controlled one-bit input perturbation breaks both conditions. The last residual equals the scalar mismatch (`0xfea6ef3f` for the perturbation used in the companion run).

## 4. Reduce the input domain without smuggling in an input

For a three-byte message, `W_0` contains 24 unknown message bits and a known trailing padding byte `0x80`; `W_1,...,W_15` are fixed by padding and the message length. Thus the whole 56-word boundary system is an exact 256-bit boundary predicate in **only 24 still-unknown input bits**. This is a reparametrization, not a solution of those bits.

At the actual `abc` input, 24 single-bit perturbations of the scalar check `q(D) - [a56+W63]` have linearly independent 32-bit XOR-difference vectors. The full 256-bit seam's 24 perturbation vectors also have rank 24. These ranks describe secants **at one input**, not a globally invertible Jacobian or proof of uniqueness.

The single 32-bit scalar cannot globally distinguish all five-byte inputs: `2^40` input strings map to `2^32` possible scalar values; at least one scalar value has at least 256 preimages. The full 256-bit seam retains more information than the scalar.

## 5. Ledger and return path

- **STANDS:** the exact digest-to-late-a bijection, scalar boundary identity, and equivalence of the eight residual equations to the `H56` state match.
- **RUNS:** seven forward/digest return checks, exact terminal state reconstruction, 24 single-bit diagnostics, and controlled one-bit mismatch.
- **UNLINKED:** unknown initial message word(s) and therefore unknown late schedule words, for digest-only execution.
- **OPEN:** deriving those unknown input words from the terminal boundary *without enumeration or an already known forward trajectory*. No conclusion about global preimage uniqueness or cryptographic weakness follows from equation counting or finite-difference rank.

**Research interpretation:** the return exists as an exact addressable relation when the late schedule is linked. The digest reader determines the terminal coordinate and a scalar seam combination; it does not directly supply the omitted schedule. The next required WHAT is an independently derived link to the schedule—not another enumeration of candidate inputs.

**Pre-data seal** for the stated return path (printed before the three new fixed inputs were linked; the four previously examined examples are retrospective ownership checks): `5c14287263c1050bbda204f0bfc27911c37f61e363a3d4fe5056bf8b8f8a8102`. The auxiliary digest-to-eight-a recoding was checked afterwards and is recorded as algebraic verification rather than a separately sealed landing.
