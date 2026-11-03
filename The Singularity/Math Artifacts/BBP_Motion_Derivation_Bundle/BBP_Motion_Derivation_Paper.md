# Accumulation as Instruction
## The digit-emission formula derived from BBP lane motion

**Dean A. Kulik · QuHarmonics Research Group**  
**Technical manuscript · 13 October 2026**

## Abstract

The Bailey–Borwein–Plouffe (BBP) identity is usually presented as a way to evaluate a digit of π at a chosen position. This paper follows the local operation that makes each BBP lane work and retains that operation as state. A lane with denominator d(k,j) = 8k + j performs one base-16 long-division step: a quotient leaves as a crossing while a remainder persists. The weighted crossings on the current anti-diagonal form an integer C_n. The aggregate field then obeys the exact recurrence F_(n+1) = 16 F_n − C_n, and the next hexadecimal digit is the boundary correction C_n + floor(F_(n+1)) − 16 floor(F_n). This is a formula derived from the lane motion, not a table of previously emitted digits. The accumulated object is a live configuration of instructions—denominators, remainders, weights, and the coupled boundary state—not the historical output string. An executable recurrence produced 2,000 hexadecimal digits, all matching an independent high-precision π reference. A separate empty-field reader uses certified intervals to avoid evaluating unopened lanes term by term.

## The formula, at a glance

**Local lane motion**

`d_(k,j) = 8k + j`

`16 r_(k,j,m) = d_(k,j) q_(k,j,m) + r_(k,j,m+1)`

`q_(k,j,m) = floor(16 r_(k,j,m) / d_(k,j))`, and `r_(k,j,m+1) = 16 r_(k,j,m) mod d_(k,j)`.

**Weighted crossings at read position n**

`C_n = sum_(j in {1,4,5,6}) c_j sum_(k=0..n) q_(k,j,n-k)`

with weights `c_1 = 4`, `c_4 = -2`, `c_5 = -1`, `c_6 = -1`.

**Aggregate state transition**

`F_(n+1) = 16 F_n - C_n`

**Digit-emission formula**

`a_(n+1) = C_n + I_(n+1) - 16 I_n`, where `I_n = floor(F_n)`.

The transition does not consume old output digits. It consumes the current lane phases, sums the quotients that cross the read boundary, updates the aggregate state, and emits the digit determined by the change in its integer boundary.

## 1. The question: can the motion become its own formula?

The task is not merely to evaluate BBP independently for each requested digit. It is to take the operation through which BBP reveals a digit and write that operation as the state transition that reveals the next digit.

Each reciprocal term is a local process. On every base-16 step it produces a quotient and retains a remainder. The denominator and remainder determine what the lane can do next. At a read position, the active lanes make crossings together; the integer-weighted sum of those crossings couples to one aggregate boundary state. The digit is what remains when that relation is closed.

This view changes what is treated as accumulated. The output string may be recorded for the user, but it is not the machine's memory of how to continue. The continuing object is the field of live lane states and their update instructions.

## 2. BBP lanes as long-division instructions

The classical identity is

`pi = sum_(k>=0) 16^(-k) [4/(8k+1) - 2/(8k+4) - 1/(8k+5) - 1/(8k+6)]`.

Let `J = {1,4,5,6}` and let `c_j` be the four integer weights shown above. For lane `(k,j)`, define its denominator `d_(k,j) = 8k + j`. Its initial remainder is `r_(k,j,0) = 1 mod d_(k,j)`.

At phase `m`, Euclidean division gives

`16 r_(k,j,m) = d_(k,j) q_(k,j,m) + r_(k,j,m+1)`,

where

`q_(k,j,m) = floor(16 r_(k,j,m) / d_(k,j))`,  
`r_(k,j,m+1) = 16 r_(k,j,m) - d_(k,j) q_(k,j,m)`,

and `0 <= r_(k,j,m+1) < d_(k,j)`. Thus each quotient is one hexadecimal crossing of the reciprocal lane, and the remainder is the phase that survives the step. The transition is the same for every lane; the denominator and coefficient specify which orbit it follows and how its crossing contributes.

## 3. The aggregate field

At read position `n`, lane `(k,j)` has advanced `n-k` times if `k <= n`. Define the exact lane-family state

`S_j(n) = sum_(k=0..n) r_(k,j,n-k)/d_(k,j) + sum_(h>=1) 16^(-h)/(8(n+h)+j)`.

The first sum is the explicit field of opened lanes. The second is the mathematical continuation of lanes not yet opened. It defines the exact quantity; the executable empty-field reader does not evaluate this infinite continuation term by term, but encloses it with a geometric bound.

Combine the four families:

`F_n = sum_(j in J) c_j S_j(n)`.

For `k <= n`, the remainder recurrence ensures

`16^(n-k)/d_(k,j) = integer + r_(k,j,n-k)/d_(k,j)`.

Because every coefficient `c_j` is an integer, replacing each processed term by its current remainder changes the total only by an integer. The unprocessed terms are exactly the continuation sum. It follows that

