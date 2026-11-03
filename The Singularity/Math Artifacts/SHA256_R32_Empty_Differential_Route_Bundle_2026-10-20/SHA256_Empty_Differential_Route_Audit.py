from pathlib import Path
import csv, json, hashlib, zipfile
from collections import Counter, defaultdict

ROOT=Path('/mnt/data'); N=1<<32; MASK=N-1
src=(ROOT/'SHA256_Ring_Native_Run.py').read_text()
ns={}; exec(src.split('# Verify global ring/address bijection at width 32.')[0], ns)
loc=ns['location']; word_at=ns['word_at']; P=ns['P']; K=ns['K']; H0=ns['H0']
sigma0=ns['sigma0']; sigma1=ns['sigma1']; Ch=ns['Ch']; Maj=ns['Maj']; Sigma0=ns['Sigma0']; Sigma1=ns['Sigma1']


def read_csv(name):
    with (ROOT/name).open(newline='') as f: return list(csv.DictReader(f))
def write_csv(name, rows):
    if not rows: return
    cols=[]
    for r in rows:
        for k in r:
            if k not in cols: cols.append(k)
    with (ROOT/name).open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=cols); w.writeheader(); w.writerows(rows)
def hx(v): return f'{v&MASK:08X}'
def val_at_addr(a): return word_at(32, int(a))
def coords(v):
    v &= MASK; a=loc(v,32); p=loc(P(v,32),32); h=min(a,N-1-a)
    side='A' if a<N-1-a else ('B' if a>N-1-a else 'seam')
    return {'address':a,'half':h,'side':side,'partner_address':p,'reflect_ok':p==N-1-a}
def enrich(prefix,v):
    c=coords(v)
    return {f'{prefix}_hex':hx(v),f'{prefix}_address':c['address'],f'{prefix}_half':c['half'],
            f'{prefix}_side':c['side'],f'{prefix}_partner_address':c['partner_address'],f'{prefix}_reflect_ok':c['reflect_ok']}
def off_fields(prefix,t,e):
    d=(t-e)&MASK; x=t^e
    return {**enrich(prefix+'_target',t),**enrich(prefix+'_empty',e),
            **enrich(prefix+'_delta',d),**enrich(prefix+'_xor',x)}

cases=['Q','GO','OK','CAT','NEXUS']
round_t=read_csv('SHA256_R32_round_route_trace.csv')
round_e=read_csv('SHA256_R32_empty_message_round_route.csv')
sched_t=read_csv('SHA256_R32_schedule_route_trace.csv')
sched_e=read_csv('SHA256_R32_empty_message_schedule_route.csv')
add_t=read_csv('SHA256_R32_add_carry_route_trace.csv')
add_e=read_csv('SHA256_R32_empty_message_add_carry_route.csv')

# Index exact corresponding executions by source identity and route identity.
empty_round={int(r['t']):r for r in round_e}
empty_sched={int(r['t']):r for r in sched_e}
empty_add={(r['phase'],r['index'],r['operation']):r for r in add_e}
round_rows=[]; round_checks=[]; sched_rows=[]; carry_rows=[]

# helper: convert state hex vector to tuple of ints

def vec(s): return [int(x,16) for x in s.split(';')]
def addmod(vals):
    z=0
    for v in vals: z=(z+v)&MASK
    return z

