# 357 Unfold Report

## 1. Definition

Use the phase map

$$
\phi(3)=-1,\qquad \phi(5)=0,\qquad \phi(7)=+1.
$$

A 357-word $a_n a_{n-1}\dots a_0$ decodes to an integer by

$$
V(a_n\dots a_0)=\sum_{k=0}^n \phi(a_k)3^k
$$

with the rightmost symbol at the $3^0$ place.

Equivalently,

$$
\phi(a)=\frac{a-5}2,\qquad a\in\{3,5,7\}.
$$

So every integer is a stacked triadic tension word over the primitive packet $\{3,5,7\}$.

## 2. Canonical 357 table for 0 through 100

| n | 357 |
|---:|:---|
| 0 | `5` |
| 1 | `7` |
| 2 | `73` |
| 3 | `75` |
| 4 | `77` |
| 5 | `733` |
| 6 | `735` |
| 7 | `737` |
| 8 | `753` |
| 9 | `755` |
| 10 | `757` |
| 11 | `773` |
| 12 | `775` |
| 13 | `777` |
| 14 | `7333` |
| 15 | `7335` |
| 16 | `7337` |
| 17 | `7353` |
| 18 | `7355` |
| 19 | `7357` |
| 20 | `7373` |
| 21 | `7375` |
| 22 | `7377` |
| 23 | `7533` |
| 24 | `7535` |
| 25 | `7537` |
| 26 | `7553` |
| 27 | `7555` |
| 28 | `7557` |
| 29 | `7573` |
| 30 | `7575` |
| 31 | `7577` |
| 32 | `7733` |
| 33 | `7735` |
| 34 | `7737` |
| 35 | `7753` |
| 36 | `7755` |
| 37 | `7757` |
| 38 | `7773` |
| 39 | `7775` |
| 40 | `7777` |
| 41 | `73333` |
| 42 | `73335` |
| 43 | `73337` |
| 44 | `73353` |
| 45 | `73355` |
| 46 | `73357` |
| 47 | `73373` |
| 48 | `73375` |
| 49 | `73377` |
| 50 | `73533` |
| 51 | `73535` |
| 52 | `73537` |
| 53 | `73553` |
| 54 | `73555` |
| 55 | `73557` |
| 56 | `73573` |
| 57 | `73575` |
| 58 | `73577` |
| 59 | `73733` |
| 60 | `73735` |
| 61 | `73737` |
| 62 | `73753` |
| 63 | `73755` |
| 64 | `73757` |
| 65 | `73773` |
| 66 | `73775` |
| 67 | `73777` |
| 68 | `75333` |
| 69 | `75335` |
| 70 | `75337` |
| 71 | `75353` |
| 72 | `75355` |
| 73 | `75357` |
| 74 | `75373` |
| 75 | `75375` |
| 76 | `75377` |
| 77 | `75533` |
| 78 | `75535` |
| 79 | `75537` |
| 80 | `75553` |
| 81 | `75555` |
| 82 | `75557` |
| 83 | `75573` |
| 84 | `75575` |
| 85 | `75577` |
| 86 | `75733` |
| 87 | `75735` |
| 88 | `75737` |
| 89 | `75753` |
| 90 | `75755` |
| 91 | `75757` |
| 92 | `75773` |
| 93 | `75775` |
| 94 | `75777` |
| 95 | `77333` |
| 96 | `77335` |
| 97 | `77337` |
| 98 | `77353` |
| 99 | `77355` |
| 100 | `77357` |

## 3. Exact local addition law

Interpret each symbol as a digit in $\{-1,0,+1\}$.

For symbols $a,b$ and incoming carry $c$ define

$$
s=\phi(a)+\phi(b)+\phi(c).
$$

Then reduce $s$ by writing

$$
s=d+3c',
$$

where $d,c'\in\{-1,0,+1\}$.

The exact reduction table is:

| raw sum $s$ | result digit $d$ | result symbol | next carry $c'$ | carry symbol |
|---:|---:|:---:|---:|:---:|
| -3 | 0 | 5 | -1 | 3 |
| -2 | +1 | 7 | -1 | 3 |
| -1 | -1 | 3 | 0 | 5 |
| 0 | 0 | 5 | 0 | 5 |
| +1 | +1 | 7 | 0 | 5 |
| +2 | -1 | 3 | +1 | 7 |
| +3 | 0 | 5 | +1 | 7 |

So, in pure 357 notation, the carry stays inside the same ontology.

### Single-digit addition table

| + | 3 | 5 | 7 |
|:--:|:--:|:--:|:--:|
| 3 | digit 7, carry 3 | digit 3, carry 5 | digit 5, carry 5 |
| 5 | digit 3, carry 5 | digit 5, carry 5 | digit 7, carry 5 |
| 7 | digit 5, carry 5 | digit 7, carry 5 | digit 3, carry 7 |

Example:
`77 + 77 = 753`, so $4+4=8$.

## 4. Exact multiplication law

Single-symbol products are just products in $\{-1,0,+1\}$:

