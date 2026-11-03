#!/usr/bin/env python3
"""Reproduce the Walsh transport checks and bridge to the scalar address law.

The uploaded main audit expects pairs_forced.py, which is absent from the input ZIP.
This review bundle supplies a prior ring-order implementation under support/ and
records that provenance in README.md. The user's sealed main source is not edited.
"""
from __future__ import annotations
import hashlib, importlib.util, json, sys, time, zipfile
from pathlib import Path
import numpy as np
ROOT = Path(__file__).resolve().parents[1]
start = time.perf_counter()

def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod

A = load('walsh_transport_audit', ROOT/'submitted'/'walsh_transport_audit.py')
P = load('palindrome_halfword_address', ROOT/'support'/'palindrome_halfword_address.py')
R = load('pairs_forced', ROOT/'support'/'pairs_forced.py')
seals = json.loads((ROOT/'submitted'/'walsh_transport_seals.json').read_text())
source_bytes = (ROOT/'submitted'/'walsh_transport_audit.py').read_bytes()
prediction_bytes = (ROOT/'submitted'/'walsh_transport_prediction.txt').read_bytes()
source_hash = hashlib.sha256(source_bytes).hexdigest()
prediction_raw_hash = hashlib.sha256(prediction_bytes).hexdigest()
prediction_without_final_newline_hash = hashlib.sha256(prediction_bytes[:-1] if prediction_bytes.endswith(b'\n') else prediction_bytes).hexdigest()
with zipfile.ZipFile(ROOT/'submitted'/'walsh_transport_bundle.zip') as zf:
    names = set(zf.namelist())
    archive_has_ring_dependency = any(Path(x).name == 'pairs_forced.py' for x in names)
assert source_hash == seals['source_sha256']
assert prediction_without_final_newline_hash == seals['prediction_sha256']
assert not archive_has_ring_dependency

# Check the ring ordering against the support implementation supplied from the
# earlier project artifact (not claimed to be the absent, original dependency).
ring_dependency_checks = 0
for n in range(1, 11):
    observed = [format(int(x), f'0{n}b') for x in A.ring(n)]
    expected = R.grow(n)
    assert observed == expected, f'ring mismatch at width {n}'
    ring_dependency_checks += len(observed)

# Compare the independent scalar palindrome address law with original-ring
# addresses at every half-word for widths 2..20.
placement = []
placement_count = 0
for n in range(2, 21):
    ring = A.ring(n)
    inv = np.empty(1 << n, dtype=np.int32)
    inv[ring] = np.arange(1 << n, dtype=np.int32)
    m = (n + 1)//2
    width_count = 1 << m
    for u in range(width_count):
        word = int(P.palindrome_word(n, u), 2)
        got = P.palindrome_address(n, u)
        exp = int(inv[word])
        assert got == exp, (n, u, got, exp)
        placement_count += 1
    placement.append({'n': n, 'half_words_checked': width_count, 'status': 'PASS'})

# Exact integer character-transport checks: C^T C = NM I and forbidden parity
# entries zero, complete Walsh cross matrices for widths 2..12.
complete = []
for n in range(2, 13):
    m = (n+1)//2
    N, M = 1 << n, 1 << m
    ring = A.ring(n)
    pal = ring == A.reverse(ring, n)
    pos = np.flatnonzero(pal)
    u = np.arange(M, dtype=np.uint32)
    degrees = A.wt(np.arange(N, dtype=np.uint32))
    small_degrees = A.wt(u)
    C = np.empty((N, M), dtype=np.int16)
    for t in range(M):
        f = np.zeros(N, dtype=np.int64)
        f[pos] = 1 - 2*(A.wt(u & np.uint32(t)) % 2).astype(np.int64)
        C[:, t] = A.fwht(f)
    assert np.array_equal(C.astype(np.int64).T @ C.astype(np.int64), N*M*np.eye(M, dtype=np.int64))
    bad = (degrees[:, None] % 2) != (small_degrees[None, :] % 2)
    assert not np.any(C[bad])
    max_terms = int(np.count_nonzero(C, axis=1).max())
    mixed_rows = int(np.count_nonzero(np.count_nonzero(C, axis=1) > 1))
    complete.append({'n': n, 'rows': N, 'columns': M, 'exact_gram': True,
                     'opposite_parity_entries_zero': True, 'rows_with_degree_mixing': mixed_rows,
                     'max_compressed_terms_in_any_row': max_terms})

