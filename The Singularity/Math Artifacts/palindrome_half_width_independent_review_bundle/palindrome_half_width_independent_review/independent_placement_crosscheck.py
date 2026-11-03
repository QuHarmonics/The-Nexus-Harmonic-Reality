#!/usr/bin/env python3
from __future__ import annotations
import importlib.util, json, hashlib, time, random
from pathlib import Path
import numpy as np
ROOT=Path(__file__).resolve().parent
ADDRESS=ROOT/'palindrome_halfword_address.py'; AUDIT=ROOT/'palindrome_half_width_audit.py'
ROUTE=ROOT/'sources'/'ring_sphere_route_rank.py'
def load(name,path):
 spec=importlib.util.spec_from_file_location(name,path);mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod);return mod
A=load('palindrome_halfword_address',ADDRESS);R=load('separate_ring_rank',ROUTE)
def reverse_array(x,n):
 y=x.astype(np.uint32,copy=True)
 y=((y>>1)&0x55555555)|((y&0x55555555)<<1)
 y=((y>>2)&0x33333333)|((y&0x33333333)<<2)
 y=((y>>4)&0x0f0f0f0f)|((y&0x0f0f0f0f)<<4)
 y=((y>>8)&0x00ff00ff)|((y&0x00ff00ff)<<8)
 y=(y>>16)|(y<<16)
 return y>>(32-n)
def ring_positions(n):
 vals=np.arange(1<<n,dtype=np.uint32);rv=reverse_array(vals,n)
 pv=np.where(rv!=vals,rv,vals^((1<<n)-1)).astype(np.uint32)
 canon=vals[vals<pv];ring=np.concatenate((canon,pv[canon[::-1]]))
 if n>1:
  M=len(ring)//2;ring[M-1],ring[M]=ring[M],ring[M-1]
 inv=np.empty(1<<n,dtype=np.int32);inv[ring]=np.arange(1<<n,dtype=np.int32)
 return inv
def word_from_half(n,u):
 m=(n+1)//2;s=format(u,f'0{m}b')
 return s+(s[::-1] if n%2==0 else s[:-1][::-1])
start=time.perf_counter();finite=[];route_samples=[]
for n in range(2,21):
 inv=ring_positions(n);m=(n+1)//2;total=1<<m
 for u in range(total):
  value=int(word_from_half(n,u),2);actual=int(inv[value]);calc=A.palindrome_address(n,u)
  assert calc==actual,(n,u,calc,actual)
 finite.append({'width':n,'palindromes':total,'scalar_vs_materialized_ring':'PASS'})
 # independent DP spot-checks at each width, including both sides of the formula's symmetry seam
 samples=sorted({0,1,total//3,total//2-1,total//2,total-2,total-1})
 for u in samples:
  word=word_from_half(n,u);calc=A.palindrome_address(n,u);independent=R.location(word)
  assert calc==independent,(n,u,calc,independent)
  route_samples.append({'width':n,'halfword':str(u),'address':'PASS'})
wide=[]
# Rank-DP checks at 10 widths. One low-prefix and one upper-prefix sample per width.
for n in (63,64,127,128,255,256,511,512,1023,1024):
 m=(n+1)//2;H=1<<m
 for u in sorted({0,H//2-1,H//2,H-1}):
  word=word_from_half(n,u);calc=A.palindrome_address(n,u);independent=R.location(word)
  assert calc==independent,(n,u,calc,independent)
  wide.append({'width':n,'halfword':str(u),'address':'PASS'})
report={'status':'PASS','scope':'Exhaustive scalar placement against materialized original ring for all palindrome addresses at widths 2-20; independent route/rank location DP spot checks at each finite width and four edge/seam prefixes at widths through 1024.','finite_widths':finite,'finite_palindrome_addresses':sum(x['palindromes'] for x in finite),'finite_dp_spot_checks':len(route_samples),'wide_scalar_dp_checks':len(wide),'wide':wide,'source_hashes':{'palindrome_halfword_address.py':hashlib.sha256(ADDRESS.read_bytes()).hexdigest(),'palindrome_half_width_audit.py':hashlib.sha256(AUDIT.read_bytes()).hexdigest()},'seconds':time.perf_counter()-start}
(ROOT/'results'/'independent_placement_crosscheck_results.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({'status':report['status'],'finite_widths':len(finite),'finite_palindrome_addresses':report['finite_palindrome_addresses'],'finite_dp_spot_checks':len(route_samples),'wide_scalar_dp_checks':len(wide),'seconds':report['seconds'],'results':str(ROOT/'results'/'independent_placement_crosscheck_results.json')},indent=2))
