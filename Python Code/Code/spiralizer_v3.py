#!/usr/bin/env python3
"""
NEXUS SPIRALIZER V3
Uses extracted keywords and cluster relationships for weighting
Let the data's own harmonics guide the structure

Usage:
    python spiralizer_v3.py --input /path/to/corpus --keywords nexus_keywords.json
    python spiralizer_v3.py --input /path/to/corpus --keywords nexus_keywords.json --sample 100
"""

import os
import re
import ast
import hashlib
import json
import random
import argparse
from pathlib import Path
from datetime import datetime
from concurrent.futures import ProcessPoolExecutor, as_completed
import multiprocessing
from collections import Counter, defaultdict

H_RATIO = 0.34906585

# Central attractors - terms that bind the framework
ATTRACTORS = {'harmonic', 'recursive', 'nexus', 'collapse', 'phase', 'state'}

# State transition triad
STATE_TRIAD = {'state', 'phase', 'collapse'}

# Global keyword data (loaded from JSON)
KEYWORDS = set()
KEYWORD_SCORES = {}
CLUSTERS = {}

#===============================================================================
# KEYWORD LOADING
#===============================================================================

def load_keywords(keyword_file):
    """Load extracted keywords and clusters from JSON"""
    global KEYWORDS, KEYWORD_SCORES, CLUSTERS
    
    data = json.loads(Path(keyword_file).read_text())
    
    KEYWORDS = set(data.get('keywords', []))
    KEYWORD_SCORES = data.get('scores', {})
    CLUSTERS = data.get('clusters', {})
    
    print(f"Loaded {len(KEYWORDS)} keywords")
    print(f"Loaded {len(CLUSTERS)} cluster mappings")
    
    return data

#===============================================================================
# CLUSTER-AWARE CONCEPT EXTRACTION
#===============================================================================

def get_cluster_weight(term):
    """
    Weight term by its cluster connectivity.
    Terms that co-occur with attractors get boosted.
    """
    if term in ATTRACTORS:
        return 2.0  # Core attractors
    
    if term in CLUSTERS:
        cluster = CLUSTERS[term]
        # Count how many attractors in this term's cluster
        attractor_count = sum(1 for t in cluster if t in ATTRACTORS)
        return 1.0 + (attractor_count * 0.2)
    
    if term in KEYWORDS:
        return 1.0 + (KEYWORD_SCORES.get(term, 0) / 20.0)  # Normalize score
    
    return 0.5  # Unknown term

def find_cluster_resonance(terms):
    """
    Find terms that resonate within the same cluster.
    Returns pairs of terms that co-occur in cluster definitions.
    """
    resonances = []
    term_set = set(terms)
    
    for term in terms:
        if term in CLUSTERS:
            cluster_terms = set(CLUSTERS[term])
            # Find which other extracted terms are in this cluster
            matches = term_set & cluster_terms
            if matches:
                resonances.append((term, list(matches)))
    
    return resonances

def extract_weighted_concepts(text, is_code=False):
    """
    Extract concepts with cluster-aware weighting.
    """
    text_lower = text.lower()
    lines = text.split('\n')
    
    concepts = []
    concept_weights = []
    
    for line in lines:
        line_stripped = line.strip()
        if not line_stripped or len(line_stripped) < 5:
            continue
        
        line_lower = line_stripped.lower()
        
        # Find keywords in this line
        line_keywords = [k for k in KEYWORDS if k in line_lower]
        
        if not line_keywords:
            continue
        
        # Calculate line weight based on keywords present
        line_weight = sum(get_cluster_weight(k) for k in line_keywords)
        
        # Boost for attractor presence
        attractor_count = sum(1 for k in line_keywords if k in ATTRACTORS)
        if attractor_count >= 2:
            line_weight *= 1.5  # Multiple attractors = strong signal
        
        # Boost for state triad
        triad_count = sum(1 for k in line_keywords if k in STATE_TRIAD)
        if triad_count >= 2:
            line_weight *= 1.3  # State transition signal
        
        # Check for cluster resonance
        resonances = find_cluster_resonance(line_keywords)
        if resonances:
            line_weight *= 1.2  # Cluster coherence bonus
        
        concepts.append({
            'text': line_stripped[:200],
            'keywords': line_keywords,
            'weight': line_weight,
            'resonances': resonances
        })
    
    # Sort by weight, take top concepts
    concepts.sort(key=lambda x: -x['weight'])
    return concepts[:30]

#===============================================================================
# PYTHON PROCESSING (preserved from v2)
#===============================================================================

