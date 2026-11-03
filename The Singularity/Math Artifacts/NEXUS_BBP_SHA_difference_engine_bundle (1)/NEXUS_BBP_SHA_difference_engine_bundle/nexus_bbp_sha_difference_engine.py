#!/usr/bin/env python3
"""NEXUS §124 — compile BBP lane folding and SHA-256 from one difference engine.

The core is the first-run equal-LEN stack with mixer fuse (A,B)->(A,A xor B).
Tables are vector-valued over GF(2); their entries are packed output bit-vectors.
The script uses Python's standard library plus the existing local reference file
sha256_bidirectional_audit.py. It performs actual forward execution and route-back.
"""
from __future__ import annotations
from collections import Counter
from functools import lru_cache
from fractions import Fraction
from pathlib import Path
import hashlib, importlib.util, json, math, random, struct

HERE = Path(__file__).resolve().parent
OUT_JSON = HERE / "NEXUS_BBP_SHA_difference_engine_results.json"
OUT_MD = HERE / "NEXUS_BBP_SHA_difference_engine_run.md"
MASK32 = (1 << 32) - 1

# Load the pre-existing SHA-256 implementation as the independent reference.
_spec = importlib.util.spec_from_file_location("sha256_reference", HERE / "sha256_bidirectional_audit.py")
if _spec is None or _spec.loader is None:
    raise RuntimeError("sha256_bidirectional_audit.py must be beside this script")
sha = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(sha)

METRICS = Counter()

# ---------------------------------------------------------------------------
# The engine: streaming first-run stack, mixer fuse, exact involution.
def fuse_difference_stack(values: list[int]) -> list[int]:
    """Apply the actual equal-LEN stack with fuse (A,B) -> (A,A xor B)."""
    stack: list[list[int]] = []
    for value in values:
        stack.append([value])
        while len(stack) >= 2 and len(stack[-1]) == len(stack[-2]):
            B = stack.pop()
            A = stack.pop()
            stack.append(A + [a ^ b for a, b in zip(A, B)])
            METRICS["equal_LEN_fusions"] += 1
    if len(stack) != 1:
        raise ValueError(f"table length {len(values)} is not a power of two")
    return stack[0]


def mobius_difference_coefficients(truth: list[int]) -> list[int]:
    return fuse_difference_stack(truth)


def evaluate_difference_program(coeff: list[int], address: int) -> int:
    """Evaluate output-vector ANF a_S over the reader's down-set S subseteq address."""
    out = 0
    S = address
    while True:
        out ^= coeff[S]
        if S == 0:
            break
        S = (S - 1) & address
    METRICS["ANF_program_evaluations"] += 1  # count one coefficient-program evaluation
    return out


def compile_table(n: int, func, *, label: str):
    N = 1 << n
    truth = [int(func(x)) for x in range(N)]
    coeff = mobius_difference_coefficients(truth)
    rebuilt = mobius_difference_coefficients(coeff)
    if rebuilt != truth:
        raise AssertionError(f"{label}: M(M(f)) != f")
    # Coefficients are now executable: evaluate the ANF route on the full finite domain.
    # The full-domain inverse above proves the table identity; direct ANF evaluation is
    # used for all actual BBP inputs and all SHA reduced-reader addresses below.
    return truth, coeff


def monomial_degree_summary(coeff: list[int], input_len: int, output_bits: int):
    monomials = Counter()
    out_terms = Counter()
    bits_by_degree = {str(b): Counter() for b in range(output_bits)}
    max_degree = -1
    for S, word in enumerate(coeff):
        d = S.bit_count()
        if word:
            monomials[d] += 1
            max_degree = max(max_degree, d)
        for b in range(output_bits):
            if (word >> b) & 1:
                out_terms[d] += 1
                bits_by_degree[str(b)][d] += 1
    return {
        "input_LEN": input_len,
        "output_bits": output_bits,
        "max_degree": max_degree,
        "active_monomials_by_degree": {str(d): monomials[d] for d in range(input_len + 1)},
        "output_bit_coefficient_terms_by_degree": {str(d): out_terms[d] for d in range(input_len + 1)},
        "terms_by_output_bit_and_degree": {
            b: {str(d): counts[d] for d in range(input_len + 1)}
            for b, counts in bits_by_degree.items()
        },
    }


