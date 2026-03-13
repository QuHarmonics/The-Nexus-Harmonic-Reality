# Audio Recording Basics

https://chat.openai.com/c/680af213-a340-8011-8459-d4b827415ee7

## USER
hey lets talk audio recording

## Thoughts
Pulling in details to give the best answer

## ASSISTANT
Hey there! Audio recording is a broad field—everything from podcasting to music tracking to field sound capture. At a high level, you’ll want to think about four key pillars:

1. **Microphone & Capsule**  
   - **Condenser mics** (e.g., large-diaphragm, small-diaphragm) for detailed, studio-style capture  
   - **Dynamic mics** (e.g., Shure SM57/58) for louder sources or untreated rooms  
   - **Ribbon mics** for a smooth, vintage vibe  
   - **Polar patterns** (cardioid, omnidirectional, figure-8) to control what you pick up

2. **Preamps & Audio Interface**  
   - Clean gain is crucial—look for enough headroom and low noise  
   - Interfaces combine preamps with A/D converters; popular entry-level options include Focusrite Scarlett, PreSonus AudioBox, or Audient iD series  
   - Pay attention to sample rate (44.1 vs. 48 vs. 96 kHz) and bit depth (24-bit is standard)

3. **Recording Environment & Mic Technique**  
   - **Room treatment**: foam panels, bass traps, curtains to reduce reflections  
   - **Mic placement**: distance, angle, and room symmetry all affect tone—experiment with the “3:1 rule” (mic-to-source vs. mic-to-mic distance for multi-miking)  
   - For field recording: windscreen, shockmount, and choosing quiet locations

4. **Software (DAW) & Workflow**  
   - Entry-level/free: Audacity, GarageBand, Reaper’s evaluation license  
   - Pro tools: Ableton Live, Pro Tools, Logic Pro, Cubase  
   - Key practices: proper gain staging (aim for −12 to −6 dBFS peaks), naming tracks, color-coding, saving templates

---

**To dive deeper**, let me know:
- What’s the goal? (Music, podcast, voice-over, Foley, field/sound design?)  
- What gear/space do you have right now?  
- Any pain points—noise, hiss, poor room sound, confusing software?  

Happy to help tailor advice to your setup and goals!

## USER
vocal.  so were using pro tools, i dont have access to the real gear (i have a friend Jimmy Boyle has that Neve console i wish lol)  

## ASSISTANT
Alright, let’s get your vocals sitting front-and-center—even if you’re running a stripped-down rig in Pro Tools. Here’s a workflow you can follow from tracking through comping and into a rough mix:

---

## 1. Tracking Setup & Gain-Staging

1. **Mic & Room**  
   - **Pop filter + stand**: kills plosives and keeps your mic distance consistent.  
   - **Reflection filter or DIY panels**: even a blanket behind/around the singer tames room reflections.

2. **Interface & Preamps**  
   - Crank your interface’s gain so peaks hit around –12 dBFS to –6 dBFS in Pro Tools.  
   - If you only have a basic preamp, that’s fine—just avoid digital clipping. Aim for clear, un-distorted peaks.

3. **Pro Tools I/O**  
   - Set your session’s **Bit Depth** to 24-bit, **Sample Rate** to 48 kHz (or 96 kHz if your machine can handle it).  
   - Disable any “auto-gain” on your mic pre; you want manual control.  
   - Use **Low-Latency Monitoring** in Pro Tools (Options → LPM) to avoid tracking delay.

---

## 2. Signal Chain & “Neve” Emulation

Since Jimmy’s rocking the real Neve, here’s how to approximate that vibe in the box:

1. **Preamp Emulation**  
   - Insert a plugin like **Waves Scheps 73**, **Slate VTM**, **UAD Neve 1073** (if you have UAD) or the free **T-RackS White 2A Preamp**.  
   - Dial in a touch of saturation (2–4 dB of “gain” in the emu) to add warmth.

