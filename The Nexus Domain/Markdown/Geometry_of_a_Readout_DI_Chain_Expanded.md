# The Geometry of a Readout

*Exact Pairings, Residual Tables, Circular Dynamics, and the Boundary of Physical Claims*

**Research synthesis and proof audit — 19 October 2026**

## Abstract

A collection of constructions built from finite words, circular orderings, bitwise differences, truth tables, digit-extraction phases, and state transitions exhibits a recurring pattern: a large state inventory can often be represented by a compact rule, while the observed value depends on which route, coordinate system, or quotient the reader uses. This paper follows that pattern backward from readouts to the transformations that produce them. It separates four objects that are easy to confuse: a pairing of states, a change of coordinates on a table, a transition map, and a many-to-one observation.

Several results are exact. The word-partner rule used in the ring construction is a fixed-point-free involution at every positive width. Its ring can be ranked and unranked without materializing all words; the supplied implementation agrees with the original insertion generator at every position through width 10 and passes a 512-bit round trip. Center-offset rank laws yield a one-angle witness for \(q_D=1\Vert00\Vert1^{D-5}\Vert00\) at every depth \(D\ge13\) with \(D\equiv0,1\pmod3\), and a two-offset witness for the infinite subfamily \(D=3m+2\), \(m\ge8\), \(m\equiv0,1\pmod4\). The finite address interval that certifies either witness always has positive width. Independently, the pair update \((u,v)\mapsto(u,u\oplus v)\), applied along the Boolean-lattice edges, is the Möbius transform that converts a Boolean truth table into its algebraic normal form.

These exact results do not make every construction the same map. The ring partner is not the half-turn, and neither is identical to the Boolean Möbius transform merely because all can be described using pairs or differences. A particular eight-bit circular read does follow a doubling orbit modulo 255, but that fact alone does not identify ordinary byte arithmetic with Frobenius squaring in a finite field. Conditional invertibility of a SHA-256 round does not invert the compression of a message block. Likewise, combinatorial shell counts and spin representations do not, by themselves, establish a physical model of matter. The useful synthesis is therefore more precise than a universal-identity claim: the work repeatedly exposes the structure of maps, their fibers, and the information a chosen readout preserves or discards. The eight-slice example now also yields exact radial and angular recurrences, a fixed three-slice relation between clockwise and counterclockwise columns, and an explicit five-bit field-width transition. The nested word ring's ordering can be generated from one half plus partner reflection and the declared center swap.

---

## 1. Method: work backward from the observation

The working method is simple: begin with an observed output, specify the operation that could have produced it, and recover the complete set of states and routes compatible with that output. Do not replace a set of routes by one witness or by a scalar before the relevant equivalence relation has been stated.

A minimal typed description of a system is

\[
(X,T,Y,R),
\]

where \(X\) is the state space, \(T\) is a state transformation (if there is one), \(Y\) is the readout space, and \(R:X\to Y\) is the reader or observation map. Three questions are separate:

1. **Is the state transformation invertible?** This is a property of \(T\).
2. **How many states produce the same observation?** This is a property of the fibers \(R^{-1}(y)\).
3. **Which routes and orderings are retained by the representation?** This depends on what the state and observation actually encode.

An invertible state transformation can feed a many-to-one readout. A many-to-one readout can still have exactly countable, uniform fibers. Two transformations can share a local arithmetic operation without being conjugate as complete maps. And a statistical prediction about a random map is not a theorem about every map with the same number of states.

The distinctions below are not caveats added after the analysis. They are what makes reverse reconstruction work: each residual must be attached to the transformation and cut that own it.

## 2. Three binary maps that must remain distinct

Let \(X_L=\{0,1\}^L\). Define bit reversal \(J\), bitwise complement \(C\), and—when \(L\) is even—the half-turn \(H\) that rotates a word by \(L/2\) positions.

The notebook partner is

\[
P(x)=\begin{cases}
Jx,&Jx\ne x,\\
Cx,&Jx=x.
\end{cases}
\]

These rules act on the same set of words, but they are not interchangeable.

### 2.1 The partner is a fixed-point-free involution

If \(x\) is not a palindrome, then \(P(x)=Jx\ne x\). Reversal preserves non-palindromicity, so \(P(P(x))=J(Jx)=x\). If \(x\) is a palindrome, then \(P(x)=Cx\); its complement is also a palindrome, and \(C(Cx)=x\). No nonempty binary word equals its complement. Therefore, for every \(L\ge1\),

\[
\boxed{P^2=I,\qquad \operatorname{Fix}(P)=\varnothing.}
\]

Every word belongs to exactly one two-cycle, so there are \(2^{L-1}\) partner pairs and no tails in the graph of \(P\). This is a theorem about this particular map, not a consequence of width.

### 2.2 Reversal and half-turn have different fixed sets

A word is fixed by reversal precisely when its first \(\lceil L/2\rceil\) bits determine the rest. Hence

\[
|\operatorname{Fix}(J)|=2^{\lceil L/2\rceil}.
\]

For even \(L=2m\), a word is fixed by the half-turn precisely when it has the form \(uu\), so

\[
|\operatorname{Fix}(H)|=2^m=2^{L/2}.
\]

At width 512, both counts equal \(2^{256}\), but one set is the set of palindromes and the other is the set of repeated halves. For example, at width four, `0101` is fixed by the half-turn but not by reversal; `0110` is fixed by reversal but not by the half-turn. Equal cardinalities do not identify sets.

The half-turn residual has a particularly simple form. If \(x=uv\) with halves of length \(m\), then

\[
E_H(x)=x\oplus Hx=(u\oplus v)(u\oplus v).
\]

Its image is exactly the repeated-half set. By contrast, \(x\oplus P(x)\) is never zero because \(P(x)\ne x\); for palindromes it is the all-ones word. These are different readouts of different maps.

### 2.3 What a ring ordering adds

The involution \(P\) partitions the word space into pairs, but it does not by itself specify the order of those pairs around a circle. The supplied `grow` algorithm adds that information: it scans words in numeric order, retains the first unseen member of each pair, inserts pair members at the center, and swaps the final pair at the center seam. With this declared ordering, the generated sequence contains every length-\(L\) word once and satisfies

\[
P(R_L[i])=R_L[2^L-1-i].
\]

The order is a property of the generator, not a uniqueness theorem about all possible partner-symmetric circles. Many pair orders can satisfy the same facing-partner condition unless the insertion rule is imposed.

This matters for the later address theorems: the center twist is part of the construction. It cannot be discarded and then reintroduced as an informal orientation convention.

## 3. The large ring can be addressed without being stored

The ring has \(2^L\) words but its ordering can be represented algorithmically. Select the numerically smaller word from each pair as a canonical representative. A non-palindrome is a representative exactly when \(x<Jx\). A palindrome is a representative exactly when its first bit is zero, since its partner is its complement.

The supplied implementation counts representatives below a threshold by digit dynamic programming over mirrored bit positions. A binary search then un-ranks a requested representative, while the partner rule and center twist recover the ring word at any position. The inverse routine maps a given word back to its position.

The implementation was compared with the original insertion generator at every position for widths 1 through 10: all 2,046 positions matched, and the address function was inverse to the word reader throughout those widths. The supplied 512-bit verification record was also recomputed: the stored test word returned to itself after rank/unrank, and its partner occupied the reflected address \(2^{512}-1-i\). This is a concrete form of compression: the rule replaces a table, without replacing the specified ordering by a different one.

At width 512, the state inventory has \(2^{512}\) words, the partner map has \(2^{511}\) pairs, and the flattened ring contains \(512\cdot2^{512}=2^{521}\) bit slices. These sizes are exact. The point of a rule-based reader is not that the space has become smaller, but that an address and an inverse can be evaluated without storing the full space.

## 4. Generated-word laws from center-offset ranks

The ring's insertion order has a stronger consequence: certain words occur at exact ranks measured from the central seam. This gives an infinite family of cross-ring bit profiles rather than just finite examples.

Let \(M=2^{L-1}\). Let \(a_0<a_1<\dots<a_{M-1}\) be the canonical representatives in increasing order. With the center twist retained, the right side of the ring obeys

