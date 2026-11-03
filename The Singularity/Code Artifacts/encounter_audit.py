import json,csv,collections,os
A="26537e8b759579d1b94e63b65e65c33f8b93d0f4b16f450810230357f1f0fabe"
S=list(range(1024))
def T(x):
    p,r=divmod(x,16);o=int(A[p],16)
    if o<4:r=(r+o+1)%16
    elif o<8:r^=o&3
    return ((p+1+(int(A[r],16)&3))%64)*16+r
def J(x):
    p,r=divmod(x,16)
    return p*16+(r+1)%16
assert len(set(map(T,S)))==1024 and len(set(map(J,S)))==1024
labels=[-1]*1024;phase=[-1]*1024;orbits=[]
for x in S:
    if labels[x]>=0:continue
    orb=[];y=x
    while labels[y]<0:
        labels[y]=len(orbits);phase[y]=len(orb);orb.append(y);y=T(y)
    assert y==x
    orbits.append(orb)
counts=[[0]*len(orbits) for _ in orbits]
for x in S:counts[labels[x]][labels[J(x)]]+=1
preserved=sum(labels[J(x)]==labels[x] for x in S)
quotient=all(sum(v>0 for v in row)==1 for row in counts)
witness=None
for orb in orbits:
    x=orb[0]
    for y in orb[1:]:
        if labels[J(x)]!=labels[J(y)]:
            witness={'x':list(divmod(x,16)),'y':list(divmod(y,16)),
                'source_class':labels[x],'phase_x':phase[x],'phase_y':phase[y],
                'Jx':list(divmod(J(x),16)),'Jy':list(divmod(J(y),16)),
                'target_class_x':labels[J(x)],'target_class_y':labels[J(y)]}
            break
    if witness:break
parent=list(S)
def root(x):
    while parent[x]!=x:
        parent[x]=parent[parent[x]];x=parent[x]
    return x
def union(x,y):
    a,b=root(x),root(y)
    if a!=b:parent[b]=a
for x in S:
    union(x,T(x));union(x,J(x))
components=sorted(collections.Counter(root(x) for x in S).values())
b=labels[:];history=[len(set(b))]
while True:
    ids={};new=[]
    for x in S:
        sig=(b[x],b[T(x)],b[J(x)])
        if sig not in ids:ids[sig]=len(ids)
        new.append(ids[sig])
    n=len(ids)
    if n==history[-1]:
        b=new;break
    history.append(n);b=new
for fn in [T,J]:
    targets={}
    for x in S:
        old=targets.setdefault(b[x],b[fn(x)])
        assert old==b[fn(x)]
with open('output/encounter_transition_table.csv','w',newline='') as f:
    w=csv.writer(f);w.writerow(['state','p','r','T_state','J_state','orbit','phase','J_orbit','predictive_class'])
    for x in S:w.writerow([x,*divmod(x,16),T(x),J(x),labels[x],phase[x],labels[J(x)],b[x]])
result={'address':A,'state_encoding':'state=16*p+r; orbit labels ordered by least encoded state',
    'orbit_sizes':list(map(len,orbits)),'T_fixed_states':sum(T(x)==x for x in S),
    'J_identity_preserved_states':preserved,'J_identity_changed_states':1024-preserved,
    'J_preserves_identity_everywhere':preserved==1024,'J_induces_map_on_orbit_classes':quotient,
    'J_destination_count_matrix':counts,'witness':witness,'common_invariant_component_sizes':components,
    'predictive_partition_sizes':history,'final_predictive_partition_size':len(set(b)),
    'definition_predictive':'Coarsest refinement of original orbit partition stable under both T and J; iteration includes current labels and successor labels.'}
with open('output/encounter_results.json','w') as f:json.dump(result,f,indent=2)
print(json.dumps(result,indent=2))
