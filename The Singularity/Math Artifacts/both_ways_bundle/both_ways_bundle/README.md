# The song that plays both ways — §22 of the Compiler Rings log

Dean A. Kulik · QuHarmonics Research Group · ORCID 0009-0003-3128-8828 · 2026-10-20

`python3 -I song_tests.py` reruns S1–S5 against `seal_song.txt` and rewrites the audio. It runs in about 5 s and needs numpy; `wheels.py` must sit beside it.

## Listening guide (22,050 Hz mono)

| File | What it shows |
|---|---|
| 01 / 02 | c-d-e-d-c with symmetric notes, forward and backward: identical, sample for sample. |
| 03 / 04 / 05 | c-d-e-d-c ∣ e-d-c-d-e forward, backward, and inverted about d. Backward equals inverted, sample for sample: the "crash" is the retrograde coming out as the inversion, the ring's twist heard. |
| 06 / 07 | c-d-e-d-c with attack-decay notes, forward and backward. The notes are a palindrome, the file is not: every layer has to be symmetric. |
| 08 / 09 | The 3-bit ring's 24-slice tape as a rhythm (hit = 1, rest = 0), forward and backward. Backward equals the tape with its two palindromic bars inverted. |

The printed ledger shows `S5: False`. Two clauses missed and are routed in the log: there are 12 face-optimal orders at n = 5 instead of 4, and the best address reader is outside-in down to a small core, then by value.
