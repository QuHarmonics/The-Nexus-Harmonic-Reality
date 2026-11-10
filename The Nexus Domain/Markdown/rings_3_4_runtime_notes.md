# R3 and R4: runtime reflection becomes conditional

Original fixed rings, with the center swap retained. R3 has eight 3-bit states and 24 serialized slots: 000,001,010,110,011,101,100,111. Its hex tape is 056767. R4 has sixteen 4-bit states and 64 serialized slots; hex tape 0123567DBE9AC48F.

Neither whole reversed tape is a cyclic rotation of its forward tape. This differs from the small R2 tape 27, whose reversal E4 is a phase rotation. It does not break the word-level inverse runtime.

## Exact correction

Let S_n be the flattened tape and Q_n mark every bit belonging to a palindromic word. Then reverse(S_n)=S_n XOR Q_n. This follows from the partner layout: nonpalindromic partner reversal returns the original bit, while a palindrome takes the complement branch. The masks are C3 at n=2, E381C7 at n=3, F0000F0000F0000F at n=4. Their one-bit counts are 4,12,16 respectively.

For arbitrary bit-reader phase j and length L, let B=n*2^n. Then CCW_j,L= CW_(B-1-j),L(S_n) XOR CW_(B-1-j),L(Q_n). All phases and lengths through two complete tape revolutions were checked: 1,152 comparisons for R3 and 8,192 for R4.

The mask is derived from palindrome positions in the fixed ring; it is not an externally fitted correction.

## Compiled runtimes

Each native framed n-bit word has exactly one successor T_n and predecessor. T_n^(2^n)=I, P_n^2=I, and P_n T_n P_n=T_n^(-1). Physical CCW reading reverses each internal word, so the viewed rule is J_n T_n^(-1) J_n.

The forward and inverse ANFs are degree one at R2, degree two at R3, degree three at R4. P is degree one at R2 and R3, degree two at R4. These are algebraic degrees of the chosen coordinate truth tables, not minimum gate counts.

Native R3 forward rule: T(a,b,c)=(a XOR b, a XOR b XOR c XOR ab, 1 XOR b XOR c XOR ab). One shared product ab supplies its quadratic part. The compiled Python module includes every forward/inverse equation for all three widths.

## Reader framing

Both frames at R2 are complete four-state cycles. At R3, frames zero and one are complete eight-state cycles; frame two sees only six distinct states and has ambiguous successors. At R4, frames zero and one are complete sixteen-state cycles; frames two and three see fourteen distinct states and have ambiguous successors. The native frame remains complete throughout.

Thus a larger ring retains a complete reversible runtime, while a shifted limited reader may lose state identity. There is no single raw phase shift replacing reflection at R3/R4; the exact palindrome-dependent reader correction supplies it.

This is a known-structure replay and extension, not a blind physical prediction or a claim that every byte is a compiler. The immutable audit source was hashed before execution and checked afterward. The standalone compiled-runtime module is a derived artifact and was checked separately on all states. Partner involution was also rechecked explicitly in the outer runner.
