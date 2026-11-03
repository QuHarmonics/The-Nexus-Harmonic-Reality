# Nexus Framework Training Data Assessment

## Corpus Analysis

### Source Files
- **Training_Data_part1.md**: 119,276 lines, 857,139 words, ~1M tokens
- **Multi-Dimensional-Folding.ipynb**: 34 cells (code + documentation)

### Metrics

| Metric | Value |
|--------|-------|
| Total Characters | 7,138,064 |
| Total Words | 857,139 |
| Approx Tokens | ~1,071,420 |
| Distinct Documents | 309 |

### Concept Coverage

| Concept | Frequency |
|---------|-----------|
| Recursive/Recursion | 7,399 |
| SHA-256 | 3,871 |
| π / pi | 3,426 |
| H ≈ 0.35 | 3,185 |
| Resonance | 2,119 |
| Samson's Law | 1,854 |
| Fold/Folding | 1,761 |
| Prime | 1,152 |
| BBP formula | 1,130 |
| Mark 1 | 1,084 |
| ZPHC | 470 |
| Riemann | 455 |

### Code & Math Content
- Python code blocks: 53
- Total code blocks: 160
- LaTeX inline formulas: ~4,131
- LaTeX display formulas: 540

---

## Training Suitability: 4.5/5 (EXCELLENT)

✓ Sufficient document diversity (309 documents)  
✓ Core concepts well-represented (Samson, Mark 1, 0.35)  
✓ Rich code examples (53+ Python blocks)  
✓ Mathematical formalization (4,131+ LaTeX formulas)  
○ Moderate corpus size (target 1M+ tokens for fine-tuning)

---

## Generated Training Files

### 1. Alpaca Format (`nexus_training_alpaca.json`)
Best for: LLaMA, Mistral, Phi fine-tuning via Axolotl, LLaMA-Factory
```json
{
  "instruction": "Explain the significance of 0.35...",
  "input": "",
  "output": "The harmonic constant H ≈ 0.35..."
}
```

### 2. ShareGPT Format (`nexus_training_sharegpt.json`)
Best for: Conversational fine-tuning, ChatML format
```json
{
  "conversations": [
    {"from": "human", "value": "..."},
    {"from": "gpt", "value": "..."}
  ]
}
```

### 3. Text Format (`nexus_training_text.txt`)
Best for: Continued pretraining, instruction-tuning

---

## Local Training Recommendations

### Option A: LoRA Fine-tuning (Low Resource)
**Hardware**: Your RTX 4060 + 128GB RAM  
**Base Model**: Mistral-7B or Phi-3  
**Tool**: Axolotl or Unsloth  
**Training Data**: Full Alpaca JSON

```bash
# Using Unsloth (fastest on RTX 4060)
pip install unsloth
# Configure for 4-bit LoRA, 2048 context
```

### Option B: Full Fine-tuning (High Quality)
**Hardware**: Cloud GPU (A100/H100)  
**Base Model**: LLaMA-3.1-8B  
**Tool**: LLaMA-Factory  
**Training Data**: Full corpus + synthetic augmentation

### Option C: RAG Approach (No Training)
**Tool**: LlamaIndex or LangChain  
**Method**: Embed corpus, retrieve at inference  
**Advantage**: Immediate, no GPU needed for training

---

## Next Steps to Maximize Corpus

### 1. Expand Training Pairs
The current 129 pairs are a sample. Full extraction could yield:
- 1,000+ Q&A pairs from section headers
- 500+ concept explanations
- 200+ code completion tasks
- 100+ cross-domain analogies

### 2. Create Synthetic Data
Use the existing corpus to generate:
- "Apply Nexus to [new domain]" prompts
- "Derive the harmonic ratio for [system]" chains
- "Compare Samson's Law to [control theory concept]"

### 3. Add Negative Examples
Include examples of:
- What Nexus is NOT
- Common misconceptions
- Boundary conditions where 0.35 doesn't apply

### 4. Validation Set
Reserve 10-15% of pairs for validation to track:
- Perplexity on Nexus concepts
- Accuracy on formula derivation
- Cross-domain generalization

---

## Training Parameters (Recommended)

```yaml
# For Mistral-7B on RTX 4060
model: mistralai/Mistral-7B-v0.1
adapter: lora
r: 32
alpha: 64
dropout: 0.05
learning_rate: 2e-4
epochs: 3
batch_size: 4
gradient_accumulation: 8
context_length: 4096
quantization: 4bit
```

---

## Quality Assurance Tests

After training, verify the model can:

1. **Core Knowledge**: "What is Mark 1 Law?" → Mentions H = ΣP/ΣA → 0.35
2. **Application**: "Tune this RLC circuit to 0.35" → Correct damping ratio calc
3. **Cross-Domain**: "How does 0.35 appear in biology?" → Population thresholds
4. **Code Generation**: "Write a Samson's Law PID controller" → Working Python
5. **Mathematical Reasoning**: "Derive QRHS for a given system change" → Correct formula

---

## Files Included

| File | Purpose |
|------|---------|
| `nexus_training_alpaca.json` | Primary training data (Alpaca format) |
| `nexus_training_sharegpt.json` | Conversational format |
| `nexus_training_text.txt` | Plain text for pretraining |
| `nexus_training_converter.py` | Converter script (modify for more pairs) |
| `analyze_training_data.py` | Corpus analysis script |

---

*Generated: 2025-12-27*