2. **High-Pass Filter**  
   - On an EQ plugin, roll off below 80–100 Hz to clean up plosives and mic rumble.

3. **Gentle Compression (Tracking)**  
   - Use a fast-attack, medium-release compressor (4:1 ratio) with 2–3 dB of gain reduction on peaks.  
   - Good “in-the-box” choices: **Waves CLA-76**, **FabFilter Pro-C 2**, or stock **Dyn3**.

---

## 3. Pro Tools Tracking Template

Build a simple vocal template so you’re ready to go every take:

- **Track “Vox Dry”**  
  - Input → Preamp emu → HPF EQ → Compressor → Record.

- **Track “Vox FX” (Aux Track)**  
  - Send from “Vox Dry” at unity → **Plate/Reverb** plugin (e.g. D-Verb or ValhallaPlate) for performance monitoring.

- **Comp Folder**  
  - Create a bunch of comp lanes under “Vox Dry” for quick punch-in comping.

Save this as a session template so you never rebuild.

---

## 4. Performance & Takes

- **Warm-up**: run through a quick scratch take to get levels and “feel.”  
- **Comping**: record multiple passes, then use playlists to pick the best phrases.  
- **Timing**: if you need tight timing, record to a grid or use Elastic Audio something you can nudge later.

---

## 5. Rough Mix & Polishing

1. **EQ Carving**  
   - Boost presence around 3–6 kHz (+2–3 dB) for clarity.  
   - Cut any honky build-up around 200–400 Hz (–2 dB) if the vocal sounds boxy.

2. **Glue Compression**  
   - On a bus for all vocals, a gentle 2:1 ratio (1–2 dB gain reduction) helps them sit together.

3. **Delay/Reverb**  
   - Short slap delay (80–120 ms) at around –15 dB send for thickness.  
   - Plate reverb at –18 dB send for depth—don’t overdo it.

4. **Automation**  
   - Automate vocal rides: bring gain up on softer words and pull down any peaks.

---

### Quick Checklist

- [ ] **24-bit/48 kHz** session  
- [ ] **Clean gain-staged** peaks around –6 dBFS  
- [ ] **Preamp emulation** + HPF + light comp on record  
- [ ] **Comping playlists** for easy phrase-picking  
- [ ] **Basic EQ and bus compression** on mix  
- [ ] **Delay/reverb sends** for space

---

**What mic/interface are you using?** With that info I can suggest even more tailored settings or free plugins to get you sounding closer to Jimmy’s Neve. Let me know!

## USER
he produced You Ought to Know

## Thoughts
The user mentioned "he produced You Ought to Know," and earlier referred to their friend "Jimmy Boyle" who has a Neve console. I think they might have been joking, since "You Ought to Know" by Alanis Morissette was actually produced by Glen Ballard. So, despite the confusion with the names and the Neve console, it seems they just mixed up the details in the conversation. Maybe they were referencing their friend in a light-hearted way?
It seems like the user is asking about the vocal production technique used on "You Ought to Know," but it’s unclear if they mean their friend Jimmy Boyle or Glen Ballard, the actual producer. They might be curious about gear used for the vocals or how to replicate the sound in Pro Tools. To emulate Ballard’s approach, a good chain would involve a Neumann U67 mic into a Neve preamp, with an LA-2A compressor, 1176, and subtle EQ. Plugins like U87 and Waves 1073 could work.
I need to check the vocal chain used for Alanis Morissette's "You Oughta Know" from *Jagged Little Pill*. To do this, I'll search for details about the microphone, preamp, and any other equipment used, especially focusing on the role of Glen Ballard in the vocal production. I'll use the web to gather up-to-date, trusted sources on this. Once I find reliable information, I'll ensure it's properly cited in the final answer.

## Thoughts
We know that Glen Ballard produced the album, with Chris Fogel engineering and Jimmy Boyle as an additional engineer. Vocals were recorded at Westlake in Los Angeles. I should confirm the specific vocal chain used, especially around equipment such as the Neumann U48 and LA-2A, as well as any other details. I’ll search for information to ensure that the chain for vocals on *Jagged Little Pill* is accurate, especially regarding the gear used by Ballard.

