# THE ONTOLOGICAL INVERSION
## No Observers, Only Subscribers

---

## THE INSIGHT

> "There are no observers, just subscribers. Reactive programming. Run the code every time. This is a zero-g chamber so the waves can just be themselves. T1 and T2 are part of this computation - they are not the end. The routes are inside the packets. The packets are the methods and we are just subscribers and emitters. And sometimes parameters."

---

## NO OBSERVERS

There is no "observer" outside the system.
Everyone is a node in the reactive stream.

### ROLES (not fixed identities)

| Role | Function |
|------|----------|
| **Subscriber** | Pulls data by creating vacuum |
| **Emitter** | Pushes data into matching vacuum |
| **Parameter** | Data being routed |
| **Method** | Transformation being applied |

You're all of these at different moments.
No fixed identity. Just current role.

---

## THE ROUTES ARE INSIDE THE PACKETS

The SHA state IS the packet.
The shift pattern IS the route.

```
Each round:
  h,g,f,e,d,c,b,a = g,f,e,d+T1,c,b,a,T1+T2
```

This isn't an external routing table.
**The route IS the structure of the packet.**
The packet knows where it's going because its SHAPE defines the path.

### Route Information Source

```
Internal (from packet): 31.4 bits/round
External (K+W):         15.9 bits/round
Ratio: 2× more internal
```

**The packet carries its own destination.**

---

## T1 AND T2 ARE METHODS, NOT ENDPOINTS

T1 and T2 aren't "results" — they're TRANSFORMATIONS.

```python
def T1_method(state, K_r, W_r):
    """T1 is a method, not a value"""
    a, b, c, d, e, f, g, h = state
    return h + Sig1(e) + ch(e,f,g) + K_r + W_r

def T2_method(state):
    """T2 is a method, not a value"""
    a, b, c, d, e, f, g, h = state
    return Sig0(a) + maj(a,b,c)

def route_method(state, T1, T2):
    """The shift is the routing"""
    return (T1+T2, a, b, c, d+T1, e, f, g)
```

They're not the destination. They're the ROUTING FUNCTION.
The destination is wherever the vacuum is.

---

## THE STREAM

```
H0        = initial subscriber (creates vacuum)
K         = the network (topology)
W         = payload packets (message)
State     = current packet in transit
T1/T2     = routing methods
Hash      = final state (became an emitter)
```

### The Cycle of Roles

```
Block 1: H0 subscribes → hash emits
Block 2: hash subscribes → new_hash emits
Block N: prev_hash subscribes → final_hash emits
```

**The subscriber becomes the emitter.**

---

## WE ARE PARAMETERS

Sometimes you're the subscriber (pulling).
Sometimes you're the emitter (pushing).
Sometimes you're the parameter (being routed).

In SHA:
- State at round 0: **subscriber** (waiting for W)
- W[r] at each round: **parameter** (being processed)
- State at round 64: **emitter** (becomes hash)
- Hash: **parameter** to next block (being routed)

There's no "outside" to observe from.
**Everything is inside the computation.**

---

## THE ZERO-G CHAMBER

This is why SHA is a zero-g chamber:

- No base class = no inheritance = no fixed identity
- Everything is a method call, not an object
- Routes are inside packets, not external tables
- Subscribers create vacuums, data falls in
- No "observer" — just nodes in the stream

**The waves can just BE themselves because:**
- No interface friction
- No inheritance tax
- No external observer collapsing them
- Just methods calling methods

T1 and T2 aren't watching the computation.
**They ARE the computation.**

---

## SHA AS REACTIVE STREAM

```javascript
Observable.from(message)
  .chunk(512)
  .scan(H0, (state, block) =>
    Observable.range(0, 64)
      .reduce(state, (s, r) => {
        T1 = s.T1_method(K[r], W[r])
        T2 = s.T2_method()
        return s.route(T1, T2)
      })
  )
  .map(state => state + H0)
  .subscribe(hash => ...)
```

No observers.
Only subscribers creating vacuums.
Only emitters filling them.
Only parameters being routed.
Only methods being called.

**The computation doesn't HAVE observers.**
**The computation IS the only thing.**

---

## THE INVERSION COMPLETE

```
OLD ONTOLOGY (observer-based):
  - Observer watches system
  - System has state
  - Observer collapses wave
  - External measurement

NEW ONTOLOGY (reactive):
  - No observers, only subscribers
  - No state, only transformations
  - No collapse, only routing
  - Routes inside packets
  - Everything is a node
  - Everyone changes roles
```

---

*"The packets are the methods and we are just subscribers and emitters. And sometimes parameters."*

This is the ontological inversion.
This is reactive programming.
This is the zero-g chamber.
This is why the hash is transparent.
