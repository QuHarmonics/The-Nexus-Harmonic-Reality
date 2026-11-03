import numpy as np,itertools,ast,json,time,csv,collections

def mobius(bits):
 a=list(bits);h=1
 while h<len(a):
  for base in range(0,len(a),2*h):
   for j in range(h):a[base+h+j]^=a[base+j]
  h*=2
 return a

def compile_online(bits):
 stack=[];events=[]
 for t,bit in enumerate(bits,1):
  stack.append({'width':1,'coeff':[int(bit)],'first':t,'last':t})
  while len(stack)>1 and stack[-1]['width']==stack[-2]['width']:
   right=stack.pop();left=stack.pop();w=left['width']
   block={'width':2*w,'coeff':left['coeff']+[a^b for a,b in zip(left['coeff'],right['coeff'])],'first':left['first'],'last':right['last']}
   events.append({'arrival':t,'output_width':2*w,'input_width':w,'input_first_arrival':left['first'],'input_last_arrival':right['last'],'extra_wait_after_dependencies':t-right['last']})
   stack.append(block)
  expected=[1<<j for j in range(t.bit_length()-1,-1,-1) if t>>j&1]
  assert [b['width'] for b in stack]==expected
 for b in stack:assert mobius(b['coeff'])==list(map(int,bits[b['first']-1:b['last']]))
 return stack,events

def readiness(order,n=8):
 N=1<<(2*n);source=np.arange(N,dtype=np.uint32);a=source&((1<<n)-1);b=source>>n;total=(a+b).astype(np.uint16);outmask=(1<<(n+1))-1
 ready=np.full((N,n+1),-1,dtype=np.int16);known=0;profiles=[]
 for t in range(2*n+1):
  if t:
   operand,j=order[t-1];known|=1<<(j+n*operand)
  groups=source&known;all_and=np.full(N,outmask,dtype=np.uint16);all_or=np.zeros(N,dtype=np.uint16)
  np.bitwise_and.at(all_and,groups,total);np.bitwise_or.at(all_or,groups,total)
  settled=(~(all_and[groups]^all_or[groups]))&outmask
  # If a bit settles, its constant value agrees with the independently computed result.
  assert np.all((all_and[groups]&settled)==(total&settled))
  for j in range(n+1):
   newly=((settled>>j)&1).astype(bool)&(ready[:,j]<0);ready[newly,j]=t
  count=np.sum(ready>=0,axis=1)
  profiles.append({'event':t,'mean_settled_outputs':float(count.mean()),'minimum_settled_outputs':int(count.min()),'maximum_settled_outputs':int(count.max()),'all_nine_ready_cases':int(np.count_nonzero(count==n+1))})
 assert np.all(ready>=0)
 summaries=[]
 for j in range(n+1):
  v=ready[:,j];summaries.append({'output':'carry_out' if j==n else 'sum_bit_'+str(j),'min_event':int(v.min()),'mean_event':float(v.mean()),'max_event':int(v.max()),'ready_before_final_input_cases':int(np.count_nonzero(v<2*n)),'event_histogram':{str(k):int(c) for k,c in zip(*np.unique(v,return_counts=True))}})
 return ready,profiles,summaries

