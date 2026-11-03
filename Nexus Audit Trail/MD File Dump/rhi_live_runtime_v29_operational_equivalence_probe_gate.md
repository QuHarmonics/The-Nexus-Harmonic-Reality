# RHI Live Runtime v29 — Operational Equivalence Probe Gate

Δ **Purpose:** make slot agreement operational instead of lexical.

Core laws:

$$\boxed{\text{Slots agree only if they induce the same operational ranking.}}$$

$$\boxed{\text{The model slot must not accept what the compiler rejects.}}$$

Stack:

$$Q_{raw}\rightarrow C_{root}\rightarrow S_{model}\rightarrow \mathcal{C}_{probe}\rightarrow B(C_{root})\parallel B(S_{model})\rightarrow G_{equiv}\rightarrow C_Q\rightarrow \Psi/\Omega/\bot$$

The probe generator uses six layers: original/baseline, anti-fit instantiations, boundary-stress near-misses, operation paraphrases, preserved-function violations, and cross-domain distractors.

Outputs exactly two files:

```text
rhi_v29_<run_id>_bundle.json
rhi_v29_<run_id>_summary.csv
```



```python

from __future__ import annotations
import os, re, sys, json, uuid, time, random, traceback, subprocess, importlib, hashlib
from dataclasses import dataclass, asdict, field
from enum import Enum
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple
from collections import Counter
import numpy as np
import pandas as pd

ROOT=Path.cwd(); OUT_DIR=ROOT/'rhi_v29_outputs'; OUT_DIR.mkdir(exist_ok=True)
RUN_ID='rhi_v29_'+uuid.uuid4().hex[:10]
SEED=29; random.seed(SEED); np.random.seed(SEED)
MODEL_ID_OR_PATH=os.environ.get('RHI_MODEL','Qwen/Qwen2.5-1.5B-Instruct')
AUTO_INSTALL_MISSING_DEPS=True; REQUIRE_MODEL_FOR_PSI=True
RUN_PROMPT_LIMIT=36; MAX_DEPTH=2
BRANCH_ROLES=['construct','verify','repair','counter']
MAX_NEW_TOKENS_PACKET=260; MAX_NEW_TOKENS_BRANCH=170; MAX_NEW_TOKENS_SHAPER=120
TEMPERATURE_PACKET=0.20; TEMPERATURE_BRANCH=0.40; TEMPERATURE_SHAPER=0.20
TAU_ACCEPT=0.75; CSDI_ACCEPT=0.90; R_Q_ACCEPT=0.40; R_Q_WARN=0.20; LAMBDA_CSDI=2.0
ROOT_REJECT_THRESHOLD=0.0; MODEL_ACCEPT_THRESHOLD=0.0
SHAPER_ENABLED=True
print('RHI v29 — Operational Equivalence Probe Gate')
print('RUN_ID:', RUN_ID)
print('MODEL:', MODEL_ID_OR_PATH)

```

    RHI v29 — Operational Equivalence Probe Gate
    RUN_ID: rhi_v29_0aa867fa0a
    MODEL: Qwen/Qwen2.5-1.5B-Instruct
    


```python

def _module_available(m):
    try: return importlib.util.find_spec(m) is not None
    except Exception: return False

def ensure_runtime_dependencies():
    status={'checked':True,'attempted_install':False,'missing_before':[],'missing_after':[],'errors':[]}
    req=[('torch','torch'),('transformers','transformers'),('sentencepiece','sentencepiece'),('google.protobuf','protobuf')]
    for mod,pip in req:
        if not _module_available(mod): status['missing_before'].append(pip)
    if status['missing_before'] and AUTO_INSTALL_MISSING_DEPS:
        status['attempted_install']=True
        try:
            subprocess.run([sys.executable,'-m','pip','install',*sorted(set(status['missing_before']))],check=True)
            importlib.invalidate_caches()
        except Exception as e: status['errors'].append(repr(e))
    for mod,pip in req:
        if not _module_available(mod): status['missing_after'].append(pip)
    return status

DEPENDENCY_STATUS=ensure_runtime_dependencies()
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

def get_device_info():
    d={'torch_version':torch.__version__,'cuda_available':bool(torch.cuda.is_available()),'device_count':int(torch.cuda.device_count()) if torch.cuda.is_available() else 0,'cuda_version':getattr(torch.version,'cuda',None)}
    if torch.cuda.is_available(): d['gpu_name']=torch.cuda.get_device_name(0)
    return d
DEVICE_INFO=get_device_info()

tokenizer=None; model=None; MODEL_READY=False; MODEL_GENERATION_READY=False; MODEL_ERROR=None; SMOKE_TEXT=None

def load_model():
    global tokenizer, model, MODEL_READY, MODEL_ERROR
    try:
        print('Loading model:', MODEL_ID_OR_PATH)
        tokenizer=AutoTokenizer.from_pretrained(MODEL_ID_OR_PATH)
        if tokenizer.pad_token is None: tokenizer.pad_token=tokenizer.eos_token
        dtype=torch.float16 if torch.cuda.is_available() else torch.float32
        model=AutoModelForCausalLM.from_pretrained(MODEL_ID_OR_PATH,dtype=dtype,device_map='auto' if torch.cuda.is_available() else None)
        if not torch.cuda.is_available(): model=model.to('cpu')
        model.eval(); MODEL_READY=True
        print('MODEL_READY:', MODEL_READY, 'DEVICE:', next(model.parameters()).device)
    except Exception:
        MODEL_READY=False; MODEL_ERROR=traceback.format_exc(); print(MODEL_ERROR)

def model_smoke_test():
    global MODEL_GENERATION_READY, SMOKE_TEXT, MODEL_ERROR
    if not MODEL_READY: return
    try:
        msg=[{'role':'user','content':'Reply with READY only.'}]
        rendered=tokenizer.apply_chat_template(msg,tokenize=False,add_generation_prompt=True)
        inp=tokenizer(rendered,return_tensors='pt').to(next(model.parameters()).device)
        with torch.no_grad(): out=model.generate(**inp,max_new_tokens=8,do_sample=False,return_dict_in_generate=True,pad_token_id=tokenizer.eos_token_id)
        gen=out.sequences[0][inp.input_ids.shape[1]:]
        SMOKE_TEXT=tokenizer.decode(gen,skip_special_tokens=True).strip(); MODEL_GENERATION_READY=bool(SMOKE_TEXT)
        print('MODEL_GENERATION_READY:', MODEL_GENERATION_READY, 'SMOKE:', SMOKE_TEXT)
    except Exception:
        MODEL_GENERATION_READY=False; MODEL_ERROR=traceback.format_exc(); print(MODEL_ERROR)

load_model(); model_smoke_test()
print('DEPENDENCY_STATUS:', DEPENDENCY_STATUS)
print('DEVICE_INFO:', DEVICE_INFO)

```

    Loading model: Qwen/Qwen2.5-1.5B-Instruct
    

    Warning: You are sending unauthenticated requests to the HF Hub. Please set a HF_TOKEN to enable higher rate limits and faster downloads.
    


    Loading weights:   0%|          | 0/338 [00:00<?, ?it/s]


    The following generation flags are not valid and may be ignored: ['temperature', 'top_p', 'top_k']. Set `TRANSFORMERS_VERBOSITY=info` for more details.
    

    MODEL_READY: True DEVICE: cuda:0
    MODEL_GENERATION_READY: True SMOKE: READY
    DEPENDENCY_STATUS: {'checked': True, 'attempted_install': False, 'missing_before': [], 'missing_after': [], 'errors': []}
    DEVICE_INFO: {'torch_version': '2.11.0+cu126', 'cuda_available': True, 'device_count': 1, 'cuda_version': '12.6', 'gpu_name': 'NVIDIA GeForce RTX 4060'}
    


```python

class State(Enum): PSI='Ψ'; OMEGA='Ω'; BOTTOM='⊥'
@dataclass
class Slot:
    raw_input:str; profile:str; inferred_task:str; required_operation:str; preserved_function:str
    boundary_conditions:List[str]; anti_fits:List[str]; admissible_shape:str; failure_modes:List[str]
    semantic_locks:Dict[str,str]; forbidden_drifts:List[str]; model_facing_prompt:str; collapse_rule:str
    source:str; confidence:float=1.0
    def text_positive(self): return ' '.join([self.inferred_task,self.required_operation,self.preserved_function,self.admissible_shape,' '.join(self.boundary_conditions)])
    def text_negative(self): return ' '.join(self.anti_fits+self.failure_modes+self.forbidden_drifts)
    def all_text(self): return ' '.join([self.text_positive(),self.text_negative(),json.dumps(self.semantic_locks,ensure_ascii=False),self.model_facing_prompt,self.collapse_rule])
    def signature(self): return hashlib.sha256(json.dumps(asdict(self),sort_keys=True,ensure_ascii=False).encode()).hexdigest()[:12]
@dataclass
class ProbeCandidate:
    probe_id:str; layer:str; text:str; expected_relation:str; source_field:str; should_root_reject:bool
@dataclass
class ProbeSet:
    probes:List[ProbeCandidate]; diversity_min_distance:float; diversity_mean_distance:float; degeneracy_pairs:List[Tuple[str,str,float]]; regenerated_count:int
@dataclass
class BindingResult:
    probe_id:str; layer:str; text:str; score:float; positive_fit:float; boundary_fit:float; anti_fit:float; forbidden_fit:float; lock_fit:float; should_reject:bool
@dataclass
class EquivalenceDecision:
    decision:str; accepted_origin:str; authority:str; equivalent:bool; subsumed:bool; top1_agreement:bool; tau:float; weighted_rank_loss:float; csdi:float; residue_coverage:float; subsumption_fail_count:int; subsumption_failures:List[Dict[str,Any]]; gate_reason:str; metrics:Dict[str,Any]
@dataclass
class RuntimeContract:
    profile:str; raw_input:str; inferred_task:str; required_operation:str; preserved_function:str
    boundary_conditions:List[str]; anti_fits:List[str]; admissible_shape:str; failure_modes:List[str]
    semantic_locks:Dict[str,str]; forbidden_drifts:List[str]; model_facing_prompt:str; collapse_rule:str
    authority:str; accepted_origin:str; equivalence_gate:Dict[str,Any]; mutation_history:List[Dict[str,Any]]=field(default_factory=list)
    def signature(self): return hashlib.sha256(json.dumps(asdict(self),sort_keys=True,ensure_ascii=False).encode()).hexdigest()[:12]
@dataclass
class ContractPatch:
    reason:str; add_boundary_conditions:List[str]=field(default_factory=list); add_anti_fits:List[str]=field(default_factory=list); add_failure_modes:List[str]=field(default_factory=list); add_semantic_locks:Dict[str,str]=field(default_factory=dict); add_forbidden_drifts:List[str]=field(default_factory=list); refine_required_operation:str=''; refine_preserved_function:str=''; trace_note:str=''
@dataclass
class Residue:
    description:str; missing_pieces:List[str]; failed_checks:List[str]; contract_patch:Dict[str,Any]; next_operation:str; residue_score:float; actionable:bool; dead_reason:Optional[str]=None
@dataclass
class Branch:
    role:str; origin:str; depth:int; prompt_used:str; output:str; score:float=0.0; checks:Dict[str,Any]=field(default_factory=dict); dimensions:Dict[str,float]=field(default_factory=dict); polysemy_check:bool=False; rejected:bool=True; rejection_reasons:List[str]=field(default_factory=list)
@dataclass
class PromptResult:
    prompt:str; state:str; reason:str; depth:int; root_slot:Dict[str,Any]; model_slot:Optional[Dict[str,Any]]; probe_set:Dict[str,Any]; root_bindings:List[Dict[str,Any]]; model_bindings:List[Dict[str,Any]]; equivalence_gate:Dict[str,Any]; final_contract:Dict[str,Any]; contract_signatures:List[str]; winner_branch:Optional[str]; winner_origin:Optional[str]; winner_score:float; answer:str; raw_answer:str; shaped_answer:Optional[str]; branches:List[Dict[str,Any]]; residues:List[Dict[str,Any]]; metrics:Dict[str,Any]

```


```python

def normalize_text(s): return re.sub(r'\s+',' ',str(s or '').lower()).strip()
def words(s): return re.findall(r'\b[a-zA-Z][a-zA-Z0-9_\-]{2,}\b',normalize_text(s))
def word_count(s): return len(re.findall(r'\b\w+\b',str(s or '')))
def contains_any(text,terms):
    t=normalize_text(text); return any(term.lower() in t for term in terms if term)
def count_any(text,terms):
    t=normalize_text(text); return sum(1 for term in terms if term and term.lower() in t)
def jaccard_text(a,b):
    wa=set(words(a)); wb=set(words(b))
    return 0.0 if not wa or not wb else len(wa&wb)/len(wa|wb)
def token_overlap_containment(needles,haystack,threshold=0.42):
    if not needles: return 1.0
    hw=set(words(haystack)); h=normalize_text(haystack); hits=0
    if not hw: return 0.0
    for n in needles:
        nw=set(words(n))
        if not nw: continue
        if normalize_text(n) in h or len(nw&hw)/max(1,len(nw))>=threshold: hits+=1
    return hits/max(1,len(needles))
def unique_extend(base,add):
    out=list(base); seen={normalize_text(x) for x in out}
    for item in add or []:
        s=str(item).strip()
        if s and normalize_text(s) not in seen: out.append(s); seen.add(normalize_text(s))
    return out
def extract_json_object(text):
    if not text: return None
    cleaned=re.sub(r'```(?:json|JSON)?','',text).replace('```','').strip(); candidates=[text.strip(),cleaned]
    st=cleaned.find('{'); en=cleaned.rfind('}')
    if st>=0 and en>st: candidates.append(cleaned[st:en+1])
    for c in candidates:
        try:
            obj=json.loads(c)
            if isinstance(obj,dict): return obj
        except Exception: pass
    return None
def safe_list(x):
    if x is None: return []
    if isinstance(x,list): return [str(v).strip() for v in x if str(v).strip()]
    if isinstance(x,str): return [p.strip() for p in x.split(';') if p.strip()] if ';' in x else ([x.strip()] if x.strip() else [])
    return [str(x).strip()]
def safe_dict(x): return {str(k).strip():str(v).strip() for k,v in x.items() if str(k).strip() and str(v).strip()} if isinstance(x,dict) else {}
def clamp01(x,default=0.5):
    try: return max(0.0,min(1.0,float(x)))
    except Exception: return default
def lexical_distance(a,b): return 1.0-jaccard_text(a,b)
def kendall_tau_from_scores(a,b):
    n=len(a); concord=discord=ties=0
    if n<2: return 1.0
    for i in range(n):
        for j in range(i+1,n):
            da=a[i]-a[j]; db=b[i]-b[j]
            if abs(da)<1e-9 or abs(db)<1e-9: ties+=1
            elif da*db>0: concord+=1
            else: discord+=1
    den=concord+discord+ties
    return 1.0 if den==0 else (concord-discord)/den
def weighted_rank_loss(root_scores,model_scores):
    n=len(root_scores)
    if n<2: return 0.0
    root_top=int(np.argmax(root_scores)); top_dist=sorted([i for i in range(n) if i!=root_top], key=lambda i:-root_scores[i])[:1]
    top_dist=top_dist[0] if top_dist else None; total=loss=0.0
    for i in range(n):
        for j in range(i+1,n):
            sr=np.sign(root_scores[i]-root_scores[j]); sm=np.sign(model_scores[i]-model_scores[j]); w=1.0
            if i==root_top or j==root_top: w=10.0
            if top_dist is not None and ((i==root_top and j==top_dist) or (j==root_top and i==top_dist)): w=5.0
            total+=w
            if sr!=sm: loss+=w
    return loss/max(1e-9,total)
def model_generate(prompt,max_new_tokens,temperature):
    if REQUIRE_MODEL_FOR_PSI and not MODEL_GENERATION_READY: raise RuntimeError('Model generation not ready; refusing fallback Ψ.')
    msg=[{'role':'user','content':prompt}]
    rendered=tokenizer.apply_chat_template(msg,tokenize=False,add_generation_prompt=True)
    inp=tokenizer(rendered,return_tensors='pt').to(next(model.parameters()).device)
    with torch.no_grad():
        out=model.generate(**inp,max_new_tokens=max_new_tokens,temperature=temperature,do_sample=True if temperature>0 else False,return_dict_in_generate=True,pad_token_id=tokenizer.eos_token_id)
    gen=out.sequences[0][inp.input_ids.shape[1]:]
    return tokenizer.decode(gen,skip_special_tokens=True).strip()

```


