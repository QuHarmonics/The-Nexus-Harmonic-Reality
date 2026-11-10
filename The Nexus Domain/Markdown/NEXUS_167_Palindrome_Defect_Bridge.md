# NEXUS §167 — The Palindrome Defect Determines the Upstairs Group at Every Width

Dean A. Kulik — QuHarmonics Research Group — ORCID 0009-0003-3128-8828

## Domain and operators

The fixed domain is X_n = {0,1}^n. Define J as bit reversal, C as complementation, tau as left shift with complemented departing bit, and P(x)=J(x) if x is not a palindrome, otherwise C(x). Then tau^n=C, J tau J=tau^{-1}, and J commutes with C. The native partner P is a fixed-point-free involution.

Define the palindrome-locus flip H(x)=C(x) when J(x)=x and H(x)=x otherwise. Then **P=HJ**, and H commutes with J. This is the exact missing correction in the upstairs lift. On the quotient V_n=X_n/{x~Cx}, H is identity, so P and J induce the same reflection; tau induces rotation. For n>=3 the quotient image of G_n=<tau,P> is D_n, of order 2n.

## The relative rotation/reflection defect

Set Q=P tau P tau (composition read right-to-left). Algebraically,

Q = H tau^{-1} H tau.

Let p([x]) equal 1 exactly when x is palindromic. This is well defined on V_n. Then

**Q(x)=C(x) if q([x])=1, and Q(x)=x otherwise, where q([x])=p([x]) XOR p([tau(x)]).**

Thus Q is precisely the circumferential binary difference of a fixed palindrome-location indicator. Q preserves every quotient location and only flips its hidden face bit. Its return is itself. The n phase translates q_t([x])=q([tau^t(x)]) and the constant-1 mask (global C) generate the full kernel of G_n->D_n: these are the lifted defects of the standard dihedral presentation r^n=s^2=(sr)^2=I. Since every kernel element acts as an independent complement flip on quotient fibres, the kernel is an elementary abelian 2-group.

The reflection action on q only reindexes the n rotation translates because p is reflection-invariant, so no further generators arise.

## All-width rank theorem

**Theorem.** For n>=5, G_n fits into the exact sequence

1 -> (Z/2Z)^n -> G_n -> D_n -> 1,

and therefore **|G_n|=2n*2^n**.

*Proof.* Every q_t is the XOR of consecutive phase shifts of p. Hence XOR_t q_t = 0 and the span has rank at most n-1. Restrict to the principal n-cycle of quotient states [tau^j(0^n)]. On that cycle p=1 at exactly phase 0; the n q_t are the incidence vectors of an n-cycle. They span the even-parity subspace, rank n-1. Thus the full q-span has rank exactly n-1.

The constant-1 global complement mask is independent for odd n because its restriction to the principal n-cycle has odd parity, whereas every q_t has even parity. For even n>=6, the n shifts of the palindrome set cover at most n*2^(n/2-1) of the 2^(n-1) quotient positions. Since n<2^(n/2) for even n>=6, some quotient position encounters no palindrome at any phase; there all q_t are zero while the global complement mask is one. Thus C adds an independent generator, giving total kernel rank n. The quotient is D_n of order 2n, giving the stated group order. QED.

Exceptions: n=3 also has kernel rank 3 and |G_3|=48. At n=4 the constant mask is already q_0 XOR q_2; kernel rank 3 and |G_4|=64. At n=2, P=C=tau^2 and |G_2|=4.

## Verification and scope

Independent 39-check execution of the attached §166 notebook: 38 passed, one declared sealed miss at 7.5 (P_3 is affine), no unexpected failures. The §167 standard-library verifier checks the palindrome defect, inverse paths, involution, and binary rank for n=3..13. Held-out widths 11, 12, 13 were sealed before execution; kernel ranks 11,12,13 RUN as predicted. The corresponding group orders 45056,98304,212992 are deduced from the proved exact sequence, not independently obtained by group enumeration at those widths. The all-width statement is mathematical, not extrapolation from samples. The 64-bit value |G_64|=2^71 and the 128-bit value |G_128|=2^136 follow without enumeration.

**STANDS:** Standard group-presentation and binary incidence-rank facts used in the proof. **RUNS:** The newly derived all-width kernel and group-order law, the palindrome-boundary defect, 38 of 39 revised companion checks (one logged sealed miss), direct group orders at n=3..7, and binary mask-rank checks n=3..13. **OPEN:** Any identification of this operator group with specific physical interaction dynamics; the relation to the full native successor is not conjugacy.
