import assert from "node:assert/strict";
import {pathToFileURL} from "node:url";
import {resolve} from "node:path";
const {chromium}=await import(process.env.PLAYWRIGHT_MODULE || "playwright");
const browser=await chromium.launch({headless:true,executablePath:process.env.CHROME_BIN||undefined,args:["--no-sandbox"]});
try{
 const page=await browser.newPage({viewport:{width:1440,height:900}});
 const errors=[];page.on("pageerror",e=>errors.push(e.message));
 await page.goto(pathToFileURL(resolve("docs/index.html")).href);
 const stage=page.locator("#stage");
 const click=async s=>{await page.locator(s).first().click();assert.equal(await page.locator("#error").innerText(),"")};
 const body=()=>stage.innerText();
 await page.locator('[data-act="flip"].bit').first().waitFor();
 assert.match(await body(),/1B36/);assert.match(await body(),/6CD8/);
 await click('[data-act="flip"][data-i="0"].bit');assert.equal(await page.locator('[data-act="flip"][data-i="0"].bit').innerText(),"1");assert.doesNotMatch(await body(),/RUNS · reversal and nibble exchange close/);
 await click("#reset");assert.match(await body(),/RUNS · reversal and nibble exchange close/);
 await click("#next");assert.match(await body(),/Offset 1 · 8 bits/);
 await click("#tab-address");await click('[data-act="word"][data-i="0"]');assert.equal(await page.locator("#word").inputValue(),"0x0");await click("#partner");assert.equal(await page.locator("#word").inputValue(),"0xF");
 await click("#tab-nested");const before=await body();const ray=await page.locator('[data-diagram="nested"]').boundingBox();await page.mouse.move(ray.x+ray.width/2,ray.y+ray.height*.20);await page.mouse.down();await page.mouse.move(ray.x+ray.width*.8,ray.y+ray.height/2,{steps:5});await page.mouse.up();assert.notEqual(await body(),before);assert.equal(await page.locator("#error").innerText(),"");
 await click("#tab-clock");await click('[data-act="bit"][data-i="0"].bit');await click("#next");await click("#back");assert.match(await body(),/Tick\s*0/);
 await click("#tab-field");await click('[data-act="cell"][data-i="3"]');await click('[data-act="field"][data-i="0"].bit');await click("#setwhere");assert.match(await body(),/At edited initial state/);await click("#next");await click("#home");assert.match(await body(),/At edited initial state/);
 await click("#tab-port");await click('[data-act="target"][data-i="5"]');await click("#run");assert.match(await body(),/RUNS · requested destination/);await click("#home");assert.match(await body(),/Full state at source/);
 await click("#tab-carry");const adderBefore=await body();await click('[data-act="a"][data-i="0"].bit');assert.notEqual(await body(),adderBefore);
 await click("#tab-clauses");const clauseBefore=await body();await click('[data-act="pol"][data-i="0"]');assert.notEqual(await body(),clauseBefore);
 await page.setViewportSize({width:390,height:844});await click("#tab-square");assert(await page.locator('body').evaluate(e=>e.scrollWidth<=innerWidth+2),"Mobile layout overflows");
 assert.deepEqual(errors,[]);console.log("PASS: eight workbench instruments, source edits, ray dragging, clock inverse, edited-field return, directed port, adder, clause signs, mobile layout; no uncaught page errors.");
}finally{await browser.close()}
