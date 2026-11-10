# Route, latitude and azimuth: independent audit

Let n be word length, w the Hamming weight and z=w-n/2. For a literal sphere of radius n, use height Z=2z and transverse radius sqrt(n*n-4*z*z). Keep the original ring ordering.

## Partner action

With seam-centered angle theta=2*pi*((i+1/2)/2^n-1/2), the partner address 2^n-1-i sends theta to -theta. It is a reflection, not an angular half-turn. On nonpalindromes, z is unchanged. On palindromes, z changes sign. In Cartesian coordinates the actions are (X,Y,Z)->(X,-Y,Z) and (X,Y,Z)->(X,-Y,-Z), respectively. The second is not generally the full antipode.

## Lift latitude

For even core x and middle m, z_odd=z_x+m-1/2. For d=0 use E_m, for d=1 use G_m. Then z_even=s*(z_odd+(m-1/2)*(-1)^d), with s=-1 precisely when m=1 and the core x is palindromic. A source width L=2h has 2^(h-1) canonical palindrome cores and two sign-reflected outputs per such core. Thus a target width n=L+2 has 2^(n/2-1) sign-reflected steps.

## Weighted prefix counters

C_w(t) counts canonical n-bit a<t of weight w. T_w(t) counts the palindromic members of that set. For partners, H_w(t)=C_w(t)-T_w(t)+T_(n-w)(t). All three counters are evaluated by fixed-comparison-state mirrored-bit digit DP with a Hamming-weight accumulator.

Let M=2^(n-1), a*=largest canonical representative, and i=location(x) for a word of weight w. Its zero-based rank inside the latitude band, in original absolute ring order, is:

- i<M-1: C_w(x).
- i=M-1: C_w(2^n)-1[weight(a*)=w].
- i=M: C_w(2^n)-1[weight(a*)=w]+1[weight(P(a*))=w].
- i>M: binom(n,w)-H_w(P(x)+1).

For the right-side formula, all canonical representatives have occurred, followed by the partners of canonical words greater than P(x). The two center cases implement the actual center swap.

The full route is decoded using the stated E/G branch convention. Its latitude follows the update above; its absolute rank follows the canonical prefix count; its within-band rank follows these four cases. No full ring is built for scalar queries.

## Monotonicity

K is nondecreasing along descending canonical representatives, including within any fixed-weight subsequence. It is not generally monotone around the entire physical latitude band: reflection reverses traversal on the other face.

## Execution scope

Partner latitude and address rules passed all 32,764 words at n=2,...,14. The E/G latitude rule passed all 699,048 outputs over even source widths 2,...,18. Full route-to-original-rank and within-band ranks passed all 2,046 words at n=1,...,10. Scalar 32- and 64-bit coordinate queries were also executed. This is an independent unsealed audit, not a replay of the unavailable /tmp/r3/sphere.py.
