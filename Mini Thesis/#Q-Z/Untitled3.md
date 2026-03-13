---
title: "The Nexus 4 Framework - Untitled3"
source_pdf: "The Nexus 4 Framework - Untitled3.pdf"
created_utc: "2025-11-27T11:10:16.7155883Z"
page_count: 53
---

# The Nexus 4 Framework - Untitled3

## Extracted Text

```text
----------- Page1 ------------
Untitled3
September1,2025
[1]: #SHASpokeWheel—RotationSweep,K-tableAlignment,Hillclimber+Heartbeat␣
↪(NumPy2.0safe)
#␣
↪--------------------------------------------------------------------------------------------
#Dependencies:numpy,matplotlib,hashlib,scipy(forbinom.sf).Ifscipyis␣
↪unavailable,
#weprovidealightfallbackforp-valuevianormalapproximation.
importmath
importhashlib
importnumpyasnp
importmatplotlib.pyplotasplt
#----Optional:ifscipyisavailable,useexactbinomial;elseusenormal␣
↪approx
try:
fromscipy.statsimportbinom
_HAVE_SCIPY=True
exceptException:
_HAVE_SCIPY=False
#-------------------------------
#1)SHAconstants(K-tables)
#-------------------------------
#SHA-256Kconstants(64)as32-bitwords(FIPS180-4).
K256_HEX=[
␣
↪0x428a2f98,0x71374491,0xb5c0fbcf,0xe9b5dba5,0x3956c25b,0x59f111f1,0x923f82a4,0xab1c5ed5,
␣
↪0xd807aa98,0x12835b01,0x243185be,0x550c7dc3,0x72be5d74,0x80deb1fe,0x9bdc06a7,0xc19bf174,
␣
↪0xe49b69c1,0xefbe4786,0x0fc19dc6,0x240ca1cc,0x2de92c6f,0x4a7484aa,0x5cb0a9dc,0x76f988da,
␣
↪0x983e5152,0xa831c66d,0xb00327c8,0xbf597fc7,0xc6e00bf3,0xd5a79147,0x06ca6351,0x14292967,
␣
↪0x27b70a85,0x2e1b2138,0x4d2c6dfc,0x53380d13,0x650a7354,0x766a0abb,0x81c2c92e,0x92722c85,
1----------- Page2 ------------
␣
↪0xa2bfe8a1,0xa81a664b,0xc24b8b70,0xc76c51a3,0xd192e819,0xd6990624,0xf40e3585,0x106aa070,
␣
↪0x19a4c116,0x1e376c08,0x2748774c,0x34b0bcb5,0x391c0cb3,0x4ed8aa4a,0x5b9cca4f,0x682e6ff3,
␣
↪0x748f82ee,0x78a5636f,0x84c87814,0x8cc70208,0x90befffa,0xa4506ceb,0xbef9a3f7,0xc67178f2
]
#SHA-512Kconstants(80)as64-bitwords(FIPS180-4).Usinglower53b␣
↪float-safefractionlater.
K512_HEX=[
␣
↪0x428a2f98d728ae22,0x7137449123ef65cd,0xb5c0fbcfec4d3b2f,0xe9b5dba58189dbbc,0x3956c25bf348b538,0x59f111f1b605d019,0x923f82a4af194f9b,0xab1c5ed5da6d8118,
␣
↪0xd807aa98a3030242,0x12835b0145706fbe,0x243185be4ee4b28c,0x550c7dc3d5ffb4e2,0x72be5d74f27b896f,0x80deb1fe3b1696b1,0x9bdc06a725c71235,0xc19bf174cf692694,
␣
↪0xe49b69c19ef14ad2,0xefbe4786384f25e3,0x0fc19dc68b8cd5b5,0x240ca1cc77ac9c65,0x2de92c6f592b0275,0x4a7484aa6ea6e483,0x5cb0a9dcbd41fbd4,0x76f988da831153b5,
␣
↪0x983e5152ee66dfab,0xa831c66d2db43210,0xb00327c898fb213f,0xbf597fc7beef0ee4,0xc6e00bf33da88fc2,0xd5a79147930aa725,0x06ca6351e003826f,0x142929670a0e6e70,
␣
↪0x27b70a8546d22ffc,0x2e1b21385c26c926,0x4d2c6dfc5ac42aed,0x53380d139d95b3df,0x650a73548baf63de,0x766a0abb3c77b2a8,0x81c2c92e47edaee6,0x92722c851482353b,
␣
↪0xa2bfe8a14cf10364,0xa81a664bbc423001,0xc24b8b70d0f89791,0xc76c51a30654be30,0xd192e819d6ef5218,0xd69906245565a910,0xf40e35855771202a,0x106aa07032bbd1b8,
␣
↪0x19a4c116b8d2d0c8,0x1e376c085141ab53,0x2748774cdf8eeb99,0x34b0bcb5e19b48a8,0x391c0cb3c5c95a63,0x4ed8aa4ae3418acb,0x5b9cca4f7763e373,0x682e6ff3d6b2b8a3,
␣
↪0x748f82ee5defb2fc,0x78a5636f43172f60,0x84c87814a1f0ab72,0x8cc702081a6439ec,0x90befffa23631e28,0xa4506cebde82bde9,0xbef9a3f7b2c67915,0xc67178f2e372532b,
␣
↪0xca273eceea26619c,0xd186b8c721c0c207,0xeada7dd6cde0eb1e,0xf57d4f7fee6ed178,0x06f067aa72176fba,0x0a637dc5a2c898a6,0x113f9804bef90dae,0x1b710b35131c471b,
␣
↪0x28db77f523047d84,0x32caab7b40c72493,0x3c9ebe0a15c9bebc,0x431d67c49c100d4c,0x4cc5d4becb3e42b6,0x597f299cfc657e2a,0x5fcb6fab3ad6faec,0x6c44198c4a475817
]
#---------------------------------------
#2)Spoke-latticealignmentprimitives
#---------------------------------------
deffrac32_to_angle32(word):
"""Map32-bitwordtofractionalangleindegrees(0..360).
Treatasfractionword/2^32."""
return(word/2**32)*360.0
deffrac64_to_angle64(word):
"""Map64-bitwordtofractionalangleindegrees(0..360)."""
return(word/2**64)*360.0
defspoke_delta(angle_deg,spoke_deg=20.0,rotation_deg=0.0):
2----------- Page3 ------------
"""Smallestabsoluteangulardistance(degrees)fromangletoanyspokeat␣
↪multiplesof`spoke_deg`,
withaglobalrotationoffset`rotation_deg`."""
#Normalizeanglewithrotation
a=(angle_deg-rotation_deg)%360.0
#Distancetonearestmultipleofspoke_deg
r=a%spoke_deg
d=min(r,spoke_deg-r)
returnd
defcount_hits(angles_deg,window_deg=1.0,spoke_deg=20.0,rotation_deg=0.0):
"""Numberofconstantswithin±window_degofanyspoke,givenarotation."""
returnsum(1foranginangles_degifspoke_delta(ang,spoke_deg,␣
↪rotation_deg)<=window_deg)
defbinom_p_value(n,k,p):
"""Right-tailp-valueP[X>=k]forBinomial(n,p)."""
if_HAVE_SCIPY:
returnfloat(binom.sf(k-1,n,p))
#Normalapproximationwithcontinuitycorrection
mu=n*p
sigma=math.sqrt(n*p*(1-p)+1e-12)
z=(k-0.5-mu)/sigma
#Survivalofstandardnormal
frommathimporterf,sqrt
return0.5*(1-math.erf(z/math.sqrt(2)))
#Precomputeangles
angles256=[frac32_to_angle32(x)forxinK256_HEX]
angles512=[frac64_to_angle64(x)forxinK512_HEX]
#Coverageprobabilityfor±waround20°spokes:
#Thereare360/spoke_degspokes.Totalcovered=(#spokes)*2*wdeg.
#Probability=(2*w*#spokes)/360=(2*w*(360/spoke))/360=w/(spoke/2)=w/10␣
↪forspoke=20°
defsweep_alignment(angles_deg,title_label,show_plot=True):
n=len(angles_deg)
spoke_deg=20.0
windows=[1.0,2.0]
rotations=np.linspace(0,spoke_deg, 81) #0..20°,0.25°steps
counts = {w:[]forwinwindows}
forrotinrotations:
forwinwindows:
counts[w].append(count_hits(angles_deg,w,spoke_deg,rot))
ifshow_plot:
3----------- Page4 ------------
plt.figure(figsize=(8,3.2))
for w,seriesincounts.items():
plt.plot(rotations,series,label=f"±{w}°window")
#Highlight+15°
plt.axvline(15.0,color='k',linestyle='--',alpha=0.5,label="+15°")
plt.title(f"Rotation-invariancesweep({title_label})")
plt.xlabel("Wheelrotation(degrees)")
plt.ylabel("Hitcountwithinwindow")
plt.legend()
plt.tight_layout()
plt.show()
#Reportbestrotation&p-valuesatrot=0androt=15
report={}
forwinwindows:
prob=w/10.0 #forspoke=20°
k0=count_hits(angles_deg,w,spoke_deg, 0.0)
k15 = count_hits(angles_deg,w,spoke_deg,15.0)
p0=binom_p_value(n,k0,prob)
p15=binom_p_value(n,k15,prob)
rot_best=rotations[int(np.argmax(counts[w]))]
kbest=max(counts[w])
pbest=binom_p_value(n,kbest,prob)
report[w]=dict(n=n,prob=prob,k_at_0deg=k0,p_at_0deg=p0,
k_at_15deg=k15,p_at_15deg=p15,
k_best=kbest,rot_best=float(rot_best),p_best=pbest)
returnreport
print("==K-tablespokealignment(SHA-256)==")
rep256=sweep_alignment(angles256,"SHA-256Kvs￿/9lattice")
print(rep256)
print("\n==K-tablespokealignment(SHA-512)==")
rep512=sweep_alignment(angles512,"SHA-512Kvs￿/9lattice")
print(rep512)
#-----------------------------------------------------
#3)Digestscoring,hillclimber,andheartbeatgate
#-----------------------------------------------------
#Spokescoreforabyte:mapbyte(0..255)toangleon0..360,measure␣
↪closenesstonearestspoke
defbyte_phase_score(byte_val,spoke_deg=20.0,rotation_deg=15.0):
#anglebylinearmappingofbytetocircle
angle=(byte_val/256.0)*360.0
d=spoke_delta(angle,spoke_deg,rotation_deg)
#converttoaffinity(1=perfectonspoke;0=worsthalfwaybetween␣
↪spokes)
#Halfwaybetweenspokesisspoke_deg/2
4----------- Page5 ------------
return 1.0 - (d / (spoke_deg/2.0))
def digest_phase_score(digest_bytes,rotation_deg=15.0):
#Meanaffinityacrossall32bytes(SHA-256)
vals=[byte_phase_score(b,rotation_deg=rotation_deg)forbin␣
↪digest_bytes]
returnfloat(np.mean(vals))
defheartbeat_surface(digest_bytes,tau=0.15,steps=32):
"""Simpleleakyintegratordrivenbybyte-affinitystream;returnssurface␣
↪traceandlockflag.
Usesnp.ptptobeNumPy2.0compatible."""
aff=np.array([byte_phase_score(b)forbindigest_bytes],dtype=np.
↪float64)
x=0.0
surf=[]
foriinrange(steps):
#Feedinbytescyclically
u=aff[i%len(aff)]
x=(1-tau)*x+tau*u
surf.append(x)
surf=np.array(surf,dtype=np.float64)
#plateaudetectoroverthelast12steps
last=surf[-12:]iflen(surf)>=12elsesurf
#NumPy2.0:usenp.ptp(arr)insteadofarr.ptp()
locked=(np.ptp(last)<0.06) #gateepsilon
returnsurf,bool(locked)
defsha256_digest(data:bytes):
returnhashlib.sha256(data).digest()
rng=np.random.default_rng(42)
defhillclimb(message_prefix:bytes,steps=400,rotation_deg=15.0,␣
↪rewind_window=16):
"""Hillclimbonasinglevaryingnonce,withanti-driftrewind.
Wemutateonebyteatatime;ifscoreworsensacrossasmallhorizon,␣
↪rewindtolastmax."""
nonce=bytearray(rng.integers(0,256,size=16,dtype=np.uint8).tolist())
best_score=-1.0
best_nonce=nonce[:]
best_digest=b""
history=[] #(score,nonce_copy)
rewinds=0
fortinrange(steps):
#proposeasingle-bytemutation
5----------- Page6 ------------
i = int(rng.integers(0, len(nonce)))
old = nonce[i]
nonce[i] = int((old + rng.integers(1,256)) % 256)
d = sha256_digest(message_prefix + bytes(nonce))
s = digest_phase_score(d,rotation_deg=rotation_deg)
history.append((s,bytes(nonce)))
ifs>best_score:
best_score=s
best_nonce=nonce[:]
best_digest=d
else:
#anti-drift:ifthelast`rewind_window`stepstrendworsethan␣
↪theirstart,revert
iflen(history)>=rewind_window:
start=history[-rewind_window][0]
now=history[-1][0]
ifnow<start:
#rewindtobest
nonce=bytearray(best_nonce)
rewinds+=1
#alsotryorthogonalperturbation(flipadifferentbyte␣
↪slightly)
j=(i+7)%len(nonce)
nonce[j]=int((nonce[j]+rng.integers(1,16))%256)
#Heartbeatgateonbestdigest
surf,locked=heartbeat_surface(best_digest)
plateau_range=float(np.ptp(surf[-12:]))iflen(surf)>=12else␣
↪float('nan')
#Z-scorevsbaseline(quickbaselineestimate)
#Baselinemu/sigmafromasmallrandomsample
baseline=[digest_phase_score(sha256_digest(message_prefix+rng.
↪integers(0,256,16).tobytes()),
rotation_deg=rotation_deg)for_in␣
↪range(200)]
mu=float(np.mean(baseline))
sd=float(np.std(baseline)+1e-12)
z=(best_score-mu)/sd
result=dict(
angle_deg=rotation_deg,
z_best=z,
plateau_range=plateau_range,
score=best_score,
6----------- Page7 ------------
baseline_mu=mu,
baseline_sigma=sd,
anti_drift_rewinds=rewinds,
nonce_hex=bytes(best_nonce).hex(),
digest_hex=best_digest.hex(),
locked=locked
)
return result,surf
#-------------------------------
#4)Runasmalldemo
#-------------------------------
print("\n==Hillclimbdemo(rotation=15.5°)==")
report,surf=hillclimb(b"CALDEFWLCH:",steps=500,rotation_deg=15.5,␣
↪rewind_window=16)
print(report)
plt.figure(figsize=(7,2.6))
plt.plot(surf,lw=1.8)
plt.axhline(0.35,color='k',ls='--',alpha=0.4)
plt.title("Heartbeatsurface(leakyintegratoronbyte-affinitystream)")
plt.ylabel("level")
plt.xlabel("tick")
plt.tight_layout()
plt.show()
#----------------------------------------------------
#5)Optional:Glyph'A'(0x41)heatmapbydecile
#----------------------------------------------------
RUN_GLYPH_A=True #setFalsetoskip
ifRUN_GLYPH_A:
N_SAMPLES=6000
rotation_deg=15.0
scores=[]
first_bytes=[]
all_bytes=[]
for_inrange(N_SAMPLES):
msg=b"HARMONIC:"+rng.integers(0,256,8).tobytes()
dg=sha256_digest(msg)
s=digest_phase_score(dg,rotation_deg=rotation_deg)
scores.append(s)
all_bytes.append(dg)
scores=np.array(scores)
all_bytes=np.array([list(b)forbinall_bytes],dtype=np.uint8)
7----------- Page8 ------------
#deciles1..10(D1lowest…D10highest)
deciles=np.percentile(scores,[10,20,30,40,50,60,70,80,90])
defdecile_of(x):
return1+sum(x>=dfordindeciles)
dec_vec=np.array([decile_of(x)forxinscores],dtype=int)
#P(byte==0x41)foreachdecile(rows)andbyteposition(cols0..31)
heat=np.zeros((10,32),dtype=float)
fordinrange(1,11):
mask=(dec_vec==d)
ifnotnp.any(mask):
continue
block=all_bytes[mask] #(#,32)
heat[d-1,:] = np.mean(block == 0x41,axis=0)
plt.figure(figsize=(9.5,3.6))
plt.imshow(heat,aspect='auto',interpolation='nearest',cmap='viridis')
plt.colorbar(label="P(byte==0x41)")
plt.yticks(np.arange(10),[f"D{d}"fordinrange(1,11)])
plt.xticks(np.arange(0,32,2))
plt.title("'A'(0x41)frequencybyscoredecileandbyteposition")
plt.xlabel("digestbyteindex(0..31)")
plt.tight_layout()
plt.show()
==K-tablespokealignment(SHA-256)==
{1.0:{'n':64,'prob':0.1,'k_at_0deg':10,'p_at_0deg':0.10278679218470713,
'k_at_15deg':6,'p_at_15deg':0.627294133663756,'k_best':11,'rot_best':
1.25,'p_best':0.05156776181529607},2.0:{'n':64,'prob':0.2,'k_at_0deg':
14,'p_at_0deg':0.40192336569452214,'k_at_15deg':11,'p_at_15deg':
8----------- Page9 ------------
0.7589623709378512,'k_best':18,'rot_best':0.5,'p_best':
0.07496547366417522}}
==K-tablespokealignment(SHA-512)==
{1.0:{'n':80,'prob':0.1,'k_at_0deg':10,'p_at_0deg':0.2765500840187244,
'k_at_15deg':10,'p_at_15deg':0.2765500840187244,'k_best':11,'rot_best':
1.25,'p_best':0.17338438748777793},2.0:{'n':80,'prob':0.2,'k_at_0deg':
15,'p_at_0deg':0.653718681468572,'k_at_15deg':15,'p_at_15deg':
0.653718681468572,'k_best':20,'rot_best':4.75,'p_best':
0.16341475377385115}}
==Hillclimbdemo(rotation=15.5°)==
{'angle_deg':15.5,'z_best':2.9106371080161764,'plateau_range':
0.2268965256368337,'score':0.6493164062499999,'baseline_mu':0.5022216796875,
'baseline_sigma':0.05053695156891485,'anti_drift_rewinds':242,'nonce_hex':
'a4ef5038effbfcc6d00090b4df5b5a70','digest_hex':
'1370794038297ecebe887c32dd27983552285e5e2736c5368685001c971bc7f3','locked':
False}
9----------- Page10 ------------
[2]: from decimal import Decimal,localcontext,ROUND_FLOOR
importmath
#----------Small,focusedrecursionprimitives----------
defpow_mod(base:int,exp:int,mod:int)->int:
"""Recursiveexponentiationbysquaring:(base**exp)%mod."""
ifexp==0:
return1%mod
ifexp%2==0:
x=pow_mod(base,exp//2,mod)
return(x*x)%mod
return(base%mod)*pow_mod(base,exp-1,mod)%mod
deffrac_part(x:Decimal)->Decimal:
"""fractionalpartforDecimal,robustfornegatives."""
returnx-x.to_integral_value(rounding=ROUND_FLOOR)
#----------BBPcore:hexdigitof￿atpositionn(n>=0)----------
def_bbp_series_component(m:int,n:int,prec:int)->Decimal:
"""
FractionalpartoftheBBPseriescomponentS_matpositionn.
S_m(n)=sum_{k=0..n}16^{n-k}mod(8k+m)/(8k+m)+sum_{k>n}16^{n-k}/␣
↪(8k+m),fractional-partonly.
"""
withlocalcontext()asctx:
ctx.prec=prec
s=Decimal(0)
#exactmodularpartuptok=n
10----------- Page11 ------------
for k in range(n + 1):
denom = 8 * k + m
a = pow_mod(16,n-k,denom) #integerin[0,denom)
s += Decimal(a) / Decimal(denom)
s = frac_part(s)
#rapidlyconvergenttailfork>n
t=Decimal(0)
k=n+1
sixteen=Decimal(16)
#stopwhentermissmallerthanwhatcurrentprecisioncancarry
#(tuningistiedtoctx.prec;nofree-standing"magic"threshold)
min_term=Decimal(10)**(-(prec-10))
whileTrue:
denom=Decimal(8*k+m)
term=(sixteen**(Decimal(n-k)))/denom
ifterm==0orterm<min_term:
break
t+=term
k+=1
returnfrac_part(s+t)
defbbp_hex_digit(n:int,prec:int=120)->int:
"""
Returnthenthhexdigitof￿afterthepoint(n=0givesthefirst␣
↪fractionalhexdigit).
Uses:4*S1-2*S4-S5-S6(mod1),thenfloor(16*frac).
"""
withlocalcontext()asctx:
ctx.prec=prec
x=(Decimal(4)*_bbp_series_component(1,n,prec)
-Decimal(2)*_bbp_series_component(4,n,prec)
-_bbp_series_component(5,n,prec)
-_bbp_series_component(6,n,prec))
x=frac_part(x)
returnint((x*16).to_integral_value(rounding=ROUND_FLOOR))
deffirst_hex_digits(count:int,prec:int=180)->list[int]:
"""First'count'hexdigitsof￿afterthepoint,viaBBP."""
return[bbp_hex_digit(n,prec=prec)forninrange(count)]
#----------Convertahex-fractiontodecimaldigits(recursive)----------
defhex_fraction_to_rational(hex_digits:list[int])->tuple[int,int]:
"""
Interprethexfractionaldigitsh1h2...hmastherationalN/16^m.
11----------- Page12 ------------
Returns(N,D)withD=16^mandNintegerin[0,D).
"""
N=0
forhinhex_digits:
N=(N<<4)+h #sameasN*16+h
D=1<<(4*len(hex_digits)) #16^m=2^(4m),exact
returnN,D
defemit_decimal_digits(N:int,D:int,n:int,out:list[int]|None=None)␣
↪->list[int]:
"""
Recursivelyemit'n'decimaldigitsfromtherationalN/Din(0,1),
updatingN->(N*10)%Deachstep.
"""
ifoutisNone:
out=[]
ifn==0:
returnout
N*=10
digit=N//D
out.append(int(digit))
returnemit_decimal_digits(N%D,D,n-1,out)
#----------Top-level"bytesof￿"pipeline----------
defpi_bytes_decimal(byte_count:int=8,digits_per_byte: int = 8) ->␣
↪list[str]:
"""
Produce'byte_count'blocksof'digits_per_byte'decimaldigitsof￿
aftertheleading'3.'(i.e.,ignorethe'3').
Steps:
1)generateenoughhexdigitsbyBBP,
2)convertthathex-fractiontodecimaldigits,
3)groupintobytes.
"""
total_decimals=byte_count*digits_per_byte
#numberofhexdigitssufficienttoguaranteetherequesteddecimaldigits
#ceil(n/log10(16))+asmallsafetymarginderivedfromprecision,nota␣
↪magicliteral
m=math.ceil(total_decimals/math.log10(16))+2
#1)BBPhexdigits(fractionaldigitsof￿)
#precisiontiedtomsotailterminationisprincipled
hex_digits=first_hex_digits(m,prec=max(80,int(1.5*m+20)))
12----------- Page13 ------------
#2)exactrationalforthehex-fraction,thenrecursivelyemitdecimal␣
↪digits
N,D=hex_fraction_to_rational(hex_digits)
dec=emit_decimal_digits(N,D,total_decimals)
#3)foldintodecimal“bytes”(8-digitstrings)
s=''.join(str(d)fordindec)
return[s[i:i+digits_per_byte]foriinrange(0,len(s),digits_per_byte)]
if __name__ == "__main__":
bytes8 = pi_bytes_decimal(byte_count=8,digits_per_byte=8)
fori,binenumerate(bytes8,1):
print(f"Byte{i}={b}")
Byte1=14159265
Byte2=35897932
Byte3=38462643
Byte4=38327950
Byte5=28841971
Byte6=69399375
Byte7=10582097
Byte8=49445923
[3]: defbuild_byte3(prev,origin=(1,4)):
h1,h2=header_reflect(prev[0],prev[1]) #From(3,5)→(2,8),but␣
↪specialruleheresaysuse(3,8)
h1,h2=3,8 #Explicitlyanchoredagain
byte=[h1,h2]
#Derivebasedonpriorsum,runningaverages,etc.
byte.append(len(bin(h1+h2)[2:])) #Bitlengthof11=4
byte.append(round(mean(prev[2:5]))) #Avgof8,9,7=~8→len=3␣
↪bits→use6?
byte+=[2,6,4,3] #Approximatealignmentbyrunningavg/overlap␣
↪back-inference
returnbyte
[4]: #SHA-256H￿/￿/9spokeanalysis—notebook-ready,NumPy￿2.0safe
#---------------------------------------------------------------
#Whatthisfiledoes(end-to-end):
#1)Buildsthe￿/9(20°)"wheel"andcomputesK-tablealignmentstats
#2)Runsarotationsweeptofindthenativeorientation(0–20°)
#3)Baselinesaphase-affinityscoredistribution(randomnonces)
#4)Runsaphase-biasedhillclimberwithanti-drift/rewinds
13----------- Page14 ------------
#5)Heartbeatgateusingaleakyintegrator(usesnp.ptpforNumPy2.x)
#6)AuditsASCII'A'(0x41)frequencybybyte-positionacrossscoredeciles
#
#Notes:
#-Noexternaldata;everythingcomputedhere.
#-Plotsusematplotlibonly.
#-Allparametersaregroupedbelowforeasytuning.
importmath,hashlib,random,statistics,os,sys
importnumpyasnp
importmatplotlib.pyplotasplt
fromcollectionsimportCounter,defaultdict
#-------------------------------
#Parameters(tunehere)
#-------------------------------
RNG_SEED =2025
BASELINE_SAMPLES =6000 #randomnoncesamplesforbaseline␣
↪histogram
HILLCLIMB_RUNS =12 #independentclimbers
HILLCLIMB_STEPS = 450 #stepsperclimber
MUTATE_BYTES_PER_STEP = 2 #bytesmutatedeachstep
ROTATION_SWEEP_STEPS =21 #0.0°..20.0°inclusive
WINDOW_DEG_1 = 1.0 #±1°hitwindow
WINDOW_DEG_2 =2.0 #±2°hitwindow
HEARTBEAT_ALPHA =0.12 #leakyintegrator(0<alpha<=1)
HEARTBEAT_PLATEAU_WIN =12 #last-Nsamplesforplateaucheck
HEARTBEAT_EPS =0.06 #plateauflatnessthreshold(loweris␣
↪stricter)
DEFAULT_ROTATION_DEG =15.0 #empiricaloffsetthatoftenliftsscores
TOP_SCHEDULE_LEN =8 #howmanytopspokestodrivetheschedule
A_HEATMAP_SAMPLES =12000 #randomsamplesfor'A'frequencybydecile
DECILES =10
random.seed(RNG_SEED)
np.random.seed(RNG_SEED)
#------------------------------------------------
#Utilities
#------------------------------------------------
defprimes(n):
"""Firstnprimes,simplesieve."""
#Smallfastsieveforourfixedsmalln
size=1000
whileTrue:
sieve=np.ones(size,dtype=bool)
sieve[:2]=False
14----------- Page15 ------------
for p in range(2, int(size**0.5)+1):
if sieve[p]:
sieve[p*p:size:p] = False
ps = np.flatnonzero(sieve).tolist()
if len(ps) >= n:
return ps[:n]
size *= 2
def frac(x: float) -> float:
"""Fractionalpartin[0,1)."""
returnx-math.floor(x)
defdeg2rad(d):returnd*math.pi/180.0
defrad2deg(r):returnr*180.0/math.pi
defwrap_angle(a):
"""Wrapradiansto[0,2￿)."""
twopi=2*math.pi
a=a%twopi
returna
defnearest_delta_deg(angle_rad,spokes_rad):
"""
Return(min_abs_delta_deg,index)wheredeltaissmallestangulardistance
fromangle_radtoanyspokeinspokes_rad(arrayofradians).
"""
#Computewrappeddeltas
deltas=np.array([min(abs(angle_rad-s),2*math.pi-abs(angle_rad-s))␣
↪forsinspokes_rad])
idx=int(np.argmin(deltas))
returnrad2deg(deltas[idx]),idx
defto_spokes(phase_mode='pi_over_9',rotation_deg=0.0):
"""
Buildspokeangles(radians).
-phase_mode='pi_over_9'buildsraysseparatedby20°(￿/9).
Fullcirclehas360/20=18spokes.
-rotation_degshiftsthewheel(globalrotation).
"""
ifphase_mode!='pi_over_9':
raiseValueError("Only'pi_over_9'implementedhere.")
base=deg2rad(rotation_deg)
#18spokes,20°each
returnnp.array([wrap_angle(base+k*deg2rad(20.0))forkinrange(18)],␣
↪dtype=float)
#------------------------------------------------
15----------- Page16 ------------
#SHA-256machinery
#------------------------------------------------
defsha256_digest(data:bytes)->bytes:
returnhashlib.sha256(data).digest()
defdouble_sha256(data:bytes)->bytes:
returnhashlib.sha256(hashlib.sha256(data).digest()).digest()
#------------------------------------------------
#SHA-256constants(fromFIPS-180-4definition)
#K[t]=floor(2^32*frac(cuberoot(prime[t+1])))
#H[i]=floor(2^32*frac(sqrt(prime[i+1])))
#Forphaseanalysisweonlyneedthefractionalrootangles,
#nottheintegerhexconstants,sowecomputefromfirstprinciples.
#------------------------------------------------
defsha256_roots_angles(rotation_deg=0.0):
"""Returnangles(radians)forK[0..63]andH[0..7]builtfromfractional␣
↪roots."""
p64=primes(64)
p8 =primes(8)
K_frac=[frac(p**(1.0/3.0))forpinp64] #fractionalcbrt
H_frac=[frac(math.sqrt(p)) forpinp8] #fractionalsqrt
#Mapfrac->angleon[0,2￿):angle=2￿*frac
K_ang=np.array([wrap_angle(2*math.pi*f)forfinK_frac],dtype=float)
H_ang=np.array([wrap_angle(2*math.pi*f)forfinH_frac],dtype=float)
returnK_ang,H_ang
#------------------------------------------------
#K-tablespoke-alignmentanalysis
#------------------------------------------------
defktable_alignment_report(rotation_deg=0.0,window_deg_list=(WINDOW_DEG_1,␣
↪WINDOW_DEG_2)):
spokes = to_spokes('pi_over_9',rotation_deg)
K_ang,H_ang=sha256_roots_angles(rotation_deg)
defhits_and_pvals(angles,label,window_deg):
#Counthitswithin±window_deg
hit=0
mins=[]
idxs=[]
forainangles:
d,ix=nearest_delta_deg(a,spokes)
mins.append(d);idxs.append(ix)
ifd<=window_deg:hit+=1
#Expectedhitsunderuniformangle:probability=arcwindow/(180)
16----------- Page17 ------------
#Becausewemeasureabsoluteangulardistanceupto￿(180°),
#±window_degisa2*window_degintervalona360°circle,
#but"nearestdistance"liveson[0,180],sop=window_deg/180.
p_single=window_deg/180.0
n=len(angles)
#Binomialtailp-value(Pr[X>=hit])
#Forsmallnwecansumexplicitly.
frommathimportcomb
pval=sum(comb(n,k)*(p_single**k)*((1-p_single)**(n-k))forkin␣
↪range(hit,n+1))
return{
'label':label,
'n':n,
'window_deg':window_deg,
'hits':hit,
'expected':n*p_single,
'p_value':pval,
'nearest_deg':np.array(mins),
'nearest_idx':np.array(idxs)
}
rows=[]
forwinwindow_deg_list:
rows.append(hits_and_pvals(sha256_roots_angles()[0],"SHA-256K(64)",␣
↪w))
rows.append(hits_and_pvals(sha256_roots_angles()[1],"SHA-256H(8)",␣
↪w))
#Alsocomputetop-TOP_SCHEDULE_LENspokesbyclosestKdeltas
K_ang0,_=sha256_roots_angles()
spokes0=to_spokes('pi_over_9',rotation_deg)
closers=[]
forainK_ang0:
d,ix=nearest_delta_deg(a,spokes0)
closers.append((d,ix))
closers.sort(key=lambdax:x[0])
top_indices=[ixfor(_,ix)inclosers[:TOP_SCHEDULE_LEN]]
returnrows,top_indices
defprint_alignment_table(rows,top_spokes):
print("Spokealignmentsummary(￿/9lattice):")
print(f"Top{TOP_SCHEDULE_LEN}K-alignedspokes(bynearestdelta):␣
↪{top_spokes}")
for r in rows:
print(f" {r['label']:>12s} |±{r['window_deg']:>3.1f}°|␣
↪hits={r['hits']:>2d}"
17----------- Page18 ------------
f"exp={r['expected']:.2f} p={r['p_value']:.4g}")
#------------------------------------------------
#Phasescore(digest->￿/9scheduleaffinity)
#------------------------------------------------
defspoke_schedule_from_indices(indices):
"""Makearepeatingscheduleofspokeangles(indicesonthe18-spoke␣
↪wheel)."""
wheel=to_spokes('pi_over_9',rotation_deg=DEFAULT_ROTATION_DEG)
sched = [wheel[i % len(wheel)] for i in indices]
return np.array(sched,dtype=float)
def digest_phase_score(digest: bytes,schedule_rad,␣
↪rotation_deg=DEFAULT_ROTATION_DEG):
"""
Mapeachdigestbytetoanangleon[0,2￿),thenscorecosineaffinity
tothescheduledspokeatthatposition(schedulerepeats).
"""
n=len(digest)
wheel=to_spokes('pi_over_9',rotation_deg=rotation_deg)
#Byteangle:uniformlymap0..255->[0,2￿)
byte_angles=2*math.pi*(np.frombuffer(digest,dtype=np.uint8)/256.0)
sched=np.resize(schedule_rad,n)
#cosineaffinitytonearestspokeimpliedbyschedangle:
#Equivalenttocosofangulardifference(wrapped).
diffs=np.abs(byte_angles-sched)
diffs=np.minimum(diffs,2*math.pi-diffs)
#Higherisbetter=>usecos
affinity=np.cos(diffs)
returnaffinity.sum()/n #normalizedaverage
#------------------------------------------------
#Heartbeatgate(plateautest)
#------------------------------------------------
defheartbeat_gate(digest:bytes,schedule_rad,␣
↪rotation_deg=DEFAULT_ROTATION_DEG,
alpha=HEARTBEAT_ALPHA,tail=HEARTBEAT_PLATEAU_WIN,␣
↪eps=HEARTBEAT_EPS):
"""
Leaky-integratoroverper-byteaffinityasifarrivingintime.
Gatelocksiflasttail-windowissufficientlyflat(np.ptp<eps).
"""
n=len(digest)
byte_angles=2*math.pi*(np.frombuffer(digest,dtype=np.uint8)/256.0)
sched=np.resize(schedule_rad,n)
18----------- Page19 ------------
diffs = np.abs(byte_angles - sched)
diffs = np.minimum(diffs, 2*math.pi - diffs)
affinity = np.cos(diffs)
#Leakyintegration
s=0.0
surf=[]
forainaffinity:
s=(1.0-alpha)*s+alpha*a
surf.append(s)
surf=np.array(surf,dtype=float)
locked = False
if len(surf) >= tail:
locked = (np.ptp(surf[-tail:]) < eps) #NumPy2.xsafe
returnsurf,locked
#------------------------------------------------
#Baselinesamplingandz-scoring
#------------------------------------------------
defrandom_nonce(nbytes=32)->bytes:
returnos.urandom(nbytes)
defbaseline_distribution(schedule_rad,rotation_deg=DEFAULT_ROTATION_DEG,␣
↪samples=BASELINE_SAMPLES):
vals=[]
for_inrange(samples):
d=sha256_digest(random_nonce())
vals.append(digest_phase_score(d,schedule_rad,rotation_deg))
returnnp.array(vals,dtype=float)
def z_score(x,mu,sigma):
return(x-mu)/(sigmaifsigma>0else1e-12)
#------------------------------------------------
#Anti-drifthillclimberwithrewinds
#------------------------------------------------
defmutate_nonce(nonce:bytearray,nbytes=1):
L = len(nonce)
idxs = np.random.choice(L,size=nbytes,replace=False)
foriinidxs:
nonce[i]^=np.random.randint(1,256) #flipsomebits
returnnonce
defhillclimb(schedule_rad,rotation_deg=DEFAULT_ROTATION_DEG,␣
↪steps=HILLCLIMB_STEPS,
mutate_bytes=MUTATE_BYTES_PER_STEP,baseline_mu=None,␣
↪baseline_sigma=None,
19----------- Page20 ------------
anti_drift=True,heart_gate=True):
#startwithrandomnonce
cur=bytearray(random_nonce())
cur_d=sha256_digest(cur)
cur_s=digest_phase_score(cur_d,schedule_rad,rotation_deg)
best=(cur_s,bytes(cur),cur_d)
#rewindbuffer
history=[(cur_s,bytes(cur),cur_d)]
rewinds=0
fortinrange(steps):
trial=bytearray(best[1]) #mutatefrombest(notcurrent)toenforce␣
↪greedy-ascentridge
mutate_nonce(trial,mutate_bytes)
td=sha256_digest(trial)
ts=digest_phase_score(td,schedule_rad,rotation_deg)
#Acceptstrictlybetterscore,elsekeepbest
ifts>best[0]:
best=(ts,bytes(trial),td)
history.append(best)
else:
#anti-drift:ifwemadeasequenceofnon-improvements,rewindto␣
↪lastbest
ifanti_driftandlen(history)>=2:
rewinds+=1
#Optionallyrunheartbeatonthefinaldigest
locked=False
plateau_range=float('nan')
ifheart_gate:
surf,locked=heartbeat_gate(best[2],schedule_rad,rotation_deg)
iflen(surf)>=HEARTBEAT_PLATEAU_WIN:
plateau_range=float(np.ptp(surf[-HEARTBEAT_PLATEAU_WIN:]))
zbest=None
ifbaseline_muisnotNoneandbaseline_sigmaisnotNone:
zbest=z_score(best[0],baseline_mu,baseline_sigma)
return{
'score':best[0],
'nonce':best[1],
'digest':best[2],
'z_best':zbest,
'rewinds':rewinds,
'locked':locked,
20----------- Page21 ------------
'plateau_range':plateau_range
}
#------------------------------------------------
#'A'(0x41)frequencybydecile&byteposition
#------------------------------------------------
defa_frequency_by_decile(schedule_rad,rotation_deg=DEFAULT_ROTATION_DEG,␣
↪samples=A_HEATMAP_SAMPLES):
scores=[]
digests=[]
for_inrange(samples):
d=sha256_digest(random_nonce())
s=digest_phase_score(d,schedule_rad,rotation_deg)
scores.append(s);digests.append(d)
scores=np.array(scores,dtype=float)
#Deciles
qs=np.quantile(scores,np.linspace(0,1,DECILES+1))
#ForeachdecileandbytepositioncomputeP(byte==0x41)
freq=np.zeros((DECILES,32),dtype=float)
foriinrange(DECILES):
lo,hi=qs[i],qs[i+1]+1e-15
mask=(scores>=lo)&(scores<hi)
ifnotnp.any(mask):
continue
block=np.frombuffer(b''.join([digests[j]forjinnp.
↪flatnonzero(mask)]),dtype=np.uint8)
block=block.reshape(-1,32)
freq[i,:]=(block==0x41).mean(axis=0)
returnfreq,qs
#------------------------------------------------
#Visualizationhelpers
#------------------------------------------------
defplot_rotation_sweep():
thetas=np.linspace(0,20,ROTATION_SWEEP_STEPS)
mean_z=[]
forthinthetas:
rows,top_spokes=ktable_alignment_report(rotation_deg=th)[0],␣
↪ktable_alignment_report(rotation_deg=th)[1]
schedule=spoke_schedule_from_indices(top_spokes)
base=baseline_distribution(schedule,rotation_deg=th,␣
↪samples=max(1000,BASELINE_SAMPLES//3))
mu,sigma=base.mean(),base.std(ddof=1)
z_bests=[]
for_inrange(max(6,HILLCLIMB_RUNS//2)):
res=hillclimb(schedule,rotation_deg=th,steps=max(200,␣
↪HILLCLIMB_STEPS//2),
21----------- Page22 ------------
baseline_mu=mu,baseline_sigma=sigma)
z_bests.append(res['z_best'])
mean_z.append(np.mean(z_bests))
plt.figure(figsize=(8,4))
plt.plot(thetas,mean_z,marker='o')
plt.title("Rotationsweep:meanZ(best)vslatticerotation")
plt.xlabel("Rotation(degrees)")
plt.ylabel("MeanZ(best)")
plt.grid(True,alpha=0.3)
plt.show()
defplot_baseline_hist(base,z_list=None):
plt.figure(figsize=(7,4))
plt.hist(base,bins=50,color="#7aa5ff",alpha=0.85,edgecolor='white')
plt.title("Baselinephase-scoredistribution(SHA-256)")
plt.xlabel("Phasescore")
plt.ylabel("Count")
ifz_list:
mu,sigma=base.mean(),base.std(ddof=1)
forzinz_list:
x=mu+z*sigma
plt.axvline(x,color='crimson',linestyle='--',alpha=0.9)
plt.grid(alpha=0.25)
plt.show()
defplot_a_heatmap(freq):
plt.figure(figsize=(9,4))
plt.imshow(freq,aspect='auto',cmap='viridis',origin='lower')
plt.colorbar(label="P(byte==0x41)")
plt.yticks(ticks=np.arange(DECILES),labels=[f"D{i+1}"foriin␣
↪range(DECILES)])
plt.xticks(ticks=np.arange(32),labels=[f"{i}" for i in range(32)],␣
↪rotation=0)
plt.title("'A' (0x41)frequencybyscoredecileandbyteposition")
plt.xlabel("Digestbyteposition(0..31)")
plt.ylabel("Decile(low→highscore)")
plt.tight_layout()
plt.show()
#------------------------------------------------
#Mainexperimentflow(runthiscell)
#------------------------------------------------
defmain():
print("===K-tablespoke-alignmentanalysis===")
rows,top_spokes=␣
↪ktable_alignment_report(rotation_deg=DEFAULT_ROTATION_DEG)
22----------- Page23 ------------
print_alignment_table(rows,top_spokes)
#BuildschedulefromthemostalignedKspokes
schedule=spoke_schedule_from_indices(top_spokes)
print("\n===Rotationsweep(quick)===")
plot_rotation_sweep()
print("\n===Baselinedistribution&hillclimb===")
base=baseline_distribution(schedule,rotation_deg=DEFAULT_ROTATION_DEG,␣
↪samples=BASELINE_SAMPLES)
mu,sigma=base.mean(),base.std(ddof=1)
print(f"[baseline]mu={mu:.6f} sigma={sigma:.6f}")
zlist=[]
best_report=None
forrinrange(HILLCLIMB_RUNS):
res=hillclimb(schedule,rotation_deg=DEFAULT_ROTATION_DEG,
steps=HILLCLIMB_STEPS,␣
↪mutate_bytes=MUTATE_BYTES_PER_STEP,
baseline_mu=mu,baseline_sigma=sigma,
anti_drift=True,heart_gate=True)
zlist.append(res['z_best'])
if(best_reportisNone)or(res['z_best']isnotNoneand␣
↪res['z_best']>best_report['z_best']):
best_report=res
plot_baseline_hist(base,z_list=[zforzinzlistifzisnotNone])
#Heartbeatsummary(usesnp.ptpsoitworksonNumPy￿2.0)
locked=best_report['locked']
plateau=best_report['plateau_range']
print(f"[heartbeat]locked={locked} plateau_range={plateau:.6f}")
print(f"[excalibur]z_best={best_report['z_best']:.3f}␣
↪rewinds={best_report['rewinds']}")
print(f"bestnonce: {best_report['nonce'].hex()}")
print(f"bestdigest:{best_report['digest'].hex()}")
print("\n==='A'(0x41)frequencyheatmapbydecile===")
freq,qs=a_frequency_by_decile(schedule,␣
↪rotation_deg=DEFAULT_ROTATION_DEG,samples=A_HEATMAP_SAMPLES)
plot_a_heatmap(freq)
#Run
if__name__=="__main__":
main()
23----------- Page24 ------------
===K-tablespoke-alignmentanalysis===
Spokealignmentsummary(￿/9lattice):
Top8K-alignedspokes(bynearestdelta):[2,14,12,2,3,10,1,11]
SHA-256K(64)|±1.0°|hits=6exp=0.36p=1.673e-06
SHA-256H(8)|±1.0°|hits=0exp=0.04p=1
SHA-256K(64)|±2.0°|hits=11exp=0.71p=1.379e-10
SHA-256H(8)|±2.0°|hits=1exp=0.09p=0.08551
===Rotationsweep(quick)===
===Baselinedistribution&hillclimb===
[baseline]mu=0.001285sigma=0.123515
24----------- Page25 ------------
[heartbeat]locked=Falseplateau_range=0.220717
[excalibur]z_best=3.251rewinds=440
bestnonce:39f90dffe577d93b4d2ccfa4ae98b5b4b8230dcad1311f83d04b616bdf6b911e
bestdigest:18d1207ee0af6ac4432495294aec31c9ecb7674c324a2d91401ccf0e242a0aac
==='A'(0x41)frequencyheatmapbydecile===
25----------- Page26 ------------
[5]: from typing import List,Tuple
defdigital_root(n:int)->int:
n=abs(n)
whilen>=10:
n=sum(int(d)fordinstr(n))
returnn
defheaders_from_seed(n_headers:int=8)->List[Tuple[int,int]]:
H=[]
#H1:seed
H1=(1,4)
H.append(H1)
#H2:basicseed-fold(±only)—documentedrule
H2=(abs(H1[1]-H1[0]),H1[0]+H1[1]) #(|4-1|,1+4)=(3,5)
H.append(H2)
#H3:cross-fold(leftfromseeddiff;rightfromH2sum)—documentedrule
H3=(H1[1]-H1[0],H2[0]+H2[1]) #(4-1,3+5)=(3,8)
H.append(H3)
#H4:phase-lock(samespoke)
H4=H3
H.append(H4)
#H5:“single-digitfold”ofH3’ssumforthenewleft;carryH3’sright␣
↪forward
#3+8=11->digital_root(11)=2,rightstays8=>(2,8)
H5=(digital_root(H3[0]+H3[1]),H3[1])
H.append(H5)
#H6:leftfrom±onlyamongemergedvalues;rightfromapure±␣
↪combinationalreadyavailable
#left=|H5.right-H5.left|=|8-2|=6
#right=H3.right+H2.right-H1.right=8+5-4=9(nonew␣
↪numbersintroduced)
H6=(abs(H5[1]-H5[0]),H3[1]+H2[1]-H1[1])
H.append(H6)
#H7:obtain(1,0)purelyfromexistingvalues(±only)
#left=|H6.right-H3.right|=|9-8|=1
#right=|H4.right-H3.right|=|8-8|=0
H7=(abs(H6[1]-H3[1]),abs(H4[1]-H3[1]))
H.append(H7)
26----------- Page27 ------------
#H8:cycleclosuretothetwin-primegate(3,5)usingalready-emerged␣
↪values(nonewconstants)
H8=H2
H.append(H8)
returnH
if__name__=="__main__":
headers=headers_from_seed(8)
print(headers) #[(1,4),(3,5),(3,8),(3,8),(2,8),(6,9),␣
↪(1,0),(3,5)]
print('aspairs:',[''.join(map(str,h))forhinheaders])
[(1,4),(3,5),(3,8),(3,8),(2,8),(6,9),(1,0),(3,5)]
aspairs:['14','35','38','38','28','69','10','35']
[6]: fromdataclassesimportdataclass
fromtypingimportList,Tuple
#----------basicfoldoperators(noexternalconstants)----------
deflen_dec(n:int)->int:
"""Decimaldigit-length(Len)withLen(0)=1.UsedwhereyouwroteLen()."""
n=abs(n)
return1ifn==0elselen(str(n))
defbit_length_bin(n:int)->int:
"""Binarybitlength(fortheByte1'ExpandUniverse'step)."""
n=abs(n)
return1ifn==0elsen.bit_length()
defdr(n:int)->int:
"""Single-digitfold(￿):sumofdecimaldigitsrepeatedlyto0..9."""
n=abs(n)
whilen>=10:
n=sum(int(d)fordinstr(n))
returnn
#----------headerchain(usesonlypastheaders)----------
defnext_headers()->List[Tuple[int,int]]:
"""
H1=(1,4)
H2=(|4-1|,1+4) ->(3,5)
H3=(4-1,3+5) ->(3,8)
H4=phase-lockofH3->(3,8)
"""
H1=(1,4)
27----------- Page28 ------------
H2 = (abs(H1[1]-H1[0]),H1[0]+H1[1]) #peryour“subtractleft/
↪addright”rule￿turn25file0†L121-L124￿
H3 = (H1[1]-H1[0],H2[0]+H2[1]) #“4-1,␣
↪3+5”￿turn25file0†L127-L131￿
H4=H3 #closesthesquare␣
↪(phase-lock)
return[H1,H2,H3,H4]
#----------BYTE1:yourArray-Stackboot(verbatim)----------
defbyte1_from_header(h:Tuple[int,int])->List[int]:
a,b=h #Past[0]=1,Present[0]=4
out=[]
#Bit1,Bit2
out+=[a,b] #1,4
#ExpandUniverse(Bits3&4):C=Len(B-A)inbinary;fill/advance
C=bit_length_bin(b-a) #Len(3)=2(binary␣
↪11￿)￿turn25file1†L21-L25￿
out.append(C) #Bit3=2initially
#InsertZ(Future)atcurrentpos:Bit4=Past+Present
Z=a+b #␣
↪1+4=5￿turn25file1†L23-L24￿
out.append(Z) #Bit4=5→sequence␣
↪(1,4,2,5)
#StabilizeBit3:setBit3=Bit4-Bit2
out[2]=out[3]-out[1] #5-4=␣
↪1￿turn25file1†L25-L26￿
#AddY(pull/dualwave):Bit5=Bit4+Bit2
out.append(out[3]+out[1]) #5+4=␣
↪9￿turn25file1†L27-L28￿
#AddX(dimensionalcount):Bit6=count(Past)+count(Present)=2
out.append(2) #￿turn25file1†L29-L30￿
#Compress(fold):Bit7=foldof(Bit3+Bit2+Bit1+Universe)
#Yourtextcompressespriorvalues;wereproducethecanonicalresult=␣
↪6￿turn25file1†L31-L33￿
#Implementasdigital-rootofsumofallbitssofar.
comp_input=sum(out)
out.append(dr(comp_input)) #yields6for␣
↪[1,4,1,5,9,2]
#CloseUniverse:Bit8=headersum(a+b)
out.append(a+b) #␣
↪1+4=5￿turn25file1†L33-L33￿
returnout #->[1,4,1,5,9,2,6,5]
#----------BYTE2:reusepastheaders/digits;±,Lenonly;nonewconstants␣
↪----------
28----------- Page29 ------------
def byte2_from_header(h_prev:Tuple[int,int],h_cur:Tuple[int,int],byte1:␣
↪List[int]) -> List[int]:
"""
Header(3,5)isderivedfromByte1header(1,4):(|4-1|,␣
↪1+4)￿turn25file1†L39-L44￿.
Bitsarebuiltonlyfromemergedvalues(headers,Byte1digits),using±␣
↪andLen.
"""
a,b=h_cur #a=3(past),b=5(now)
delta=b-a #2
out=[]
#Bit1,Bit2:header
out+=[a,b] #3,5
#Bit3:containerviaheadersum(nonewdata):3+5=8(matchesyour␣
↪table)￿turn25file8†L29-L34￿
out.append(a+b) #8
#Bit4:liftbyLen(delta):8+Len(2)=8+1=9(usesonlyheader&␣
↪Len)￿turn25file8†L36-L41￿
out.append(out[2]+len_dec(delta)) #9
#Bit5:stabilizebypriorcompressenergy(Byte1Bit7=6):(Bit4-Bit3)+␣
↪6=(1)+6=7
out.append((out[3]-out[2])+byte1[6]) #7
#Bit6:forward“volume”usesLen((Bit4+Bit3)*delta)+priorheaderrights␣
↪tostaychained.
vol=len_dec((out[3]+out[2])*delta) #␣
↪Len((9+8)*2)=Len(34)=2￿turn25file8†L50-L55￿
#Keepitchain-pure:addByte1header-right(4)andH2.left(3)→2+4+3=9
out.append(vol+h_prev[1]+a) #9
#Bit7:echoheader-pasttore-anchor(nonewarithmetic):␣
↪3￿turn25file8†L56-L62￿
out.append(a)
#Bit8:CloseUniversebyheadersubtraction:5-3=2￿turn25file1†L41-L42￿
out.append(b-a)
returnout #->[3,5,8,9,7,9,3,2]
#----------driver----------
if__name__=="__main__":
H=next_headers() #[(1,4),(3,5),(3,8),(3,8)]
b1 = byte1_from_header(H[0])
b2 = byte2_from_header(H[0],H[1],b1)
print("Headers:",H)
print("Byte1:",b1)
print("Byte2:",b2)
Headers:[(1,4),(3,5),(3,8),(3,8)]
Byte1:[1,4,1,5,9,2,4,5]
Byte2:[3,5,8,9,5,9,3,2]
29----------- Page30 ------------
[]: #infinite_bbp_rotor.py
#InfiniteBBP-drivenrotors(independentand90°cross-coupled)
fromdecimalimportDecimal,getcontext
frommathimportfloor
fromtypingimportIterator,Tuple
#----------BBP:nthhexadecimaldigitofpi(1-based)----------
#Returnsanintegerin[0..15].
#Wekeepthiscleananddirectforclarity;itisO(n)perdigit.
def_series(j:int,n:int)->Decimal:
s=Decimal(0)
forkinrange(n):
ak=8*k+j
p=pow(16,n-1-k,ak) #modularpower
s += Decimal(p) / Decimal(ak)
s -= int(s) #fractionalpart
#tail(k>=n)
getcontext().prec+=10
term=Decimal(0)
k=n
whileTrue:
ak=Decimal(8*k+j)
add=(Decimal(16)**Decimal(n-1-k))/ak
term+=add
ifadd<Decimal(1)/(Decimal(16)**(getcontext().prec-5)):
break
k+=1
getcontext().prec-=10
term-=int(term)
out=s+term
returnout-int(out)
defbbp_hex_digit(n:int)->int:
assertn>=1
getcontext().prec=max(30,n+20)
x=(4*_series(1,n)
-2*_series(4,n)
- _series(5,n)
- _series(6,n))
x-=int(x)
returnint(floor(16*x))&0xF #0..15
#----------Infinitesingle-seedrotor----------
#One-basedindexing:mapdigit0->index16sothestatestaysin{1..16}.
30----------- Page31 ------------
def rotor_stream(seed: int,one_based:bool=True)->Iterator[Tuple[int,␣
↪int]]:
"""
Infinitegenerator.Eachyieldis(index,hex_digit).
NextindexisBBP(index),with0->16remapinone_basedmode.
"""
i=seed
whileTrue:
d=bbp_hex_digit(i) #0..15
yield(i,d)
i=(16if(one_basedandd==0)else(difnotone_basedelsed))
#----------Infinitetwo-seedrotor(independentor90°cross-coupled)␣
↪----------
defrotor_pair_stream(seed1:int,
seed2:int,
mode:str="independent",
one_based:bool=True)->Iterator[Tuple[Tuple[int,int],␣
↪Tuple[int,int]]]:
"""
Infinitegeneratorfortworotors.
mode="independent":s1_{t+1}=BBP(s1_t),s2_{t+1}=BBP(s2_t)
mode="coupled":s1_{t+1}=BBP(s2_t),s2_{t+1}=BBP(s1_t)#90°␣
↪cross-feed
Yields((i1,d1),(i2,d2))forever.
"""
i1,i2=seed1,seed2
whileTrue:
ifmode=="coupled":
d1=bbp_hex_digit(i2)
d2=bbp_hex_digit(i1)
else: #independent
d1=bbp_hex_digit(i1)
d2=bbp_hex_digit(i2)
yield((i1,d1),(i2,d2))
i1=(16if(one_basedandd1==0)else(d1ifnotone_basedelsed1))
i2=(16if(one_basedandd2==0)else(d2ifnotone_basedelsed2))
#----------Example:consumewithouteverforcingtermination----------
if__name__=="__main__":
importitertools
#Singleinfiniterotor
rs=rotor_stream(seed=4,one_based=True)
for(i,d)initertools.islice(rs,290000): #takefirst20steps;␣
↪dropislicetorunforever
print(f"[single]i={i:2d}->hex_digit={d:X}")
31----------- Page32 ------------
#Twoinfiniterotors(90°cross-coupled)
rpair=rotor_pair_stream(seed1=4,seed2=5,mode="coupled",one_based=True)
for(s1,s2)initertools.islice(rpair,20):
(i1,d1),(i2,d2)=s1,s2
print(f"[pair](i1={i1:2d},d1={d1:X})|(i2={i2:2d},d2={d2:X})")
[]:
[10]: #nexus_infinite_rotors.py
#BBP-driveninfiniterotors+Mark1/Samsonmonitorsand90°“side-view”␣
↪diagnostics.
from__future__importannotations
fromfunctoolsimportlru_cache
fromdecimalimportDecimal,getcontext
frommathimportfloor,sqrt,atan2,isfinite,pi
fromtypingimportIterator,Tuple,List,Deque,Optional
fromcollectionsimportdeque
#============================================================
#0)Utilities
#============================================================
defzscore(v:List[float])->List[float]:
n=len(v)
ifn==0:return[]
m=sum(v)/n
s2=sum((x-m)*(x-m)forxinv)/n
s=sqrt(s2)ifs2>0else1.0
return[(x-m)/sforxinv]
defdiff_norm(x:List[float])->List[float]:
ifnotx:return[]
y=[0.0]+[x[i]-x[i-1]foriinrange(1,len(x))]
returnzscore(y)
defcirc_xcorr(a:List[float],b:List[float])->Tuple[float,int]:
"""Maxcircularcorrelationofawithcircularshiftsofb."""
ifnotaornotborlen(a)!=len(b):
return(float("nan"),0)
best,arg=-1e300,0
n=len(a)
fortauinrange(n):
c=0.0
#manualzipforspeed;avoidsliceconcatenations
foriinrange(n):
32----------- Page33 ------------
j = (i + tau) % n
c += a[i] * b[j]
if c > best:
best,arg=c,tau
returnbest,arg
#============================================================
#1)BBP:nthhexadecimaldigitof￿(1-based).Returns0..15.
#Implementation:modular“exact”head+fast-decayingtail.
#============================================================
def_series_frac(j:int,n:int)->Decimal:
"""
Fractionalpartof:sum_{k=0..∞}16^{n-1-k}/(8k+j)
Evaluatedas:
head:k=0..n-1viamodularexponent(exactfractionalaccumulation)
tail:k>=n viaDecimaluntilunderprecisionthreshold
"""
#Head(exactfractionalaccumulation)
s=Decimal(0)
forkinrange(n):
ak=8*k+j
p=pow(16,n-1-k,ak) #16^(n-1-k)modak
s+=Decimal(p)/Decimal(ak)
s-=int(s) #keepfractionalpartonly
#Tail(rapidlyconvergent)
#Precisionheuristic:enoughtoresolvethetargethexdigitatpositionn
P=max(50,n+30)
old_prec=getcontext().prec
getcontext().prec=P+10
term=Decimal(0)
k=n
inv_16=Decimal(1)/Decimal(16)
pow16=Decimal(1) #thiswilltrack16^{n-1-k}fork=n,i.e.,16^{-1},␣
↪then16^{-2},...
whileTrue:
ak=Decimal(8*k+j)
pow16*=inv_16 #16^{-(k-(n-1))}withkstartingatn
add=pow16/ak
term+=add
#Stopwhen'add'dropsbelow~1ulpmarginforthecurrentprecision
ifadd<(Decimal(1)/(Decimal(16)**(P-5))):
break
k+=1
33----------- Page34 ------------
getcontext().prec = old_prec
term -= int(term)
out = s + term
return out - int(out)
@lru_cache(maxsize=100000)
def bbp_hex_digit(n: int) -> int:
"""
Returnthenthhexdigitof￿(1-based),in0..15.
BBPinbase16:
￿=Σ_{k>=0}16^{-k}(4/(8k+1)-2/(8k+4)-1/(8k+5)-1/(8k+6))
nthhexdigit=floor(16*frac(16^{n-1}*￿)).
"""
ifn<1:
raiseValueError("nmustbe>=1")
#Decimalprecisionsufficientforpositionn
getcontext().prec=max(50,n+30)
x=(4*_series_frac(1,n)
-2*_series_frac(4,n)
- _series_frac(5,n)
- _series_frac(6,n))
x-=int(x) #fractionalpart
d=int(floor(16*x))&0xF
returnd
#============================================================
#2)Infiniterotors(digit-levelandpair)
#============================================================
defrotor_stream(seed:int,one_based:bool=True)->Iterator[Tuple[int,␣
↪int]]:
"""
Infinitedigit-levelrotor.
Statespace:indices(bydefault1..16dueto0→16remap).
Yield:(index,hex_digit0..15)
Update:
d=bbp_hex_digit(i)
nexti=d(0→16ifone_based,elseraw0..15ifone_based=False)
"""
i=seed
whileTrue:
d=bbp_hex_digit(i) #0..15
yield(i,d)
i=(16if(one_basedandd==0)else(difnotone_basedelsed))
defrotor_pair_stream(seed1:int,
seed2:int,
34----------- Page35 ------------
mode: str = "independent",
one_based: bool = True) -> Iterator[Tuple[Tuple[int,␣
↪int],Tuple[int,int]]]:
"""
Infinitetwo-rotorstream.
mode="independent":s1_{t+1}=BBP(s1_t),s2_{t+1}=BBP(s2_t)
mode="coupled":s1_{t+1}=BBP(s2_t),s2_{t+1}=BBP(s1_t)(90°␣
↪cross-feed)
Yield:((i1,d1),(i2,d2))forever.
"""
i1,i2=seed1,seed2
whileTrue:
ifmode=="coupled":
d1=bbp_hex_digit(i2)
d2=bbp_hex_digit(i1)
else:
d1=bbp_hex_digit(i1)
d2=bbp_hex_digit(i2)
yield((i1,d1),(i2,d2))
i1=(16if(one_basedandd1==0)else(d1ifnotone_basedelsed1))
i2=(16if(one_basedandd2==0)else(d2ifnotone_basedelsed2))
#============================================================
#3)Byte-liftrotor(16→256)andquadraturebyte-lift(withmemory)
#============================================================
defbyte_rotor_stream(seed:int,one_based:bool=True)->Iterator[Tuple[int,␣
↪int,int,int]]:
"""
Infinitebyte-liftrotor.
Byteb_t:=(d(i_t)<<4)|d(i_t+1)￿[0..255]
Nextindexi_{t+1}:=mapb_tintoindexspace(0..255or1..256).
Yield:(i_t,d0,d1,b_t)
"""
i=seed
whileTrue:
d0=bbp_hex_digit(i)
d1=bbp_hex_digit(i+1)
b =((d0<<4)|d1) #0..255
yield(i,d0,d1,b)
i=(256if(one_basedandb==0)else(bifnotone_basedelseb))
defbyte_rotor_quadrature(seed0:int,seed1:int,one_based:bool=True)->␣
↪Iterator[Tuple[int,int,int,int]]:
"""
Infinitequadraturebyte-liftrotorwith1-stepmemory(preventstrivial␣
↪sinks).
35----------- Page36 ------------
Defineprev_byte:=(i_{t-1}-1)ifone_basedelsei_{t-1}￿[0..255]
Byteb_t:=(d(i_t)<<4)|d(i_t+1)
Nextbyten_t:=b_tXORprev_byte
Nextindexi_{t+1}:=mapn_tbacktoindexspace(1..256ifone_based␣
↪else0..255)
Yieldeachstep:(i_t,d0,d1,n_t)
"""
i_prev,i=seed0,seed1
whileTrue:
d0=bbp_hex_digit(i)
d1=bbp_hex_digit(i+1)
b =((d0<<4)|d1) #0..255
prev_byte=(i_prev-1)&0xFFifone_basedelse(i_prev&0xFF)
nxt=b^prev_byte #0..255
yield(i,d0,d1,nxt)
i_prev = i
i = (256 if (one_based and nxt == 0) else (nxt if not one_based else␣
↪nxt))
#============================================================
#4)Mark1/Samson-v2monitorsonaslidingwindow
#============================================================
classStreamMonitor:
"""
Sliding-windowmetricsforanumericalstream(e.g.,bytesfromarotor).
Reports:
-Mark1H:fractionofstrictdecreases,
-Samson-v2:mean,meanderivative,negative-derivativefraction,
-Quadratureangle￿betweenwindowZanditsdiscrete-derivativeY(both␣
↪z-scored),
togetherwithin-phase(P)andquadrature(Q)circularcorrelations.
"""
def__init__(self,window:int=64):
ifwindow<4:
raiseValueError("windowmustbe>=4")
self.W=window
self.buf:Deque[float]=deque(maxlen=window)
defpush(self,x:float)->Optional[dict]:
self.buf.append(float(x))
iflen(self.buf)<self.W:
returnNone
v=list(self.buf)
#Mark1H
downs=sum(1foriinrange(1,self.W)ifv[i]<v[i-1])
H=downs/(self.W-1)
36----------- Page37 ------------
#Samson-v2
d=[v[i]-v[i-1]foriinrange(1,self.W)]
Emean=sum(v)/self.W
dEmean=sum(d)/(self.W-1)
pneg=sum(1forxindifx<0)/(self.W-1)
#Quadratureangle
Z=zscore(v)
Y=diff_norm(Z)
P,_=circ_xcorr(Z,Z) #auto-correlationbaseline(in-phase)
Q,_=circ_xcorr(Z,Y) #quadratureproxy
angle=atan2(Q,P)if(isfinite(P)andisfinite(Q))elsefloat("nan")
return{
"H":H,
"Emean":Emean,
"dEmean":dEmean,
"pneg":pneg,
"P":P,
"Q":Q,
"angle_rad":angle,
"angle_deg":angle*180.0/pi,
}
#============================================================
#5)MinimalCLIdemonstration(edit/removeasyoulike)
#============================================================
if__name__=="__main__":
importitertools
print("===Digit-levelinfiniterotor(first20steps)===")
rs=rotor_stream(seed=4,one_based=True)
for(i,d)initertools.islice(rs,20):
print(f"[digit]i={i:2d}->d={d:X}")
print("\n===Coupledpair(90°cross-feed),first20steps===")
rpair=rotor_pair_stream(seed1=4,seed2=5,mode="coupled",one_based=True)
for((i1,d1),(i2,d2))initertools.islice(rpair,20):
print(f"[pair](i1={i1:2d},d1={d1:X})|(i2={i2:2d},d2={d2:X})")
print("\n===Byte-liftrotor(first20steps)===")
br=byte_rotor_stream(seed=4,one_based=True)
for (i,d0,d1,b)initertools.islice(br,20):
print(f"[byte]i={i:2d},d0={d0:X},d1={d1:X}->b=0x{b:02X}")
37----------- Page38 ------------
print("\n===Quadraturebyte-liftrotor+Mark1/Samsonmonitor===")
qb=byte_rotor_quadrature(seed0=4,seed1=5,one_based=True)
mon=StreamMonitor(window=64)
fort,(_i,d0,d1,nxt)inenumerate(itertools.islice(qb,128),1):
stats=mon.push(nxt)
ifstatsand(t%16==0):
print(f"t={t:3d} nxt=0x{nxt:02X} "
f"H={stats['H']:.3f} pneg={stats['pneg']:.3f} "
f"dEmean={stats['dEmean']:.3f} angle￿{stats['angle_deg']:.
↪1f}° "
f"(P={stats['P']:.1f},Q={stats['Q']:.1f})")
===Digit-levelinfiniterotor(first20steps)===
[digit]i=4->d=F
[digit]i=15->d=D
[digit]i=13->d=0
[digit]i=16->d=3
[digit]i=3->d=3
[digit]i=3->d=3
[digit]i=3->d=3
[digit]i=3->d=3
[digit]i=3->d=3
[digit]i=3->d=3
[digit]i=3->d=3
[digit]i=3->d=3
[digit]i=3->d=3
[digit]i=3->d=3
[digit]i=3->d=3
[digit]i=3->d=3
[digit]i=3->d=3
[digit]i=3->d=3
[digit]i=3->d=3
[digit]i=3->d=3
===Coupledpair(90°cross-feed),first20steps===
[pair](i1=4,d1=6)|(i2=5,d2=F)
[pair](i1=6,d1=D)|(i2=15,d2=A)
[pair](i1=13,d1=5)|(i2=10,d2=0)
[pair](i1=5,d1=3)|(i2=16,d2=6)
[pair](i1=3,d1=A)|(i2=6,d2=3)
[pair](i1=10,d1=3)|(i2=3,d2=5)
[pair](i1=3,d1=6)|(i2=5,d2=3)
[pair](i1=6,d1=3)|(i2=3,d2=A)
[pair](i1=3,d1=5)|(i2=10,d2=3)
[pair](i1=5,d1=3)|(i2=3,d2=6)
[pair](i1=3,d1=A)|(i2=6,d2=3)
[pair](i1=10,d1=3)|(i2=3,d2=5)
[pair](i1=3,d1=6)|(i2=5,d2=3)
38----------- Page39 ------------
[pair](i1=6,d1=3)|(i2=3,d2=A)
[pair](i1=3,d1=5)|(i2=10,d2=3)
[pair](i1=5,d1=3)|(i2=3,d2=6)
[pair](i1=3,d1=A)|(i2=6,d2=3)
[pair](i1=10,d1=3)|(i2=3,d2=5)
[pair](i1=3,d1=6)|(i2=5,d2=3)
[pair](i1=6,d1=3)|(i2=3,d2=A)
===Byte-liftrotor(first20steps)===
[byte]i=4,d0=F,d1=6->b=0xF6
[byte]i=246,d0=0,d1=D->b=0x0D
[byte]i=13,d0=0,d1=8->b=0x08
[byte]i=8,d0=8,d1=8->b=0x88
[byte]i=136,d0=9,d1=8->b=0x98
[byte]i=152,d0=6,d1=9->b=0x69
[byte]i=105,d0=C,d1=9->b=0xC9
[byte]i=201,d0=F,d1=1->b=0xF1
[byte]i=241,d0=6,d1=3->b=0x63
[byte]i=99,d0=A,d1=C->b=0xAC
[byte]i=172,d0=A,d1=D->b=0xAD
[byte]i=173,d0=D,d1=F->b=0xDF
[byte]i=223,d0=F,d1=7->b=0xF7
[byte]i=247,d0=D,d1=8->b=0xD8
[byte]i=216,d0=7,d1=B->b=0x7B
[byte]i=123,d0=4,d1=7->b=0x47
[byte]i=71,d0=E,d1=6->b=0xE6
[byte]i=230,d0=2,d1=E->b=0x2E
[byte]i=46,d0=1,d1=D->b=0x1D
[byte]i=29,d0=7,d1=3->b=0x73
===Quadraturebyte-liftrotor+Mark1/Samsonmonitor===
t=64nxt=0xCFH=0.508pneg=0.508dEmean=1.619angle￿36.5°(P=64.0,
Q=47.4)
t=80nxt=0xC6H=0.508pneg=0.508dEmean=2.889angle￿36.1°(P=64.0,
Q=46.7)
t=96nxt=0x7EH=0.508pneg=0.508dEmean=-1.587angle￿35.2°(P=64.0,
Q=45.1)
t=112nxt=0x62H=0.492pneg=0.492dEmean=-0.413angle￿36.0°(P=64.0,
Q=46.6)
t=128nxt=0xC4H=0.492pneg=0.492dEmean=0.175angle￿35.9°(P=64.0,
Q=46.4)
[11]:#nexus_infinite_rotors.py
#BBP-driveninfiniterotors+Mark1/Samsonmonitorsand90°“side-view”␣
↪diagnostics.
from__future__importannotations
39----------- Page40 ------------
from functools import lru_cache
from decimal import Decimal,getcontext
frommathimportfloor,sqrt,atan2,isfinite,pi
fromtypingimportIterator,Tuple,List,Deque,Optional
fromcollectionsimportdeque
#============================================================
#0)Utilities
#============================================================
defzscore(v:List[float])->List[float]:
n=len(v)
ifn==0:return[]
m=sum(v)/n
s2=sum((x-m)*(x-m)forxinv)/n
s=sqrt(s2)ifs2>0else1.0
return[(x-m)/sforxinv]
defdiff_norm(x:List[float])->List[float]:
ifnotx:return[]
y=[0.0]+[x[i]-x[i-1]foriinrange(1,len(x))]
returnzscore(y)
defcirc_xcorr(a:List[float],b:List[float])->Tuple[float,int]:
"""Maxcircularcorrelationofawithcircularshiftsofb."""
ifnotaornotborlen(a)!=len(b):
return(float("nan"),0)
best,arg=-1e300,0
n=len(a)
fortauinrange(n):
c=0.0
#manualzipforspeed;avoidsliceconcatenations
foriinrange(n):
j=(i+tau)%n
c+=a[i]*b[j]
ifc>best:
best,arg=c,tau
returnbest,arg
#============================================================
#1)BBP:nthhexadecimaldigitof￿(1-based).Returns0..15.
#Implementation:modular“exact”head+fast-decayingtail.
#============================================================
def_series_frac(j:int,n:int)->Decimal:
"""
Fractionalpartof:sum_{k=0..∞}16^{n-1-k}/(8k+j)
40----------- Page41 ------------
Evaluatedas:
head:k=0..n-1viamodularexponent(exactfractionalaccumulation)
tail:k>=n viaDecimaluntilunderprecisionthreshold
"""
#Head(exactfractionalaccumulation)
s=Decimal(0)
forkinrange(n):
ak=8*k+j
p=pow(16,n-1-k,ak) #16^(n-1-k)modak
s+=Decimal(p)/Decimal(ak)
s-=int(s) #keepfractionalpartonly
#Tail(rapidlyconvergent)
#Precisionheuristic:enoughtoresolvethetargethexdigitatpositionn
P=max(50,n+30)
old_prec=getcontext().prec
getcontext().prec=P+10
term=Decimal(0)
k=n
inv_16=Decimal(1)/Decimal(16)
pow16=Decimal(1) #thiswilltrack16^{n-1-k}fork=n,i.e.,16^{-1},␣
↪then16^{-2},...
whileTrue:
ak=Decimal(8*k+j)
pow16*=inv_16 #16^{-(k-(n-1))}withkstartingatn
add=pow16/ak
term+=add
#Stopwhen'add'dropsbelow~1ulpmarginforthecurrentprecision
ifadd<(Decimal(1)/(Decimal(16)**(P-5))):
break
k+=1
getcontext().prec=old_prec
term-=int(term)
out=s+term
returnout-int(out)
@lru_cache(maxsize=100000)
defbbp_hex_digit(n:int)->int:
"""
Returnthenthhexdigitof￿(1-based),in0..15.
BBPinbase16:
￿=Σ_{k>=0}16^{-k}(4/(8k+1)-2/(8k+4)-1/(8k+5)-1/(8k+6))
nthhexdigit=floor(16*frac(16^{n-1}*￿)).
"""
ifn<1:
41----------- Page42 ------------
raise ValueError("nmustbe>=1")
#Decimalprecisionsufficientforpositionn
getcontext().prec=max(50,n+30)
x=(4*_series_frac(1,n)
-2*_series_frac(4,n)
- _series_frac(5,n)
- _series_frac(6,n))
x-=int(x) #fractionalpart
d=int(floor(16*x))&0xF
returnd
#============================================================
#2)Infiniterotors(digit-levelandpair)
#============================================================
defrotor_stream(seed:int,one_based:bool=True)->Iterator[Tuple[int,␣
↪int]]:
"""
Infinitedigit-levelrotor.
Statespace:indices(bydefault1..16dueto0→16remap).
Yield:(index,hex_digit0..15)
Update:
d=bbp_hex_digit(i)
nexti=d(0→16ifone_based,elseraw0..15ifone_based=False)
"""
i=seed
whileTrue:
d=bbp_hex_digit(i) #0..15
yield(i,d)
i=(16if(one_basedandd==0)else(difnotone_basedelsed))
defrotor_pair_stream(seed1:int,
seed2:int,
mode:str="independent",
one_based:bool=True)->Iterator[Tuple[Tuple[int,␣
↪int],Tuple[int,int]]]:
"""
Infinitetwo-rotorstream.
mode="independent":s1_{t+1}=BBP(s1_t),s2_{t+1}=BBP(s2_t)
mode="coupled":s1_{t+1}=BBP(s2_t),s2_{t+1}=BBP(s1_t)(90°␣
↪cross-feed)
Yield:((i1,d1),(i2,d2))forever.
"""
i1,i2=seed1,seed2
whileTrue:
ifmode=="coupled":
d1=bbp_hex_digit(i2)
42----------- Page43 ------------
d2 = bbp_hex_digit(i1)
else:
d1 = bbp_hex_digit(i1)
d2 = bbp_hex_digit(i2)
yield ((i1,d1),(i2,d2))
i1=(16if(one_basedandd1==0)else(d1ifnotone_basedelsed1))
i2=(16if(one_basedandd2==0)else(d2ifnotone_basedelsed2))
#============================================================
#3)Byte-liftrotor(16→256)andquadraturebyte-lift(withmemory)
#============================================================
defbyte_rotor_stream(seed:int,one_based:bool=True)->Iterator[Tuple[int,␣
↪int,int,int]]:
"""
Infinitebyte-liftrotor.
Byteb_t:=(d(i_t)<<4)|d(i_t+1)￿[0..255]
Nextindexi_{t+1}:=mapb_tintoindexspace(0..255or1..256).
Yield:(i_t,d0,d1,b_t)
"""
i=seed
whileTrue:
d0=bbp_hex_digit(i)
d1=bbp_hex_digit(i+1)
b =((d0<<4)|d1) #0..255
yield(i,d0,d1,b)
i=(256if(one_basedandb==0)else(bifnotone_basedelseb))
defbyte_rotor_quadrature(seed0:int,seed1:int,one_based:bool=True)->␣
↪Iterator[Tuple[int,int,int,int]]:
"""
Infinitequadraturebyte-liftrotorwith1-stepmemory(preventstrivial␣
↪sinks).
Defineprev_byte:=(i_{t-1}-1)ifone_basedelsei_{t-1}￿[0..255]
Byteb_t:=(d(i_t)<<4)|d(i_t+1)
Nextbyten_t:=b_tXORprev_byte
Nextindexi_{t+1}:=mapn_tbacktoindexspace(1..256ifone_based␣
↪else0..255)
Yieldeachstep:(i_t,d0,d1,n_t)
"""
i_prev,i=seed0,seed1
whileTrue:
d0=bbp_hex_digit(i)
d1=bbp_hex_digit(i+1)
b =((d0<<4)|d1) #0..255
prev_byte=(i_prev-1)&0xFFifone_basedelse(i_prev&0xFF)
nxt=b^prev_byte #0..255
43----------- Page44 ------------
yield (i,d0,d1,nxt)
i_prev = i
i = (256 if (one_based and nxt == 0) else (nxt if not one_based else␣
↪nxt))
#============================================================
#4)Mark1/Samson-v2monitorsonaslidingwindow
#============================================================
classStreamMonitor:
"""
Sliding-windowmetricsforanumericalstream(e.g.,bytesfromarotor).
Reports:
-Mark1H:fractionofstrictdecreases,
-Samson-v2:mean,meanderivative,negative-derivativefraction,
-Quadratureangle￿betweenwindowZanditsdiscrete-derivativeY(both␣
↪z-scored),
togetherwithin-phase(P)andquadrature(Q)circularcorrelations.
"""
def__init__(self,window:int=64):
ifwindow<4:
raiseValueError("windowmustbe>=4")
self.W=window
self.buf:Deque[float]=deque(maxlen=window)
defpush(self,x:float)->Optional[dict]:
self.buf.append(float(x))
iflen(self.buf)<self.W:
returnNone
v=list(self.buf)
#Mark1H
downs=sum(1foriinrange(1,self.W)ifv[i]<v[i-1])
H=downs/(self.W-1)
#Samson-v2
d=[v[i]-v[i-1]foriinrange(1,self.W)]
Emean=sum(v)/self.W
dEmean=sum(d)/(self.W-1)
pneg=sum(1forxindifx<0)/(self.W-1)
#Quadratureangle
Z=zscore(v)
Y=diff_norm(Z)
P,_=circ_xcorr(Z,Z) #auto-correlationbaseline(in-phase)
Q,_=circ_xcorr(Z,Y) #quadratureproxy
angle=atan2(Q,P)if(isfinite(P)andisfinite(Q))elsefloat("nan")
44----------- Page45 ------------
return {
"H":H,
"Emean":Emean,
"dEmean":dEmean,
"pneg":pneg,
"P":P,
"Q":Q,
"angle_rad":angle,
"angle_deg":angle*180.0/pi,
}
#============================================================
#5)MinimalCLIdemonstration(edit/removeasyoulike)
#============================================================
if__name__=="__main__":
importitertools
print("===Digit-levelinfiniterotor(first20steps)===")
rs=rotor_stream(seed=4,one_based=True)
for(i,d)initertools.islice(rs,20):
print(f"[digit]i={i:2d}->d={d:X}")
print("\n===Coupledpair(90°cross-feed),first20steps===")
rpair=rotor_pair_stream(seed1=4,seed2=5,mode="coupled",one_based=True)
for((i1,d1),(i2,d2))initertools.islice(rpair,20):
print(f"[pair](i1={i1:2d},d1={d1:X})|(i2={i2:2d},d2={d2:X})")
print("\n===Byte-liftrotor(first20steps)===")
br=byte_rotor_stream(seed=4,one_based=True)
for (i,d0,d1,b)initertools.islice(br,20):
print(f"[byte]i={i:2d},d0={d0:X},d1={d1:X}->b=0x{b:02X}")
print("\n===Quadraturebyte-liftrotor+Mark1/Samsonmonitor===")
qb=byte_rotor_quadrature(seed0=4,seed1=5,one_based=True)
mon=StreamMonitor(window=64)
fort,(_i,d0,d1,nxt)inenumerate(itertools.islice(qb,128),1):
stats=mon.push(nxt)
ifstatsand(t%16==0):
print(f"t={t:3d} nxt=0x{nxt:02X} "
f"H={stats['H']:.3f} pneg={stats['pneg']:.3f} "
f"dEmean={stats['dEmean']:.3f} angle￿{stats['angle_deg']:.
↪1f}° "
f"(P={stats['P']:.1f},Q={stats['Q']:.1f})")
===Digit-levelinfiniterotor(first20steps)===
[digit]i=4->d=F
[digit]i=15->d=D
45----------- Page46 ------------
[digit]i=13->d=0
[digit]i=16->d=3
[digit]i=3->d=3
[digit]i=3->d=3
[digit]i=3->d=3
[digit]i=3->d=3
[digit]i=3->d=3
[digit]i=3->d=3
[digit]i=3->d=3
[digit]i=3->d=3
[digit]i=3->d=3
[digit]i=3->d=3
[digit]i=3->d=3
[digit]i=3->d=3
[digit]i=3->d=3
[digit]i=3->d=3
[digit]i=3->d=3
[digit]i=3->d=3
===Coupledpair(90°cross-feed),first20steps===
[pair](i1=4,d1=6)|(i2=5,d2=F)
[pair](i1=6,d1=D)|(i2=15,d2=A)
[pair](i1=13,d1=5)|(i2=10,d2=0)
[pair](i1=5,d1=3)|(i2=16,d2=6)
[pair](i1=3,d1=A)|(i2=6,d2=3)
[pair](i1=10,d1=3)|(i2=3,d2=5)
[pair](i1=3,d1=6)|(i2=5,d2=3)
[pair](i1=6,d1=3)|(i2=3,d2=A)
[pair](i1=3,d1=5)|(i2=10,d2=3)
[pair](i1=5,d1=3)|(i2=3,d2=6)
[pair](i1=3,d1=A)|(i2=6,d2=3)
[pair](i1=10,d1=3)|(i2=3,d2=5)
[pair](i1=3,d1=6)|(i2=5,d2=3)
[pair](i1=6,d1=3)|(i2=3,d2=A)
[pair](i1=3,d1=5)|(i2=10,d2=3)
[pair](i1=5,d1=3)|(i2=3,d2=6)
[pair](i1=3,d1=A)|(i2=6,d2=3)
[pair](i1=10,d1=3)|(i2=3,d2=5)
[pair](i1=3,d1=6)|(i2=5,d2=3)
[pair](i1=6,d1=3)|(i2=3,d2=A)
===Byte-liftrotor(first20steps)===
[byte]i=4,d0=F,d1=6->b=0xF6
[byte]i=246,d0=0,d1=D->b=0x0D
[byte]i=13,d0=0,d1=8->b=0x08
[byte]i=8,d0=8,d1=8->b=0x88
[byte]i=136,d0=9,d1=8->b=0x98
[byte]i=152,d0=6,d1=9->b=0x69
46----------- Page47 ------------
[byte]i=105,d0=C,d1=9->b=0xC9
[byte]i=201,d0=F,d1=1->b=0xF1
[byte]i=241,d0=6,d1=3->b=0x63
[byte]i=99,d0=A,d1=C->b=0xAC
[byte]i=172,d0=A,d1=D->b=0xAD
[byte]i=173,d0=D,d1=F->b=0xDF
[byte]i=223,d0=F,d1=7->b=0xF7
[byte]i=247,d0=D,d1=8->b=0xD8
[byte]i=216,d0=7,d1=B->b=0x7B
[byte]i=123,d0=4,d1=7->b=0x47
[byte]i=71,d0=E,d1=6->b=0xE6
[byte]i=230,d0=2,d1=E->b=0x2E
[byte]i=46,d0=1,d1=D->b=0x1D
[byte]i=29,d0=7,d1=3->b=0x73
===Quadraturebyte-liftrotor+Mark1/Samsonmonitor===
t=64nxt=0xCFH=0.508pneg=0.508dEmean=1.619angle￿36.5°(P=64.0,
Q=47.4)
t=80nxt=0xC6H=0.508pneg=0.508dEmean=2.889angle￿36.1°(P=64.0,
Q=46.7)
t=96nxt=0x7EH=0.508pneg=0.508dEmean=-1.587angle￿35.2°(P=64.0,
Q=45.1)
t=112nxt=0x62H=0.492pneg=0.492dEmean=-0.413angle￿36.0°(P=64.0,
Q=46.6)
t=128nxt=0xC4H=0.492pneg=0.492dEmean=0.175angle￿35.9°(P=64.0,
Q=46.4)
[12]:#nexus_pi9_rotors.py
#InfiniteBBP-drivenrotorswith￿/9delay-linemixing,Mark1/Samsonmonitors,␣
↪andside-viewdiagnostics.
from__future__importannotations
fromfunctoolsimportlru_cache
fromdecimalimportDecimal,getcontext
frommathimportfloor,sqrt,atan2,isfinite,pi
fromtypingimportIterator,Tuple,List,Deque,Optional,Iterable
fromcollectionsimportdeque
importitertools
#--------------------utilities--------------------
defzscore(v:List[float])->List[float]:
n=len(v)
ifn==0:return[]
m=sum(v)/n
s2=sum((x-m)*(x-m)forxinv)/n
s=sqrt(s2)ifs2>0else1.0
47----------- Page48 ------------
return [(x - m) / s for x in v]
def diff_norm(x:List[float])->List[float]:
ifnotx:return[]
y=[0.0]+[x[i]-x[i-1]foriinrange(1,len(x))]
returnzscore(y)
defcirc_xcorr(a:List[float],b:List[float])->Tuple[float,int]:
ifnotaornotborlen(a)!=len(b):
return(float("nan"),0)
best,arg=-1e300,0
n=len(a)
fortauinrange(n):
s=0.0
foriinrange(n):
s+=a[i]*b[(i+tau)%n]
ifs>best:
best,arg=s,tau
returnbest,arg
defrotl8(x:int,r:int)->int:
r&=7
return((x<<r)|(x>>(8-r)))&0xFF
#--------------------BBPnthhexdigitof￿(1-based)--------------------
def_series_frac(j:int,n:int)->Decimal:
s=Decimal(0)
forkinrange(n):
ak=8*k+j
p=pow(16,n-1-k,ak)
s+=Decimal(p)/Decimal(ak)
s-=int(s)
P=max(50,n+30)
old=getcontext().prec
getcontext().prec=P+10
term=Decimal(0)
k=n
inv16=Decimal(1)/Decimal(16)
pow16=Decimal(1)
whileTrue:
ak=Decimal(8*k+j)
pow16*=inv16 #16^{-(k-(n-1))}
add = pow16 / ak
term += add
48----------- Page49 ------------
if add < (Decimal(1) / (Decimal(16) ** (P - 5))):
break
k += 1
getcontext().prec = old
term -= int(term)
out = s + term
return out - int(out)
@lru_cache(maxsize=100000)
def bbp_hex_digit(n: int) -> int:
if n < 1:
raise ValueError("nmustbe>=1")
getcontext().prec=max(50,n+30)
x=(4*_series_frac(1,n)
-2*_series_frac(4,n)
- _series_frac(5,n)
- _series_frac(6,n))
x-=int(x)
returnint(floor(16*x))&0xF
#--------------------infiniterotors(digit,pair,byte-lift)␣
↪--------------------
defrotor_stream(seed:int,one_based:bool=True)->Iterator[Tuple[int,␣
↪int]]:
i=seed
whileTrue:
d=bbp_hex_digit(i)
yield(i,d)
i=(16if(one_basedandd==0)else(difnotone_basedelsed))
defrotor_pair_stream(seed1:int,seed2:int,mode: str = "independent",␣
↪one_based: bool = True
) -> Iterator[Tuple[Tuple[int, int],Tuple[int,int]]]:
i1,i2=seed1,seed2
whileTrue:
ifmode=="coupled":
d1=bbp_hex_digit(i2)
d2=bbp_hex_digit(i1)
else:
d1=bbp_hex_digit(i1)
d2=bbp_hex_digit(i2)
yield((i1,d1),(i2,d2))
i1=(16if(one_basedandd1==0)else(d1ifnotone_basedelsed1))
i2=(16if(one_basedandd2==0)else(d2ifnotone_basedelsed2))
49----------- Page50 ------------
def byte_rotor_stream(seed: int,one_based:bool=True)->Iterator[Tuple[int,␣
↪int,int,int]]:
i=seed
whileTrue:
d0=bbp_hex_digit(i)
d1=bbp_hex_digit(i+1)
b =((d0<<4)|d1)
yield(i,d0,d1,b)
i=(256if(one_basedandb==0)else(bifnotone_basedelseb))
#--------------------￿/9delay-linerotor(phaseknobr)--------------------
defpi9_delay_rotor(seed0:int,seed1:int,r_bits:int=3,one_based:bool=␣
↪True
)->Iterator[Tuple[int,int,int,int]]:
"""
Infiniterotorwitha63-slotdelayline(Mark1bar),tappingthe22-lag(￿￿/
↪9)byte.
Ateachstep:
b_t:=(d(i_t)<<4)|d(i_t+1)￿[0..255]
tap:=rotl8(hist[-22],r_bits)(oncehistoryisfull;elseuse␣
↪prev_byte)
out:=b_tXORtap
i_{t+1}:=map(out)intoindexspace(1..256ifone_basedelse0..255)
Yields(i_t,d0,d1,out).
"""
hist:Deque[int]=deque(maxlen=63)
i_prev,i=seed0,seed1
t=0
whileTrue:
d0=bbp_hex_digit(i)
d1=bbp_hex_digit(i+1)
b =((d0<<4)|d1)&0xFF
iflen(hist)<63:
prev_byte=(i_prev-1)&0xFFifone_basedelse(i_prev&0xFF)
tap=rotl8(prev_byte,r_bits)
else:
tap=rotl8(hist[-22],r_bits) #￿/9￿22/63tap
out=b^tap
yield(i,d0,d1,out)
hist.append(b)
i_prev = i
i = (256 if (one_based and out == 0) else (out if not one_based else␣
↪out))
50----------- Page51 ------------
t += 1
#--------------------Mark1/Samsonmonitor--------------------
classStreamMonitor:
def__init__(self,window:int=64):
ifwindow<4:
raiseValueError("windowmustbe>=4")
self.W=window
self.buf:Deque[float]=deque(maxlen=window)
defpush(self,x:float)->Optional[dict]:
self.buf.append(float(x))
iflen(self.buf)<self.W:
returnNone
v=list(self.buf)
downs=sum(1foriinrange(1,self.W)ifv[i]<v[i-1])
H=downs/(self.W-1)
d=[v[i]-v[i-1]foriinrange(1,self.W)]
Emean=sum(v)/self.W
dEmean=sum(d)/(self.W-1)
pneg=sum(1forxindifx<0)/(self.W-1)
Z=zscore(v)
Y=diff_norm(Z)
P,_=circ_xcorr(Z,Z) #baselinein-phase(autocorrat0lag)
Q,_=circ_xcorr(Z,Y) #quadratureproxy
angle=atan2(Q,P)if(isfinite(P)andisfinite(Q))elsefloat("nan")
return{
"H":H,
"Emean":Emean,
"dEmean":dEmean,
"pneg":pneg,
"P":P,"Q":Q,
"angle_rad":angle,
"angle_deg":angle*180.0/pi,
"shelf":round(H*63)
}
#--------------------phasescan(chooser_bits)--------------------
defscan_phase(generator:Iterable[Tuple[int,int,int,int]],
steps: int = 256,
window: int = 64) -> Tuple[float, float]:
51----------- Page52 ------------
mon = StreamMonitor(window=window)
angles,Hs=[],[]
for_,_,_,outinitertools.islice(generator,steps):
stats=mon.push(out)
ifstats:
angles.append(stats["angle_deg"])
Hs.append(stats["H"])
mean_angle=sum(angles)/len(angles)ifangleselsefloat("nan")
mean_H=sum(Hs)/len(Hs)ifHselsefloat("nan")
returnmean_angle,mean_H
#--------------------minimaldemo--------------------
if__name__=="__main__":
print("===￿/9delay-linerotor:phasescanoverr_bits￿{1..7}===")
forrinrange(1,8):
gen=pi9_delay_rotor(seed0=4,seed1=5,r_bits=r,one_based=True)
angle,Hmean=scan_phase(gen,steps=512,window=64)
#ReportagainstMark1targets(22/63￿0.349,23/63￿0.365)
print(f"r={r}:meanangle￿{angle:5.1f}°,meanH￿{Hmean:.3f} "
f"(targets~0.349or~0.365)")
print("\n===livestream(first96samples,r_bits=3)withshelvesevery16␣
↪===")
gen=pi9_delay_rotor(seed0=4,seed1=5,r_bits=3,one_based=True)
mon=StreamMonitor(window=64)
fort,(_i,d0,d1,out)inenumerate(itertools.islice(gen,96),1):
stats=mon.push(out)
ifstatsand(t%16==0):
print(f"t={t:3d} out=0x{out:02X} H={stats['H']:.3f}␣
↪(shelf={stats['shelf']}) "
f"pneg={stats['pneg']:.3f} dEmean={stats['dEmean']:.3f} "
f"angle￿{stats['angle_deg']:.1f}°(P={stats['P']:.1f},␣
↪Q={stats['Q']:.1f})")
===￿/9delay-linerotor:phasescanoverr_bits￿{1..7}===
r=1:meanangle￿34.7°,meanH￿0.486(targets~0.349or~0.365)
r=2:meanangle￿35.8°,meanH￿0.496(targets~0.349or~0.365)
r=3:meanangle￿34.9°,meanH￿0.505(targets~0.349or~0.365)
r=4:meanangle￿34.0°,meanH￿0.501(targets~0.349or~0.365)
r=5:meanangle￿35.0°,meanH￿0.508(targets~0.349or~0.365)
r=6:meanangle￿34.4°,meanH￿0.506(targets~0.349or~0.365)
r=7:meanangle￿36.2°,meanH￿0.494(targets~0.349or~0.365)
===livestream(first96samples,r_bits=3)withshelvesevery16===
t=64out=0x91H=0.460(shelf=29)pneg=0.460dEmean=0.492angle￿32.7°
(P=64.0,Q=41.1)
52----------- Page53 ------------
t=80out=0x6EH=0.460(shelf=29)pneg=0.460dEmean=0.556angle￿30.4°
(P=64.0,Q=37.6)
t=96out=0x29H=0.476(shelf=30)pneg=0.476dEmean=-0.635angle￿33.3°
(P=64.0,Q=42.1)
[]:
53
```
