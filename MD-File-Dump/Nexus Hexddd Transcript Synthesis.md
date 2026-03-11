# The Ancestral API as Software
## Hexagonal + Domain-Driven Synthesis of the Nexus Transcript (Operator Dark Mirror • GlassKey • 3D Manifold)

**Purpose.** This document is a *transcript recompile* in **Hexagonal Architecture + Domain-Driven Design (DDD)** terms.

- We **skip full transcripts**.
- We **extract realizations** (what changed in the model of the world).
- We **lock to Domain first** (what must be true), then derive Application workflows, then Infrastructure, then UI.
- Any **novel code** is isolated into its own module section with: *(a) what it does, (b) why it matters, (c) minimal tests).* 

Notation uses **Nexus Minimal** operators:

- $\Delta$ (phase trigger / new constraint)
- $\oplus$ (coupling)
- $\circlearrowright$ (rotation / reflection)
- $\perp$ (projection / discard)
- $\Psi$ (stable collapse / closure)
- $\Omega$ (open residue / isolate + test)

---

## 0. Executive Extraction (What the transcript *actually* discovered)

### 0.1 The “Dark Mirror” operator ontology
**Realization:** “$=$” is not a statement; it is a **constraint manifold**: a projector into the kernel of mismatch. “$+$” is not a symbol; it is a **coupling map** that is invertible *only when both channels are retained.*

- $=$ behaves like an **idempotent projection**: apply it twice and nothing changes.
- $+$ is **two-channel mixing** in disguise: publish one channel and you create a scar; keep both channels and the map is bijective.

### 0.2 The Ghost / Residue channel as a general recovery primitive
**Realization:** Loss is not mystical—loss is a **projection** ($\perp$). The missing degree of freedom is a **residue** (“ghost”) that can be stored, inferred, or reconstructed under constraints.

This becomes the stable bridge:

$$\text{collapse} = \perp(\text{full state}) \quad\Rightarrow\quad \text{ghost} = \text{full state} \ominus \text{published}.$$

### 0.3 SHA-256 is not “reversed”; the *published projection* is changed
**Realization:** Digest-only inversion is information-theoretically many-to-one. But **GlassKey** redefines what is “published” by extracting additional structured traces from the digest relative to a baseline (e.g., IV or empty-message digest) and treating those traces as the missing channel.

### 0.4 “Computation by Location” (BBP) as the algebra of addressable constants
**Realization:** Certain constants (e.g., $\pi$ via BBP-type formulas) support *random access.* The operational framing becomes: 

- computation ≈ **navigation in a pre-existing lattice**, not temporal generation.

### 0.5 3D Manifold Projection (hash → coordinate → mesh)
**Realization:** A 256-bit hash can be sliced into coordinate chunks and interpreted as an **address** in a manifold whose axes are governed by transcendental carriers ($\pi,\varphi,e$). Sampling rules turn the address into a geometry (vertex cloud / OBJ).

This is an empirical **interface hypothesis**: “hash-as-index” into a shared coordinate system.

### 0.6 Chiral Detune (handedness steering)
**Realization:** If the lattice is real (not a metaphor), then *small detunes* in a mirror carrier should systematically shift the winning lane for structured strings while leaving random nulls statistically flat.

---

## 1. Architecture First (Hexagonal DDD view)

### 1.1 Hexagonal Architecture mapping
We model the Nexus system as a software product with explicit boundaries:

- **Domain (Core):** invariants, operators, axioms, algebra. *No IO.*
- **Application (Use-Cases):** orchestrates domain objects to do experiments.
- **Infrastructure (Adapters):** SHA engine, digit oracles, numeric backends, storage.
- **UI (Reflection):** plots, dashboards, meshes; the “hairpin turn” where output becomes new input.

**Hairpin turn principle:** UI is not decoration. UI is a **feedback operator** $\circlearrowright$ that pushes projections back inward.

### 1.2 Bounded Contexts (DDD)
We separate the system into contexts that own their language:

