# NEXUS even-Delta spectrum audit

This package continues the Compiler Rings log by sealing and running the exact prefix-kernel formula for the Walsh spectrum of `Delta_n`, including the formerly open even-degree coefficients and zero mode.

Key outcomes:
- Kernel pairs checked: 86,868 at widths 2–8.
- Nonzero Delta Walsh modes checked: 8,177 across widths 2–12.
- Comparator Walsh coefficients checked against the analytic sparse expansion: 8,188 across widths 2–12.
- Zero-mode closed form checked against direct prefix-area sums: 19 widths, 2–20.
- Failed executed assertions: 0.

The updated `compiler_rings_log.md` appends the previously audited §10 full-body interior entry and §11 spectrum entry. The originally uploaded running log is preserved; this is a new copy. Seals use literal file bytes including final newlines.

Run `python even_delta_spectrum_audit.py` to reproduce the checks.
