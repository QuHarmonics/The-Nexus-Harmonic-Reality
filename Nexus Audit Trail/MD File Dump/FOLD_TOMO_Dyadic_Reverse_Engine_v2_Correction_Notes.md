# Dyadic Tomography Reverse Engine v2 — Correction Notes

**Corrected from:** `dyadic_tomography_reverse_engine_v1.pdf`  
**Branch:** `FOLD-TOMO`  
**Fix target:** align the old prototype with the current finite-cone / fractional-$\pi$ FOLD-TOMO lock.

## Fixes

1. **Skip the leading `3`.** Use the first $2048$ digits after the decimal point:
   $$D^{(0)}=(1,4,1,5,9,\ldots).$$

2. **Use finite open cone, not circular wrap.**
   $$x_i^{(\ell+1)}=x_i^{(\ell)}\oplus x_{i+1}^{(\ell)},\qquad N_\ell=2048-\ell.$$

3. **Use terminal rows of length $2^k$, not 2048 cyclic constraints.**
   $$x_i^{(N-2^k)}=\bigoplus_{q=0}^{2^{m-k}-1}x_{i+q2^k}^{(0)},\qquad 0\le i<2^k.$$

4. **Exclude the identity level.** For $N=2048=2^{11}$, use $k=0,1,\ldots,10$, not $k=11$.

5. **Correct rank locks.**
   $$\operatorname{rank}(C_{\mathrm{dyadic}})=1024,$$
   $$\operatorname{rank}\begin{bmatrix}C_{\mathrm{dyadic}}\\C_{448}\end{bmatrix}=1600,$$
   $$2048-1600=448.$$

6. **Correct residue counts.**
   $$R=0:44,\qquad R\ne0:2004.$$
   Interior window $20\le\ell<1800$:
   $$R=0:30,\qquad R\ne0:1750.$$

7. **Mark-9 / $H=\pi/9$ phase checkpoint.**
   $$H=\frac{\pi}{9},\qquad 9H=\pi,\qquad 18H=2\pi.$$
   On the $64n$ ladder:
   $$\ell_9=9\cdot64=576.$$
   Since:
   $$576=512+64,$$
   $$M_{576}=\{0,64,512,576\}.$$
   Verified:
   $$N_{576}=1472,\qquad S_{576}=749,\qquad R_{576}=13.$$

Final lock:

$$
\boxed{
\text{The old cyclic prototype is fixed into the finite-cone fractional-}\pi\text{ FOLD-TOMO engine.}
}
$$