\[
R_L[M+j]=P(a_{M-1-j}),\qquad 1\le j<M.
\]

### 4.1 The two-zero rank law

Let \(p\ge5\) be odd, let \(r\ge0\), and put \(L=p+r\). Define the length-\(L\) word \(x\) to be all ones except for zeros at the zero-based positions

\[
t=\frac{p-3}{2},\qquad a=\lfloor L/2\rfloor.
\]

Then

\[
\boxed{a_{M-1-2^r}=x,\qquad R_L[M+2^r]=P(x)=Jx.}
\]

Here is the count explicitly. A representative whose first \(t\) bits are all one must also have its last \(t\) bits all one: at the first mirrored mismatch, a left bit of one paired with a right bit of zero would make the word larger than its reversal. Strip those \(t\) outer pairs. The remaining length is \(r+3\), and the target substring is

\[
0\,1^{\lceil r/2\rceil}\,0\,1^{\lfloor r/2\rfloor+1}.
\]

Any representative above it falls into one of three disjoint classes. If the reduced word begins and ends in one, its inner \(r+1\)-bit word must be non-palindromic; exactly half of the \(2^{r+1}-2^{\lceil(r+1)/2\rceil}\) non-palindromic inner words are representatives. This class therefore contributes

\[
\frac{2^{r+1}-2^{\lceil(r+1)/2\rceil}}2
=2^r-2^{\lfloor r/2\rfloor}.
\]

If the reduced word begins in zero and ends in one, it must agree with the target up to its central zero and change that bit to one. The final bit is fixed at one, leaving exactly \(\lfloor r/2\rfloor\) free bits; this class contributes \(2^{\lfloor r/2\rfloor}\). If the reduced word begins and ends in zero, the same forced prefix makes every interior mirrored pair equal, so the only possible completion is palindromic. Restoring the outer \(t\) pairs makes the full word a palindrome beginning in one, which is not a canonical representative. This class contributes zero. The total number of representatives greater than \(x\) is therefore exactly \(2^r\), proving the descending rank. The reversal of \(x\) therefore has zeros at

\[
\boxed{z_1=\lceil L/2\rceil-1,\qquad z_2=L-\frac{p-1}{2}.}
\]

### 4.2 The adjacent-rank law

