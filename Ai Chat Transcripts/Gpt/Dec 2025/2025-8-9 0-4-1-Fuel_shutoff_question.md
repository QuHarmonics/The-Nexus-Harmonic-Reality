# Fuel shutoff question

https://chat.openai.com/c/6896c8af-fb58-8323-82a3-3294f099b1e1

## USER
hey buddy, 97 e36 convertible does it have a fuel shutoff that might trip from a bad bump

## ASSISTANT
Yes — your ’97 E36 convertible does have an inertia fuel cut-off function, though BMW didn’t use a big red reset button like some Fords and Hondas.  

On the E36, the crash-related fuel shut-off is built into the **airbag/SRS control module**. If the module detects a severe impact (or a signal from the crash sensors), it sends a **fuel pump cut signal** to the DME via the fuel pump relay. That stops the pump immediately.  

A couple of points that apply to your car:  

- A *minor* bump or pothole usually won’t trip it — the threshold is set high so it only reacts to crash-like deceleration.  
- If it does trigger, there’s no physical button to push. The system resets when you turn the ignition off and back on, as long as there’s no stored crash flag in the SRS module.  
- If the SRS module has logged a crash event, it may need to be cleared with a BMW-capable scan tool before fuel delivery returns to normal.  

If you’re dealing with a **no-start after a jolt**, the common checks are:  
1. Listen for the fuel pump priming when you turn the key to position II.  
2. Check the fuel pump relay (in the fuse/relay box under the hood).  
3. Scan the SRS module for crash data — clearing it can restore pump power if it was falsely triggered.  

If you want, I can walk you through **jumpering the relay** to quickly test whether the pump is actually being shut off by the crash logic. That’ll tell you if the issue is the safety shut-off or something else entirely.  

## USER
i flipped the relay with another matching one.  i checked for voltage at the fuel pump but none

## Thoughts
Based on the user's info, since they've swapped the relay and checked for voltage at the fuel pump with no result, I need to guide them through further checks. They should verify the fuse (F18, 15A), relay socket, EWS immobilizer status, ignition switch, and the crash safety signal from the SRS to the DME for fuel pump power. We'll take it step by step.
To guide the user, I'd suggest checking the fuel pump fuse using the cover diagram. Then, measure the relay socket pins (30, 87, 85, 86) and make sure the K6300 main relay is working. You can jumper 30 to 87 to check the wiring. If no power, check for an open circuit, fuse, or fusible link.
We should suggest scanning the SRS and DME for crash status. Also, check the ignition switch to rule out accessory circuit failures that could affect the pump. EWS immobilizer could be an issue if there's no fuel pump prime while the engine cranks. Alignment loss might require syncing with INPA or DIS. 

Testing steps: 

1. Verify fuses (pump and DME relay). 
2. At fuel pump relay socket: Pin 30 should have constant 12V from battery.
If there's no 12V, check the fusible link (80A/50A near the battery, under the carpet). Ensure you reference the rear power distribution cable for accuracy. 

For Pin 85/86, one side gets ignition 12V; the DME grounds the other for 2 seconds during prime and cranking. Jumper 30 to 87 to force the fuel pump on. If the pump runs, check the DME relay and alignment, ignition switch, and other wiring components, like cam/crank sensors.

## ASSISTANT
Understood. Since you have no voltage at the pump after substituting a known-good relay, proceed methodically through the power path and control logic. The E36 fuel pump is only powered for ~1–2 seconds at key-on (prime) and then continuously while cranking/running. Ensure measurements are taken during that brief prime and during cranking; otherwise you may read 0 V even on a healthy system.

### 1) Verify constant power feed at the fuel-pump relay socket
- Remove the fuel-pump relay and probe **terminal 30** in the relay base.
- **Expected:** battery voltage at all times.
- **If 0 V:** check the **fuel-pump fuse** (refer to the fuse-cover diagram), and then the **rear fusible link** in the battery feed (common on E36, located near the battery under the rear seat area). A blown fusible link or corroded battery feed will leave the relay with no supply.

### 2) Force the pump on (bypass test)
- With the relay removed, install a **fused jumper** (15–20 A) between **terminal 30 → terminal 87** of the fuel-pump relay socket.
- **Outcomes:**
  - **Pump runs / 12 V present at pump connector:** wiring to the pump and the pump itself are likely sound; the problem is in **control** (relay coil drive, main relay, ignition switch, DME/EWS/SRS crash signal).
  - **Pump silent / still 0 V at the pump connector:** suspect **open circuit** between relay and pump, poor **ground** at the pump, a **blown pump fuse**, or a failed **pump**. At this point, apply 12 V and ground directly at the pump connector (with appropriate fusing) to confirm pump operation.

*Notes to help you identify conductors at the tank:* on BMWs of this era, pump **positive** is typically **green/violet (GN/VI)** and **ground** is **brown**. The sender wires are different colors; do not confuse them with the pump feed.

### 3) If the pump runs on the jumper, diagnose control of the relay
The relay coil needs two things: ignition-switched power on one side and a ground command from the DME on the other.

- **Terminal 85/86 (relay coil):**
  - With ignition ON, one side should have **12 V** (from ignition switch via the **DME main relay**).
  - During key-on prime (brief) and while **cranking**, the **DME** grounds the other side to energize the coil.