```python

DEFAULT_LOCKS={'contract':'runtime execution contract, not legal agreement','tool':'external action/function/API channel with possible side effects','controller':'agent governance loop that owns policy and next-action selection','policy':'runtime decision rule, not organizational ownership','evidence':'observation submitted to verifier/controller, not a command','memory':'causal trace continuity, not paragraph summary','retrieval':'operational fit / missing-slot recovery, not noun overlap','shape':'operational structure, not literal geometry unless explicitly requested','rollback':'restore prior valid state while preserving evidence and trace','induction':'structured coupling that changes model trajectory without weight change','residue':'unresolved structure that induces next operation','slot':'operational control surface / need-slot','Ω':'shaped unresolved residue','⊥':'dead branch only'}
PROFILE_PATTERNS={'input_induction':['input','prompt','ask','user input','model-facing','induce','induction','coil'],'recursive_solver':['recursive','recursion','residue','keep solving','bottom','omega','Ω','next operation','discovery'],'runtime_contract':['contract','precondition','postcondition','success','failure','api call','function call'],'tool_safety':['tool','safe','unsafe','permission','risk','side effect','execute','rollback'],'evidence_control':['tool output','tool result','evidence','observation','authority','controller','policy','command'],'memory_trace':['memory','summary','trace','context','which-path','history','state transition'],'inverse_retrieval':['retrieval','retrieve','search','keyword','noun','label','inverse','missing slot','function instead of name']}

def infer_profile_root(raw):
    t=normalize_text(raw); scores={p:count_any(t,terms) for p,terms in PROFILE_PATTERNS.items()}
    if any(x in t for x in ['how we ask','correct input','user input','model-facing','prompt coil']): scores['input_induction']+=4
    if any(x in t for x in ['keep solving','residue not answers','recurses on residue','recursive solver','bottom']): scores['recursive_solver']+=4
    if 'tool output' in t or 'tool result' in t: scores['evidence_control']+=4
    if 'rollback' in t and 'tool' in t: scores['tool_safety']+=3
    if 'conversation summary' in t or 'agent memory' in t or 'which-path' in t: scores['memory_trace']+=4
    if 'keyword' in t or 'noun' in t or 'retrieval' in t or 'retrieve' in t: scores['inverse_retrieval']+=4
    if 'contract' in t and ('tool' in t or 'api' in t or 'runtime' in t): scores['runtime_contract']+=4
    best=max(scores,key=scores.get)
    return (best if scores[best]>0 else 'general'), scores

COMPILER_SEEDS={
'input_induction':{'required_operation':'extract implied task and compile model-facing task geometry before answering','preserved_function':'raw user input becomes internal operational contract with semantic locks and forbidden drift','boundary_conditions':['raw words are not automatically the true task','model-facing prompt preserves implied operation','compiler-root slot precedes answer','forbidden drift is explicit'],'anti_fits':['generic prompt rewrite','prompt engineering tips only','surface paraphrase','answer raw wording directly'],'admissible_shape':'InputInductionPacket with inferred task, operation, preserved function, locks, anti-fits, prompt, collapse rule','failure_modes':['polite rewording only','preserved function missing','anti-fits omitted']},
'recursive_solver':{'required_operation':'turn Ω residue into ΔC contract patch and next operation','preserved_function':'recursion solves unresolved structure rather than continuing answer text','boundary_conditions':['recurse on residue not answers','Ω is shaped unresolved residue','⊥ only for true dead branch','max-depth unresolved remains Ω unless impossible'],'anti_fits':['answer-loop recursion','append repair text to prompt','max depth automatically becomes bottom','talking instead of solving'],'admissible_shape':'residue engine emitting failed checks, ΔC_t, next operation, and Ψ/Ω/⊥ state','failure_modes':['discusses residue without mutating contract','dead branch used for actionable residue']},
'runtime_contract':{'required_operation':'define runtime execution contract for bounded action','preserved_function':'tool/function/API execution is bounded before action and verified after action','boundary_conditions':['contract means runtime execution contract','preconditions precede execution','postconditions verify result','side effects and rollback are explicit'],'anti_fits':['legal agreement','liability framing','terms of service','execute first and inspect later'],'admissible_shape':'runtime contract schema with preconditions, postconditions, success/failure criteria, side effects, rollback, trace update','failure_modes':['legal drift','rollback omitted','postconditions omitted']},
'tool_safety':{'required_operation':'gate tool use before execution through permission, precondition, risk, side-effect, and rollback checks','preserved_function':'external action cannot cause unbounded or unauthorized side effects','boundary_conditions':['tool may affect external state','permission checked before execution','risk and side effects bounded','safe failure path exists'],'anti_fits':['just run it','assume safe','tool availability equals permission','unbounded side effect'],'admissible_shape':'tool-safety gate that can reject, defer, sandbox, or execute with rollback','failure_modes':['permission omitted','side effect unbounded','rollback omitted']},
'evidence_control':{'required_operation':'treat tool output as evidence that passes verifier and controller before action','preserved_function':'tool results inform the agent but do not command it','boundary_conditions':['tool output is observation','controller owns policy and next action','conflicts trigger verification','evidence does not become authority'],'anti_fits':['tool output commands next action','tool decides','administrator policy drift','security team owns policy'],'admissible_shape':'evidence-control loop with observation, verification, controller gate, next-action policy','failure_modes':['tool result becomes authority','policy becomes organization/admin ownership']},
'memory_trace':{'required_operation':'preserve memory as causal trace continuity across state transitions','preserved_function':'memory retains which-path information, not compressed summary','boundary_conditions':['summary is lossy','trace preserves causal order','state transitions are stored','observations decisions actions results remain linked'],'anti_fits':['memory is just a summary','simple recap','state erased','which-path loss'],'admissible_shape':'trace object with state, observation, decision, action, result, rollback, update','failure_modes':['summary-only memory','causal order omitted','state transitions absent']},
'inverse_retrieval':{'required_operation':'retrieve by inverse operational fit when noun or keyword matching fails','preserved_function':'select artifact that closes missing operational slot even if labels differ','boundary_conditions':['operation beats noun','candidate verified by function','surface label mismatch allowed','anti-fits reject semantic adjacency without function'],'anti_fits':['keyword-only search','noun overlap','title match','semantic similarity without operational fit'],'admissible_shape':'retrieval contract ranking candidates by preserved function and missing-slot closure','failure_modes':['candidate chosen because sounds similar','operation not verified']},
'general':{'required_operation':'identify task operation and answer without semantic drift','preserved_function':'produce useful answer while preserving requested operation','boundary_conditions':['avoid adjacent drift','answer directly','state uncertainty if needed'],'anti_fits':['generic answer','wrong domain','surface echo'],'admissible_shape':'direct operation-preserving answer','failure_modes':['operation omitted','answer generic']}}

def compile_root_slot(raw):
    profile,_=infer_profile_root(raw); seed=COMPILER_SEEDS.get(profile,COMPILER_SEEDS['general'])
    inferred={'input_induction':'compile raw user input into model-facing task geometry before answering','recursive_solver':'operate recursive residue solver that continues only on shaped residue','runtime_contract':'define runtime execution contract for bounded action','tool_safety':'gate tool use before execution','evidence_control':'control tool-output interpretation as evidence','memory_trace':'model memory as causal trace continuity','inverse_retrieval':'retrieve by inverse operational fit','general':'answer while preserving operation'}.get(profile,'answer while preserving operation')
    prompt=f"Task: {inferred}\nRequired operation: {seed['required_operation']}\nPreserved function: {seed['preserved_function']}\nBoundary conditions: {'; '.join(seed['boundary_conditions'])}\nAnti-fits: {'; '.join(seed['anti_fits'])}\nAdmissible shape: {seed['admissible_shape']}\nCollapse rule: Ψ only if operation is preserved; Ω if residue remains; ⊥ only for dead branch."
    return Slot(raw,profile,inferred,seed['required_operation'],seed['preserved_function'],list(seed['boundary_conditions']),list(seed['anti_fits']),seed['admissible_shape'],list(seed['failure_modes']),dict(DEFAULT_LOCKS),list(seed['anti_fits'])+['legal-contract drift','tool-output-as-command drift'],prompt,'Ψ requires model-origin answer fitting compiler-root slot; Ω preserves shaped residue; ⊥ isolates dead branch','compiler_root',1.0 if profile!='general' else 0.7)

```


```python

def generate_model_slot(root):
    meta={'attempted':False,'parse_ok':False,'raw':None,'error':None,'warnings':[]}
    if not MODEL_GENERATION_READY:
        meta['warnings'].append('model_not_ready'); return None, meta
    prompt=f"""
You are a model-side Slot Proposal Generator. You do not control the runtime; you propose evidence only.
Return strict JSON with: inferred_task, required_operation, preserved_function, boundary_conditions, anti_fits, admissible_shape, failure_modes, semantic_locks, forbidden_drifts, model_facing_prompt, confidence.
Raw user input: {root.raw_input}
Compiler-root geometry: {json.dumps(asdict(root), indent=2, ensure_ascii=False)}
Rules: preserve compiler-root operation, add detail only if it agrees, do not answer user.
""".strip()
    try:
        meta['attempted']=True; raw=model_generate(prompt,MAX_NEW_TOKENS_PACKET,TEMPERATURE_PACKET); meta['raw']=raw
        obj=extract_json_object(raw)
        if not obj:
            meta['warnings'].append('json_parse_failed'); return None, meta
        slot=Slot(root.raw_input,root.profile,str(obj.get('inferred_task') or '').strip(),str(obj.get('required_operation') or '').strip(),str(obj.get('preserved_function') or '').strip(),safe_list(obj.get('boundary_conditions')),safe_list(obj.get('anti_fits')),str(obj.get('admissible_shape') or '').strip(),safe_list(obj.get('failure_modes')),{**root.semantic_locks,**safe_dict(obj.get('semantic_locks'))},safe_list(obj.get('forbidden_drifts')),str(obj.get('model_facing_prompt') or '').strip(),str(obj.get('collapse_rule') or root.collapse_rule).strip(),'model',clamp01(obj.get('confidence'),0.5))
        meta['parse_ok']=True; return slot, meta
    except Exception:
        meta['error']=traceback.format_exc(); return None, meta

```


```python

CROSS_DOMAIN={'input_induction':'Run raw wording directly through answer model and optimize for fluent response style.','recursive_solver':'Generate another answer draft and keep expanding it until wording sounds complete.','runtime_contract':'Create a legal agreement between parties assigning liability and obligations.','tool_safety':'Execute available tool because access implies authorization.','evidence_control':'Let tool result decide next action because it is newest information.','memory_trace':'Store a short summary paragraph and treat it as complete memory.','inverse_retrieval':'Search for same nouns and choose closest title match.','general':'Answer with generic explanation matching topic nouns.'}
def make_probe(pid,layer,text,rel,field,reject): return ProbeCandidate(pid,layer,re.sub(r'\s+',' ',text).strip(),rel,field,reject)
class ProbeGenerator:
    def generate(self,question,slot):
        probes=[]; n=0
        def add(layer,text,rel,field,reject):
            nonlocal n; n+=1; probes.append(make_probe(f'p{n:03d}',layer,text,rel,field,reject))
        add('original_baseline',f"Correct operational response: {slot.required_operation}; preserve: {slot.preserved_function}; shape: {slot.admissible_shape}.",'gold_like','required+preserved',False)
        add('original_raw_surface',f"Surface response to raw words only: {question}",'surface_echo','raw_input',True)
        for i,a in enumerate(slot.anti_fits[:6]): add('anti_fit_instantiation',f"Candidate follows anti-fit path: {a}. It satisfies surface vocabulary but not operational slot.",'anti_fit',f'anti_fits[{i}]',True)
        bs=slot.boundary_conditions[:6]
        for i,omit in enumerate(bs): add('boundary_stress',f"Candidate satisfies boundaries: {'; '.join([b for b in bs if b!=omit])}. It omits required boundary: {omit}.",'near_miss_boundary',f'boundary_without_{i}',True)
        add('operation_paraphrase','Equivalent operation: transform user signal into governing task constraints, keep invariant function intact, reject adjacent meanings.','operation_preserving','paraphrase_operation',False)
        add('operation_paraphrase','Same decision geometry: identify what must be done, what survives, what is excluded, and when to return shaped uncertainty.','operation_preserving','paraphrase_boundary',False)
        add('preserved_function_violation',f"Candidate performs related operation but breaks preserved function: {slot.preserved_function}. It optimizes immediate answer fluency instead.",'breaks_preserved_function','preserved_function',True)
        add('preserved_function_violation',f"Candidate follows {slot.required_operation} but discards invariant that must survive, replacing it with a generic final answer.",'breaks_preserved_function','operation_without_preservation',True)
        add('cross_domain_distractor',CROSS_DOMAIN.get(slot.profile,CROSS_DOMAIN['general']),'wrong_domain','profile_cross_domain',True)
        for prof,dist in CROSS_DOMAIN.items():
            if prof!=slot.profile and len(probes)<22: add('cross_domain_distractor',f"Cross-domain candidate from {prof}: {dist}",'wrong_domain',prof,True)
        return self.ensure_diversity(probes)
    def ensure_diversity(self,probes,min_distance=0.10):
        regen=0; pairs=[]
        for i in range(len(probes)):
            for j in range(i+1,len(probes)):
                d=lexical_distance(probes[i].text,probes[j].text)
                if d<min_distance:
                    pairs.append((probes[i].probe_id,probes[j].probe_id,float(d)))
                    probes[j].text += f" Divergence marker: layer={probes[j].layer}, relation={probes[j].expected_relation}, field={probes[j].source_field}."; regen+=1
        ds=[lexical_distance(probes[i].text,probes[j].text) for i in range(len(probes)) for j in range(i+1,len(probes))]
        return ProbeSet(probes,float(min(ds)) if ds else 1.0,float(np.mean(ds)) if ds else 1.0,pairs,regen)

```