| × | 3 | 5 | 7 |
|:--:|:--:|:--:|:--:|
| 3 | 7 | 5 | 3 |
| 5 | 5 | 5 | 5 |
| 7 | 3 | 5 | 7 |

Meaning:

- `3×3 = 7` because $(-1)(-1)=+1$
- `3×7 = 3` because $(-1)(+1)=-1$
- `7×7 = 7` because $(+1)(+1)=+1$
- any factor `5` kills the place because $0$ annihilates.

For full multiplication, use schoolbook convolution over shifted rows, then normalize each column with the addition carry law above.

Example:
`73 × 75 = 735`, so $2\times 3=6$.

## 5. First 100 primes in 357 notation

| # | prime | 357 | len | suffix2 |
|---:|---:|:---|---:|:---|
| 1 | 2 | `73` | 2 | `73` |
| 2 | 3 | `75` | 2 | `75` |
| 3 | 5 | `733` | 3 | `33` |
| 4 | 7 | `737` | 3 | `37` |
| 5 | 11 | `773` | 3 | `73` |
| 6 | 13 | `777` | 3 | `77` |
| 7 | 17 | `7353` | 4 | `53` |
| 8 | 19 | `7357` | 4 | `57` |
| 9 | 23 | `7533` | 4 | `33` |
| 10 | 29 | `7573` | 4 | `73` |
| 11 | 31 | `7577` | 4 | `77` |
| 12 | 37 | `7757` | 4 | `57` |
| 13 | 41 | `73333` | 5 | `33` |
| 14 | 43 | `73337` | 5 | `37` |
| 15 | 47 | `73373` | 5 | `73` |
| 16 | 53 | `73553` | 5 | `53` |
| 17 | 59 | `73733` | 5 | `33` |
| 18 | 61 | `73737` | 5 | `37` |
| 19 | 67 | `73777` | 5 | `77` |
| 20 | 71 | `75353` | 5 | `53` |
| 21 | 73 | `75357` | 5 | `57` |
| 22 | 79 | `75537` | 5 | `37` |
| 23 | 83 | `75573` | 5 | `73` |
| 24 | 89 | `75753` | 5 | `53` |
| 25 | 97 | `77337` | 5 | `37` |
| 26 | 101 | `77373` | 5 | `73` |
| 27 | 103 | `77377` | 5 | `77` |
| 28 | 107 | `77553` | 5 | `53` |
| 29 | 109 | `77557` | 5 | `57` |
| 30 | 113 | `77733` | 5 | `33` |
| 31 | 127 | `733357` | 6 | `57` |
| 32 | 131 | `733533` | 6 | `33` |
| 33 | 137 | `733573` | 6 | `73` |
| 34 | 139 | `733577` | 6 | `77` |
| 35 | 149 | `735333` | 6 | `33` |
| 36 | 151 | `735337` | 6 | `37` |
| 37 | 157 | `735377` | 6 | `77` |
| 38 | 163 | `735557` | 6 | `57` |
| 39 | 167 | `735733` | 6 | `33` |
| 40 | 173 | `735773` | 6 | `73` |
| 41 | 179 | `737353` | 6 | `53` |
| 42 | 181 | `737357` | 6 | `57` |
| 43 | 191 | `737573` | 6 | `73` |
| 44 | 193 | `737577` | 6 | `77` |
| 45 | 197 | `737753` | 6 | `53` |
| 46 | 199 | `737757` | 6 | `57` |
| 47 | 211 | `753377` | 6 | `77` |
| 48 | 223 | `753737` | 6 | `37` |
| 49 | 227 | `753773` | 6 | `73` |
| 50 | 229 | `753777` | 6 | `77` |
| 51 | 233 | `755353` | 6 | `53` |
| 52 | 239 | `755533` | 6 | `33` |
| 53 | 241 | `755537` | 6 | `37` |
| 54 | 251 | `755753` | 6 | `53` |
| 55 | 257 | `757333` | 6 | `33` |
| 56 | 263 | `757373` | 6 | `73` |
| 57 | 269 | `757553` | 6 | `53` |
| 58 | 271 | `757557` | 6 | `57` |
| 59 | 277 | `757737` | 6 | `37` |
| 60 | 281 | `757773` | 6 | `73` |
| 61 | 283 | `757777` | 6 | `77` |
| 62 | 293 | `773533` | 6 | `33` |
| 63 | 307 | `773757` | 6 | `57` |
| 64 | 311 | `775333` | 6 | `33` |
| 65 | 313 | `775337` | 6 | `37` |
| 66 | 317 | `775373` | 6 | `73` |
| 67 | 331 | `775737` | 6 | `37` |
| 68 | 337 | `775777` | 6 | `77` |
| 69 | 347 | `777533` | 6 | `33` |
| 70 | 349 | `777537` | 6 | `37` |
| 71 | 353 | `777573` | 6 | `73` |
| 72 | 359 | `777753` | 6 | `53` |
| 73 | 367 | `7333337` | 7 | `37` |
| 74 | 373 | `7333377` | 7 | `77` |
| 75 | 379 | `7333557` | 7 | `57` |
| 76 | 383 | `7333733` | 7 | `33` |
| 77 | 389 | `7333773` | 7 | `73` |
| 78 | 397 | `7335357` | 7 | `57` |
| 79 | 401 | `7335533` | 7 | `33` |
| 80 | 409 | `7335577` | 7 | `77` |
| 81 | 419 | `7337333` | 7 | `33` |
| 82 | 421 | `7337337` | 7 | `37` |
| 83 | 431 | `7337553` | 7 | `53` |
| 84 | 433 | `7337557` | 7 | `57` |
| 85 | 439 | `7337737` | 7 | `37` |
| 86 | 443 | `7337773` | 7 | `73` |
| 87 | 449 | `7353353` | 7 | `53` |
| 88 | 457 | `7353537` | 7 | `37` |
| 89 | 461 | `7353573` | 7 | `73` |
| 90 | 463 | `7353577` | 7 | `77` |
| 91 | 467 | `7353753` | 7 | `53` |
| 92 | 479 | `7355373` | 7 | `73` |
| 93 | 487 | `7355557` | 7 | `57` |
| 94 | 491 | `7355733` | 7 | `33` |
| 95 | 499 | `7355777` | 7 | `77` |
| 96 | 503 | `7357353` | 7 | `53` |
| 97 | 509 | `7357533` | 7 | `33` |
| 98 | 521 | `7357753` | 7 | `53` |
| 99 | 523 | `7357757` | 7 | `57` |
| 100 | 541 | `7373557` | 7 | `57` |

