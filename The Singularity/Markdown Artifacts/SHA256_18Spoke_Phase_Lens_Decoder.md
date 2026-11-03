# Exact decoder for the 18-spoke phase lens

Define the integer phase tick for a 32-bit word x by

`q = 18*x mod 2^32`.

Because `18 = 2*9`, q is always even and

`q/2 = 9*x mod 2^31`.

Since 9 is invertible modulo `2^31`, its inverse is `954437177`. Therefore the original lower 31 bits are recovered by

`low31 = ((q/2) * 954437177) mod 2^31`.

The map has a two-element kernel: x and `x XOR 0x80000000` have identical phase. The one missing bit is exactly the 32-bit word's high bit. Retaining that bit as the other face/branch restores the complete word:

`x = low31 | (msb << 31)`.

This identity is exact, not a statistical fit. It was checked against 100192 values: all 64 indexed SHA-256 constants, all available word values in the Ovaltine and empty-message schedule traces, and 100,000 deterministic random 32-bit words; 0 failures.

The 18-spoke phase itself is not a unique 32-bit address. The pair (phase tick, high bit) is a unique address. In angular units, `angle = 20*q/2^32` degrees.
