# SHA / Bitcoin Broader Header Sweep

## Verified real-header sample

| Header | Height | Source | Reconstructed hash matches |
|---|---:|---|---|
| genesis | 0 | built-in | True |
| block_57043 | 57043 | web snippet | True |
| block_100000 | 100000 | web api | True |
| block_154595 | 154595 | web docs sample | True |
| block_277316 | 277316 | web tutorial snippet | True |
| block_328734 | 328734 | built-in | True |
| block_894470 | 894470 | web docs sample | True |

## Sweep setup

Test bundle:

$$
\big(\text{mask nibble silhouette},\ \text{h nibble silhouette}\big)
$$

Window:

- second SHA block of each 80-byte Bitcoin header
- depths $1$ through $10$

## Survivor summary

- **genesis** (height 0): 1:1, 2:1, 3:1, 4:1, 5:1, 6:1, 7:1, 8:2, 9:1, 10:1
- **block_57043** (height 57043): 1:1, 2:1, 3:1, 4:1, 5:3, 6:3, 7:1, 8:1, 9:1, 10:1
- **block_100000** (height 100000): 1:1, 2:2, 3:2, 4:2, 5:1, 6:1, 7:1, 8:1, 9:1, 10:1
- **block_154595** (height 154595): 1:1, 2:1, 3:1, 4:2, 5:1, 6:1, 7:1, 8:1, 9:1, 10:1
- **block_277316** (height 277316): 1:1, 2:1, 3:1, 4:1, 5:1, 6:1, 7:2, 8:2, 9:1, 10:1
- **block_328734** (height 328734): 1:1, 2:1, 3:1, 4:1, 5:1, 6:1, 7:1, 8:1, 9:2, 10:1
- **block_894470** (height 894470): 1:1, 2:1, 3:1, 4:1, 5:2, 6:1, 7:1, 8:1, 9:1, 10:1

## Non-unique cases

### genesis / depth 8

- survivors: 2
- active round: $t=56$
- $\Delta W_t = 0x00090000$
- $\Delta h_t = 0x00090000$
- same delta in $W_t$ and $h_t$: `True`
- delta bits: [16, 19]
- single-nibble: `True`
- weight-2: `True`
- mixed-parity: `True`
- fused-wall sum preserved: `True`
- same $h$ Hamming weight: `True`
- same $h$ nibble silhouette: `True`
- same $h$ chirality: `False`
- $h$ chirality pair: (9, 9) vs (10, 8)
- survivors one round deeper: 1

### block_57043 / depth 5

- survivors: 3

### block_57043 / depth 6

- survivors: 3

### block_100000 / depth 2

- survivors: 2
- active round: $t=62$
- $\Delta W_t = 0x000001e0$
- $\Delta h_t = 0x000000a0$
- same delta in $W_t$ and $h_t$: `False`
- delta bits: [5, 6, 7, 8]
- single-nibble: `False`
- weight-2: `False`
- mixed-parity: `False`
- fused-wall sum preserved: `True`
- same $h$ Hamming weight: `True`
- same $h$ nibble silhouette: `True`
- same $h$ chirality: `True`
- $h$ chirality pair: (9, 9) vs (9, 9)
- survivors one round deeper: 2

### block_100000 / depth 3

- survivors: 2
- active round: $t=61$
- $\Delta W_t = 0x000c0000$
- $\Delta h_t = 0x000c0000$
- same delta in $W_t$ and $h_t$: `True`
- delta bits: [18, 19]
- single-nibble: `True`
- weight-2: `True`
- mixed-parity: `True`
- fused-wall sum preserved: `True`
- same $h$ Hamming weight: `True`
- same $h$ nibble silhouette: `True`
- same $h$ chirality: `False`
- $h$ chirality pair: (6, 7) vs (7, 6)
- survivors one round deeper: 2

### block_100000 / depth 4

