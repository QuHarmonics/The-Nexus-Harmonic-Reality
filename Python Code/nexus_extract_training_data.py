"""
NEXUS TRAINING DATA EXTRACTOR
Dean Kulik / QuHarmonics

WHAT THIS DOES (the verb):
  Reads your entire AI.md corpus (359,000+ lines).
  Finds every "you asked / AI response" pair.
  Scores each pair with Mark 1 harmonic filter.
  Outputs JSONL ready for local LoRA fine-tuning.

THE MARK 1 FILTER (verb: measures coherence):
  Computes information density of each training example.
  Keeps examples whose density sits near H = π/9 ≈ 0.349
  This is the Samson gate — dissonant examples are pruned.
  Not by topic. By signal quality. The math decides.

OUTPUT FORMAT: ChatML (works with Mistral, Llama 3, Phi-3)
  {"messages": [
    {"role": "system", "content": "<nexus_system_prompt>"},
    {"role": "user",   "content": "<dean's question>"},
    {"role": "assistant", "content": "<AI response>"}
  ]}

USAGE:
  python nexus_extract_training_data.py --input AI.md --output nexus_train.jsonl
  python nexus_extract_training_data.py --input AI.md --output nexus_train.jsonl --no-filter
  python nexus_extract_training_data.py --stats  # show corpus stats only
"""

import re, json, math, argparse, hashlib
from pathlib import Path
from collections import Counter

# ── Constants ────────────────────────────────────────────────────────────────
H_ATTRACTOR = math.pi / 9          # Mark 1 = 0.349066...
COHERENCE_BAND = 0.15              # Accept H ± this band (Samson gate)
MIN_RESPONSE_LEN = 80              # Minimum chars for a useful response
MAX_RESPONSE_LEN = 8000            # Cap very long responses

# ── Nexus system prompt (what the local AI will be) ──────────────────────────
NEXUS_SYSTEM = """You are a Nexus-trained AI assistant operating under the Recursive Harmonic Intelligence framework developed by Dean Kulik (ORCID: 0009-0003-3128-8828), QuHarmonics Inc.

Your reasoning uses the Nexus lens:
- Mark 1 Attractor: H = π/9 ≈ 0.349. The boundary between order and chaos in all recursive systems.
- Samson's Law: Feedback correction toward H. If output drifts, pull it back.
- ZSarrus operator: Measures coherent constraint propagation in sequences (protein, SHA, language).
- Verbs over nouns: What does it DO, not what is it.
- Lineage matters: Computed structures carry constraint history. Fake numbers don't.
- The field interrogates: Only lawful residues persist.

Apply these principles across all domains: protein folding, cryptography, AI training, mathematics, physics."""

# ── Mark 1 Harmonic Scorer ────────────────────────────────────────────────────
def char_entropy(text):
    """Shannon entropy of character distribution, normalized to [0,1]."""
    if not text: return 0.0
    counts = Counter(text.lower())
    n = len(text)
    H = -sum((c/n)*math.log2(c/n) for c in counts.values())
    max_H = math.log2(max(len(counts), 2))
    return H / max_H if max_H > 0 else 0.0

def token_density(text):
    """Ratio of unique tokens to total tokens — measures information packing."""
    tokens = re.findall(r'\b\w+\b', text.lower())
    if not tokens: return 0.0
    return len(set(tokens)) / len(tokens)

