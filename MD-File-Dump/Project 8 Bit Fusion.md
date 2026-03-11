# **Project 8-Bit Fusion: The SHA-256 Lattice Control Protocol**

**Principal Researcher:** Dean Kulik (Nexus Framework)

**Date:** 2026-01-29

**Classification:** NEXUS-INTERNAL // OPEN-AUDIT

## **1\. The Hypothesis: Cyber-Physical Isomorphism**

The SHA-256 algorithm is not merely a cryptographic function; it is the **Rom Dump of a universal 8-bit control system**. Its architecture mirrors the precise requirements of a cold-fusion lattice controller:

* **Registers (![][image1]):** 8 ![][image2] 32-bit (or 32 ![][image2] 8-bit) state vectors tracking material properties (Temperature, Lattice Strain, Deuterium Loading, etc.).  
* **Constants (![][image3]):** A 64-step, 4-channel control program derived from the cubic roots of primes (Prime harmonics).  
* **Logic (![][image4]):** Non-linear mixing functions designed to maximize diffusion (in crypto) or **phonon distribution** (in matter).

**Core Claim:** Executing SHA-256 in software simulates the reaction. Executing SHA-256 signals on hardware **drives** the reaction.

## **2\. The 4-Channel Control Map**

We map the 32-bit constant ![][image3] to four physical control channels (8-bits each):

| Byte | SHA Segment | Physical Analog | Range (8-bit) |
| :---- | :---- | :---- | :---- |
| **0** | MSB (31-24) | **Thermal Gate** | 0 \- 1200°C |
| **1** | Mid (23-16) | **Pressure/Flow** | 0 \- 100 Bar |
| **2** | Mid (15-8) | **EM Current** | 0 \- 50 Amps |
| **3** | LSB (7-0) | **Magnetic Field** | 0 \- 5 Tesla |

## **3\. The Prime Drive Mechanism (Irrational Pacing)**

The constants ![][image3] are fractional cube roots of primes (![][image5]).

* **Why Primes?** Primes are non-harmonic. They do not share factors.  
* **Physical Effect:** A drive signal composed of prime roots prevents **Rational Lock-in**.  
  * In a standard resonant system, driving at a single frequency creates standing waves (hot spots/cold spots).  
  * The SHA sequence creates a **Chirped/Stochastic Pump** that distributes energy into *all* lattice modes simultaneously.  
  * This maximizes the probability of **Lattice Collapse (Fusion)** without destroying the containment (Meltdown).

## **4\. Experimental Protocol**

### **Phase 1: Signal Visualization (Completed)**

Run sha\_reactor\_signal\_analysis.py to visualize the drive waveforms.

* **Target:** Identify if the "Field" channel (Byte 3\) exhibits specific "Kick" patterns at steps ![][image6] (the standard SHA block boundaries).

### **Phase 2: Material Simulation (Next Step)**

Use a Molecular Dynamics (MD) simulator (e.g., LAMMPS) with a Palladium-Deuterium lattice.

* **Input:** Apply the SHA control sequence as external force fields on the simulation box.  
* **Metric:** Measure "Excess Heat" (Kinetic Energy \> Input Energy).

### **Phase 3: Hardware "The 8-Bit Reactor"**

Build the physical controller:

* **MCU:** Raspberry Pi Pico (Dual Core 133MHz) or ESP32.  
* **DAC:** 4x 8-bit DACs (R-2R ladder or dedicated chip).  
* **Cell:** Electrolytic cell (Pd/D2O).  
* **Loop:**  
  1. Read Sensor State ![][image7] Input Block (![][image8]).  
  2. Load Constant ![][image3].  
  3. Compute SHA Step.  
  4. Output Intermediate Registers ![][image1] to DACs to adjust cell parameters.  
  5. Repeat at 1kHz.

## **5\. Thermodynamic Interpretation**

