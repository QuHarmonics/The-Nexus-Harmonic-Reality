# Append-only stroke: readiness is the execution rule

This is an active-event audit, not another static rank or Walsh test. The original ring is unchanged. The rule is taken from the corpus's emit-when-settled semantics. Physical identification remains PULL.

## Two kinds of readiness

A paired-difference block is ready as soon as both input blocks are present. Merge (A,B)->(A,A xor B), retaining both lanes. This is the online Mobius stack; its output is its own inverse. Partial blocks do not wait for the final requested word width.

For an arithmetic output f and current observations o, let Omega(o) be every complete input compatible with those observations. The output is semantically ready iff {f(x):x in Omega(o)} is a singleton. This is stronger than requiring every input port to be known. A carry can be fixed by two agreeing inputs of its majority cell even while the third is unknown.

## Fixed eight-slot orbit

Original flattened R2 = 00100111. This is an eight-slot orbit, not the 256-word inventory R8. It supplied all phases and both directions. The same compiler was also tested on every possible byte.

At arrivals 2,4,6,8 the two-bit units close. At arrivals 4 and 8 the four-bit units close. The first eight-bit unit closes at arrival 8. On a 64-arrival stream it still closes at arrival 8 rather than waiting for 64. All 256 byte round trips passed. All 64 phase/direction/length stream runs passed; every closure had zero additional event wait after its dependencies arrived.

The frontier widths after t arrivals are exactly the descending powers of two occurring in the binary expansion of t. This is an invariant of the fixed equal-width fusion rule, not a delay selected to match a physical result.

## Exact partial arithmetic readout

All 65,536 pairs of eight-bit operands were tested, with eight sum bits and final carry (nine outputs). Input events are individual operand-bit arrivals. Three fixed input orders were used: LSB-first, MSB-first, and center-out (positions 3,4,2,5,1,6,0,7; operand a then b at each position).

Every output emitted at its first semantically settled event agreed with the independent full sum. Every output settled by event 16. Results are averages over all operand pairs and all nine output bits, not whole-program completion times:

- LSB-first mean event 9.7222222222; avoidable average wait under a blanket event-16 barrier 6.2777777778.
- MSB-first mean event 11.0021701389; avoidable average barrier wait 4.9978298611.
- Center-out mean event 11.8420138889; avoidable average barrier wait 4.1579861111.

LSB-first sum bit j always settles at event 2j+2. MSB-first final carry settles at event 2 for exactly 32,768 pairs: the two highest operand bits agree, so the lower carry cannot change the result. Its mean readiness event is 3.98046875. The whole sum still requires the last input event; early readiness is per output, not a claim that the entire addition completed at event 2.

There were also 256 actual ring phase/direction operand-pair settings. Direction/phase settings need not be distinct byte values.

## What is and is not measured

The hold here is unresolved output information, not an imposed eight-event release timer. Once an output is invariant over all completions, retaining a global barrier adds measurable event-index waiting. The ring bits and operator laws do not change between schedules.

The exhaustive completion calculation is the audit method for semantic readiness. It is not a claimed efficient implementation for arbitrarily wide constraints. Internal fold computation is modeled with no extra arrival-event delay; gate latency and physical time are not derived. Calling these holds physical reality remains a separate hypothesis.

## Provenance

The source and predictions were sealed before execution, with SHA-256 over literal bytes including the final newline. Both matched after execution. Source: 9972a199c70fd0d14c7fd19f0647e4abe2a6e523185c57ff7994d7e80d347903. Prediction: 81ed39a83ff869fecef77af77d397b84382a5e87dc9aeb2963194275cadac719.

Ledger: online lower-width closure and first-settled emission RUNS on the declared finite domains. Eight-slot activation is observed in this fixed closure rule, not established as a universal physical threshold. Static coordinate results remain unchanged. Physical reality/holding identification PULL.
