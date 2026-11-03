---
title: "The Nesus 4 Framework - Stiheatmap"
source_pdf: "The Nesus 4 Framework - Stiheatmap.pdf"
created_utc: "2025-11-27T11:10:03.8219058Z"
page_count: 23
---

# The Nesus 4 Framework - Stiheatmap

## Extracted Text

```text
----------- Page1 ------------
Untitled8
June24,2025
[1]: import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import uniform_filter
#Parameters
grid_size=64 #Spatialgridresolution
time_steps=100 #Numberoftimestepstosimulate
delta_t=0.01 #Timeincrement
viscosity=0.1 #Fluidviscosity
jacobi_iterations=20 #PressurePoissonsolveriterations
stability_threshold=0.7#STIthresholdforinstability
base_alpha=0.35 #Baseharmonicfoldgain
#Initializesymbolicgenomevelocityfield(Psi):shape(grid_size,grid_size,␣
↪2)
Psi=np.random.randn(grid_size,grid_size,2)*0.1
#PreviousdeltaforSTIcalculation
prev_delta=np.zeros_like(Psi)
defddx(f):
return(np.roll(f,-1,axis=1)-np.roll(f,1,axis=1))/2
defddy(f):
return(np.roll(f,-1,axis=0)-np.roll(f,1,axis=0))/2
defnavier_stokes_update_full(Psi,delta_t,viscosity=0.1,iterations=20):
u=Psi[...,0]
v=Psi[...,1]
#Nonlinearadvection
u_x=ddx(u)
u_y=ddy(u)
v_x=ddx(v)
v_y=ddy(v)
adv_u=u*u_x+v*u_y
adv_v=u*v_x+v*v_y
1----------- Page2 ------------
#Diffusion(viscousterm)
laplace_u=(np.roll(u,1,axis=0)+np.roll(u,-1,axis=0)+
np.roll(u,1,axis=1)+np.roll(u,-1,axis=1)-4*u)
laplace_v=(np.roll(v,1,axis=0)+np.roll(v,-1,axis=0)+
np.roll(v,1,axis=1)+np.roll(v,-1,axis=1)-4*v)
u_new=u+delta_t*(viscosity*laplace_u-adv_u)
v_new=v+delta_t*(viscosity*laplace_v-adv_v)
#Pressureprojectiontoenforceincompressibility
div=ddx(u_new)+ddy(v_new)
p=np.zeros_like(u_new)
for_inrange(iterations):
p=(np.roll(p,1,axis=0)+np.roll(p,-1,axis=0)+
np.roll(p,1,axis=1)+np.roll(p,-1,axis=1)-div)/4
u_proj=u_new-delta_t*ddx(p)
v_proj=v_new-delta_t*ddy(p)
returnnp.stack([u_proj,v_proj],axis=-1)
defsymbolic_trust_index(delta,prev_delta):
drift=np.linalg.norm(delta-prev_delta,axis=2)
max_drift=np.max(drift)ifnp.max(drift)>0else1.0
sti=1-drift/max_drift
returnsti
defplot_sti_heatmap(sti,step):
plt.figure(figsize=(6,5))
plt.imshow(sti,cmap='inferno',vmin=0,vmax=1)
plt.colorbar(label='SymbolicTrustIndex(STI)')
plt.title(f'STIHeatmapatStep{step}')
plt.xlabel('X')
plt.ylabel('Y')
plt.tight_layout()
plt.show()
defmulti_scale_fold(Psi,delta,sti,base_alpha=0.35):
fromscipy.ndimageimportuniform_filter
scales=[1,2,4,8]
Psi_corrected=Psi.copy()
forscaleinscales:
#Aggregatedeltaandstiatcurrentscale
delta_avg=uniform_filter(delta,size=scale,mode='reflect')[::scale,:
↪:scale,:]
2----------- Page3 ------------
sti_avg = uniform_filter(sti,size=scale,mode='reflect')[::scale,::
↪scale]
gain=base_alpha*(1+1.5*(1-sti_avg))
gain=np.clip(gain,0,1)[...,None]
correction=-gain*delta_avg
#Broadcastcorrectionbacktofullgrid
correction_full=np.repeat(np.repeat(correction,scale,axis=0),␣
↪scale,axis=1)
Psi_corrected+=correction_full[:Psi.shape[0],:Psi.shape[1],:]
returnPsi_corrected
#Mainsimulationloop
fortinrange(time_steps):
Psi_new=navier_stokes_update_full(Psi,delta_t,viscosity,␣
↪jacobi_iterations)
delta=Psi_new-Psi
sti=symbolic_trust_index(delta,prev_delta)
unstable_mask=sti<stability_threshold
delta_corrected=np.where(unstable_mask[...,None],delta,0)
Psi_new=multi_scale_fold(Psi_new,delta_corrected,sti,base_alpha)
prev_delta=delta
Psi=Psi_new
ift%5==0:
avg_sti=np.mean(sti)
print(f"Step{t}:AvgSTI={avg_sti:.4f}")
plot_sti_heatmap(sti,t)
Step0:AvgSTI=0.7499
3----------- Page4 ------------
Step5:AvgSTI=0.7022
4----------- Page5 ------------
Step10:AvgSTI=0.8014
5----------- Page6 ------------
Step15:AvgSTI=0.7417
6----------- Page7 ------------
Step20:AvgSTI=0.8006
7----------- Page8 ------------
Step25:AvgSTI=0.7410
8----------- Page9 ------------
Step30:AvgSTI=0.8024
9----------- Page10 ------------
Step35:AvgSTI=0.7396
10----------- Page11 ------------
Step40:AvgSTI=0.8039
11----------- Page12 ------------
Step45:AvgSTI=0.7383
12----------- Page13 ------------
Step50:AvgSTI=0.8057
13----------- Page14 ------------
Step55:AvgSTI=0.7366
14----------- Page15 ------------
Step60:AvgSTI=0.8070
15----------- Page16 ------------
Step65:AvgSTI=0.7359
16----------- Page17 ------------
Step70:AvgSTI=0.8075
17----------- Page18 ------------
Step75:AvgSTI=0.7357
18----------- Page19 ------------
Step80:AvgSTI=0.8097
19----------- Page20 ------------
Step85:AvgSTI=0.7345
20----------- Page21 ------------
Step90:AvgSTI=0.8111
21----------- Page22 ------------
Step95:AvgSTI=0.7343
22----------- Page23 ------------
[]:
23
```
