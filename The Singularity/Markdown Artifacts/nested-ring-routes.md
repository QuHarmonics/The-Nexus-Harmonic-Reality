# Nested partner ring — routes and laws (session of 19–20 Oct 2026)

Paper: "Where Yes and No Become Maybe" (Where_Yes_and_No_Become_Maybe.docx). Code: nested_ring_routes.ipynb (47 RUNS, 0 MISS, 1 DEAD END). Companion: nested_ring_beyond_2bit.xlsx (rings 2–4 in the two_bit_circle layout, DI-chain sheet for rings 1–10).

Held state: even width 2n, word x = f||g plotted at (f/2^n, J(g)/2^n). Reps = triangle above the diagonal + lower half of the diagonal; partner = mirror cell; palindromes go to the diagonal antipode. Square folded on its diagonal, diagonal folded at its midpoint.

Laws that RUN:
- Sheet: w_i(W+1) = 2^W s_i + w_(i+1)(W) = 2 w_i(W) + s_(i+W). G_0(W) = B_0(W+3). Byte = nib(i)||nib(i+4); half turn = nibble swap (the 8-bit cross pairs). 2-bit sheet reflects at every width; for L >= 3 reverse(T_L) is never a rotation.
- Antipode: R[N-1-i] = P(R[i]); tape twist only on palindromic words. Sheet reading = tape with non-palindromic words complemented (counting only at L = 2).
- Frame law: b m c is a rep iff (0,1); or (0,0) with m <= Jm; or (1,1) with m < Jm; never (1,0). reps(L) = 0.W(L-2).1 + 0.reps(L-2).0 + F(reps(L-2)).
- Density of reps at value t is 1 - t (exact block law). Angle u = t - t^2/2 + tent (1/2)min(f, 2^n - f) + back count. Apex = seam.
- Depth: Pr(depth >= t) = 4^-t, roots 3*2^(L-3), mean -> 1/3. Complement branch phi -> (1-phi)/2, attractor value 1/3 at angle 5/18.
- Address: rank = Q(f) + D_f(g) + [f<2^(n-1)][J(f)<g], Q(f) = f(2^n-1) - f(f-1)/2 + min(f,2^(n-1)); unrank by one isqrt + O(1) count per bit; O(L) steps.
- Radial reader's front half reads digits of 1 - sqrt(1 - 2u) (3891/3892).
- Merge: sum |x xor Px| = floor(L/2) 2^L + L 2^ceil(L/2); grey total at L = 2, -> 1/2; all-grey words = palindromes + anti-palindromes.
- Radial language R_17..R_20 = 109200, 216428, 429416, 852130; per-ring deficit falling (OPEN: growth rate).

DEAD END / withdrawn: "the rings are counting" (true only of the 2-bit sheet); the two-hole Law 3 candidate (uniform occupancy does not force two holes); S7 at L = 1.
PULL: Law 3 candidate — 1/2 - u = (1 - t)^2/2; apex where the price reaches zero; the last pair exchanges places there.
OPEN: radial-language growth rate; uniform witness family for the profile 1 0 0 1^(D-5) 0 0; which factor of the constant -1 is mass and which acceleration.
