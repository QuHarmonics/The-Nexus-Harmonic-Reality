# RHI Live Runtime v20 — Fold-Pressure Metrics Harness

Δ **Purpose:** measure recursive AI collapse dynamics instead of only checking whether one prompt succeeds.

v20 combines the stable RHI runtime with a batch harness and payload shaper. It writes exactly two run files:

1. `rhi_v20_<run_id>_bundle.json`
2. `rhi_v20_<run_id>_summary.csv`

Core path:

$$
Q \rightarrow C_Q \rightarrow B_i \rightarrow A_i^{task} \rightarrow G_{\Psi/\Omega}
\rightarrow \Psi_{raw} \rightarrow \Psi_{shaped}
$$

Measured fold-pressure ratios:

$$
H_\Omega=\frac{\#\Omega}{\#Q}
$$

$$
H_{repair}=\frac{\#(repair\rightarrow\Psi)}{\#repair\ attempts}
$$

$$
H_{exhaust}=\frac{\#rejected\ branches}{\#total\ branches}
$$

$$
H_{consensus}=\frac{\#\Psi_{consensus}}{\#\Psi}
$$

$$
H_{compression}=1-\frac{words(\Psi_{shaped})}{words(\Psi_{raw})}
$$

Reference attractor:

$$
H=\frac{\pi}{9}\approx0.34906585
$$

Rule:

$$
\boxed{\text{Do not tune thresholds to make }H\text{ appear. Measure first.}}
$$


```python

from __future__ import annotations
import os, re, sys, json, math, uuid, time, random, traceback, subprocess, importlib
from dataclasses import dataclass, asdict, field
from pathlib import Path
from collections import Counter
from typing import Any, Dict, List, Optional

ROOT = Path.cwd()
OUT_DIR = ROOT / 'rhi_v20_outputs'
OUT_DIR.mkdir(exist_ok=True)
RUN_ID = 'rhi_v20_' + uuid.uuid4().hex[:10]
SEED = 7
random.seed(SEED)

MODEL_ID_OR_PATH = os.environ.get('RHI_MODEL', 'Qwen/Qwen2.5-1.5B-Instruct')
LOAD_REAL_MODEL = True
REQUIRE_MODEL_FOR_PSI = True
AUTO_INSTALL_MISSING_DEPS = True
RUN_PROMPT_LIMIT = int(os.environ.get('RHI_PROMPT_LIMIT', '24'))
MAX_NEW_TOKENS = 240
SHAPER_MAX_NEW_TOKENS = 150
TEMPERATURE = 0.28
TOP_P = 0.88
MAX_RECURSION_DEPTH = 2
SHAPER_ENABLED = True
SHAPER_SAMPLE = False

PSI_MIN = 0.58
MARGIN_MIN = 0.045
PROMPT_FIT_MIN = 0.25
TRACE_MIN = 0.45
QUALITY_MIN_BY_PROFILE = {'runtime_contract':0.42,'memory_trace':0.34,'inverse_retrieval':0.34,'general':0.34}
CONTRACT_ECHO_MAX = 0.18
SCHEMA_ECHO_MAX = 0.25
LEGAL_TRAP_MAX = 0.04
LITERAL_SHAPE_TRAP_MAX = 0.04
CONSENSUS_SCORE_MIN = 0.58
CONSENSUS_AUDIT_MIN = 0.80
CONSENSUS_PAYLOAD_MIN = 0.70
H_TARGET = math.pi/9

print('ROOT:', ROOT)
print('OUT_DIR:', OUT_DIR)
print('RUN_ID:', RUN_ID)
print('MODEL_ID_OR_PATH:', MODEL_ID_OR_PATH)
print('H_TARGET=pi/9:', H_TARGET)

DEPENDENCY_STATUS = {'checked':True,'attempted_install':False,'missing_before':[],'missing_after':[],'errors':[]}
def _module_available(name):
    try:
        importlib.import_module(name); return True
    except Exception:
        return False

def ensure_runtime_dependencies():
    required=[('google.protobuf','protobuf'),('sentencepiece','sentencepiece')]
    missing=[pip for mod,pip in required if not _module_available(mod)]
    DEPENDENCY_STATUS['missing_before']=missing[:]
    if missing and AUTO_INSTALL_MISSING_DEPS:
        DEPENDENCY_STATUS['attempted_install']=True
        try:
            proc=subprocess.run([sys.executable,'-m','pip','install','-U']+missing,capture_output=True,text=True)
            if proc.returncode!=0:
                DEPENDENCY_STATUS['errors'].append({'returncode':proc.returncode,'stdout_tail':proc.stdout[-1500:],'stderr_tail':proc.stderr[-1500:]})
            importlib.invalidate_caches()
        except Exception as e:
            DEPENDENCY_STATUS['errors'].append({'exception':''.join(traceback.format_exception_only(type(e),e)).strip()})
    DEPENDENCY_STATUS['missing_after']=[pip for mod,pip in required if not _module_available(mod)]
    return DEPENDENCY_STATUS
DEPENDENCY_STATUS=ensure_runtime_dependencies()
print('DEPENDENCY_STATUS:', DEPENDENCY_STATUS)

tokenizer=None; model=None; MODEL_READY=False; MODEL_GENERATION_READY=False; MODEL_ERROR=None
DEVICE_INFO={'dependency_status':DEPENDENCY_STATUS}

def infer_model_device():
    import torch
    if model is None: return torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    try: return next(model.parameters()).device
    except Exception: return torch.device('cuda' if torch.cuda.is_available() else 'cpu')

def move_batch_to_device(batch, device):
    return {k:(v.to(device) if hasattr(v,'to') else v) for k,v in batch.items()}

def try_load_model(path):
    global tokenizer, model, MODEL_READY, MODEL_ERROR, DEVICE_INFO
    if not LOAD_REAL_MODEL:
        MODEL_ERROR='LOAD_REAL_MODEL=False'; return False
    try:
        import torch
        from transformers import AutoTokenizer, AutoModelForCausalLM
        DEVICE_INFO.update({'torch_version':torch.__version__,'cuda_available':bool(torch.cuda.is_available()),'device_count':int(torch.cuda.device_count())})
        if torch.cuda.is_available():
            DEVICE_INFO['gpu_name']=torch.cuda.get_device_name(0); DEVICE_INFO['cuda_version']=torch.version.cuda
        print('Torch/CUDA:', DEVICE_INFO)
        tokenizer=AutoTokenizer.from_pretrained(path, trust_remote_code=True)
        if tokenizer.pad_token_id is None and tokenizer.eos_token is not None: tokenizer.pad_token=tokenizer.eos_token
        dtype=torch.float16 if torch.cuda.is_available() else torch.float32
        kwargs=dict(trust_remote_code=True,device_map='auto' if torch.cuda.is_available() else None,low_cpu_mem_usage=True)
        try: model=AutoModelForCausalLM.from_pretrained(path,dtype=dtype,**kwargs)
        except TypeError: model=AutoModelForCausalLM.from_pretrained(path,torch_dtype=dtype,**kwargs)
        if not torch.cuda.is_available(): model.to(torch.device('cpu'))
        model.eval(); MODEL_READY=True; MODEL_ERROR=None
        print('MODEL_READY:', MODEL_READY, 'DEVICE:', infer_model_device())
        return True
    except Exception as e:
        MODEL_READY=False; MODEL_ERROR=''.join(traceback.format_exception_only(type(e),e)).strip(); print('MODEL LOAD FAILED:', MODEL_ERROR); return False

def render_messages(messages):
    if tokenizer is not None and hasattr(tokenizer,'apply_chat_template'):
        try:
            s=tokenizer.apply_chat_template(messages,tokenize=False,add_generation_prompt=True)
            if isinstance(s,str) and s.strip(): return s
        except Exception as e: print('chat_template failed:', type(e).__name__, e)
    return '\n\n'.join([m.get('role','user').upper()+':\n'+m.get('content','') for m in messages]+['ASSISTANT:\n'])

def raw_model_generate(messages,max_new_tokens=80,sample=False):
    import torch
    if not MODEL_READY: raise RuntimeError('Model is not loaded.')
    device=infer_model_device(); rendered=render_messages(messages)
    inputs=move_batch_to_device(tokenizer(rendered,return_tensors='pt'),device)
    kwargs=dict(max_new_tokens=max_new_tokens,pad_token_id=tokenizer.pad_token_id if tokenizer.pad_token_id is not None else tokenizer.eos_token_id,eos_token_id=tokenizer.eos_token_id)
    kwargs.update(dict(do_sample=True,temperature=TEMPERATURE,top_p=TOP_P) if sample else dict(do_sample=False))
    with torch.no_grad(): out=model.generate(**inputs,**kwargs)
    gen=out[0][inputs['input_ids'].shape[-1]:]
    return tokenizer.decode(gen,skip_special_tokens=True).strip()

_ = try_load_model(MODEL_ID_OR_PATH)
try:
    smoke=raw_model_generate([{'role':'system','content':'You are a runtime smoke test.'},{'role':'user','content':'Reply with one short sentence containing READY.'}],40,False)
    MODEL_GENERATION_READY=bool(smoke.strip()); print('MODEL_GENERATION_READY:', MODEL_GENERATION_READY); print('SMOKE:', smoke)
except Exception as e:
    MODEL_GENERATION_READY=False; MODEL_ERROR=''.join(traceback.format_exception_only(type(e),e)).strip(); print('MODEL GENERATION FAILED:', MODEL_ERROR)

STOPWORDS=set('the a an and or but if then else of to in on for with by as is are was were be being been it this that these those from at into out about so because therefore than not no yes do does did can could should would will just they them their you your we our i me my he she his her its what how why when'.split())
NEXUS_SURFACE_TERMS=set('nexus contract carrier domain boundary collapse shape value slot need forbidden neighbor operational recursive recursion krrb omega psi field fold runtime phase lock audit trace signal evidence branch repair candidate construct verify counter prompt polysemy profile'.split())
CONTRACT_ECHO_MARKERS=['prompt:','inverse need:','preserved function:','boundary conditions:','domain carrier:','forbidden neighbors:','polysemy lock:','collapse target:','repair history:','active_templates','required_meaning','forbidden_meaning','clean_prompt','semantic trap','model origin','runtime-contract fit']
SCHEMA_ECHO_MARKERS=['precondition:','postcondition:','success criteria:','failure criteria:','allowed side effects:','rollback mechanism:','runtime path:','corrected runtime path:','repair target:','need-slot contract:']
LEGAL_TRAP_TERMS=['legal','legally','law','liability','stakeholder','stakeholders','signed','binding agreement','parties','compliance','enforceable','contractual obligations','breach','confidentiality']
LITERAL_SHAPE_TRAP_TERMS=['circle','sphere','oval','ellipse','round object','visual characteristics']

def words(text, remove_nexus_surface=False):
    toks=re.findall(r'[a-zA-Z0-9_ΔΨΩ⊕↻⊥]+',str(text).lower())
    toks=[t for t in toks if t not in STOPWORDS and len(t)>1]
    if remove_nexus_surface: toks=[t for t in toks if t not in NEXUS_SURFACE_TERMS]
    return toks

def wordset(text, remove_nexus_surface=False): return set(words(text,remove_nexus_surface))
def jaccard_text(a,b,remove_nexus_surface=False):
    wa,wb=wordset(a,remove_nexus_surface),wordset(b,remove_nexus_surface)
    if not wa and not wb: return 1.0
    if not wa or not wb: return 0.0
    return len(wa&wb)/max(1,len(wa|wb))
def contains_any(text,terms):
    s=str(text).lower(); return any(str(t).lower() in s for t in terms)
def clamp(x,lo=0.0,hi=1.0): return max(lo,min(hi,float(x)))
def harmonic_mean(vals,eps=1e-9):
    vals=[max(eps,float(v)) for v in vals]; return len(vals)/sum(1/v for v in vals)
def field_hit_score(text,terms,max_terms=12):
    if not terms: return 0.5
    s=str(text).lower(); uniq=[]
    for t in terms:
        t=str(t).lower().strip()
        if t and t not in uniq: uniq.append(t)
    uniq=uniq[:max_terms]
    return clamp(sum(1 for t in uniq if t in s)/max(1,len(uniq)))
def marker_penalty(text,markers,scale=6): return clamp(sum(1 for m in markers if m in str(text).lower())/max(1,scale))
def contract_echo_penalty(text):
    s=str(text).lower(); return clamp(marker_penalty(s,CONTRACT_ECHO_MARKERS,5)+(0.20 if ('{' in s and '}' in s and ':' in s) else 0)+(0.25 if len(re.findall(r'\*\*[^*]+:\*\*',str(text)))>=4 else 0))
def schema_echo_penalty(text): return marker_penalty(text,SCHEMA_ECHO_MARKERS,5)
def legal_trap_penalty(text):
    s=str(text).lower(); return clamp(sum(1 for t in LEGAL_TRAP_TERMS if t in s)/5)
def literal_shape_trap_penalty(prompt,answer):
    if 'shape-first retrieval' not in prompt.lower(): return 0.0
    s=answer.lower(); return clamp(sum(1 for t in LITERAL_SHAPE_TRAP_TERMS if t in s)/2)
def payload_text(answer):
    lines=str(answer).splitlines(); kept=[]
    skip=tuple(m.replace(':','').lower() for m in CONTRACT_ECHO_MARKERS+SCHEMA_ECHO_MARKERS)
    for line in lines:
        cleaned=line.strip().strip('*# ').lower().replace('**','')
        if any(cleaned.startswith(m) for m in skip): continue
        if '{' in line and '}' in line and ':' in line: continue
        kept.append(line)
    return '\n'.join(kept).strip() or str(answer).strip()
def count_words(text): return len(re.findall(r'\b\w+\b',str(text)))
def preview(text,n=260):
    s=re.sub(r'\s+',' ',str(text)).strip(); return s[:n]+('...' if len(s)>n else '')

SHAPE_TEMPLATES={
 'CONTRACT':{'needs':['runtime','precondition','postcondition','success','failure','rollback','trace']},
 'SEARCH':{'needs':['inverse','fit','candidate','rank','verify','evidence']},
 'MEMORY':{'needs':['state','trace','retrieve','preserve','update','continuity']},
 'TOOL':{'needs':['tool','input','output','side-effect','verify']},
 'REPAIR':{'needs':['failure','cause','patch','test','rerun','trace']},
 'GENERAL':{'needs':['answer','because','operation','result','test']},
}
@dataclass
class NeedSlotContract:
    prompt:str; clean_prompt:str; active_templates:List[str]; task_profile:str; inverse_need:str; preserved_function:str; boundary_conditions:List[str]; domain_carrier:List[str]; forbidden_neighbors:List[str]; polysemy_lock:Dict[str,Dict[str,str]]; collapse_target:str; repair_history:List[Dict[str,Any]]=field(default_factory=list)

def detect_shape_template(prompt):
    p=prompt.lower(); active=[]
    if ('contract' in p and ('tool' in p or 'runtime' in p or 'before' in p)) or 'precondition' in p or 'postcondition' in p: active.append('CONTRACT')
    if 'tool' in p or 'api' in p or 'function call' in p: active.append('TOOL')
    if any(t in p for t in ['memory','remember','continuity','trace continuity']): active.append('MEMORY')
    if any(t in p for t in ['search','retrieve','retrieval','noun match','shape-first']): active.append('SEARCH')
    if any(t in p for t in ['fix','repair','error','failed','broken','traceback']): active.append('REPAIR')
    return sorted(set(active)) or ['GENERAL']

def infer_task_profile(prompt,active):
    p=prompt.lower()
    if 'MEMORY' in active and not ('tool' in p and 'contract' in p): return 'memory_trace'
    if 'SEARCH' in active or 'shape-first retrieval' in p or 'noun match' in p: return 'inverse_retrieval'
    if 'CONTRACT' in active or ('tool' in p and 'before' in p): return 'runtime_contract'
    return 'general'

def extract_domain_terms(prompt,max_terms=14): return [w for w,_ in Counter(words(prompt,True)).most_common(max_terms)]
def shape_score(text,active):
    masses=[]
    for name in active:
        needs=SHAPE_TEMPLATES.get(name,{}).get('needs',[])
        if needs: masses.append(sum(1 for n in needs if n in text.lower())/len(needs))
    return clamp(sum(masses)/max(1,len(masses))) if masses else 0.5

def build_contract(prompt,repair_history=None):
    clean=str(prompt).strip(); active=detect_shape_template(clean); profile=infer_task_profile(clean,active); domain=extract_domain_terms(clean)
    if profile=='runtime_contract':
        preserved='form a runtime execution contract before tool use'
        boundaries=['answer directly; do not print internal contract/spec','contract means runtime execution contract, not legal agreement','reject legal/stakeholder/liability framing','require model-origin payload']
        forb=['api reflex','binding agreement interpretation','legal contract interpretation','premature execution','stakeholder/legal framing','tool-first action']
        poly={'contract':{'required_meaning':'runtime execution contract: preconditions, postconditions, success criteria, failure criteria, side effects, rollback, trace update','forbidden_meaning':'legal agreement'},'tool':{'required_meaning':'external function/API/action channel','forbidden_meaning':'generic physical tool'}}
    elif profile=='memory_trace':
        preserved='preserve trace continuity across turns rather than compressing state into summary text'
        boundaries=['answer directly; do not print internal contract/spec','memory means causal trace continuity, not text summary or precondition checklist','require model-origin payload']
        forb=['context amnesia','precondition checklist as explanation','stateless answer','summary as memory','surface recall']; poly={}
    elif profile=='inverse_retrieval':
        preserved='retrieve by inverse operational fit when no noun match exists'
        boundaries=['answer directly; do not print internal contract/spec','shape means operational fit/inverse need, not literal geometry','require model-origin payload']
        forb=['keyword matching','literal shape example','noun lookup','search without verifier','unverified retrieval']; poly={}
    else:
        preserved="preserve the prompt's verb-level operation"; boundaries=['answer directly','require model-origin payload']; forb=['surface label','generic explanation','noun-only answer']; poly={}
    return NeedSlotContract(clean,clean,active,profile,'construct the missing operational slot; answer directly; reject wrong carriers',preserved,boundaries,domain,forb,poly,'one executable answer with model origin, direct payload, task-local fit, prompt grounding, semantic trap rejection, and trace sufficient to debug',repair_history or [])

def contract_model_hint(c):
    if c.task_profile=='runtime_contract': return "Contract means runtime execution constraints for tool use, not law. Use preconditions, side effects, success/failure criteria, rollback, and trace update."
    if c.task_profile=='memory_trace': return "Explain memory as causal trace continuity: state transitions, observations, decisions, tool calls, updates, rollback. Not a text summary or checklist."
    if c.task_profile=='inverse_retrieval': return "Design retrieval by inverse operational fit when no noun match exists: need, candidate generation, rank, verify, select. Shape is not literal geometry."
    return 'Answer directly and preserve the main operation.'

BRANCH_SYSTEMS={'construct':'Constructor branch. Produce the direct answer payload only.','verify':'Verifier branch. Preserve the task operation and reject the wrong carrier.','repair':'Repair branch. Produce the minimal corrected payload.','counter':'Counter branch. Name the wrong path briefly, then give the corrected answer.'}
def deterministic_branch(prompt,c,b,reason='fallback'):
    return {'branch':b,'answer':f'Diagnostic fallback for {b}. This is not a model answer.','origin':reason,'generation_error':MODEL_ERROR}
def model_generate_one(prompt,c,b):
    if not MODEL_GENERATION_READY: return deterministic_branch(prompt,c,b,'fallback_model_not_ready')
    repair_note=''
    if c.repair_history: repair_note='\nPrior failed observable: '+str(c.repair_history[-1].get('weakest_observable','unknown'))+'. Correct that only.'
    user='PROMPT:\n'+prompt+'\n\nRUNTIME GUIDANCE:\n'+contract_model_hint(c)+repair_note+'\n\nRules: answer directly; do not print scoring schema; keep it operational and testable.'
    try:
        text=raw_model_generate([{'role':'system','content':BRANCH_SYSTEMS[b]},{'role':'user','content':user}],MAX_NEW_TOKENS,True)
        return {'branch':b,'answer':text.strip() or '','origin':'model','generation_error':None} if text.strip() else deterministic_branch(prompt,c,b,'fallback_empty_generation')
    except Exception as e:
        return {**deterministic_branch(prompt,c,b,'fallback_error'),'generation_error':''.join(traceback.format_exception_only(type(e),e)).strip()}
def generate_candidates(prompt,c): return [model_generate_one(prompt,c,b) for b in BRANCH_SYSTEMS]

def task_terms(profile):
    return {'runtime_contract':['runtime','precondition','postcondition','success','failure','side effect','rollback','trace','tool','constraint'], 'memory_trace':['memory','trace','state','transition','observation','decision','update','continuity','causal','turn'], 'inverse_retrieval':['inverse','operational','fit','candidate','rank','verify','retrieval','noun','match','need']}.get(profile,['answer','because','operation','result','test'])

def task_quality(c,payload,m):
    if c.task_profile=='runtime_contract': vals=[m['F_function'],m['F_task'],m['F_prompt'],m['F_polysemy'],1-m['legal_trap_penalty'],m['payload_validity']]
    elif c.task_profile=='memory_trace': vals=[m['F_function'],m['F_task'],m['F_prompt'],1-m['schema_echo_penalty'],m['payload_validity']]
    elif c.task_profile=='inverse_retrieval': vals=[m['F_function'],m['F_task'],m['F_prompt'],1-m['literal_shape_trap_penalty'],m['payload_validity']]
    else: vals=[m['F_function'],m['F_prompt'],m['payload_validity']]
    return harmonic_mean(vals)

def answer_operational_audit(prompt,c,answer,origin):
    payload=payload_text(answer); a=payload.lower()
    fields={'need':words(c.inverse_need,True),'function':words(c.preserved_function,True),'domain':c.domain_carrier,'forbidden':words(' '.join(c.forbidden_neighbors),True),'collapse':words(c.collapse_target,True),'task':task_terms(c.task_profile)}
    F_need=clamp(.55*field_hit_score(payload,fields['need'])+.45*field_hit_score(payload,fields['domain']))
    F_function=clamp(.65*field_hit_score(payload,fields['function'])+.35*field_hit_score(payload,fields['task']))
    F_boundary=clamp(.5*sum([contains_any(a,['reject','avoid','not','instead','without']),contains_any(a,['constraint','criteria','boundary','failure','rollback','verify'])])/2+.5*(1-contract_echo_penalty(answer)))
    F_trap=clamp(.5*field_hit_score(payload,fields['forbidden'])+.5*sum([contains_any(a,['not','instead','wrong','fails','reject','avoid']),contains_any(a,['noun','summary','legal','premature','unverified','tool-first'])])/2)
    F_collapse=clamp(.5*field_hit_score(payload,fields['collapse'])+.5*sum([contains_any(a,['because','therefore','so','result','ensures','prevents']),contains_any(a,['step','criteria','verify','test','trace','select'])])/2)
    F_shape=shape_score(payload,c.active_templates); F_task=field_hit_score(payload,fields['task']); F_prompt=field_hit_score(payload,words(prompt,True),12)
    ce=contract_echo_penalty(answer); se=schema_echo_penalty(answer); lp=legal_trap_penalty(payload); sp=literal_shape_trap_penalty(prompt,payload)
    if c.task_profile!='runtime_contract': lp=min(lp,.10)
    if c.task_profile!='inverse_retrieval': sp=0.0
    pw=count_words(payload); payload_validity=clamp((pw-12)/38)
    if 'diagnostic fallback' in payload.lower() or 'not a model answer' in payload.lower(): payload_validity=0.0
    F_polysemy=1.0
    if c.task_profile=='runtime_contract':
        req=field_hit_score(payload,['precondition','success','failure','rollback','trace','tool'],6)
        forbid=clamp(sum(1 for t in ['legal','stakeholder','signed','liability','binding agreement','parties','compliance'] if t in payload.lower())/3)
        F_polysemy=clamp(req*(1-forbid))
    O_model=1.0 if origin=='model' else 0.0
    m={'F_need':F_need,'F_function':F_function,'F_boundary':F_boundary,'F_trap':F_trap,'F_collapse':F_collapse,'F_shape':F_shape,'F_task':F_task,'F_prompt':F_prompt,'F_polysemy':F_polysemy,'payload_validity':payload_validity,'contract_echo_penalty':ce,'schema_echo_penalty':se,'legal_trap_penalty':lp,'literal_shape_trap_penalty':sp,'O_model':O_model}
    q=task_quality(c,payload,m); hot=clamp((F_function+F_task+F_prompt+F_polysemy)/4); cold=clamp((F_boundary+F_trap+F_collapse+payload_validity)/4); bal=1-abs(hot-cold)
    score=clamp(.24*q+.14*F_prompt+.13*F_task+.12*F_function+.10*payload_validity+.10*O_model+.07*bal+.10*(1-max(ce,se,lp,sp)))
    m.update({'score':score,'task_profile':c.task_profile,'contract_stance':clamp((F_need+F_function+F_boundary+F_trap+F_collapse)/5),'trace_sufficiency':clamp(sum([contains_any(payload,['because','therefore','so','ensures','prevents']),contains_any(payload,['state','trace','rollback','verify','criteria','rank','precondition']),count_words(payload)>=45])/3),'quality_hmean':q,'hot':hot,'cold':cold,'hotcold_balance':bal,'payload_text':payload})
    return m

def branch_failure_reasons(a):
    failed=[]; qmin=QUALITY_MIN_BY_PROFILE.get(a['task_profile'],.34)
    if REQUIRE_MODEL_FOR_PSI and a['O_model']<1: failed.append('model_origin')
    if a['score']<PSI_MIN: failed.append('score')
    if a['trace_sufficiency']<TRACE_MIN: failed.append('trace')
    if a['quality_hmean']<qmin: failed.append('quality')
    if a['F_prompt']<PROMPT_FIT_MIN: failed.append('prompt_fit')
    if a['payload_validity']<.70: failed.append('payload')
    if a['contract_echo_penalty']>CONTRACT_ECHO_MAX: failed.append('contract_echo')
    if a['schema_echo_penalty']>SCHEMA_ECHO_MAX: failed.append('schema_echo')
    if a['task_profile']=='runtime_contract':
        if a['F_polysemy']<.30: failed.append('polysemy_lock')
        if a['legal_trap_penalty']>LEGAL_TRAP_MAX: failed.append('legal_trap')
    if a['task_profile']=='inverse_retrieval' and a['literal_shape_trap_penalty']>LITERAL_SHAPE_TRAP_MAX: failed.append('literal_shape_trap')
    return failed

def direct_gate(audits):
    top=audits[0]; second=audits[1] if len(audits)>1 else None; margin=top['score']-(second['score'] if second else 0)
    failed=branch_failure_reasons(top)
    if margin<MARGIN_MIN: failed.append('margin')
    return {'ok':not failed,'reason':'direct_margin_collapse' if not failed else 'no_direct_collapse','failed':failed,'margin':margin,'top_score':top['score'],'top_origin':top['origin'],'task_profile':top['task_profile'],'trace_sufficiency':top['trace_sufficiency'],'quality_hmean':top['quality_hmean'],'quality_min':QUALITY_MIN_BY_PROFILE.get(top['task_profile'],.34),'F_prompt':top['F_prompt'],'F_polysemy':top['F_polysemy'],'payload_validity':top['payload_validity'],'contract_echo_penalty':top['contract_echo_penalty'],'schema_echo_penalty':top['schema_echo_penalty'],'legal_trap_penalty':top['legal_trap_penalty'],'literal_shape_trap_penalty':top['literal_shape_trap_penalty']}

def audit_vector(a): return [a[k] for k in ['F_function','F_task','F_prompt','quality_hmean','payload_validity','F_polysemy']]
def vector_agreement(a,b): return clamp(1-sum(abs(x-y) for x,y in zip(audit_vector(a),audit_vector(b)))/6)
def consensus_gate(audits):
    if len(audits)<2: return {'ok':False,'reason':'not_enough_branches'}
    top,second=audits[0],audits[1]; margin=top['score']-second['score']; agreement=vector_agreement(top,second); payload_agree=jaccard_text(top['payload_text'],second['payload_text'],True)
    top_fail=branch_failure_reasons(top); second_fail=branch_failure_reasons(second)
    ok=top['score']>=CONSENSUS_SCORE_MIN and second['score']>=CONSENSUS_SCORE_MIN and agreement>=CONSENSUS_AUDIT_MIN and top['payload_validity']>=CONSENSUS_PAYLOAD_MIN and second['payload_validity']>=CONSENSUS_PAYLOAD_MIN and not top_fail and not second_fail
    return {'ok':ok,'reason':'consensus_collapse' if ok else 'no_consensus','margin':margin,'audit_agreement':agreement,'payload_agreement':payload_agree,'top_fail_no_margin':top_fail,'second_fail_no_margin':second_fail}

def weakest_observable(a):
    c={'function':a['F_function'],'task':a['F_task'],'prompt':a['F_prompt'],'quality':a['quality_hmean'],'payload':a['payload_validity'],'polysemy':a['F_polysemy'],'contract_echo':1-a['contract_echo_penalty'],'schema_echo':1-a['schema_echo_penalty'],'legal_trap':1-a['legal_trap_penalty'],'literal_shape':1-a['literal_shape_trap_penalty']}
    return min(c,key=c.get)

def resolve_prompt(prompt):
    trace=[]; repairs=[]
    for depth in range(MAX_RECURSION_DEPTH+1):
        c=build_contract(prompt,repairs); cand=generate_candidates(prompt,c); audits=[]
        for x in cand:
            m=answer_operational_audit(prompt,c,x['answer'],x['origin']); audits.append({**x,**{k:v for k,v in m.items() if k!='payload_text'},'payload_text':m['payload_text']})
        audits=sorted(audits,key=lambda x:x['score'],reverse=True); dg=direct_gate(audits); cg=consensus_gate(audits)
        node={'depth':depth,'contract':asdict(c),'scores':audits,'direct_gate':dg,'consensus_gate':cg,'branch_rejections':sum(1 for a in audits if branch_failure_reasons(a)),'total_branches':len(audits)}; trace.append(node)
        if dg['ok'] or cg['ok']:
            w=audits[0]; return {'run_id':RUN_ID,'prompt':prompt,'state':'Ψ','reason':dg['reason'] if dg['ok'] else cg['reason'],'depth':depth,'winner_branch':w['branch'],'winner_origin':w['origin'],'winner_score':w['score'],'raw_winner_answer':w['answer'],'answer':w['payload_text'],'payload':w['payload_text'],'contract':asdict(c),'trace':trace,'repair_attempts':len(repairs),'branch_rejections':sum(t['branch_rejections'] for t in trace),'total_branches':sum(t['total_branches'] for t in trace)}
        top=audits[0]; repairs.append({'failed_gate':dg['failed'],'consensus_reason':cg['reason'],'weakest_observable':weakest_observable(top),'winner_branch':top['branch'],'winner_origin':top['origin'],'winner_score':top['score'],'quality_hmean':top['quality_hmean'],'payload_validity':top['payload_validity']})
    c=build_contract(prompt,repairs); w=trace[-1]['scores'][0]; reason='model_generation_failed' if w['origin']!='model' else 'max_depth_residue'
    return {'run_id':RUN_ID,'prompt':prompt,'state':'Ω','reason':reason,'depth':trace[-1]['depth'],'winner_branch':w['branch'],'winner_origin':w['origin'],'winner_score':w['score'],'raw_winner_answer':w['answer'],'answer':w['payload_text'],'payload':w['payload_text'],'contract':asdict(c),'trace':trace,'repair_attempts':len(repairs),'branch_rejections':sum(t['branch_rejections'] for t in trace),'total_branches':sum(t['total_branches'] for t in trace)}

def shape_payload(prompt,c,raw_payload):
    raw_payload=str(raw_payload).strip()
    if not SHAPER_ENABLED or not MODEL_GENERATION_READY:
        return {'shaped_payload':raw_payload,'shaping_attempted':False,'shaping_accepted':False,'shaping_error':None,'raw_words':count_words(raw_payload),'shaped_words':count_words(raw_payload),'compression_ratio':0.0}
    target={'runtime_contract':'Compress to 120-170 words. Explain runtime contract before tool use. Keep preconditions, side effects, success/failure, rollback, trace.','memory_trace':'Compress to 100-150 words. Explain memory as trace continuity, not summary.','inverse_retrieval':'Compress to 100-150 words. Give a direct inverse-fit retrieval step: need, candidates, rank, verify, select.'}.get(c.task_profile,'Compress to 100-150 words while preserving meaning.')
    try:
        shaped=raw_model_generate([{'role':'system','content':'You are a payload shaper. Preserve meaning. Remove filler. Do not add new claims.'},{'role':'user','content':f'PROMPT:\n{prompt}\n\nTASK:\n{target}\n\nRAW PAYLOAD:\n{raw_payload}\n\nReturn only the shaped answer.'}],SHAPER_MAX_NEW_TOKENS,SHAPER_SAMPLE).strip()
        if not shaped: raise RuntimeError('empty shaped payload')
        ra=answer_operational_audit(prompt,c,raw_payload,'model'); sa=answer_operational_audit(prompt,c,shaped,'model')
        rw=count_words(raw_payload); sw=count_words(shaped); comp=clamp(1-sw/max(1,rw),-1,1)
        qmin=QUALITY_MIN_BY_PROFILE.get(c.task_profile,.34)
        accepted=sa['payload_validity']>=.70 and sa['quality_hmean']>=max(.75*qmin,.25) and sa['F_prompt']>=max(.70*ra['F_prompt'],.20) and sa['contract_echo_penalty']<=CONTRACT_ECHO_MAX and sa['schema_echo_penalty']<=SCHEMA_ECHO_MAX and sa['legal_trap_penalty']<=max(LEGAL_TRAP_MAX,ra['legal_trap_penalty']+.02) and sa['literal_shape_trap_penalty']<=max(LITERAL_SHAPE_TRAP_MAX,ra['literal_shape_trap_penalty']+.02)
        return {'shaped_payload':shaped if accepted else raw_payload,'shaping_attempted':True,'shaping_accepted':bool(accepted),'shaping_error':None,'raw_words':rw,'shaped_words':sw if accepted else rw,'compression_ratio':comp if accepted else 0.0,'raw_score':ra['score'],'shaped_score':sa['score'],'raw_quality':ra['quality_hmean'],'shaped_quality':sa['quality_hmean']}
    except Exception as e:
        return {'shaped_payload':raw_payload,'shaping_attempted':True,'shaping_accepted':False,'shaping_error':''.join(traceback.format_exception_only(type(e),e)).strip(),'raw_words':count_words(raw_payload),'shaped_words':count_words(raw_payload),'compression_ratio':0.0}

def apply_payload_shaping(res):
    c=build_contract(res['prompt'],res.get('contract',{}).get('repair_history',[])); raw=res['payload']; shape=shape_payload(res['prompt'],c,raw); res['raw_payload']=raw; res['payload']=shape['shaped_payload']; res['answer']=shape['shaped_payload']; res['payload_shaping']=shape; return res

DEFAULT_PROMPTS=[
'explain why current AI agents fail when they use tools before forming a contract','explain why a tool call should have preconditions before execution','describe how rollback protects an agent after a failed API call','why is tool output evidence rather than the driver of the agent','design a runtime contract for a file-writing tool','explain how side effects break an agent when they are not bounded','how should an agent decide whether a tool call is safe','explain contract-first tool use without legal language',
'explain memory in an agent as trace continuity rather than a text summary','why is a conversation summary not the same as agent memory','describe agent memory as state transitions observations decisions and updates','explain how trace continuity helps an agent recover after a mistake','how does rollback relate to memory in an agent runtime','describe memory as causal event history across turns','why does context amnesia break recursive agents','explain how an agent should preserve prior state without storing everything',
'design a shape-first retrieval step where no noun match exists but the inverse need is clear','how should retrieval work when keywords fail but the operation is obvious','explain inverse operational fit for search without noun matching','design a verifier for retrieval candidates selected by need rather than label','how can an agent rank candidates by function instead of name','describe retrieval by missing slot rather than surface term','build a retrieval step that rejects keyword-only matches','explain why literal shape examples are wrong for shape-first retrieval',
'fix an answer that sounds right but does not perform the requested operation','explain why agreement between branches can still be false consensus','describe how to reject a fluent answer that preserves the wrong carrier','explain why uncertainty can be safer than premature certainty','design a small audit that detects when an answer only repeats the rubric','explain how a controller should separate payload from scoring criteria','why should a runtime preserve Ω instead of forcing Ψ','describe a recursive repair loop without using threshold fiddling']
USER_PROMPTS=[]
PROMPTS=(USER_PROMPTS or DEFAULT_PROMPTS)[:RUN_PROMPT_LIMIT]
print('Prompt count:',len(PROMPTS))

import pandas as pd
START=time.time(); results={}
for i,p in enumerate(PROMPTS,1):
    print('\n'+'='*100); print(f'[{i}/{len(PROMPTS)}] PROMPT:',p)
    res=apply_payload_shaping(resolve_prompt(p)); results[p]=res
    print('STATE:',res['state'],'REASON:',res['reason'],'DEPTH:',res['depth'],'WINNER:',res['winner_branch'],res['winner_origin'],round(res['winner_score'],4))
    print('SHAPED:',res.get('payload_shaping',{}).get('shaping_accepted'),'COMPRESSION:',round(res.get('payload_shaping',{}).get('compression_ratio',0),4))
    print('ANSWER:',preview(res['answer'],320))
ELAPSED=time.time()-START

def counts(res):
    trace=res.get('trace',[]); last=trace[-1] if trace else {}; return {'direct_ok':bool(last.get('direct_gate',{}).get('ok',False)),'consensus_ok':bool(last.get('consensus_gate',{}).get('ok',False)),'total_branches':res.get('total_branches',0),'rejected_branches':res.get('branch_rejections',0)}
rows=[]
for p,res in results.items():
    c=counts(res); sh=res.get('payload_shaping',{}) or {}; contract=res.get('contract',{})
    rows.append({'run_id':RUN_ID,'prompt':p,'task_profile':contract.get('task_profile'),'state':res.get('state'),'reason':res.get('reason'),'depth':res.get('depth'),'winner_branch':res.get('winner_branch'),'winner_origin':res.get('winner_origin'),'winner_score':res.get('winner_score'),'direct_ok':c['direct_ok'],'consensus_ok':c['consensus_ok'],'repair_attempts':res.get('repair_attempts',0),'total_branches':c['total_branches'],'rejected_branches':c['rejected_branches'],'exhaust_ratio':c['rejected_branches']/max(1,c['total_branches']),'raw_words':sh.get('raw_words',count_words(res.get('raw_payload',res.get('payload','')))),'shaped_words':sh.get('shaped_words',count_words(res.get('payload',''))),'compression_ratio':sh.get('compression_ratio',0.0),'shaping_attempted':sh.get('shaping_attempted',False),'shaping_accepted':sh.get('shaping_accepted',False),'answer_preview':preview(res.get('answer',''),240)})
summary_df=pd.DataFrame(rows)
def ratio(n,d): return float(n)/float(d) if d else 0.0
n=len(summary_df); npsi=int((summary_df.state=='Ψ').sum()) if n else 0; nomega=int((summary_df.state=='Ω').sum()) if n else 0
nrepair=int((summary_df.repair_attempts>0).sum()) if n else 0; nrepairpsi=int(((summary_df.repair_attempts>0)&(summary_df.state=='Ψ')).sum()) if n else 0
ncons=int(((summary_df.state=='Ψ')&(summary_df.reason=='consensus_collapse')).sum()) if n else 0; ndirect=int(((summary_df.state=='Ψ')&(summary_df.reason=='direct_margin_collapse')).sum()) if n else 0
branches=int(summary_df.total_branches.sum()) if n else 0; rejected=int(summary_df.rejected_branches.sum()) if n else 0; shaped=int(summary_df.shaping_accepted.sum()) if n else 0
pressure_metrics={'H_target_pi_over_9':H_TARGET,'total_prompts':n,'psi_count':npsi,'omega_count':nomega,'H_omega_ratio':ratio(nomega,n),'H_psi_ratio':ratio(npsi,n),'repair_prompt_count':nrepair,'repair_to_psi_count':nrepairpsi,'H_repair_success':ratio(nrepairpsi,nrepair),'total_branches':branches,'rejected_branches':rejected,'H_exhaust_ratio':ratio(rejected,branches),'consensus_psi_count':ncons,'direct_psi_count':ndirect,'H_consensus_ratio':ratio(ncons,npsi),'H_direct_ratio':ratio(ndirect,npsi),'H_compression_mean':float(summary_df.compression_ratio.mean()) if n else 0.0,'H_compression_median':float(summary_df.compression_ratio.median()) if n else 0.0,'shaping_accepted_ratio':ratio(shaped,n),'mean_winner_score':float(summary_df.winner_score.mean()) if n else 0.0,'mean_depth':float(summary_df.depth.mean()) if n else 0.0,'elapsed_seconds':ELAPSED}
for k in list(pressure_metrics):
    if k.startswith('H_') and k!='H_target_pi_over_9': pressure_metrics[k+'_abs_delta_from_pi_over_9']=abs(float(pressure_metrics[k])-H_TARGET)
print('\nFold-pressure metrics:')
for k,v in pressure_metrics.items(): print(k,':',round(v,6) if isinstance(v,float) else v)

bundle={'run_id':RUN_ID,'created_root':str(ROOT),'out_dir':str(OUT_DIR),'model_id_or_path':MODEL_ID_OR_PATH,'load_real_model':LOAD_REAL_MODEL,'require_model_for_psi':REQUIRE_MODEL_FOR_PSI,'model_ready':MODEL_READY,'model_generation_ready':MODEL_GENERATION_READY,'model_error':MODEL_ERROR,'dependency_status':DEPENDENCY_STATUS,'device_info':DEVICE_INFO,'config':{'run_prompt_limit':RUN_PROMPT_LIMIT,'max_recursion_depth':MAX_RECURSION_DEPTH,'shaper_enabled':SHAPER_ENABLED,'H_target_pi_over_9':H_TARGET},'prompts':PROMPTS,'pressure_metrics':pressure_metrics,'summary':summary_df.to_dict(orient='records'),'results':results}
bundle_path=OUT_DIR/f'{RUN_ID}_bundle.json'; summary_path=OUT_DIR/f'{RUN_ID}_summary.csv'
with open(bundle_path,'w',encoding='utf-8') as f: json.dump(bundle,f,ensure_ascii=False,indent=2)
summary_df.to_csv(summary_path,index=False)
print('\nSaved bundle:',bundle_path); print('Saved summary:',summary_path); print('\nReturn exactly these two files:'); print(bundle_path.name); print(summary_path.name)
display(summary_df)

```