for case in cases:
    rt=sorted([r for r in round_t if r['case']==case], key=lambda r:int(r['t']))
    st=sorted([r for r in sched_t if r['case']==case], key=lambda r:int(r['t']))
    by_sched={int(r['t']):r for r in st}
    assert len(rt)==64 and len(st)==64
    # Get value-level schedule arrays, retaining index.
    W=[int(by_sched[t]['word_hex'],16) for t in range(64)]
    WE=[int(empty_sched[t]['word_hex'],16) for t in range(64)]
    # schedule differential recurrence at each index
    for t in range(64):
        a=by_sched[t]; b=empty_sched[t]
        tv=int(a['word_hex'],16); ev=int(b['word_hex'],16); d=(tv-ev)&MASK; x=tv^ev
        row={'case':case,'t':t,'kind':a['kind'],'padding_or_expanded':a['kind'],
             **off_fields('W_t',tv,ev),
             'bitwise_diff_is_sigma_inputs': 'not_applicable' if t<16 else 'see sigma XOR fields'}
        if t>=16:
            s1t=sigma1(W[t-2]); s1e=sigma1(WE[t-2]); s0t=sigma0(W[t-15]); s0e=sigma0(WE[t-15])
            dS1=(s1t-s1e)&MASK; xS1=s1t^s1e
            dS0=(s0t-s0e)&MASK; xS0=s0t^s0e
            terms=[dS1,(W[t-7]-WE[t-7])&MASK,dS0,(W[t-16]-WE[t-16])&MASK]
            rhs=addmod(terms)
            row.update({
                'dep_t_minus_2':t-2,'dep_t_minus_7':t-7,'dep_t_minus_15':t-15,'dep_t_minus_16':t-16,
                **off_fields('sigma1_W_t_minus_2',s1t,s1e),
                **off_fields('sigma0_W_t_minus_15',s0t,s0e),
                'delta_schedule_rhs_hex':hx(rhs),'delta_schedule_lhs_hex':hx(d),
                'delta_schedule_identity_pass':rhs==d,
                'xor_sigma1_equals_sigma1_xor_input':xS1==sigma1(W[t-2]^WE[t-2]),
                'xor_sigma0_equals_sigma0_xor_input':xS0==sigma0(W[t-15]^WE[t-15]),
                'delta_schedule_terms_mod32':' + '.join(hx(z) for z in terms),
            })
        else:
            row.update({'delta_schedule_rhs_hex':'','delta_schedule_lhs_hex':hx(d),'delta_schedule_identity_pass':'padding/input',
                        'xor_sigma1_equals_sigma1_xor_input':'','xor_sigma0_equals_sigma0_xor_input':''})
        sched_rows.append(row)

    # exact per-round differential equations, with every component independently addressed.
    for r in rt:
        t=int(r['t']); e=empty_round[t]
        before_t=vec(r['state_before_hex']); before_e=vec(e['state_before_hex'])
        after_t=vec(r['state_after_hex']); after_e=vec(e['state_after_hex'])
        components=[]
        for j,lab in enumerate('abcdefgh'):
            components.append((f'state_before_{lab}',before_t[j],before_e[j]))
        term_map={
          'Sigma1_e': (val_at_addr(r['Sigma1_e_address']),val_at_addr(e['Sigma1_e_address'])),
          'Ch_e_f_g': (val_at_addr(r['Ch_address']),val_at_addr(e['Ch_address'])),
          'K_t': (int(r['K_hex'],16),int(e['K_hex'],16)),
          'W_t': (int(r['W_hex'],16),int(e['W_hex'],16)),
          'partial_after_K': (val_at_addr(r['T1_partial_after_K_address']),val_at_addr(e['T1_partial_after_K_address'])),
          'T1': (val_at_addr(r['T1_address']),val_at_addr(e['T1_address'])),
          'Sigma0_a': (val_at_addr(r['Sigma0_a_address']),val_at_addr(e['Sigma0_a_address'])),
          'Maj_a_b_c': (val_at_addr(r['Maj_address']),val_at_addr(e['Maj_address'])),
          'T2': (val_at_addr(r['T2_address']),val_at_addr(e['T2_address'])),
        }
        components.extend((k,*v) for k,v in term_map.items())
        for j,lab in enumerate('abcdefgh'):
            components.append((f'state_after_{lab}',after_t[j],after_e[j]))
        for comp,tv,ev in components:
            d=(tv-ev)&MASK; x=tv^ev
            base={'case':case,'t':t,'K_t_hex':r['K_hex'],'K_t_address':int(r['K_address']),
                  'component':comp,**off_fields('value',tv,ev),
                  'K_same_both_faces':r['K_hex']==e['K_hex']}
            round_rows.append(base)
        # Round-equation exact differential check.
        # T1: Δh + ΔΣ1 + ΔCh + ΔW (the K term cancels because K_t is the same).
        idx='abcdefgh'.index('h'); dh=(before_t[idx]-before_e[idx])&MASK
        s1t,s1e=term_map['Sigma1_e']; cht,che=term_map['Ch_e_f_g']; wt,we=term_map['W_t']
        p_t,p_e=term_map['partial_after_K']; t1_t,t1_e=term_map['T1']
        dpartial=(p_t-p_e)&MASK; dt1=(t1_t-t1_e)&MASK
        dS1=(s1t-s1e)&MASK; dCh=(cht-che)&MASK; dW=(wt-we)&MASK
        partial_rhs=addmod([dh,dS1,dCh])
        t1_rhs=addmod([dh,dS1,dCh,dW])
        s0t,s0e=term_map['Sigma0_a']; mt,me=term_map['Maj_a_b_c']; t2t,t2e=term_map['T2']
        dt2=(t2t-t2e)&MASK; t2_rhs=addmod([(s0t-s0e)&MASK,(mt-me)&MASK])
        # next register differences: a' = T1 + T2 ; e' = d + T1
        da_next=(after_t[0]-after_e[0])&MASK; de_next=(after_t[4]-after_e[4])&MASK
        dd=(before_t[3]-before_e[3])&MASK
        check={
          'case':case,'t':t,'K_t_hex':r['K_hex'],'K_t_address':int(r['K_address']),
          'delta_partial_after_K_hex':hx(dpartial),'delta_h_hex':hx(dh),'delta_Sigma1_hex':hx(dS1),'delta_Ch_hex':hx(dCh),
          'partial_rhs_hex':hx(partial_rhs),'partial_identity_pass':dpartial==partial_rhs,
          'delta_W_hex':hx(dW),'delta_T1_hex':hx(dt1),'T1_rhs_hex':hx(t1_rhs),'T1_identity_pass':dt1==t1_rhs,
          'K_cancels_explicitly':r['K_hex']==e['K_hex'],
          'delta_T2_hex':hx(dt2),'T2_rhs_hex':hx(t2_rhs),'T2_identity_pass':dt2==t2_rhs,
          'delta_a_next_hex':hx(da_next),'delta_T1_plus_delta_T2_hex':hx(addmod([dt1,dt2])),
          'a_update_identity_pass':da_next==addmod([dt1,dt2]),
          'delta_d_hex':hx(dd),'delta_e_next_hex':hx(de_next),'d_plus_T1_delta_hex':hx(addmod([dd,dt1])),
          'e_update_identity_pass':de_next==addmod([dd,dt1]),
        }
        round_checks.append(check)

