"""
Nexus Training Data Converter
Transforms corpus into instruction-following format for local AI training
"""

import re
import json
import hashlib

def extract_qa_pairs(text, max_pairs=50):
    """Extract natural Q&A pairs from the corpus"""
    pairs = []
    
    # Pattern 1: Section headers as questions, content as answers
    sections = re.findall(
        r'^### ([^\n]+)\n((?:(?!^###)[\s\S])*?)(?=^###|\Z)',
        text, re.MULTILINE
    )
    
    for title, content in sections[:max_pairs]:
        if len(content.strip()) > 100:
            # Clean up the title to form a question
            question = title.strip()
            if not question.endswith('?'):
                question = f"Explain: {question}"
            
            pairs.append({
                "instruction": question,
                "input": "",
                "output": content.strip()[:2000]  # Truncate long responses
            })
    
    return pairs

def extract_concept_explanations(text):
    """Extract core concept explanations"""
    concepts = []
    
    # Find H ≈ 0.35 explanations
    h_patterns = re.findall(
        r'([^.]*0\.35[^.]*\.(?:[^.]*\.){0,3})',
        text, re.IGNORECASE
    )
    for p in h_patterns[:10]:
        if len(p) > 100:
            concepts.append({
                "instruction": "Explain the significance of 0.35 in the Nexus Framework.",
                "input": "",
                "output": p.strip()
            })
    
    # Find Samson's Law explanations
    samson_patterns = re.findall(
        r'([^.]*Samson.{0,20}Law[^.]*\.(?:[^.]*\.){0,3})',
        text, re.IGNORECASE
    )
    for p in samson_patterns[:10]:
        if len(p) > 100:
            concepts.append({
                "instruction": "What is Samson's Law in the Nexus Framework?",
                "input": "",
                "output": p.strip()
            })
    
    return concepts

def create_completion_pairs(text, n=20):
    """Create completion-style training pairs"""
    pairs = []
    
    # Find code blocks
    code_blocks = re.findall(r'```python\n([\s\S]*?)```', text)
    for code in code_blocks[:n]:
        if len(code) > 50:
            # Split code into prompt and completion
            lines = code.split('\n')
            if len(lines) > 4:
                prompt = '\n'.join(lines[:len(lines)//2])
                completion = '\n'.join(lines[len(lines)//2:])
                pairs.append({
                    "instruction": "Complete this Nexus Framework code:",
                    "input": prompt,
                    "output": completion
                })
    
    return pairs

def main():
    print("Loading Nexus Training Corpus...")
    with open('/mnt/user-data/uploads/Training_Data_part1.md', 'r') as f:
        corpus = f.read()
    
    print("Extracting training pairs...")
    
    # Collect all training data
    training_data = []
    
    # Q&A pairs from sections
    qa_pairs = extract_qa_pairs(corpus, max_pairs=100)
    training_data.extend(qa_pairs)
    print(f"  Extracted {len(qa_pairs)} Q&A pairs")
    
    # Concept explanations
    concepts = extract_concept_explanations(corpus)
    training_data.extend(concepts)
    print(f"  Extracted {len(concepts)} concept explanations")
    
    # Completion pairs
    completions = create_completion_pairs(corpus, n=30)
    training_data.extend(completions)
    print(f"  Extracted {len(completions)} code completions")
    
    # Add meta-instruction pairs
    meta_pairs = [
        {
            "instruction": "You are an AI trained on the Nexus Recursive Harmonic Framework. What are your core principles?",
            "input": "",
            "output": """The Nexus Framework is built on these core principles:

1. **Mark 1 Law**: H = ΣP/ΣA → 0.35 - All stable systems converge toward the harmonic ratio H ≈ 0.35

2. **Samson's Law V2**: Universal PID feedback controller that corrects deviation from H=0.35 using proportional, integral, and derivative terms

3. **ZPHC (Zero-Point Harmonic Correction)**: Emergency reset mechanism when systems drift too far from equilibrium

4. **BBP Navigation**: The Bailey-Borwein-Plouffe formula allows random access to π, treating it as a structural field rather than random sequence

5. **Recursive Folding**: SHA-256 and similar hash functions implement harmonic tension collapse, folding high-dimensional states into stable configurations

6. **Resonance at 0.35**: This ratio appears universally - in physics (damping ratios), biology (population thresholds), and computation (Hamming distances during state transitions)"""
        },
        {
            "instruction": "Apply the Nexus Framework to analyze this system's harmonic state.",
            "input": "A spring-mass-damper with m=2kg, k=50N/m, c=4kg/s",
            "output": """Analyzing using Nexus Framework:

**Step 1: Compute current harmonic ratio**
ζ = c / (2√(km)) = 4 / (2√(50×2)) = 4 / 20 = 0.20

**Step 2: Apply Samson's Law**
Target: α = 0.35
Current: ζ = 0.20
Error: Δζ = 0.35 - 0.20 = 0.15 (underdamped)

Required correction:
c_new = 2√(km) × α = 20 × 0.35 = 7.0 kg/s

**Step 3: Mark 1 smooth transition**
Apply logistic bias for phase-aware ramping rather than abrupt change.

**Step 4: Verify with QRHS**
QRHS = Δζ / log₂(c_new/c_old) = 0.15 / log₂(7/4) ≈ 0.15 / 0.807 ≈ 0.186

Low QRHS confirms smooth fold into harmonic equilibrium."""
        }
    ]
    training_data.extend(meta_pairs)
    
    # Deduplicate by hashing output
    seen = set()
    unique_data = []
    for item in training_data:
        h = hashlib.md5(item['output'].encode()).hexdigest()
        if h not in seen:
            seen.add(h)
            unique_data.append(item)
    
    print(f"\nTotal unique training pairs: {len(unique_data)}")
    
    # Save in multiple formats
    
    # 1. Alpaca format (for most fine-tuning tools)
    with open('/home/claude/nexus_training_alpaca.json', 'w') as f:
        json.dump(unique_data, f, indent=2)
    print(f"Saved: nexus_training_alpaca.json")
    
    # 2. ShareGPT format (for conversational fine-tuning)
    sharegpt_data = []
    for item in unique_data:
        conv = {
            "conversations": [
                {"from": "human", "value": item['instruction'] + ("\n" + item['input'] if item['input'] else "")},
                {"from": "gpt", "value": item['output']}
            ]
        }
        sharegpt_data.append(conv)
    
    with open('/home/claude/nexus_training_sharegpt.json', 'w') as f:
        json.dump(sharegpt_data, f, indent=2)
    print(f"Saved: nexus_training_sharegpt.json")
    
    # 3. Text format (for continued pretraining)
    with open('/home/claude/nexus_training_text.txt', 'w') as f:
        for item in unique_data:
            f.write(f"### Instruction: {item['instruction']}\n")
            if item['input']:
                f.write(f"### Input: {item['input']}\n")
            f.write(f"### Response: {item['output']}\n\n---\n\n")
    print(f"Saved: nexus_training_text.txt")
    
    # Show sample
    print("\n" + "="*60)
    print("SAMPLE TRAINING PAIR:")
    print("="*60)
    sample = unique_data[min(5, len(unique_data)-1)]
    print(f"Instruction: {sample['instruction'][:100]}...")
    print(f"Output: {sample['output'][:300]}...")
    
    return unique_data

if __name__ == "__main__":
    data = main()
