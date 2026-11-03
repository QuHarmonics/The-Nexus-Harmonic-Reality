#!/usr/bin/env python3
"""Independent exact audit of the structured NEXUS address reader, widths 13-16.

The ring is reconstructed directly from P(x)=reverse(x) except complement on palindromes,
representatives x<P(x), reversed partner face, and the retained center swap. Readiness is
computed semantically from all input words consistent with each observed-bit mask.
"""
from __future__ import annotations
import csv, hashlib, importlib.util, itertools, json, math, time, sys
from fractions import Fraction
from pathlib import Path
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "outputs"
OUT.mkdir(parents=True, exist_ok=True)
T0 = time.time()
SEAL = ROOT / "prediction_seal.txt"
SOURCE = ROOT / "sources" / "wheels.py"
SOURCE_HASH_BEFORE = hashlib.sha256(SOURCE.read_bytes()).hexdigest()
spec = importlib.util.spec_from_file_location("sealed_wheels_source", SOURCE)
sealed_wheels = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = sealed_wheels
spec.loader.exec_module(sealed_wheels)
SEAL_HASH_BEFORE = hashlib.sha256(SEAL.read_bytes()).hexdigest()


def reverse_bits(x: int, n: int) -> int:
    r = 0
    for _ in range(n):
        r = (r << 1) | (x & 1)
        x >>= 1
    return r


def partner(x: int, n: int) -> int:
    r = reverse_bits(x, n)
    return r if r != x else ((1 << n) - 1) ^ x


def direct_ring(n: int):
    N = 1 << n
    P = [partner(x, n) for x in range(N)]
    reps = [x for x in range(N) if x < P[x]]
    assert len(reps) == N // 2
    ring = reps + [P[x] for x in reversed(reps)]
    if n > 1:
        mid = N // 2
        ring[mid - 1], ring[mid] = ring[mid], ring[mid - 1]
    loc = np.empty(N, dtype=np.int64)
    for i, x in enumerate(ring):
        loc[x] = i
    assert sorted(map(int, loc)) == list(range(N))
    assert all(P[P[x]] == x for x in range(N))
    return P, ring, loc


class ReadinessScorer:
    def __init__(self, n: int, loc: np.ndarray):
        self.n = n
        self.N = 1 << n
        self.x = np.arange(self.N, dtype=np.int64)
        self.loc = loc
        self.outbits = np.column_stack([((loc >> b) & 1).astype(np.int8) for b in range(n)])
        self.cache: dict[int, np.ndarray] = {}

    def unready_by_output_bit(self, mask: int) -> np.ndarray:
        if mask in self.cache:
            return self.cache[mask]
        keys = self.x & np.int64(mask)
        sizes = np.bincount(keys, minlength=self.N)
        bad_counts = np.zeros(self.n, dtype=np.int64)
        for b in range(self.n):
            ones = np.bincount(keys, weights=self.outbits[:, b], minlength=self.N)
            bad_groups = (ones != 0) & (ones != sizes)
            # Every input in a mixed-output observation class is still unready.
            bad_counts[b] = int(bad_groups[keys].sum())
        self.cache[mask] = bad_counts
        return bad_counts

    def score(self, order: tuple[int, ...] | list[int]):
        assert len(order) == self.n and sorted(order) == list(range(self.n))
        mask = 0
        sum_by_bit = np.zeros(self.n, dtype=np.int64)
        sum_by_bit += self.unready_by_output_bit(mask)
        for b in order[:-1]:
            mask |= 1 << b
            sum_by_bit += self.unready_by_output_bit(mask)
        total = int(sum_by_bit.sum())
        denom = self.N * self.n
        per_bit = [Fraction(int(v), self.N) for v in sum_by_bit]
        return {
            "score_event_sum": total,
            "mean_exact": str(Fraction(total, denom)),
            "mean_float": total / denom,
            "per_address_bit_mean_event_exact_lsb_output_indexed": [str(v) for v in per_bit],
            "per_address_bit_mean_event_float_lsb_output_indexed": [float(v) for v in per_bit],
        }


