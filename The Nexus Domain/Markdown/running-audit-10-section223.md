## § 223. Address plus generator: the ring's complete binary signature regenerates on demand; the shared reader uses an information-minimal address — `section223_address_generator.py`

**Dean (31 Oct).** "Memory can be generated with math. All transformations are binary. All things have a binary signature." The requested next step: "Memory is an address plus a generator. Take one thing's binary signature and find the smallest address-and-rule pair that regenerates it on demand, the way BBP regenerates π. Append §223."

**Scope and correction.** The object selected is the *entire width-16 native-ring walk* as a single ordered 1,048,576-bit signature. This is generated output, not a pre-stored file used by the reader. The smallest-address claim below is exact **only within the specified model**: a fixed, shared, lossless reader that must be able to select any one of all 2^n different n-bit words. It does **not** prove a shortest total program for this particular string. Earlier paper outputs, including `0x27`, the width-4 `0123567dbe9ac48f` walk, and the previously recorded 64-bit π word/address, were already known. The run is an independently implemented execution route and regression, not an independent blind landing.

**Prediction seal.** Before the execution, the text file `seal223_predictions.txt` was written and hashed SHA-256 `33c2bb8283516406e5e9f5b53e8511e98a7854b762d8e59d16697af95211ef72`; all seven scoped predictions held. The known source outputs in that text are identified as regressions.

**One reader, not a stored ring.** Let `P_n(x)` be the existing involution: reverse the word unless it is palindromic, in which case complement it. Write `M_n={x: x<P_n(x)}`. For any fixed binary prefix, the count of completions in `M_n` can be obtained by walking **symmetric bit pairs**, recording whether the prefix has already become smaller than its reversal. If all pairs match, only a leading zero survives. No candidate words, sorted representative list, or ring builder enter the reader. Repeated branch counts unrank the representative at any near address; the established partner maps it into the far address.

With `N=2^n`, `h=N/2`, and `u(i)` the branch-count unranking operator,

```
G_counter(n,a) = u(a)                if a < h
                 P_n(u(N-1-a))     if a >= h

G_record(n,a) = G_counter(n,a)      except at a=h-1 and a=h,
where those two words exchange places (n>=2).
```

The inverse `SAVE` computes the representative's lexicographic rank by adding the counts of skipped zero branches along the input word's bits. The partner side determines the far address; the record-crease exception swaps the two center addresses back. Both directions use the same fixed rule.

**The §208 lane supplies the bit execution.** For any returned word `x`, run `2r = 2^n q + r'` for `n` steps, starting `r=x`. Its crossing bits are exactly the bits of `x`, and the remainder reaches 0. Conversely, integrating the crossings in base two returns `x`. This is the recorded lane, not an invented instruction set.

**The actual run.** Script `section223_address_generator.py` was executed successfully, comparing only *after generation* to an independent conventional ring builder. Widths 1–12 were run at every address under both crease contracts, verifying uniqueness, `READ -> SAVE`, crossing reconstruction, and the facing involution. At width 16, the reader emitted every word at its address, all 65,536 addresses returned exactly from the emitted word, all 32,768 facing pairs held, and the conventional builder agreed when invoked afterwards.

```
TARGET:             complete record-crease R_16 walk
NUMBER OF WORDS:    65,536
WORD WIDTH:         16 bits
BINARY SIGNATURE:   1,048,576 bits = 131,072 bytes
INPUT TO READER:    n=16, crease=record, address a (16 bits)
NO RING TABLE:      in READ or SAVE
SHA-256 OF OUTPUT:  ba3eac43b1c08d6d3267535fd587238a159eab6a1a2060328aa02890867fd961
OUTPUT FILE:        R16_signature_regenerated.bin (written by executor, not loaded by it)
```

**Previously recorded 64-bit object.** Independently, using the recorded ring address `2,427,008,858,123,944,441` and the same shared reader at width 64 returns `0x243f6a8885a308d3`; `SAVE` returns the recorded address. This is a return to an already known datum, not a new prediction.

**Smallest address, with its exact qualifier.** A shared fixed reader must distinguish `2^n` possible n-bit values. No fixed-length address shorter than `n` bits has that many encodings. `G(n,a,c)` uses exactly `n` address bits when `n` and the crease contract are fixed. The generator code has a separate, shared cost, and a particular highly structured word can have a shorter description. The result proves optimal *universal address width*, not absolute Kolmogorov minimality or that arbitrary signatures compress.

**What moves.** `READ` is not a materialized copy of the field. The address determines the next binary word by an executable rule; `SAVE` computes its inverse address; the same word's lane emits its crossings. The 131,072 output bytes are an *artifact of execution* and can be discarded and reproduced. That is exactly the distinction between generating memory and storing an independent copy of its contents.

| Claim | Status |
|---|---|
| address-wise generation and inverse on both crease contracts, n=1..12, every address | RUNS |
| complete R_16 output without input ring table, every word once | RUNS |
| all R_16 32,768 facing pairs and independent builder match | RUNS |
| base-2 crossings and weighted save return word | RUNS (n=1..12 exhaustive; follows §208 algebra at n=16) |
| previously recorded 64-bit π word/address reconstruct | RUNS — previously seen data, provenance regression |
| address-width lower bound n for a shared lossless reader | STANDS — counting argument |
| absolute smallest total address-and-rule program for this string | OPEN — depends on machine/description language |
| unique physical generation of all real-world objects from binary signatures | OPEN — not asserted by this execution |

**Files.** `section223_address_generator.py`; `section223_actual_run.txt`; `seal223_predictions.txt`; `R16_signature_regenerated.bin`. `READ` contains no call to the independent `regression_ring` oracle; that function is executed only to compare after the generated output exists.
