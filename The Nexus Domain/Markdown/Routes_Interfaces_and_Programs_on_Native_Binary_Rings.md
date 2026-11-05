# Routes, Interfaces and Programs on Native Binary Rings

*Addendum to Facing, Composition and the Center in Native Binary Rings*

Dean A. Kulik · QuHarmonics Research Group · ORCID 0009-0003-3128-8828

5 November 2026

## Abstract

This addendum carries the facing manual's reading of single contacts to whole routes, circular routes, the interfaces of affine programs, the center of a register under motion, and programs taken as transition tables. Facing applied contact by contact keeps a closed route of the wheel B(n) closed exactly when every palindromic contact pair that carries a defect appears whole or not at all, and the defects sit on disjoint sets of four faces {u, Ju, Cu, CJu}. A circular route is its own facing partner exactly when it is a palindrome followed by its own NOT, repeated; each dyadic half-period s contributes 2<sup>⌈s/2⌉−1</sup> of them, and odd lengths contribute none.

The 322,560 affine programs of LEN 4 form 25 interfaces, the number derived before the run from the centralizer orbits on coker(A + I). Nineteen contain their own inverse, and six form three mirror-twin pairs, whose linear parts have reciprocal characteristic polynomials. Reversal, reversal followed by NOT, and the half turn are one interface; the twisted clock occupies the translated Jordan block [4]; the shift register with feedback x<sub>0</sub> ⊕ x<sub>3</sub> is a Singer cycle. Facing, the native successor, the increment and the Gray counter leave the affine catalog.

On the paired register at odd LEN, facing and NOT act as NOT on the center alone, and the twisted clock carries the center's difference one site per tick. The native successor keeps 1 − 2<sup>−k</sup> of the difference on the center and moves 2<sup>−k</sup> to the last site through the poles 0<sup>n</sup> and 1<sup>n</sup>, which meet at the closure of the ring; the sealed prediction that it erases the difference failed. A reversible program is native, meaning facing carries its transition table onto itself, exactly when reading it backward runs it backward and its self-reading states are closed under NOT. There are 2, 6, 188 and 3,460,368 native programs at LEN 1–4. A shift program is native exactly when its feedback reads the same on a word and its reversal and agrees on complementary palindromes, which gives 2<sup>N/4</sup> native shift programs on the N = 2<sup>n</sup> words of LEN n, none of them a maximal-length register. The twisted clock reproduces itself one LEN up: its contacts are the next clock with the poles removed. The ring stores each word's reading direction as its top address bit, exchanged only across the seam, and its first two rings are NOT and reversal: R<sub>1</sub> = 1|0 and R<sub>2</sub>[a] = J<sub>2</sub>(a). At odd LEN facing reads the word from its center: the center flips exactly when the rest of the word reads the same both ways, a k-controlled NOT. Holding the center's response to facing forces signed amplitudes read by their squares, and definite responses to the ring's clock force complex phases at every even LEN.

## Contents

- 1  Scope and how to use this addendum
- 2  Closed routes of the wheel
- 3  Circular routes
- 4  The LEN-4 interface catalog
- 5  The center under ring motions
- 6  Native programs
- 7  The twisted clock one LEN up
- 8  The reading direction as one address bit
- 9  The reader at the center
- 10  Technical notes
- 11  Ledger
- 12  How it continues
- Appendix A  Seals
- Appendix B  Reproduction
- References

## 1  Scope and how to use this addendum

This addendum holds the manual's founding claim fixed. Difference is existence, the first distinction is NOT, and chained difference routes, that is transformations, are the constitutive substrate of reality. The manual mapped how the ring reads a single contact in both directions. The same reading is carried here to whole routes, to circular routes with no marked start, to the interfaces of affine programs, to the center of a register under motion, and to programs as transition tables.

The addendum continues Section 14 of the manual. Item 1 (split the closed routes) is Section 2, item 3 (complete the LEN-4 catalog) is Section 4, and item 4 (test the center) is Section 5. Sections 3, 6, 7, 8 and 9 add circular routes, native programs, the twisted clock one LEN up, the reading direction as an address bit, and the reader at the center. Objects, notation, the native ring and the two contact models are those of the manual, Section 3. The status labels are the manual's: **STANDS** (proved for every LEN), **RUNS** (checked on every word in the stated range), **measured**, **ELSEWHERE**, **OPEN** and **PULL**.

Five prediction sets were sealed before their computations: predictions14 (the LEN-4 catalog and the motion of the center), predictions15 (native programs and the twisted clock one LEN up), predictions16 (native feedback shift programs), predictions17 (the reading direction as one address bit) and predictions18 (the reader at the center). Appendix A gives their text and SHA-256 hashes. Every sealed claim landed except P14.6 and the LEN-1 clauses of P17.1 and P17.3, which failed as sealed; Sections 5 and 8 record them and state what runs.

External notebooks supplied the reversal formulas for closed routes, the circular-seam classification, the fixed-necklace count, a program survey, a first draft of this addendum, and the observation that the reading direction collapses to one address bit. Each result taken from them was re-derived or re-run here by a different route, and Technical Note A2 lists the corrections. Every table is produced and asserted by one script, `addendum_tables.py` (Appendix B). Each section gives the objects, a theorem with its proof, a procedure with an example, and a table.

## 2  Closed routes of the wheel

### 2.1  Objects

The wheel B(n) has the 2<sup>n</sup> words of LEN n as faces and the 2<sup>n+1</sup> words of LEN n+1 as contacts. A contact e runs from IN(e) = e<sub>0</sub>…e<sub>n−1</sub> to OUT(e) = e<sub>1</sub>…e<sub>n</sub>. Over F<sub>2</sub> its boundary is ∂e = IN(e) + OUT(e), and a closed route is a set of contacts with zero boundary: every face is touched an even number of times. The closed routes form the space Z<sub>n</sub> = ker ∂, of dimension 2<sup>n</sup> + 1, the cycle rank of the connected wheel (manual, Section 3.6).

Write p = 2<sup>⌈n/2⌉</sup> for the number of faces that read the same both ways and q = 2<sup>⌈(n+1)/2⌉</sup> for the number of contacts that do. Reversal acts on contacts as J<sub>n+1</sub> and facing as P<sub>n+1</sub>: a contact that reads differently backward is faced by its reversal, a palindromic contact by its NOT. Applied contact by contact, both act on routes. Over F<sub>2</sub> an involution splits a space into t blocks it fixes and r two-dimensional blocks whose two halves it exchanges, so the dimension is t + 2r and the fixed dimension is t + r.

### 2.2  Reversal

**Theorem A1 (closed routes under reversal).** Reversal maps closed routes to closed routes. On Z<sub>n</sub> it has t = p + q − 1 fixed blocks and r = (2<sup>n</sup> + 2 − p − q)/2 exchanged pairs, and the closed routes that read the same both ways span dim Z<sub>n</sub><sup>J</sup> = (2<sup>n</sup> + p + q)/2. **STANDS**; **RUNS** n = 1–10.

**Proof.** A contact read backward exchanges its ends and reverses each: IN(Je) = J(OUT e) and OUT(Je) = J(IN e). So ∂J = J∂, and closed routes go to closed routes. The contact chains fixed by reversal span (2<sup>n+1</sup> + q)/2 dimensions. Their boundaries fill exactly the image of I + J on faces: a palindromic contact from u has boundary u + Ju, a pair e + Je has boundary (I + J)∂e, and a path γ from 0<sup>n</sup> to any face v gives the fixed chain γ + Jγ with boundary v + Jv. That image has dimension (2<sup>n</sup> − p)/2, so dim Z<sup>J</sup> = (2<sup>n+1</sup> + q)/2 − (2<sup>n</sup> − p)/2 = (2<sup>n</sup> + p + q)/2. Then r = (2<sup>n</sup> + 1) − dim Z<sup>J</sup> and t = dim Z<sup>J</sup> − r. ∎

### 2.3  Facing

**Theorem A2 (closed routes under facing).** Write a closed route as z = z<sub>dir</sub> + z<sub>pal</sub>, its direction-faced and its palindromic contacts. Facing applied contact by contact gives a chain with boundary ∂(Pz) = (I + C)∂(z<sub>pal</sub>).

- (i) The palindromic contacts form q/2 complement pairs {e, Ce}. The defect of the pair of a contact from u is the set of four faces {u, Ju, Cu, CJu}. It vanishes for the constant pair and, at even n, for the alternating pair. Every other defect has four distinct faces, and no face lies in two defects. **STANDS**; **RUNS** n = 1–14.
- (ii) Pz is closed exactly when every pair with a defect appears in z whole or not at all: both contacts or neither, counted mod 2. **STANDS**.
- (iii) The closed routes that facing keeps closed span dim Z<sup>P</sup> = 2<sup>n</sup> − q/2 + 2 + [n even]. Facing has t<sub>P</sub> = p + q/2 − 2 − [n even] fixed blocks on them and exchanges r<sub>P</sub> = r + 1 + [n even] pairs. **STANDS** wherever the wheel stays connected without its palindromic contacts, which **RUNS** n = 1–18; the dimensions **RUN** n = 1–10 by stacked F<sub>2</sub> ranks.

**Proof.** Since ∂z = 0, ∂z<sub>dir</sub> = ∂z<sub>pal</sub>. The direction-faced contacts contribute J∂z<sub>dir</sub> = J∂z<sub>pal</sub>, and J fixes the boundary u + Ju of every palindromic contact, so this is ∂z<sub>pal</sub>; the palindromic contacts contribute C∂z<sub>pal</sub>. The sum is (I + C)∂z<sub>pal</sub>, and (I + C)(u + Ju) = u + Ju + Cu + CJu. A palindromic contact from u forces u<sub>i</sub> = u<sub>n−i</sub> for 1 ≤ i ≤ n−1. If Ju or CJu also starts a palindromic contact, then u<sub>j</sub> = u<sub>n−2−j</sub> as well, so u has period 2 and Ju ∈ {u, Cu}. That leaves only the constant pair and, at even n, the alternating pair, whose four faces cancel, and it shows that no face belongs to two defects. Disjoint nonempty defects are independent, which gives (ii). For (iii), a contact with a defect, closed by a path from OUT(e) back to IN(e) that avoids palindromic contacts, is a closed route that meets one defect pair once, so the q/2 − 1 − [n even] constraints of (ii) are independent. The routes fixed by facing are spanned by the pairs e + Pe. Their boundaries again fill the image of I + J, since each defect equals (I + J)(u + Cu), so dim (Z<sup>P</sup>)<sup>P</sup> = 2<sup>n</sup> − (2<sup>n</sup> − p)/2 = (2<sup>n</sup> + p)/2, and t<sub>P</sub> and r<sub>P</sub> follow as in Theorem A1. ∎

### 2.4  Procedure A: does facing keep a closed route closed?

1. List the route's palindromic contacts.
2. Group them into complement pairs {e, Ce}. Drop the constant pair and, at even n, the alternating pair.
3. The faced route is closed exactly when every remaining pair appears with both contacts or with neither.

