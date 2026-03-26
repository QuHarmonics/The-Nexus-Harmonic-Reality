
import struct, hashlib, math
from dataclasses import dataclass
from typing import List, Dict, Any
import pandas as pd

MASK32 = 0xFFFFFFFF
IV = [
    0x6a09e667, 0xbb67ae85, 0x3c6ef372, 0xa54ff53a,
    0x510e527f, 0x9b05688c, 0x1f83d9ab, 0x5be0cd19,
]
K = [
    0x428a2f98,0x71374491,0xb5c0fbcf,0xe9b5dba5,0x3956c25b,0x59f111f1,0x923f82a4,0xab1c5ed5,
    0xd807aa98,0x12835b01,0x243185be,0x550c7dc3,0x72be5d74,0x80deb1fe,0x9bdc06a7,0xc19bf174,
    0xe49b69c1,0xefbe4786,0x0fc19dc6,0x240ca1cc,0x2de92c6f,0x4a7484aa,0x5cb0a9dc,0x76f988da,
    0x983e5152,0xa831c66d,0xb00327c8,0xbf597fc7,0xc6e00bf3,0xd5a79147,0x06ca6351,0x14292967,
    0x27b70a85,0x2e1b2138,0x4d2c6dfc,0x53380d13,0x650a7354,0x766a0abb,0x81c2c92e,0x92722c85,
    0xa2bfe8a1,0xa81a664b,0xc24b8b70,0xc76c51a3,0xd192e819,0xd6990624,0xf40e3585,0x106aa070,
    0x19a4c116,0x1e376c08,0x2748774c,0x34b0bcb5,0x391c0cb3,0x4ed8aa4a,0x5b9cca4f,0x682e6ff3,
    0x748f82ee,0x78a5636f,0x84c87814,0x8cc70208,0x90befffa,0xa4506ceb,0xbef9a3f7,0xc67178f2
]

def rotr(x, n): return ((x >> n) | (x << (32 - n))) & MASK32
def Sig0(x): return rotr(x, 2) ^ rotr(x, 13) ^ rotr(x, 22)
def Sig1(x): return rotr(x, 6) ^ rotr(x, 11) ^ rotr(x, 25)
def sig0(x): return rotr(x, 7) ^ rotr(x, 18) ^ (x >> 3)
def sig1(x): return rotr(x, 17) ^ rotr(x, 19) ^ (x >> 10)
def Ch(e, f, g): return (e & f) ^ ((~e) & g & MASK32)
def Maj(a, b, c): return (a & b) ^ (a & c) ^ (b & c)

def add_carries(*values: int) -> int:
    total = 0
    carry_union = 0
    for v in values:
        carry_union |= (total & v)
        total = (total + v) & MASK32
    return carry_union & MASK32

def popcount(x: int) -> int:
    return int(x & MASK32).bit_count()

def to_printable(bs: bytes) -> str:
    return ''.join(chr(b) if 32 <= b <= 126 else '·' for b in bs)

def hex32(x: int) -> str:
    return f"0x{x & MASK32:08x}"

def pad_sha256(msg: bytes) -> bytes:
    out = bytearray(msg)
    out.append(0x80)
    while len(out) % 64 != 56:
        out.append(0)
    out += struct.pack('>Q', len(msg) * 8)
    return bytes(out)

def word_to_bytes(word: int) -> bytes:
    return struct.pack('>I', word & MASK32)

def msg_ascii_0_127() -> bytes:
    return bytes(range(128))

