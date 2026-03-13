## USER
nts expert what do i set to read the vo?

## ASSISTANT
To read the **Vehicle Order (VO)** in **NCS Expert**, you need to load the chassis and then read the VO from a module that stores it (usually CAS or LCM). Here's how to do it step by step:

---

### ✅ Steps to Read VO in NCS Expert:

1. **Open NCS Expert.**
2. **File > Load Profile**  
   Load a profile with full access like **"Expertmode"** or **"Revtor’s NCS Expert Profile"**.

3. **F1: VIN/ZCS/FA**
4. **F3: ZCS/FA f. ECU**

   - For E90, choose **E89 chassis** (E89 covers E9x models).
   - Choose the module to read the VO from:
     - **CAS** (Car Access System) is the most common and reliable.
     - **NFRM/FRM** or **LCM** can also hold the VO.

5. Once it reads the VO, you will see the VIN and the full list of VO/FA codes in the main window.

6. Press **F6: Back** to return to the main menu.
7. Now you can use **F4: Process ECU** to code a specific module or **F3: Execute Job** to perform actions.

---

Let me know if you want to **add, remove or change VO codes**, or if you're trying to code a specific module — I can walk you through that too.

## USER
im trying to get my aux woking again and i put in a new head unitl 

## ASSISTANT
Got it — you're trying to get **AUX back working** after installing a **new head unit** in your E90. Let's break it down and get you sorted 👇

---

## 🔧 What You Need to Know:

When you replace the **factory head unit (CCC, CIC, or standard radio)**, the **AUX input** can stop working because:

1. The VO (Vehicle Order) no longer includes the AUX feature (`+MP3` or `+6FL`, depending).
2. The new head unit isn’t coded or doesn’t recognize AUX due to missing configuration.
3. Some aftermarket units bypass the factory audio system and need a separate AUX input setup.

---

### 🔍 Questions to Confirm First:

1. **What kind of head unit did you install?**
   - OEM (e.g., a newer BMW unit like CIC)?
   - Aftermarket (e.g., Android, Sony, etc.)?

2. **Where is your AUX port connected?**
   - Center console port (factory wiring)?
   - Rear of the head unit (new connection)?

3. **Was AUX working with the original unit before the swap?**

---

## 🛠️ If You Installed an OEM Unit (like CIC, CCC, or another BMW HU):

### ✅ Steps to Re-enable AUX:

1. **Read VO with NCS Expert** (just like you’re doing now).
2. Check if these options exist in your VO:
   - `+6FL` – USB/AUX-in
   - `+MP3` – MP3 capability (sometimes required)

3. If missing, **add them to VO**:
   - Go to **FA_WRITE**, write the updated VO back to CAS and NFRM.
4. **Use NCS Expert to code the radio module** (usually **CHAMP**, **CIC**, or **RAD**):
   - Select the module.
   - Use **Job: SG_CODIEREN** to code it with the new VO.

---

## 🛠️ If You Installed an Aftermarket Unit:

- AUX from the factory system likely won't work unless your new unit **accepts AUX-IN directly**.
- You’ll need to:
  - Use the **new head unit’s AUX input** (if available).
  - Connect your 3.5mm AUX cable directly to the new HU.
  - Ignore factory AUX wiring — it’s no longer active unless you're integrating with OEM audio paths.

---

## ⚠️ Pro Tip:

If you're using something like a **MOST-to-analog adapter** or **retaining OEM amp**, the coding might still matter. Otherwise, coding won’t help an aftermarket unit.

---

Want to drop the **exact model of your new head unit** and if it’s aftermarket or OEM? I’ll give you the exact steps tailored to your setup.

## USER
how do i read it agin?

## ASSISTANT
Perfect — here's how to **read your VO (Vehicle Order)** again using **NCS Expert**. This lets you verify if AUX is present in the coding, or prep for adding it back in if needed.

---

### ✅ Step-by-Step: How to Read the VO in NCS Expert

#### 🔌 Pre-req:
Make sure your cable (e.g., K+DCAN) is connected to the car and the ignition is ON (position 2).

---

### 1. **Open NCS Expert**

### 2. **Load a Profile**
- Go to **File > Load Profile**
- Select **“Expertmode”** or **“Revtor’s NCS Expert Profile”**

---

### 3. **Click F1: VIN/ZCS/FA**

This starts the process to load the car’s VO (Vehicle Order).

---

### 4. **Click F3: ZCS/FA f. ECU**

Now you'll select the chassis and where to read the VO from.

- **Select chassis:** `E89` (for E90/E91/E92/E93)
- **Select module:** Choose **CAS**  
  (If CAS doesn’t work, try **FRM**)

> ✅ This will load your VIN and FA/VO string.

---

### 5. **Click F6: Back**

Returns you to the main screen with VO loaded.

---

### 6. **Click F4: Process ECU**  
To choose a module to code or inspect.

Or if you're just reading the VO, you can now:
- Click **F5: Read ECU** (optional)
- Or just go to **F2: Change Job** and run `FA_READ` to dump the current FA/VO.

---

Once you’ve done this, you’ll have the VO loaded and can:
- Check if options like `+6FL` or `+MP3` are present
- Modify the VO if needed
- Code any module (like **RAD** or **CHAMP**) to activate AUX again

---

Need help checking for `+6FL` or want help **editing the VO** and coding a module? Drop what you see and I’ll walk you through it line by line.

## USER


## USER
here is he fa 

## ASSISTANT
Thanks! I see your current **FA/VO string** is:

```
E90_#0909&LCB4%0475*PL33S1CA5203$205$240$249$2SZ$2SZ
```

### 🔍 What's Missing?

You're **missing the VO option for AUX**, which should be either:

- `+6FL` – **USB/AUX-IN** (used in most E9x models)
- `+MP3` – **MP3/AUX capability** (sometimes required)

---

## ✅ How to Fix AUX (Add Back to VO)

To get AUX working again, you'll need to **add the option `+6FL` to your VO** and then **code the radio module**.

---

### 🛠 Step-by-Step: Add `+6FL` to VO

1. **Launch NCS Expert**
2. Load profile: `Expertmode`
3. Press **F1: VIN/ZCS/FA**
4. Press **F3: ZCS/FA f. ECU**
   - Chassis: `E89`
   - Module: `CAS`

5. Press **F2: Enter FA**
6. Add the new option:
   - Scroll to your VO and add `+6FL` (be sure to match the format)
   - New VO:  
     ```
     E90_#0909&LCB4%0475*PL33S1CA5203$205$240$249$2SZ$2SZ$6FL
     ```

7. Press **F6: Back**
8. Use **FA_WRITE** to write the updated VO:
   - Press **F4: Process ECU**
   - Select `CAS`, then **Change job to `FA_WRITE`**
   - Execute
   - Repeat and write to `NFRM` as well

---

### 🧠 Final Step: Code Radio Module

1. In NCS Expert:
   - Press **F4: Process ECU**
   - Select `RAD`, `CHAMP`, or `CIC` (depends on your head unit)
2. Change job to `SG_CODIEREN`
3. Execute the job

---

✅ That will activate the AUX input again (if your wiring is intact and supported by the new head unit).

Let me know what head unit you installed and I can guide you even more specifically.