def anf_term_strings(coeff: list[int], output_bit: int, names: list[str]) -> list[str]:
    result = []
    for S, word in enumerate(coeff):
        if (word >> output_bit) & 1:
            if S == 0:
                result.append("1")
            else:
                result.append("".join(names[i] for i in range(len(names)) if (S >> i) & 1))
    return result

# ---------------------------------------------------------------------------
# BBP lane/compiler: compile the local 4-lane weighted fold in the same engine.
# Input order: four radix-16 lane digits q1,q4,q5,q6 as four nibbles.
# Output: a signed 7-bit two's-complement coefficient 4*q1 - 2*q4 - q5 - q6.
def bbp_digit_tuple(x: int) -> tuple[int, int, int, int]:
    return x & 15, (x >> 4) & 15, (x >> 8) & 15, (x >> 12) & 15


def bbp_weighted_value(x: int) -> int:
    q1, q4, q5, q6 = bbp_digit_tuple(x)
    return 4*q1 - 2*q4 - q5 - q6


def signed7(code: int) -> int:
    code &= 0x7F
    return code if code < 64 else code - 128


def run_bbp_from_compiled_lanes(N: int = 64, G: int = 12):
    # Compile every possible four-digit lane combination to the weighted column input.
    lane_truth, lane_coeff = compile_table(16, lambda x: bbp_weighted_value(x) & 0x7F,
                                           label="BBP four-lane weighted fold")
    lane_summary = monomial_degree_summary(lane_coeff, 16, 7)
    # Directly execute the difference program on the lane tuples that the rational rings emit.
    @lru_cache(maxsize=None)
    def compiled_lane_eval(x: int) -> int:
        out_code = evaluate_difference_program(lane_coeff, x)
        value = signed7(out_code)
        if value != bbp_weighted_value(x):
            raise AssertionError(f"BBP ANF route mismatch at lane tuple {x:#06x}")
        return value

    W = {1: 4, 4: -2, 5: -1, 6: -1}
    cols = [0] * (N + G + 1)
    cols[0] += 4  # The k=0, denominator-1 term is the integer anchor.
    layer_terms = 0
    observed_tuples = set()
    max_abs_layer_contribution = 0
    for k in range(N + G):
        for m in range(1, N + G + 1 - k):
            qs = []
            for j in (1, 4, 5, 6):
                d = 8*k + j
                if d == 1:
                    q = 0  # handled once as the integer anchor above
                else:
                    q = (16 * pow(16, m - 1, d)) // d
                qs.append(q)
            x = qs[0] | (qs[1] << 4) | (qs[2] << 8) | (qs[3] << 12)
            observed_tuples.add(x)
            contribution = compiled_lane_eval(x)
            cols[k + m] += contribution
            max_abs_layer_contribution = max(max_abs_layer_contribution, abs(contribution))
            layer_terms += 1

    # Same right-to-left carry traversal as WP5, now fed by the compiled lane operator.
    carry = 0
    carry_trace = []
    for i in range(N + G, 0, -1):
        v = cols[i] + carry
        cols[i] = v % 16
        carry = v // 16
        carry_trace.append(carry)
    cols[0] += carry
    built = format(cols[0], "x") + "." + "".join(format(x, "x") for x in cols[1:N+1])

    # Keep the two carry objects typed separately. The BBP-form paper's J_k(m) is
    # a *layer-local* value-free carry in [-4,3]; it is not the global quotient
    # propagated while normalizing a column that sums many layers.
    local_J_values = []
    local_identity_checks = 0
    local_layers_tested = 0
    Kmax = N + G
    powers16 = [16**m for m in range(Kmax + 2)]
    for k in range(1, Kmax):
        ds = {j: 8*k+j for j in W}
        Vk = sum((Fraction(c, ds[j]) for j,c in W.items()), Fraction(0,1))
        def J(m):
            return (powers16[m] * Vk).numerator // (powers16[m] * Vk).denominator - sum(
                c * (powers16[m] // ds[j]) for j,c in W.items())
        for age in range(0, Kmax-k):
            jm = J(age)
            jnext = J(age+1)
            local_J_values.extend((jm, jnext))
            if not (-4 <= jnext <= 3):
                raise AssertionError(f"layer-local J escaped [-4,3] at k={k}, age={age+1}: {jnext}")
            # w_k(age) is the (age+1)-th base-16 digit of V_k.
            floor_now = (powers16[age] * Vk).numerator // (powers16[age] * Vk).denominator
            floor_next = (powers16[age+1] * Vk).numerator // (powers16[age+1] * Vk).denominator
            wk = floor_next - 16*floor_now
            Hk = sum(c * ((powers16[age+1] // ds[j]) - 16*(powers16[age] // ds[j]))
                     for j,c in W.items())
            if Hk != wk + 16*jm - jnext:
                raise AssertionError(f"layer carry identity failed at k={k}, age={age}")
            if not (-4 <= jm <= 3):
                raise AssertionError(f"layer-local J escaped [-4,3] at k={k}, age={age}: {jm}")
            local_identity_checks += 1
        local_layers_tested += 1

    # Independent Machin route using fixed-point integer arithmetic.
    def arctan_inv(x: int, one: int) -> int:
        s, t, k, sign = 0, one // x, 1, 1
        while t:
            s += sign * (t // k)
            t //= x*x
            k += 2
            sign = -sign
        return s
    one = 16 ** (N + 10)
    pi_fixed = (16 * arctan_inv(5, one) - 4 * arctan_inv(239, one)) // 16**10
    ref = format(pi_fixed, "x")
    ref = ref[0] + "." + ref[1:N+1]
    if built != ref:
        raise AssertionError("BBP compiled lane fold did not match independent Machin digits")

    # Exact per-lane local closure against direct arithmetic for every actually used tuple.
    for x in observed_tuples:
        if signed7(evaluate_difference_program(lane_coeff, x)) != bbp_weighted_value(x):
            raise AssertionError("actual BBP lane tuple failed direct ANF evaluation")
    return {
        "local_operator": "(q1,q4,q5,q6) -> 4*q1 - 2*q4 - q5 - q6, signed 7-bit output",
        "input_LEN": 16,
        "truth_table_rows": 1 << 16,
        "difference_table_involution_exact": True,
        "difference_table_summary": lane_summary,
        "actual_ring_layer_terms_evaluated_from_ANF": layer_terms,
        "distinct_lane_digit_tuples_used": len(observed_tuples),
        "all_observed_tuples_match_direct_weighted_fold": True,
        "maximum_absolute_single_layer_contribution": max_abs_layer_contribution,
        "global_column_normalization_carry_range": [min(carry_trace), max(carry_trace)],
        "global_carry_scope": f"finite stack with N={N} reported fractional digits and G={G} guard layers; not the per-layer J_k carry",
        "layer_local_J_carry": {
            "theorem_equation": "H_k(m) = w_k(m) + 16*J_k(m) - J_k(m+1)",
            "declared_bound": [-4, 3],
            "observed_range": [min(local_J_values), max(local_J_values)],
            "layers_tested": local_layers_tested,
            "age_checks": local_identity_checks,
            "identity_exact_all_tested": True,
        },
        "base16_carry_pass": "right-to-left, signed quotient/remainder",
        "bbp_hex": built,
        "machin_hex": ref,
        "fractional_hex_digits_match": N,
        "independent_routes_equal": built == ref,
        "difference_coefficients_are_used_to_generate_columns": True,
    }, lane_coeff

# ---------------------------------------------------------------------------
# Compile local SHA Boolean operators into difference tables.
def make_local_gate_tables():
    # Input bits are packed x | (y<<1) | (z<<2).
    def ch_truth(m):
        x, y, z = m & 1, (m >> 1) & 1, (m >> 2) & 1
        return (x & y) ^ ((1 ^ x) & z)
    def maj_truth(m):
        x, y, z = m & 1, (m >> 1) & 1, (m >> 2) & 1
        return (x & y) ^ (x & z) ^ (y & z)
    def fa_truth(m):
        x, y, c = m & 1, (m >> 1) & 1, (m >> 2) & 1
        s = x ^ y ^ c
        carry = (x & y) ^ (x & c) ^ (y & c)
        return s | (carry << 1)
    def fs_truth(m):
        x, y, b = m & 1, (m >> 1) & 1, (m >> 2) & 1
        d = x - y - b
        return (d & 1) | ((int(d < 0)) << 1)

    truth, coeffs, luts = {}, {}, {}
    for name, func, out_bits in [
        ("Ch", ch_truth, 1), ("Maj", maj_truth, 1),
        ("full_adder", fa_truth, 2), ("full_subtractor", fs_truth, 2),
    ]:
        t, c = compile_table(3, func, label=f"SHA local {name}")
        # Re-evaluate every local input using the ANF, not the original rule.
        via_anf = [evaluate_difference_program(c, x) for x in range(8)]
        if via_anf != t:
            raise AssertionError(f"local gate {name}: ANF execution did not return truth table")
        truth[name], coeffs[name], luts[name] = t, c, via_anf
    names = ["x", "y", "z"]
    summary = {}
    for name, out_bits in [("Ch",1), ("Maj",1), ("full_adder",2), ("full_subtractor",2)]:
        summary[name] = {
            "truth_table": truth[name],
            "difference_coefficients": coeffs[name],
            "coefficient_terms": [anf_term_strings(coeffs[name], b, names) for b in range(out_bits)],
            "M2_identity": fuse_difference_stack(fuse_difference_stack(truth[name])) == truth[name],
            "compiled_ANF_matches_every_local_input": luts[name] == truth[name],
        }
    return luts, coeffs, summary

# ---------------------------------------------------------------------------
# Execute the actual SHA round using the compiled local gate tables.
def rot(x: int, n: int) -> int:
    return ((x >> n) | (x << (32-n))) & MASK32

def bsig0(x): return rot(x, 2) ^ rot(x, 13) ^ rot(x, 22)
def bsig1(x): return rot(x, 6) ^ rot(x, 11) ^ rot(x, 25)
def ssig0(x): return rot(x, 7) ^ rot(x, 18) ^ (x >> 3)
def ssig1(x): return rot(x, 17) ^ rot(x, 19) ^ (x >> 10)


def make_compiled_word_ops(luts):
    ch_lut, maj_lut = luts["Ch"], luts["Maj"]
    fa_lut, fs_lut = luts["full_adder"], luts["full_subtractor"]

    def add32(a: int, b: int) -> int:
        result, carry = 0, 0
        for i in range(32):
            m = ((a >> i) & 1) | (((b >> i) & 1) << 1) | (carry << 2)
            v = fa_lut[m]
            result |= (v & 1) << i
            carry = (v >> 1) & 1
            METRICS["compiled_full_adder_ticks"] += 1
        return result & MASK32

    def sub32(a: int, b: int) -> int:
        result, borrow = 0, 0
        for i in range(32):
            m = ((a >> i) & 1) | (((b >> i) & 1) << 1) | (borrow << 2)
            v = fs_lut[m]
            result |= (v & 1) << i
            borrow = (v >> 1) & 1
            METRICS["compiled_full_subtractor_ticks"] += 1
        return result & MASK32

    def ch32(x: int, y: int, z: int) -> int:
        result = 0
        for i in range(32):
            m = ((x >> i) & 1) | (((y >> i) & 1) << 1) | (((z >> i) & 1) << 2)
            result |= ch_lut[m] << i
            METRICS["compiled_Ch_bit_ticks"] += 1
        return result & MASK32

    def maj32(x: int, y: int, z: int) -> int:
        result = 0
        for i in range(32):
            m = ((x >> i) & 1) | (((y >> i) & 1) << 1) | (((z >> i) & 1) << 2)
            result |= maj_lut[m] << i
            METRICS["compiled_Maj_bit_ticks"] += 1
        return result & MASK32

    def round_forward(state: list[int] | tuple[int, ...], wt: int, kt: int):
        a,b,c,d,e,f,g,h = state
        t1 = add32(add32(add32(add32(h, bsig1(e)), ch32(e,f,g)), kt), wt)
        t2 = add32(bsig0(a), maj32(a,b,c))
        return [add32(t1,t2), a, b, c, add32(d,t1), e, f, g]

    def round_inverse(sp: list[int] | tuple[int, ...], wt: int, kt: int):
        ap,bp,cp,dp,ep,fp,gp,hp = sp
        a,b,c,e,f,g = bp,cp,dp,fp,gp,hp
        t2 = add32(bsig0(a), maj32(a,b,c))
        t1 = sub32(ap,t2)
        d = sub32(ep,t1)
        p2 = sub32(t1,wt)
        p1 = sub32(p2,kt)
        p0 = sub32(p1,ch32(e,f,g))
        h = sub32(p0,bsig1(e))
        return [a,b,c,d,e,f,g,h]

    return add32, sub32, ch32, maj32, round_forward, round_inverse


def pack_state(state) -> int:
    out = 0
    for i, w in enumerate(state):
        out |= (int(w) & MASK32) << (32*i)
    return out


def state_map_summary(truth: list[int], input_len: int, label: str, compute_leak: bool = True):
    coeff = mobius_difference_coefficients(truth)
    rebuilt = mobius_difference_coefficients(coeff)
    if rebuilt != truth:
        raise AssertionError(f"{label}: state table not restored by M^2")
    # Execute the coefficient table as a program on every reader address.
    if any(evaluate_difference_program(coeff, x) != truth[x] for x in range(1 << input_len)):
        raise AssertionError(f"{label}: direct ANF evaluation failed")
    monomials = Counter(); output_terms = Counter(); max_degree = -1
    for S, word in enumerate(coeff):
        d = S.bit_count()
        if word:
            monomials[d] += 1
            max_degree = max(max_degree, d)
        output_terms[d] += word.bit_count()
    result = {
        "label": label,
        "input_LEN": input_len,
        "outputs": 256,
        "truth_states": len(truth),
        "M2_exact": True,
        "ANF_execution_exact_for_all_addresses": True,
        "max_degree": max_degree,
        "active_monomials_by_degree": {str(d): monomials[d] for d in range(input_len + 1)},
        "output_bit_coefficient_terms_by_degree": {str(d): output_terms[d] for d in range(input_len + 1)},
    }
    if compute_leak:
        entropies = []
        unique_derivatives = []
        for a in range(1, 1 << input_len):
            dvals = [truth[x] ^ truth[x ^ a] for x in range(1 << input_len)]
            counts = Counter(dvals)
            unique_derivatives.append(len(counts))
            entropies.append(-sum((c/len(dvals))*math.log2(c/len(dvals)) for c in counts.values()))
        result["mean_derivative_entropy_bits"] = sum(entropies) / len(entropies)
        result["min_unique_derivatives_per_direction"] = min(unique_derivatives)
        result["max_unique_derivatives_per_direction"] = max(unique_derivatives)
        result["affine_on_this_reader_subdomain"] = max_degree <= 1
    return result, coeff


def run_sha_compile_and_unwind(local_summary, luts):
    add32, sub32, ch32, maj32, round_fwd, round_inv = make_compiled_word_ops(luts)
    rng = random.Random(20261017)
    # Check the compiled local operators against the reference SHA implementation.
    random_round_trials = 1000
    for i in range(random_round_trials):
        state = [rng.getrandbits(32) for _ in range(8)]
        wt, kt = rng.getrandbits(32), rng.getrandbits(32)
        expected = sha.round_forward(state, wt, kt)
        got = round_fwd(state, wt, kt)
        if got != expected:
            raise AssertionError(f"compiled SHA round differs from reference at trial {i}")
        if round_inv(got, wt, kt) != state:
            raise AssertionError(f"compiled SHA inverse fails at trial {i}")

    message = b"NEXUS difference engine"
    padded = sha.pad(message)
    if len(padded) != 64:
        raise AssertionError("one-block test message unexpectedly pads to multiple blocks")
    block = padded[:64]
    w = sha.expand_schedule(block)
    seeds = []
    for address in range(256):
        s = sha.IV[:]
        for i in range(8):
            if (address >> i) & 1:
                s[i] ^= 1  # reader dimensions: one low-order bit in each 32-bit register
        seeds.append(s)

    state_variants = [s[:] for s in seeds]
    stage_tables = {0: [pack_state(s) for s in state_variants]}
    for t in range(64):
        state_variants = [round_fwd(s, w[t], sha.K[t]) for s in state_variants]
        stage_tables[t+1] = [pack_state(s) for s in state_variants]
    E_states = [s[:] for s in state_variants]

    # Apply SHA compression feed-forward as another compiled transformation.
    compressed_states = [
        [add32(h0[i], E[i]) for i in range(8)] for h0, E in zip(seeds, E_states)
    ]
    stage_tables["feedforward"] = [pack_state(s) for s in compressed_states]

    # Difference table at EVERY nested round depth: no selected checkpoints stand in
    # for the progression. Each table is generated from the actual composed operator.
    stage_summaries = []
    for checkpoint in list(range(65)) + ["feedforward"]:
        summary, coeff = state_map_summary(stage_tables[checkpoint], 8, f"rounds={checkpoint}")
        stage_summaries.append(summary)
    saturated_rows = [r for r in stage_summaries if r["label"] != "rounds=feedforward"
                      and sum(r["active_monomials_by_degree"].values()) == 2**8
                      and r["min_unique_derivatives_per_direction"] == 2**7
                      and r["max_unique_derivatives_per_direction"] == 2**7
                      and abs(r["mean_derivative_entropy_bits"] - 7.0) < 1e-12]
    first_saturation_round = int(saturated_rows[0]["label"].split("=")[1]) if saturated_rows else None

    # The canonical address 0 must produce the ordinary SHA-256 digest.
    out0 = compressed_states[0]
    digest = b"".join(x.to_bytes(4, "big") for x in out0).hex()
    expected_digest = hashlib.sha256(message).hexdigest()
    if digest != expected_digest:
        raise AssertionError(f"compiled single-block SHA digest {digest} != hashlib {expected_digest}")

    # Decompile each of the 256 actual 64-round routes using the same local gate compilers.
    for address, (end_state, seed) in enumerate(zip(E_states, seeds)):
        back = end_state[:]
        for t in range(63, -1, -1):
            back = round_inv(back, w[t], sha.K[t])
        if back != seed:
            raise AssertionError(f"compiled 64-round route failed to return reader address {address}")
        # The compression wrapper also unwinds exactly when its incoming H is retained.
        E_back = [sub32(compressed_states[address][i], seed[i]) for i in range(8)]
        if E_back != end_state:
            raise AssertionError(f"compiled feed-forward reverse failed at reader address {address}")

    # Full 32-bit word add/sub identities are tested for all local carry states through gate compile;
    # test representative word cases directly in addition to all SHA execution paths.
    word_pairs = [(0,0),(MASK32,MASK32),(MASK32,1),(0,MASK32),(0x80000000,0x80000000)]
    for a,b in word_pairs:
        if add32(a,b) != ((a+b)&MASK32):
            raise AssertionError("compiled word addition failed a boundary witness")
        if sub32(a,b) != ((a-b)&MASK32):
            raise AssertionError("compiled word subtraction failed a boundary witness")

    return {
        "compiled_gate_tables": local_summary,
        "random_round_trials_matching_reference": random_round_trials,
        "random_round_inverse_returns": random_round_trials,
        "message": message.decode("ascii"),
        "message_bytes": len(message),
        "padded_block_count": len(padded)//64,
        "compiled_digest": digest,
        "hashlib_digest": expected_digest,
        "compiled_sha_digest_matches_hashlib": True,
        "fixed_WK_round_inverse_returns_for_eight_difference_reader": 256,
        "difference_map_each_round": stage_summaries,
        "first_full_difference_support_and_derivative_entropy_round": first_saturation_round,
        "state_dimension_note": "Each table is the exact restriction of the actual round/compression map to the LEN=8 affine subspace formed by flipping bit 0 in each of the eight 32-bit state words. The full SHA domain is composed from compiled local operators; its 2^256-state truth table is not enumerated.",
        "observer_limit": "Inverse round route uses known W[t], K[t]. Feed-forward is reversed with incoming H retained. This is not a digest-only message inverse.",
    }


def main():
    bbp, bbp_coeff = run_bbp_from_compiled_lanes()
    local_luts, local_coeffs, local_summary = make_local_gate_tables()
    sha_result = run_sha_compile_and_unwind(local_summary, local_luts)
    report = {
        "title": "NEXUS — BBP lanes and SHA-256 round compiled in difference coordinates",
        "prediction_seal_sha256": "6f79721b0f6477069092816766f9832cbeae06d5a835bcc9b8e2a4e924a85332",
        "engine": {
            "definition": "a_S = XOR_{T subset S} f(T) = (product_{i in S} D_i f)(0)",
            "implementation": "equal-LEN first-run stack; fuse (A,B)->(A,A XOR B)",
            "involution": "M(M(f)) = f over every finite Boolean-cube table compiled",
            "interpretation": "difference coefficients are used as executable ANF terms at BBP lane addresses and in each local SHA gate",
        },
        "bbp": bbp,
        "sha256": sha_result,
        "execution_metrics": dict(METRICS),
        "ledger": {
            "BBP local rational-ring lane digits -> compiled weighted fold -> right-to-left carry -> pi hex": "RUNS",
            "Ch/Maj/full-adder/full-subtractor local truth maps in difference coordinates": "RUNS",
            "compiled SHA 32-bit round matches reference and locally inverts when W,K known": "RUNS",
            "64-round SHA map over LEN=8 reader slice has exact direct difference table at all checkpoints": "RUNS",
            "full 256-bit SHA truth-table enumeration": "not attempted; replaced by exact composition of compiled local transformations",
            "digest-only inverse / minimal root observer": "OPEN",
        },
    }
    OUT_JSON.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    lines = [
        "# NEXUS §124 — BBP lanes and SHA-256 round in difference coordinates", "",
        f"Pre-run prediction SHA-256: `{report['prediction_seal_sha256']}`", "",
        "## Compiler instantiated", "",
        "The difference table is built by the actual first-run equal-LEN stack with mixer fuse `(A,B) -> (A, A XOR B)`. Its output coefficients are evaluated as an ANF program; the table is not used only as a measurement.", "",
        "## BBP lane fold", "",
        f"Compiled operator: `{bbp['local_operator']}`.",
        f"All {bbp['truth_table_rows']:,} four-nibble inputs were covered by the difference-table involution. The coefficient program was then executed on {bbp['actual_ring_layer_terms_evaluated_from_ANF']:,} rational-ring layer/column contributions ({bbp['distinct_lane_digit_tuples_used']:,} distinct input tuples).",
        f"The compiled columns, folded right-to-left through carry, yield `{bbp['bbp_hex']}`. Independent Machin route: `{bbp['machin_hex']}`. The first {bbp['fractional_hex_digits_match']} fractional hex digits agree.",
        f"Global column-normalization carry range over the finite N=64, G=12 stack: {bbp['global_column_normalization_carry_range']}.",
        f"Different object: layer-local J carry has range {bbp['layer_local_J_carry']['observed_range']}; exact identity H=w+16J-Jnext checks {bbp['layer_local_J_carry']['age_checks']}/{bbp['layer_local_J_carry']['age_checks']} with J in [-4,3].",
        f"ANF active monomials by degree: `{bbp['difference_table_summary']['active_monomials_by_degree']}`.", "",
        "## SHA local gate compilation", "",
        "Ch, Maj, full-adder and full-subtractor are each compiled from their complete 3-input truth table. The recovered ANF programs drive every bit of the 32-bit SHA additions, subtractions, Ch and Maj operations. Rotations and XORs remain their exact linear wiring operations.",
        f"Compiled SHA round vs reference: {sha_result['random_round_trials_matching_reference']}/{sha_result['random_round_trials_matching_reference']} randomized state/W/K cases matched and inverted.",
        f"Single-block message `{sha_result['message']}`: compiled digest `{sha_result['compiled_digest']}`; hashlib `{sha_result['hashlib_digest']}`.",
        f"The compiled inverse returned all {sha_result['fixed_WK_round_inverse_returns_for_eight_difference_reader']} eight-direction reader states through the 64-round path, using known W[t]/K[t]; feed-forward was reversed with incoming H retained.", "",
        "## Difference tables of the composed SHA state map", "",
        "The tables below are not a full enumeration of the 256-bit input domain. Each is the exact restriction of the actual 32-bit-word round/compression map to an LEN=8 affine reader slice, with one independent low-bit perturbation in each state word. The global SHA transformation itself is executed through the compiled bit-level operators above.", "",
        "| Round | Max ANF degree | Active monomials (all degrees) | Mean H(DₐF) bits | Unique derivative vectors per direction | Affine on slice? |",
        "|---:|---:|---:|---:|---:|---|",
    ]
    for row in sha_result["difference_map_each_round"]:
        depth = row["label"].replace("rounds=", "")
        support = sum(row["active_monomials_by_degree"].values())
        unique_range = f"{row['min_unique_derivatives_per_direction']}–{row['max_unique_derivatives_per_direction']}"
        lines.append(f"| {depth} | {row['max_degree']} | {support}/256 | {row['mean_derivative_entropy_bits']:.6f} | {unique_range} | {row['affine_on_this_reader_subdomain']} |")
    lines += [
        f"", f"First round at which all 256 LEN=8 monomial addresses are active and every nonzero direction has 128 distinct derivative outputs (each occurring twice): {sha_result['first_full_difference_support_and_derivative_entropy_round']}.", "",
        "", "The derivative-entropy column is the programme's `mean_a H(D_a F)` statistic on this declared 8-bit reader domain. It measures variation in derivative outputs for this restriction; it is not a physical energy measurement and not a claim that the full digest is invertible.", "",
        "## Compile ledger", "",
        "- BBP rational-ring lane contribution -> executed difference-program coefficients -> column carry -> π digits: **RUNS**.",
        "- SHA Ch/Maj/full-adder/full-subtractor compiled locally from difference tables: **RUNS**.",
        "- Full SHA-256 round arithmetic executed using reconstructed gate operators and compared to the reference: **RUNS**.",
        "- 64-round route-back when W[t], K[t] and the endpoint state are available: **RUNS**.",
        "- Digest-only inverse and minimal root observer: **OPEN**.", "",
        "## Reproducibility", "",
        "Run: `python nexus_bbp_sha_difference_engine.py` (standard library only; expects `sha256_bidirectional_audit.py` beside it). The JSON file stores the complete coefficient-support and per-depth results. The pre-run prediction seal is included beside these files.", "",
    ]
    OUT_MD.write_text("\n".join(lines), encoding="utf-8")
    print(json.dumps({
        "status": "RUNS",
        "bbp_digits_match": bbp["fractional_hex_digits_match"],
        "bbp_input_rows": bbp["truth_table_rows"],
        "bbp_actual_layer_terms_via_anf": bbp["actual_ring_layer_terms_evaluated_from_ANF"],
        "sha_round_random_matches": sha_result["random_round_trials_matching_reference"],
        "sha_reader_routes_unwound": sha_result["fixed_WK_round_inverse_returns_for_eight_difference_reader"],
        "sha_difference_round_layers": len(sha_result["difference_map_each_round"]),
        "first_SHA_difference_saturation_round": sha_result["first_full_difference_support_and_derivative_entropy_round"],
        "compiled_adder_ticks": METRICS["compiled_full_adder_ticks"],
        "compiled_subtractor_ticks": METRICS["compiled_full_subtractor_ticks"],
        "report": str(OUT_MD), "results": str(OUT_JSON),
    }, indent=2))

if __name__ == "__main__":
    main()