Example (n = 3). The palindromic contacts of LEN 4 are 0000, 0110, 1001 and 1111. The constant pair {0000, 1111} carries no defect; the pair {0110, 1001} carries {011, 110, 100, 001}. The closed route 011 → 110 → 101 → 011 uses the contacts 0110, 1101 and 1011. Facing gives 1001, 1011 and 1101, whose boundary is 100 + 001 + 011 + 110, the defect of the pair: 0110 appears without 1001.

*Table A1. Closed routes of the wheel B(n) under reversal and under contact-wise facing (stacked F<sub>2</sub> ranks; every entry equals its formula).*

| n | dim Z | p | q | dim Z<sup>J</sup> | t | r | defect pairs | dim Z<sup>P</sup> | t<sub>P</sub> | r<sub>P</sub> |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 3 | 2 | 2 | 3 | 3 | 0 | 0 | 3 | 1 | 1 |
| 2 | 5 | 2 | 4 | 5 | 5 | 0 | 0 | 5 | 1 | 2 |
| 3 | 9 | 4 | 4 | 8 | 7 | 1 | 1 | 8 | 4 | 2 |
| 4 | 17 | 4 | 8 | 14 | 11 | 3 | 2 | 15 | 5 | 5 |
| 5 | 33 | 8 | 8 | 24 | 15 | 9 | 3 | 30 | 10 | 10 |
| 6 | 65 | 8 | 16 | 44 | 23 | 21 | 6 | 59 | 13 | 23 |
| 7 | 129 | 16 | 16 | 80 | 31 | 49 | 7 | 122 | 22 | 50 |
| 8 | 257 | 16 | 32 | 152 | 47 | 105 | 14 | 243 | 29 | 107 |
| 9 | 513 | 32 | 32 | 288 | 63 | 225 | 15 | 498 | 46 | 226 |
| 10 | 1025 | 32 | 64 | 560 | 95 | 465 | 30 | 995 | 61 | 467 |

## 3  Circular routes

### 3.1  Objects

A circular route of length L is a word read around a circle with no marked start: the necklace [w], the class of w under rotation. It reads the same both ways, or is achiral, when [Jw] = [w]. Such a necklace is mapped to itself by a reflection of the circle. At odd L every reflection axis passes through one bit and the gap opposite it, and cutting at that gap reads a palindrome: a reading seam. At even L an axis passes either through two gaps, each a reading seam, or through two bits, a hinge with no palindromic cut. Cyclic facing sends an achiral necklace to [Cw] and every other necklace to [Jw]: the rule for words, applied to the class.

### 3.2  Theorem

**Theorem A3 (circular routes).** Write p = 2<sup>⌈L/2⌉</sup> and q = 2<sup>⌈(L+1)/2⌉</sup>.

- (i) Achiral necklaces number (p + q)/2. **STANDS**.
- (ii) At odd L each achiral necklace holds exactly one palindrome among its rotations, a unique reading seam. At even L an achiral necklace either holds palindromic rotations or has hinge axes only, and both kinds occur at every even L. **STANDS**; counts **RUN** L = 1–18.
- (iii) Cyclic facing is well defined on necklaces and is an involution. **STANDS**.
- (iv) A necklace is its own facing partner exactly when it is (u | Cu)<sup>r</sup>: a palindrome u of length s followed by its NOT, repeated r = L/2s times. Write L = 2<sup>a</sup>k with k odd. Every such necklace has exactly one dyadic level b < a with s = 2<sup>b</sup>k, and it holds exactly two such palindromes, u and Cu. Level b therefore contributes 2<sup>⌈s/2⌉−1</sup> necklaces. **STANDS**; **RUNS** L = 1–18 against brute force.

> Fixed(L) = 0 at odd L,     Fixed(2<sup>a</sup>k) = Σ over b = 0, …, a−1 of 2<sup>⌈s/2⌉−1</sup>,  with s = 2<sup>b</sup>k

**Proof.** (i) By the orbit-counting lemma for a coset, the achiral necklaces number the average count of words fixed by the L reflections: 2<sup>(L+1)/2</sup> for each axis at odd L, and 2<sup>L/2+1</sup> and 2<sup>L/2</sup> for the two kinds of axis at even L. (ii) If w and its rotation by d both read the same both ways, w is invariant under rotation by 2d, and at odd L that makes it invariant under rotation by d, so the two palindromes coincide. (iii) Achirality is a property of the class, [Cw] and [Jw] are classes, and [Cw] is achiral when [w] is, so applying the rule twice returns [w]. (iv) If [Cw] = [w], some rotation complements w, and twice that rotation fixes it, so the complementing rotations are the odd multiples of half the minimal period. None exists at odd L. Otherwise let b be the 2-adic order of the half period; the rotation by s = 2<sup>b</sup>k is an odd multiple of it and complements w, so w = (u | Cu)<sup>r</sup> with u its first s bits, and b is the only level whose rotation complements. Rotating such a w by one bit acts on u as the twisted clock τ<sub>s</sub>, so the necklaces at level b are the orbits of τ<sub>s</sub> on words of length s, and [w] is achiral exactly when the orbit of u contains Ju. Read the orbit as one tape on which each bit is followed s steps later by its NOT. If Ju = τ<sup>t</sup>u, the tape is symmetric about one point and antisymmetric about the point s/2 further on. An antisymmetric point cannot sit on a bit, so t is even and τ<sup>t/2</sup>u reads the same both ways. Two palindromes in one orbit differ by a τ<sup>j</sup> with τ<sup>2j</sup>u = u, which leaves only u and τ<sup>s</sup>u = Cu. So each fixed necklace at level b holds exactly one complement pair of palindromes, and the 2<sup>⌈s/2⌉</sup> palindromes of length s give 2<sup>⌈s/2⌉−1</sup> necklaces. ∎

### 3.3  Procedure B: is a circular route its own facing partner?

1. If L is odd: no.
2. If [Jw] ≠ [w]: no. Its partner is its reversal.
3. Find the smallest rotation d that turns w into Cw. If there is none: no. Its partner is its NOT.
4. Otherwise yes. Rotate w until its first d bits read the same both ways; then w = (u | Cu)<sup>L/2d</sup>.

Example. Take 01101001 at L = 8. Rotating by 4 gives 10010110, which is its NOT, and no smaller rotation does. The first four bits, 0110, read the same both ways, so the necklace is (0110 | 1001) and is its own facing partner (Figure 1).

*Figure 1. The four circular routes of length 8 that are their own facing partner. Dark beads are 1. The gold arc marks u and the blue arc Cu: rotating by s exchanges them, which is NOT. The dashed axis through u is a reading seam, so reversal fixes the route as well.*

*Table A2. Circular routes of length L. Fixed: necklaces that are their own facing partner, with the contribution of each dyadic level b = 0, 1, … (brute force; equal to the formula).*

| L | necklaces | achiral (p + q)/2 | with a palindromic seam | hinge only | fixed | by level b |
|---|---|---|---|---|---|---|
| 1 | 2 | 2 | 2 | 0 | 0 | — |
| 2 | 3 | 3 | 2 | 1 | 1 | 1 |
| 3 | 4 | 4 | 4 | 0 | 0 | — |
| 4 | 6 | 6 | 3 | 3 | 2 | 1 + 1 |
| 5 | 8 | 8 | 8 | 0 | 0 | — |
| 6 | 14 | 12 | 6 | 6 | 2 | 2 |
| 7 | 20 | 16 | 16 | 0 | 0 | — |
| 8 | 36 | 24 | 9 | 15 | 4 | 1 + 1 + 2 |
| 9 | 60 | 32 | 32 | 0 | 0 | — |
| 10 | 108 | 48 | 20 | 28 | 4 | 4 |
| 11 | 188 | 64 | 64 | 0 | 0 | — |
| 12 | 352 | 96 | 34 | 62 | 6 | 2 + 4 |
| 13 | 632 | 128 | 128 | 0 | 0 | — |
| 14 | 1182 | 192 | 72 | 120 | 8 | 8 |
| 15 | 2192 | 256 | 256 | 0 | 0 | — |
| 16 | 4116 | 384 | 129 | 255 | 12 | 1 + 1 + 2 + 8 |
| 17 | 7712 | 512 | 512 | 0 | 0 | — |
| 18 | 14602 | 768 | 272 | 496 | 16 | 16 |

Up to L = 8 the fixed necklaces are 01 at L = 2; 0011 and 0101 at L = 4; 000111 and 010101 at L = 6; and 00001111, 00101101, 00110011 and 01010101 at L = 8, each written as its smallest rotation.

## 4  The LEN-4 interface catalog

### 4.1  Interfaces of affine programs

An affine program of LEN L is g(x) = Ax + b with A invertible over F<sub>2</sub>. Two programs are the same interface when one is the other read through an affine relabeling of the words, g′ = hgh<sup>−1</sup> (manual, Section 11.1). Conjugating by a translation moves b by the image of A + I, and conjugating by a linear H that commutes with A moves b to Hb. So the interfaces with linear part A are the orbits of the centralizer of A on the cokernel of A + I. A program has a fixed word exactly when b lies in the image of A + I, so each linear class has one interface with fixed words, and its other interfaces are translated and fixed-point-free.

GL(4,2) has 14 classes of linear part: the unipotent Jordan types [1,1,1,1], [2,1,1], [2,2], [3,1] and [4]; q+[1,1] and q+[2] with q = x<sup>2</sup> + x + 1; q+q and q²; c₁+[1] and c₂+[1] with c₁ = x<sup>3</sup> + x + 1 and c₂ = x<sup>3</sup> + x<sup>2</sup> + 1; and the irreducible quartics x<sup>4</sup> + x<sup>3</sup> + x<sup>2</sup> + x + 1, x<sup>4</sup> + x + 1 and x<sup>4</sup> + x<sup>3</sup> + 1. Their centralizer-orbit counts are 2, 3, 2, 3, 2; 2, 2; 1, 1; 2, 2; 1, 1, 1.

**Theorem A4 (the LEN-4 catalog).**

- (i) AGL(4,2), with 322,560 programs, has 25 interfaces, the sum of the orbit counts. Derived before the run (P14.1); **RUNS**.
- (ii) The inverse of x ↦ Ax + b has linear part A<sup>−1</sup>, whose characteristic polynomial is the reciprocal of that of A. The interfaces whose polynomial is not its own reciprocal therefore pair up as mirror twins, each the way home of the other: c₁+[1] with c₂+[1] (order 7, two fixed words), the same pair translated (order 14), and the Singer cycles x<sup>4</sup> + x + 1 with x<sup>4</sup> + x<sup>3</sup> + 1 (order 15). **STANDS**. The other nineteen interfaces contain their own inverse. **RUNS** (P14.2).
- (iii) The motion signature, the cycle type of g on the 16 words together with the cycle type of its contact-difference map Dg(t) = g(x + t) + g(x) = At, takes 22 values and separates every interface except the twins; the cycle type of g alone takes 19. The characteristic polynomial of A separates the twins. **RUNS** (P14.3). At LEN 3 the signature takes 10 values on 11 interfaces with one twin pair.

### 4.2  Where the ring’s motions sit

