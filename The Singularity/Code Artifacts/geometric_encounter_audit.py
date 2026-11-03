import json,csv,collections
A="26537e8b759579d1b94e63b65e65c33f8b93d0f4b16f450810230357f1f0fabe"
S=range(1024)
def T(x):
 p,r=divmod(x,16);o=int(A[p],16)
 if o<4:r=(r+o+1)%16
 elif o<8:r^=o&3
 return ((p+1+(int(A[r],16)&3))%64)*16+r
def G(x):
 p,r=divmod(x,16);return ((p+1)%64)*16+r
def partition_permutation(fn):
 labels=[-1]*1024;phase=[-1]*1024;orbits=[]
 for x in S:
  if labels[x]>=0:continue
  orb=[];y=x
  while labels[y]<0:
   labels[y]=len(orbits);phase[y]=len(orb);orb.append(y);y=fn(y)
  assert y==x;orbits.append(orb)
 return labels,phase,orbits
assert len(set(map(T,S)))==len(set(map(G,S)))==1024
lab,phase,orb=partition_permutation(T)
counts=[[0]*5 for _ in range(5)]
for x in S:counts[lab[x]][lab[G(x)]]+=1
witness=None
for o in orb:
 x=o[0]
 for y in o[1:]:
  if lab[G(x)]!=lab[G(y)]:
   witness={'x':divmod(x,16),'y':divmod(y,16),'phase_x':phase[x],'phase_y':phase[y],'class':lab[x],'Gx':divmod(G(x),16),'Gy':divmod(G(y),16),'class_Gx':lab[G(x)],'class_Gy':lab[G(y)]};break
 if witness:break
parent=list(S)
def root(x):
 while parent[x]!=x:parent[x]=parent[parent[x]];x=parent[x]
 return x
for x in S:
 for y in [T(x),G(x)]:
  a,b=root(x),root(y)
  if a!=b:parent[b]=a
components=list(collections.Counter(root(x) for x in S).values())
b=lab[:];history=[5]
while True:
 ids={};new=[]
 for x in S:
  sig=(b[x],b[T(x)],b[G(x)])
  if sig not in ids:ids[sig]=len(ids)
  new.append(ids[sig])
 if len(ids)==history[-1]:b=new;break
 b=new;history.append(len(ids))
with open('output/geometric_encounter_states.csv','w',newline='') as f:
 w=csv.writer(f);w.writerow(['state','p','r','T_state','G_state','T_orbit','T_phase','G_target_orbit','predictive_class'])
 for x in S:w.writerow([x,*divmod(x,16),T(x),G(x),lab[x],phase[x],lab[G(x)],b[x]])
with open('output/exact_T_orbit_partition.json','w') as f:
 json.dump({'encoding':'x=16*p+r','blocks':[{'class':i,'size':len(o),'states_in_phase_order':o} for i,o in enumerate(orb)]},f,indent=2)
result={'operation':'G(p,r)=((p+1)%64,r)','T_cycle_sizes':list(map(len,orb)),'G_cycle_sizes':list(map(len,partition_permutation(G)[2])),'matrix':counts,'preserved':sum(counts[i][i] for i in range(5)),'changed':1024-sum(counts[i][i] for i in range(5)),'witness':witness,'joint_components':components,'predictive_partition_sizes':history,'G_quotient_map_exists':all(sum(v>0 for v in row)==1 for row in counts),'T_quotient_is_identity':all(lab[T(x)]==lab[x] for x in S),'T_and_G_are_permutations':True}
with open('output/geometric_encounter_results.json','w') as f:json.dump(result,f,indent=2)
print(json.dumps(result,indent=2))