def outside_in_high_first(n: int) -> tuple[int, ...]:
    order=[]
    for j in range(n//2):
        order += [n-1-j, j]
    if n%2:
        order.append(n//2)
    return tuple(order)


def outside_in_low_first(n: int) -> tuple[int, ...]:
    order=[]
    for j in range(n//2):
        order += [j, n-1-j]
    if n%2:
        order.append(n//2)
    return tuple(order)


def hybrid_order(n: int, core_width: int, pair_orientations: tuple[int,...], core_order: tuple[int,...]):
    p=(n-core_width)//2
    out=[]
    for j in range(p):
        pair=(j,n-1-j)
        if pair_orientations[j]: pair=pair[::-1]
        out.extend(pair)
    core=tuple(range(p,n-p))
    out.extend(core[i] for i in core_order)
    assert len(out)==n and sorted(out)==list(range(n))
    return tuple(out)


def family_orders(n: int, core_width: int):
    p=(n-core_width)//2
    if p < 0 or (n-core_width)%2:
        raise ValueError("core width must match parity and fit")
    for orient in itertools.product((0,1), repeat=p):
        for perm in itertools.permutations(range(core_width)):
            yield hybrid_order(n,core_width,orient,perm)


def fraction_dict(score):
    return {"mean_exact":score["mean_exact"],"mean_float":score["mean_float"],"score_event_sum":score["score_event_sum"]}

results={
    "title":"Structured NEXUS address-reader audit, widths 13-16",
    "prediction_seal_sha256_before":SEAL_HASH_BEFORE,
    "definition":{
        "partner":"P(x)=reverse_n(x), unless x is a palindrome, then complement(x)",
        "ring":"sorted representatives x<P(x), followed by their partners in reverse representative order, then swap the two central entries",
        "address":"physical position loc[x] in that ring; address bits are indexed from least significant bit 0",
        "readiness":"for input x, address bit b is ready after k arrivals iff it is constant among all words agreeing with x on the k observed bit positions",
        "score":"exact average of event index across all 2^n input words and all n output address bits",
        "scope":"Exhaustive over every input word for each listed reader and over all structured-family orders; not exhaustive over all n! bit-arrival orders at widths 13-16."
    },
    "widths":{},
}
summary=[]; bit_rows=[]; family_rows=[]

for n in range(13,17):
    c=3 if n%2 else 4
    p=(n-c)//2
    P, ring, loc=direct_ring(n)
    _, _, Psrc, Rsrc, locsrc = sealed_wheels.ring_arrays(n)
    source_match = (P == list(map(int, Psrc)) and ring == list(map(int, Rsrc)) and list(map(int, loc)) == list(map(int, locsrc)))
    if not source_match:
        raise AssertionError(f"direct reconstruction differs from sealed wheels.py at width {n}")
    scorer=ReadinessScorer(n,loc)
    N=1<<n
    baseline_orders={
        "outside_in_high_first": outside_in_high_first(n),
        "outside_in_low_first": outside_in_low_first(n),
        "MSB_first_value_order": tuple(reversed(range(n))),
        "LSB_first": tuple(range(n)),
        "plain_value_core_hybrid": tuple([v for j in range(p) for v in (j,n-1-j)] + list(range(n-p-1,p-1,-1))),
    }
    # Search exactly the predeclared structured family: every outer-pair orientation
    # and every permutation of the 3- or 4-bit core.
    family=[]
    for order in family_orders(n,c):
        sc=scorer.score(order)
        family.append((sc["score_event_sum"],order,sc))
    best_score=min(q[0] for q in family)
    best=[q for q in family if q[0]==best_score]
    family.sort(key=lambda q:(q[0],q[1]))
    baseline={name:{"order_lsb_indexed":list(order),**scorer.score(order)} for name,order in baseline_orders.items()}
    best_local_core_orders=[]
    # Recompute width-3 or width-4 core's own local optimal input order independently.
    Pc,Rc,locc=direct_ring(c)
    core_scorer=ReadinessScorer(c,locc)
    core_scores=[]
    for cp in itertools.permutations(range(c)):
        cs=core_scorer.score(cp)
        core_scores.append((cs["score_event_sum"],cp,cs))
    core_min=min(v[0] for v in core_scores)
    best_local_core_orders=[list(q[1]) for q in core_scores if q[0]==core_min]
    local_core_choice=tuple(best_local_core_orders[0])
    local_recipe=hybrid_order(n,c,tuple(0 for _ in range(p)),local_core_choice)
    local_recipe_score=scorer.score(local_recipe)
    # Verify all words are covered by the observed-signature method and address is a permutation.
    assert len(set(map(int,loc)))==N
    width_result={
        "n":n,"N_inputs":N,"address_output_bits":n,"core_width":c,"outer_pair_count":p,
        "matches_sealed_wheels_source":source_match,
        "structured_family_order_count":len(family),
        "structured_family_minimizer_count":len(best),
        "structured_family_min_score":best_score,
        "structured_family_min_mean_exact":str(Fraction(best_score,N*n)),
        "structured_family_min_mean_float":best_score/(N*n),
        "first_32_minimizing_orders_lsb_indexed":[list(q[1]) for q in best[:32]],
        "all_minimizers_stored_in_csv":True,
        "local_core_width_min_mean_exact":str(Fraction(core_min,(1<<c)*c)),
        "local_core_width_minimizing_orders_lsb_indexed":best_local_core_orders,
        "local_core_choice_used_in_hybrid_lsb_indexed":list(local_core_choice),
        "local_core_recipe_order_lsb_indexed":list(local_recipe),
        "local_core_recipe_score":local_recipe_score,
        "baseline_readers":baseline,
        "plain_value_core_is_family_minimizer":baseline["plain_value_core_hybrid"]["score_event_sum"]==best_score,
        "local_core_recipe_is_family_minimizer":local_recipe_score["score_event_sum"]==best_score,
        "improvement_vs_full_outside_in_event_sum":baseline["outside_in_high_first"]["score_event_sum"]-best_score,
        "improvement_vs_MSB_first_event_sum":baseline["MSB_first_value_order"]["score_event_sum"]-best_score,
        "improvement_vs_plain_value_core_event_sum":baseline["plain_value_core_hybrid"]["score_event_sum"]-best_score,
        "family_all_orders_scored_exactly":True,
    }
    results["widths"][str(n)]=width_result
    for name,entry in baseline.items():
        summary.append({"width":n,"reader":name,"order_lsb_indexed":" ".join(map(str,entry["order_lsb_indexed"])),
                        "mean_exact":entry["mean_exact"],"mean_float":entry["mean_float"],
                        "score_event_sum":entry["score_event_sum"],"relative_to_family_minimum_event_sum":entry["score_event_sum"]-best_score,
                        "is_family_minimum":entry["score_event_sum"]==best_score})
        for b,(mf,ff) in enumerate(zip(entry["per_address_bit_mean_event_exact_lsb_output_indexed"],entry["per_address_bit_mean_event_float_lsb_output_indexed"])):
            bit_rows.append({"width":n,"reader":name,"address_output_bit_lsb_indexed":b,"mean_ready_event_exact":mf,"mean_ready_event_float":ff})
    summary.append({"width":n,"reader":"structured_family_minimum","order_lsb_indexed":";".join(" ".join(map(str,q[1])) for q in best),
                    "mean_exact":str(Fraction(best_score,N*n)),"mean_float":best_score/(N*n),
                    "score_event_sum":best_score,"relative_to_family_minimum_event_sum":0,"is_family_minimum":True})
    for b in range(n):
        vals=[q[2]["per_address_bit_mean_event_exact_lsb_output_indexed"][b] for q in best]
        nums=[Fraction(s) for s in vals]
        # Different minimizers could have different per-bit distributions; preserve range.
        bit_rows.append({"width":n,"reader":"structured_family_minimum_first_tie_only","address_output_bit_lsb_indexed":b,
                         "mean_ready_event_exact":vals[0],"mean_ready_event_float":float(nums[0]),
                         "minimizer_tie_range_exact":"..".join([str(min(nums)),str(max(nums))])})
    for rank,(score,order,sc) in enumerate(family):
        family_rows.append({"width":n,"family_rank_by_score":rank+1,"core_width":c,"order_lsb_indexed":" ".join(map(str,order)),
                            "score_event_sum":score,"mean_exact":str(Fraction(score,N*n)),"mean_float":score/(N*n),
                            "is_minimizer":score==best_score})
    print(f"n={n} family={len(family)} best={Fraction(best_score,N*n)} ties={len(best)} plain-core={baseline['plain_value_core_hybrid']['mean_exact']} local-core={local_recipe_score['mean_exact']} outside-in={baseline['outside_in_high_first']['mean_exact']} msb={baseline['MSB_first_value_order']['mean_exact']}",flush=True)

seal_hash_after=hashlib.sha256(SEAL.read_bytes()).hexdigest()
results["prediction_seal_sha256_after"]=seal_hash_after
results["source_wheels_sha256_before"]=SOURCE_HASH_BEFORE
results["source_wheels_sha256_after"]=hashlib.sha256(SOURCE.read_bytes()).hexdigest()
results["source_wheels_unchanged"]=results["source_wheels_sha256_before"]==results["source_wheels_sha256_after"]
results["prediction_seal_unchanged"]=seal_hash_after==SEAL_HASH_BEFORE
results["elapsed_seconds"]=time.time()-T0
# Explicit outcomes versus sealed predictions.
results["predictions"]={
    "structured_family_beats_full_outside_in_and_MSB_first_at_all_target_widths":all(
        r["improvement_vs_full_outside_in_event_sum"]>0 and r["improvement_vs_MSB_first_event_sum"]>0
        for r in results["widths"].values()),
    "plain_value_core_is_family_minimizer_all_target_widths":all(r["plain_value_core_is_family_minimizer"] for r in results["widths"].values()),
    "global_optimality_over_all_n_factorial_orders_established":False,
}
(OUT/"address_reader_width13_16_results.json").write_text(json.dumps(results,indent=2))
for fname, rows in [("address_reader_summary.csv",summary),("address_reader_per_output_bit.csv",bit_rows),("address_reader_structured_family.csv",family_rows)]:
    with (OUT/fname).open("w",newline="") as f:
        fieldnames=list(dict.fromkeys(k for row in rows for k in row.keys()))
        writer=csv.DictWriter(f,fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader();writer.writerows(rows)
print("PREDICTIONS",json.dumps(results["predictions"],sort_keys=True),flush=True)
print("SEAL",SEAL_HASH_BEFORE,seal_hash_after,"unchanged",results["prediction_seal_unchanged"],flush=True)
print("SOURCE",SOURCE_HASH_BEFORE,results["source_wheels_sha256_after"],"unchanged",results["source_wheels_unchanged"],flush=True)
print("ELAPSED",round(results["elapsed_seconds"],3),flush=True)