Table A3 places the ring's own motions at LEN 4. Reversal J, reversal followed by NOT (CJ) and the half turn σ² are one interface: each fixes four words and exchanges the other twelve in pairs. Rotation after reversal, σJ, exchanges two positions and is the same interface as a controlled NOT. Rotation σ and its inverse occupy the Jordan block [4]. The twisted clock τ and its inverse occupy the translated [4], τ² the translated [2,2], and τJ the translated transvection. NOT is a pure translation. The shift register with feedback x<sub>0</sub> ⊕ x<sub>3</sub> runs once through all fifteen nonzero words: a Singer cycle with polynomial x<sup>4</sup> + x<sup>3</sup> + 1, whose way home is its mirror twin x<sup>4</sup> + x + 1. Facing P<sub>4</sub>, the native successor T<sub>4</sub>, the increment and the Gray counter are not affine. At LEN 4 the native partner leaves the affine catalog: P<sub>4</sub> has algebraic degree 2 (manual, Theorem 5.3).

*Table A3. The 25 interfaces of AGL(4,2). Cycle types carry multiplicities as exponents (2<sup>4</sup> 1<sup>8</sup>: four exchanges and eight fixed words). Linear parts as in Section 4.1.*

| # | programs | order | fixed | cycle type of g | cycle type of Dg | linear part | translated | ring motions and programs |
|---|---|---|---|---|---|---|---|---|
| 0 | 1 | 1 | 16 | 1<sup>16</sup> | 1<sup>16</sup> | [1,1,1,1] | no | identity |
| 1 | 210 | 2 | 8 | 2<sup>4</sup> 1<sup>8</sup> | 2<sup>4</sup> 1<sup>8</sup> | [2,1,1] | no | σJ, CNOT |
| 2 | 840 | 2 | 4 | 2<sup>6</sup> 1<sup>4</sup> | 2<sup>6</sup> 1<sup>4</sup> | [2,2] | no | J, CJ, σ² |
| 3 | 15 | 2 | 0 | 2<sup>8</sup> | 1<sup>16</sup> | [1,1,1,1] | yes | C (NOT) |
| 4 | 630 | 2 | 0 | 2<sup>8</sup> | 2<sup>4</sup> 1<sup>8</sup> | [2,1,1] | yes | τJ |
| 5 | 4,480 | 3 | 4 | 3<sup>4</sup> 1<sup>4</sup> | 3<sup>4</sup> 1<sup>4</sup> | q+[1,1] | no | — |
| 6 | 1,792 | 3 | 1 | 3<sup>5</sup> 1 | 3<sup>5</sup> 1 | q+q | no | — |
| 7 | 5,040 | 4 | 4 | 4<sup>2</sup> 2<sup>2</sup> 1<sup>4</sup> | 4<sup>2</sup> 2<sup>2</sup> 1<sup>4</sup> | [3,1] | no | — |
| 8 | 20,160 | 4 | 2 | 4<sup>3</sup> 2 1<sup>2</sup> | 4<sup>3</sup> 2 1<sup>2</sup> | [4] | no | σ, σ⁻¹ |
| 9 | 5,040 | 4 | 0 | 4<sup>2</sup> 2<sup>4</sup> | 4<sup>2</sup> 2<sup>2</sup> 1<sup>4</sup> | [3,1] | yes | — |
| 10 | 840 | 4 | 0 | 4<sup>4</sup> | 2<sup>4</sup> 1<sup>8</sup> | [2,1,1] | yes | — |
| 11 | 2,520 | 4 | 0 | 4<sup>4</sup> | 2<sup>6</sup> 1<sup>4</sup> | [2,2] | yes | τ² |
| 12 | 10,080 | 4 | 0 | 4<sup>4</sup> | 4<sup>2</sup> 2<sup>2</sup> 1<sup>4</sup> | [3,1] | yes | — |
| 13 | 21,504 | 5 | 1 | 5<sup>3</sup> 1 | 5<sup>3</sup> 1 | x<sup>4</sup>+x<sup>3</sup>+x<sup>2</sup>+x+1 | no | — |
| 14 | 26,880 | 6 | 2 | 6 3<sup>2</sup> 2 1<sup>2</sup> | 6 3<sup>2</sup> 2 1<sup>2</sup> | q+[2] | no | — |
| 15 | 26,880 | 6 | 1 | 6<sup>2</sup> 3 1 | 6<sup>2</sup> 3 1 | q² | no | — |
| 16 | 13,440 | 6 | 0 | 6<sup>2</sup> 2<sup>2</sup> | 3<sup>4</sup> 1<sup>4</sup> | q+[1,1] | yes | — |
| 17 | 23,040 | 7 | 2 | 7<sup>2</sup> 1<sup>2</sup> | 7<sup>2</sup> 1<sup>2</sup> | c₂+[1] (twin) | no | — |
| 18 | 23,040 | 7 | 2 | 7<sup>2</sup> 1<sup>2</sup> | 7<sup>2</sup> 1<sup>2</sup> | c₁+[1] (twin) | no | — |
| 19 | 20,160 | 8 | 0 | 8<sup>2</sup> | 4<sup>3</sup> 2 1<sup>2</sup> | [4] | yes | τ, τ⁻¹ |
| 20 | 26,880 | 12 | 0 | 12 4 | 6 3<sup>2</sup> 2 1<sup>2</sup> | q+[2] | yes | — |
| 21 | 23,040 | 14 | 0 | 14 2 | 7<sup>2</sup> 1<sup>2</sup> | c₂+[1] (twin) | yes | — |
| 22 | 23,040 | 14 | 0 | 14 2 | 7<sup>2</sup> 1<sup>2</sup> | c₁+[1] (twin) | yes | — |
| 23 | 21,504 | 15 | 1 | 15 1 | 15 1 | x<sup>4</sup>+x+1 (twin) | no | register x<sub>0</sub> ⊕ x<sub>3</sub>, inverse |
| 24 | 21,504 | 15 | 1 | 15 1 | 15 1 | x<sup>4</sup>+x<sup>3</sup>+1 (twin) | no | register x<sub>0</sub> ⊕ x<sub>3</sub> |

### 4.3  Procedure C: place an affine program

1. Write g(x) = Ax + b with b = g(0) and A(x) = g(x) + b, and check that A is linear.
2. Find the linear class of A from its characteristic polynomial and, for repeated factors, the ranks of A + I, (A + I)<sup>2</sup> and (A + I)<sup>3</sup>, or of q(A).
3. Count the fixed words of g; none means a translated interface.
4. Match the cycle types of g and of A in Table A3. For order 7, 14 or 15 the characteristic polynomial picks the twin.

Example. τ<sub>4</sub>(x) = x<sub>1</sub>x<sub>2</sub>x<sub>3</sub>¬x<sub>0</sub> has A = σ<sub>4</sub>, and A + I has ranks 3, 2, 1 for its first three powers: the Jordan block [4]. τ<sub>4</sub> fixes no word and has cycle type 8<sup>2</sup>, and σ<sub>4</sub> has cycle type 4<sup>3</sup> 2 1<sup>2</sup>, so τ<sub>4</sub> is interface 19.

## 5  The center under ring motions

### 5.1  The registers and how a difference is located

At odd LEN n = 2k + 1, Ψ<sub>+</sub> and Ψ<sub>−</sub> are the equal superpositions of the 2<sup>k+1</sup> palindromes of LEN n, with sign +1, or −1 raised to the center bit. Each mirror pair (i, n−1−i) is a Bell pair, and the center is (|0⟩ ± |1⟩)/√2, unentangled (manual, Theorem 8.4). No value reading of the center separates Ψ<sub>+</sub> from Ψ<sub>−</sub>; a NOT reading always does.

A ring motion permutes words and so acts on both registers. The single-site trace distance between the two images locates the difference. A pair of palindromes with opposite centers whose images differ only at site j contributes 2<sup>−k</sup> at site j; pairs with equal centers contribute the same to both registers, and pairs whose images differ at two or more sites contribute to no single site.

**Theorem A5 (motion of the center).**

- (i) Facing and NOT act on both registers as NOT on the center alone: PΨ<sub>±</sub> = CΨ<sub>±</sub> = ±Ψ<sub>±</sub>. Reversal fixes both. **STANDS** (P14.4).
- (ii) The twisted clock keeps the difference on one site and moves it one site per tick. After t ticks the distance is 1 at site k − t (mod n) and 0 elsewhere; after n ticks the difference is back at the center. **STANDS** (P14.5); **RUNS** n = 3–13.
- (iii) For n ≥ 5 the native successor keeps the center's difference on 2<sup>k</sup> − 1 of the 2<sup>k</sup> center pairs. The one pair it disturbs is {1<sup>k</sup>01<sup>k</sup>, 1<sup>n</sup>}: its step crosses the closure of the ring and lands on the difference 1<sup>k</sup>0<sup>k+1</sup>, spread over k sites. The poles 0<sup>n</sup> and 1<sup>n</sup>, which differ everywhere, step to 0<sup>n−1</sup>1 and 0<sup>n</sup>, which differ only at the last site. After one step the center holds 1 − 2<sup>−k</sup>, the last site 2<sup>−k</sup>, and every other site 0. **STANDS** for the split and the poles; the full single-site profile **RUNS** n = 5–13. P14.6, which sealed that the successor erases the difference from every single site, failed.
- (iv) Facing reverses the successor, PTP = T<sup>−1</sup>, so facing and the successor generate a dihedral group. **STANDS** (P14.7); **RUNS** n = 2–12.

**Proof.** (i) On palindromes facing is NOT, and NOT sends w to Cw with the opposite center: Ψ<sub>+</sub> is unchanged and Ψ<sub>−</sub> changes sign. (ii) τ(x) + τ(y) = σ(x + y): the twisted clock rotates the difference between any two words, so pairs one site apart stay one site apart, the site moving by one per tick, and pairs farther apart never close up. (iii) A palindrome that starts with 0 is a representative, and its successor is the next representative, w + 1, which changes only the last bit. A palindrome that starts with 1 is the partner Cr of a representative r, and its successor is the partner of the previous representative, J(r − 1). The borrow in r − 1 stays below the center unless the right half of r is all zeros, that is r ∈ {0<sup>n</sup>, 0<sup>k</sup>10<sup>k</sup>}, whose partners are 1<sup>n</sup> and 1<sup>k</sup>01<sup>k</sup>. The closure step 1<sup>n</sup> → 0<sup>n</sup> and the first step 0<sup>n</sup> → 0<sup>n−1</sup>1 put the poles one site apart, at the last site. (iv) From the address law R[N−1−a] = P(R[a]): PTP(R[a]) = P(R[N−a]) = R[a−1]. ∎

At n = 3 the successor disturbs both center pairs and spreads the difference over all three sites, 1/2 at each (**RUNS**).

### 5.2  Procedure D: follow a difference

1. List the pairs of palindromes with opposite centers.
2. Apply the motion to both words of each pair.
3. A pair whose images differ only at site j adds 2<sup>−k</sup> at site j. The total at each site is the trace distance there.

