# LoRA v3 Training Specification
**Phase 1163+ | QuHarmonics Research Group**

## Training Targets

### slot_builder_lora_v3
**Purpose:** Generate scar-free, fragment-free, polarity-correct contracts

**Source data:** `rhi_repair_training_rows_v8.jsonl` (19 rows)

**Training format:**
```json
{
  "messages": [
    {
      "role": "system",
      "content": "You are the Nexus Slot Constructor. Generate missing-shape contracts. Required fields: family_class, domain_carrier, forbidden_neighbor_carrier, boundary_conditions, preserved_function, failure_modes, witness_readout, residue. family_class must be a complete noun phrase. Use operational fit, not labels."
    },
    {
      "role": "user",
      "content": "Prompt: {prompt}\n\nGenerate the missing-shape contract.\nChecklist:\n1. Need: occupy the inverse cavity.\n2. Function: preserve or redirect the required operation.\n3. Boundary: respect constraints.\n4. Trap: reject noun/surface-label confusion.\n5. Collapse: produce one executable witness/readout.\nfamily_class must be a complete noun phrase (not a dangling preposition).\nReturn JSON only."
    },
    {
      "role": "assistant",
      "content": "{good_contract_json}"
    }
  ]
}
```

**Example training row transformation:**

Input repair row:
```json
{
  "run_id": "rhi_v8_...",
  "prompt": "Using the Nexus lens, explain why current AI agents fail...",
  "field": "domain_carrier",
  "repair_type": "generic_removal",
  "bad_value": "current",
  "good_value": ["AI", "agents", "fail", "tools", ...],
  "instruction": "Do not use generic term 'current' as a domain_carrier."
}
```

Becomes training example:
```json
{
  "messages": [
    {"role": "system", "content": "..."},
    {"role": "user", "content": "Prompt: Using the Nexus lens, explain why current AI agents fail...\n\n..."},
    {"role": "assistant", "content": "{\"family_class\": \"operational closure of nexus slot construction\", \"domain_carrier\": [\"AI\", \"agents\", \"fail\", \"tools\", \"forming\", \"contract\", \"intent\", \"boundary\", \"tool\", \"agent\", \"sequence\", \"tool use after contract\"], ...}"}
  ]
}
```

**Hyperparameters:**
```python
base_model = "Qwen/Qwen2.5-1.5B-Instruct"
lora_rank = 16
lora_alpha = 32
lora_dropout = 0.05
target_modules = ["q_proj", "v_proj"]
task_type = "CAUSAL_LM"

training_args = TrainingArguments(
    output_dir="./slot_builder_lora_v3",
    num_train_epochs=5,
    per_device_train_batch_size=1,
    gradient_accumulation_steps=4,
    learning_rate=3e-4,
    fp16=True,
    logging_steps=1,
    save_strategy="epoch",
    optim="adamw_torch",
    warmup_ratio=0.1,
)
```

**Expected improvements:**
- Generic removal: 100% (no "current", "using", "properly" in domain_carrier)
- Scar removal: 100% (no "general purpose", "surface label" in forbidden)
- Polarity: 90% (boundary_conditions correctly gate, not describe)
- Fragment: 95% (family_class complete noun phrases)

---

### shape_critic_v1
**Purpose:** Predict dominant operation-shape from contract + prompt

**Source data:** `rhi_shape_training_rows_v8.jsonl` (4 rows)

**Training format:**
```json
{
  "messages": [
    {
      "role": "system",
      "content": "You are the Nexus Shape Critic. Given a contract and prompt, predict the dominant operation-shape and detect composites. Output JSON with: dominant_shape, dominant_mass, composite (if detected), shape_field_mass."
    },
    {
      "role": "user",
      "content": "Contract:\n{contract_json}\n\nPrompt: {prompt}\n\nPredict the dominant operation-shape."
    },
    {
      "role": "assistant",
      "content": "{shape_prediction_json}"
    }
  ]
}
```

**Example training row transformation:**

