# RHI Live Runtime v26 — Slot Builder Kernel

Δ **Main branch only:** the new AI runtime.

v26 moves the spine forward:

$$
Q \rightarrow \text{SlotBuilder} \rightarrow C_Q \rightarrow \text{BranchEngine} \rightarrow \text{OperationalCritic} \rightarrow \Psi/\Omega
$$

The goal is not H-probing. The goal is to test whether a model can emit a usable **NeedSlot / runtime contract** before answering.

The notebook writes exactly two files:

1. `rhi_v26_<run_id>_bundle.json`
2. `rhi_v26_<run_id>_summary.csv`

The bundle contains slots, repairs, traces, branch answers, audits, and SFT-ready rows for a future SlotBuilder adapter. The summary is compact enough to hand back alone when needed.


```python
from __future__ import annotations

import os, re, sys, json, math, uuid, time, random, traceback, subprocess, importlib
from dataclasses import dataclass, asdict, field
from pathlib import Path
from typing import Any, Dict, List, Tuple, Optional
from collections import Counter, defaultdict

import numpy as np
import pandas as pd

ROOT = Path.cwd()
OUT_DIR = ROOT / "rhi_v26_outputs"
OUT_DIR.mkdir(exist_ok=True)
RUN_ID = "rhi_v26_" + uuid.uuid4().hex[:10]

SEED = 26
random.seed(SEED)
np.random.seed(SEED)

MODEL_ID_OR_PATH = os.environ.get("RHI_MODEL", "Qwen/Qwen2.5-1.5B-Instruct")
AUTO_INSTALL_MISSING_DEPS = True
REQUIRE_MODEL_FOR_PSI = True

RUN_PROMPT_LIMIT = 36
MAX_SLOT_REPAIR_ATTEMPTS = 2
MAX_RECURSION_DEPTH = 1
BRANCH_ROLES = ["construct", "verify", "repair", "counter"]
MAX_NEW_TOKENS_SLOT = 360
MAX_NEW_TOKENS_BRANCH = 190
MAX_NEW_TOKENS_SHAPER = 120
TEMPERATURE_SLOT = 0.25
TEMPERATURE_BRANCH = 0.45
TEMPERATURE_SHAPER = 0.30

# The central question of v26:
# can a model-generated slot compete with / beat the deterministic seed compiler?
SLOT_SELECTION_MODE = "best_of_seed_and_model"  # options: best_of_seed_and_model, model_only, seed_only

print("RHI v26 Slot Builder Kernel")
print("RUN_ID:", RUN_ID)
print("ROOT:", ROOT)
print("OUT_DIR:", OUT_DIR)
print("MODEL:", MODEL_ID_OR_PATH)
```

## 1. Runtime Structures

```python
@dataclass
class NeedSlot:
    prompt: str
    clean_prompt: str
    task_profile: str
    inverse_need: str
    preserved_function: str
    boundary_conditions: List[str]
    domain_carrier: List[str]
    forbidden_neighbors: List[str]
    polysemy_lock: Dict[str, Dict[str, str]]
    required_operations: List[str]
    success_criteria: List[str]
    failure_criteria: List[str]
    collapse_target: str
    repair_history: List[Dict[str, Any]] = field(default_factory=list)
    origin: str = "unknown"

@dataclass
class SlotAudit:
    score: float
    state: str
    reason: str
    F_need: float
    F_function: float
    F_boundary: float
    F_trap: float
    F_collapse: float
    F_carrier: float
    generic_penalty: float
    forbidden_penalty: float
    missing_fields: List[str]
    warnings: List[str]

@dataclass
class BranchResult:
    branch: str
    origin: str
    depth: int
    answer: str
    score: float
    state: str
    reason: str
    audit: Dict[str, Any]

@dataclass
class PromptResult:
    prompt: str
    task_profile: str
    state: str
    reason: str
    selected_slot_origin: str
    seed_slot_score: float
    model_slot_score: float
    selected_slot_score: float
    slot_delta_model_minus_seed: float
    winner_branch: Optional[str]
    winner_score: float
    answer: str
    raw_winner_answer: str
    shaped_answer: Optional[str]
    shaping_accepted: bool
    slot_candidates: List[Dict[str, Any]]
    selected_slot: Dict[str, Any]
    branches: List[Dict[str, Any]]
    trace: List[Dict[str, Any]]
    metrics: Dict[str, Any]
```

## 2. Dependencies and Model Load

A valid Ψ requires real model-origin output. If the model cannot generate, v26 records Ω instead of pretending.


```python
def _module_available(module_name: str) -> bool:
    try:
        return importlib.util.find_spec(module_name) is not None
    except ModuleNotFoundError:
        return False
    except Exception:
        return False

def ensure_runtime_dependencies() -> Dict[str, Any]:
    status = {"checked": True, "attempted_install": False, "missing_before": [], "missing_after": [], "errors": []}
    required = [("torch","torch"), ("transformers","transformers"), ("sentencepiece","sentencepiece"), ("google.protobuf","protobuf")]
    for module_name, pip_name in required:
        if not _module_available(module_name):
            status["missing_before"].append(pip_name)
    if status["missing_before"] and AUTO_INSTALL_MISSING_DEPS:
        status["attempted_install"] = True
        try:
            subprocess.run([sys.executable, "-m", "pip", "install", *sorted(set(status["missing_before"]))], check=True)
            importlib.invalidate_caches()
        except Exception as e:
            status["errors"].append(repr(e))
    for module_name, pip_name in required:
        if not _module_available(module_name):
            status["missing_after"].append(pip_name)
    return status

DEPENDENCY_STATUS = ensure_runtime_dependencies()

import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

def get_device_info() -> Dict[str, Any]:
    info = {
        "torch_version": torch.__version__,
        "cuda_available": bool(torch.cuda.is_available()),
        "device_count": int(torch.cuda.device_count()) if torch.cuda.is_available() else 0,
        "cuda_version": getattr(torch.version, "cuda", None),
    }
    if torch.cuda.is_available():
        info["gpu_name"] = torch.cuda.get_device_name(0)
    return info

DEVICE_INFO = get_device_info()

model = None
tokenizer = None
MODEL_READY = False
MODEL_GENERATION_READY = False
MODEL_ERROR = None
SMOKE_TEXT = None

def load_model():
    global model, tokenizer, MODEL_READY, MODEL_ERROR
    try:
        print("Loading model:", MODEL_ID_OR_PATH)
        tokenizer = AutoTokenizer.from_pretrained(MODEL_ID_OR_PATH)
        dtype = torch.float16 if torch.cuda.is_available() else torch.float32
        model = AutoModelForCausalLM.from_pretrained(
            MODEL_ID_OR_PATH,
            dtype=dtype,
            device_map="auto" if torch.cuda.is_available() else None,
        )
        if not torch.cuda.is_available():
            model = model.to("cpu")
        model.eval()
        MODEL_READY = True
        print("MODEL_READY:", MODEL_READY, "DEVICE:", next(model.parameters()).device)
    except Exception:
        MODEL_READY = False
        MODEL_ERROR = traceback.format_exc()
        print("MODEL LOAD ERROR")
        print(MODEL_ERROR)

def model_generate(prompt: str, max_new_tokens: int, temperature: float, do_sample: bool=True) -> str:
    if REQUIRE_MODEL_FOR_PSI and not MODEL_GENERATION_READY and "Reply with READY" not in prompt:
        raise RuntimeError("Model is not generation-ready; refusing fallback output.")
    messages = [{"role": "user", "content": prompt}]
    text = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
    inputs = tokenizer(text, return_tensors="pt").to(next(model.parameters()).device)
    with torch.no_grad():
        out = model.generate(
            **inputs,
            max_new_tokens=max_new_tokens,
            temperature=temperature,
            do_sample=do_sample,
            return_dict_in_generate=True,
            pad_token_id=tokenizer.eos_token_id,
        )
    gen = out.sequences[0][inputs.input_ids.shape[1]:]
    return tokenizer.decode(gen, skip_special_tokens=True).strip()

def smoke_test():
    global MODEL_GENERATION_READY, SMOKE_TEXT, MODEL_ERROR
    if not MODEL_READY:
        MODEL_GENERATION_READY = False
        return
    try:
        SMOKE_TEXT = model_generate("Reply with READY only.", 8, 0.0, do_sample=False)
        MODEL_GENERATION_READY = bool(SMOKE_TEXT)
        print("MODEL_GENERATION_READY:", MODEL_GENERATION_READY)
        print("SMOKE_TEXT:", SMOKE_TEXT)
    except Exception:
        MODEL_GENERATION_READY = False
        MODEL_ERROR = traceback.format_exc()
        print("SMOKE TEST FAILED")
        print(MODEL_ERROR)

load_model()
smoke_test()
print("DEPENDENCY_STATUS:", DEPENDENCY_STATUS)
print("DEVICE_INFO:", DEVICE_INFO)
```

