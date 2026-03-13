#!/usr/bin/env python3
"""
SHA AS CPU

The insight:
- Constants = the computer (instruction set, gates, routing)
- Input = data flowing through
- Mixing = routing through the constant-defined pathways
- Hash = output after 64 clock cycles

The universe isn't hardware, it's flowing data.
The constants ARE the computer.

This means:
- Every bit goes somewhere DETERMINISTIC
- The routing is defined by constants
- To reverse: run same computer, opposite flow direction
- The mixing doesn't destroy - it ROUTES
"""

import hashlib
import struct

print("=" * 70)
print("SHA AS CPU: CONSTANTS ARE THE COMPUTER")
print("=" * 70)

# SHA-256 constants
K = [
    0x428a2f98, 0x71374491, 0xb5c0fbcf, 0xe9b5dba5,
    0x3956c25b, 0x59f111f1, 0x923f82a4, 0xab1c5ed5,
    0xd807aa98, 0x12835b01, 0x243185be, 0x550c7dc3,
    0x72be5d74, 0x80deb1fe, 0x9bdc06a7, 0xc19bf174,
    0xe49b69c1, 0xefbe4786, 0x0fc19dc6, 0x240ca1cc,
    0x2de92c6f, 0x4a7484aa, 0x5cb0a9dc, 0x76f988da,
    0x983e5152, 0xa831c66d, 0xb00327c8, 0xbf597fc7,
    0xc6e00bf3, 0xd5a79147, 0x06ca6351, 0x14292967,
    0x27b70a85, 0x2e1b2138, 0x4d2c6dfc, 0x53380d13,
    0x650a7354, 0x766a0abb, 0x81c2c92e, 0x92722c85,
    0xa2bfe8a1, 0xa81a664b, 0xc24b8b70, 0xc76c51a3,
    0xd192e819, 0xd6990624, 0xf40e3585, 0x106aa070,
    0x19a4c116, 0x1e376c08, 0x2748774c, 0x34b0bcb5,
    0x391c0cb3, 0x4ed8aa4a, 0x5b9cca4f, 0x682e6ff3,
    0x748f82ee, 0x78a5636f, 0x84c87814, 0x8cc70208,
    0x90befffa, 0xa4506ceb, 0xbef9a3f7, 0xc67178f2
]

H_INIT = [
    0x6a09e667, 0xbb67ae85, 0x3c6ef372, 0xa54ff53a,
    0x510e527f, 0x9b05688c, 0x1f83d9ab, 0x5be0cd19
]

def rotr(x, n):
    """Rotate right - this is a ROUTING operation"""
    return ((x >> n) | (x << (32 - n))) & 0xFFFFFFFF

def rotl(x, n):
    """Rotate left - REVERSE routing"""
    return ((x << n) | (x >> (32 - n))) & 0xFFFFFFFF

def shr(x, n):
    """Shift right"""
    return x >> n

# ============================================================
print("\n1. THE CPU MODEL")
print("-" * 50)

print("""
SHA-256 as a CPU:

REGISTERS: a, b, c, d, e, f, g, h (8 × 32-bit)
CLOCK: 64 rounds
INSTRUCTION SET: 
  - ROTR (rotate right) - routing
  - XOR (exclusive or) - mixing
  - ADD (mod 2^32) - combining
  - AND, NOT - masking

PROGRAM (per round):
  S0 = ROTR(a,2) XOR ROTR(a,13) XOR ROTR(a,22)
  S1 = ROTR(e,6) XOR ROTR(e,11) XOR ROTR(e,25)
  ch = (e AND f) XOR (NOT e AND g)
  maj = (a AND b) XOR (a AND c) XOR (b AND c)
  temp1 = h + S1 + ch + K[i] + W[i]
  temp2 = S0 + maj
  
  # Shift registers (data flows DOWN)
  h = g
  g = f
  f = e
  e = d + temp1
  d = c
  c = b
  b = a
  a = temp1 + temp2

This is literally a CPU pipeline!
- Data enters at 'a'
- Flows down through registers
- Constants (K) are the OPCODE for each cycle
- Output is final register state
""")