- **If there is no ignition 12 V at the coil:** suspect **ignition switch** failure (common on E36) or a failed **DME main relay**/power supply.
- **If there is ignition 12 V, but the DME never grounds the coil:**
  - Check that the **engine speed (crank) signal** is present during cranking; without a valid RPM signal many DMEs will not sustain pump operation.
  - Verify **EWS (immobilizer) alignment**. If EWS/DME are not synchronized, the DME may inhibit pump control. A quick EWS-DME sync with INPA/DIS often resolves this.
  - Check the **SRS/MRS module** for a stored **crash (inertia) event**. On the E36, a crash output can command fuel shutoff; clearing a latched crash flag with a BMW-capable scan tool may be required to restore fuel-pump control.

### 4) Ground and harness checks (if the jumper test fails)
- Inspect the **pump ground point** (in the rear seat area/body). Verify continuity from pump ground to chassis (<0.3 Ω).
- Load-test the **pump positive circuit** (relay 87 → pump): with the jumper installed, measure voltage at the pump connector **under load**; a large drop (>1 V) indicates a high-resistance connection or broken conductor.
- Inspect the **rear harness run** to the tank lid for chafing or corrosion at the pump/sender flange.

### 5) Practical sequence to minimize time
1. Probe **relay terminal 30** for constant 12 V.
2. **Jumper 30→87**; listen/measure at the pump.
3. If the pump runs: check **coil feed and DME ground command** at 85/86 while cranking; then evaluate **main relay, ignition switch, EWS sync, SRS crash flag**.
4. If the pump does **not** run: verify **fuse**, **fusible link**, **pump ground**, and **apply 12 V directly at the pump** to confirm pump health.

If you can share:
- Whether you measured during **cranking**,
- The voltage you see at **relay terminal 30**,
- The result of the **30→87 jumper**,

…I can pinpoint the next exact test (e.g., which pin to back-probe at the DME or how to sync EWS).

## USER
do issue. my e90. the bottom case (the front drive) it covered in oil. i may have spilled too much one time but im not sure

## Thoughts
It sounds like you're dealing with an oil leak on the front bottom of the case. Given the context, this could involve the oil pan, oil filter housing, valve cover gasket, or even seals like the front crank or the power steering system. If you spilled oil during a refill, it might have spread to areas near the serpentine belt.
We’ll follow these steps: Identify fluid type (color, smell, and viscosity), locate the leak, and check common sources: OFHG, oil cooler, valve cover gasket, PCV issues, and front differential (for AWD). Degrease and use UV dye to pinpoint leaks, ensure oil level is correct, inspect the belt for contamination, and watch for potential hydrolock or serpentine belt wear. Provide torque specs without images, keeping everything clear and concise.
The user requested a formal academic style, so I'll focus on clear, actionable steps without emojis. I'll avoid issuing too many clarifying questions and provide a diagnostic decision tree, addressing both AWD and RWD differences. I'll outline telltale signs of leaks and recommend parts like the OFHG, oil cooler gasket, and valve cover gasket.

## ASSISTANT
Below is a structured differential and a step-wise test plan for an E90 with oil accumulation at the front underside (“bottom case/front drive”). The objective is to distinguish a one-time spill from an active leak and to localize the true source before parts replacement.

# Likely sources by location (E90 petrol engines)

1. **Oil Filter Housing Gasket (OFHG)**  
   - **Pattern:** Oil wetting around the oil filter housing, running down the front of the engine block and accessory bracketry; oil mist on the serpentine belt and lower splash shield.  
   - **Notes:** Most common on N52/N51/N54/N55. If equipped with an external **oil cooler/thermostat**, the **oil cooler gasket** can leak simultaneously.

2. **Valve Cover Gasket (VCG)**  
   - **Pattern:** Wetness along the perimeter of the valve cover. Oil can travel down the front timing cover and mimic an OFHG or front-case leak. Often accompanied by burnt-oil odor.

3. **Oil Pan Gasket (OPG)**  
   - **Pattern:** Uniform wetting along the mating seam of the pan; drips at the rear of the pan and subframe. On xi/xDrive, remember the front differential is bolted to/near the pan; leaks may look “front-drive” related.

4. **Front Crankshaft Seal / Upper Timing Cover Seep**  
   - **Pattern:** Oil behind the vibration damper and crank pulley; belt and fan area oily. Less common than OFHG/VCG but possible.

5. **Power Steering System (ATF on most E90s)**  
   - **Pattern:** Reddish fluid at the reservoir hoses, pump, or lines; can coat the same front undertray area. Distinguish by color/odor (ATF vs engine oil).

6. **Transmission fluid (ZF 6HP or GM 6L40)**  
   - **Pattern:** Amber/reddish drips farther rearward; typically not limited to the very front.

7. **xDrive front differential (if xi)**  
   - **Pattern:** Wetness at axle seals or pinion seal. Fluid has a distinct gear-oil odor (sulfurous).

# Quick discrimination: spill vs active leak

- **Degrease & baseline:** Thoroughly clean the front of the engine, belt area, and lower cover with a solvent degreaser; dry completely.  
- **UV dye test (preferred):** Add engine-oil UV dye, run for 15–30 minutes (idle + short drive), then inspect with a UV lamp. Fresh tracks pinpoint the source.  
- **Talc “dusting” (no dye available):** Apply a light dusting of talc/chalk on suspect seams (OFHG edge, valve cover corner, front cover). The first damp track indicates origin.

