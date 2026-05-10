# Nexus code salvage notebook

This notebook is a **curated salvage** from `Untitled1.md` plus the recent SHA tuner work in this session.

What I kept: - self-contained, runnable SHA-256 core utilities - harmonic / hex-native input builders - inverse-constant experiments - BBP finite-state orbit tooling - digest scar / A-value readers - a new **resonance scanner** that ranks input families by separation, energy drift, and mirrored-state alignment

What I deliberately left out: - placeholder solvers with missing globals - duplicated scripts that said the same thing with different wrappers - pseudo-code that could not survive execution without external state

The goal is simple: keep the code that actually moves experiments forward.

    from __future__ import annotations

    import ast
    import json
    import math
    import re
    import struct
    import hashlib
    from dataclasses import dataclass
    from pathlib import Path
    from typing import Dict, List, Tuple, Iterable

    import numpy as np
    import pandas as pd
    # Paths
    DATA_DIR = Path('/mnt/data')
    SOURCE_MD = DATA_DIR / 'Untitled1.md'
    H = math.pi / 9
    M32 = 0xFFFFFFFF

    STD_H = [
        0x6A09E667, 0xBB67AE85, 0x3C6EF372, 0xA54FF53A,
        0x510E527F, 0x9B05688C, 0x1F83D9AB, 0x5BE0CD19,
    ]

    STD_K = [
        0x428A2F98, 0x71374491, 0xB5C0FBCF, 0xE9B5DBA5, 0x3956C25B, 0x59F111F1, 0x923F82A4, 0xAB1C5ED5,
        0xD807AA98, 0x12835B01, 0x243185BE, 0x550C7DC3, 0x72BE5D74, 0x80DEB1FE, 0x9BDC06A7, 0xC19BF174,
        0xE49B69C1, 0xEFBE4786, 0x0FC19DC6, 0x240CA1CC, 0x2DE92C6F, 0x4A7484AA, 0x5CB0A9DC, 0x76F988DA,
        0x983E5152, 0xA831C66D, 0xB00327C8, 0xBF597FC7, 0xC6E00BF3, 0xD5A79147, 0x06CA6351, 0x14292967,
        0x27B70A85, 0x2E1B2138, 0x4D2C6DFC, 0x53380D13, 0x650A7354, 0x766A0ABB, 0x81C2C92E, 0x92722C85,
        0xA2BFE8A1, 0xA81A664B, 0xC24B8B70, 0xC76C51A3, 0xD192E819, 0xD6990624, 0xF40E3585, 0x106AA070,
        0x19A4C116, 0x1E376C08, 0x2748774C, 0x34B0BCB5, 0x391C0CB3, 0x4ED8AA4A, 0x5B9CCA4F, 0x682E6FF3,
        0x748F82EE, 0x78A5636F, 0x84C87814, 0x8CC70208, 0x90BEFFFA, 0xA4506CEB, 0xBEF9A3F7, 0xC67178F2,
    ]

    INV_H = [(-x) & M32 for x in STD_H]
    INV_K = [(-x) & M32 for x in STD_K]

    PI_HEX_64 = '243F6A8885A308D313198A2E03707344A4093822299F31D0082EFA98EC4E6C89'

    BBP_TRANS = {0:3, 1:1, 2:3, 3:3, 4:1, 5:2, 6:1, 7:1, 8:1, 9:2, 10:2, 11:3, 12:3, 13:1, 14:1, 15:3}

    print('H =', H)
    print('H + INV_H = 0 mod 2^32 ?', all(((a+b) & M32) == 0 for a, b in zip(STD_H, INV_H)))
    print('K + INV_K = 0 mod 2^32 ?', all(((a+b) & M32) == 0 for a, b in zip(STD_K, INV_K)))
    H = 0.3490658503988659
    H + INV_H = 0 mod 2^32 ? True
    K + INV_K = 0 mod 2^32 ? True

## 1) Markdown code-block salvage

