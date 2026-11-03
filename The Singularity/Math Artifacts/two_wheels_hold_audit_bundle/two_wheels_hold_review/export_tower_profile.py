#!/usr/bin/env python3
"""Materialize every tower-mirror profile point from the audited formula.

The full profile is compressed CSV so each (L,k,t) case is independently
inspectable, not represented only by sampled rows and a zero-miss count.
"""
from __future__ import annotations
import csv, gzip, json, sys, time
from pathlib import Path
ROOT = Path(__file__).resolve().parent
OUT = ROOT / 'outputs'
sys.path.insert(0, str(ROOT))
import wheels as wh
start = time.perf_counter()
def is_pal(x,n): return wh.J(x,n)==x
def partner_side_prefix(w):
    if w == 0: return [0]
    c=0; out=[0]
    for x in range(1<<w):
        if x > wh.P(x,w) and not is_pal(x,w): c += 1
        out.append(c)
    return out
prefix={w:partner_side_prefix(w) for w in range(1,17)}
prefix[0]=[0,0]  # width-zero tower base: C_0(q)=0 for q=0 or 1
path=OUT/'tower_mirror_full_profile.csv.gz'
rows=0; mismatches=0
with gzip.open(path,'wt',newline='',encoding='utf-8') as f:
    writer=csv.DictWriter(f,fieldnames=['L','k','target_width_n','low_width','t','q_ceil_t_over_2k','low_partner_side_nonpal_count','predicted_hold','wheels_hold','match'])
    writer.writeheader()
    for L in range(2,17):
        T=1<<L
        for k in range(1,L+1):
            n=L+k; low=L-k; pref=prefix[low]
            for t in range(T+1):
                q=(t+(1<<k)-1)//(1<<k)
                c=pref[q]
                pred=t-2*c
                got=wh.hold(t,n)
                match=pred==got
                mismatches += not match
                writer.writerow({'L':L,'k':k,'target_width_n':n,'low_width':low,'t':t,'q_ceil_t_over_2k':q,'low_partner_side_nonpal_count':c,'predicted_hold':pred,'wheels_hold':got,'match':int(match)})
                rows += 1
summary={'file':path.name,'rows':rows,'mismatches':mismatches,'L':'2..16','k':'1..L','t':'every integer 0..2^L','seconds':time.perf_counter()-start}
(OUT/'tower_mirror_export_summary.json').write_text(json.dumps(summary,indent=2)+'\n')
print(json.dumps(summary,indent=2))
if mismatches: raise SystemExit('tower profile export mismatch')