Example (n = 5). The center pairs are {00000, 00100}, {01010, 01110}, {10001, 10101} and {11011, 11111}. The successor steps the first two to {00001, 00101} and {01011, 01111} and the third to {10110, 10010}, each still apart at the center only. It steps {11011, 11111} to {11000, 00000}, apart at the first two sites. The poles step to 00001 and 00000, apart at the last site. The center holds 3/4 and the last site 1/4.

*Table A4. The native successor on the paired register at odd LEN n = 2k + 1: single-site trace distance after one step (RUNS n = 5–13).*

| n | k | center pairs | kept on the center | center | last site | disturbed pair | its new difference | poles step to |
|---|---|---|---|---|---|---|---|---|
| 5 | 2 | 4 | 3 | 0.7500 | 0.2500 | 1<sup>2</sup>01<sup>2</sup> \| 1<sup>5</sup> | 1<sup>2</sup>0<sup>3</sup> | 0<sup>4</sup>1 \| 0<sup>5</sup> |
| 7 | 3 | 8 | 7 | 0.8750 | 0.1250 | 1<sup>3</sup>01<sup>3</sup> \| 1<sup>7</sup> | 1<sup>3</sup>0<sup>4</sup> | 0<sup>6</sup>1 \| 0<sup>7</sup> |
| 9 | 4 | 16 | 15 | 0.9375 | 0.0625 | 1<sup>4</sup>01<sup>4</sup> \| 1<sup>9</sup> | 1<sup>4</sup>0<sup>5</sup> | 0<sup>8</sup>1 \| 0<sup>9</sup> |
| 11 | 5 | 32 | 31 | 0.9688 | 0.0312 | 1<sup>5</sup>01<sup>5</sup> \| 1<sup>11</sup> | 1<sup>5</sup>0<sup>6</sup> | 0<sup>10</sup>1 \| 0<sup>11</sup> |
| 13 | 6 | 64 | 63 | 0.9844 | 0.0156 | 1<sup>6</sup>01<sup>6</sup> \| 1<sup>13</sup> | 1<sup>6</sup>0<sup>7</sup> | 0<sup>12</sup>1 \| 0<sup>13</sup> |

## 6  Native programs

### 6.1  The criterion

A reversible program f on words of LEN n is its transition table: the 2<sup>n</sup> transitions x|f(x), words of LEN 2n in the §181 model. The program is native when facing P<sub>2n</sub> carries every transition of f onto a transition of f, so that the ring's own reading of the table returns the table.

**Theorem A6 (native programs).** f is native exactly when JfJ = f<sup>−1</sup>, so that reading the program backward runs it backward, and its self-reading states S = {x : f(x) = Jx} are closed under NOT. Equivalently, f = Jg with g an involution whose fixed words are closed under NOT. **STANDS** (P15.1); **RUNS** on all 24 programs at n = 2 and all 40,320 at n = 3.

**Proof.** A transition that reads differently backward is faced by J(fx)|J(x), which is a transition of f exactly when f(Jfx) = Jx. A transition reads the same both ways exactly when f(x) = Jx; it is faced by its NOT, Cx|J(Cx), which is a transition of f exactly when Cx ∈ S. On S the first condition holds by itself. So f is native exactly when fJf = J and S is closed under NOT, and fJf = J is JfJ = f<sup>−1</sup>. With g = Jf the first condition says that g is an involution, and S is its fixed set. ∎

**Corollary (count).** The native programs on LEN n correspond to the involutions of the 2<sup>n</sup> words whose fixed words come in complement pairs. Choosing j fixed pairs among the 2<sup>n−1</sup> complement pairs and pairing the remaining words gives

> Native(n) = Σ over j of (2<sup>n−1</sup> choose j) · (2<sup>n</sup> − 2j − 1)!!

where (2m − 1)!! = (2m − 1)(2m − 3)⋯1 counts the ways to pair 2m words. Native(n) = 2, 6, 188, 3,460,368 and 321,626,829,363,798,272 at n = 1–5. **STANDS**; the values at n = 2 and 3 equal the exhaustive runs.

### 6.2  Chains and the native successor

**Theorem A7 (chains).** NOT, rotation σ and the twisted clock τ commute with NOT and satisfy JgJ = g<sup>−1</sup>. A program built from them, f = g<sub>m</sub>⋯g<sub>1</sub> with g<sub>1</sub> applied first, is native exactly when its instruction word read backward computes the same map, g<sub>1</sub>⋯g<sub>m</sub> = g<sub>m</sub>⋯g<sub>1</sub>. Every palindromic instruction word is native. **STANDS** (P15.3); **RUNS** on all 1,092 words of length up to 6 at n = 3, 4 and 5.

**Proof.** A program that commutes with NOT has a self-reading set closed under NOT, since f(Cx) = Cf(x) = CJx = J(Cx) for x in S. Only JfJ = f<sup>−1</sup> remains. JfJ = (Jg<sub>m</sub>J)⋯(Jg<sub>1</sub>J) = g<sub>m</sub><sup>−1</sup>⋯g<sub>1</sub><sup>−1</sup>, while f<sup>−1</sup> = g<sub>1</sub><sup>−1</sup>⋯g<sub>m</sub><sup>−1</sup>, and the two agree exactly when g<sub>1</sub>⋯g<sub>m</sub> = g<sub>m</sub>⋯g<sub>1</sub>. ∎

**Theorem A8 (the native successor as a program).** For n ≥ 3 facing carries exactly 2<sup>n</sup> − 2 × 2<sup>⌈n/2⌉</sup> transitions of the native successor T onto transitions of T. It fails on the 2 × 2<sup>⌈n/2⌉</sup> − 1 transitions that touch a palindrome, of which only the closure 1<sup>n</sup> → 0<sup>n</sup> joins two, and on the seam transition, the one transition that reads the same both ways. **STANDS** (P15.4); **RUNS** n = 3–12.

**Proof.** Where x and T(x) both read differently backward, facing acts as reversal at both ends, and PTP = T<sup>−1</sup> applied at Jx gives J(Tx) = T<sup>−1</sup>(Jx): the faced transition J(Tx)|Jx is a transition of T. Where x or T(x) is a palindrome, facing acts there as NOT, the same identity lands on a complement, and the faced transition is not a transition of T. T(x) = Jx holds only across the seam, at x = R[m−1] (manual, Theorem 8.3); that transition is faced by its NOT, whose first word is not self-reading, so it fails as well. The palindromes occupy 2 × 2<sup>⌈n/2⌉</sup> transition ends, and the closure transition holds two of them. ∎

### 6.3  Programs on the ring

Table A5 runs eight programs at LEN 3 and 4 and records where each is native for n = 1–12. Seam crossings count the states whose step crosses the ring's seam between addresses m−1 and m. The §181 column counts transitions that facing carries onto transitions of the same program. The offset columns apply to shift programs, whose transitions are contacts of the wheel: the contacts that facing P<sub>n+1</sub> carries onto contacts of the same program, and the contacts that read the same both ways. NOT, rotation and the twisted clock are native at every LEN, and the twisted clock has no self-reading transition in either contact model, since its contacts begin with x<sub>0</sub> and end with ¬x<sub>0</sub>. The increment is native only at LEN 1, where it is NOT; the Gray counter only at LEN 1 and 2; CNOT and the register x<sub>0</sub> ⊕ x<sub>n−1</sub> never.

*Table A5. Programs on the native ring. Cells give LEN 3, LEN 4. Native pattern for n = 1–12, left to right: Y native, · not native, – not reversible at that LEN.*

| program | seam crossings | §181: facing carries | offset: facing carries | palindromic contacts | JfJ = f<sup>−1</sup> (n = 4) | self-reading states (n = 4) | native, n = 1–12 |
|---|---|---|---|---|---|---|---|
| NOT | 4/8, 12/16 | 8/8, 16/16 | — | — | yes | 4 | `YYYYYYYYYYYY` |
| rotation σ | 4/8, 10/16 | 8/8, 16/16 | 8/8, 16/16 | 4/8, 8/16 | yes | 8 | `YYYYYYYYYYYY` |
| twisted clock τ | 6/8, 6/16 | 8/8, 16/16 | 8/8, 16/16 | 0/8, 0/16 | yes | 0 | `YYYYYYYYYYYY` |
| register x<sub>0</sub> ⊕ x<sub>n−1</sub> | 6/8, 10/16 | 2/8, 4/16 | 2/8, 4/16 | 2/8, 4/16 | no | 4 (not closed) | `–···········` |
| increment x + 1 | 4/8, 6/16 | 0/8, 0/16 | — | — | no | 0 | `Y···········` |
| CNOT (lsb → msb) | 2/8, 6/16 | 0/8, 2/16 | — | — | no | 2 (not closed) | `–···········` |
| Gray counter | 4/8, 4/16 | 4/8, 4/16 | — | — | no | 0 | `YY··········` |
| native successor T | 2/8, 2/16 | 0/8, 8/16 | — | — | no | 1 (not closed) | `Y···········` |

### 6.4  Feedback shift programs (predictions16)

A shift program steps x<sub>0</sub>x<sub>1</sub>…x<sub>n−1</sub> to x<sub>1</sub>…x<sub>n−1</sub>g(x). Its transitions are single contacts x·g(x) of the wheel, so it is a program the wheel runs one contact at a time. It is reversible exactly when g(x) = x<sub>0</sub> ⊕ h(v) with v = x<sub>1</sub>…x<sub>n−1</sub>. Rotation (h = 0) and the twisted clock (h = 1) are native at every LEN; the register with feedback x<sub>0</sub> ⊕ x<sub>n−1</sub> is native at none (Table A5). predictions16 sealed which feedback functions are native before the check ran.

**Theorem A9 (native shift programs).**

- (i) The shift program with feedback x<sub>0</sub> ⊕ h(v) is native exactly when h reads the same on every word and its reversal, h(Jv) = h(v), and agrees on each complement pair of palindromes, h(Cv) = h(v) for v ∈ Pal<sub>n−1</sub>. **STANDS**; **RUNS** on every h at n = 2–5 (P16.1).
- (ii) With N = 2<sup>n</sup>, there are 2<sup>N/4</sup> native shift programs at LEN n ≥ 2: one free bit for each reversal pair of words that read differently backward and one for each complement pair of palindromes, 2<sup>n−2</sup> bits in all. That is 2, 4, 16, 256 and 65,536 at n = 2–6. **STANDS**; **RUNS** n = 2–5 (P16.2).
- (iii) An affine feedback h(v) = c·v ⊕ c<sub>0</sub> is native exactly when its tap vector c reads the same both ways and has even weight; there are 2<sup>⌊(n−1)/2⌋+1</sup> such registers. At n = 3 all four native shift programs are affine: rotation, the twisted clock, the parity register x<sub>0</sub> ⊕ x<sub>1</sub> ⊕ x<sub>2</sub> and its NOT. **STANDS**; **RUNS** n = 2–10 (P16.3).
- (iv) Every native linear register (c<sub>0</sub> = 0) fixes 1<sup>n</sup>, so x + 1 divides its characteristic polynomial, and no native linear register runs through all 2<sup>n</sup> − 1 nonzero words: a maximal-length register is never native. The register x<sub>0</sub> ⊕ x<sub>n−1</sub> fails at every n ≥ 2, its tap having no mirror partner for n ≥ 3 and odd weight at n = 2. **STANDS**; **RUNS** over every linear h at n = 2–10 (P16.4).