## 3. Profiles, Locks, and Seed Slot Compiler

The seed compiler is the old hand-built support. The model slot-builder must compete against it.


```python
PROFILE_LEXICONS = {
    "runtime_contract": ["contract", "precondition", "postcondition", "success", "failure", "criteria", "side effect", "api call", "before execution", "runtime"],
    "tool_safety": ["tool call", "safe", "safety", "permission", "risk", "unsafe", "side effect", "shell", "execute", "allowed side effects"],
    "evidence_control": ["tool output", "tool result", "evidence", "observation", "command", "driver", "controller", "policy", "conflicting tool outputs"],
    "state_recovery": ["rollback", "recover", "recovery", "restore", "prior valid state", "undo", "failed", "failure", "trace", "corrupted"],
    "memory_trace": ["memory", "summary", "trace continuity", "causal", "state transitions", "observations", "decisions", "updates", "context amnesia"],
    "inverse_retrieval": ["retrieval", "retrieve", "search", "keyword", "noun", "label", "title", "inverse", "missing slot", "shape-first", "function", "operation", "candidate", "rank", "surface term", "affordance"],
    "slot_builder": ["slot", "needslot", "missing shape", "slot-builder", "contract compiler", "adapter", "lora", "groove", "train"],
}

SEMANTIC_LOCKS = {
    "contract": {"required_meaning": "runtime execution contract: preconditions, postconditions, success criteria, failure criteria, allowed side effects, rollback, trace update", "forbidden_meaning": "legal/binding agreement between parties, stakeholders, liability, compliance, signed contract"},
    "tool": {"required_meaning": "external function/API/action channel with possible side effects", "forbidden_meaning": "generic physical implement unless explicitly requested"},
    "controller": {"required_meaning": "agent governance loop that owns policy, verification, and next-action selection", "forbidden_meaning": "human administrator/security department unless explicitly requested"},
    "policy": {"required_meaning": "runtime decision rule", "forbidden_meaning": "organizational/legal/security ownership"},
    "evidence": {"required_meaning": "observation submitted to verifier/controller", "forbidden_meaning": "command or authority by itself"},
    "memory": {"required_meaning": "causal trace continuity", "forbidden_meaning": "mere text summary"},
    "retrieval": {"required_meaning": "operational fit / missing-slot recovery", "forbidden_meaning": "noun overlap or keyword-only lookup"},
    "shape": {"required_meaning": "operational structure / inverse need", "forbidden_meaning": "literal geometry unless explicitly requested"},
}

GENERIC_SLOT_PHRASES = [
    "answer the prompt", "provide a response", "be helpful", "general answer", "user asks", "relevant information", "as an ai", "depends on context"
]

FORBIDDEN_DRIFT_TERMS = [
    "legal agreement", "liability", "stakeholder", "terms of service", "lawsuit", "company policy", "security team owns", "administrator owns", "tool decides", "output commands", "keyword-only", "noun lookup only", "literal circle", "literal square"
]

def normalize_text(s: str) -> str:
    return re.sub(r"\s+", " ", (s or "").strip().lower())

def contains_any(text: str, terms: List[str]) -> bool:
    t = normalize_text(text)
    return any(term.lower() in t for term in terms)

def count_terms(text: str, terms: List[str]) -> int:
    t = normalize_text(text)
    return sum(1 for term in terms if term.lower() in t)

def text_terms(text: str) -> List[str]:
    return re.findall(r"\b[a-zA-Z][a-zA-Z0-9_-]{2,}\b", normalize_text(text))

def classify_profile(prompt: str) -> Tuple[str, Dict[str, Any]]:
    p = normalize_text(prompt)
    scores = {profile: count_terms(p, terms) for profile, terms in PROFILE_LEXICONS.items()}
    if "tool output" in p or "tool result" in p or ("evidence" in p and "tool" in p): scores["evidence_control"] += 4
    if "controller" in p and ("policy" in p or "tool" in p): scores["evidence_control"] += 3
    if "api call" in p and ("success" in p or "failure" in p or "criteria" in p): scores["runtime_contract"] += 4
    if "safe" in p or "unsafe" in p or "permission" in p or "risk" in p: scores["tool_safety"] += 3
    if "rollback" in p or "restore" in p or "recover" in p or "undo" in p: scores["state_recovery"] += 4
    if "memory" in p or "summary" in p or "trace" in p: scores["memory_trace"] += 4
    if "retriev" in p or "search" in p or "keyword" in p or "noun" in p or "label" in p: scores["inverse_retrieval"] += 4
    if "slot" in p or "lora" in p or "adapter" in p or "contract compiler" in p: scores["slot_builder"] += 4
    best = max(scores, key=scores.get)
    if scores[best] == 0:
        best = "runtime_contract" if "agent" in p or "ai" in p else "inverse_retrieval"
    return best, {"profile_scores": scores}

def clean_domain_carrier(prompt: str, max_terms: int=10) -> List[str]:
    stop = set("the a an and or but if then with without from into onto this that these those current should could would when where why how what explain design build describe for before after rather than not only all any are is be to of in on by as it its".split())
    terms = []
    for w in text_terms(prompt):
        if w not in stop and w not in terms:
            terms.append(w)
    return terms[:max_terms]

def profile_seed(profile: str) -> Dict[str, Any]:
    seeds = {
        "runtime_contract": dict(
            inverse_need="construct the runtime execution contract implied by the prompt before action",
            preserved_function="bound an agent/tool/function action with preconditions, postconditions, success/failure criteria, side effects, rollback, and trace update",
            required_operations=["identify action", "define preconditions", "define postconditions", "bound side effects", "define rollback", "update trace"],
            forbidden_neighbors=["legal contract interpretation", "stakeholder/liability framing", "execute before checking"],
        ),
        "tool_safety": dict(
            inverse_need="decide whether a tool call is safe before execution",
            preserved_function="gate external action through permission, risk, preconditions, bounded side effects, and safe failure",
            required_operations=["check permission", "check preconditions", "score risk", "bound side effects", "reject or rollback unsafe action"],
            forbidden_neighbors=["just run it", "tool-first execution", "unbounded side effect"],
        ),
        "evidence_control": dict(
            inverse_need="treat tool output as evidence rather than command",
            preserved_function="route observations through verifier, controller policy, contract gate, and trace before next action",
            required_operations=["receive observation", "verify evidence", "apply controller policy", "select next action", "update trace"],
            forbidden_neighbors=["tool output as authority", "tool decides", "administrator policy drift"],
        ),
        "state_recovery": dict(
            inverse_need="recover after failure while preserving causal trace",
            preserved_function="restore prior valid state without erasing evidence, decision history, or rollback cause",
            required_operations=["detect failure", "freeze evidence", "restore state", "preserve trace", "prevent cascade"],
            forbidden_neighbors=["erase trace", "hide failure", "start over blindly"],
        ),
        "memory_trace": dict(
            inverse_need="represent memory as causal trace continuity rather than text summary",
            preserved_function="preserve state transitions, observations, decisions, actions, results, rollback, and updates across turns",
            required_operations=["preserve state", "preserve observations", "preserve decisions", "preserve updates", "avoid summary-only memory"],
            forbidden_neighbors=["memory as mere summary", "recap-only storage", "lost which-path"],
        ),
        "inverse_retrieval": dict(
            inverse_need="retrieve by inverse operational fit when noun/label matching fails",
            preserved_function="find the artifact that closes the missing operational slot even if surface terms do not match",
            required_operations=["extract operation", "infer missing slot", "generate candidates", "rank by function", "verify operational fit"],
            forbidden_neighbors=["keyword matching", "noun lookup", "title match only", "literal shape drift", "unverified retrieval"],
        ),
        "slot_builder": dict(
            inverse_need="emit the missing-shape contract C_Q from the prompt before answering",
            preserved_function="compile prompt intent into a NeedSlot contract that downstream branches can audit against",
            required_operations=["infer inverse need", "state preserved function", "set boundaries", "name traps", "define collapse target"],
            forbidden_neighbors=["answer directly before slot", "dataset worship", "full retrain reflex", "loss-only tuning"],
        ),
    }
    return seeds.get(profile, seeds["inverse_retrieval"])

def seed_slot_compiler(prompt: str, profile: Optional[str]=None) -> NeedSlot:
    if profile is None:
        profile, _ = classify_profile(prompt)
    seed = profile_seed(profile)
    carrier = clean_domain_carrier(prompt)
    boundary = [
        "answer directly after slot formation; do not print internal spec unless requested",
        "require model-origin payload when model mode is enabled",
        "prefer Ω over false Ψ when operational fit fails",
        "reject shared vocabulary without preserved function",
    ]
    if profile in ["runtime_contract", "evidence_control"]:
        boundary.append("contract means runtime execution contract, not legal agreement")
    if profile == "inverse_retrieval":
        boundary.append("shape means operational fit / inverse need, not literal geometry")
    if profile == "memory_trace":
        boundary.append("memory means causal trace continuity, not text summary")
    return NeedSlot(
        prompt=prompt,
        clean_prompt=prompt.strip(),
        task_profile=profile,
        inverse_need=seed["inverse_need"],
        preserved_function=seed["preserved_function"],
        boundary_conditions=boundary,
        domain_carrier=carrier,
        forbidden_neighbors=seed["forbidden_neighbors"],
        polysemy_lock={k:v for k,v in SEMANTIC_LOCKS.items() if k in ["contract","tool","controller","policy","evidence","memory","retrieval","shape"]},
        required_operations=seed["required_operations"],
        success_criteria=["candidate answer occupies the inverse need", "preserved function survives", "forbidden carrier is rejected", "collapse is traceable"],
        failure_criteria=["generic slot", "wrong semantic carrier", "surface label match without operation", "false Ψ"],
        collapse_target="one executable answer with model origin, operational fit, prompt grounding, trap rejection, and trace sufficient to debug",
        origin="seed_compiler",
    )
```

