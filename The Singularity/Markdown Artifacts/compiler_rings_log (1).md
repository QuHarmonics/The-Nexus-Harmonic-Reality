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