This cell scans `Untitled1.md`, finds Python code fences, syntax-checks them, and extracts a compact manifest. This gives you a live inventory of what survived curation and what to revisit later.

    def extract_python_blocks(md_text: str) -> List[dict]:
        parts = re.split(r"```", md_text)
        out = []
        for idx in range(1, len(parts), 2):
            raw = parts[idx]
            if not raw.lstrip().startswith("python"):
                continue
            raw_lines = raw.splitlines()
            code = "\n".join(raw_lines[1:]) if len(raw_lines) > 1 else ""
            title = ""
            header_lines = [ln.strip() for ln in code.splitlines()[:8] if ln.strip()]
            if header_lines:
                title = header_lines[0][:120]
            try:
                tree = ast.parse(code)
                ok = True
                err = ""
                defs = [n.name for n in ast.walk(tree) if isinstance(n, (ast.FunctionDef, ast.ClassDef))]
            except Exception as exc:
                ok = False
                err = str(exc).splitlines()[0]
                defs = []
            out.append({
                "block_id": (idx + 1) // 2,
                "ok": ok,
                "title": title,
                "lines": len(code.splitlines()),
                "defs": defs[:12],
                "error": err,
                "code": code,
            })
        return out

    md_text = SOURCE_MD.read_text(errors="ignore")
    blocks = extract_python_blocks(md_text)
    manifest = pd.DataFrame([{k: v for k, v in b.items() if k != "code"} for b in blocks])
    manifest.sort_values(["ok", "lines"], ascending=[False, False]).head(20)

block_id

ok

title

lines

defs

error

32

82

True

"""

763

\[add32, sub32, rotr, shr, Sig0, Sig1, sig0, si...

11

15

True

#!/usr/bin/env python3

741

\[rotr, shr, ch, maj, sigma0, sigma1, gamma0, g...

14

49

True

#!/usr/bin/env python3

741

\[rotr, shr, ch, maj, sigma0, sigma1, gamma0, g...

13

48

True

#!/usr/bin/env python3

642

\[sha256_bytes, sha256_hex, bytes_to_words, wor...

15

50

True

#!/usr/bin/env python3

619

\[trace\]

16

51

True

"""

512