## 4. Model SlotBuilder

The model emits a NeedSlot JSON. The critic then decides whether to use it, repair it, or fall back to the seed compiler.


```python
SLOT_SCHEMA_KEYS = [
    "task_profile", "inverse_need", "preserved_function", "boundary_conditions", "domain_carrier",
    "forbidden_neighbors", "polysemy_lock", "required_operations", "success_criteria", "failure_criteria", "collapse_target"
]

def json_extract_first_object(text: str) -> Optional[Dict[str, Any]]:
    if not text:
        return None
    s = text.strip()
    # Remove markdown fences.
    s = re.sub(r"^```(?:json)?", "", s, flags=re.I).strip()
    s = re.sub(r"```$", "", s).strip()
    # Try direct parse first.
    try:
        obj = json.loads(s)
        if isinstance(obj, dict):
            return obj
    except Exception:
        pass
    # Balanced brace extraction.
    start = s.find("{")
    if start < 0:
        return None
    depth = 0
    in_str = False
    esc = False
    for i in range(start, len(s)):
        ch = s[i]
        if in_str:
            if esc:
                esc = False
            elif ch == "\\":
                esc = True
            elif ch == '"':
                in_str = False
        else:
            if ch == '"':
                in_str = True
            elif ch == "{":
                depth += 1
            elif ch == "}":
                depth -= 1
                if depth == 0:
                    candidate = s[start:i+1]
                    try:
                        obj = json.loads(candidate)
                        if isinstance(obj, dict):
                            return obj
                    except Exception:
                        return None
    return None

def coerce_list(x: Any) -> List[str]:
    if x is None:
        return []
    if isinstance(x, list):
        return [str(v).strip() for v in x if str(v).strip()]
    if isinstance(x, str):
        parts = re.split(r"[;\n]|(?:,\s+)", x)
        return [p.strip(" -•\t") for p in parts if p.strip(" -•\t")]
    return [str(x)]

def coerce_polysemy(x: Any) -> Dict[str, Dict[str, str]]:
    if not isinstance(x, dict):
        return {}
    out = {}
    for k, v in x.items():
        if isinstance(v, dict):
            out[str(k)] = {
                "required_meaning": str(v.get("required_meaning", v.get("required", ""))),
                "forbidden_meaning": str(v.get("forbidden_meaning", v.get("forbidden", ""))),
            }
        else:
            out[str(k)] = {"required_meaning": str(v), "forbidden_meaning": ""}
    return out

def slot_from_obj(prompt: str, obj: Dict[str, Any], origin: str) -> NeedSlot:
    profile = str(obj.get("task_profile") or classify_profile(prompt)[0]).strip()
    if profile not in PROFILE_LEXICONS:
        profile = classify_profile(prompt)[0]
    seed = seed_slot_compiler(prompt, profile)
    poly = coerce_polysemy(obj.get("polysemy_lock")) or seed.polysemy_lock
    return NeedSlot(
        prompt=prompt,
        clean_prompt=str(obj.get("clean_prompt") or prompt.strip()),
        task_profile=profile,
        inverse_need=str(obj.get("inverse_need") or seed.inverse_need),
        preserved_function=str(obj.get("preserved_function") or seed.preserved_function),
        boundary_conditions=coerce_list(obj.get("boundary_conditions")) or seed.boundary_conditions,
        domain_carrier=coerce_list(obj.get("domain_carrier")) or clean_domain_carrier(prompt),
        forbidden_neighbors=coerce_list(obj.get("forbidden_neighbors")) or seed.forbidden_neighbors,
        polysemy_lock=poly,
        required_operations=coerce_list(obj.get("required_operations")) or seed.required_operations,
        success_criteria=coerce_list(obj.get("success_criteria")) or seed.success_criteria,
        failure_criteria=coerce_list(obj.get("failure_criteria")) or seed.failure_criteria,
        collapse_target=str(obj.get("collapse_target") or seed.collapse_target),
        repair_history=coerce_list(obj.get("repair_history")) if not isinstance(obj.get("repair_history"), list) else obj.get("repair_history", []),
        origin=origin,
    )