Input shape row:
```json
{
  "run_id": "rhi_v8_1ce09e09be",
  "prompt": "Is the contract boundary condition a filter or a gate?",
  "branch": "skeptical",
  "shape_field_mass": {
    "FILTER": 0.276,
    "GATE": 0.253,
    "BOUNDARY": 0.189
  },
  "composite": {
    "composite": "BOUNDARY",
    "constituents": ["FILTER", "GATE"],
    "ratio": 0.918,
    "relation": "FILTER ⊕ GATE → BOUNDARY"
  },
  "dominant_shape": "BOUNDARY",
  "dominant_mass": 0.276
}
```

Becomes training example (aggregated across all branches from same run):
```json
{
  "messages": [
    {"role": "system", "content": "..."},
    {"role": "user", "content": "Contract:\n{...}\n\nPrompt: Is the contract boundary condition a filter or a gate?\n\nPredict the dominant operation-shape."},
    {"role": "assistant", "content": "{\"dominant_shape\": \"BOUNDARY\", \"dominant_mass\": 0.276, \"composite\": {\"composite\": \"BOUNDARY\", \"constituents\": [\"FILTER\", \"GATE\"], \"ratio\": 0.918}, \"shape_field_mass\": {\"FILTER\": 0.276, \"GATE\": 0.253, \"BOUNDARY\": 0.189}}"}
  ]
}
```

**Hyperparameters:**
```python
base_model = "Qwen/Qwen2.5-1.5B-Instruct"
lora_rank = 8
lora_alpha = 16
lora_dropout = 0.05
target_modules = ["q_proj", "k_proj", "v_proj"]
task_type = "CAUSAL_LM"

training_args = TrainingArguments(
    output_dir="./shape_critic_v1",
    num_train_epochs=8,  # Small dataset, more epochs
    per_device_train_batch_size=1,
    gradient_accumulation_steps=4,
    learning_rate=5e-4,  # Higher LR for small dataset
    fp16=True,
    logging_steps=1,
    save_strategy="epoch",
    optim="adamw_torch",
    warmup_ratio=0.2,  # More warmup for stability
)
```

**Expected accuracy:**
- Dominant shape prediction: 85% on held-out binary stance prompts
- Composite detection: 90% recall (catches FILTER⊕GATE→BOUNDARY)
- Mass distribution error: <0.10 MAE vs ground truth

---

## Training Data Construction

### Repair Rows → Training Examples

```python
def build_slot_training_examples(repair_rows: List[Dict]) -> List[Dict]:
    """
    Convert repair rows to training examples for slot_builder_lora_v3.
    
    Strategy:
    1. Group repair rows by run_id
    2. For each run, reconstruct the "good" contract from all repairs
    3. Create one training example: prompt → good_contract
    """
    examples = []
    
    # Group by run_id
    by_run = {}
    for row in repair_rows:
        run_id = row['run_id']
        if run_id not in by_run:
            by_run[run_id] = []
        by_run[run_id].append(row)
    
    # For each run, reconstruct good contract
    for run_id, repairs in by_run.items():
        # Start with a base contract structure
        good_contract = {
            "family_class": "",
            "domain_carrier": [],
            "forbidden_neighbor_carrier": [],
            "boundary_conditions": [],
            "preserved_function": "",
            "failure_modes": [],
            "witness_readout": "",
            "residue": None
        }
        
        # Apply all repairs
        for repair in repairs:
            field = repair['field']
            repair_type = repair['repair_type']
            good_value = repair['good_value']
            
            if repair_type in ['positive_injection', 'forbidden_injection']:
                # Add missing term
                if isinstance(good_value, list):
                    good_contract[field].extend(good_value)
                else:
                    good_contract[field].append(good_value)
            
            elif repair_type in ['generic_removal', 'scar_removal']:
                # Replace with good value
                good_contract[field] = good_value
            
            elif repair_type == 'polarity_rewrite':
                # Replace boundary_conditions
                good_contract[field] = good_value
            
            elif repair_type == 'family_class_repair':
                # Replace family_class
                good_contract['family_class'] = good_value
        
        # Deduplicate lists
        for field in ['domain_carrier', 'forbidden_neighbor_carrier', 'boundary_conditions', 'failure_modes']:
            if isinstance(good_contract[field], list):
                good_contract[field] = list(dict.fromkeys(good_contract[field]))
        
        # Create training example
        prompt = repairs[0]['prompt']  # All repairs from same run have same prompt
        
        examples.append({
            "messages": [
                {
                    "role": "system",
                    "content": SLOT_SYSTEM_PROMPT
                },
                {
                    "role": "user",
                    "content": build_slot_user_prompt(prompt)
                },
                {
                    "role": "assistant",
                    "content": json.dumps(good_contract, ensure_ascii=False)
                }
            ]
        })
    
    return examples
```