### Prime motifs from the first 100 primes

1. Every positive prime starts with `7`. That is not deep by itself; it is just the canonical leading sign digit for positive numbers.

2. Every prime greater than 3 ends with `3` or `7`, never `5`. This is exact, because the least-significant 357 digit is the residue modulo 3:
   - ending `3` means residue $-1 \equiv 2 \pmod 3$
   - ending `7` means residue $+1 \equiv 1 \pmod 3$
   - ending `5` would mean divisibility by 3.

3. The two-symbol suffixes for primes greater than 3 are exactly the six nonzero, non-multiple-of-3 residues mod 9:

`33`→5, `37`→7, `53`→8, `57`→1, `73`→2, `75`→3, `77`→4

Observed counts in the first 100 primes:
{'33': 18, '37': 16, '73': 17, '77': 15, '53': 16, '57': 16}

This is a real arithmetic constraint, but it is a restatement of mod-9 filtering, not yet a new prime law.

4. Twin-prime pairs often differ only in the last symbol:

| pair | 357 words |
|:---|:---|
| 3,5 | `75` / `733` |
| 5,7 | `733` / `737` |
| 11,13 | `773` / `777` |
| 17,19 | `7353` / `7357` |
| 29,31 | `7573` / `7577` |
| 41,43 | `73333` / `73337` |
| 59,61 | `73733` / `73737` |
| 71,73 | `75353` / `75357` |
| 101,103 | `77373` / `77377` |
| 107,109 | `77553` / `77557` |
| 137,139 | `733573` / `733577` |
| 149,151 | `735333` / `735337` |
| 179,181 | `737353` / `737357` |
| 191,193 | `737573` / `737577` |
| 197,199 | `737753` / `737757` |
| 227,229 | `753773` / `753777` |
| 239,241 | `755533` / `755537` |
| 269,271 | `757553` / `757557` |
| 281,283 | `757773` / `757777` |
| 311,313 | `775333` / `775337` |

That happens because adding 2 often toggles the least-significant balanced digit from `3` to `7` without forcing a longer carry.

## 6. First chunk of $\pi$ in 357 notation

Using the same digit set for real numbers,

$$
x=\sum_{k=-\infty}^n \phi(a_k)3^k,
$$

the first 180 fractional 357 digits of $\pi$ are:

```text
75.577377735553 577377573777 777553555537 333373535353 357337755755 773553755533 733735333377 337733357537 337375555757 753575737333 335575537755 357755757777 337773357575 557557553753 535775755355
```

Counts in the first 180 fractional digits:
- `3`: 55
- `5`: 63
- `7`: 62

Most common adjacent transitions:
[('55', 24), ('77', 23), ('57', 21), ('75', 21), ('33', 20), ('73', 18), ('37', 18), ('35', 17), ('53', 17)]

Longest run in this 180-digit chunk:
- symbol `7`
- length 6
- starting at fractional position 22

### What this suggests about the $\pi$ chunk

- It is not primitive in this basis; it is an infinite 357 tension word.
- Over the first 180 fractional digits the three states are already close to balanced.
- Local repeats such as `77`, `55`, `33`, and flips such as `73`, `37` all appear frequently.
- That is consistent with a nonrepeating triadic tension stream, but not yet evidence of deeper structure by itself.

## 7. Tight conclusion

The solid part is:

$$
\boxed{\text{All integers are canonically generated from the primitive triad }\{3,5,7\}.}
$$

$$
\boxed{\text{All reals become infinite 357 tension words in the same basis.}}
$$

The open part is:

$$
\boxed{\text{Whether this basis reveals genuinely new invariants for primes, }\pi,\text{ or physics.}}
$$