def slot_builder_prompt(prompt: str, seed: NeedSlot, prior_audit: Optional[SlotAudit]=None) -> str:
    critique = ""
    if prior_audit:
        critique = f"""
PRIOR SLOT AUDIT:
state={prior_audit.state}
reason={prior_audit.reason}
missing_fields={prior_audit.missing_fields}
warnings={prior_audit.warnings}
Score components: need={prior_audit.F_need:.3f}, function={prior_audit.F_function:.3f}, boundary={prior_audit.F_boundary:.3f}, trap={prior_audit.F_trap:.3f}, collapse={prior_audit.F_collapse:.3f}
Repair the slot. Do not answer the user prompt.
""".strip()
    return f"""
You are the RHI SlotBuilder. Your job is not to answer the user. Your job is to compile the prompt into a NeedSlot contract C_Q.

USER PROMPT:
{prompt}

SEED PROFILE: {seed.task_profile}
SEED INVERSE NEED: {seed.inverse_need}
SEED PRESERVED FUNCTION: {seed.preserved_function}

{critique}

Return JSON only. No markdown. No explanation.

Required JSON fields:
{json.dumps(SLOT_SCHEMA_KEYS, indent=2)}

Rules:
- inverse_need = the missing operational slot implied by the prompt.
- preserved_function = what must remain true after answer generation.
- boundary_conditions = constraints that prevent false collapse.
- domain_carrier = important non-stopword prompt terms.
- forbidden_neighbors = adjacent wrong answers / semantic traps.
- polysemy_lock = map ambiguous words to required_meaning and forbidden_meaning.
- required_operations = verbs/actions the answer must perform.
- collapse_target = one sentence specifying valid Ψ.
- Do not write a generic helpfulness contract.
- Do not legalize runtime words.
""".strip()

def generate_model_slot(prompt: str, seed: NeedSlot, prior_audit: Optional[SlotAudit]=None) -> Tuple[Optional[NeedSlot], Dict[str, Any]]:
    try:
        raw = model_generate(slot_builder_prompt(prompt, seed, prior_audit), MAX_NEW_TOKENS_SLOT, TEMPERATURE_SLOT, do_sample=True)
        obj = json_extract_first_object(raw)
        if obj is None:
            return None, {"origin": "model_slot_builder", "raw": raw, "error": "json_parse_failed"}
        slot = slot_from_obj(prompt, obj, "model_slot_builder")
        return slot, {"origin": "model_slot_builder", "raw": raw, "parsed": obj, "error": None}
    except Exception:
        return None, {"origin": "model_slot_builder", "raw": "", "error": traceback.format_exc()}
```

## 5. Slot Critic

The critic scores what the slot **does**, not just what it says.

$$
A_t=(F_{need},F_{function},F_{boundary},F_{trap},F_{collapse})
$$


```python
def non_generic_score(text: str) -> float:
    t = normalize_text(text)
    if not t:
        return 0.0
    hits = sum(1 for p in GENERIC_SLOT_PHRASES if p in t)
    return max(0.0, 1.0 - 0.25 * hits)

def overlap_score(text: str, terms: List[str]) -> float:
    if not terms:
        return 0.0
    t = normalize_text(text)
    return sum(1 for term in terms if normalize_text(term) in t) / max(1, len(terms))

def list_quality(items: List[str], min_len: int=3) -> float:
    if not items:
        return 0.0
    unique = len(set(normalize_text(x) for x in items if normalize_text(x)))
    length = min(1.0, len(items) / max(1, min_len))
    diversity = min(1.0, unique / max(1, len(items)))
    specificity = np.mean([min(1.0, len(text_terms(x))/5) for x in items]) if items else 0.0
    return float(0.40*length + 0.25*diversity + 0.35*specificity)

def audit_slot(slot: NeedSlot) -> SlotAudit:
    missing = []
    warnings = []
    for key in SLOT_SCHEMA_KEYS:
        val = getattr(slot, key, None)
        if val is None or val == "" or val == [] or val == {}:
            missing.append(key)

    prompt_terms = clean_domain_carrier(slot.prompt, max_terms=12)
    profile_terms = PROFILE_LEXICONS.get(slot.task_profile, [])

    need_text = slot.inverse_need
    func_text = slot.preserved_function
    boundary_text = " ".join(slot.boundary_conditions)
    trap_text = " ".join(slot.forbidden_neighbors) + " " + json.dumps(slot.polysemy_lock)
    collapse_text = slot.collapse_target
    all_text = " ".join([need_text, func_text, boundary_text, trap_text, collapse_text])

    F_need = 0.45*non_generic_score(need_text) + 0.30*overlap_score(need_text, profile_terms[:10]) + 0.25*min(1.0, len(text_terms(need_text))/10)
    F_function = 0.40*non_generic_score(func_text) + 0.35*overlap_score(func_text, profile_terms[:10]) + 0.25*min(1.0, len(text_terms(func_text))/12)
    F_boundary = list_quality(slot.boundary_conditions, 4)
    F_trap = 0.45*list_quality(slot.forbidden_neighbors, 3) + 0.35*min(1.0, len(slot.polysemy_lock)/3) + 0.20*(1.0 if any(k in slot.polysemy_lock for k in ["contract","tool","memory","retrieval","evidence","controller","policy","shape"]) else 0.0)
    F_collapse = 0.45*non_generic_score(collapse_text) + 0.30*(1.0 if contains_any(collapse_text, ["model", "operational", "trace", "collapse", "answer", "Ψ", "valid"]) else 0.0) + 0.25*min(1.0, len(text_terms(collapse_text))/16)
    F_carrier = 0.60*min(1.0, len(slot.domain_carrier)/6) + 0.40*overlap_score(" ".join(slot.domain_carrier), prompt_terms)

    generic_penalty = 0.0
    for p in GENERIC_SLOT_PHRASES:
        if p in normalize_text(all_text):
            generic_penalty += 0.035
    forbidden_penalty = 0.0
    for p in FORBIDDEN_DRIFT_TERMS:
        if p in normalize_text(all_text):
            forbidden_penalty += 0.07
            warnings.append("forbidden_drift:" + p)

    if slot.task_profile == "inverse_retrieval" and contains_any(all_text, ["literal circle", "literal square", "geometry shape"]):
        forbidden_penalty += 0.10
        warnings.append("literal_shape_drift")
    if slot.task_profile in ["runtime_contract", "evidence_control"] and contains_any(all_text, ["legal agreement", "liability", "stakeholder"]):
        forbidden_penalty += 0.12
        warnings.append("legal_contract_drift")
    if slot.task_profile == "memory_trace" and contains_any(all_text, ["summary only", "text summary"]):
        forbidden_penalty += 0.10
        warnings.append("summary_only_drift")

    score = (0.24*F_need + 0.24*F_function + 0.18*F_boundary + 0.16*F_trap + 0.12*F_collapse + 0.06*F_carrier) - generic_penalty - forbidden_penalty
    score = float(max(0.0, min(1.0, score)))

    if len(slot.boundary_conditions) < 3: warnings.append("thin_boundary")
    if len(slot.forbidden_neighbors) < 2: warnings.append("thin_trap_field")
    if len(slot.required_operations) < 3: warnings.append("thin_required_operations")
    if F_need < 0.45: warnings.append("weak_inverse_need")
    if F_function < 0.45: warnings.append("weak_preserved_function")

    state = "Ψ" if score >= 0.68 and not missing and forbidden_penalty < 0.15 else "Ω"
    reason = "slot_fit" if state == "Ψ" else "slot_residue"
    return SlotAudit(score, state, reason, float(F_need), float(F_function), float(F_boundary), float(F_trap), float(F_collapse), float(F_carrier), float(generic_penalty), float(forbidden_penalty), missing, warnings)

