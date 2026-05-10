# SHA-256 Shape-Class Inversion Engine v0 — Run Report

## Δ Objective

Build the seven-gate shape-first inversion scaffold and test the immediate proof target:

$$
\boxed{\text{tail class is recoverable from shape traces before payload is known}}
$$

This is not a digest-only preimage claim. This run tests whether the discarded shape channel contains recoverable tail grammar.

## Corpus alignment

The project stack defines the mechanical basis:

- The die uses exact round algebra, shift transport, carry closure, and local reverse seams.
- The one-block ROM grammar separates payload rails from the control tail.
- The structural decoder order is:

$$
\boxed{(M_{13},M_{14},M_{15})\to\text{gate class}\to M_{0..12}}
$$

The seven-gate engine therefore implements:

| Gate | Function |
|---|---|
| G0 | terminal restore from digest |
| G1 | reverse closure into fused wall |
| G2 | tail grammar inference |
| G3 | schedule legality |
| G4 | carry topology |
| G5 | transport shape |
| G6 | final digest verification |

## Δ What was actually measured

Generated `3920` balanced one-block messages:

$$
L\in\{0,\dots,55\},\qquad 70\text{ samples per length}
$$

For each message, the engine computed a full SHA-256 trace and extracted **shape-only features**:

- Hamming-weight trajectory of `W`, `T1`, `T2`
- carry-count trajectory for `T1` and `T2`
- fused-wall pair-class counts $P/G/K/C$ for $h+W$
- state-lane Hamming statistics
- T1/T2 phase-angle statistics
- Pythagorean shape residuals
- early/mid/late temporal bands

No raw digest value, raw message value, raw schedule word value, or raw round word value was used in the shape classifier.

A digest-only control was also trained using only final SHA-256 digest statistics.

## Ψ Tail / length recovery results

| Target | Classes | Majority baseline | Shape top-1 | Shape top-3 | Shape top-5 | Digest-only top-1 |
|---|---:|---:|---:|---:|---:|---:|
| `length` | 56 | 0.018 | 0.668 | 0.976 | 0.998 | 0.038 |
| `pad_word` | 14 | 0.073 | 0.818 | 1.000 | 1.000 | 0.093 |
| `pad_offset` | 4 | 0.251 | 0.627 | 0.984 | 1.000 | 0.259 |
| `tail_regime` | 5 | 0.929 | 0.993 | 1.000 | 1.000 | 0.929 |
| `M13_mode` | 3 | 0.929 | 1.000 | 1.000 | 1.000 | 0.929 |
| `len_bucket4` | 14 | 0.073 | 0.818 | 1.000 | 1.000 | 0.093 |


## Main lock

The shape channel recovered:

$$
\boxed{L\text{ top-1} = 0.668}
$$

$$
\boxed{L\text{ top-3} = 0.976}
$$

$$
\boxed{L\text{ top-5} = 0.998}
$$

against a 56-class balanced random baseline near:

$$
\frac1{56}\approx 0.0179.
$$

The length bucket / pad word was recovered at:

$$
\boxed{0.818\text{ top-1},\quad 1.000\text{ top-3}}
$$

The M13 regime was recovered at:

$$
\boxed{1.000}
$$

## Feature importance: length

Top features:

- `sched_hw_r15`: 0.02803
- `sched_hw_delta_abs_r14`: 0.02781
- `W_hw_early_mean`: 0.02759
- `sched_hw_early_mean`: 0.02759
- `sched_hw_tail15_15_23_min`: 0.02691
- `W_hw_r15`: 0.02663
- `W_hw_tail15_15_23_min`: 0.02545
- `sched_hw_global_std`: 0.01976
- `hW_G_early_mean`: 0.01857
- `W_hw_global_std`: 0.01841


## Feature importance: tail regime

Top features:

- `W_hw_r13`: 0.08514
- `sched_hw_r13`: 0.08003
- `sched_hw_delta_abs_r13`: 0.07117
- `hW_G_r13`: 0.06414
- `sched_hw_global_std`: 0.04999
- `hW_C_r13`: 0.04929
- `W_hw_global_std`: 0.03194
- `W_hw_early_mean`: 0.02873
- `sched_hw_early_mean`: 0.02305
- `sched_hw_delta_abs_r14`: 0.01899


## Restricted recovery demonstration

A constrained external grammar was used:

$$
\Sigma=\texttt{"abcdef0123456789"},\qquad |\Sigma|=16.
$$

Target message:

```text
fade
```

Target digest:

```text
009978b8c24f47f63fbbf3cd8fb774ba7e20c5586c5998c74cfd3c448173dada
```

Shape-channel predicted length ranking:

| Rank | Length | Probability |
|---:|---:|---:|
| 1 | 4 | 0.884333 |
| 2 | 3 | 0.056619 |
| 3 | 2 | 0.024381 |
| 4 | 5 | 0.022667 |
| 5 | 6 | 0.008667 |
| 6 | 9 | 0.002000 |
| 7 | 8 | 0.001333 |
| 8 | 55 | 0.000000 |


Using only the top-1 predicted length, G6 verification found:

```text
fade
```

Candidates checked:

$$
20533
$$

Top-1 length search space:

$$
16^4=65536
$$

Unconditioned grammar space for lengths 0..8:

$$
\sum_{L=0}^8 16^L=4581298449
$$

Reduction factor:

$$
\boxed{69905.1\times}
$$

## Ψ Collapse

This run proves the immediate v0 target:

$$
\boxed{\text{tail grammar is strongly present in trace shape before payload recovery}}
$$

It does **not** prove arbitrary SHA-256 digest-only inversion.

The correct interpretation is:

$$
\boxed{H+\mathcal{S}_{\text{trace}}\rightarrow\text{tail class}\rightarrow\text{conditioned payload search}\rightarrow M}
$$

where $\mathcal{S}_{\text{trace}}$ is the recovered or observed shape channel.

## Ω isolated gap

The remaining open gap is:

$$
\boxed{\Omega=\text{derive enough trace shape from }H\text{ alone for arbitrary targets}}
$$

Until that gap is closed, this is a white-box / side-shape inversion engine, not a black-box digest-only preimage solver.
