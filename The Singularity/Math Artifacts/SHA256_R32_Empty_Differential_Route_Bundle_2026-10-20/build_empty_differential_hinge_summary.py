from pathlib import Path
import csv,json,zipfile,hashlib
P=Path('/mnt/data')
def read(n):
 with (P/n).open(newline='') as f:return list(csv.DictReader(f))
def write(n,rows):
 keys=[]
 for r in rows:
  for k in r:
   if k not in keys:keys.append(k)
 with (P/n).open('w',newline='') as f:
  w=csv.DictWriter(f,fieldnames=keys);w.writeheader();w.writerows(rows)
checks=read('SHA256_R32_Empty_Differential_Round_Identity_Checks.csv')
sched=read('SHA256_R32_Empty_Differential_Schedule.csv')
carries=read('SHA256_R32_Empty_Differential_Add_Carries.csv')
components=read('SHA256_R32_Empty_Differential_Round_Components.csv')
digest=read('SHA256_R32_Empty_Digest_Offset_Overview.csv')
cases=['Q','GO','OK','CAT','NEXUS']
hinges=[]; carry_stats=[]; ff_checks=[]; schedule_seed=[]
for case in cases:
 s0=next(r for r in sched if r['case']==case and r['t']=='0')
 s1=next(r for r in sched if r['case']==case and r['t']=='1')
 s15=next(r for r in sched if r['case']==case and r['t']=='15')
 r0=next(r for r in checks if r['case']==case and r['t']=='0')
 r1=next(r for r in checks if r['case']==case and r['t']=='1')
 ops=[('T1.1','h+Sigma1(e)'),('T1.2','+Ch'),('T1.3','+K_t'),('T1.4','+W_t'),('T2=','Sigma0(a)+Maj'),('a_next','T1+T2'),('e_next','d+T1')]
 for prefix,label in ops:
  rr=[r for r in carries if r['case']==case and r['phase']=='round' and r['operation'].startswith(prefix)]
  carry_stats.append({'case':case,'round_stage':label,'operation_prefix':prefix,'round_count':len(rr),
    'carry_masks_equal_to_empty':sum(r['carry_mask_target_hex']==r['carry_mask_empty_hex'] for r in rr),
    'carry_masks_different_from_empty':sum(r['carry_mask_target_hex']!=r['carry_mask_empty_hex'] for r in rr),
    'first_differing_round':next((int(r['index']) for r in rr if r['carry_mask_target_hex']!=r['carry_mask_empty_hex']),''),
    'different_rounds':' '.join(str(r['index']) for r in rr if r['carry_mask_target_hex']!=r['carry_mask_empty_hex'])})
 hinges.append({'case':case,'empty_W0':s0['W_t_empty_hex'],'target_W0':s0['W_t_target_hex'],
  'delta_W0':s0['W_t_delta_hex'],'delta_W0_R32_address':s0['W_t_delta_address'],'delta_W0_half_ring':s0['W_t_delta_half'],'delta_W0_side':s0['W_t_delta_side'],
  'round0_delta_partial_after_K':r0['delta_partial_after_K_hex'],'round0_delta_T1':r0['delta_T1_hex'],'round0_delta_W0':r0['delta_W_hex'],
  'round0_delta_T2':r0['delta_T2_hex'],'round0_partial_identity_pass':r0['partial_identity_pass'],'round0_T1_identity_pass':r0['T1_identity_pass'],
  'round0_T1_delta_equals_W0_delta':r0['delta_T1_hex']==s0['W_t_delta_hex'],'round0_T2_delta_zero':r0['delta_T2_hex']=='00000000',
  'round1_delta_partial_after_K':r1['delta_partial_after_K_hex'],'round1_partial_nonzero':r1['delta_partial_after_K_hex']!='00000000',
  'initial_seed_words_different_from_empty':sum(1 for r in sched if r['case']==case and int(r['t'])<16 and r['W_t_delta_hex']!='00000000'),
  'W1_delta':s1['W_t_delta_hex'],'W15_delta':s15['W_t_delta_hex']})
# Validate feed-forward: delta digest words equal delta S64 words wordwise.
for row in digest:
 case=row['case']
 if case not in cases: continue
 dd=[row['wordwise_delta_mod32_hex'][i:i+8].upper() for i in range(0,64,8)]
 ss=[]
 for lab in 'abcdefgh':
  r=next(x for x in components if x['case']==case and x['t']=='63' and x['component']==f'state_after_{lab}')
  ss.append(r['value_delta_hex'])
 ff_checks.append({'case':case,'digest_delta_words':' '.join(dd),'S64_delta_words':' '.join(ss),'wordwise_match':dd==ss,'matched_lanes':sum(a==b for a,b in zip(dd,ss))})
