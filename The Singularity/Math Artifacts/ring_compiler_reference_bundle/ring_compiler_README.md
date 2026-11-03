# Fixed-ring reference compiler

This adds a small textual front end to the earlier cycle-list prototype. It is not represented as a previously existing parser. The source denotes the original ring ordering and carries width and framing explicitly. It does not silently accept arbitrary permutations as the original ring.

## Source and target

See ring_source_grammar.ebnf. R3_cycle.ring and R3_fold.ring are two valid source encodings of the same ring. The folded input is normalized by A || reverse(A xor D), innermost reference first. The semantic IR is then identical, as is the generated target Python.

ring_target_boolean_grammar.ebnf describes the emitted Boolean kernels, not the whole Python language. Python wrappers validate integer input, extract n input bits, evaluate XOR/AND kernels and pack n output bits. R3_target.py contains both directions.

## IR

R3_ir.json contains word width, cycle, successor/predecessor/partner tables, and ANF monomial masks. Input mask bit k refers to the kth bit from LSB. Mask zero represents the constant-one monomial. Output lists are MSB first. For n=3 masks 4,2,1 are a,b,c; mask 6 is ab. Fold parsing/unfolding has its own front-end trace, R3_fold_frontend_trace.json; that source-representation metadata is kept outside the semantic IR.

## Audit

The two encodings produce byte-identical targets at every tested width 1 through 8. All 510 states passed generated forward and inverse transitions, two-way returns and reflection covariance. Nine malformed source cases and ten invalid runtime calls were rejected. Width 13 also exercised the configured resource cap; that is a resource policy, not mathematical invalidity. MAX_WIDTH=12 protects this deliberately table-based reference implementation. No claim of scalability or universal language completeness is made.

Every n-bit pattern is a valid runtime state. Invalid calls are out-of-width values or wrong types. No masking, wrapping or string coercion is performed. The valid R3 edge 111 wraps to 000; it is not an error. The zero state advances to 001.

## Reproduce

Extract the bundle into one directory and run:

    python run_reference_tests.py

Only the Python standard library is needed. The original pairs_forced.py is included for the verifier to read its two function definitions; its large top-level audit is not executed. New result files are written under output/.

Compiler and test source checksums were recorded before testing and verified afterward. The convenience runner, grammar documents and generated target are derivative artifacts, not a byte-identical copy of the sealed compiler module.
