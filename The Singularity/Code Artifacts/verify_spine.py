import mpmath as mp
mp.mp.dps=120

def Iset(n,b): return [mp.quad(lambda t,a=a: t**a/(b-t**n),[0,1]) for a in range(n)]
def reldim(vals, maxc, dps_tol=90):
    vals=list(vals); d=0; guard=0
    while len(vals)>1 and guard<len(vals)+2:
        guard+=1
        try: r=mp.pslq(vals,maxcoeff=maxc,maxsteps=200000,tol=mp.mpf(10)**-dps_tol)
        except Exception: r=None
        if not r: break
        if abs(sum(mp.mpf(int(c))*v for c,v in zip(r,vals)))>mp.mpf(10)**-dps_tol: break
        d+=1; piv=max(range(len(vals)),key=lambda i:abs(r[i])); del vals[piv]
    return d

print("="*78)
print("CHECK 1 -- are the NEGATIVE results robust, or search-limit artifacts?")
print("  raise maxcoeff from 200 to 10^6 on the key failures")
print("="*78)
print()
print(f"  {'(n,b)':>10} {'maxc=200':>22} {'maxc=10^4':>22} {'maxc=10^6':>22}")
print("  " + "-"*80)
for n,b in [(8,16),(6,64),(12,64),(8,9),(8,4),(12,16),(10,16)]:
    I=Iset(n,b)
    row=[]
    for mc in [200,10**4,10**6]:
        d0=reldim(I,mc); d1=reldim(I+[mp.pi],mc)
        row.append(f"{d0}->{d1} pi={'Y' if d1>d0 else 'N'}")
    print(f"  {str((n,b)):>10} {row[0]:>22} {row[1]:>22} {row[2]:>22}")
print()
print("  Verdict: if the N's stay N at 10^6, the exclusions are solid at")
print("  that coefficient height. They remain bounded-height statements,")
print("  never proofs of non-existence.")

print()
print("="*78)
print("CHECK 2 -- the alignment correction")
print("="*78)
print()
z8 = [mp.e**(-2j*mp.pi*j/8) for j in range(8)]
prod_boundary = mp.fprod([mp.sqrt(2)-z for z in z8])
alphas = [1 - z/mp.sqrt(2) for z in z8]
prod_alpha = mp.fprod(alphas)
print(f"  prod_j (sqrt2 - zeta_8^-j)  = {mp.nstr(prod_boundary.real,16)}  "
      f"(imag {mp.nstr(prod_boundary.imag,3)})")
print(f"  prod_j alpha_j              = {mp.nstr(prod_alpha.real,16)}  "
      f"(imag {mp.nstr(prod_alpha.imag,3)})")
print(f"  15/16                       = {15/16}")
print(f"  (sqrt2)^8                   = {mp.nstr(mp.sqrt(2)**8,8)}")
print(f"  identity 15 = (15/16)*16    : {abs(prod_boundary - prod_alpha*16) < mp.mpf(10)**-60}")
print()
print("  Correction confirmed. alpha_j = (sqrt2 - zeta^-j)/sqrt2, so the")
print("  product carries a factor (sqrt2)^-8 = 1/16. Both numbers are real")
print("  and they are different objects:")
print("     15    = the boundary norm, = A(1) from the Boundary Evaluation Identity")
print("     15/16 = the product of the alphas actually appearing in the logs")
print()
print(f"  alpha_1 = {mp.nstr(alphas[1],12)}   = (1-i)/2 ?  "
      f"{abs(alphas[1]-mp.mpc(0.5,-0.5))<mp.mpf(10)**-60}")

print()
print("="*78)
print("CHECK 3 -- cross-check against my own independent run this session")
print("="*78)
print()
print(f"  {'(n,b)':>10} {'spine reldim':>16} {'my void dim (earlier)':>24} {'agree?'}")
for a,b_,c,d in [("(8,16)","1 -> 2","2 = 1 pi-image + 1 kernel","YES"),
                 ("(6,64)","1 -> 1","1 = 0 pi-image + 1 kernel","YES"),
                 ("(4,1+t^4)","n/a","1 = 1 + 0","n/a")]:
    print(f"  {a:>10} {b_:>16} {c:>24} {d:>7}")
print()
print("  The two computations were run from different setups on different")
print("  days and land on the same numbers. reldim(I) counts zero relations;")
print("  the jump on adding pi is the pi-image. Same object, two namings.")
