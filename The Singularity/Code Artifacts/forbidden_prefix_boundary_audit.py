import ast,json
from fractions import Fraction as F
nb=json.load(open('nested_rings-3.ipynb'))
s=next(''.join(c['source']) for c in nb['cells'] if c['cell_type']=='code')
a=ast.parse(s)
exec(compile(ast.Module(body=[n for n in a.body if isinstance(n,ast.FunctionDef) and n.name in ('partner','grow')],type_ignores=[]),'growth','exec'))
segments=[(F(0),F(1),'')];forbidden=[]
for L in range(1,11):
 bits=''.join(grow(L));N=len(bits);runs=[];start=0
 for j in range(1,N+1):
  if j==N or bits[j]!=bits[start]:
   runs.append((F(start,N),F(j,N),bits[start]));start=j
 nxt=[];i=j=0
 while i<len(segments) and j<len(runs):
  a,b,p=segments[i];c,d,v=runs[j];lo=max(a,c);hi=min(b,d)
  if lo<hi:
   if nxt and nxt[-1][2]==p+v and nxt[-1][1]==lo:nxt[-1]=(nxt[-1][0],hi,p+v)
   else:nxt.append((lo,hi,p+v))
  if b<=d:i+=1
  if d<=b:j+=1
 old={p for a,b,p in segments};new={p for a,b,p in nxt}
 forbidden.extend(sorted(p+v for p in old for v in '01' if p+v not in new))
 segments=nxt
 print(L,len(new))
assert len(forbidden)==32
assert sum(2**(10-len(p)) for p in forbidden)==100
assert len({p for a,b,p in segments})==924
print('Minimal forbidden prefixes:',forbidden)