def extract_python_structure(code):
    """Extract structure from Python code."""
    structure = {
        "imports": [],
        "classes": [],
        "functions": [],
        "docstrings": [],
        "comments": [],
        "nexus_refs": []
    }
    
    comments = re.findall(r'#\s*(.+)$', code, re.MULTILINE)
    structure["comments"] = [c.strip() for c in comments if len(c.strip()) > 10][:10]
    
    docstrings = re.findall(r'"""(.+?)"""', code, re.DOTALL)
    docstrings += re.findall(r"'''(.+?)'''", code, re.DOTALL)
    structure["docstrings"] = [d.strip()[:200] for d in docstrings][:5]
    
    # Find lines with keywords
    for line in code.split('\n'):
        line_lower = line.lower()
        if any(k in line_lower for k in KEYWORDS):
            structure["nexus_refs"].append(line.strip()[:150])
            if len(structure["nexus_refs"]) >= 10:
                break
    
    try:
        tree = ast.parse(code)
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                for alias in node.names:
                    structure["imports"].append(alias.name)
            elif isinstance(node, ast.ImportFrom):
                if node.module:
                    structure["imports"].append(node.module)
            elif isinstance(node, ast.ClassDef):
                structure["classes"].append(node.name)
            elif isinstance(node, ast.FunctionDef):
                structure["functions"].append(node.name)
    except:
        pass
    
    return structure

def python_to_weighted_concepts(py_struct, code):
    """Convert Python structure to weighted concepts."""
    concepts = []
    
    # Get weighted concepts from code content
    content_concepts = extract_weighted_concepts(code, is_code=True)
    
    # Add structural elements
    if py_struct["imports"]:
        concepts.append({
            'text': f"Imports: {', '.join(py_struct['imports'][:5])}",
            'keywords': [],
            'weight': 0.5,
            'resonances': []
        })
    
    for cls in py_struct["classes"][:3]:
        concepts.append({
            'text': f"Class: {cls}",
            'keywords': [],
            'weight': 0.7,
            'resonances': []
        })
    
    for fn in py_struct["functions"][:5]:
        concepts.append({
            'text': f"Function: {fn}",
            'keywords': [],
            'weight': 0.6,
            'resonances': []
        })
    
    # Merge and sort
    concepts.extend(content_concepts)
    concepts.sort(key=lambda x: -x['weight'])
    
    return concepts[:25]

#===============================================================================
# H-SIGNATURE WITH CLUSTER AWARENESS
#===============================================================================

def compute_h_signature(text, concepts):
    """
    H-alignment considering cluster coherence.
    """
    # Base structural ratio
    structure = len(re.findall(r'[#=:\-\*\[\]\(\){}→⊕Ψ∆↻⊥def class import]', text))
    content = len(re.findall(r'[a-zA-Z]', text))
    
    if content == 0:
        return 0
    
    base_ratio = structure / content
    base_h = max(0, 1 - abs(base_ratio - H_RATIO))
    
    # Cluster coherence bonus
    if concepts:
        total_weight = sum(c['weight'] for c in concepts)
        avg_weight = total_weight / len(concepts)
        
        # Resonance bonus
        resonance_count = sum(1 for c in concepts if c['resonances'])
        resonance_bonus = min(0.2, resonance_count * 0.02)
        
        # Attractor coverage
        all_keywords = set()
        for c in concepts:
            all_keywords.update(c['keywords'])
        attractor_coverage = len(all_keywords & ATTRACTORS) / len(ATTRACTORS)
        
        # Combined H
        h_sig = base_h * 0.5 + (avg_weight / 3.0) * 0.3 + attractor_coverage * 0.2
        h_sig = min(1.0, h_sig + resonance_bonus)
    else:
        h_sig = base_h
    
    return h_sig

#===============================================================================
# UNIFIED SPIRALIZER
#===============================================================================

