---
title: "The Nexus 4 Framework - Untitled1"
source_pdf: "The Nexus 4 Framework - Untitled1.pdf"
created_utc: "2025-11-27T11:10:16.3218024Z"
page_count: 14
---

# The Nexus 4 Framework - Untitled1

## Extracted Text

```text
----------- Page1 ------------
Untitled1
September16,2025
[6]: from decimal import Decimal,getcontext
getcontext().prec=32 #100digitsplussafety
defbbp_pi(n_terms):
x=Decimal(0)
forkinrange(n_terms):
x+=(Decimal(1)/(16**k))*(
Decimal(4)/(8*k+1)
-Decimal(2)/(8*k+4)
-Decimal(1)/(8*k+5)
-Decimal(1)/(8*k+6))
print(x)
#convertxtoarray,computedifferenceandplot
returnx
x=bbp_pi(32)
3.1333333333333333333333333333333
3.1414224664224664224664224664224
3.1415873903465815230521112874053
3.1415924575674353818370045550572
3.1415926454603363195570212224423
3.1415926532280875347343780355361
3.1415926535728808277852407618958
3.1415926535889727049407777671701
3.1415926535897522752361778683980
3.1415926535897911463887769659102
3.1415926535897931296141705640412
3.1415926535897932327112922619299
3.1415926535897932381547663225017
3.1415926535897932384459775019401
3.1415926535897932384617324820378
3.1415926535897932384625931746705
3.1415926535897932384626405951379
3.1415926535897932384626432274246
3.1415926535897932384626433745155
3.1415926535897932384626433827838
1----------- Page2 ------------
3.1415926535897932384626433832511
3.1415926535897932384626433832776
3.1415926535897932384626433832791
3.1415926535897932384626433832792
3.1415926535897932384626433832792
3.1415926535897932384626433832792
3.1415926535897932384626433832792
3.1415926535897932384626433832792
3.1415926535897932384626433832792
3.1415926535897932384626433832792
3.1415926535897932384626433832792
3.1415926535897932384626433832792
[1]: from decimal import Decimal,getcontext
importmatplotlib.pyplotasplt
importnumpyasnp
getcontext().prec=64 #enoughprecisionfordigits
defbbp_pi(n_terms,digits_per_row=32):
prev_digits = None
x = Decimal(0)
for k in range(n_terms):
x += (Decimal(1) / (16**k)) * (
Decimal(4)/(8*k+1)
- Decimal(2)/(8*k+4)
- Decimal(1)/(8*k+5)
- Decimal(1)/(8*k+6))
#convertcurrentsumtostringofdigits
s=str(x).replace('.','') #stripdecimal
digits=np.array([int(ch)forchins[:digits_per_row]])
ifprev_digitsisnotNone:
#computedifferencefrompreviousrow
diff=digits-prev_digits
#plotforthisiteration
plt.figure(figsize=(10,2))
plt.bar(range(len(diff)),diff,color="seagreen")
plt.title(f"Digitdifferencesatiteration{k}")
plt.xlabel("Digitindex")
plt.ylabel("Δdigit")
plt.ylim(-9,9)
plt.show()
2----------- Page3 ------------
prev_digits = digits
return x
#runit
x=bbp_pi(32,digits_per_row=32)
3----------- Page4 ------------
4----------- Page5 ------------
5----------- Page6 ------------
6----------- Page7 ------------
7----------- Page8 ------------
8----------- Page9 ------------
9----------- Page10 ------------
10----------- Page11 ------------
[2]: from decimal import Decimal,getcontext
importmatplotlib.pyplotasplt
importnumpyasnp
getcontext().prec=64 #increaseprecisiontoholdenoughdigits
defbbp_pi(n_terms,digits_per_row=64):
rows = []
x = Decimal(0)
for k in range(n_terms):
x += (Decimal(1) / (16**k)) * (
Decimal(4)/(8*k+1)
- Decimal(2)/(8*k+4)
- Decimal(1)/(8*k+5)
- Decimal(1)/(8*k+6))
#convertcurrentsumtostringofdigits
s=str(x).replace('.','') #removedecimalpoint
digits=[int(ch)forchins[:digits_per_row]] #takefirstNdigits
rows.append(digits)
rows=np.array(rows)
#computedifferencesbetweenconsecutiverows
diffs=np.diff(rows,axis=0)
#plot
plt.figure(figsize=(12,6))
plt.imshow(diffs,cmap="seismic",aspect="auto",vmin=-9,vmax=9)
plt.colorbar(label="Digitdifference")
plt.title(f"Row-to-RowDigitDifferencesinBBPPartialSums(first␣
↪{n_terms}terms)")
plt.xlabel("Digitindexwithinrow")
plt.ylabel("Rowindex")
plt.show()
returnx
#runit
x=bbp_pi(32,digits_per_row=64)
11----------- Page12 ------------
[3]: def pi_bbp_partial(N):
pi_sum = 0.0
for k in range(N):
pi_sum += (4/(8*k+1) - 2/(8*k+4) - 1/(8*k+5) - 1/(8*k+6)) / (16**k)
return pi_sum
#Testthepartialsumconvergence
forNin[1,2,3,5,10]:
print(N,pi_bbp_partial(N))
defgoertzel(x,k0,N):
"""ComputeGoertzeloutputforfrequencybink0onsignalx."""
omega0=2*np.pi*k0/N
coeff=2*np.cos(omega0)
s_prev=0.0
s_prev2=0.0
#ApplyGoertzelrecurrence
forsampleinx:
s=sample+coeff*s_prev-s_prev2
s_prev2=s_prev
s_prev=s
#Aftertheloop,s_prevholdss[N],ands_prev2holdss[N-1].
#TherealDFTresultatk0isgivenby:
12----------- Page13 ------------
X_k0 = s_prev - np.exp(-1j*omega0) * s_prev2
return X_k0
13.1333333333333333
23.1414224664224664
33.1415873903465816
53.1415926454603365
103.1415926535897913
[4]: importnumpyasnp
importmath
N=50
k0=5
#On-targetsignal:5cyclesover50samples
signal_on=[math.cos(2*math.pi*k0*n/N)forninrange(N)]
#Off-targetsignal:6cyclesover50samples(close,butnotk0)
signal_off=[math.cos(2*math.pi*6*n/N)forninrange(N)]
X_on=goertzel(signal_on,k0,N)
X_off=goertzel(signal_off,k0,N)
print("Goertzelmagnitude(on-target):",abs(X_on))
print("Goertzelmagnitude(off-target):",abs(X_off))
Goertzelmagnitude(on-target):25.0
Goertzelmagnitude(off-target):6.2059882649897314e-15
[5]: importnumpyasnp
importmatplotlib.pyplotasplt
#BBP-basedindexing:simulateaccessingadigitofpi
#RealBBPrequireshigh-precisionarithmetic;wesimulateharmonicmapping
#Generatedigitsofpi(uptoafewplaces)usingasimplifiedapproximation
#SincefullBBPdigitaccessiscomputationallyintensive,we'llsimulate␣
↪harmonicpositions
#Createaphasespaceusingreal-valuedpositionsmappedtosine-based␣
↪harmonicvalues
n_points=256 #Numberofpositionsinthesimulatedlattice
x=np.linspace(0,4*np.pi,n_points) #Phasedomain(simulated)
harmonic_memory=np.sin(x)*0.35 #ApplyH=0.35asharmonicamplitude
#BBP-likeindexing:simulateglide-basedaccessintothisharmonicfield
#Herewe"jump"tospecificphase-alignedindicesasifthey'rememoryreads
access_indices=[int(i*3.1415)%n_pointsforiinrange(1,10)] #␣
↪SimulatedBBP-likejumps
accessed_values=harmonic_memory[access_indices]
13----------- Page14 ------------
#Plotting
plt.figure(figsize=(12,4))
plt.plot(x,harmonic_memory,label="HarmonicMemoryField",alpha=0.7)
plt.scatter(np.array(x)[access_indices],accessed_values,color='red',␣
↪label="BBPPhaseAccess",zorder=5)
plt.axhline(0,color='gray',linewidth=0.5)
plt.title("SimulatedHarmonicMemorywithBBP-likePhaseAccess(H=0.35)")
plt.xlabel("PhaseSpace(radians)")
plt.ylabel("Amplitude")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
[]:
14
```