**Proof.** With f(x) = v·(x<sub>0</sub> ⊕ h(v)), JfJ(y) = (y<sub>n−1</sub> ⊕ h(y<sub>n−2</sub>…y<sub>0</sub>), y<sub>0</sub>, …, y<sub>n−2</sub>) and f<sup>−1</sup>(y) = (y<sub>n−1</sub> ⊕ h(y<sub>0</sub>…y<sub>n−2</sub>), y<sub>0</sub>, …, y<sub>n−2</sub>), so JfJ = f<sup>−1</sup> exactly when h(Jv) = h(v). f(x) = Jx exactly when v reads the same both ways and h(v) = 0, so S = {x<sub>0</sub>v : v ∈ Pal<sub>n−1</sub>, h(v) = 0} with x<sub>0</sub> free, and S is closed under NOT exactly when h(Cv) = h(v) on palindromes. The free values are one per reversal pair of the 2<sup>n−1</sup> − p′ words that read differently backward and one per complement pair of the p′ = 2<sup>⌈(n−1)/2⌉</sup> palindromes, (2<sup>n−1</sup> − p′)/2 + p′/2 = 2<sup>n−2</sup> in all. For affine h, reversal symmetry is symmetry of the taps, and h(Cv) = h(v) + c·1<sup>n−1</sup> requires even weight. A native linear register sends 1<sup>n</sup> to 1<sup>n−1</sup>(1 ⊕ c·1<sup>n−1</sup>) = 1<sup>n</sup>, and a register with a fixed nonzero word cannot run through all nonzero words. ∎

*Table A6. Native feedback shift programs (predictions16). Feedback functions h are counted on the 2<sup>n−1</sup> words v; every h was checked at n = 2–5, and every affine h at n = 2–10.*

| n | feedback functions | native shift programs | native affine registers | maximal-length linear registers (none native) |
|---|---|---|---|---|
| 2 | 4 | 2 | 2 | 1 |
| 3 | 16 | 4 | 4 | 2 |
| 4 | 256 | 16 | 4 | 2 |
| 5 | 65,536 | 256 | 8 | 6 |
| 6 | 2<sup>32</sup> | 65,536 | 8 | 6 |
| 7 | 2<sup>64</sup> | 2<sup>32</sup> | 16 | 18 |
| 8 | 2<sup>128</sup> | 2<sup>64</sup> | 16 | 16 |
| 9 | 2<sup>256</sup> | 2<sup>128</sup> | 32 | 48 |
| 10 | 2<sup>512</sup> | 2<sup>256</sup> | 32 | 60 |

### 6.5  Procedure E: test a program

1. Compute the self-reading states S = {x : f(x) = Jx}.
2. Check that S is closed under NOT.
3. Check that J(f(J(f(x)))) = x for every x, which is JfJ = f<sup>−1</sup>.
4. The program is native exactly when both checks pass. For a chain of NOT, σ and τ, step 2 always passes and step 3 is the instruction word read backward. For a shift program, check h(Jv) = h(v) for every v and h(Cv) = h(v) for every palindrome v.

Example. At LEN 3 the parity register x ↦ x<sub>1</sub>x<sub>2</sub>(x<sub>0</sub> ⊕ x<sub>1</sub> ⊕ x<sub>2</sub>) has h(v) = v<sub>0</sub> ⊕ v<sub>1</sub>: symmetric taps of even weight, so it is native. The register x<sub>0</sub> ⊕ x<sub>2</sub> has h(v) = v<sub>1</sub>, a tap with no mirror partner, so reading it backward does not run it backward.

## 7  The twisted clock one LEN up

Each step x → f(x) of a shift program has two places on the rings: the state x in R<sub>n</sub>, and the contact x·g(x) in R<sub>n+1</sub>. The contact is a word of LEN n+1, so its address in R<sub>n+1</sub> is its LEN address one level up by definition. The content is whether the program reproduces itself one level up.

**Theorem A10 (the twisted clock reproduces itself).** Write ĉ(x) = x·¬x<sub>0</sub> for the contact of the twisted clock at x.

- (i) ĉ(τ<sub>n</sub>x) = τ<sub>n+1</sub>(ĉ(x)) exactly when x<sub>0</sub> = x<sub>1</sub>. **STANDS**; **RUNS** n = 2–12.
- (ii) The contacts of the principal cycle of τ<sub>n</sub>, the orbit of 0<sup>n</sup>, are the principal cycle of τ<sub>n+1</sub> with the poles 0<sup>n+1</sup> and 1<sup>n+1</sup> removed, in order. At the two steps of the principal cycle where x<sub>0</sub> ≠ x<sub>1</sub>, τ<sub>n+1</sub> passes through a pole that the contacts step over. **STANDS** (P15.5).
- (iii) Every other orbit of τ<sub>n</sub> has steps with x<sub>0</sub> ≠ x<sub>1</sub>, and at each of them τ<sub>n+1</sub> leaves through a word that is not a pole: the copy holds on the principal cycle only. **STANDS**; **RUNS** n = 2–12.
- (iv) In R<sub>n+1</sub> the principal-cycle contacts sit at strictly increasing addresses for n ≥ 3, in mirror pairs a<sub>i</sub> + a<sub>2n−1−i</sub> = 2<sup>n+1</sup> − 1; at n = 2 the seam reverses one step. **STANDS**; **RUNS** n = 2–12.

**Proof.** τ<sub>n+1</sub>(ĉ(x)) = x<sub>1</sub>…x<sub>n−1</sub>¬x<sub>0</sub>¬x<sub>0</sub> and ĉ(τ<sub>n</sub>x) = x<sub>1</sub>…x<sub>n−1</sub>¬x<sub>0</sub>¬x<sub>1</sub>, equal exactly when x<sub>0</sub> = x<sub>1</sub>. The principal cycle of τ<sub>n</sub> runs through 0<sup>n−j</sup>1<sup>j</sup> and then 1<sup>n−j</sup>0<sup>j</sup>; its contacts are 0<sup>n−j</sup>1<sup>j+1</sup> and 1<sup>n−j</sup>0<sup>j+1</sup> for j = 0, …, n−1, the principal cycle of τ<sub>n+1</sub> without its poles. τ<sub>n+1</sub>(ĉ(x)) is a pole only when x<sub>1</sub>…x<sub>n−1</sub>¬x<sub>0</sub> is constant, that is at x = 01<sup>n−1</sup> or 10<sup>n−1</sup>, both on the principal cycle. An orbit with x<sub>0</sub> = x<sub>1</sub> at every step would be constant along a tape on which every bit is followed n steps later by its NOT, which is impossible. The contacts 0<sup>n−j</sup>1<sup>j+1</sup> begin with 0 and end with 1, so they are representatives, increasing in value and therefore in address; the contacts 1<sup>n−j</sup>0<sup>j+1</sup> are their reversals, at the mirrored addresses. At n = 2 the last representative of R<sub>3</sub>, 011, is itself a principal-cycle contact, and the seam places it after its partner 110. ∎

*Table A7. The principal cycle of the twisted clock at LEN n: addresses of its states in R<sub>n</sub> and of its contacts in R<sub>n+1</sub>.*

| n | principal cycle of τ<sub>n</sub> | state addresses in R<sub>n</sub> | contact addresses in R<sub>n+1</sub> |
|---|---|---|---|
| 2 | 00 01 11 10 | 0, 2, 3, 1 | 1, 4, 3, 6 |
| 3 | 000 001 011 111 110 100 | 0, 1, 4, 7, 3, 6 | 1, 3, 6, 9, 12, 14 |
| 4 | 0000 0001 0011 0111 1111 1110 1100 1000 | 0, 1, 3, 6, 15, 9, 12, 14 | 1, 3, 7, 13, 18, 24, 28, 30 |
| 5 | 00000 00001 00011 00111 01111 11111 11110 11100 11000 10000 | 0, 1, 3, 7, 13, 31, 18, 24, 28, 30 | 1, 3, 7, 14, 25, 38, 49, 56, 60, 62 |

## 8  The reading direction as one address bit

A word that reads differently backward has two readings, x and Jx, and they are different numbers: one of them is the larger. The comparator c(x) = sgn(Jx − x) records which, +1 when the word reads smaller than its reversal and −1 when it reads larger. The outermost mirror pair that disagrees decides it: 01 gives +1 and 10 gives −1. A palindrome has one reading, and c(x) = 0. The native ring stores this single distinction as one address bit.

**Theorem A11 (the reading direction is the top address bit).**

- (i) For n ≥ 2 the top address bit of a word that reads differently backward is 1 exactly when the word reads larger than its reversal, except for the seam pair {r⋆, J(r⋆)}, whose two words exchange places. The top address bit of a palindrome is its first bit, the bit that NOT changes. **STANDS**; **RUNS** n = 2–20 on every word (P17.1).
- (ii) Read along the ring, the comparator g(a) = c(R<sub>n</sub>[a]) has Walsh coefficient (N − p − 4)/N on the top address bit and total energy (N − p)/N, with N = 2<sup>n</sup> and p = 2<sup>⌈n/2⌉</sup>. The top bit therefore carries the share (N − p − 4)<sup>2</sup>/(N(N − p)) of its spectral energy: 1/2 at n = 2, exactly 0 at n = 3, where the seam exchange balances the two halves, 0.961 at n = 10 and 0.99902 at n = 20. The rest belongs to the palindromes, which have no reading direction, and to the seam pair. **STANDS**; **RUNS** n = 2–20 (P17.2).
- (iii) The first two rings are the two primitive readings. R<sub>1</sub> = 1|0 places each bit at the address of its NOT. R<sub>2</sub> = 00|10|01|11 places each word at the address of its reversal, R<sub>2</sub>[a] = J<sub>2</sub>(a), so its top address bit is the bit read last. From LEN 3 on the ring is neither. **STANDS**; **RUNS** n = 3–12 (P17.3; its clause R<sub>1</sub> = J<sub>1</sub> failed as sealed).
- (iv) With the step signs s<sub>i</sub>(x) = x<sub>i+1</sub> − x<sub>i</sub>, facing a word that reads differently backward reads its steps backward and negates them: s<sub>i</sub>(Px) = −s<sub>n−2−i</sub>(x). Facing a palindrome negates its steps in place: s<sub>i</sub>(Px) = −s<sub>i</sub>(x) = s<sub>n−2−i</sub>(x). The reflected identity therefore fails on exactly the 2<sup>⌈n/2⌉</sup> − 2 non-constant palindromes. **STANDS**; **RUNS** n = 2–14 (P17.4).