# Safety interlude

- **Do not drive if the belt is oil-soaked.** Oil degrades the belt; shredded belts can get ingested past the front crank seal (“belt ingestion”), causing severe engine damage. Replace a contaminated belt after fixing the leak.

# Targeted inspections (5–10 minutes each)

1. **Oil filter housing area**  
   - Mirror the lower edge where housing meets the block; check the junction to the oil cooler/thermostat (if present). Any fresh sheen here is highly predictive of OFHG/ocg failure.

2. **Valve cover front corner (exhaust side)**  
   - Look for wetness at the front-right corner; trace downward along the timing cover. If the upper area is dry, VCG is less likely as the primary source.

3. **Crank pulley & lower timing cover**  
   - If dye emerges right behind the pulley, suspect front main seal.

4. **Oil pan perimeter**  
   - Clean, drive, and recheck the pan seam. Uniform beading along the seam points to OPG; streaks above the seam point you back up to OFHG/VCG.

5. **Fluid identification**  
   - Engine oil: amber/brown, characteristic smell.  
   - ATF (power steering): red/pink, sweet/varnish odor.  
   - Gear oil (front diff): dark, strong sulfur odor.

# Probable repairs and practical notes

- **OFHG (and oil cooler gasket if equipped):**  
  - Most common fix for this presentation.  
  - Use OE or high-quality Viton gaskets.  
  - Clean all mating surfaces meticulously; torque housing bolts to spec in a cross-pattern.  
  - Replace the serpentine belt and thoroughly clean pulleys if oil-contaminated.

- **VCG:**  
  - Replace the perimeter gasket and spark-plug tube seals.  
  - Inspect/replace PCV/valve-cover breather; excessive crankcase vacuum can exacerbate leaks.

- **OPG:**  
  - More labor (subframe support). Consider if pan seam is the first wet point after a proper clean-and-retest.

- **Front main seal:**  
  - Confirm with dye; replace only if clearly implicated.

- **Power steering hoses/reservoir:**  
  - Many E90s seep at the low-pressure return hose clamps and reservoir—cheap fix; use new clamps/hoses and correct fluid.

# Minimal test sequence you can perform today

1. **Clean thoroughly** (engine front, housing, belt path, pan seam).  
2. **Short drive (10–15 min)** and re-inspect with a light:  
   - **Wet first at oil filter housing edge →** plan OFHG (+/− oil cooler gasket).  
   - **Wet first at top valve cover corner →** plan VCG.  
   - **Wet first at pan seam with dry upper engine →** plan OPG.  
   - **Wet behind crank pulley →** evaluate front main seal.  
   - **Reddish fluid at PS lines/reservoir →** repair PS hoses/clamps.  
3. **If the belt shows oil sheen**, replace it after correcting the leak.

If you can report back on (a) whether your car is **RWD or xDrive (xi)**, and (b) **where the first fresh dye/talc track appears** (OFHG edge, valve cover corner, pan seam, or crank pulley), I can provide an exact parts list, torque values, and a time-saving order of operations for that specific repair.

## USER
its not above the bottom case, everything above is clean

## Thoughts
It seems the leak could be from the oil pan gasket, front differential (if it's xDrive), or possibly the crank seal. They mentioned the bottom case is clean, so we might look at areas like the oil level sensor o-ring or drain plug. For xDrive, we should also check the front diff seals, including pinion and axle seals, and use UV dye for diagnostic clarity.
It might also be a valve cover rear leak, but since the area above is clean, it’s worth checking a few things in sequence: identifying the fluid type, doing a sniff test, and looking for undertray saturation. For the oil pan, torque specs for the drain plug are around 25 Nm. For the front diff, check the fluid type and level. Let’s focus on those specific steps!
I’ll avoid using the tool that needs citations since it’s unnecessary here. Instead, I’ll stick to crafting a thorough but concise response. I should inquire about drivetrain info (RWD or xDrive), engine model, and transmission type minimally. The main focus is narrowing down the leak source based on fluid type, behavior, and location.
I should focus on a few key areas to identify the leak: 1) Inspect the entire oil pan gasket seam, 360° around. 2) Check the oil level sensor (triangle module) at the right rear of the pan (on N5x) for any dye ring. 3) Inspect the drain plug and 4) Oil cooler lines.

## ASSISTANT
Given that all components above the lower case are clean, the most probable sources are those located at or below the oil-pan plane. Focus your diagnosis on these items first; they account for the majority of “front underside soaked” presentations on the E90:

### Primary candidates at/below the pan
1. **Oil pan gasket (OPG) – engine oil**  
   - Signature: a continuous wet seam around the pan perimeter, often heaviest at the front and corners; drips accumulate on the undertray.  
   - Behavior: worsens after hot drives; upper block and timing cover remain dry.

2. **Oil level sensor O-ring (mounted in the pan) – engine oil**  
   - Signature: localized wet ring around the level sensor flange (typically right-rear quadrant of the pan on N5x); oil tracks forward with airflow and coats the front underbody.  
   - Common after prior service or with hardened seals.

3. **Drain plug/crush washer – engine oil**  
   - Signature: clean pan but oil concentrated at the plug boss and along the pan’s lowest lip; often misinterpreted as a pan gasket leak.

