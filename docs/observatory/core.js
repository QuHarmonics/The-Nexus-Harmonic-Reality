/* NEXUS observatory — source-grounded browser implementations. See GUIDE.md. */
globalThis.NexusCore = (function makeCore(){
 const mask=n=>(1n<<BigInt(n))-1n, bit=(x,i)=>Number((x>>BigInt(i))&1n), sg=(a,b)=>Math.sign(a-b), bits=(x,n)=>x.toString(2).padStart(n,"0");
 function reverse(x,n){let y=0n;for(let i=0;i<n;i++){y=(y<<1n)|(x&1n);x>>=1n}return y}
 function partner(x,n){const j=reverse(x,n);return j===x?x^mask(n):j}
 function count(p,n,pal){let states=new Map([["0,0,0,0",1n]]);const h=n>>1;
 for(let k=0;k<h;k++){let next=new Map(),hi=bit(p,n-1-k),lo=bit(p,k);for(const [s,v] of states){const [hx,hj,lx,lj]=s.split(",").map(Number);for(let a=0;a<2;a++)for(let b=0;b<2;b++){if(pal&&a!==b)continue;let X=hx||sg(a,hi),L=b===lo?lx:sg(b,lo);if(X>0)continue;if(X<0)L=0;let J=0,K=0;if(!pal){J=hj||sg(b,hi);if(J<0)continue;K=a===lo?lj:sg(a,lo);if(J>0)K=0}const key=[X,J,L,K].join(",");next.set(key,(next.get(key)||0n)+v)}}states=next}
 let total=0n;for(const [s,v] of states){const [hx,hj,lx,lj]=s.split(",").map(Number);for(const c of n%2?[0,1]:[null]){const m=c===null?0:sg(c,bit(p,h));if((hx||m||lx)<0&&(pal||(hj||m||lj)>=0))total+=v}}return total}
 function rank(p,n){let pal=count(p,n,true),d=count(p,n,false),cap=1n<<BigInt(Math.ceil(n/2)-1);return (p-pal+d)/2n+(pal<cap?pal:cap)}
 function address(x,n){const N=1n<<BigInt(n),M=N/2n,p=partner(x,n);let a=x<p?rank(x,n):N-1n-rank(p,n);return n>=2&&(a===M||a===M-1n)?N-1n-a:a}
 function wordAt(a,n){const N=1n<<BigInt(n),M=N/2n;if(a<0n||a>=N)throw Error("Address outside ring");if(n>=2&&(a===M||a===M-1n))a=N-1n-a;const upper=a>=M;if(upper)a=N-1n-a;let lo=0n,hi=N-1n;while(lo<hi){let m=(lo+hi+1n)/2n;if(rank(m,n)<=a)lo=m;else hi=m-1n}return upper?partner(lo,n):lo}
 function ring(n){const N=2**n,r=[];for(let x=0;x<N;x++){let p=Number(partner(BigInt(x),n));if(x<p)r.push(x)}const R=r.concat([...r].reverse().map(x=>Number(partner(BigInt(x),n))));if(n>=2){let m=N/2;[R[m-1],R[m]]=[R[m],R[m-1]]}return R}
 function tau(x,n){return ((x<<1n)&mask(n))|(1n^(x>>BigInt(n-1)))}
 function untau(y,n){return (y>>1n)|((1n^(y&1n))<<BigInt(n-1))}
 function orbit(x,n){const a=[x];for(let y=tau(x,n);y!==x;y=tau(y,n))a.push(y);return a}
 function census(n){const N=2**n,seen=new Uint8Array(N),c={};for(let x=0;x<N;x++)if(!seen[x]){const o=orbit(BigInt(x),n);for(const y of o)seen[Number(y)]=1;c[o.length]=(c[o.length]||0)+1}return c}
 function read(p,w,D,n){const d=D[p],x=d^w,wp=Number(partner(BigInt(x),n)),dp=D.slice();dp[p]^=wp;return {p:p^x,w:wp,D:dp,d,x}}
 function unread(p,w,D,n){const x=Number(partner(BigInt(w),n)),q=p^x,dp=D.slice();dp[q]^=w;return {p:q,w:x^dp[q],D:dp}}
 function span(w,n){let s=new Set([0]);for(const g of [2**n-1,w,Number(reverse(BigInt(w),n))])for(const z of [...s])s.add(z^g);return [...s].sort((a,b)=>a-b)}
 function frame(n,s){let R=ring(n),N=R.length,m=(1<<(n-s))-1,W=R.map((v,i)=>((v&m)<<s)|(R[(i+1)%N]>>(n-s)));let c=new Uint16Array(N);for(const v of W)c[v]++;return {W,missing:R.filter(v=>!c[v]),duplicates:R.filter(v=>c[v]>1),c,R}}
 const J5=x=>(x&16)|((x&1)<<1)|((x>>1)&1)|((x&4)<<1)|((x>>1)&4),P5=x=>J5(x)===x?x^16:J5(x),l0=x=>(x^(x>>1))&1,l1=x=>((x>>2)^(x>>3))&1,A5=x=>J5(x)^((l0(x)^l1(x))<<4);
 function joint(readers,D=Array(32).fill(0)){return {p:readers.map(x=>x[0]),w:readers.map(x=>x[1]),D:[...D]}}
 function jstep(s){const x=s.p.map((p,i)=>s.D[p]^s.w[i]),o=x.map(P5),D=s.D.slice();s.p.forEach((p,i)=>D[p]^=o[i]);return {p:s.p.map((p,i)=>p^x[i]),w:o,D}}
 function jback(s){const x=s.w.map(P5),p=s.p.map((p,i)=>p^x[i]),D=s.D.slice();p.forEach((q,i)=>D[q]^=s.w[i]);return {p,w:p.map((q,i)=>x[i]^D[q]),D}}
 function charge(s){return s.D.reduce((a,b)=>a^b,0)^A5(s.p.reduce((a,b)=>a^b,0))}
 function port(target,T=3){let s=joint([[0,1],[0,4]]),hist=[s];for(let i=1;i<T;i++){s=jstep(s);hist.push(s)}const c=s.p[0],dNeed=c^target^s.w[0],prev=hist[T-2];let others=0;prev.p.forEach((p,i)=>{if(p===c)others^=P5(prev.D[c]^prev.w[i])});const deposit=prev.D[c]^dNeed^others;let p=c,w=prev.D[c]^P5(deposit);for(let k=T-2;k>0;k--){const x=P5(w);p^=x;w=x^hist[k-1].D[p]}return {seed:[p,w],cell:c,dNeed,deposit,base:hist}}
 function runPort(seed,T){let s=joint([[0,1],[0,4],seed]),rows=[s];for(let t=0;t<T;t++){s=jstep(s);rows.push(s)}for(let t=0;t<T;t++)s=jback(s);return {rows,home:JSON.stringify(s)===JSON.stringify(rows[0])}}
 const carry=(a,b,n)=>{const z=a+b,N=1n<<BigInt(n);return [Number(z/N),Number((z+1n)/N)]};
 function carryTree(a,b,n,offset=0){const code=carry(a,b,n),node={n,offset,code,address:Number(address(BigInt(code[0]*2+code[1]),2))};if(n>1){let k=n>>1,m=mask(k);node.low=carryTree(a&m,b&m,k,offset);node.high=carryTree(a>>BigInt(k),b>>BigInt(k),n-k,offset+k);node.composed=node.low.code.map(c=>node.high.code[c]);if(node.composed.join()!==code.join())throw Error("carry composition")}return node}
 function clauses(n,seed){let z=seed>>>0;const polar=[];for(let i=0;i<n-2;i++){z=(Math.imul(z,1664525)+1013904223)>>>0;polar.push((z>>>16)&7)}return polar}
 const sat=(p,a,b,c)=>Boolean((a^(p&1))|(b^((p>>1)&1))|(c^((p>>2)&1)));
 function boundary(n,seed){let ps=clauses(n,seed),D=[1n,1n,1n,1n],rows=[D];for(const p of ps){let E=Array(4).fill(0n);for(let a=0;a<2;a++)for(let b=0;b<2;b++)for(let c=0;c<2;c++)if(sat(p,a,b,c))E[b*2+c]+=D[a*2+b];rows.push(E);D=E}return {ps,rows,total:D.reduce((a,b)=>a+b,0n),checks:8*ps.length}}
 return {mask,bit,bits,reverse,partner,count,rank,address,wordAt,ring,tau,untau,orbit,census,read,unread,span,frame,J5,P5,l0,l1,A5,joint,jstep,jback,charge,port,runPort,carry,carryTree,clauses,sat,boundary}
})();