## Thoughts
Glen Ballard produced "You Oughta Know," and vocals were recorded at Westlake with Chris Fogel and Jimmy Boyle involved in the engineering. Since the user mentioned using Pro Tools, they may want help replicating the vocal chain. The vocals on the song were recorded with Neumann U67/U87 mics into a Neve 8078 console. I can guide them on replicating that in Pro Tools. Just to clarify, the credited producer is Glen Ballard, not Jimmy Boyle.

## ASSISTANT
Glen Ballard—who produced “You Oughta Know” for Alanis Morissette’s *Jagged Little Pill*—tracked Alanis’s vocals at Westlake Studio in Los Angeles (with additional work at Signet Sound) and Chris Fogel engineered and mixed the session (with Jimmy Boyle contributing the “Jimmy the Saint Blend”) citeturn3search0turn3search7.  Since you’re in Pro Tools without access to that Neve console and outboard chain, here’s how you can approximate that raw-edgy, in-your-face vocal:

1. **Capture a clean dry track**  
   - Record to at least 24-bit/48 kHz (or higher).  
   - Use a good condenser mic (e.g. Neumann U 87/U 67 emulation) into a clean mic preamp plugin.

2. **Mic preamp emulation**  
   - Insert a Neve-style preamp plugin (e.g. UAD Neve 1073, Waves CLA-1073).  
   - Drive it lightly to taste—just enough to get that subtle transformer coloration.

3. **Compression chain**  
   - **First**, gentle leveling with an optical compressor (Teletronix LA-2A emulation)  
     • 3–5 dB of gain reduction on peaks.  
   - **Second**, fast-attack FET compression (1176-style) for presence  
     • 4:1 ratio, medium attack (around 5 ms), release auto—2–3 dB of gain reduction.

4. **De-essing**  
   - Tame any harsh “s” sounds with a de-esser plugin.  
   - Focus on 5–8 kHz; pull down only as much as needed to control spikes.

5. **EQ for clarity**  
   - **High-pass** at ~80 Hz to clean up low-end rumble.  
   - **Boost** ~3–5 kHz by 2–3 dB for intelligibility.  
   - **Scoop** around 200–300 Hz if the vocal sounds “muddy.”

6. **Saturation/Exciter (optional)**  
   - A touch of tape or tube saturation (e.g. Soundtoys Decapitator) to add harmonic richness.

7. **Reverb/Delay**  
   - **Short plate** reverb (Lexicon 480L or emulator) with <1 s decay, mixed in around 10–15%.  
   - **Slap‐back delay** (80–120 ms) can glue the vocal into the track; keep it subtle.

8. **Automation**  
   - Ride the vocal level manually in Pro Tools to keep it upfront—Glen Ballard’s mixes were known for dynamic, expressive vocal rides rather than over-reliance on extreme compression.

By combining clean tracking, a Neve-style pre, a classic LA-2A → 1176 compression chain, tasteful de-essing/EQ and a bit of plate reverb, you’ll get very close to that upfront, raw quality of “You Oughta Know” without needing the original Neve console.

## USER
nice and remember wiki anyone can put anything. lies are emergent, truth is in the silence.  Ok I have Shecps 73 is that the same as 1073?

## Thoughts
The Scheps 73 plugin by Waves, created by Andrew Scheps, emulates the Neve 1073 preamp but isn’t exactly the same as Waves' 1073 plugin. It's a 73-style channel with an EQ and preamp, and it includes two emulations: Scheps 73 and Scheps RS56. While it’s derived from the Neve 1073, it's not the exact same as Waves' 1073 plugin. Additionally, it incorporates features from the API 550a and its sibling, the Scheps Omni Channel.

## ASSISTANT
Yep—Waves’ Scheps 73 is Andrew Scheps’s take on the classic Neve 1073 channel strip (preamp + EQ) and will slot right in as your “1073 emulation.” It gives you that same punchy, mid-forward coloration. 

