# Compiler Rings — Running Log

Dean A. Kulik · QuHarmonics Research Group · ORCID 0009-0003-3128-8828
Started 2026-10-20. Append newest entries at the bottom. Ledger words: STANDS, RUNS, SEALED, DEAD END, OPEN, PULL. Never CONFIRMED.

---

## 0. Base held from the corpus

Source papers: *Only Addressable*, *Decompiling Addressable Binary Rings* (plus *The Way Home in a Finite Scope*, *Algebraic Routing*, *Where Yes and No Become Maybe*, *The Geometry of a Readout*, *The Reading of Potential*).

- Partner P(x) = J(x) (reversal) if J(x) ≠ x, else C(x) (complement). Fixed-point-free involution; 2^(L−1) pairs; palindromes pair among themselves. STANDS.
- Ring R_L: representatives (x < P(x)) ascending on the left face, partners descending on the right, centre pair at M−1, M swapped. Facing law R[N−1−i] = P(R[i]). STANDS.
- Location of any word in O(L), word at any position in O(L²). STANDS / RUNS (π at L = 64, seeded word at L = 512).
- Lemma A: μ(2^h − 1 − ℓ) representatives share left half ℓ ≥ 2^(h−1). Triangular top, core ≈ log₂ j. Theorem C (clean cores), Theorem D (pad law L → L+2), Theorem E (witness law for q_D = 100 1^(D−5) 00, D ≥ 13). STANDS.
- Open on entry: the map from ring L to ring L+1 (pad law skips the odd ring); regularity of the profile language; full A(q_D).

---

## 1. The L → L+1 link (2026-10-20)

**Even → odd.** Inserting the middle bit is the whole step. The middle bit is compared only with itself, so it is the first free bit of every block. Odd block K = even block K twice, middle 1 then middle 0. RUNS (top quarter, L = 4–18; peer: exhaustive, 262,144 odd children at width 19).

Offsets (peer, full form with palindromes): H = 2^h, K = H − 1 − A,
- D_K = K(K−1)/2 + max(0, K − H/2), s_K = K + 1[K ≥ H/2]
- j_even = D_K + i → j₁ = 2D_K + i, j₀ = 2D_K + s_K + i. RUNS.
- Before palindromes enter: j₁ = K(K−1) + i, j₀ = K² + i.

**Readout.** Q_{L+1}(I₀(a)) = Q_{L+1}(I₁(a)) = Q_L(a) with a 0 at the middle (all ones for palindromes). The readout cannot say which child; the middle bit is the qualifier (the value kept beside the difference). AMBIGUOUS → bound by the lift.

**Odd → even.** The middle-1 half carries forward by deletion and padding; pad law = this step twice. The middle-0 half was the piece with no way home. OPEN at that point.

---

## 2. Filling the middle-0 slot: E/G lift (2026-10-20)

Two peer providers, same partition of A_{L+2} by outer frame (00/11 vs 01):

- **E/G:** E_m(x) = canon(m x m), G_m(x) = 0 P^m(x) 1. Partitions all 2^(L+1) canonical words at width L+2. RUNS (L = 2–18, target width 20, seal `ab543c24…7a39a7fb0`).
- **Four-family table:** F(A) ∪ 0A0 ∪ 0A1 ∪ 0P(A)1 with a stored branch label. Binds too.

**Labeling forced:** in E/G the branch bit d = a ⊕ c is the residual of the new outer pair, and m is readable off the word (frame bit if d = 0, palindrome exception aside; core face if d = 1). RUNS (L = 2–16, zero failures). E/G STANDS as the readable gauge; the four-family table needs a stored label.

Reading: even → odd inserts a pure value (residual 0); odd → even inserts a pair carrying (value, difference) = the butterfly (u, u ⊕ v). When d = 1 the frame is full and m moves inward into the core's face. The homeless middle-0 piece is the value that leaves the frame.

**DEAD END, routed to its owner:** route codes of SHA digests and source blocks belong to the codec (a fixed L-bit ↔ L-bit bijection), not to SHA-256. Block-to-digest in route coordinates is SHA-256 conjugated by two relabelings; no change in preimage cost. SHA parked by Dean (2026-10-20).

---

## 3. Route ↔ word ↔ rank ↔ address (peer closure)

- Route code: width-2 root, then m on odd steps, d on even steps, final side bit ε. Exactly L bits. RUNS (widths 2–18).
- q = 2^(L−1) − 1 − r_L(a); p_L(q) = M if q = 0, else M − 1 − q; address i = p_L(q) if ε = 0, else 2^L − 1 − p_L(q). RUNS (exhaustive to width 10–12, scalar at 64, 256, 512; cross-bundle 8,188 words, seal `ee827844…03020b`).
- Mixed-end offset Q_L(z) = C(2H−1−A, 2) + (H−1−A) + 2(H−1−B) − A + ℛ_h(B+1, A), with ℛ_h(u,v) = #{b < u : J_h(b) < v}. q(G₀) = Q_L(x), q(E₀) = Q_L(x)+1, q(G₁) = Q_L(P(x)); q(E₁) = j − s_L(x) (non-palindrome) or Q_L(P(x))+1 (palindrome). RUNS (seal `75ca9d28…aec1eb6cf`).
- Within-weight-band rank: β = C(n,w) − H_w(a+1), H_w = C_w − T_w + T_{n−w}. RUNS (65 bands).
- Address mechanism is now a provider, not an open link.

---

## 4. The sphere (2026-10-20)

Coordinates: radius r = n, latitude z = w − n/2 (Z = 2z), azimuth θ_i = 2π((i + ½)/2^n − ½), ρ = √(n² − 4z²).

- **Partner on the sphere:** P : (θ, z) ↦ (−θ, z) for non-palindromes, (−θ, −z) for palindromes. Cartesian: (X, −Y, Z) and (X, −Y, −Z). RUNS (all words, widths 2–20, 228 bands).
- **Correction logged:** I first called this an azimuthal half-turn and the palindrome action an antipode. Both wrong. It is an azimuthal reflection, and on palindromes a half-turn about the X-axis; equal to the antipode only at the poles. Half-turn impossible at every n ≥ 2: 2i ≡ N/2 − 1 (mod N) has odd right side. STANDS.
- **Lift as a spin-½ walk:** z_odd = z_even + (m − ½); z_child = s·[z_odd + (m − ½)(−1)^d], s = −1 iff the core is palindromic and m = 1. RUNS (699,048 outputs, zero failures, seal `4277c3f1…e607d8f`). Sign-reflected transitions: 2^(L/2) from source width L = 2^(n/2−1) at target width n.
- Reflection covariance: P(I_m(x)) = I_{m⊕p(x)}(P(x)); P(T_m(x)) = T_{m⊕p(x)}(P(x)); P(G_m(x)) = 1 J(P^m(x)) 0. RUNS.
- **Correction logged:** C(n,w) counts weight-w words (fixed-weight basis states), not the symmetric spin sector (dimension n+1). Physical spin reading stays PULL.
- K is monotone on each oriented face; the full band folds back (n = 6, w = 3 sequence 7,6,6,6,5,5,5,4,3,3,3,3,4,5,5,5,6,6,6,7). RUNS.

---

## 5. Waveforms (2026-10-20)

**Walsh parity split.** Partner address N−1−i = i ⊕ (N−1), so complementing the address multiplies Walsh coefficients by (−1)^|s|. Latitude waveform z(i): non-palindromes carry only even Walsh degrees, palindromes only odd. Odd energy share = 2^(1−n/2) (even n), (4h+1)/((2h+1)2^h) (n = 2h+1).
SEALED `be9c1901…bfa652c` · RUNS exactly n = 2–20 (1/4 at 6, 13/56 at 7, 1/512 at 20). Peer rerun RUNS.

**Half-width carrier (OPEN 1 resolved).**
- Literal order copy: DEAD END for n ≥ 3. Palindromes in ring order read their half-words in counting order 0, 1, …, 2^m − 1, not R_m order. STANDS as a failure with its reason.
- Re-addressed waveform copy: z_{2m}(i(R_m(j))) = 2 z_m(j); z_{2m−1}(…) = 2 z_m(j) + ½ − lastbit. RUNS.
- In half-word coordinates the carrier has Walsh degree 1 only: Z = −2 Σ χ_j (odd n: middle term −1). All higher odd degrees come from the address placement i_n(u). RUNS.
- Scalar placement (even n, u < H/2): i_{2m}(u) = uH − u(u−1)/2 + B − ℛ_m(B, u+1), B = J_m(u); upper half by i_n(u) = 2^n − 1 − i_n(2^m − 1 − u). RUNS (4,090 addresses to width 20; 40 checks to width 1,024).
- Complementing the half-word ≠ the half ring's native partner from half-width 3. So waveform nesting STANDS; unchanged-spectrum nesting does not follow.

**Spectral transport (peer).** S_n places the half-word signal at palindrome addresses; T_n = H_N S_n H_M, Tᵀ T = I (CᵀC = NM·I exact, n = 2–12). Parity preserved (C_{s,t} = 0 when |s| ≢ |t| mod 2), degree mixed within parity. Carrier = combination of m singleton columns; factored filter b = AᵀF/(NM), F_carrier = Ab returns the carrier exactly. RUNS.
First degree mixing at n = 5: i₅(u) = 4u + 2u₂ + Maj(1 − u₀, u₁, u₂). RUNS.

---

## 6. The address is a comparator (2026-10-20)

Gap named: a gate-level description of i_n(u) across widths. The majority with one complemented input is a borrow cell, so the address must be a comparator count.

For a canonical palindrome p with half-word u:
- **P1:** i_n(u) = (p + u + Δ(p)) / 2, with Δ(p) = #{x < p : x < J(x)} − #{x < p : x > J(x)}. Upper half by reflection.
- **P2:** c(x) = sgn(J(x) − x) = borrow(x − J(x)) − borrow(J(x) − x), where the borrow is the ripple chain of cells Maj(¬a, b, borrow_in). The n = 5 majority is the first such cell.

SEALED `5910642e…12438bfb` (seal text in /tmp/r5/seal.txt) · P1 RUNS n = 2–20 (every palindrome, materialized ring) · P2 RUNS on every word n = 2–16.

Reading: the palindrome sits at half of (its own value + palindromes below + comparator imbalance below). The nonlinear part of the address, and hence every higher odd Walsh degree in the carrier, is the running sum of one waveform: the comparator sign c(x) of each word against its reverse. The ring's gate is the subtractor's borrow, which is the full-adder carry (majority) with one input complemented. Same gate, read at a different location.

---

## Ledger (current)

| Item | Status |
|---|---|
| P involution, layout, facing law, Lemma A, Theorems C/D/E | STANDS |
| Even → odd middle insertion, offsets D_K, s_K | RUNS |
| E/G lift partition; d = a ⊕ c; m readable | RUNS; E/G gauge STANDS |
| Route ↔ word ↔ rank ↔ address, band rank | RUNS |
| Partner = azimuth reflection, palindrome X-axis half-turn | RUNS; half-turn impossibility STANDS |
| Spin-½ latitude walk | RUNS |
| Walsh parity split and energy law | SEALED, RUNS |
| Half-width literal order copy | DEAD END (counting order instead) |
| Re-addressed waveform copy, scalar placement | RUNS |
| Spectral transport, singleton-column carrier, filter | RUNS |
| Palindrome address = (p + u + Δ)/2, comparator borrow chain | SEALED, RUNS |
| SHA route codes | DEAD END (codec owns them); parked |
| Physical spin / physical sphere | PULL |
| Even body shape: log cusp at seam (Lemma A), smooth closure | OPEN (sealable) |
| Spectrum of c(x) and of Δ; closed form for Δ(p) | OPEN — next |
| Regularity of the profile language (≥ 312 states) | OPEN |
| Full A(q_D) as union over blocks | OPEN |

## Open threads, next stroke

