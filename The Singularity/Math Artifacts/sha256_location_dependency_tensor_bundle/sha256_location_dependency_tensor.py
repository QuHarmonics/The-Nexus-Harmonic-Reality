#!/usr/bin/env python3
"""Derive the SHA-256 word-level location-dependency tensor from schedule and round wiring.

This is a static may-dependence / taint analysis at 32-bit word granularity.
It tracks which original schedule words can feed each expanded schedule word and
which originals can feed each state register after each round. It does not assert
that every concrete input causes every dependent value to differ.
"""
from __future__ import annotations
import csv
import json
import zipfile
from pathlib import Path

OUT = Path(__file__).resolve().parent
REGISTERS = "abcdefgh"
SOURCE_WORDS = 16
ROUNDS = 64

# Each original schedule word W[0..15] is itself one distinct source location.
schedule_deps: list[set[int]] = [{j} for j in range(SOURCE_WORDS)]
for t in range(16, ROUNDS):
    # W[t] = sig1(W[t-2]) + W[t-7] + sig0(W[t-15]) + W[t-16] mod 2^32.
    # At word-level, each operand can influence the result, so take dependency union.
    schedule_deps.append(set().union(
        schedule_deps[t-2], schedule_deps[t-7],
        schedule_deps[t-15], schedule_deps[t-16]
    ))

# Register dependency sets before round 0 are empty with respect to this block's
# 16 source words; the chaining value is held fixed and is not an input location.
state = {r: set() for r in REGISTERS}
state_snapshots = [(-1, {r: set(v) for r, v in state.items()})]
for t in range(ROUNDS):
    # T1 reads h,e,f,g and W[t]; T2 reads a,b,c.
    t1 = set().union(state['h'], state['e'], state['f'], state['g'], schedule_deps[t])
    t2 = set().union(state['a'], state['b'], state['c'])
    # Simultaneous SHA-256 register update.
    new_state = {
        'a': t1 | t2,
        'b': set(state['a']),
        'c': set(state['b']),
        'd': set(state['c']),
        'e': state['d'] | t1,
        'f': set(state['e']),
        'g': set(state['f']),
        'h': set(state['g']),
    }
    state = new_state
    state_snapshots.append((t, {r: set(v) for r, v in state.items()}))

# Full tensor, long form: every source word x round snapshot x register.
tensor_path = OUT / 'sha256_location_dependency_tensor.csv'
with tensor_path.open('w', newline='', encoding='utf-8') as f:
    w = csv.writer(f)
    w.writerow(['source_word_j', 'snapshot_after_round_t', 'register_r', 'L_jtr'])
    for t, snap in state_snapshots:
        for r in REGISTERS:
            for j in range(SOURCE_WORDS):
                w.writerow([j, t, r, int(j in snap[r])])

# Expanded schedule support, retaining the actual source-word set for each W[t].
schedule_path = OUT / 'sha256_schedule_location_dependencies.csv'
with schedule_path.open('w', newline='', encoding='utf-8') as f:
    w = csv.writer(f)
    w.writerow(['schedule_word_t', 'source_word_count', 'source_words_j', 'source_mask_hex'])
    for t, deps in enumerate(schedule_deps):
        mask = sum(1 << j for j in deps)
        w.writerow([t, len(deps), ' '.join(map(str, sorted(deps))), f'0x{mask:04x}'])

# Summary facts extracted from this computed tensor.
first_schedule_full = next(t for t, deps in enumerate(schedule_deps) if len(deps) == SOURCE_WORDS)
first_full_register = {
    r: next(t for t, snap in state_snapshots[1:] if len(snap[r]) == SOURCE_WORDS)
    for r in REGISTERS
}
first_all_registers_by_source = {
    str(j): next(
        t for t, snap in state_snapshots[1:]
        if all(j in snap[r] for r in REGISTERS)
    )
    for j in range(SOURCE_WORDS)
}
first_all_sources_every_register = next(
    t for t, snap in state_snapshots[1:]
    if all(len(snap[r]) == SOURCE_WORDS for r in REGISTERS)
)

# Compact counts for selected snapshots.
selected_rounds = [-1, 0, 1, 2, 3, 7, 15, 16, 17, 18, 25, 26, 31, 63]
round_counts = []
for t, snap in state_snapshots:
    if t in selected_rounds:
        round_counts.append({
            'after_round': t,
            'source_dependencies_by_register': {r: len(snap[r]) for r in REGISTERS},
            'total_source_register_pairs': sum(len(snap[r]) for r in REGISTERS),
        })