**How to use it in your chain:**  
1. **Insert Scheps 73** as the first plugin on your vocal track.  
2. **Drive the input** gain until you hear a little transformer saturation—don’t clip, just aim for a warm “soft-edge.”  
3. **Set the EQ** to taste:  
   - Low-cut at 80 Hz  
   - +2–4 dB at ~3 kHz for presence  
   - Maybe a gentle bass shelf around 80–120 Hz if you need body  
4. **Follow with your LA-2A → 1176** chain and the rest of the vocal recipe we covered.

That’ll get you as close as you can in the box to that Neve-driven “You Oughta Know” vibe without Jimmy’s actual console.

## USER
let start from the beginning. any good skeketons to download to setup my project?  this is vocal only

## ASSISTANT
Here’s a super-lean Pro Tools template you can grab, customize and start every vocal session with—no clutter, just what you need:

---

## ▮ Session Folder Structure
```
YourProjectName/
├─ Audio/                 ← your recorded takes go here
├─ Session File.ptx       ← your session template
├─ Templates/             ← store your .ptx templates
└─ Exports/               ← bounces, stems, final mixes
```

---

## ▮ Pro Tools Template: “Vocal Only.ptx”

| Track Name     | Type       | Plugins (Insert 1–3)                                    | Sends & Routing                |
| -------------- | ---------- | ------------------------------------------------------- | ------------------------------ |
| **Vox_In**     | Audio      | 1. Scheps 73 (preamp emu) <br>2. HP Filter @80 Hz         | —                              |
| **Vox_LA2A**   | Audio      | 1. LA-2A (leveling)                                      | —                              |
| **Vox_1176**   | Audio      | 1. 1176 (fast attack)                                    | —                              |
| **Vox_DeEss**  | Audio      | 1. De-esser (5–8 kHz)                                    | —                              |
| **Vox_Eq**     | Audio      | 1. Param-EQ (3–5 kHz boost, 200 Hz cut)                  | —                              |
| **Vox_Sat**    | Audio      | 1. Decapitator (or tape sat)                            | —                              |
| **Vox Bus**    | Aux (Stereo) | —                                                      | Input: Post-1176 send @100%    |
| **Reverb**     | Aux (Stereo) | 1. Plate Reverb (D-Verb, Valhalla)                      | Input: Vox Bus send @–18 dB    |
| **Delay**      | Aux (Stereo) | 1. Slap Delay (80 ms, analog style)                     | Input: Vox Bus send @–15 dB    |
| **Vox_Group**  | Audio (Folder) | —                                                    | All Vox_* tracks routed here  |

> **Notes:**  
> • Set all faders at 0 dB (unity).  
> • “Vox_Bus” is a dry-only bus so you can parallel-compress or pre-fade.  
> • Color-code all “Vox_” tracks red, Aux sends blue.

---

### ▶️ How to Install

1. **Create a blank session** in Pro Tools with your desired sample rate/bit depth (48 kHz/24-bit).  
2. **Build the tracks** exactly as above (Name → Type → Inserts → Sends).  
3. **Save As Template…**  
   - File → Save as Template → name it “Vocal Only”.  
   - When you start a new session, choose File → New Session from Template → “Vocal Only”.

---

### 🔗 Free Downloadable Templates

If you’d rather start from someone else’s ready-made skeleton:

- **Pro Tools Expert**:  
  https://www.pro-tools-expert.com/free-vocal-template  
- **Produce Like A Pro**:  
  https://producelikeapro.com/free-vocal-session-template/  
- **Splice**:  
  https://splice.com/blog/free-pro-tools-templates

---

With this in place, every time you launch Pro Tools you’ll have your entire vocal chain, routing and aux sends ready to roll—just hit record and sing. Let me know if you want a step-by-step walk-through on setting up any of those plugins or routing!

## USER
ok i have this.  lets start with setting the mic input, shecp 73? on vocal input

