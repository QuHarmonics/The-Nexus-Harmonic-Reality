#!/usr/bin/env python3
"""Independent audit of three ring-chain links: Walsh spectrum, radial certificate, ROBDD binding.
Uses exact integer Walsh transforms and Fraction-based radial replay. The SHA/ROBDD code is not in the supplied artifacts, so that link is checked for provider availability only.
"""
from __future__ import annotations
import hashlib, json, math, sys, time, zipfile
from fractions import Fraction
from pathlib import Path
import numpy as np

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "results"
OUT.mkdir(exist_ok=True)
SCALAR = ROOT / "src" / "full_body_scalar_reader.py"
sys.path.insert(0, str(SCALAR.parent))
from full_body_scalar_reader import word_at

def reverse_int(x: int, n: int) -> int:
    y = 0
    for _ in range(n):
        y = (y << 1) | (x & 1)
        x >>= 1
    return y

def reverse_array(x: np.ndarray, n: int) -> np.ndarray:
    y=x.astype(np.uint32,copy=True)
    y=((y>>1)&0x55555555)|((y&0x55555555)<<1)
    y=((y>>2)&0x33333333)|((y&0x33333333)<<2)
    y=((y>>4)&0x0F0F0F0F)|((y&0x0F0F0F0F)<<4)
    y=((y>>8)&0x00FF00FF)|((y&0x00FF00FF)<<8)
    y=(y>>16)|(y<<16)
    return y >> (32-n) if n else np.zeros_like(y)

BYTE_WT = np.array([i.bit_count() for i in range(256)], dtype=np.uint8)
def popcount_array(x: np.ndarray) -> np.ndarray:
    y=x.astype(np.uint32, copy=False)
    return (BYTE_WT[y & 255].astype(np.int16) + BYTE_WT[(y>>8)&255].astype(np.int16) +
            BYTE_WT[(y>>16)&255].astype(np.int16) + BYTE_WT[(y>>24)&255].astype(np.int16))

def fwht(a: np.ndarray) -> np.ndarray:
    x=a.astype(np.int64, copy=True)
    n=x.size
    step=1
    while step<n:
        v=x.reshape(-1,2,step)
        left=v[:,0,:].copy(); right=v[:,1,:].copy()
        v[:,0,:]=left+right; v[:,1,:]=left-right
        step*=2
    return x

def ring_data(n: int):
    N=1<<n; M=N//2
    x=np.arange(N,dtype=np.uint32)
    rev=reverse_array(x,n)
    partner=np.where(rev!=x,rev,x^np.uint32(N-1)).astype(np.uint32)
    canonical=x<partner
    reps=x[canonical]
    ring=np.concatenate((reps,partner[reps][::-1])).astype(np.uint32)
    ring[M-1],ring[M]=ring[M],ring[M-1]
    weights=popcount_array(ring).astype(np.int64)
    pal=reverse_array(ring,n)==ring
    lat2=2*weights-n
    body2=np.where(pal,0,lat2).astype(np.int64)
    carrier2=np.where(pal,lat2,0).astype(np.int64)
    return ring,weights,pal,lat2,body2,carrier2

def parity_sign(mask: int, value: int) -> int:
    return -1 if (mask & value).bit_count() & 1 else 1