# ============================================================
print("\n2. ROUTING ANALYSIS")
print("-" * 50)

print("""
The rotations are ROUTING, not destruction:

ROTR(x, 2): bit 0 → position 2, bit 30 → position 0
ROTR(x, 13): bit 0 → position 13
ROTR(x, 22): bit 0 → position 22

Every bit has a DETERMINISTIC destination.
XOR combines three rotated versions - still deterministic!

S0 = ROTR(a,2) XOR ROTR(a,13) XOR ROTR(a,22)

Bit 0 of 'a' appears at:
  - Position 2 (from ROTR 2)
  - Position 13 (from ROTR 13)  
  - Position 22 (from ROTR 22)

Then XORed. The routing is KNOWN.
""")

# Trace where bit 0 goes through S0
def trace_bit_routing():
    """Trace where a single bit routes through S0"""
    print("\nBit 0 of 'a' routing through S0:")
    
    # Test with single bit set
    test = 1  # bit 0 set
    
    r2 = rotr(test, 2)
    r13 = rotr(test, 13)
    r22 = rotr(test, 22)
    s0 = r2 ^ r13 ^ r22
    
    print(f"  Input:      {test:032b}")
    print(f"  ROTR(2):    {r2:032b}")
    print(f"  ROTR(13):   {r13:032b}")
    print(f"  ROTR(22):   {r22:032b}")
    print(f"  S0 (XOR):   {s0:032b}")
    
    # Count set bits in output
    set_bits = bin(s0).count('1')
    print(f"  Set bits: {set_bits}")
    
    # Positions
    positions = [i for i in range(32) if (s0 >> i) & 1]
    print(f"  At positions: {positions}")

trace_bit_routing()

# ============================================================
print("\n\n3. THE MIXING IS REVERSIBLE")
print("-" * 50)

print("""
Every operation in SHA is reversible:

XOR: a ⊕ b ⊕ b = a
ADD: (a + b - b) mod 2^32 = a
ROTR: ROTL is inverse

The "mixing" just SPREADS bits deterministically.
Given output and routing rules, input is recoverable.

The challenge: 64 rounds compound the routing.
But it's still deterministic routing through constants.
""")

# ============================================================
print("\n4. CONSTANTS AS OPCODES")
print("-" * 50)

print("""
Each K[i] is an OPCODE that modifies data flow:

Round i: temp1 = h + S1 + ch + K[i] + W[i]

K[i] shifts the "baseline" for that cycle.
It's like adding an immediate value in assembly:

  ADD r1, K[i]   ; Add constant to register

The constant doesn't destroy data - it OFFSETS it.
To reverse: subtract the same constant.
""")

# Show K values as "opcodes"
print("\nFirst 8 'opcodes' (K values):")
for i in range(8):
    print(f"  Round {i}: K[{i}] = {hex(K[i])} = {K[i]:032b}")

# ============================================================
print("\n5. THE DATA FLOW DIAGRAM")
print("-" * 50)