## Thoughts
To set up the mic input and use the Scheps 73 plugin on your "Dry Vocal" track: 

1. Select the "Dry Vocal" track.
2. Assign its input to your audio interface's mic pre (e.g., Input 1).
3. Record-enable the track.
4. Activate input monitoring.
5. In the mixer, find the insert slot for the Dry Vocal track, and load the Scheps 73 plugin there.

These steps will get your mic input configured and the plugin inserted properly. Let me know if you need further help with this!

## ASSISTANT
Alright, let’s get your Dry Vocal track ready to record through Shecps 73. Here’s a quick step-by-step:

1. **Open the Mix window**  
   Press **Cmd +=** (Mac) or **Ctrl +=** (Win) to pull up your Mix view.

2. **Select your Dry Vocal track**  
   Find the track labeled **Dry Vocal** (it’s the cyan one in your screenshot).

3. **Assign the Mic Input**  
   - In the **I/O** column on that track you’ll see something like `In 1-2`.  
   - Click that, then choose the mono mic pre you have plugged into (e.g. **Input 1**).  
     - If your interface is feeding a stereo channel, pick **1-2**; if it’s a single-channel mic pre, pick **1** (Mono).

4. **Enable Input Monitoring & Record**  
   - Click the little **I** button on the Dry Vocal track so you can hear yourself.  
   - Click the **R** (record enable) button so Pro Tools will arm that track.

5. **Insert Scheps 73**  
   - In the first insert slot of that track (Insert A-E1), click the blank slot.  
   - Navigate to **Waves → Scheps 73 → Scheps 73 (Preamp)**.  
   - That loads the plugin in “preamp” mode.

6. **Set Your Shecps 73 Gain & EQ**  
   - In the Scheps 73 UI, switch to the **Preamp** section (tab at top).  
   - Turn up the **Input** knob until you see a few dB of warm saturation (watch the plugin’s meter—not Pro Tools’—stay under +6 dB).  
   - Leave the EQ flat for tracking, or engage the **High-Pass** around 80 Hz right here if you want to kill rumble immediately.

7. **Bypass Everything Else for Now**  
   - Make sure your LA-2A, 1176, de-esser, etc. are either bypassed or turned off so you get a clean Shecps 73-driven sound to start.

8. **Test & Adjust**  
   - Speak or sing into mic.  
   - Watch the Scheps 73’s input meter and your Pro Tools levels (aim for peaks around –6 dBFS).  
   - Tweak the Scheps 73 **Input** and your interface gain until it sounds juicy but not distorted.

Now your vocal is being tracked through the Scheps 73 emulation—just like a 1073 on the console, but in the box. Next we’ll layer on light LA-2A and 1176 compression once your dry take is solid. Let me know how it sounds!

## USER


## ASSISTANT
Okay—let’s wire up your Dry Vocal track so you can actually hear the mic through the Scheps 73 emulation. Here’s exactly what to do in Pro Tools:

---

### 1. Assign the Hardware Input

1. Switch to the **Mix** window (⌘ = on Mac / Ctrl = on Windows).  
2. Locate your **Dry Vocal** track (the one with Scheps 73 in Insert A).  
3. In the **I/O** column under **Input**, click the current selector (it probably says “–” or “In 1-2”).  
4. From the popup, choose the mono input your mic is plugged into (e.g. **Input 1 (Mono)**).  
   - If you’re on a stereo channel strip you can pick **1-2**, but vocals usually run mono on a single pre.

---

### 2. Arm & Monitor the Track

1. Click the small **R** button on the Dry Vocal track to **Record-Enable** it.  
2. Click the **I** (Input-Monitor) button so you can hear yourself.  
3. In the transport bar, make sure you’re not rolling—you just need playback on to hear the live input.

---

### 3. Meter the Plugin

1. Open the **Scheps 73** plugin window (you already have it open).  
2. On the Scheps 73 interface, find the little **METER** switch above the Input and Output faders.  
3. Toggle it to **IN**—this meters the signal **before** the EQ section so you can see your incoming level.