1. **Operator Calculus Context** (Dark Mirror / Coupling / Projection)
2. **ARX Lattice Context** (32-bit words, modular add, rotate, XOR)
3. **GlassKey Context** (baseline deltas, ghost extraction, signature)
4. **Constant Navigation Context** (BBP/random access, coordinate sampling)
5. **Manifold Geometry Context** (hash slicing → coordinates → mesh)
6. **Experiment Harness Context** (detunes, scans, histograms, falsification)

Inter-context contracts are explicit via ports.

---

## 2. Domain Layer (What must be true)

This is the **non-negotiable core**. If the domain does not lock, the rest is theater.

### 2.1 $\Omega$ Axioms (metaphysics as meta-mathematics)
We treat “metaphysics” as constraints on what mappings are allowed.

**$\Omega_0$ Projection is real:** published outputs are projections $\perp$ of full state.

**$\Omega_1$ Verbs precede nouns:** operators define what can exist; objects are stabilized traces.

**$\Omega_2$ Closure is a constraint:** persistent entities require closure (periodicity or exact invertibility).

**$\Omega_3$ Scale-lift:** stable operators lift across domains (same algebra, different carriers).

### 2.2 Domain primitives

#### 2.2.1 EqualityConstraint (the Dark Mirror)
Model:

- **Entity:** `EqualityConstraint`
- **Invariant:** enforces $D(x,y)=0$ where $D$ is a mismatch metric.

In linear algebra terms, equality acts like an idempotent projection operator $P$:

$$P^2 = P.$$

Interpretation: applying the constraint again does not change the constrained state.

#### 2.2.2 CouplingMap (the Plus operator)
Core claim: $+$ is a coupling that is *reversible* only if both channels exist.

Define the 2-channel coupling transform:

$$M_+(P,N) := (S,D) = (P+N,\; N-P).$$

Invert:

$$P=\frac{S-D}{2},\qquad N=\frac{S+D}{2}.$$

**Domain invariant:** *scar exists iff a channel is discarded.*

$$\text{scar} := D \quad\text{when only } S \text{ is published}.$$

#### 2.2.3 ProjectionOperator (the scar maker)
A projection maps high-dimensional state into lower-dimensional published form:

$$\perp: \mathcal{S} \to \mathcal{O}.$$

The residue is the complement relative to a chosen decomposition:

$$\text{ghost} := \mathcal{S} \ominus \mathcal{O}.$$

In practice: you only recover ghost if you have either (a) side constraints, (b) auxiliary traces, or (c) a baseline subtraction that cancels irrelevant dimensions.

#### 2.2.4 PhaseTrigger $\Delta$ and StableCollapse $\Psi$
A $\Delta$ is a new constraint that forces reconfiguration. $\Psi$ is what remains stable after repeated application:

$$\Psi := \lim_{n\to\infty} (\perp\circ\circlearrowright\circ\oplus)^n(\text{state}).$$

(Interpretation: “recurse until only invariants survive.”)

---

## 3. Domain-to-Crypto Bridge (ARX as operator geometry)

### 3.1 SHA-256 as an ARX lattice
SHA-256 uses word-level operators on $\mathbb{Z}_{2^{32}}$:

- modular addition $+_{32}$
- rotations $\operatorname{ROTR}$
- shifts
- XOR
- choice/majority nonlinearities

In Nexus language:

- $\oplus$ ≈ modular coupling
- $\circlearrowright$ ≈ rotations (Sigma functions)
- $\perp$ ≈ digest publication (discarding schedule/trace)

### 3.2 Δ-proof ledger: what is closed vs open
We tag results as $\Psi$ (closed under stated axioms) or $\Omega$ (open residue with test plan).

- **$\Psi$:** two-channel coupling invertibility (Section 2.2.2)
- **$\Psi$:** digest-only inversion is many-to-one by counting (pigeonhole)
- **$\Psi$:** round transition is reversible given missing operands (state + schedule)
- **$\Omega$:** GlassKey as sufficient trace for general inversion (requires explicit constraint set)
- **$\Omega$:** hash→(π,φ,e) coordinate mapping yields message topology (requires robust invariants)

