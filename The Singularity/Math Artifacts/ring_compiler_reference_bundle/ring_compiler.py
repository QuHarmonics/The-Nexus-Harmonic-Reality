"""Small reference compiler for the fixed original ring cycles.
Source: the ring DSL below. Target: guarded Python with XOR/AND Boolean cores.
Fold is a source-representation normalization pass, not a lossy runtime opcode.
"""
import re,json
from collections import Counter

MAX_WIDTH=12
class SourceError(ValueError):pass
class GrammarError(SourceError):pass
class FoldError(SourceError):pass
class ResourceLimit(RuntimeError):pass

def partner(x,n):
 r=int(format(x,f'0{n}b')[::-1],2)
 return r if r!=x else x^((1<<n)-1)

def original_cycle(n):
 reps=[x for x in range(1<<n) if x<partner(x,n)]
 seq=reps+[partner(x,n) for x in reversed(reps)]
 if n>1:
  M=len(reps);seq[M-1],seq[M]=seq[M],seq[M-1]
 return seq

def normalize_fold(root,references,n):
 if len(root)>1 and len(root)%2==0:raise FoldError('root is not a terminal equal-half residual')
 current=root;trace=[]
 for index,A in enumerate(references):
  if len(A)!=len(current):raise FoldError('reference '+str(index)+' must have '+str(len(current))+' bits, got '+str(len(A)))
  old=current;lower=''.join(str(int(a)^int(b)) for a,b in zip(A,current))[::-1];current=A+lower
  trace.append({'reference':A,'residual':old,'reconstructed':current})
 expected=n*(1<<n)
 if len(current)!=expected:raise FoldError('unfolded tape must have '+str(expected)+' bits, got '+str(len(current)))
 return [current[j:j+n] for j in range(0,len(current),n)],trace

def parse(text):
 outer=re.fullmatch(r'\s*ring\s+([A-Za-z_][A-Za-z_0-9]*)\s+width\s+([0-9]+)\s*\{(.*)\}\s*',text,re.S)
 if not outer:raise GrammarError('expected ring NAME width INTEGER { description }')
 name=outer[1];n=int(outer[2]);body=outer[3].strip()
 if n<1:raise SourceError('width must be positive')
 if n>MAX_WIDTH:raise ResourceLimit('reference implementation width cap is '+str(MAX_WIDTH))
 cycle=re.fullmatch(r'cycle\s*:\s*([01]+(?:\s*->\s*[01]+)*)\s*;',body,re.S)
 fold=re.fullmatch(r'fold\s*\{\s*root\s*:\s*([01]+)\s*;\s*refs_inner_to_outer\s*:\s*\[\s*([01]+(?:\s*,\s*[01]+)*)?\s*\]\s*;\s*\}',body,re.S)
 if cycle:
  words=re.split(r'\s*->\s*',cycle[1]);trace={'representation':'literal_cycle','unfold_steps':[]}
 elif fold:
  refs=re.findall(r'[01]+',fold[2]) if fold[2] else []
  words,steps=normalize_fold(fold[1],refs,n);trace={'representation':'fold_packet','root':fold[1],'references_inner_to_outer':refs,'unfold_steps':steps}
 else:raise GrammarError('description must be a binary cycle or a fold packet')
 if any(len(w)!=n for w in words):raise SourceError('every state must contain exactly '+str(n)+' bits')
 values=[int(w,2) for w in words]
 if len(values)!=1<<n:raise SourceError('expected exactly '+str(1<<n)+' state entries')
 if len(set(values))!=1<<n:raise SourceError('duplicate or missing state')
 # The language denotes the fixed original ordering, not an arbitrary cyclic permutation.
 reps=sorted({min(x,partner(x,n)) for x in values});expected=reps+[partner(x,n) for x in reversed(reps)]
 if n>1:
  M=len(reps);expected[M-1],expected[M]=expected[M],expected[M-1]
 if values!=expected:raise SourceError('cycle differs from the original ring ordering or center swap')
 return name,n,values,trace

def anf(table,n,output_bit):
 a=[(table[x]>>output_bit)&1 for x in range(1<<n)]
 for k in range(n):
  for x in range(1<<n):
   if x>>k&1:a[x]^=a[x^(1<<k)]
 return [mask for mask,value in enumerate(a) if value]

def lower(name,n,cycle):
 forward=[0]*(1<<n);inverse=[0]*(1<<n)
 for i,x in enumerate(cycle):
  y=cycle[(i+1)%len(cycle)];forward[x]=y;inverse[y]=x
 return {'format':'ring-compiler-ir-v1','name':name,'width':n,'state_encoding':'unsigned integer; source words MSB first','cycle':cycle,'successor_by_state':forward,'predecessor_by_state':inverse,'partner_by_state':[partner(x,n) for x in range(1<<n)],'anf':{'mask_semantics':'mask 0 is constant 1; mask bit k selects input bit k from LSB','output_order':'MSB first','forward':[anf(forward,n,b) for b in range(n-1,-1,-1)],'inverse':[anf(inverse,n,b) for b in range(n-1,-1,-1)]}}

def emit(ir):
 n=ir['width'];names='abcdefghijkl'[:n]
 text='"""Generated ring runtime; Boolean arithmetic is XOR and AND."""\n\ndef _check_state(x, width):\n    if type(x) is not int:\n        raise TypeError("state must be a Python integer")\n    if not 0 <= x < (1 << width):\n        raise ValueError("state outside runtime width")\n\n'
 for direction in ('forward','inverse'):
  outputs=ir['anf'][direction];nonlinear=sorted({m for terms in outputs for m in terms if m.bit_count()>1},key=lambda x:(x.bit_count(),x));gates={m:'g'+str(i) for i,m in enumerate(nonlinear)}
  def term(m):
   if m==0:return '1'
   if m in gates:return gates[m]
   return names[n-1-(m.bit_length()-1)]
  text+='def '+ir['name']+'_'+direction+'(x):\n    _check_state(x, '+str(n)+')\n'
  for j,v in enumerate(names):text+='    '+v+' = (x >> '+str(n-1-j)+') & 1\n'
  for mask,g in gates.items():text+='    '+g+' = '+' & '.join(names[j] for j in range(n) if mask>>(n-1-j)&1)+'\n'
  for j,terms in enumerate(outputs):text+='    y'+str(j)+' = '+(' ^ '.join(term(m) for m in terms) if terms else '0')+'\n'
  text+='    return '+' | '.join('(y'+str(j)+' << '+str(n-1-j)+')' for j in range(n))+'\n\n'
 return text

def compile_source(text):
 name,n,cycle,trace=parse(text);ir=lower(name,n,cycle)
 return ir,emit(ir),trace

def make_fold_source(name,n,cycle):
 current=''.join(format(x,f'0{n}b') for x in cycle);references=[]
 while len(current)>1 and len(current)%2==0:
  h=len(current)//2;A=current[:h];D=''.join(str(int(a)^int(b)) for a,b in zip(A,current[h:][::-1]));references.append(A);current=D
 refs=', '.join(reversed(references))
 return 'ring '+name+' width '+str(n)+' { fold { root: '+current+'; refs_inner_to_outer: ['+refs+']; } }'