1. Δ(p) in closed form. c(x) is decided at the outermost unequal mirrored pair, so Δ over a dyadic block factors by mirrored-pair prefixes. Expected: Δ is a digit sum over the outside-in pairs of p, the same DP state the O(L) ranker already carries. Seal the formula, then run.
2. Walsh spectrum of c(x). It is odd under J (c(J(x)) = −c(x)). Derive its degree support from that symmetry before computing.
3. Even-body cusp: z(seam ± j) = n/2 − (zeros in core), clean offsets 2^s from Theorem C. Seal and run.

## Scripts and seals (this session)

- /tmp/r/link.py, link2.py — L → L+1 steps
- /tmp/r2/gauge.py — d = a ⊕ c, m readout
- /tmp/r3/sphere.py — partner on sphere, latitude walk
- /tmp/r4/walsh_split.py, seal.txt (`be9c1901…`) — Walsh parity split
- /tmp/r5/address_comparator.py, seal.txt (`5910642e…`) — comparator address
- Peer seals: `ab543c24…` (two-branch lift), `ee827844…` (route/rank), `4277c3f1…` (reflection/lift), `75ca9d28…` (position map), `1db03220…` (half-width audit)

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
Prediction text SHA-256 with the final newline removed: 21895d2da4a74d2338d00cfb5e79754ac42091a26262cfb14a5195cae221e0de. The uploaded prediction file including its final newline hashes to c560fad25fe397675b789d10a357ed5fba0320804d62284f1b9a972e4422e393.

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

---

## 8. Archive re-run and seal normalization (2026-10-20)

The `comparator_imbalance_audit.py` included in `comparator_imbalance_bundle.zip` was executed from the uploaded archive. Its exact byte SHA-256 before and after execution is `5d5583fae11e6e2f75c6ab01ccefd63fb5370367efe9c3063d839294fe86be66`, matching the source seal. The run completed with 2,097,167 prefix-threshold checks, 4,090 palindrome-address checks, 90 wide scalar threshold checks, and 64 width-20 tent spot checks; all executed assertions passed.

**Prediction-seal qualification:** the sealed digest `21895d2da4a74d2338d00cfb5e79754ac42091a26262cfb14a5195cae221e0de` matches the prediction text after removing its final newline. The literal uploaded file bytes, including that newline, hash to `c560fad25fe397675b789d10a357ed5fba0320804d62284f1b9a972e4422e393`. The normalized content matches; the byte-for-byte file does not match that digest unless the terminal newline is excluded. This is recorded explicitly rather than treating the two hashes as identical.

The machine-readable flags `borrow_gate_check=false` for widths 17–20 and `full_tent_check=false` for widths 13–20 mean those exhaustive subtests were not run at those widths. They are coverage limits, not reported failures. The full comparator Walsh transform and the closed-Delta prefix identity were still checked throughout widths 2–20.

### Current ledger snapshot

| Item | Current status |
|---|---|
| Closed even/odd `Delta_n(p)` formulas and rectangle digit sum | SEALED, RUNS; exhaustive thresholds through width 20, scalar comparisons through width 1,024 |
| Sparse comparator Walsh expansion and exact support counts | SEALED, RUNS; full transforms through width 20 |
| Odd-degree `Delta` coefficients equal `-1/2` of comparator coefficients | SEALED, RUNS through width 20 |
| Dyadic-tent representation of `Delta` | RUNS; full-width tests through width 12, plus 64 scalar checks at width 20 |
| Palindrome address `(p + u + Delta(p))/2` | RUNS; every palindrome through width 20 |
| Literal smaller-ring word order | DEAD END; half-words occur in counting order |
| Re-addressed half-width waveform and spectral transport | RUNS |
| Compact standalone formula for all even-degree `Delta` coefficients | OPEN; exact tent representation is available |
| Even-body seam cusp / smooth-closure claim | OPEN; not tested in this stroke |
| Regularity of profile language (≥312 states) | OPEN |
| Full `A(q_D)` as union over blocks | OPEN |
| Physical spin/sphere interpretation | PULL |
| SHA route-code investigation | PARKED; codec relabeling is not an inversion result |

### Next stroke

Take the even-body seam profile next. State the one-sided seam values using the existing `Lemma A` and clean-offset result, formulate the cusp/smoothness prediction before evaluating the profile, seal that prediction, and then test it. Do not infer smooth closure from the comparator or Walsh results: those prove address and waveform identities, not regularity of the seam profile.

---

## 9. Seam cusp and closure: both ends are digit sums (2026-10-20)

Gap named: the shape of the even body at its two ends, the seam (θ = 0) and the closure (θ = ±π). The prediction was derived from Lemma A and the representative condition, sealed, then run.

**Correction to my own earlier claim (logged):** §5's "smooth closure" is a DEAD END. The closure is a digit-sum waveform.

**S1, closure.** Every x < H = 2^⌊n/2⌋ is a representative: x = 0 is the canonical palindrome, and for 0 < x < H the first h bits of J(x) are nonzero, so J(x) > x. So R_n[i] = i and z(i) = s₂(i) − n/2 for 0 ≤ i < H. By reflection, z(N−1−i) = z(i) for 1 ≤ i < H, and z(N−1) = +n/2.

**S2, seam.** The j-th largest representative (j = 0 at address M; j ≥ 1 at M−1−j, partner of equal weight at M+j) lies in block K, which holds μK representatives for K < H/2. Write K = 2^g + v with v's g bits v₀…v_{g−1} from the top, and o_k = ones of v among v₀…v_{k−1}. Then the total zeros over block K is

Z_sum(K) = μ[ K·s₂(K) + g·2^(g−1) + Σ_{k: v_k = 1} 2^(g−1−k)(1 + o_k + (g−1−k)/2) ] + (μ−1)K,

with μ = 1 for even n and μ = 2 for odd n (the last term is the middle zero). Block-mean latitude z̄_K = n/2 − Z_sum(K)/(μK): depth below the north pole ≈ s₂(K) + (log₂ K)/2 + O(1), with K ≈ √(2j/μ). A logarithmic cusp modulated by the digit sum of the block index.

SEALED `947b3f56…cbe59adb` (/tmp/r6/seal.txt) · S1 RUNS n = 4–20, every i < H, both ends · S2 RUNS n = 4–20, every block K < H/2, exact.

**What falls out.**
- Z_sum(K) contains n only through the parity μ. The seam cusp is the same at every radius. This is the pad law (Theorem D) at waveform level: extra outer ones add no zeros.
- Both ends of the even body carry the binary digit sum: of the address itself at the closure, of the block index K at the seam. The same function sits at two locations, a linear address at one end and a square-root (triangular) address at the other. The square root is Lemma A's triangle.
- The jump at the closure (south pole 0ⁿ beside north pole 1ⁿ) is a palindrome pair, so it sits wholly in the odd (carrier) part; the even body's closure is the digit-sum ripple without the jump.

### Ledger additions

| Item | Status |
|---|---|
| Closure profile z(i) = s₂(i) − n/2, i < 2^⌊n/2⌋ | SEALED, RUNS (n = 4–20) |
| "Smooth closure" | DEAD END (it is a digit-sum waveform) |
| Seam block zero sum Z_sum(K), cusp depth s₂(K) + (log₂K)/2 | SEALED, RUNS (n = 4–20, all K < H/2) |
| Radius invariance of the seam profile | RUNS (follows from the formula; pad law) |
| Seam blocks with palindromes (K ≥ H/2) | OPEN — the block size and one zero count shift by the palindrome; same derivation with s_K |
| Interior: between closure (s₂ of address) and seam (s₂ of block) | OPEN |

### Next stroke

The interior of the body. At the closure the address is the word; at the seam the address is triangular in the block index. In between, the address is the rank formula (p + u + Δ)/2 with Δ = A(H − A) + rectangle correction. Prediction to derive and seal: z on the left face is s₂ of the representative at that rank, and the rank-to-word map is the inverse of i = (p + π(p) + Δ(p))/2 extended from palindromes to all representatives. That makes the whole body one digit-sum waveform read through Δ.

Scripts: /tmp/r6/seam_closure.py, /tmp/r6/seal.txt.

# Append-only section 10: full interior, corrected rank, and palindrome blocks

This entry does not replace earlier sections. SHA remains parked.

## Rank extension: all palindromes versus canonical palindromes

Let pi_n(p)=#{palindromes x<p}, m=ceil(n/2), and T_n(p)=min(pi_n(p),2^(m-1)). Then T counts canonical palindrome representatives below p. The all-threshold rank is

r_n(p)=(p-pi_n(p)+Delta_n(p))/2+T_n(p)
      =(p+pi_n(p)+Delta_n(p))/2-max(0,pi_n(p)-2^(m-1)).

Proof: the nonpalindromic words below p split into x<Jx and x>Jx, whose difference is Delta and whose total is p-pi. Add only the canonical palindromes, not every palindrome. The original plus-pi formula is correct whenever pi=T, in particular on the lower half containing canonical palindromes, but not for all representatives. At n=4,p=1011, pi=3,T=2,Delta=2: the uncorrected value is 8, actual rank 7. At n=20 the uncorrected formula fails on 130,816 canonical words; the corrected formula passes every threshold.

The palindrome count also needs no search: let u be the first ceil(n/2) bits of p, and B_n(u) its palindrome completion. Then pi_n(p)=u+1[B_n(u)<p], with endpoint pi_n(2^n)=2^m.

## Full block decomposition

Put h=floor(n/2), H=2^h, K=H-1-A, e_K=1[K>=H/2], S_K=K+e_K and D_K=K(K-1)/2+max(0,K-H/2). The admitted low-half labels are exactly r=0,...,S_K-1, ordered by increasing h-bit reversal. The sole palindrome label is r=K when e_K=1.

For even n: q=D_K+i, canonical word a=(H-1-K)H+(H-1-J_h(r)).
For odd n: q=2D_K+(1-mu)S_K+i, a=(H-1-K)2H+mu H+(H-1-J_h(r)).

For nonpalindromes, n/2-E_n=wt(K)+wt(r)+(1-mu if odd). At r=K, E_n is exactly zero. Partners and the center swap provide both physical faces.

## Full block sums

Let nu=1 for even n and 2 for odd n; F(S)=sum_(0<=r<S)wt(r), evaluated by per-bit complete periods and remainders.

Canonical-zero sum:
Z_can=nu*(S_K*wt(K)+F(S_K))+(nu-1)*S_K.

Exact even-body deficit sum:
D_body=Z_can+nu*e_K*(h-2wt(K)).

The correction replaces each canonical palindrome's digit-sum latitude by the actual zero in the even projection. Canonical zeros, right-face zeros and body deficits are different sums once palindromes enter; the formula above names the owner explicitly.

## Direct full-ring reader

For either face, let q be center depth and Q=floor(q/nu). If Q<binom(H/2,2), K=floor((1+sqrt(1+8Q))/2). Otherwise K=floor((sqrt(1+8(Q+H/2))-1)/2). Integer square root implements these exactly. Determine i and middle mu from q, D_K and S_K. Select r in reversal order with binary residue counts below S_K. Reconstruct a and apply the physical partner side, including the center swap at q=0.

This avoids binary search over possible word values. The scalar reader uses one integer square root and at most h residue decisions; this is an arithmetic-operation description, not a claim of constant-cost large integers.

## Whole waveform

If a_i is the canonical representative selected by physical address i, then

E_n(i)=1[a_i != J(a_i)]*(wt(a_i)-n/2).

Thus the complete body is a centered digit sum read through the corrected Delta rank/unrank, with the palindrome mask retained. At the closure, r(p)=p for p<2^floor(n/2), giving the address digit sum; at the seam the same general reader reduces to the triangular block law. No extra interpolation or smoothness claim is introduced.

## Execution

All n=2,...,20: 2,097,148 rank thresholds, 2,097,148 full-ring word predictions, 3,049 blocks including 1,534 palindrome-containing blocks. All pointwise body predictions and block sums passed. Additional 120 scalar word/address returns and 90 independent rank comparisons through n=1024 passed. Source and prediction were sealed before execution, using literal file bytes including final newlines, and verified afterward.