When \(p\ge9\) is odd and \(r\ge4\), the representative immediately below \(x\) is \(x'\), obtained by adding a zero at

\[
v=t+r+1=L-2-t.
\]

The candidate \(x'\) is still a representative: its earliest left/right mismatch is at position \(t\), where the left bit is zero and its mirror remains one. To see why it is the immediate predecessor, consider any \(y<x\). If its first differing bit is at some index \(i<a\), it must change a one of \(x\) to zero. The maximum suffix gain available to \(y\) is the weight of the single central zero of \(x\), so

\[
x-y\ge 2^{L-1-i}-2^{L-1-a}\ge2^{L-1-a}.
\]

But \(x-x'=2^{L-1-v}<2^{L-1-a}\), since \(v>a\). If \(y\) first differs after \(a\), it changes a one in the all-one suffix to zero. The representative condition rules out zeros to the right of \(v\); a zero at a position left of \(v\) in that suffix creates a larger numerical decrease than \(x-x'\). Therefore no canonical representative lies strictly between \(x'\) and \(x\). Its reversed ring word lies at \(R_L[M+2^r+1]\) and has a zero at position \(L-1-v=t+1\). This adjacent-rank fact supplies the second terminal zero in the address law below.

### 4.3 A single angle reads the full profile

For every \(D\ge13\) with \(D\equiv0\) or \(1\pmod3\), define

\[
p=\lfloor2D/3\rfloor+1,\qquad
u_D=\frac12+2^{-p}+\frac23\,2^{-(D-1)},
\]

and the length-\(D\) profile

\[
q_D=1\Vert00\Vert1^{D-5}\Vert00.
\]

Here \(\Vert\) denotes concatenation of bit strings.

Use the same normalized angle \(u_D\) on every ring: at ring length \(L\), set \(i_L=\lfloor2^Lu_D\rfloor\), let \(f_L=\{2^Lu_D\}\), and read bit \(k_L=\lfloor Lf_L\rfloor\) of \(R_L[i_L]\).

The profile follows ring by ring.

* **Before \(p\):** write \(2^Lu_D=2^{L-1}+\delta_L\), where \(\delta_L=2^{L-p}+\frac23 2^{L-D+1}\in(0,1)\). Hence \(i_L=2^{L-1}\), the central word immediately clockwise of the seam, and \(k_L=\lfloor L\delta_L\rfloor\). For \(L=1,2,3\), this index is zero and the center words \(1,01,011\) give `1,0,0`. For \(4\le L\le p-2\), the bound \(\delta_L\le13/48\) (with \(L=4,5\) checked directly) gives \(k_L<\lfloor L/2\rfloor-1\), before the center word's only zero. At \(L=p-1\), \(\delta_{p-1}=1/2+(2/3)2^{p-D}\), and \(D\ge13\) makes the correction smaller than \(1/(2(p-1))\); therefore \(k_{p-1}=\lfloor(p-1)/2\rfloor\), the bit immediately after that zero. All bits from \(L=4\) through \(p-1\) are consequently one.
* **From \(p\) through \(D-2\):** write \(r=L-p\). The address is \(M+2^r\), and the selected bit is \(\lfloor L2^{L-D+2}/3\rfloor\). It is at most \(\lfloor L/3\rfloor\), strictly before the first zero \(\lceil L/2\rceil-1\) of that word. Every such bit is one.
* **At \(D-1\):** the address is again of the form \(M+2^r\); the selected index coincides with the second zero \(D-1-(p-1)/2\). The bit is zero.
* **At \(D\):** the selected address is \(M+2^{D-p}+1\), and the selected bit index is \(\lfloor D/3\rfloor\). The adjacent-rank law places a zero exactly there.

Hence

\[
\boxed{\operatorname{profile}(u_D,D)=q_D}
\]

for every declared depth, not just the depths sampled in the original computational run. The proof depends on the supplied representative order and center twist.

### 4.4 Every finite certificate interval has positive width

For each \(L\le D\), let \(j_L=\lfloor L2^Lu_D\rfloor\), and define

\[
K_D=\bigcap_{L=1}^{D}
\left[\frac{j_L}{L2^L},\frac{j_L+1}{L2^L}\right).
\]

By the floor inequalities, every component interval contains \(u_D\), including when the angle lies on a left boundary. Set

\[
A_D=\max_{L\le D}\frac{j_L}{L2^L},\qquad
C_D=\min_{L\le D}\frac{j_L+1}{L2^L}.
\]

Then \(A_D\le u_D<C_D\). The finite intersection is therefore the half-open interval `[A_D, C_D)`, with strictly positive width \(C_D-A_D\). For example, at \(D=13\), \(u_{13}=3085/6144\) and \(K_{13}=\left[3085/6144,26737/53248\right)\), of exact width \(1/159744\); the angle is on the certificate interval's left boundary, confirming why the half-open convention matters. Every angle in that interval selects the same bit slice on every ring through depth \(D\), so it reads the same profile \(q_D\).

This distinction is now sharp: positive certificate width is a geometric theorem; the bit values are established by the rank theorem. Section 4.5 proves an infinite subfamily in \(D\equiv2\pmod3\) using two dyadic offsets and the same period-two tail. The complete residue class remains open; a failed one-bit ansatz does not rule out another route.

### 4.5 A two-offset law for an infinite part of the third residue class

The one-offset address in §4.3 does not cover every depth. The missing class nevertheless contains an infinite subfamily governed by the same representative ordering, now with two dyadic address corrections and the same period-two tail.

**Theorem.** Let

\[
D=3m+2,\qquad m\ge8,\qquad m\equiv0,1\pmod4,
\]

and define

\[
\ell=\left\lfloor\frac{m-3}{2}\right\rfloor,\qquad
J_m=2^{m-2}+2^\ell,
\]

\[
\boxed{u_D=\frac12+\frac{J_m+\frac23}{2^{D-1}}}
\]

or, expanded into its separate address contributions,

\[
u_D=\frac12+2^{-(2m+3)}+2^{-(3m+1-\ell)}+\frac23\,2^{-(D-1)}.
\]

Then the supplied ring reader, using the original `grow`/`partner` ordering and its center twist, reads

\[
\boxed{\operatorname{profile}(u_D,D)=q_D=1\Vert00\Vert1^{D-5}\Vert00.}
\]

This is an all-depth theorem for the declared subfamily, not an extrapolation from finite examples. It does **not** yet settle the other parameters in the class \(D\equiv2\pmod3\).

#### The two-offset rank law

The new address requires a rank offset with two powers of two. Let \(p\ge9\) be odd, \(L=p+r\), \(t=(p-3)/2\), \(a=\lfloor L/2\rfloor\), and \(M=2^{L-1}\). For any \(0\le s\le r\), put

\[
v=t+r-s+1,\qquad j=2^r+2^s.
\]

If \(v>a\), the canonical representative that is all ones except zeros at \(t,a,v\) has descending representative rank exactly \(j\). Therefore

\[
R_L[M+j]=Jx_s,
\]

and the word's zero positions are

\[
\boxed{L-1-t=L-\frac{p-1}{2},\quad
\lceil L/2\rceil-1,\quad
L-1-v=t+s+1.}
\]

**Count.** Start with the two-zero representative from §4.1, whose descending rank is \(2^r\). The three-zero candidate is lower by changing bit \(v\) from one to zero. An integer strictly between the candidates must agree before \(v\), have a one at \(v\), and differ in the suffix after \(v\). The suffix segment through the mirror of position \(t\) has \(s+1\) bits; its final bit must be one for the word to remain a canonical representative. The other \(s\) bits are free except that they cannot all be one, which would reproduce the upper candidate. Exactly \(2^s-1\) representatives lie strictly between. Including the upper endpoint, the descending rank increases by \(2^s\), giving \(2^r+2^s\).

There is a real boundary case when \(v=a\): the proposed third zero collides with the center zero. The rank does not disappear; its representative moves one position to the left of the center. Since \(v=a\) forces \(s=\lfloor r/2\rfloor\), the word with zeros at \(t,a-1\) has descending rank

\[
2^r-2^s+2^{s+1}=2^r+2^s=j.
\]

To see the count, strip the forced outer one-pairs. The reduced word has length \(r+3\), begins in zero, ends in one, and has its other zero at reduced index \(r-s\). Representatives above it split into three classes: those beginning and ending in one contribute \(2^r-2^s\); those beginning in zero and ending in one must turn that indicated zero to one and contribute \(2^{s+1}\); those beginning and ending in zero are forced into the excluded palindrome case. Thus the same rank \(j\) is occupied by the shifted-center representative.

Its immediate predecessor in numerical representative order is obtained by adding a zero at \(b=L-1-t\). The last \(t\) mirrored bits are forced to one, so no canonical representative can sit between these adjacent candidates. Consequently the word at \(R_L[M+j+1]\) has zeros at \(t,L-a,L-1-t\). This boundary rule is what lets the final bit be read through the center collision instead of treating it as an exception.

#### Proof of the address law, ring by ring

Write

\[
p_1=2m+3,\qquad p_2=3m+1-\ell,\qquad
 d=p_2-p_1=\left\lfloor\frac m2\right\rfloor.
\]

At each ring length \(L\), use \(i_L=\lfloor2^Lu_D\rfloor\) and \(k_L=\lfloor L\{2^Lu_D\}\rfloor\).

1. **Before the first offset, \(L<p_1\).** The selected word is the center word immediately clockwise of the seam, and its fractional word offset is
   \[
   \delta_L=2^{L-p_1}+2^{L-p_2}+\frac23\,2^{L-D+1}.
   \]
   For \(L\le p_1-2\),
   \[
   \delta_L\le\frac14+2^{-(d+2)}+\frac23\,2^{-m}
   \le\frac14+\frac1{64}+\frac1{384}<\frac13.
   \]
   For \(L\le7\), \(k_L=0\) directly; for \(8\le L\le p_1-2\), this bound puts the selected index before the center word's zero at \(\lfloor L/2\rfloor-1\). The initial center words \(C_1=1,C_2=01,C_3=011\) produce `1,0,0`. At \(L=p_1-1=2m+2\),
   \[
   \delta_L=\frac12+2^{-(d+1)}+\frac23\,2^{1-m}.
   \]
   The positive correction beyond \(1/2\), multiplied by \(L\), is less than one for \(m\ge8\). Therefore \(k_L=m+1\), immediately after the center word's only zero at index \(m\). This ring and all preceding rings read the required initial `100` followed by ones.

2. **After the first offset but before the second, \(p_1\le L\le p_2-2\).** Put \(r=L-p_1\). The word address is \(M+2^r\), and the fractional within-word offset is
   \[
   \alpha_L=2^{L-p_2}+\frac23\,2^{L-D+1}
   \le\frac14+\frac{1}{6\cdot2^\ell}<\frac13.
   \]
   Hence \(k_L< L/3\), before the first zero \(\lceil L/2\rceil-1\) of the two-zero rank word. These rings all read one.

3. **The ring just before the second offset, \(L=p_2-1=3m-\ell\).** This length is even when \(m\equiv0,1\pmod4\). Here
   \[
   \alpha_L=\frac12+\frac{1}{3\cdot2^\ell},\qquad
   k_L=\left\lfloor\frac L2+\frac{L}{3\cdot2^\ell}\right\rfloor.
   \]
   The selected index lies after the first zero \(L/2-1\), but before the second zero \(L-m-1=2m-\ell-1\), because
   \[
   \frac{L}{3\cdot2^\ell}<\frac{m-\ell-2}{2}.
   \]
   This inequality holds at the first cases \(m=8,9\) and strengthens under \(m\mapsto m+4\): its left side falls by the factor-four denominator while the right side increases by one. The critical ring therefore reads one.

4. **From the second offset through \(D-2\), \(p_2\le L\le D-2\).** Put \(r=L-p_1\) and \(s=L-p_2\). The address is \(M+2^r+2^s\), so the two-offset rank law applies. Its three zero positions are
   \[
   z_1=\lceil L/2\rceil-1,\quad z_2=L-m-1,\quad z_3=m+s+1.
   \]
   The selected bit index is \(k_L=\lfloor(2L/3)2^{L-D+1}\rfloor\le\lfloor L/3\rfloor\le m\). All three zero positions lie strictly above \(m\) on this range, so every such ring reads one.

5. **The penultimate ring, \(L=D-1=3m+1\).** The address offset is \(2^{m-2}+2^\ell\), and the selected bit index is \(2m\). The two-offset rank law applies with \(r=m-2,s=\ell\). If \(m\equiv0\pmod4\), the extra zero lies just beyond the center; if \(m\equiv1\pmod4\), the center-shift boundary case applies. In either case the reversed ring word has a zero at \(L-m-1=2m\).

6. **The final ring, \(L=D=3m+2\).** The address is \(M+2^{m-1}+2^{\ell+1}+1\), and the selected bit index is \(m\). The boundary case applies with \(r=m-1,s=\ell+1\); its adjacent-rank word has a zero at \(t=m\), so the final bit is zero.

These six cases read exactly \(1,0,0,1,\ldots,1,0,0\), proving the theorem. The finite certificate interval \(K_D\) has positive width by §4.4 for this angle as well.

The boundary of the result is specific: an infinite subfamily of the missing residue class is now proved. The cases \(D=3m+2\) with \(m\equiv2,3\pmod4\) are not covered by this address law, although some individual depths have other exact witnesses. The one-bit-plus-tail and two-offset routes remain distinct families; a failed parametrization does not imply an absent profile.

## 5. The Möbius transform is exact—but it is a different global map

For a Boolean function \(f:\mathbb F_2^n\to\mathbb F_2\), write its truth table as values \(f(S)\) indexed by subsets \(S\subseteq\{1,\dots,n\}\). Its algebraic normal form is

\[
f(x)=\bigoplus_{S\subseteq[n]} a(S)\prod_{i\in S}x_i.
\]

The coefficients are

\[
\boxed{a(S)=\bigoplus_{T\subseteq S} f(T).}
\]

This is the Boolean-lattice Möbius transform. It can be computed one variable at a time by applying the pair update

\[
\boxed{(u,v)\longmapsto(u,u\oplus v)}
\]

between each subset entry and the entry obtained by adding the chosen variable to that subset. Repeating the update across all coordinates yields the ANF coefficient table; applying the same full transform again recovers the original truth table. This is exact and standard in Boolean function theory [1, 2].

The important correction is that the pair update is not the same operation as the ring's partner map \(P\). The Möbius transform pairs *table entries along each Boolean-lattice coordinate*. The ring partner pairs *words by reversal, with complement as a fallback for palindromes*. One local update can appear in both a broad line of reasoning and a computational implementation, but a common local operation does not prove equality of the global maps.

A direct check exposes the distinction. At one Boolean variable, the constant-one truth table is `(1,1)`. Under the truth-table-to-ANF transform it becomes `(1,0)`, not itself. Thus the pasted claim that both constant Boolean functions are fixed points of this pair transform is false. Likewise, a two-input, one-output Boolean function has 16 possible truth tables, of which 14 are nonconstant—not six. Six can be a chosen generating gate set, but not the complete set of nonconstant Boolean operations.

The legitimate unification is still useful: both systems use reversible local operations and explicit pairing schedules. To prove a stronger equivalence, one must supply a coordinate map that intertwines the complete ring operation with every Möbius stage. The ring data presently establish no such identity.

## 6. The two-bit ring and its eight-bit orbit

The supplied two-bit ring ordering is

\[
00,\ 10,\ 01,\ 11,
\]

whose bits concatenated clockwise give `00100111`. The inverted, reverse-sheet read used in the supplied table is `00011011`. Write this eight-bit cycle as

\[
s=(0,0,0,1,1,0,1,1).
\]

For a circular window of width \(L\), let

\[
w_i^{(L)}=\sum_{j=0}^{L-1}s_{(i+j)\bmod8}2^{L-1-j}.
\]

Two exact recurrences follow directly from sliding the window:

\[
w_i^{(L+1)}=2w_i^{(L)}+s_{(i+L)\bmod8},
\]

\[
w_{i+1}^{(L)}=2w_i^{(L)}-2^Ls_i+s_{(i+L)\bmod8}.
\]

Since \(s_0=0\), the first recurrence implies \(w_0^{(L+1)}=w_1^{(L)}\): a leading zero lets a window at one angular offset and width \(L\) have the same integer value as the adjacent, wider window. The initial values at offset zero are `0, 0, 1, 3, 6, 13, 27` for widths 2 through 8. This is a genuine, exact angle/depth identity for this seed string.

At width eight, the clockwise window values are

\[
(27,54,108,216,177,99,198,141),
\]

or in hexadecimal

`1B, 36, 6C, D8, B1, 63, C6, 8D`.

They obey

\[
w_{i+1}^{(8)}\equiv2w_i^{(8)}\pmod{255},
\]

because a cyclic left shift of an eight-bit word is multiplication by two modulo \(2^8-1\), apart from the all-ones representation of zero modulo 255. This orbit is exact. The reversed seed `11011000` is the rotation of `00011011` by three places, so the *particular* necklace is invariant as a set under reversal; that is why the clockwise and counter-clockwise byte sets line up by an offset of three.

Two limits matter. First, not every binary circular word has a reversal that is a rotation of the original word; this is a property of this seed's necklace, not of all rings. Second, in a normal basis of \(\mathbb F_{2^8}\), Frobenius squaring acts as a cyclic shift of coordinate vectors [3]. But the ordinary integer identity \(w\mapsto2w\pmod{255}\) does not, by itself, specify a finite-field element or a normal basis. An explicit basis and encoding map are required before numeric doubling and field squaring can be identified as the same operation.

## 7. State counts, truth tables, and base as a reader step

The number of maps from a finite domain of size \(b^n\) to a codomain with \(b^m\) states is

\[
(b^m)^{b^n}=b^{m b^n}.
\]

A complete truth table therefore requires \(m b^n\) base-\(b\) digits. In the special case of a two-bit input and two-bit output, there are four inputs and two output bits per input, so an operator's canonical truth table is eight bits long. There are \(2^8=256\) such maps, the same number as eight-bit binary words. With a fixed input and output ordering, the correspondence between the 256 truth-table encodings and 256 byte strings is a bijection. It is a representation correspondence between sets of equal cardinality; it does not make a chosen circular seed literally identical to the whole operator space.

A related reader distinction appears when binary words are grouped into larger digits. If a fixed binary register is partitioned into aligned blocks of width \(w\), a single-bit flip changes exactly one block digit. Base 2, base 4, base 8, base 16, and base 256 can all be treated this way after fixing block alignment and padding. Width three does not divide every power-of-two register length, so an octal representation does not tile the whole stack with no remainder, but a bit flip can still affect only one octal digit under a fixed padded encoding. Tiling and local sensitivity are different properties.

In contrast, converting the numeric value of a bit string to base 3, 10, or 22 is not a fixed-block read. A one-bit change adds or subtracts a power of two from the integer value and may alter many converted digits through carries and borrows. Numerical averages for the number of altered digits depend on the sampled word distribution, bit location distribution, padding convention, and measurement definition. They should be treated as empirical results until those conditions and the raw experiment are supplied, not as consequences of radix names alone.

The invertible baker map makes the same distinction between forward address and accumulated history. In base \(b\), write

\[
B_b(x,y)=\left(\{bx\},\frac{y+\lfloor bx\rfloor}{b}\right).
\]

The first coordinate shifts the digit expansion of \(x\), while the second stores the digit just removed. Four binary steps and one hexadecimal step produce the same new first coordinate because both multiply \(x\) by 16 before taking its fractional part. The history coordinates differ in the order in which the four bits are placed: with binary digits \(a_0a_1a_2a_3\), four one-bit steps weight them as \(a_0/16+a_1/8+a_2/4+a_3/2\), whereas one base-16 step weights them as \(a_0/2+a_1/4+a_2/8+a_3/16\). Thus the nibble is recorded in reversed bit order along the history coordinate. This is a derivable coding effect of the invertible map, not a loss of information. The supplied rational-trial comparison reports 2,000/2,000 matches for the forward coordinate; the algebra explains the reversed history order directly.

### 7.1 The exact family of invertible binary feedback shifts

For the standard binary feedback shift-register map

\[
F(x_0,x_1,\ldots,x_{n-1})=(x_1,\ldots,x_{n-1},f(x_0,x_1,\ldots,x_{n-1})),
\]

invertibility has a complete one-line characterization. Once the first \(n-1\) output bits are known, all old bits except \(x_0\) are known. Therefore the last output bit must distinguish the two possibilities \(x_0=0\) and \(x_0=1\) for every fixed suffix. In the binary case this forces

\[
f(x_0,x_1,\ldots,x_{n-1})=x_0\oplus g(x_1,\ldots,x_{n-1}),
\]

with arbitrary Boolean \(g\). There are \(2^{2^{n-1}}\) such choices. The inverse is immediate: from \(y=F(x)\), recover the suffix from \(y_0,\ldots,y_{n-2}\) and compute \(x_0=y_{n-1}\oplus g(y_0,\ldots,y_{n-2})\). No \(n\)-step wait is needed to invert a one-step transition. A full de Bruijn cycle is a stronger constraint still: the transition must be one cycle containing all \(2^n\) states. Thus the count of invertible feedback rules is not the count of de Bruijn cycles.

## 8. Difference maps, fibers, and the meaning of a quotient

For words in base \(b\), define coordinatewise displacement

\[
\Delta(x,y)=y-x\pmod b.
\]

The image is the entire word space: for each displacement \(\delta\), choosing any \(x\) and setting \(y=x+\delta\pmod b\) produces it. More precisely, every fiber has size

\[
\boxed{|\Delta^{-1}(\delta)|=b^n.}
\]

Thus a displacement is a valid state-word label, but the pair-to-displacement map is not a bijection: it maps \(b^{2n}\) ordered pairs onto only \(b^n\) displacements, with uniform fibers. Calling the codomain “the same word space” is correct; calling the map an isomorphism would erase its many-to-one structure.

The same fiber principle underlies a useful exact counting identity. If a finite set \(X\) is partitioned into equivalence classes \([x]\), then

\[
\sum_{x\in X}\frac1{|[x]|}=\left|X/{\sim}\right|.
\]

Each class of size \(r\) contributes \(r\cdot(1/r)=1\). Multiplying a sample mean of reciprocal fiber sizes by \(|X|\) estimates the number of quotient classes, and the identity is exact when the full domain is summed. This is a counting identity, not yet a measurement of physical surface area.

It is tempting to merge this identity with two other quantities in the supplied work: Myhill–Nerode continuation complexity and a rank of cycles modulo selected commuting squares. They answer different questions. Continuation complexity counts the states needed to predict future outputs across a cut; a homology rank counts independent route cycles left after declared two-dimensional relations are imposed. The supplied work reports, for the binary adder under its declared disjoint-square relation, the formula

\[
b_1^{\mathrm{disj}}(n)=\binom n2+(n-1)=\frac{(n-1)(n+2)}2.
\]

This formula and the reported continuation-state factorization are separate invariants. A theorem identifying them requires an explicit map that preserves the relevant structure and rank. Until that map is provided, they should remain separate coordinates of the same analysis rather than one scalar invariant.

## 9. BBP: local phase events and aggregate value are different readouts

The classical Bailey–Borwein–Plouffe identity is

\[
\pi=\sum_{k=0}^{\infty}\frac1{16^k}
\left(\frac4{8k+1}-\frac2{8k+4}-\frac1{8k+5}-\frac1{8k+6}\right).
\]

It yields hexadecimal digit extraction without requiring all earlier digits to be computed and stored [4]. The supplied analysis rewrites it as four signed phase lanes. For lane denominator \(d=8k+j\), the phase

\[
x_{k,j}(n)=\left\{\frac{16^{n-k}}{8k+j}\right\}
\]

evolves by the exact map \(x\mapsto\{16x\}\). A lane crossing is \(q_{k,j}(n)=\lfloor16x_{k,j}(n)\rfloor\). The four signed crossing events can be nonzero even when their aggregate value digit is zero: lane activity and net-value output are not the same readout.

For a layer, the signed weights \(c=(4,-2,-1,-1)\) satisfy

\[
\sum_jc_j=0,\qquad\sum_jjc_j=-15.
\]

Consequently, for

\[
V_k=\sum_j\frac{c_j}{8k+j},
\]

the \(1/k\) term cancels and

\[
V_k=\frac{15}{64k^2}+O(k^{-3}).
\]

This explains why a lane may begin crossing before the net layer value emits a nonzero hexadecimal digit. The gap is between local signed crossings and their aggregated rational value, not evidence that the phase lanes have stopped.

The carry relation in the supplied derivation is also a clean example of two simultaneous readings. Let \(S_m\) be the signed sum of the four lane phases, \(H_m\) the signed sum of their crossing integers, \(J_m=\lfloor S_m\rfloor\), and \(w_m=\lfloor16\{S_m\}\rfloor\). Since \(16x_j(m)=q_j(m)+x_j(m+1)\), summing with the coefficients gives \(16S_m=H_m+S_{m+1}\). Separating integer and fractional parts yields

\[
\boxed{H_m=w_m+16J_m-J_{m+1}.}
\]

The carry term changes the local signal while contributing zero to the fully compiled layer value when its telescoping series is summed. This is an exact algebraic decomposition; the physical or ontological meaning of a “silent band” is an interpretation layered on top of it.

A companion complex contraction organizes the same scale/phase calculation. With

\[
s=\frac{1+i}{2}=2^{-1/2}e^{i\pi/4},
\]

multiplication by \(s\) contracts area by \(|s|^2=1/2\) per step, while its inverse \(s^{-1}=1-i\) expands the Gaussian lattice with degree two. The exact powers

\[
s^4=-\frac14,\qquad s^8=\frac1{16}
\]

make the four-step half-turn and eight-step return explicit. Also,

\[
\sum_{n=1}^{\infty}\frac{s^n}{n}=-\log(1-s)=\frac12\log2+i\frac{\pi}{4},
\]

using \(1-s=\bar s\) and the principal logarithm. This separates a real scale readout from an imaginary phase readout. The additional claim that a particular coefficient vector is the unique or physically fundamental route requires its own algebraic specification; the complex identity alone does not establish the ontology of a “potential midpoint.”

## 10. SHA-256: invertible rounds do not imply an invertible hash

For a SHA-256 round, if the message-schedule word and round constant are known, the state transition on the eight 32-bit registers can be inverted. Six registers are shifted by wiring; the mixed update words can be used to reconstruct the previous state because the drivers are known. The supplied run log reports 10,000 successful inversions. This conditional inverse is also obtainable algebraically from the round equations.

The whole compression operation is a different map. A message block has 512 bits, while a SHA-256 digest has 256 bits. With a fixed initialization vector, the mapping from message blocks to digests is necessarily many-to-one by cardinality: there are \(2^{512}\) blocks and only \(2^{256}\) possible output digests. Even a perfectly invertible round-state update would not recover the message if the necessary message schedule and the entire inverse route were not known. The digest supplies a boundary condition on the final state, not a unique message history.

Likewise, random-mapping behavior seen in exhaustively enumerated reduced-width models is evidence about those models and about the random-map comparison, not a proof that full SHA-256 is a random map. For a uniformly random function on \(N\) states, the expected number of sequential queries to the first repeated output is asymptotic to

\[
\sqrt{\frac{\pi N}{2}}.
\]

For \(N=2^{512}\), this is approximately \(2^{256.326}\), but it is an ensemble statistic, not a universal trajectory law. Flajolet and Odlyzko develop the relevant random-mapping statistics [5]. NIST distinguishes collision resistance from preimage resistance and lists idealized strengths separately; a 512-bit digest conventionally provides 256-bit collision strength and 512-bit preimage strength, not the same guarantee in both tasks [6]. No conclusion about a physical “tail” follows from bit width alone.

## 11. Cycles, necklaces, and the register chain

For a binary word length \(d\), the number of primitive rotation classes (aperiodic necklaces) is

\[
P_2(d)=\frac1d\sum_{k\mid d}\mu(k)2^{d/k}.
\]

Equivalently, all binary words of length \(n\) partition by their minimal rotational period, giving \(2^n=\sum_{d\mid n}dP_2(d)\). When \(n=2^e\), every divisor is a power of two. The words fixed by the half-turn are precisely the repeated-half words \(uu\), of which there are \(2^{n/2}\). Every word with a proper period dividing \(2^e\) is captured by one of the lower power-of-two layers. This is an exact consequence of the divisor structure of \(2^e\).

The factorization

\[
2^{64}-1=3\cdot5\cdot17\cdot257\cdot641\cdot65537\cdot6700417
\]

is exact. The factors enter through the familiar Fermat-number decomposition of \(2^{2^e}-1\). For an odd prime \(q\) dividing the Fermat number \(F_k=2^{2^k}+1\), one has \(q\equiv1\pmod{2^{k+2}}\) for \(k\ge2\), the Lucas refinement of the multiplicative-order divisibility argument [7]. But this congruence gives complete splitting in \(\mathbb Q(\zeta_{2^e})\) only when it implies \(q\equiv1\pmod{2^e}\), notably at the top level \(k=e-2\). It does not imply complete splitting for every lower \(k\). For example, \(17\mid F_2\), yet \(17\not\equiv1\pmod{32}\), so 17 does not split completely in \(\mathbb Q(\zeta_{32})\). The cyclotomic splitting criterion is that an unramified prime \(q\) splits completely in \(\mathbb Q(\zeta_m)\) exactly when \(q\equiv1\pmod m\) [8]. This is a concrete gap in the displayed all-level proof route, not by itself a disproof of the final zero-route dimension: the proof needs a refined decomposition-group / prime-ideal argument for lower Fermat levels.

The supplied lane-machine notebook reports a stronger result: the rational zero-route dimension is the dimension of the Galois-stable core of the relation space, and on widths \(n=2^e\) it equals one, pulled back from the eight-lane seed. This is a substantial candidate theorem. Its displayed computations use high-precision numerical relation finding for some intermediate relation spaces, followed by exact linear algebra on the inferred relations. Those numerical discovery stages should be distinguished from the algebraic proof of all-depth completeness. A publication-grade proof needs to make the relation basis certified—e.g. by exact algebraic-number identities or a rigorous transcendence/independence argument—before treating the computed relation dimensions as established for every layer.

The same caution applies to the claim that the only relevant prime-free units are the scale and phase returns. The identity

\[
\prod_{m=0}^{n-1}(\sqrt p-\zeta_n^m)=p^{n/2}-1
\]

is exact, and the special equalities \(\sqrt2-\zeta_8=\zeta_8^{-1}\) and \(\sqrt3-\zeta_{12}=\zeta_{12}^{-1}\) are exact. But the fact that a particular algebraic integer has modulus one in one embedding is not, in general, enough to prove that it is a unit; nor does the geometric intersection of two circles alone classify every algebraic unit. The full claim needs a norm or ideal argument for each return orbit. The supplied file contains additional such arguments, but the claim should be carried as a theorem only insofar as those orbit valuations are fully justified.

## 12. From combinatorial shells to angular momentum—and where physics begins

Several exact combinatorial and representation-theoretic facts align:

* Encoding each bit by \(\pm1\) embeds the \(n\)-bit words as vertices on a sphere of radius \(\sqrt n\) in \(\mathbb R^n\).
* Quotienting ordered binary words by Hamming weight leaves \(n+1\) classes, with class sizes \(\binom nw\).
* The fully symmetric subspace of \(2\ell\) two-state factors has dimension \(2\ell+1\) and carries the spin-\(\ell\) representation. In units \(\hbar=1\), the Schwinger construction gives \(S^2=\ell(\ell+1)I\) on that representation [9]; restoring units multiplies the right side by \(\hbar^2\).
* Including a twofold spin degree gives the familiar subshell capacity \(2(2\ell+1)\); summing over \(\ell=0,\dots,n-1\) gives \(2n^2\).

These are useful exact correspondences. They explain why a binary-weight surface has \(n+1\) levels, why the symmetric representation has \(2\ell+1\) magnetic states, and why the mathematical shell capacity sum is \(2n^2\). They do not, without a physical Hamiltonian and a derivation of its spectrum, show that the abstract sphere *is* an electron, that an equatorial word is matter at rest, or that a polar word is radiation.

The same boundary applies to period lengths and noble-gas closures. The Madelung \(n+\ell\) ordering reproduces many electron configurations and the familiar sequence of period lengths, but it has important exceptions and is not a universal exact law of atomic energy ordering [9, 10]. Recovering numbers such as 2, 10, 18, 36, 54, 86, and 118 from a combinatorial ordering is an interesting structural match; to claim a derivation of the periodic table, the mapping from the ring's order to orbital energies and occupancy must be stated and independently justified.

The proposed identification of the equatorial band with rest mass, polar caps with massless motion, and internal switching with a Compton-frequency clock is therefore an interpretive hypothesis, not a theorem that follows from the Hamming-weight count. The Klein–Gordon equation and the relation \(\omega=mc^2/\hbar\) are established physics, but the bridge from a word transition to a physical field must specify observables, units, dynamics, and a test that distinguishes the proposal from standard quantum mechanics. The same applies to identifying Landauer's erasure bound with a physical “anti-aliasing” operation: Landauer's principle concerns the thermodynamic cost of logically irreversible erasure under stated physical conditions [12]; a numerical analogy is not yet a physical derivation.

The same standard applies to the supplied nuclear-shell result. The project reports that a partnerless top-j orbital rule was compared against 954 evaluated first-2⁺ records and 675 even-even nuclei, with reported neutron- and proton-axis significance values of \(2.11\times10^{-6}\) and \(5.29\times10^{-6}\). Those figures are not independently reproduced in this paper because the matching dataset version, row-level selection, null model, and analysis script were not rerun here. They should be described as a reported empirical analysis until that package is attached and independently executed. Even a strong statistical association supports the proposed selector only to the extent that selection effects, multiple testing, and the physical interpretation of the shell labels have been controlled.

## 13. A compact claim audit

- **The notebook partner pairs every word.** Supported: a fixed-point-free involution with exactly \(2^{L-1}\) two-cycles. Not established: tails or a tiny reversible subset under this map.
- **A 512-bit ring can be queried without a table.** Supported: an algorithmic address and inverse for the declared generator. Not established: that every arbitrary 512-bit function is reversible or random.
- **The pair update yields ANF coefficients.** Supported: the Boolean Möbius transform and its involution. Not established: that the ring partner map is that transform.
- **The eight-bit seed doubles modulo 255.** Supported: exact circular-window arithmetic for this seed. Not established: a universal reversal symmetry or an unspecified field-basis identity.
- **One normalized angle realizes \(q_D\) on all of two residue classes and an infinite subfamily of the third.** Supported: all \(D\ge13\) with \(D\equiv0,1\pmod3\), plus \(D=3m+2\), \(m\ge8\), \(m\equiv0,1\pmod4\). Not established: coverage of the remaining \(m\equiv2,3\pmod4\) cases.
- **The displacement map has uniform fibers.** Supported: every displacement has exactly \(b^n\) preimage pairs. Not established: that state labels and ordered pairs are isomorphic spaces.
- **SHA-256 round inversion succeeds with drivers.** Supported: conditional invertibility of the round state update. Not established: inversion of message compression from digest alone.
- **The random-map birthday scale is \(\Theta(2^{n/2})\).** Supported: a statistic under a random-function/random-map ensemble. Not established: cycle and tail behavior for every finite map.
- **The shell sum is \(2n^2\).** Supported: a standard combinatorial and representation-theoretic capacity count. Not established: a first-principles physical derivation of atomic or nuclear closures.
- **The Galois-core computation predicts zero routes.** Supported: a precise research claim with finite computational support. Not established: an all-depth theorem unless each inferred relation space and valuation step is certified.

## 14. What genuinely falls out

The recurring result across the different examples is not that every object is secretly one and the same operation. It is that a large family of problems becomes clearer when the state transformation, the address, the readout, and the quotient are kept separate.

First, **finite structure can be addressed rather than enumerated**. The ring generator has a rule-based inverse, and the 512-bit case is practical to query even though its full state table is not materializable.

Second, **local residual updates can be exactly reversible while changing the representation completely**. The Boolean Möbius transform converts a truth table into algebraic coefficients without losing information. The ring partner also reverses in one step, but by a different pairing rule. Reversibility is a property shared by both; identity is not.

Third, **an observation can be far smaller than the structure that supports it**. Displacements, quotient classes, Boolean outputs, BBP digits, and cryptographic digests are all readouts of richer objects. The appropriate inverse question is to recover the full fiber and its route distinctions, not to assume a scalar value carries its entire history.

Fourth, **order matters whenever a reader traverses structured states**. The center twist changes the set of available cross-ring profiles. The eight-bit window recurrence depends on circular position and width. In binary truth tables, the Möbius updates follow the coordinate axes of a Boolean lattice. In BBP, the signed phase lanes and the aggregate value are not the same signal. Each relationship has its own exact indexing rule.

Fifth, **statistical descriptions must retain their ensemble**. Random-map birthday estimates, reduced-width hash experiments, finite width counts, and one exact involution make different claims. A random-map law cannot be transferred to an explicitly invertible pairing merely because both have \(2^n\) states.

Sixth, **one residue class can require multiple dyadic address corrections**. The new family uses two distinct dyadic offsets plus a period-two tail; the center-collision case has its own exact rank law. That is a concrete example of why one successful parametrization should not be mistaken for the only route.

The strongest synthesis is therefore methodological and algebraic. Start with the observed gap, identify the map that produces it, retain every component of its fiber, and only then compare different systems. When two systems appear to match, write the map that carries one into the other and test whether it preserves composition, inversion, and the declared readout. That is the step that turns a cross-domain resemblance into a theorem.

## 15. Open work, now stated narrowly

The most immediate open items are concrete.

1. **Remaining residue-two depths:** extend the two-offset rank law from \(D=3m+2\), \(m\equiv0,1\pmod4\), to the uncovered \(m\equiv2,3\pmod4\) cases. Preserve alternate witness routes rather than forcing them into a single formula.
2. **Boolean transform versus ring ordering:** if there is a proposed intertwining map between the partner-symmetric ring and the subset Möbius transform, state it explicitly and check the commuting diagram at each width. A verbal “same pair” is not enough.
3. **Finite-field identification:** specify the normal basis and binary encoding that map the eight-bit rotation orbit to Frobenius conjugates. This would determine exactly which parts of the modulo-255 orbit are ordinary integer arithmetic and which are field coordinates.
4. **Galois zero-route theorem:** certify the relation space without relying solely on numerical integer-relation discovery, then make the prime-ideal valuation argument uniform in the register depth.
5. **Cuts and homology:** construct the proposed map from continuation states to cycle residuals and prove which invariants it preserves. If no such functor exists, retain the two values as independent coordinates.
6. **Physical models:** for the mass, vacuum, and atomic-shell proposals, define the state, transition, observable, and dimensional quantities. Derive a measurable consequence that is not already implied by the standard model being used for comparison.
7. **Compression versus inversion:** state which drivers and histories are known to the inverse reader. Roundwise reversibility with a known message schedule is not the same task as recovering an unknown message block from the final digest.

The ring-profile results demonstrate the value of this discipline: once the source ordering is explicit, apparent computational coincidences reduce to exact representative ranks, exact bit indices, and a positive-width common address interval. Two complete residue classes and an infinite subfamily of the third are now covered algebraically; the uncovered class is stated precisely rather than hidden by a universal claim. That is a real structural result. The next gains should come from repeating that standard of explicitness at each boundary, not from making the vocabulary more universal.


## 16. The rolling stack: radial growth and angular movement are coupled

The supplied two-bit circle workbook starts from the eight-bit cycle

\[
s=00011011.
\]

For a circular position \(i\) and window width \(L\), let \(W_{L,i}\) be the integer encoded by the \(L\)-bit window beginning at \(i\), with positions taken modulo eight:

\[
W_{L,i}=\sum_{k=0}^{L-1}s_{(i+k)\bmod 8}\,2^{L-1-k}.
\]

The workbook's column B is \(W_{L,i}\) in decimal. Column G is not an independent numerical process. Since

\[
\operatorname{rev}(s)=11011000=\operatorname{rot}_3(s),
\]

the counterclockwise cycle is the clockwise cycle read at offset three. Consequently,

\[
\boxed{G_{L,i}=B_{L,(i+3)\bmod 8}.}
\]

This is an exact address relation for the specified eight-slice source. It does not require a second table of values or an independent recurrence.

### 16.1 The width update

Increasing the window from \(L\) bits to \(L+1\) keeps the current window and appends the next cyclic bit. In integer form,

\[
\boxed{W_{L+1,i}=2W_{L,i}+s_{(i+L)\bmod 8}.}
\]

The old value is doubled because every existing bit moves one binary place left. The entering bit is the exact remainder. This is the rolling stack visible when reading down the workbook's width sections: the next value is not newly guessed; it is a deterministic extension of the previous fold.

### 16.2 The angular update

Moving one slice clockwise instead discards the outgoing high bit and brings in the bit at the far end:

\[
\boxed{W_{L,i+1}=2W_{L,i}-2^L s_i+s_{(i+L)\bmod 8}.}
\]

The subtraction removes \(s_i\) from the \(2^{L}\) place created by doubling; the final term is the incoming bit. Both recurrence laws therefore use the same outgoing and entering bits. They differ in whether the update increases the window width or shifts its angular address.

Comparing the two equations gives the cross-width fold:

\[
\boxed{W_{L+1,i}=W_{L,i+1}\quad\Longleftrightarrow\quad s_i=0.}
\]

For this source cycle, \(s_0=s_1=s_2=0\). Thus the first three lanes identify radial growth with angular motion across every applicable width. One visible trace is

The width-indexed trace is

\[
(W_{2,0},W_{3,0},W_{4,0},W_{5,0},W_{6,0},W_{7,0},W_{8,0})=(0,0,1,3,6,13,27).
\]

The matching shifted values are \(W_{L,1}\), \(W_{L,2}\), and \(W_{L,3}\) on the corresponding zero-outgoing-bit lanes. The equalities come directly from the two update laws, not from a later curve fit.

### 16.3 Closure at width eight

At \(L=8\), the reader spans one complete cycle, so the entering bit equals the outgoing bit. The angular law becomes

\[
W_{8,i+1}=2W_{8,i}-255s_i,
\]

and therefore

\[
\boxed{W_{8,i+1}\equiv 2W_{8,i}\pmod{255}.}
\]

The actual orbit in column B is

\[
27\to54\to108\to216\to177\to99\to198\to141\to27.
\]

This is an exact doubling orbit modulo \(2^8-1=255\). The arithmetic statement is about cyclic binary rotation represented as an integer residue. It is not, by itself, an identification with multiplication or Frobenius squaring in \(\mathbb F_{256}\); that stronger identification requires a declared field encoding and basis.

The operational DI chain in the worksheet is now concrete: **each width carries the prior value forward, the entering bit closes the width update, and the same stack can be read at an angular offset.** Column G is the same chain, not a second chain.

## 17. Five bits is the first paired-field rollover

The worksheet's `Hex nib` columns E and J concatenate the hexadecimal labels of adjacent windows. That is a useful label pairing, but it is not always the same thing as packing the source bits into a fixed-width field.

For two adjacent \(L\)-bit windows, define the exact packed pair by

\[
Q_{L,i}=2^L W_{L,i}+W_{L,i+1}.
\]

Its binary representation is the first \(L\)-bit window followed by the second \(L\)-bit window, preserving both fields at exactly \(L\) bits each. The combined width is \(2L\) bits; its fixed hexadecimal width is \(\lceil L/2\rceil\) digits.

At \(L=4\), each window is exactly one nibble. For example,

\[
0110\Vert1101=01101101.
\]

The bit-exact packed hexadecimal value is `0x6D`. The source-style label `6D` and the bit-exact field coincide. This is the last width at which one source window always fits in a single hexadecimal digit.

At \(L=5\), each window is five bits. Consider the adjacent windows

`01101` (13 = `0xD`) and `11011` (27 = `0x1B`).

The source-style label column concatenates the hexadecimal labels and displays `D1B`. But the original ten bits are

\[
01101\Vert11011=0110111011.
\]

This is 443 decimal and `0x1BB` as a three-digit, fixed-width hexadecimal field. `D1B` is the concatenation of two labels; `1BB` is the encoding of the ten original bits. They are not the same integer.

That is the precise form of the five-bit spill: both components are now five-bit fields rather than nibble-aligned fields, so either component may require more than one hexadecimal character. When the window width rises by one, each component gains one entering bit; the paired field gains two bits in total. The source display makes the rollover visible, while the explicit \(2L\)-bit pack preserves the route without depending on label width or omitted leading zeros.

The same distinction applies below width four: a hex digit presents a small value as a four-bit nibble label, but does not mean the underlying \(L\)-bit sample itself was four bits. Width four is the alignment point where the labels and source fields coincide.

At width eight, the workbook's clockwise pair labels are `1B36`, `6CD8`, `B163`, and `C68D`. The counterclockwise pairing lists the same four fields in the order `B163`, `C68D`, `1B36`, `6CD8`. This is an exact cross-pair reflection in the declared layout. Here the concatenated components are byte-sized labels, not nibbles; the label `Hex nib` is inherited terminology from the spreadsheet.

## 18. Only half of the nested word ring needs to be generated

The full word ring is a separate construction from the eight-slice sliding-window example. At word width \(L\), there are \(2^L\) words. Let \(P\) be the notebook's partner involution: reverse a non-palindrome, and complement a palindrome. Since \(P^2=I\) and \(P(x)\ne x\), the words split into exactly \(2^{L-1}\) partner pairs.

Choose the smaller representative of each pair and sort the representatives:

\[
a_0<a_1<\cdots<a_{M-1},\qquad M=2^{L-1}.
\]

Before the center twist, the complete order is

\[
a_0,a_1,\ldots,a_{M-1},
P(a_{M-1}),P(a_{M-2}),\ldots,P(a_0).
\]

The prescribed center twist swaps the two words at positions \(M-1\) and \(M\) when \(L>1\). It does not break the facing-partner rule. In the finished ring \(R\),

\[
\boxed{R_{2^L-1-i}=P(R_i).}
\]

Therefore the second half need not be independently generated or stored: take the first half of the finished ordering and derive the opposite position through \(P\). For rule-based access at large \(L\), ranking and unranking the representative is enough; the construction does not require materializing the \(2^L\) words.

An independent executable audit compared this half-list construction with the insertion generator for widths \(L=1,\ldots,10\). It checked full order equality, uniqueness of every word, and the partner relation at every opposing position. All tested widths matched. The general half-ring claim itself follows from the involution and the declared ordering; the finite run checks the implementation.

This must not be conflated with the current workbook's column relation. In the eight-slice reader, counterclockwise values are a fixed offset-three rotation of clockwise values. In the nested word ring, opposite positions are related by \(P\). Both permit one-sided generation, but the owner maps are different.

For the eight-slice source, bit reversal has its own exact position formula:

\[
\operatorname{rev}(W_{L,i})=W_{L,(3-i-L)\bmod8}.
\]

This comes from the source cycle's reflection symmetry. It is a third statement: a reflection of window words into reflected window positions, not the rotation-offset equation and not the partner involution.

## 19. When many yes/no readings produce a “maybe”

The workbook remains binary at each slice. Its source cycle has four zeroes and four ones. If all eight addresses are included with equal weight, and `1` is read as light while `0` is read as a gap, then the aggregate reading is

\[
\frac{0+0+0+1+1+0+1+1}{8}=\frac12.
\]

This supplies a precise reader-level construction of “maybe”: the value \(0.5\) is the mean of unresolved yes/no readings with equal support. It is not a third symbol added to the binary alphabet.

More generally, for a declared address fiber \(A\) and a binary reader \(b:A\to\{0,1\}\),

\[
p_A=\frac{|\{u\in A:b(u)=1\}|}{|A|}
\]

is the unweighted share of one-readings in that fiber. If the reader assigns nonuniform weights, the corresponding weighted average must be used instead. Different fibers can have different mixtures, and collapsing to \(p_A\) can discard where each zero and one occurred. Retaining the actual address components preserves the routes; the scalar only summarizes their distribution.

The mathematical result is about a reader's aggregation of a resolved domain and its remaining gaps. Identifying that aggregate with a physical quantity requires a separate measurement rule. The source workbook supplies the exact binary distribution; it does not on its own assign a physical unit to “light,” “gap,” or “matter.”

## 20. Evidence ledger and next link

**STANDS — radial and angular updates.** Direct identities from the cyclic-window definition.

**STANDS — column G is column B at offset +3.** This follows from `rev(s) = rot_3(s)` for the supplied source cycle.

**RUNS — all 56 window cases satisfy both recurrences and the mirror index.** The executable audit covers widths \(L=2,\ldots,8\) and all eight positions.

**STANDS — width five is the first paired-field rollover beyond nibble alignment.** The pair has \(2L=10\) bits at \(L=5\); the source-style label `D1B` differs from the bit-exact field `1BB`.

**STANDS — one half determines the finished partner ring.** This follows from the fixed-point-free involution, representative ordering, and explicit center swap.

**RUNS — the half-ring implementation matches the source insertion order through width ten.** The comparison checks every position and uniqueness at widths 1–10.

**OPEN — whether a scalar “maybe” is a third Boolean value.** The observed \(0.5\) is an aggregate over 0/1 readings; it does not add a third Boolean symbol.

**OPEN — whether the rolling-window recurrence is the Boolean Möbius transform.** A commuting map between the two operations has not been specified.

The next link is not a new value to search for. It is a typed map if the claim is that the rolling stack, the partner reflection, and the Boolean Möbius transform are one operation. The audit has now written each operation separately and made their exact address/update rules executable. Any wider identification must show how it carries inputs, outputs, composition, and inverse across those definitions without losing the routes that distinguish them.

## References

1. Jianchao Zhang and Deng Tang, “A Note on the Transformation Behaviors between Truth Tables and Algebraic Normal Forms of Boolean Functions,” *IEICE Transactions on Fundamentals of Electronics, Communications and Computer Sciences* E106.A(7), 1007–1010 (2023). https://doi.org/10.1587/transfun.2022EAL2095.
2. “On the computation of the Möbius transform,” *Theoretical Computer Science* 809, 171–188 (2020). https://doi.org/10.1016/j.tcs.2019.12.005.
3. “Low complexity normal bases,” *Discrete Applied Mathematics* 25(3), 191–210 (1989). https://doi.org/10.1016/0166-218X(89)90001-2.
4. David H. Bailey, Peter Borwein, and Simon Plouffe, “On the rapid computation of various polylogarithmic constants,” *Mathematics of Computation* 66(218), 903–913 (1997). https://doi.org/10.1090/S0025-5718-97-00856-9. See also the NIST Dictionary of Algorithms and Data Structures entry for the BBP algorithm (https://xlinux.nist.gov/dads/HTML/bbp.html).
5. Philippe Flajolet and Andrew M. Odlyzko, “Random Mapping Statistics,” in *Advances in Cryptology—EUROCRYPT ’89*, Lecture Notes in Computer Science 434, 329–354 (1990/2001). https://doi.org/10.1007/3-540-46885-4_34.
6. National Institute of Standards and Technology, Hash Functions: Approved algorithms and security strengths (https://csrc.nist.gov/Projects/hash-functions).
7. Keith Conrad, Fermat Numbers and Their Factors (https://kconrad.math.uconn.edu/blurbs/ugradnumthy/fermat-numbers-and-factors.pdf); see also the classical Lucas congruence for prime divisors of Fermat numbers.
8. Lawrence C. Washington, *Introduction to Cyclotomic Fields*, 2nd ed., Graduate Texts in Mathematics 83 (Springer, 1997), for the splitting criterion in cyclotomic fields.
9. S. Chaturvedi, G. Marmo, N. Mukunda, R. Simon, and A. Zampini, “The Schwinger Representation of a Group: Concept and Applications,” *Reviews in Mathematical Physics*. https://doi.org/10.1142/S0129055X06002802.
10. Terry L. Meek and Leland C. Allen, “Configuration irregularities: deviations from the Madelung rule and inversion of orbital energy levels,” *Chemical Physics Letters* 362 (2002), 362–364. https://doi.org/10.1016/S0009-2614(02)00919-3.
11. “The Challenge of the So-Called Electron Configurations of the Transition Metals,” *Chemistry—A European Journal* (2006). https://doi.org/10.1002/chem.200500945.
12. Iulia Georgescu, “60 years of Landauer’s principle,” *Nature Reviews Physics* 3, 770 (2021). https://doi.org/10.1038/s42254-021-00400-8.

## Reproducibility notes

The ring-address results in this paper were checked against the files supplied with this conversation: `rule_based_ring.py`, `rule_based_512_verification.json`, `involution_cycle_counts.json`, `NEXUS_Record_136_Exact_Center_Offset_Rank_Law.md`, and the original `nested_rings (3).ipynb`. The independent checks in this session covered every word position at widths 1–10, a 512-bit rank/unrank test, the complete profiles for all 42 depths \(13\le D\le75\) with \(D\equiv0,1\pmod3\), and exact full-profile checks for the new subfamily at 18 depths through \(D=125\). A rank-check grid separately tested the three-zero and center-collision formulas on small parameter ranges. Those finite tests corroborate the derivation; the proof of the two-residue family rests on the rank arguments in Sections 4.1–4.3 rather than extrapolation from the tests.

Claims based on other reported project runs—such as large-scale SHA round inversions, the reduced-width hash graph, nuclear data analyses, and numerical relation finding—are marked as reported or conditional where this session did not independently rerun the underlying experiment. The source notebooks and raw data should accompany any external publication that relies on those results.


The DI-chain continuation is independently executable in `DI_chain_rollup_and_half_ring.ipynb`. `DI_chain_analysis.xlsx` contains a `Read Me` sheet, the 56-row rolling-stack audit, and the fixed-width field-packing comparison. The uploaded source workbook `two_bit_circle.xlsx` was not modified.