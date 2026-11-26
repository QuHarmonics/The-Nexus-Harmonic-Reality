import "../docs/observatory/core.js";
import assert from "node:assert/strict";
import {createHash} from "node:crypto";
const C=globalThis.NexusCore;
const vectors=[[1,"0","0"],[2,"1","2"],[2,"2","1"],[3,"6","3"],[4,"7","6"],[8,"a3","113"],[16,"b163","29716"],[32,"deadbeef","2111105292"],[64,"243f6a8885a308d3","2427008858123944441"],[64,"ffffffffffffffff","18446744073709551615"],[64,"7fffffffffffffff","6917529028714823679"]];
const rings=Array.from({length:9},(_,i)=>C.ring(i+1));
assert.equal(createHash("sha256").update(JSON.stringify(rings)).digest("hex"),"a1d5afc6c1ff7e4dd043d6d36b60c357699c93199d3b2a724939bbb6812dae9a");
let addressChecks=0;for(let n=1;n<=9;n++)for(const [i,x] of rings[n-1].entries()){assert.equal(C.address(BigInt(x),n),BigInt(i));assert.equal(C.wordAt(BigInt(i),n),BigInt(x));addressChecks++}
for(const [n,x,a] of vectors){const w=BigInt("0x"+x);assert.equal(C.address(w,n),BigInt(a));assert.equal(C.wordAt(BigInt(a),n),w)}
assert.deepEqual(C.census(9),{2:1,6:1,18:28});
for(let n=1;n<=9;n++)for(let x=0n;x<=C.mask(n);x++){assert.equal(C.untau(C.tau(x,n),n),x);let y=x;for(let k=0;k<n;k++)y=C.tau(y,n);assert.equal(y,x^C.mask(n))}
const loss=[[0,0],[0,0,2],[0,0,2,2],[0,0,2,2,6],[0,0,0,6,2,6],[0,0,0,10,10,6,14],[0,0,0,8,14,10,6,14],[0,0,0,16,26,26,22,14,30]];
for(let n=2;n<=9;n++)assert.deepEqual(Array.from({length:n},(_,s)=>C.frame(n,s).missing.length),loss[n-2]);
let readerChecks=0;for(let n=1;n<=2;n++){const N=2**n;for(let i=0;i<N**N;i++){let q=i,D=Array.from({length:N},()=>{const v=q%N;q=Math.floor(q/N);return v});for(let p=0;p<N;p++)for(let w=0;w<N;w++){let s=C.read(p,w,D,n),r=C.unread(s.p,s.w,s.D,n);assert.deepEqual(r,{p,w,D});readerChecks++}}}
for(const [n,w,period] of [[2,0,6],[6,12,132]]){let p=0,carry=w,D=Array(2**n).fill(0);for(let t=1;t<=period;t++){const s=C.read(p,carry,D,n);p=s.p;carry=s.w;D=s.D;assert.equal(p===0&&carry===w&&D.every(v=>v===0),t===period)}}
const p=C.port(5,3),r=C.runPort(p.seed,3);assert.deepEqual(p.seed,[4,7]);assert.equal(r.rows[3].p[0],5);assert(r.home);
let portChecks=0;for(let t=0;t<32;t++){const q=C.port(t,3),r=C.runPort(q.seed,3);assert(r.home);for(let i=1;i<r.rows.length;i++){const b=r.rows[i-1],a=r.rows[i],x=b.p.map((p,k)=>b.D[p]^b.w[k]);assert.equal(C.charge(b)^C.charge(a),((b.p.length&1)^x.reduce((s,v)=>s^(C.l0(v)&C.l1(v)),0))<<4);portChecks++}}
let carryChecks=0,boundaryChecks=0;for(let n=1;n<=5;n++)for(let x=0;x<2**n;x++)for(let y=0;y<2**n;y++){C.carryTree(BigInt(x),BigInt(y),n);carryChecks++}
for(let n=3;n<=10;n++)for(let seed=1;seed<=4;seed++){const r=C.boundary(n,seed);let count=0n;for(let x=0;x<2**n;x++)if(r.ps.every((p,i)=>C.sat(p,(x>>i)&1,(x>>(i+1))&1,(x>>(i+2))&1)))count++;assert.equal(count,r.total);boundaryChecks++}
const tape="00011011",read=(i,n)=>BigInt("0b"+Array.from({length:n},(_,k)=>tape[(i+k)%8]).join(""));
const words=[0,2,4,6].map(i=>(read(i,8)<<8n)|read(i+1,8));
assert.deepEqual(words,[0x1b36n,0x6cd8n,0xb163n,0xc68dn]);assert.equal(C.reverse(words[0],16),words[1]);assert.equal(words[0]^words[2],0xaa55n);assert.equal(words.reduce((a,b)=>a^b,0n),0n);
for(let i=0;i<8;i++)assert.equal((read(i,8)^read(i+1,8)).toString(2).replaceAll("0","").length,4);
console.log(JSON.stringify({addressChecks,atlasVectors:vectors.length,readerChecks,portChecks,carryChecks,boundaryChecks,ringDigest:"matches original Atlas",clockCensus:"9-bit source match",wrappingSquare:"source match"}));