\[S0, S1, Ch, Maj, s0, s1, sha_forward_trace, s...

35

89

True

"""

508

\[add32, sub32, rotr, shr, Sig0, Sig1, sig0, si...

36

90

True

"""

508

\[add32, sub32, rotr, shr, Sig0, Sig1, sig0, si...

12

47

True

#!/usr/bin/env python3

504

\[rotr, shr, ch, maj, sigma0, sigma1, gamma0, g...

20

55

True

"""

498

\[rotr, sig0, sig1, Sig0, Sig1, Ch, Maj, sha_co...

0

2

True

#!/usr/bin/env python3

493

\[rotr, sigma0, sigma1, Sigma0, Sigma1, Ch, Maj...

34

84

True

"""

381

\[add32, sub32, rotr, rotl, shr, Sig0, Sig1, si...

21

57

True

"""

371

\[rotr, sig0, sig1, Sig0, Sig1, Ch, Maj, zone, ...

38

92

True

"""

345

\[rotr, S0, S1, s0, s1, Ch, Maj, add, expand, s...

33

83

True

"""

336

\[add32, sub32, rotr, shr, Sig0, Sig1, sig0, si...

17

52

True

"""

319

\[s0, s1, sha_n, A_shape, mean_A\]

23

59

True

"""

319

\[rotr, sig0, sig1, Sig0, Sig1, Ch, Maj, zone, ...

22

58

True

"""

311

\[s0, s1, compress_block, A_signed, acf, bx\]

27

73

True

#!/usr/bin/env python3

289

\[rotr, sig0, sig1, Sig0, Sig1, ch, maj, add32,...

18

53

True

"""

265

\[s0, s1, full_trace, acf, bx\]

## 2) SHA-256 core that is actually usable

This is the clean spine. It replaces the duplicated one-off scripts with one trace engine that supports: - standard constants - inverse constants - per-round state capture - digest scar inspection - reverse / byte / word / bit variants

    def rotr(x: int, n: int) -> int:
        return ((x >> n) | (x << (32 - n))) & M32

    def ch(x: int, y: int, z: int) -> int:
        return ((x & y) ^ (~x & z)) & M32

    def maj(x: int, y: int, z: int) -> int:
        return ((x & y) ^ (x & z) ^ (y & z)) & M32

    def big_sigma0(x: int) -> int:
        return rotr(x, 2) ^ rotr(x, 13) ^ rotr(x, 22)

    def big_sigma1(x: int) -> int:
        return rotr(x, 6) ^ rotr(x, 11) ^ rotr(x, 25)

    def small_sigma0(x: int) -> int:
        return rotr(x, 7) ^ rotr(x, 18) ^ (x >> 3)

    def small_sigma1(x: int) -> int:
        return rotr(x, 17) ^ rotr(x, 19) ^ (x >> 10)

    def words_to_bytes(words: Iterable[int]) -> bytes:
        return b''.join(struct.pack('>I', w & M32) for w in words)

    def bytes_to_words(buf: bytes) -> List[int]:
        assert len(buf) % 4 == 0
        return list(struct.unpack(f'>{len(buf)//4}I', buf))

    def pad_sha256(msg: bytes) -> bytes:
        out = bytearray(msg)
        bit_len = len(msg) * 8
        out.append(0x80)
        while len(out) % 64 != 56:
            out.append(0)
        out += struct.pack('>Q', bit_len)
        return bytes(out)

    @dataclass
    class TraceResult:
        digest_hex: str
        final_state: Tuple[int, ...]
        round_states: List[Tuple[int, ...]]
        T1: List[int]
        T2: List[int]
        block_count: int
        first_block_words: List[int]


    def sha256_trace(msg: bytes, H_init: List[int] | None = None, K: List[int] | None = None) -> TraceResult:
        H_init = list(STD_H if H_init is None else H_init)
        K = list(STD_K if K is None else K)
        state = H_init[:]
        padded = pad_sha256(msg)
        all_states, all_T1, all_T2 = [], [], []
        first_block_words = []

        for off in range(0, len(padded), 64):
            block = padded[off:off+64]
            W = list(struct.unpack('>16I', block))
            if off == 0:
                first_block_words = W[:]
            for t in range(16, 64):
                W.append((small_sigma1(W[t-2]) + W[t-7] + small_sigma0(W[t-15]) + W[t-16]) & M32)
            a, b, c, d, e, f, g, h = state
            for t in range(64):
                T1 = (h + big_sigma1(e) + ch(e, f, g) + K[t] + W[t]) & M32
                T2 = (big_sigma0(a) + maj(a, b, c)) & M32
                h, g, f, e, d, c, b, a = g, f, e, (d + T1) & M32, c, b, a, (T1 + T2) & M32
                all_states.append((a, b, c, d, e, f, g, h))
                all_T1.append(T1)
                all_T2.append(T2)
            state = [((x + y) & M32) for x, y in zip(state, [a, b, c, d, e, f, g, h])]

        return TraceResult(
            digest_hex=''.join(f'{x:08x}' for x in state),
            final_state=tuple(state),
            round_states=all_states,
            T1=all_T1,
            T2=all_T2,
            block_count=len(padded) // 64,
            first_block_words=first_block_words,
        )


    def reverse_hex_variants(hex_digest: str) -> Dict[str, str]:
        b = [hex_digest[i:i+2] for i in range(0, len(hex_digest), 2)]
        w = [hex_digest[i:i+8] for i in range(0, len(hex_digest), 8)]
        def reverse_bits_in_byte(hx: str) -> str:
            v = int(hx, 16)
            return f"{int(f'{v:08b}'[::-1], 2):02x}"
        return {
            'chars_rev': hex_digest[::-1],
            'bytes_rev': ''.join(reversed(b)),
            'words32_rev': ''.join(reversed(w)),
            'bits_each_byte_rev': ''.join(reverse_bits_in_byte(x) for x in b),
        }

    # smoke check
    msg = b'NEXUS|TEST|' * 12
    tr = sha256_trace(msg)
    assert tr.digest_hex == hashlib.sha256(msg).hexdigest()
    print(tr.digest_hex, 'blocks=', tr.block_count)
    3ee61390166701ed753bb5e32a4c18469c798796367414b0d169f912d2bebf6e blocks= 3
    def digest_words(hex_digest: str) -> List[int]:
        return [int(hex_digest[i:i+8], 16) for i in range(0, len(hex_digest), 8)]

    def signed32(x: int) -> int:
        x &= M32
        return x if x < 0x80000000 else x - 0x100000000

    def word_A_values(hex_digest: str, H: float = H) -> List[dict]:
        out = []
        for i, w in enumerate(digest_words(hex_digest)):
            C = w / M32
            if C >= H:
                A = math.sqrt(max(C*C - H*H, 0.0))
                sign = +1
            else:
                A = math.sqrt(max(H*H - C*C, 0.0))
                sign = -1
            bits = f'{w:032b}'
            out.append({
                'word': i,
                'hex': f'0x{w:08x}',
                'C': C,
                'A_signed': sign * A,
                'ones': bits.count('1'),
                'runs_1': len([x for x in bits.split('0') if x]),
            })
        return out

    pd.DataFrame(word_A_values(tr.digest_hex))

word

hex

C

A_signed

ones

runs_1

0

0

0x3ee61390

0.245698

-0.247950

15

6

1

1

0x166701ed

0.087509

-0.337919

15

7

2

2

0x753bb5e3

0.457942

0.296419

20

9

3

3

0x2a4c1846

0.165224

-0.307487

11

8

4

4

0x9c798796

0.611229

0.501751

17

7

5

5

0x367414b0

0.212709

-0.276771

13

8

6

6

0xd169f912

0.818023

0.739807

16

9

7

7

0xd2bebf6e

0.823223

0.745553

22

9

## 3) Hex-native input families

These are the families worth testing first because they stay in the machine's own alphabet.

    def build_inputs() -> Dict[str, bytes]:
        K_bytes = words_to_bytes(STD_K)
        H_bytes = words_to_bytes(STD_H)
        K_inv_bytes = words_to_bytes(INV_K)
        H_inv_bytes = words_to_bytes(INV_H)

        # phase-shifted / echoed family from the recent experiments
        K_phase_shifted = K_bytes + K_bytes[4:] + K_bytes[:4]

        interleave_HK = bytearray()
        for h, k in zip(STD_H * 8, STD_K[:64]):
            interleave_HK += struct.pack('>I', h)
            interleave_HK += struct.pack('>I', k)

        reversed_K_words = words_to_bytes(list(reversed(STD_K)))
        pi_hex_bytes = bytes.fromhex(PI_HEX_64)

        return {
            'K_constants_full': K_bytes,
            'K_constants_half': words_to_bytes(STD_K[:32]),
            'H_constants': H_bytes,
            'K_INV_as_msg': K_inv_bytes,
            'H_INV_as_msg': H_inv_bytes,
            'K_phase_shifted': K_phase_shifted,
            'K_reversed_words': reversed_K_words,
            'H_then_K_interleave': bytes(interleave_HK),
            'PI_hex_slice': pi_hex_bytes,
        }

    INPUTS = build_inputs()
    {k: len(v) for k, v in INPUTS.items()}
    {'K_constants_full': 256,
     'K_constants_half': 128,
     'H_constants': 32,
     'K_INV_as_msg': 256,
     'H_INV_as_msg': 32,
     'K_phase_shifted': 512,
     'K_reversed_words': 256,
     'H_then_K_interleave': 512,
     'PI_hex_slice': 32}

## 4) Metrics that survive execution

These are the metrics I kept because they are explicit and reproducible: - digest hamming distance - transition energy (sum of round-to-round state bit changes) - mirrored-state hamming - zone balance (words above / below H)

    def hamming_hex(h1: str, h2: str) -> int:
        return (int(h1, 16) ^ int(h2, 16)).bit_count()

    def state_transition_energy(states: List[Tuple[int, ...]]) -> int:
        if len(states) < 2:
            return 0
        total = 0
        for prev, cur in zip(states[:-1], states[1:]):
            total += sum((a ^ b).bit_count() for a, b in zip(prev, cur))
        return total

    def mirrored_state_hamming(states_a: List[Tuple[int, ...]], states_b: List[Tuple[int, ...]]) -> dict:
        n = min(len(states_a), len(states_b))
        comp = []
        rev_b = list(reversed(states_b[:n]))
        for sa, sb in zip(states_a[:n], rev_b):
            comp.append(sum((a ^ b).bit_count() for a, b in zip(sa, sb)))
        return {
            'rounds_compared': n,
            'min': min(comp) if comp else None,
            'max': max(comp) if comp else None,
            'avg': round(sum(comp)/len(comp), 2) if comp else None,
        }

    def zone_balance(hex_digest: str, H: float = H) -> Tuple[int, int]:
        vals = [w / M32 for w in digest_words(hex_digest)]
        real = sum(v >= H for v in vals)
        imag = len(vals) - real
        return real, imag

    def summarize_pair(msg: bytes, H_init_a=STD_H, K_a=STD_K, H_init_b=INV_H, K_b=INV_K) -> dict:
        std = sha256_trace(msg, H_init_a, K_a)
        inv = sha256_trace(msg, H_init_b, K_b)
        e_std = state_transition_energy(std.round_states)
        e_inv = state_transition_energy(inv.round_states)
        return {
            'size_bytes': len(msg),
            'blocks': std.block_count,
            'std_digest': std.digest_hex,
            'inv_digest': inv.digest_hex,
            'hamming_bits': hamming_hex(std.digest_hex, inv.digest_hex),
            'std_energy': e_std,
            'inv_energy': e_inv,
            'energy_ratio_inv_over_std': (e_inv / e_std) if e_std else float('nan'),
            'std_zone': zone_balance(std.digest_hex),
            'inv_zone': zone_balance(inv.digest_hex),
            'mirrored_alignment': mirrored_state_hamming(std.round_states, inv.round_states),
        }

    summarize_pair(INPUTS['K_constants_full'])
    {'size_bytes': 256,
     'blocks': 5,
     'std_digest': 'e4c62ae41929873b99fa3f871694451c9dbd0300448aba7ea4ff6d68a6b52d95',
     'inv_digest': '5f80e54690df0f0cfb86a07823db4ff973eec9c4031d6fab0055120f03c8e6a9',
     'hamming_bits': 146,
     'std_energy': 40723,
     'inv_energy': 40640,
     'energy_ratio_inv_over_std': 0.9979618397465806,
     'std_zone': (5, 3),
     'inv_zone': (4, 4),
     'mirrored_alignment': {'rounds_compared': 320,
      'min': 109,
      'max': 151,
      'avg': 128.25}}
    rows = []
    for name, msg in INPUTS.items():
        rec = summarize_pair(msg)
        rec['name'] = name
        rec['mirrored_avg'] = rec['mirrored_alignment']['avg']
        rows.append(rec)

    runs = pd.DataFrame(rows)[[
        'name', 'size_bytes', 'blocks', 'hamming_bits', 'std_energy', 'inv_energy',
        'energy_ratio_inv_over_std', 'std_zone', 'inv_zone', 'mirrored_avg'
    ]].sort_values(['hamming_bits', 'mirrored_avg'])
    runs

name

size_bytes

blocks

hamming_bits

std_energy

inv_energy

energy_ratio_inv_over_std

std_zone

inv_zone

mirrored_avg

4

H_INV_as_msg

32

1

121

8304

8132

0.979287

(4, 4)

(4, 4)

127.64

3

K_INV_as_msg

256

5

124

41147

40953

0.995285

(6, 2)

(6, 2)

127.45

5

K_phase_shifted

512

9

125

73418

73409

0.999877

(5, 3)

(5, 3)

127.81

8

PI_hex_slice

32

1

125

8076

7926

0.981426

(4, 4)

(7, 1)

128.73

2

H_constants

32

1

126

8129

8218

1.010948

(6, 2)

(5, 3)

128.27

7

H_then_K_interleave

512

9

132

73653

73364

0.996076

(4, 4)

(6, 2)

128.38

6

K_reversed_words

256

5

133

40884

40966

1.002006

(5, 3)

(5, 3)

127.67

1

K_constants_half

128

3

139

24154

24509

1.014697

(6, 2)

(4, 4)

128.23

0

K_constants_full

256

5

146

40723

40640

0.997962

(5, 3)

(4, 4)

128.25

## 5) BBP finite-state orbit tooling

This keeps the useful part of the BBP material: the moment the state is restricted to hex digits, repeated application becomes a finite directed graph with basins and cycles. That is real and testable.

    def bbp_step(n: int) -> int:
        return BBP_TRANS[n % 16]

    def orbit(seed: int, limit: int = 64) -> List[int]:
        out = [seed]
        seen = {seed: 0}
        cur = seed
        for _ in range(limit - 1):
            cur = bbp_step(cur)
            out.append(cur)
            if cur in seen:
                break
            seen[cur] = len(out) - 1
        return out

    def orbit_signature(seed: int) -> dict:
        path = orbit(seed)
        last = path[-1]
        first_idx = path.index(last)
        cycle = path[first_idx:-1] if path.count(last) > 1 else [last]
        return {
            'seed': seed,
            'path': path,
            'tail_len': first_idx,
            'cycle': cycle,
            'cycle_len': len(cycle),
        }

    orbit_table = pd.DataFrame([orbit_signature(s) for s in range(16)])
    orbit_table[['seed', 'tail_len', 'cycle', 'cycle_len']]

seed

tail_len

cycle

cycle_len

0

0

1

\[3\]

1

1

1

0

\[1\]

1

2

2

1

\[3\]

1

3

3

0

\[3\]

1

4

4

1

\[1\]

1

5

5

2

\[3\]

1

6

6

1

\[1\]

1

7

7

1

\[1\]

1

8

8

1

\[1\]

1

9

9

2

\[3\]

1

10

10

2

\[3\]

1

11

11

1

\[3\]

1

12

12

1

\[3\]

1

13

13

1

\[1\]

1

14

14

1

\[1\]

1

15

15

1

\[3\]

1

## 6) New synthesis: resonance scanner

This is the extra piece I added from the whole pile.

It sweeps **input family × transform family × engine family** and ranks candidates by: - lower digest separation - lower energy drift from 1.0 - lower mirrored-state hamming

This gives you one place to look for the next hook instead of manually comparing scattered scripts.

    def message_transforms(msg: bytes) -> Dict[str, bytes]:
        # byte-safe transforms only
        words = bytes_to_words(msg[:len(msg) - (len(msg) % 4)]) if len(msg) >= 4 else []
        out = {
            'identity': msg,
            'bytes_rev': msg[::-1],
            'xor_ff': bytes(b ^ 0xFF for b in msg),
        }
        if words:
            out['words32_rev'] = words_to_bytes(list(reversed(words)))
        return out


    def H_conjugate_constants(constants: List[int], H_value: float = H) -> List[int]:
        # reflect normalized constants across H on the unit interval
        conj = []
        for w in constants:
            c = w / M32
            rc = (2 * H_value - c) % 1.0
            conj.append(int(rc * M32) & M32)
        return conj

    CONJ_K = H_conjugate_constants(STD_K)
    CONJ_H = H_conjugate_constants(STD_H)

    ENGINE_FAMILIES = {
        'std_vs_inv': (STD_H, STD_K, INV_H, INV_K),
        'std_vs_conj': (STD_H, STD_K, CONJ_H, CONJ_K),
        'std_vs_std': (STD_H, STD_K, STD_H, STD_K),
    }

    scanner_rows = []
    for input_name, raw in INPUTS.items():
        for transform_name, transformed in message_transforms(raw).items():
            for engine_name, (Ha, Ka, Hb, Kb) in ENGINE_FAMILIES.items():
                rec = summarize_pair(transformed, Ha, Ka, Hb, Kb)
                scanner_rows.append({
                    'input': input_name,
                    'transform': transform_name,
                    'engine': engine_name,
                    'bytes': len(transformed),
                    'hamming': rec['hamming_bits'],
                    'energy_ratio': rec['energy_ratio_inv_over_std'],
                    'energy_drift': abs(rec['energy_ratio_inv_over_std'] - 1.0),
                    'mirrored_avg': rec['mirrored_alignment']['avg'],
                })

    scan = pd.DataFrame(scanner_rows)
    scan['score'] = (256 - scan['hamming']) + (1 - scan['energy_drift']) * 50 + (160 - scan['mirrored_avg'])
    scan.sort_values('score', ascending=False).head(20)

input

transform

engine

bytes

hamming

energy_ratio

energy_drift

mirrored_avg

score

26

H_constants

identity

std_vs_std

32

0

1.0

0.0

124.97

341.03

44

K_INV_as_msg

xor_ff

std_vs_std

256

0

1.0

0.0

126.91

339.09

98

PI_hex_slice

identity

std_vs_std

32

0

1.0

0.0

126.94

339.06

8

K_constants_full

xor_ff

std_vs_std

256

0

1.0

0.0

127.12

338.88

89

H_then_K_interleave

bytes_rev

std_vs_std

512

0

1.0

0.0

127.26

338.74

50

H_INV_as_msg

identity

std_vs_std

32

0

1.0

0.0

127.28

338.72

104

PI_hex_slice

xor_ff

std_vs_std

32

0

1.0

0.0

127.38

338.62

20

K_constants_half

xor_ff

std_vs_std

128

0

1.0

0.0

127.58

338.42

5

K_constants_full

bytes_rev

std_vs_std

256

0

1.0

0.0

127.61

338.39

47

K_INV_as_msg

words32_rev

std_vs_std

256

0

1.0

0.0

127.64

338.36

32

H_constants

xor_ff

std_vs_std

32

0

1.0

0.0

127.72

338.28

80

K_reversed_words

xor_ff

std_vs_std

256

0

1.0

0.0

127.78

338.22

65

K_phase_shifted

bytes_rev

std_vs_std

512

0

1.0

0.0

127.85

338.15

2

K_constants_full

identity

std_vs_std

256

0

1.0

0.0

127.88

338.12

83

K_reversed_words

words32_rev

std_vs_std

256

0

1.0

0.0

127.88

338.12

14

K_constants_half

identity

std_vs_std

128

0

1.0

0.0

127.89

338.11

56

H_INV_as_msg

xor_ff

std_vs_std

32

0

1.0

0.0

128.03

337.97

74

K_reversed_words

identity

std_vs_std

256

0

1.0

0.0

128.14

337.86

11

K_constants_full

words32_rev

std_vs_std

256

0

1.0

0.0

128.14

337.86

77

K_reversed_words

bytes_rev

std_vs_std

256

0

1.0

0.0

128.16

337.84

## 7) Digest scar reader

This is the compact reader that survived from the stronger analysis sections: - normalized digest words - A-values from the (A\^2 + H\^2 = C\^2) carve - bit-density and run structure

That exact carve shows up repeatedly in the file's harmonic SHA reflection / Glass Key material.

    sample_name = scan.sort_values('score', ascending=False).iloc[0]['input']
    sample_msg = INPUTS[sample_name]
    sample_trace = sha256_trace(sample_msg)
    scar_df = pd.DataFrame(word_A_values(sample_trace.digest_hex))
    print('sample input =', sample_name)
    print('digest =', sample_trace.digest_hex)
    scar_df
    sample input = H_constants
    digest = 5cce668898a2e2d7dedbb552165a2a77596d092b03df3fcf68118d63982b6106

word

hex

C

A_signed

ones

runs_1

0

0

0x5cce6688

0.362524

0.097862

15

8

1

1

0x98a2e2d7

0.596235

0.483373

16

10

2

2

0xdedbb552

0.870540

0.797492

20

11

3

3

0x165a2a77

0.087313

-0.337969

16

10

4

4

0x596d092b

0.349320

0.013323

15

11

5

5

0x03df3fcf

0.015125

-0.348738

21

4

6

6

0x68118d63

0.406518

0.208350

13

8

7

7

0x982b6106

0.594412

0.481122

12

8

## 8) Export helpers

Use these to save the current curation state.

    def export_curated_state(out_dir: str = 'curated_exports'):
        out = Path(out_dir)
        out.mkdir(exist_ok=True)
        manifest.to_csv(out / 'code_block_manifest.csv', index=False)
        runs.to_csv(out / 'harmonic_input_runs.csv', index=False)
        scan.sort_values('score', ascending=False).to_csv(out / 'resonance_scan.csv', index=False)
        scar_df.to_csv(out / 'sample_digest_scar.csv', index=False)
        with open(out / 'summary.json', 'w') as f:
            json.dump({
                'source': str(SOURCE_MD),
                'kept_python_blocks': int(manifest['ok'].sum()),
                'total_python_blocks': int(len(manifest)),
                'top_resonance_row': scan.sort_values('score', ascending=False).iloc[0].to_dict(),
            }, f, indent=2, default=str)
        return out

    export_curated_state()
    PosixPath('curated_exports')
