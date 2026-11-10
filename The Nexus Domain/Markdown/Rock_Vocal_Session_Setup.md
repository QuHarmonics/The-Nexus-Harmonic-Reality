# Rock Vocal & Backing Track Session Setup Guide
*Optimized for Waves Ultimate Bundle users*

This document serves as your step-by-step session framework and template guide for tracking and mixing rock vocals over a stereo backing track. 

---

## 1. The Session Structure

Set up your DAW with the following track layout:

1. **[Stereo Audio Track]** - "Backing Track" (Route directly to Master)
2. **[Mono Audio Track]** - "Lead Vocal" (Route to Vocal Bus)
3. **[Mono Audio Track]** - "Vocal Double" (Route to Vocal Bus, pan slightly or leave center)
4. **[Mono Audio Track]** - "Vocal Harmonies / Ad-libs" (Route to Vocal Bus)
5. **[Stereo Aux/Bus]** - "Vocal Bus" (Where all vocals combine before hitting Master)
6. **[Stereo Aux/Bus]** - "FX 1: Slap Delay" (100% Wet effect return)
7. **[Stereo Aux/Bus]** - "FX 2: Rock Reverb" (100% Wet effect return)
8. **[Stereo Aux/Bus]** - "FX 3: MicroShift Width" (100% Wet effect return)

---

## 2. The Waves Plugin Signal Chains

Since you have the full Waves bundle, use these exact "sleeper" and classic chains to make a raw vocal cut through a heavy rock backing track.

### Track 1: The Backing Track
*Rock backing tracks are often pre-mastered and limited. They leave very little "hole" for a raw lead vocal. Use these to carve out space.*
* **Insert 1: Waves Center**
  * *Setting:* Drop the "Center" fader down by -1.5 dB to -3 dB. Boost the "Sides" slightly if needed.
  * *Why:* This pushes the mid-frequency instruments (guitars, snare) to the edges, creating a physical pocket in the center for your voice.
* **Insert 2: Manny Marroquin EQ (or H-EQ)**
  * *Setting:* Take a wide, gentle dip of 1 to 2 dB around **2.5 kHz to 4 kHz**. 
  * *Why:* This is the "presence" zone for vocals. Clearing it out of the backing track prevents masking.

### Track 2: Lead Vocal (The Core Chain)
* **Insert 1: Scheps Omni Channel 2**
  * *Preamp Module:* Turn on the "Heavy" saturation slider slightly to add analog grit.
  * *De-Esser Module:* Engage it to catch harsh 'S' sounds before compression.
  * *EQ Module:* High-pass filter up to 80Hz. Boost a tiny bit of 3kHz for cut, and a shelf at 10kHz for air.
* **Insert 2: Renaissance Vox (RVox)**
  * *Setting:* Pull the gate down to silence background noise. Pull the compressor fader down until you see 3–5 dB of gain reduction on loud notes.
* **Insert 3: MV2 (The Low-Level Compressor Hidden Gem)**
  * *Setting:* Leave the top fader (downward compression) alone. Raise the bottom fader (Upward Compression) to about +3 dB to +5 dB.
  * *Why:* Rock vocals have a massive dynamic range. MV2 will pull up the quiet trailing words and breath details so they remain perfectly audible over loud rock guitars without over-compressing your loud peaks.

### Track 5: The Vocal Bus (Group Processing)
*Route all your vocal tracks here to "glue" them together before the master fader.*
* **Insert 1: Abbey Road TG Master Channels**
  * *Setting:* Choose the "Live" or "Modern" preset, or slight compression using the original EMI console modeling. It adds a thick, expensive-sounding analog top end.
* **Insert 2: PuigChild 660 (or 670)**
  * *Setting:* Fast time constant (1 or 2). Just let the needle dance at less than 1 dB of movement. It provides classic tube warmth.

---

## 3. The FX Sends (Spatial Width & Depth)
*Do not insert delays and reverbs directly onto your vocal tracks. Send them to these Aux tracks via your DAW's bus sends.*

* **FX 1 (Slap Delay): H-Delay**
  * *Setting:* Set delay time to **1/16 note** or a manual MS time between **80ms – 140ms**. Turn feedback to 0 (only 1 repeat). Lo-Fi button ON. 
  * *Why:* Standard rock trick. Gives the vocal immediate attitude and depth without washing it out in reverb.
* **FX 2 (Rock Reverb): Abbey Road Plates (or Renaissance Reverb)**
  * *Setting:* Select Plate B or C. Set pre-delay to **20–40ms** so the raw transient of your vocal escapes before the reverb kicks in. Keep the decay short (1.2s to 1.8s).
* **FX 3 (Width Trick): Abbey Road Reel ADT**
  * *Setting:* Use the "Vocal Double Stereo" preset. 
  * *Why:* It creates a true variable tape-emulated double-track effect. It spreads the voice wide into the stereo field, giving it a massive, modern rock hook feel.

---

## 4. Quick Workflow Checklist
1. **Gain Stage:** Turn down your stereo backing track by about **-6 dB** before you start singing. This gives your vocal chain plenty of headroom so you don't clip your master bus.
2. **DeBreath:** If manual editing takes too long, place **Waves DeBreath** as the very first insert on your Lead Vocal track to automatically pull down breathing noises.
3. **Check Mono:** Toggle your master bus to mono occasionally. Ensure plugins like *Reel ADT* or *Center* aren't causing your vocal to disappear due to phase cancellation.