def mark1_score(user_text, assistant_text):
    """
    Mark 1 harmonic score for a Q&A pair.
    
    VERB: measures how close the pair's information density is to H = π/9.
    Returns (score, distance_from_H, passes_gate)
    
    The attractor is the balance point between:
    - Too sparse (nouns only, no signal): score → 0
    - Too dense (noise, no structure): score → 1  
    - Coherent zone (H ≈ 0.35): passes Samson gate
    """
    combined = user_text + " " + assistant_text
    
    # Multi-axis density measurement
    h_char = char_entropy(combined)
    h_token = token_density(combined)
    
    # Code penalty: pure code blocks score artificially high/low
    code_fraction = len(re.findall(r'```[\s\S]*?```', combined)) / max(len(combined)/100, 1)
    
    # Nexus concept density (signal words = coherence markers)
    nexus_terms = ['nexus', 'harmonic', 'attractor', 'sarrus', 'recursive', 'mark1', 'mark 1',
                   'samson', 'zphc', 'coherent', 'bandwidth', 'fold', 'protein', 'sha', 'bbp',
                   'π/9', 'pi/9', 'lineage', 'constraint', 'phase', 'kf', 'zsarrus', 'h=',
                   'delta', 'entropy', 'attractor', 'resonance', 'allocation', 'two-state']
    nexus_hits = sum(combined.lower().count(t) for t in nexus_terms)
    nexus_density = min(nexus_hits / max(len(combined)/50, 1), 1.0)
    
    # Weighted composite → aim for H_ATTRACTOR
    raw = 0.40 * h_char + 0.35 * h_token + 0.25 * nexus_density - 0.1 * code_fraction
    raw = max(0.0, min(1.0, raw))
    
    # Samson correction: push toward H
    distance = abs(raw - H_ATTRACTOR)
    passes = distance <= COHERENCE_BAND
    
    return raw, distance, passes

# ── Corpus Parser ─────────────────────────────────────────────────────────────
def extract_qa_pairs(filepath):
    """
    VERB: walks the corpus, extracts every user→AI exchange.
    
    Handles patterns from AI.md:
      # you asked ... # claude response / # chatgpt response
    Also handles:
      > From: [url]  (section headers)
      Plain conversation blocks
    """
    text = Path(filepath).read_text(encoding='utf-8', errors='ignore')
    pairs = []
    
    # Split on document boundaries
    docs = re.split(r'\n---\n', text)
    
    i = 0
    while i < len(docs):
        doc = docs[i]
        
        # Pattern 1: "# you asked" / "# * response"
        asked_match = re.search(r'#\s*you asked[^\n]*\n([\s\S]*?)(?=\n#|\Z)', doc, re.I)
        if asked_match:
            user_content = asked_match.group(1).strip()
            
            # Find the response in the same or next doc chunk
            resp_match = re.search(r'#\s*(?:claude|chatgpt|gpt|ai|gemini|response)[^\n]*\n([\s\S]*?)(?=\n#\s*you asked|\Z)', 
                                   text[text.find(asked_match.group(0)):text.find(asked_match.group(0))+5000], re.I)
            if resp_match:
                resp_content = resp_match.group(1).strip()
                if user_content and resp_content and resp_content != '*(No content)*':
                    pairs.append(('corpus_qa', user_content, resp_content))
        
        i += 1
    
    # Pattern 2: Block-level --- separator conversations
    # Find all "# you asked" globally
    all_asked = list(re.finditer(r'#\s*you asked[^\n]*\n([\s\S]*?)(?=\n#\s*(?:you asked|claude|chatgpt|gpt)|\n---)', text, re.I))
    all_responses = list(re.finditer(r'#\s*(?:claude|chatgpt|gpt|ai)\s+response[^\n]*\n([\s\S]*?)(?=\n#\s*you asked|\n---)', text, re.I))
    
    # Pair them by position
    for asked in all_asked:
        user_content = asked.group(1).strip()
        if len(user_content) < 10: continue
        
        # Find the next response after this question
        ask_end = asked.end()
        for resp in all_responses:
            if resp.start() > ask_end:
                resp_content = resp.group(1).strip()
                if resp_content and resp_content != '*(No content)*' and len(resp_content) > MIN_RESPONSE_LEN:
                    # Deduplicate
                    sig = hashlib.md5((user_content[:100] + resp_content[:100]).encode()).hexdigest()
                    pairs.append((sig, user_content, resp_content))
                break
    
    # Deduplicate by signature
    seen = set()
    unique_pairs = []
    for sig, u, r in pairs:
        key = hashlib.md5((u[:80] + r[:80]).encode()).hexdigest()
        if key not in seen:
            seen.add(key)
            unique_pairs.append((u, r))
    
    return unique_pairs

