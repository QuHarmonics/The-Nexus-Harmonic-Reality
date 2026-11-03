Real-constant prefix / ring-fold audit

Contents:
- Real_Constant_Ring_Fold_Audit.md: results, finite-scope limitations, and R4 seam correction.
- Real_Constant_Ring_Fold_Audit.csv: pi/phi/e prefixes at widths 8,16,32,64,128,256; exact ring locations, partner addresses, fold counts, and normalized errors against alpha-alpha^2/2.
- Real_Constant_Empty_Anchor_Offsets.csv: signed width-32 address offsets from the empty-hash word E3B0C442 and reflected-side reversal checks.
- Real_Constant_Ring_Fold_Audit_Summary.json: machine-readable checks.
- run_real_constant_fold_audit.py: reproducible script using the existing SHA256_Ring_Native_Run.py exact rank/partner/location definitions.

Important scope boundary: this verifies address/fold readout and the asymptotic fold-count approximation. It does not derive SHA-256's K_t sequence from pi, phi, e, or from K-sequence endpoints.
