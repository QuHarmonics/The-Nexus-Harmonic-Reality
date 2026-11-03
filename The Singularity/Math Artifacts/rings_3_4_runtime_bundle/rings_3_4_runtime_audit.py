import ast,json,csv,time

def read(tape,phase,length,direction=1):return ''.join(tape[(phase+direction*k)%len(tape)] for k in range(length))
def reverse_word(x,n):return int(format(x,f'0{n}b')[::-1],2)
def anf_coeff(table,output_bit,n):
 coeff=[(table[x]>>output_bit)&1 for x in range(1<<n)]
 for k in range(n):
  for x in range(1<<n):
   if (x>>k)&1:coeff[x]^=coeff[x^(1<<k)]
 return coeff

def expression(coeff,n):
 names='abcd'[:n];terms=[]
 for mask in sorted(range(1<<n),key=lambda x:(x.bit_count(),x)):
  if coeff[mask]:
   factors=[names[j] for j in range(n) if mask>>(n-1-j)&1]
   terms.append(''.join(factors) if factors else '1')
 return ' XOR '.join(terms) if terms else '0'

def apply_anf(x,coeffs,n):
 out=0
 for j,coeff in enumerate(coeffs):
  value=0
  for mask,c in enumerate(coeff):
   if c and x&mask==mask:value^=1
  out|=value<<(n-1-j)
 return out

def run():
 start=time.perf_counter();original={};tree=ast.parse(open('pairs_forced.py').read())
 exec(compile(ast.Module(body=[n for n in tree.body if isinstance(n,ast.FunctionDef) and n.name in ('partner','grow')],type_ignores=[]),'original','exec'),original)
 results=[];phase_rows=[]
 for n in (2,3,4):
  words=original['grow'](n);states=[int(w,2) for w in words];N=len(words);tape=''.join(words);B=len(tape)
  fwd={states[j]:states[(j+1)%N] for j in range(N)};inv={y:x for x,y in fwd.items()};P={x:int(original['partner'](format(x,f'0{n}b')),2) for x in states}
  fp=[anf_coeff(fwd,b,n) for b in range(n-1,-1,-1)];ip=[anf_coeff(inv,b,n) for b in range(n-1,-1,-1)];pp=[anf_coeff(P,b,n) for b in range(n-1,-1,-1)]
  for x in states:
   assert apply_anf(x,fp,n)==fwd[x] and apply_anf(x,ip,n)==inv[x] and apply_anf(x,pp,n)==P[x]
   assert inv[fwd[x]]==x and P[fwd[P[x]]]==inv[x]
   y=x;visited=[]
   for _ in range(N):visited.append(y);y=fwd[y]
   assert y==x and len(set(visited))==N
  pal_words=[w==w[::-1] for w in words];mask=''.join(('1' if pal else '0')*n for pal in pal_words)
  whole_reverse=tape[::-1];xor_reverse=''.join(str(int(a)^int(b)) for a,b in zip(tape,mask));assert whole_reverse==xor_reverse
  shifts=[k for k in range(B) if read(tape,k,B)==whole_reverse]
  axes=[k for k in range(B) if all(tape[j]==tape[(k-j)%B] for j in range(B))]
  correction_checks=0
  for L in range(1,2*B+1):
   for phase in range(B):
    q=(B-1-phase)%B
    predicted=''.join(str(int(a)^int(b)) for a,b in zip(read(tape,q,L),read(mask,q,L)))
    assert read(tape,phase,L,-1)==predicted;correction_checks+=1
  for k,x in enumerate(states):
   phase=(n*k+n-1)%B;y=int(read(tape,phase,n,-1),2)
   assert y==reverse_word(x,n)
   y_next=int(read(tape,phase-n,n,-1),2)
   assert y_next==reverse_word(inv[reverse_word(y,n)],n)
  frames=[]
  for frame in range(n):
   observed=[int(read(tape,frame+n*k,n),2) for k in range(N)];successors={}
   for k,x in enumerate(observed):successors.setdefault(x,set()).add(observed[(k+1)%N])
   frames.append({'frame':frame,'distinct_word_states':len(set(observed)),'full_state_cycle':len(set(observed))==N,'ambiguous_state_successors':sum(len(v)>1 for v in successors.values())})
  for phase in range(B):phase_rows.append({'n':n,'phase':phase,'cw_hex':format(int(read(tape,phase,B),2),f'0{B//4}X'),'ccw_same_anchor_hex':format(int(read(tape,phase,B,-1),2),f'0{B//4}X')})
  report={'n':n,'word_states':N,'binary_slots':B,'state_cycle_hex':[format(x,'X') for x in states],'cw_full_hex':format(int(tape,2),f'0{B//4}X'),'whole_reversal_hex':format(int(whole_reverse,2),f'0{B//4}X'),'ccw_same_anchor_hex':format(int(read(tape,0,B,-1),2),f'0{B//4}X'),'whole_reversal_cw_phase_shifts':shifts,'raw_tape_reflection_axes':axes,'palindrome_word_count':sum(pal_words),'palindrome_correction_bit_count':mask.count('1'),'palindrome_correction_mask_hex':format(int(mask,2),f'0{B//4}X'),'masked_CW_CCW_window_checks':correction_checks,'forward_ANF':{v:expression(c,n) for v,c in zip('abcd'[:n],fp)},'inverse_ANF':{v:expression(c,n) for v,c in zip('abcd'[:n],ip)},'partner_ANF':{v:expression(c,n) for v,c in zip('abcd'[:n],pp)},'forward_max_degree':max(mask.bit_count() for c in fp for mask,value in enumerate(c) if value),'inverse_max_degree':max(mask.bit_count() for c in ip for mask,value in enumerate(c) if value),'partner_max_degree':max(mask.bit_count() for c in pp for mask,value in enumerate(c) if value),'runtime_relations':{'forward_full_cycle':True,'P2_identity':True,'P_T_P_equals_inverse':True,'CCW_bit_view_J_inverse_J':True},'frame_checks':frames}
  results.append(report)
 final={'scope':'Original R2,R3,R4 framed runtime and exact raw bit-reader reflection. Known structure extended and replayed; no physical or universality claim.','results':results,'seconds':time.perf_counter()-start}
 with open('output/rings_3_4_runtime_results.json','w') as f:json.dump(final,f,indent=2)
 with open('output/rings_3_4_hex_phases.csv','w',newline='') as f:
  writer=csv.DictWriter(f,fieldnames=phase_rows[0]);writer.writeheader();writer.writerows(phase_rows)
 print(json.dumps(final,indent=2))
if __name__=='__main__':run()