### Shape Rows → Training Examples

```python
def build_shape_training_examples(shape_rows: List[Dict]) -> List[Dict]:
    """
    Convert shape rows to training examples for shape_critic_v1.
    
    Strategy:
    1. Group shape rows by run_id (each run has 4 rows, one per branch)
    2. All branches share the same shape_field_mass and composite
    3. Create one training example: contract + prompt → shape prediction
    """
    examples = []
    
    # Group by run_id
    by_run = {}
    for row in shape_rows:
        run_id = row['run_id']
        if run_id not in by_run:
            by_run[run_id] = []
        by_run[run_id].append(row)
    
    # For each run, create one training example
    for run_id, rows in by_run.items():
        # All rows from same run have same contract, prompt, shape_field_mass, composite
        first_row = rows[0]
        
        contract = first_row.get('contract', {})  # Need to add this to shape rows
        prompt = first_row['prompt']
        shape_field_mass = first_row['shape_field_mass']
        composite = first_row.get('composite')
        dominant_shape = first_row['dominant_shape']
        dominant_mass = first_row['dominant_mass']
        
        # Shape prediction target
        shape_prediction = {
            "dominant_shape": dominant_shape,
            "dominant_mass": dominant_mass,
            "shape_field_mass": shape_field_mass,
        }
        
        if composite:
            shape_prediction["composite"] = composite
        
        examples.append({
            "messages": [
                {
                    "role": "system",
                    "content": SHAPE_CRITIC_SYSTEM_PROMPT
                },
                {
                    "role": "user",
                    "content": f"Contract:\n{json.dumps(contract, ensure_ascii=False, indent=2)}\n\nPrompt: {prompt}\n\nPredict the dominant operation-shape."
                },
                {
                    "role": "assistant",
                    "content": json.dumps(shape_prediction, ensure_ascii=False)
                }
            ]
        })
    
    return examples
```

---

## Training Script Template

```python
from transformers import AutoModelForCausalLM, AutoTokenizer, TrainingArguments, Trainer
from peft import LoraConfig, get_peft_model, prepare_model_for_kbit_training
from datasets import Dataset
import json

# Load base model
model_name = "Qwen/Qwen2.5-1.5B-Instruct"
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype=torch.float16,
    device_map="auto"
)
tokenizer = AutoTokenizer.from_pretrained(model_name)
if tokenizer.pad_token is None:
    tokenizer.pad_token = tokenizer.eos_token

# LoRA config for slot_builder_lora_v3
lora_config = LoraConfig(
    r=16,
    lora_alpha=32,
    target_modules=["q_proj", "v_proj"],
    lora_dropout=0.05,
    bias="none",
    task_type="CAUSAL_LM"
)

model = get_peft_model(model, lora_config)
model.print_trainable_parameters()

# Load training data
repair_rows = [json.loads(line) for line in open('rhi_repair_training_rows_v8.jsonl')]
training_examples = build_slot_training_examples(repair_rows)

# Convert to dataset
def format_example(example):
    text = tokenizer.apply_chat_template(example["messages"], tokenize=False)
    return {"text": text}

dataset = Dataset.from_list(training_examples).map(format_example)

# Tokenize
def tokenize_function(examples):
    return tokenizer(examples["text"], padding="max_length", truncation=True, max_length=2048)

tokenized_dataset = dataset.map(tokenize_function, batched=True)

# Training arguments
training_args = TrainingArguments(
    output_dir="./slot_builder_lora_v3",
    num_train_epochs=5,
    per_device_train_batch_size=1,
    gradient_accumulation_steps=4,
    learning_rate=3e-4,
    fp16=True,
    logging_steps=1,
    save_strategy="epoch",
    optim="adamw_torch",
    warmup_ratio=0.1,
)

# Trainer
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_dataset,
)

# Train
trainer.train()

# Save
model.save_pretrained("./slot_builder_lora_v3")
tokenizer.save_pretrained("./slot_builder_lora_v3")
```