4. **xDrive front differential seals/cover (if xi) – gear oil**  
   - Signature: wetness at the pinion seal (behind the prop flange) or either axle seal; odor is distinctly sulfurous compared with engine oil. Oil may sling onto the lower engine and undertray, making the “front drive” appear soaked.  
   - Also inspect the diff **vent**; a clogged vent elevates internal pressure and promotes leaks.

5. **Power steering low-pressure hose/reservoir weep (ATF on most E90s)**  
   - Signature: reddish fluid originating low near the rack or hose crimps; can coat the same bottom surfaces while everything above appears clean. Confirm by color/odor.

6. **Residual spill retained by the undertray**  
   - Signature: soaked felt/plastic underpanel with no fresh tracks on any metal surface after cleaning; oil can reappear on the tray for days if it wasn’t degreased after an overfill/spill.

---

### Fast discrimination steps (10–20 minutes)
1. **Identify the fluid**  
   - Engine oil: amber/brown, “oil” smell.  
   - Gear oil: dark with strong sulfur odor (front differential).  
   - ATF: red/pink, varnish-sweet odor (power steering on many E90s).

2. **Remove and clean the undertray** thoroughly. Degrease the pan, level sensor flange, drain boss, front diff (if fitted), and surrounding surfaces. Dry completely.

3. **Apply UV dye** to the engine oil (preferred) or use a talc/chalk dusting on suspect seams. Drive 10–15 minutes and re-inspect with a UV lamp:
   - First emergence at **pan seam** → oil pan gasket.  
   - First emergence at **level sensor flange** → level-sensor O-ring.  
   - First emergence at **drain boss** → crush washer/plug.  
   - Dye absent on engine but **fresh wetness on front diff** → differential seal/cover.  
   - Reddish tracks low at the rack/hoses → power steering.

---

### Targeted checks and corrective actions
- **Oil pan gasket**  
  - Confirm with dye along the 360° seam.  
  - Repair entails supporting the engine and lowering the front subframe (more involved on xDrive). Replace the gasket and fasteners as specified for your engine family; clean mating faces meticulously.  
  - After repair, replace any oil-contaminated serpentine belt.

- **Oil level sensor O-ring**  
  - If wet only at the sensor flange, replace the O-ring and torque the fasteners evenly. Clean the connector; ensure no wicking through the harness.

- **Drain plug/washer**  
  - Replace the crush washer and torque the plug to specification for your pan material/plug size. Verify the sealing face is unmarred.

- **Front differential (xi)**  
  - Pinion/axle seals: verify the vent is open; replace the offending seal(s) and refill with the correct gear oil. Inspect the pinion flange surface for grooves before reassembly.

- **Power steering**  
  - Replace weeping low-pressure hoses and clamps and re-seal the reservoir if necessary; refill/bleed with the correct fluid.

- **Residual spill**  
  - If no fresh dye tracks appear but the tray keeps getting oily, the undertray is acting as a reservoir. A thorough degreasing (or temporary removal) usually resolves the recurrence.

---

### Practical next step
Since you report that everything **above** is clean, begin with the **undertray off, surfaces clean, and UV dye in the engine oil.** The first fresh track will isolate the source unambiguously. If you can specify whether the car is **RWD or xDrive** and what fluid you identified by **color/odor**, I can provide a focused parts list and a streamlined repair outline for that exact configuration.

## USER
ok but its from front to back

## Thoughts
The user’s leak could result from engine oil having been blown back by airflow, possibly from a malfunctioning transmission pan or oil filter housing. Residual spills, multiple fluids, or an overfilled PCV may also cause such leaks. Likely sources are the oil pan gasket, level sensor, or transmission seals.
Start by identifying fluid types at multiple points, using oil and UV dye in the ATF or gear oil. Clean the area, take a short drive, and check fluid emergence at the leading edge. Inspect oil cooler lines, especially for RWD vs xDrive models. Airflow likely pushes the leak backwards.

## ASSISTANT
Your description—oil contamination extending “front to back” with all upper engine areas clean—strongly indicates a **low-mounted source** whose discharge is being carried rearward by airflow and along the undertray/tunnel. The correct approach is to localize by fluid type and by the *first* forward-most emergence after a full clean. The following differential and test protocol are tailored for an E90.

### Primary causes consistent with “front→rear” wetting
**Engine-oil sources (front half, below seam level)**
1. **Oil pan gasket (OPG):** Continuous beading at the pan/block interface; heaviest at front corners. Airflow carries oil along the tray and transmission tunnel.
2. **Oil-level sensor O-ring (in pan):** Localized ring-shaped wetting at the sensor flange, then streaking rearward.
3. **Drain plug/crush washer:** Oil collects at the lowest lip and tracks rearward despite a clean upper engine.

**Power steering (ATF on most E90) – low/front**
4. **Low-pressure return hose and reservoir outlet:** Reddish fluid accumulates low, then trails the full length of the underbody. Common and often mistaken for engine oil when aged/darkened.

**Transmission (mid-vehicle)**
5. **ZF 6HP plastic pan/gasket seep or fill/overflow plug:** Broad wetting centered at the pan perimeter; fluid migrates rearward.
6. **ZF mechatronics sleeve (bridge seal) leak:** Fluid originates at the sleeve on the right-rear of the transmission and spreads along the tunnel.
7. **GM 6L45 pan gasket or case connector:** Similar presentation if so equipped.

