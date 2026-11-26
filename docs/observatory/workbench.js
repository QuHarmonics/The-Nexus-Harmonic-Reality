/* NEXUS direct-manipulation workbench. All calculations use the audited core. */
(function workbench(){
"use strict";
const C=globalThis.NexusCore,$=id=>document.getElementById(id),stage=$("stage"),controls=$("controls");
const cyan="#70e3d1",gold="#ffc477",pink="#e9a0c2",muted="#9aaebc",lineColor="#365061",fg="#e8f0f4";
const B=(x,n)=>C.bits(BigInt(x),n),H=(x,n=0)=>BigInt(x).toString(16).toUpperCase().padStart(Math.ceil(n/4),"0"),F=x=>BigInt(x).toLocaleString("en-US");
const hex=x=>"0x"+H(x),range=(n)=>Array.from({length:n},(_,i)=>i),copy=x=>JSON.parse(JSON.stringify(x));
function parse(s,n){if(!/^(?:0x[0-9a-f]+|0b[01]+|[0-9]+)$/i.test(s.trim()))throw Error("Enter decimal, 0x hex or 0b binary.");const x=BigInt(s.trim());if(x>C.mask(n))throw Error("Value exceeds width.");return x}
const select=(id,label,values,v)=>`<label>${label}<select id="${id}">${values.map(x=>`<option ${x===v?"selected":""} value="${x}">${x}</option>`).join("")}</select></label>`;
const input=(id,label,v)=>`<label>${label}<input id="${id}" type="text" spellcheck="false" value="${v}"></label>`;
const slider=(id,label,min,max,v)=>`<label>${label}<input type="range" id="${id}" min="${min}" max="${max}" value="${v}"></label>`;
const btn=(id,label,primary=false)=>`<button type="button" id="${id}" class="${primary?"action":""}">${label}</button>`;
const bit=(b,act,i,changed=false)=>act?`<button type="button" class="bit ${b?"on":""} ${changed?"changed":""}" data-act="${act}" data-i="${i}" aria-label="Toggle bit ${i}" aria-pressed="${Boolean(b)}">${b}</button>`:`<span class="bit static ${b?"on":""} ${changed?"changed":""}">${b}</span>`;
const bits=(label,x,n,act="",other=null)=>`<div class="bitrowlabel">${label}</div><div class="bits">${[...B(x,n)].map((v,i)=>bit(+v,act,i,other!==null&&v!==B(other,n)[i])).join("")}</div>`;
const m=(name,v)=>`<div class="metric"><small>${name}</small><strong>${v}</strong></div>`;
const metrics=(...ms)=>`<div class="readout">${ms.join("")}</div>`;
const panel=(name,s,wide=false)=>`<section class="panel ${wide?"wide":""}"><h2>${name}</h2>${s}</section>`;
const grid=(...xs)=>`<div class="grid">${xs.join("")}</div>`;
const tab=(headers,rows)=>`<div class="tablewrap"><table><thead><tr>${headers.map(x=>`<th>${x}</th>`).join("")}</tr></thead><tbody>${rows.join("")}</tbody></table></div>`;
const row=(values,attrs="")=>`<tr ${attrs}>${values.map(v=>`<td>${v}</td>`).join("")}</tr>`;
const svg=(g,w=480,h=360,kind="")=>`<svg viewBox="0 0 ${w} ${h}" role="group" aria-label="Interactive diagram" ${kind?`data-diagram="${kind}"`:""}>${g}</svg>`;
const txt=(x,y,v,color=muted,size=12,align="middle")=>`<text x="${x}" y="${y}" fill="${color}" font-family="monospace" font-size="${size}" text-anchor="${align}" pointer-events="none">${v}</text>`;
const circ=(x,y,r,c="#1b3544",stroke=lineColor,w=1)=>`<circle cx="${x}" cy="${y}" r="${r}" fill="${c}" stroke="${stroke}" stroke-width="${w}"/>`;
const ln=(x,y,X,Y,c=lineColor,w=1)=>`<line x1="${x}" y1="${y}" x2="${X}" y2="${Y}" stroke="${c}" stroke-width="${w}" pointer-events="none"/>`;
const pos=(x,y,r,u)=>[x+r*Math.sin(2*Math.PI*u),y-r*Math.cos(2*Math.PI*u)];
const group=(act,i,label,g)=>`<g data-act="${act}" data-i="${i}" role="button" tabindex="0" aria-label="${label}">${g}</g>`;
const note=s=>`<p class="note">${s}</p>`;
const status=s=>`<div class="status" role="status">${s}</div>`;
let timer=null,active=null,draw=()=>{},action=()=>{},drag=null;
function stop(){if(timer!==null)clearInterval(timer);timer=null}
function safe(f){try{$("error").textContent="";f()}catch(e){$("error").textContent=e.message;stop()}}
function bind(id,f,event="click"){$(id).addEventListener(event,()=>safe(f))}
function play(f){if(timer!==null){stop();return}timer=setInterval(()=>safe(f),350)}
function open(title,desc,cs,render,act){$("experiment").innerHTML=`<h1>${title}</h1><p class="hint">${desc}</p>`;controls.innerHTML=cs;draw=render;action=act;drag=null}
function show(s){stage.innerHTML=s}
function edit(x,n,i){return x^(1n<<BigInt(n-1-i))}
function dispatch(el){safe(()=>action(el.dataset.act,+el.dataset.i))}
stage.addEventListener("click",e=>{const el=e.target.closest("[data-act]");if(el)dispatch(el)});
stage.addEventListener("keydown",e=>{if((e.key==="Enter"||e.key===" ")&&e.target.matches("svg [data-act]")){e.preventDefault();dispatch(e.target)}});
function angle(e,kind,cx,cy){const s=stage.querySelector('svg[data-diagram="'+kind+'"]');if(!s)return null;const p=s.createSVGPoint();p.x=e.clientX;p.y=e.clientY;const q=p.matrixTransform(s.getScreenCTM().inverse());return (Math.atan2(q.x-cx,-(q.y-cy))/(2*Math.PI)+1)%1}
stage.addEventListener("pointerdown",e=>{if(e.target.closest("[data-ray]")&&drag){e.preventDefault();drag(e)}});
let down=false,lastMove=0;stage.addEventListener("pointerdown",e=>{if(e.target.closest("[data-ray]"))down=true});
window.addEventListener("pointermove",e=>{if(down&&drag&&performance.now()-lastMove>35){lastMove=performance.now();safe(()=>drag(e))}});
window.addEventListener("pointerup",()=>down=false);window.addEventListener("pointercancel",()=>down=false);
function wrapping(){
 let source=[0,0,0,1,1,0,1,1],base=source.slice(),offset=0,n=8;
 const read=(s,i,k)=>{let x=0n;for(let j=0;j<k;j++)x=(x<<1n)|BigInt(s[(i+j)%8]);return x};
 const pop=x=>[...x.toString(2)].filter(b=>b==="1").length;
 function render(){
 const w=read(source,offset,n),next=read(source,offset+1,n),initial=read(base,offset,n),words=[0,2,4,6].map(i=>(read(source,i,8)<<8n)|read(source,i+1,8));
 const [A,B0,D,E]=words,swap=x=>((x&0x0f0fn)<<4n)|((x&0xf0f0n)>>4n),J=x=>C.reverse(x,16),closed=J(A)===B0&&J(D)===E&&swap(A)===D&&swap(B0)===E;
 let g=circ(220,183,134,"none")+circ(220,183,105,"none","#253b4a");
 const coords=range(8).map(i=>pos(220,183,105,i/8));coords.forEach((p,i)=>{g+=ln(...p,...coords[(i+1)%8],source[i]!==source[(i+1)%8]?gold:lineColor,2)});
 const q=pos(220,183,134,offset/8);g+=ln(220,183,...q,gold,2.5);
 for(let i=0;i<8;i++){const [x,y]=coords[i],o=pos(220,183,145,i/8);g+=group("flip",i,"Flip source bit "+i,circ(x,y,22,source[i]?"#226f65":"#1b3544",source[i]!==base[i]?gold:lineColor,source[i]!==base[i]?3:1)+txt(x,y+6,source[i],source[i]?"#e8fffb":fg,20));g+=group("offset",i,"Read at offset "+i,circ(...o,13,offset===i?gold:"#182c3b",offset===i?gold:lineColor)+txt(o[0],o[1]+4,i,offset===i?"#18212c":muted,11))}
 g+=txt(220,177,"READ "+offset,cyan,20)+txt(220,201,n+"-bit window",muted,12);
 let sq=ln(100,70,340,70,cyan,2)+ln(100,220,340,220,cyan,2)+ln(100,70,100,220,gold,2)+ln(340,70,340,220,gold,2)+txt(220,57,"bit reversal",cyan,11)+txt(220,207,"bit reversal",cyan,11)+txt(110,145,"nibble swap",gold,10,"start")+txt(330,145,"nibble swap",gold,10,"end");
 words.forEach((v,i)=>{const x=i%2?340:100,y=i<2?70:220;sq+=`<rect x="${x-62}" y="${y-24}" width="124" height="48" rx="7" fill="#173440" stroke="#476a72"/>`+txt(x,y+7,H(v,16),cyan,23)});
 show(grid(panel("Click the source bits · click a numbered read position",svg(g,440,366)+`<div class="legend"><span style="color:${cyan}">● 1 bit</span><span>● 0 bit</span><span style="color:${gold}">● Reader / changed source</span></div>`+bits("Editable source",BigInt("0b"+source.join("")),8,"flip")+note("Inner circles edit the source. Outer numbered circles move the reader without editing the source.")),panel("Live readout",bits("Current window",w,n,"",initial)+bits("One position later",next,n,"",w)+metrics(m("Hexadecimal",H(w,n)),m("Reader shift",pop(w^next)+" / "+n),m("Source edit",pop(w^initial)+" / "+n))+status("Offset "+offset+" · "+n+" bits")+note("Gold outlines mark changed bits. Moving a reader is not the same operation as changing its source.")),panel("Four wrapped 16-bit words",svg(sq,440,285)+status(closed?"RUNS · reversal and nibble exchange close the square":"Square does not close for this edited source")+metrics(m("Four-word XOR",H(A^B0^D^E,16)),m("A XOR C",H(A^D,16)))+note("This is a circular 00 | 01 | 10 | 11 tape, not the seam-exchanged native R2 order.")),panel("All eight read positions",tab(["Offset","6 bits","7 bits","8 bits","Hex"],range(8).map(i=>row([i,B(read(source,i,6),6),B(read(source,i,7),7),B(read(source,i,8),8),H(read(source,i,8),8)],`class="${offset===i?"selected":""}" data-act="offset" data-i="${i}" style="cursor:pointer"`)))+note("Click a row to move the read head."))));
 $("offset").value=offset}
 open("Wrapping tape","Flip a bit or move the reader. The entire square and every readout update immediately.",select("aperture","Reader width",[2,4,6,7,8,16,32,64],8)+slider("offset","Read position",0,7,0)+btn("prev","← Read")+btn("next","Read →",true)+btn("reset","Reset source"),render,(a,i)=>{if(a==="flip")source[i]^=1;if(a==="offset")offset=i;render()});
 bind("aperture",()=>{n=+$("aperture").value;render()},"change");bind("offset",()=>{offset=+$("offset").value;render()},"input");bind("prev",()=>{offset=(offset+7)%8;render()});bind("next",()=>{offset=(offset+1)%8;render()});bind("reset",()=>{source=base.slice();offset=0;render()});render()
}
function native(){
 let n=4,x=6n;
 function render(){
 const N=1n<<BigInt(n),a=C.address(x,n),p=C.partner(x,n),pa=C.address(p,n),j=C.reverse(x,n),back=C.wordAt(a,n);
 let g=circ(220,190,145,"none");
 const u=Number(a*1000000n/N)/1e6,v=Number(pa*1000000n/N)/1e6,A=pos(220,190,145,u),P=pos(220,190,145,v);
 g+=ln(...A,...P,gold,2.3);
 if(n<=8){const R=C.ring(n);R.forEach((w,i)=>{let q=pos(220,190,145,i/R.length),focus=BigInt(w)===x,partner=BigInt(w)===p,r=n<=4?15:n<=5?10:n<=6?6:n===7?4:3;g+=group("word",w,"Read word "+B(w,n),circ(...q,r,focus?cyan:partner?gold:"#2c4858",focus?cyan:lineColor)+((n<=4)?txt(q[0],q[1]+3,H(w,n),focus||partner?"#12232b":fg,11):""))})}else{g+=circ(...A,9,cyan)+circ(...P,9,gold)}
 g+=txt(220,184,"R"+n,cyan,29)+txt(220,211,F(N)+" words",muted,12);
 show(grid(panel(n<=8?"Click a word on the native ring":"Exact address · schematic position",svg(g,440,380)+note(n<=8?"Labels are hexadecimal. The facing partner is gold. Native order includes the seam exchange.":"No large ring is allocated. Marker positions are rounded only for display.")),panel("Edit the word",bits("Click any bit",x,n,"bit")+metrics(m("Address",F(a)),m("Facing address",F(pa)),m("Partner",H(p,n)),m("Inverse read",H(back,n)))+bits("Partner",p,n)+status(back===x&&pa===N-1n-a?"RUNS · exact address inverse":"Mismatch")+note(x===j?"Palindrome → complement supplies the partner.":"Nonpalindrome → bit reversal supplies the partner."))));
 $("word").value=hex(x);$("addr").value=a.toString()}
 open("Native ring & 64-bit addresses","Click a word on the ring or edit its bits. The partner and exact address follow instantly.",select("width","Width",[1,2,3,4,5,6,7,8,12,16,24,32,48,64],n)+input("word","Word (hex or decimal)",hex(x))+btn("locate","Locate",true)+input("addr","Exact address","0")+btn("decode","Read address")+btn("partner","Follow partner"),render,(a,i)=>{if(a==="bit")x=edit(x,n,i);if(a==="word")x=BigInt(i);render()});
 bind("width",()=>{n=+$("width").value;x&=C.mask(n);render()},"change");bind("locate",()=>{x=parse($("word").value,n);render()});bind("decode",()=>{x=C.wordAt(parse($("addr").value,n),n);render()});bind("partner",()=>{x=C.partner(x,n);render()});bind("word",()=>{x=parse($("word").value,n);render()},"change");bind("addr",()=>{x=C.wordAt(parse($("addr").value,n),n);render()},"change");render()
}
function nested(){
 let depth=6,u=0.14,n=6,offset=2;const rings=new Map();
 const R=k=>{if(!rings.has(k))rings.set(k,C.ring(k));return rings.get(k)};
 function render(){
 let g="",rows=[],profile="";const cx=230,cy=230,rmax=205;
 for(let k=1;k<=depth;k++){const ring=R(k),N=ring.length,r0=(k-1)*rmax/depth+2,r1=k*rmax/depth-1;for(let j=0;j<N;j++)for(let b=0;b<k;b++){const a=(j+b/k)/N,z=(j+(b+1)/k)/N,A=pos(cx,cy,r0,a),B0=pos(cx,cy,r1,a),B1=pos(cx,cy,r1,z),A1=pos(cx,cy,r0,z),v=(ring[j]>>(k-1-b))&1;g+=`<path d="M${A[0]},${A[1]} L${B0[0]},${B0[1]} A${r1},${r1} 0 0 1 ${B1[0]},${B1[1]} L${A1[0]},${A1[1]} A${r0},${r0} 0 0 0 ${A[0]},${A[1]} Z" fill="${v?"#327e73":"#162b3a"}"/>`}
 g+=circ(cx,cy,r1,"none","#59727d",.6);const slot=Math.floor(u*N),slice=Math.min(k-1,Math.floor(k*(u*N-slot))),w=ring[slot],b=(w>>(k-1-slice))&1;profile+=b;rows.push(row([k,slot,slice,B(w,k),b]));}
 const q=pos(cx,cy,rmax+6,u);g+=ln(cx,cy,...q,gold,2)+circ(...q,6,gold)+`<circle cx="${cx}" cy="${cy}" r="${rmax+12}" fill="transparent" data-ray="true" style="cursor:crosshair"/>`;
 const fr=C.frame(n,offset),loss=range(n).map(i=>C.frame(n,i).missing.length),max=Math.max(...loss,1);
 show(grid(panel("Drag the read ray anywhere on the rings",svg(g,460,460,"nested")+note("Teal = one, dark = zero. Each word occupies an angular sector subdivided into its bits.")),panel("Radial profile",bits("One bit per ring",BigInt("0b"+profile),depth)+metrics(m("Angle",(360*u).toFixed(2)+"°"),m("Profile",profile))+tab(["Ring","Slot","Slice","Word","Bit"],rows)+note("The same ray reads a different word and bit slice at each width.")),panel("Tape-reader offset loss",metrics(m("Windows",2**n),m("Distinct",2**n-fr.missing.length),m("Missing",fr.missing.length))+loss.map((v,i)=>`<div data-act="offset" data-i="${i}" style="cursor:pointer"><span class="note">Offset ${i}: ${v} missing ${i===offset?"← selected":""}</span><div class="bar"><i style="width:${v/max*100}%;background:${i===offset?gold:cyan}"></i></div></div>`).join("")+note("Click an offset to inspect its window frame."),true)));
 $("angle").value=Math.floor(u*4096);$("offset").max=n-1;$("offset").value=offset}
 open("Nested radial reader","Drag the ray through the binary rings. Every ring returns its own bit at the same angle.",select("depth","Ring depth",[2,3,4,5,6,7,8,9],depth)+slider("angle","Ray angle",0,4095,Math.floor(u*4096))+select("width","Tape width",[2,3,4,5,6,7,8,9],n)+slider("offset","Tape offset",0,n-1,offset),render,(a,i)=>{if(a==="offset")offset=i;render()});
 drag=e=>{const v=angle(e,"nested",230,230);if(v!==null){u=Math.floor(v*4096)/4096;render()}};bind("depth",()=>{depth=+$("depth").value;render()},"change");bind("angle",()=>{u=+$("angle").value/4096;render()},"input");bind("width",()=>{n=+$("width").value;offset=Math.min(n-1,offset);render()},"change");bind("offset",()=>{offset=+$("offset").value;render()},"input");render()
}
function clock(){
 let n=9,x=0n,t=0;
 function tick(dir){x=dir>0?C.tau(x,n):C.untau(x,n);t+=dir;render()}
 function render(){const o=C.orbit(x,n),cs=C.census(n),pts=range(n).map(i=>pos(220,182,128,i/n));let g=circ(220,182,128,"none");
 pts.forEach((q,i)=>{const b=Number((x>>BigInt(n-1-i))&1n),next=pts[(i+1)%n];g+=ln(...q,...next,i===n-1?gold:lineColor,2)+group("bit",i,"Flip register bit "+i,circ(...q,Math.min(21,90/n),b?"#226f65":"#1b3544")+txt(q[0],q[1]+4,b,fg,14))});g+=txt(220,177,"t = "+t,cyan,23)+txt(220,202,"period "+o.length,muted,12);
 const points=o.map(y=>{let re=0,im=0;for(let i=0;i<n;i++){const s=1-2*C.bit(y,i);re+=s*Math.cos(Math.PI*i/n);im+=s*Math.sin(Math.PI*i/n)}return [re,im]}),scale=Math.max(1e-12,...points.map(q=>Math.hypot(...q)));let s=circ(190,150,117,"none")+ln(60,150,320,150)+ln(190,20,190,280);points.forEach((q,i)=>{const r=points[(i+1)%points.length];s+=ln(190+q[0]/scale*110,150-q[1]/scale*110,190+r[0]/scale*110,150-r[1]/scale*110,cyan,1.5)});s+=circ(190+points[0][0]/scale*110,150-points[0][1]/scale*110,6,gold);
 show(grid(panel("Click register bits · step the inverter",svg(g,440,366)+bits("Current register",x,n,"bit")+metrics(m("Least period",o.length),m("Tick",t))+note("One complemented return. Atlas convention: rotate left, XOR 1.")),panel("Live fundamental spin projection",svg(s,380,300)+metrics(m("Mode angle",(180/n).toFixed(2)+"°"),m("Inverse",C.untau(C.tau(x,n),n)===x?"exact":"error"))+tab(["Period","Orbits","States"],Object.entries(cs).map(([k,v])=>row([k,v,+k*v])))+note("Discrete spectral projection, not a physical frequency."))))}
 open("One-inverter clock","Click any register bit. Run the clock forward, backward, or continuously.",select("width","Register width",range(15).map(i=>i+1),n)+btn("back","← Reverse")+btn("next","Forward →",true)+btn("play","Play / pause")+btn("reset","Zero register"),render,(a,i)=>{if(a==="bit"){stop();x=edit(x,n,i);t=0;render()}});
 bind("width",()=>{stop();n=+$("width").value;x&=C.mask(n);t=0;render()},"change");bind("back",()=>tick(-1));bind("next",()=>tick(1));bind("play",()=>play(()=>tick(1)));bind("reset",()=>{stop();x=0n;t=0;render()});render()
}
function field(){
 let n=4,p=0,w=3,D=Array(16).fill(0),t=0,selected=0,baseline=JSON.stringify([p,w,D]);
 function newbase(){stop();t=0;baseline=JSON.stringify([p,w,D])}
 function step(dir,paint=true){const s=dir>0?C.read(p,w,D,n):C.unread(p,w,D,n);p=s.p;w=s.w;D=s.D;t+=dir;selected=p;if(paint)render()}
 function reset(){stop();p=0;w=Math.min(3,2**n-1);D=Array(2**n).fill(0);selected=0;newbase();render()}
 function render(){const next=C.read(p,w,D,n),prev=C.unread(next.p,next.w,next.D,n),ok=JSON.stringify([prev.p,prev.w,prev.D])===JSON.stringify([p,w,D]),home=JSON.stringify([p,w,D])===baseline;
 const cells=`<div class="cellgrid">${D.map((v,i)=>`<button type="button" data-act="cell" data-i="${i}" class="${i===p?"current":""} ${i===selected?"editing":""}" aria-label="Edit field cell ${i}">q${i}<b>${H(v,n)}</b></button>`).join("")}</div>`;
 show(grid(panel("Click any field cell to edit it",cells+`<div class="legend"><span style="color:${cyan}">Teal border: reader</span><span style="color:${gold}">Gold border: selected cell</span></div>`+bits("Edit D["+selected+"]",D[selected],n,"field")+btn("setwhere","Move reader to selected cell")+note("Editing a value or moving the reader establishes a new initial state.")),panel("Reader and next transition",bits("WHERE p",p,n,"where")+bits("Carry w",w,n,"carry")+bits("Read D[p]",D[p],n)+bits("Difference x",next.x,n)+bits("Next carry P(x)",next.w,n)+metrics(m("Next WHERE",H(next.p,n)),m("Tick",t),m("Written cell","q"+p),m("Next D[p]",H(next.D[p],n)))+status(home?"At edited initial state":ok?"RUNS · one-step inverse exact":"Mismatch")+note("Forward and reverse use only the complete current state. No history stack."))));
 $("setwhere").onclick=()=>safe(()=>{p=selected;newbase();render()})}
 open("Reversible retained field","Edit a field cell, carry, or reader position. Step forward, then reverse the actual computation.",select("width","Word width",[2,3,4,5,6,7,8],n)+btn("back","← Inverse")+btn("next","Forward →",true)+btn("play","Play / pause")+btn("home","Return to initial state")+btn("reset","Reset field"),render,(a,i)=>{if(a==="cell")selected=i;else{if(a==="field")D[selected]=Number(edit(BigInt(D[selected]),n,i));if(a==="carry")w=Number(edit(BigInt(w),n,i));if(a==="where")p=Number(edit(BigInt(p),n,i));newbase()}render()});
 bind("width",()=>{n=+$("width").value;reset()},"change");bind("back",()=>step(-1));bind("next",()=>step(1));bind("play",()=>play(()=>step(1)));bind("reset",reset);bind("home",()=>{stop();if(Math.abs(t)>100000)throw Error("Return capped at 100,000 steps.");while(t)step(t>0?-1:1,false);render()});render()
}
function port(){
 let target=5,q,s,t=0,initial,land=null;
 function derive(){stop();q=C.port(target,3);s=C.joint([[0,1],[0,4],q.seed]);initial=JSON.stringify(s);t=0;land=null;render()}
 function step(dir){if(dir===1&&t===3||dir===-1&&t===0)return;s=dir===1?C.jstep(s):C.jback(s);t+=dir;if(t===3)land=s.p[0];render()}
 function render(){const colors=[cyan,gold,pink],cells=`<div class="cellgrid">${s.D.map((v,i)=>`<button type="button" data-act="target" data-i="${i}" class="${i===target?"target":""}" aria-label="Set target ${i}">q${i}<b>${H(v,5)}</b>${s.p.map((p,k)=>p===i?`<span style="color:${colors[k]}">${"ABC"[k]} </span>`:"").join("")||"&nbsp;"}</button>`).join("")}</div>`;
 show(grid(panel("Click a field cell to request A's destination",cells+`<div class="legend"><span style="color:${cyan}">A</span><span style="color:${gold}">B / target outline</span><span style="color:${pink}">C · derived reader</span></div>`+tab(["Reader","WHERE","Carry","Cell value"],s.p.map((p,i)=>row(["ABC"[i],p,B(s.w[i],5),B(s.D[p],5)])))+metrics(m("Tick",t+" / 3"),m("Charge",B(C.charge(s),5)))),panel("Derive the missing reader",metrics(m("Requested target",target),m("Required write cell",q.cell),m("Required field",B(q.dNeed,5)),m("Deposit",B(q.deposit,5)),m("C seed (p,w)",q.seed.join(", ")),m("A actual WHERE",s.p[0]))+status(land===null?"Provider derived · execute to read":land===target?"RUNS · requested destination":"OPEN · base trace changed; actual "+land)+status(t===0?(JSON.stringify(s)===initial?"Full state at source":"Source mismatch"):"")+note("The third reader is derived from the base trace, not selected by candidate search. Some targets interfere with that trace; the actual landing is always shown."))))}
 open("Directed collision port","Choose a destination by clicking the field. The third reader is derived from the requested result.",btn("derive","Re-derive")+btn("back","← Inverse")+btn("step","Forward →",true)+btn("run","Execute to tick 3")+btn("home","Reverse to source"),render,(a,i)=>{if(a==="target"){target=i;derive()}});
 bind("derive",derive);bind("back",()=>step(-1));bind("step",()=>step(1));bind("run",()=>{while(t<3)step(1)});bind("home",()=>{while(t>0)step(-1)});derive()
}
function carry(){
 let n=8,a=0x63n,b=0x36n,cin=0;
 const col=c=>c[0]?gold:c[1]?cyan:"#718596",name=c=>c[0]?"Generate":c[1]?"Propagate":"Kill";
 function render(){const root=C.carryTree(a,b,n),sum=a+b+BigInt(cin),N=1n<<BigInt(n),levels=[],queue=[[root,0]];while(queue.length){const [v,l]=queue.shift();(levels[l]??=[]).push(v);if(v.low)queue.push([v.low,l+1],[v.high,l+1])}
 let g="";const h=levels.length*52+20;levels.forEach((nodes,l)=>nodes.forEach((v,i)=>{const count=nodes.length,X=(i+.5)*640/count,Y=25+52*l,W=Math.min(96,630/count-2);if(l)g+=ln((Math.floor(i/2)+.5)*640/(count/2),Y-52,X,Y);g+=`<rect x="${X-W/2}" y="${Y-13}" width="${W}" height="26" rx="4" fill="${col(v.code)}"/>`;if(W>=20)g+=txt(X,Y+4,W>55?v.n+"b · "+v.code.join(""):v.code.join(""),"#10212b",11)}));
 show(grid(panel("Build an adder by editing operand bits",bits("A",a,n,"a")+bits("B",b,n,"b")+bits("Sum",sum%N,n)+metrics(m("Carry-in",cin),m("Carry-out",sum/N),m("Root contract",root.code.join("")+" "+name(root.code)),m("R2 address",root.address))+note("A + B + carry-in = sum + 2ⁿ × carry-out.")),panel("Live composed carry tree",svg(g,640,h)+`<div class="legend"><span style="color:#718596">● Kill 00</span><span style="color:${cyan}">● Propagate 01</span><span style="color:${gold}">● Generate 11</span></div>`+status("RUNS · carry composition")+note("The boundary remains a single carry bit as width grows. Balanced decomposition is a selected implementation, not a unique consequence of the contract."))));$("a").value=hex(a);$("b").value=hex(b)}
 open("Carry-contract compiler","Toggle either operand. Watch the same three carry contracts compose into a larger computation.",select("width","Operand width",[2,4,8,16,32,64],n)+input("a","A",hex(a))+input("b","B",hex(b))+select("cin","Carry in",[0,1],cin)+btn("apply","Apply operands",true),render,(act,i)=>{if(act==="a")a=edit(a,n,i);if(act==="b")b=edit(b,n,i);render()});
 bind("width",()=>{n=+$("width").value;a&=C.mask(n);b&=C.mask(n);render()},"change");bind("cin",()=>{cin=+$("cin").value;render()},"change");bind("apply",()=>{const A=parse($("a").value,n),B0=parse($("b").value,n);a=A;b=B0;render()});bind("a",()=>{a=parse($("a").value,n);render()},"change");bind("b",()=>{b=parse($("b").value,n);render()},"change");render()
}
function clauses(){
 let n=12,ps=C.clauses(n,136);
 function render(){let D=[1n,1n,1n,1n],rows=[D];for(const pol of ps){const E=Array(4).fill(0n);for(let a=0;a<2;a++)for(let b=0;b<2;b++)for(let c=0;c<2;c++)if(C.sat(pol,a,b,c))E[b*2+c]+=D[a*2+b];rows.push(E);D=E}const total=D.reduce((a,b)=>a+b,0n),max=Math.max(1,...rows.map(r=>Math.log2(Number(r.reduce((a,b)=>a+b,0n))+1))),cols=[cyan,gold,pink,"#80aef5"];let g=ln(24,190,596,190);for(let j=0;j<4;j++){let points=rows.map((r,i)=>`${24+572*i/(rows.length-1)},${190-170*Math.log2(Number(r[j])+1)/max}`);g+=`<polyline points="${points.join(" ")}" fill="none" stroke="${cols[j]}" stroke-width="2"/>`}
 const edits=tab(["Clause","Toggle literal signs"],ps.map((p,i)=>row([i+1,range(3).map(j=>`<button data-act="pol" data-i="${i*3+j}" class="${(p>>j)&1?"bit":"bit on"}" aria-label="Toggle clause ${i+1} literal ${j+1}">${(p>>j)&1?"¬":""}x${i+j+1}</button>`).join(" ∨ ")])));
 show(grid(panel("Edit the actual clauses",edits+note("Each clause shares two variables with the next. Click a literal to negate or restore it.")),panel("Four boundary entries",metrics(m("Global assignments",F(1n<<BigInt(n))),m("Persistent entries",4),m("Satisfying assignments",F(total)),m("Local checks",ps.length*8))+svg(g,620,215)+`<div class="legend">${cols.map((c,j)=>`<span style="color:${c}">● ${B(j,2)}</span>`).join("")}</div>`+tab(["Cut","00","01","10","11"],rows.map((r,i)=>row([i,...r.map(F)])))+note("Plot scale: log₂(count + 1). This exact recurrence applies to the specified local chain, not general SAT."))))}
 open("Clause-boundary reader","Toggle literal signs. The exact count updates through four boundary entries, without enumerating global assignments.",select("width","Variables",[3,4,8,12,16,24,32,48,64],n)+btn("reset","Restore example",true),render,(a,i)=>{if(a==="pol"){ps[Math.floor(i/3)]^=1<<(i%3);render()}});
 bind("width",()=>{n=+$("width").value;ps=C.clauses(n,136);render()},"change");bind("reset",()=>{ps=C.clauses(n,136);render()});render()
}
const tabs=[["square","Wrapping tape",wrapping],["address","Native ring",native],["nested","Nested reader",nested],["clock","Inverter clock",clock],["field","Reversible field",field],["port","Collision port",port],["carry","Carry compiler",carry],["clauses","Clause boundary",clauses]];
function activate(i,write){stop();down=false;drag=null;active=i;[...$("tabs").children].forEach((b,k)=>{b.classList.toggle("active",i===k);b.setAttribute("aria-pressed",String(i===k))});if(write)history.replaceState(null,"","#"+tabs[i][0]);safe(tabs[i][2])}
tabs.forEach(([key,name],i)=>{const b=document.createElement("button");b.id="tab-"+key;b.type="button";b.innerHTML="<small>"+String(i+1).padStart(2,"0")+"</small>"+name;b.onclick=()=>activate(i,true);$("tabs").appendChild(b)});
function route(){const h=location.hash.slice(1);if(h==="research"){$("research").open=true;if(active===null)activate(0,false);return}let i=tabs.findIndex(x=>x[0]===h);if(h==="explorer")i=1;activate(i<0?0:i,false)}
window.addEventListener("hashchange",route);route()
})();