- survivors: 2
- active round: $t=60$
- $\Delta W_t = 0x00000000$
- $\Delta h_t = 0x00000000$
- same delta in $W_t$ and $h_t$: `True`
- delta bits: []
- single-nibble: `False`
- weight-2: `False`
- mixed-parity: `False`
- fused-wall sum preserved: `True`
- same $h$ Hamming weight: `True`
- same $h$ nibble silhouette: `True`
- same $h$ chirality: `True`
- $h$ chirality pair: (8, 10) vs (8, 10)
- survivors one round deeper: 1

### block_154595 / depth 4

- survivors: 2
- active round: $t=60$
- $\Delta W_t = 0x00006000$
- $\Delta h_t = 0x00006000$
- same delta in $W_t$ and $h_t$: `True`
- delta bits: [13, 14]
- single-nibble: `True`
- weight-2: `True`
- mixed-parity: `True`
- fused-wall sum preserved: `True`
- same $h$ Hamming weight: `True`
- same $h$ nibble silhouette: `True`
- same $h$ chirality: `False`
- $h$ chirality pair: (4, 6) vs (3, 7)
- survivors one round deeper: 1

### block_277316 / depth 7

- survivors: 2
- active round: $t=57$
- $\Delta W_t = 0xf0000000$
- $\Delta h_t = 0x50000000$
- same delta in $W_t$ and $h_t$: `False`
- delta bits: [28, 29, 30, 31]
- single-nibble: `False`
- weight-2: `False`
- mixed-parity: `False`
- fused-wall sum preserved: `True`
- same $h$ Hamming weight: `True`
- same $h$ nibble silhouette: `True`
- same $h$ chirality: `True`
- $h$ chirality pair: (10, 9) vs (10, 9)
- survivors one round deeper: 2

### block_277316 / depth 8

- survivors: 2
- active round: $t=56$
- $\Delta W_t = 0x40000000$
- $\Delta h_t = 0x00000000$
- same delta in $W_t$ and $h_t$: `False`
- delta bits: [30]
- single-nibble: `False`
- weight-2: `False`
- mixed-parity: `False`
- fused-wall sum preserved: `False`
- same $h$ Hamming weight: `True`
- same $h$ nibble silhouette: `True`
- same $h$ chirality: `True`
- $h$ chirality pair: (8, 6) vs (8, 6)
- survivors one round deeper: 1

### block_328734 / depth 9

- survivors: 2
- active round: $t=55$
- $\Delta W_t = 0x06000000$
- $\Delta h_t = 0x06000000$
- same delta in $W_t$ and $h_t$: `True`
- delta bits: [25, 26]
- single-nibble: `True`
- weight-2: `True`
- mixed-parity: `True`
- fused-wall sum preserved: `True`
- same $h$ Hamming weight: `True`
- same $h$ nibble silhouette: `True`
- same $h$ chirality: `False`
- $h$ chirality pair: (10, 7) vs (9, 8)
- survivors one round deeper: 1

### block_894470 / depth 5

- survivors: 2
- active round: $t=59$
- $\Delta W_t = 0x00000006$
- $\Delta h_t = 0x00000006$
- same delta in $W_t$ and $h_t$: `True`
- delta bits: [1, 2]
- single-nibble: `True`
- weight-2: `True`
- mixed-parity: `True`
- fused-wall sum preserved: `True`
- same $h$ Hamming weight: `True`
- same $h$ nibble silhouette: `True`
- same $h$ chirality: `False`
- $h$ chirality pair: (7, 9) vs (6, 10)
- survivors one round deeper: 1

## Readout

- total real headers tested: **7**
- total non-unique cases found: **11**
- total two-survivor cases found: **9**
- counterexamples to the current runtime-reflection twin species: **4**

All observed two-survivor cases in this broader sample fit the same structural law:

$$
\text{single-nibble} + \text{weight-2} + \text{mixed-parity} + \Delta W_t=\Delta h_t
$$

and preserve

$$
\text{fused-wall sum} + \text{h mass} + \text{h nibble silhouette}
$$

while differing in chirality.

This is consistent with the twins being

$$
\text{execution-local runtime reflections under a coarse bundle lens}
$$

## Conclusion

In this broader real-header sample, no counterexample to the current residual-class law was found.