**xDrive components (if applicable)**
8. **Transfer case input/output seals or case vent:** Film starting at the transfer case, tracking both directions.
9. **Front differential pinion/axle seals:** Gear oil (sulfur odor) slings onto the front underbody, then carries rearward.

**Rear half**
10. **Rear main seal (engine) / bellhousing seam:** Oil first appears at the engine–transmission junction, then coats the tunnel and floor.
11. **Rear differential cover/axle seals:** Originates aft; gear oil odor differentiates it.

**Non-fault scenario**
12. **Retained spill in the undertray:** A past overfill or spill saturates the tray/felt liners; oil releases over multiple drives with no fresh metal-surface tracks.

---

### Rapid discrimination protocol (objective: pinpoint the *origin*)
1. **Remove and thoroughly degrease** the front undertray, pan exterior, level-sensor flange, transmission pan, transfer case (if xi), and adjacent surfaces. Dry fully.  
   *Rationale:* any retained oil will otherwise masquerade as a new leak along the entire underside.

2. **Identify the fluid family before dye:**
   - Engine oil: amber/brown, familiar oil odor.
   - ATF: red/pink when fresh; turns brown with age; varnish-sweet odor.
   - Gear oil: darker; strong sulfurous odor.

3. **Stage 1 UV dye (engine oil):** Add engine-oil UV dye, run 10–15 minutes (idle + short drive), re-inspect with UV lamp.  
   - Fluorescence first seen at **pan seam**, **level sensor**, or **drain boss** → engine-oil source confirmed.
   - No engine-oil fluorescence on metal surfaces, yet underside wet → proceed to Stage 2.

4. **Stage 2 UV dye (ATF):** If the vehicle uses ATF for power steering or you suspect transmission, add ATF-compatible dye to the **transmission** (or to the **PS reservoir** if steering hoses are suspect). Drive 10–15 minutes, reinspect.  
   - Dye at **trans pan perimeter**, **mechatronics sleeve area**, or **PS lines/reservoir outlet** → ATF source confirmed.

5. **If xDrive:** Wipe the **transfer case** and **front differential** clean, then dust the seams/vents with talc. A first damp track at these units indicates a driveline fluid leak (confirm by odor).

6. **Determine the forward-most point of reappearance.** With front-to-rear wetting, the true source is almost always located at, or slightly ahead of, the *first* glowing/damp point after cleaning.

---

### Repair cues from test outcomes
- **Oil pan gasket:** Confirmed by continuous dye line at the seam. Repair requires subframe support; on xi this is more involved. Replace the belt if oil-contaminated.
- **Oil-level sensor O-ring:** Dye local to sensor perimeter only; replace O-ring and clean connector.
- **Drain plug/crush washer:** Replace washer; verify sealing face; torque to specification.
- **Power steering return hose/reservoir:** Replace hose and clamps; refill with specified fluid; clean thoroughly.
- **Transmission pan/mechatronics sleeve:** Replace pan (integrated filter on ZF), sleeve and sealing mechatronic seals; refill and set fluid level at the correct temperature window.
- **Rear main seal:** Dye emerging at bellhousing joint; confirm before undertaking, as labor is substantial.
- **Transfer case/differentials:** Renew implicated seals; ensure vents are open; refill with correct fluids.

---

### Critical precautions
- **Serpentine belt contamination:** Replace any belt exhibiting oil sheen; belt degradation can lead to ingestion past the front crank seal with catastrophic sequelae.
- **Overfill check:** Verify engine-oil level (cluster/iDrive). Persistent overfill can promote pan and rear main weeping; correct the level before retesting.
- **Undertray:** Do not reinstall a saturated tray until it is fully cleaned or replaced; it will otherwise “re-leak” and obscure diagnosis.

---

If you perform the clean-and-dye stages exactly as outlined, the origin will declare itself at the forward edge within one short drive. Once you note **where the first dye appears** (pan seam, level sensor, drain boss, transmission pan/sleeve, transfer case, or differential), the corresponding repair can be planned precisely with parts and torque data for your specific engine/transmission and (if applicable) xDrive configuration.

## USER
ok lets get specific. the lower block down is clean. the turbo oil lines look ok and were replace not long ago.  this appars on both sides. the passenger output case area is covers as is the drivers side transfer case all the way back to the trans and the lower metal that protects the bottom of the engine was soaked

## Thoughts
Based on the user’s request, I’ll follow a formal academic tone. For the diagnostic reasoning on the E90, the oil soaked areas suggest possible issues with the engine oil, transmission fluid, or transfer case fluid. It’s likely the oil from areas like the passenger output shaft or driver's side transfer case.
It seems like the contamination might be linked to the xDrive front differential input seal leaking gear oil and the transfer case, though the oil cooler or thermostat housing could also be involved. The discrepancy between “lower block down is clean” and references to soaked areas could suggest power steering fluid spraying onto both sides, affecting the transfer case.
It seems like there are multiple driveline fluid leaks, likely from the front differential axle seal and the transfer case output/input seal, both causing gear oil leaks (which has a sulfur smell). A good approach would be to check the fluid levels, inspect wetness around seals, and possibly inspect the transmission mechatronic sleeve or pan. Specific E90 points include the right and left axle seals, and potential pinion seal leaks.
For the E90 xDrive, the transfer case is either an ATC300 (early) or ATC35L (later). Common leaks include the input shaft seal, drive flange seals, and case seam. Fluid types to mention: front differential uses SAE 75W-90 GL-5, transfer case uses BMW DTF1. Fluid for power steering may be ATF or CHF 11S, depending on model.