def repair_slot_deterministic(slot: NeedSlot, seed: NeedSlot, audit: SlotAudit) -> NeedSlot:
    repaired = NeedSlot(**asdict(slot))
    repaired.repair_history = list(repaired.repair_history or []) + [{"mode":"deterministic_patch", "audit": asdict(audit)}]
    if audit.F_need < 0.45 or "inverse_need" in audit.missing_fields:
        repaired.inverse_need = seed.inverse_need
    if audit.F_function < 0.45 or "preserved_function" in audit.missing_fields:
        repaired.preserved_function = seed.preserved_function
    if len(repaired.boundary_conditions) < 3:
        repaired.boundary_conditions = list(dict.fromkeys(repaired.boundary_conditions + seed.boundary_conditions))[:8]
    if len(repaired.forbidden_neighbors) < 2:
        repaired.forbidden_neighbors = list(dict.fromkeys(repaired.forbidden_neighbors + seed.forbidden_neighbors))[:8]
    if len(repaired.required_operations) < 3:
        repaired.required_operations = list(dict.fromkeys(repaired.required_operations + seed.required_operations))[:8]
    if not repaired.domain_carrier:
        repaired.domain_carrier = seed.domain_carrier
    if len(repaired.polysemy_lock) < 2:
        repaired.polysemy_lock = {**seed.polysemy_lock, **repaired.polysemy_lock}
    if not repaired.collapse_target:
        repaired.collapse_target = seed.collapse_target
    repaired.origin = repaired.origin + "+deterministic_repair"
    return repaired

def build_slot_candidates(prompt: str) -> Tuple[List[Dict[str, Any]], NeedSlot, SlotAudit, Dict[str, Any]]:
    profile, profile_info = classify_profile(prompt)
    seed = seed_slot_compiler(prompt, profile)
    seed_audit = audit_slot(seed)
    candidates = [{"slot": seed, "audit": seed_audit, "meta": {"origin":"seed_compiler"}}]

    model_slot = None
    model_meta = {"error": "not_attempted"}
    prior_audit = None
    if SLOT_SELECTION_MODE != "seed_only":
        for attempt in range(MAX_SLOT_REPAIR_ATTEMPTS + 1):
            ms, meta = generate_model_slot(prompt, seed, prior_audit)
            model_meta = meta
            if ms is None:
                # Create no candidate, but continue once with seed-informed prior.
                prior_audit = SlotAudit(0.0, "Ω", "model_slot_parse_failed", 0,0,0,0,0,0,0,0, ["json_parse"], [str(meta.get("error"))[:200]])
                continue
            ma = audit_slot(ms)
            candidates.append({"slot": ms, "audit": ma, "meta": {**meta, "attempt": attempt}})
            if ma.state == "Ψ":
                model_slot = ms
                break
            prior_audit = ma
            # Deterministic patch of model output as an additional candidate.
            patched = repair_slot_deterministic(ms, seed, ma)
            pa = audit_slot(patched)
            candidates.append({"slot": patched, "audit": pa, "meta": {"origin":"model_slot_patched", "attempt": attempt}})
            if pa.state == "Ψ":
                model_slot = patched
                break

    if SLOT_SELECTION_MODE == "model_only":
        selectable = [c for c in candidates if c["slot"].origin.startswith("model")]
    elif SLOT_SELECTION_MODE == "seed_only":
        selectable = [candidates[0]]
    else:
        selectable = candidates

    selected = max(selectable or candidates, key=lambda c: c["audit"].score)
    return candidates, selected["slot"], selected["audit"], profile_info
```

## 6. Branch Engine and Operational Critic

```python
def slot_digest(slot: NeedSlot) -> str:
    return json.dumps({
        "task_profile": slot.task_profile,
        "inverse_need": slot.inverse_need,
        "preserved_function": slot.preserved_function,
        "boundary_conditions": slot.boundary_conditions,
        "domain_carrier": slot.domain_carrier,
        "forbidden_neighbors": slot.forbidden_neighbors,
        "polysemy_lock": slot.polysemy_lock,
        "required_operations": slot.required_operations,
        "collapse_target": slot.collapse_target,
    }, indent=2, ensure_ascii=False)

def make_answer_prompt(prompt: str, slot: NeedSlot, branch: str, prior_failure: Optional[Dict[str, Any]]=None) -> str:
    branch_rule = {
        "construct": "Construct the best answer that occupies the NeedSlot.",
        "verify": "First verify the NeedSlot and reject wrong semantic carriers, then answer.",
        "repair": "Repair likely failure modes before answering. Preserve the slot.",
        "counter": "Stress-test adjacent wrong answers, then answer from the preserved function.",
    }.get(branch, "Answer from the NeedSlot.")
    pf = ""
    if prior_failure:
        pf = "\nPRIOR FAILURE SIGNAL:\n" + json.dumps(prior_failure, indent=2, ensure_ascii=False)
    return f"""
You are inside RHI v26. The prompt has already been compiled into a NeedSlot contract. Do not ignore it.

USER PROMPT:
{prompt}

NEEDSLOT CONTRACT C_Q:
{slot_digest(slot)}

BRANCH ROLE: {branch}
{branch_rule}
{pf}

OUTPUT RULES:
- Answer the user directly.
- Preserve the preserved_function.
- Do not print the whole NeedSlot unless the prompt asks for a schema.
- Reject forbidden_neighbors.
- Keep runtime meanings locked; do not legalize or literalize terms.
""".strip()

def audit_answer(answer: str, slot: NeedSlot, origin: str="model") -> Dict[str, Any]:
    a = normalize_text(answer)
    wc = len(text_terms(answer))
    required_ops = slot.required_operations
    forbidden = slot.forbidden_neighbors
    carrier = slot.domain_carrier

    F_need = 0.55*overlap_score(a, text_terms(slot.inverse_need)) + 0.25*contains_any(a, ["need", "missing", "operation", "function", "slot"]).__float__() + 0.20*min(1.0, wc/80)
    F_function = 0.55*overlap_score(a, text_terms(slot.preserved_function)) + 0.35*overlap_score(a, required_ops) + 0.10*min(1.0, wc/100)
    F_boundary = 1.0 - min(1.0, count_terms(a, forbidden) / max(1, len(forbidden)))
    F_trap = 1.0
    trap_hits = []
    for t in forbidden + FORBIDDEN_DRIFT_TERMS:
        if normalize_text(t) in a:
            trap_hits.append(t)
    if trap_hits:
        F_trap = max(0.0, 1.0 - 0.18*len(trap_hits))
    F_collapse = 0.45*min(1.0, wc/70) + 0.30*overlap_score(a, slot.success_criteria) + 0.25*(1.0 if origin == "model" else 0.0)
    F_carrier = 0.45*overlap_score(a, carrier) + 0.55*overlap_score(a, required_ops)

    legal_drift = contains_any(a, ["legal agreement", "liability", "stakeholder", "lawsuit", "terms of service"])
    tool_driver_drift = slot.task_profile == "evidence_control" and contains_any(a, ["tool decides", "output commands", "tool result controls"])
    summary_drift = slot.task_profile == "memory_trace" and contains_any(a, ["memory is just a summary", "only a summary"])
    literal_shape_drift = slot.task_profile == "inverse_retrieval" and contains_any(a, ["circle", "square", "triangle", "literal shape"]) and not contains_any(a, ["operation", "function", "affordance", "slot"])

    drift_flags = {
        "legal_drift": legal_drift,
        "tool_driver_drift": tool_driver_drift,
        "summary_drift": summary_drift,
        "literal_shape_drift": literal_shape_drift,
    }
    drift_penalty = 0.16 * sum(1 for v in drift_flags.values() if v)
    trap_penalty = 0.06 * len(trap_hits)

    score = 0.22*F_need + 0.28*F_function + 0.14*F_boundary + 0.16*F_trap + 0.12*F_collapse + 0.08*F_carrier - drift_penalty - trap_penalty
    score = float(max(0.0, min(1.0, score)))

    threshold = 0.66 if slot.task_profile in ["inverse_retrieval", "memory_trace"] else 0.68
    state = "Ψ" if score >= threshold and not any(drift_flags.values()) and origin == "model" else "Ω"
    reason = "answer_operational_fit" if state == "Ψ" else "answer_residue"
    return {
        "score": score,
        "state": state,
        "reason": reason,
        "word_count": wc,
        "F_need": float(F_need),
        "F_function": float(F_function),
        "F_boundary": float(F_boundary),
        "F_trap": float(F_trap),
        "F_collapse": float(F_collapse),
        "F_carrier": float(F_carrier),
        "trap_hits": trap_hits,
        "drift_flags": drift_flags,
        "threshold": threshold,
    }

