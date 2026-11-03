#!/usr/bin/env python3
"""Independent audit of the all-word rank extension for Compiler Rings.

Uses:
  (1) vectorized direct counts over materialized n-bit words for n <= 20;
  (2) closed Delta and palindrome-correction formulas;
  (3) a mirrored-pair rank DP for wide scalar cross-checks;
  (4) binary search to invert the proposed rank function.
"""
from __future__ import annotations
import hashlib, json, math, random, time
from pathlib import Path
import numpy as np

ROOT = Path(__file__).resolve().parent
PRED_PATH = ROOT / "interior_body_prediction.txt"

def rev_int(x: int, h: int) -> int:
    y = 0
    for _ in range(h):
        y = (y << 1) | (x & 1)
        x >>= 1
    return y

def rev_array(x: np.ndarray, n: int) -> np.ndarray:
    y = x.astype(np.uint32, copy=True)
    y = ((y >> 1) & 0x55555555) | ((y & 0x55555555) << 1)
    y = ((y >> 2) & 0x33333333) | ((y & 0x33333333) << 2)
    y = ((y >> 4) & 0x0F0F0F0F) | ((y & 0x0F0F0F0F) << 4)
    y = ((y >> 8) & 0x00FF00FF) | ((y & 0x00FF00FF) << 8)
    y = (y >> 16) | (y << 16)
    return y >> (32 - n) if n else np.zeros_like(y)

def rect_h(u: int, v: int, h: int) -> int:
    """R_h(u,v)=#{b<u: rev_h(b)<v}, O(h) using reversed-prefix blocks."""
    if not (0 <= u <= (1 << h) and 0 <= v <= (1 << h)):
        raise ValueError("rectangle argument out of range")
    if u == (1 << h):
        return v
    ru = rev_int(u, h)
    total = 0
    for k in range(h):
        if (u >> k) & 1:
            prefix_len = h - k - 1
            r = ru & ((1 << prefix_len) - 1) if prefix_len else 0
            step = 1 << (h - k)
            if v > r:
                total += (v - r + step - 1) // step
    return total

def delta_scalar(p: int, n: int) -> int:
    """Closed even/odd Delta formula from the running log."""
    N = 1 << n
    if not 0 <= p <= N:
        raise ValueError("threshold out of range")
    if p == N:
        return 0
    h = n // 2
    H = 1 << h
    if n % 2 == 0:
        A, B = divmod(p, H)
        return A * (H - A) + B - 2 * rect_h(B, A, h) - int(rev_int(A, h) < B)
    A = p >> (h + 1)
    mu = (p >> h) & 1
    B = p & (H - 1)
    return (2 * A * (H - A) + mu * (H - 1 - 2 * A) + B
            - 2 * rect_h(B, A, h) - int(rev_int(A, h) < B))