def block_body_spectrum_formula(n: int) -> np.ndarray:
    """Predict FWHT of E2=2*E using the corrected full-block formula.
    The r=K palindrome slot is retained but contributes zero via eta=1[r<K]."""
    N=1<<n; M=N//2; h=n//2; H=1<<h
    out=np.zeros(N,dtype=np.int64)
    for s in range(N):
        if s.bit_count() & 1:
            continue
        t=s & (M-1)
        accum=0
        for K in range(1,H):
            e=int(K>=H//2)
            S=K+e
            D=K*(K-1)//2+max(0,K-H//2)
            rs=sorted(range(S), key=lambda r: reverse_int(r,h))
            middle_values=(None,) if n%2==0 else (1,0)
            for mu in middle_values:
                qstart=D if mu is None else 2*D+(1-mu)*S
                for i,r in enumerate(rs):
                    eta=int(r<K)
                    if not eta: v2=0
                    elif mu is None: v2=2*(h-K.bit_count()-r.bit_count())
                    else: v2=2*h-1+2*mu-2*K.bit_count()-2*r.bit_count()
                    if v2:
                        accum += v2*parity_sign(t,qstart+i)
        out[s]=2*(-1 if t.bit_count()&1 else 1)*accum
    return out

def palindrome_word(u: int, n: int) -> int:
    m=(n+1)//2
    if n%2==0:
        return (u<<m)|reverse_int(u,m)
    return (u<<(m-1))|reverse_int(u>>1,m-1)

def carrier_spectrum_formula(n: int, position_of_word: np.ndarray) -> np.ndarray:
    """Predict FWHT of O2=2*z_- through canonical palindrome half-word placement."""
    N=1<<n; m=(n+1)//2
    out=np.zeros(N,dtype=np.int64)
    for u in range(1<<(m-1)):
        p=palindrome_word(u,n)
        address=int(position_of_word[p])
        z2=2*p.bit_count()-n
        if z2==0: continue
        for s in range(N):
            # Only odd spectral masks can receive the anti-symmetric carrier.
            if s.bit_count()&1:
                out[s]+=2*z2*parity_sign(s,address)
    return out

def audit_hole1():
    rows=[]; total_coeffs=0; total_body_checks=0; total_carrier_checks=0
    expected_degree2={6:0.53125,8:0.559937,10:0.519287,12:0.467403,16:0.389498,20:0.327503}
    for n in range(2,21):
        ring,w,pal,lat2,body2,carrier2=ring_data(n)
        full_spec=fwht(lat2)
        body_spec=fwht(body2)
        carrier_spec=fwht(carrier2)
        if not np.array_equal(full_spec,body_spec+carrier_spec):
            raise AssertionError(("decomposition",n))
        if any(body_spec[s]!=0 for s in range(1<<n) if s.bit_count()&1):
            raise AssertionError(("body parity",n))
        if any(carrier_spec[s]!=0 for s in range(1<<n) if not(s.bit_count()&1)):
            raise AssertionError(("carrier parity",n))
        masks=np.arange(1<<n,dtype=np.uint32)
        degrees=popcount_array(masks).astype(np.int64)
        total_energy=int(np.dot(full_spec,full_spec))
        body_energy=int(np.dot(body_spec,body_spec))
        deg2_energy=int(np.dot(full_spec[degrees==2],full_spec[degrees==2]))
        body_deg2_energy=int(np.dot(body_spec[degrees==2],body_spec[degrees==2]))
        deg1_energy=int(np.dot(full_spec[degrees==1],full_spec[degrees==1]))
        row={"n":n,"N":1<<n,"active_full_modes":int(np.count_nonzero(full_spec)),
             "degree2_full_share":deg2_energy/total_energy,
             "degree2_body_share":body_deg2_energy/body_energy if body_energy else 0,
             "degree1_full_share":deg1_energy/total_energy,
             "even_odd_decomposition_exact":True}
        if n in expected_degree2:
            row["matches_reported_degree2_4dp"] = round(row["degree2_full_share"],4)==round(expected_degree2[n],4)
        # Exact formula vs direct coefficients on widths <= 12.
        if n<=12:
            predicted_body=block_body_spectrum_formula(n)
            pos=np.empty(1<<n,dtype=np.int64); pos[ring.astype(np.int64)]=np.arange(1<<n,dtype=np.int64)
            predicted_carrier=carrier_spectrum_formula(n,pos)
            if not np.array_equal(predicted_body,body_spec):
                bad=np.flatnonzero(predicted_body!=body_spec)
                i=int(bad[0]); raise AssertionError(("body formula mismatch",n,i,int(predicted_body[i]),int(body_spec[i])))
            if not np.array_equal(predicted_carrier,carrier_spec):
                bad=np.flatnonzero(predicted_carrier!=carrier_spec)
                i=int(bad[0]); raise AssertionError(("carrier formula mismatch",n,i,int(predicted_carrier[i]),int(carrier_spec[i])))
            total_body_checks += (1<<n); total_carrier_checks += (1<<n)
            row["body_formula_coefficients_checked"] = 1<<n
            row["carrier_formula_coefficients_checked"] = 1<<n
        rows.append(row)
    return {"status":"PASS","n_widths":len(rows),"per_width":rows,
            "direct_formula_coefficients_checked_body":total_body_checks,
            "direct_formula_coefficients_checked_carrier":total_carrier_checks,
            "n20_active_modes":rows[-1]["active_full_modes"],
            "degree2_expected_share_matches":all(r.get("matches_reported_degree2_4dp",True) for r in rows)}

def target_profile(D: int) -> str:
    if D<5: raise ValueError(D)
    return "100"+"1"*(D-5)+"00"

def certificate_angle(D: int):
    p=(2*D)//3+1
    u=Fraction(1,2)+Fraction(1,2**p)+Fraction(2,3*2**(D-1))
    return u,p

def replay_radial(D: int):
    u,p=certificate_angle(D); target=target_profile(D)
    rows=[]
    for L in range(1,D+1):
        scaled=(1<<L)*u
        i=scaled.numerator//scaled.denominator
        frac=scaled-i
        k=(L*frac.numerator)//frac.denominator
        # n=1 is the identity ring; scalar reader supports it.
        word=word_at(i,L)
        bit=format(word,f'0{L}b')[k] if 0<=k<L else None
        expected=target[L-1]
        offset=i-(1<<(L-1))
        rows.append({"L":L,"address":i,"seam_offset":offset,"slice":k,"word":format(word,f'0{L}b'),"bit":bit,"expected":expected,"pass":bit==expected})
    return {"D":D,"p":p,"u_num":u.numerator,"u_den":u.denominator,
            "total_slices":len(rows),"matches":sum(r["pass"] for r in rows),
            "failures":[r for r in rows if not r["pass"]],"trace":rows}

def audit_hole2c():
    cases=[replay_radial(D) for D in range(13,97)]
    groups={}
    for c in cases:
        key=str(c["D"]%3)
        item=groups.setdefault(key,{"D_mod_3":int(key),"D_count":0,"fully_matching_D":0,"total_slice_tests":0,"slice_matches":0,"first_failure":None})
        item["D_count"]+=1; item["fully_matching_D"]+=int(not c["failures"])
        item["total_slice_tests"]+=c["total_slices"]; item["slice_matches"]+=c["matches"]
        if item["first_failure"] is None and c["failures"]:
            f=c["failures"][0]; item["first_failure"]={"D":c["D"],"L":f["L"],"address":f["address"],"slice":f["slice"],"word":f["word"],"got":f["bit"],"expected":f["expected"]}
    # Independently verify the offset formula on each L >= p using exact rational arithmetic.
    offset_checks=0
    for c in cases:
        D,p=c["D"],c["p"]; u=Fraction(c["u_num"],c["u_den"])
        for L in range(p,D+1):
            scaled=(1<<L)*(u-Fraction(1,2))
            q=scaled.numerator//scaled.denominator
            # Exact second term in q_L, valid for all L>=p.
            second=Fraction(2,3)*Fraction(1,1<<(D-L-1)) if D-L-1>=0 else Fraction(2,3)*Fraction(1<<(-D+L+1),1)
            pred=(1<<(L-p))+(second.numerator//second.denominator)
            if q!=pred:
                raise AssertionError(("offset",D,L,q,pred))
            offset_checks+=1
    return {"status":"PASS_OFFSET_FORMULA_BUT_PROFILE_FAILS_SOME_CASES","D_range":[13,96],"cases":cases,"residue_summary":list(groups.values()),"offset_formula_checks":offset_checks}

def audit_hole3_availability():
    # Inspect the available source bundle for an executable ROBDD/SHA implementation.
    relevant=[]
    roots=[Path('/mnt/data'),Path('/mnt/data/relation_layer_five_holes_review')]
    for root in roots:
        if root.exists():
            for p in root.rglob('*'):
                if p.is_file() and (('bdd' in p.name.lower()) or ('sha256' in p.name.lower()) or ('cofactor' in p.name.lower())):
                    relevant.append(str(p))
    zip_path=Path('/mnt/data/nexus_exact_certificates(2).zip')
    zip_entries=[]
    if zip_path.exists():
        with zipfile.ZipFile(zip_path) as z:
            zip_entries=z.namelist()
    has_bdd=any('cofactor_inverse_bdd.py' in p or 'cofactor_inverse_bdd.py' in Path(p).name for p in relevant+zip_entries)
    return {"status":"OPEN_PROVIDER_MISSING" if not has_bdd else "PROVIDER_FOUND_NEEDS_EXECUTION",
            "cofactor_inverse_bdd_found":has_bdd,"candidate_files":relevant,"exact_cert_archive_entries":zip_entries[:80],
            "named_certificate":"C(H) = {a in R_512 : TailValid(a) AND PadValid(a) AND DigestClosure(a)}",
            "missing_to_claim_RUNS":["runnable ROBDD package/API","variable ordering and node schema","backward schedule-tail relation","PadValid and digest-closure predicates","equivalence or preservation check against unpruned constraints","same-order node-count benchmark"]}

def main():
    t0=time.perf_counter()
    h1=audit_hole1()
    h2=audit_hole2c()
    h3=audit_hole3_availability()
    result={"hole1":h1,"hole2c":h2,"hole3":h3,"elapsed_seconds":time.perf_counter()-t0}
    (OUT/'three_holes_results.json').write_text(json.dumps(result,indent=2))
    # Compact CSVs for spectrum and radial residue summary.
    import csv
    with (OUT/'spectrum_widths.csv').open('w',newline='') as f:
        rows=h1['per_width']; w=csv.DictWriter(f,fieldnames=sorted(set().union(*(r.keys() for r in rows)))); w.writeheader();w.writerows(rows)
    with (OUT/'radial_residue_summary.csv').open('w',newline='') as f:
        rows=h2['residue_summary'];w=csv.DictWriter(f,fieldnames=list(rows[0].keys()));w.writeheader();w.writerows(rows)
    print(json.dumps({"hole1":{"status":h1['status'],"body_coeffs":h1['direct_formula_coefficients_checked_body'],"carrier_coeffs":h1['direct_formula_coefficients_checked_carrier'],"n20_active_modes":h1['n20_active_modes'],"degree2":{str(r['n']):r['degree2_full_share'] for r in h1['per_width'] if r['n'] in (6,8,10,12,16,20)}},
                      "hole2c":{"status":h2['status'],"offset_checks":h2['offset_formula_checks'],"residue_summary":h2['residue_summary'],"first_global_failure":next(({'D':c['D'],'L':c['failures'][0]['L'],'word':c['failures'][0]['word'],'got':c['failures'][0]['bit'],'expected':c['failures'][0]['expected']} for c in h2['cases'] if c['failures']),None)},
                      "hole3":h3,"elapsed_seconds":result['elapsed_seconds']},indent=2))

if __name__=='__main__':main()