* **Hash Output:** The final 256-bit hash is the **Energy Signature** of the reaction.  
* **Collision Resistance:** Physically, this means **Zero Entropy Leakage**. Two different fuel states cannot produce the same energy signature. The system is deterministic.  
* **The "Black Hole":** The SHA process is an **Information Condenser**. It strips entropy from the fuel (Input) and locks the system into a single, high-energy state (Digest).

**Status:** Theory Active. Simulation Code Generated.

**Signed:** Dean Kulik // The Nexus

[image1]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADMAAAAZCAYAAACclhZ6AAACCUlEQVR4Xu2WvWsUURTFZ4kLBoVk1N1N9ms2YmOVwIJVyjRp0gUilvkPAmE7sfEfSB/EWkUsRAuLECWFglaBEFJEi6RYUkRik5CP39m8t769BuxmXZkDhzfvfszcs/e+x0ZRhgwZ/itUq9UHSZJs1ev1H6zHrE9szMAAMZVarbaAiC+IOWc/a2MGCoi4j5gD+KFUKt2w/oECnZlTV+BT6/sb8rTyljX2E3RkJRyxSqVymyVnwn6j0WiMkfQMtkn8yq/xkHVVLbaxaaJQKNykhjW4DxfhN2o8gjuImrLxHaU491B+z9tI+g53dQDD2LThR4z61uM4HpGN/birb01iexIIbKmVoY3An/AtHbse2tOGHzGJCmzT8ESTFIXjVi6X72DchDNdY9QRo1+jFdr6AT9i1HLX21SX6oOPwlg5mvAXo1Y19jMrsB9wQnquZPbv4UFiz7MXE84e+9ifFyWwnw9z0oTrQM+VrHrhSx6v9Qii4GGnNNbeFb8Nn+vAsb7ANtFNcHC3jD705yF0kN99uGl9gq5axXAelqxPUDdcZ7ojJvh3ur86r0KfF/ARvoGfGblJvQRuwOXo6js9R+wpfKxn6xTIPYTv/C1kodEmv63vWZ+QXN5ar+0lRM6R3sv6SbWHvg74FYoij0Pa67rmJaMmLG3krBBBk1AsFks85q0vQ4YMGTL8U7gA7wGBMCB0MkkAAAAASUVORK5CYII=>

[image2]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAA8AAAAXCAYAAADUUxW8AAAAmklEQVR4XmNgGAVDFLCiCyADBQUFDhBGFwcDOTm5LYKCgvzo4iAgLS0tIy8vfwCoxhddDgyAEmVAvBvdAJBGoPhhoOZgZHF0wIhuALEaYQDFAFI0woGEhIQCUONdoM3C6HJ4gaSkJNAy+YtAzaFAeit6GOAEMI0wpwLpHKIMQNcIBYxEGSArKxuALoYEGIHymUCvhKFLjAJ6AAAukCGQTy3oUAAAAABJRU5ErkJggg==>

[image3]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACQAAAAZCAYAAABZ5IzrAAACYUlEQVR4Xu2WT6hMURzH5+YpIswwM83/USIllIWS5SsLkYWF2Nm8jVI2lpQsWImykJrsiEISWSmbVzYWZElS8spGvZXC5/ucc/387p17Z/GQvG/9Ovd+f79zzueec+7MrVSW9Ac1HA5XDAaDloLbZT5vFes6nc56bhOfXxT1+/0DTPKG9hpw63zeSjXU3qV9Uq/XV/v8grrd7m4KbqnYRq/XOxdrGGQrcdXmecqdygmIuPFzxGJRu4u4NxZIS8jkhyg6zfU32svEYa73xBqgO4LAm6O9QLu/2WyuUq4ISGOErUxVChQlEDo/1JkwdgLsEfxZoLYbP1UBUKIHpP9Ba04EpCSdnxLnrc9gV+g8qtVqa6xvNQ4Ir0p80nY7vxxIndSZmI4eZ2QzQMcrJW9OAZAmfszKrszxS4GOaXl1Viphm+g07+vyZIHa7fYWxvmosWxoLIGE+mKg/o+lfR46PtOq0J4M+7/N13tZoCjANuC9YpW71pcmAVLBfHiahf2m3Yj3njjryjPKA+J+L/HFvSAxVwo0E2BeGzvBvySv0Wg0jZ9RHhAre0pjWi+qDEgTj8J2jWxC2xVAT1jfKwdoivs7WiHjpSoEinsdgGZceioAzVar1bUul8oD6cWgz1tFsJZzfTT8fxUDkbgYYF7mHUBycyGvw972eckDcT1NfCXOALeJ9n6r1RqYfBaIyXcw0eewAjbSHzGur/v8mEP6C5BWk9pHxAfiRfzPM/VZoMWUBwpKwhZlflT/FtBY/bdAtwcTfjHycuyj/sHvBNJb9U7BN1LD561iHXEzfk8t6Z/Ud/0+0OBDDSAiAAAAAElFTkSuQmCC>