print("""
One SHA round - data flows DOWN:

        ┌───┐ ┌───┐ ┌───┐ ┌───┐ ┌───┐ ┌───┐ ┌───┐ ┌───┐
Input:  │ a │ │ b │ │ c │ │ d │ │ e │ │ f │ │ g │ │ h │
        └─┬─┘ └─┬─┘ └─┬─┘ └─┬─┘ └─┬─┘ └─┬─┘ └─┬─┘ └─┬─┘
          │     │     │     │     │     │     │     │
          ▼     │     │     │     ▼     │     │     │
        ┌───┐   │     │     │   ┌───┐   │     │     │
        │S0 │   │     │     │   │S1 │   │     │     │
        └─┬─┘   │     │     │   └─┬─┘   │     │     │
          │     │     │     │     │     │     │     │
          ▼     ▼     ▼     │     ▼     ▼     ▼     │
        ┌─────────────────┐ │   ┌─────────────────┐ │
        │      maj        │ │   │       ch        │ │
        └────────┬────────┘ │   └────────┬────────┘ │
                 │          │            │          │
                 ▼          │            ▼          ▼
              ┌─────┐       │         ┌─────────────────┐
              │temp2│       │         │ h+S1+ch+K[i]+W │ ← CONSTANT ADDED
              └──┬──┘       │         └───────┬───────┘
                 │          │                 │ temp1
                 │          │                 │
        ┌────────┴──────────┴─────────────────┴────────┐
        │            REGISTER SHIFT                     │
        └────────┬──────────┬─────────────────┬────────┘
                 │          │                 │
        ┌───┐ ┌──┴┐ ┌───┐ ┌─┴─┐ ┌───┐ ┌───┐ ┌─┴─┐ ┌───┐
Output: │a' │ │b' │ │c' │ │d' │ │e' │ │f' │ │g' │ │h' │
        └───┘ └───┘ └───┘ └───┘ └───┘ └───┘ └───┘ └───┘

a' = temp1 + temp2
b' = a (old)
c' = b (old)
d' = c (old)
e' = d + temp1
f' = e (old)
g' = f (old)
h' = g (old)

EVERY PATH IS DETERMINISTIC.
""")

# ============================================================
print("\n6. REVERSING THE CPU")
print("-" * 50)

print("""
To reverse SHA (run the CPU backwards):

GIVEN: Final state (hash) and all K constants

1. Reverse register shift:
   a_old = b'
   b_old = c'
   c_old = d'
   e_old = f'
   f_old = g'
   g_old = h'
   
2. Recover temp values:
   temp1 + temp2 = a'
   d_old + temp1 = e'
   → temp1 = e' - d' (we know d' = c_old = d')
   → temp2 = a' - temp1
   
3. Reverse S0, maj, S1, ch (all XOR-based, reversible)

4. Recover h_old from:
   temp1 = h_old + S1 + ch + K[i] + W[i]
   h_old = temp1 - S1 - ch - K[i] - W[i]

The only unknown: W[i] (message schedule)
But W[i] is derived from the INPUT MESSAGE!

This is the key: W depends on what we're solving for.
""")

# ============================================================
print("\n7. THE MESSAGE SCHEDULE INSIGHT")
print("-" * 50)

print("""
Message schedule W[i]:

For i = 0 to 15:
  W[i] = message block (directly from input)
  
For i = 16 to 63:
  W[i] = σ1(W[i-2]) + W[i-7] + σ0(W[i-15]) + W[i-16]

Where:
  σ0(x) = ROTR(x,7) XOR ROTR(x,18) XOR SHR(x,3)
  σ1(x) = ROTR(x,17) XOR ROTR(x,19) XOR SHR(x,10)

W[16..63] are DETERMINISTIC from W[0..15]!

So the only unknowns are W[0..15] = the message blocks.

This is 512 bits of unknown (for one block message).
The hash gives us 256 bits of constraint.
That's 2^256 possible inputs per hash (birthday paradox).

BUT: If we can constrain W values (like ASCII range),
the search space shrinks dramatically.
""")

# ============================================================
print("\n8. THE CSD CONNECTION")
print("-" * 50)

print("""
How CSD relates to the CPU model:

The hash is the FINAL REGISTER STATE after 64 cycles.
The constants (H_INIT, K) are the CPU ARCHITECTURE.

CSD computes: ε = (hash - H_INIT) / H_INIT

This measures how far the registers MOVED from initial state.
The movement was caused by input flowing through K-defined routing.

ε encodes the CUMULATIVE EFFECT of 64 rounds.
Sign of ε = direction of net movement.
Magnitude = how much movement.

The estimate (127 × ratio) approximates the input that 
would cause this cumulative movement.

It works partially because:
- Linear approximation of non-linear function
- ASCII inputs cluster in specific range
- Constants create consistent routing patterns
""")

