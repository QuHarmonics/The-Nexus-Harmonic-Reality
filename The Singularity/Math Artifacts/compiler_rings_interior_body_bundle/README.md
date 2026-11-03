# Compiler Rings — Interior Body Rank Audit

This bundle records the next stroke after the even-body seam result. It extends the palindrome-only address equation to an all-word prefix-rank identity and connects the entire left-face body to popcount after rank inversion.

## Main identities

For reversal J, partner P, comparator prefix Δ, and signed palindrome correction Π:

\[
\operatorname{rank}_n(p)=\#\{x<p:x<P_n(x)\}
=\frac{p+\Delta_n(p)+\Pi_n(p)}2.
\]

If t_n(p) counts palindromes strictly below p and M_pal=2^ceil(n/2), then Π_n(p)=min(t_n(p), M_pal−t_n(p)). For p<N, writing h=floor(n/2), H=2^h, U=floor(p/H), and B=p mod H,

\[
t_n(p)=U+\mathbf1\{\operatorname{rev}_h(U\gg(n\bmod2))<B\}.
\]

For canonical palindromes only, Π_n(p)=u (the half-word integer), recovering the previously established address formula. The physical center swap remains a separate operation.

## Audit coverage

- 2,097,148 thresholds checked exhaustively at widths 2–20.
- 4,090 palindromes and 2,045 canonical-palindrome special cases.
- 88,408 rectangle-counter argument pairs.
- 32,777 scalar Δ checks against direct comparator prefix sums.
- 4,160 rank/select inverse checks.
- 108 wide scalar rank comparisons against the independent mirrored-pair rank DP, through 1,024 bits.
- Terminal p=2^n endpoints and physical address uniqueness are explicit checks.

All final artifact hashes and the history of corrected test attempts are in `interior_body_seals.json`. The first failure was a too-strong validation assertion for noncanonical palindromes; the general rank identity then passed all exhaustive direct-count checks. A later syntax error was caught before any audit ran. These are documented transparently.

## Status

**SEALED, RUNS:** finite discrete rank/select description of the body.

**OPEN:** continuum smoothness or coarse-grained profile, compact even-degree Δ spectrum, profile-language regularity, and full A(q_D). Physical spin/sphere interpretation remains PULL. SHA route-code investigation remains parked.