`F_n = 16^n pi - integer`,

so `frac(F_n) = frac(16^n pi)`. At `n=0`, the term with denominator 1 contributes the integer 4 to π and has remainder zero after reduction. Hence `F_0 = pi - 4`, whose fractional part is `pi - 3`, the first hexadecimal fraction of π.

The field is therefore an exact, moving representative of the current fractional position. It is not a stored prefix of digits.

## 4. From the local division to the aggregate recurrence

For each family `j`, collect the quotients that leave on the anti-diagonal at position `n`:

`C_(j,n) = sum_(k=0..n) q_(k,j,n-k)`.

Then define the weighted crossing sum

`C_n = 4 C_(1,n) - 2 C_(4,n) - C_(5,n) - C_(6,n)`.

For every opened lane, the local identity states that multiplying its current remainder fraction by 16 gives the quotient crossing plus the next remainder fraction. For the continuation, multiplying by 16 moves its first term into the new layer `k=n+1` and shifts the remaining terms by one position. Therefore, family by family,

`16 S_j(n) = C_(j,n) + S_j(n+1)`.

Rearrange and combine the four families using the same weights:

`S_j(n+1) = 16 S_j(n) - C_(j,n)`

and

**`F_(n+1) = 16 F_n - C_n`.**

This is the aggregate motion law. The current diagonal of quotient crossings becomes one integer, and that integer advances the aggregate field. The complete earlier crossing history is not needed to perform the next update; the live remainders and their common transition rule regenerate the next diagonal.

## 5. Deriving the digit-emission formula

Let

`I_n = floor(F_n)` and `x_n = F_n - I_n`, with `0 <= x_n < 1`.

Because `frac(F_n) = frac(16^n pi)`, the next hexadecimal fractional digit is

`a_(n+1) = floor(16 x_n)`.

Apply the aggregate recurrence:

`F_(n+1) = 16(I_n + x_n) - C_n`.

Since `C_n` is an integer, taking floors gives

`I_(n+1) = 16 I_n + floor(16 x_n) - C_n`.

Replace `floor(16 x_n)` by `a_(n+1)` and rearrange:

## The motion-derived digit formula

**`a_(n+1) = C_n + I_(n+1) - 16 I_n`**

where `I_n = floor(F_n)` and

`C_n = sum_(j in J) c_j sum_(k=0..n) floor(16 r_(k,j,n-k)/(8k+j))`.

The term `I_(n+1) - 16 I_n` is the boundary correction. It resolves the carry relation between the weighted crossings and the integer boundary of the aggregate field. Their sum is the digit, an integer from 0 to 15. No previous digit appears on the right-hand side. The machine needs the current state and its next transition, not the historical string.

## 6. A worked trace

Let `Q_(j,n) = sum_(k=0..n) q_(k,j,n-k)`. Then `C_n = 4Q_(1,n) - 2Q_(4,n) - Q_(5,n) - Q_(6,n)`. The last column is obtained by adding the boundary correction `I_(n+1) - 16 I_n` to `C_n`.

| n | Q1 | Q4 | Q5 | Q6 | C_n | Boundary correction | Digit |
|---:|---:|---:|---:|---:|---:|---:|:---:|
| 0 | 0 | 4 | 3 | 2 | -13 | 15 | 2 |
| 1 | 1 | 1 | 4 | 11 | -13 | 17 | 4 |
| 2 | 12 | 5 | 6 | 12 | 20 | -17 | 3 |
| 3 | 22 | 17 | 26 | 25 | 3 | 12 | F |
| 4 | 11 | 26 | 15 | 37 | -60 | 66 | 6 |
| 5 | 37 | 26 | 25 | 28 | 43 | -33 | A |
| 6 | 38 | 27 | 48 | 52 | -2 | 10 | 8 |
| 7 | 32 | 55 | 46 | 60 | -88 | 96 | 8 |
| 8 | 48 | 45 | 38 | 56 | 8 | 0 | 8 |
| 9 | 58 | 48 | 66 | 62 | 8 | -3 | 5 |
| 10 | 49 | 65 | 46 | 65 | -45 | 55 | A |
| 11 | 89 | 60 | 44 | 65 | 127 | -124 | 3 |
| 12 | 29 | 79 | 79 | 76 | -197 | 197 | 0 |
| 13 | 107 | 81 | 70 | 105 | 91 | -83 | 8 |
| 14 | 69 | 84 | 63 | 77 | -32 | 45 | D |
| 15 | 90 | 85 | 138 | 90 | -38 | 41 | 3 |

The prefix emitted by these transitions is `243F6A8885A308D3`. This table is an audit view of one run; it is not a lookup table used by the generator.

## 7. Accumulation is instruction-state, not stored output

At each position the live lane field is represented by the denominator, remainder, coefficient and phase of every opened lane. The denominator fixes the local orbit; the remainder fixes the phase; the quotient is the crossing for this step. One new layer of four lanes can enter as the address advances. The existing lanes persist and continue their own long divisions.

The operation has three coupled parts:

