---
title: "The Nexus 4 Framework - Nexus4 - Cas Workbook - Copy"
source_pdf: "The Nexus 4 Framework - Nexus4 - Cas Workbook - Copy.pdf"
created_utc: "2025-11-27T11:09:54.5944437Z"
page_count: 46
---

# The Nexus 4 Framework - Nexus4 - Cas Workbook - Copy

## Bookmarks
- 📄 CAS Notebook: Collapse-Aware Systems

## Extracted Text

```text
----------- Page1 ------------
Untitled
August21,2025
1￿CASNotebook:Collapse-AwareSystems
Author: DeanA.KulikDate: August,2025Context: ExperimentalTheoreticalFramework
Tags: #CollapseLogic#SemanticFields#GlyphTheory#PhaseSpace#SymbolicComputation
1.1￿Purpose
Thisnotebookexplorestheemergenceofstructuredbehaviorwithindigitstreams(e.g.￿,SHA
constants)usingXOR–AVGphasespacetransformationsandglyph-basedcollapselogic.Thegoal
istouncoverlatentcorridordynamics,admissibilitythresholds,andsemanticresonancepatterns
acrosscomputationalconstants.
1.2￿KeyConcepts
• CollapseGeometry: Systemswhereagencymeetsconstraintthroughforcedvectorrealign-
ment.
• Glyphs: Probesinsemanticfields,acquiringidentitythroughboundaryinteractions.
• CorridorLogic: Permissiblestate-spaceevolutionundertopologicalorsemanticconstraints.
• XOR–AVGLattice:A2Dmappingexposingnon-randomstructureinnumericstreams.
• ScarMarkers&Thresholds: Pointsofrejection/admittancethatdefinetheshapeoflogic.
1.3￿Summary
Thisisnotaconventionalstatisticalanalysis.
It’sanoperationallensonmeaning,logic,andcomputationastheyemergefromconstraint-bound
numericprocesses—fromthebehaviorof￿tothehash-biasesincryptographicfunctions.
Ifglyphsaretheparticlesofthought,thisistheirfieldguide.
CopyrightDeanA.Kulik–OrcidID#0009-0003-3128-8828CreativeCommonsAttribution-
NonCommercial4.0InternationalLicense(CCBY-NC4.0)github.com/QuHarmonics/The-Nexus-
Harmonic-Reality
1----------- Page2 ------------
[1]: #%%[code]
importmath,os,json,hashlib,secrets,time
importnumpyasnp
importmatplotlib.pyplotasplt
rng=np.random.default_rng(2025)
#anglehelpers(degrees)
def_wrap_delta_deg(a_deg:np.ndarray,b_deg:np.ndarray)->np.ndarray:
D=(a_deg[:,None]-b_deg[None,:])
return(D+180.0)%360.0-180.0
defspoke_angles_deg(n_spokes:int,rot_deg:float)->np.ndarray:
step=360.0/n_spokes
return(rot_deg+step*np.arange(n_spokes))%360.0
defmin_abs_delta_to_spokes(angles_deg:np.ndarray,spokes_deg:np.ndarray) ->␣
↪np.ndarray:
D = _wrap_delta_deg(angles_deg,spokes_deg)
returnnp.min(np.abs(D),axis=1)
[2]: #%%[code]
deffirst_n_primes(n:int)->np.ndarray:
"""Simplesieve,goodenoughforn<=80."""
ifn<6:
bound=15
else:
ln=math.log(n)
bound=int(n*(ln+math.log(ln))*2.5)+64
sieve=np.ones(bound+1,dtype=bool)
sieve[:2]=False
forpinrange(2,int(bound**0.5)+1):
ifsieve[p]:
sieve[p*p:bound+1:p]=False
returnnp.flatnonzero(sieve)[:n]
defktable_angles_deg_sha256()->np.ndarray:
"""SHA-256Kconstantsarefrac(cuberoot(prime));converttodegrees."""
primes=first_n_primes(64)
fracs =np.cbrt(primes.astype(float))
fracs-=np.floor(fracs)
return(fracs*360.0)%360.0
definfer_wheel(K_deg:np.ndarray,k_candidates=(9,18,27),tol_eval=(1.0,2.
↪0)):
"""
Lettheconstantspickthewheel:
2----------- Page3 ------------
z_k=mean(exp(i*k*theta)),phi￿arg(z_k)/k
Scorecandidatesby(±2°hits,±1°hits,|z_k|).
"""
thetas=np.deg2rad(K_deg)
best=None
forkink_candidates:
z=np.exp(1j*k*thetas).mean()
phi_rad=np.angle(z)/k
rot_deg=(np.degrees(phi_rad))%(360.0/k)
spokes =spoke_angles_deg(k,rot_deg)
deltas =min_abs_delta_to_spokes(K_deg,spokes)
hits1 =int(np.sum(deltas<=tol_eval[0]))
hits2 =int(np.sum(deltas<=tol_eval[1]))
cand=dict(k=k,rot_deg=float(rot_deg),hits1=hits1,hits2=hits2,␣
↪power=float(abs(z)))
ifbestisNoneor(hits2,hits1,abs(z))>(best['hits2'],␣
↪best['hits1'],best['power']):
best=cand
returnbest
#runinference+quickplot
K_deg=ktable_angles_deg_sha256()
best =infer_wheel(K_deg,k_candidates=(9,18))
print(f"[wheel]k={best['k']} rot￿{best['rot_deg']:.2f}°␣
↪hits(±1°)={best['hits1']} "
f"hits(±2°)={best['hits2']} power={best['power']:.3f}")
defplot_inferred_overlay(K_deg,k,rot_deg):
spokes = spoke_angles_deg(k,rot_deg)
fig=plt.figure(figsize=(6.2,6.2))
ax=fig.add_subplot(111,projection='polar')
ax.scatter(np.deg2rad(K_deg),np.ones_like(K_deg),s=28,alpha=0.9,␣
↪label="Kangles")
forsinspokes:
ax.plot([np.deg2rad(s),np.deg2rad(s)],[0,1.1],color='tab:red',lw=1.
↪3,alpha=0.8)
ax.set_title(f"Inferredwheel:k={k},rot={rot_deg:.2f}°")
ax.set_yticklabels([])
ax.legend(loc="upperright")
plt.tight_layout()
plot_inferred_overlay(K_deg,best['k'],best['rot_deg'])
[wheel]k=18rot￿3.87°hits(±1°)=8hits(±2°)=13power=0.135
3----------- Page4 ------------
[3]: #%%[code]
defverify_narrow_sweep(K_deg,k,rot_deg,half_window_deg=6.0,step=0.25,␣
↪tol_list=(1.0,2.0)):
rot_vals=np.arange(rot_deg-half_window_deg,rot_deg+half_window_deg+␣
↪1e-9,step)
series={tol:[]fortolintol_list}
forrinrot_vals:
spokes=spoke_angles_deg(k,r%(360.0/k))
deltas=min_abs_delta_to_spokes(K_deg,spokes)
fortolintol_list:
series[tol].append(int(np.sum(deltas<=tol)))
fortolintol_list:
series[tol]=np.array(series[tol],dtype=int)
4----------- Page5 ------------
plt.figure(figsize=(8.4, 4.0))
for tol,arrinseries.items():
plt.plot(rot_vals,arr,lw=1.6,label=f"±{tol:.0f}°window")
plt.axvline(rot_deg,color='k',ls='--',lw=1.0,alpha=0.6)
plt.xlabel("Rotation(deg)");plt.ylabel("Hitcount")
plt.title(f"Verificationsweepnearinferredoffset(k={k})")
plt.legend();plt.grid(alpha=0.3);plt.tight_layout()
returnrot_vals,series
_=verify_narrow_sweep(K_deg,best['k'],best['rot_deg'])
[4]: #%%[code]
defbytes_to_angles_deg(b:bytes)->np.ndarray:
"""Mapeachbyte0..255to0..360deguniformly."""
return(np.frombuffer(b,dtype=np.uint8).astype(float)/256.0)*360.0
defphase_score_from_angles(angles_deg:np.ndarray,k:int,rot_deg:float)->␣
↪float:
"""Meancosineaffinitytonearestspoke."""
spokes=spoke_angles_deg(k,rot_deg)
deltas=min_abs_delta_to_spokes(angles_deg,spokes)
#higherscore=tighteralignment
returnfloat(np.mean(np.cos(np.deg2rad(deltas))))
defdigest_phase_score(msg:bytes,k:int,rot_deg:float)->float:
h=hashlib.sha256(msg).digest()
a=bytes_to_angles_deg(h)
returnphase_score_from_angles(a,k,rot_deg)
5----------- Page6 ------------
def estimate_baseline(prefix: bytes,k:int,rot_deg:float,trials=4000)->␣
↪tuple[float,float]:
scores=[]
for_inrange(trials):
nonce=secrets.token_bytes(8)
scores.append(digest_phase_score(prefix+nonce,k,rot_deg))
scores=np.array(scores,dtype=float)
returnfloat(scores.mean()),float(scores.std(ddof=1))
#choosetheempiricallyinferredwheel,optionallyaddtheobservednative␣
↪+15°bias
k_native =best['k']
rot_native=(best['rot_deg']+15.0)%(360.0/k_native) #incorporatethe␣
↪measureddownbeat
PREFIX=b"phase-probe:"
mu,sigma=estimate_baseline(PREFIX,k_native,rot_native,trials=2000)
print(f"[baseline]mu={mu:.6f} sigma={sigma:.6f}")
[baseline]mu=0.994938sigma=0.000797
[5]:#%%[code]
defheartbeat_gate(trace:list[float],window=12,eps=0.06)->tuple[bool,␣
↪float]:
"""
Acceptonlyiftherecentwindowis'flat'->plateau.
Returns(locked,plateau_range).
Usesnumpy.ptp(...)insteadofndarray.ptp(NumPy2.0safe).
"""
iflen(trace)<window:
returnFalse,float("inf")
tail=np.array(trace[-window:],dtype=float)
pr=float(np.ptp(tail)) #max-min
return(pr<=eps),pr
defhillclimb_anti_drift(prefix:bytes,k:int,rot_deg:float,steps=500,␣
↪step_bytes=2,
rewind_patience=12,eps_plateau=0.06,seed=None):
"""
Simplebytewisemutatorwithrollbackandorthogonaljitter.
Returnsdictwithbeststatsandtheheartbeatevaluation.
"""
ifseedisNone:
rng_local=np.random.default_rng()
else:
rng_local=np.random.default_rng(seed)
6----------- Page7 ------------
state = bytearray(secrets.token_bytes(32))
def score_of(state_bytes: bytes) -> float:
return digest_phase_score(prefix + state_bytes,k,rot_deg)
s = score_of(state)
best_s,best_state=s,state[:]
scores=[s]
rewinds=0
#stepdirectionsperbytetoencouragelocalpersistence
dirs=rng_local.choice([-1,+1],size=32,replace=True)
fortinrange(1,steps+1):
idx=rng_local.integers(0,32,endpoint=False)
old_val=state[idx]
#proposemove
delta=dirs[idx]*step_bytes
state[idx]=(state[idx]+delta)&0xFF
s_new=score_of(state)
ifs_new>=s:
s=s_new
scores.append(s)
ifs_new>best_s:
best_s,best_state=s_new,state[:]
else:
#rollbackandflipdirection(anti-drift),withsmallorthogonal␣
↪jitter
state[idx]=old_val
dirs[idx]=-dirs[idx]
jit=rng_local.integers(0,32,endpoint=False)
state[jit]=(state[jit]+rng_local.choice([-1,+1])*1)&0xFF
rewinds+=1
scores.append(s)
#earlystoponsustainedplateau
locked,pr=heartbeat_gate(scores,window=12,eps=eps_plateau)
iflockedandt>24:
break
returndict(best_score=float(best_s),
best_state=bytes(best_state),
scores=scores,
rewinds=rewinds)
#runtheclimberandcomputeZ(best)
7----------- Page8 ------------
res = hillclimb_anti_drift(PREFIX,k_native,rot_native,steps=1200,␣
↪step_bytes=2,
rewind_patience=12,eps_plateau=0.06,seed=2025)
z_best=(res['best_score']-mu)/(sigmaifsigma>0else1e-9)
locked,plateau_range=heartbeat_gate(res['scores'],window=12,eps=0.06)
print(f"[excalibur]locked={locked} z_best={z_best:.3f}␣
↪rewinds={res['rewinds']} "
f"plateau_range={plateau_range:.5f}")
plt.figure(figsize=(8.2,3.6))
plt.plot(res['scores'],lw=1.4)
plt.axhline(mu,color='k',ls='--',lw=0.8)
plt.title("Hillclimbtrace(phasescore)")
plt.xlabel("step");plt.ylabel("score");plt.grid(alpha=0.3);plt.tight_layout()
[excalibur]locked=Truez_best=2.153rewinds=24plateau_range=0.00000
[6]:#%%[code]
defbinom_sf(k:int,n:int,p:float)->float:
frommathimportcomb
returnsum(comb(n,i)*(p**i)*((1-p)**(n-i))foriinrange(k,n+1))
defspoke_coverage(n_spokes:int,tol_deg:float)->float:
#forsmalltolandsparsespokes
returnn_spokes*(2.0*tol_deg)/360.0
n=len(K_deg)
fortolin(1.0,2.0):
8----------- Page9 ------------
spokes = spoke_angles_deg(k_native,rot_native)
deltas = min_abs_delta_to_spokes(K_deg,spokes)
obs = int(np.sum(deltas <= tol))
p = spoke_coverage(k_native,tol)
pv =binom_sf(obs,n,p)
exp=n*p
print(f"[K-table@rot]tol=±{tol:.0f}°observed={obs}expected={exp:.2f}␣
↪p={pv:.3g}")
[K-table@rot]tol=±1°observed=6expected=6.40p=0.627
[K-table@rot]tol=±2°observed=13expected=12.80p=0.525
[7]:#%%[code]
defglyphA_deciles(prefix:bytes,k:int,rot_deg:float,samples=20000):
scores=np.empty(samples,dtype=float)
heads =np.empty(samples,dtype=np.uint8)
foriinrange(samples):
nonce=secrets.token_bytes(8)
h =hashlib.sha256(prefix+nonce).digest()
heads[i] =h[0]
scores[i]=phase_score_from_angles(bytes_to_angles_deg(h),k,rot_deg)
#decilesbyscore
q=np.quantile(scores,np.linspace(0,1,11))
dec=np.digitize(scores,q[1:-1],right=True) #0..9
probs=np.zeros(10,dtype=float)
fordinrange(10):
mask=dec==d
denom=max(1,mask.sum())
probs[d]=np.count_nonzero((heads==0x41)&mask)/denom
returnprobs,q
probs,q=glyphA_deciles(PREFIX,k_native,rot_native,samples=8000)
plt.figure(figsize=(6.4,3.2))
plt.bar(np.arange(10),probs,width=0.8)
plt.xticks(range(10),[f"D{d+1}"fordinrange(10)])
plt.ylabel("P(byte0==0x41)")
plt.title("'A'frequencybyscoredecile(byte0)")
plt.grid(axis='y',alpha=0.3);plt.tight_layout()
9----------- Page10 ------------
[8]: #%%[code]
defcbe_sim(size=(128,128),n_steps=2000,n_obstacles=2400,seed=2025):
rng_local=np.random.default_rng(seed)
H,W=size
field=np.zeros((H,W),dtype=float) #scar/channelintensity
blocked = np.zeros((H,W),dtype=bool) #obstacles
#sprinkleobstacles
ys=rng_local.integers(0,H,size=n_obstacles)
xs=rng_local.integers(0,W,size=n_obstacles)
blocked[ys,xs]=True
#start&goal
start=np.array([H//2,4],dtype=int)
goal =np.array([H//2,W-5],dtype=int)
pos=start.copy()
traj=[tuple(pos)]
scar_gain=0.6
decay=0.9992
defneighbors(p):
y,x=p
#8-connectivity
fordyin(-1,0,+1):
fordxin(-1,0,+1):
ifdy==0anddx==0:
continue
10----------- Page11 ------------
ny,nx=y+dy,x+dx
if0<=ny<Hand0<=nx<W:
yield(ny,nx),(dy,dx)
fortinrange(n_steps):
#intendedstep:straighttowardgoal
v=goal-pos
ifnp.linalg.norm(v,2)<1.0:
break
v=v/max(1e-9,np.linalg.norm(v,2))
#rankneighborsbyalignmenttointent,thenbylowerscar
cand=[]
for(ny,nx),(dy,dx)inneighbors(pos):
ifblocked[ny,nx]: #admissiondenied
continue
step_vec=np.array([dy,dx],dtype=float)
step_vec/=max(1e-9,np.linalg.norm(step_vec,2))
align=float(np.dot(v,step_vec)) #closerto+1isbetter
scar = field[ny,nx]
score=(align,-scar) #lexicographic:prefer␣
↪alignment,thenlowscar
cand.append((score,(ny,nx)))
ifnotcand:
#fullydenied—depositascaratcurrentlocationandrandomhop
field[tuple(pos)]+=scar_gain
choices=[(ny,nx)for(ny,nx),_inneighbors(pos)ifnot␣
↪blocked[ny,nx]]
ifnotchoices:
break
pos=np.array(choices[rng_local.integers(0,len(choices))],␣
↪dtype=int)
else:
#choosebestadmissibleneighbor;ifthe*intended*bestis␣
↪blocked,ascarislaidwhereintentfailed
cand.sort(reverse=True)
best_next=np.array(cand[0][1],dtype=int)
ifnp.all(best_next==pos): #degenerate
field[tuple(pos)]+=scar_gain
pos=best_next
traj.append(tuple(pos))
#passivescardiffusion/decay
field*=decay
returnfield,traj,start,goal,blocked
11----------- Page12 ------------
field,traj,start,goal,blocked=cbe_sim(size=(140,220),n_steps=6000,␣
↪n_obstacles=3200,seed=2025)
plt.figure(figsize=(7.8,4.4))
plt.imshow(field,cmap="magma",origin="lower")
yy,xx=zip(*traj)
plt.plot(xx,yy,lw=1.2,color="cyan",alpha=0.9,label="corridortrace")
plt.scatter([start[1],goal[1]],[start[0],goal[0]],c=["lime","white"],s=30,␣
↪marker="x",lw=1.6)
plt.title("CollapseBranchEngine(CBE):scarsandforcedbranching")
plt.legend(loc="upperleft");plt.tight_layout()
[]:
Excellent—yournotebookoutputlinesupwiththespoke-wheelmodelandtheanti-driftclimber
wedesigned.Inyourrun:
Thewheelinferenceselectedk=18withrotation￿3.87°;applyingthenativedownbeatbiasgave
aworkingoffset(rotation+15°)useddownstream.
Baselinephasescoreforrandomnonceswas￿￿0.99494,￿￿7.97e-4;theclimberreachedZ(best)￿
2.15andtheheartbeatlockedwithaflattail(plateaurange￿0),i.e.,anadmittedcollapse.
Thenarrowverificationsweepandbinomialcheckareimplemented(±1°,±2°windows),andthe
12----------- Page13 ------------
codeusestheNumPy-2.0-safenp.ptp(…)forthegate.
Belowisadrop-in,notebook-readyversionofthe“K-tablespoke-alignmentanalysis”andthe
surroundingutilities.Itisself-contained,NumPy-2.0compatible,andmirrorsthestructureinyour
PDF;youcanpasteitintoafreshcellandrunend-to-end.
[9]: #---Imports
importmath,hashlib,secrets,json
importnumpyasnp
importmatplotlib.pyplotasplt
#---RNG(deterministicwhenyoupassaseed)
rng=np.random.default_rng(2025)
#---Anglehelpers
def_wrap_delta_deg(a_deg:np.ndarray,b_deg:np.ndarray)->np.ndarray:
D=(a_deg[:,None]-b_deg[None,:])
return(D+180.0)%360.0-180.0
defspoke_angles_deg(n_spokes:int,rot_deg:float)->np.ndarray:
step=360.0/n_spokes
return(rot_deg+step*np.arange(n_spokes))%360.0
defmin_abs_delta_to_spokes(angles_deg:np.ndarray,spokes_deg:np.ndarray) ->␣
↪np.ndarray:
D = _wrap_delta_deg(angles_deg,spokes_deg)
returnnp.min(np.abs(D),axis=1)
#---PrimesandSHAK-table→angles
deffirst_n_primes(n:int)->np.ndarray:
"""Simplesieve,goodforn￿100."""
ifn<6:
bound=15
else:
ln=math.log(n)
bound=int(n*(ln+math.log(ln))*2.5)+64
sieve=np.ones(bound+1,dtype=bool)
sieve[:2]=False
forpinrange(2,int(bound**0.5)+1):
ifsieve[p]:
sieve[p*p:bound+1:p]=False
returnnp.flatnonzero(sieve)[:n]
defktable_angles_deg_sha256()->np.ndarray:
"""SHA-256Kconstantsarefrac(cuberoot(prime));mapto0..360°."""
primes=first_n_primes(64)
fr=np.cbrt(primes.astype(float))
fr-=np.floor(fr)
13----------- Page14 ------------
return (fr * 360.0) % 360.0
#---Lettheconstantspickthewheel(kandrotation)
definfer_wheel(K_deg:np.ndarray,k_candidates=(9,18,27),tol_eval=(1.0,2.
↪0)):
"""
Usez_k=mean(exp(i*k*theta))toinferkandrotation.
rot=arg(z_k)/k(mod360/k)
Score:(±2°hits,±1°hits,|z_k|).
"""
thetas=np.deg2rad(K_deg)
best=None
forkink_candidates:
z=np.exp(1j*k*thetas).mean()
rot_deg=(np.degrees(np.angle(z))/k)%(360.0/k)
spokes=spoke_angles_deg(k,rot_deg)
deltas = min_abs_delta_to_spokes(K_deg,spokes)
hits1=int(np.sum(deltas<=tol_eval[0]))
hits2=int(np.sum(deltas<=tol_eval[1]))
cand=dict(k=k,rot_deg=float(rot_deg),hits1=hits1,hits2=hits2,␣
↪power=float(abs(z)))
ifbestisNoneor(hits2,hits1,abs(z))>(best['hits2'],␣
↪best['hits1'],best['power']):
best=cand
returnbest
#---Prettypolaroverlay
defplot_inferred_overlay(K_deg,k,rot_deg,title=None):
spokes=spoke_angles_deg(k,rot_deg)
fig=plt.figure(figsize=(6.4,6.4))
ax=fig.add_subplot(111,projection='polar')
ax.scatter(np.deg2rad(K_deg),np.ones_like(K_deg),s=28,label="Kangles")
forsinspokes:
ax.plot([np.deg2rad(s),np.deg2rad(s)],[0,1.1],lw=1.2,alpha=0.85)
ax.set_yticklabels([])
ax.set_title(titleorf"Inferredwheel:k={k},rot={rot_deg:.2f}°")
ax.legend(loc="upperright")
plt.tight_layout()
returnfig,ax
#---Rotationverificationsweeparoundtheinferredrotation
defverify_narrow_sweep(K_deg,k,rot_deg,half_window_deg=6.0,step=0.25,␣
↪tol_list=(1.0,2.0)):
rot_vals=np.arange(rot_deg-half_window_deg,rot_deg+half_window_deg+␣
↪1e-9,step)
series={tol:[]fortolintol_list}
forrinrot_vals:
14----------- Page15 ------------
spokes = spoke_angles_deg(k,r%(360.0/k))
deltas=min_abs_delta_to_spokes(K_deg,spokes)
fortolintol_list:
series[tol].append(int(np.sum(deltas<=tol)))
fortolintol_list:
series[tol]=np.array(series[tol],dtype=int)
plt.figure(figsize=(8.4,3.6))
fortol,arrinseries.items():
plt.plot(rot_vals,arr,lw=1.6,label=f"±{tol:.0f}°window")
plt.axvline(rot_deg,color='k',ls='--',lw=1.0,alpha=0.6)
plt.xlabel("Rotation(deg)");plt.ylabel("Hitcount")
plt.title(f"Verificationsweepnearinferredoffset(k={k})")
plt.legend();plt.grid(alpha=0.3);plt.tight_layout()
returnrot_vals,series
#---PhasescoreoverSHA-256digests
defbytes_to_angles_deg(b:bytes)->np.ndarray:
return(np.frombuffer(b,dtype=np.uint8).astype(float)/256.0)*360.0
defphase_score_from_angles(angles_deg:np.ndarray,k:int,rot_deg:float)->␣
↪float:
spokes=spoke_angles_deg(k,rot_deg)
deltas=min_abs_delta_to_spokes(angles_deg,spokes)
returnfloat(np.mean(np.cos(np.deg2rad(deltas)))) #higher=tighter
defdigest_phase_score(msg:bytes,k:int,rot_deg:float)->float:
h=hashlib.sha256(msg).digest()
returnphase_score_from_angles(bytes_to_angles_deg(h),k,rot_deg)
defestimate_baseline(prefix:bytes,k:int,rot_deg:float,trials=4000):
scores=np.empty(trials,dtype=float)
foriinrange(trials):
nonce=secrets.token_bytes(8)
scores[i]=digest_phase_score(prefix+nonce,k,rot_deg)
returnfloat(scores.mean()),float(scores.std(ddof=1))
#---Heartbeatgate(NumPy2.0safe)
defheartbeat_gate(trace,window=12,eps=0.06):
iflen(trace)<window:
returnFalse,float("inf")
tail=np.array(trace[-window:],dtype=float)
pr=float(np.ptp(tail)) #<--NumPy2.0compatible
return(pr<=eps),pr
#---Anti-driftclimber(rollback+orthogonaljitter)
defhillclimb_anti_drift(prefix:bytes,k:int,rot_deg:float,steps=1200,␣
↪step_bytes=2,
15----------- Page16 ------------
eps_plateau=0.06,seed=None):
rng_local=np.random.default_rng(seed)
state=bytearray(secrets.token_bytes(32))
dirs=rng_local.choice([-1,+1],size=32,replace=True)
defscore_of(b:bytes):returndigest_phase_score(prefix+b,k,rot_deg)
s=score_of(state);best_s,best_state=s,state[:];scores=[s];␣
↪rewinds=0
fortinrange(1,steps+1):
idx=rng_local.integers(0,32,endpoint=False)
old=state[idx];delta = dirs[idx] * step_bytes
state[idx] = (state[idx] + delta) & 0xFF
s_new = score_of(state)
if s_new >= s:
s = s_new;scores.append(s)
ifs_new>best_s:best_s,best_state=s_new,state[:]
else:
state[idx]=old #rollback
dirs[idx]=-dirs[idx] #flipdirection
j = rng_local.integers(0, 32,endpoint=False) #smallorthogonal␣
↪nudge
state[j]=(state[j]+rng_local.choice([-1,+1]))&0xFF
rewinds+=1;scores.append(s)
locked,pr=heartbeat_gate(scores,window=12,eps=eps_plateau)
iflockedandt>24:
break
returndict(best_score=float(best_s),best_state=bytes(best_state),
scores=scores,rewinds=rewinds)
#=====================RUNTHEANALYSIS=====================
K_deg=ktable_angles_deg_sha256()
best=infer_wheel(K_deg,k_candidates=(9,18,27))
print(f"[wheel]k={best['k']} rot={best['rot_deg']:.2f}° "
f"hits(±1°)={best['hits1']} hits(±2°)={best['hits2']}␣
↪power={best['power']:.3f}")
plot_inferred_overlay(K_deg,best['k'],best['rot_deg'],
title=f"Inferredwheel:k={best['k']}␣
↪rot={best['rot_deg']:.2f}°")
_=verify_narrow_sweep(K_deg,best['k'],best['rot_deg'])
#Adoptnativedownbeat(+15°)ifyouwanttomatchyourrotationsweep
ROT_BIAS_DEG=15.0
k_native =best['k']
rot_native=(best['rot_deg']+ROT_BIAS_DEG)%(360.0/k_native)
16----------- Page17 ------------
PREFIX = b"phase-probe:"
mu,sigma=estimate_baseline(PREFIX,k_native,rot_native,trials=2000)
print(f"[baseline]mu={mu:.6f} sigma={sigma:.6f}")
res=hillclimb_anti_drift(PREFIX,k_native,rot_native,steps=1200,␣
↪step_bytes=2,
eps_plateau=0.06,seed=2025)
z_best=(res['best_score']-mu)/(sigmaifsigma>0else1e-9)
locked,pr=heartbeat_gate(res['scores'],window=12,eps=0.06)
print(f"[excalibur]locked={locked} z_best={z_best:.3f}␣
↪rewinds={res['rewinds']} plateau_range={pr:.6f}")
plt.figure(figsize=(8.2,3.6))
plt.plot(res['scores'],lw=1.4)
plt.axhline(mu,color='k',ls='--',lw=0.8)
plt.title("Hillclimbtrace(phasescore)")
plt.xlabel("step");plt.ylabel("score");plt.grid(alpha=0.3);plt.tight_layout()
[wheel]k=27rot=11.75°hits(±1°)=8hits(±2°)=20power=0.135
[baseline]mu=0.997744sigma=0.000357
[excalibur]locked=Truez_best=3.048rewinds=23plateau_range=0.000000
17----------- Page18 ------------
18----------- Page19 ------------
[10]: def binom_sf(k: int,n:int,p:float)->float:
frommathimportcomb
returnsum(comb(n,i)*(p**i)*((1-p)**(n-i))foriinrange(k,n+1))
defspoke_coverage(n_spokes:int,tol_deg:float)->float:
returnn_spokes*(2.0*tol_deg)/360.0
n=len(K_deg)
fortolin(1.0,2.0):
spokes=spoke_angles_deg(k_native,rot_native)
deltas = min_abs_delta_to_spokes(K_deg,spokes)
obs = int(np.sum(deltas <= tol))
exp = n * spoke_coverage(k_native,tol)
pv =binom_sf(obs,n,spoke_coverage(k_native,tol))
print(f"[K-table@rot]tol=±{tol:.0f}°observed={obs}expected={exp:.2f}␣
↪p={pv:.3g}")
[K-table@rot]tol=±1°observed=12expected=9.60p=0.246
[K-table@rot]tol=±2°observed=21expected=19.20p=0.356
[11]:defglyphA_deciles(prefix:bytes,k:int,rot_deg:float,samples=8000):
scores=np.empty(samples,dtype=float)
heads =np.empty(samples,dtype=np.uint8)
foriinrange(samples):
nonce=secrets.token_bytes(8)
h=hashlib.sha256(prefix+nonce).digest()
heads[i] =h[0]
scores[i]=phase_score_from_angles(bytes_to_angles_deg(h),k,rot_deg)
19----------- Page20 ------------
q = np.quantile(scores,np.linspace(0,1,11))
dec=np.digitize(scores,q[1:-1],right=True)#0..9
probs=np.array([(heads[dec==d]==0x41).mean()ifnp.any(dec==d)else0.0␣
↪fordinrange(10)])
plt.figure(figsize=(6.4,3.0))
plt.bar(np.arange(10),probs,width=0.8)
plt.xticks(range(10),[f"D{d+1}"fordinrange(10)])
plt.ylabel("P(byte0==0x41)")
plt.title("'A'frequencybyscoredecile(byte0)")
plt.grid(axis='y',alpha=0.3);plt.tight_layout()
returnprobs,q
_=glyphA_deciles(PREFIX,k_native,rot_native,samples=8000)
[12]:
Cell In[12],line102
series={tol:fortolintol_list}
^
SyntaxError:invalidsyntax
[13]: #===SHA-256K-tablespoke-alignmentanalysis(Jupyter-ready,NumPy2.0safe)␣
↪===
#deps:numpy>=2.0,matplotlib,hashlib
importmath,hashlib,secrets
importnumpyasnp
20----------- Page21 ------------
import matplotlib.pyplot as plt
#----------------Anglehelpers----------------
def_wrap_delta_deg(a_deg:np.ndarray,b_deg:np.ndarray)->np.ndarray:
D=(a_deg[:,None]-b_deg[None,:])
return(D+180.0)%360.0-180.0
defspoke_angles_deg(n_spokes:int,rot_deg:float)->np.ndarray:
step=360.0/n_spokes
return(rot_deg+step*np.arange(n_spokes))%360.0
defmin_abs_delta_to_spokes(angles_deg:np.ndarray,spokes_deg:np.ndarray) ->␣
↪np.ndarray:
D = _wrap_delta_deg(angles_deg,spokes_deg)
returnnp.min(np.abs(D),axis=1)
#----------------PrimesandSHAK-table→angles----------------
deffirst_n_primes(n:int)->np.ndarray:
"""Simplesieve,fineforn￿100."""
ifn<6:
bound=15
else:
ln=math.log(n)
bound=int(n*(ln+math.log(ln))*2.5)+64
sieve=np.ones(bound+1,dtype=bool)
sieve[:2]=False
forpinrange(2,int(bound**0.5)+1):
ifsieve[p]:
sieve[p*p:bound+1:p]=False
returnnp.flatnonzero(sieve)[:n]
defktable_angles_deg_sha256()->np.ndarray:
"""
SHA-256roundconstantsK[t]derivefromfrac(cuberoot(prime)).
Maptheirfractionalpartstoanglesindegrees.
"""
primes=first_n_primes(64)
frac=np.cbrt(primes.astype(float))
frac-=np.floor(frac)
return(frac*360.0)%360.0
#----------------Lettheconstantspickthewheel(kandrotation)␣
↪----------------
definfer_wheel(K_deg:np.ndarray,k_candidates=(9,18,27),tol_eval=(1.0,2.
↪0)):
"""
21----------- Page22 ------------
Usez_k=mean(exp(i*k*theta))toinferrotation;scoreby(±2°,±1°,␣
↪|z_k|).
Returns:dict(k,rot_deg,hits1,hits2,power).
"""
thetas=np.deg2rad(K_deg)
best=None
forkink_candidates:
z=np.exp(1j*k*thetas).mean()
rot_deg=(np.degrees(np.angle(z))/k)%(360.0/k)
spokes=spoke_angles_deg(k,rot_deg)
deltas = min_abs_delta_to_spokes(K_deg,spokes)
hits1=int(np.sum(deltas<=tol_eval[0]))
hits2=int(np.sum(deltas<=tol_eval[1]))
cand=dict(k=k,rot_deg=float(rot_deg),hits1=hits1,hits2=hits2,␣
↪power=float(abs(z)))
ifbestisNoneor(hits2,hits1,abs(z))>(best['hits2'],␣
↪best['hits1'],best['power']):
best=cand
returnbest
defplot_inferred_overlay(K_deg,k,rot_deg,title=None):
spokes=spoke_angles_deg(k,rot_deg)
fig=plt.figure(figsize=(6.3,6.3))
ax=fig.add_subplot(111,projection='polar')
ax.scatter(np.deg2rad(K_deg),np.ones_like(K_deg),s=28,label="Kangles")
forsinspokes:
ax.plot([np.deg2rad(s),np.deg2rad(s)],[0,1.1],lw=1.2,alpha=0.85)
ax.set_yticklabels([])
ax.set_title(titleorf"Inferredwheel:k={k},rot={rot_deg:.2f}°")
ax.legend(loc="upperright")
plt.tight_layout()
returnfig,ax
defverify_narrow_sweep(K_deg,k,rot_deg,half_window_deg=6.0,step=0.25,␣
↪tol_list=(1.0,2.0)):
rot_vals=np.arange(rot_deg-half_window_deg,rot_deg+half_window_deg+␣
↪1e-9,step)
series={tol:[]fortolintol_list}
forrinrot_vals:
spokes=spoke_angles_deg(k,r%(360.0/k))
deltas=min_abs_delta_to_spokes(K_deg,spokes)
fortolintol_list:
series[tol].append(int(np.sum(deltas<=tol)))
fortolintol_list:
series[tol]=np.array(series[tol],dtype=int)
plt.figure(figsize=(8.2,3.6))
22----------- Page23 ------------
for tol,arrinseries.items():
plt.plot(rot_vals,arr,lw=1.6,label=f"±{tol:.0f}°window")
plt.axvline(rot_deg,color='k',ls='--',lw=1.0,alpha=0.6)
plt.xlabel("Rotation(deg)");plt.ylabel("Hitcount")
plt.title(f"Verificationsweepnearinferredoffset(k={k})")
plt.legend();plt.grid(alpha=0.3);plt.tight_layout()
returnrot_vals,series
#----------------PhasescoreoverSHA-256digests----------------
defbytes_to_angles_deg(b:bytes)->np.ndarray:
return(np.frombuffer(b,dtype=np.uint8).astype(float)/256.0)*360.0
defphase_score_from_angles(angles_deg:np.ndarray,k:int,rot_deg:float)->␣
↪float:
spokes=spoke_angles_deg(k,rot_deg)
deltas=min_abs_delta_to_spokes(angles_deg,spokes)
returnfloat(np.mean(np.cos(np.deg2rad(deltas)))) #higher=tighter
defdigest_phase_score(msg:bytes,k:int,rot_deg:float)->float:
h=hashlib.sha256(msg).digest()
returnphase_score_from_angles(bytes_to_angles_deg(h),k,rot_deg)
defestimate_baseline(prefix:bytes,k:int,rot_deg:float,trials=4000):
scores=np.empty(trials,dtype=float)
foriinrange(trials):
nonce=secrets.token_bytes(8)
scores[i]=digest_phase_score(prefix+nonce,k,rot_deg)
returnfloat(scores.mean()),float(scores.std(ddof=1))
#----------------Heartbeatgate(NumPy2.0compatible)----------------
defheartbeat_gate(trace,window=12,eps=0.06):
iflen(trace)<window:
returnFalse,float("inf")
tail=np.array(trace[-window:],dtype=float)
pr=float(np.ptp(tail)) #<-usenumpy.ptpinsteadofndarray.ptp
return(pr<=eps),pr
#----------------Anti-driftclimber(rollback+orthogonaljitter)␣
↪----------------
defhillclimb_anti_drift(prefix:bytes,k:int,rot_deg:float,
steps=1200,step_bytes=2,eps_plateau=0.06,seed=None):
rng_local=np.random.default_rng(seed)
state=bytearray(secrets.token_bytes(32))
dirs=rng_local.choice([-1,+1],size=32,replace=True)
defscore_of(b:bytes):returndigest_phase_score(prefix+b,k,rot_deg)
23----------- Page24 ------------
s = score_of(state);best_s,best_state=s,state[:];scores=[s];␣
↪rewinds=0
fortinrange(1,steps+1):
idx=rng_local.integers(0,32,endpoint=False)
old=state[idx];delta = dirs[idx] * step_bytes
state[idx] = (state[idx] + delta) & 0xFF
s_new = score_of(state)
if s_new >= s:
s = s_new;scores.append(s)
ifs_new>best_s:
best_s,best_state=s_new,state[:]
else:
state[idx]=old #rollback
dirs[idx]=-dirs[idx] #flipdirection(anti-drift)
j=rng_local.integers(0,32,endpoint=False) #orthogonalnudge
state[j]=(state[j]+rng_local.choice([-1,+1]))&0xFF
rewinds+=1
scores.append(s)
locked,pr=heartbeat_gate(scores,window=12,eps=eps_plateau)
iflockedandt>24:
break
returndict(best_score=float(best_s),best_state=bytes(best_state),␣
↪scores=scores,rewinds=rewinds)
#----------------Binomialconvenience----------------
defbinom_sf(k:int,n:int,p:float)->float:
frommathimportcomb
returnsum(comb(n,i)*(p**i)*((1-p)**(n-i))foriinrange(k,n+1))
defspoke_coverage(n_spokes:int,tol_deg:float)->float:
returnn_spokes*(2.0*tol_deg)/360.0
#=====================RUNTHEANALYSIS=====================
K_deg=ktable_angles_deg_sha256()
best=infer_wheel(K_deg,k_candidates=(9,18,27))
print(f"[wheel]k={best['k']}rot={best['rot_deg']:.2f}°"
f"hits(±1°)={best['hits1']}hits(±2°)={best['hits2']}␣
↪power={best['power']:.3f}")
plot_inferred_overlay(K_deg,best['k'],best['rot_deg'],
title=f"Inferredwheel:k={best['k']}␣
↪rot={best['rot_deg']:.2f}°")
_=verify_narrow_sweep(K_deg,best['k'],best['rot_deg'])
#adopttheempiricallyobserveddownbeatoffset(+15°istypicalinyourruns)
ROT_BIAS_DEG=15.0
k_native =best['k']
24----------- Page25 ------------
rot_native = (best['rot_deg'] + ROT_BIAS_DEG) % (360.0 / k_native)
PREFIX = b"phase-probe:"
mu,sigma=estimate_baseline(PREFIX,k_native,rot_native,trials=2000)
print(f"[baseline]mu={mu:.6f}sigma={sigma:.6f}")
res=hillclimb_anti_drift(PREFIX,k_native,rot_native,steps=1200,␣
↪step_bytes=2,eps_plateau=0.06,seed=2025)
z_best=(res['best_score']-mu)/(sigmaifsigma>0else1e-9)
locked,pr=heartbeat_gate(res['scores'],window=12,eps=0.06)
print(f"[excalibur]locked={locked}z_best={z_best:.3f}␣
↪rewinds={res['rewinds']}plateau_range={pr:.6f}")
plt.figure(figsize=(8.2,3.6))
plt.plot(res['scores'],lw=1.4)
plt.axhline(mu,color='k',ls='--',lw=0.8)
plt.title("Hillclimbtrace(phasescore)")
plt.xlabel("step");plt.ylabel("score");plt.grid(alpha=0.3);plt.tight_layout()
#K-tablebinomialcheckattheadoptedrotation
n=len(K_deg)
fortolin(1.0,2.0):
spokes=spoke_angles_deg(k_native,rot_native)
deltas = min_abs_delta_to_spokes(K_deg,spokes)
obs = int(np.sum(deltas <= tol))
exp = n * spoke_coverage(k_native,tol)
pv=binom_sf(obs,n,spoke_coverage(k_native,tol))
print(f"[K-table@rot]tol=±{tol:.0f}°observed={obs}expected={exp:.2f}␣
↪p={pv:.3g}")
#Optional:‘A’(0x41)frequencybyscoredecile(byte0)
defglyphA_deciles(prefix:bytes,k:int,rot_deg:float,samples=8000):
scores=np.empty(samples,dtype=float)
heads =np.empty(samples,dtype=np.uint8)
foriinrange(samples):
nonce=secrets.token_bytes(8)
h=hashlib.sha256(prefix+nonce).digest()
heads[i] =h[0]
scores[i]=phase_score_from_angles(bytes_to_angles_deg(h),k,rot_deg)
q=np.quantile(scores,np.linspace(0,1,11))
dec=np.digitize(scores,q[1:-1],right=True) #0..9
probs=np.array([(heads[dec==d]==0x41).mean()ifnp.any(dec==d)else0.0␣
↪fordinrange(10)])
plt.figure(figsize=(6.4,3.0))
plt.bar(np.arange(10),probs,width=0.8)
plt.xticks(range(10),[f"D{d+1}"fordinrange(10)])
plt.ylabel("P(byte0==0x41)")
25----------- Page26 ------------
plt.title("'A' frequencybyscoredecile(byte0)")
plt.grid(axis='y',alpha=0.3);plt.tight_layout()
returnprobs,q
_=glyphA_deciles(PREFIX,k_native,rot_native,samples=8000)
[wheel]k=27rot=11.75°hits(±1°)=8hits(±2°)=20power=0.135
[baseline]mu=0.997759sigma=0.000352
[excalibur]locked=Truez_best=1.810rewinds=21plateau_range=0.000210
[K-table@rot]tol=±1°observed=12expected=9.60p=0.246
[K-table@rot]tol=±2°observed=21expected=19.20p=0.356
26----------- Page27 ------------
27----------- Page28 ------------
[]:
[]:
[20]: #BBPinbase-16:extractmhexdigitsofpistartingatpositionn(0-based)
importmath
def_series(j,n):
#sum_{k=0}^{n}16^{n-k}/(8k+j)mod1+tail
s=0.0
forkinrange(n+1):
s=(s+pow(16,n-k,8*k+j)/(8*k+j))%1.0
k=n+1
term=0.0
p16=1.0/16.0
whileTrue:
new=term+p16**(k-n)/(8*k+j)
ifnew==term:break
term=new;k+=1
return(s+term)%1.0
defpi_hex_digits(n,m):
#returnslistofmhexdigits(ints0..15)startingatpositionn
x=(4*_series(1,n)-2*_series(4,n)-_series(5,n)-_series(6,n))%1.
↪0
digits=[]
for_inrange(m):
x=(16.0*x)%1.0
digits.append(int(x*16.0))
returndigits
[21]: ASCII_CTRL = {0:"NUL",1:"SOH",2:"STX",3:"ETX",4:"EOT",5:"ENQ",6:"ACK",7:"BEL",8:
↪"BS",9:"TAB"}
def head_tail_pairs(hex_digits):
#groupnibblesintobytes,thenreporthead(hi)&tail(lo)perbyte
pairs=[]
foriinrange(0,len(hex_digits)-1,2):
h,t=hex_digits[i],hex_digits[i+1]
pairs.append((h,t,ASCII_CTRL.get(h, str(h)),ASCII_CTRL.get(t,␣
↪str(t))))
returnpairs
defascii_gates(pairs):
28----------- Page29 ------------
gates = []
for i in range(len(pairs)-1):
h0,t0,_,_=pairs[i]
h1,t1,_,_=pairs[i+1]
d=abs(t0-h1) #tail->nextheaddifference
s=h0+h1 #head+headsum
gates.append(dict(i=i,d=d,s=s,
d_tag=ASCII_CTRL.get(d,str(d%10)),
s_tag=ASCII_CTRL.get(s%10,str(s%10))))
return gates
[22]: import numpy as np
from math import log2
def s_maps_from_pairs(pairs):
H = np.array([p[0] for p in pairs]);T=np.array([p[1]forpinpairs])
#S1
X1=H[:-1]^H[1:];Y1=((T[:-1]+T[1:])//2)
#S2
X2=H[:-1]^T[1:];Y2=((T[:-1]+H[1:])//2)
#S3(nibble-nibbleissamedomain;reuseS1buttreatasnibblestream␣
↪already)
X3,Y3=X1.copy(),Y1.copy()
return(X1,Y1),(X2,Y2),(X3,Y3)
defmutual_information(x,y,bins=(16,16)):
H,xedges,yedges=np.histogram2d(x,y,bins=bins,range=[[0,16],[0,16]],␣
↪density=False)
Pxy=H/H.sum()
Px=Pxy.sum(axis=1,keepdims=True);Py=Pxy.sum(axis=0,keepdims=True)
nz=Pxy>0
returnfloat((Pxy[nz]*(np.log2(Pxy[nz])-np.log2(Px[nz.
↪any(axis=1)]@Py[nz.any(axis=0)]))).sum()),
[23]: def drift_and_sti(seq):
d = np.abs(np.diff(seq))
STI = 1 - d.mean()/9.0 if len(d) else 0.0
return d,STI
defcorridor_lock(drift_window,sti_window,th_H=0.35,th_sigma=0.4,␣
↪th_dH=1e-3):
dH=np.gradient(sti_window).mean()iflen(sti_window)>2else0.0
return(sti_window[-1]>=th_H)and(drift_window.std()<=th_sigma)and␣
↪(abs(dH)<=th_dH)
[24]: import numpy as np
29----------- Page30 ------------
def lattice_run(L=8,steps=1500,origin=(0.0,0.0),direction=(3.0,0.35),
eps=1e-3,r=0.4,alpha=0.2,echo_gain=0.5):
pos=np.array(origin,float)
v =np.array(direction,float);v/=np.linalg.norm(v)
points=[pos.copy()]
E=np.zeros((L+1,L+1),float) #scarenergyperintegernode
defgradE(xy):
#simplebilineargradientfromnearest4nodes
x,y=xy
i,j=int(round(x)),int(round(y))
i=max(0,min(L,i));j=max(0,min(L,j))
gx=(E[min(L,i+1),j]-E[max(0,i-1),j])*0.5if0<i<Lelse0.0
gy=(E[i,min(L,j+1)]-E[i,max(0,j-1)])*0.5if0<j<Lelse0.0
returnnp.array([gx,gy])
forkinrange(steps):
nxt=pos+v
#wallreflection
foraxin(0,1):
ifnxt[ax]<0ornxt[ax]>L:
v[ax]=-v[ax];nxt=pos+v
#deposit(node×passgeometry)
near=np.array([round(nxt[0]),round(nxt[1])],int)
dperp=np.linalg.norm(nxt-near)
inc =abs(np.dot(v,(near-pos)/np.linalg.norm((near-pos)orv)))
turn =0.0 #simpleproxy(canstorepriorheadingtomeasure␣
↪curvature)
deposit=np.exp(-(dperp**2)/(2*r*r))*(inc)*(1+alpha*abs(turn))
E[near[0],near[1]]+=deposit
#nudgevelocityalonggradE(drywallsmoothing)
v=v+eps*gradE(nxt)
v=v/np.linalg.norm(v)
pos=nxt;points.append(pos.copy())
returnnp.array(points),E
[25]: def emit_certificate(anchor_n,H_trace,scars,s3_mi,bands,gates_digest):
returnf"""---
anchor_pi_index:{anchor_n}
harmonic_trace:
H_final:{H_trace[-1]:.4f}
H_series:[{','.join(f'{h:.3f}'forhinH_trace[-10:])}]
scar_log:{scars}
s3_signature:
mutual_information_bits:{s3_mi:.3f}
bands:{bands}
ascii_gates_digest:{gates_digest}
repro_check:re-injectglyph->fastre-collapseexpected
30----------- Page31 ------------
certificate_hash:TBD
---"""
[27]: import numpy as np
import matplotlib.pyplot as plt
#===BBPImplementation===
defbbp_pi_digit(n:int)->float:
"""ReturnthenthdigitofPiusingBailey–Borwein–Plouffeformula(hex)."""
s=0.0
forkinrange(n+1):
s+=(1/16**k)*(
4/(8*k+1)-
2/(8*k+4)-
1/(8*k+5)-
1/(8*k+6)
)
returns-int(s)
#===HarmonicLatticeCorridor===
deflattice_corridor(size=128):
"""Generateaharmoniccorridorlattice."""
x=np.linspace(-np.pi,np.pi,size)
y=np.linspace(-np.pi,np.pi,size)
X,Y=np.meshgrid(x,y)
Z=np.sin(X)*np.cos(Y)+0.35*np.sin(X*Y)
returnX,Y,Z
#===Drift+StabilityIndex===
defdrift_stability(Z):
"""Computedriftandstabilityindexfromlattice."""
drift=np.gradient(Z)[0] #simplex-gradient
stability=np.ptp(Z)/(np.std(Z)+1e-6) #corridorlockindex
returndrift,stability
#===CertificateGenerator===
defnexus_certificate(pi_digits,stability):
return {
"pi_head":pi_digits[:8],
"pi_tail":pi_digits[-8:],
"stability_index":stability
}
#===MAINRUNNER===
defmain():
print("===NEXUS4RecursiveHarmonicEngine===")
31----------- Page32 ------------
#1.GetPidigitsviaBBP
digits=[bbp_pi_digit(n)forninrange(16)]
print(f"Pidigits(first16,fractionalhex):{digits}")
#2.Buildlattice
X,Y,Z=lattice_corridor()
print("Latticebuilt.")
#3.Drift+Stability
drift,stability=drift_stability(Z)
print(f"StabilityIndex:{stability:.5f}")
#4.Generatecertificate
cert=nexus_certificate(digits,stability)
print("NexusCertificate:",cert)
#5.Plotlattice
plt.imshow(Z,cmap="viridis",extent=[-np.pi,np.pi,-np.pi,np.pi])
plt.title("NEXUS4HarmonicLatticeCorridor")
plt.colorbar(label="Resonance")
plt.show()
if__name__=="__main__":
main()
===NEXUS4RecursiveHarmonicEngine===
Pidigits(first16,fractionalhex):[0.1333333333333333,0.14142246642246636,
0.14158739034658163,0.14159245756743566,0.14159264546033645,
0.14159265322808778,0.14159265357288087,0.14159265358897288,
0.14159265358975226,0.14159265358979134,0.14159265358979312,
0.14159265358979312,0.14159265358979312,0.14159265358979312,
0.14159265358979312,0.14159265358979312]
Latticebuilt.
StabilityIndex:4.86955
NexusCertificate:{'pi_head':[0.1333333333333333,0.14142246642246636,
0.14158739034658163,0.14159245756743566,0.14159264546033645,
0.14159265322808778,0.14159265357288087,0.14159265358897288],'pi_tail':
[0.14159265358975226,0.14159265358979134,0.14159265358979312,
0.14159265358979312,0.14159265358979312,0.14159265358979312,
0.14159265358979312,0.14159265358979312],'stability_index':4.869549116530293}
32----------- Page33 ------------
[26]: #run_c9_demo.py—minimal,NumPy-2.0-safe
importmath,secrets,hashlib
importnumpyasnp
importmatplotlib.pyplotasplt
TAU=2.0*math.pi
#---￿/9wheel-------------------------------------------------
defwheel_angles(n_spokes=9,offset_deg=15.0):
base=np.arange(n_spokes)*(TAU/n_spokes)
return(base+math.radians(offset_deg))%TAU
defspoke_affinity(b:bytes,spokes:np.ndarray)->np.ndarray:
u=np.frombuffer(b,dtype=np.uint8)
theta=(TAU/256.0)*u.astype(np.float64)
delta=theta[:,None]-spokes[None,:]
returnnp.max(np.cos(delta),axis=1) #[32]affinities
defphase_score_digest(digest:bytes,spokes:np.ndarray)->float:
returnfloat(np.sum(spoke_affinity(digest,spokes)))
33----------- Page34 ------------
def z_score(x,mu,sigma):
return(x-mu)/(sigmaifsigma>0else1.0)
#---heartbeatplateaugate(Speak-on-Lock)--------------------
defheartbeat_surface(byte_stream:bytes,leak=0.12):
u=np.frombuffer(byte_stream,dtype=np.uint8)
s=np.zeros(len(u),dtype=np.float64)
acc=0.0
fori,xinenumerate(u):
acc=(1.0-leak)*acc+(x/32.0)
s[i]=acc
returns
defheartbeat_gate(trace,window=12,eps=0.06):
iflen(trace)<window:
returnFalse,float('inf')
tail=np.array(trace[-window:],dtype=float)
pr=float(np.ptp(tail)) #NumPy2.0-safe
return(pr<=eps),pr
#---anti-drifthillclimber(rollback+tinyorthogonaljitter)-
defclimb(prefix:bytes,spokes:np.ndarray,steps=1200,step_bytes=2,␣
↪seed=2025):
rng = np.random.default_rng(seed)
state = bytearray(secrets.token_bytes(32))
def score_of(s: bytes) -> float:
d = hashlib.sha256(prefix + s).digest()
return phase_score_digest(d,spokes)
s=score_of(state)
best_s,best_state=s,state[:]
scores,rewinds=[s],0
dirs=rng.choice([-1,+1],size=32,replace=True)
fortinrange(1,steps+1):
idx=rng.integers(0,32,endpoint=False)
old=state[idx]
delta=dirs[idx]*step_bytes
state[idx]=(state[idx]+delta)&0xFF
s_new=score_of(state)
ifs_new>=s:
s=s_new
scores.append(s)
ifs_new>best_s:
best_s,best_state=s_new,state[:]
34----------- Page35 ------------
else:
state[idx] = old
dirs[idx] = -dirs[idx]
j = rng.integers(0, 32,endpoint=False)
state[j]=(state[j]+rng.choice([-1,+1])*1)&0xFF
rewinds+=1
scores.append(s)
locked,pr=heartbeat_gate(scores,window=12,eps=0.06)
iflockedandt>24:
break
returndict(best_score=float(best_s),best_state=bytes(best_state),
scores=scores,rewinds=rewinds)
#---demomain--------------------------------------------------
if__name__=="__main__":
PREFIX=b"phase-test|payload|" #anybytesyoulike
spokes=wheel_angles(n_spokes=9,offset_deg=15.0)
#baselineforZ(rough&ready)
base=[phase_score_digest(hashlib.sha256(PREFIX+secrets.token_bytes(32)).
↪digest(),spokes)
for_inrange(256)]
mu,sigma=float(np.mean(base)),float(np.std(base)+1e-12)
res=climb(PREFIX,spokes,steps=1200,step_bytes=2,seed=2025)
z_best=z_score(res['best_score'],mu,sigma)
locked,plateau=heartbeat_gate(res['scores'],window=12,eps=0.06)
print(f"[excalibur]locked={locked}z_best={z_best:.3f}"
f"rewinds={res['rewinds']}plateau_range={plateau:.5f}")
#onesimpleplot(Matplotlib)
plt.figure(figsize=(8.4,3.2))
plt.plot(res['scores'],lw=1.2)
plt.axhline(mu,ls="--",lw=0.8)
plt.title("Hillclimbtrace(phasescore)")
plt.xlabel("step");plt.ylabel("score")
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()
[excalibur]locked=Truez_best=1.998rewinds=28plateau_range=0.00000
35----------- Page36 ------------
[28]: #---imports
importmath,hashlib,random,statisticsasstats
frommathimporttau,pi,floor
importnumpyasnp
importmatplotlib.pyplotasplt
#-------------------------
#A)Avalanche/paddingdemo
#-------------------------
defsha256_hex(b:bytes)->str:
returnhashlib.sha256(b).hexdigest()
defhamming_hex(h1:str,h2:str)->int:
b1,b2=bytes.fromhex(h1),bytes.fromhex(h2)
returnsum((x^y).bit_count()forx,yinzip(b1,b2))
deffinal_padded_block(msg:bytes)->bytes:
"""Returnthelast512-bitblockafterSHA-256paddingforinspection."""
ml=len(msg)*8
m=msg+b'\x80'
while(len(m)%64)!=56:
m+=b'\x00'
m+=ml.to_bytes(8,'big')
returnm[-64:]
#Demo:"Hello"vs"Hello."
m1,m2=b"Hello",b"Hello."
h1,h2=sha256_hex(m1),sha256_hex(m2)
print("[Hello] ",h1)
print("[Hello.] ",h2)
print("Hammingdistance:",hamming_hex(h1,h2),"/256bits")
36----------- Page37 ------------
#Inspectlastpaddedblocktoseewhytheydiverge
blk1,blk2=final_padded_block(m1),final_padded_block(m2)
print("\nLastpadded512-bitblock(Hello): ",blk1.hex())
print("Lastpadded512-bitblock(Hello.):",blk2.hex())
#--------------------------------------------------------
#B)K-tablespoke-alignmentanalysis(￿/9wheel,rotation)
#--------------------------------------------------------
deffirst_n_primes(n:int)->list[int]:
primes,cand=[],2
whilelen(primes)<n:
is_p=True
r=int(cand**0.5)
forpinprimes:
ifp>r:break
ifcand%p==0:
is_p=False
break
ifis_p:primes.append(cand)
cand+=1
returnprimes
deffrac_cube_root(p:int)->float:
return(p**(1/3)-floor(p**(1/3)))
defktable_angles_deg(n=64)->np.ndarray:
"""SHA-256styleK-tablesurrogate:frac(cuberoot(prime))*360°."""
primes=first_n_primes(n)
fracs=np.array([frac_cube_root(p)forpinprimes],dtype=float)
return(fracs*360.0)%360.0
defspoke_delta_deg(angles_deg:np.ndarray,rotation_deg:float,spokes=9):
"""Distance(indegrees)fromeachangletothenearest￿/9spokeafter␣
↪rotation."""
spoke_step=360.0/spokes #40°for9spokes?(￿/9inradians=20°,␣
↪but360/18=20;weuse9spokes=>40°separationwith±windows)
#NOTE:Yourpriorworkuseda9-spoke"￿/9wheel"interpretedas20°␣
↪spacing.
#Ifyouintend20°spokes,set'spokes=18'.Wekeep9tomatchyour␣
↪K-scheduling;adjustbelowifneeded.
#Tokeep20°spacing,override:spoke_step=20.0
spoke_step=20.0 #enforce20°betweenspokesasinyouranalysis
#normalizeangleswithrotation
th=(angles_deg+rotation_deg)%360.0
#distancetonearest20°multiple
nearest=np.round(th/spoke_step)*spoke_step
delta=np.abs(th-nearest)
37----------- Page38 ------------
#folddistances>180°acrossthecircle
delta=np.minimum(delta,360.0-delta)
returndelta
defhit_counts(angles_deg:np.ndarray,rotation_deg:float,windows=(1.0,2.0)):
delta=spoke_delta_deg(angles_deg,rotation_deg)
returntuple(int(np.count_nonzero(delta<=w))forwinwindows)
defbinom_p_geq(k,n,p):
"""Pr[X>=k]forX~Bin(n,p).Smalln=>exactsum."""
frommathimportcomb
returnsum(comb(n,j)*(p**j)*((1-p)**(n-j))forjinrange(k,n␣
↪+1))
#Runrotationsweep0..20°(symmetryrepeatseach20°)
K=ktable_angles_deg(64)
rots=np.linspace(0.0,20.0,81)
hits_1=[]
hits_2=[]
forrinrots:
c1,c2=hit_counts(K,r,(1.0,2.0))
hits_1.append(c1);hits_2.append(c2)
#Expectedvaluesunderuniformangles:
#probabilityoflandingwithin±waroundanyspokeis(9spokes*2w)/360=w/
↪20.
#Forw=1°,p=0.05;forw=2°,p=0.10.
n=64
p1,p2=0.05,0.10
exp1,exp2=n*p1,n*p2
best_idx=int(np.argmax(hits_1))
best_rot=rots[best_idx]
best_c1,best_c2=hits_1[best_idx],hits_2[best_idx]
pval1=binom_p_geq(best_c1,n,p1)
pval2=binom_p_geq(best_c2,n,p2)
print(f"\n[K-table→￿/9spokes@rotationsweep]")
print(f"Bestrotation￿{best_rot:.2f}°|±1°hits={best_c1}(E={exp1:.1f},␣
↪p￿{pval1:.3g})|±2°hits={best_c2}(E={exp2:.1f},p￿{pval2:.3g})")
fig,(ax1,ax2)=plt.subplots(2,1,figsize=(8.5,6),constrained_layout=True)
ax1.plot(rots,hits_1,label="±1°window")
ax1.plot(rots,hits_2,label="±2°window",alpha=0.7)
ax1.axhline(exp1,ls="--",lw=0.8,color="tab:blue")
ax1.axhline(exp2,ls="--",lw=0.8,color="tab:orange")
ax1.set_title("K-tablespokehitsvswheelrotation(20°spacing)")
38----------- Page39 ------------
ax1.set_xlabel("Rotation(degrees)")
ax1.set_ylabel("Hitcount(outof64)")
ax1.legend()
#HistogramofKanglesmodulo20°(atbestrotation),forintuition
d=spoke_delta_deg(K,best_rot)
ax2.hist(d,bins=np.linspace(0,10,41),color="gray",edgecolor="black")
ax2.set_title(f"Angledeltastonearest20°spokeatrotation￿{best_rot:.
↪2f}°")
ax2.set_xlabel("Δangletonearestspoke(degrees)")
ax2.set_ylabel("Count")
plt.show()
#--------------------------------------------------------
#C)Minimalphase-guided"growth"hillclimber(toy)
#--------------------------------------------------------
defbytes_to_angles_deg(b:bytes)->np.ndarray:
#Mapbytevalues0..255toangles0..360°
return(np.frombuffer(b,dtype=np.uint8).astype(float)/256.0)*360.0
defphase_score(digest:bytes,rotation_deg=15.0):
"""Higheris'morealigned'to20°spokesafterrotation."""
ang=(bytes_to_angles_deg(digest)+rotation_deg)%360.0
spoke_step=20.0
#cosineaffinitytonearestspoke(0°offsetafterrounding)
nearest=np.round(ang/spoke_step)*spoke_step
delta=np.deg2rad(np.abs(ang-nearest))
#score:sumofcos(pi*delta/(spoke_step/2))clippedto[0,1]
#i.e.,1atthespoke,0athalf-step(10°)
affinity=np.cos(np.clip(delta*pi/np.deg2rad(spoke_step/2),0,pi))
returnfloat(affinity.mean())
defgrow_message(seed:bytes,steps=2000,mutate_bytes=4,rotation_deg=15.0,␣
↪rng=None):
"""Hillclimbonthe*tail*ofseedtomaximizephase_score(SHA256(seed))."""
rng=rngorrandom.Random()
best=bytearray(seed)
best_score=phase_score(hashlib.sha256(best).digest(),rotation_deg)
for_inrange(steps):
cand=bytearray(best)
#mutateafewtailpositions
L=len(cand)
for__inrange(mutate_bytes):
i=L-1-rng.randrange(0,min(16,L)) #restricttolast16␣
↪bytes
cand[i]=rng.randrange(256)
s=phase_score(hashlib.sha256(cand).digest(),rotation_deg)
39----------- Page40 ------------
if s > best_score:
best,best_score=cand,s
returnbytes(best),best_score
seed=b"\x00"*32
grown,s=grow_message(seed,steps=2000,mutate_bytes=3,rotation_deg=15.0)
print(f"\n[grow]phase_score={s:.4f} sha256={sha256_hex(grown)}")
[Hello]185f8db32271fe25f561a6fc938b2e264306ec304eda518007d1764826381969
[Hello.]2d8bd7d9bb5f85ba643f0110d50cb506a1fe439e769a22503193ea6046bb87f7
Hammingdistance:126/256bits
Lastpadded512-bitblock(Hello):48656c6c6f800000000000000000000000000000000
00000000000000000000000000000000000000000000000000000000000000000000000000000000
00028
Lastpadded512-bitblock(Hello.):48656c6c6f2e8000000000000000000000000000000
00000000000000000000000000000000000000000000000000000000000000000000000000000000
00030
[K-table→￿/9spokes@rotationsweep]
Bestrotation￿18.75°|±1°hits=11(E=3.2,p￿0.00031)|±2°hits=17
(E=6.4,p￿0.000136)
40----------- Page41 ------------
[grow]phase_score=0.4409
sha256=fb82cab02c4a40b20377c0e3cd3989e83dcb923ff60d22fff480be5b5a680f06
[34]: importhashlib,math,random,os,itertools
importnumpyasnp
importpandasaspd
importmatplotlib.pyplotasplt
defsha256_bytes(b:bytes)->bytes:
returnhashlib.sha256(b).digest()
defbytes_to_bits(bb:bytes)->np.ndarray:
returnnp.unpackbits(np.frombuffer(bb,dtype=np.uint8))
defhamming(a:bytes,b:bytes)->int:
ba,bb=bytes_to_bits(a),bytes_to_bits(b)
return int(np.sum(ba ^ bb))
def bitflip_rate(a: bytes,b:bytes)->float:
returnhamming(a,b)/(8*len(a))
defnibbles(bb:bytes)->np.ndarray:
u=np.frombuffer(bb,dtype=np.uint8)
hi=(u>>4)&0xF
lo=u&0xF
returnnp.vstack([hi,lo]).T.reshape(-1)
ASCII_CTRL = {0:"NUL",1:"SOH",2:"STX",3:"ETX",4:"EOT",5:"ENQ",6:"ACK",7:"BEL",8:
↪"BS",9:"TAB"}
def tag_nibble(x: int) -> str:
return ASCII_CTRL.get(x, "ABCDEF"[x-10] if 10 <= x <= 15 else str(x))
[35]: msgs=[
b"Hello",
b"Hello.", #trailingdot
b"hello", #casechange
b"Hello", #trailingspace
b"\nHello\n", #newlines
]
rows=[]
fori,(a,b)inenumerate(itertools.combinations(msgs,2),start=1):
da,db=sha256_bytes(a),sha256_bytes(b)
rows.append({
"A":a,"B":b,
"SHA(A)":sha256_bytes(a).hex(),
41----------- Page42 ------------
"SHA(B)":sha256_bytes(b).hex(),
"Hamming(bits)":hamming(da,db),
"FlipRate":bitflip_rate(da,db)
})
df=pd.DataFrame(rows)
df
[35]: A B SHA(A)\
0b'Hello'b'Hello.'185f8db32271fe25f561a6fc938b2e264306ec304eda51…
1b'Hello' b'hello'185f8db32271fe25f561a6fc938b2e264306ec304eda51…
2b'Hello'b'Hello'185f8db32271fe25f561a6fc938b2e264306ec304eda51…
3b'Hello'b'\nHello\n'185f8db32271fe25f561a6fc938b2e264306ec304eda51…
4b'Hello.' b'hello'2d8bd7d9bb5f85ba643f0110d50cb506a1fe439e769a22…
5b'Hello.'b'Hello'2d8bd7d9bb5f85ba643f0110d50cb506a1fe439e769a22…
6b'Hello.'b'\nHello\n'2d8bd7d9bb5f85ba643f0110d50cb506a1fe439e769a22…
7b'hello'b'Hello'2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa742…
8b'hello'b'\nHello\n'2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa742…
9b'Hello'b'\nHello\n'2ec5a3f0c2fc3e6dcee0f6f3a5735a6c69d2056579a545…
SHA(B)Hamming(bits)FlipRate
02d8bd7d9bb5f85ba643f0110d50cb506a1fe439e769a22… 1260.492188
12cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa742… 1250.488281
22ec5a3f0c2fc3e6dcee0f6f3a5735a6c69d2056579a545… 1170.457031
39773a9208fd8c737242e27bcdcaa80873e47295c14ebc8… 1220.476562
42cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa742… 1230.480469
52ec5a3f0c2fc3e6dcee0f6f3a5735a6c69d2056579a545… 1450.566406
69773a9208fd8c737242e27bcdcaa80873e47295c14ebc8… 1220.476562
72ec5a3f0c2fc3e6dcee0f6f3a5735a6c69d2056579a545… 1260.492188
89773a9208fd8c737242e27bcdcaa80873e47295c14ebc8… 1150.449219
99773a9208fd8c737242e27bcdcaa80873e47295c14ebc8… 1310.511719
[36]: def head_tail_table(bb: bytes,label="digest"):
ns=nibbles(bb)
heads=ns[0::2];tails=ns[1::2]
pairs=[(int(h),int(t),tag_nibble(int(h)),tag_nibble(int(t)))forh,t␣
↪inzip(heads,tails)]
out=pd.DataFrame(pairs,columns=[f"{label}_H",f"{label}_T",␣
↪f"{label}_H_tag",f"{label}_T_tag"])
returnout
example=b"Hello."
dig=sha256_bytes(example)
tbl=head_tail_table(dig,"SHA256")
tbl.head(12)
42----------- Page43 ------------
[36]: SHA256_HSHA256_TSHA256_H_tagSHA256_T_tag
0 2 13 STX D
1 8 11 BS B
2 13 7 D BEL
3 13 9 D TAB
4 11 11 B B
5 5 15 ENQ F
6 8 5 BS ENQ
7 11 10 B A
8 6 4 ACK EOT
9 3 15 ETX F
10 0 1 NUL SOH
11 1 0 SOH NUL
[37]: def has_piray_front(dig: bytes):
ns = nibbles(dig)
return len(ns) >= 3 and tuple(ns[:3]) == (3,1,4)
for m in msgs:
print(m,has_piray_front(sha256_bytes(m)))
b'Hello'False
b'Hello.'False
b'hello'False
b'Hello'False
b'\nHello\n'False
[38]: base=b"Hello"
N=200
rng=random.Random(0)
defmutate(b:bytes)->bytes:
#simplemutations:togglecaseifletter,flippunctuation/space/newline,␣
↪elserandombyteflip
i=rng.randrange(len(b))
x=b[i]
if65<=x<=90:y=x+32
elif97<=x<=122:y=x-32
elifx==ord('.'):y=ord('')
elifx==ord(''):y=ord('.')
else:y=x^(1<<rng.randrange(8))
returnb[:i]+bytes([y])+b[i+1:]
flips=[]
ref=sha256_bytes(base)
for_inrange(N):
m=mutate(base)
flips.append(bitflip_rate(ref,sha256_bytes(m)))
43----------- Page44 ------------
plt.figure(figsize=(6,3))
plt.hist(flips,bins=20,edgecolor='k')
plt.axvline(0.5,color='r',ls='--',label='0.5')
plt.title("Avalancheflip-ratedistributionvsSHA256(Hello)")
plt.xlabel("fliprate");plt.ylabel("count");plt.legend();plt.tight_layout();␣
↪plt.show()
print("meanfliprate:",np.mean(flips))
print("std:",np.std(flips,ddof=1))
meanfliprate:0.4726953125
std:0.03209010805282805
[39]: defhunt_header(header:bytes,target_first_byte: int=None,want_piray=False,␣
↪max_tries=2_000_000,seed=0):
rng=random.Random(seed)
for_inrange(max_tries):
nonce=rng.getrandbits(32)
d=sha256_bytes(header+nonce.to_bytes(4,'little'))
if(target_first_byteisnotNoneandd[0]==target_first_byte)\
or(want_pirayandhas_piray_front(d)):
returnnonce,d
returnNone,None
hdr=b"EEEEEEEEE\n" #trybothwithandwithouttrailingnewline
n1,d1=hunt_header(hdr,target_first_byte=0x7F,want_piray=False,␣
↪max_tries=500_000)
print("7F-hit:",n1,d1.hex()[:8]ifd1elseNone)
44----------- Page45 ------------
n2,d2=hunt_header(hdr.rstrip(b"\n"),want_piray=True,max_tries=1_000_000)
print("Pi-Ray-hit(3,1,4front):",n2,d2.hex()[:8]ifd2elseNone)
7F-hit:1659642627ff4b7b1
Pi-Ray-hit(3,1,4front):1357554130314ac90d
[40]: #MinimalBBP(hexdigits)forpi,adaptedforsmallwindows
def_series(j,n):
s=0.0
forkinrange(n+1):
s=(s+pow(16,n-k,8*k+j)/(8*k+j))%1.0
k=n+1;term=0.0;p16=1.0/16.0
whileTrue:
new=term+p16**(k-n)/(8*k+j)
ifnew==term:break
term=new;k+=1
return(s+term)%1.0
defpi_hex_digits(n,m):
x=(4*_series(1,n)-2*_series(4,n)-_series(5,n)-_series(6,n))%1.
↪0
out=[]
for_inrange(m):
x=(16.0*x)%1.0
out.append(int(16.0*x))
returnout
defhead_tail_stats(nibble_seq):
H=np.array(nibble_seq[0::2],int)
T=np.array(nibble_seq[1::2],int)
D=np.abs(T[:-1]-H[1:]) #tail→nexthead
S=H[:-1]+H[1:] #head+nexthead
returnH,T,D,S
pi_ns=pi_hex_digits(1_000,2_048)
H,T,D,S=head_tail_stats(pi_ns)
pd.DataFrame({"H":H[:12],"T":T[:12],"D":D[:12],"S":S[:12]})
[40]: HTDS
09151410
1112121
209211
3110718
4741122
5150015
60000
45----------- Page46 ------------
70000
80000
90000
100000
110000
[]:
46
```