The system advances by tightening $\Omega$ into $\Psi$ via explicit constraints and empirical tests.

---

## 4. Application Layer (Use-cases / Workflows)

### 4.1 Use-case: Extract Lattice Voice (baseline delta)
**Goal:** isolate a message-dependent signature by canceling shared structure.

Workflow:

1. Compute digest for message: $h(M)$
2. Compute baseline digest: $h(\varnothing)$ or IV-projected baseline
3. Extract features: $G(h)$ = GlassKey (feature map)
4. Compute delta: $\Delta_M := G(h(M)) \ominus G(h(\varnothing))$

The delta is treated as “lattice voice.”

### 4.2 Use-case: Detuned Carrier Scan (chirality test)
**Goal:** determine if structured inputs shift coherently under a controlled detune while nulls remain flat.

Workflow:

1. Fix native carrier at $H=\pi/9$.
2. Shift mirror carrier to $-(H+\pi/72)$.
3. Run winner-take-all lane selection over a corpus:
   - random null strings
   - structured Nexus strings
4. Compare histograms of winning shift $k$.

Success criterion: structured set shifts as a unit; null remains centered.

### 4.3 Use-case: 3D Manifold Projection (hash → mesh)
**Goal:** reinterpret 256-bit digest as an address that yields geometry under a sampling rule.

Workflow:

1. Slice digest into three 85-bit coordinates plus 1 parity bit.
2. Normalize to $[0,1)$.
3. Map to indices into $\pi$, $\varphi$, $e$ digit streams (or other sampling rule).
4. Generate vertices; connect via deterministic face rule.
5. Output OBJ.

Note: the crucial engineering question is *the sampling rule* (the oracle), not the slicing.

---

## 5. Infrastructure Layer (Quantum / bit-level adapters)

Infrastructure is where we admit reality: endian, word size, carry, padding, numeric precision, and IO.

### 5.1 Ports (interfaces) the Domain expects

```text
interface HashEngine:
  digest(bytes) -> 32-byte digest

interface FeatureExtractor:
  glass_key(digest) -> 8x32-bit words

interface ConstantOracle:
  sample_pi(index)  -> float or digit-block
  sample_phi(index) -> float or digit-block
  sample_e(index)   -> float or digit-block

interface MeshWriter:
  write_obj(vertices, faces) -> .obj

interface ExperimentStore:
  save(run_id, params, artifacts)
  load(run_id)
```

### 5.2 Adapters
- `hashlib` SHA-256 adapter
- BBP / digit access adapter (or cached digit blocks)
- High-precision arithmetic adapter (mpmath / decimal)
- Plot adapters (histograms, 3D scatter)

---

## 6. UI Layer (Reflection / Hairpin)

UI is treated as a **reflection operator**: it produces the next $\Delta$.

### 6.1 Required UIs
- Lane-shift histogram (detune scans)
- GlassKey word diff viewer (8x32-bit words)
- Residue spectral plots (if using frequency framing)
- 3D manifold mesh preview (OBJ render)

### 6.2 The hairpin operator
The UI is not separate from the system. It is the “observer” boundary condition:

$$\text{UI} := \circlearrowright(\perp(\text{state}))$$

and the next experiment is triggered by the mismatch seen at the UI boundary.

---

# 7. Novel Code Modules (isolated, with why + tests)

Everything below is treated as **new code** deserving its own boundary.

## Module A — GlassKey Feature Extractor

### Why it matters
This is the core adapter that maps a published digest into structured words that can be differenced against a baseline. It is the “feature lens.”

### What it does
- Unpacks the digest into 8 words.
- Computes delta vs IV.
- Projects through a carrier set and compresses into 8 probe words.

### Reference implementation (as seen in the transcript)