## Ledger update

- Corrected all-threshold Delta rank: SEALED, RUNS.
- Uncorrected plus-all-palindromes extension to upper canonical representatives: DEAD END; owner is noncanonical palindromes counted below the cut.
- Full block rule including r=K palindrome entries: SEALED, RUNS.
- Full block canonical-zero sums and even-body deficit sums: SEALED, RUNS.
- Whole pointwise even-body reader: SEALED, RUNS in the audited domains, with scalar wide queries.
- Compact even-degree Delta coefficients, profile-language regularity, full A(q_D) union and physical interpretations retain their previous statuses.

---

## 11. Exact Delta spectral kernel, all nonzero modes, and zero mode (2026-10-20)

The §10 interior/rank extension remains in force. This new section closes the next spectral link with a sealed prediction and an exact audit. SHA inversion remains parked; physical interpretation remains PULL.

### Exact prefix kernel

Let `N=2^n`, `chi_s(x)=(-1)^(s dot x)`, `c_n(x)=sgn(rev_n(x)-x)`, and `Delta_n(p)=sum_(x<p)c_n(x)`. Walsh transforms are unnormalized. For `s != 0`, set `j=LSB(s)`, `e_k=2^k`,

`S_s(x)=sum_(p=0)^x chi_s(p)`,

`K(s,t)=N^(-1) sum_x chi_t(x) S_s(x)`.

The exact kernel support is

- `t=s`: `K(s,t)=1/2`;
- `t=s xor e_j`: `K(s,t)=2^(j-1)`;
- `t=s xor e_k`, `0<=k<j`: `K(s,t)=-2^(k-1)`;
- zero otherwise.

The convention `2^(-1)=1/2` applies for bit index zero. This follows by splitting `x=q*2^(j+1)+r`: summation over `q` forces agreement above bit `j`, and the remaining triangular-prefix Walsh transform has only the listed low masks.

### Closed spectrum for every nonzero mask

Since `Delta(p)=sum_(x<p)c(x)`,

`Delta_hat(s)=-sum_t c_hat(t) K(s,t)` for `s!=0`.

Writing `w=popcount(s)`,

- if `w` is odd: `Delta_hat(s)=-c_hat(s)/2`;
- if `w` is even: `Delta_hat(s)=-2^(j-1)c_hat(s xor e_j) + sum_(k=0)^(j-1) 2^(k-1)c_hat(s xor e_k)`.

This supersedes the §10 LSB-toggle-only shortcut. That shortcut is a DEAD END because it omits the exact `e_j` mode and all lower-bit `e_k` corrections. The new expression closes every nonzero even-degree coefficient as well as retaining the odd-degree identity.

### The zero mode

`Delta_hat(0)=sum_p Delta(p)=-sum_x x c(x)=sum_k 2^(k-1)c_hat(e_k)`.

The sparse comparator expansion gives `c_hat(e_(n-1-j))=N/2^(j+1)` and `c_hat(e_j)=-N/2^(j+1)` for `0<=j<floor(n/2)`, with zero coefficient at an odd-width middle bit. Let `h=floor(n/2)`. Then the compact scalar formula is

- even `n`: `Delta_hat(0)=N(N-1)/6 - h*N/4`;
- odd `n`: `Delta_hat(0)=N(N-2)/6 - h*N/4`.

Thus the previously open zero mode is closed as well.

### Sealed run scope

Prediction SHA-256 (literal file bytes, including final newline): `2f7d21a88107b4147843d550cdd0689f22e197b5760a0fe1050787631fee01c7`.

Audit source SHA-256 before and after execution: `982f6838dab82a3ff2a0c51ed4520f0abdadc7aabd096443d045b3d9251bebc2`.

- Direct nonzero Delta Walsh coefficients, all masks at widths 2–12: 8,177 exact comparisons, zero failures.
- Comparator Walsh coefficients against the analytic sparse expansion, widths 2–12: 8,188 exact comparisons, zero failures.
- Direct kernel entries, all nonzero `s` and all `t` at widths 2–8: 86,868 exact comparisons, zero failures.
- Zero-mode closed form against direct prefix-area sums at widths 2–20: 19 checks, zero failures.
- Every predicted coefficient was integral; all computation used exact integers and rational arithmetic.

### Ledger update

| Item | Status and scope |
|---|---|
| Corrected all-threshold rank and full interior reader | SEALED, RUNS; carried forward from §10 |
| Exact prefix kernel `K(s,t)` | SEALED, RUNS; all pairs at widths 2–8 |
| Closed nonzero `Delta_hat(s)`, including all even-degree modes | SEALED, RUNS; every mask at widths 2–12 |
| Closed zero mode `Delta_hat(0)` | SEALED, RUNS; direct sums at widths 2–20 |
| LSB-toggle-only even-spectrum shortcut | DEAD END; replaced by sparse kernel formula |
| Seam staircase / smooth closure | Seam law STANDS and full body reader RUNS; smooth closure DEAD END |
| Profile-language regularity | OPEN |
| Full `A(q_D)` union over blocks | OPEN |
| Physical spin/sphere interpretation | PULL |
| SHA route-code investigation | PARKED; codec relabeling is not an inversion result |

### Next stroke

The full Walsh spectrum of `Delta` now reduces to the already explicit sparse comparator spectrum plus a finite kernel. The next unresolved combinatorial target is profile-language regularity (the claimed state count), unless the full `A(q_D)` union is selected first. Keep these independent from the physical PULL claims.

---

## 10.1 Endpoint amendment and final delivery seals (recovered addendum)

Carried over verbatim in substance from the interior-body bundle (e258ddc9), whose log had this addendum and the review bundle's log did not.

The final packaged interior audit adds an explicit p = 2^n endpoint assertion for each width and checks uniqueness of the shifted physical-address set after the M−1, M centre swap. These supplement §10; they do not alter its rank identity or exhaustive counts.

- Terminal threshold for each n = 2..20: rank_n(2^n) = 2^(n−1), Δ_n(2^n) = 0, Π_n(2^n) = 0.
- Physical address uniqueness is an explicit assertion.
- Active artifacts: prediction `5cde4126a76c415bd4397164cf1b09b1a07fcdb82f40e140fd539a9f065757a1`; audit source (before and after) `756fb657ec768bf6d1552668fc035ba617e35eda82564d33e56d45030b030977`; results `d73c5dcc72c8000fa2f9f84287499a51a231a7d99c720e834d15d726d25d657a`; proof `74bb5de6e8dbe4f8f4ba6a4aa98c243ed7ee30f09d6122bc9f4d6f6fa89d6891`. The §10 hashes refer to the preceding implementation (`215b2a8b…` source, `358e76d2…` prediction).
- No failed run was relabelled as a pass; the earlier incorrect assertion concerned the half-word special case for non-canonical palindromes.

---

## 12. Pulling back: one mirror lift, two readers — and the paper (2026-10-20)

Dean: "write up a new paper; build the entire structure and math, then pull back and see what that becomes."

### What it became

Every result in §1–§11 reads one of two halves of one lifted word. Lift each mirror pair (x_j, x_{n−1−j}) to value v_j = x_j beside difference δ_j = x_j ⊕ x_{n−1−j} (the butterfly (u, u ⊕ v) across the mirror).

- **Value reader:** latitude, sphere height, the carrier, the poles.
- **Difference reader:** the comparator c(x) = sgn(J(x) − x), representatives, Δ, rank, address, borrow gate.
- The palindromes are where the difference reader reads nothing: they are placed by the comparisons of all other words (i(u) = (p + u + Δ)/2), linear in their own coordinates, own the poles, and are where the partner turns from reflection to X-axis half-turn.
- The ring is the coordinate system of the comparison: on addresses the comparator is one address bit (the face bit); the complexity moved into the coordinate change, which is Δ.

### Sealed and run

SEALED `359b4d3e9e043262928226047a9bed3feb0122a7b5c672464c11909bcd1584bd` (paper/seal_pullback.txt) · RUNS all six parts (pullback_run.py, 9.9 s):

- **PB1 the route is the mirror lift:** route residual bits (root + every even-step d) = δ_{h−1}, …, δ_0, innermost first; c(x) = [δ ≠ 0](1 − 2ε). Every word n = 2..18; round trip n ≤ 12.
- **PB2 lifted partner:** δ(P(x)) = δ(x); δ ≠ 0 → P flips v exactly on unequal pairs; δ = 0 → P flips every value and the middle. Every word n = 2..18.
- **PB3 latitude is the value half:** z = Σ_{equal pairs}(2v_j − 1) + [odd](x_h − ½); |z| ≤ h − |δ| + [odd]/2, attained for every k; census C(h,k)·2^k·C(h−k,t) (×2 odd), Σ_k = C(n,w). Body words never reach the poles. n = 2..18.
- **PB4 orthogonality:** Σ_x f(wt(x)) c(x) = 0 for all f. n = 2..18.
- **PB5 the ring makes the comparison one bit:** c_R(i) = χ_top(i)(1 − pal(i) − 2[i ∈ {M−1, M}]); coefficient on χ_top = N − 2^⌈n/2⌉ − 4, energy N − 2^⌈n/2⌉; share 0.982 at n = 12, 0.999 at n = 20. General: g∘P = ±g ⇒ g∘R_n Walsh-even/odd. n = 2..20.
- **PB6 closed address:** rank(p) = (p − π + Δ)/2 + π_c with closed Δ and digit-sum ℛ puts π's first 64 bits at 2,427,008,858,123,944,441 (Only Addressable's DP value); equals the DP rank on 60 random words at widths 64, 255, 256, 512, 1024; equals the materialized ring at every position n = 2..14.

### Measured (not sealed): the trade

Nonzero Walsh modes (participation ratio):

| n | latitude, word | comparison, word | latitude, ring | comparison, ring |
|---|---|---|---|---|
| 8 | 8 (8.0) | 30 (6.2) | 211 (9.5) | 100 (1.22) |
| 12 | 12 (12.0) | 126 (6.8) | 3,808 (14.2) | 1,787 (1.04) |
| 16 | 16 (16.0) | 510 (6.9) | 63,806 (22.8) | 30,444 (1.01) |
| 20 | 20 (20.0) | 2,046 (7.0) | 1,036,432 (34.6) | 505,764 (1.00) |

Latitude in ring coordinates: degree 2 holds 47% (n = 12), 33% (n = 20); degree 1 holds 0.036% and 8·10⁻⁷ (carrier only). **Correction logged:** a first reading said degree 1 was empty; it is not.

### The paper

**"Against Its Own Reverse — One comparison of each binary word with its reverse builds the ring's address, its sphere and its waveform"** (Against_Its_Own_Reverse.docx, 18 pp., 5 figures, 3 tables). Written from the held end (Theorem 1, the address), then back along the hole-by-hole path (L→L+1; the outer pair and readable gauge; sphere; waveform; comparator; spectra; body), then the pull-back (§10: Proposition 10.1 the lift carries everything; Theorem 10.2 the comparison is one address bit). Ledger, corrections box, Appendix A (all seals with digests), Appendix B (script outputs). paper_checks.py reruns every stated identity from scratch in 5.4 s; all RUN.

Neutral voice used for corrections (the session's first statements, not the author's). Seam stated as staircase under a log envelope (returns to 1 at K = 2^t), per the seam-profile peer; Theorem C's parity hypothesis named for the n = 10, depth-64 five-zero word.

### Ledger additions

| Item | Status |
|---|---|
| Route = mirror lift (PB1) | SEALED, RUNS |
| Lifted partner; latitude = value half; bound; census; orthogonality (PB2–PB4) | SEALED, RUNS |
| Comparison is one address bit; P-parity → Walsh parity (PB5) | SEALED, RUNS |
| Closed address at 64 bits and against DP to 1,024 (PB6) | SEALED, RUNS |
| The trade for the latitude | computed (n ≤ 20) |
| Closed form of the latitude in ring coordinates | OPEN |
| Profile-language regularity; full A(q_D) | OPEN (unchanged) |
| Physical spin/sphere | PULL |