def msg_digits(n: int) -> bytes:
    return (b"0123456789" * ((n + 9)//10))[:n]

@dataclass
class GlassKeyTrace:
    message: bytes
    padded: bytes
    blocks: List[Dict[str, Any]]
    digest_words: List[int]
    digest_hex: str

def sha256_forward_trace(message: bytes) -> GlassKeyTrace:
    padded = pad_sha256(message)
    H = IV[:]
    blocks = []
    for bi in range(len(padded)//64):
        blk = padded[bi*64:(bi+1)*64]
        W = list(struct.unpack('>16I', blk))
        for t in range(16, 64):
            W.append((sig1(W[t-2]) + W[t-7] + sig0(W[t-15]) + W[t-16]) & MASK32)

        a,b,c,d,e,f,g,h = H
        rounds = []
        block_H_in = H[:]
        for t in range(64):
            pre = dict(a=a,b=b,c=c,d=d,e=e,f=f,g=g,h=h)
            sigma1 = Sig1(e)
            choose = Ch(e,f,g)
            t1_carry = add_carries(h, sigma1, choose, K[t], W[t])
            T1 = (h + sigma1 + choose + K[t] + W[t]) & MASK32

            sigma0 = Sig0(a)
            major = Maj(a,b,c)
            t2_carry = add_carries(sigma0, major)
            T2 = (sigma0 + major) & MASK32

            new_a = (T1 + T2) & MASK32
            new_e = (d + T1) & MASK32
            rounds.append({
                "block": bi,
                "round": t,
                "Wt": W[t],
                "Kt": K[t],
                "pre_a": a, "pre_b": b, "pre_c": c, "pre_d": d, "pre_e": e, "pre_f": f, "pre_g": g, "pre_h": h,
                "Sig1_e": sigma1, "Ch_efg": choose,
                "Sig0_a": sigma0, "Maj_abc": major,
                "T1": T1, "T2": T2,
                "T1_carry": t1_carry, "T2_carry": t2_carry,
                "T1_carry_bits": popcount(t1_carry), "T2_carry_bits": popcount(t2_carry),
                "post_a": new_a, "post_b": a, "post_c": b, "post_d": c,
                "post_e": new_e, "post_f": e, "post_g": f, "post_h": g,
                "delta_ae": (new_a - new_e) & MASK32,
                "sigma_ae": (new_a + new_e) & MASK32,
                "t2_minus_d": (T2 - d) & MASK32,
                "a_xor_e": (new_a ^ new_e) & MASK32,
            })
            a,b,c,d,e,f,g,h = new_a,a,b,c,new_e,e,f,g

        H = [(x+y) & MASK32 for x,y in zip(H, [a,b,c,d,e,f,g,h])]
        blocks.append({
            "block": bi,
            "raw_block": blk,
            "block_hex": blk.hex(),
            "block_ascii": to_printable(blk),
            "W": W,
            "rounds": rounds,
            "H_in": block_H_in,
            "H_internal_out": [a,b,c,d,e,f,g,h],
            "H_out": H[:],
        })
    digest_hex = ''.join(f"{x:08x}" for x in H)
    assert digest_hex == hashlib.sha256(message).hexdigest(), "hash mismatch"
    return GlassKeyTrace(message=message, padded=padded, blocks=blocks, digest_words=H, digest_hex=digest_hex)

def df_bytes(trace: GlassKeyTrace) -> pd.DataFrame:
    rows = []
    msg_len = len(trace.message)
    for i,b in enumerate(trace.padded):
        block = i // 64
        offset = i % 64
        word = offset // 4
        lane = offset % 4
        source = "MSG" if i < msg_len else ("PAD80" if i == msg_len else ("LEN" if i >= len(trace.padded)-8 else "PAD"))
        rows.append({
            "byte_index": i,
            "block": block,
            "offset": offset,
            "word": word,
            "lane": lane,
            "byte_hex": f"0x{b:02x}",
            "ascii": chr(b) if 32 <= b <= 126 else "·",
            "source": source,
        })
    return pd.DataFrame(rows)

def df_words(trace: GlassKeyTrace, block: int = 0) -> pd.DataFrame:
    blk = trace.blocks[block]
    rows = []
    for i, w in enumerate(blk["W"][:16]):
        bs = word_to_bytes(w)
        rows.append({
            "block": block,
            "word": i,
            "W": hex32(w),
            "bytes": ' '.join(f"{b:02x}" for b in bs),
            "ascii": to_printable(bs),
            "transitions": sum(bs[j] != bs[j-1] for j in range(1,4)),
            "bitcount": popcount(w),
        })
    return pd.DataFrame(rows)

def df_schedule(trace: GlassKeyTrace, block: int = 0, expanded: bool = True) -> pd.DataFrame:
    blk = trace.blocks[block]
    rng = range(64 if expanded else 16)
    rows = []
    for t in rng:
        w = blk["W"][t]
        rows.append({
            "block": block,
            "t": t,
            "W": hex32(w),
            "bitcount": popcount(w),
            "bytes": ' '.join(f"{b:02x}" for b in word_to_bytes(w)),
            "ascii": to_printable(word_to_bytes(w)),
            "src_t-16": t-16 if t>=16 else None,
            "src_t-15": t-15 if t>=16 else None,
            "src_t-7": t-7 if t>=16 else None,
            "src_t-2": t-2 if t>=16 else None,
        })
    return pd.DataFrame(rows)

def df_rounds(trace: GlassKeyTrace, block: int = 0) -> pd.DataFrame:
    rows = []
    for r in trace.blocks[block]["rounds"]:
        rows.append({
            "block": r["block"],
            "round": r["round"],
            "Wt": hex32(r["Wt"]),
            "Kt": hex32(r["Kt"]),
            "T1": hex32(r["T1"]),
            "T2": hex32(r["T2"]),
            "pre_a": hex32(r["pre_a"]),
            "pre_e": hex32(r["pre_e"]),
            "post_a": hex32(r["post_a"]),
            "post_e": hex32(r["post_e"]),
            "delta_ae": hex32(r["delta_ae"]),
            "sigma_ae": hex32(r["sigma_ae"]),
            "t2_minus_d": hex32(r["t2_minus_d"]),
            "shape_lock": r["delta_ae"] == r["t2_minus_d"],
            "T1_carry_bits": r["T1_carry_bits"],
            "T2_carry_bits": r["T2_carry_bits"],
        })
    return pd.DataFrame(rows)

def df_feedforward(trace: GlassKeyTrace) -> pd.DataFrame:
    rows = []
    for blk in trace.blocks:
        for i, (hin, hout, internal) in enumerate(zip(blk["H_in"], blk["H_out"], blk["H_internal_out"])):
            rows.append({
                "block": blk["block"],
                "lane": i,
                "H_in": hex32(hin),
                "internal_out": hex32(internal),
                "H_out": hex32(hout),
            })
    return pd.DataFrame(rows)

def df_weave(values, labels=None, name="x") -> pd.DataFrame:
    if labels is None:
        labels = list(range(len(values)))
    rows = []
    for i in range(len(values)-1):
        A = values[i] & MASK32
        B = values[i+1] & MASK32
        delta = (B - A) & MASK32
        sigma = (A + B) & MASK32
        p_budget = (sigma*sigma + delta*delta)
        rows.append({
            "i": i,
            "left_label": labels[i],
            "right_label": labels[i+1],
            f"{name}_left": hex32(A),
            f"{name}_right": hex32(B),
            "delta": hex32(delta),
            "sigma": hex32(sigma),
            "delta_bits": popcount(delta),
            "sigma_bits": popcount(sigma),
            "budget_int": p_budget,
        })
    return pd.DataFrame(rows)

def df_schedule_weave(trace: GlassKeyTrace, block: int = 0) -> pd.DataFrame:
    W = trace.blocks[block]["W"]
    return df_weave(W, labels=[f"W{t}" for t in range(64)], name="W")

def df_channel_weave(trace: GlassKeyTrace, block: int = 0, field: str = "post_a") -> pd.DataFrame:
    vals = [r[field] for r in trace.blocks[block]["rounds"]]
    return df_weave(vals, labels=[f"r{t}" for t in range(64)], name=field)

def summary(trace: GlassKeyTrace) -> pd.DataFrame:
    rows = []
    total_rounds = sum(len(b["rounds"]) for b in trace.blocks)
    rows.append({"field":"message_len","value":len(trace.message)})
    rows.append({"field":"padded_len","value":len(trace.padded)})
    rows.append({"field":"blocks","value":len(trace.blocks)})
    rows.append({"field":"rounds","value":total_rounds})
    rows.append({"field":"digest","value":trace.digest_hex})
    return pd.DataFrame(rows)

def show_case(name: str, message: bytes, block: int = 0, round_head: int = 12):
    from IPython.display import display, Markdown
    trace = sha256_forward_trace(message)
    display(Markdown(f"## GlassKey Viewer Alpha — {name}"))
    display(summary(trace))
    display(Markdown("### Byte stream"))
    display(df_bytes(trace).head(min(len(trace.padded), 32)))
    display(Markdown(f"### Block {block} input words W0..W15"))
    display(df_words(trace, block=block))
    display(Markdown(f"### Block {block} schedule W0..W63"))
    display(df_schedule(trace, block=block, expanded=True).head(20))
    display(Markdown(f"### Block {block} rounds"))
    display(df_rounds(trace, block=block).head(round_head))
    display(Markdown(f"### Block {block} feed-forward"))
    display(df_feedforward(trace).query("block == @block"))
    return trace

def run_alpha():
    from IPython.display import display, Markdown
    print("GlassKey Viewer Alpha — notebook-first forward pass orbit")
    print("Scope: bytes -> words -> schedule -> rounds -> feed-forward")
    print()
    t1 = show_case("abc", b"abc", block=0, round_head=16)
    print()
    t2 = show_case("GlassKey", b"GlassKey", block=0, round_head=16)
    print()
    print("Custom calls:")
    print("  trace = sha256_forward_trace(b'abc')")
    print("  df_bytes(trace)")
    print("  df_words(trace, 0)")
    print("  df_schedule(trace, 0, expanded=True)")
    print("  df_rounds(trace, 0)")
    print("  df_feedforward(trace)")
    print("  df_schedule_weave(trace, 0)")
    print("  df_channel_weave(trace, 0, 'post_a')")
    return t1, t2
