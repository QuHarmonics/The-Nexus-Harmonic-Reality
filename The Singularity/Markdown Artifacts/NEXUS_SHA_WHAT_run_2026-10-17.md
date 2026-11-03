# NEXUS — What SHA-256 is when the route is kept typed

**Prediction seal:** `520682a8f49b1076b69be5023a16b825b9322e6c70e91f943a133b7bfd1b6f59`  
**Witness:** `NEXUS route home`  
**Result digest:** `bc5d06af3852248d22c535d4c701968c3b1972e876080d5f8135ba3e8ad72db4`

## Compiler landing

The concrete route matches `hashlib.sha256`; the 64 inverse-round steps return to the initial chaining state when the schedule words and public round constants are retained. The final 16 schedule words reconstruct the full 64-word schedule and the original padded block. For the known incoming chaining state, feed-forward is undone by subtracting it wordwise modulo 2^32.

The observer coordinate used in this run is 512 bits (the schedule tail), exactly the size of the 512-bit source block. It is a reversible recoding, not a compression. The route returns home because the driver information was kept. The 256-bit digest alone is not the root observer.

## The bound that seals the distinction

For the fixed-length class of 33-byte messages, the source domain contains 2^264 messages and the digest codomain contains at most 2^256 digests. Therefore at least one digest has at least 256 messages in its fiber. This is a theorem about cardinality, not an identified collision pair.

For fixed n-byte messages, if `(digest, residual)` must identify each source uniquely and the residual has q fixed bits, then `256 + q >= 8n`, so `q >= max(0, 8n - 256)`. A fixed-width residual cannot return arbitrary-length messages of unbounded length.

## Typed answer

- **Static program:** padding, schedule recurrence, 64 round operators, feed-forward, public constants.
- **Realized route:** the specific padded message blocks, message-derived schedule words, and traversed internal states.
- **Digest:** the folded 256-bit surface readout, not the realized route.
- **Root observer:** reverse rules plus sufficient source-specific driver/fiber data. Its minimal general form remains OPEN.

**Landing:** local reversibility with drivers **RUNS**; forced many-to-one folding at the message/digest boundary **STANDS** by counting; digest-only universal return is a **DEAD END**; minimum practical root observer **OPEN**. This is not a cryptographic break.