**Proof.** (i) The ring places the representative of each pair, the member that reads smaller or, for a palindrome, starts with 0, below address m − 1 and its partner at the mirrored address above m, and it exchanges only the last pair across the seam (manual, Section 3.5 and Theorem 8.3). r⋆ never reads the same both ways, since its mirror positions ⌊n/2⌋ − 1 and ⌈n/2⌉ hold 0 and 1. (ii) In the lower half every word that reads differently backward contributes +1 except J(r⋆), and in the upper half −1 except r⋆, so the top-bit sum is 2(m − p/2 − 2) = N − p − 4, while c² sums to N − p. (iii) At LEN 1 and 2 the last pair is the only pair that the seam can exchange: {0, 1} gives R<sub>1</sub> = 1|0, and {01, 10} puts 10 at address 1 and 01 at address 2. (iv) For P = J, s<sub>i</sub>(Jx) = x<sub>n−2−i</sub> − x<sub>n−1−i</sub> = −s<sub>n−2−i</sub>(x). For P = C every step changes sign in place, and on a palindrome s<sub>n−2−i</sub>(x) = −s<sub>i</sub>(x). ∎

At LEN 1 the seam exchange takes the only pair, so R<sub>1</sub> = 1|0 and the palindrome clause of P17.1 fails there, as does the clause R<sub>1</sub> = J<sub>1</sub> of P17.3; both failed as sealed. The LEN-1 ring is NOT itself, the single distinction: its first address holds 1 and its second holds 0. Every word of every longer ring carries its reading as one address bit, and every offset adds one address bit (manual, Section 7).

*Table A8. Share of the comparator’s spectral energy on the top address bit of R<sub>n</sub> (formula, equal to the run at every n = 2–20).*

| n | N | p | top-bit coefficient (N − p − 4)/N | share (N − p − 4)<sup>2</sup>/(N(N − p)) |
|---|---|---|---|---|
| 2 | 4 | 2 | -2/4 | 0.50000 |
| 3 | 8 | 4 | 0/8 | 0.00000 |
| 4 | 16 | 4 | 8/16 | 0.33333 |
| 5 | 32 | 8 | 20/32 | 0.52083 |
| 6 | 64 | 8 | 52/64 | 0.75446 |
| 8 | 256 | 16 | 236/256 | 0.90651 |
| 10 | 1,024 | 32 | 988/1,024 | 0.96095 |
| 12 | 4,096 | 64 | 4,028/4,096 | 0.98242 |
| 16 | 65,536 | 256 | 65,276/65,536 | 0.99597 |
| 20 | 1,048,576 | 1,024 | 1,047,548/1,048,576 | 0.99902 |

## 9  The reader at the center

At odd LEN the center is fixed by reversal and lies outside the selector (manual, Theorems 5.3 and 8.1). Facing therefore acts on it as a NOT controlled by the rest of the word. The reader is the center itself: nothing has to be attached to the ring to read it.

**Theorem A12 (the center reader).** At odd n = 2k + 1, facing is reversal followed by a NOT of every bit controlled by the selector, P<sub>n</sub> = C<sup>s</sup> J<sub>n</sub> with s = s<sub>n</sub>(w). On the center only the controlled NOT acts:

> b′ = b ⊕ s<sub>n</sub>(w)

The control is the conjunction of the k mirror-pair agreements, a k-controlled NOT of algebraic degree k: one control at LEN 3, where facing is affine; two at LEN 5, a Toffoli gate on agreement bits; k at LEN 2k + 1. The center flips on exactly the 2<sup>k+1</sup> palindromes, a share 2<sup>−k</sup>, and keeps its value on every other word. At LEN 1 the control is empty and the center always flips. **STANDS**; **RUNS** n = 1, 3, …, 15 on every word (P18.1).

**Proof.** The selector is a product over mirror pairs, contains no center variable, and is invariant under reversal, so J(w) ⊕ s<sub>n</sub>(w)·1<sup>n</sup> is the NOT of J(w) exactly when s<sub>n</sub>(w) = 1. Reversal fixes position k. ∎