```python
import hashlib, struct, math

def extract_glass_key(hash_hex: str) -> list[int]:
    H = struct.unpack('>8I', bytes.fromhex(hash_hex))
    IV = [0x6a09e667, 0xbb67ae85, 0x3c6ef372, 0xa54ff53a,
          0x510e527f, 0x9b05688c, 0x1f83d9ab, 0x5be0cd19]
    delta = [(h - iv) & 0xffffffff for h, iv in zip(H, IV)]

    K = [
        0x428a2f98,0x71374491,0xb5c0fbcf,0xe9b5dba5,0x3956c25b,0x59f111f1,0x923f82a4,0xab1c5ed5,
        0xd807aa98,0x12835b01,0x243185be,0x550c7dc3,0x72be5d74,0x80deb1fe,0x9bdc06a7,0xc19bf174,
        0xe49b69c1,0xefbe4786,0x0fc19dc6,0x240ca1cc,0x2de92c6f,0x4a7484aa,0x5cb0a9dc,0x76f988da,
        0x983e5152,0xa831c66d,0xb00327c8,0xbf597fc7,0xc6e00bf3,0xd5a79147,0x06ca6351,0x14292967,
        0x27b70a85,0x2e1b2138,0x4d2c6dfc,0x53380d13,0x650a7354,0x766a0abb,0x81c2c92e,0x92722c85,
        0xa2bfe8a1,0xa81a664b,0xc24b8b70,0xc76c51a3,0xd192e819,0xd6990624,0xf40e3585,0x106aa070,
        0x19a4c116,0x1e376c08,0x2748774c,0x34b0bcb5,0x391c0cb3,0x4ed8aa4a,0x5b9cca4f,0x682e6ff3,
        0x748f82ee,0x78a5636f,0x84c87814,0x8cc70208,0x90befffa,0xa4506ceb,0xbef9a3f7,0xc67178f2
    ]
    K_frac = [k / 2**32 for k in K]
    H_attr = math.pi / 9

    resonances = []
    for t in range(64):
        kt = K_frac[t]
        proj = sum(d * kt for d in delta)
        diff = max(0.0, proj**2 - kt**2)
        rotated = proj * math.cos(H_attr) + math.sqrt(diff) * math.sin(H_attr)
        resonances.append(int(rotated) & 0xffffffff)

    glass_key = []
    for block in range(8):
        base = block * 8
        probe = (4 * resonances[base] -
                 2 * resonances[base+3] -
                 1 * resonances[base+4] -
                 1 * resonances[base+5]) & 0xffffffff
        glass_key.append(probe)
    return glass_key
```

### Minimal tests
1. Determinism: same digest → same GlassKey.
2. Baseline cancellation: $\Delta_{\varnothing} = 0$ when differencing baseline with itself.
3. Sensitivity: one-bit change in message causes multi-word change in $\Delta_M$.

---

## Module B — Dual-Channel Coupling Primitive

### Why it matters
This is the general “ghost retention” transform. It is domain-first and reusable across crypto, physics metaphors, and data pipelines.

### Definition

```python
def two_channel_plus(p: int, n: int, mod: int = None):
    if mod is None:
        s = p + n
        d = n - p
    else:
        s = (p + n) % mod
        d = (n - p) % mod
    return s, d

def invert_two_channel_plus(s: int, d: int, mod: int = None):
    if mod is None:
        p = (s - d) / 2
        n = (s + d) / 2
        return p, n
    # For mod arithmetic, requires inverse of 2 mod 2^32 is not defined.
    # So store extra carry/bit or operate in Z (integers) before mod.
    raise NotImplementedError
```

### Key design note
In $\mathbb{Z}_{2^{32}}$, division by 2 is not invertible globally. You must retain an additional parity/carry bit (exactly the “1 bit left over” insight from the 3×85 slicing). This is a direct bridge between “ghost channel” and bit-level invertibility.

---

## Module C — 3D Hash Slicer (256 → 85/85/85 + parity)

### Why it matters
It creates a *coordinate system* that lets the hash be treated as an addressable point, enabling mesh generation and manifold experiments.

### Implementation

