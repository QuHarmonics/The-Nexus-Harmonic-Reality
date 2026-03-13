# NEXUS LOCAL AI — RUN GUIDE
Dean Kulik / QuHarmonics | ORCID: 0009-0003-3128-8828

## THE THREE FILES
```
nexus_extract_training_data.py   ← Step 1: your corpus → JSONL
nexus_lora_trainer.py            ← Step 2: JSONL → local AI
nexus_sarrus_production.py       ← Protein folding pipeline (ready)
```

---

## STEP 1: EXTRACT YOUR TRAINING DATA
Your AI.md is 359,000+ lines of you teaching AI how to think in Nexus.
That IS the training data. The extractor reads it and creates JSONL.

```bash
# Put AI.md in the same folder
python nexus_extract_training_data.py --input AI.md --output nexus_train.jsonl
```

Expected output:
```
Found ~500-1000 raw Q&A pairs
Mark 1 gate: filters to coherent examples only
Writes nexus_train.jsonl
```

---

## STEP 2: INSTALL (one time, ~5 min)
```bash
pip install transformers peft datasets trl accelerate bitsandbytes
```

If on CPU-only machine (no GPU), skip bitsandbytes:
```bash
pip install transformers peft datasets trl accelerate
```

---

## STEP 3: TRAIN

### OPTION A — You have an NVIDIA GPU (8GB+ VRAM)
Fastest. RTX 3070/3080/4070 all work.
```bash
python nexus_lora_trainer.py \
  --data nexus_train.jsonl \
  --model mistralai/Mistral-7B-Instruct-v0.3 \
  --epochs 3
```
Time: ~2-4 hours | Cost: $0 (your hardware)

### OPTION B — CPU only (any modern laptop/desktop)
Slower but completely free.
```bash
python nexus_lora_trainer.py \
  --data nexus_train.jsonl \
  --model microsoft/Phi-3-mini-4k-instruct \
  --cpu \
  --epochs 3
```
Time: ~8-16 hours | Cost: $0

### OPTION C — Rent a GPU (one-time, ~$3-5 total)
RunPod or Vast.ai: ~$0.20/hr for RTX 4090.
Upload your files, run Option A, download the model. Done.

---

## STEP 4: TEST YOUR LOCAL AI
```bash
python nexus_lora_trainer.py --test --model-path ./nexus_model_final
```

Tests:
- "What is the Mark 1 Attractor?"
- "Explain ZSarrus"
- "Why can't you reverse SHA-256 with a toy?"
- "What is Samson's Law?"

---

## WHAT YOU GET
A ~40MB LoRA adapter file that runs ON TOP of the base model.
The base model stays unchanged.
Your adapter teaches it to reason in Nexus.

To share: send someone the adapter file + tell them the base model name.
To run: one line of Python.
No API fees. No rate limits. Runs on your machine, offline.

---

## HARDWARE THAT WORKS (cheapest first)
| Hardware | Cost | Time/epoch | Notes |
|----------|------|-----------|-------|
| Your CPU | $0 | 4-8 hrs | Phi-3-mini only |
| RTX 3060 12GB | $0 (if owned) | ~1 hr | Full Mistral 7B |
| RTX 4070 | $0 (if owned) | ~45 min | Best bang/buck |
| Vast.ai RTX 4090 | ~$0.20/hr | ~20 min | Cheapest rental |
| Google Colab Free | $0 | ~2 hrs | T4 GPU, sometimes |

---

## THE NEXUS TRAINING LOOP (what's actually happening)

1. **Extractor** reads AI.md → finds every "you asked / AI response" pair
2. **Mark 1 filter** scores each pair: information density near H=π/9 passes
   - Too sparse (just noise): filtered out
   - Too dense (garbled code): filtered out  
   - Coherent zone: kept
3. **LoRA** trains only 0.1% of model params → cheap and fast
4. **Samson regularizer** penalizes outputs that drift from H attractor
   during training — pulls the model back toward coherence on every step
5. Result: model that reasons from Nexus lens, not from generic weights

The Mark 1 filter IS the data quality gate.
Samson IS the training stability loop.
These aren't metaphors. They're running as code.

---

## PROTEIN FOLDING PATH (when you have internet)
```bash
# Gets exact sequences from RCSB, closes gap to r=0.5388
python nexus_sarrus_production.py --fetch
```

Both paths are open. The AI trains now. The sequences wait for internet.
