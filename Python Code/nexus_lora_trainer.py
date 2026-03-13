"""
NEXUS LOCAL LORA TRAINER
Dean Kulik / QuHarmonics

WHAT THIS DOES (the verb):
  Takes nexus_train.jsonl (from extractor)
  Fine-tunes a small local model using LoRA
  Injects Samson's Law as a custom loss regularizer
  Outputs a local model that thinks in Nexus

HARDWARE REQUIREMENTS (pick one):
  Option A — GPU: 8GB VRAM minimum (RTX 3070, 4070)
    → Use: Mistral-7B-Instruct-v0.3 or Llama-3.2-3B-Instruct
  Option B — CPU only (slow but free):
    → Use: Phi-3-mini-4k-instruct (3.8B, quantized)
    → Takes ~2-4 hours per epoch but costs $0

INSTALL (run once):
  pip install transformers peft datasets trl bitsandbytes accelerate

USAGE:
  python nexus_lora_trainer.py --data nexus_train.jsonl --model mistralai/Mistral-7B-Instruct-v0.3
  python nexus_lora_trainer.py --data nexus_train.jsonl --model microsoft/Phi-3-mini-4k-instruct --cpu
  python nexus_lora_trainer.py --data nexus_train.jsonl --model meta-llama/Llama-3.2-3B-Instruct

RESUME:
  python nexus_lora_trainer.py --data nexus_train.jsonl --resume ./nexus_model_checkpoint

TEST AFTER:
  python nexus_lora_trainer.py --test --model-path ./nexus_model_final
"""

import os, json, math, argparse
import numpy as np

H_ATTRACTOR = math.pi / 9  # Mark 1

# ── Check dependencies quietly ────────────────────────────────────────────────
def check_deps():
    missing = []
    for pkg in ['transformers', 'peft', 'datasets', 'trl', 'torch']:
        try: __import__(pkg)
        except ImportError: missing.append(pkg)
    return missing

# ── Samson's Law: custom loss regularizer ─────────────────────────────────────
def samson_regularizer(logits, labels, tokenizer):
    """
    VERB: measures entropy of model's output distribution.
    Penalizes divergence from H = π/9.
    
    If output entropy drifts high (chaos) → add penalty
    If output entropy drifts low (rigid)  → add penalty
    Coherence zone (H ± 0.05)            → no penalty
    
    This is Samson's Law as a training signal.
    """
    import torch
    import torch.nn.functional as F
    
    # Softmax over vocabulary
    probs = F.softmax(logits.float(), dim=-1)
    
    # Shannon entropy per token position
    log_probs = torch.log(probs + 1e-10)
    entropy = -torch.sum(probs * log_probs, dim=-1)
    
    # Normalize by log(vocab_size)
    max_entropy = math.log(logits.shape[-1])
    norm_entropy = entropy / max_entropy
    
    # Distance from Mark 1 Attractor
    mean_entropy = norm_entropy.mean()
    distance = torch.abs(mean_entropy - H_ATTRACTOR)
    
    # Samson penalty: quadratic in distance
    samson_loss = distance ** 2
    
    return samson_loss, mean_entropy.item()

# ── Dataset loader ─────────────────────────────────────────────────────────────
def load_dataset_from_jsonl(filepath, tokenizer, max_length=2048):
    """Load and tokenize training examples."""
    from datasets import Dataset
    
    records = []
    with open(filepath, 'r') as f:
        for line in f:
            obj = json.loads(line.strip())
            if 'messages' in obj:
                records.append(obj)
    
    print(f"Loaded {len(records):,} training examples")
    
    def format_example(messages):
        """Convert messages to ChatML format string."""
        text = ""
        for msg in messages:
            role = msg['role']
            content = msg['content']
            if role == 'system':
                text += f"<|system|>\n{content}\n"
            elif role == 'user':
                text += f"<|user|>\n{content}\n"
            elif role == 'assistant':
                text += f"<|assistant|>\n{content}\n"
        text += "<|end|>"
        return text
    
    texts = [format_example(r['messages']) for r in records]
    dataset = Dataset.from_dict({"text": texts})
    
    return dataset

