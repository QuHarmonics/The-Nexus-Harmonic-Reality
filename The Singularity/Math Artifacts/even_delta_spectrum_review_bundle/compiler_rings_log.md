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