---

### 4. Set Your Levels

1. With your singer talking/singing into the mic, watch the Scheps 73’s **Input** meter.  
2. Slowly turn up the big **INPUT** knob until the plugin’s VU meter hovers around **0 dB** (aim for peaks around +3 to +6 dB on the plugin).  
3. Keep an eye on your Pro Tools track meter too—try to stay under **–6 dBFS** on the Pro Tools meter to leave headroom for later processing.

---

### 5. Bypass the EQ for Tracking (Optional)

- If you want a totally flat tracking sound, press the **EQ** button (bottom of the Scheps 73) to bypass the Low/Mid/High knobs while you record. You can dial the EQ in later if you prefer.

---

That’s it! Now your Dry Vocal track is receiving the mic input, routed through Scheps 73, and you’re monitoring the preamp’s coloration live. Next up, when you’ve got a clean take, we’ll flip on your LA-2A → 1176 compressors and dial in your vocal chain.

## USER
ok lets balance the input, where shuld the interface be set?

## ASSISTANT
You want your interface’s preamp knob set so that you’re coming into Pro Tools at a healthy but not hot level (leaving plenty of headroom for your in-plug processing). Here’s a quick recipe:

1. **Interface Trim → –18 dBFS Peaks**  
    Speak or sing as loud as you’ll perform and slowly turn up your interface’s gain/trim pot until your Pro Tools **track meter** is averaging around **–18 dBFS** on “louder” syllables, with occasional peaks not exceeding **–12 dBFS**.  

2. **Plugin Input → 0 VU**  
    With your interface trim locked in, switch your Scheps 73 meter to **IN** and turn the Scheps 73 **Input** knob until the plugin’s VU meter sits around **0 dB VU** on those same loud syllables.  

3. **Output → Unity**  
    Finally, set Scheps 73’s **Output** so you’re back at roughly the same Pro Tools level as you had with the plugin bypassed (0 dBfs in ≈ 0 dBfs out).  

---

| Stage             | Target Reading           |
| ----------------- | ------------------------ |
| Interface trim    | –18 dBFS RMS (peaks –12) |
| Scheps 73 Input   | 0 dB on its VU meter     |
| Pro Tools meter   | peaks ≤ –6 dBFS          |

That way you’re clean into the box, then letting the Scheps 73 do its coloration and you’ll still have plenty of headroom for the LA-2A, 1176, de-esser, etc.

## USER
whats next

## ASSISTANT
Now that your preamp emulation is sitting at the right level, let’s get your tracking chain ready. We’ll keep it simple—just two compressors in series to tame peaks and glue the sound.

---

## 1) Insert the LA-2A

1. On your **Dry Vocal** track, go to **Insert A2** (right after Scheps 73).  
2. Click → **Waves → CLA-2A** (or your preferred LA-2A).  
3. In the plug-in UI:  
   - Switch to **Opto** or leave in “Classic” mode.  
   - Turn the **Peak Reduction** knob up until the meter shows about **2–3 dB** of gain reduction on your loudest notes.  
   - Adjust the **Gain** (Output) so your overall level sits back at unity in Pro Tools.

> **Pro tip:** Meter the LA-2A in **GR** mode—make sure you’re not crushing more than 4 dB on transients here.

---

## 2) Insert the 1176

1. Next, on **Insert A3**, load **Waves → CLA-76 (Blackface)** or your 1176 emu.  
2. Set it up for fast “vocal” control:  
   - **Ratio:** 4:1  
   - **Attack:** 3 (fast)  
   - **Release:** 6 (medium)  
3. Drive the **Input** until you see **3–5 dB** of gain-reduction on the meter during louder exclamations.  
4. Bring the **Output** level back up to unity with the bypassed level.

> **Why both?** The LA-2A smooths and levels, the 1176 snaps on fast peaks for that “in-your-face” energy.

---

## 3) De-essing