write('SHA256_R32_Empty_Differential_Entry_Hinge.csv',hinges)
write('SHA256_R32_Empty_Differential_Carry_Stage_Summary.csv',carry_stats)
write('SHA256_R32_Empty_Differential_Feedforward_Check.csv',ff_checks)
# patch report controls character + insert derived pattern section
report=P/'SHA256_R32_Empty_Differential_Route_Audit.md'
s=report.read_text()
s=s.replace('\x07sigma_0','\\sigma_0')
if '## First hinge and propagation' not in s:
 section='''\n## First hinge and propagation\n\nThe first-round comparison is exact for all five test cases: the state before round 0 and the indexed constant `K_0` are shared with the empty execution, so the differential `partial_after_K` is zero. `T2` is also unchanged in round 0. Therefore `ΔT1_0 = ΔW_0`, with the `W_0` difference itself retained as an R32 address plus half-ring and side. At round 1, the `partial_after_K` difference is nonzero in all five tests: the state-dependent route has begun to diverge.\n\nFor each case, the carry mask in the `+K_t` stage matches the empty baseline at round 0 and differs at all 63 subsequent rounds. This is observed for these five runs, not claimed as a theorem for all messages. The explicit `K_t` term cancels from the modular differential identity, but the indexed constant remains causally present in each execution and in the different carry routes it induces after the two states diverge.\n\nThe feed-forward check also passes wordwise for all 40 target lanes: because the same IV word is added on both faces, the eight modular digest offsets equal the eight final working-state offsets `ΔS_64`.\n\n'''
 s=s.replace('## Results\n',section+'## Results\n')
 s=s.replace('- `SHA256_R32_Empty_Differential_Route_Summary.json`: counts, checks, and file hashes.','- `SHA256_R32_Empty_Differential_Route_Summary.json`: counts, checks, and file hashes.\n- `SHA256_R32_Empty_Differential_Entry_Hinge.csv`: per-message round-0/round-1 hinge values.\n- `SHA256_R32_Empty_Differential_Carry_Stage_Summary.csv`: carry-mask change counts by indexed round stage.\n- `SHA256_R32_Empty_Differential_Feedforward_Check.csv`: digest-offset / final-state-offset equality.')
 report.write_text(s)
# add summaries to JSON and hashes
jpath=P/'SHA256_R32_Empty_Differential_Route_Summary.json'; j=json.loads(jpath.read_text())
j['round0_hinge_check']={'all_five_pass':all(x['round0_T1_delta_equals_W0_delta'] and x['round0_T2_delta_zero'] and x['round0_partial_identity_pass'] and x['round0_T1_identity_pass'] for x in hinges),
 'law':'At t=0, Δpartial_after_K=0, ΔT2=0, and ΔT1=ΔW0. At t=1 the state-dependent partial difference is nonzero in each tested case.'}
j['K_stage_carry_pattern']={'for_each_case':'K-stage carry mask equal to empty baseline at t=0, different at t=1..63', 'scope':'observed in these five test messages only'}
j['feedforward_offset_identity']={'all_five_cases_all_eight_words_match':all(x['wordwise_match'] for x in ff_checks),'law':'ΔD_j = ΔS64_j wordwise because H0_j is the same additive IV on both routes.'}
for f in ['SHA256_R32_Empty_Differential_Entry_Hinge.csv','SHA256_R32_Empty_Differential_Carry_Stage_Summary.csv','SHA256_R32_Empty_Differential_Feedforward_Check.csv','SHA256_R32_Empty_Differential_Route_Audit.md']:
 j.setdefault('sha256',{})[f]=hashlib.sha256((P/f).read_bytes()).hexdigest()
jpath.write_text(json.dumps(j,indent=2)+'\n')
# Rebuild bundle with every differential artifact and source script.
bundle=P/'SHA256_R32_Empty_Differential_Route_Bundle_2026-10-20.zip'
files=['SHA256_Empty_Differential_Route_Audit.py','build_empty_differential_hinge_summary.py','SHA256_R32_Empty_Differential_Route_Audit.md','SHA256_R32_Empty_Differential_Route_Summary.json',
'SHA256_R32_Empty_Differential_Round_Components.csv','SHA256_R32_Empty_Differential_Round_Identity_Checks.csv','SHA256_R32_Empty_Differential_Schedule.csv','SHA256_R32_Empty_Differential_Add_Carries.csv',
'SHA256_R32_Empty_Differential_Entry_Hinge.csv','SHA256_R32_Empty_Differential_Carry_Stage_Summary.csv','SHA256_R32_Empty_Differential_Feedforward_Check.csv',
'SHA256_R32_Whole_Route_Empty_Offset_Audit.md','SHA256_R32_Whole_Route_Empty_Offsets.csv','SHA256_R32_Empty_Digest_Offset_Overview.csv']
with zipfile.ZipFile(bundle,'w',zipfile.ZIP_DEFLATED,compresslevel=6) as z:
 for f in files:
  p=P/f
  if p.exists():z.write(p,arcname=f)
j['bundle']=bundle.name;j['bundle_sha256']=hashlib.sha256(bundle.read_bytes()).hexdigest();jpath.write_text(json.dumps(j,indent=2)+'\n')
print('HINGES')
for x in hinges:print(x['case'],x['delta_W0'],x['delta_W0_R32_address'],x['delta_W0_half_ring'],x['delta_W0_side'],'dP0',x['round0_delta_partial_after_K'],'dT1',x['round0_delta_T1'],'dT2',x['round0_delta_T2'],'dP1',x['round1_delta_partial_after_K'])
print('CARRY K stage')
for x in carry_stats:
 if x['round_stage']=='+K_t': print(x['case'],x['carry_masks_equal_to_empty'],x['carry_masks_different_from_empty'])
print('FEED FORWARD',ff_checks)
print('BUNDLE',bundle, bundle.stat().st_size)