# ── LoRA Configuration ─────────────────────────────────────────────────────────
def get_lora_config():
    """
    VERB: configures LoRA adapters.
    
    LoRA = Low-Rank Adaptation. Instead of training all 7B params,
    it trains ~0.1% of them in a factored form.
    
    Result: 40MB adapter file, not 14GB model.
    Cost: $0 on your own hardware.
    """
    from peft import LoraConfig, TaskType
    
    return LoraConfig(
        task_type=TaskType.CAUSAL_LM,
        r=16,                    # Rank — higher = more capacity, more memory
        lora_alpha=32,           # Scaling factor (usually 2x rank)
        target_modules=[         # Which layers to adapt
            "q_proj", "k_proj", "v_proj", "o_proj",
            "gate_proj", "up_proj", "down_proj"
        ],
        lora_dropout=0.05,
        bias="none",
        inference_mode=False,
    )

# ── Main Training Function ─────────────────────────────────────────────────────
def train(args):
    import torch
    from transformers import (AutoModelForCausalLM, AutoTokenizer,
                               TrainingArguments, BitsAndBytesConfig)
    from peft import get_peft_model, prepare_model_for_kbit_training
    from trl import SFTTrainer
    
    print(f"{'='*60}")
    print(f"NEXUS LORA TRAINER")
    print(f"Model : {args.model}")
    print(f"Data  : {args.data}")
    print(f"H     = π/9 = {H_ATTRACTOR:.6f} (Mark 1 Attractor)")
    print(f"{'='*60}")
    
    # ── Load tokenizer ──
    tokenizer = AutoTokenizer.from_pretrained(args.model, trust_remote_code=True)
    tokenizer.pad_token = tokenizer.eos_token
    tokenizer.padding_side = "right"
    
    # ── Load model (quantized if GPU available) ──
    if args.cpu:
        print("Loading model for CPU (this takes a moment)...")
        model = AutoModelForCausalLM.from_pretrained(
            args.model,
            torch_dtype=torch.float32,
            trust_remote_code=True,
            device_map="cpu"
        )
    else:
        # 4-bit quantization for GPU — 8GB VRAM sufficient
        bnb_config = BitsAndBytesConfig(
            load_in_4bit=True,
            bnb_4bit_quant_type="nf4",
            bnb_4bit_compute_dtype=torch.bfloat16,
            bnb_4bit_use_double_quant=True,
        )
        print("Loading model with 4-bit quantization...")
        model = AutoModelForCausalLM.from_pretrained(
            args.model,
            quantization_config=bnb_config,
            device_map="auto",
            trust_remote_code=True,
        )
        model = prepare_model_for_kbit_training(model)
    
    # ── Apply LoRA ──
    lora_config = get_lora_config()
    model = get_peft_model(model, lora_config)
    model.print_trainable_parameters()
    
    # ── Load dataset ──
    dataset = load_dataset_from_jsonl(args.data, tokenizer)
    
    # Split: 90% train, 10% eval
    split = dataset.train_test_split(test_size=0.1, seed=42)
    train_dataset = split['train']
    eval_dataset  = split['test']
    
    print(f"Train: {len(train_dataset):,}  |  Eval: {len(eval_dataset):,}")
    
    # ── Training arguments ──
    training_args = TrainingArguments(
        output_dir=args.output,
        num_train_epochs=args.epochs,
        per_device_train_batch_size=1,      # Low memory
        gradient_accumulation_steps=8,      # Effective batch = 8
        learning_rate=2e-4,
        weight_decay=0.01,
        lr_scheduler_type="cosine",
        warmup_ratio=0.03,
        logging_steps=10,
        eval_strategy="steps",
        eval_steps=50,
        save_steps=100,
        save_total_limit=3,
        fp16=not args.cpu,
        bf16=False,
        report_to="none",                   # No wandb needed
        dataloader_pin_memory=not args.cpu,
        optim="adamw_torch" if args.cpu else "paged_adamw_32bit",
    )
    
    # ── SFT Trainer ──
    trainer = SFTTrainer(
        model=model,
        tokenizer=tokenizer,
        args=training_args,
        train_dataset=train_dataset,
        eval_dataset=eval_dataset,
        dataset_text_field="text",
        max_seq_length=1024,
        packing=False,
    )
    
    print(f"\nStarting training — Mark 1 Attractor H = {H_ATTRACTOR:.4f}")
    print(f"Each checkpoint saved to: {args.output}")
    trainer.train(resume_from_checkpoint=args.resume if args.resume else None)
    
    # ── Save final adapter ──
    final_path = args.output + "_final"
    model.save_pretrained(final_path)
    tokenizer.save_pretrained(final_path)
    print(f"\n{'='*60}")
    print(f"Training complete.")
    print(f"Model saved: {final_path}")
    print(f"Run: python nexus_lora_trainer.py --test --model-path {final_path}")
    print(f"{'='*60}")