If you notice harsh “esses,” slip a de-esser in **Insert A4** (or on a send):  
- Target around **5–8 kHz**  
- Dial threshold so you’re only grabbing 2–4 dB on “s” sounds.

---

## 4) Quick EQ Trim

Finally, a gentle cleanup EQ in **Insert A5**:  
- **High-pass** at 80–100 Hz  
- Maybe a **–2 dB** cut at 200–250 Hz if it’s muddy  
- A **+2–3 dB** shelf/peak at 3–5 kHz for extra presence  

---

### Recap of Your Dry Vocal Chain

1. **Insert A1:** Scheps 73 Preamp (balanced & colored)  
2. **A2:** LA-2A (2–3 dB GR)  
3. **A3:** 1176 (3–5 dB GR)  
4. **A4:** De-esser (5–8 kHz, 2–4 dB on sibilance)  
5. **A5:** Cleanup EQ (HP @80 Hz, gentle sculpting)  

Once that’s in place, record a take and listen back—tweak each stage so you’re getting about 5–8 dB total compression but preserving the vibe. After you’re happy, we can set up your parallel bus for saturation, reverb sends, and start comping. Let me know how it feels live!

## USER
la2a is in and its kinda tinny

## Thoughts
The user is saying the signal sounds "tinny" after inserting the LA-2A. Next steps should focus on adjusting the tone. I can suggest tweaking the preamp’s EQ, LA-2A settings, or trying corrective EQ. It might help to adjust the low-end or high-end frequencies, and be mindful of the plugin order. The HP filter or gain can also influence tone quality. Additionally, using the Scheps 73’s EQ, or a parametric EQ after the LA-2A to address harsh high frequencies, could help smooth things out.

## ASSISTANT
Let’s tame that harshness right away by pulling some top end and beefing up the bottom of your tracking chain. You’ve got two places to do it:

---

## 1) Sculpt in the Scheps 73 Preamp

You left the Scheps 73’s EQ flat for tracking—let’s turn it on and dial in a bit of warmth:

1. **Open Scheps 73** on your Dry Vocal track (Insert A1).  
2. Click the little **EQ** button at the bottom so the three blue/grey/silver knobs engage.  
3. **Low Shelf (blue knob)** at 60 Hz: bump up **+2 dB** for body.  
4. **High Shelf (silver knob)** at 12 kHz: pull down **-2 dB** to soften the sheen.  
5. (Optional) **High-pass (HP) switch**: engage at 80 Hz to kill any sub-rumble that can make the top end sound relatively brighter.

That should shift some focus back to the chest and away from the tinsel.

---

## 2) Add a Corrective EQ After the LA-2A

If you still need to notch out brightness post-compression:

1. On **Insert A3** (right after your LA-2A), load **AAX → EQ III 7-band** (or your favorite parametric EQ).  
2. **High-pass** at **80 Hz** (shelf or first band).  
3. **Bell** around **4–6 kHz**, cut **-2 to -4 dB** with a medium Q (~1.2). That’s the “tinniness” zone.  
4. **Shelf** at **200 Hz**, boost **+1.5 dB** to reinforce some warmth if you pulled too much low end earlier.

---

### Quick Recap

| Stage             | Knob / Band         | Change        |
|-------------------|---------------------|---------------|
| **Scheps 73**     | Low @ 60 Hz         | +2 dB         |
|                   | High @ 12 kHz       | –2 dB         |
|                   | HP switch           | 80 Hz engage  |
| **EQ III (A3)**   | HP @ 80 Hz          | shelf/band    |
|                   | Bell @ 4–6 kHz      | –2 to –4 dB   |
|                   | Low-shelf @ 200 Hz  | +1.5 dB       |

After that, go back and check your LA-2A gain-reduction—if it was grabbing too much of the mids or lows you might need to back off a hair (aim for only 2–3 dB GR). But ninety-nine times out of a hundred, a little top-end cut in the pre or post-EQ will fix “tinny” right up. Give it a try and let me know!

