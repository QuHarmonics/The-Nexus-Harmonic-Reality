import ast,json,hashlib,time
from ring_compiler import compile_source,make_fold_source,original_cycle,SourceError,GrammarError,FoldError,ResourceLimit

CYCLE='ring R3 width 3 { cycle: 000 -> 001 -> 010 -> 110 -> 011 -> 101 -> 100 -> 111; }'
FOLDED='ring R3 width 3 { fold { root: 000; refs_inner_to_outer: [111, 111000, 000001010110]; } }'

def expect_error(label,call,kind):
 try:call()
 except kind as e:return {'case':label,'expected':kind.__name__,'actual':type(e).__name__,'message':str(e),'passed':True}
 except Exception as e:raise AssertionError(label+' raised unexpected '+type(e).__name__) from e
 raise AssertionError(label+' was not rejected')

def run():
 start=time.perf_counter();original={};tree=ast.parse(open('pairs_forced.py').read())
 exec(compile(ast.Module(body=[n for n in tree.body if isinstance(n,ast.FunctionDef) and n.name in ('partner','grow')],type_ignores=[]),'original','exec'),original)
 widths=[];total_states=0
 for n in range(1,9):
  words=original['grow'](n);cycle=[int(w,2) for w in words]
  source='ring R'+str(n)+' width '+str(n)+' { cycle: '+' -> '.join(words)+'; }'
  folded=make_fold_source('R'+str(n),n,cycle)
  ir,target,trace=compile_source(source);ir2,target2,trace2=compile_source(folded)
  assert ir==ir2 and target==target2 and cycle==original_cycle(n)
  module={};exec(compile(target,'generated_R'+str(n),'exec'),module)
  f=module['R'+str(n)+'_forward'];g=module['R'+str(n)+'_inverse'];P=ir['partner_by_state']
  for x in range(1<<n):
   assert f(x)==ir['successor_by_state'][x] and g(x)==ir['predecessor_by_state'][x]
   assert g(f(x))==x and f(g(x))==x and P[f(P[x])]==g(x)
   total_states+=1
  widths.append({'width':n,'states':1<<n,'literal_and_folded_semantic_IR_identical':True,'generated_python_byte_identical':True,'all_forward_and_inverse_transitions':True})
 ir,target,trace=compile_source(CYCLE);ir2,target2,foldtrace=compile_source(FOLDED)
 assert ir==ir2 and target==target2
 module={};exec(compile(target,'R3_target','exec'),module);f=module['R3_forward'];g=module['R3_inverse']
 source_errors=[]
 source_errors.append(expect_error('wrong word width',lambda:compile_source(CYCLE.replace('111;','11;')),SourceError))
 source_errors.append(expect_error('duplicate/missing state',lambda:compile_source(CYCLE.replace('111;','110;')),SourceError))
 source_errors.append(expect_error('ordinary counting order instead of ring order',lambda:compile_source('ring Bad width 3 { cycle: 000 -> 001 -> 010 -> 011 -> 100 -> 101 -> 110 -> 111; }'),SourceError))
 source_errors.append(expect_error('nonbinary state token',lambda:compile_source(CYCLE.replace('000','002',1)),GrammarError))
 source_errors.append(expect_error('fold reference has wrong width',lambda:compile_source(FOLDED.replace('[111,','[11,')),FoldError))
 source_errors.append(expect_error('fold references discarded',lambda:compile_source('ring Bad width 3 { fold { root: 000; refs_inner_to_outer: []; } }'),FoldError))
 source_errors.append(expect_error('fold root not a terminal equal-half residue',lambda:compile_source(FOLDED.replace('root: 000;','root: 00;')),FoldError))
 source_errors.append(expect_error('zero source width',lambda:compile_source('ring Bad width 0 { cycle: 0; }'),SourceError))
 source_errors.append(expect_error('malformed source header',lambda:compile_source('width 3 { cycle: 000; }'),GrammarError))
 big=original_cycle(13);bigsource='ring Big width 13 { cycle: '+' -> '.join(format(x,'013b') for x in big)+'; }'
 resource=expect_error('valid-width-13 ring exceeds implementation budget',lambda:compile_source(bigsource),ResourceLimit)
 runtime_errors=[]
 for name,fn in [('forward',f),('inverse',g)]:
  for label,value,kind in [('overflow',8,ValueError),('negative',-1,ValueError),('float',1.5,TypeError),('string','010',TypeError),('bool',True,TypeError)]:
   runtime_errors.append(expect_error(name+' '+label,lambda fn=fn,value=value:fn(value),kind))
 edges=[{'input':format(x,'03b'),'forward':format(f(x),'03b'),'inverse':format(g(x),'03b'),'inverse_of_forward':format(g(f(x)),'03b')} for x in (0,7)]
 with open('output/R3_cycle.ring','w') as h:h.write(CYCLE+'\n')
 with open('output/R3_fold.ring','w') as h:h.write(FOLDED+'\n')
 with open('output/R3_target.py','w') as h:h.write(target)
 with open('output/R3_ir.json','w') as h:json.dump(ir,h,indent=2)
 with open('output/R3_fold_frontend_trace.json','w') as h:json.dump(foldtrace,h,indent=2)
 report={'scope':'New explicit text front end for the earlier Python-list prototype; fixed original ring descriptions only. The semantic IR and generated rules are verified, not a universal compiler claim.','width_tests':widths,'total_state_cases':total_states,'source_rejection_tests':source_errors,'resource_policy_test':resource,'runtime_rejection_tests':runtime_errors,'valid_edge_cases':edges,'R3_literal_folded_IR_equal':ir==ir2,'R3_literal_folded_target_equal':target==target2,'R3_target_sha256':hashlib.sha256(target.encode()).hexdigest(),'seconds':time.perf_counter()-start}
 with open('output/ring_compiler_test_results.json','w') as h:json.dump(report,h,indent=2)
 print(json.dumps({'all_state_cases':total_states,'source_rejections':len(source_errors),'resource_rejections':1,'runtime_rejections':len(runtime_errors),'edges':edges,'fold_normalization':foldtrace,'generated_R3_target':target,'R3_IR':ir,'seconds':report['seconds']},indent=2))
if __name__=='__main__':run()
