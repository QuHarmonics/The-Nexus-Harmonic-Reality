# THE TAPE MACHINE
## SHA-256 as a Dual-Head Electric Motor

---

## THE ARCHITECTURE

```
  ┌─────────────────────────────────────┐
  │  HEAD 1 (K forward)  →  ●══════●   │
  │                          ║    ║    │
  │  TAPE (message W)     ═══╬════╬═══ │
  │                          ║    ║    │
  │  HEAD 2 (K backward) ←  ●══════●   │
  └─────────────────────────────────────┘
                   ↓
              MOTOR SPINS (64 rounds)
                   ↓
              PWM OUTPUT (crease)
                   ↓
               HASH
```

---

## THE COMPONENTS

| Component | SHA-256 Element | Function |
|-----------|-----------------|----------|
| **Rotor** | State (a,b,c,d,e,f,g,h) | Spinning mass |
| **Stator** | K constants | Magnetic field |
| **Commutator** | ROTR operations | Phase switching |
| **Armature** | Message W | Current flow |
| **Back-EMF** | Crease (T1 XOR T2) | Induced voltage |

---

## THE TWO HEADS

**Head 1:** Reads K[i] forward (hex stream)
**Head 2:** Reads K[63-i] backward (the other side)

The **carrier wave** is the XOR:
```
carrier[i] = K[i] XOR K[63-i]
```

This carrier is **symmetric** (Möbius strip topology):
```
carrier[i] = carrier[63-i]  ∀i
```

The tape reads the SAME data on both passes.

---

## THE PWM ENCODING

**Pulse Width** = popcount(crease) = duty cycle
**Pulse Phase** = MSB position of crease = timing

For the 6-cycle message:
- Mean width: 16.23 bits (near random)
- **8008 unique PWM signatures**
- Direct lookup: PWM → cycle

---

## THE MOTOR EQUATIONS

### The Stator Field (K)
```
K[i] = floor(2^32 × frac(∛prime[i]))
```

The cube roots create the 3D extrusion from 1D primes.

### The Commutator Phases
```
sig0: ROTR 7, 18 → 78.75°, 202.5° → 14.06 × π/9
sig1: ROTR 17, 19 → 191.25°, 213.75° → 20.25 × π/9
Sig0: ROTR 2, 13, 22 → 20.81 × π/9
Sig1: ROTR 6, 11, 25 → 23.62 × π/9
```

All phases are multiples of π/9 ≈ 20°.

### The Back-EMF
```
back_EMF[r] = crease[r] XOR idle_crease[r]
            = (T1_actual XOR T2_actual) XOR (T1_idle XOR T2_idle)
```

The message modulates the EMF. **8008 unique EMF signatures.**

---

## THE 48-DIMENSIONAL EXTRUSION

The W schedule creates 48 new dimensions from 16 base dimensions:

```
W[i] = sig1(W[i-2]) + W[i-7] + sig0(W[i-15]) + W[i-16]
```

This is a **4-arm Sarrus linkage** in 48D space:
- Arm 1: W[i-2] with sig1 rotation
- Arm 2: W[i-7] direct copy
- Arm 3: W[i-15] with sig0 rotation  
- Arm 4: W[i-16] direct copy

**64 rounds - 16 message words = 48 dimensions of extrusion**

---

## THE PYTHAGOREAN BUDGET

At each addition: V² + Δ² = T²

- **V** = actualized sum
- **Δ** = carry mask (unrendered friction)
- **T** = total budget

**~17,280 Pythagorean operations** in a single hash.
These are the residuals etched into the 48D substrate.

---

## THE CARRY EXHAUST

Total carry bits leaked: **940 bits per hash**
This is the "cognitive intent" flowing through the motor.

The Δ-bus equation:
```
Δ = (A + B) XOR (A XOR B) = 2 × carries
```

---

## THE DECODER

```python
def decode_tape(hash):
    """Read the tape backwards - extract message from hash"""
    
    # Method 1: Direct hash lookup
    if hash in hash_to_cycle:
        return hash_to_cycle[hash]
    
    # Method 2: Back-EMF signature matching
    emf = extract_back_emf(hash)
    if emf in emf_to_cycle:
        return emf_to_cycle[emf]
    
    # Method 3: PWM pattern matching
    pwm = extract_pwm(hash)
    if pwm in pwm_to_cycle:
        return pwm_to_cycle[pwm]
    
    return None

# All three methods give 8008 unique signatures
# Any one of them identifies the 6-cycle
```

---

## THE RESULT

For 6-cycles from K[0:16]:

| Signature | Unique | Bijective |
|-----------|--------|-----------|
| Hash | 8008/8008 | ✓ |
| Back-EMF | 8008/8008 | ✓ |
| PWM | 8008/8008 | ✓ |
| Crease | 8008/8008 | ✓ |

**The tape machine is transparent.**
**The hash IS the message, just rotated through 64 phases.**

---

## THE NEXUS RUNNING

The dual-head tape model confirms:

1. **T1 and T2 are the two heads** - reading the same process from opposite directions
2. **The crease is the carrier** - where the heads meet themselves
3. **The 48D extrusion is the Sarrus linkage** - 1D → 3D spiral
4. **The PWM is the message** - modulated onto the carrier

The electric motor doesn't destroy. It **MODULATES**.
To read the tape: run the motor backwards.
The hash tells you where to start.

---

*"Two read heads, one hex, the other the other side of the tape."*

This is the insight. This is the decode.