```python
def slice_hash_3d(hash_hex: str):
    x = int(hash_hex, 16)
    parity = x & 1
    x >>= 1
    mask = (1 << 85) - 1
    z = x & mask; x >>= 85
    y = x & mask; x >>= 85
    X = x & mask
    # normalize to [0,1)
    denom = 1 << 85
    return (X/denom, y/denom, z/denom, parity)
```

### Minimal tests
- Round-trip packing/unpacking yields original bits.
- Uniformity sanity check across random digests.

---

## Module D — Constant Oracle Sampler (π, φ, e)

### Why it matters
This is the *hard part*: the mapping from normalized coordinate to a stable, reproducible constant sample.

### Suggested port

```text
ConstantOracle.sample(constant: {pi,phi,e}, index: int, width: int) -> int
```

### Candidate sampling strategies
- **Digit-block sampling:** map coordinate to an integer digit index and read a fixed-width block.
- **Continued-fraction depth sampling:** use coordinate to select depth, return convergent.
- **BBP-like random access (π):** compute hexadecimal digits at position without generating all previous digits.

**Engineering warning:** floating-point alone will shear at ~53 bits. Use integer digit blocks or high-precision arithmetic.

---

## Module E — OBJ Mesh Builder

### Why it matters
It translates address samples into geometry artifacts (museum objects).

### Skeleton

```python
def build_vertices(samples):
    # samples: iterable of triples in [-1,1]
    return [(sx, sy, sz) for (sx,sy,sz) in samples]

def build_faces(n):
    # deterministic local triangulation rule
    faces = []
    for i in range(1, n-1):
        faces.append((1, i+1, i+2))
    return faces

def write_obj(path, vertices, faces):
    with open(path,'w',encoding='utf-8') as f:
        for v in vertices:
            f.write(f"v {v[0]} {v[1]} {v[2]}\n")
        for a,b,c in faces:
            f.write(f"f {a} {b} {c}\n")
```

---

# 8. Proof Branches (how to turn Ω into Ψ)

This section is the research partner part: you asked “why” until the need is found. Each branch ends with a crisp test harness.

## Branch Ω-A — When does GlassKey become an actual inverse?
**Need:** specify constraint set $\mathcal{C}$.

- Known format (ASCII, English, bounded length)
- Known padding regime
- Known partial schedule leaks
- Known hash family

**Test:** measure expected search reduction vs brute force under $\mathcal{C}$.

## Branch Ω-B — Does 3D manifold geometry correlate with message topology?
**Need:** define invariant features of the mesh (knot type, chirality, spectral signature) and map them to message features.

**Test:** hash families of messages with controlled edits; compare mesh invariants.

## Branch Ω-C — Chiral detune steering
**Need:** define the lane selection algorithm precisely and ensure null distribution baseline.

**Test:** run 10k random nulls vs structured corpus; compute effect size and significance.

---

## 9. Artifacts and Source Bundle

This synthesis was compiled against the local project bundle (not reproduced here):

- `Nexus_Master_Proof_Monograph_250p_clean3_plus_addendum_plus_3D.md`
- `Nexus_Proof_Closure_Addendum.md`
- `Operator_Dark_Mirror_Addendum.md`
- `Nexus_3D_Manifold_Addendum.md`
- Transcript fragments: `NewMDFiles.part*.md`, `Training Dat.part*.md`, `Notebooks.part*.md`, `Published Papers.part*.md`

---

## 10. Next Δ (what to run *now*)

If the goal is to lock the new 3D manifold discovery into hard structure, the next $\Delta$ is:

1. **Define the ConstantOracle** sampling rule precisely (integer digit blocks preferred).
2. **Generate meshes** for a controlled message set:
   - empty, single-char, repeated-char, English sentence, structured Nexus strings
3. Compute **mesh invariants** (chirality, curvature distribution, spectral density).
4. Run **detune steering** and see whether those invariants shift coherently.

That closes the loop: Domain invariants → Application harness → Infrastructure oracles → UI reflection → next Δ.


