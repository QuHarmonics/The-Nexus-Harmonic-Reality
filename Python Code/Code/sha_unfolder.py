# sha_unfolder.py — Analyze + Echo-align SHA-256 (Nexus 4 field unfolding)
import argparse, json, math, os, random, sys, importlib.util
from typing import List, Dict, Tuple

HERE = os.path.dirname(os.path.abspath(__file__))
N4_PATH = os.path.join(HERE, "nexus4_psi.py")

# --- Load nexus4_psi dynamically ---
if not os.path.exists(N4_PATH):
    sys.stderr.write("Required file nexus4_psi.py not found next to sha_unfolder.py\n")
    sys.exit(2)
spec = importlib.util.spec_from_file_location("nexus4_psi", N4_PATH)
n4 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(n4)

# ------------------- Utilities -------------------
def top_windows(nibbles: List[int], k: int = 10):
    out = []
    for i in range(len(nibbles)-2):
        a,b,c = sorted((nibbles[i], nibbles[i+1], nibbles[i+2]), reverse=True)
        if a == 0:
            continue
        s = b / a
        ZH = min(abs(s - n4.H_MARK1), abs(s - (1.0-n4.H_MARK1)), abs(s - 0.5))
        eps = (b + c - a)/a
        kind = "constructive" if eps>0 else ("ray" if abs(eps)<1e-12 else "invalid")
        out.append({
            "i": i, "triad": [int(a), int(b), int(c)],
            "kind": kind, "s": s, "Z_H": ZH, "eps": eps
        })
    out.sort(key=lambda r: r["Z_H"])
    return out[:max(0,k)]

def feature_vector(feats: Dict[str, float]):
    return [
        feats.get("H", 0.0),
        feats.get("rcq", 0.0),
        min(1.0, abs(feats.get("avg_abs_eps", 0.0))),
        min(1.0, abs(feats.get("avg_ZH", 0.0))),
        min(1.0, abs(feats.get("avg_Zsym", 0.0))),
        max(0.0, min(1.0, feats.get("avg_Knorm", 0.0))),
    ]

def feature_distance(f_cand, f_tgt, weights):
    return sum(w*abs(a-b) for (w,a,b) in zip(weights, f_cand, f_tgt))

def mutate_ascii(s: str, step=1, p_ops=(0.6, 0.3, 0.1)):
    import string
    b = bytearray(s.encode('utf-8', errors='ignore') or b'?')
    r = random.random()
    if r < p_ops[0]:  # jitter a byte
        i = random.randrange(len(b))
        delta = random.choice([-step, step])
        b[i] = max(0, min(255, b[i] + delta))
    elif r < p_ops[0]+p_ops[1] and len(b) > 1:  # swap two
        i, j = random.sample(range(len(b)), 2)
        b[i], b[j] = b[j], b[i]
    else:  # insert/delete (light touch)
        if random.random() < 0.5 and len(b) > 1:
            del b[random.randrange(len(b))]
        else:
            ins = random.choice((list(range(32,127)) + [10,32]))
            b.insert(random.randrange(len(b)+1), ins)
    out = b.decode('utf-8', errors='ignore')
    return out if out else s

def analyze_text(text: str):
    return n4.analyze_ascii(text)

def analyze_hex(hex_digest: str):
    return n4.analyze_hex(hex_digest)

# ------------------- Commands -------------------
def cmd_analyze(args):
    if args.text:
        res = analyze_text(args.text)
        nibbles = n4.hex_to_nibbles(res["hex"])
    else:
        res = analyze_hex(args.hex)
        nibbles = n4.hex_to_nibbles(args.hex)
    tops = top_windows(nibbles, k=args.top)
    res2 = {"summary": res, "top_windows": tops}
    if args.md:
        write_md_report(args.md, res2, args.text, args.hex)
    print(json.dumps(res2, indent=2))

def write_md_report(path, data, text, hex_digest):
    lines = []
    lines.append("# SHA Unfolding Report")
    src = f"text `{text}`" if text is not None else f"hex `{hex_digest}`"
    lines.append(f"**Source:** {src}")
    lines.append("")
    lines.append("## Summary Features")
    lines.append("```json")
    import json as _json
    lines.append(_json.dumps(data["summary"], indent=2))
    lines.append("```")
    lines.append("")
    lines.append("## Top windows (lowest Z_H)")
    lines.append("")
    lines.append("| i | triad | kind | s=b/a | Z_H | eps |")
    lines.append("|---:|:-----:|:----:|:-----:|:---:|:---:|")
    for r in data["top_windows"]:
        lines.append(f"| {r['i']} | {r['triad']} | {r['kind']} | {r['s']:.6f} | {r['Z_H']:.6f} | {r['eps']:.6f} |")
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

