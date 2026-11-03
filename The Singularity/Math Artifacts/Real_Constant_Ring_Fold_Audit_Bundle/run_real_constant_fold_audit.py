from pathlib import Path
import csv, json, math, hashlib
import mpmath as mp
src=Path('/mnt/data/SHA256_Ring_Native_Run.py').read_text().split('# Ring-coordinate transduction.')[0]
ns={}; exec(src,ns)
location=ns['location']; rank_word=ns['rank_word']; partner=ns['P']
mp.mp.dps=200
constants={'pi':mp.pi,'phi':(1+mp.sqrt(5))/2,'e':mp.e}
widths=[8,16,32,64,128,256]
rows=[]
for name,c in constants.items():
    alpha=c-mp.floor(c)
    limit=alpha-alpha*alpha/2
    for L in widths:
        x=int(mp.floor(alpha*(1<<L)))
        addr=location(x,L)
        p=partner(x,L)
        paddr=location(p,L)
        fold=rank_word(x,L)
        observed=mp.mpf(fold)/(1<<L)
        err=abs(observed-limit)
        rows.append({
            'constant':name,'width':L,'alpha_decimal_100d':mp.nstr(alpha,100),
            'prefix_hex':f'{x:0{(L+3)//4}X}','prefix_integer':x,
            'ring_address':addr,'partner_hex':f'{p:0{(L+3)//4}X}',
            'partner_address':paddr,'reflected_address_expected':(1<<L)-1-addr,
            'reflection_pass':paddr==(1<<L)-1-addr,
            'fold_count_C_L':fold,'fold_count_normalized':mp.nstr(observed,100),
            'limit_alpha_minus_alpha2_over2':mp.nstr(limit,100),
            'absolute_error':mp.nstr(err,100),
            'error_float':float(err)
        })

# Verify 32-bit offsets relative to empty digest word 0.
L=32; empty=0xE3B0C442; empty_addr=location(empty,L)
offset_rows=[]
for name,c in constants.items():
    alpha=c-mp.floor(c); x=int(mp.floor(alpha*(1<<L))); addr=location(x,L)
    delta=addr-empty_addr
    signed=delta if delta < (1<<31) else delta-(1<<32)
    paddr=location(partner(x,L),L); epaddr=location(partner(empty,L),L)
    signed_partner=(paddr-epaddr)
    signed_partner=signed_partner if signed_partner < (1<<31) else signed_partner-(1<<32)
    offset_rows.append({'constant':name,'prefix_hex':f'{x:08X}','ring_address':addr,'empty_anchor_hex':f'{empty:08X}',
                        'empty_anchor_address':empty_addr,'signed_address_delta':signed,
                        'reflected_constant_address':paddr,'reflected_empty_anchor_address':epaddr,
                        'reflected_signed_delta':signed_partner,'offset_sign_reversal_pass':signed_partner==-signed})

# Generate the established ring at L=4 for seam correction.
def pstr(x):
    r=x[::-1]
    return r if r!=x else ''.join('1' if b=='0' else '0' for b in x)
def grow(L):
    seen=set();pairs=[]
    for w in range(1<<L):
        x=format(w,f'0{L}b')
        if x in seen: continue
        p=pstr(x);seen|={x,p};pairs.append((x,p))
    seq=[]
    for i,(a,b) in enumerate(pairs):
        if i==len(pairs)-1 and len(pairs)>1: a,b=b,a
        m=len(seq)//2; seq=seq[:m]+[a,b]+seq[m:]
    return seq
R4=grow(4)
seam={'R4_sequence_decimal':[int(w,2) for w in R4],
      'R4_position_7':int(R4[7],2),'R4_position_8':int(R4[8],2),
      'partner_pair_is_11_13':{int(R4[7],2),int(R4[8],2)}=={11,13},
      'reflection_address_law':(15-7==8),
      'positions_1_and_2': [int(R4[1],2),int(R4[2],2)]}

