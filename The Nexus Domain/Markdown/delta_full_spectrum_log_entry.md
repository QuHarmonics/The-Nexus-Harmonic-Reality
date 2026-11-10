# Append-only section 11: complete Walsh spectrum of Delta, including DC

This entry records a new independent audit. It does not re-open the already executed full seam/interior profiles. SHA remains parked.

## Convention

All coefficients are unnormalized: hat f(s)=sum_x f(x)(-1)^(s dot x). Delta(p)=sum_(x<p)c(x), c(x)=sgn(J(x)-x), p=0,...,N-1 and N=2^n.

## Inclusive-prefix kernel

For s!=0 set j=LSB(s), e_k=2^k. The kernel K(s,t)=N^(-1)sum_x chi_t(x)sum_(p<=x)chi_s(p) is zero except

K(s,s)=1/2,
K(s,s xor e_j)=2^(j-1),
K(s,s xor e_k)=-2^(k-1), 0<=k<j.

The j=0 factor is 1/2. These are statements about the kernel before the comparator's parity support is used. The high-block sum fixes agreement above j; the low-block inclusive tent has only these Walsh modes.

## Every nonzero coefficient

For odd popcount(s): 2 hat Delta(s)=-hat c(s).
For nonzero even popcount(s):

2 hat Delta(s)=-2^j hat c(s xor e_j)+sum_(k<j)2^k hat c(s xor e_k).

The comparator coefficient itself is scalar-readable: the support mask must have exactly one unequal mirrored pair, any complete pairs outside it, no inside bits, and no odd-width middle bit. Its sign and magnitude are fixed by that unique pair. Thus no full spectrum is required for a requested Delta coefficient.

The universal bit-zero-toggle shortcut remains a DEAD END; it is not the same as toggling the least set bit plus the lower-bit terms. Example n=3,s=6: chat(4)=4,chat(7)=0, giving Deltahat(6)=-4.

## DC is also closed

Since sum c=0,

Deltahat(0)=-sum_x x*c(x)=sum_k 2^(k-1)*chat(2^k).

Substitute the known singleton comparator coefficients, and write h=floor(n/2):

Deltahat(0)=N^2*(1-4^(-h))/6-N*h/4
           =N*(4N-3n-4-(n mod 2))/24.

This equals the direct prefix area and the reversal-pair distance sum. At n=20 it is 183,249,141,760. The normalized DC coefficient is this value divided by N.

## Execution

All 2,097,148 modes at widths 2,...,20 matched direct full Walsh transforms. All 2,035 nonzero kernel rows at widths 2,...,10 matched direct inclusive-prefix transforms, including all their zero entries. All four DC expressions agreed at every tested width. The scalar mode reader was exhaustively checked through width 12 and additionally on deterministic modes thereafter; constructed nonzero-mode checks ran through width 1024 without full arrays. Fifty modes at n=13,14 were independently evaluated through direct dyadic-tent integration. No executed assertion failed.

At width 20, c has 2,046 nonzero coefficients and Delta has 6,109 nonzero coefficients. These are word-value-domain spectra; they are not automatically the spectra of the physical ring-address carrier.

## Ledger update

- Complete inclusive-prefix kernel: SEALED, RUNS in the stated domain, with its algebraic derivation.
- All nonzero Delta coefficients, odd and even: SEALED, RUNS.
- DC/zero-mode closed form: SEALED, RUNS.
- Compact standalone formula for the complete Delta spectrum: CLOSED within this defined arithmetic problem.
- Seam/interior/body results keep their already-executed status; older OPEN-to-RUN drafts remain historical, not current.
- Profile-language regularity, full A(q_D) union-over-blocks and physical PULL claims retain their previous statuses.

## Provenance

The new source and prediction files were hashed before execution and rechecked afterward. Hashes cover literal bytes including final newlines. This does not verify the user's separate reported source files or seals. The scalar convenience reader is a derivative module, not the sealed audit source.

Source SHA-256: 8c866820ca9c8cf87097954cf1b5450c2e1c1348e2ca1c4d58c36ef4821bf7ee
Prediction SHA-256: f3275b7b05c81590907b35f50d7d03843edbb149cfd638b28ef3964646bfa61d