def cmd_echo(args):
    # target features
    if args.target_text:
        tgt = analyze_text(args.target_text)
        tgt_hex = tgt["hex"]
    else:
        tgt = analyze_hex(args.target_hex)
        tgt_hex = args.target_hex.lower()
    f_tgt = feature_vector(tgt)

    # weights
    if args.weights:
        weights = [float(x) for x in args.weights.split(",")]
        assert len(weights) == 6
        s = sum(weights)
        weights = [w/s for w in weights]
    else:
        weights = [0.30, 0.15, 0.10, 0.25, 0.10, 0.10]

    temp = args.temp
    cool = args.cool

    cur = args.seed
    cur_res = analyze_text(cur)
    f_cur = feature_vector(cur_res)
    cur_loss = feature_distance(f_cur, f_tgt, weights)
    best = dict(text=cur, hex=cur_res["hex"], loss=cur_loss, feats=cur_res)

    for it in range(args.iters):
        cand = mutate_ascii(cur, step=args.step)
        cand_res = analyze_text(cand)
        f_cand = feature_vector(cand_res)
        cand_loss = feature_distance(f_cand, f_tgt, weights)

        accept = False
        if cand_loss < cur_loss:
            accept = True
        else:
            if random.random() < math.exp(-(cand_loss - cur_loss)/max(1e-9,temp)):
                accept = True

        if accept:
            cur, cur_res, f_cur, cur_loss = cand, cand_res, f_cand, cand_loss
            if cand_loss < best["loss"]:
                best = dict(text=cur, hex=cur_res["hex"], loss=cur_loss, feats=cur_res)
        temp *= cool

    out = {
        "target_hex": tgt_hex,
        "target_feats": tgt,
        "weights": weights,
        "best_text": best["text"],
        "best_hex": best["hex"],
        "best_loss": best["loss"],
        "best_feats": best["feats"],
    }
    if args.md:
        write_md_echo(args.md, out)
    print(json.dumps(out, indent=2))

def write_md_echo(path, data):
    lines = []
    lines.append("# SHA Echo-Alignment Result")
    lines.append(f"**Target hex:** `{data['target_hex']}`")
    lines.append("")
    lines.append("## Target features")
    lines.append("```json")
    import json as _json
    lines.append(_json.dumps(data["target_feats"], indent=2))
    lines.append("```")
    lines.append("")
    lines.append("## Best echo candidate")
    lines.append(f"**Text:** `{data['best_text']}`")
    lines.append(f"**Hex:** `{data['best_hex']}`")
    lines.append(f"**Loss:** `{data['best_loss']:.6f}`")
    lines.append("")
    lines.append("### Candidate features")
    lines.append("```json")
    import json as _json2
    lines.append(_json2.dumps(data["best_feats"], indent=2))
    lines.append("```")
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

def main():
    p = argparse.ArgumentParser(description="SHA Unfolding (Nexus 4 field echo)")
    sub = p.add_subparsers(dest="cmd", required=True)

    pa = sub.add_parser("analyze", help="Analyze a text or hex digest")
    g = pa.add_mutually_exclusive_group(required=True)
    g.add_argument("--text", type=str)
    g.add_argument("--hex", type=str)
    pa.add_argument("--top", type=int, default=10, help="top-k windows by lowest Z_H")
    pa.add_argument("--md", type=str, help="optional markdown report path")
    pa.set_defaults(func=cmd_analyze)

    pe = sub.add_parser("echo", help="Echo-align a seed message to target digest features")
    g2 = pe.add_mutually_exclusive_group(required=True)
    g2.add_argument("--target-text", type=str)
    g2.add_argument("--target-hex", type=str)
    pe.add_argument("--seed", type=str, default="Nexus")
    pe.add_argument("--iters", type=int, default=3000)
    pe.add_argument("--step", type=int, default=1)
    pe.add_argument("--temp", type=float, default=0.05)
    pe.add_argument("--cool", type=float, default=0.999)
    pe.add_argument("--weights", type=str, help="comma list of 6 weights for (H,RCQ,eps,ZH,Zsym,K)")
    pe.add_argument("--md", type=str, help="optional markdown report path")
    pe.set_defaults(func=cmd_echo)

    args = p.parse_args()
    args.func(args)

if __name__ == "__main__":
    main()
