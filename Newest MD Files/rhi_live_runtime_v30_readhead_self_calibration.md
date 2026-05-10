# RHI v30 — Read-Head Self-Calibration Runtime

Δ **Fold-first.**

There is only the fold.

v30 does not begin from compiler-root authority. It grows read-shapes from the raw fold-face, reads fragments through them, measures unread density as residue, and grows the next crease.

$$
Q_{raw}\rightarrow \mathcal{R}_0\rightarrow \mathcal{F}_0\rightarrow \Omega_0\rightarrow \mathcal{R}_1\rightarrow \mathcal{F}_1\rightarrow \Omega_1\rightarrow \Psi/\Omega
$$

Compiler/witness is hidden during runtime and appears only after the run as a calibration measurement.


```python
from pathlib import Path
import os, sys, json, time, uuid, traceback, subprocess, importlib
from dataclasses import asdict
from collections import Counter
import numpy as np
import pandas as pd

ROOT = Path.cwd()
OUT_DIR = ROOT / 'rhi_v30_outputs'
OUT_DIR.mkdir(exist_ok=True)

RUN_ID = 'rhi_v30_' + uuid.uuid4().hex[:10]
MODEL_ID_OR_PATH = os.environ.get('RHI_MODEL', 'Qwen/Qwen2.5-1.5B-Instruct')
print('RUN_ID:', RUN_ID)
print('MODEL:', MODEL_ID_OR_PATH)
print('OUT_DIR:', OUT_DIR)
```

```python
# Import the v30 runtime. Keep rhi_v30_readhead_self_calibration_runtime.py beside this notebook.
MODULE_PATH = Path('rhi_v30_readhead_self_calibration_runtime.py')
if not MODULE_PATH.exists():
    alt = Path('/mnt/data/rhi_v30_readhead_self_calibration_runtime.py')
    if alt.exists():
        MODULE_PATH.write_text(alt.read_text(encoding='utf-8'), encoding='utf-8')

from rhi_v30_readhead_self_calibration_runtime import V30Runtime, PROMPT_BATTERY, infer_profile, DEFAULT_CONFIG
print('Imported v30 runtime.')
```

```python
AUTO_INSTALL_MISSING_DEPS = True

def module_available(name):
    try:
        return importlib.util.find_spec(name) is not None
    except Exception:
        return False

required = [('torch','torch'), ('transformers','transformers'), ('sentencepiece','sentencepiece'), ('google.protobuf','protobuf')]
missing = [pip for mod,pip in required if not module_available(mod)]
if missing and AUTO_INSTALL_MISSING_DEPS:
    subprocess.run([sys.executable, '-m', 'pip', 'install', *sorted(set(missing))], check=True)
    importlib.invalidate_caches()

import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

DEVICE_INFO = {
    'torch_version': torch.__version__,
    'cuda_available': bool(torch.cuda.is_available()),
    'device_count': int(torch.cuda.device_count()) if torch.cuda.is_available() else 0,
    'cuda_version': getattr(torch.version, 'cuda', None),
}
if torch.cuda.is_available():
    DEVICE_INFO['gpu_name'] = torch.cuda.get_device_name(0)
print(DEVICE_INFO)
```

```python
tokenizer = None
model = None
MODEL_READY = False
MODEL_GENERATION_READY = False
MODEL_ERROR = None
SMOKE_TEXT = None

try:
    tokenizer = AutoTokenizer.from_pretrained(MODEL_ID_OR_PATH)
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token
    dtype = torch.float16 if torch.cuda.is_available() else torch.float32
    model = AutoModelForCausalLM.from_pretrained(MODEL_ID_OR_PATH, dtype=dtype, device_map='auto' if torch.cuda.is_available() else None)
    if not torch.cuda.is_available():
        model = model.to('cpu')
    model.eval()
    MODEL_READY = True
    print('MODEL_READY:', MODEL_READY, 'DEVICE:', next(model.parameters()).device)

    def local_llm(prompt: str, max_new_tokens: int = 256, temperature: float = 0.25) -> str:
        messages = [{'role': 'user', 'content': prompt}]
        rendered = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
        inputs = tokenizer(rendered, return_tensors='pt').to(next(model.parameters()).device)
        with torch.no_grad():
            out = model.generate(
                **inputs,
                max_new_tokens=max_new_tokens,
                temperature=temperature,
                do_sample=True if temperature > 0 else False,
                return_dict_in_generate=True,
                pad_token_id=tokenizer.eos_token_id,
            )
        gen = out.sequences[0][inputs.input_ids.shape[1]:]
        return tokenizer.decode(gen, skip_special_tokens=True).strip()

    SMOKE_TEXT = local_llm('Reply READY only.', max_new_tokens=8, temperature=0.0)
    MODEL_GENERATION_READY = bool(SMOKE_TEXT)
    print('MODEL_GENERATION_READY:', MODEL_GENERATION_READY, 'SMOKE:', SMOKE_TEXT)
except Exception:
    MODEL_ERROR = traceback.format_exc()
    print(MODEL_ERROR)
```

