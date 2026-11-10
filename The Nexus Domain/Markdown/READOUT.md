# NEXUS — Carry Has a Shape: Exact Residual-State Reader

**Independent computation for Dean A. Kulik, QuHarmonics Research Group**  
**Date:** 2026-11-03  
**Scope:** exact finite-domain Boolean functions; full truth-table construction is deliberately exponential in input variable count.

## 1. WHAT was sealed

At any fixed cut in any fixed variable order, two read histories are indistinguishable precisely if they induce the same Boolean function of the unread variables. Thus the number of *minimal deterministic reader states* at cut `k` is

\[
W_k = |\{F_a: a\in\{0,1\}^k\}|,\qquad F_a(b) = F(a,b).
\]

Here `W_k` is a state count; the binary storage capacity for a state identifier is `ceil(log2 W_k)` bits. In the decision-diagram interpretation, it is the width of a fully semantically reduced ordered Boolean decision diagram (up to the convention for the terminal layer).

The sealed predictions and their readouts are recorded in `PREDICTION_SEAL.txt`, `PAIR_PREDICTION_SEAL.txt`, and their SHA-256 files. Both seals were generated before either corresponding experiment executed.

## 2. Consequence: a tiny quotient can still be hard to construct

Let `s` be the number of satisfying assignments of `F`. Every nonzero residual at cut `k` corresponds to a prefix extending to at least one satisfying assignment, and distinct prefixes partition the satisfying assignments. Consequently

\[
W_k \le s + 1.
\]

For UNSAT formulas, every residual is zero and `W_k=1`. For a unique-solution formula, `W_0=1` and `W_k=2` for every `1<=k<=n`.

**Critical distinction:** This is the width of the *already-constructed semantic quotient*. It does **not** say that a polynomial-time compiler can derive the quotient, decide residual equivalence, or find a satisfying witness from a succinct CNF. Constructing the truth table in this audit explicitly takes exponential space and time in `n`.

## 3. Uniform random 3-CNF: no fixed-order privilege

Generator: for each `n` in `8,10,12,14,16,18,20`, independently draw 60 formulas with `m = round(4.26*n)` three-literal clauses; within each clause, choose three distinct variables uniformly, and give each literal an independent random sign. A clause may repeat across draws. Seed: `20261103`.

Three fixed-rule orders were used: identity `0,1,...,n-1`, outside-in `0,n-1,1,n-2,...`, and a uniform independent random permutation per formula. Exact residual truth functions were computed as contiguous bit blocks in the fully evaluated Boolean truth table. This use of truth tables is a measurement method, **not** a polynomial-time SAT solver.

### Seal-resolved theorem

The distribution of these signed random formulas is unchanged under any variable permutation. Therefore **all fixed variable orders have the same distribution of full cut-width profiles**. A randomly selected order independent of the formula has the same distribution too. The finite sample may have order-dependent differences on individual formulas, but a fixed outside-in rule cannot have a systematic advantage under this exchangeable generator.

### Run results

| n | Clauses | SAT / 60 | UNSAT / 60 | Mean peak W: binary, SAT only | Mirror, SAT only | Random, SAT only |
|---:|---:|---:|---:|---:|---:|---:|
| 8  | 34 | 48 | 12 | 3.083 | 3.021 | 3.000 |
| 10 | 43 | 43 | 17 | 3.186 | 3.302 | 3.279 |
| 12 | 51 | 50 | 10 | 4.160 | 4.060 | 4.060 |
| 14 | 60 | 48 | 12 | 4.021 | 3.875 | 3.958 |
| 16 | 68 | 45 | 15 | 3.956 | 4.111 | 4.111 |
| 18 | 77 | 45 | 15 | 5.400 | 5.378 | 5.244 |
| 20 | 85 | 45 | 15 | 5.800 | 5.800 | 6.000 |

Of 420 formulas, 324 were satisfiable and 96 were unsatisfiable. Among the SAT instances, mirror had lower/equal/higher peak width than binary on 33/252/39 cases. All UNSAT instances had width 1. All 46 unique-SAT instances had peak width 2. The seven-size pooled SAT-only means were binary `4.222`, mirror `4.210`, and random `4.225`.

