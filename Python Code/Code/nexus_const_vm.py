from __future__ import annotations

from dataclasses import dataclass
from decimal import Decimal, getcontext
import struct
from typing import List, Tuple, Dict

MASK32 = 0xFFFFFFFF

# ---------------------------
# Basic bit ops
# ---------------------------
def rotl32(x: int, r: int) -> int:
    r &= 31
    x &= MASK32
    return ((x << r) | (x >> (32 - r))) & MASK32

def rotr32(x: int, r: int) -> int:
    r &= 31
    x &= MASK32
    return ((x >> r) | (x << (32 - r))) & MASK32

def popcount32(x: int) -> int:
    return (x & MASK32).bit_count()

# ---------------------------
# Carry metrics (telemetry)
# ---------------------------
def add32_carry_metrics(a: int, b: int) -> Tuple[int, int, int]:
    """Return (sum32, carry_pop, max_carry_chain_len) for ripple-carry add."""
    a &= MASK32
    b &= MASK32
    s = (a + b) & MASK32

    carry = 0
    carry_pop = 0
    max_chain = 0
    chain = 0

    for i in range(32):
        ai = (a >> i) & 1
        bi = (b >> i) & 1
        carry_out = (ai & bi) | (ai & carry) | (bi & carry)
        if carry_out:
            carry_pop += 1
            chain += 1
            if chain > max_chain:
                max_chain = chain
        else:
            chain = 0
        carry = carry_out

    return s, carry_pop, max_chain

# ---------------------------
# Tiny PRNG for permutations
# ---------------------------
class XorShift32:
    def __init__(self, seed: int):
        self.x = (seed & MASK32) or 0x6D2B79F5

    def next(self) -> int:
        x = self.x
        x ^= (x << 13) & MASK32
        x ^= (x >> 17) & MASK32
        x ^= (x << 5) & MASK32
        self.x = x & MASK32
        return self.x

def permute_indices(n: int, seed: int) -> List[int]:
    rng = XorShift32(seed)
    idx = list(range(n))
    for i in range(n - 1, 0, -1):
        j = rng.next() % (i + 1)
        idx[i], idx[j] = idx[j], idx[i]
    return idx

# ---------------------------
# VM definitions
# ---------------------------
@dataclass
class Telemetry:
    carry_pop_total: int = 0
    carry_chain_max: int = 0
    bitflip_total: int = 0
    rounds: int = 0

    def to_dict(self) -> Dict[str, float]:
        if self.rounds == 0:
            return {}
        return {
            "rounds": float(self.rounds),
            "carry_pop_avg": self.carry_pop_total / self.rounds,
            "carry_chain_max": float(self.carry_chain_max),
            "bitflip_avg": self.bitflip_total / self.rounds,
        }

def decode_opcode(c: int) -> Tuple[int, int, int]:
    op = c & 7
    r = (c >> 3) & 31
    imm = c & MASK32
    return op, r, imm

