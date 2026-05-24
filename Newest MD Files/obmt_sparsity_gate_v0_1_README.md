# OBMT Sparsity Gate v0.1

## Purpose

Execute Gate 2:

$$
\mathcal{R}_{emp} \times \mathcal{A}_{168} \rightarrow N_{hit}
$$

The gate tests whether the finite OBMT address map produces sparse exact physical hits or dense numerological overproduction.

## Gate

$$
N_{hit} \le 2 \Rightarrow \Psi_{\text{sparse signal}}
$$

$$
N_{hit} \ge 100 \Rightarrow \bot_{\text{dense numerology}}
$$

If no real 10,000-ratio corpus is supplied, the notebook returns:

$$
\Omega_{\text{needs 10000-ratio corpus}}
$$

## Optional Input

Place `empirical_ratios.csv` next to the notebook with columns:

```text
name,value,domain,dimension
```

Only `name` and `value` are required.

## Outputs

- `obmt_predictions_168.csv`
- `obmt_empirical_input_used.csv`
- `obmt_hits.csv`
- `obmt_null_distribution.csv`
- `obmt_gate_summary.json`