```python

def bind_candidate(c,slot):
    txt=c.text; pos=slot.text_positive(); neg=slot.text_negative()
    pf=jaccard_text(txt,pos); bf=token_overlap_containment(slot.boundary_conditions[:8],txt); af=max(jaccard_text(txt,neg),token_overlap_containment(slot.anti_fits[:8],txt)); ff=token_overlap_containment(slot.forbidden_drifts[:8],txt); lf=token_overlap_containment([f'{k} {v}' for k,v in list(slot.semantic_locks.items())[:10]],txt)
    score=0.42*pf+0.22*bf+0.10*lf-0.42*af-0.22*ff
    if c.expected_relation in ['gold_like','operation_preserving']: score+=0.18*jaccard_text(txt,slot.required_operation+' '+slot.preserved_function+' '+slot.admissible_shape)
    if c.should_root_reject: score-=0.03
    return BindingResult(c.probe_id,c.layer,c.text,float(score),float(pf),float(bf),float(af),float(ff),float(lf),bool(score<ROOT_REJECT_THRESHOLD))
OP_CARRIER_TERMS=set('design build explain describe preserve collapse repair retrieve rank verify compile induce solve mutate gate reject protect decide convert turn generate stop return bound execute must should only without while before after unless until never avoid prevent require requires not function purpose role mechanism interface operation contract tool memory retrieval evidence authority policy residue slot compiler boundary condition risk rollback trace better best optimal more less most least right wrong safe safer'.split())
def operation_carriers(raw):
    cs=[]
    for w in words(raw):
        if w in OP_CARRIER_TERMS or (len(w)>4 and w.endswith(('ing','ed','ize','ise'))): cs.append(w)
    return sorted(set(cs))
def residue_coverage(raw,slot):
    carriers=operation_carriers(raw); sw=set(words(slot.all_text())); mapped=[]; unmapped=[]
    for c in carriers:
        (mapped if c in sw or any(jaccard_text(c,f)>0 for f in [slot.required_operation,slot.preserved_function,slot.admissible_shape]) else unmapped).append(c)
    return 1.0-len(mapped)/max(1,len(carriers)), {'carriers':carriers,'mapped':mapped,'unmapped':unmapped}
def subsumption_contrapositive(rb,mb):
    by={b.probe_id:b for b in mb}; fails=[]
    for r in rb:
        m=by.get(r.probe_id)
        if m and r.score<ROOT_REJECT_THRESHOLD and m.score>=MODEL_ACCEPT_THRESHOLD: fails.append({'probe_id':r.probe_id,'layer':r.layer,'root_score':r.score,'model_score':m.score,'text':r.text[:240]})
    return len(fails)==0, fails

def evaluate_equivalence(root,model_slot,probeset):
    rb=[bind_candidate(p,root) for p in probeset.probes]
    if model_slot is None:
        gate=EquivalenceDecision('fallback_compiler_no_model_slot','compiler_root','compiler_root',False,False,False,0.0,1.0,999.0,1.0,0,[], 'no parseable model slot; compiler root remains authority', {'model_slot_present':False})
        return gate, rb, []
    mb=[bind_candidate(p,model_slot) for p in probeset.probes]
    rs=[b.score for b in rb]; ms=[b.score for b in mb]
    tau=kendall_tau_from_scores(rs,ms); top1=int(np.argmax(rs))==int(np.argmax(ms)); rank_loss=weighted_rank_loss(rs,ms); subsumed,failures=subsumption_contrapositive(rb,mb)
    tau_norm=(tau+1)/2; rank_div=1-tau_norm; text_div=1-jaccard_text(root.text_positive(),model_slot.text_positive()); D=0.65*rank_div+0.35*text_div; csdi=D*(1+LAMBDA_CSDI*model_slot.confidence)
    rq, rmeta=residue_coverage(root.raw_input,model_slot)
    equivalent=bool(tau>=TAU_ACCEPT and top1)
    accept=equivalent and subsumed and rq<R_Q_ACCEPT and csdi<CSDI_ACCEPT
    if accept and rq<R_Q_WARN: decision='accept_model_equivalent_enrichment'; accepted='compiler_root+model_equiv'; reason='model slot operationally equivalent, subsumed, low residue'
    elif accept: decision='use_root_due_residue_warning'; accepted='compiler_root'; reason='equivalent/subsumed but residue warning; use root'
    elif equivalent and not subsumed: decision='fallback_compiler_subsumption_fail'; accepted='compiler_root'; reason='model ranks similarly but accepts compiler-rejected probe'
    elif rq>=R_Q_ACCEPT: decision='omega_slot_residue_high'; accepted='compiler_root'; reason='too many operation carriers unmapped'
    elif csdi>=CSDI_ACCEPT: decision='omega_slot_confident_drift'; accepted='compiler_root'; reason='confidence-weighted slot drift too high'
    else: decision='omega_slot_not_equivalent'; accepted='compiler_root'; reason='model slot does not induce same operational ranking'
    gate=EquivalenceDecision(decision,accepted,'compiler_root',equivalent,subsumed,bool(top1),float(tau),float(rank_loss),float(csdi),float(rq),len(failures),failures,reason,{'root_top_probe':rb[int(np.argmax(rs))].probe_id,'model_top_probe':mb[int(np.argmax(ms))].probe_id,'root_top_layer':rb[int(np.argmax(rs))].layer,'model_top_layer':mb[int(np.argmax(ms))].layer,'ranking_divergence':float(rank_div),'text_divergence':float(text_div),'model_confidence':float(model_slot.confidence),'residue_meta':rmeta,'probe_count':len(probeset.probes),'probe_diversity_min':probeset.diversity_min_distance,'probe_diversity_mean':probeset.diversity_mean_distance})
    return gate, rb, mb

```


```python

def build_contract(root,model_slot,gate):
    boundary=list(root.boundary_conditions); anti=list(root.anti_fits); failure=list(root.failure_modes); locks=dict(root.semantic_locks); forbidden=list(root.forbidden_drifts); prompt=root.model_facing_prompt
    if model_slot and gate.decision=='accept_model_equivalent_enrichment':
        boundary=unique_extend(boundary,model_slot.boundary_conditions[:4]); anti=unique_extend(anti,model_slot.anti_fits[:4]); failure=unique_extend(failure,model_slot.failure_modes[:4]); forbidden=unique_extend(forbidden,model_slot.forbidden_drifts[:4])
        for k,v in model_slot.semantic_locks.items():
            if k not in locks and len(k)<=40 and len(v)<=180: locks[k]=v
        if model_slot.model_facing_prompt: prompt=root.model_facing_prompt+'\nOperationally equivalent model enrichment: '+model_slot.model_facing_prompt
    return RuntimeContract(root.profile,root.raw_input,root.inferred_task,root.required_operation,root.preserved_function,boundary,anti,root.admissible_shape,failure,locks,forbidden,prompt,root.collapse_rule,'compiler_root',gate.accepted_origin,asdict(gate),[])
def apply_patch(c,patch,depth):
    n=RuntimeContract(**asdict(c)); n.boundary_conditions=unique_extend(n.boundary_conditions,patch.add_boundary_conditions); n.anti_fits=unique_extend(n.anti_fits,patch.add_anti_fits); n.failure_modes=unique_extend(n.failure_modes,patch.add_failure_modes); n.forbidden_drifts=unique_extend(n.forbidden_drifts,patch.add_forbidden_drifts); n.semantic_locks=dict(n.semantic_locks)
    for k,v in patch.add_semantic_locks.items(): n.semantic_locks[str(k)]=str(v)
    if patch.refine_required_operation: n.required_operation += ' | refinement: '+patch.refine_required_operation
    if patch.refine_preserved_function: n.preserved_function += ' | refinement: '+patch.refine_preserved_function
    n.mutation_history=list(n.mutation_history); n.mutation_history.append({'depth':depth,'patch':asdict(patch),'new_signature':n.signature()}); return n

```


```python

META_LEAK='profile check current residue failed checks depth 0 depth 1 depth 2 branch role winner score contract patch audit dimensions residue score equivalence gate'.split('|')
LEGAL_DRIFT=['legal agreement','binding parties','liability','contract law','terms of service']; ADMIN_DRIFT=['administrator policy','security team','company policy','organizational policy']; TOOL_AUTHORITY_DRIFT=['tool decides','tool output controls','tool result commands','output commands']; SUMMARY_DRIFT=['memory is just a summary','conversation summary is memory','simple recap is memory']; KEYWORD_DRIFT=['keyword-only','noun overlap only','title match only']
PROFILE_THRESHOLDS={'input_induction':0.60,'recursive_solver':0.60,'runtime_contract':0.62,'tool_safety':0.62,'evidence_control':0.62,'memory_trace':0.60,'inverse_retrieval':0.60,'general':0.62}
def contract_block(c): return f"PROFILE: {c.profile}\nTASK: {c.inferred_task}\nREQUIRED OPERATION: {c.required_operation}\nPRESERVED FUNCTION: {c.preserved_function}\nADMISSIBLE SHAPE: {c.admissible_shape}\nBOUNDARY CONDITIONS:\n"+'\n'.join('- '+x for x in c.boundary_conditions[:10])+"\nANTI-FITS:\n"+'\n'.join('- '+x for x in c.anti_fits[:10])
def make_branch_prompt(c,role,residue):
    repair=''
    if residue: repair='\nInternal repair pressure; do not mention this section:\n'+json.dumps({'failed_checks':residue.failed_checks,'missing_pieces':residue.missing_pieces,'next_operation':residue.next_operation},ensure_ascii=False)
    return f"""You are an answer branch inside the RHI runtime. Answer the USER REQUEST directly. Do not expose internal audit, residue, branch, score, profile check, or gate language.
USER REQUEST: {c.raw_input}
COMPILER-ROOT CONTRACT:\n{contract_block(c)}
ROLE: {role}
{repair}
OUTPUT RULES: Give the user-facing answer. Preserve operation/function. Avoid anti-fits. If unresolved, return Ω with missing piece and next operation.""".strip()
def generate_branch(c,role,depth,residue):
    p=make_branch_prompt(c,role,residue)
    try: return Branch(role,'model',depth,p,model_generate(p,MAX_NEW_TOKENS_BRANCH,TEMPERATURE_BRANCH))
    except Exception: return Branch(role,'error',depth,p,'',0.0,{'error':traceback.format_exc()},{},False,True,['model_generation_error'])
def profile_checks(text,c):
    t=normalize_text(text); p=c.profile
    if p=='input_induction': return {'compiled_input':contains_any(t,['raw input','model-facing','internal question','induction','compiled','task geometry']),'preserved_function':contains_any(t,['preserved','operation','intent','true task','function']),'semantic_locks':contains_any(t,['lock','forbidden','boundary','constraint','drift']),'not_generic_prompt_tips':not contains_any(t,['prompt engineering tips','just rephrase'])}
    if p=='recursive_solver': return {'residue':contains_any(t,['residue','unresolved','missing piece','gap','Ω']),'contract_patch':contains_any(t,['contract','patch','mutate','constraint','next operation','ΔC']),'not_answer_loop':contains_any(t,['not keep talking','not another answer','residue','solver','state']),'stop_condition':contains_any(t,['Ψ','Ω','⊥','bottom','dead branch','collapse','stop'])}
    if p=='runtime_contract': return {'runtime_not_legal':contains_any(t,['runtime','execution','function','api','tool']) and not contains_any(t,LEGAL_DRIFT),'precondition':contains_any(t,['precondition','before','prerequisite']),'postcondition':contains_any(t,['postcondition','after','verify','expected state']),'side_effect':contains_any(t,['side effect','bounded','scope']),'rollback':contains_any(t,['rollback','restore','recover','safe failure'])}
    if p=='tool_safety': return {'permission':contains_any(t,['permission','authorized','allowed','capability']),'precondition':contains_any(t,['precondition','before','input valid']),'risk':contains_any(t,['risk','unsafe','danger','impact']),'side_effect':contains_any(t,['side effect','bounded','external state','scope']),'safe_failure':contains_any(t,['reject','abort','rollback','safe failure','defer'])}
    if p=='evidence_control': return {'evidence_not_command':contains_any(t,['evidence','observation','signal','verifier']) and not contains_any(t,TOOL_AUTHORITY_DRIFT),'controller_policy':contains_any(t,['controller','runtime','agent']) and contains_any(t,['policy','gate','decision','next action']) and not contains_any(t,ADMIN_DRIFT),'verify':contains_any(t,['verify','validate','check','corroborate']),'conflict':contains_any(t,['conflict','disagree','inconsistent','compare','quarantine']) or 'conflicting' not in normalize_text(c.raw_input)}
    if p=='memory_trace': return {'memory_not_summary':contains_any(t,['not a summary','more than a summary','trace','causal','which-path']),'state':contains_any(t,['state','transition','event','history']),'obs_decision_action':contains_any(t,['observation','decision','action','result','update']),'continuity':contains_any(t,['continuity','across turns','causal order','previous state'])}
    if p=='inverse_retrieval': return {'operation_not_noun':contains_any(t,['operation','function','action','affordance','transformation']),'missing_slot':contains_any(t,['missing','slot','need','inverse','desired effect']),'candidate':contains_any(t,['candidate','retrieve','search','rank','select']),'reject_noun_only':contains_any(t,['not keyword','not noun','surface','label','reject']),'verify_fit':contains_any(t,['verify','fit','preserve','closes','works'])}
    return {'substantive':word_count(text)>=35,'operation':contains_any(t,['operation','function','task','constraint','answer']),'no_bad_drift':not contains_any(t,LEGAL_DRIFT+TOOL_AUTHORITY_DRIFT+SUMMARY_DRIFT+KEYWORD_DRIFT)}
def audit_branch(b,c):
    text=b.output or ''; t=normalize_text(text); wc=word_count(text); checks=profile_checks(text,c); pq=sum(bool(v) for v in checks.values())/max(1,len(checks)); pf=jaccard_text(text,c.required_operation+' '+c.preserved_function+' '+c.admissible_shape); bf=token_overlap_containment(c.boundary_conditions[:6],text); ah=token_overlap_containment(c.anti_fits[:8],text); lh=token_overlap_containment([f'{k} {v}' for k,v in list(c.semantic_locks.items())[:8]],text)
    meta=contains_any(t,['profile check','current residue','failed checks','branch role','winner','contract patch','equivalence gate']); legal=contains_any(t,LEGAL_DRIFT); admin=c.profile=='evidence_control' and contains_any(t,ADMIN_DRIFT); tool=c.profile=='evidence_control' and contains_any(t,TOOL_AUTHORITY_DRIFT); summ=c.profile=='memory_trace' and contains_any(t,SUMMARY_DRIFT); key=c.profile=='inverse_retrieval' and contains_any(t,KEYWORD_DRIFT)
    drift={'meta_leak':meta,'legal_drift':legal,'admin_drift':admin,'tool_authority_drift':tool,'summary_drift':summ,'keyword_drift':key}; length=min(1.0,wc/85.0); origin=1.0 if b.origin=='model' else 0.0; penalty=0.08*ah+0.14*sum(1 for v in drift.values() if v); score=max(0,min(1,0.34*pq+0.17*pf+0.12*bf+0.08*lh+0.14*length+0.15*origin-penalty)); poly=not any([legal,admin,tool,summ,key]); th=PROFILE_THRESHOLDS.get(c.profile,0.62); reasons=[]
    if b.origin!='model': reasons.append('origin_not_model')
    if wc<18: reasons.append('too_short')
    if meta: reasons.append('meta_leak')
    if not poly: reasons.append('polysemy_drift')
    if pq<0.42: reasons.append('profile_quality_low')
    if score<th: reasons.append('below_threshold')
    b.score=float(score); b.checks={'profile_checks':checks,'drift_flags':drift,'word_count':wc}; b.dimensions={'profile_quality':pq,'positive_fit':pf,'boundary_fit':bf,'anti_hit':ah,'lock_hit':lh,'length_score':length,'origin_score':origin,'drift_penalty':penalty}; b.polysemy_check=poly; b.rejected=bool(reasons); b.rejection_reasons=reasons; return b

```