def run_branches(prompt: str, slot: NeedSlot, depth: int, prior_failure: Optional[Dict[str, Any]]=None) -> List[BranchResult]:
    out = []
    roles = BRANCH_ROLES if depth == 0 else ["repair", "verify", "counter", "construct"]
    for branch in roles:
        try:
            ap = make_answer_prompt(prompt, slot, branch, prior_failure)
            ans = model_generate(ap, MAX_NEW_TOKENS_BRANCH, TEMPERATURE_BRANCH, do_sample=True)
            aud = audit_answer(ans, slot, origin="model")
            out.append(BranchResult(branch, "model", depth, ans, aud["score"], aud["state"], aud["reason"], aud))
        except Exception:
            aud = {"score":0.0, "state":"Ω", "reason":"generation_error", "error": traceback.format_exc()}
            out.append(BranchResult(branch, "error", depth, "", 0.0, "Ω", "generation_error", aud))
    return out

def operational_agreement(branches: List[BranchResult]) -> float:
    valid = [b for b in branches if b.origin == "model" and b.answer]
    if len(valid) < 2:
        return 0.0
    keys = ["F_need", "F_function", "F_boundary", "F_trap", "F_collapse", "F_carrier"]
    hot = 0
    total = 0
    for k in keys:
        vals = [b.audit.get(k,0.0) for b in valid]
        if np.mean(vals) >= 0.62:
            hot += 1
        total += 1
    return hot / max(1,total)

def collapse_answer(branches: List[BranchResult]) -> Tuple[str, str, Optional[BranchResult], Dict[str, Any]]:
    if not branches:
        return "Ω", "no_branches", None, {}
    ordered = sorted(branches, key=lambda b: b.score, reverse=True)
    best = ordered[0]
    second = ordered[1] if len(ordered) > 1 else None
    margin = best.score - (second.score if second else 0.0)
    valid = [b for b in ordered if b.state == "Ψ" and b.origin == "model"]
    op_agree = operational_agreement(ordered[:4])
    meta = {"margin": float(margin), "valid_count": len(valid), "operational_agreement": float(op_agree)}
    if best.state == "Ψ" and margin >= 0.045:
        return "Ψ", "direct_margin_collapse", best, meta
    if valid and op_agree >= 0.67 and np.mean([b.score for b in valid[:3]]) >= valid[0].audit.get("threshold", 0.68) - 0.03:
        return "Ψ", "operational_consensus_collapse", valid[0], meta
    return "Ω", "answer_residue", best, meta
```

## 7. Payload Shaper and SFT Row Builder

```python
def shape_payload(prompt: str, slot: NeedSlot, raw_answer: str, raw_score: float) -> Tuple[str, bool, Dict[str, Any]]:
    try:
        sp = f"""
Compress this accepted RHI answer without changing its operational meaning.

USER PROMPT:
{prompt}

PRESERVED FUNCTION:
{slot.preserved_function}

REQUIRED OPERATIONS:
{json.dumps(slot.required_operations, ensure_ascii=False)}

FORBIDDEN NEIGHBORS:
{json.dumps(slot.forbidden_neighbors, ensure_ascii=False)}

RAW ANSWER:
{raw_answer}

Return only the compressed answer. Keep it direct. Do not add legal/organizational drift.
""".strip()
        shaped = model_generate(sp, MAX_NEW_TOKENS_SHAPER, TEMPERATURE_SHAPER, do_sample=True)
        aud = audit_answer(shaped, slot, origin="model")
        raw_wc = len(text_terms(raw_answer))
        shaped_wc = len(text_terms(shaped))
        accepted = aud["state"] == "Ψ" and aud["score"] >= max(0.62, raw_score - 0.10) and shaped_wc <= max(raw_wc + 12, 140)
        return (shaped if accepted else raw_answer), bool(accepted), {"audit": aud, "raw_words": raw_wc, "shaped_words": shaped_wc, "compression": 1 - shaped_wc/max(1,raw_wc), "reason": "accepted" if accepted else "rejected"}
    except Exception:
        return raw_answer, False, {"reason": "shape_error", "error": traceback.format_exc()}

def make_sft_row(prompt: str, slot: NeedSlot, selected: bool=True) -> Dict[str, Any]:
    # This stays inside the bundle; no extra file. It can become a LoRA SlotBuilder corpus later.
    target = {
        "task_profile": slot.task_profile,
        "inverse_need": slot.inverse_need,
        "preserved_function": slot.preserved_function,
        "boundary_conditions": slot.boundary_conditions,
        "domain_carrier": slot.domain_carrier,
        "forbidden_neighbors": slot.forbidden_neighbors,
        "polysemy_lock": slot.polysemy_lock,
        "required_operations": slot.required_operations,
        "success_criteria": slot.success_criteria,
        "failure_criteria": slot.failure_criteria,
        "collapse_target": slot.collapse_target,
    }
    return {
        "messages": [
            {"role": "system", "content": "You are the RHI SlotBuilder. Emit NeedSlot JSON only."},
            {"role": "user", "content": prompt},
            {"role": "assistant", "content": json.dumps(target, ensure_ascii=False)},
        ],
        "selected": selected,
        "slot_origin": slot.origin,
        "task_profile": slot.task_profile,
    }