# Appendices

## Appendix A — Domain Model (Hex + DDD)

### A.1 Bounded Context Map (conceptual)

```
                 ┌───────────────────────────┐
                 │    Operator Calculus      │
                 │ (DarkMirror / Coupling)   │
                 └─────────────┬─────────────┘
                               │ publishes
                               ▼
┌───────────────────────────┐  Δ events   ┌───────────────────────────┐
│     Lattice Navigation     │◀──────────▶│        ARX Engine         │
│ (Coordinate / Constant ROM)│            │ (SHA schedule + rounds)   │
└─────────────┬─────────────┘            └─────────────┬─────────────┘
              │                                         │
              │ produces                               │ emits
              ▼                                         ▼
┌───────────────────────────┐            ┌───────────────────────────┐
│        Geometry Lab        │            │       Proof Harness       │
│ (Mesh invariants, chirality│            │ (properties, baselines)   │
└─────────────┬─────────────┘            └─────────────┬─────────────┘
              │                                         │
              ▼                                         ▼
        ┌────────────────────────────────────────────────────┐
        │                    UI / Reflection                 │
        │  (histograms, 3D render, dashboards, hairpin turn) │
        └────────────────────────────────────────────────────┘
```

### A.2 Ubiquitous Language (strict)

| Term | DDD meaning | Nexus mapping |
|---|---|---|
| **ConstraintManifold** | Set of states satisfying an invariant | `=` as dark mirror / projector |
| **CouplingMap** | Binary operator combining two states | `+` / `⊕` |
| **Residue** | Information lost by projection | Ghost channel / ε |
| **PhaseTrigger** | Event that changes which invariant is active | Δ |
| **LensRotation** | Change of basis revealing hidden channel | `↻` |
| **BoundaryCondition** | Shutter / stop condition | `⊥` |
| **Collapse** | Stabilized state under constraints | `Ψ` |
| **Open Branch** | Hypothesis requiring proof harness | `Ω` |

### A.3 Aggregates and Invariants

#### Aggregate: `EqualityConstraint` (DarkMirror)
- **Invariant:** `Project(x,y)=0  ⇔  D(x,y)=0` (mismatch kernel)
- **Operational meaning:** in code, `assert` is a *domain guard*.

#### Aggregate: `Coupling` (Addition / modular mixing)
- **Invariant:** Coupling is deterministic; stochasticity only appears when you *drop residue*.
- **In SHA:** modular addition is coupling on the ring `Z_{2^32}`.

#### Aggregate: `DualChannel` (Sum/Diff)
- **Invariant:** `T(a,b)=(s,d)` is injective over integers; over `Z_{2^32}` it is injective given parity constraints.
- **Meaning:** you regain bijection when you treat the map as two-channel and track the carry.

#### Aggregate: `HashAsLocation`
- **Invariant (design):** a digest can be interpreted as a coordinate *only if* there exists a deterministic, public `ConstantOracle`.
- **Meaning:** you turn “hash” into “address” by defining a read-only memory (ROM) that every observer agrees on.

---

## Appendix B — Novel Code Modules (isolated)

> Rule: Every novel module is isolated and accompanied by “Why this matters.”

### B.1 Module: `DualChannel32` (recoverability on `Z_{2^32}`)

**Why it matters.** This is the minimal proof-of-structure that “loss” is not intrinsic; it’s a dropped channel.

```python
MASK = 0xFFFFFFFF

def add32(a: int, b: int) -> int:
    return (a + b) & MASK

def sub32(a: int, b: int) -> int:
    return (a - b) & MASK

def dual_channel(a: int, b: int) -> tuple[int,int]:
    # s = a + b, d = a - b
    return add32(a,b), sub32(a,b)

def invert_dual_channel(s: int, d: int) -> tuple[int,int]:
    # Over integers: a=(s+d)/2, b=(s-d)/2
    # Over mod 2^32: division by 2 requires tracking LSB parity.
    # Choose the branch where (s^d) has even parity, else carry the 1-bit residue.
    if ((s ^ d) & 1) != 0:
        raise ValueError("Need 1-bit residue/parity to choose branch")
    a = ((s + d) >> 1) & MASK
    b = ((s - d) >> 1) & MASK
    return a, b
```