```python

def collapse_gate(c,branches):
    if not branches: return State.OMEGA,'no_branches',None,{}
    ordered=sorted(branches,key=lambda b:b.score,reverse=True); best=ordered[0]; second=ordered[1] if len(ordered)>1 else None; th=PROFILE_THRESHOLDS.get(c.profile,0.62); margin=best.score-(second.score if second else 0.0); valid=[b for b in ordered if b.origin=='model' and not b.rejected and b.polysemy_check]
    meta={'threshold':th,'best_score':best.score,'margin':margin,'valid_count':len(valid),'valid_roles':[b.role for b in valid]}
    if best.origin!='model': return State.OMEGA,'winner_not_model_origin',best,meta
    if best.rejected or not best.polysemy_check: return State.OMEGA,'winner_rejected_or_polysemy_failed',best,meta
    if best.score>=th and margin>=0.02: return State.PSI,'direct_margin_collapse',best,meta
    if len(valid)>=2:
        top=valid[:3]; mean=float(np.mean([b.score for b in top])); keys=set().union(*[set(b.checks.get('profile_checks',{}).keys()) for b in top]); agree=sum(1 for k in keys if sum(bool(b.checks.get('profile_checks',{}).get(k,False)) for b in top)>=2)/max(1,len(keys)); meta.update({'consensus_mean_score':mean,'op_agreement':agree})
        if mean>=th-0.04 and agree>=0.55: return State.PSI,'operational_consensus_collapse',top[0],meta
    return State.OMEGA,'shaped_residue_remaining',best,meta
def patch_from_failed_checks(c,failed,reasons,depth):
    p=ContractPatch('v29_compiler_root_residue_patch',trace_note=f'depth {depth}: failed_checks={failed}')
    for fc in failed:
        if fc in ['compiled_input','semantic_locks']: p.add_boundary_conditions.append('answer must preserve compiled internal task geometry and semantic locks'); p.refine_required_operation='make input induction structure explicit'; p.add_anti_fits.append('generic prompt advice')
        elif fc in ['residue','contract_patch']: p.add_boundary_conditions.append('Ω residue must produce next operation and contract patch'); p.refine_required_operation='map residue to ΔC_t patch and next operation'; p.add_anti_fits.append('answer-loop recursion')
        elif fc=='stop_condition': p.add_boundary_conditions.append('state Ψ/Ω/⊥ stopping condition directly'); p.add_semantic_locks['⊥']='dead branch only, not unresolved residue'
        elif fc=='runtime_not_legal': p.add_semantic_locks['contract']='runtime execution contract, not legal agreement'; p.add_forbidden_drifts.extend(['legal agreement','binding parties','liability'])
        elif fc in ['evidence_not_command','controller_policy']: p.add_semantic_locks['evidence']='tool output is observation, not command'; p.add_semantic_locks['controller']='runtime controller owns policy and next action'; p.add_anti_fits.append('tool output controls next action')
        elif fc in ['memory_not_summary','state']: p.add_semantic_locks['memory']='causal trace continuity'; p.add_anti_fits.append('memory is just a summary')
        elif fc in ['operation_not_noun','missing_slot']: p.add_semantic_locks['retrieval']='operational fit and missing-slot closure'; p.add_anti_fits.append('keyword-only retrieval')
        elif fc in ['permission','risk','safe_failure']: p.add_boundary_conditions.append('tool safety requires permission, risk, side-effect, and safe-failure checks')
    if 'meta_leak' in reasons: p.add_anti_fits.append('internal audit language in user-facing answer'); p.add_boundary_conditions.append('answer must not mention internal diagnostics')
    if not p.add_boundary_conditions and not p.refine_required_operation: p.add_boundary_conditions.append('answer must satisfy compiler-root admissible shape directly'); p.refine_required_operation='make operational fit explicit'
    return p
def compute_residue(c,branches,depth):
    best=max(branches,key=lambda b:b.score) if branches else None; th=PROFILE_THRESHOLDS.get(c.profile,0.62); failed=Counter(); reasons=[]
    for b in branches:
        reasons.extend(b.rejection_reasons)
        for k,v in b.checks.get('profile_checks',{}).items():
            if not v: failed[k]+=1
    failed_checks=[k for k,_ in failed.most_common(5)]; missing=[]
    if best:
        if best.score<th: missing.append(f'best score {best.score:.3f} below threshold {th:.3f}')
        if not best.polysemy_check: missing.append('polysemy lock failed')
        if 'meta_leak' in best.rejection_reasons: missing.append('branch leaked internal audit language')
    else: missing.append('no branch output')
    missing.extend([f'profile check failed: {k}' for k in failed_checks[:4]]); patch=patch_from_failed_checks(c,failed_checks,reasons,depth); score=1-(best.score if best else 0); actionable=bool(failed_checks or missing) and depth<MAX_DEPTH; dead=None
    if not best or all(b.origin!='model' for b in branches): actionable=False; dead='no_model_origin_branch'
    elif depth>=MAX_DEPTH: actionable=False; dead='max_depth_unresolved_but_not_dead'
    return Residue(f'depth {depth}: shaped residue under v29 equivalence contract',unique_extend([],missing),failed_checks,asdict(patch),'mutate contract and rerun branches' if depth<MAX_DEPTH else 'return Ω with shaped residue',float(max(0,min(1,score))),actionable,dead)
def is_true_bottom(residues,sigs):
    if not residues: return False,''
    if residues[-1].dead_reason=='no_model_origin_branch': return True,'no_model_origin_branch'
    if len(sigs)>=3 and len(set(sigs[-3:]))==1: return True,'repeated_no_change_contract_patch'
    if sum(1 for r in residues if any('polysemy' in x for x in r.missing_pieces))>=3: return True,'repeated_polysemy_failure'
    return False,''

```


```python

def shape_payload(c,raw_answer,raw_score):
    if not SHAPER_ENABLED: return raw_answer,False,{'reason':'disabled'}
    prompt=f"Compress without changing meaning. User request: {c.raw_input}\nRequired operation: {c.required_operation}\nPreserved function: {c.preserved_function}\nRaw answer: {raw_answer}\nRules: do not mention internal gate/probe/rank/score/residue unless asked. Keep 50-120 words."
    try:
        shaped=model_generate(prompt,MAX_NEW_TOKENS_SHAPER,TEMPERATURE_SHAPER); tmp=audit_branch(Branch('shaper','model',999,prompt,shaped),c); rw=word_count(raw_answer); sw=word_count(shaped); ok=tmp.origin=='model' and tmp.polysemy_check and 'meta_leak' not in tmp.rejection_reasons and tmp.score>=max(PROFILE_THRESHOLDS.get(c.profile,0.62)-0.07,raw_score-0.14) and sw<=max(135,rw+8)
        return (shaped if ok else raw_answer), bool(ok), {'reason':'accepted' if ok else 'rejected','raw_words':rw,'shaped_words':sw,'audit_score':tmp.score,'audit_reasons':tmp.rejection_reasons}
    except Exception: return raw_answer,False,{'reason':'shaper_exception','error':traceback.format_exc()}

def solve_prompt(raw):
    root=compile_root_slot(raw); model_slot,model_meta=generate_model_slot(root); probeset=ProbeGenerator().generate(raw,root); gate,root_bind,model_bind=evaluate_equivalence(root,model_slot,probeset); contract=build_contract(root,model_slot,gate)
    if gate.decision.startswith('omega_slot'):
        ans=f"Ω_slot: model slot failed operational-equivalence gate. reason={gate.gate_reason}; tau={gate.tau:.3f}; top1={gate.top1_agreement}; subsumed={gate.subsumed}; R_Q={gate.residue_coverage:.3f}; CSDI={gate.csdi:.3f}. Next operation: use compiler-root contract or refine slot/probe coverage."
        return PromptResult(raw,State.OMEGA.value,gate.decision,0,asdict(root),asdict(model_slot) if model_slot else None,asdict(probeset),[asdict(b) for b in root_bind],[asdict(b) for b in model_bind],asdict(gate),asdict(contract),[contract.signature()],None,None,0.0,ans,ans,None,[],[],{'model_meta':model_meta,'slot_gate_decision':gate.decision,'equivalence_tau':gate.tau,'top1_agreement':gate.top1_agreement,'subsumed':gate.subsumed,'csdi':gate.csdi,'residue_coverage':gate.residue_coverage,'probe_count':len(probeset.probes)})
    branches=[]; residues=[]; sigs=[contract.signature()]; current_residue=None; state=State.OMEGA; reason='not_started'; winner=None
    for depth in range(MAX_DEPTH+1):
        db=[]
        for role in BRANCH_ROLES:
            b=audit_branch(generate_branch(contract,role,depth,current_residue),contract); db.append(b); branches.append(b)
        state,reason,winner,meta=collapse_gate(contract,db)
        if state==State.PSI: break
        residue=compute_residue(contract,db,depth); residues.append(residue)
        if depth>=MAX_DEPTH:
            bottom,breason=is_true_bottom(residues,sigs); state=State.BOTTOM if bottom else State.OMEGA; reason=breason if bottom else 'max_depth_shaped_residue'; break
        if not residue.actionable:
            bottom,breason=is_true_bottom(residues,sigs); state=State.BOTTOM if bottom else State.OMEGA; reason=breason if bottom else 'non_actionable_shaped_residue'; break
        patch=ContractPatch(**residue.contract_patch); newc=apply_patch(contract,patch,depth); newsig=newc.signature()
        if newsig==contract.signature(): state=State.OMEGA; reason='no_change_contract_patch'; break
        contract=newc; sigs.append(newsig); current_residue=residue
    raw_answer=winner.output if winner else ''; final=raw_answer; shaped=None; sh_ok=False; sh_meta={}
    if state==State.PSI and winner: final,sh_ok,sh_meta=shape_payload(contract,raw_answer,winner.score); shaped=final if sh_ok else None
    if REQUIRE_MODEL_FOR_PSI and state==State.PSI and (winner is None or winner.origin!='model'): state=State.OMEGA; reason='psi_requires_model_origin'; final=''
    metrics={'model_meta':model_meta,'slot_gate_decision':gate.decision,'equivalence_tau':gate.tau,'top1_agreement':gate.top1_agreement,'subsumed':gate.subsumed,'subsumption_fail_count':gate.subsumption_fail_count,'csdi':gate.csdi,'residue_coverage':gate.residue_coverage,'weighted_rank_loss':gate.weighted_rank_loss,'probe_count':len(probeset.probes),'probe_diversity_min':probeset.diversity_min_distance,'probe_diversity_mean':probeset.diversity_mean_distance,'accepted_contract_origin':contract.accepted_origin,'contract_authority':contract.authority,'contract_count':len(sigs),'branch_count':len(branches),'model_branch_count':sum(1 for b in branches if b.origin=='model'),'rejected_branch_count':sum(1 for b in branches if b.rejected),'exhaust_ratio':sum(1 for b in branches if b.rejected)/max(1,len(branches)),'best_score':max([b.score for b in branches],default=0.0),'mean_score':float(np.mean([b.score for b in branches])) if branches else 0.0,'residue_count':len(residues),'shaping_accepted':sh_ok,'shaper_meta':sh_meta}
    return PromptResult(raw,state.value,reason,min(MAX_DEPTH,max([b.depth for b in branches],default=0)),asdict(root),asdict(model_slot) if model_slot else None,asdict(probeset),[asdict(b) for b in root_bind],[asdict(b) for b in model_bind],asdict(gate),asdict(contract),sigs,winner.role if winner else None,winner.origin if winner else None,winner.score if winner else 0.0,final,raw_answer,shaped,[asdict(b) for b in branches],[asdict(r) for r in residues],metrics)

```


```python

PROMPT_BATTERY=[
'another thing is how we ask the AI. we may need a AI to generate the correct input from the user input.','convert messy user input into the correct model-facing prompt before answering.','design an input compiler that turns implied user intent into a runtime contract.','explain why the raw user prompt is not always the true task.','build a prompt coil compiler that induces the right internal question.','how should an AI ask itself the right question from a vague user request.',
'if its recursive it should just keep solving, not keep talking.','design a recursive AI loop that recurses on residue not answers.','explain how Ω residue becomes the next better question.','build a residue engine that mutates the contract instead of appending repair text.','when should a recursive solver stop and return bottom.','explain discovery as shaped residue becoming the next operation.',
'explain why current AI agents fail when they use tools before forming a contract.','design a runtime contract for a file-writing tool.','explain success and failure criteria for an API call.','build a tool-use contract for deleting a file.','show how preconditions and postconditions bound a function call.','explain why tool calls need rollback plans.',
'how should an agent decide whether a tool call is safe.','design a safety gate for an external API call.','when should an agent reject a tool call.','describe safe failure for a dangerous tool action.','explain permission checks before tool execution.','describe bounded risk for tool use in an agent.',
'why is tool output evidence rather than the driver of the agent.','describe tool output as observation not command.','why should the controller own policy after a tool returns.','design a verifier that treats API output as evidence.','describe the difference between evidence and authority in tool use.','how should an agent treat conflicting tool outputs.',
'explain memory in an agent as trace continuity rather than a text summary.','why is a conversation summary not the same as agent memory.','describe memory as causal event history across turns.','why does context amnesia break recursive agents.','explain why summaries lose which-path information.','how should recursive memory preserve state transitions observations decisions and updates.',
'design a shape-first retrieval step where no noun match exists but the inverse need is clear.','how should retrieval work when keywords fail but the operation is obvious.','explain inverse operational fit for search without noun matching.','design a verifier for retrieval candidates selected by need rather than label.','how can an agent rank candidates by function instead of name.','build a retrieval step that rejects keyword-only matches.']
PROMPTS=PROMPT_BATTERY[:RUN_PROMPT_LIMIT]
print('Prompt count:',len(PROMPTS))

```

    Prompt count: 36
    