### Next stroke

Profile-language regularity needs a distinguishability proof; the closed seam blocks (reversal-ordered labels, palindrome label r = K) are its material. Or the other side of the trade: a closed spectrum for the latitude in ring coordinates, now fixed by Theorems 1, 6 and 9.3.

Files: paper/Against_Its_Own_Reverse.docx, paper/build_paper.js, paper/paper_checks.py (+ _output.txt), paper/pullback_run.py (+ _output.txt), paper/trade_measure.py, paper/figures.py, paper/figs/, paper/seals/.

---

## 13. Using the ring for compression: what it can remove and what it cannot (2026-10-20)

Dean: "figure out how to use this — if the rings build half of themselves, apply data to the ring as compression."

### The gap, named by what must be there

A compressor is a reader that already knows part of the data, and it can remove only what it knows. The ring is a bijection on n-bit words (address, route and lift are each exactly n bits), so it knows nothing about a single word that the word does not carry. The half that builds itself is the partner P(x): it is free because x already determines it, which is also why it carries nothing new. What the ring knows for free is structure — the partner, the mirror difference of every pair, the weight — so it removes exactly the part of the data that repeats under the partner or the mirror, and nothing else.

### Sealed and run

SEALED `2051041e62bc6753aa37ea731b19dcf97d83841e627a8f26c9849715c8fe6156` (compress/seal_compression.txt) · ring_compression_bench.py, 18.4 s. Datasets all local: RAND (1 MiB, seed 20261020), TEXT (the seven papers via pandoc, 382,662 bytes), IMAGE (grace_hopper.jpg, 8-bit gray), MRI (s1045, 16-bit), DEM (jacksboro elevation, 16-bit), FIR (512 firwin lowpass filters × 255 taps, int16), COV (256×256 covariance of 16×16 image patches, int16). Every transform round-trips exactly.

| | raw | ring address | lift | route | side split |
|---|---|---|---|---|---|
| TEXT (best coder, bytes) | 103,334 | 104,816 | 103,675 | 105,471 | 148,781 |
| IMAGE | 199,744 | 210,341 | 200,244 | 213,282 | 238,808 |
| MRI | 22,192 | 25,409 | 24,799 | 23,627 | 26,263 |
| DEM | 108,482 | 109,338 | 124,685 | 115,912 | 110,766 |
| RAND (1,048,576 in) | 1,048,688 | 1,048,688 | 1,048,688 | 1,048,688 | 1,051,317 |

- **E1 pigeonhole — RUNS.** Order-0 word statistics identical (same multiset of counts) under every transform on every dataset; RAND and RAND16 never shrink under any transform or coder.
- **E2 no free compression of natural data — RUNS.** Best transformed / best raw: TEXT 1.003, IMAGE 1.003, MRI 1.065, DEM 1.008. The ring address is worse than raw under lzma on IMAGE (1.082), MRI (1.092), DEM (1.001): the two faces separate numerically adjacent values.
- **E3 the half that builds itself — RUNS.** idx(x) = rank(canon(x)) from the closed address is constant on every pair and maps pairs one-to-one onto [0, 2^(n−1)): exhaustive n = 2..20 (vectorised closed rank against the counted rank), random words at 64, 256 and 1,024 bits with unrank by bisection. HalfTable(20) holds 524,288 entries for a symmetric or antisymmetric table over 1,048,576 words; no hash, no collisions.
- **E4 the mirror at the data's own scale — DEAD END as sealed.** COV: upper triangle plus lower-minus-upper differences = 0.503 of raw lzma (sealed ≤ 0.60 ✓). FIR: tap-scale lift = 0.584 of raw lzma (sealed ≤ 0.55 ✗). The same lift at the wrong location, inside each 16-bit word: 1.010 (FIR) and 0.993 (COV) ✓. Owner of the FIR miss, routed back after the run (names an owner, not a landing): the mirror is exact (all 127 differences zero in all 512 filters, so exactly half the samples are removed; the zeros cost 152 bytes), but lzma already compresses the whole bank 14.3% better than its two halves compressed apart (156,100 vs 90,216 + 92,032): it was already harvesting part of the mirror's redundancy through shared statistics, without reversal matching. With a 16-bit literal model (lc=0, lp=1, pb=1) the ratio is 0.571.

Observation (not sealed): the side-bit entropy measures how oriented data is against its own reverse — TEXT 1.000, FIR 1.000, MRI 0.987, COV 0.941, IMAGE 0.883, DEM 0.048 (small elevations sit in the closure region, almost all on the left face).

### How to use it

- **DEAD END:** "apply arbitrary data to the ring as compression." Owner: the ring is a bijection; E1 is exact and E2 measured.
- **Index (RUNS):** halve any table or set that respects the partner — features or counts of words up to reversal, a set closed under P — with the closed-form, collision-free O(n) index at any width (ringpack.HalfTable, half_index, half_unindex). The other half is computed, not stored.
- **Transform (COV RUNS, FIR owned by the coder):** remove mirror redundancy where the data holds its mirror (symmetric taps, symmetric matrices, mirrored image regions, palindromic sequences). The ring's own pairing (bits inside a word) is the right location only for data whose words are near-palindromes.
- **Meter:** H(side bit) reads a source's orientation preference.

### Ledger additions

| Item | Status |
|---|---|
| Ring/route/lift as compressors of arbitrary or natural data | DEAD END (pigeonhole; E1, E2) |
| Half index and HalfTable at any width | SEALED, RUNS |
| Mirror lift at the data's scale: COV 0.503 | SEALED, RUNS |
| Mirror lift: FIR ≤ 0.55 | DEAD END (0.584; owner lzma shared statistics) |
| Bit-level lift at the wrong location | SEALED, RUNS (no gain, as predicted) |
| Reverse-match coder (partner as an LZ match type, for data with reversed copies) | OPEN — next |

### Next stroke

A coder that knows the partner: LZ with reversed matches (the partner as a match type), tested on data that actually contains reversed copies — inverted repeats in DNA (with reverse-complement as the involution) or mirrored image regions — against lzma, which cannot match reversed strings. That is the one place the ring's structure can beat a standard coder on real data.

Files: compress/ringpack.py, compress/ring_compression_bench.py, compress/bench_output.txt, compress/ring_compression_results.json, compress/seal_compression.txt.

---

## 14. The partner as a match type: the half that builds itself, found in a genome (2026-10-20)

Dean: "run it" (the §13 next stroke).

### Structure before data

In DNA the partner of a strand is its reverse complement — reverse the order, complement A↔T, C↔G — the ring's partner at a different location. A land-plant chloroplast carries two inverted repeats, one the reverse complement of the other: the half that builds itself. LZ-family coders copy forward only and cannot use it. A coder whose match types include the partner can.

### Sealed and run

SEALED `88618d1325d650d7c9e82dd9cf6c6dd0a2ce8ade3aae42d298bbf91290d10c0d` (partner/seal_partner_coder.txt) — written after confirming the record was reachable and before its sequence was read. partner_coder.py: greedy pre-pass, k = 24 seed, minimum copy 32, reverse-complement copy tokens (literal run, distance, length) as varints; literals and tokens by lzma (9e). Data: NC_000932, *Arabidopsis thaliana* chloroplast, from the Biopython test suite (record sha256 a8b5d8239001f56a…), 154,478 bases, all A/C/G/T.

| | lzma alone | partner coder | ratio |
|---|---|---|---|
| NC_000932 | 41,784 bytes (2.164 b/base) | 34,752 bytes (1.800 b/base) | 0.8317 |
| forward-only control | 41,784 | 41,736 | 0.9989 |
| random DNA, same length | 43,264 | 43,264 | 1.0000 |

- **P1 RUNS:** one partner copy, length 26,264 — bases [128,214, 154,478) are the reverse complement of [84,170, 110,434), coverage 0.1700. The coder found the inverted repeat on its own; 26,264 bases rebuilt from three numbers.
- **P2 RUNS:** 0.8317 ≤ 0.87.
- **P3 RUNS:** forward copies already belong to lzma, 0.9989.
- **P4 RUNS:** random DNA, no copy ≥ 32, 1.0000.
- **P5 RUNS:** every encoding decodes byte for byte.

### Observations (not sealed)

- The gain does not depend on lzma. Ideal code length of an adaptive order-k DNA context model (KT estimator): whole genome 1.924 b/base at order 2; literals + tokens 1.589 b/base; ratio 0.826. Orders 2–12 all land at 0.826–0.830.
- NC_005816 (*Yersinia pestis* plasmid pPCP1, 9,609 bases): no partner copy ≥ 32, ratio 1.0000 — no inverted repeat, nothing to remove.
- Prior art, stated plainly: inverted-repeat modelling is established in specialised DNA compressors (e.g. XM, GeCo). What lands here is the route: the ring's partner, read at the DNA location, is exactly the match type such a coder needs, and it was derived, sealed and then found in the data.

### Ledger additions

| Item | Status |
|---|---|
| Partner coder finds the chloroplast inverted repeat (26,264, 17.0%) | SEALED, RUNS |
| Partner coder vs lzma on NC_000932: 0.832 | SEALED, RUNS |
| Forward-only and random controls | SEALED, RUNS |
| Gain under an order-2..12 DNA model: 0.826–0.830 | computed |
| Plasmid without inverted repeats: no gain | computed |
| Partner coder on data without its partner | DEAD END by structure (nothing to remove) |

### Next stroke

Bring the partner home to bits: a byte-stream coder with the ring's own P (reverse; complement on palindromes) as a match type, tested on data with mirrored content (symmetric images, mirrored waveforms), and the partner layered on a full context-mixing DNA model to read where the remaining 1.59 b/base sits.

Files: partner/partner_coder.py, partner/seal_partner_coder.txt, partner/partner_output.txt, partner/partner_coder_results.json.

---

## 15. The ring's partner at every symbol scale, and layered on a DNA model (2026-10-20)

Dean: "run it" (the §14 next stroke).

### Structure before data

The partner of a stretch of symbols is the stretch reversed with each symbol mapped by the alphabet's own involution φ: P on 16-bit ring words, identity on samples, bytes and bits, complement on DNA bases. The facing law R[N−1−i] = P(R[i]) says the right half of a ring tape is its left half reversed with every word mapped by P — so a coder that knows P stores a ring as its left half and one token.

### Sealed and run

SEALED `0805b5ebe9068ae568ef20bee1658f36d982a0a6dfecd528d20dd59092f0f3fc` (partner2/seal_partner_general.txt) · partner_general.py, 30 s. One greedy pre-pass over symbols; at each candidate the longer of a forward copy and a partner copy (ties to forward); literals and tokens by lzma 9e.

| data | φ | lzma raw | coder | ratio | partner copies | coverage | forward-only |
|---|---|---|---|---|---|---|---|
| RING16 (R_16 tape, 65,536 words) | P_16 | 104,640 | 44,852 | 0.4286 | 1 (32,768 words at 32,768) | 0.5000 | 1.0000 |
| FIR (512 × 255 taps) | identity | 156,100 | 90,904 | 0.5823 | 513 | 0.4981 | 1.0036 |
| DNA (NC_000932) | complement | 41,784 | 34,672 | 0.8298 | 1 (26,264) | 0.1700 | 0.9989 |
| TEXT (seven papers) | identity | 107,176 | 114,816 | 1.0713 | 169 | 0.0122 | 1.0683 |
| RAND16 | identity | 131,140 | 131,140 | 1.0000 | 0 | 0 | 1.0000 |

