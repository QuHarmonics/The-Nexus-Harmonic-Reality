Computation of Z(5) Using a BBP-Extension Formula

The Riemann zeta function at 3:5, denoted Z(5), is an odd integer argument case without a
simple closed form in terms of it, unlike even values such as Z(2) = n2/6. However, BBP-like
extensions provide series representations that enable efficient numerical computation. One

such formula, conjectured by Simon Plouffe and based on exponential denominators, is:

((5) = 2455(1) — 215:35(2) + 1465:;(4),

where 3,, (7“) : 212:1 k,,(e,,,,,1). This series converges rapidly due to the exponential

decay, making it suitable for high—precision evaluation, akin to the original BBP formula for

T[.

To compute this, the following Python code was executed using the mpmath library for

arbitrary-precision arithmetic (set to 50 decimal places):

V —
:3 “Hap D’

python A' CoHapse Run

from mpmath import mp, mpf, exp, pi, nsum

mp.dps 50

def S(n, I):
return nsum(lambda k: mpf(1) / (k**n * (exp(pi * r * k) - 1)), [1, mp.i

$51 = 5(5, 1)
$52 = 8(5, 2)
554 = 5(5, 4)

zetaS = 24 * $51 - mpf(259)/10 * 552 + mpf(l)/10 * $54

print(zeta5)

1.0369284526143494977190190055778453892283151516229

The result is:

1.0369284526143494977190190055778453892283151516229

Computation of Z(5) Using a BBP-Extension Formula

The Riemann zeta function at 3:5, denoted Z(5), is an odd integer argument case without a
simple closed form in terms of it, unlike even values such as Z(2) = n2/6. However, BBP-like
extensions provide series representations that enable efficient numerical computation. One

such formula, conjectured by Simon Plouffe and based on exponential denominators, is:

((5) = 2455(1) — 215:35(2) + 1465:;(4),

where 3,, (7“) : 212:1 k,,(e,,,,,1). This series converges rapidly due to the exponential

decay, making it suitable for high—precision evaluation, akin to the original BBP formula for

T[.

To compute this, the following Python code was executed using the mpmath library for

arbitrary-precision arithmetic (set to 50 decimal places):

V —
:3 “Hap D’

python A' CoHapse Run

from mpmath import mp, mpf, exp, pi, nsum

mp.dps 50

def S(n, I):
return nsum(lambda k: mpf(1) / (k**n * (exp(pi * r * k) - 1)), [1, mp.i

$51 = 5(5, 1)
$52 = 8(5, 2)
554 = 5(5, 4)

zetaS = 24 * $51 - mpf(259)/10 * 552 + mpf(l)/10 * $54

print(zeta5)

1.0369284526143494977190190055778453892283151516229

The result is:

1.0369284526143494977190190055778453892283151516229