# Exact singleton-column reconstruction of the palindrome latitude carrier for
# all widths 2..20, plus Gram orthogonality of the transported columns.
carrier_checks = []
for n in range(2, 21):
    m = (n+1)//2
    N, M = 1 << n, 1 << m
    ring = A.ring(n)
    pal = ring == A.reverse(ring, n)
    pos = np.flatnonzero(pal)
    u = np.arange(M, dtype=np.uint32)
    degrees = A.wt(np.arange(N, dtype=np.uint32))
    Z = (2*A.wt(ring)-n).astype(np.int64)
    coeff = np.array([-1 if (n % 2 and j == 0) else -2 for j in range(m)], dtype=np.int64)
    cols = np.empty((N, m), dtype=np.int16)
    predicted = np.zeros(N, dtype=np.int64)
    for j in range(m):
        f = np.zeros(N, dtype=np.int64)
        f[pos] = 1 - 2*((u >> np.uint32(j)) & np.uint32(1)).astype(np.int64)
        col = A.fwht(f)
        assert np.all(col[degrees % 2 == 0] == 0)
        cols[:, j] = col
        predicted += coeff[j]*col
    carrier = np.where(pal, Z, 0)
    direct = A.fwht(carrier)
    assert np.array_equal(predicted, direct)
    gram = cols.astype(np.int64).T @ cols.astype(np.int64)
    assert np.array_equal(gram, N*M*np.eye(m, dtype=np.int64))
    carrier_checks.append({'n': n, 'm': m, 'columns_used': m, 'coefficients': coeff.tolist(),
                           'coefficient_count': N, 'exact_reconstruction': True,
                           'orthogonal_columns': True, 'nonzero_carrier_coefficients': int(np.count_nonzero(direct))})

# Verify the n=5 majority truth table against original ring addresses.
n5_ring = A.ring(5)
n5_inv = np.empty(32, dtype=np.int32)
n5_inv[n5_ring] = np.arange(32, dtype=np.int32)
majority_rows = []
for u in range(8):
    u0, u1, u2 = u & 1, (u >> 1) & 1, (u >> 2) & 1
    a, b, c = 1-u0, u1, u2
    maj = int((a & b) | (a & c) | (b & c))
    formula = 4*u + 2*u2 + maj
    word = int(P.palindrome_word(5, u), 2)
    actual = int(n5_inv[word])
    assert formula == actual
    majority_rows.append({'u': u, 'word': format(word, '05b'), 'address': actual,
                          'majority_inputs': [a,b,c], 'majority_output': maj, 'status': 'PASS'})

# Factored projector from the uploaded post-run checker at four stated widths.
projection_checks = []
for n in (10, 11, 19, 20):
    m = (n+1)//2
    N, M = 1 << n, 1 << m
    ring = A.ring(n)
    pal = ring == A.reverse(ring, n)
    pos = np.flatnonzero(pal)
    u = np.arange(M, dtype=np.uint32)
    Z = (2*A.wt(ring)-n).astype(np.int64)
    F = A.fwht(Z)
    cols = np.empty((N,m), dtype=np.int16)
    for j in range(m):
        f = np.zeros(N, dtype=np.int64)
        f[pos] = 1 - 2*((u >> np.uint32(j)) & np.uint32(1)).astype(np.int64)
        cols[:,j] = A.fwht(f)
    Acols = cols.astype(np.int64)
    numerator = Acols.T @ F
    denom = N*M
    assert np.all(numerator % denom == 0)
    recovered = numerator // denom
    expected = np.array([-1 if (n%2 and j==0) else -2 for j in range(m)], dtype=np.int64)
    assert np.array_equal(recovered, expected)
    assert np.array_equal(Acols @ recovered, A.fwht(np.where(pal, Z, 0)))
    projection_checks.append({'n': n, 'reader_channels': m, 'recovered_coefficients': recovered.tolist(), 'exact': True})

result = {
  'status': 'PASS',
  'scope': 'Uploaded Walsh transport claims plus independent scalar palindrome placement check.',
  'integrity': {
    'source_sha256': source_hash,
    'source_hash_matches_record': True,
    'prediction_sha256_raw': prediction_raw_hash,
    'prediction_sha256_without_one_terminal_LF': prediction_without_final_newline_hash,
    'prediction_seal_matches_after_terminal_LF_removal': True,
    'zip_contains_required_pairs_forced_dependency': archive_has_ring_dependency,
    'rerun_dependency_note': 'The rerun uses support/pairs_forced.py from the earlier ring audit; this file is not present in the submitted ZIP and is not authenticated as the original omitted dependency.'
  },
  'ring_compatibility': {'words_compared': ring_dependency_checks, 'widths': '1..10', 'status': 'PASS'},
  'palindrome_scalar_placement': {'widths': placement, 'addresses_checked': placement_count,
                                  'wide_dp_crosscheck_from_prior_audit': json.loads((ROOT/'results'/'palindrome_placement_crosscheck.json').read_text())['wide_scalar_dp_checks'],
                                  'prior_crosscheck_widths_2_to_20_addresses': json.loads((ROOT/'results'/'palindrome_placement_crosscheck.json').read_text())['finite_palindrome_addresses'],
                                  'status': 'PASS'},
  'complete_character_matrices': complete,
  'singleton_carrier_reconstruction': carrier_checks,
  'majority_n5_truth_table': majority_rows,
  'factored_projector_checks': projection_checks,
  'seconds': time.perf_counter()-start
}
(ROOT/'results'/'independent_verify_results.json').write_text(json.dumps(result, indent=2)+'\n')
print(json.dumps({'status': result['status'], 'integrity': result['integrity'],
                  'ring_words_checked': ring_dependency_checks,
                  'palindrome_addresses_checked': placement_count,
                  'complete_matrix_widths': len(complete),
                  'carrier_widths': len(carrier_checks),
                  'n5_majority_rows': len(majority_rows),
                  'projector_widths': len(projection_checks),
                  'seconds': result['seconds']}, indent=2))