- **Q1 RUNS — the ring stores half of itself.** Exactly one copy: a partner copy of 32,768 words starting at word 32,768, covering exactly half the tape (the whole right face from one token). 0.4286 of lzma; lzma's forward copies give 1.0000.
- **Q2 RUNS — mirrored waveforms.** FIR partner coverage 0.4981, ratio 0.5823 (the §13 tap-scale lift, now found by the general coder).
- **Q3 RUNS — replication.** DNA longest partner copy 26,264, ratio 0.8298 (|Δ| = 0.0019 from §14).
- **Q4 DEAD END — control coverage.** TEXT partner coverage 0.0122 > 0.01 (ratio part holds: no gain). Owner, routed back after the run: pandoc's plain-text tables, whose whitespace-padded cell borders mirror around line breaks (most copied string `"      |\n|        "`); only 0.4% of the copied bytes equal their own reversal. The 7% text loss belongs to the greedy pre-pass taking forward copies from lzma (forward-only control 1.0683). The practical form is a partner-only pre-pass in front of lzma, forward copies left to lzma: TEXT 1.0087, DNA 0.8317, FIR 0.5818, RING16 0.4286.
- **Q5 RUNS — exact.** Every encoding decodes to its input.
- **Q6 RUNS — the partner layered on a DNA model.** Order mixture (orders 1–24, fixed-share Bayesian mixing), ideal code length on NC_000932: plain 1.9114 b/base; IR-aware (every context also learns from the reverse-complement strand) 1.6002; partner pre-pass + plain 1.5808; pre-pass + IR-aware 1.5791. (a) IR/plain 0.8372 ≤ 0.88; (b) pre-pass + plain / IR 0.9879; (c) pre-pass + IR / IR 0.9868. Two routes to one partner, and it is removed once.

**Where the remaining 1.58 b/base sits:** in the 83% of the genome without a partner, at 1.902 b/base under the IR-aware mixture — the unique sequence, close to the two-bit ceiling.

### Observation (not sealed): mirrored images

partner2/mirror_context_images.py. Two glyph sheets in DejaVu Sans Bold at 150 px in 192-px cells, coded by a 12-pixel causal template (ideal code length, KT estimate), then by the same template plus three mirror pixels at columns W−1−x+{−2, −1, 0} once they are decoded.

| sheet | pixels | lzma | template | + mirror | ratio | rows exactly mirror-symmetric |
|---|---|---|---|---|---|---|
| symmetric AHIMOTUVWXY08 | 479,232 | 1,988 B | 1,005 B | 882 B | 0.878 | 0.937 |
| asymmetric BCDEFGJKLNPQRSZ | 552,960 | 2,136 B | 961 B | 1,015 B | 1.055 | 0.106 |

The mirror context pays where the data holds its mirror and costs context dilution where it does not: the Q4 law at pixel scale.

### Ledger additions (§15)

| Item | Status |
|---|---|
| Q1 the ring stores half of itself (one partner token) | SEALED, RUNS |
| Q2 mirrored waveforms | SEALED, RUNS |
| Q3 chloroplast replication | SEALED, RUNS |
| Q4 text control coverage | DEAD END; owner pandoc table borders; text loss owned by the greedy forward pre-pass |
| Q5 exactness | SEALED, RUNS |
| Q6 partner on a mixing DNA model, removed once | SEALED, RUNS |
| Partner-only pre-pass | computed: TEXT 1.0087, DNA 0.8317, FIR 0.5818, RING16 0.4286 |
| Mirror context on glyph images | computed, not sealed: 0.878 symmetric, 1.055 asymmetric |

Next stroke from §15: superseded by Dean's two-wheel question (§17).

Files: partner2/partner_general.py, seal_partner_general.txt, partner_general_output.txt, partner_general_results.json, mirror_context_images.py, mirror_context_output.txt, mirror_context_results.json.

---

## 16. Peer five-hole audit, merged, with independent replication (2026-10-20)

Inputs (sha256): peer bundle relation_layer_five_holes_review_bundle_1.zip (`070a1648…cd49c`, two identical copies) holding five_open_holes_audit.md (`792c65cd…`), review_metadata.json (`8db00b00…`) and a review copy of this log (`e7829ce5…`). That copy is identical to this log through §14 and adds one entry numbered §15; it is merged here as §16, since §15 here holds the partner work. Also the five-hole draft (a5141f13: Hole 2C continuation, Holes 3–5), the two peer audit replies (bd4b2684, fb0f7c4d) and the NotebookLM relation-layer note.

Peer findings as received:
- **Hole 1.** The draft's even-body block sum dropped the palindrome slot from blocks K ≥ H/2. Kept and masked, C*_K(t) = Σ_{i<S_K} 1[r_i < K] χ_t(D_K + i), the block formula matches every coefficient (peer: 2,097,148 coefficients, widths 2–20; source seal `2222f11b…840a`, declaration `1182cea8…aa8b`). Folding Ê_n(s) = 2(−1)^|t| B̂_n(t), t = s mod M, B the centre-out body: full degree two receives exactly the centre-out degree-one and degree-two bins. Degree-two concentration is a measurement, not a derived law. Compact evaluator for C*_{K,ℓ}: OPEN, the peer's next stroke.
- **Hole 2A.** STANDS as a preimage identity (all addresses, both faces, centre convention); the reduced seam-block form is OPEN.
- **Hole 2B.** The exact finite identity "a front-half reading is a digit of 1 − √(1−2u)" fails: L = 4, u = 49/128 reads 0 where τ's first digit is 1. Route 7's sampled agreement (3,891 of 3,892 front-half readings, L = 24–160) stays a measurement. The Myhill–Nerode argument lacks one common distinguishing suffix per pair: OPEN. Entropy asymptotic: OPEN.
- **Hole 2C.** The single angle u_D closes D ≡ 0, 1 (mod 3) and fails most of D ≡ 2 (mod 3). The draft's two-parameter (K_D, r_i) witness is never instantiated as an angle: OPEN.
- **Hole 3** (SHA ROBDD pruning): no invariant or benchmark supplied. SHA stays PARKED; route-code relabeling is not inversion (§2 DEAD END).
- **Hole 4.** The carry transfer monoid {kill, set, trans} STANDS (standard generate/propagate/kill). Completeness of the n = 6 classes for every n and the functor onto M_ij are asserted, not constructed: OPEN.
- **Hole 5.** u'' = −1 STANDS; the mass/acceleration split is PULL.
- Root-of-unity product: Π_m (p − ζ_n^m) = p^n − 1 STANDS; the p^(n/2) − 1 form is wrong (255, not 15, at p = 2, n = 8).
- Quantum identifications (Born law, Bell state, uncertainty): PULL. Finite combinatorial identities supply no amplitudes, coherence or non-commuting observables.
- Relation-layer D = A/W: a bookkeeping template until the ring's ambient module, known-relation submodule, group action, reader subgroup and bridge map are written. Not imported.

Replication, independent code, sealed `bf6fd7b3…6c18d` (wheels/seal_five_holes_replication.txt), 1.1 s, seal unchanged after:
- **R1 RUNS.** L = 4, u = 49/128: address 6, slice 0 of 0111, bit 0; τ digit 1.
- **R2 RUNS.** Exact rationals, D = 13–96: class 0 28/28, class 1 28/28, class 2 6/28. First failure D = 14 at L = 12: address 2052, slice 4 of 111101001111. The six passing class-2 depths are D = 26, 32, 35, 65, 83, 89 (m = 8, 10, 11, 21, 27, 29). *The Geometry of a Readout* covers m ≥ 8, m ≡ 0, 1 (mod 4) with a two-offset witness, so the open set is D = 3m + 2 with m = 4–7 or m ≡ 2, 3 (mod 4). The single angle certifies D = 32, 35 and 83 inside it. The open set has witnesses; a uniform one is not written.
- **R3 RUNS.** The corrected full-block formula equals the direct Walsh transform at every mode, n = 4–12, both parities. The compressed version gives 8 at n = 6, mode 000011, where the direct value is 0.
- **R4 RUNS.** Degree-two share of the full latitude energy 53.1250, 55.9937, 51.9287, 46.7403, 38.9498, 32.7503 % at n = 6, 8, 10, 12, 16, 20. Degree two is the largest bin at every n = 4–20. Also n = 12 degree-one 0.0361125 %; n = 20 active modes 1,036,432, participation ratio 34.5728.