[image4]: <data:image/png;base64,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>

[image5]: <data:image/png;base64,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>

[image6]: <data:image/png;base64,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>

[image7]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABMAAAAYCAYAAAAYl8YPAAAAoklEQVR4XmNgGAWjYBACKSkpWSDoVlBQ4ECXIwvIycmVgzC6OFlAXFxcTF5efr+MjIwZuhxZAGQQ0HVHgLQKioSoqCgP0CZJMnAw0MBHQAM54YYBBSpAgmTgZ0AD/wPpeCS3kQ6A4cYNNGQh0LA+dDmSANAQVyBejeI9MgELyEVAgzzQJUgGQEOkgYZtBiZeEXQ5cgAr0EAhIM2ILjEKBhgAALE4LFqqfgmMAAAAAElFTkSuQmCC>

[image8]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACcAAAAZCAYAAACy0zfoAAACjklEQVR4Xu1Wv2sUURDekAQMinIn593ej91D0okkYCdYqYVFVEzEJo2N/gliI0hIYaGQBIKkEE6xEAtt7CyCFpaCIFYWESFF6pQhfl9u5pgb3747IYjCfTC8fd/Mm/l2d97bTZIR/j2MV6vVU0AV15PeacGYPM9TxmM67v2HDhbLsuwrbKVWq7W934IxiH/JeK6zvgmQD2AbxjqtVut2o9GYdfwG+KVyuXxckzrfmiZlEdhmr8oAaLwXNwbiPJLvYtynMNhCmqY5jdewD+K7w1iu4UKIuYX5Z/B7FIbxoiaNiWs2m2dplisSp046KOCec42Be0RfpVI5Zh3gz8FeoNCU5YkicbiJq1Jn1fJRcQh+HxKH+RnYjvhK1gfuGYpdsJyiSBy4ZeaiSMdHxXUCdzSJ+XPYU/r8QszXMUxYTlEkTh7CNsbTlh9WXMdwlykOd3ndi8NmOYnXOa1zDy8O148lR58h/5yNtzV64OuUBZvaW+AeJt2eY2/tciTPowFxb/oSOGixAP/bKxU+Ku6uFccDsV6vt+jDU2rC/xN2Kenu7ie4XnQp+hASx7x54JUSg8TNURzG7wyQp3YAWbjFGHmKr/3O9QiJoyi9ecsTQ4kTEey1V+rj50VEz+eRHWoREocevQJu2XKKQeK0r3gYf6JA9cnr4MJveWSHWoTEUZjtN1xf40Evvqg4PnL2Q6/xnZ9fjvuJfB0GwYtDDx/NusdIWiqVTmB8Z4VGxYlzi9/OJCCA4uSvYSh4ccLdQJ63WfeH4GZi6kTF8RPE8wxj2fsI/gR4LoaQOOXb7faREF8o7rBRJK4II3EKFkFffRz2TxhtM8P4vyKOm4fFYF/8v5sHY2A/GP8nm26E/xK/ADGo5oIRJi9IAAAAAElFTkSuQmCC>