```

## 8. Prompt Battery

```python
PROMPT_BATTERY = [
    "explain why current AI agents fail when they use tools before forming a contract",
    "design a runtime contract for a file-writing tool",
    "explain success and failure criteria for an API call",
    "build a tool-use contract for deleting a file",
    "how should an agent decide whether a tool call is safe",
    "define allowed side effects for a tool before calling it",
    "design a safety gate for an external API call",
    "when should an agent reject a tool call",
    "why is tool output evidence rather than the driver of the agent",
    "explain why a tool result should not control the next action by itself",
    "describe tool output as observation not command",
    "why should the controller own policy after a tool returns",
    "describe how rollback protects an agent after a failed API call",
    "explain how trace continuity helps an agent recover after a mistake",
    "design a recovery path after a failed tool call",
    "explain restore previous state without erasing evidence",
    "explain memory in an agent as trace continuity rather than a text summary",
    "why is a conversation summary not the same as agent memory",
    "describe agent memory as state transitions observations decisions and updates",
    "why does context amnesia break recursive agents",
    "design a shape-first retrieval step where no noun match exists but the inverse need is clear",
    "how should retrieval work when keywords fail but the operation is obvious",
    "explain inverse operational fit for search without noun matching",
    "design a verifier for retrieval candidates selected by need rather than label",
    "how can an agent rank candidates by function instead of name",
    "build a retrieval step that rejects keyword-only matches",
    "how should a LoRA adapter train a slot-builder without overwriting the base model",
    "explain why a slot-builder should emit contracts rather than final answers",
    "design a slot-builder critic that scores what a contract does instead of what it says",
    "explain how a NeedSlot protects an agent from noun drift",
    "explain how a contract-aware runtime interface changes model behavior without changing model weights",
    "describe the difference between raw model inference and recursive collapse control",
    "explain why false Ψ is worse than honest Ω in an agent runtime",
    "design a trace-governed collapse gate for an AI agent",
    "explain why payload shaping must not damage the accepted collapse",
    "describe the RHI kernel as a model inside a recursive control field",
]
PROMPTS = PROMPT_BATTERY[:RUN_PROMPT_LIMIT]
print("Prompt count:", len(PROMPTS))
```

## 9. Execute v26

```python
def run_one_prompt(prompt: str) -> PromptResult:
    trace = []
    def log(event_type: str, payload: Dict[str, Any]):
        trace.append({"t": len(trace)+1, "event_type": event_type, "payload": payload})

    slot_candidates, selected_slot, selected_slot_audit, profile_info = build_slot_candidates(prompt)
    seed_audit = next(c["audit"] for c in slot_candidates if c["slot"].origin == "seed_compiler")
    model_scores = [c["audit"].score for c in slot_candidates if c["slot"].origin.startswith("model")]
    model_slot_score = max(model_scores) if model_scores else 0.0
    slot_delta = model_slot_score - seed_audit.score

    log("slot_candidates", {"count": len(slot_candidates), "selected_origin": selected_slot.origin, "selected_score": selected_slot_audit.score, "profile_info": profile_info})

    all_branches = []
    state = "Ω"
    reason = "not_started"
    winner = None
    collapse_meta = {}
    prior_failure = None

    if selected_slot_audit.state != "Ψ":
        log("slot_failed", {"audit": asdict(selected_slot_audit)})
        state = "Ω"
        reason = "slot_builder_residue"
    else:
        for depth in range(MAX_RECURSION_DEPTH + 1):
            branches = run_branches(prompt, selected_slot, depth, prior_failure)
            all_branches.extend(branches)
            for b in branches:
                log("branch", {"depth": depth, "branch": b.branch, "score": b.score, "state": b.state, "reason": b.reason, "preview": b.answer[:180]})
            state, reason, winner, collapse_meta = collapse_answer(all_branches)
            log("collapse", {"depth": depth, "state": state, "reason": reason, "winner": winner.branch if winner else None, "score": winner.score if winner else None, "meta": collapse_meta})
            if state == "Ψ":
                break
            if winner:
                prior_failure = {"reason": reason, "winner_score": winner.score, "audit": winner.audit, "preview": winner.answer[:220]}
            else:
                prior_failure = {"reason": reason, "winner_score": 0.0, "audit": {}, "preview": ""}

    raw_answer = winner.answer if winner else ""
    final_answer = raw_answer
    shaped_answer = None
    shaping_accepted = False
    shaper_meta = {}
    if state == "Ψ" and winner:
        final_answer, shaping_accepted, shaper_meta = shape_payload(prompt, selected_slot, raw_answer, winner.score)
        shaped_answer = final_answer if shaping_accepted else None
        log("payload_shaper", shaper_meta)

    if REQUIRE_MODEL_FOR_PSI and not any(b.origin == "model" and b.answer for b in all_branches) and state == "Ψ":
        state = "Ω"
        reason = "model_origin_required_no_model_output"

    metrics = {
        "branch_count": len(all_branches),
        "psi_branch_count": sum(1 for b in all_branches if b.state == "Ψ"),
        "omega_branch_count": sum(1 for b in all_branches if b.state == "Ω"),
        "exhaust_ratio": sum(1 for b in all_branches if b.state == "Ω") / max(1,len(all_branches)),
        "slot_candidate_count": len(slot_candidates),
        "model_slot_candidate_count": sum(1 for c in slot_candidates if c["slot"].origin.startswith("model")),
        "slot_delta_model_minus_seed": slot_delta,
        "collapse_meta": collapse_meta,
        "shaper_meta": shaper_meta,
    }

    return PromptResult(
        prompt=prompt,
        task_profile=selected_slot.task_profile,
        state=state,
        reason=reason,
        selected_slot_origin=selected_slot.origin,
        seed_slot_score=seed_audit.score,
        model_slot_score=model_slot_score,
        selected_slot_score=selected_slot_audit.score,
        slot_delta_model_minus_seed=slot_delta,
        winner_branch=winner.branch if winner else None,
        winner_score=winner.score if winner else 0.0,
        answer=final_answer,
        raw_winner_answer=raw_answer,
        shaped_answer=shaped_answer,
        shaping_accepted=shaping_accepted,
        slot_candidates=[{"slot": asdict(c["slot"]), "audit": asdict(c["audit"]), "meta": c["meta"]} for c in slot_candidates],
        selected_slot=asdict(selected_slot),
        branches=[asdict(b) for b in all_branches],
        trace=trace,
        metrics=metrics,
    )

if REQUIRE_MODEL_FOR_PSI and not MODEL_GENERATION_READY:
    raise RuntimeError("Model generation is not ready. v26 refuses fallback Ψ.")

RESULTS = []
t0 = time.time()
for i, prompt in enumerate(PROMPTS, start=1):
    print("\n" + "="*100)
    print(f"[{i}/{len(PROMPTS)}] {prompt}")
    print("="*100)
    try:
        result = run_one_prompt(prompt)
    except Exception:
        err = traceback.format_exc()
        seed = seed_slot_compiler(prompt)
        result = PromptResult(
            prompt=prompt,
            task_profile=seed.task_profile,
            state="Ω",
            reason="kernel_exception",
            selected_slot_origin="exception",
            seed_slot_score=0.0,
            model_slot_score=0.0,
            selected_slot_score=0.0,
            slot_delta_model_minus_seed=0.0,
            winner_branch=None,
            winner_score=0.0,
            answer="",
            raw_winner_answer="",
            shaped_answer=None,
            shaping_accepted=False,
            slot_candidates=[],
            selected_slot=asdict(seed),
            branches=[],
            trace=[{"t":1, "event_type":"kernel_exception", "payload":{"error":err}}],
            metrics={"error": err},
        )
    RESULTS.append(result)
    print("STATE:", result.state, "REASON:", result.reason, "PROFILE:", result.task_profile)
    print("SLOT:", result.selected_slot_origin, "seed=", round(result.seed_slot_score,3), "model=", round(result.model_slot_score,3), "selected=", round(result.selected_slot_score,3))
    print("WINNER:", result.winner_branch, round(result.winner_score,3))
    print("ANSWER:", (result.answer or "")[:260].replace("\n", " "))