**Theorem A13 (what the center's response forces on states).** Give a state of the center weights on its two values, read by value through a rule |weight|<sup>p</sup>. Ask for equal value weights, as on the palindromes (manual, Theorem 8.1), together with a definite response to facing: NOT carries the state to a multiple of itself.

- (i) With nonnegative weights there is exactly one such state, (1/2, 1/2), and its response is +1. The response carries nothing.
- (ii) With signed weights there are exactly two, (1, ±1) normalized, with responses +1 and −1: one bit that no value reading sees. They are the centers of Ψ<sub>+</sub> and Ψ<sub>−</sub>.
- (iii) If the value reading and the response reading are readings of one state by the same rule, each normalized, then p = 2: the state with a definite value carries total weight 2<sup>2−p</sup> in the response reading.

**STANDS** (P18.2). **Proof.** NOT exchanges the two weights, so (a<sub>1</sub>, a<sub>0</sub>) = r(a<sub>0</sub>, a<sub>1</sub>) and r = ±1; nonnegative equal weights allow only r = +1. In the response reading the state (1, 0) expands on (1, ±1)/2<sup>1/p</sup> with both coefficients 2<sup>1/p</sup>/2, whose weights sum to 2<sup>2−p</sup>. ∎ The center law forces signed amplitudes read by their squares. It does not by itself force complex phases.

**Theorem A14 (the clock forces phases at even LEN).** The twisted clock satisfies τ<sub>n</sub><sup>n</sup> = C<sub>n</sub>. On states that respond to NOT with −1, every definite response λ of τ<sub>n</sub> satisfies λ<sup>n</sup> = −1. At even n none is real. At LEN 2 the twisted clock is a square root of NOT, τ<sub>2</sub>² = C<sub>2</sub>, and its definite responses on those states are ±i. At odd n the real response −1 occurs on every orbit, and non-real responses join it from n = 3. **STANDS**; **RUNS** n = 1–12 by orbit count and n = 1–8 by numerical spectra (P18.3).

**Proof.** Every orbit of τ<sub>n</sub> has a length o that divides 2n but not n, so its definite responses are the o-th roots of unity ω, and C = τ<sup>n</sup> responds with ω<sup>n</sup>. Responding to NOT with −1 means ω<sup>n</sup> = −1. A real ω is ±1: ω = 1 gives +1, and ω = −1 gives (−1)<sup>n</sup>, which is −1 exactly at odd n, where every orbit length is even. ∎ One bit cannot hold a square root of NOT with real weights, since its determinant would square to −1. The ring holds one on two bits as the permutation τ<sub>2</sub>, and its definite responses there are the phases ±i.

**Theorem A15 (the center reads the outside as a sign).** Prepare the center with response −1, (|0⟩ − |1⟩)/√2. Facing leaves the center unchanged and writes the selector on the rest of the word as a sign: |o⟩|−⟩ ↦ (−1)<sup>s</sup>|o′⟩|−⟩, with s = s<sub>n</sub>(o) and o′ the faced outside. With response +1, (|0⟩ + |1⟩)/√2, no sign is written. **STANDS**; **RUNS** on random outside states at n = 3, 5, 7 (P18.4). **Proof.** The controlled NOT sends |0⟩ − |1⟩ to |s⟩ − |1 ⊕ s⟩ = (−1)<sup>s</sup>(|0⟩ − |1⟩). ∎

Read together, the center has three readings. By value it is a probability, (1/2, 1/2). By its response to facing it is a sign, ±1, and holding the sign forces signed amplitudes read by their squares. By its response to the ring's clock at even LEN it is a phase, ±i at LEN 2. The paired register's center, (|0⟩ + |1⟩)/√2, is the reader in its silent state: facing writes nothing into it. The opposite center, (|0⟩ − |1⟩)/√2, writes the reflection symmetry of the word around it as a sign.

Comparators. The square rule is the Born rule. Among p-norm rules only p = 1 and p = 2 admit norm-preserving linear maps beyond signed permutations [12], and Theorem A13(iii) is that selection made by the center's two readings. Real-number and complex quantum theory make different predictions in network experiments [13], so the phases of Theorem A14 carry testable content. Writing a controlled operation's condition as a sign on the control register is phase kickback, the mechanism of oracle-based quantum algorithms [14].

## 10  Technical notes

> **Technical Note A1. Sources of the external results**
>
> Three notebooks and a draft addendum from an external AI session were supplied by the author on 5 November 2026. They contributed the reversal formulas of Theorem A1 and the facing defect of Theorem A2, computed with spanning-tree cycle bases; the circular-seam classification and the fixed-necklace formula of Theorem A3, obtained with the orbit-counting lemma on the group generated by τ<sub>s</sub> and J<sub>s</sub>; the program survey behind Table A5; and the two-address observation behind Theorem A10.
>
> The draft's tables agree with this addendum wherever they overlap. Each result was re-derived here by a different route (stacked F<sub>2</sub> ranks, the complement-pair argument, the native-program criterion, the copy law), and every table was re-run from one script.

> **Technical Note A2. Corrections to the external record**
>
> 1. A mid-run assertion t<sub>P</sub> = p + [n even] was wrong; the notebook dropped it, and its final formulas are those of Theorem A2.
>
> 2. The AGL(4,2) separation claim was stated before any run. P14.3 sealed it, and the run checks it.
>
> 3. The fixed-necklace formula passed through an intermediate version that failed after L = 5. The notebook replaced it, and Theorem A3(iv) proves the replacement by a different route.
>
> 4. The program survey's seam-crossing cell for the register x<sub>0</sub> ⊕ x<sub>n−1</sub> (8/16 on R<sub>4</sub>) was never computed. The value is 10/16, and 6/8 on R<sub>3</sub>.
>
> 5. The two-address law equated a contact's reading address with its LEN address one level up. That holds by definition. The content is the twisted clock's self-reproduction, which holds on the principal cycle only (Theorem A10).
>
> 6. The draft addendum derived the last site's share 2<sup>−k</sup> from the disturbed pair. That pair's new difference 1<sup>k</sup>0<sup>k+1</sup> spreads over k sites and adds nothing at any single site; the share comes from the poles (Theorem A5(iii)).
>
> 7. The draft's scope line credits every claim to spanning-tree bases and stacked ranks; that describes its first section only.
>
> 8. The draft omits predictions15. Sections 6 and 7 hold it.

> **Technical Note A3. P14.6 as sealed and as run**
>
> Sealed: the native successor removes the difference from every single site at odd n ≥ 5, so that after one step no single-site reduced state distinguishes Ψ<sub>+</sub> from Ψ<sub>−</sub> while the two registers stay orthogonal.
>
> Run: the center keeps 1 − 2<sup>−k</sup> and the last site receives 2<sup>−k</sup>. The successor moves palindromes in two families, to the next representative and to the reversal of the previous one, and only the closure breaks the pattern (Theorem A5(iii)). The prediction failed as sealed and stays in the record as sealed.

> **Technical Note A4. The single-distinction transcript**
>
> A further external transcript, supplied by the author on 5 November 2026, proposed that the rings begin with a single distinction that collapses to one bit and expands by one bit per offset, that the comparator collapses onto the top address bit with 99.9% of its spectral energy, and that facing satisfies s<sub>i</sub>(Px) = −s<sub>n−2−i</sub>(x) unconditionally. The collapse is Theorem A11(i)–(ii): exact, a consequence of how the ring is built, and 0.99902 at n = 20, while at n = 3 the share is 0. The one-bit step per offset is the manual's Section 7. The sign identity holds on words that read differently backward and fails on every non-constant palindrome (Theorem A11(iv)).
>
> The transcript also states that the reversible instruction set closes at width 3. At LEN 2 every reversible program is affine (AGL(2,2) contains all 24 permutations of the four words; manual, Table 7), and composition never leaves the affine programs, so a universal set needs a gate of width at least 3. That width 3 suffices, with Toffoli's gate, NOT and CNOT and ancilla bits, is ELSEWHERE [11]. Its readout of light and matter is not derived in this record.

> **Technical Note A5. The center-reader message**
>
> A further external AI message, supplied by the author on 5 November 2026, withdrew a CNOT reader it had attached to the ring, stated the center law b′ = b ⊕ s<sub>n</sub>(w), checked it at odd LEN 1–11, and named the next distinction: whether the reader law forces quantum amplitudes rather than binary responses. The law follows from the definitions (manual, Theorems 5.3 and 8.1), so its exhaustive check cannot fail; Theorem A12 gives its circuit form. Theorems A13–A15 answer the named distinction: the center's response to facing forces signs and the square rule, and the ring's clock forces phases at even LEN.

## 11  Ledger

- **A1** closed routes under reversal: **STANDS**; **RUNS** n = 1–10.
- **A2** closed routes under facing: the closure criterion and the disjoint four-face defects **STAND**; the dimensions **STAND** given the connectivity, which **RUNS** n = 1–18; the ranks **RUN** n = 1–10.
- **A3** circular routes: **STANDS**; the fixed necklaces **RUN** L = 1–18 against brute force.
- **A4** the LEN-4 catalog: P14.1 **RUNS**, landed exactly as derived; P14.2 **STANDS** for the twin pairing and **RUNS** for the nineteen self-inverse interfaces; P14.3 **RUNS**. The ring's motions occupy seven interfaces besides the identity, and facing leaves the affine catalog at LEN 4.
- **A5** the center: P14.4 and P14.5 **STAND**; P14.6 failed as sealed, and the retention 1 − 2<sup>−k</sup> with the pole share 2<sup>−k</sup> **STANDS** for the split and **RUNS** n = 5–13 for the profile; P14.7 **STANDS**. At n = 3, 1/2 on every site, **RUNS**.
- **A6** native programs: P15.1 **STANDS**, **RUNS** n = 2–3; the count Native(n) **STANDS**.
- **A7** chains: P15.3 **STANDS**, **RUNS** n = 3–5.
- **A8** the successor as a program: P15.4 **STANDS**, **RUNS** n = 3–12.
- **A9** native shift programs: P16.1–P16.4 **STAND**; **RUNS** on every h at n = 2–5 and every affine h at n = 2–10. Every sealed claim landed.
- **A10** the twisted clock one LEN up: P15.5 **STANDS**; the copy holds exactly where x<sub>0</sub> = x<sub>1</sub>; **RUNS** n = 2–12.
- **A11** the reading direction: P17.1, P17.2 and P17.4 **STAND**, **RUN** n = 2–20 and n = 2–14; P17.3 **STANDS** at LEN 2 and **RUNS** n = 3–12. The LEN-1 clauses of P17.1 and P17.3 failed as sealed: R<sub>1</sub> = 1|0 = C<sub>1</sub>.
- **A12–A15** the reader at the center: P18.1 **STANDS**, **RUNS** n = 1–15 (facing at odd LEN is a k-controlled NOT on the center); P18.2 **STANDS** (one center state with nonnegative weights, two with signs, p = 2 from one reading rule); P18.3 **STANDS**, **RUNS** n = 1–12 (non-real clock responses at every even LEN, ±i at LEN 2; −1 real on every orbit at odd LEN); P18.4 **STANDS**, **RUNS** n = 3, 5, 7 (the sign reading). Every claim of predictions18 landed.
- Program survey (P15.2): **RUNS** n = 1–12 (Table A5).

## 12  How it continues

1. **Follow the collective selector upward** (manual, item 14.2). Map how the selectors of k composed contacts combine and where the collective seams sit at each LEN. **OPEN**.
2. **The boundary-driven compiler** (manual, item 14.6). Implement bind, compose and close as verbs on contacts. Theorems A6 and A7 give compose a test: a composed program is native exactly when reading it backward runs it backward and its self-reading states are closed under NOT, and for programs built from NOT, σ and τ that is the instruction word read backward. **PULL**.
3. **Native shift programs as the wheel's instruction set.** The 2<sup>N/4</sup> native shift programs at LEN n are the programs the wheel runs one contact at a time and the ring reads back unchanged. Next test: which of them reproduce themselves one LEN up, as the twisted clock does (Theorem A10). **PULL**.
4. **Sign and phase at the center.** Facing writes a sign through the center (Theorem A15) and the clock writes a phase at even LEN (Theorem A14). Next test: alternate the two readings on the paired register and map which center states they reach. **PULL**.
5. **Binary against ternary at horizons** (manual, item 14.5). Unchanged: one remnant with the 220 tone resolved to well under 1%, or a population with spread spins, decides between 4 ln 2 and 4 ln 3. **OPEN**.

## Appendix A  Seals

Each file was hashed with SHA-256 before the computation it predicts was run. The hash of the exact text below must match.

**predictions14**, sealed 5 November 2026, 09:30:10 UTC.

```
SHA-256  50d1278b635d33a8611820dec32ebc0bdce090c593c5b90e07da0264d8242961
```

```
predictions14: the LEN-4 interface catalog and the motion of the center
Sealed 2026-11-05, before running any LEN-4 catalog or center-motion computation.

Contract-side derivation for P14.1-P14.3
Two affine maps x -> A x + b on LEN-4 words are the same interface when they are conjugate in
AGL(4,2). Conjugating by a translation moves b by the image of A + I, so the interfaces with
linear part A are the orbits of the centralizer of A acting on the cokernel of A + I.
GL(4,2) has 14 classes: unipotent [1111], [211], [22], [31], [4]; q+[11] and q+[2] with
q = x^2+x+1; q+q; q^2; c+[1] for each of the two cubics; the three irreducible quartics.
Orbit counts, in that order: 2, 3, 2, 3, 2; 2, 2; 1; 1; 2, 2; 1, 1, 1.

P14.1  AGL(4,2) (322,560 maps) has 25 interfaces.
P14.2  19 interfaces contain their own inverse. The other 6 form 3 mirror-twin pairs: the two
       order-15 Singer interfaces, and two pairs whose linear part has order 7 (c+[1] with a
       fixed point, and without one).
P14.3  The motion signature (cycle type of g on the 16 words, cycle type of its contact-difference
       map Dg(t) = g(x+t) + g(x) = A t) separates all 25 interfaces except the 3 mirror-twin
       pairs: exactly 22 distinct signatures. Vertex cycle type alone separates fewer.

Center motion. Odd LEN n = 2k+1. Psi+ and Psi- are the equal superposition of all palindromes of
LEN n with sign (+1 or -1)^(center bit): every mirror pair a Bell pair, the center in
(|0> + |1>)/sqrt2 or (|0> - |1>)/sqrt2. Ring motions act as permutations of words.

P14.4  Facing P_n and NOT C_n act on Psi+- as NOT on the center alone: Psi+ and Psi- are their
       eigenstates with eigenvalues +1 and -1. Reversal J_n fixes both.
P14.5  The twisted clock tau_n keeps the difference on a single site and moves it one site per tick
       (site k - t mod n after t ticks); every other site reads 0 under NOT. After n ticks it is
       back at the center.
P14.6  The native successor T_n removes the difference from every single site for odd n >= 5:
       after one step no single-site reduced state distinguishes Psi+ from Psi-. The two
       registers stay orthogonal.
P14.7  Facing reverses the successor: P T P = T^-1 on every native ring (from the address law).
```

**predictions15**, sealed 5 November 2026, 09:40:40 UTC.

```
SHA-256  970fcf5e5a44d74513a09cd46d2a41605a79cfe466dd64e14eb5b0dc6fd3dd6f
```

```
predictions15: which programs are native to the ring, and the twisted clock one LEN up
Sealed 2026-11-05, before running any check on the external program notebook.

Contract-side derivation for P15.1
A reversible program f on n-bit words is a set of transitions x|f(x) (the §181 table). Facing a
transition that does not read the same both ways gives J(f x)|J(x); it is again a transition of f
iff f(J(f(x))) = J(x). A transition reads the same both ways iff f(x) = J(x); its partner
C(x)|C(J x) is a transition of f iff C(x) is also such a point. On a self-reading point
f J f x = f x = J x holds automatically, so the first condition holds everywhere.

P15.1  Facing carries the transition table of a reversible program f onto itself iff J f J = f^-1
       (reading the program backward runs it backward) and the self-reading set
       {x : f(x) = J(x)} is closed under NOT. Equivalently f = J g with g an involution whose
       fixed points are closed under NOT. Exhaustive at n = 2 (all 24 programs) and
       n = 3 (all 40,320).
P15.2  NOT C_n, rotation sigma_n and the twisted clock tau_n satisfy P15.1 at every n; tau_n has no
       self-reading transition in either contact model. The increment x+1 fails at every n >= 2,
       CNOT (lsb -> msb) fails at every n >= 2, the Gray counter is native at n = 2 and fails at
       n = 3-10.
P15.3  Chains. Every program built from NOT, rotation and the twisted clock commutes with NOT, so it
       is native iff J f J = f^-1, that is iff its instruction word read backward computes the same
       map. Every palindromic instruction word is native. Exhaustive over all words of length
       <= 6 at n = 3, 4, 5.
P15.4  The native successor T is reversed by facing (P T P = T^-1) but not by reversal: facing
       carries exactly 2^n - 2*2^ceil(n/2) of its transitions onto transitions of T, all except
       the edges touching a palindrome and the seam edge (n = 3-12).
P15.5  The contacts of tau_n's principal cycle (from 0^n) are tau_{n+1}'s principal cycle with the
       poles 0^{n+1} and 1^{n+1} removed, in order. Their addresses in R_{n+1} increase strictly for
       n >= 3 and are mirror-symmetric (a[k] + a[2n-1-k] = 2^{n+1} - 1); at n = 2 the seam reverses
       one step. Every other orbit of tau_n leaves tau_{n+1} at its alternation steps through a word
       that is not a pole: the copy law holds on the principal cycle only (n = 3-12).
```

**predictions16**, sealed 5 November 2026, 10:07:13 UTC.

```
SHA-256  259b0d3693ed968fbbc6b4f12db0cf2e46139819e8e9bd114d1d26a19616db58
```

```
predictions16: which feedback shift programs are native to the ring
Sealed 2026-11-05, before running any check on feedback shift programs beyond Table A5.

Contract-side derivation
A shift program steps x0 x1 ... x(n-1) -> x1 ... x(n-1) g(x). It is reversible iff
g(x) = x0 + h(v) over F2 with v = x1 ... x(n-1), a word of LEN n-1. By P15.1 it is native iff
J f J = f^-1 and its self-reading set S = {x : f(x) = J x} is closed under NOT.
J f J (y) = (y(n-1) + h(y(n-2) ... y0), y0, ..., y(n-2)) and f^-1(y) = (y(n-1) + h(y0 ... y(n-2)), y0, ..., y(n-2)),
so J f J = f^-1 iff h(J v) = h(v) for every v.
f(x) = J x iff v reads the same both ways and h(v) = 0, so S = {x0 v : v in Pal(n-1), h(v) = 0} with x0 free,
and S is closed under NOT iff h(C v) = h(v) for every palindrome v of LEN n-1.

P16.1  A reversible shift program x -> x1 ... x(n-1) (x0 + h(x1 ... x(n-1))) is native iff h reads the same
       on every word and its reversal, h(J v) = h(v), and takes equal values on each complement pair of
       palindromes, h(C v) = h(v) for v in Pal(n-1). Exhaustive over every h at n = 2-5.
P16.2  Native shift programs number 2^(2^(n-2)) at LEN n >= 2: one free bit per reversal pair of
       non-palindromes and one per complement pair of palindromes, 2^(n-2) bits in all.
       2, 4, 16, 256 at n = 2-5. At n = 1 the two programs (identity and NOT) are both native.
P16.3  Affine feedback h(v) = c.v + c0: native iff the tap vector c reads the same both ways and has even
       weight (c0 free). There are 2^(floor((n-1)/2) + 1) of them. At n = 3 all four native shift
       programs are affine: rotation (h = 0), twisted clock (h = 1), and the parity registers
       g = x0 + x1 + x2 and g = x0 + x1 + x2 + 1.
P16.4  Every native linear feedback register (c0 = 0) fixes 1^n, so x + 1 divides its characteristic
       polynomial and no native linear register runs through all 2^n - 1 nonzero words (n >= 2).
       The register with feedback x0 + x(n-1) is native at no n >= 2: its tap is not reversal-symmetric
       for n >= 3 and has odd weight at n = 2. Checked over every linear h at n = 2-10.
```

**predictions17**, sealed 5 November 2026, 10:17:51 UTC.

```
SHA-256  fe74e0473c69148dbb59f71c5a8481ff32abad815386ae1501314fcf2ba68515
```

```
predictions17: the reading direction as one address bit of the native ring
Sealed 2026-11-05, before running any check of these claims.

Contract-side derivation
R_n puts the representative r_a (the smaller word of each facing pair) at address a < m-1 and its partner
P(r_a) opposite, at N-1-a; the last representative r* = 1^(floor(n/2)-1) 0 1^ceil(n/2) and its partner J(r*)
exchange places across the seam (addresses m-1 and m). For a word that reads differently backward the
representative is the one that reads smaller than its reversal; for a palindrome it is the one starting with 0.
The comparator c(x) = sgn(Jx - x) is +1 on representatives that read differently backward, -1 on their partners,
0 on palindromes. Read along the ring, g(a) = c(R_n[a]); the top-bit Walsh coefficient is
(1/N) sum_a g(a) (-1)^(top bit of a) = 2(m - p/2 - 2)/N = (N - p - 4)/N, and sum_a g(a)^2 / N = (N - p)/N.

P17.1  For every n >= 2: the top address bit of a word that reads differently backward is 1 exactly when the
       word reads larger than its reversal, except the seam pair {r*, J(r*)}, where it is the opposite. The top
       address bit of a palindrome is its first bit. (n = 1-20, every word.)
P17.2  The top address bit carries the share (N - p - 4)^2 / (N (N - p)) of the comparator's Walsh energy on R_n,
       N = 2^n, p = 2^ceil(n/2): 1/2 at n = 2, exactly 0 at n = 3 (the seam exchange balances the halves),
       1/3 at n = 4, 0.99902 at n = 20, tending to 1. (n = 2-20.)
P17.3  R_2[a] = J_2(a): the LEN-2 ring lists every word at the address of its reversal, so its top address bit
       is the bit read last and its low address bit the bit read first. R_1 = J_1 trivially; at every n = 3-12
       some address has R_n[a] != J_n(a).
P17.4  Step signs s_i(x) = x(i+1) - x(i), i = 0..n-2. For a word that reads differently backward,
       s_i(P x) = -s_(n-2-i)(x): the steps are read backward and negated. For a palindrome,
       s_i(P x) = -s_i(x) = s_(n-2-i)(x): negated in place. The identity s_i(P x) = -s_(n-2-i)(x) fails exactly on
       the 2^ceil(n/2) - 2 non-constant palindromes. (n = 2-14, every word.)
```

**predictions18**, sealed 5 November 2026, 10:28:52 UTC.

```
SHA-256  e7d9a2870d83031febe8fa2480be4590bee90b40f4743e680ed699839faa7b63
```

```
predictions18: the reader at the center, and what its response forces on states
Sealed 2026-11-05, before running any check of these claims.

Contract-side derivation
At odd LEN n = 2k+1, P_n(w) = J_n(w) + s_n(w) 1^n. The selector s_n is the product of the k mirror-pair agreements
(1 + w_i + w_(n-1-i)), it contains no center variable, and it is invariant under J. So P_n = C^(s_n) J_n: reversal,
then a NOT of every bit controlled by s_n. J fixes position k, so on the center only the controlled NOT acts.
A state of the center that is carried to a multiple of itself by NOT (a definite response) with equal value weights:
NOT swaps the two weights, (a1, a0) = r (a0, a1), so r = +1 or -1. Nonnegative weights allow only r = +1.
Reading by values with rule |a|^p, and reading by NOT-responses with the same rule on the expansion in the
p-normalized response states (1, +-1)/2^(1/p): the definite-value state (1, 0) has response weights 2^(1/p)/2 each,
total 2^(2-p), which is 1 only at p = 2.
The twisted clock: tau_n^n = C_n, and each orbit length o divides 2n but not n.

P18.1  At odd n = 2k+1, P_n = C^(s_n) J_n and the center obeys b' = b + s_n(w), with s_n a conjunction of k mirror-pair
       agreements: a k-controlled NOT of algebraic degree k (one control at n = 3, affine; two at n = 5, a Toffoli on
       agreement bits). The center flips on exactly the 2^(k+1) palindromes, share 2^-k. At n = 1 the control is empty
       and the center always flips. (Every word, n = 1, 3, ..., 15.)
P18.2  Center states with equal value weights and a definite response to NOT: nonnegative weights give exactly one,
       (1/2, 1/2), response +1; signed weights give exactly two, (1, +-1) normalized, responses +-1, the centers of
       Psi+ and Psi-. One state read by values and by NOT-responses under one rule |a|^p, each normalized, forces p = 2.
P18.3  On the NOT-odd sector (C v = -v) every definite response lambda of tau_n satisfies lambda^n = -1. At even n no such
       lambda is real; at n = 2, tau_2^2 = C_2 and the responses are +-i. At odd n the real response -1 occurs on every
       orbit, and non-real responses occur from n = 3. (Exact orbit count n = 1-12; numerical spectra n = 1-8.)
P18.4  Phase reading: with the center in (|0> - |1>)/sqrt2, facing leaves the center unchanged and writes the selector as a
       sign on the rest of the word, |o>|-> -> (-1)^(s_n(o)) |o'>|->, with o' the faced outside; with the center in
       (|0> + |1>)/sqrt2 no sign is written. (Statevector, random outside states, n = 3, 5, 7.)
```

## Appendix B  Reproduction

- Environment: Python 3.11 or later. The standard library suffices except for `center_motion.py` (NumPy), the numeric cross-check in `addendum_tables.py` (NumPy, skipped if absent) and `fig_fixed.py` (Matplotlib). Run each script from the folder that holds it; `ringops.py` holds the shared operators.
- `python3 addendum_tables.py`: every table of this addendum, each entry asserted against its law (a few seconds). Writes tables.json. Last line: ALL TABLES ASSERTED.
- `python3 programs16.py`: predictions16, P16.1–P16.4. Last line: ALL PREDICTIONS16 CHECKS PASS.
- `python3 direction17.py`: predictions17, P17.1–P17.4, including the two LEN-1 clauses that failed as sealed. Last line: ALL PREDICTIONS17 CHECKS PASS.
- `python3 center18.py`: predictions18, P18.1–P18.4 (NumPy for the spectra and the statevector check). Last line: ALL PREDICTIONS18 CHECKS PASS.
- `python3 verify_routes.py`: closed routes by stacked ranks (n = 1–10), defect supports (n = 1–14) and necklaces (L = 1–14).
- `python3 catalog4.py`: the interfaces of AGL(L,2) for L = 2, 3 and 4 (P14.1–P14.3).
- `python3 center_motion.py` and `python3 successor_center.py`: the center under ring motions (P14.4–P14.7).
- `python3 programs15.py`: native programs, chains, the successor's carried transitions and the twisted clock one LEN up (P15.1–P15.5).
- `python3 addendum_checks.py`: the fixed-necklace formula against brute force (L = 1–18), the orbit and reflection counts of the twisted clock, and the pairs that carry the successor's single-site shares (about a minute).
- `python3 fig_fixed.py`: Figure 1.
- Record: the computations were run in a Claude (Anthropic) session on 5 November 2026. The external notebooks are described in Technical Note A1.

## References

[1] D. A. Kulik, Facing, Composition and the Center in Native Binary Rings (technical manual). QuHarmonics Research Group, 2026.

[2] D. A. Kulik, Native Binary Rings, Observation Depth, and the Memory of Continuation. QuHarmonics Research Group, 2026.

[3] D. A. Kulik, One Inverter. QuHarmonics Research Group, 2026.

[4] D. A. Kulik, Chained Difference Routes as Transformations are the Constitutive Substrate of Reality. QuHarmonics Research Group, 2026.

[5] D. A. Kulik, NEXUS §181: The Ring as a Memory Map of Transitions (exact finite verifier). QuHarmonics Research Group, 2026.

[6] D. A. Kulik, NEXUS v6.2 Return Operator Ledger (project record), 2026.

[7] N. G. de Bruijn, A combinatorial problem. Proc. Koninklijke Nederlandse Akademie van Wetenschappen 49, 758 (1946).

[8] J. Singer, A theorem in finite projective geometry and some applications to number theory. Trans. Amer. Math. Soc. 43, 377 (1938).

[9] S. W. Golomb, Shift Register Sequences. Holden-Day, San Francisco (1967).

[10] W. Burnside, Theory of Groups of Finite Order. Cambridge University Press (1897).

[11] T. Toffoli, Reversible computing. In Automata, Languages and Programming (ICALP 1980), Lecture Notes in Computer Science 85, 632–644. Springer (1980).

[12] S. Aaronson, Is quantum mechanics an island in theoryspace? arXiv:quant-ph/0401062 (2004).

[13] M.-O. Renou et al., Quantum theory based on real numbers can be experimentally falsified. Nature 600, 625–629 (2021).

[14] R. Cleve, A. Ekert, C. Macchiavello and M. Mosca, Quantum algorithms revisited. Proc. R. Soc. Lond. A 454, 339–354 (1998).
