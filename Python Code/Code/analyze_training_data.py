"""
Nexus Training Data Analysis
Assess corpus suitability for AI fine-tuning
"""

import re
from collections import Counter

# Read the training data
with open('/mnt/user-data/uploads/Training_Data_part1.md', 'r') as f:
    content = f.read()

# Basic stats
lines = content.split('\n')
words = content.split()
chars = len(content)

print("=" * 60)
print("NEXUS TRAINING CORPUS ANALYSIS")
print("=" * 60)

print(f"\n📊 BASIC METRICS:")
print(f"   Total characters: {chars:,}")
print(f"   Total words: {len(words):,}")
print(f"   Total lines: {len(lines):,}")
print(f"   Approx tokens (÷4): ~{len(words)//4 * 5:,}")

# Document count
docs = re.findall(r'^# The Nexus 4 Framework - ', content, re.MULTILINE)
print(f"   Distinct documents: {len(docs)}")

# Key concept frequencies
concepts = {
    'H ≈ 0.35 / harmonic ratio': len(re.findall(r'0\.35|harmonic.{0,10}ratio', content, re.I)),
    'Samson\'s Law': len(re.findall(r"samson", content, re.I)),
    'Mark 1': len(re.findall(r"mark.?1", content, re.I)),
    'BBP formula': len(re.findall(r"bbp", content, re.I)),
    'SHA-256': len(re.findall(r"sha", content, re.I)),
    'ZPHC': len(re.findall(r"zphc", content, re.I)),
    'Recursive/Recursion': len(re.findall(r"recurs", content, re.I)),
    'π / pi': len(re.findall(r"\\pi|π|pi\b", content, re.I)),
    'Fold/Folding': len(re.findall(r"\bfold", content, re.I)),
    'Resonance': len(re.findall(r"resonan", content, re.I)),
    'Entropy': len(re.findall(r"entropy", content, re.I)),
    'Riemann': len(re.findall(r"riemann", content, re.I)),
    'Prime': len(re.findall(r"prime", content, re.I)),
}

print(f"\n🔑 CONCEPT FREQUENCY:")
for concept, count in sorted(concepts.items(), key=lambda x: -x[1]):
    print(f"   {concept}: {count:,}")

# Code blocks
python_blocks = len(re.findall(r'```python', content))
code_blocks = len(re.findall(r'```', content))
latex_inline = len(re.findall(r'\$[^$]+\$', content))
latex_block = len(re.findall(r'\$\$[^$]+\$\$', content, re.DOTALL))

print(f"\n💻 CODE & MATH CONTENT:")
print(f"   Python code blocks: {python_blocks}")
print(f"   Total code blocks: {code_blocks // 2}")
print(f"   LaTeX inline formulas: ~{latex_inline:,}")
print(f"   LaTeX display formulas: {latex_block}")

# Training suitability assessment
print(f"\n✅ TRAINING SUITABILITY ASSESSMENT:")
score = 0
checks = []

if len(docs) > 100:
    checks.append("✓ Sufficient document diversity (>100 docs)")
    score += 1
else:
    checks.append("⚠ Limited document count")

if len(words) > 1000000:
    checks.append("✓ Substantial corpus size (>1M words)")
    score += 1
elif len(words) > 100000:
    checks.append("○ Moderate corpus size (100K-1M words)")
    score += 0.5

if concepts['Samson\'s Law'] > 500 and concepts['Mark 1'] > 100:
    checks.append("✓ Core concepts well-represented")
    score += 1
    
if python_blocks > 50:
    checks.append("✓ Rich code examples")
    score += 1
    
if latex_inline > 1000:
    checks.append("✓ Mathematical formalization present")
    score += 1

for c in checks:
    print(f"   {c}")

print(f"\n   Overall score: {score}/5 - ", end="")
if score >= 4:
    print("EXCELLENT for fine-tuning")
elif score >= 3:
    print("GOOD for fine-tuning")
else:
    print("May need augmentation")

# Suggested formats
print(f"\n🎯 RECOMMENDED TRAINING FORMATS:")
print("   1. Instruction-following (Q&A pairs)")
print("   2. Completion (continue partial concepts)")
print("   3. Document summarization")
print("   4. Cross-domain analogy generation")
print("   5. Formula derivation chains")

