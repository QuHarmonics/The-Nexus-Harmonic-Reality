# NEXUS — Nested Transformation Unwind

**Run date:** 2026-10-16  
**Scope:** Recursively expand a BBP radix-16 step and SHA-256 schedule/round transformations, then unwind the composition at each layer. The test uses the existing NEXUS SHA constants and equations. It is an exact algorithmic experiment, not a physical voltage-waveform measurement.

## Main correction

Do not stop at the output boundary of a composite transform. Expand the transform into its child operations, follow their dependencies, and then unwind the same tree in reverse composition order. A parent node's observer may rely on sibling operands and retained context; a local inverse is not necessarily defined from that node's output alone.

The execution audited here follows this recursion:

```text
source block
  └─ message schedule
       └─ schedule word W[t]
            ├─ σ₁(W[t−2])
            ├─ W[t−7]
            ├─ σ₀(W[t−15])
            └─ W[t−16]
  └─ 64-round state path
       └─ round t
            ├─ T₁ = ((((h + Σ₁(e)) + Ch(e,f,g)) + K[t]) + W[t])
            ├─ T₂ = Σ₀(a) + Maj(a,b,c)
            ├─ a′ = T₁ + T₂
            ├─ e′ = d + T₁
            └─ register shifts
  └─ feed-forward: H′ = H + E
```

All word additions are modulo \(2^{32}\). Each sigma function is itself a nested composition of rotations or shifts and XORs; `Ch` and `Maj` are nested Boolean expressions. The implementation evaluates those constituent nodes explicitly.

## 1. BBP: unwind the radix instead of sampling only the digit

A radix-16 phase step is four radix-2 steps:

\[
2x_i=b_i+x_{i+1},\qquad b_i\in\{0,1\},\quad i=0,1,2,3.
\]

The emitted hexadecimal digit and residual phase are

\[
q=8b_0+4b_1+2b_2+b_3,\qquad x_4=\{16x_0\}.
\]

Recursively unwinding the tree gives

\[
x_0=\frac{b_0+\frac{b_1+\frac{b_2+\frac{b_3+x_4}{2}}{2}}{2}}{2}.
\]

The actual four-lane witness was recovered exactly:

| Lane start | Nested branch | Hex digit | Residual | Recovered start |
|---|---:|---:|---:|---:|
| \(7/9\) | `1100` | 12 | \(4/9\) | \(7/9\) |
| \(1/3\) | `0101` | 5 | \(1/3\) | \(1/3\) |
| \(3/13\) | `0011` | 3 | \(9/13\) | \(3/13\) |
| \(1/7\) | `0010` | 2 | \(2/7\) | \(1/7\) |

For weights \(c=(4,-2,-1,-1)\), the per-depth weighted branches are

\[
h=(4,2,-2,-3).
\]

Folding these four levels produces the same scalar as the weighted hexadecimal digits:

\[
8(4)+4(2)+2(-2)-3=33
=4(12)-2(5)-3-2.
\]

The scalar 33 is the readout; the nested branch/residual path identifies the route that produced it. The experiment verifies all four lane returns and the equality of the coarse readout with the weighted nested levels.

## 2. SHA schedule: recursively compile, then recursively unwind

The message schedule node is

\[
W_t=(((\sigma_1(W_{t-2})+W_{t-7})+\sigma_0(W_{t-15}))+W_{t-16})\bmod2^{32}.
\]

The observer starts from \(W_{48},\ldots,W_{63}\), recomputes the prefix of each nested addition, then obtains the missing leftward schedule word by subtraction:

\[
W_{t-16}=W_t-\big((\sigma_1(W_{t-2})+W_{t-7})+\sigma_0(W_{t-15})\big)\pmod{2^{32}}.
\]

It calls itself at \(t-1\) until the whole schedule is restored. Across 207 padded blocks, all \(207\times48=9{,}936\) missing schedule words were reconstructed; the recovered schedules matched the forward schedules exactly.

## 3. SHA round: recursively unwind the nested state transform

Forward, each round forms

\[
\begin{aligned}
T_1&=((((h+\Sigma_1(e))+Ch(e,f,g))+K_t)+W_t),\\
T_2&=\Sigma_0(a)+Maj(a,b,c),\\
a'&=T_1+T_2,\\
e'&=d+T_1.
\end{aligned}
\]

The new state is \((a',a,b,c,e',e,f,g)\). The observer follows the child relationships backward:

1. The shifts recover \(a,b,c,e,f,g\).
2. Recompute \(T_2\), then recover \(T_1=a'-T_2\).
3. Recover \(d=e'-T_1\).
4. Unwind the nested \(T_1\) additions from right to left:
   \(T_1-W_t\), then \(-K_t\), then \(-Ch(e,f,g)\), then \(-\Sigma_1(e)\), recovering \(h\).
5. Re-evaluate the six local closures to verify each recovered parent/child relation.

The 64 round observers are themselves composed recursively, with the final round unwound first. This recovered the starting working state for every one of 13,248 round chains across the 207 blocks.

The feed-forward node was also checked as a local transform: \(H'=H+E\) and, **when the incoming chaining state \(H\) is known**, its working-state operand is recovered as \(E=H'-H\). This condition matters: the audit has not established a digest-only inverse for an unknown prior chaining state.

## 4. Executed results

- 54 messages, including padding-boundary cases: exact returns 54/54.
- Standard digest checks against `hashlib.sha256`: 54/54.
- Compression blocks: 207.
- Schedule nodes unwound: 9,936.
- Round trees unwound: 13,248.
- Register coordinates checked during forward and reverse round traversal: 105,984 in each direction.
- Internal round-node inverse checks: 79,488.
- Feed-forward coordinate inversions with known incoming chaining state: 1,656.
- Recursive low-level execution audit: 367,632 word-add node evaluations and 11,764,224 bit-carry node evaluations, including closure rechecks; 91,080 word-subtraction evaluations and 2,914,560 bit-borrow nodes, including the inverse checks.

The node counts include deliberate recomputation used to verify closure, not just the count of primitive operations in one normal SHA-256 evaluation.

## 5. The exact limit of this result

The reverse route stores the final 16 schedule words for each padded block. That is \(16\times32=512\) bits per block, equal to the size of the padded source block. Reversibility follows because this tail is an invertible coordinate for the schedule, but it is not a smaller-than-source residual.

The complete SHA digest was checked by running forward from the recovered blocks. The experiment does **not** derive the original arbitrary message from the 256-bit digest alone, nor does it prove that a fixed-width, non-scaling observer is sufficient for all sources. The root digest-only inverse and minimum residual remain OPEN.

## Ledger

- BBP radix-16 → four radix-2 nested branches, exact unwind: **RUNS**.
- SHA schedule recursive compile/unwind from \(W_{48..63}\): **RUNS**.
- SHA nested round-tree unwind with known schedule words: **RUNS**.
- Feed-forward local inverse when incoming chaining state is known: **RUNS**.
- Reverse complete multi-block SHA from digest alone: **OPEN**.
- Minimal residual that identifies a source within each digest fiber without recoding the source: **OPEN**.

## Artifacts

- `nexus_nested_recursive_unwind.py` — executable audit.
- `nexus_nested_recursive_unwind_results.json` — machine-readable results.
- `nexus_nested_recursive_unwind_run.txt` — run summary.
