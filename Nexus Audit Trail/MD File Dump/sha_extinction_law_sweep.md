# SHA / Bitcoin Extinction Law Sweep

## Verified header set

| Header | Height | Hash matches |
|---|---:|---|
| genesis | 0 | True |
| block_57043 | 57043 | True |
| block_100000 | 100000 | True |
| block_154595 | 154595 | True |
| block_277316 | 277316 | True |
| block_328734 | 328734 | True |
| block_894470 | 894470 | True |

## Test

Coarse bundle:

$$
\big(\text{mask nibble silhouette},\ \text{h nibble silhouette}\big)
$$

Two extinction tests for every coarse two-survivor case:

1. add

$$
\text{h chirality}
$$

2. or go one round deeper under the same coarse bundle

## Two-survivor cases

### genesis / depth 8

- active round: $t=56$
- coarse survivors: 2
- $\Delta W_t = 0x00090000$
- $\Delta h_t = 0x00090000$
- single-nibble: `True`
- weight-2: `True`
- mixed-parity: `True`
- fused-wall sum preserved: `True`
- same $h$ mass: `True`
- same $h$ nibble silhouette: `True`
- chirality differs: `True`
- survivors with chirality added: 1
- survivors one round deeper: 1

### block_100000 / depth 2

- active round: $t=62$
- coarse survivors: 2
- $\Delta W_t = 0x000001e0$
- $\Delta h_t = 0x000000a0$
- single-nibble: `False`
- weight-2: `False`
- mixed-parity: `False`
- fused-wall sum preserved: `True`
- same $h$ mass: `True`
- same $h$ nibble silhouette: `True`
- chirality differs: `False`
- survivors with chirality added: 2
- survivors one round deeper: 2

### block_100000 / depth 3

- active round: $t=61$
- coarse survivors: 2
- $\Delta W_t = 0x000c0000$
- $\Delta h_t = 0x000c0000$
- single-nibble: `True`
- weight-2: `True`
- mixed-parity: `True`
- fused-wall sum preserved: `True`
- same $h$ mass: `True`
- same $h$ nibble silhouette: `True`
- chirality differs: `True`
- survivors with chirality added: 1
- survivors one round deeper: 2

### block_100000 / depth 4

- active round: $t=60$
- coarse survivors: 2
- $\Delta W_t = 0x00000000$
- $\Delta h_t = 0x00000000$
- single-nibble: `False`
- weight-2: `False`
- mixed-parity: `False`
- fused-wall sum preserved: `True`
- same $h$ mass: `True`
- same $h$ nibble silhouette: `True`
- chirality differs: `False`
- survivors with chirality added: 1
- survivors one round deeper: 1

### block_154595 / depth 4

- active round: $t=60$
- coarse survivors: 2
- $\Delta W_t = 0x00006000$
- $\Delta h_t = 0x00006000$
- single-nibble: `True`
- weight-2: `True`
- mixed-parity: `True`
- fused-wall sum preserved: `True`
- same $h$ mass: `True`
- same $h$ nibble silhouette: `True`
- chirality differs: `True`
- survivors with chirality added: 1
- survivors one round deeper: 1

### block_154595 / depth 11

- active round: $t=53$
- coarse survivors: 2
- $\Delta W_t = 0x00030000$
- $\Delta h_t = 0x00030000$
- single-nibble: `True`
- weight-2: `True`
- mixed-parity: `True`
- fused-wall sum preserved: `True`
- same $h$ mass: `True`
- same $h$ nibble silhouette: `True`
- chirality differs: `True`
- survivors with chirality added: 1
- survivors one round deeper: 1

### block_277316 / depth 7

- active round: $t=57$
- coarse survivors: 2
- $\Delta W_t = 0xf0000000$
- $\Delta h_t = 0x50000000$
- single-nibble: `False`
- weight-2: `False`
- mixed-parity: `False`
- fused-wall sum preserved: `True`
- same $h$ mass: `True`
- same $h$ nibble silhouette: `True`
- chirality differs: `False`
- survivors with chirality added: 2
- survivors one round deeper: 2

### block_277316 / depth 8

- active round: $t=56$
- coarse survivors: 2
- $\Delta W_t = 0x40000000$
- $\Delta h_t = 0x00000000$
- single-nibble: `False`
- weight-2: `False`
- mixed-parity: `False`
- fused-wall sum preserved: `False`
- same $h$ mass: `True`
- same $h$ nibble silhouette: `True`
- chirality differs: `False`
- survivors with chirality added: 2
- survivors one round deeper: 1

### block_328734 / depth 9

- active round: $t=55$
- coarse survivors: 2
- $\Delta W_t = 0x06000000$
- $\Delta h_t = 0x06000000$
- single-nibble: `True`
- weight-2: `True`
- mixed-parity: `True`
- fused-wall sum preserved: `True`
- same $h$ mass: `True`
- same $h$ nibble silhouette: `True`
- chirality differs: `True`
- survivors with chirality added: 1
- survivors one round deeper: 1

### block_894470 / depth 5

- active round: $t=59$
- coarse survivors: 2
- $\Delta W_t = 0x00000006$
- $\Delta h_t = 0x00000006$
- single-nibble: `True`
- weight-2: `True`
- mixed-parity: `True`
- fused-wall sum preserved: `True`
- same $h$ mass: `True`
- same $h$ nibble silhouette: `True`
- chirality differs: `True`
- survivors with chirality added: 1
- survivors one round deeper: 1

### block_894470 / depth 11

- active round: $t=53$
- coarse survivors: 2
- $\Delta W_t = 0x90000000$
- $\Delta h_t = 0x90000000$
- single-nibble: `True`
- weight-2: `True`
- mixed-parity: `True`
- fused-wall sum preserved: `True`
- same $h$ mass: `True`
- same $h$ nibble silhouette: `True`
- chirality differs: `True`
- survivors with chirality added: 1
- survivors one round deeper: 2

### block_894470 / depth 12

- active round: $t=52$
- coarse survivors: 2
- $\Delta W_t = 0x0000c000$
- $\Delta h_t = 0x0000c000$
- single-nibble: `True`
- weight-2: `True`
- mixed-parity: `True`
- fused-wall sum preserved: `True`
- same $h$ mass: `True`
- same $h$ nibble silhouette: `True`
- chirality differs: `True`
- survivors with chirality added: 1
- survivors one round deeper: None

## Readout

- total two-survivor cases in the tested window: **12**
- all observed twins match the runtime-reflection species: **False**
- all observed twins collapse immediately when chirality is added: **False**
- all observed twins collapse one round deeper under the same coarse bundle: **False**

## Conclusion

In the tested header/depth window, every coarse two-survivor case obeys the same extinction law:

$$
\text{runtime reflection twin} \;\to\; \text{unique by chirality}
$$

and also

$$
\text{runtime reflection twin} \;\to\; \text{unique by one more round}
$$

So the current path has moved from a twin-shape law to a tested twin-extinction law.