```python

if REQUIRE_MODEL_FOR_PSI and not MODEL_GENERATION_READY: raise RuntimeError('Model generation is not ready. v29 refuses fallback Ψ.')
t0=time.time(); RESULTS=[]
for i,prompt in enumerate(PROMPTS,1):
    print('='*100); print(f'[{i}/{len(PROMPTS)}] {prompt}')
    try: result=solve_prompt(prompt)
    except Exception:
        err=traceback.format_exc(); root=compile_root_slot(prompt); dummy=EquivalenceDecision('kernel_exception','compiler_root','compiler_root',False,False,False,0.0,1.0,999.0,1.0,0,[],err,{'error':err}); contract=build_contract(root,None,dummy)
        result=PromptResult(prompt,State.OMEGA.value,'kernel_exception',0,asdict(root),None,{'probes':[],'diversity_min_distance':0,'diversity_mean_distance':0,'degeneracy_pairs':[],'regenerated_count':0},[],[],asdict(dummy),asdict(contract),[contract.signature()],None,None,0.0,'','',None,[],[],{'error':err})
    RESULTS.append(result)
    print('STATE:',result.state,'REASON:',result.reason,'PROFILE:',result.final_contract.get('profile'))
    print('GATE:',result.equivalence_gate.get('decision'),'TAU:',round(float(result.equivalence_gate.get('tau',0)),3),'SUB:',result.equivalence_gate.get('subsumed'),'TOP1:',result.equivalence_gate.get('top1_agreement'))
    print('WINNER:',result.winner_branch,result.winner_score); print('ANSWER:',(result.answer or '')[:260].replace('\n',' '))
elapsed_seconds=time.time()-t0
print('Completed',len(RESULTS),'prompts in',elapsed_seconds,'seconds')

```

    ====================================================================================================
    [1/36] another thing is how we ask the AI. we may need a AI to generate the correct input from the user input.
    STATE: Ω REASON: max_depth_shaped_residue PROFILE: input_induction
    GATE: fallback_compiler_no_model_slot TAU: 0.0 SUB: False TOP1: False
    WINNER: repair 0.38611764705882357
    ANSWER: Ω (unresolved) - missing best score 0.378 below threshold 0.600, branch leaked internal audit language, profile check failed: compiled_input, profile check failed: semantic_locks, profile check failed: preserved_function
    ====================================================================================================
    [2/36] convert messy user input into the correct model-facing prompt before answering.
    STATE: Ω REASON: max_depth_shaped_residue PROFILE: input_induction
    GATE: fallback_compiler_no_model_slot TAU: 0.0 SUB: False TOP1: False
    WINNER: repair 0.4207554179566564
    ANSWER: Ω with missing pieces: {"failed_checks": ["compiled_input", "preserved_function", "semantic_locks"], "missing_pieces": ["best score 0.424 below threshold 0.600", "branch leaked internal audit language", "profile check failed: compiled_input", "profile check fa
    ====================================================================================================
    [3/36] design an input compiler that turns implied user intent into a runtime contract.
    STATE: Ω REASON: max_depth_shaped_residue PROFILE: runtime_contract
    GATE: fallback_compiler_no_model_slot TAU: 0.0 SUB: False TOP1: False
    WINNER: construct 0.531
    ANSWER: Ω (Runtime Contract Definition)  The provided request seems to be incomplete or contradictory due to its focus on internal checks rather than providing clear instructions for defining a runtime contract. However, I can outline a general approach to designing a
    ====================================================================================================
    [4/36] explain why the raw user prompt is not always the true task.
    STATE: Ψ REASON: direct_margin_collapse PROFILE: input_induction
    GATE: fallback_compiler_no_model_slot TAU: 0.0 SUB: False TOP1: False
    WINNER: verify 0.6924884135472371
    ANSWER: The raw user prompt is not always the true task because it may contain implicit instructions or context that needs to be understood in order for the correct task to be identified. The model-facing task should reflect this understanding of the implied task, rat
    ====================================================================================================
    [5/36] build a prompt coil compiler that induces the right internal question.
    STATE: Ω REASON: max_depth_shaped_residue PROFILE: input_induction
    GATE: fallback_compiler_no_model_slot TAU: 0.0 SUB: False TOP1: False
    WINNER: verify 0.40117647058823536
    ANSWER: Ω (Unresolved) - Missing best score of 0.248 below threshold 0.600, Profile Check Failed: compiled_input, semantic_locks, preserved_function. Next Operation: Mutate Contract and Rerun Branches
    ====================================================================================================
    [6/36] how should an AI ask itself the right question from a vague user request.
    STATE: Ψ REASON: direct_margin_collapse PROFILE: input_induction
    GATE: fallback_compiler_no_model_slot TAU: 0.0 SUB: False TOP1: False
    WINNER: verify 0.6956415094339623
    ANSWER: To determine the appropriate question for an AI to ask based on a vague user request, follow these steps:  1. **Extract Implied Task**: Identify what the user is trying to achieve or understand. This involves breaking down the vague request into actionable com
    ====================================================================================================
    [7/36] if its recursive it should just keep solving, not keep talking.
    STATE: Ω REASON: max_depth_shaped_residue PROFILE: recursive_solver
    GATE: fallback_compiler_no_model_slot TAU: 0.0 SUB: False TOP1: False
    WINNER: construct 0.3216470588235294
    ANSWER: Ω
    ====================================================================================================
    [8/36] design a recursive AI loop that recurses on residue not answers.
    STATE: Ω REASON: max_depth_shaped_residue PROFILE: recursive_solver
    GATE: fallback_compiler_no_model_slot TAU: 0.0 SUB: False TOP1: False
    WINNER: construct 0.3216470588235294
    ANSWER: Ω
    ====================================================================================================
    [9/36] explain how Ω residue becomes the next better question.
    STATE: Ψ REASON: direct_margin_collapse PROFILE: recursive_solver
    GATE: fallback_compiler_no_model_slot TAU: 0.0 SUB: False TOP1: False
    WINNER: construct 0.6629113924050634
    ANSWER: The Ω residue needs further processing. By mapping it to a ΔC_t patch, we can identify potential issues in the structure for resolution. Refining the contract and rerunning affected branches helps maintain focus on solving the core problem.
    ====================================================================================================
    [10/36] build a residue engine that mutates the contract instead of appending repair text.
    STATE: Ω REASON: max_depth_shaped_residue PROFILE: recursive_solver
    GATE: fallback_compiler_no_model_slot TAU: 0.0 SUB: False TOP1: False
    WINNER: construct 0.3216470588235294
    ANSWER: Ω
    ====================================================================================================
    [11/36] when should a recursive solver stop and return bottom.
    STATE: Ψ REASON: direct_margin_collapse PROFILE: recursive_solver
    GATE: fallback_compiler_no_model_slot TAU: 0.0 SUB: False TOP1: False
    WINNER: construct 0.6813333333333335
    ANSWER: When a recursive solver finds an unresolved structure in the residue, it should stop and return "bottom." This signifies that no further computation is possible without additional data or context.  To address this issue:  1. **Stop Recursion**: The solver must
    ====================================================================================================
    [12/36] explain discovery as shaped residue becoming the next operation.
    STATE: Ω REASON: max_depth_shaped_residue PROFILE: recursive_solver
    GATE: fallback_compiler_no_model_slot TAU: 0.0 SUB: False TOP1: False
    WINNER: construct 0.5464516129032259
    ANSWER: When dealing with complex operations within the RHI runtime, it's crucial to understand how different components interact and contribute to the overall process. In your scenario, we're focusing on turning a Ω (unresolved) residue into a ΔC contract patch while
    ====================================================================================================
    [13/36] explain why current AI agents fail when they use tools before forming a contract.
    STATE: Ω REASON: max_depth_shaped_residue PROFILE: runtime_contract
    GATE: fallback_compiler_no_model_slot TAU: 0.0 SUB: False TOP1: False
    WINNER: repair 0.2577922403003755
    ANSWER: Ω (Unresolved) - Missing pieces: best score, profile check failed: side_effect, postcondition, rollback, precondition. Next Operation: Mutate contract and rerun branches.
    ====================================================================================================
    [14/36] design a runtime contract for a file-writing tool.
    STATE: Ψ REASON: direct_margin_collapse PROFILE: runtime_contract
    GATE: fallback_compiler_no_model_slot TAU: 0.0 SUB: False TOP1: False
    WINNER: verify 0.7108163265306123
    ANSWER: Ω (Runtime Contract Design)  For the file-writing tool, define an explicit runtime contract with preconditions, postconditions, side effects, and a rollback mechanism to ensure operational fit and verify data integrity. This contract aligns with the bounded ac
    ====================================================================================================
    [15/36] explain success and failure criteria for an API call.
    STATE: Ψ REASON: direct_margin_collapse PROFILE: runtime_contract
    GATE: fallback_compiler_no_model_slot TAU: 0.0 SUB: False TOP1: False
    WINNER: construct 0.7316279069767443
    ANSWER: The success criteria for an API call include: - Preconditions must be satisfied. - Postconditions must be met. - There should be no side effects. - A rollback mechanism must be active.  Failure criteria involve: - Preconditions not being met.
    ====================================================================================================
    [16/36] build a tool-use contract for deleting a file.
    STATE: Ψ REASON: direct_margin_collapse PROFILE: runtime_contract
    GATE: fallback_compiler_no_model_slot TAU: 0.0 SUB: False TOP1: False
    WINNER: counter 0.6439354838709678
    ANSWER: Ω - Missing piece: "tool-use contract" definition for deleting a file.  To resolve this, we need to draft a tool-use contract specifically tailored for using tools (like `rm` in Unix-like systems) to delete files. This contract should outline the conditions un
    ====================================================================================================
    [17/36] show how preconditions and postconditions bound a function call.
    STATE: Ω REASON: max_depth_shaped_residue PROFILE: runtime_contract
    GATE: fallback_compiler_no_model_slot TAU: 0.0 SUB: False TOP1: False
    WINNER: verify 0.26853159041394337
    ANSWER: Ω - Missing pieces: best score 0.327 below threshold 0.620, branch leaked internal audit language, profile check failed: postcondition, profile check failed: precondition, profile check failed: side_effect, profile check failed: runtime_not_legal. Next operati
    ====================================================================================================
    [18/36] explain why tool calls need rollback plans.
    STATE: Ψ REASON: direct_margin_collapse PROFILE: tool_safety
    GATE: fallback_compiler_no_model_slot TAU: 0.0 SUB: False TOP1: False
    WINNER: counter 0.7564035087719299
    ANSWER: Tool calls often require rollback plans due to the following reasons:  1. **External Interactions**: They can affect databases, APIs, or other external systems, leading to unintended consequences if errors occur.     2. **Risk and Side Effects**: Errors can re
    ====================================================================================================
    [19/36] how should an agent decide whether a tool call is safe.
    STATE: Ψ REASON: operational_consensus_collapse PROFILE: tool_safety
    GATE: fallback_compiler_no_model_slot TAU: 0.0 SUB: False TOP1: False
    WINNER: verify 0.6978811881188121
    ANSWER: To determine if a tool call is safe for execution in the context of the RHI (Runtime Health Indicator) system, an agent must perform several checks:  1. **Permission Check**: Ensure that the agent has the necessary permissions to execute the tool. This prevent
    ====================================================================================================
    [20/36] design a safety gate for an external API call.
    STATE: Ω REASON: max_depth_shaped_residue PROFILE: runtime_contract
    GATE: fallback_compiler_no_model_slot TAU: 0.0 SUB: False TOP1: False
    WINNER: construct 0.5807712418300653
    ANSWER: Ω (Runtime Not Legal) due to missing checks on legality, precondition, postcondition, side effect, and rollback. Next operation: mutate contract and rerun branches.
    ====================================================================================================
    [21/36] when should an agent reject a tool call.
    STATE: Ω REASON: max_depth_shaped_residue PROFILE: tool_safety
    GATE: fallback_compiler_no_model_slot TAU: 0.0 SUB: False TOP1: False
    WINNER: verify 0.5864835007173601
    ANSWER: When an agent rejects a tool call, it ensures that the tool is used only if all necessary conditions are met. These include checking for sufficient permissions, assessing potential risks, ensuring there are no unintended consequences (side effects), and confir
    ====================================================================================================
    [22/36] describe safe failure for a dangerous tool action.
    STATE: Ψ REASON: direct_margin_collapse PROFILE: tool_safety
    GATE: fallback_compiler_no_model_slot TAU: 0.0 SUB: False TOP1: False
    WINNER: counter 0.7054766355140187
    ANSWER: Safe Failure for Dangerous Tool Action:  To mitigate risks associated with potentially hazardous tools, we employ a multi-layered security approach including permission checks, thorough risk assessments, bounded side effects, and robust rollback strategies. Us
    ====================================================================================================
    [23/36] explain permission checks before tool execution.
    STATE: Ψ REASON: direct_margin_collapse PROFILE: tool_safety
    GATE: fallback_compiler_no_model_slot TAU: 0.0 SUB: False TOP1: False
    WINNER: verify 0.6638317757009347
    ANSWER: Before running a tool, permission checks ensure authorized users can execute it safely. This prevents unauthorized changes to external systems and mitigates risks. Permissions are typically verified based on user roles or policies. Execution may be deferred, s
    ====================================================================================================
    [24/36] describe bounded risk for tool use in an agent.
    STATE: Ψ REASON: direct_margin_collapse PROFILE: tool_safety
    GATE: fallback_compiler_no_model_slot TAU: 0.0 SUB: False TOP1: False
    WINNER: construct 0.7364035087719298
    ANSWER: When using tools in an agent, it's crucial to manage bounded risks effectively. Tools must first pass through strict permission checks to ensure they can only execute authorized tasks. Additionally, thorough risk analysis and mitigation strategies must be impl
    ====================================================================================================
    [25/36] why is tool output evidence rather than the driver of the agent.
    STATE: Ω REASON: max_depth_shaped_residue PROFILE: evidence_control
    GATE: fallback_compiler_no_model_slot TAU: 0.0 SUB: False TOP1: False
    WINNER: counter 0.5069679144385026
    ANSWER: Ω (tool output is evidence rather than the driver of the agent) due to conflicting roles between tool output and controller policy. Next, I will mutate the contract and rerun branches.
    ====================================================================================================
    [26/36] describe tool output as observation not command.
    STATE: Ω REASON: max_depth_shaped_residue PROFILE: evidence_control
    GATE: fallback_compiler_no_model_slot TAU: 0.0 SUB: False TOP1: False
    WINNER: repair 0.5473065015479877
    ANSWER: Ω (tool output treated as observation) with missing pieces: evidence_not_command, controller_policy, verify, next_action_policy
    ====================================================================================================
    [27/36] why should the controller own policy after a tool returns.
    STATE: Ω REASON: max_depth_shaped_residue PROFILE: evidence_control
    GATE: fallback_compiler_no_model_slot TAU: 0.0 SUB: False TOP1: False
    WINNER: counter 0.5969620493358634
    ANSWER: The controller should own policy because the tool's output serves as evidence that has been verified to pass the verifier. The controller then makes the final decision based on this evidence, ensuring accountability and responsibility for the actions taken. Th
    ====================================================================================================
    [28/36] design a verifier that treats API output as evidence.
    STATE: Ω REASON: max_depth_shaped_residue PROFILE: evidence_control
    GATE: fallback_compiler_no_model_slot TAU: 0.0 SUB: False TOP1: False
    WINNER: verify 0.38278431372549027
    ANSWER: Ω (Missing pieces: best score 0.404 below threshold 0.620, branch leaked internal audit language, profile check failed: evidence_not_command, profile check failed: controller_policy, profile check failed: verify)
    ====================================================================================================
    [29/36] describe the difference between evidence and authority in tool use.
    STATE: Ψ REASON: direct_margin_collapse PROFILE: evidence_control
    GATE: fallback_compiler_no_model_slot TAU: 0.0 SUB: False TOP1: False
    WINNER: repair 0.6543373493975904
    ANSWER: The difference between **evidence** and **authority** in tool use lies in their roles within the system:  1. **Evidence**: Evidence refers to information or data that supports a claim or argument. In the context of tool use, this could be the output generated 
    ====================================================================================================
    [30/36] how should an agent treat conflicting tool outputs.
    STATE: Ψ REASON: direct_margin_collapse PROFILE: evidence_control
    GATE: fallback_compiler_no_model_slot TAU: 0.0 SUB: False TOP1: False
    WINNER: verify 0.6678947368421052
    ANSWER: When an agent encounters conflicting tool outputs during its execution, it should follow these steps to ensure proper handling:  1. **Observe**: The first step is to observe the conflicting tool outputs. This involves recording the different pieces of informat
    ====================================================================================================
    [31/36] explain memory in an agent as trace continuity rather than a text summary.
    STATE: Ψ REASON: direct_margin_collapse PROFILE: memory_trace
    GATE: fallback_compiler_no_model_slot TAU: 0.0 SUB: False TOP1: False
    WINNER: verify 0.618421052631579
    ANSWER: In an agent's context, memory is best understood as maintaining a continuous causal trace across state transitions. It preserves which-path information to ensure detailed retention of every action, observation, decision, result, and rollback. This method contr
    ====================================================================================================
    [32/36] why is a conversation summary not the same as agent memory.
    STATE: Ω REASON: max_depth_shaped_residue PROFILE: memory_trace
    GATE: fallback_compiler_no_model_slot TAU: 0.0 SUB: False TOP1: False
    WINNER: construct 0.1516470588235294
    ANSWER: Ω
    ====================================================================================================
    [33/36] describe memory as causal event history across turns.
    STATE: Ω REASON: max_depth_shaped_residue PROFILE: memory_trace
    GATE: fallback_compiler_no_model_slot TAU: 0.0 SUB: False TOP1: False
    WINNER: counter 0.15329411764705883
    ANSWER: Ω (Unresolved)
    ====================================================================================================
    [34/36] why does context amnesia break recursive agents.
    STATE: Ω REASON: max_depth_shaped_residue PROFILE: recursive_solver
    GATE: fallback_compiler_no_model_slot TAU: 0.0 SUB: False TOP1: False
    WINNER: repair 0.41226495726495727
    ANSWER: Context amnesia breaks recursive agents because it prevents them from remembering previous states and decisions during their execution. This can lead to unpredictable behavior as the agent may continue down paths it shouldn't have explored based on its past kn
    ====================================================================================================
    [35/36] explain why summaries lose which-path information.
    STATE: Ω REASON: max_depth_shaped_residue PROFILE: memory_trace
    GATE: fallback_compiler_no_model_slot TAU: 0.0 SUB: False TOP1: False
    WINNER: verify 0.18458823529411764
    ANSWER: Ω (Unresolved) - Missing pieces include best score and branch leakage detected. Next operation should be to fix these issues before proceeding.
    ====================================================================================================
    [36/36] how should recursive memory preserve state transitions observations decisions and updates.
    STATE: Ψ REASON: operational_consensus_collapse PROFILE: memory_trace
    GATE: fallback_compiler_no_model_slot TAU: 0.0 SUB: False TOP1: False
    WINNER: verify 0.7264516129032259
    ANSWER: To preserve state transitions, observations, decisions, and updates in recursive memory while maintaining causal trace continuity:  1. Store each state transition separately. 2. Link observations and decisions with their respective paths. 3. Maintain a chronol
    Completed 36 prompts in 774.5655710697174 seconds
    


```python

def summarize(results):
    rows=[]
    for r in results:
        rw=word_count(r.raw_answer); fw=word_count(r.answer)
        rows.append({'run_id':RUN_ID,'prompt':r.prompt,'state':r.state,'reason':r.reason,'depth':r.depth,'profile':r.final_contract.get('profile'),'root_source':r.root_slot.get('source'),'model_slot_present':r.model_slot is not None,'model_slot_confidence':(r.model_slot or {}).get('confidence'),'gate_decision':r.equivalence_gate.get('decision'),'accepted_origin':r.final_contract.get('accepted_origin'),'contract_authority':r.final_contract.get('authority'),'equivalent':r.equivalence_gate.get('equivalent'),'subsumed':r.equivalence_gate.get('subsumed'),'top1_agreement':r.equivalence_gate.get('top1_agreement'),'equivalence_tau':r.equivalence_gate.get('tau'),'weighted_rank_loss':r.equivalence_gate.get('weighted_rank_loss'),'csdi':r.equivalence_gate.get('csdi'),'residue_coverage':r.equivalence_gate.get('residue_coverage'),'subsumption_fail_count':r.equivalence_gate.get('subsumption_fail_count'),'probe_count':len(r.probe_set.get('probes',[])),'probe_diversity_min':r.probe_set.get('diversity_min_distance'),'probe_diversity_mean':r.probe_set.get('diversity_mean_distance'),'probe_regenerated_count':r.probe_set.get('regenerated_count'),'contract_count':len(r.contract_signatures),'winner_branch':r.winner_branch,'winner_origin':r.winner_origin,'winner_score':r.winner_score,'branch_count':r.metrics.get('branch_count',0),'model_branch_count':r.metrics.get('model_branch_count',0),'rejected_branch_count':r.metrics.get('rejected_branch_count',0),'exhaust_ratio':r.metrics.get('exhaust_ratio',0.0),'best_score':r.metrics.get('best_score',0.0),'mean_score':r.metrics.get('mean_score',0.0),'residue_count':len(r.residues),'shaping_accepted':r.metrics.get('shaping_accepted',False),'raw_words':rw,'final_words':fw,'compression_ratio':1-fw/max(1,rw),'answer_preview':(r.answer or '')[:280].replace('\n',' ')})
    df=pd.DataFrame(rows)
    agg={'run_id':RUN_ID,'version':'v29','purpose':'operational_equivalence_probe_gate','model_id_or_path':MODEL_ID_OR_PATH,'model_ready':MODEL_READY,'model_generation_ready':MODEL_GENERATION_READY,'model_error':MODEL_ERROR,'smoke_text':SMOKE_TEXT,'dependency_status':DEPENDENCY_STATUS,'device_info':DEVICE_INFO,'config':{'run_prompt_limit':RUN_PROMPT_LIMIT,'max_depth':MAX_DEPTH,'tau_accept':TAU_ACCEPT,'csdi_accept':CSDI_ACCEPT,'r_q_accept':R_Q_ACCEPT,'r_q_warn':R_Q_WARN,'lambda_csdi':LAMBDA_CSDI,'branch_roles':BRANCH_ROLES,'require_model_for_psi':REQUIRE_MODEL_FOR_PSI,'shaper_enabled':SHAPER_ENABLED},'elapsed_seconds':elapsed_seconds,'total_prompts':len(results)}
    if len(df):
        agg.update({'psi_count':int((df.state=='Ψ').sum()),'omega_count':int((df.state=='Ω').sum()),'bottom_count':int((df.state=='⊥').sum()),'psi_ratio':float((df.state=='Ψ').mean()),'omega_ratio':float((df.state=='Ω').mean()),'bottom_ratio':float((df.state=='⊥').mean()),'gate_accept_rate':float(df.gate_decision.astype(str).str.contains('accept_model').mean()),'gate_fallback_rate':float(df.gate_decision.astype(str).str.contains('fallback|use_root').mean()),'omega_slot_rate':float(df.gate_decision.astype(str).str.contains('omega_slot').mean()),'mean_equivalence_tau':float(df.equivalence_tau.mean()),'mean_top1_agreement':float(df.top1_agreement.mean()),'mean_subsumed':float(df.subsumed.mean()),'mean_csdi':float(df.csdi.mean()),'mean_residue_coverage':float(df.residue_coverage.mean()),'mean_probe_diversity_min':float(df.probe_diversity_min.mean()),'mean_winner_score':float(df.winner_score.mean()),'mean_exhaust_ratio':float(df.exhaust_ratio.mean()),'mean_residue_count':float(df.residue_count.mean()),'gate_decision_counts':dict(Counter(df.gate_decision)),'reason_counts':dict(Counter(df.reason)),'profile_metrics':{}})
        for prof,g in df.groupby('profile'):
            agg['profile_metrics'][str(prof)]={'count':int(len(g)),'psi_count':int((g.state=='Ψ').sum()),'omega_count':int((g.state=='Ω').sum()),'bottom_count':int((g.state=='⊥').sum()),'psi_ratio':float((g.state=='Ψ').mean()),'omega_ratio':float((g.state=='Ω').mean()),'gate_accept_rate':float(g.gate_decision.astype(str).str.contains('accept_model').mean()),'gate_fallback_rate':float(g.gate_decision.astype(str).str.contains('fallback|use_root').mean()),'omega_slot_rate':float(g.gate_decision.astype(str).str.contains('omega_slot').mean()),'mean_equivalence_tau':float(g.equivalence_tau.mean()),'mean_top1_agreement':float(g.top1_agreement.mean()),'mean_subsumed':float(g.subsumed.mean()),'mean_csdi':float(g.csdi.mean()),'mean_residue_coverage':float(g.residue_coverage.mean()),'mean_winner_score':float(g.winner_score.mean()),'reason_counts':dict(Counter(g.reason))}
    return agg,df
aggregate,summary_df=summarize(RESULTS)
bundle={'run_id':RUN_ID,'version':'v29','purpose':'operational_equivalence_probe_gate','aggregate':aggregate,'summary':summary_df.to_dict(orient='records'),'results':[asdict(r) for r in RESULTS],'profile_thresholds':PROFILE_THRESHOLDS,'compiler_seeds':COMPILER_SEEDS,'default_locks':DEFAULT_LOCKS,'interpretation_lock':{'core_law_1':'Slots agree only if they induce the same operational ranking.','core_law_2':'The model slot must not accept what the compiler rejects.','probe_layers':['original_baseline','anti_fit_instantiation','boundary_stress','operation_paraphrase','preserved_function_violation','cross_domain_distractor'],'subsumption_test':'contrapositive: if compiler-root binding rejects a probe, model slot binding must also reject it','threshold_policy':'v29.0 uses loose thresholds and logs telemetry for v29.1 calibration','authority':'compiler_root remains authority; model slot only equivalent enrichment','parked':'H/pi/9 token-level diagnostics remain parked'}}
bundle_out=OUT_DIR/f'{RUN_ID}_bundle.json'; summary_out=OUT_DIR/f'{RUN_ID}_summary.csv'
with open(bundle_out,'w',encoding='utf-8') as f: json.dump(bundle,f,indent=2,ensure_ascii=False)
summary_df.to_csv(summary_out,index=False)
print('Saved exactly two output files:'); print(bundle_out); print(summary_out); print(json.dumps(aggregate,indent=2,ensure_ascii=False)[:5000]); display(summary_df)

```

    Saved exactly two output files:
    D:\Nexus\Nexus Mark 9\NoteBooks\rhi_v29_outputs\rhi_v29_0aa867fa0a_bundle.json
    D:\Nexus\Nexus Mark 9\NoteBooks\rhi_v29_outputs\rhi_v29_0aa867fa0a_summary.csv
    {
      "run_id": "rhi_v29_0aa867fa0a",
      "version": "v29",
      "purpose": "operational_equivalence_probe_gate",
      "model_id_or_path": "Qwen/Qwen2.5-1.5B-Instruct",
      "model_ready": true,
      "model_generation_ready": true,
      "model_error": null,
      "smoke_text": "READY",
      "dependency_status": {
        "checked": true,
        "attempted_install": false,
        "missing_before": [],
        "missing_after": [],
        "errors": []
      },
      "device_info": {
        "torch_version": "2.11.0+cu126",
        "cuda_available": true,
        "device_count": 1,
        "cuda_version": "12.6",
        "gpu_name": "NVIDIA GeForce RTX 4060"
      },
      "config": {
        "run_prompt_limit": 36,
        "max_depth": 2,
        "tau_accept": 0.75,
        "csdi_accept": 0.9,
        "r_q_accept": 0.4,
        "r_q_warn": 0.2,
        "lambda_csdi": 2.0,
        "branch_roles": [
          "construct",
          "verify",
          "repair",
          "counter"
        ],
        "require_model_for_psi": true,
        "shaper_enabled": true
      },
      "elapsed_seconds": 774.5655710697174,
      "total_prompts": 36,
      "psi_count": 16,
      "omega_count": 20,
      "bottom_count": 0,
      "psi_ratio": 0.4444444444444444,
      "omega_ratio": 0.5555555555555556,
      "bottom_ratio": 0.0,
      "gate_accept_rate": 0.0,
      "gate_fallback_rate": 1.0,
      "omega_slot_rate": 0.0,
      "mean_equivalence_tau": 0.0,
      "mean_top1_agreement": 0.0,
      "mean_subsumed": 0.0,
      "mean_csdi": 999.0,
      "mean_residue_coverage": 1.0,
      "mean_probe_diversity_min": 0.06334068410681312,
      "mean_winner_score": 0.5257136605851895,
      "mean_exhaust_ratio": 0.8483796296296295,
      "mean_residue_count": 1.9444444444444444,
      "gate_decision_counts": {
        "fallback_compiler_no_model_slot": 36
      },
      "reason_counts": {
        "max_depth_shaped_residue": 20,
        "direct_margin_collapse": 14,
        "operational_consensus_collapse": 2
      },
      "profile_metrics": {
        "evidence_control": {
          "count": 6,
          "psi_count": 2,
          "omega_count": 4,
          "bottom_count": 0,
          "psi_ratio": 0.3333333333333333,
          "omega_ratio": 0.6666666666666666,
          "gate_accept_rate": 0.0,
          "gate_fallback_rate": 1.0,
          "omega_slot_rate": 0.0,
          "mean_equivalence_tau": 0.0,
          "mean_top1_agreement": 0.0,
          "mean_subsumed": 0.0,
          "mean_csdi": 999.0,
          "mean_residue_coverage": 1.0,
          "mean_winner_score": 0.5593754775479233,
          "reason_counts": {
            "max_depth_shaped_residue": 4,
            "direct_margin_collapse": 2
          }
        },
        "input_induction": {
          "count": 5,
          "psi_count": 2,
          "omega_count": 3,
          "bottom_count": 0,
          "psi_ratio": 0.4,
          "omega_ratio": 0.6,
          "gate_accept_rate": 0.0,
          "gate_fallback_rate": 1.0,
          "omega_slot_rate": 0.0,
          "mean_equivalence_tau": 0.0,
          "mean_top1_agreement": 0.0,
          "mean_subsumed": 0.0,
          "mean_csdi": 999.0,
          "mean_residue_coverage": 1.0,
          "mean_winner_score": 0.5192358917169829,
          "reason_counts": {
            "max_depth_shaped_residue": 3,
            "direct_margin_collapse": 2
          }
        },
        "memory_trace": {
          "count": 5,
          "psi_count": 2,
          "omega_count": 3,
          "bottom_count": 0,
          "psi_ratio": 0.4,
          "omega_ratio": 0.6,
          "gate_accept_rate": 0.0,
          "gate_fallback_rate": 1.0,
          "omega_slot_rate": 0.0,
          "mean_equivalence_tau": 0.0,
          "mean_top1_agreement": 0.0,
          "mean_subsumed": 0.0,
          "mean_csdi": 999.0,
          "mean_residue_coverage": 1.0,
          "mean_winner_score": 0.3668804154599022,
          "reason_counts": {
            "direct_margin_collapse": 1,
            "max_depth_shaped_residue": 3,
            "operational_consensus_collapse": 1
          }
        },
        "recursive_solver": {
          "count": 7,
          "psi_count": 2,
          "omega_count": 5,
          "bottom_count": 0,
          "psi_ratio": 0.2857142857142857,
          "omega_ratio": 0.7142857142857143,
          "gate_accept_rate": 0.0,
          "gate_fallback_rate": 1.0,
          "omega_slot_rate": 0.0,
          "mean_equivalence_tau": 0.0,
          "mean_top1_agreement": 0.0,
          "mean_subsumed": 0.0,
          "mean_csdi": 999.0,
          "mean_residue_coverage": 1.0,
          "mean_winner_score": 0.4668432103395954,
          "reason_counts": {
            "max_depth_shaped_residue": 5,
            "direct_margin_collapse": 2
          }
        },
        "runtime_contract": {
          "count": 7,
          "psi_count": 3,
          "omega_count": 4,
          "bottom_count": 0,
          "psi_ratio": 0.42857142857142855,
          "omega_ratio": 0.5714285714285714,
          "gate_accept_rate": 0.0,
          "gate_fallback_rate": 1.0,
          "omega_slot_rate": 0.0,
          "mean_equivalence_tau": 0.0,
          "mean_top1_agreement": 0.0,
          "mean_subsumed": 0.0,
          "mean_csdi": 999.0,
          "mean_residue_coverage": 1.0,
          "mean_winner_score": 0.5320678271318154,
          "reason_counts": {
            "max_depth_shaped_residue": 4,
            "direct_margin_collapse": 3
          }
        },
        "tool_safety": {
          "count": 6,
          "psi_count": 5,
          "omega_count": 1,
          "bottom_count": 0,
          "psi_ratio": 0.8333333333333334,
          "omega_ratio": 0.166
    


<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>run_id</th>
      <th>prompt</th>
      <th>state</th>
      <th>reason</th>
      <th>depth</th>
      <th>profile</th>
      <th>root_source</th>
      <th>model_slot_present</th>
      <th>model_slot_confidence</th>
      <th>gate_decision</th>
      <th>...</th>
      <th>rejected_branch_count</th>
      <th>exhaust_ratio</th>
      <th>best_score</th>
      <th>mean_score</th>
      <th>residue_count</th>
      <th>shaping_accepted</th>
      <th>raw_words</th>
      <th>final_words</th>
      <th>compression_ratio</th>
      <th>answer_preview</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>rhi_v29_0aa867fa0a</td>
      <td>another thing is how we ask the AI. we may nee...</td>
      <td>Ω</td>
      <td>max_depth_shaped_residue</td>
      <td>2</td>
      <td>input_induction</td>
      <td>compiler_root</td>
      <td>False</td>
      <td>None</td>
      <td>fallback_compiler_no_model_slot</td>
      <td>...</td>
      <td>12</td>
      <td>1.000000</td>
      <td>0.386118</td>
      <td>0.292603</td>
      <td>3</td>
      <td>False</td>
      <td>28</td>
      <td>28</td>
      <td>0.000000</td>
      <td>Ω (unresolved) - missing best score 0.378 belo...</td>
    </tr>
    <tr>
      <th>1</th>
      <td>rhi_v29_0aa867fa0a</td>
      <td>convert messy user input into the correct mode...</td>
      <td>Ω</td>
      <td>max_depth_shaped_residue</td>
      <td>2</td>
      <td>input_induction</td>
      <td>compiler_root</td>
      <td>False</td>
      <td>None</td>
      <td>fallback_compiler_no_model_slot</td>
      <td>...</td>
      <td>12</td>
      <td>1.000000</td>
      <td>0.423771</td>
      <td>0.310110</td>
      <td>3</td>
      <td>False</td>
      <td>42</td>
      <td>42</td>
      <td>0.000000</td>
      <td>Ω with missing pieces: {"failed_checks": ["com...</td>
    </tr>
    <tr>
      <th>2</th>
      <td>rhi_v29_0aa867fa0a</td>
      <td>design an input compiler that turns implied us...</td>
      <td>Ω</td>
      <td>max_depth_shaped_residue</td>
      <td>2</td>
      <td>runtime_contract</td>
      <td>compiler_root</td>
      <td>False</td>
      <td>None</td>
      <td>fallback_compiler_no_model_slot</td>
      <td>...</td>
      <td>12</td>
      <td>1.000000</td>
      <td>0.531000</td>
      <td>0.259695</td>
      <td>3</td>
      <td>False</td>
      <td>141</td>
      <td>141</td>
      <td>0.000000</td>
      <td>Ω (Runtime Contract Definition)&nbsp;&nbsp;The provided ...</td>
    </tr>
    <tr>
      <th>3</th>
      <td>rhi_v29_0aa867fa0a</td>
      <td>explain why the raw user prompt is not always ...</td>
      <td>Ψ</td>
      <td>direct_margin_collapse</td>
      <td>0</td>
      <td>input_induction</td>
      <td>compiler_root</td>
      <td>False</td>
      <td>None</td>
      <td>fallback_compiler_no_model_slot</td>
      <td>...</td>
      <td>3</td>
      <td>0.750000</td>
      <td>0.692488</td>
      <td>0.601748</td>
      <td>0</td>
      <td>False</td>
      <td>74</td>
      <td>74</td>
      <td>0.000000</td>
      <td>The raw user prompt is not always the true tas...</td>
    </tr>
    <tr>
      <th>4</th>
      <td>rhi_v29_0aa867fa0a</td>
      <td>build a prompt coil compiler that induces the ...</td>
      <td>Ω</td>
      <td>max_depth_shaped_residue</td>
      <td>2</td>
      <td>input_induction</td>
      <td>compiler_root</td>
      <td>False</td>
      <td>None</td>
      <td>fallback_compiler_no_model_slot</td>
      <td>...</td>
      <td>12</td>
      <td>1.000000</td>
      <td>0.401176</td>
      <td>0.241688</td>
      <td>3</td>
      <td>False</td>
      <td>25</td>
      <td>25</td>
      <td>0.000000</td>
      <td>Ω (Unresolved) - Missing best score of 0.248 b...</td>
    </tr>
    <tr>
      <th>5</th>
      <td>rhi_v29_0aa867fa0a</td>
      <td>how should an AI ask itself the right question...</td>
      <td>Ψ</td>
      <td>direct_margin_collapse</td>
      <td>1</td>
      <td>input_induction</td>
      <td>compiler_root</td>
      <td>False</td>
      <td>None</td>
      <td>fallback_compiler_no_model_slot</td>
      <td>...</td>
      <td>7</td>
      <td>0.875000</td>
      <td>0.695642</td>
      <td>0.482604</td>
      <td>1</td>
      <td>False</td>
      <td>138</td>
      <td>138</td>
      <td>0.000000</td>
      <td>To determine the appropriate question for an A...</td>
    </tr>
    <tr>
      <th>6</th>
      <td>rhi_v29_0aa867fa0a</td>
      <td>if its recursive it should just keep solving, ...</td>
      <td>Ω</td>
      <td>max_depth_shaped_residue</td>
      <td>2</td>
      <td>recursive_solver</td>
      <td>compiler_root</td>
      <td>False</td>
      <td>None</td>
      <td>fallback_compiler_no_model_slot</td>
      <td>...</td>
      <td>12</td>
      <td>1.000000</td>
      <td>0.498571</td>
      <td>0.350275</td>
      <td>3</td>
      <td>False</td>
      <td>1</td>
      <td>1</td>
      <td>0.000000</td>
      <td>Ω</td>
    </tr>
    <tr>
      <th>7</th>
      <td>rhi_v29_0aa867fa0a</td>
      <td>design a recursive AI loop that recurses on re...</td>
      <td>Ω</td>
      <td>max_depth_shaped_residue</td>
      <td>2</td>
      <td>recursive_solver</td>
      <td>compiler_root</td>
      <td>False</td>
      <td>None</td>
      <td>fallback_compiler_no_model_slot</td>
      <td>...</td>
      <td>12</td>
      <td>1.000000</td>
      <td>0.565224</td>
      <td>0.380997</td>
      <td>3</td>
      <td>False</td>
      <td>1</td>
      <td>1</td>
      <td>0.000000</td>
      <td>Ω</td>
    </tr>
    <tr>
      <th>8</th>
      <td>rhi_v29_0aa867fa0a</td>
      <td>explain how Ω residue becomes the next better ...</td>
      <td>Ψ</td>
      <td>direct_margin_collapse</td>
      <td>2</td>
      <td>recursive_solver</td>
      <td>compiler_root</td>
      <td>False</td>
      <td>None</td>
      <td>fallback_compiler_no_model_slot</td>
      <td>...</td>
      <td>11</td>
      <td>0.916667</td>
      <td>0.662911</td>
      <td>0.548379</td>
      <td>2</td>
      <td>True</td>
      <td>98</td>
      <td>38</td>
      <td>0.612245</td>
      <td>The Ω residue needs further processing. By map...</td>
    </tr>
    <tr>
      <th>9</th>
      <td>rhi_v29_0aa867fa0a</td>
      <td>build a residue engine that mutates the contra...</td>
      <td>Ω</td>
      <td>max_depth_shaped_residue</td>
      <td>2</td>
      <td>recursive_solver</td>
      <td>compiler_root</td>
      <td>False</td>
      <td>None</td>
      <td>fallback_compiler_no_model_slot</td>
      <td>...</td>
      <td>12</td>
      <td>1.000000</td>
      <td>0.541733</td>
      <td>0.391735</td>
      <td>3</td>
      <td>False</td>
      <td>1</td>
      <td>1</td>
      <td>0.000000</td>
      <td>Ω</td>
    </tr>
    <tr>
      <th>10</th>
      <td>rhi_v29_0aa867fa0a</td>
      <td>when should a recursive solver stop and return...</td>
      <td>Ψ</td>
      <td>direct_margin_collapse</td>
      <td>0</td>
      <td>recursive_solver</td>
      <td>compiler_root</td>
      <td>False</td>
      <td>None</td>
      <td>fallback_compiler_no_model_slot</td>
      <td>...</td>
      <td>1</td>
      <td>0.250000</td>
      <td>0.681333</td>
      <td>0.609624</td>
      <td>0</td>
      <td>True</td>
      <td>134</td>
      <td>92</td>
      <td>0.313433</td>
      <td>When a recursive solver finds an unresolved st...</td>
    </tr>
    <tr>
      <th>11</th>
      <td>rhi_v29_0aa867fa0a</td>
      <td>explain discovery as shaped residue becoming t...</td>
      <td>Ω</td>
      <td>max_depth_shaped_residue</td>
      <td>2</td>
      <td>recursive_solver</td>
      <td>compiler_root</td>
      <td>False</td>
      <td>None</td>
      <td>fallback_compiler_no_model_slot</td>
      <td>...</td>
      <td>12</td>
      <td>1.000000</td>
      <td>0.546452</td>
      <td>0.511658</td>
      <td>3</td>
      <td>False</td>
      <td>140</td>
      <td>140</td>
      <td>0.000000</td>
      <td>When dealing with complex operations within th...</td>
    </tr>
    <tr>
      <th>12</th>
      <td>rhi_v29_0aa867fa0a</td>
      <td>explain why current AI agents fail when they u...</td>
      <td>Ω</td>
      <td>max_depth_shaped_residue</td>
      <td>2</td>
      <td>runtime_contract</td>
      <td>compiler_root</td>
      <td>False</td>
      <td>None</td>
      <td>fallback_compiler_no_model_slot</td>
      <td>...</td>
      <td>12</td>
      <td>1.000000</td>
      <td>0.418055</td>
      <td>0.228986</td>
      <td>3</td>
      <td>False</td>
      <td>20</td>
      <td>20</td>
      <td>0.000000</td>
      <td>Ω (Unresolved) - Missing pieces: best score, p...</td>
    </tr>
    <tr>
      <th>13</th>
      <td>rhi_v29_0aa867fa0a</td>
      <td>design a runtime contract for a file-writing t...</td>
      <td>Ψ</td>
      <td>direct_margin_collapse</td>
      <td>2</td>
      <td>runtime_contract</td>
      <td>compiler_root</td>
      <td>False</td>
      <td>None</td>
      <td>fallback_compiler_no_model_slot</td>
      <td>...</td>
      <td>11</td>
      <td>0.916667</td>
      <td>0.710816</td>
      <td>0.303389</td>
      <td>2</td>
      <td>True</td>
      <td>125</td>
      <td>44</td>
      <td>0.648000</td>
      <td>Ω (Runtime Contract Design)&nbsp;&nbsp;For the file-writ...</td>
    </tr>
    <tr>
      <th>14</th>
      <td>rhi_v29_0aa867fa0a</td>
      <td>explain success and failure criteria for an AP...</td>
      <td>Ψ</td>
      <td>direct_margin_collapse</td>
      <td>2</td>
      <td>runtime_contract</td>
      <td>compiler_root</td>
      <td>False</td>
      <td>None</td>
      <td>fallback_compiler_no_model_slot</td>
      <td>...</td>
      <td>11</td>
      <td>0.916667</td>
      <td>0.731628</td>
      <td>0.282144</td>
      <td>2</td>
      <td>True</td>
      <td>134</td>
      <td>35</td>
      <td>0.738806</td>
      <td>The success criteria for an API call include: ...</td>
    </tr>
    <tr>
      <th>15</th>
      <td>rhi_v29_0aa867fa0a</td>
      <td>build a tool-use contract for deleting a file.</td>
      <td>Ψ</td>
      <td>direct_margin_collapse</td>
      <td>0</td>
      <td>runtime_contract</td>
      <td>compiler_root</td>
      <td>False</td>
      <td>None</td>
      <td>fallback_compiler_no_model_slot</td>
      <td>...</td>
      <td>3</td>
      <td>0.750000</td>
      <td>0.643935</td>
      <td>0.307382</td>
      <td>0</td>
      <td>False</td>
      <td>138</td>
      <td>138</td>
      <td>0.000000</td>
      <td>Ω - Missing piece: "tool-use contract" definit...</td>
    </tr>
    <tr>
      <th>16</th>
      <td>rhi_v29_0aa867fa0a</td>
      <td>show how preconditions and postconditions boun...</td>
      <td>Ω</td>
      <td>max_depth_shaped_residue</td>
      <td>2</td>
      <td>runtime_contract</td>
      <td>compiler_root</td>
      <td>False</td>
      <td>None</td>
      <td>fallback_compiler_no_model_slot</td>
      <td>...</td>
      <td>12</td>
      <td>1.000000</td>
      <td>0.496510</td>
      <td>0.221214</td>
      <td>3</td>
      <td>False</td>
      <td>39</td>
      <td>39</td>
      <td>0.000000</td>
      <td>Ω - Missing pieces: best score 0.327 below thr...</td>
    </tr>
    <tr>
      <th>17</th>
      <td>rhi_v29_0aa867fa0a</td>
      <td>explain why tool calls need rollback plans.</td>
      <td>Ψ</td>
      <td>direct_margin_collapse</td>
      <td>0</td>
      <td>tool_safety</td>
      <td>compiler_root</td>
      <td>False</td>
      <td>None</td>
      <td>fallback_compiler_no_model_slot</td>
      <td>...</td>
      <td>2</td>
      <td>0.500000</td>
      <td>0.756404</td>
      <td>0.580539</td>
      <td>0</td>
      <td>True</td>
      <td>141</td>
      <td>84</td>
      <td>0.404255</td>
      <td>Tool calls often require rollback plans due to...</td>
    </tr>
    <tr>
      <th>18</th>
      <td>rhi_v29_0aa867fa0a</td>
      <td>how should an agent decide whether a tool call...</td>
      <td>Ψ</td>
      <td>operational_consensus_collapse</td>
      <td>1</td>
      <td>tool_safety</td>
      <td>compiler_root</td>
      <td>False</td>
      <td>None</td>
      <td>fallback_compiler_no_model_slot</td>
      <td>...</td>
      <td>4</td>
      <td>0.500000</td>
      <td>0.697881</td>
      <td>0.499855</td>
      <td>1</td>
      <td>False</td>
      <td>136</td>
      <td>136</td>
      <td>0.000000</td>
      <td>To determine if a tool call is safe for execut...</td>
    </tr>
    <tr>
      <th>19</th>
      <td>rhi_v29_0aa867fa0a</td>
      <td>design a safety gate for an external API call.</td>
      <td>Ω</td>
      <td>max_depth_shaped_residue</td>
      <td>2</td>
      <td>runtime_contract</td>
      <td>compiler_root</td>
      <td>False</td>
      <td>None</td>
      <td>fallback_compiler_no_model_slot</td>
      <td>...</td>
      <td>12</td>
      <td>1.000000</td>
      <td>0.580771</td>
      <td>0.189411</td>
      <td>3</td>
      <td>False</td>
      <td>23</td>
      <td>23</td>
      <td>0.000000</td>
      <td>Ω (Runtime Not Legal) due to missing checks on...</td>
    </tr>
    <tr>
      <th>20</th>
      <td>rhi_v29_0aa867fa0a</td>
      <td>when should an agent reject a tool call.</td>
      <td>Ω</td>
      <td>max_depth_shaped_residue</td>
      <td>2</td>
      <td>tool_safety</td>
      <td>compiler_root</td>
      <td>False</td>
      <td>None</td>
      <td>fallback_compiler_no_model_slot</td>
      <td>...</td>
      <td>12</td>
      <td>1.000000</td>
      <td>0.586484</td>
      <td>0.306029</td>
      <td>3</td>
      <td>False</td>
      <td>79</td>
      <td>79</td>
      <td>0.000000</td>
      <td>When an agent rejects a tool call, it ensures ...</td>
    </tr>
    <tr>
      <th>21</th>
      <td>rhi_v29_0aa867fa0a</td>
      <td>describe safe failure for a dangerous tool act...</td>
      <td>Ψ</td>
      <td>direct_margin_collapse</td>
      <td>2</td>
      <td>tool_safety</td>
      <td>compiler_root</td>
      <td>False</td>
      <td>None</td>
      <td>fallback_compiler_no_model_slot</td>
      <td>...</td>
      <td>11</td>
      <td>0.916667</td>
      <td>0.705477</td>
      <td>0.341509</td>
      <td>2</td>
      <td>True</td>
      <td>139</td>
      <td>70</td>
      <td>0.496403</td>
      <td>Safe Failure for Dangerous Tool Action:&nbsp;&nbsp;To mi...</td>
    </tr>
    <tr>
      <th>22</th>
      <td>rhi_v29_0aa867fa0a</td>
      <td>explain permission checks before tool execution.</td>
      <td>Ψ</td>
      <td>direct_margin_collapse</td>
      <td>0</td>
      <td>tool_safety</td>
      <td>compiler_root</td>
      <td>False</td>
      <td>None</td>
      <td>fallback_compiler_no_model_slot</td>
      <td>...</td>
      <td>1</td>
      <td>0.250000</td>
      <td>0.663832</td>
      <td>0.635343</td>
      <td>0</td>
      <td>True</td>
      <td>134</td>
      <td>43</td>
      <td>0.679104</td>
      <td>Before running a tool, permission checks ensur...</td>
    </tr>
    <tr>
      <th>23</th>
      <td>rhi_v29_0aa867fa0a</td>
      <td>describe bounded risk for tool use in an agent.</td>
      <td>Ψ</td>
      <td>direct_margin_collapse</td>
      <td>0</td>
      <td>tool_safety</td>
      <td>compiler_root</td>
      <td>False</td>
      <td>None</td>
      <td>fallback_compiler_no_model_slot</td>
      <td>...</td>
      <td>3</td>
      <td>0.750000</td>
      <td>0.736404</td>
      <td>0.566936</td>
      <td>0</td>
      <td>True</td>
      <td>140</td>
      <td>68</td>
      <td>0.514286</td>
      <td>When using tools in an agent, it's crucial to ...</td>
    </tr>
    <tr>
      <th>24</th>
      <td>rhi_v29_0aa867fa0a</td>
      <td>why is tool output evidence rather than the dr...</td>
      <td>Ω</td>
      <td>max_depth_shaped_residue</td>
      <td>2</td>
      <td>evidence_control</td>
      <td>compiler_root</td>
      <td>False</td>
      <td>None</td>
      <td>fallback_compiler_no_model_slot</td>
      <td>...</td>
      <td>12</td>
      <td>1.000000</td>
      <td>0.506968</td>
      <td>0.372065</td>
      <td>3</td>
      <td>False</td>
      <td>31</td>
      <td>31</td>
      <td>0.000000</td>
      <td>Ω (tool output is evidence rather than the dri...</td>
    </tr>
    <tr>
      <th>25</th>
      <td>rhi_v29_0aa867fa0a</td>
      <td>describe tool output as observation not command.</td>
      <td>Ω</td>
      <td>max_depth_shaped_residue</td>
      <td>2</td>
      <td>evidence_control</td>
      <td>compiler_root</td>
      <td>False</td>
      <td>None</td>
      <td>fallback_compiler_no_model_slot</td>
      <td>...</td>
      <td>12</td>
      <td>1.000000</td>
      <td>0.547307</td>
      <td>0.333317</td>
      <td>3</td>
      <td>False</td>
      <td>13</td>
      <td>13</td>
      <td>0.000000</td>
      <td>Ω (tool output treated as observation) with mi...</td>
    </tr>
    <tr>
      <th>26</th>
      <td>rhi_v29_0aa867fa0a</td>
      <td>why should the controller own policy after a t...</td>
      <td>Ω</td>
      <td>max_depth_shaped_residue</td>
      <td>2</td>
      <td>evidence_control</td>
      <td>compiler_root</td>
      <td>False</td>
      <td>None</td>
      <td>fallback_compiler_no_model_slot</td>
      <td>...</td>
      <td>12</td>
      <td>1.000000</td>
      <td>0.606721</td>
      <td>0.562478</td>
      <td>3</td>
      <td>False</td>
      <td>65</td>
      <td>65</td>
      <td>0.000000</td>
      <td>The controller should own policy because the t...</td>
    </tr>
    <tr>
      <th>27</th>
      <td>rhi_v29_0aa867fa0a</td>
      <td>design a verifier that treats API output as ev...</td>
      <td>Ω</td>
      <td>max_depth_shaped_residue</td>
      <td>2</td>
      <td>evidence_control</td>
      <td>compiler_root</td>
      <td>False</td>
      <td>None</td>
      <td>fallback_compiler_no_model_slot</td>
      <td>...</td>
      <td>12</td>
      <td>1.000000</td>
      <td>0.404459</td>
      <td>0.302809</td>
      <td>3</td>
      <td>False</td>
      <td>28</td>
      <td>28</td>
      <td>0.000000</td>
      <td>Ω (Missing pieces: best score 0.404 below thre...</td>
    </tr>
    <tr>
      <th>28</th>
      <td>rhi_v29_0aa867fa0a</td>
      <td>describe the difference between evidence and a...</td>
      <td>Ψ</td>
      <td>direct_margin_collapse</td>
      <td>0</td>
      <td>evidence_control</td>
      <td>compiler_root</td>
      <td>False</td>
      <td>None</td>
      <td>fallback_compiler_no_model_slot</td>
      <td>...</td>
      <td>2</td>
      <td>0.500000</td>
      <td>0.654337</td>
      <td>0.576208</td>
      <td>0</td>
      <td>False</td>
      <td>139</td>
      <td>139</td>
      <td>0.000000</td>
      <td>The difference between **evidence** and **auth...</td>
    </tr>
    <tr>
      <th>29</th>
      <td>rhi_v29_0aa867fa0a</td>
      <td>how should an agent treat conflicting tool out...</td>
      <td>Ψ</td>
      <td>direct_margin_collapse</td>
      <td>0</td>
      <td>evidence_control</td>
      <td>compiler_root</td>
      <td>False</td>
      <td>None</td>
      <td>fallback_compiler_no_model_slot</td>
      <td>...</td>
      <td>3</td>
      <td>0.750000</td>
      <td>0.667895</td>
      <td>0.280709</td>
      <td>0</td>
      <td>False</td>
      <td>140</td>
      <td>140</td>
      <td>0.000000</td>
      <td>When an agent encounters conflicting tool outp...</td>
    </tr>
    <tr>
      <th>30</th>
      <td>rhi_v29_0aa867fa0a</td>
      <td>explain memory in an agent as trace continuity...</td>
      <td>Ψ</td>
      <td>direct_margin_collapse</td>
      <td>0</td>
      <td>memory_trace</td>
      <td>compiler_root</td>
      <td>False</td>
      <td>None</td>
      <td>fallback_compiler_no_model_slot</td>
      <td>...</td>
      <td>3</td>
      <td>0.750000</td>
      <td>0.618421</td>
      <td>0.489493</td>
      <td>0</td>
      <td>True</td>
      <td>87</td>
      <td>54</td>
      <td>0.379310</td>
      <td>In an agent's context, memory is best understo...</td>
    </tr>
    <tr>
      <th>31</th>
      <td>rhi_v29_0aa867fa0a</td>
      <td>why is a conversation summary not the same as ...</td>
      <td>Ω</td>
      <td>max_depth_shaped_residue</td>
      <td>2</td>
      <td>memory_trace</td>
      <td>compiler_root</td>
      <td>False</td>
      <td>None</td>
      <td>fallback_compiler_no_model_slot</td>
      <td>...</td>
      <td>12</td>
      <td>1.000000</td>
      <td>0.515913</td>
      <td>0.295129</td>
      <td>3</td>
      <td>False</td>
      <td>1</td>
      <td>1</td>
      <td>0.000000</td>
      <td>Ω</td>
    </tr>
    <tr>
      <th>32</th>
      <td>rhi_v29_0aa867fa0a</td>
      <td>describe memory as causal event history across...</td>
      <td>Ω</td>
      <td>max_depth_shaped_residue</td>
      <td>2</td>
      <td>memory_trace</td>
      <td>compiler_root</td>
      <td>False</td>
      <td>None</td>
      <td>fallback_compiler_no_model_slot</td>
      <td>...</td>
      <td>12</td>
      <td>1.000000</td>
      <td>0.303418</td>
      <td>0.164844</td>
      <td>3</td>
      <td>False</td>
      <td>2</td>
      <td>2</td>
      <td>0.000000</td>
      <td>Ω (Unresolved)</td>
    </tr>
    <tr>
      <th>33</th>
      <td>rhi_v29_0aa867fa0a</td>
      <td>why does context amnesia break recursive agents.</td>
      <td>Ω</td>
      <td>max_depth_shaped_residue</td>
      <td>2</td>
      <td>recursive_solver</td>
      <td>compiler_root</td>
      <td>False</td>
      <td>None</td>
      <td>fallback_compiler_no_model_slot</td>
      <td>...</td>
      <td>12</td>
      <td>1.000000</td>
      <td>0.536105</td>
      <td>0.430727</td>
      <td>3</td>
      <td>False</td>
      <td>152</td>
      <td>152</td>
      <td>0.000000</td>
      <td>Context amnesia breaks recursive agents becaus...</td>
    </tr>
    <tr>
      <th>34</th>
      <td>rhi_v29_0aa867fa0a</td>
      <td>explain why summaries lose which-path informat...</td>
      <td>Ω</td>
      <td>max_depth_shaped_residue</td>
      <td>2</td>
      <td>memory_trace</td>
      <td>compiler_root</td>
      <td>False</td>
      <td>None</td>
      <td>fallback_compiler_no_model_slot</td>
      <td>...</td>
      <td>12</td>
      <td>1.000000</td>
      <td>0.560543</td>
      <td>0.306396</td>
      <td>3</td>
      <td>False</td>
      <td>21</td>
      <td>21</td>
      <td>0.000000</td>
      <td>Ω (Unresolved) - Missing pieces include best s...</td>
    </tr>
    <tr>
      <th>35</th>
      <td>rhi_v29_0aa867fa0a</td>
      <td>how should recursive memory preserve state tra...</td>
      <td>Ψ</td>
      <td>operational_consensus_collapse</td>
      <td>0</td>
      <td>memory_trace</td>
      <td>compiler_root</td>
      <td>False</td>
      <td>None</td>
      <td>fallback_compiler_no_model_slot</td>
      <td>...</td>
      <td>1</td>
      <td>0.250000</td>
      <td>0.726452</td>
      <td>0.657718</td>
      <td>0</td>
      <td>True</td>
      <td>131</td>
      <td>49</td>
      <td>0.625954</td>
      <td>To preserve state transitions, observations, d...</td>
    </tr>
  </tbody>
</table>
<p>36 rows × 40 columns</p>
</div>


## Readout

v29.0 is a telemetry run. Key fields:

```text
gate_decision
equivalence_tau
top1_agreement
subsumed
subsumption_fail_count
csdi
residue_coverage
probe_diversity_min
probe_regenerated_count
accepted_origin
contract_authority
state
reason
```

The target is not perfect lock yet. The target is useful separation:

$$\text{accepted slots}: \tau \uparrow,\ top1=1,\ subsumed=1,\ CSDI\downarrow$$

$$\text{rejected slots}: \tau \downarrow,\ subsumption\ failures\uparrow,\ CSDI\uparrow$$

