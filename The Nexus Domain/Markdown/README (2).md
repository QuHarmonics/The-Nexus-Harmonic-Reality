# Walsh transport and palindrome-address review

## Result

**Mathematical verdict: PASS for the stated finite/combinatorial claims.** The uploaded main audit reruns successfully with the ring-order dependency made explicit. The exact matrix and carrier identities are consistent with the algebraic proof.

- Complete integer Walsh transport matrices at widths \(n=2,\ldots,12\): \(C^TC=NM I\) and opposite-parity entries are zero.
- Singleton-carrier reconstruction at every width \(n=2,\ldots,20\): exact coefficient-by-coefficient equality. At width 20, 10 transported columns reconstruct all 1,048,576 coefficients; 512,674 are nonzero.
- Width-five address formula: all eight inputs match \(i_5(u)=4u+2u_2+\operatorname{Maj}(1-u_0,u_1,u_2)\).
- Factored projector: exact coefficient recovery and output equality at widths 10, 11, 19, and 20.
- Scalar palindrome placement: 4,090/4,090 addresses pass against materialized original rings at widths 2–20. The earlier independent rank/location audit additionally passed 122 finite-width rank-DP samples and 40 wide prefix/seam samples through width 1,024.

## Source-seal / packaging detail

The main audit source hash matches the recorded SHA-256 exactly:

`ae92dcb15998c4a9a32d60565ce2f16b89916efa610e3dd7d8f58f66a0037ce9`

The prediction seal corresponds to the prediction text with its single terminal LF removed. The raw file including that final newline has hash `ab5237a0…8c166`; removing exactly that newline yields the recorded `6c81e47d…a96e0c`. This is a newline-normalization difference, not a body-text difference.

The submitted ZIP omits `pairs_forced.py`, even though the main audit opens that file to compare the original ring order. Consequently, the archive is not standalone-runnable as uploaded. For the rerun in this review, `support/pairs_forced.py` is copied from an earlier NEXUS ring audit and is labelled as a compatibility dependency, not claimed to be the original missing sealed file. The rerun explicitly confirms that it produces the same ring lists as the uploaded script for every word at widths 1–10.

The width-five majority and projection checks are post-main-run checks, as stated by the supplied report; they are stored separately and not backdated into the main prediction seal.

## Reproduce

The independent review verifier is self-contained relative to this folder and requires Python plus NumPy:

```bash
python scripts/independent_verify.py
```

To rerun the submitted audit source with the compatibility dependency supplied by this review:

```bash
bash rerun/run_original_audit.sh
```

The source bundle remains unchanged under `submitted/`. The independent scalar placement formula and the finite-state rectangle counter are explained in `gate_level_address.md`.

## Ledger

- Isometric character transport: **RUNS**.
- Parity preservation with degree mixing: **RUNS**.
- Width-five majority correction: **RUNS**.
- Exact m-column latitude carrier reconstruction: **RUNS**.
- Rank-m factored filter for the specified carrier family: **RUNS**.
- General minimized bit-level netlist for every address bit: **OPEN / next synthesis step**.
- Universal spectral nesting for arbitrary inputs, physical-spin interpretation, or SHA inversion: **not established by these checks**.
