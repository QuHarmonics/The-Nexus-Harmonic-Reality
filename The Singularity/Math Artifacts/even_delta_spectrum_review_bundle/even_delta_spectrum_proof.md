# Exact Walsh spectrum of the comparator-prefix imbalance

## Scope and conventions

For width `n`, let `N=2^n`, `J_n(x)=rev_n(x)`,

`c_n(x) = sgn(J_n(x)-x)`,

and

`Delta_n(p) = sum_{0 <= x < p} c_n(x)` for `0 <= p < N`.

All Walsh transforms here are **unnormalized**:

`f_hat(s) = sum_{x=0}^{N-1} f(x) (-1)^(s dot x)`.

Set `e_k=2^k`. For nonzero mask `s`, let `j=LSB(s)`, the index of its least significant set bit.

## 1. Exact prefix kernel

Define

`S_s(x) = sum_{p=0}^{x} chi_s(p)`,

`K(s,t) = (1/N) sum_x chi_t(x) S_s(x)`.

For every `s != 0`, the kernel has only `j+2` possible nonzero entries:

- `K(s,s)=1/2`;
- `K(s,s xor e_j)=2^(j-1)`;
- `K(s,s xor e_k)=-2^(k-1)` for `0 <= k < j`;
- all other entries are zero.

The convention `2^(-1)=1/2` covers `j=0` and `k=0`.

Proof sketch: write `x=q*2^(j+1)+r`. Since `s` has no set bits below `j` and has bit `j` set, the inclusive character prefix is a signed triangular segment within each block. Summing over the high block index `q` annihilates every `t` except those with the same bits as `s` above `j`. The remaining low-block Walsh transform is supported at low masks `0`, `2^j`, and `2^j+2^k` for `k<j`, giving the kernel entries above.

## 2. Closed nonzero Walsh spectrum of Delta

Since `Delta(p)=sum_{x<p} c(x)`, for every nonzero `s`,

`Delta_hat(s) = -sum_x c(x) S_s(x) = -sum_t c_hat(t) K(s,t)`.

The comparator spectrum has only odd-degree support. Hence, writing `w=popcount(s)`,

**Odd `w`:**

`Delta_hat(s) = -c_hat(s)/2`.

**Even `w`:**

`Delta_hat(s) = -2^(j-1) c_hat(s xor e_j) + sum_{k=0}^{j-1} 2^(k-1) c_hat(s xor e_k)`.

This is a compact formula for every nonzero even-degree coefficient; it also retains the already established odd-degree formula. The former LSB-only shortcut failed because the exact kernel has the `e_j` correction and all `e_k` corrections for `k<j`.

## 3. The zero mode also has a closed form

The zero coefficient is the total prefix area:

`Delta_hat(0) = sum_p Delta(p) = -sum_x x c(x)`.

Use `x=(N-1)/2 - sum_k 2^(k-1) chi_{e_k}(x)` and `sum_x c(x)=0` to obtain

`Delta_hat(0) = sum_k 2^(k-1) c_hat(e_k)`.

From the sparse mirrored-pair expansion of `c`, with `h=floor(n/2)`, the singleton coefficients are

`c_hat(e_{n-1-j})=N/2^(j+1)`,

`c_hat(e_j)=-N/2^(j+1)`, for `0 <= j < h`; an odd-width middle singleton is zero.

Summing those terms yields

- if `n` is even: `Delta_hat(0)=N(N-1)/6 - h*N/4`;
- if `n` is odd: `Delta_hat(0)=N(N-2)/6 - h*N/4`.

Both expressions are integers for the stated widths.

## 4. Executed audit and scope

A pre-run prediction file and source were hashed before execution. The exact audit passed:

- all nonzero Delta Walsh coefficients at widths 2–12: **8,177** coefficient comparisons;
- comparator Walsh coefficients at widths 2–12: **8,188** coefficient comparisons, each matching the analytic sparse mirrored-pair expansion;
- direct prefix-kernel entries at widths 2–8: **86,868** `(s,t)` pairs;
- zero-mode formula at every width 2–20: **19** direct prefix-area checks;
- failed executed assertions: **0**.

The source SHA-256 before and after execution is `982f6838dab82a3ff2a0c51ed4520f0abdadc7aabd096443d045b3d9251bebc2`. The sealed prediction SHA-256 is `2f7d21a88107b4147843d550cdd0689f22e197b5760a0fe1050787631fee01c7`.

The audit uses exact integer/Fraction arithmetic and unnormalized Walsh transforms. It does not make a physical-spin claim or any SHA inversion claim.

## 5. Ledger interpretation

- Exact nonzero prefix kernel: **SEALED, RUNS** in the audited widths.
- Closed formula for every nonzero `Delta_hat(s)`, including even degrees: **SEALED, RUNS** at widths 2–12.
- Zero-mode closed form: **SEALED, RUNS** at widths 2–20.
- The former LSB-toggle-only shortcut: **DEAD END**, superseded by the full sparse kernel.
- Profile-language regularity, full `A(q_D)` union, and physical interpretation: unchanged and still **OPEN/PULL**.
