# State-Space Closure: Probes K, L, and M

Three independently defined observable classes are used to test whether
secondary re-injection at $t = k + 16$ produces any detectable second wave in
SHA-256 state space.  All three return null.  The claims marked **[FORCED]**
follow directly from the computed numbers and are not interpretive.

---

## Probe K — Cumulative New-Bit Support

### Metric

Let $M_r$ denote the 256-bit XOR mask between the reference and perturbed state
after round $r$.  Define the cumulative new-bit count at round $r$ as

$$
N(r) = \mathrm{HW}\!\left( M_r \;\wedge\; \neg \bigvee_{t < r} M_t \right)
$$

that is, the number of bits active in $M_r$ that have never appeared in any
prior mask.  Average over the 32 single-bit probes within a source word to
obtain $N_k(r)$ per word $k$.

The signal-to-noise ratio for the secondary window is

$$
\mathrm{SNR}_K(k) = \frac{\displaystyle\operatorname{mean}_{r \,\in\, [k+15,\; k+21]} N_k(r)}
                         {\displaystyle\operatorname{mean}_{r \,\in\, [k+6,\; k+14]}  N_k(r)}
$$

### Results

| Word | $\text{base\_mean}$ | $\text{sec\_mean}$ | $\mathrm{SNR}_K$ |
|------|-------------------:|------------------:|----------------:|
| W[0]  | 4.7291666667 | 0.0133928571 | 0.0028319698 |
| W[1]  | 4.5590277778 | 0.0089285714 | 0.0019584376 |
| W[2]  | 5.0000000000 | 0.0044642857 | 0.0008928571 |
| W[3]  | 4.4687500000 | 0.0133928571 | 0.0029970030 |
| W[4]  | 4.4826388889 | 0.0044642857 | 0.0009959057 |
| W[5]  | 4.2812500000 | 0.0223214286 | 0.0052137643 |
| W[6]  | 4.9930555556 | 0.0446428571 | 0.0089409895 |
| W[7]  | 4.1631944444 | 0.0089285714 | 0.0021446443 |
| W[8]  | 4.4791666667 | 0.0044642857 | 0.0009966777 |
| W[9]  | 4.6076388889 | 0.0223214286 | 0.0048444397 |
| W[10] | 4.4409722222 | 0.0223214286 | 0.0050262482 |
| W[11] | 4.3715277778 | 0.0357142857 | 0.0081697492 |
| W[12] | 4.6250000000 | **0.0000000000** | **0.0000000000** |
| W[13] | 4.8506944444 | **0.0000000000** | **0.0000000000** |
| W[14] | 4.8958333333 | 0.0401785714 | 0.0082066869 |
| W[15] | 4.4756944444 | 0.0178571429 | 0.0039898038 |

$$
\overline{\mathrm{SNR}}_K = 0.0035755736, \qquad \max_k \mathrm{SNR}_K(k) = 0.0089409895
$$

### W[12] and W[13] exact-zero audit

The secondary-window values for W[12] and W[13] were printed as `0.0000` in
the earlier scan.  The precision audit confirms this is not a display artifact:
every individual round value `new_prof[k, r]` in the secondary window rounds
27–33 (W[12]) and 28–34 (W[13]) is exactly `0.0` in IEEE 754 float64
accumulation.  Not one of the 14 affected per-round values is nonzero.

$$
N_{12}(r) = 0.0 \;\text{ for all } r \in [27, 33], \qquad
N_{13}(r) = 0.0 \;\text{ for all } r \in [28, 34]
$$

These two words are in the $P = 3$ path-multiplicity regime.  Their exact zeros
are consistent with the saturation picture: the support manifold for W[12] and
W[13] is more completely exhausted by round 27–28 than for most other words.
No special structural significance is claimed beyond this. **[FORCED: literal
float64 zeros, not rounding]**

### Verdict

**[FORCED]** The cumulative new-bit rate has collapsed to effectively zero before
the secondary window for every input word.  The reachable support manifold is
exhausted by the primary injection wave.  Secondary re-injection at $t = k + 16$
does not open a second support-expansion front.

---

## Probe L — Amplitude Inside Support

### Metrics

For each round $r$ and word $k$, compute four secondary/baseline ratios using
the same window boundaries as Probe K:

$$
R_{\mathrm{active}}(k) = \frac{\operatorname{mean}_{r \in [k+15,\; k+21]} \mathrm{HW}(M_k(r))}
                               {\operatorname{mean}_{r \in [k+6,\; k+14]}  \mathrm{HW}(M_k(r))}
$$

$$
R_{\mathrm{toggle}}(k) = \frac{\operatorname{mean}_{r} \mathrm{HW}(M_k(r) \oplus M_k(r-1))}
                               {\operatorname{mean}_{r} \mathrm{HW}(M_k(r) \oplus M_k(r-1))}
\Bigg|_{\text{sec}/\text{base}}
$$

