# §135 — Alternate Routes in the Nested-Ring Address

**Subject:** the radial profile family \(q_D=100\,1^{D-5}00\), exact alternate locations, and the current reachability law.  
**Source construction:** the supplied `partner(x)` / `grow(L)` ring, including the center-pair twist.  
**Method:** exact rational addresses, direct `word_at` reading, half-open slice intervals, and retention of every surviving location component.

## 135.1 Held object: one address, all rings

For ring length \(L\), the bit tape has \(N_L=L2^L\) slices. At normalized clockwise angle \(u\in[0,1)\), its read is

\[
b_L(u)=R_L[\lfloor 2^L u\rfloor]\!\left[\left\lfloor L\{2^L u\}\right\rfloor\right].
\]

The first coordinate selects the word in `grow(L)`; the second selects the bit within that word. The same \(u\) supplies both coordinates at every LEN. No ring needs to be materialized: `word_at` recovers a word directly from its address.

For a finite radial profile \(p=p_1\cdots p_D\), retain its complete location set

\[
A_p=\bigcap_{L=1}^{D}\{u:b_L(u)=p_L\}.
\]

This set is a finite union of exact, half-open rational intervals. Its components are all part of the route; their count, total measure, or a single selected point is not a substitute for the set.

## 135.2 Candidate family and the local/global distinction

For \(D\ge 8\), define

\[
q_D=100\,1^{D-5}00.
\]

The center-word theorem gives a local exclusion: within the declared depth-\(D\) center cell

\[
J_D=[1/2,\,1/2+2^{-D}),
\]

the final `00` cannot occur. That does **not** imply \(A_{q_D}=\varnothing\). The same profile may be realized at other angles.

Exact, branch-specific intersection of every required bit region gives the following checked global witnesses:

- Every \(D=8,\ldots,40\) has a verified rational witness for \(q_D\), using one of the certificate routes below.
- For \(D\equiv0,1\pmod3\), \(13\le D\le75\), one uniform address law succeeds at every tested depth: 42/42 runs.
- These results establish global reachability only for the stated finite ranges. They do not yet prove reachability for every \(D\ge8\).

The candidate sets are pairwise disjoint. If \(E>D\), then at position \(D-1\), \(q_D\) has `0`, while \(q_E\) still has `1`. A single angle therefore cannot witness two different members of this family:

\[
A_{q_D}\cap A_{q_E}=\varnothing\qquad(D\ne E).
\]

The address remains common across rings for each profile, but this candidate family uses different address regions at different depths.

## 135.3 Uniform witness law for residues 0 and 1 modulo 3

For \(D\ge13\), \(D\equiv0,1\pmod3\), the checked address is

\[
\boxed{
 u_D=\frac12+2^{-\left(\lfloor2D/3\rfloor+1\right)}+\frac23\,2^{-(D-1)}.
}
\]

Let \(j_L=\lfloor L2^L u_D\rfloor\) be the selected slice in ring \(L\). Define the common slice intersection

\[
K_D=\bigcap_{L=1}^{D}
\left[\frac{j_L}{L2^L},\frac{j_L+1}{L2^L}\right).
\]

Whenever \(K_D\) has positive width, every \(u\in K_D\) reads the same slice at every ring and therefore has the same profile as \(u_D\). The certificate checks the profile, both sides of the intersection, and positive width. The executable audit reports all 42 required cases through \(D=75\) as `RUNS`.

The address has three coupled contributions: the seam baseline \(1/2\), an isolated dyadic displacement at \(p=\lfloor2D/3\rfloor+1\), and a tail with fractional phase \(2/3\). Under doubling, the nontrivial period-two orbit \(\{1/3,2/3\}\) alternates the tail phase. The isolated bit places the route at the required interior depth; the tail aligns the final rings with their zero positions.

For \(D=3m+1\), the tail-word audit reports these exact zero-index sets:

\[
Z(R_{D-1})=\left\{\left\lfloor\frac{3m-1}{2}\right\rfloor,2m\right\},
\quad
Z(R_D)=\left\{m,\left\lfloor\frac{3m}{2}\right\rfloor,2m+1\right\}.
\]

The address lands at index \(2m\) in ring \(D-1\) and index \(m\) in ring \(D\). For \(D=3m\), the checked sets are

