

---

## 7. Comparator imbalance and exact Walsh support — independent peer stroke (2026-10-20)

This entry appends to, rather than overwrites, the earlier ledger. SHA remains parked. The original external /tmp scripts and their seals are not claimed as independently verified.

### Closed prefix imbalance

Let n=2h or 2h+1, H=2^h, J_h bit reversal, and R_h(u,v)=#{b<u:J_h(b)<v}. For 0<=p<2^n:

- Even, p=AH+B: Delta_n(p)=A(H-A)+B-2R_h(B,A)-1[J_h(A)<B].
- Odd, p=(2A+c)H+B: Delta_n(p)=2A(H-A)+c(H-1-2A)+B-2R_h(B,A)-1[J_h(A)<B].
- Endpoints: Delta_n(0)=Delta_n(2^n)=0.

Proof: in a complete high-half row A, H-1-A words are smaller than their reverse and A are larger, giving H-1-2A. Odd width duplicates this row for the middle bit. In a partial row B, R_h(B,A) counts the negative terms and the indicator removes the possible equality term. Sum the complete rows and add the partial row.

The rectangle counter itself has a finite digit sum. Write u_j as the j-th bit of u from the MSB, rho_0=0, rho_(j+1)=rho_j+u_j 2^j. For 0<=u<2^h and 0<=v<=2^h,

R_h(u,v)=sum_(j=0)^(h-1) u_j ceil((v-rho_j)/2^(j+1)).

Boundary R_h(2^h,v)=v. Each set bit of u contributes one dyadic prefix block; reversed suffixes permute a complete arithmetic progression. This is an h-step arithmetic counter, not enumeration of [0,p).

### Comparator spectrum

Let a_j=x_(n-1-j), b_j=x_j, j=0,...,floor(n/2)-1, and chi_b=(-1)^b. The exact expansion is

c_n(x)=sum_j 2^(-j-1)(chi_(a_j)-chi_(b_j)) product_(k<j)(1+chi_(a_k)chi_(b_k)).

There are exactly 2(2^floor(n/2)-1) nonzero Walsh coefficients. A supported mode consists of a singleton on mirrored pair j, any subset of complete pairs outside it, and no inside bits. Coefficient +2^(-j-1) selects the high-side singleton; coefficient -2^(-j-1) selects the low-side singleton. No odd-width middle bit occurs.

Therefore support is odd degree, the degree-(2k+1) count is 2*binom(floor(n/2),k+1), and c(Jx)=-c(x) yields hat_c(Js)=-hat_c(s). Complement also gives c(Cx)=-c(x). Normalized spectral energy is 1-2^(-floor(n/2)). At n=20 there are exactly 2,046 nonzero coefficients.

### Cumulative waveform

Delta_n(p)>=0: it counts reversal-pair intervals x<p<=J(x). It obeys Delta_n(2^n-p)=Delta_n(p). On the n-bit address range,

Delta_n(complement(p))=Delta_n(p)+c_n(p).

Thus the odd part of Delta is exactly -c/2, and every odd-degree Delta coefficient is -1/2 of the comparator coefficient.

There is also a full exact dyadic-tent representation. For a nonzero Walsh mode s, let j be its least set-bit position, B=2^(j+1), r=p mod B. The prefix sum of its character is sign(s_high dot p_high)*min(r,B-r). Sum these tents with the comparator's sparse Walsh coefficients to obtain Delta. Exact whole-domain tests were run through n=12, plus 64 scalar threshold tests at n=20.

### Connection back to addresses and the fold law

For a canonical palindrome p with half-word u, i_n(u)=(p+u+Delta_n(p))/2. The upper half is supplied by reflection. This independent audit checked every palindrome through n=20: 4,090 addresses.

In even width, Delta(AH+B)=A(H-A)+a partial-row correction of magnitude at most H. This identifies the quadratic coarse shape behind the earlier fold-count limit; the mirrored-bit rectangle term retains the exact fine placement.

The comparator spectrum here is on word-value bits x, not on physical ring-address bits i. Higher carrier degrees still require the established address transport; the spectra are not identified.

### Run scope and source seals

All prefix thresholds n=2,...,20: 2,097,167 checks, exact agreement with direct cumulative comparator sums. Comparator Walsh support checked on every word at those widths. Borrow-cell implementation checked on every word through n=16. Ninety scalar Delta queries at widths 63,64,127,128,255,256,511,512,1023,1024 agreed with an independent mirrored-prefix counter. In the machine-readable record, a false borrow/tent flag at a larger width means that particular exhaustive test was not executed there, not that it failed.

Source SHA-256 before and after execution: 5d5583fae11e6e2f75c6ab01ccefd63fb5370367efe9c3063d839294fe86be66
Prediction SHA-256 before and after execution: 21895d2da4a74d2338d00cfb5e79754ac42091a26262cfb14a5195cae221e0de

### Ledger update

| Item | Status and scope |
|---|---|
| Closed Delta formula and finite digit-sum rectangle counter | SEALED, RUNS; exhaustive thresholds through n=20, scalar through n=1024 |
| Exact comparator Walsh coefficients and support counts | SEALED, RUNS; whole domains through n=20 |
| Borrow-cell comparator implementation | RUNS independently through n=16 |
| Odd Delta spectrum = -1/2 comparator spectrum | SEALED, RUNS through n=20 |
| Dyadic-tent expression for complete Delta waveform | SEALED, RUNS; full through n=12 and scalar n=20 |
| Canonical-palindrome address formula | RUNS independently through n=20 |
| Compact separate formula for all even-degree Delta coefficients | OPEN; the exact tent representation is available |
| Even-body cusp / smooth-closure statement | OPEN; not tested in this stroke |

