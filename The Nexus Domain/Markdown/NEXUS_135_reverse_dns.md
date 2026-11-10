# § 135 — Reverse DNS is the routing law (the digest-only gap, re-owned)

Dean A. Kulik, QuHarmonics Research Group · ORCID 0009-0003-3128-8828 · 17 Oct 2026
Seal `417f74fca5bed94ee787afcf953c0844b6a6bb968ed6f947042cc950371af905`
(SHA-256 of the prediction text, including its way home, sealed before any data was linked).
Live output: `reverse_dns_fit.py`. Standard library only, forward hashing throughout.

## The gap, named by type

§§ 131 and 134 carried one item as **DEAD END**: "digest-only return." That word was
wrong, and the record's own rule — there are no dead ends, only transformations that run
in a different direction — is what corrects it. A DEAD END means the route ran and the
landing belongs to someone else; the move is to route it back to its owner, not to stop.
This entry routes it back.

The gap is not "recover the message from the digest." Named by type, it is a **binding**:
the relation address → owner. The forward route already **RUNS** — a route inverts given
its drivers (schedule words, constants, incoming chaining value). Subtract that. The
remainder is exactly the binding, and the binding is a **copy of a PTR record**: a
name published in advance, read by the other wave at an offset, then forward-confirmed.
Reverse DNS is that structure, and it is the general shape of all resolution.

## Reverse DNS, exactly as it resolves

A reverse lookup never derives the owner from the address. It takes the address as a key,
reads a **PTR record published in advance**, gets the name, forward-resolves that name, and
confirms it lands back on the address (FCrDNS). Two parts: a stored binding, and a forward
check. The key's bits do not contain the owner; the registry does. That is the whole fit —
every aspect of computation is routing, and routing resolves against a written binding, not
by computing the destination out of the key.

Mapped onto the digest, one-to-one:

- digest = the address / key
- the route that produced it (W, K, incoming H) = the owner
- **PTR record = the kept residual** — the binding published when the route ran
- forward-confirm = re-run the route and check it lands on the digest

When the residual was kept, lookup + forward-confirm **is** the drivers-kept round inverse
that already RUNS. That is reverse DNS working on the digest — it compiles.

The one direction that does not run is the one that is not reverse DNS: pulling the owner
out of the address bits with **no PTR published**. Reverse DNS has no mechanism for that
either — an address with no record returns **NXDOMAIN**, and the resolver does not
synthesize a name from the octets. "Owner from the key with no registry" is precisely
**SEARCH**, the one move the method forbids. So the preimage reading is not a limitation
of this result; it is a category error the framework refuses on its own terms. The digest
is complete as itself; its 64-round trajectory was never a second object sitting underneath
it, it was reader-side the whole time.

## What ran (`reverse_dns_fit.py`, all exact)

| claim | what was run | landing |
|---|---|---|
| **P1** address is its own route | width-8 register, shift in the destination's own 8 bits from every start | 65,536 / 65,536 pairs land in 8 steps, 0 misroutes — route, not search. **RUNS** |
| **P2** published binding resolves | content-addressed store, 5,000 objects; resolve + forward-confirm (re-hash owner = address) | 5,000 / 5,000. **RUNS** |
| **P3** empty fiber = NXDOMAIN | 5,000 unpublished addresses queried | 0 synthesized an owner; resolver returns the empty set. **RUNS** |
| **P4** forced collision = multi-PTR | 2⁴+1 = 17 distinct objects into 16 addresses | 3 addresses hold ≥ 2 owners (AMBIGUOUS, the multi-PTR case DNS permits). **RUNS** |
| **P5** FCrDNS is the validity test | honest binding vs a spoofed owner claiming the same address | honest accepted, spoof rejected — "no WHAT without a way home." **RUNS** |
| **P6** self-publishing binding | the § 123 difference engine M (subset-XOR) on every boolean value-table at n = 3 | M·M = I on 256 / 256; resolve and forward-confirm are the same op, no external registry. **RUNS** |

P1 is the § 131 destination-shift result (256/256, zero misroutes) read as DNS routing.
P6 is the sharpest half: when the binding is an **involution**, publishing and confirming
are one operation, so the store needs no registry at all — the address and its owner resolve
to each other by re-applying the engine. That is the kept residual (the fold) seen as a PTR
that writes itself.

## Correction in place

§§ 131 / 134 "digest-only return: **DEAD END**" → **UNBOUND**, owner named. The owner is the
published binding (the kept residual / PTR), and the routing law it resolves under is reverse
DNS: address → published binding → forward-confirm. UNBOUND is not absence; it names the next
WHAT — *keep the route / publish the binding*. Logged where it arose, not silently.

## One mechanism, three domains

- **keep the residual** (the fold, § 99.1, § 123) = publish the PTR record.
- **retained-driver inference** (the AI rebuild, § 134-tail): a forward pass that publishes
  its own PTR — keeps the drivers it read by — so the pass is a WHAT, resolvable in both
  directions, instead of a digest-only reader that keeps the landing and drops the route.
- **reverse DNS** = the general name: resolution is lookup + forward-confirm against a binding
  that was written. Same mechanism, read at three widths.

The two prices sit where the record already puts them: a reversible route is free (the lookup
and the forward-confirm merge nothing); the one priced step is the blind overwrite — a binding
written over a published one with no record kept, which is the only place a way home is lost.

## Ledger

- reverse DNS as a routing law (address → published binding → forward-confirm): **STANDS** — that is how resolution works (DNS/FCrDNS, content-addressed stores, Git objects, IPFS, Kademlia).
- digest resolves when the residual was kept (PTR published): **RUNS** — the drivers-kept round inverse; P2, P6.
- route, not search (address is its own route): **RUNS** — P1, 65,536/65,536.
- empty fiber = NXDOMAIN, no synthesis: **RUNS** — P3.
- forced collision = multi-PTR / AMBIGUOUS: **RUNS** — P4 (pigeonhole, exact).
- FCrDNS validity (no WHAT without a way home): **RUNS** — P5.
- digest-only return with no residual kept: **UNBOUND**, names the next WHAT (publish the binding) — not DEAD END. Supersedes the §§ 131/134 word.
- owner-from-bits with no binding (preimage / message recovery): **not in the field** — it is SEARCH, which reverse DNS (NXDOMAIN) and the method both refuse. Not built, by design.

## Still OPEN (unchanged by this entry)

- the balanced-lane density law (§§ 120, 130);
- the digest-only minimal root observer — by counting a **cost frontier**, not a missing link (a minimal cheaply-decodable observer would be a preimage oracle, § 114.5);
- the tick gradient for gravity (§ 116);
- Law 3;
- retained-driver inference as a written mechanism, and its first exact measurement site (the partial trace ρ_S = Tr_E ρ_SE) — the typed map from retained residual to a readable observable.

Way home for the entry: re-run `reverse_dns_fit.py`; its printed seal must equal `417f74fc…`
and P1–P6 must land as above.
