# NEXUS — Inverting the Entire Contact: a Binary Collective-Interface Law

**Dean A. Kulik · QuHarmonics Research Group · ORCID 0009-0003-3128-8828**  
**5 November 2026**

## Target

Find an interface-side property of the native binary ring under opposite-direction reading. No fitting to physical systems or interpreting readout values as interface definitions. The primitive is the native partner involution and the ring's prescribed opposite-address law.

## 1. Binary facing in native rings

For a binary word \(w\) of LEN \(m\), let \(J_m\) reverse its bit order and \(C_m(w)=w\oplus 1^m\) perform complement (NOT on every position). The native partner operator is

\[
P_m(w)=\begin{cases}
J_m(w),&J_m(w)\ne w,\\
C_m(w),&J_m(w)=w.
\end{cases}
\]

Equivalently, using the single palindrome-selector bit \(s_m(w)=[J_m(w)=w]\),

\[
\boxed{P_m(w)=J_m(w)\oplus s_m(w)1^m.}
\]

When the selector is 0 the operation is reversal; when it is 1 the reversed word would be unchanged, so the branch flips every distinction. For all \(m\ge2\), \(P_m^2=I\) and \(P_m\) has no fixed points. The native ring \(R_m\) satisfies \(R_m[2^m-1-i]=P_m(R_m[i])\), so the opposite address holds the other face.

## 2. Whole contact at higher LEN

Let \(a,b,c\in\{0,1\}^n\). The composable path

\[
a\longrightarrow b\longrightarrow c
\]

is the LEN-\(4n\) contact \(W=a\,|\,b\,|\,b\,|\,c\). It is a legitimate contact because the two internal faces are literally the same, \(b=b\).

Reversal of the *whole* word is

\[
J_{4n}(W)=J_n(c)\,|\,J_n(b)\,|\,J_n(b)\,|\,J_n(a).
\]

The palindrome-selector bit of this whole contact is **not** either lower contact's palindrome bit. It is

\[
\boxed{s_{4n}(W)=[a=J_n(c)]\land[b=J_n(b)].}
\]

Thus

\[
\boxed{P_{4n}(W)=\begin{cases}
J(c)|J(b)|J(b)|J(a),&s_{4n}(W)=0,\\
C(a)|C(b)|C(b)|C(c),&s_{4n}(W)=1.
\end{cases}}
\]

In both branches the exposed middle faces still match. **Whole-contact inversion preserves composability.** This is an exact identity for every \(n\), not a finite-test extrapolation.

## 3. Why separate inversion does not generally compile

The two lower-LEN contacts are \(U=a|b\) and \(V=b|c\). Inverting their faces separately and reversing their order gives \(P_{2n}(V)|P_{2n}(U)\). Their lower palindrome selectors are

\[
s_U=[a=J(b)],\qquad s_V=[b=J(c)].
\]

For the resulting lower contacts to compose, their common boundary must match. Direct substitution into \(P_{2n}\) shows that this happens **if and only if** \(s_U=s_V\):

- If both are non-palindromic, their two internal faces are both \(J(b)\).
- If both are palindromic, then \(a=c\), and their two internal faces are both \(C(a)\).
- If exactly one is palindromic, the two internal faces are a word and its complement, so they cannot match.

**Therefore the facing map at LEN \(4n\) does not factor through independent partner operations at LEN \(2n\).** The whole path has a collective condition that must be assessed at its own LEN.

Notice a stronger case: even if *neither* lower contact is palindromic, the **whole** contact can be. Choose \(b=J(b)\), \(a=J(c)\), but \(a\ne b\). The higher-level selector is 1 while both lower selectors are 0. The collective boundary has a feature absent from each constituent boundary examined separately.

## 4. Minimal illustrations, not the source of the result

For \(n=2\), write two-bit faces separated by a vertical bar.

**Separate inversions break contact:**

- Original: `00 | 00 | 00 | 01`  (\(00\to00\to01\))
- Whole-facing: `10 | 00 | 00 | 00` — still composable
- Partwise-facing: `10 | 00 | 11 | 11` — middle faces no longer fit

**Collective seam arises despite no lower seam:**

- Original: `00 | 11 | 11 | 00`
- Whole-facing: `11 | 00 | 00 | 11` — whole-word palindrome invokes complement
- Partwise-facing: `00 | 11 | 11 | 00` — each lower non-palindromic segment invokes reversal

This is an interface-side distinction between the property of the entire contact and properties of each piece.

## 5. All-LEN counts derived symbolically

Set \(N=2^n\) and \(r=2^{\lceil n/2\rceil}\), the number of palindromic \(n\)-bit words. There are \(N^3\) composable paths \(a\to b\to c\).

The collective palindrome condition independently chooses a palindromic \(b\) (\(r\) possibilities) and an arbitrary \(a\) (\(N\) possibilities), then fixes \(c=J(a)\). So there are \(rN\) collective seams.

Exactly one lower contact is palindromic in \(2N(N-1)\) paths. These and only these fail to compose after **separate** inversion.

Among paths with neither lower palindrome, an additional \(r(N-1)\) have a collective palindrome seam and therefore give different whole/partwise readings. Among paths with two lower palindromes, another \(N-r\) have an unpalindromic whole path and also differ. These three cases are disjoint. Thus the total count of whole-vs-partwise differences is

\[
\boxed{2N(N-1)+r(N-1)+(N-r)=2N^2-N+rN-2r.}
\]

These counts characterize **how** independent inversion fails, not merely how often.

## 6. Exact executable audit

Source: `NEXUS_Binary_Facing_Collective_Interface_Audit.py` (standard library only).

The audit checks (i) the native ring reflection law at widths 2–9; (ii) the whole-path identity against the actual native partner operator; (iii) closure of the whole inverted path; (iv) involution of the whole partner; (v) local-fit classification; (vi) all three all-width counting formulas by exhaustive traversal for \(n=2\) through \(6\).

| Face LEN \(n\) | Paths | Whole seams | Separate inversion breaks fit | Whole differs from separate |
|---:|---:|---:|---:|---:|
| 2 | 64 | 8 | 24 | 32 |
| 3 | 512 | 32 | 112 | 144 |
| 4 | 4,096 | 64 | 480 | 552 |
| 5 | 32,768 | 256 | 1,984 | 2,256 |
| 6 | 262,144 | 512 | 8,064 | 8,624 |

All executable assertions pass.

## 7. Ledger

- **STANDS:** Native facing is an involution without fixed points. Whole-contact facing preserves the equal middle boundary. The whole palindrome selector is \([a=J(c)]\land[b=J(b)]\). Local facing composes iff its two smaller palindrome flags agree. The all-width counts follow by elementary counting.
- **RUNS (retrospective independent audit):** These identities match the native ring and partner code over the listed finite widths, with all assertions passing. No new presealed physical prediction is claimed.
- **OPEN:** Whether the two facing directions realize the proposed interface-versus-implementation dual in physical systems. The binary theorem determines how the dual contact is constructed, not which material realizes it. Also open is an all-domain theorem that the ring operations exhaust physical interfaces.

**Operational conclusion:** A collective contact can have a facing/closure operation that cannot be obtained by independently facing its constituents. The new requirement is already a binary property of the higher-LEN ring, not a fitted value or an additional material object.