1. **Persist and advance.** Each lane performs `16r = dq + r'`. The quotient leaves; the remainder persists.
2. **Accumulate crossings.** The weighted quotient crossings on the current anti-diagonal reduce to `C_n`.
3. **Emit from the boundary relation.** The aggregate state advances by `F_(n+1) = 16F_n - C_n`; the change in its integer boundary closes the digit formula.

“Accumulation is instruction-state” does not mean that nothing is stored or that storage is constant. The persistent-lane realization stores `4(n+1)` active lane states after opening layers 0 through n. It accumulates the instructions and phases that determine the next move, not the previously emitted digits as a substitute for those instructions. The live representation grows; what is avoided is recomputation of each past lane's modular power from scratch at every new position.

## 8. Turning the identity into a certified reader

The exact recurrence has the mathematical initial state `F_0 = pi - 4`. A finite computer cannot hold that irrational exactly, so an executable version carries an interval containing the state. One transparent reference implementation seeds the interval with a rational partial sum of BBP and a rigorous geometric bound on the omitted tail, then advances the recurrence and multiplies the interval error by 16 at each emission.

A second implementation starts with an empty field. It keeps separate frontiers for opened layers and lower precision, preserves its lane cursors, and introduces unopened terms only through a bound. It emits only when the interval endpoints certify the same hexadecimal digit; otherwise it opens another layer or widens precision. These are two implementations of the same lane relation with different initialization and bookkeeping, so their results must be reported separately.

For the unopened contribution after opening layers 0 through K, a valid absolute bound is

`|U_(n,K)| <= (16/15) * 8/(8K+9) * 16^(n-K-1)`.

The denominator floor comes from `8k+j >= 8K+9` for `k>K`; the factor 8 is the sum of absolute BBP weights; and `16/15` is the geometric sum `1 + 1/16 + 1/16^2 + ...`. The exponent accounts for the first unopened layer's position relative to n. This bound lets the reader delay the explicit opening of a lane without pretending the lane is absent.

The exact recurrence is an identity. The interval implementation is sound when its rational endpoint calculations and this tail bound enclose the true state, and certification occurs only when both endpoints imply the same digit.

## 9. Computational check

The reference implementation `bbp_motion_formula.py` was rerun with 2,000 output digits, 96 guard terms, and an exact-rational seed containing 2,096 BBP terms. It generated 2,000 trace rows and matched an independent high-precision `mpmath` calculation at all 2,000 positions. Wall time in this environment was 6.46 seconds. The trace records `C_n`, the boundary correction, each output digit and the certification flag.

This is a regression check, not the proof of the formula. The proof follows from the Euclidean division identity and the recurrence derivation above. The second, empty-field `pending.py` reader is separate; its previously audited longer runs are not being treated as if they used the same initialization as the finite-seed reference.

## 10. Scope

This paper is about deriving and making explicit the digit-emission formula from BBP's lane motion. It does not claim a new identity for π, nor does it claim that sequential BBP digit generation has never been implemented. Prior work includes incremental/co-recursive BBP computation and other stateful methods for producing π digits. The present contribution is the explicit crossing-sum/boundary-correction derivation presented as a reusable state transition, with a persistent lane implementation and a separately certified reader. Any broad novelty or priority claim would require a more exhaustive comparison of algorithms and their internal state representations.

## Conclusion

The formula drops out once the local long-division motion is preserved instead of being discarded after each read. Every lane turns a remainder into a quotient crossing and a new remainder. The weighted crossings form `C_n`. That integer advances the aggregate field through `F_(n+1) = 16F_n - C_n`. The emitted digit is the exact boundary correction that closes the transition:

**`a_(n+1) = C_n + floor(F_(n+1)) - 16 floor(F_n)`.**

This is the process written as its own formula. The accumulated object is a growing field of live instructions and phase relations—not a mass of previously emitted digits.

## References

1. Bailey, D. H., Borwein, P. B., and Plouffe, S. (1997). “On the rapid computation of various polylogarithmic constants.” *Mathematics of Computation*, 66(218), 903–913.
2. Bailey, D. H. (2006). “The BBP Algorithm for Pi.” Manuscript, 8 September 2006.
3. Rabinowitz, S. and Wagon, S. (1995). “A Spigot Algorithm for the Digits of Pi.” *The American Mathematical Monthly*, 102(3), 195–203.
4. Gibbons, J. (2006). “Unbounded Spigot Algorithms for the Digits of Pi.” *The American Mathematical Monthly*, 113(4), 318–328.
5. Ziv, A. (1991). “Fast Evaluation of Elementary Mathematical Functions with Correctly Rounded Last Bit.” *ACM Transactions on Mathematical Software*, 17(3), 410–423.
6. Karczmarczuk, J. (1998). “The Most Unreliable Technique in the World to Compute π.” An incremental, co-recursive BBP implementation.
7. OEIS Foundation. “A062964: Pi in hexadecimal.” Includes the Bailey–Crandall conjectured scalar recurrence for hexadecimal digits of π: https://oeis.org/A062964.