| Hole | Status |
|---|---|
| 1 corrected finite block formula | RUNS (peer, widths 2–20; replication n = 4–12) |
| 1 compact C*_{K,ℓ} evaluator, closed all-n spectrum | OPEN (peer's stroke) |
| 1 degree-two concentration | measurement STANDS; cause OPEN |
| 2A interval preimage | STANDS; reduction OPEN |
| 2B exact τ-digit identity | DEAD END at finite width; owner: the tent and back-half count that ride on the parabola (Route 5); the digit law holds as a majority law |
| 2B non-regularity, entropy | OPEN |
| 2C uniform witness, m = 4–7 and m ≡ 2, 3 (mod 4) | OPEN; single angle covers D = 32, 35, 83 |
| 3 SHA ROBDD pruning | PARKED |
| 4 all-n carry seam functor | OPEN |
| 5 mass/acceleration | PULL; the −1 gets an owner in §17 |
| Quantum identifications | PULL |
| Relation-layer module bridge | not written; not imported |

---

## 17. Two wheels: the compile is instant, the hold is the gap (2026-10-20)

Dean: "are we considering how these rings compile as soon as it hits 8 bit orbits. or starts too. things run as soon as they can. holding that back is what reality is. that is what the excel sheet showed us. ther are two wheels the one below is complete the one above is the slots i think. always spinning. the search is the orbit the path is looking from above. INSANT TRANSFORMATION (COMPILATION) ISTHE WHOLE CORE." Then the workbook nested_ring_beyond_2bit.xlsx (sha256 `c08b4ac4…40a1`): rings 2, 3 and 4 in the two_bit_circle layout, the DI chain for rings 1–10, the constants.

Reading taken. The wheel below is what has been counted: one counter runs every value once, complete up to the cursor. The wheel above is the ring's slots, every one already assigned. A word compiles the instant it is counted. What is held is a slot assigned and not yet filled. The search is walking the orbit to find a place; the path is the address read from above.

Sealed `bf244a22…6f61b8` (wheels/seal_wheels.txt) before any run; 31.9 s; seal unchanged after.

**W1 RUNS — nothing is searched.** L = 2–20: every representative lands on the first empty left-face slot, except the largest, which lands at M with M−1 still empty for its partner; every partner lands facing a slot already filled. One exception per ring: the centre twist.

**W2 RUNS — the hold is twice where minus when.** O_L(t) = 2r_L(t) − t = Δ_L(t) + min(π_L(t), 2Hp − π_L(t)) at every t, L = 2–20, against an independent open-interval count. The tent is the palindromes: a palindrome pair opens at p and closes at its complement.

**W3 RUNS — the most is held at the seam.** max O_L = 2^(L−2) + Hp at t = M only: 6, 72, 1,056, 16,512, 262,656 at L = 4, 8, 12, 16, 20. When the counter crosses value 1/2 the address stands at angle 3/8 + Hp/2N, the workbook's "start of the 11 frame", and a quarter of the ring is held.

**W4 RUNS — the wheel below completes when the wheel above holds most.** At t = 2^L ring L holds nothing, ring L+1 holds its peak, rings L+2 to 2L−2 hold strictly between, and every ring n ≥ 2L−1 holds all 2^L counted words open: each counted word is a representative still waiting. L = 2–12, n up to 2L+4 and n = 64, 128.
Derived after the run (not sealed; checked on 819 cases, L ≤ 40): at that instant ring L+k holds 2^L − (2^(L−k) − 2^⌈(L−k)/2⌉). Below 2^L a partner of ring L+k must be 0^k m 0^k with m a non-palindromic partner of ring L−k; the 00 frame passes the decision inward. The tower is mirrored about the completing ring: ring L+k holds what ring L−k reflects.

**W4b RUNS — every ring starts as a counter.** R_n[i] = i for every i < 2^⌈n/2⌉, n ≥ 4 (exhaustive to 20, sampled to 64), and R_n[2^⌈n/2⌉] = 2^⌈n/2⌉ + 1. At odd n this tightens §9 S1, which was stated with ⌊n/2⌋. Rings 15 and 16 open with the whole byte orbit, 0–255 in slots 0–255; slot 256 holds 257.

**W5 RUNS — the mean hold is a third of a turn.** Σ_t O_L(t) = Σ_pairs (P(r) − r) = S_J/2 + Hp(N/2 + 1), S_J = N(N−1)/3 − hN/2 (L even), N(N−2)/3 − hN/2 (L odd). Mean hold per pair over N: 0.3906, 0.3557, 0.3403, 0.3352, 0.3338 at L = 4, 8, 12, 16, 20, tending to 1/3. The outermost unequal mirror pair k is reached with probability 2^−(k+1) and moves the word by about 2^(L−1−k): a quarter per step, summing to 1/3. This is the fourth landing of 1/3, beside mean continuation depth, the complement attractor and the representatives' centre of mass. One path at four locations.

**W6 RUNS — the workbook beyond two bits.** Every ring L = 1–12, every width W = 1–min(C, 64): the sheet read counter-clockwise from slice C−1−i equals the sheet read clockwise from slice i with every palindromic sheet word complemented. Zero offset. No rotation of the sheet equals its reversal for L = 3–14; at L = 1 and 2 rotations 1 and 3 do, and agree with the twist. The workbook's rule "start where the first 1^L lands" gives L·2^L − 2L + 1 for L ≥ 3: 151, 373, 883, 2033, 4591, 10221, 22507, 49129, 106471, 229349 at L = 5–14 (19 and 57 were seen before the seal). That offset is where the tape's first two words, 0^L and 0^(L−1)1, come back around reversed and complemented as the closing run 0 1^(2L−1).
Measured, not sealed: the workbook's offset column agrees with the true counter-clockwise reading on 1/2, 1/3, 1/4, 1/6, 1/12, 1/24 of ring-3 rows at widths 2–7 and on none from width 8; on ring 4 on 30, 20, 12, 7, 4, 3, 2, 1 of 64 rows at widths 2–9 and on none from width 10. On ring 2 it agrees everywhere.

**W7 RUNS — the workbook rebuilds.** 63,521 cached cells, rebuilt from the rolling stack and Route 3, zero mismatches: rings 2–4 columns A–Q, and the DI chain for rings 1–10 with partner, frame, provider, provider position one ring down, residual, depth and root.

**W8 RUNS — the path, not the orbit.** Direct unrank: the front half from the quadratic with one integer square root and an O(1) correction, the back half with one count per bit. Exact at every address for L = 1–16; 2,000 round trips at each of L = 64, 256, 1024, 4096. Per word 0.031, 0.147, 0.663 ms against bisection's 1.46, 25.6, 394 ms at 64, 256, 1024 bits (47×, 174×, 594×); a 4096-bit word in 5.3 ms.

What fell out.
- The compile is instant at every width from the first word, in every ring at once. Nothing waits for 8 bits. Every ring opens as a counter, and the byte orbit appears whole at the start of rings 15 and 16.
- Holding is the only thing that takes time. Where a word sits is known before it arrives (W1, W8); its pair does not close until its partner is counted. The hold is 2·where − when. Sampled at the start of each front-half column (even L) it is f(H − f) + min(f, H − f): the triangle's area plus the tent, Route 7's Q(f) read as a hold (checked L = 2–30).
- The angle law's −1 has its owner here. With o(t) = t − t² the normalized hold, u = (t + o)/2, so u'' = o''/2 = −1. The hold's curvature −2 splits evenly: −1 from the built face thinning (density 1 − t) and −1 from the reflected face filling (density t). PULL: both faces pay the same price, Dean's Constraint 3 ("all change is equal") read at this location.
- The workbook's two wheels separate past two bits. At ring 2 the counter-clockwise column is a hold (rotation by 3, the three dark slices) and the transformation at once: the twist hides inside the rotation. From ring 3 on no hold reproduces it. The offset column agrees on fewer rows at each width, and at ring 3 on none once the window reaches 8 bits. The transformation reproduces it at every ring at zero offset: complement the palindromic words. The offset rule is a search over the orbit; the twist is the path from above.
- Instant transformation is wiring. Reversal crosses wires and costs no gates; complement is one inverter per wire; the only decision is the palindrome test. The reflected half needs no generation (one partner token, §15 Q1), and the decompile needs no search (W8).

Corrections logged: the cascade threshold n ≥ 2L was corrected to n ≥ 2L−1 before sealing (the odd middle bit is free); §9 S1 tightened at odd n.

### Ledger additions

| Item | Status |
|---|---|
| W1 compile without search, one centre exception | SEALED, RUNS (L = 2–20) |
| W2 hold = 2r − t = Δ + palindrome tent | SEALED, RUNS (all t, L = 2–20) |
| W3 peak 2^(L−2) + Hp, at the seam only | SEALED, RUNS (L = 2–20) |
| W4 cascade at t = 2^L | SEALED, RUNS (L = 2–12) |
| Tower mirror: ring L+k holds 2^L minus the non-palindromic part of ring L−k | derived after the run, checked (819 cases); not a landing |
| W4b every ring opens as a counter to 2^⌈n/2⌉ | SEALED, RUNS (exhaustive n ≤ 20, sampled to 64) |
| W5 total hold in closed form, mean hold → N/3 | SEALED, RUNS (L = 2–20) |
| W6 sheet twist at zero offset, every ring and width | SEALED, RUNS (L = 1–12) |
| W6 no rotation for L ≥ 3; offset rule L·2^L − 2L + 1 | SEALED, RUNS (L = 3–14; landings L = 5–14) |
| Offset column against the counter-clockwise reading | measured: no agreement from width 8 (ring 3), 10 (ring 4) |
| W7 workbook rebuild | SEALED, RUNS (63,521 cells) |
| W8 direct unrank, the path | SEALED, RUNS; 47–594× faster than bisection |
| Column-start hold f(H − f) + min(f, H − f) | derived, checked L = 2–30 |
| Angle −1 = half the hold's −2, equal shares by face | derived; physical attribution PULL |

### Next stroke

The hold depends on the reading order. Address order holds half the ring at the seam (every left-face word waits for its facing partner), the counter holds a quarter, pair order holds one. Seal the hold under every order the corpus already uses (address, value, sheet, route code, half-table index) and the tower mirror as a full profile for t ≤ 2^L (ring L+k holds t minus twice the non-palindromic partners of ring L−k below ⌈t/2^k⌉). Then one hold, three locations (counter, sheet, frames), and write it up.

Files: wheels/wheels.py (instant compiler both ways, hold), run_wheels.py, seal_wheels.txt, wheels_output.txt, wheels_results.json, mirror_cascade_check.py, five_holes_replicate.py, seal_five_holes_replication.txt, five_holes_replication_output.txt, five_holes_replication_results.json; inbox/xlsx_beyond2 (workbook copy), inbox/five_holes_a (peer bundle).


---

## 18. Hold at three locations: counter, sheet, frames (2026-10-20)

Prediction and finite scope are in `hold_order_prediction.md`; the pre-run prediction hash is `76f4398f…ece6b5c`. The audit code hash was recorded before the official run and matches the executed source. The full run completed in 7.17 s; the full-profile exporter then materialized every tower row. An initial exporter attempt exposed a width-zero base indexing error; the base was corrected to `C_0(q)=0`, the exporter was resealed, and the successful export had zero mismatches. No partial export is used as evidence.

**Definition.** For an order σ of all n-bit words, `Hσ(t)` is the number of partner pairs with exactly one endpoint in the first t words. This is an order-dependent prefix-cut count, not elapsed time.

**O1 RUNS — five orders, all prefixes.** Widths 2–12, all 40,995 prefix points across five explicitly defined orders; each order was verified to be a permutation, and each profile was accumulated by a direct seen/unseen-partner counter.

| Order | Full profile | Maximum / seam |
|---|---|---|
| Address order `R_n[i]` | `min(t, 2^n−t)` | `2^(n−1)` at the seam |
| Value/counter `0,…,2^n−1` | `Δ_n(t) + min(π_n(t), 2H_p−π_n(t))` | `2^(n−2)+H_p` at `t=2^(n−1)` |
| Sheet order (reverse all tape bits, complement, re-chunk) | `min(t, 2^n−t)` | `2^(n−1)` at the seam |
| E/G route-code order, side bit leading | `min(t, 2^n−t)` | `2^(n−1)` at the seam |
| Half-table pair-adjacent lift | `t mod 2` | 1 at odd prefixes; 0 at even prefixes |

Address, sheet, and route-code profiles are not merely equal at the seam: every recorded prefix agrees, at every width 2–12, with the entire triangle `min(t, 2^n−t)`. For the sheet, the reverse-and-complement chunk maps each address word x to `F(x)=C(x)` if x is non-palindromic and `F(x)=x` if palindromic; F is a bijection commuting with P, so the first sheet half still contains exactly one endpoint from each partner pair. For route order, the leading side bit places all representatives before all partners. The half-table itself is pair-indexed, so its reported word-level hold uses the declared lift: emit each canonical representative and then its partner.

The value/counter profile matches the existing W2 formula at every prefix for widths 2–12; its predicted seam peak also matches at each width. Examples: width 4, value peak 6 versus address/sheet/route peak 8; width 8, 72 versus 128; width 12, 1,056 versus 2,048. The pair-adjacent half-table lift holds at most one pair.

**O2 RUNS — the tower mirror as a full profile.** Let `C_w(q)` count values x below q that are non-palindromic partner-side words in width w: `x>P_w(x)` and `J_w(x) != x`; define `C_0(q)=0`. For `n=L+k`, the executable prediction is

`H_(L+k)(t) = t − 2 C_(L−k)(ceil(t / 2^k))`, for `0 ≤ t ≤ 2^L`, `1 ≤ k ≤ L`.

This explicit partner-side count is the intended meaning of “non-palindromic partners below the ceiling”; it must not be replaced by half the number of all non-palindromic words below the cut. The formula matched `wheels.hold(t,n)` at **1,966,215 / 1,966,215** profile points for L = 2–16, all k = 1…L, every t, with zero misses. **130,111** of those points also matched an independent direct counter-order stream profile at target widths n ≤ 16. The complete point-by-point record is `outputs/tower_mirror_full_profile.csv.gz` (1,966,215 rows); sparse landmark rows are also supplied. At t = 2^L, the identity reduces to the pre-existing seam form `2^L − (2^(L−k) − 2^ceil((L−k)/2))`, preserving the 819-case seam check through L = 40.

**One hold, three locations.** The counter gives the Δ plus palindrome tent; the sheet/address/route views give the same triangular cut because one member of each pair appears in the first half; the frame/tower view resolves the high-width hold into the partner-side count at a lower ring after the ceiling projection. Half-table pair adjacency is the limiting one-open-pair order. This is a discrete finite-domain synthesis only; physical time or physical attribution remains PULL.

**Ledger additions**

| Item | Status |
|---|---|
| Five order profiles, widths 2–12 | RUNS (40,995 prefixes; zero failures) |
| Exact address = sheet = route triangle | RUNS (every prefix, widths 2–12) |
| Value-order W2/W3 profile rechecked | RUNS (every prefix, widths 2–12) |
| Half-table pair-adjacent lift `t mod 2` | RUNS (widths 2–12) |
| Full tower mirror profile, L = 2–16 | RUNS (1,966,215 points; zero misses) |
| Direct tower cross-check, n ≤ 16 | RUNS (130,111 points; zero misses) |
| Workbook cached-cell replay from XLSX itself | OPEN in this bundle; workbook file was not included, so sheet order was reproduced from supplied W6 source code |
| Physical interpretation of the hold | PULL |

Files: `hold_three_locations.md`, `hold_order_prediction.md`, `hold_order_audit.py`, `export_tower_profile.py`, `outputs/hold_order_profiles.csv`, `outputs/hold_order_summary.csv`, `outputs/hold_order_summary.json`, `outputs/tower_mirror_full_profile.csv.gz`, `outputs/tower_mirror_profile_samples.csv`, `outputs/tower_mirror_export_summary.json`, `official_pre_run_seal.sha256`, `export_pre_run_seal.sha256`, `execution_provenance.json`, `SHA256SUMS.txt`.

---

## 19. Readiness-first compilation and semantic output settlement (2026-10-20)

*Merge note.* Peer entry from readiness_execution_audit_bundle_1.zip (sha256 `c117aed5…fb04`), written as §15 on an older copy of this log (through §14); renumbered §19 here, text otherwise unchanged. §18 above is appended verbatim from two_wheels_hold_audit_bundle.zip (sha256 `93b9a488…14ef2`), whose log is this log plus §18 exactly (prefix sha256 `585d4db8…`). The workbook replay that §18 lists as OPEN for its bundle is §17 W7: 63,521 cells against the workbook itself.

This is the execution layer beside the static ring/rank/spectrum work. The original submitted `readiness_first_audit.py` and its prediction were hash-checked; both hashes match their seals after execution. The source ZIP is not standalone-runnable as packaged: it omits `pairs_forced.py` and the assumed `output/` directory. The rerun supplied a separately documented compatibility adapter from the previously audited partner/grow rule and created `output/`. Its non-runtime output fields match the archived results exactly.

### Two distinct execution rules

- **Dyadic compiler closure.** On arrival of a bit, push a one-bit block; while the last two blocks have equal width, fuse `(A,B) -> (A,A xor B)`, retaining both channels. The frontier widths equal the descending powers of two in the binary expansion of the arrival count. Each merge occurs at the arrival that completes its right dependency; this is a property of the scheduler implementation, not a measured physical latency.
- **Semantic readiness.** An output `f` is ready under observations `o` iff `{f(x): x agrees with o}` has cardinality one. The 8-bit-adder audit evaluates this by grouping the complete truth domain according to observed input prefixes, then aggregating per-output AND/OR masks. This proves readiness on the finite tested domain; it is not claimed as an efficient general-purpose solver.

### Executed scope

- All 256 bytes: compiler/unfold round trips.
- Original Ring 2 flattened orbit `00100111`: all phases, both directions, and stream lengths 8, 16, 32, 64 (64 runs). The first 8-bit block closes at arrival 8 even in the 64-arrival streams.
- Independent workbook cross-check: `Ring 2!B3`, `Ring 3!B3`, `Ring 4!B3` match the partner/grow ordering exactly. Testing all phases and both directions at lengths 8/16/32/64 for Ring 2 and Ring 4, and 8/16/24 for Ring 3, produced 720 stream runs: 64, 144, 512 by ring width. Every block round-tripped using a separate direct subset-XOR definition; each compiler closure had zero extra event wait. Ring 3 at length 24 retains a `16+8` frontier rather than falsely claiming one width-24 dyadic root.
- Every pair of 8-bit operands (65,536 pairs), all nine output bits including final carry, and three input orders (LSB-first, MSB-first, center-out). The independent observation-signature grouping reproduces the original event histogram for every output bit. LSB-first sum bit `j` settles at event `2j+2`; MSB-first final carry settles at event 2 for 32,768 pairs. Mean first-ready event / average wait behind an event-16 barrier: LSB-first 9.722222 / 6.277778; MSB-first 11.002170 / 4.997830; center-out 11.842014 / 4.157986.

### Interpretation and provenance limits

The workbook was read without edits. Its flattened R2/R3/R4 streams are `00100111`, `000001010110011101100111`, and `0000000100100011010101100111110110111110100110101100010010001111`. Workbook SHA-256: `c08b4ac4b1442853a74ebdd7098667a7499ecd8240efcd3da3c0e4624be640a1.

The local readiness script defines `compile_online` and `readiness` inside `readiness_first_audit.py`; it does not import `reactive_ledger.py`. So the tested implementation agrees with the stated emit-when-settled semantics, but “used `reactive_ledger.py` directly” is not evidenced by this archive. The exact semantic predicate is evaluated by exhaustive grouping on the 16-input arithmetic domain. Event numbers count bit arrivals, not physical seconds. No hardware latency or physical holding mechanism is inferred.

The first independent-verifier draft had a syntax error, detected by `py_compile` before assertions ran; the corrected file was sealed before its successful run, with an unchanged post-run source hash. The earlier original-audit rerun first needed its output directory created; no assertion ran on that initial invocation. These preflight/package corrections are recorded in the provenance bundle.

### Ledger update

| Item | Status |
|---|---|
| Online dyadic block closure and reversible transform | RUNS on bytes and declared ring streams |
| Ring 2/3/4 workbook orbit agreement | RUNS (three B3 strings) |
| Readiness predicate and output emission for all 8-bit operand pairs under three schedules | RUNS on the 65,536-pair domain; all output histograms reproduced |
| Efficient arbitrary-width readiness solver | OPEN (not claimed) |
| Physical latency / physical realization of holding | PULL |
| Direct use of `reactive_ledger.py` | UNBOUND by submitted archive; equivalent semantics were reimplemented locally |

Files: `readiness_first_audit.py`, `readiness_independent_prediction.txt`, `independent_readiness_crosscheck.py`, `independent_readiness_results.json`, `execution_provenance.json`, `readiness_first_log_entry.md`.

---

## 20. Folds, unfolds and the runtime as a Boolean map: peer results, replicated (2026-10-20)

Peer results arriving with Dean's message: the literal fold of each tape, its recursive unfold (unfold_actual_folds_bundle, two identical copies, sha256 `b599b227…a7b1`, source seal `5f0a3baf…3328`), and the runtime as a Boolean map (reply ce3c0464). Independent replication and extension sealed `349151d5…6fbef7` (folds/seal_folds.txt); 1.2 s; seal unchanged after.

**The fold reads the twist.** Fold a tape S = A‖B by laying the reversed lower half on the upper half: D = A ⊕ J(B). D is the palindromic-word mask of the left face, all ones on each palindromic word and zero elsewhere (U1 RUNS, L = 1–16; R3 E38 and R4 F0000F00, as the peer reported). Non-palindromic words coincide with their folded partners; palindromes meet their complements. The palindrome mask is not added to make the reflection work. It is the disagreement between the folded layers.

**The folded runtime.** Keep the depth j (address M−1−j on the left face, M+j on the right) and the face. The ring walk becomes a zig-zag: inward on the left face, across the seam 0L → 0R, outward on the right face, back at the closure (M−1)R → (M−1)L. At both turning points the depth holds while the face changes. This is §18's address-order hold seen as a walk: min(t, N−t) counts the depths with one face visited, and it peaks at the seam turn and vanishes at the closure turn. A depth-only reader loses the direction; the face carries it.

**The unfold.** Folding while the residual has even length, then inverting with S = A‖J(A ⊕ D), returns every tape exactly (U2 RUNS, L = 1–14; the peer's R2, R3, R4 chains reproduced). Extension, sealed and landed: L + v₂(L) folds; terminal width the odd part of L; terminal residual zero for every L ≥ 2; the residual after L folds is 0^L for L ≥ 3 (11 at L = 2), because it is the parity of the 2^(⌈L/2⌉−1) palindromic left-face words. The packet is lossless, not compression; every level past the first is read off the left face's words. The recursive fold is §12's mirror lift applied to the whole tape. At word scale a palindrome is where the mirror difference vanishes; at tape scale a palindromic word is where the difference is all ones. One lift at two scales, with the two readers exchanged.
Correction logged: the first comparison script read the R3 terminal 000, written in bits in the seal, against the hex print 0. The values are identical.

**The runtime as a Boolean map.** T^(2^L) = I, P² = I and P T P = T^−1 at every word (U3 RUNS, L = 1–16): successor and partner generate the ring's dihedral group, and reflection exchanges forward and reverse execution. Algebraic degree over GF(2): the partner has degree ⌊L/2⌋ (derived from P = J ⊕ pal(x)·1^L; RUNS L = 2–16); the forward and inverse runtimes have degree L−1 (RUNS L = 2–12), as nonlinear as a permutation can be. The peer's T₃ = (a⊕b, a⊕b⊕c⊕ab, 1⊕b⊕c⊕ab) reproduces exactly. In address coordinates the same runtime is +1. The nonlinearity is the coordinate change, and the instant compile (§17 W8) is the change of coordinates that turns the runtime into a counter.

**Reading frames.** Word i read from slice iL + f. Frames 0 and 1 are complete readings at every width (RUNS L = 2–16). Owner of frame 1, derived and landed (L = 4–16): the frame-1 word is rot(R[i] ⊕ g_i 2^(L−1)), with g_i marking a top-bit change from R[i] to R[i+1]. The change words are exactly {01^(L−1), 1^L} and {0J(a)0, 1J(a)0 : a a non-palindromic representative of width L−2}. Each non-palindromic frame-00 representative 0a0 sits between 0(a−1)1 and 0a1, so the partner face's top bit switches twice around it, at two words that differ only in the top bit. The change set is closed under a top-bit flip, so frame 1 is a permutation.
**DEAD END:** "every frame from 2 up is incomplete" holds only at L = 3, 4, 5. Frame 2 is a complete reading for every L = 6–16. Owner: the small widths of the peer's sample and my extrapolation from them. The frame-2 law itself is OPEN: the successors of the four words that share their low L−2 bits must carry four distinct top-two patterns.
Measured, not sealed: the last frame loses exactly 2^⌈L/2⌉ − 2 states (L = 3–16); frame 3 loses exactly 2^(⌈L/2⌉−1) (L = 8–16); no frame loses as many states as there are palindromes, 2^⌈L/2⌉.

| Item | Status |
|---|---|
| U1 fold residual = palindromic-word mask | SEALED, RUNS (L = 1–16) |
| U2 recursive fold and exact inverse; fold count, terminal width, zero terminal, parity level | SEALED, RUNS (L = 1–14); notation correction logged |
| Folded runtime: the depth holds and the face turns, at seam and closure | STANDS (peer); identified with the §18 triangle |
| U3 dihedral relation P T P = T^−1 | SEALED, RUNS (L = 1–16) |
| U4 degree: partner ⌊L/2⌋, runtime L−1 | SEALED, RUNS (L = 2–16; L = 2–12) |
| U5 frames 0 and 1 complete; frame-1 owner (change words) | SEALED, RUNS (L = 2–16; L = 4–16) |
| U5 frames from 2 up incomplete | DEAD END from L = 6; frame 2 complete for L = 6–16; its law OPEN |
| Frame losses: last frame 2^⌈L/2⌉ − 2, frame 3 2^(⌈L/2⌉−1) | measured |

---

## 21. The ring's own readiness: the path from above runs as soon as it can (2026-10-20)

Gap, named by what must be there. §19 gives "as soon as it can" an exact meaning: an output is ready when every input still possible gives the same value. The ring's decisions are made by the comparator at the outermost unequal mirror pair, and its frames are peeled from the outside. So the order that lets the ring compile soonest must deliver the word from its outer frame inward: the path from above. Every other order holds the decision back, and how much it holds must have a closed form.

Sealed `2bc9c18c…14a753` (readiness/seal_readiness.txt) before any run; 0.9 s; seal unchanged after. Orders: MSB-first, LSB-first, centre-out, and outside-in (pairs outermost to innermost, high member first, middle bit last). Face = [x > P(x)].

**RD1 RUNS — the face is ready after two pairs.** Under outside-in the face is ready at arrival 2(j+1), j the first unequal pair. When pairs 0..h−2 agree it is ready at 2h−1 if x_(n−h) = x_(n−1), otherwise at 2h. Exact at every word, n = 2–16. Mean 4 − 5·2^−h: 2.75, 3.6875, 3.9219, 3.9805 at n = 4, 8, 12, 16; under 4 at every width.

**RD2 RUNS — every other order holds it to the end.** Exact means, n = 2–16: MSB-first n − 1 − (h−1)2^−h (n even), n − 1 − (h+1)2^−h (n odd); LSB-first n − 1 + (h+1)2^−h; centre-out n − 1/2 − 2^−h. At n = 16: outside-in 3.98, MSB-first 14.97, LSB-first 15.04, centre-out 15.50. Outside-in ties MSB-first at n = 4 (2.75) and is strictly earliest from n = 5.

**RD3 RUNS — where comes out from the top.** The mean readiness of the n address bits, and of the folded coordinates (face and depth), is smallest under outside-in at every n = 5–14. At n = 14 the address mean is 11.19 against 12.92 (MSB-first), 12.98 (LSB-first) and 13.19 (centre-out). Read from above, the address comes out top-down at about one address bit per arriving pair: 3.96, 5.81, 7.69, 9.48, 10.79, 12.14 for its top six bits at n = 14. Read MSB-first, every address bit waits until 12.6–13.6.

Measured, not sealed: the decompile runs the same way. With the address arriving MSB-first, the word comes out from its outer frame inward. At n = 14 the mirror pairs, outer to inner, are ready at 8.31, 9.67, 10.09 on average, then level near 10.2; the top bit comes first, at 6.91.

What fell out.
- The ring has a native reading order, and it is the path from above. Read outside-in, the reflection decision is ready the instant the pair that decides it arrives, in under four arrivals at any width. Read in the counter's own order (MSB-first, the value), the same decision waits until about one arrival before the end. Holding is now exact per order: n − 1 − O(h·2^−h) against 4 − 5·2^−h.
- Same path, different location. The peer's adder (§19) is ready soonest LSB-first: sum bit j at arrival 2j+2, so nothing waits beyond its own operands. Its DI chain is the carry, which runs from the bottom. The ring is ready soonest outside-in, because its DI chain is the comparator, which runs from the outer frame. Each machine runs as soon as it can only when it is read in the direction its chain flows; read against the chain, its outputs are held.
- The compile streams in both directions. Read from above, the address comes out from its top bit down. Given the address from its top bit, the word comes out from its outer frame in.
- The face is the direction the fold hides (§20). A depth-only reader never sees it; the outside-in reader has it after two pairs; the value reader not until the end.

### Ledger additions

| Item | Status |
|---|---|
| RD1 outside-in face readiness, exact per word, mean 4 − 5·2^−h | SEALED, RUNS (n = 2–16) |
| RD2 closed-form means for MSB-first, LSB-first, centre-out | SEALED, RUNS (n = 2–16) |
| RD2 outside-in strictly earliest from n = 5, tie at n = 4 | SEALED, RUNS |
| RD3 address and folded coordinates earliest outside-in | SEALED, RUNS (n = 5–14) |
| Decompile emits the word outside-in | measured |
| Native order = the direction of the DI chain (adder LSB-first, ring outside-in) | reading from §19 and RD1–RD3; general claim OPEN |

### Next stroke

Is the path from above the best possible reader, not only the best of four? Seal that outside-in attains the minimum mean face readiness, and the minimum mean address readiness, over all n! arrival orders for n = 4–8 (exhaustive, with ties declared in the seal). Then the frame-2 law (§20 OPEN), by the change-word argument one bit deeper.

Files: folds/fold_replicate.py, seal_folds.txt, fold_output.txt, fold_results.json; readiness/readiness_ring.py, seal_readiness.txt, readiness_output.txt, readiness_results.json; inbox/ holds the four peer bundles, each unpacked separately.

---

## 22. The song that plays both ways: bookends, twins and the reader (2026-10-20)

Dean, translating the ring for a music producer (DJ Clay, ICP): a song that plays the same in both directions. c-d-e-d-c alone is perfect; c-d-e-d-c | e-d-c-d-e "crashes". The bookends fix the possibilities, not in total but in reflection; the middle fills from the centre out as pairs, and that constraint is what made the twins. Every song is a projection you address, not enumerate. Context and code: a palindrome at the melody layer is not one at the waveform layer unless the layers fold together. Doom against the placemat maze: the hard part sits in the point of view. Two peer replies came with it, d195fbe7 (a summary through §21 with an optimality argument and a frame-2 sketch) and 7f8cf7d6 (a quantum-ring correspondence and three probes); both are audited at the end of this entry.

Sealed `86152e14…9b9f81` (song/seal_song.txt) before any run; 4.8 s; seal unchanged after. Dean stopped the first launch after it had written the audio files; no result was read from it.

**S1 RUNS — bars fill from the centre out as twins.** Exhaustive over 5,050 binary songs (up to 4 bars of up to 3 slices): a song is a palindrome iff bar B+1−k is the retrograde of bar k. Bars can be chained into a palindrome only as twins around the centre.

**S2 RUNS — a song that holds every bar once cannot play both ways.** No ordering of all 2^L bars is a palindrome (every ordering at L = 1, 2, 3: 2, 24 and 40,320 of them), because a palindromic bar would have to face itself. The ring's tape played backward is the tape with exactly its palindromic bars inverted (L = 1–16). This is why the ring needs the twist.

**S3 RUNS — the crash is the twist.** With notes symmetric about their own centres, c-d-e-d-c backward equals c-d-e-d-c (relative error 2.8e−16). c-d-e-d-c | e-d-c-d-e backward equals the same song inverted about d (2.8e−16), and differs from itself played forward by 110%. The R3 tape as a rhythm, played backward, equals the tape with its palindromic bars inverted (2.6e−16). With attack-decay notes, c-d-e-d-c backward differs from itself forward by 131% although its notes are a palindrome. The crash is the retrograde coming out as the inversion, which is exactly what the ring does with every self-symmetric bar. A palindrome at the note layer is a palindrome at the waveform layer only when every note is symmetric: context and code have to fold together.

**S4 RUNS — the palindrome wave file, in frequency.** With phase referenced to the tape's centre, the real part of the tape's spectrum is exactly the spectrum of the twin bars and the imaginary part exactly that of the self-symmetric bars, at every L = 1–16 (deviation at most 6.4e−16 of the peak). The imaginary share is 2^(⌈L/2⌉−L), falling to 1/256 at L = 16. This is §5's Walsh parity split, read in Fourier.

**S5 — the reader carries the hard part.**
- RUNS: over all n! orders, the least mean number of arrivals until the face is fixed is 4 − 5·2^−h at every n = 5–14 (an exact dynamic programme over all 2^n observed-bit sets). For n = 6–14 it is attained by exactly the 2^h orders that read the mirror pairs from the outside in, either member first, middle bit last: 8, 8, 16, 16, 32, 32, 64, 64, 128 orders. At n = 4, MSB-first also attains 11/4, as sealed.
- DEAD END: "exactly 2^h optimal orders at n = 5". There are 12. Owner: at h = 2 the face is the top bit except for one pattern of the other three outer bits for each top-bit value (0100 and 1011 at n = 4; 01·00 and 10·11 at n = 5). So the top bit plus any one of those three bits rules out the exception half the time, exactly as the outermost pair does. From h = 3 on the exceptions are many, and only the outermost pair halves them.
- DEAD END: "an outside-in order is the best address reader". It is best only at n = 6. The best reader takes the outer pairs from the outside in, then the innermost core (the last two pairs at even n; the last pair and the middle at odd n) by value. It beats outside-in by 0.05 arrivals per bit at n = 5 and by 0.002–0.023 at n = 7–12. Owner, read after the run: Route 7's address is a frame count from the outside plus a value count inside. Once the outer frames fix the face and the column, the core is a counter. The reflection is read from above; the core is read by the other wheel.

What fell out.
- Dean's intuition, in exact form. The bookends fix the count in reflection: 2^⌈L/2⌉ palindromes, (2^L + 2^⌈L/2⌉)/2 classes under retrograde alone, and with the twist exactly 2^(L−1) twin pairs with none left single. The middle fills from the centre out as twins (S1). A song holding every bar once cannot play both ways (S2), so pairing every bar needs a second move, inversion, and the crash is that move heard (S3).
- Context and code. The note layer and the waveform layer must both be palindromic for the file to be (S3). The ring's tape is palindromic on its twins and anti-palindromic on its self-symmetric bars, and its spectrum separates the two exactly (S4).
- Point of view. Of every possible way to read a word, the fastest way to know which twin you hold is from the bookends inward. The address is read from the bookends inward, then by value at the core. The hard part sits in the reader.
- Collisions, as Dean predicted. Messiaen's non-retrogradable rhythms are the palindromes, built by flanking a central value with mirrored values. The serial operations prime, retrograde, inversion and retrograde-inversion form the group ⟨J, C⟩. Crab canons (Machaut's *Ma fin est mon commencement*, the crab canon in Bach's *Musical Offering*) are retrograde pairings. Symmetric and antisymmetric linear-phase FIR filters are the twin and self-symmetric parts, and time reversal conjugates the spectrum. What the ring adds: retrograde alone leaves the non-retrogradable phrases unpaired. The ring pairs them by inversion, so every phrase has exactly one twin, an O(L) address, and a reading order that decides its side in under four arrivals.
- What addressing does and does not do. Every song has an address and comes back from it in O(L) (§17 W8), but the number of songs stays 2^L. The ring gives random access to any one of them, not a short list of all.

Peer replies audited.
- **d195fbe7.** Its summary of §17–§21 is accurate. Its optimality argument predicts exactly 2^h orders, which holds from n = 6 and fails at n = 4 and 5 (12 orders each). Its frame-2 provider sketch is not a proof; that law stays OPEN.
- **7f8cf7d6.** The quantum-ring correspondences (Aharonov–Bohm phase, persistent current, interference fringes, quantized angular momentum) are PULL. The ring's twist is a Z2 sign on one sector under reflection, a formal relative of an antiperiodic boundary condition, not a measured flux.
  - Case A holds exactly: a palindromic bar followed by its inversion lies on the anti-diagonal J(x) = C(x), at latitude 0, and merges with its partner 100% grey. It is the bar-level form of S3.
  - Case B has two corrections. 0110011001100110 is a canonical palindrome at address 21,021 (Δ = 15,726, ℛ₈(102, 102) = 42), not 21,025. Its continuation stops at depth 1 with root 00110011001100, not 0110.
  - "Exactly 4 of 24 orders at n = 4" is wrong: there are 12.
  - Its frame-3 question is answered by §20's data: frame 3 stays incomplete through L = 16 and loses exactly 2^(⌈L/2⌉−1) states from L = 8. The complete frames are 0, 1, and 2 from L = 6.

### Ledger additions

| Item | Status |
|---|---|
| S1 palindromic song = twin bars around the centre | SEALED, RUNS (exhaustive) |
| S2 no song with every bar once is a palindrome; ring tape backward = palindromic bars inverted | SEALED, RUNS (L = 1–3 exhaustive; tapes L = 1–16) |
| S3 crash song backward = inverted; attack-decay notes break the file palindrome | SEALED, RUNS (rendered audio) |
| S4 spectrum: real part = twins, imaginary part = self-symmetric bars, share 2^(⌈L/2⌉−L) | SEALED, RUNS (L = 1–16) |
| S5 least face readiness over all n! orders = 4 − 5·2^−h | SEALED, RUNS (n = 5–14) |
| S5 exactly 2^h optimal orders, all outside-in | SEALED, RUNS (n = 6–14); DEAD END at n = 5 (12 orders; owner: the h = 2 exception pattern) |
| S5 outside-in is the best address reader | DEAD END (best only at n = 6); best reader = outside-in frames, then the core by value |
| Collisions: Messiaen, serial ⟨R, I⟩, crab canon, linear-phase FIR, spectral conjugation | STANDS (known); the ring's addition is the inversion pairing, address and reader |
| Quantum-ring correspondence | PULL |

### Next stroke

Seal the two-wheel reader as a law: the best address reader reads outside-in down to a core of four bits (even n) or three bits (odd n), then the core by value, with the optimum computed exactly for n = 13–16. Then the frame-2 law (§20 OPEN).

Files: song/song_tests.py, seal_song.txt, song_output.txt, song_results.json, audio/01–09 (WAV, 22,050 Hz mono).
