# Comparator imbalance closure audit

This bundle includes the updated running log and the comparator/Delta audit from the uploaded archive. The supplied source was re-executed; all assertions that the script runs passed. The exact source seal matches. The prediction digest matches the text after removing its terminal newline; the literal file hash is separately recorded in `rerun_provenance.json`.

Main result scope: 2,097,167 prefix thresholds across widths 2–20; 4,090 palindrome addresses; 90 wide scalar comparisons through width 1,024; and 64 width-20 tent spot checks. The borrow-cell exhaustive check ran through width 16, and the full tent reconstruction ran through width 12. False flags beyond those limits mean not executed.

The current running-log ledger keeps the seam cusp/smooth-closure claim OPEN; this stroke did not test it.