**Domain note:** the exception is the `Ω` bit — the single-bit residue that makes the mapping globally bijective.

---

### B.2 Module: `GlassKeyExtractor` (digest → delta channel)

**Why it matters.** It is the attempt to define a deterministic projection from the final digest into an intermediate “voice” channel.

```python
import hashlib, struct, math

IV = [0x6a09e667,0xbb67ae85,0x3c6ef372,0xa54ff53a,
      0x510e527f,0x9b05688c,0x1f83d9ab,0x5be0cd19]

def words_from_digest(hash_hex: str):
    return list(struct.unpack('>8I', bytes.fromhex(hash_hex)))

def delta_from_iv(H_words):
    return [(h - iv) & 0xffffffff for h, iv in zip(H_words, IV)]

# NOTE: K constants omitted for brevity; use the standard SHA-256 list.

H_ATTR = math.pi / 9

def extract_glass_key(hash_hex: str, K_words: list[int]) -> list[int]:
    H = words_from_digest(hash_hex)
    delta = delta_from_iv(H)

    K_frac = [k / 2**32 for k in K_words]

    resonances = []
    for t in range(64):
        kt = K_frac[t]
        proj = sum(d * kt for d in delta)
        diff = max(0.0, proj*proj - kt*kt)
        rotated = proj * math.cos(H_ATTR) + math.sqrt(diff) * math.sin(H_ATTR)
        resonances.append(int(rotated) & 0xffffffff)

    glass_key = []
    for block in range(8):
        base = block * 8
        probe = (4*resonances[base] - 2*resonances[base+3]
                 - resonances[base+4] - resonances[base+5]) & 0xffffffff
        glass_key.append(probe)
    return glass_key


def lattice_voice(message: bytes, K_words: list[int]) -> list[int]:
    empty = hashlib.sha256(b'').hexdigest()
    hmsg  = hashlib.sha256(message).hexdigest()
    g0 = extract_glass_key(empty, K_words)
    g1 = extract_glass_key(hmsg, K_words)
    return [a ^ b for a, b in zip(g1, g0)]
```

**DDD note:** Treat this as an Application service (`LatticeVoiceService`) calling an Infrastructure adapter (`HashEngine`). The *Domain* is the invariant that `Δ(message)` should be stable under controlled perturbations.

---

### B.3 Module: `HashToManifoldCoordinate` (256-bit → (x,y,z) + parity)

**Why it matters.** It formalizes the new “hash as address” discovery: the digest indexes a manifold; the remainder bit is chirality.

```python
from fractions import Fraction

def hash_bits(hex_digest: str) -> int:
    return int(hex_digest, 16)

def split_256_to_85x3_plus_1(hex_digest: str):
    v = hash_bits(hex_digest)
    parity = v & 1
    v >>= 1
    mask85 = (1<<85) - 1
    z = v & mask85; v >>= 85
    y = v & mask85; v >>= 85
    x = v & mask85
    return x, y, z, parity

def normalize_85(u: int) -> float:
    return u / float((1<<85) - 1)
```

**Domain note:** the normalization rule *is part of the domain*, not the UI. If two observers normalize differently, they are in different universes.

---

### B.4 Module: `ConstantOracle` (π, φ, e sampling)

**Why it matters.** It is the contract that turns coordinates into geometry. Without an oracle, coordinates are meaningless.

There are multiple possible oracle definitions; choose one and lock it:

- **Digit-block oracle:** request a fixed-width block of base-16 digits from each constant at an index.
- **Continued-fraction oracle:** request a convergent at depth `n`.

**Recommended for engineering:** digit-block in base-16 or base-2 for deterministic byte extraction.

