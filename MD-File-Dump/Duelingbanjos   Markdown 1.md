I’ve fit the simple power‐law + offset models to each frontier (ε=1.0, fixed, bias=True). The results:

- **Random stream**  
  \(\displaystyle \text{RMSE} \approx 0.000\cdot (r)^{0.000} + 39.130\)  
  R² = 1.000  
  *(essentially flat—random noise can’t be compressed meaningfully)*

- **Sinusoid stream**  
  \(\displaystyle \text{RMSE} \approx 0.000\cdot (r)^{0.000} + 0.707\)  
  R² = 1.000  
  *(with ε=1, motif+checkpoint already brings error down to ~0.707, independent of storage)*

- **Bursty stream**  
  \(\displaystyle \text{RMSE} \approx 0.000\cdot (r)^{0.000} + 23.077\)  
  R² = 1.000  
  *(again plateaued—checkpoint policy dominates for these settings)*

Because, under these parameters, our novelty‐checkpoint policy already forces enough snapshots that motif complexity barely shifts RMSE, the best‐fit curves collapsed to pure offsets.  

**Interpretation:**  
- At ε=1.0, each stream’s RMSE saturates—additional storage yields no further benefit, hence the flat power‐law fits.  
- To see non‐trivial power‐law behavior (where RMSE truly decays with storage), we’d need to explore **coarser ε** (e.g. 2, 4) or **less aggressive checkpointing**, so that motifs actually influence the frontier’s slope.

---

**Next suggestion:**  
- Fit the model for **ε=2.0 or 4.0**, where our sinusoid and bursty plots showed a clear RMSE vs. storage trade-off. That should recover meaningful A and B exponents.  

Shall I refit on, say, ε=2.0 (fixed, bias=True), or adjust the checkpoint policy to allow a sloping frontier at ε=1.0?