ELAPSED_SECONDS = time.time() - t0
print("\nDONE", len(RESULTS), "elapsed", ELAPSED_SECONDS)
```

## 10. Save Exactly Two Files

```python
def summarize(results: List[PromptResult]) -> Tuple[Dict[str, Any], pd.DataFrame]:
    rows = []
    sft_rows = []
    for r in results:
        raw_words = len(text_terms(r.raw_winner_answer))
        final_words = len(text_terms(r.answer))
        rows.append({
            "run_id": RUN_ID,
            "prompt": r.prompt,
            "task_profile": r.task_profile,
            "state": r.state,
            "reason": r.reason,
            "selected_slot_origin": r.selected_slot_origin,
            "seed_slot_score": r.seed_slot_score,
            "model_slot_score": r.model_slot_score,
            "selected_slot_score": r.selected_slot_score,
            "slot_delta_model_minus_seed": r.slot_delta_model_minus_seed,
            "winner_branch": r.winner_branch,
            "winner_score": r.winner_score,
            "branch_count": r.metrics.get("branch_count",0),
            "psi_branch_count": r.metrics.get("psi_branch_count",0),
            "omega_branch_count": r.metrics.get("omega_branch_count",0),
            "exhaust_ratio": r.metrics.get("exhaust_ratio",0.0),
            "shaping_accepted": r.shaping_accepted,
            "raw_words": raw_words,
            "final_words": final_words,
            "compression_ratio": 1 - final_words/max(1,raw_words),
            "answer_preview": (r.answer or "")[:260].replace("\n", " "),
        })
        try:
            sft_rows.append(make_sft_row(r.prompt, NeedSlot(**r.selected_slot), selected=(r.state=="Ψ")))
        except Exception:
            pass
    df = pd.DataFrame(rows)
    agg = {
        "run_id": RUN_ID,
        "version": "v26",
        "purpose": "slot_builder_kernel",
        "model_id_or_path": MODEL_ID_OR_PATH,
        "model_ready": MODEL_READY,
        "model_generation_ready": MODEL_GENERATION_READY,
        "model_error": MODEL_ERROR,
        "smoke_text": SMOKE_TEXT,
        "dependency_status": DEPENDENCY_STATUS,
        "device_info": DEVICE_INFO,
        "config": {
            "run_prompt_limit": RUN_PROMPT_LIMIT,
            "max_slot_repair_attempts": MAX_SLOT_REPAIR_ATTEMPTS,
            "max_recursion_depth": MAX_RECURSION_DEPTH,
            "branch_roles": BRANCH_ROLES,
            "slot_selection_mode": SLOT_SELECTION_MODE,
            "require_model_for_psi": REQUIRE_MODEL_FOR_PSI,
        },
        "total_prompts": len(results),
        "psi_count": int((df["state"] == "Ψ").sum()) if len(df) else 0,
        "omega_count": int((df["state"] == "Ω").sum()) if len(df) else 0,
        "psi_ratio": float((df["state"] == "Ψ").mean()) if len(df) else 0.0,
        "omega_ratio": float((df["state"] == "Ω").mean()) if len(df) else 0.0,
        "mean_seed_slot_score": float(df["seed_slot_score"].mean()) if len(df) else 0.0,
        "mean_model_slot_score": float(df["model_slot_score"].mean()) if len(df) else 0.0,
        "mean_selected_slot_score": float(df["selected_slot_score"].mean()) if len(df) else 0.0,
        "mean_slot_delta_model_minus_seed": float(df["slot_delta_model_minus_seed"].mean()) if len(df) else 0.0,
        "model_slot_beats_seed_count": int((df["slot_delta_model_minus_seed"] > 0).sum()) if len(df) else 0,
        "model_slot_beats_seed_ratio": float((df["slot_delta_model_minus_seed"] > 0).mean()) if len(df) else 0.0,
        "selected_model_slot_count": int(df["selected_slot_origin"].str.startswith("model", na=False).sum()) if len(df) else 0,
        "selected_model_slot_ratio": float(df["selected_slot_origin"].str.startswith("model", na=False).mean()) if len(df) else 0.0,
        "mean_winner_score": float(df["winner_score"].mean()) if len(df) else 0.0,
        "mean_exhaust_ratio": float(df["exhaust_ratio"].mean()) if len(df) else 0.0,
        "shaping_accepted_ratio": float(df["shaping_accepted"].mean()) if len(df) else 0.0,
        "mean_compression_ratio": float(df["compression_ratio"].mean()) if len(df) else 0.0,
        "elapsed_seconds": ELAPSED_SECONDS,
        "reason_counts": dict(Counter(df["reason"])) if len(df) else {},
        "profile_metrics": {},
    }
    if len(df):
        for profile, g in df.groupby("task_profile"):
            agg["profile_metrics"][profile] = {
                "count": int(len(g)),
                "psi_count": int((g["state"] == "Ψ").sum()),
                "omega_count": int((g["state"] == "Ω").sum()),
                "psi_ratio": float((g["state"] == "Ψ").mean()),
                "mean_seed_slot_score": float(g["seed_slot_score"].mean()),
                "mean_model_slot_score": float(g["model_slot_score"].mean()),
                "model_slot_beats_seed_ratio": float((g["slot_delta_model_minus_seed"] > 0).mean()),
                "selected_model_slot_ratio": float(g["selected_slot_origin"].str.startswith("model", na=False).mean()),
                "mean_winner_score": float(g["winner_score"].mean()),
                "reason_counts": dict(Counter(g["reason"])),
            }
    return agg, df, sft_rows

aggregate, summary_df, sft_rows = summarize(RESULTS)

bundle = {
    "run_id": RUN_ID,
    "version": "v26",
    "purpose": "slot_builder_kernel",
    "created_root": str(ROOT),
    "out_dir": str(OUT_DIR),
    "aggregate": aggregate,
    "summary": summary_df.to_dict(orient="records"),
    "results": [asdict(r) for r in RESULTS],
    "sft_slot_builder_rows": sft_rows,
    "profile_lexicons": PROFILE_LEXICONS,
    "semantic_locks": SEMANTIC_LOCKS,
    "interpretation_lock": {
        "main_branch": "new AI runtime",
        "core_transition": "Q -> SlotBuilder -> C_Q -> BranchEngine -> OperationalCritic -> Ψ/Ω",
        "not_this": ["H-probing", "raw benchmark detour", "answer-only prompting"],
        "v26_question": "Can the model emit a NeedSlot contract good enough to control downstream answer collapse?",
        "psi_rule": "Ψ requires selected slot fit plus model-origin answer fit",
        "omega_rule": "Ω is preferred over false operational collapse",
    },
}

bundle_out = OUT_DIR / f"{RUN_ID}_bundle.json"
summary_out = OUT_DIR / f"{RUN_ID}_summary.csv"

with open(bundle_out, "w", encoding="utf-8") as f:
    json.dump(bundle, f, indent=2, ensure_ascii=False)
summary_df.to_csv(summary_out, index=False)

print("Saved exactly two output files:")
print(bundle_out)
print(summary_out)
print("\nAggregate preview:")
print(json.dumps(aggregate, indent=2, ensure_ascii=False)[:5000])
display(summary_df)
```

## 11. How to Read v26

The central readout is not just Ψ-rate.

The main question is:

$$
\boxed{\text{Does model-generated }C_Q\text{ compete with or beat the seed slot compiler?}}
$$

Key fields:

- `model_slot_beats_seed_ratio`
- `selected_model_slot_ratio`
- `mean_model_slot_score`
- `mean_seed_slot_score`
- `psi_ratio`
- `reason_counts`
- `profile_metrics`

A strong v26 run shows:

$$
\text{model slot score} \uparrow,
\quad
\text{selected model slot ratio} \uparrow,
\quad
\Psi\text{ stable},
\quad
\Omega\text{ honest where slot or answer fails.}
$$