# Detailed differential arithmetic rows, including carry-mask differences.
for tr in add_t:
    case=tr['case']
    if case not in cases: continue
    key=(tr['phase'],tr['index'],tr['operation'])
    er=empty_add.get(key)
    if er is None:
        raise RuntimeError(f'No empty addition row for {key}')
    xt,yt,rtv,ct=(int(tr[k],16) for k in ['x_hex','y_hex','result_hex','carry_out_mask_hex'])
    xe,ye,rev,ce=(int(er[k],16) for k in ['x_hex','y_hex','result_hex','carry_out_mask_hex'])
    dx=(xt-xe)&MASK; dy=(yt-ye)&MASK; dr=(rtv-rev)&MASK; rhs=(dx+dy)&MASK
    cx=ct^ce; cd=(ct-ce)&MASK
    row={'case':case,'phase':tr['phase'],'index':tr['index'],'operation':tr['operation'],
         **off_fields('x',xt,xe),**off_fields('y',yt,ye),**off_fields('result',rtv,rev),
         **off_fields('carry_mask',ct,ce),
         'delta_result_rhs_hex':hx(rhs),'delta_result_identity_pass':dr==rhs,
         'carry_xor_popcount':cx.bit_count(),'carry_mod_delta_hex':hx(cd),
         'carry_delta_address':coords(cd)['address'],'carry_delta_half':coords(cd)['half'],'carry_delta_side':coords(cd)['side'],
         'carry_positions_target':tr['carry_positions'],'carry_positions_empty':er['carry_positions']}
    carry_rows.append(row)