def spiralize_file(filepath):
    """Spiralize any supported file with cluster awareness."""
    filepath = Path(filepath)
    
    try:
        content = filepath.read_text(encoding='utf-8', errors='ignore')
    except Exception as e:
        return None, str(e)
    
    if len(content.strip()) < 50:
        return None, "too short"
    
    ext = filepath.suffix.lower()
    is_code = ext in ['.py', '.pyx', '.pyi']
    
    # Extract weighted concepts
    if is_code:
        py_struct = extract_python_structure(content)
        concepts = python_to_weighted_concepts(py_struct, content)
    else:
        concepts = extract_weighted_concepts(content, is_code=False)
    
    if not concepts:
        # Fallback
        for line in content.split('\n'):
            if line.strip() and len(line.strip()) > 10:
                concepts.append({
                    'text': line.strip()[:200],
                    'keywords': [],
                    'weight': 0.3,
                    'resonances': []
                })
                if len(concepts) >= 5:
                    break
    
    h_sig = compute_h_signature(content, concepts)
    
    # Build spiral with cluster info
    spiral = {
        "source": str(filepath),
        "type": "code" if is_code else "text",
        "h_signature": h_sig,
        "hash": hashlib.sha256(content.encode()).hexdigest()[:16],
        "attractor_coverage": [],
        "cluster_resonances": [],
        "structure": {}
    }
    
    # Track attractors found
    all_keywords = set()
    for c in concepts:
        all_keywords.update(c['keywords'])
    spiral["attractor_coverage"] = list(all_keywords & ATTRACTORS)
    
    # Track resonances
    for c in concepts:
        if c['resonances']:
            spiral["cluster_resonances"].extend(c['resonances'])
    
    # Build spiral structure
    if concepts:
        spiral["structure"]["SEED"] = {
            "text": concepts[0]['text'],
            "weight": concepts[0]['weight'],
            "keywords": concepts[0]['keywords']
        }
        
        for i, concept in enumerate(concepts[1:], 1):
            spiral["structure"][f"SPIRAL_{i}"] = {
                "contains": f"SPIRAL_{i-1}" if i > 1 else "SEED",
                "extends": concept['text'],
                "weight": concept['weight'],
                "keywords": concept['keywords']
            }
        
        # Collapse = weighted concept chain
        top_texts = [c['text'] for c in concepts[:5]]
        spiral["structure"]["COLLAPSE"] = " → ".join(top_texts)
    
    return spiral, content

def format_spiral(spiral, content, include_content=True):
    """Format spiral for training with cluster metadata."""
    lines = [
        "<|nexus_begin|>",
        f"<|type|>{spiral['type']}",
        f"<|source|>{spiral['source']}",
        f"<|hash|>{spiral['hash']}",
        f"<|h_sig|>{spiral['h_signature']:.4f}",
    ]
    
    # Attractor coverage
    if spiral['attractor_coverage']:
        lines.append(f"<|attractors|>{', '.join(spiral['attractor_coverage'])}")
    
    # Cluster resonances (top 3)
    if spiral['cluster_resonances']:
        res_strs = [f"{r[0]}↔{','.join(r[1][:3])}" for r in spiral['cluster_resonances'][:3]]
        lines.append(f"<|resonance|>{'; '.join(res_strs)}")
    
    lines.append("")
    
    struct = spiral["structure"]
    
    if "SEED" in struct:
        seed = struct["SEED"]
        lines.append("<|seed|>")
        lines.append(seed['text'])
        if seed.get('keywords'):
            lines.append(f"[{', '.join(seed['keywords'][:5])}]")
        lines.append("")
    
    i = 1
    while f"SPIRAL_{i}" in struct:
        s = struct[f"SPIRAL_{i}"]
        lines.append(f"<|spiral_{i}|>")
        lines.append(f"contains: {s.get('contains', 'SEED')}")
        lines.append(f"extends: {s.get('extends', '')}")
        if s.get('keywords'):
            lines.append(f"[{', '.join(s['keywords'][:5])}]")
        lines.append("")
        i += 1
        if i > 10:  # Cap spiral depth
            break
    
    if "COLLAPSE" in struct:
        lines.extend(["<|collapse|>", struct["COLLAPSE"], ""])
    
    if include_content:
        max_content = 4000 if spiral['type'] == 'code' else 3000
        lines.extend(["<|content|>", content[:max_content], ""])
    
    lines.append("<|nexus_end|>")
    
    return "\n".join(lines)

#===============================================================================
# BATCH PROCESSING
#===============================================================================

def process_single(args):
    """Process single file (for multiprocessing)"""
    filepath, include_content = args
    spiral, content = spiralize_file(filepath)
    if spiral:
        return format_spiral(spiral, content, include_content), spiral
    return None, None