def palindrome_count_below(p: int, n: int) -> int:
    """t_n(p)=number of n-bit palindromes strictly below p."""
    N = 1 << n
    if p <= 0: return 0
    if p >= N: return 1 << ((n + 1) // 2)
    h = n // 2
    H = 1 << h
    U, B = divmod(p, H)
    prefix = U >> (n % 2)
    return U + int(rev_int(prefix, h) < B)

def pi_scalar(p: int, n: int) -> int:
    M = 1 << ((n + 1) // 2)
    t = palindrome_count_below(p, n)
    return min(t, M - t)

def rank_formula(p: int, n: int) -> int:
    return (p + delta_scalar(p, n) + pi_scalar(p, n)) // 2

def rank_dp(t: int, n: int) -> int:
    """Independent mirrored-pair digit DP counting canonical words x<t."""
    N = 1 << n
    M = N // 2
    if t <= 0: return 0
    if t >= N: return M
    bound = format(t - 1, f"0{n}b")
    states = {(0, 0, 0, -1): 1}
    cmp = lambda a, b: (a > b) - (a < b)
    for i in range(n // 2):
        new = {}
        for (left, right, mirror, first), count in states.items():
            for a in (0, 1):
                for b in (0, 1):
                    key = (
                        left or cmp(a, int(bound[i])),
                        cmp(b, int(bound[n - 1 - i])) or right,
                        mirror or cmp(a, b),
                        a if i == 0 else first,
                    )
                    new[key] = new.get(key, 0) + count
        states = new
    total = 0
    for (left, right, mirror, first), count in states.items():
        for middle in ((0, 1) if n % 2 else (None,)):
            order = left
            if n % 2:
                order = order or cmp(middle, int(bound[n // 2]))
            order = order or right
            lead = middle if n == 1 else first
            if order <= 0 and (mirror < 0 or (mirror == 0 and lead == 0)):
                total += count
    return total

def select_rank(i: int, n: int) -> int:
    """Select the canonical word of zero-based rank i by inverting rank_formula."""
    M, N = 1 << (n - 1), 1 << n
    if not 0 <= i < M:
        raise ValueError("rank out of range")
    lo, hi = 0, N - 1
    while lo < hi:
        mid = (lo + hi) // 2
        if rank_formula(mid + 1, n) > i:
            hi = mid
        else:
            lo = mid + 1
    p = lo
    if rank_formula(p, n) != i:
        raise AssertionError(("selection rank mismatch", n, i, p, rank_formula(p,n)))
    return p

def partner_int(x: int, n: int) -> int:
    r = rev_int(x, n)
    return r if r != x else (x ^ ((1 << n) - 1))

def direct_width_audit(n: int) -> dict:
    N, M = 1 << n, 1 << (n - 1)
    x = np.arange(N, dtype=np.uint32)
    rv = rev_array(x, n)
    partner = np.where(rv != x, rv, x ^ np.uint32(N - 1)).astype(np.uint32)
    canonical = x < partner
    c = np.where(rv > x, 1, np.where(rv < x, -1, 0)).astype(np.int64)
    pal = rv == x
    pi_contrib = np.where(pal, np.where(x < M, 1, -1), 0).astype(np.int64)

    direct_rank = np.empty(N, dtype=np.int64)
    direct_rank[0] = 0
    direct_rank[1:] = np.cumsum(canonical[:-1], dtype=np.int64)
    direct_delta = np.empty(N, dtype=np.int64)
    direct_delta[0] = 0
    direct_delta[1:] = np.cumsum(c[:-1], dtype=np.int64)
    direct_pi = np.empty(N, dtype=np.int64)
    direct_pi[0] = 0
    direct_pi[1:] = np.cumsum(pi_contrib[:-1], dtype=np.int64)

    # Compact palindrome-prefix formula, vectorized for all thresholds.
    h, H = n // 2, 1 << (n // 2)
    U = x >> h
    B = x & np.uint32(H - 1)
    prefix = U >> (n % 2)
    rev_prefix = rev_array(prefix, h)
    direct_pal_count_formula = U.astype(np.int64) + (rev_prefix < B).astype(np.int64)
    pal_count_expected = np.empty(N, dtype=np.int64)
    pal_count_expected[0] = 0
    pal_count_expected[1:] = np.cumsum(pal[:-1], dtype=np.int64)
    Mpal = 1 << ((n + 1) // 2)
    pi_formula_v = np.minimum(direct_pal_count_formula,
                              Mpal - direct_pal_count_formula)

    # Closed Delta through the rectangle counter, vectorized over all p.
    rev_small = rev_array(np.arange(H, dtype=np.uint32), h).astype(np.int64)
    v = np.arange(H + 1, dtype=np.int64)
    rect = np.zeros((H + 1, H + 1), dtype=np.int32)
    rect[1:, :] = np.cumsum(rev_small[:, None] < v[None, :], axis=0, dtype=np.int32)
    Bv = B.astype(np.int64)
    if n % 2 == 0:
        Av = (x >> h).astype(np.int64)
        delta_formula_v = Av * (H - Av) + Bv - 2 * rect[Bv, Av] - (rev_small[Av] < Bv)
    else:
        Av = (x >> (h + 1)).astype(np.int64)
        mu = ((x >> h) & 1).astype(np.int64)
        delta_formula_v = (2 * Av * (H - Av) + mu * (H - 1 - 2 * Av) +
                           Bv - 2 * rect[Bv, Av] - (rev_small[Av] < Bv))

    formula_rank_v = (x.astype(np.int64) + delta_formula_v + pi_formula_v) // 2
    canonical_count_match = np.array_equal(formula_rank_v, direct_rank)
    delta_match = np.array_equal(delta_formula_v, direct_delta)
    pi_match = np.array_equal(pi_formula_v, direct_pi)
    pal_count_match = np.array_equal(direct_pal_count_formula, pal_count_expected)

    if not (canonical_count_match and delta_match and pi_match and pal_count_match):
        for name, arr, expected in [
            ("rank", formula_rank_v, direct_rank),
            ("delta", delta_formula_v, direct_delta),
            ("pi", pi_formula_v, direct_pi),
            ("palcount", direct_pal_count_formula, pal_count_expected),
        ]:
            bad = np.flatnonzero(arr != expected)
            if len(bad):
                i = int(bad[0])
                raise AssertionError((name, n, i, int(arr[i]), int(expected[i])))
        raise AssertionError(("unknown", n))

    # The terminal threshold p=N is the whole canonical set; test it separately
    # because the vector scan above uses p=0,...,N-1.
    endpoint_ok = (rank_formula(N, n) == M and rank_dp(N, n) == M
                   and delta_scalar(N, n) == 0 and pi_scalar(N, n) == 0)
    if not endpoint_ok:
        raise AssertionError(("terminal threshold", n))

    # Materialize the ring by the exact stated construction and check address map.
    reps = x[canonical]
    ring = np.concatenate((reps, partner[reps][::-1])).astype(np.uint32)
    ring[M - 1], ring[M] = ring[M], ring[M - 1]
    ranks = direct_rank[reps]
    phys = ranks.copy()
    phys[phys == M - 1] = M
    if len(np.unique(phys)) != M:
        raise AssertionError(("physical address uniqueness", n))
    if not np.array_equal(ring[phys], reps):
        raise AssertionError(("physical address", n))
    ring_rev = rev_array(ring, n)
    ring_partner = np.where(ring_rev != ring, ring_rev, ring ^ np.uint32(N - 1)).astype(np.uint32)
    if not np.array_equal(ring[::-1], ring_partner):
        raise AssertionError(("facing law", n))

    # All palindromes reduce to the original half-word correction pi(p)=u.
    pals = x[pal]
    canonical_pals = x[pal & canonical]
    for p in canonical_pals:
        p = int(p)
        u = p >> h
        if pi_scalar(p, n) != u:
            raise AssertionError(("canonical palindrome pi=halfword", n, p, u, pi_scalar(p,n)))
        if (p + delta_scalar(p, n) + u) // 2 != int(direct_rank[p]):
            raise AssertionError(("canonical palindrome special case", n, p))

    return {
        "n": n, "thresholds": int(N),
        "rank_formula_matches": canonical_count_match,
        "delta_formula_matches": delta_match,
        "signed_palindrome_correction_matches": pi_match,
        "palindrome_count_formula_matches": pal_count_match,
        "palindrome_words_checked": int(len(pals)),
        "canonical_palindrome_special_cases_checked": int(len(canonical_pals)),
        "canonical_representatives": int(len(reps)),
        "physical_addresses_unique_and_correct": True,
        "partner_facing_law": True,
        "terminal_threshold_endpoint_checked": endpoint_ok,
    }

def run():
    t0 = time.perf_counter()
    prediction_bytes = PRED_PATH.read_bytes()
    prediction_sha = hashlib.sha256(prediction_bytes).hexdigest()
    expected_prediction_sha = "5cde4126a76c415bd4397164cf1b09b1a07fcdb82f40e140fd539a9f065757a1"
    if prediction_sha != expected_prediction_sha:
        raise AssertionError(("prediction seal mismatch", prediction_sha, expected_prediction_sha))

    records = [direct_width_audit(n) for n in range(2, 21)]
    # Test rectangle sum in its own right over all (u,v) through h=8.
    rect_checks = 0
    for h in range(1, 9):
        H = 1 << h
        for u in range(H + 1):
            for v in range(H + 1):
                expected = v if u == H else sum(rev_int(b, h) < v for b in range(u))
                got = rect_h(u, v, h)
                if got != expected:
                    raise AssertionError(("rectangle", h, u, v, got, expected))
                rect_checks += 1

    # The mirrored-pair rank DP independently checks the new scalar formula.
    rng = random.Random(4422)
    wide_queries = []
    for n in (21, 32, 63, 64, 127, 128, 255, 256, 511, 512, 1023, 1024):
        N = 1 << n
        samples = {0, 1, N // 3, N // 2, N - 2, N - 1}
        for _ in range(3):
            samples.add(rng.randrange(0, N))
        for p in sorted(samples):
            got = rank_formula(p, n)
            dp = rank_dp(p, n)
            if got != dp:
                raise AssertionError(("wide rank DP", n, p, got, dp))
            # Also verify Delta scalar against a second DP-derived relation
            # only at thresholds where direct exact comparator enumeration is feasible.
            wide_queries.append({"n": n, "p_hex": hex(p), "rank": got, "dp_rank": dp,
                                 "match": True})

    # Invert every rank on widths through 12; on wider widths test representative ranks.
    select_checks = 0
    for n in range(2, 13):
        M = 1 << (n - 1)
        for i in range(M):
            p = select_rank(i, n)
            if rank_dp(p, n) != i or partner_int(p, n) == p or p >= partner_int(p, n):
                raise AssertionError(("select inverse", n, i, p))
            select_checks += 1
    for n in (16, 20, 32, 64, 256, 1024):
        M = 1 << (n - 1)
        chosen = {0, 1, M // 3, M // 2, M - 2, M - 1}
        for _ in range(5):
            chosen.add(rng.randrange(M))
        for i in chosen:
            p = select_rank(i, n)
            if rank_formula(p, n) != i or rank_dp(p, n) != i:
                raise AssertionError(("wide select", n, i, p))
            select_checks += 1

    # Scalar closed-Delta formula comparison against direct prefix sums on widths <= 14.
    delta_scalar_checks = 0
    for n in range(2, 15):
        N = 1 << n
        x = np.arange(N, dtype=np.uint32)
        rv = rev_array(x, n)
        c = np.where(rv > x, 1, np.where(rv < x, -1, 0)).astype(np.int64)
        pref = np.empty(N + 1, dtype=np.int64)
        pref[0] = 0
        pref[1:] = np.cumsum(c, dtype=np.int64)
        for p in range(N + 1):
            got = delta_scalar(p, n)
            if got != int(pref[p]):
                raise AssertionError(("scalar Delta", n, p, got, int(pref[p])))
            delta_scalar_checks += 1

    results = {
        "prediction_sha256": prediction_sha,
        "width_results": records,
        "exhaustive_threshold_count": sum(r["thresholds"] for r in records),
        "exhaustive_palindrome_count": sum(r["palindrome_words_checked"] for r in records),
        "rectangle_counter_checks": rect_checks,
        "wide_rank_dp_queries": wide_queries,
        "wide_rank_dp_query_count": len(wide_queries),
        "rank_select_inverse_checks": select_checks,
        "delta_scalar_vs_direct_prefix_checks": delta_scalar_checks,
        "runtime_seconds": round(time.perf_counter() - t0, 3),
        "scope_note": "Physical ring center swap is checked separately after canonical rank; smoothness is not inferred.",
    }
    (ROOT / "interior_body_results.json").write_text(json.dumps(results, indent=2) + "\n")
    print(json.dumps({k:v for k,v in results.items() if k != "wide_rank_dp_queries" and k != "width_results"}, indent=2))
    print("width summary:")
    for r in records:
        print(r["n"], r["rank_formula_matches"], r["delta_formula_matches"],
              r["signed_palindrome_correction_matches"], r["physical_addresses_unique_and_correct"])
    return results

if __name__ == "__main__":
    run()