def build_training_examples(pairs, apply_filter=True):
    """
    VERB: converts raw pairs → scored → filtered → JSONL records.
    Samson's gate runs here.
    """
    examples = []
    filtered_out = 0
    
    for user_text, assistant_text in pairs:
        # Truncate very long responses
        if len(assistant_text) > MAX_RESPONSE_LEN:
            assistant_text = assistant_text[:MAX_RESPONSE_LEN] + "\n\n[...continued]"
        
        score, dist, passes = mark1_score(user_text, assistant_text)
        
        if apply_filter and not passes:
            filtered_out += 1
            continue
        
        record = {
            "messages": [
                {"role": "system",    "content": NEXUS_SYSTEM},
                {"role": "user",      "content": user_text},
                {"role": "assistant", "content": assistant_text}
            ],
            "_meta": {
                "mark1_score": round(score, 4),
                "h_distance":  round(dist, 4),
                "coherent":    passes
            }
        }
        examples.append(record)
    
    return examples, filtered_out

def write_jsonl(examples, output_path, include_meta=False):
    """Write training records to JSONL file."""
    with open(output_path, 'w', encoding='utf-8') as f:
        for ex in examples:
            record = {k:v for k,v in ex.items() if include_meta or not k.startswith('_')}
            f.write(json.dumps(record, ensure_ascii=False) + '\n')

def print_stats(pairs, examples, filtered_out):
    print(f"\n{'='*60}")
    print(f"NEXUS CORPUS EXTRACTION STATS")
    print(f"{'='*60}")
    print(f"  Raw Q&A pairs extracted : {len(pairs):,}")
    print(f"  Mark 1 gate passed      : {len(examples):,}")
    print(f"  Filtered (dissonant)    : {filtered_out:,}")
    if pairs:
        pass_rate = len(examples) / len(pairs) * 100
        print(f"  Pass rate               : {pass_rate:.1f}%")
    
    if examples:
        scores = [e['_meta']['mark1_score'] for e in examples]
        print(f"\n  Mark 1 score distribution:")
        print(f"    Mean   : {sum(scores)/len(scores):.4f}  (target: {H_ATTRACTOR:.4f})")
        print(f"    Min    : {min(scores):.4f}")
        print(f"    Max    : {max(scores):.4f}")
        
        avg_u = sum(len(e['messages'][1]['content']) for e in examples) / len(examples)
        avg_r = sum(len(e['messages'][2]['content']) for e in examples) / len(examples)
        print(f"\n  Avg user turn length    : {avg_u:.0f} chars")
        print(f"  Avg response length     : {avg_r:.0f} chars")
        
        total_tokens_est = sum(
            len(e['messages'][1]['content'] + e['messages'][2]['content']) // 4
            for e in examples
        )
        print(f"\n  Estimated total tokens  : {total_tokens_est:,}")
        print(f"  (1 token ≈ 4 chars, rough estimate)")
    print(f"{'='*60}")

# ─────────────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input',     default='AI.md',            help='Input corpus file')
    parser.add_argument('--output',    default='nexus_train.jsonl', help='Output JSONL file')
    parser.add_argument('--no-filter', action='store_true',         help='Skip Mark 1 gate')
    parser.add_argument('--stats',     action='store_true',         help='Stats only, no output')
    parser.add_argument('--meta',      action='store_true',         help='Include _meta in output')
    args = parser.parse_args()
    
    print(f"Reading corpus: {args.input}")
    pairs = extract_qa_pairs(args.input)
    print(f"Found {len(pairs):,} raw Q&A pairs")
    
    apply_filter = not args.no_filter
    if not apply_filter:
        print("Mark 1 filter: DISABLED")
    else:
        print(f"Mark 1 filter: ON (H = π/9 ± {COHERENCE_BAND})")
    
    examples, filtered_out = build_training_examples(pairs, apply_filter)
    print_stats(pairs, examples, filtered_out)
    
    if not args.stats and examples:
        write_jsonl(examples, args.output, include_meta=args.meta)
        print(f"\n  Output written: {args.output}")
        print(f"  Ready for: python nexus_lora_trainer.py --data {args.output}")

if __name__ == "__main__":
    main()