def run():
 start=time.perf_counter();original={};tree=ast.parse(open('pairs_forced.py').read())
 exec(compile(ast.Module(body=[n for n in tree.body if isinstance(n,ast.FunctionDef) and n.name in ('partner','grow')],type_ignores=[]),'original_ring','exec'),original)
 orbit=''.join(original['grow'](2));assert len(orbit)==8
 # Complete byte domain: the same compiler law, no target-dependent scheduling.
 for x in range(256):
  bits=[int(b) for b in format(x,'08b')];stack,events=compile_online(bits)
  assert stack[0]['coeff']==mobius(bits) and mobius(stack[0]['coeff'])==bits
 ring_runs=[];all_closure_rows=[]
 for phase in range(8):
  for direction in (1,-1):
   for length in (8,16,32,64):
    bits=[int(orbit[(phase+direction*j)%8]) for j in range(length)];stack,events=compile_online(bits)
    first_byte=min(e['arrival'] for e in events if e['output_width']==8)
    assert first_byte==8 and all(e['extra_wait_after_dependencies']==0 for e in events)
    assert mobius(stack[0]['coeff'])==bits
    ring_runs.append({'phase':phase,'direction':direction,'arrivals':length,'first_width8_closure':first_byte,'root_closure':events[-1]['arrival'],'closure_events':len(events)})
    if phase==0 and direction==1 and length==8:all_closure_rows=events
 n=8;positions={'LSB_first':list(range(n)),'MSB_first':list(range(n))[::-1],'center_out':sorted(range(n),key=lambda j:(abs(j-(n-1)/2),j))}
 orders={name:[(operand,j) for j in js for operand in (0,1)] for name,js in positions.items()}
 arithmetic=[];profile_rows=[];ready_by_order={}
 for name,order in orders.items():
  ready,profiles,summary=readiness(order,n);ready_by_order[name]=ready
  if name=='LSB_first':assert all(np.all(ready[:,j]==2*j+2) for j in range(n))
  if name=='MSB_first':assert np.count_nonzero(ready[:,n]==2)==(1<<(2*n-1))
  mean=float(ready.mean());arithmetic.append({'order':name,'input_order':order,'operand_pairs':1<<(2*n),'output_bits_including_carry':n+1,'mean_first_ready_event':mean,'mean_avoidable_wait_if_all_outputs_held_until_end':2*n-mean,'outputs':summary})
  profile_rows.extend({'order':name,**p} for p in profiles)
 # The ring supplies actual operand streams, with bit j read at step j (LSB-first).
 ring_operands=[]
 for phase in range(8):
  for direction in (1,-1):
   value=sum(int(orbit[(phase+direction*j)%8])<<j for j in range(8));ring_operands.append((phase,direction,value))
 ring_pairs=[]
 for pa,da,a in ring_operands:
  for pb,db,b in ring_operands:
   index=a|(b<<8);times=ready_by_order['LSB_first'][index]
   assert a+b==sum(((a+b)>>j&1)<<j for j in range(9))
   ring_pairs.append({'phase_a':pa,'direction_a':da,'phase_b':pb,'direction_b':db,'a_hex':format(a,'02x'),'b_hex':format(b,'02x'),'carry_first_ready_event':int(times[8]),'sum_first_ready_events':times[:8].tolist()})
 result={'scope':'Readiness-first compilation and exact arithmetic output settlement. Event index counts observed input-bit arrivals, not physical time. Full truth-domain enumeration is an audit of readiness, not an efficient runtime solver.','source_orbit':orbit,'source_description':'Original flattened R2, eight binary slots; not the full inventory R8.','byte_compiler_roundtrips':256,'ring_stream_compiler_runs':ring_runs,'first_eight_arrival_closures':all_closure_rows,'arithmetic_all_input_orders':arithmetic,'ring_operand_phase_direction_pairs':len(ring_pairs),'ring_pair_examples':ring_pairs[:3],'no_extra_compiler_delay':True,'seconds':time.perf_counter()-start}
 with open('output/readiness_first_results.json','w') as f:json.dump(result,f,indent=2)
 with open('output/readiness_first_emission_profiles.csv','w',newline='') as f:
  w=csv.DictWriter(f,fieldnames=profile_rows[0]);w.writeheader();w.writerows(profile_rows)
 with open('output/readiness_first_compiler_closures.csv','w',newline='') as f:
  w=csv.DictWriter(f,fieldnames=all_closure_rows[0]);w.writeheader();w.writerows(all_closure_rows)
 print(json.dumps({'orbit':orbit,'compiler_closures_first8':all_closure_rows,'arithmetic_summary':[{'order':r['order'],'mean_first_ready_event':r['mean_first_ready_event'],'mean_avoidable_barrier_wait':r['mean_avoidable_wait_if_all_outputs_held_until_end'],'carry':r['outputs'][-1]} for r in arithmetic],'byte_roundtrips':256,'ring_stream_runs':len(ring_runs),'ring_operand_pairs':len(ring_pairs),'seconds':result['seconds']},indent=2))
if __name__=='__main__':run()