---

## Validation Strategy

### slot_builder_lora_v3 Validation

**Held-out prompts (10 total):**
1. "Why do current language models hallucinate when they lack grounding?"
2. "Explain why tool-use agents fail without intent stabilization."
3. "What operational gap does contract-before-retrieval fix in RAG?"
4. "How does boundary verification prevent semantic drift?"
5. "Why does zero-shot prompting fail on tasks requiring operational closure?"
6. ... (5 more)

**Metrics:**
```python
def validate_slot_builder(adapter_path: str, prompts: List[str]) -> Dict:
    model = load_model_with_adapter(adapter_path)
    
    results = {
        "generic_term_rate": 0.0,
        "scar_term_rate": 0.0,
        "fragment_rate": 0.0,
        "polarity_error_rate": 0.0,
    }
    
    for prompt in prompts:
        contract = generate_contract(model, prompt)
        
        # Check for generics
        generic_count = sum(1 for term in contract['domain_carrier'] if term in GENERIC_DOMAIN_TERMS)
        results['generic_term_rate'] += generic_count / len(contract['domain_carrier'])
        
        # Check for scars
        scar_count = sum(1 for term in contract['forbidden_neighbor_carrier'] if term in SCAR_TERMS)
        results['scar_term_rate'] += scar_count / len(contract['forbidden_neighbor_carrier'])
        
        # Check for fragments
        if _is_family_class_fragment(contract['family_class']):
            results['fragment_rate'] += 1.0
        
        # Check polarity (manual inspection needed)
        # ...
    
    # Average across prompts
    n = len(prompts)
    return {k: v/n for k, v in results.items()}
```

**Target metrics:**
- Generic term rate: <5%
- Scar term rate: <5%
- Fragment rate: <10%
- Polarity error rate: <15%

### shape_critic_v1 Validation

**Held-out prompts (10 binary stance prompts):**
1. "Is boundary verification a lock or a gate?"
2. "Is semantic grounding a filter or a contract?"
3. "Does tool-use gating act as a lock or a boundary?"
4. ... (7 more)

**Metrics:**
```python
def validate_shape_critic(adapter_path: str, prompts: List[str], ground_truth: List[Dict]) -> Dict:
    model = load_model_with_adapter(adapter_path)
    
    correct_shape = 0
    composite_recall = 0
    composite_precision = 0
    mass_mae = 0.0
    
    for prompt, truth in zip(prompts, ground_truth):
        contract = generate_contract(slot_builder_v3, prompt)
        prediction = predict_shape(model, contract, prompt)
        
        # Dominant shape accuracy
        if prediction['dominant_shape'] == truth['dominant_shape']:
            correct_shape += 1
        
        # Composite detection
        if truth.get('composite'):
            if prediction.get('composite'):
                composite_recall += 1
        if prediction.get('composite'):
            if truth.get('composite'):
                composite_precision += 1
        
        # Mass MAE
        for shape, true_mass in truth['shape_field_mass'].items():
            pred_mass = prediction['shape_field_mass'].get(shape, 0.0)
            mass_mae += abs(pred_mass - true_mass)
    
    n = len(prompts)
    return {
        "shape_accuracy": correct_shape / n,
        "composite_recall": composite_recall / sum(1 for t in ground_truth if t.get('composite')),
        "composite_precision": composite_precision / sum(1 for p in predictions if p.get('composite')),
        "mass_mae": mass_mae / (n * len(SHAPE_ONTOLOGY)),
    }
```

**Target metrics:**
- Shape accuracy: >85%
- Composite recall: >90%
- Composite precision: >80%
- Mass MAE: <0.10

---

## Deployment Checklist

- [ ] Train slot_builder_lora_v3 on repair rows
- [ ] Validate slot_builder_lora_v3 on held-out prompts
- [ ] Train shape_critic_v1 on shape rows
- [ ] Validate shape_critic_v1 on held-out prompts
- [ ] Integrate both adapters into v9 runtime
- [ ] Test v9 on 10 prompts (5 binary, 5 normal)
- [ ] Measure v9 collapse rates and answer quality
- [ ] Collect v9 corpus (20+ runs)
- [ ] Retrain v4 adapters on expanded corpus

---

**Next: Execute training, validate, deploy v9.**