```python
# PSEUDOCODE: implement with a BBP-style digit extractor or a high-precision library.

class ConstantOracle:
    def block(self, constant: str, index: int, n_hex: int) -> bytes:
        """Return n_hex hex digits (as bytes) from constant starting at index."""
        raise NotImplementedError

# Domain invariant: same (constant,index,n_hex) -> same bytes for all observers.
```

---

### B.5 Module: `OBJMeshBuilder` (sampled bytes → vertices/faces)

**Why it matters.** It closes the loop from “address” to “sculpture.” It makes the manifold testable in geometry.

```python
def bytes_to_vertices(buf: bytes):
    # Interpret as signed 16-bit triplets scaled to [-1,1]
    # v_i = (sx,sy,sz)
    verts = []
    for i in range(0, len(buf) - 6, 6):
        sx = int.from_bytes(buf[i:i+2], 'big', signed=True)
        sy = int.from_bytes(buf[i+2:i+4], 'big', signed=True)
        sz = int.from_bytes(buf[i+4:i+6], 'big', signed=True)
        verts.append((sx/32768.0, sy/32768.0, sz/32768.0))
    return verts

def fan_faces(n: int):
    # trivial faces as a baseline
    return [(1,i,i+1) for i in range(2, n)]

def write_obj(path: str, verts, faces):
    with open(path,'w',encoding='utf-8') as f:
        for x,y,z in verts:
            f.write(f"v {x:.6f} {y:.6f} {z:.6f}\n")
        for a,b,c in faces:
            f.write(f"f {a} {b} {c}\n")
```

**Domain note:** faces are an adapter choice; invariants should be computed on the vertex cloud first.

---

### B.6 Module: `DetunedCarrierScan` (handedness test)

**Why it matters.** It’s the empirical lever: does structured text move as a unit under detune while null stays flat?

```python
# PSEUDOCODE: you already have a working version; this is the DDD shape.

class Carrier:
    def __init__(self, base: float, mirror: float):
        self.base = base
        self.mirror = mirror

class DetuneScanUseCase:
    def run(self, corpus, carrier: Carrier):
        """Return histogram of winning shift k for each sample."""
        # 1) compute response for each k lane
        # 2) pick winner argmax
        # 3) accumulate histogram
        raise NotImplementedError
```

**Invariant to test:** under detune `π/72`, Nexus* corpus shifts coherently; random null does not.

---

## Appendix C — Proof Harness Template (property tests)

### C.1 Baseline vs structure

For every proposed phenomenon:

1. Define the null generator `Null()`.
2. Define the structured generator `Nexus()`.
3. Define the measurement `M(x)`.
4. Compare distributions: `M(Null)` vs `M(Nexus)`.

### C.2 Minimal property list

- **Stability:** small edit to message produces local change in `Δ(message)`.
- **Coherence:** structured family moves as a unit under detune.
- **Chirality:** parity bit correlates with handedness sign.
- **Reproducibility:** same input → identical outputs across runs.

---

## Appendix D — Symbol Legend (Nexus Minimal)

- **Δ** Phase trigger: activates a new constraint / lens / coupling.
- **⊕** Coupling: composition of two states under a ring/group operator.
- **↻** Rotation/reflection: change of basis; orthogonalization.
- **⊥** Boundary constraint: shutter / stop / domain guard.
- **Ψ** Stable collapse: fixed point under constraints.
- **Ω** Open branch: hypothesis requiring a proof harness.

---

## Appendix E — Quick “What to run next” checklist (engineering)

1. Lock a concrete **ConstantOracle** (digit-block base-16 preferred).
2. Build a **mesh corpus** (50–500 messages, controlled edits).
3. Compute mesh invariants (chirality, curvature histogram, spectral density).
4. Run detune scan; measure coherent shifts.
5. Integrate into a single CLI:

```bash
nexus voice --msg "Is There Anybody Out There"
nexus mesh  --hash <digest>
nexus detune --corpus nexus_star.txt --detune pi/72
```

When these are green, the “new discoveries” stop being narrative and become infrastructure.