def vm_step(state: List[int], c: int, tel: Telemetry) -> None:
    """Generic opcode-driven update over an 8-word state. Not SHA."""
    op, r, imm = decode_opcode(c)
    a, b, cw, d, e, f, g, h = state

    before = state.copy()

    if op == 0:
        x, cp, chain = add32_carry_metrics(a, imm)
        a = rotl32(x, r)
        tel.carry_pop_total += cp
        tel.carry_chain_max = max(tel.carry_chain_max, chain)

    elif op == 1:
        a = rotr32(a ^ imm, r)

    elif op == 2:
        x, cp, chain = add32_carry_metrics(a, e)
        a = (x ^ rotl32(imm, r)) & MASK32
        tel.carry_pop_total += cp
        tel.carry_chain_max = max(tel.carry_chain_max, chain)

    elif op == 3:
        a, e = e, a
        x, cp, chain = add32_carry_metrics(a, imm ^ e)
        e = x
        tel.carry_pop_total += cp
        tel.carry_chain_max = max(tel.carry_chain_max, chain)

    elif op == 4:
        maj = (a & b) ^ (a & e) ^ (b & e)
        a = rotl32(maj ^ imm, r)

    elif op == 5:
        chooser = (a & f) ^ (~a & g)
        x, cp, chain = add32_carry_metrics(e, chooser ^ imm)
        e = rotr32(x, r)
        tel.carry_pop_total += cp
        tel.carry_chain_max = max(tel.carry_chain_max, chain)

    elif op == 6:
        a = (a * (imm | 1)) & MASK32
        a = rotl32(a ^ ((e + 0x9E3779B9) & MASK32), r)

    else:
        a = (a - imm) & MASK32
        a = rotr32(a ^ e, r)

    # diffusion shuffle (simple)
    state[:] = [a, cw, b, d, e, f ^ a, g, h ^ e]

    flips = 0
    for i in range(8):
        flips += popcount32(before[i] ^ state[i])
    tel.bitflip_total += flips
    tel.rounds += 1

# ---------------------------
# Cube-root constant ROM (SHA-style derivation, but we will NOT use SHA order)
# ---------------------------
def first_n_primes(n: int) -> List[int]:
    primes: List[int] = []
    x = 2
    while len(primes) < n:
        is_p = True
        for p in primes:
            if p * p > x:
                break
            if x % p == 0:
                is_p = False
                break
        if is_p:
            primes.append(x)
        x += 1
    return primes

def cbrt_decimal(N: Decimal) -> Decimal:
    """Cube root via Newton-Raphson in Decimal context."""
    if N == 0:
        return Decimal(0)

    # Initial guess: float-based
    x = Decimal(float(N) ** (1.0 / 3.0))
    # Refine
    for _ in range(40):
        x2 = x * x
        if x2 == 0:
            x = Decimal(1)
            continue
        x = (2 * x + (N / x2)) / 3
    return +x

def cube_root_rom(n: int = 64, prec: int = 90) -> List[int]:
    getcontext().prec = prec
    primes = first_n_primes(n)
    two32 = Decimal(1 << 32)
    rom: List[int] = []

    for p in primes:
        r = cbrt_decimal(Decimal(p))
        frac = r - int(r)
        k = int(frac * two32) & MASK32
        rom.append(k)
    return rom

# ---------------------------
# Runner
# ---------------------------
def run_vm(seed_bytes: bytes, constants: List[int], rounds: int = 512) -> Tuple[List[int], Telemetry]:
    if len(constants) < 8:
        raise ValueError("Need at least 8 constants")

    seed = (seed_bytes * ((32 // len(seed_bytes)) + 1))[:32]
    state = list(struct.unpack(">8I", seed))
    state = [x & MASK32 for x in state]

    seed32 = struct.unpack(">I", seed[:4])[0] ^ struct.unpack(">I", seed[4:8])[0]
    perm = permute_indices(len(constants), seed32 ^ state[0] ^ rotl32(state[4], 7))

    tel = Telemetry()
    for t in range(rounds):
        j = (t + (state[0] ^ state[4] ^ (state[7] >> 1))) % len(constants)
        k = perm[j]
        c = constants[k]
        vm_step(state, c, tel)

    return state, tel

def hex_state(state: List[int]) -> List[str]:
    return [hex(x & MASK32) for x in state]

if __name__ == "__main__":
    # Benign seed (00..0f)
    seed = bytes.fromhex("000102030405060708090a0b0c0d0e0f")

    # Build cube-root ROM (SHA-style derivation), then reorder to avoid SHA order.
    rom = cube_root_rom(64, prec=110)

    # Pick ONE: largest -> smallest (deterministic keep-away from SHA order)
    rom_desc = sorted(rom, reverse=True)

    final_state, tel = run_vm(seed, rom_desc, rounds=512)

    print("final_state:", hex_state(final_state))
    print("telemetry:", tel.to_dict())
