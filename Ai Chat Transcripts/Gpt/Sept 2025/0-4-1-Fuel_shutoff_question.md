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