The true random-3-SAT distribution is being sampled here at small sizes. The absence of a mirror advantage at these sizes is *consistent* with the symmetry theorem; the theorem, not this sample, establishes equality of the fixed-order distributions.

## 4. Derived structural test: mirrored equality constraints

Seal a fixed, fully specified relation on even `n` variables:

\[
E_n(x)=\bigwedge_{i=0}^{n/2-1}(x_i\leftrightarrow x_{n-1-i}).
\]

Each equality is represented by its two standard 2-CNF clauses, but the geometry comes from the ring's mirror partners, not from a fitted variable order. This is a *constructed* 2-CNF control, not a random 3-SAT hardness sample.

**Before execution:** under ordinary order, after `n/2` variables have been read, every bit is an unresolved obligation for a distinct mirrored bit, yielding `W_{n/2}=2^(n/2)`. Under outside-in order, a pair is finished before proceeding; only one equality can be pending, giving at most three residual states: contradiction, pending value 0, pending value 1. Hence `max_k W_k=3` for even `n>=4`.

| n | Solutions | Binary midpoint width | Binary peak width | Mirror peak width |
|---:|---:|---:|---:|---:|
| 4 | 4 | 4 | 4 | 3 |
| 8 | 16 | 16 | 16 | 3 |
| 12 | 64 | 64 | 64 | 3 |
| 16 | 256 | 256 | 256 | 3 |
| 20 | 1024 | 1024 | 1024 | 3 |
| 24 | 4096 | 4096 | 4096 | 3 |

All six exact executions matched the sealed relations. The general claims follow from the structural argument above, independently of these six readouts.

## 5. What the ring says the gap is

A 3-CNF formula itself provides a **syntactic** frontier. At a cut, future-only clauses are fixed, past-only falsified clauses collapse into a contradiction state, and each crossing clause is either already satisfied or leaves a residual obligation on unread variables. Recording that active obligation subset produces a correct, generally nonminimal deterministic reader.

The semantic quotient identifies obligation subsets whose future truth functions are identical. The step

\[
\text{CNF syntax}\;\longrightarrow\;\text{future-equivalence classes}
\]

is the missing compiler provider. After the classes and their transitions are known, the satisfaction/witness route is straightforward. Before they are known, the size of the eventual quotient does not tell us how expensive it is to construct.

For mirrored equalities, the pair boundaries force a narrow syntactic frontier, so both the *description* and its residual quotient are cheap. For uniform random 3-SAT, the chosen mirror order is statistically no more privileged than any other fixed labeling. To exploit a ring order, the input's constraint structure must be mapped to those mirror relations, and the **cost of that mapping** belongs in the ledger.

## 6. Ledger

- **STANDS:** `W_k` as residual-function quotient; width bound `W_k <= s+1`; `W_k=1` on UNSAT and 2 for unique-SAT after the first bit; fixed-order random 3-SAT permutation-invariance; mirrored-equality width theorem.
- **RUNS:** 120 independent small-instance semantic-oracle profile comparisons, 42 exact relabeling identity checks, 1,260 solution-count bound assertions, 420 three-order random formulas, six mirrored-relation widths, all with zero assertion failures.
- **ELSEWHERE:** The identification of tiny *minimal residual width* with efficient SAT solving belongs to a different owner: the resource cost of deriving the semantic quotient from the succinct formula.
- **OPEN:** An input-to-quotient compiler with bounded total route construction cost on the intended formula class. A structural embedding of constraint graphs into mirror-pair reading geometry must account for the cost of finding the embedding.

This study does not settle P versus NP; its exact results locate a necessary distinction and exhibit an explicit case where ring-relative reading order changes memory exponentially.

## 7. Reproduce

The principal runnable program uses only Python's standard library:

```bash
python carry_shape_3sat.py --trials 60 --sizes 8 10 12 14 16 18 20 --seed 20261103 --output EXACT_CARRY_WIDTHS.json
```

`EXACT_CARRY_WIDTHS.json` contains every per-instance width profile and random variable order. `PAIRED_RELATION_WIDTHS.json` holds the independent mirrored relation readout. The full outputs and their corresponding prediction seals are kept unmodified in the ZIP. The implementation intentionally does **not** pretend to be a polynomial-time reader: it materializes the complete truth function so that residual equality is unambiguous and independently testable.
