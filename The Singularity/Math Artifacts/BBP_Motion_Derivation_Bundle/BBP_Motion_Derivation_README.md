# BBP Motion Derivation Bundle

The central result is the transition derived from BBP lane motion:

- local lane: `16r = dq + r'`
- crossing sum: `C_n = sum c_j sum q_(k,j,n-k)`
- aggregate state: `F_(n+1) = 16F_n - C_n`
- emitted digit: `a_(n+1) = C_n + floor(F_(n+1)) - 16 floor(F_n)`

`BBP_Motion_Derivation_Paper.docx` and `.md` explain the derivation. `bbp_motion_formula.py` is the finite-rational-seed recurrence implementation. Its 2,000-digit run matched an independent high-precision mpmath reference at all 2,000 positions in 6.46 seconds on the measured run; the trace is `bbp_motion_formula_trace_2000_final.csv`. The seed uses 2,096 BBP terms plus a rigorous geometric omitted-tail bound (96 guard terms beyond the requested output length).

`pending.py` and `accept.py` are the separate empty-field, interval-certified reader. Do not conflate its initialization and scheduling with the finite-seed recurrence driver.