## ASSISTANT
Given your clarification—upper engine clean, turbo feed/return lines recently renewed, contamination present on both sides from the front axle area rearward, under-shield saturated—the presentation is most consistent with **xDrive driveline fluid leaks** rather than an engine-oil leak. Two frequent, sometimes concurrent, sources on E90 xDrive platforms are:

1. **Front differential (integrated to the oil-pan carrier) axle-shaft oil seals**  
   • Especially the **right/passenger output seal**; leakage is centrifuged by the rotating tripod/axle and splays oil across the passenger half of the subframe and undertray.  
   • The **left/driver output seal** can also weep, creating bilateral contamination.  
   • Less often, the **pinion (prop-flange) seal** or the **diff cover/pan interface** (if previously disturbed) is implicated.

2. **ATC transfer case shaft seals or breather** (ATC300/ATC35L depending on build)  
   • **Input seal** (transmission → transfer case) and/or **front output seal** (transfer case → front prop) can mist fluid forward and rearward.  
   • An **obstructed transfer-case vent** raises internal pressure and promotes weeping at multiple seals, yielding a “front-to-back film.”

A third masquerader that can coat both sides is the **power-steering low-pressure return circuit** (ATF on most E90s). However, your note that the “lower block down is clean” and that the contamination originates around the front output and transfer case favors **gear/transfer-case oil** rather than ATF or engine oil.

---

## Rapid source confirmation (objective, non-destructive)

1. **Identify the fluid family at the forward edge of wetting.**  
   • **Gear oil (front diff / rear diff):** dark amber to brown; **strong sulfurous odor**.  
   • **Transfer-case fluid (DTF-1/TF-0870 family):** light amber to brown, thinner than gear oil; odor is less sulfurous, more like ATF.  
   • **ATF/power steering:** reddish when fresh, varnish-sweet odor.  
   • **Engine oil:** familiar engine-oil smell; but your clean upper engine and bilateral driveline wetting argues against it.

2. **Degrease, dry, and dust.**  
   • Remove the undertray. Thoroughly clean the **front diff housing and both axle seal areas**, the **pinion flange**, the **transfer case input and both outputs**, and adjacent crossmembers.  
   • After drying, **dust** the suspects with talc/chalk (or apply UV dye specific to the *suspected* fluid—gear-oil dyes exist, but talc is usually sufficient).  
   • Drive 10–15 minutes; re-inspect. The **first damp track** will reveal origin(s). It is common to find **two** sources: e.g., RH front-diff axle seal **and** transfer-case input or front-output seal.

---

## Targeted inspections you can perform now

- **Front differential:**  
  • Inspect the **RH (passenger) axle seal lip** circumference where the stub enters the housing. Look for a fresh, radial “fan” pattern on the surrounding casting and subframe.  
  • Check the **LH (driver) axle seal** similarly.  
  • Inspect the **pinion/flange area** for sling patterns; grasp the flange and check for perceptible play (excess play accelerates pinion seal wear).  
  • Crack the **fill plug** cold and confirm fluid level at the lower edge of the port; top with the correct **GL-5 75W-90** only to avoid running it low.

- **Transfer case (ATC):**  
  • Examine the **input coupling (transmission side)**: fresh wetting that migrates circumferentially onto the case points to the input seal.  
  • Examine **front and rear output flanges**; look for radial sling patterns and fresh tracking along the case seam.  
  • Locate the **vent** (top of case); verify it is not clogged or capped by debris. A blocked vent often correlates with multi-seal weeping.  
  • Verify fluid level with the specified **DTF-1/TF-0870** equivalent for your ATC variant; never substitute gear oil here.

- **Power steering sanity check (to exclude):**  
  • Wipe the **reservoir outlets and return hose crimps** and the **rack boots**. If these areas remain dry while the driveline housings re-wet, power steering is not the origin.

---

## Probable resolution paths (from most to less likely given your symptoms)

1. **Front differential axle-seal renewal (one or both sides)**  
   • Remove axle from the housing, extract the old seal without scoring the bore, and press a new OE-spec seal to the correct depth (lip facing inward).  
   • Lightly lubricate the seal lip and axle journal during reassembly.  
   • Refill/confirm diff fluid level; road-test and re-inspect.

2. **Transfer-case shaft-seal renewal and vent check**  
   • Replace the leaking **input** and/or **front output** seal(s); inspect the sealing surfaces of the corresponding flanges for grooves and address as needed.  
   • Ensure the **vent is patent**; a restricted vent will recidivate leaks.  
   • Refill with the **correct transfer-case fluid** and perform the level-set procedure at the specified temperature window.

3. **If present, secondary contributors**  
   • **Pinion seal** at the front diff if specific evidence exists (wet yoke and sling), often addressed with a fresh crush sleeve/nut per TIS procedure.  
   • **Power-steering return lines** only if concurrent ATF evidence is detected.

---

## Why this matters now

- **Lubricant starvation risk:** Both the **front differential** and **transfer case** carry limited capacities; modest leakage rates can drop levels below safe limits quickly, risking bearing and gear damage.  
- **Diagnostic clarity:** A saturated undertray preserves and redistributes fluids, obscuring origin. Removing it until the leak is resolved prevents false positives.

