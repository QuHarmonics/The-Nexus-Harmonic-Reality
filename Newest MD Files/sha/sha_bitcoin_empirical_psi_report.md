# SHA + Bitcoin Empirical Ψ-Controller Audit

## Scope

This run takes the revised empirical Ψ-controller idea and applies it to the **real saved schedule-boundary frontier**.

It does **not** claim direct inversion.
It asks a narrower question:

$$
\text{Does } J_{\mathrm{emp}} \text{ give the lawful branch a clean score margin over the false branch on the real late-wave frontier?}
$$

## Controller used

Measured late-wave prior:

$$
r_{\mathrm{mean}} = 57.800,
\qquad
\sigma_r = 2.926
$$

Late-wave deviation:

$$
D_{\mathrm{wave}}(n)
=
1 - \exp\left(-\frac{(n-r_{\mathrm{mean}})^2}{2\sigma_r^2}\right)
$$

Empirical carry-scar proxy:

$$
\rho_\Gamma(n)
=
0.5\,\frac{\text{schedule\_abs\_sum}}{\max(\text{schedule\_abs\_sum})}
+
0.5\,\frac{\text{schedule\_hw\_sum}}{\max(\text{schedule\_hw\_sum})}
$$

Return penalty:

$$
K_{\mathrm{return}}(n)
=
\begin{cases}
0 & \text{lawful continuation} \\
1 - \frac{\text{support depth}}{64} & \text{otherwise}
\end{cases}
$$

Residual inconsistency proxy:

$$
g_{\mathrm{emp}}(n)
=
\begin{cases}
0 & \text{exact schedule} \\
1 - \frac{\text{zero count}}{\max(\text{zero count})} & \text{otherwise}
\end{cases}
$$

Combined score:

$$
J_{\mathrm{emp}}(n)
=
0.4\,g_{\mathrm{emp}}(n)
+
0.3\,\rho_\Gamma(n)
+
0.2\,D_{\mathrm{wave}}(n)
+
0.1\,K_{\mathrm{return}}(n)
$$

Lower is better.

## Main results

- event pairs scored: **12**
- true branch lower than false branch rate:
$$
1.000
$$
- mean false-minus-true margin:
$$
0.482767
$$
- median false-minus-true margin:
$$
0.478793
$$
- minimum margin:
$$
0.364500
$$
- maximum margin:
$$
0.582918
$$

## Interpretation

On the real saved schedule frontier, the empirical Ψ-controller gives the true branch
a lower score than the false branch in:

$$
1.000
$$

of event pairs.

That means this controller is viable as a **branch-ranking overlay** on the late-wave frontier.

It does not replace exact schedule compatibility.
It turns the frontier into a graded score landscape instead of a hard yes/no gate only.

## Most ambiguous cases

The smallest positive margins are listed in the saved ambiguous-cases CSV.
Those are the best candidates for the next deeper continuation push.