assert len(round_checks)==len(cases)*64
assert len(sched_rows)==len(cases)*64
assert len(carry_rows)==len(cases)*600
assert all(r['partial_identity_pass'] and r['T1_identity_pass'] and r['T2_identity_pass'] and r['a_update_identity_pass'] and r['e_update_identity_pass'] for r in round_checks)
assert all(r['delta_schedule_identity_pass'] is True for r in sched_rows if isinstance(r['delta_schedule_identity_pass'],bool))
assert all(r['delta_result_identity_pass'] for r in carry_rows)
assert all(r['K_cancels_explicitly'] for r in round_checks)
assert all(r['xor_sigma1_equals_sigma1_xor_input'] for r in sched_rows if r['t']>=16)
assert all(r['xor_sigma0_equals_sigma0_xor_input'] for r in sched_rows if r['t']>=16)

write_csv('SHA256_R32_Empty_Differential_Round_Components.csv',round_rows)
write_csv('SHA256_R32_Empty_Differential_Round_Identity_Checks.csv',round_checks)
write_csv('SHA256_R32_Empty_Differential_Schedule.csv',sched_rows)
write_csv('SHA256_R32_Empty_Differential_Add_Carries.csv',carry_rows)

summary={
 'task':'Differential SHA-256 route with empty-message execution as the aligned baseline, all words and differences addressed in R32',
 'cases':cases,
 'empty_digest':'e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855',
 'round_component_rows':len(round_rows),'round_identity_checks':len(round_checks),'schedule_differential_rows':len(sched_rows),'addition_carry_differential_rows':len(carry_rows),
 'all_round_difference_identities_pass':True,'all_schedule_difference_identities_pass':True,'all_add_result_difference_identities_pass':True,
 'all_K_t_same_in_target_and_empty':True,
 'K_cancellation_rule':'ΔT1_t = Δh_t + ΔΣ1(e_t) + ΔCh(e_t,f_t,g_t) + ΔW_t mod 2^32. K_t cancels from the explicit differential sum because target and baseline use the same indexed K_t; baseline states and carry masks still encode its effect.',
 'schedule_difference_rule':'For t>=16, ΔW_t = Δσ1(W[t-2]) + ΔW[t-7] + Δσ0(W[t-15]) + ΔW[t-16] mod 2^32. The XOR readout is also retained independently; linearity of σ0/σ1 over GF(2) is separately checked on XOR differences.',
 'carry_rule':'For each binary addition, Δ(result) = Δ(x)+Δ(y) mod 2^32. Target and empty carry masks are both retained with modular and XOR differences; they are not replaced by one another.',
 'limitations':'These identities verify the aligned differential route for five known source messages. They do not yet produce a digest-only selector for an unknown multi-byte preimage, and arithmetic offsets are not assumed to obey the ring partner map as arithmetic values; the ring map only gives their exact coordinate and reflected partner.',
}
for f in ['SHA256_R32_Empty_Differential_Round_Components.csv','SHA256_R32_Empty_Differential_Round_Identity_Checks.csv','SHA256_R32_Empty_Differential_Schedule.csv','SHA256_R32_Empty_Differential_Add_Carries.csv']:
 summary.setdefault('sha256',{})[f]=hashlib.sha256((ROOT/f).read_bytes()).hexdigest()