\[
Z(R_{D-1})=\left\{\left\lfloor\frac{3m-2}{2}\right\rfloor,2m-1\right\},
\quad
Z(R_D)=\left\{m,\left\lfloor\frac{3m-1}{2}\right\rfloor,2m\right\},
\]

and the address lands at indices \(2m-1\) and \(m\), respectively. The scripts verify these identities for the tested range \(13\le D\le75\); a general proof from the representative-order formula remains an explicit proof obligation.

## 135.4 Residue class 2: several route types, no uniform law yet

For \(D\equiv2\pmod3\), no all-depth formula has been established. The certificate still verifies one rational witness at every \(D=8,\ldots,40\), using one of three routes:

- `BIT`: seam baseline plus an isolated bit and phase \(1/3\) or \(2/3\);
- `J2`: a selected integer offset followed by the period-two tail;
- `ATOM`: a midpoint taken from an exactly computed surviving interval component for the target profile.

Examples in the run log include \(D=14\) with an isolated-bit route, \(D=20\) and \(D=23\) with `J2` routes, and smaller depths whose certificate uses an exact interval component. These are different routes to the same requested readout; the certificate deliberately does not collapse them into a single mechanism.

The unresolved task is to derive a uniform witness construction for this residue class, including the cases where a one-isolated-bit address fails and two address bits are needed.

## 135.5 Center-seam obstruction and the role of the twist

The obstruction audit checks the closed forms for words at ring positions \(M+j\), \(M=2^{L-1}\), \(j=0,1,2,3\), for \(L=6\) and \(7\le L\le40\). It also checks that no component of \(A_{q_D}\) enters the neighborhood

\[
\left(\frac12-2^{-(D-2)},\frac12+2^{-(D-2)}\right)
\]

for \(D=8,\ldots,22\). The uniform law's successful addresses sit outside that tested seam neighborhood; the escape is an alternate location, not a relaxation of the center-cell exclusion.

The center twist is structural, not decorative: it changes the words placed next to the seam and consequently changes which radial continuations are possible. The across-language comparison previously computed 924 profiles at depth 10 and 3,606 at depth 12 with the twist, versus 947 and 3,710 without it. The local center condition cannot be promoted to global nonexistence without checking all components of \(A_p\).

## 135.6 Evidence ledger

**RUNS**

- Exact reader checks a witness for every \(D=8,\ldots,40\).
- The uniform formula checks at 42/42 depths \(D\equiv0,1\pmod3\), \(13\le D\le75\).
- The common interval \(K_D\) is constructed from the actual half-open slice containing the witness at each LEN.
- The center-neighborhood obstruction is checked for \(D=8,\ldots,22\).
- Tail-word zero-index sets are checked for \(D\equiv0,1\pmod3\), \(13\le D\le75\).

**DERIVED, with the scope stated**

- The candidate sets \(A_{q_D}\) are pairwise disjoint because their finite profiles disagree at an earlier coordinate.
- The uniform witness formula, when its tail-word identities and all intermediate `1` reads are proved for arbitrary \(D\), yields a positive-width global witness interval for those residue classes.
- The center-cell exclusion and global reachability are compatible because they concern different location sets.

**OPEN**

1. Prove the tail-word zero sets as identities in \(m\) from the closed form of the representative order, instead of relying on checks through \(D=75\).
2. Prove that every intermediate ring from \(\lfloor2D/3\rfloor+1\) through \(D-2\) reads `1` at \(u_D\), for arbitrary \(D\equiv0,1\pmod3\).
3. Derive one constructive route family for all \(D\equiv2\pmod3\).
4. Keep all alternative interval components in the route ledger; never replace a full location set by its nearest-to-seam component, its measure, or a single witness.

## 135.7 Interpretation boundary

This section establishes a computationally certified family of alternate routes and a uniform address law on two residue classes over the stated tested range. It does not yet establish the all-depth theorem for all three residue classes. The result is a location law inside the supplied nested-ring construction, not by itself a claim about physical geometry outside that construction.

**Artifacts:** `Kd_run_log.txt`, `Kd_witness_bundle.zip` (including `witness_Kd.py`, `Kd_law.py`, `Kd_certificate.py`, `Kd_certificate.json`, `obstruction_check.py`, `tailwords_check.py`, and the route-specific probes).
