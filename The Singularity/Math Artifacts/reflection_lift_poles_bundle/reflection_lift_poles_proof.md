# Reflection, lift, poles and radius

Use r=n, z=w-n/2, physical height Z=2z, rho=sqrt(n^2-4z^2), and theta=2*pi*((i+1/2)/2^n-1/2). For palindromes the complete transform is (n,w,z,i,theta,rho)->(n,n-w,-z,2^n-1-i,-theta,rho). In Cartesian coordinates it is (X,Y,Z)->(X,-Y,-Z). On nonpalindromes the transform is (X,-Y,Z). The palindrome transform is not generally the full antipode; at the two poles it is.

Let p(x)=1 when x is a palindrome and 0 otherwise. For insertion I_m and the raw equal-end frame T_m(x)=mxm,

P_(L+1) I_m(x)=I_(m XOR p(x))(P_L(x)),
P_(L+2) T_m(x)=T_(m XOR p(x))(P_L(x)).

For the mixed-end frame G_m(x)=0 P_L^m(x) 1,

P_(L+2)G_m(x)=1 J_L(P_L^m(x)) 0.

These identities are checked before discarding the partner side through canonicalization.

For canonical even core x, middle m and d selecting E or G,

z_odd=z_x+m-1/2,
z_even=s*(z_odd+(m-1/2)*(-1)^d),
s=-1 iff x is palindromic and m=1.

E_m outputs are palindromic exactly when x is; G_m outputs are never palindromic. Thus the reflection of the final output must be distinguished from the sign change used inside its construction.

Every weight band has binom(n,w) words. Its palindrome count is binom(n/2,w/2) for even n and even w, zero for even n and odd w, and binom(floor(n/2),floor(w/2)) for odd n. Nonpalindromes stay in the same weight band under P; palindromes go to weight n-w. At the equator these destinations coincide.

For a canonical south-pole core 0^L, the four target outputs have (m,d;word;twice-z) equal to:
(0,0;0^(L+2);-(L+2)),
(0,1;0^(L+1)1;-L),
(1,0;0 1^L 0;L-2),
(1,1;0 1^(L+1);L).

The physical radius is L+2 for all four; their normalized heights tend to -1,-1,+1,+1 as L grows. Only E0 is exactly the south pole at finite L; the other branches are distinct near-pole states.

The executed audit covered every word at widths 2 through 20, every E/G output from even source widths 2 through 18, wide pole queries through source width 4096, and full 255-step outward route traces of the empty and Ovaltine digests. Radius increases by one per extension, not per final side flip. This radius law is the chosen length coordinate, not a derived physical growth law.
