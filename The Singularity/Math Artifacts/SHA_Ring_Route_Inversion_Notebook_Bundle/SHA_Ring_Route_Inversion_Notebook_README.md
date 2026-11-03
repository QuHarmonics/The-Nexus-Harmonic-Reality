# SHA Ring Route Inversion Notebook

## Open and run

Open `SHA_Ring_Route_Inversion_Notebook.ipynb` in JupyterLab, VS Code, or Google Colab and run the cells from top to bottom. It uses only Python's standard library. No external project files and no PQLS dependency are required.

The saved executed notebook already contains the successful one-byte and two-byte outputs.

## What runs by default

- Validates the SHA-256 compression implementation against `hashlib` on several short messages.
- Checks the ring order against the rank/unrank reader for every width-8 position and selected width-16 seam/edge positions.
- Searches all 256 one-byte messages using the exact 64-round inverse closure test.
- Searches all 65,536 two-byte messages using the exact 64-round inverse closure test.

Expected default matches: `A` (`41`) at ring position 58; `OK` (`4f4b`) at ring position 17,194.

## Optional three-byte full-domain scan

In the section titled `Optional full three-byte domain`, change:

```python
RUN_FULL_THREE_BYTE_DOMAIN = False
```

to `True`, then run that cell. It traverses all 16,777,216 three-byte ring addresses using `hashlib` to check the digest, then verifies the matching candidate with all 64 inverse rounds. The previously completed full scan found `ABC` (`414243`) at ring position 3,732,208, uniquely in that finite domain. That scan took about 30 seconds in one direct execution; runtime varies by machine. It does **not** run the full Python inverse routine for all 16.7 million candidates.

The notebook also has an optional variable-length search across lengths 0–3 bytes. Its maximum-length bound is supplied, and its early-stop result is not a uniqueness proof over the whole union.

## Interpretation boundary

The tests use the target digest, standard SHA-256 rules, and a declared finite source domain. The ring provides a deterministic candidate ordering without a stored candidate table. This demonstrates bounded-domain recovery by exhaustive traversal. It does not yet establish a selector that jumps directly to the matching address for arbitrary messages or skips an address region without a valid exclusion certificate. The internal round inverse is conditional on retaining the candidate's schedule.