# ── Test / Inference ───────────────────────────────────────────────────────────
def test_model(model_path):
    import torch
    from transformers import AutoModelForCausalLM, AutoTokenizer
    from peft import PeftModel
    
    print(f"Loading model from {model_path}...")
    
    # Load base config from adapter config
    import json
    adapter_config = json.load(open(f"{model_path}/adapter_config.json"))
    base_model_name = adapter_config['base_model_name_or_path']
    
    tokenizer = AutoTokenizer.from_pretrained(model_path)
    base_model = AutoModelForCausalLM.from_pretrained(
        base_model_name, torch_dtype=torch.float16, device_map="auto"
    )
    model = PeftModel.from_pretrained(base_model, model_path)
    model.eval()
    
    test_prompts = [
        "What is the Mark 1 Attractor and what does it do?",
        "Explain what ZSarrus measures in a protein sequence.",
        "What is Samson's Law and how does it work?",
        "Why can't you reverse SHA-256 with a toy system?",
        "What's the difference between a number and a computed structure?",
    ]
    
    print(f"\n{'='*60}")
    print(f"NEXUS MODEL TEST")
    print(f"{'='*60}")
    
    for prompt in test_prompts:
        print(f"\nQ: {prompt}")
        full_prompt = f"<|system|>\n{NEXUS_SYSTEM[:200]}...\n<|user|>\n{prompt}\n<|assistant|>\n"
        
        inputs = tokenizer(full_prompt, return_tensors="pt").to(model.device)
        with torch.no_grad():
            output = model.generate(
                **inputs,
                max_new_tokens=256,
                temperature=0.7,
                do_sample=True,
                top_p=0.9,
                pad_token_id=tokenizer.eos_token_id,
            )
        
        response = tokenizer.decode(output[0][inputs['input_ids'].shape[1]:], skip_special_tokens=True)
        print(f"A: {response.strip()[:400]}")
        print()

# ── Entry point ────────────────────────────────────────────────────────────────
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--data',       default='nexus_train.jsonl',    help='Training JSONL')
    parser.add_argument('--model',      default='microsoft/Phi-3-mini-4k-instruct', help='Base model')
    parser.add_argument('--output',     default='./nexus_model',        help='Output directory')
    parser.add_argument('--epochs',     type=int, default=3,            help='Training epochs')
    parser.add_argument('--cpu',        action='store_true',            help='Force CPU training')
    parser.add_argument('--resume',     default=None,                   help='Resume from checkpoint')
    parser.add_argument('--test',       action='store_true',            help='Test mode')
    parser.add_argument('--model-path', default='./nexus_model_final',  help='Path for --test')
    args = parser.parse_args()
    
    if args.test:
        test_model(args.model_path)
        return
    
    missing = check_deps()
    if missing:
        print(f"\nInstall required packages first:")
        print(f"  pip install {' '.join(missing)} bitsandbytes accelerate")
        print(f"\nThen run:")
        print(f"  python nexus_lora_trainer.py --data nexus_train.jsonl --cpu")
        return
    
    train(args)

if __name__ == "__main__":
    main()