---

## Actionable checklist for your next session

1. Remove undertray; **deep-clean** front diff, both axle exits, pinion area, transfer case input & outputs.  
2. **Verify fluid identities** at the forward edge by odor/appearance.  
3. **Talc dust** the cleaned seal perimeters; perform a short drive; re-inspect to identify the **first wet point(s)**.  
4. **Top-off levels** (front diff with GL-5 75W-90; transfer case with the specified DTF fluid) to protect components pending repair.  
5. Plan the **specific seal replacement(s)** indicated by step 3, and ensure the **transfer-case vent** is clear.

If you report which exact interface shows the first fresh track—e.g., “RH front-diff axle seal” and/or “transfer-case input flange”—I can provide a concise parts list (seals, circlips, one-time-use hardware, fluid quantities) and a step-ordered procedure tailored to your E90’s build (ATC variant and differential type).

## USER
whats the best degraser

## Thoughts
To degrease an E90’s underside, options include solvent or water-based cleaners. For safety, ensure products are plastic, aluminum, and rubber-safe, and check oxygen sensor compatibility. Consider products like citrus-based or sodium-metasilicate cleaners and aerosol brake cleaners for precision. Dilution ratios and dwell times are key; avoid oven cleaner on aluminum. Always wear PPE and dispose of waste properly.
Popular options include Simple Green Pro HD, Purple Power, Gunk Engine Degreaser, and more, but avoid over-promising. For safe use, cool the engine, cover sensitive components, and avoid direct spray on O2 sensors. After applying, use low-pressure rinsing, agitation brushes, and compressed air. Follow proper disposal and safety protocols.

## ASSISTANT
Below is a concise, practical selection guide and procedure tailored for an E90 underbody saturated with engine/gear/transfer-case oil. The goal is maximum cleaning efficiency with minimal risk to aluminum/magnesium components, elastomers, and coatings.

### 1) Degreaser types and when to use them
**A. Non-chlorinated brake cleaner (spot cleaning, final rinse)**
- **Use for:** Pinpoint removal on metal castings, fast drying, no water rinse needed.
- **Chemistry:** Hydrocarbon/ketone blends (e.g., heptane/acetone).  
- **Pros:** Very effective on fresh and baked oil films; leaves no residue.  
- **Cautions:** Flammable; avoid prolonged contact with painted/plastic parts and rubber bushings.

**B. Solvent (petroleum/citrus) engine degreasers (bulk grime)**
- **Use for:** Heavy accumulations on differential housings, transfer case, subframe, and the metal belly pan.  
- **Chemistry:** Kerosene/mineral spirits or d-limonene (citrus) with emulsifiers.  
- **Pros:** Excellent on thick, oxidized oil/grease; good creep into crevices.  
- **Cautions:** Requires water rinse; protect rubber if dwell times are long. Work in ventilated area.

**C. Water-based, aluminum-safe alkaline degreasers (wide-area cleaning)**
- **Use for:** Large surfaces after gross soil is removed (engine block exterior, oil pan, crossmembers).  
- **Chemistry:** Surfactants with moderate alkalinity; explicitly labeled “aluminum/magnesium safe.”  
- **Pros:** Safer for painted and light-alloy parts; economical in pump sprayers.  
- **Cautions:** Avoid high-pH heavy-duty products (sodium hydroxide/metasilicate concentrated) on BMW N5x light-alloy cases; rinse thoroughly.

**D. Plastic/felt undertray cleaning**
- **Use for:** The soaked lower shield and acoustic felt liners.  
- **Method:** Hot water + mild detergent (dish soap) or an aluminum-safe APC; multiple rinses. Severely saturated felt is best **replaced**, as it can continue to weep oil.

### 2) Recommended, commonly available choices (aluminum-safe where noted)
- **Brake cleaner (non-chlorinated):** CRC “non-chlorinated” or 3M High Power Brake Cleaner — for spot work and final pass.
- **Solvent engine degreaser:** Gunk Original/Heavy Duty (petroleum) or a d-limonene citrus degreaser — for heavy deposits.
- **Water-based, aluminum-safe:** Simple Green **Pro HD** (purple) diluted **1:3 to 1:5** with warm water; or Purple Power **Aluminum Safe** per label — for broad areas after bulk removal.
- **Electrical contacts only:** Dedicated electrical contact cleaner — dry, no residue.

*(Brand names are illustrative; an equivalent with the same chemistry profile is acceptable.)*

### 3) Field-tested, low-risk procedure (underbody/xDrive housings)
1. **Preparation**
   - Vehicle cool. Remove the undertray. Mask/avoid O₂ sensors, boots, and painted surfaces when using strong solvents. Wear gloves/eye protection.
2. **Bulk removal (solvent phase)**
   - Apply a petroleum or citrus engine degreaser to the differential/transfer-case exteriors and subframe. Dwell 3–5 minutes. Agitate with nylon brushes.  
   - Rinse with **low-pressure** water. Avoid driving water into bearings/seals.
3. **Wide-area cleanup (water-based phase)**
   - Spray aluminum-safe degreaser (e.g., Pro HD 1:3–1:5). Short dwell (1–2 minutes), agitate, then rinse thoroughly.  
   - Repeat once if needed; do **not** allow to dry on aluminum/magnesium.