(ROOT/'SHA256_R32_Empty_Differential_Route_Summary.json').write_text(json.dumps(summary,indent=2)+'\n')
md=f'''# SHA-256 differential route against the empty-message reference

## Held coordinates

The empty-message run is the reference trajectory at each matching typed coordinate. Target and baseline remain separated; every target value, baseline value, modular difference, and XOR difference is represented by an exact R32 address with its canonical half-ring address and side marker. Round index `t`, `K_t`, `W_t`, and operation labels are retained.

## Exact differential laws checked

For each of five source messages and all 64 rounds, the audit checks:

\\[
\\Delta T1_t = \\Delta h_t + \\Delta\\Sigma_1(e_t) + \\Delta\\operatorname{{Ch}}(e_t,f_t,g_t) + \\Delta W_t \\pmod{{2^{{32}}}}.
\\]

The explicit `K_t` terms cancel from this difference because the target and empty route use the same constant at the same `t`. This does not erase the constant's causal effect: its value has already shaped the two state trajectories and their carry masks. The audit keeps the `K_t` address and the carry masks for the `+K_t` stage on both sides.

Likewise, the schedule difference is checked for every `t >= 16`:

\\[
\\Delta W_t=\\Delta\\sigma_1(W_{{t-2}})+\\Delta W_{{t-7}}+\\Delta\\sigma_0(W_{{t-15}})+\\Delta W_{{t-16}}\\pmod{{2^{{32}}}}.
\\]

The \\(sigma_0,\\sigma_1\\) maps are linear under XOR, so the audit independently checks the corresponding XOR-difference identity. XOR differences are kept distinct from modular subtraction differences. For every binary addition in all five routes, the audit verifies the modular result-difference identity and records target and empty carry masks side by side, with both difference forms.

## Results

- Round-component rows: {len(round_rows)}.
- Per-round identity checks: {len(round_checks)}; all passed.
- Schedule difference rows: {len(sched_rows)}; all applicable identities passed.
- Addition/carry route pairs: {len(carry_rows)}; all modular result-difference identities passed.
- Explicit `K_t` alignment checks: all passed for all cases and rounds.

## Interpretation boundary

This is a verified differential route for the five known test messages, not yet a digest-only preimage selector. The ring is used as the coordinate system for every value/difference and the fold side is retained. The result is the exact empty-relative recurrence to be studied next; it does not claim the indexed interior constants can be generated from endpoint constants alone.

## Data files

- `SHA256_R32_Empty_Differential_Round_Components.csv`: normalized long-form component table with target/empty/delta/XOR values and ring coordinates.
- `SHA256_R32_Empty_Differential_Round_Identity_Checks.csv`: every round identity and Boolean result.
- `SHA256_R32_Empty_Differential_Schedule.csv`: schedule differences and dependency inputs.
- `SHA256_R32_Empty_Differential_Add_Carries.csv`: every matched binary addition, both carry masks and both offset forms.
- `SHA256_R32_Empty_Differential_Route_Summary.json`: counts, checks, and file hashes.
'''
(ROOT/'SHA256_R32_Empty_Differential_Route_Audit.md').write_text(md)
# bundle the new differential tables, report, and reproducible script
bundle=ROOT/'SHA256_R32_Empty_Differential_Route_Bundle_2026-10-20.zip'
files=['SHA256_Empty_Differential_Route_Audit.py','SHA256_R32_Empty_Differential_Route_Audit.md','SHA256_R32_Empty_Differential_Route_Summary.json',
'SHA256_R32_Empty_Differential_Round_Components.csv','SHA256_R32_Empty_Differential_Round_Identity_Checks.csv','SHA256_R32_Empty_Differential_Schedule.csv','SHA256_R32_Empty_Differential_Add_Carries.csv',
'SHA256_R32_Whole_Route_Empty_Offset_Audit.md','SHA256_R32_Whole_Route_Empty_Offsets.csv','SHA256_R32_Empty_Digest_Offset_Overview.csv']
with zipfile.ZipFile(bundle,'w',zipfile.ZIP_DEFLATED,compresslevel=6) as z:
 for f in files:
  p=ROOT/f
  if p.exists(): z.write(p,arcname=f)
summary['bundle']=bundle.name; summary['bundle_sha256']=hashlib.sha256(bundle.read_bytes()).hexdigest()
(ROOT/'SHA256_R32_Empty_Differential_Route_Summary.json').write_text(json.dumps(summary,indent=2)+'\n')
print(json.dumps(summary,indent=2)); print('bundle_bytes',bundle.stat().st_size)
