# Native mathematical reference

[Documentation](README.md) · [Method contract](../METHODS.md) · [Machine-readable registry](methods.json)

This initial software-style reader uses equations in the [native domain core](../The%20Nexus%20Domain/Markdown/NEXUS_Domain_Core_20261103.md) and [ring ISA stack](../The%20Nexus%20Domain/Markdown/NEXUS_ring_ISA_stack_1_to_64.md). Method names are documentation identifiers, not claims that an existing library exports these functions. A word width, first nontrivial operation and minimal implementation address are distinct; missing bindings remain OPEN. No new experiments were executed.

| Method | Dependencies |
| --- | --- |
| [Complement](#word-complement) | — |
| [Bit reversal](#word-reverse) | — |
| [Native partner](#ring-partner) | `word-complement`, `word-reverse` |
| [Ring address / READ](#ring-read) | `ring-partner` |
| [One-inverter recirculation](#clock-tick) | `word-complement` |
| [Native reader–field step](#reader-step) | `ring-partner` |
| [Binary state count](#ring-state-count) | — |
| [Total transformation count](#ring-map-count) | `ring-state-count` |

## word-complement

**Complement** — STANDS (source-level mathematical relation)

- Expression: `C_n(x) = x XOR (2^n - 1)`
- Input: n-bit word, n >= 1
- Output: n-bit word
- Dependencies: None in this registry
- Address: R1 for single-bit NOT; general width n
- Return route: C_n(C_n(x)) = x
- Scope: Fixed-width involution
- Source: [NEXUS_Domain_Core_20261103.md](../The%20Nexus%20Domain/Markdown/NEXUS_Domain_Core_20261103.md), 1.1; 2.

## word-reverse

**Bit reversal** — STANDS (source-level mathematical relation)

- Expression: `J_n(x) = reverse the n bit positions of x`
- Input: n-bit word, n >= 1
- Output: n-bit word
- Dependencies: None in this registry
- Address: Width n; earliest nonidentity ISA binding OPEN
- Return route: J_n(J_n(x)) = x
- Scope: Commutes with complement
- Source: [NEXUS_Domain_Core_20261103.md](../The%20Nexus%20Domain/Markdown/NEXUS_Domain_Core_20261103.md), 1.1.

## ring-partner

**Native partner** — STANDS (source-level mathematical relation)

- Expression: `P_n(x) = C_n(x) if J_n(x) = x; otherwise J_n(x)`
- Input: n-bit word, n >= 1
- Output: Distinct partner word
- Dependencies: word-complement, word-reverse
- Address: Source-defined family at width n
- Return route: P_n(P_n(x)) = x
- Scope: Fixed-point-free involution
- Source: [NEXUS_Domain_Core_20261103.md](../The%20Nexus%20Domain/Markdown/NEXUS_Domain_Core_20261103.md), 1.1, equation (1.1).

## ring-read

**Ring address / READ** — STANDS (source-level mathematical relation)

- Expression: `READ = R_n^(-1); R_n(2^n - 1 - a) = P_n(R_n(a))`
- Input: Native ring order R_n and n-bit word
- Output: Address a, 0 <= a < 2^n
- Dependencies: ring-partner
- Address: Width n; ordering supplied by source
- Return route: R_n(READ(x)) = x
- Scope: Fixed ring permutation, not arbitrary permutation search
- Source: [NEXUS_Domain_Core_20261103.md](../The%20Nexus%20Domain/Markdown/NEXUS_Domain_Core_20261103.md), 1.1, equation (1.2).

## clock-tick

**One-inverter recirculation** — STANDS (source-level mathematical relation)

- Expression: `tau(b0,...,b[r-1]) = (NOT b[r-1],b0,...,b[r-2])`
- Input: r-bit register, r >= 1
- Output: Successor register
- Dependencies: word-complement
- Address: R1 for NOT; register width r
- Return route: tau^(-1)(y0,...,y[r-1]) = (y1,...,y[r-1],NOT y0); tau^r = C_r; tau^(2r) = I
- Scope: The 2r identity does not imply every state has least period 2r
- Source: [NEXUS_Domain_Core_20261103.md](../The%20Nexus%20Domain/Markdown/NEXUS_Domain_Core_20261103.md), 2, equations (2.1)–(2.2).

## reader-step

**Native reader–field step** — STANDS (source-level mathematical relation)

- Expression: `x = D[p] XOR w; p' = p XOR x; w' = P_n(x); D'[p] = D[p] XOR w'; other cells unchanged`
- Input: Complete width-n state (p,w,D)
- Output: Complete successor (p',w',D')
- Dependencies: ring-partner
- Address: Width n; minimal instruction composition OPEN
- Return route: x = P_n(w'); p = p' XOR x; D[p] = D'[p] XOR w'; w = x XOR D[p]; other cells unchanged
- Scope: Bijection on complete states; not inversion from an incomplete observation
- Source: [NEXUS_Domain_Core_20261103.md](../The%20Nexus%20Domain/Markdown/NEXUS_Domain_Core_20261103.md), 3.1, equations (3.1)–(3.2).

## ring-state-count

**Binary state count** — STANDS (source-level mathematical relation)

- Expression: `|S_n| = 2^n; S_n = {0,1}^n`
- Input: Integer width n >= 1
- Output: Exact integer count
- Dependencies: None in this registry
- Address: Width n; count rather than gate binding
- Return route: For an exact power of two, n = log2(count)
- Scope: Counts words, not maps
- Source: [NEXUS_ring_ISA_stack_1_to_64.md](../The%20Nexus%20Domain/Markdown/NEXUS_ring_ISA_stack_1_to_64.md), The flip: the state is not the whole instruction space.

## ring-map-count

**Total transformation count** — STANDS (source-level mathematical relation)

- Expression: `Total maps = 2^(n*2^n); bijections = (2^n)!`
- Input: Integer width n >= 1
- Output: Exact symbolic count
- Dependencies: ring-state-count
- Address: Transformation meta-layer, not gate binding
- Return route: A count does not encode a particular transformation
- Scope: The native ISA is a structured subfamily
- Source: [NEXUS_ring_ISA_stack_1_to_64.md](../The%20Nexus%20Domain/Markdown/NEXUS_ring_ISA_stack_1_to_64.md), The flip; What the stack forces.


## Next binding

Derive minimal provider chains and connect actual implementations, seals, execution and corrections. See the [fixed-ring compiler](../The%20Nexus%20Domain/Markdown/ring_compiler_README.md) and [native code](../The%20Nexus%20Domain/Code). The full formula census and method-to-ring dependency graph remain OPEN.