result = {
    'scope': 'single 512-bit compression block; the 16 initial message-schedule words are source locations; chaining state fixed',
    'analysis_type': 'word-level static may-dependence / taint propagation',
    'L_definition': 'L[j,t,r] = 1 when a dependency path from source word W[j], j=0..15, reaches register r after round t; t=-1 is the pre-round state',
    'first_schedule_word_depending_on_all_16_sources': first_schedule_full,
    'first_round_each_register_depends_on_all_16_sources': first_full_register,
    'first_round_every_register_depends_on_all_16_sources': first_all_sources_every_register,
    'first_round_all_registers_depend_on_each_source_word': first_all_registers_by_source,
    'selected_round_counts': round_counts,
    'limitations': [
        'This is word-level structural support, not a bit-level Boolean derivative.',
        'A dependency edge means a source can influence a value through the code path; for a particular input, numeric differences can cancel or remain zero.',
        'The source set is the 16 words entering one compression block. For later blocks, the incoming chaining state is another dependency source and must be included.',
        'Padding and message-length encoding are outside this block-local tensor; their constructed words can be added as source classes in a full-message location model.'
    ]
}
(OUT / 'sha256_location_dependency_tensor_report.json').write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')

report = f'''# SHA-256 location-dependency tensor (word-level)

## Definition

`L[j,t,r] = 1` when original source schedule word `W[j]`, `j = 0..15`, has a structural dependency path to register `r` after round `t`. `t = -1` denotes the state before round 0. The chaining state is held fixed, so the tensor isolates this block's 16 source-word locations.

The schedule graph is built from the actual recurrence

`W[t] = σ1(W[t−2]) + W[t−7] + σ0(W[t−15]) + W[t−16] (mod 2^32)`.

The state graph uses the code's operand dependencies: `T1` reads `h,e,f,g,W[t]`; `T2` reads `a,b,c`; then `a′` depends on `T1,T2`, `e′` on `d,T1`, and `b′,c′,d′,f′,g′,h′` shift prior registers.

## Results from the computed tensor

- Each `W[j]` enters its first compression round at round `j`.
- Its structural support reaches all eight register slots by the end of round `j+3`.
- Therefore all eight registers structurally depend on all 16 original source words by the end of round **18**.
- The *schedule expansion* reaches a different milestone: the first expanded schedule word whose dependency set contains all 16 originals is **W[26]**.
- These are distinct pathways. State-register support fills first by sequential injections and register shifts; schedule-word support fills through the recurrence offsets.

Per-register first round with all 16 source-word dependencies: {json.dumps(first_full_register, sort_keys=True)}.

First round by which each individual source word reaches all eight registers: {json.dumps({int(k):v for k,v in first_all_registers_by_source.items()}, sort_keys=True)}.

## What this establishes—and what it does not

This is a word-level static dependency map derived from the schedule recurrence and round wiring, not merely a record of input addresses. A 1 means a code path exists by which that source word can affect the state slot. It does **not** claim that every specific numeric input must exhibit a different value in every marked slot; concrete equality can occur through value-specific behavior or cancellation. A bit-exact dependency analysis would preserve bit coordinates and carry/rotation behavior instead of collapsing each 32-bit word to one support set.

For a full multi-block hash, prior chaining state must be added as a source. To include length-as-location, model original payload bits, the padding marker, zero fill, and the 64-bit length trailer as separately labelled source classes.
'''
(OUT / 'sha256_location_dependency_tensor_report.md').write_text(report, encoding='utf-8')

zip_path = OUT / 'sha256_location_dependency_tensor_bundle.zip'
with zipfile.ZipFile(zip_path, 'w', compression=zipfile.ZIP_DEFLATED) as z:
    for p in [Path(__file__), tensor_path, schedule_path, OUT/'sha256_location_dependency_tensor_report.json', OUT/'sha256_location_dependency_tensor_report.md']:
        z.write(p, arcname=p.name)

print(json.dumps({
    'tensor_csv': str(tensor_path),
    'schedule_csv': str(schedule_path),
    'report_md': str(OUT/'sha256_location_dependency_tensor_report.md'),
    'bundle_zip': str(zip_path),
    'tensor_rows': 16 * 65 * 8,
    'first_schedule_full': first_schedule_full,
    'first_full_each_register': first_full_register,
    'all_sources_all_registers': first_all_sources_every_register,
    'first_all_registers_by_source': first_all_registers_by_source,
}, indent=2))
