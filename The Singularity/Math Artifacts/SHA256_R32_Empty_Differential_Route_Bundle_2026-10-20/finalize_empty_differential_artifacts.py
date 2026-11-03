from pathlib import Path
import csv,json,hashlib,zipfile
P=Path('/mnt/data')
def read(name):
 with (P/name).open(newline='') as f:return list(csv.DictReader(f))
def write(name,rows):
 fields=[]
 for r in rows:
  for k in r:
   if k not in fields:fields.append(k)
 with (P/name).open('w',newline='') as f:
  w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows(rows)
sched=read('SHA256_R32_Empty_Differential_Schedule.csv')
cases=['Q','GO','OK','CAT','NEXUS']
initial=[]
for case in cases:
 for r in sorted((x for x in sched if x['case']==case and int(x['t'])<16),key=lambda x:int(x['t'])):
  t=int(r['t']); val=r['W_t_delta_hex']; nz=val!='00000000'
  role='leading message/padding boundary' if t==0 else ('trailing bit-length boundary' if t==15 else ('leading message/padding continuation' if nz else 'interior unchanged against empty'))
  initial.append({'case':case,'t':t,'role':role,'target_W_hex':r['W_t_target_hex'],'empty_W_hex':r['W_t_empty_hex'],
   'delta_mod32_hex':val,'delta_R32_address':r['W_t_delta_address'],'delta_half_ring':r['W_t_delta_half'],'delta_side':r['W_t_delta_side'],
   'xor_hex':r['W_t_xor_hex'],'xor_R32_address':r['W_t_xor_address'],'changed_vs_empty':nz,
   'generated_schedule_t_ge_16':False})
 for r in sorted((x for x in sched if x['case']==case and int(x['t'])>=16),key=lambda x:int(x['t'])):
  initial.append({'case':case,'t':int(r['t']),'role':'generated schedule recurrence','target_W_hex':r['W_t_target_hex'],'empty_W_hex':r['W_t_empty_hex'],
   'delta_mod32_hex':r['W_t_delta_hex'],'delta_R32_address':r['W_t_delta_address'],'delta_half_ring':r['W_t_delta_half'],'delta_side':r['W_t_delta_side'],
   'xor_hex':r['W_t_xor_hex'],'xor_R32_address':r['W_t_xor_address'],'changed_vs_empty':r['W_t_delta_hex']!='00000000',
   'generated_schedule_t_ge_16':True})
write('SHA256_R32_Empty_Differential_Initial_Block.csv',initial)
# fix equation display typo if present
rp=P/'SHA256_R32_Empty_Differential_Route_Audit.md'; txt=rp.read_text().replace('\x07sigma_0','\\sigma_0')
# Ensure explicit seed-support observation is in the report.
if '## Two-end seed support' not in txt:
 block='''\n## Two-end seed support in the padded block\n\nIn these five short-message controls, the target-versus-empty input difference is confined to the leading content/padding word `W_0` and trailing length word `W_15`; the interior `W_1..W_14` words match the empty block, except that the five-byte `NEXUS` control also differs at `W_1` because the content and padding cross the 32-bit word boundary. Once the recurrence starts, all 48 generated schedule words `W_16..W_63` differ from the empty baseline in every one of the five cases. This is a verified pattern for these controls, not a claim that every message length has only two changed 32-bit seed words.\n\nThe input block’s two boundary conditions therefore give a useful route decomposition: message/padding enters at the leading edge, length enters at the trailing edge, and the schedule recurrence propagates their difference through the generated interior. The exact target and empty values, modular offsets, XOR offsets, R32 addresses, half-ring coordinates, and side markers are retained in `SHA256_R32_Empty_Differential_Initial_Block.csv`.\n\n'''
 txt=txt.replace('## First hinge and propagation\n',block+'## First hinge and propagation\n')
 txt=txt.replace('- `SHA256_R32_Empty_Differential_Entry_Hinge.csv`: per-message round-0/round-1 hinge values.','- `SHA256_R32_Empty_Differential_Entry_Hinge.csv`: per-message round-0/round-1 hinge values.\n- `SHA256_R32_Empty_Differential_Initial_Block.csv`: all 16 initial schedule words and all 48 generated schedule words, with the changed-seed support marked.')
rp.write_text(txt)
# Update summary. Keep bundle hash external to avoid circular self-reference.
jp=P/'SHA256_R32_Empty_Differential_Route_Summary.json'; j=json.loads(jp.read_text())
j.pop('bundle_sha256',None)
j['two_end_seed_support']={
 'scope':'five short-message controls only',
 'cases_with_W0_and_W15_as_only_changed_initial_words':['Q','GO','OK','CAT'],
 'case_with_extra_leading_word_due_to_message_crossing_a_32_bit_word_boundary':'NEXUS (W1 also differs)',
 'all_48_generated_schedule_words_differ_from_empty_for_each_case':True,
 'interpretation':'The changed initial-block support is at the leading message/padding edge and trailing length edge; the schedule recurrence propagates the difference into every generated W16..W63 word in these tested cases.'}
j.setdefault('sha256',{})['SHA256_R32_Empty_Differential_Initial_Block.csv']=hashlib.sha256((P/'SHA256_R32_Empty_Differential_Initial_Block.csv').read_bytes()).hexdigest()
j.setdefault('sha256',{})['SHA256_R32_Empty_Differential_Route_Audit.md']=hashlib.sha256(rp.read_bytes()).hexdigest()
jp.write_text(json.dumps(j,indent=2)+'\n')
# Update bundle
bundle=P/'SHA256_R32_Empty_Differential_Route_Bundle_2026-10-20.zip'
files=['SHA256_Empty_Differential_Route_Audit.py','build_empty_differential_hinge_summary.py','finalize_empty_differential_artifacts.py',
'SHA256_R32_Empty_Differential_Route_Audit.md','SHA256_R32_Empty_Differential_Route_Summary.json',
'SHA256_R32_Empty_Differential_Round_Components.csv','SHA256_R32_Empty_Differential_Round_Identity_Checks.csv','SHA256_R32_Empty_Differential_Schedule.csv','SHA256_R32_Empty_Differential_Add_Carries.csv',
'SHA256_R32_Empty_Differential_Entry_Hinge.csv','SHA256_R32_Empty_Differential_Carry_Stage_Summary.csv','SHA256_R32_Empty_Differential_Feedforward_Check.csv','SHA256_R32_Empty_Differential_Initial_Block.csv',
'SHA256_R32_Whole_Route_Empty_Offset_Audit.md','SHA256_R32_Whole_Route_Empty_Offsets.csv','SHA256_R32_Empty_Digest_Offset_Overview.csv']
with zipfile.ZipFile(bundle,'w',zipfile.ZIP_DEFLATED,compresslevel=6) as z:
 for f in files:
  p=P/f
  if p.exists():z.write(p,arcname=f)
sha=hashlib.sha256(bundle.read_bytes()).hexdigest()
(P/'SHA256_R32_Empty_Differential_Route_Bundle_2026-10-20.zip.sha256').write_text(f'{sha}  {bundle.name}\n')
print('initial_rows',len(initial),'initial nonzero per case')
for c in cases:
 rows=[r for r in initial if r['case']==c and int(r['t'])<16]
 gens=[r for r in initial if r['case']==c and int(r['t'])>=16]
 print(c, [int(r['t']) for r in rows if r['changed_vs_empty']], sum(r['changed_vs_empty'] for r in gens),len(gens))
print('report_chars',len(txt),'bundle_bytes',bundle.stat().st_size,'bundle_sha256',sha)