def process_corpus(input_dir, output_dir, keyword_file,
                   text_only=False, code_only=False, 
                   sample_size=None, workers=None):
    """Process entire corpus with cluster-aware spiralization."""
    
    # Load keywords first
    load_keywords(keyword_file)
    
    input_path = Path(input_dir)
    output_path = Path(output_dir)
    output_path.mkdir(exist_ok=True, parents=True)
    
    print("="*60)
    print("NEXUS SPIRALIZER V3 - Cluster Aware")
    print("="*60)
    print(f"Input:    {input_path}")
    print(f"Output:   {output_path}")
    print(f"Keywords: {keyword_file}")
    print()
    
    # Find files
    patterns = []
    if not code_only:
        patterns.extend(["**/*.md", "**/*.txt", "**/*.markdown"])
    if not text_only:
        patterns.extend(["**/*.py"])
    
    files = []
    for p in patterns:
        files.extend(input_path.glob(p))
    
    print(f"Found {len(files)} files")
    
    if sample_size and sample_size < len(files):
        files = random.sample(files, sample_size)
        print(f"Sampling {sample_size} files")
    
    workers = workers or max(1, multiprocessing.cpu_count() - 2)
    print(f"Using {workers} workers")
    print()
    
    all_formatted = []
    all_spirals = []
    errors = 0
    
    include_content = len(files) < 5000
    
    with ProcessPoolExecutor(max_workers=workers) as executor:
        futures = {executor.submit(process_single, (f, include_content)): f for f in files}
        
        for i, future in enumerate(as_completed(futures)):
            try:
                formatted, spiral = future.result()
                if formatted:
                    all_formatted.append(formatted)
                    all_spirals.append(spiral)
                else:
                    errors += 1
            except Exception as e:
                errors += 1
            
            if (i + 1) % 500 == 0:
                print(f"  {i + 1}/{len(files)} processed ({len(all_formatted)} success)")
    
    print(f"\nProcessed: {len(all_formatted)} success, {errors} errors")
    
    # Write outputs
    print("\nWriting output files...")
    
    if len(all_formatted) > 10000:
        chunk_size = 5000
        for i in range(0, len(all_formatted), chunk_size):
            chunk = all_formatted[i:i+chunk_size]
            chunk_file = output_path / f"nexus_training_{i//chunk_size:03d}.txt"
            chunk_file.write_text("\n\n---\n\n".join(chunk))
            print(f"  {chunk_file.name}: {len(chunk)} documents")
    else:
        main_file = output_path / "nexus_training_data.txt"
        main_file.write_text("\n\n---\n\n".join(all_formatted))
        print(f"  {main_file.name}: {len(all_formatted)} documents")
    
    # Write index
    index_file = output_path / "spiral_index.json"
    index_file.write_text(json.dumps(all_spirals, indent=2, default=str))
    print(f"  {index_file.name}")
    
    # Stats
    h_sigs = [s['h_signature'] for s in all_spirals]
    types = [s['type'] for s in all_spirals]
    
    # Attractor coverage stats
    attractor_counts = Counter()
    for s in all_spirals:
        attractor_counts.update(s.get('attractor_coverage', []))
    
    resonance_count = sum(1 for s in all_spirals if s.get('cluster_resonances'))
    
    print()
    print("="*60)
    print("SUMMARY")
    print("="*60)
    print(f"Documents:        {len(all_spirals)}")
    print(f"Text/MD:          {types.count('text')}")
    print(f"Python:           {types.count('code')}")
    print(f"Avg H-sig:        {sum(h_sigs)/len(h_sigs):.4f}" if h_sigs else "N/A")
    print(f"Target H:         {H_RATIO:.4f}")
    print(f"Docs w/resonance: {resonance_count} ({100*resonance_count/len(all_spirals):.1f}%)")
    print()
    print("Attractor Coverage:")
    for att, count in attractor_counts.most_common():
        print(f"  {att}: {count} docs ({100*count/len(all_spirals):.1f}%)")
    
    total_size = sum(f.stat().st_size for f in output_path.glob("*.txt")) / 1e6
    print(f"\nOutput size: {total_size:.1f} MB")

#===============================================================================
# MAIN
#===============================================================================

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Spiralize corpus with cluster awareness')
    parser.add_argument('--input', '-i', required=True, help='Input directory')
    parser.add_argument('--output', '-o', required=True, help='Output directory')
    parser.add_argument('--keywords', '-k', required=True, help='Keywords JSON file')
    parser.add_argument('--text-only', action='store_true', help='Only process text/md')
    parser.add_argument('--code-only', action='store_true', help='Only process Python')
    parser.add_argument('--sample', type=int, help='Process random sample')
    parser.add_argument('--workers', type=int, help='Parallel workers')
    
    args = parser.parse_args()
    
    process_corpus(
        args.input, args.output, args.keywords,
        text_only=args.text_only,
        code_only=args.code_only,
        sample_size=args.sample,
        workers=args.workers
    )
