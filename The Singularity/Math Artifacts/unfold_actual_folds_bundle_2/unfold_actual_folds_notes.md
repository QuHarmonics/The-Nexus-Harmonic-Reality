# Unfolding the recorded literal folds

Each fold records A=upper half and D=A xor reverse(lower half). Its exact inverse is A || reverse(A xor D). The decoder uses only the terminal residual and reference halves, from innermost outward; the original tape is a verification target, not an input to that decoder.

## Measured unfold chains (hex, with widths retained)

R2: 0[1] -> 3[2] -> C[4] -> 27[8]. References inner to outer: 1[1],3[2],2[4].

R3: 000[3] -> 3F[6] -> E38[12] -> 056767[24]. References inner to outer: 111[3],111000[6],000001010110[12].

R4: 0[1] -> 0[2] -> 0[4] -> FF[8] -> F0F0[16] -> F0000F00[32] -> 0123567DBE9AC48F[64]. References inner to outer: 0[1],00[2],1111[4],F0[8],F000[16],0123567D[32].

The zero-to-FF step is not data creation: the retained reference 1111, with residual 0000, reconstructs lower 1111 and therefore 11111111.

## Runtime return

Unfold the folded coordinate by i=M-1-j on the L face and i=M+j on the R face. Every original position and word order returned exactly. The endpoint face changes split into ordinary transitions: for R3, 0L->0R becomes 110->011; the outer 3R->3L becomes 111->000. For R4, 0L->0R becomes 1101->1011 and 7R->7L becomes 1111->0000.

Clockwise / counterclockwise from the same first slot:
R2: 27 / 72.
R3: 056767 / 737350.
R4: 0123567DBE9AC48F / 7891ACBEDF356240.

Forward and inverse native runtimes and P T P=T_inverse passed at every word state. All positions were restored exactly once. Flipping any one of the 96 total packet bits changed its unfolded output, verifying that the retained channels participate in reconstruction.

## Accounting

R2: 1 terminal bit + 7 reference bits = 8 serialized bits.
R3: 3 terminal bits + 21 reference bits = 24 serialized bits.
R4: 1 terminal bit + 63 reference bits = 64 serialized bits.

The inverse is lossless, not compression. A fixed ring-generating map can supply these reference values, but this replay specifically reversed the recorded fold packet. It does not claim to recover arbitrary erased information from a terminal zero.

The source hash was recorded before this known-structure replay and verified afterward. It is not represented as a new blind prediction.