4. **Spot finishing**
   - Use **non-chlorinated brake cleaner** on stubborn films and to purge seams/crevices. Allow to flash dry.
5. **Undertray**
   - Pressure-rinse both sides, then soak with hot water + detergent. If oil continues to leach after drying, **replace** the felt insert or the entire tray.
6. **Drying**
   - Compressed air (gentle) to remove trapped moisture. A short drive aids evaporation.

### 4) Safety and material-compatibility notes
- **Avoid chlorinated brake cleaners** entirely (hazardous byproducts if heated/welded; material compatibility concerns).  
- **Do not use oven cleaner/caustic soda** on light alloys (risk of dark staining and surface etching).  
- Keep dwell times short on rubber mounts and bushings; rinse promptly.  
- Collect runoff where feasible; dispose according to local regulations.

### 5) Simple decision tree
- **Heavy, tar-like deposits:** Solvent engine degreaser → rinse → water-based aluminum-safe degreaser → rinse → brake cleaner spots.  
- **Light film over large area:** Water-based aluminum-safe degreaser (warm dilution) → rinse → brake cleaner for residual seams.  
- **Electrical connectors:** Contact cleaner only.

If you indicate whether you prefer **solvent-based** (faster on heavy grime) or **water-based** (lower odor, driveway-friendly) products, I can provide exact dilution ratios, brush types, and a shopping list sized for one thorough session.

## USER
anything that will clean the alumnium

## Thoughts
To clean aluminum in automotive contexts safely, use pH-neutral or mildly alkaline degreasers like Simple Green Pro HD. Avoid caustic soda and aluminum-brightening products with hydrofluoric acid. For oxidation, citric acid or oxalic acid works, but remember to neutralize and passivate. Consider buffered alkaline products for aluminum safety.

## ASSISTANT
Below is a safe, aluminum-focused approach for drivetrain housings (front differential, transfer case, transmission pan/case) that are oil-soaked.

### Suitable chemistries (aluminum-safe)
- **Water-based, “aluminum-safe” alkaline cleaners (preferred for broad areas)**
  - Examples: *Simple Green Pro HD* (purple), *Purple Power Aluminum Safe*, *P21S Total Auto Wash*.
  - Rationale: buffered alkalinity with corrosion inhibitors; effective on petroleum soils while minimizing etching.
  - Working dilution: **1:3 to 1:5 (cleaner:warm water)** for heavy soil; **1:8 to 1:10** for maintenance.
- **Citrus/solvent pre-cleaners (for heavy, tar-like buildup)**
  - Examples: d-limonene degreasers; low-odor mineral-spirits products.
  - Use as a short-dwell *pre-soak*, then follow with the water-based cleaner.
- **Non-chlorinated brake cleaner (localized, final pass)**
  - Use only for spot flushing of crevices after the main wash; keep off painted surfaces and elastomers.

### Avoid
- **Strong caustics** (sodium hydroxide / high-metasilicate “purple” degreasers not labeled aluminum-safe): cause dark staining and surface etch.
- **Acidic “aluminum brighteners”** (often fluoride-based): unnecessary for oil removal and hazardous; can undercut the surface and create “smut.”
- **Chlorinated brake cleaners** (toxicity and welding byproducts).

### Procedure (optimized for bare cast aluminum underbody parts)
1. **Preparation**
   - Vehicle cool. Remove the undertray. Plug/cover electrical connectors and rubber boots where practical. PPE: gloves, eye protection.
2. **Gross soil removal (optional, if caked)**
   - Mist a **citrus/solvent pre-cleaner**, dwell **2–3 min**, agitate with nylon brushes. Do **not** let it dry.
   - Low-pressure water rinse.
3. **Primary clean (aluminum-safe, water-based)**
   - Spray **Simple Green Pro HD 1:3–1:5** (warm water improves action).
   - **Dwell 1–2 min** only; agitate with nylon detailing brushes.
   - Rinse thoroughly with **low pressure**; avoid forcing water into seals/breathers.
   - Repeat once if needed. Do not allow cleaner to dry on the metal.
4. **Spot finishing**
   - For seams/bolt heads, use **non-chlorinated brake cleaner** with a straw to flush residual film, then wipe.
5. **Drying and flash corrosion control**
   - Blow off with gentle compressed air; a short drive helps evaporate trapped moisture.
   - If hard water leaves deposits, a quick mist of **distilled water** before the final wipe minimizes mineral spotting.

### If light oxidation (white bloom) remains after degreasing
- Prepare a **very mild citric–surfactant wash** (e.g., 1–2% citric acid in water with a drop of dish surfactant), dwell **≤60 s**, agitate lightly, then rinse copiously and dry. This removes superficial oxide without aggressive attack. Do **not** use strong acids, and always test a small area first.

### Tools that help
- Nylon bore/crevice brushes; soft detailing brushes.
- Low-pressure garden sprayer for even application.
- Microfiber and lint-free shop towels (discard after oil cleanup).

### Practical notes
- Keep dwell times short on aluminum; effectiveness comes from **agitation + repeated light applications**, not soaking.
- Always finish with a thorough rinse and rapid drying to prevent chalky residues.
- If the felt acoustic pads in the undertray are saturated, replacement is preferable; they will continue to leach oil even after cleaning.

If you prefer a specific product family (hardware-store vs. automotive-detail brands), I can translate the above into an exact shopping list with dilutions for a single cleaning session.