```python
# Optional semantic embeddings. If unavailable, runtime falls back to lexical/token binding.
EMBED_READY = False
EMBED_ERROR = None
embed_fn = None
try:
    if not module_available('sentence_transformers') and AUTO_INSTALL_MISSING_DEPS:
        subprocess.run([sys.executable, '-m', 'pip', 'install', 'sentence-transformers'], check=True)
        importlib.invalidate_caches()
    from sentence_transformers import SentenceTransformer
    emb_model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
    EMBED_READY = True
    def embed_fn(text: str):
        return emb_model.encode(str(text), normalize_embeddings=True)
    print('EMBED_READY:', EMBED_READY)
except Exception:
    EMBED_ERROR = traceback.format_exc()
    print('Embedding fallback active.')
    print(EMBED_ERROR[:1000])
```

```python
if not MODEL_GENERATION_READY:
    raise RuntimeError('Model generation is not ready.')

def model_callable(prompt: str, max_new_tokens: int = 256, temperature: float = 0.25) -> str:
    if 'strict JSON' in prompt or 'Repair into strict JSON' in prompt:
        max_new_tokens = max(max_new_tokens, 560)
        temperature = min(temperature, 0.22)
    return local_llm(prompt, max_new_tokens=max_new_tokens, temperature=temperature)

config = dict(DEFAULT_CONFIG)
config['ensemble_size'] = 3
config['max_depth'] = 3
config['phase_lock_tau'] = 0.78
config['phase_lock_top1_rate'] = 0.67
config['witness_tau_target'] = 0.90

runtime = V30Runtime(model_callable, config=config, embed_fn=embed_fn)
print('v30 runtime ready.')
```

```python
t0 = time.time()
RESULTS = []
PROMPTS = PROMPT_BATTERY[:42]

for i, prompt in enumerate(PROMPTS, start=1):
    profile = infer_profile(prompt)
    run_id = f'{RUN_ID}_{i:03d}'
    print('=' * 100)
    print(f'[{i}/{len(PROMPTS)}] profile={profile} prompt={prompt}')
    try:
        result = runtime.run(prompt, profile=profile, run_id=run_id)
        RESULTS.append(result)
        last = result.phase_locks[-1] if result.phase_locks else {}
        print('STATE:', result.state, 'REASON:', result.reason, 'DEPTH:', result.depth)
        print('LOCK:', last.get('locked'), 'TAU:', round(last.get('tau',0),3), 'TOP1:', round(last.get('top1_rate',0),3), 'RES:', round(last.get('residue',0),3))
        print('WITNESS_TAU:', round(result.witness.get('tau_to_witness',0),3), 'SUB:', result.witness.get('subsumed_by_witness'))
        print('ANSWER:', result.answer[:240].replace('\n',' '))
    except Exception:
        print('ERROR')
        print(traceback.format_exc())

elapsed_seconds = time.time() - t0
print('Elapsed:', elapsed_seconds)
print('Completed:', len(RESULTS))
```