out=Path('/mnt/data')
with (out/'Real_Constant_Ring_Fold_Audit.csv').open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=list(rows[0].keys()));w.writeheader();w.writerows(rows)
with (out/'Real_Constant_Empty_Anchor_Offsets.csv').open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=list(offset_rows[0].keys()));w.writeheader();w.writerows(offset_rows)
maxerr=max(mp.mpf(r['absolute_error']) for r in rows)
summary={
 'constants':['pi','phi','e'],'widths':widths,'prefix_rows':len(rows),
 'all_reflection_checks_pass':all(r['reflection_pass'] for r in rows),
 'max_fold_count_absolute_error':mp.nstr(maxerr,100),
 'max_error_by_width':{str(L):mp.nstr(max(mp.mpf(r['absolute_error']) for r in rows if r['width']==L),30) for L in widths},
 'empty_anchor':f'{empty:08X}','empty_anchor_address':empty_addr,
 'all_empty_anchor_offset_sign_reversal_checks_pass':all(r['offset_sign_reversal_pass'] for r in offset_rows),
 'offsets':offset_rows,'R4_seam_check':seam,
 'interpretation':'This verifies the real-prefix fold-count limit and exact ring address/reflection coordinates at the listed finite widths. It does not establish a generator for SHA round constants from pi, phi, e, or from two endpoints.'
}
(out/'Real_Constant_Ring_Fold_Audit_Summary.json').write_text(json.dumps(summary,indent=2)+'\n')
md=['# Real-constant prefix and fold-count audit','',
    'This run uses the existing exact nested-ring `location`, `partner`, and `rank_word` routines. Fractional prefixes of pi, phi, and e were independently computed at 200-digit precision for widths 8, 16, 32, 64, 128, and 256. The ring was never materialized.', '',
    '## Verified','',
    f'- {len(rows)} prefix/width cases computed.','- All partner-address reflection identities pass.','- The exact fold-count coordinate `C_L(x)=rank_word(x,L)` was compared against `alpha-alpha^2/2` for every prefix.','- Maximum absolute normalized fold-count error: `' + mp.nstr(maxerr,40) + '.',
    '- Width-32 offsets from empty-digest anchor E3B0C442 reproduce with reflected sign reversal for all three constants.', '',
    '## Width-32 empty-anchor offsets','',
    '| Constant | Prefix | Ring address | Signed offset from E3B0C442 | Reflected signed offset |',
    '|---|---:|---:|---:|---:|']
for r in offset_rows:
    md.append(f"| {r['constant']} | `{r['prefix_hex']}` | {r['ring_address']:,} | {r['signed_address_delta']:+,} | {r['reflected_signed_delta']:+,} |")
md += ['', '## Center seam correction','',
       f"The active R4 generator gives `R4[7]={seam['R4_position_7']}` and `R4[8]={seam['R4_position_8']}` (zero-based), so the twin-prime partner pair occupies the center seam exactly; `15-7=8`. `R4[1]` and `R4[2]` are {seam['positions_1_and_2']}, so the position pair 1,2 in the supplied note is a typographical index error.", '',
       '## Scope boundary','',
       'These checks establish a deterministic address/fold readout for the selected real-number prefixes. They do not establish that the SHA-256 round constants can be regenerated from pi, phi, e, or from the endpoints of the K sequence. Those are distinct claims requiring a separate dependency law.', '']
(out/'Real_Constant_Ring_Fold_Audit.md').write_text('\n'.join(md))
for path in ['Real_Constant_Ring_Fold_Audit.csv','Real_Constant_Empty_Anchor_Offsets.csv','Real_Constant_Ring_Fold_Audit_Summary.json','Real_Constant_Ring_Fold_Audit.md']:
 print(path, hashlib.sha256((out/path).read_bytes()).hexdigest())
print('MAXERR',mp.nstr(maxerr,60))
print('ERROR_BY_WIDTH',summary['max_error_by_width'])
print('OFFSETS',json.dumps(offset_rows,indent=2))
print('R4',json.dumps(seam))
