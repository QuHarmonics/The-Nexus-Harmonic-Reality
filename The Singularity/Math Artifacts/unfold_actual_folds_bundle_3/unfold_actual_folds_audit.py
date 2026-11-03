import ast,json,csv,time

def hexbits(bits):return format(int(bits,2),f'0{(len(bits)+3)//4}X')
def fold_once(bits):
 h=len(bits)//2;A=bits[:h];D=''.join(str(int(a)^int(b)) for a,b in zip(A,bits[h:][::-1]))
 return A,D

def fold_all(bits):
 current=bits;refs=[]
 while len(current)>1 and len(current)%2==0:
  A,D=fold_once(current);refs.append(A);current=D
 return current,refs

def unfold_all(root,references):
 current=root;steps=[]
 for A in reversed(references):
  assert len(A)==len(current)
  lower=''.join(str(int(a)^int(b)) for a,b in zip(A,current))[::-1]
  old=current;current=A+lower
  steps.append({'input_width':len(old),'reference_width':len(A),'reference_hex':hexbits(A),'residual_hex':hexbits(old),'reconstructed_width':len(current),'reconstructed_hex':hexbits(current)})
 return current,steps

def unposition(depth,face,N):return N//2-1-depth if face=='L' else N//2+depth

def run():
 start=time.perf_counter();original={};tree=ast.parse(open('pairs_forced.py').read())
 exec(compile(ast.Module(body=[n for n in tree.body if isinstance(n,ast.FunctionDef) and n.name in ('partner','grow')],type_ignores=[]),'original','exec'),original)
 records=[];step_rows=[];perturbations=0
 for n in (2,3,4):
  ring=original['grow'](n);actual=''.join(ring);N=len(ring);root,refs=fold_all(actual)
  recovered,steps=unfold_all(root,refs);assert recovered==actual
  restored_words=[recovered[k:k+n] for k in range(0,len(recovered),n)];assert restored_words==ring
  # The decoder consumes only root and references; flipping any one packet bit changes the output.
  fields=[root]+refs
  for field_index,value in enumerate(fields):
   for bit in range(len(value)):
    modified=value[:bit]+str(1-int(value[bit]))+value[bit+1:];changed=fields.copy();changed[field_index]=modified
    restored,_=unfold_all(changed[0],changed[1:]);assert restored!=recovered;perturbations+=1
  field_bits=sum(map(len,fields));assert field_bits==len(actual)
  # Unfold depth/face back to position and word, rather than guessing between the two faces.
  walk=[];positions=[]
  for i in range(N):
   M=N//2;depth=M-1-i if i<M else i-M;face='L' if i<M else 'R';index=unposition(depth,face,N)
   assert index==i;positions.append(index);walk.append({'depth':depth,'face':face,'word':restored_words[index],'position':index})
  fwd={restored_words[i]:restored_words[(i+1)%N] for i in range(N)};inv={v:k for k,v in fwd.items()}
  for x in restored_words:
   assert inv[fwd[x]]==x
   assert original['partner'](fwd[original['partner'](x)])==inv[x]
  cw=recovered;ccw=''.join(recovered[(-j)%len(recovered)] for j in range(len(recovered)))
  assert ''.join(recovered[(len(recovered)-1-j)%len(recovered)] for j in range(len(recovered)))==recovered[::-1]
  record={'n':n,'original_serialized_width':len(actual),'terminal_residual_width':len(root),'terminal_residual_bits':root,'references_outer_to_inner':[{'width':len(a),'hex':hexbits(a)} for a in refs],'packet_bits_total':field_bits,'unfold_steps':steps,'restored_clockwise_hex':hexbits(cw),'restored_counterclockwise_same_anchor_hex':hexbits(ccw),'whole_byte_or_tape_reverse_hex':hexbits(recovered[::-1]),'original_tape_exact':True,'all_words_and_order_exact':True,'forward_inverse_runtime_exact':True,'partner_conjugates_forward_to_inverse':True,'unfolded_runtime_walk':walk,'all_positions_used_once':len(set(positions))==N}
  records.append(record)
  step_rows.extend({'n':n,**s} for s in steps)
 result={'scope':'Exact inverse of the recorded literal folds. Input to unfolding is terminal residual plus retained reference halves, not the original whole tape. This is not recovery of arbitrary lost information from zero alone.','rings':records,'all_single_packet_bit_perturbations_change_output':perturbations,'seconds':time.perf_counter()-start}
 with open('output/unfold_actual_folds_results.json','w') as f:json.dump(result,f,indent=2)
 with open('output/unfold_actual_folds_steps.csv','w',newline='') as f:
  w=csv.DictWriter(f,fieldnames=step_rows[0]);w.writeheader();w.writerows(step_rows)
 print(json.dumps({'ring_unfolds':[{'n':r['n'],'root':r['terminal_residual_bits'],'widths':[r['terminal_residual_width']]+[s['reconstructed_width'] for s in r['unfold_steps']],'hex_sequence':[hexbits(r['terminal_residual_bits'])]+[s['reconstructed_hex'] for s in r['unfold_steps']],'CW':r['restored_clockwise_hex'],'CCW_same_anchor':r['restored_counterclockwise_same_anchor_hex'],'reference_halves':r['references_outer_to_inner']} for r in records],'packet_bit_perturbations':perturbations,'seconds':result['seconds']},indent=2))
if __name__=='__main__':run()