$$
R_{\mathrm{overlap}}(k) = \frac{\operatorname{mean}_{r} \mathrm{HW}(M_k(r) \wedge M_k(r-1))}
                                {\operatorname{mean}_{r} \mathrm{HW}(M_k(r) \wedge M_k(r-1))}
\Bigg|_{\text{sec}/\text{base}}
$$

$$
R_{\mathrm{new}}(k) = \mathrm{SNR}_K(k) \quad \text{(same as Probe K)}
$$

### Significance test for overlap dips

The overlap ratios at W[9], W[12], W[13] were flagged as possibly low in the
earlier scan.  A z-score test against the cross-word empirical distribution
(mean and ddof=1 std over all 16 words) is used to assess significance.

$$
z_k = \frac{R_{\mathrm{overlap}}(k) - \overline{R}_{\mathrm{overlap}}}
           {\hat{\sigma}_{R_{\mathrm{overlap}}}}
$$

### Results

| Word | $R_\text{active}$ | $R_\text{toggle}$ | $R_\text{overlap}$ | $R_\text{new}$ | $z_k$ |
|------|------------------:|------------------:|-------------------:|---------------:|------:|
| W[0]  | 1.013708 | 1.010999 | 1.017772 | 0.002832 | +1.050 |
| W[1]  | 0.977335 | 0.974487 | 0.980434 | 0.001958 | −0.727 |
| W[2]  | 1.010478 | 1.011747 | 1.012451 | 0.000893 | +0.797 |
| W[3]  | 1.005402 | 0.988614 | 1.017149 | 0.002997 | +1.020 |
| W[4]  | 0.998316 | 0.985289 | 1.012928 | 0.000996 | +0.820 |
| W[5]  | 0.993599 | 1.002477 | 0.990250 | 0.005214 | −0.260 |
| W[6]  | 0.999551 | 1.004526 | 0.993313 | 0.008941 | −0.114 |
| W[7]  | 0.980625 | 0.989616 | 0.970536 | 0.002145 | −1.198 |
| W[8]  | 1.011131 | 1.009389 | 1.013780 | 0.000997 | +0.860 |
| W[9]  | 0.990132 | 1.013312 | 0.962814 | 0.004844 | −1.565 |
| W[10] | 0.990328 | 1.003060 | 0.976947 | 0.005026 | −0.893 |
| W[11] | 1.006199 | 1.004352 | 1.009769 | 0.008170 | +0.669 |
| W[12] | 0.985817 | 1.002880 | 0.971622 | 0.000000 | −1.146 |
| W[13] | 0.991645 | 1.016587 | 0.973507 | 0.000000 | −1.056 |
| W[14] | 1.008484 | 0.991457 | 1.029780 | 0.008207 | +1.621 |
| W[15] | 1.003619 | 1.006269 | 0.998255 | 0.003990 | +0.121 |

$$
\overline{R}_{\mathrm{active}} = 0.9979, \quad
\overline{R}_{\mathrm{toggle}} = 1.0009, \quad
\overline{R}_{\mathrm{overlap}} = 0.9957 \;(\hat\sigma = 0.0210), \quad
\overline{R}_{\mathrm{new}} = 0.0036
$$

No word exceeds $|z| = 2.0$ for the overlap ratio.  The dips at W[9], W[12],
W[13] are not statistically distinguishable from ordinary cross-word variation
under the z-score criterion.  **[FORCED]**

### Verdict

**[FORCED]** $R_\text{active}$, $R_\text{toggle}$, and $R_\text{overlap}$ are all
within approximately 3% of 1.0 across all words.  The amplitude level and mask
geometry inside the saturated support are unchanged by secondary re-injection.
There is no second amplitude wave.  The only ratio that departs from 1.0 is
$R_\text{new} \approx 0.004$, which is consistent with and implied by Probe K.

---

## Probe M — Phase-Selective Support Echo

### Metrics

For each word $k$ and lag $L$, compute the mean Jaccard and cosine similarity
between the round-$r$ mask and the round-$(r+L)$ mask:

$$
J_k(L) = \operatorname{mean}_{r=0}^{63-L} \frac{|M_k(r) \wedge M_k(r+L)|}{|M_k(r) \vee M_k(r+L)|}
$$

$$
C_k(L) = \operatorname{mean}_{r=0}^{63-L}
          \frac{|M_k(r) \wedge M_k(r+L)|}{\sqrt{\mathrm{HW}(M_k(r)) \cdot \mathrm{HW}(M_k(r+L))}}
$$

Averages are over 32 single-bit probes per word.  Lags $L \in \{10, 11, \ldots, 24\}$.

### Control design — eliminating the monotone-decay artifact

The mask similarity profile is monotone-decreasing in $L$: more separated
rounds are less correlated.  Consequently, $J_k(16) > \operatorname{mean}_{L \neq 16} J_k(L)$
trivially whenever the control set contains many lags $L > 16$.  A global-mean
control therefore confounds lag-16 resonance with monotone decay.

The correct null test uses the local adjacent-lag interpolant as control:

$$
\Delta J_{16}^{\mathrm{local}}(k) = J_k(16) - \tfrac{1}{2}\bigl[J_k(15) + J_k(17)\bigr]
$$

A genuine phase echo at period 16 would appear as a systematic positive
deviation in $\Delta J_{16}^{\mathrm{local}}$ across words, and would produce
peaks at $L = 16$ in the per-word argmax.

### Results

| Word | $J_\text{peak}$ | $J_k(15)$ | $J_k(16)$ | $J_k(17)$ | $\Delta J_{16}^\text{local}$ | $\Delta C_{16}^\text{local}$ |
|------|----------------:|----------:|----------:|----------:|-----------------------------:|-----------------------------:|
| W[0]  | 11 | 0.3170783 | 0.3168038 | 0.3185732 | −0.0010219 | −0.0010656 |
| W[1]  | 10 | 0.3099951 | 0.3102901 | 0.3063069 | +0.0021391 | +0.0025683 |
| W[2]  | 10 | 0.3019286 | 0.3035361 | 0.3019619 | +0.0015908 | +0.0017003 |
| W[3]  | 10 | 0.2954626 | 0.2958664 | 0.2939559 | +0.0011571 | +0.0014294 |
| W[4]  | 11 | 0.2852572 | 0.2860522 | 0.2833274 | +0.0017599 | +0.0016062 |
| W[5]  | 11 | 0.2816563 | 0.2799083 | 0.2833408 | −0.0025903 | −0.0029449 |
| W[6]  | 10 | 0.2756262 | 0.2764559 | 0.2741520 | +0.0015667 | +0.0021291 |
| W[7]  | 10 | 0.2697998 | 0.2688620 | 0.2687274 | −0.0004016 | −0.0004579 |
| W[8]  | 11 | 0.2623664 | 0.2640145 | 0.2620395 | +0.0018116 | +0.0023539 |
| W[9]  | 10 | 0.2545209 | 0.2546108 | 0.2522783 | +0.0012112 | +0.0011229 |
| W[10] | 10 | 0.2500787 | 0.2468612 | 0.2442627 | −0.0003095 | −0.0006488 |
| W[11] | 10 | 0.2411822 | 0.2383952 | 0.2379343 | −0.0011630 | −0.0011885 |
| W[12] | 11 | 0.2338693 | 0.2323601 | 0.2274270 | +0.0017119 | +0.0018302 |
| W[13] | 10 | 0.2284903 | 0.2266245 | 0.2260826 | −0.0006620 | −0.0009671 |
| W[14] | 10 | 0.2221347 | 0.2211963 | 0.2171356 | +0.0015612 | +0.0019226 |
| W[15] | 10 | 0.2134383 | 0.2120865 | 0.2100584 | +0.0003382 | +0.0004844 |

$$
\overline{\Delta J_{16}^{\mathrm{local}}} = +0.00054, \quad
\hat\sigma_{\Delta J} = 0.00135, \quad
\text{(mean/std ratio: } 0.40\text{)}
$$

$$
\text{words peaking at } L = 16: \quad 0 \,/\, 16
$$

The global-mean control gives $\overline{\Delta J_{16}^{\mathrm{global}}} = +0.00279$,
but this value is a monotone-decay artifact and does not constitute evidence
of a lag-16 resonance; it is retained only for reference.

### Verdict

**[FORCED]** No phase-locked support echo at lag 16.  The local-control mean
advantage ($+5.4 \times 10^{-4}$) is well within one standard deviation across
words ($1.35 \times 10^{-3}$), indicating no systematic lag-16 elevation
above the monotone-decay baseline.  The similarity profile peaks at lags 10–11
for all 16 words; lag 16 is never the argmax.

---

## Combined State-Space Closure

Three independent observable classes:

| Probe | Class | Metric | Result | Status |
|-------|-------|--------|--------|--------|
| K | Support-growth | $\overline{\mathrm{SNR}}_K$ | $0.0036$ | **NULL** [FORCED] |
| L | Amplitude-wave | $\overline{R}_\text{active/toggle/overlap}$ | $\approx 1.000$ | **NULL** [FORCED] |
| L | Overlap dips | $\max_k |z_k|$ | $1.62 < 2.0$ | **not significant** [FORCED] |
| M | Phase-echo | $\overline{\Delta J_{16}^\text{local}}$ | $+5.4\times10^{-4} < \hat\sigma$ | **NULL** [FORCED] |

The joint conclusion is:

> Secondary re-injection at $t = k+16$ is algebraically certain in schedule
> space — Probe N measures $\mathbb{E}[\mathrm{HW}(\Delta W[k+16])] \approx 4.910$
> bits, rising to $\approx 16$ bits at $t = k+32$.  Under all three observable
> classes defined above it produces no detectable second wave in state space.
> Primary injection is support-forming; later injections are support-revisiting.

The remaining open object is the projection law

$$
\Delta W[t] \;\longrightarrow\; \Delta S[r]
$$

and the criterion separating schedule-space echoes that are support-forming
from those that are state-subcritical due to saturation.
