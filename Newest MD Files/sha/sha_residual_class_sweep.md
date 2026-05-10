# SHA / Bitcoin Residual-Class Sweep

## Goal

Sweep the current law over deeper tail windows using the bundle

$$
\big(\text{mask nibble silhouette},\ \text{h nibble silhouette}\big)
$$

and check whether **any** non-unique cases appear outside the observed twin species.

## Survivor counts

### block_328734

- depth 1: survivors = 1
- depth 2: survivors = 1
- depth 3: survivors = 1
- depth 4: survivors = 1
- depth 5: survivors = 1
- depth 6: survivors = 1
- depth 7: survivors = 1
- depth 8: survivors = 1
- depth 9: survivors = 2
- depth 10: survivors = 1
- depth 11: survivors = 1
- depth 12: survivors = 1
- depth 13: survivors = 1
- depth 14: survivors = 1
- depth 15: survivors = 1
- depth 16: survivors = 1

### genesis

- depth 1: survivors = 1
- depth 2: survivors = 1
- depth 3: survivors = 1
- depth 4: survivors = 1
- depth 5: survivors = 1
- depth 6: survivors = 1
- depth 7: survivors = 1
- depth 8: survivors = 2
- depth 9: survivors = 1
- depth 10: survivors = 1
- depth 11: survivors = 1
- depth 12: survivors = 1
- depth 13: survivors = 1
- depth 14: survivors = 1
- depth 15: survivors = 1
- depth 16: survivors = 2

## Non-unique cases

### genesis depth 8

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

### genesis depth 16

- survivors: 2
- active round: $t=48$
- $\Delta W_t = 0x60000000$
- $\Delta h_t = 0x60000000$
- same delta in $W_t$ and $h_t$: `True`
- delta bits: [29, 30]
- single-nibble: `True`
- weight-2: `True`
- mixed-parity: `True`
- fused-wall sum preserved: `True`
- same $h$ Hamming weight: `True`
- same $h$ nibble silhouette: `True`
- same $h$ chirality: `False`
- $h$ chirality pair: (7, 9) vs (6, 10)

### block_328734 depth 9

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

## Readout

All observed two-survivor cases match the runtime-reflection twin species: `True`.

In the tested depth window, every observed twin is:

$$
\text{single-nibble} + \text{weight-2} + \text{mixed-parity} + \Delta W_t=\Delta h_t
$$

and preserves:

$$
\text{fused-wall sum} + \text{h mass} + \text{h nibble silhouette}
$$

while changing chirality.

## Conclusion

Within the tested range (depths 1–16 on the two real Bitcoin headers), no counterexample to the current residual-class law was found.
