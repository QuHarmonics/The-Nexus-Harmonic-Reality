# SHA-256 as a ring-addressed boundary-value problem

**Record date:** 19 October 2026  
**Purpose:** Apply the nested-ring address/partner construction to the SHA-256 inverse problem, then state exactly what the executable tests establish.

## Executive result

The ring can serve as a rule-defined traversal of a candidate-message domain. Starting from a target SHA-256 digest and a declared input length, the candidate search can walk ring addresses, construct each message's schedule, and test whether the corresponding SHA-256 route closes at the known initial state. This was executed on three complete finite domains:

- all 256 one-byte messages: unique match `41` (`A`) at ring position 58;
- all 65,536 two-byte messages: unique match `4f4b` (`OK`) at ring position 17,194;
- all 16,777,216 three-byte messages: unique match `414243` (`ABC`) at ring position 3,732,208.

For the one- and two-byte cases, every candidate was tested through the exact reverse-round condition. For the three-byte case, every ring address was streamed and checked against the target digest using the standard forward SHA-256 implementation; the recovered candidate was then independently run through the exact 64-round inverse and returned to the SHA initial state. No candidate-to-digest table was stored. The source strings listed above were used only to define reproducible targets and validate the recovered outputs; the search itself consumed the target digest and the declared source domain.

This is a real, bounded-domain digest-driven recovery. The three-byte scan took 27.456 seconds. It remains exhaustive candidate traversal; no direct, non-enumerative address selector for arbitrary-length messages has been established by these tests.

## 1. The digest boundary exposes an exact terminal state

For a single SHA-256 block and the standard initial chaining value `IV`, let `S64` be the eight-word working state after 64 rounds, before the final feed-forward addition. The final digest words satisfy

\[
H_1[i] = IV[i] + S_{64}[i] \pmod {2^{32}}, \qquad i=0,\ldots,7.
\]

Consequently, the digest and fixed initial state determine the terminal working state exactly:

\[
\boxed{S_{64}[i] = H_1[i] - IV[i] \pmod {2^{32}}.}
\]

This is the key boundary equation. It does not require the original message. It also does not by itself give the unknown message schedule.

For a candidate message `m` of a declared length at most 55 bytes, the message and standard SHA padding fit in one 512-bit block. That block determines the 64-word schedule `W(m)`. Each SHA-256 round is invertible when `W_t` and `K_t` are supplied, so define

\[
I_{W(m)} = R^{-1}_{W_0,K_0}\circ R^{-1}_{W_1,K_1}\circ\cdots\circ R^{-1}_{W_{63},K_{63}},
\]

where composition order is understood as applying the round inverses from round 63 down to round 0. Then a candidate matches the target exactly when

\[
\boxed{I_{W(m)}(H_1-IV)=IV.}
\]

This turns preimage search into a concrete boundary-value condition: *which candidate schedule makes the reverse trajectory land on the required root?*

## 2. The ring supplies addresses for the candidate domain

For width `L`, the ring reader `R_L[i]` contains every `L`-bit word exactly once. When the declared message consists of `n` bytes, use `L=8n` and interpret each ring word as a candidate message. The candidate set compatible with digest `h` and declared length `n` is

\[
\mathcal F_{h,n}=\{R_{8n}[i]: I_{W(R_{8n}[i])}(h-IV)=IV\}.
\]

The ordering is not needed to prove that the candidate set exists, but it gives a canonical route through it. The implementation generates the canonical half and supplies the other half by the partner involution plus the specified center swap; it does not save an array containing the full ring. In the three-byte run, all 2^24 candidate addresses were streamed in this ordering.

This is the precise connection: the ring is an addressable organization of possible drivers/messages, and the SHA inverse-round relation is the closure test that labels an address compatible or incompatible with the requested terminal readout.

## 3. Executed results

| Declared source domain | Candidate addresses | Target digest | Unique match | Ring position | Search/closure method |
|---|---:|---|---|---:|---|
| 1 byte | 256 | `559aead08264d5795d3909718cdd05abd49572e84fe55590eef31a88a08fdffd` | `41` (`A`) | 58 | Exact reverse-round predicate for every candidate |
| 2 bytes | 65,536 | `565339bc4d33d72817b583024112eb7f5cdf3e5eef0252d6ec1b9c9a94e12bb3` | `4f4b` (`OK`) | 17,194 | Exact reverse-round predicate for every candidate; 9.707 s |
| 3 bytes | 16,777,216 | `b5d4045c3f466fa91fe2cc6abe79232a1a57cdf104f7a26e716e0a1e2789df78` | `414243` (`ABC`) | 3,732,208 | Streamed ring-order digest comparison; recovered candidate then exact inverse-round closure; 27.456 s |

The SHA constants and initial state were derived using high-precision arithmetic and the implementation was checked against Python's independent `hashlib.sha256` on five one-byte inputs before the search. The reverse-round check passed for those known forward routes. In the one- and two-byte search scripts, the inverse condition was applied to every candidate. The three-byte search's full-domain filter used the standard digest computation, and the resulting match was then independently tested through the inverse route.

## 4. What this does and does not establish

**Established by the executable runs:**

1. The digest plus the fixed initial state gives an exact terminal working state at the final feed-forward boundary.
2. The ring ordering can enumerate each candidate in a finite declared source domain without storing a lookup table.
3. Fixed-driver SHA rounds can be reversed and used as an exact root-closure predicate.
4. For the three tested target digests, each declared domain had exactly one candidate matching the target.

**Still open:**

1. A general, non-enumerative rule that jumps from an arbitrary digest to the compatible ring address.
2. Recovery when the original message length/domain is not declared.
3. A proof that the route chosen from a digest is the historical original for unrestricted message domains.
4. A minimum residual or selector that preserves the original member of a digest fiber without merely re-encoding the source.

The universal version of “the digest alone recovers every original message” cannot hold over unrestricted message classes: SHA-256 outputs only 256 bits, while the set of all 33-byte messages has 2^264 members. By pigeonhole, distinct 33-byte messages must share at least one digest. Thus no function of the digest alone can return the original for *every* message in that class. This does not rule out exact recovery on an injective restricted domain, a canonical section, or a direct selector for a declared structured family.

This is not a reason to dismiss the ring. It identifies the exact requirement for the next step: prove that a proposed address law selects the right member of the target fiber over a declared source family, then test whether the selector avoids exhaustive traversal.

## 5. Reproducibility files

- `sha_ring_route_test.py`: SHA constants, one-block schedule expansion, round inverse, exact 1-byte ring-address search.
- `sha_ring_route_test_2byte.py`: full 65,536-candidate ring-order search with exact reverse-round predicate.
- `sha_ring_route_test_3byte.py`: streaming 2^24-candidate ring traversal, standard digest check, and inverse-route closure of the match.
- `rule_based_ring.py`: source ring rank/unrank and partner definition used for small-width cross-checks.
- JSON result records preserve exact digests, matching addresses, timings, and scope limitations.

## Ledger

- **DERIVED:** `S64 = H1 - IV (mod 2^32)` at the one-block feed-forward boundary.
- **STANDS:** fixed-schedule SHA-256 round is bijective; 64 fixed-driver rounds compose to a bijection.
- **RUNS:** exact complete-domain recoveries for the declared 1-byte and 2-byte classes; complete three-byte streamed ring search and inverse closure.
- **OPEN:** a non-enumerative digest-to-address selector at scale; unknown-length inversion; exact recovery of the historical input over unrestricted domains.