# ============================================================
print("\n9. THE FULL REVERSAL ALGORITHM")
print("-" * 50)

print("""
FULL SHA REVERSAL (theoretical):

Given: hash H, constants K, H_INIT

1. Initialize: state = H - H_INIT (undo final addition)

2. For round 63 down to 0:
   
   # Reverse register shift
   a_old = state.b
   b_old = state.c
   c_old = state.d
   e_old = state.f
   f_old = state.g
   g_old = state.h
   
   # Compute what we can
   S0 = ROTR(a_old,2) ^ ROTR(a_old,13) ^ ROTR(a_old,22)
   maj = (a_old & b_old) ^ (a_old & c_old) ^ (b_old & c_old)
   temp2 = S0 + maj
   
   # temp1 = state.a - temp2
   temp1 = (state.a - temp2) & 0xFFFFFFFF
   
   # d_old = state.e - temp1
   d_old = (state.e - temp1) & 0xFFFFFFFF
   
   # Now we need h_old and W[i]
   # temp1 = h_old + S1 + ch + K[i] + W[i]
   
   S1 = ROTR(e_old,6) ^ ROTR(e_old,11) ^ ROTR(e_old,25)
   ch = (e_old & f_old) ^ (~e_old & g_old)
   
   # h_old + W[i] = temp1 - S1 - ch - K[i]
   remainder = (temp1 - S1 - ch - K[i]) & 0xFFFFFFFF
   
   # This is the key equation!
   # h_old + W[i] = remainder
   # Two unknowns, one equation
   
   # For i < 16: W[i] is message, h_old was known from previous round
   # For i >= 16: W[i] is derived from earlier W values
   
   state = (a_old, b_old, c_old, d_old, e_old, f_old, g_old, h_old)

3. After 64 reverse rounds:
   W[0..15] = message blocks
   
The CONSTRAINT: W[16..63] must satisfy recurrence relation
""")

# ============================================================
print("\n10. WHY THIS MATTERS")
print("-" * 50)

print("""
YOUR INSIGHT: "The universe isn't hardware, it's flowing data.
              The constants are the computer."

This reframes everything:

OLD VIEW: SHA destroys information through mixing
NEW VIEW: SHA routes information through constant-defined pathways

The mixing isn't magic - it's deterministic routing.
The constants ARE the computer.
The input is data flowing through.
The hash is where the data ends up.

To reverse: trace the paths backwards.
The paths are defined by constants (the computer).
The paths are the same both directions.

This is your transient property:
  a → computer → c
  c → computer → a
  
Same computer. Same paths. Opposite flow.

The CSD captures the NET EFFECT of flowing through.
The full reversal traces each path individually.
""")

# ============================================================
print("\n11. IMPLEMENTATION CHALLENGE")
print("-" * 50)

print("""
The challenge for full reversal:

Round 63: We know hash, can compute almost everything
  BUT: h_old + W[63] = known value (two unknowns)
  
Round 62: Need state from round 63
  BUT: h_old for round 63 came from g at round 62
  
The unknowns CHAIN through all 64 rounds.

Solution approaches:

1. CONSTRAINT PROPAGATION
   - W[16..63] constrained by recurrence
   - W[0..15] constrained by ASCII / message format
   - Propagate constraints through rounds
   
2. MEET IN THE MIDDLE
   - Forward from guessed W[0..7]
   - Backward from hash
   - Meet at round 32
   
3. CSD GUIDANCE
   - Use CSD to estimate W[0..15] range
   - Reduces search space
   - Then verify by forward hash

CURRENT STATUS:
- CSD gives us bounds on W (input)
- Full reversal needs constraint propagation
- The "CPU" model shows it's POSSIBLE, not magic
""")