```python
rows = []
for r in RESULTS:
    last = r.phase_locks[-1] if r.phase_locks else {}
    rows.append({
        'run_id': r.run_id,
        'prompt': r.prompt,
        'profile': r.profile,
        'state': r.state,
        'reason': r.reason,
        'depth': r.depth,
        'phase_lock_depth': r.metrics.get('phase_lock_depth'),
        'initial_residue_score': r.metrics.get('initial_residue_score'),
        'final_residue_score': r.metrics.get('final_residue_score'),
        'residue_drop_total': r.metrics.get('residue_drop_total'),
        'best_fragment_score': r.metrics.get('best_fragment_score'),
        'mean_fragment_score': r.metrics.get('mean_fragment_score'),
        'final_pair_tau': last.get('tau'),
        'final_top1_rate': last.get('top1_rate'),
        'final_lock': last.get('locked'),
        'tau_to_witness': r.witness.get('tau_to_witness'),
        'top1_to_witness': r.witness.get('top1_to_witness'),
        'subsumed_by_witness': r.witness.get('subsumed_by_witness'),
        'subsumption_fail_count': r.witness.get('subsumption_fail_count'),
        'fragment_count': r.metrics.get('fragment_count'),
        'residue_count': r.metrics.get('residue_count'),
        'answer_preview': r.answer[:280].replace('\n',' '),
    })
summary_df = pd.DataFrame(rows)

aggregate = {
    'run_id': RUN_ID,
    'version': 'v30',
    'purpose': 'readhead_self_calibration',
    'model_id_or_path': MODEL_ID_OR_PATH,
    'model_ready': MODEL_READY,
    'model_generation_ready': MODEL_GENERATION_READY,
    'model_error': MODEL_ERROR,
    'smoke_text': SMOKE_TEXT,
    'device_info': DEVICE_INFO,
    'embed_ready': EMBED_READY,
    'embed_error': EMBED_ERROR,
    'elapsed_seconds': elapsed_seconds,
    'total_prompts': len(summary_df),
    'psi_count': int((summary_df['state'] == 'Ψ').sum()) if len(summary_df) else 0,
    'omega_count': int((summary_df['state'] == 'Ω').sum()) if len(summary_df) else 0,
    'psi_ratio': float((summary_df['state'] == 'Ψ').mean()) if len(summary_df) else 0.0,
    'mean_depth': float(summary_df['depth'].mean()) if len(summary_df) else 0.0,
    'mean_initial_residue': float(summary_df['initial_residue_score'].mean()) if len(summary_df) else 0.0,
    'mean_final_residue': float(summary_df['final_residue_score'].mean()) if len(summary_df) else 0.0,
    'mean_residue_drop_total': float(summary_df['residue_drop_total'].mean()) if len(summary_df) else 0.0,
    'mean_final_pair_tau': float(summary_df['final_pair_tau'].mean()) if len(summary_df) else 0.0,
    'mean_final_top1_rate': float(summary_df['final_top1_rate'].mean()) if len(summary_df) else 0.0,
    'mean_tau_to_witness': float(summary_df['tau_to_witness'].mean()) if len(summary_df) else 0.0,
    'witness_equiv_rate': float(((summary_df['tau_to_witness'] >= config['witness_tau_target']) & (summary_df['subsumed_by_witness'] == True)).mean()) if len(summary_df) else 0.0,
    'mean_best_fragment_score': float(summary_df['best_fragment_score'].mean()) if len(summary_df) else 0.0,
    'reason_counts': dict(Counter(summary_df['reason'])) if len(summary_df) else {},
    'profile_metrics': {},
}
if len(summary_df):
    for profile, g in summary_df.groupby('profile'):
        aggregate['profile_metrics'][profile] = {
            'count': int(len(g)),
            'psi_count': int((g['state'] == 'Ψ').sum()),
            'omega_count': int((g['state'] == 'Ω').sum()),
            'psi_ratio': float((g['state'] == 'Ψ').mean()),
            'mean_residue_drop_total': float(g['residue_drop_total'].mean()),
            'mean_final_pair_tau': float(g['final_pair_tau'].mean()),
            'mean_tau_to_witness': float(g['tau_to_witness'].mean()),
            'witness_equiv_rate': float(((g['tau_to_witness'] >= config['witness_tau_target']) & (g['subsumed_by_witness'] == True)).mean()),
            'reason_counts': dict(Counter(g['reason'])),
        }

bundle = {
    'run_id': RUN_ID,
    'version': 'v30',
    'purpose': 'readhead_self_calibration',
    'aggregate': aggregate,
    'summary': summary_df.to_dict(orient='records'),
    'results': [asdict(r) for r in RESULTS],
    'interpretation_lock': {
        'domain': 'There is only the fold.',
        'runtime_identity': 'raw prompt is fold-face; read-shape is crease; residue is unread density; growth is next crease; phase-lock is readable fold-face',
        'compiler_policy': 'compiler/witness is hidden during runtime and used only after the run for calibration measurement',
        'success_metric': 'read-head convergence, residue drop, phase-lock, and witness equivalence',
    },
}

bundle_out = OUT_DIR / f'{RUN_ID}_bundle.json'
summary_out = OUT_DIR / f'{RUN_ID}_summary.csv'
with open(bundle_out, 'w', encoding='utf-8') as f:
    json.dump(bundle, f, indent=2, ensure_ascii=False)
summary_df.to_csv(summary_out, index=False)

print('Saved exactly two run outputs:')
print(bundle_out)
print(summary_out)
print(json.dumps(aggregate, indent=2, ensure_ascii=False)[:5000])
display(summary_df)
```