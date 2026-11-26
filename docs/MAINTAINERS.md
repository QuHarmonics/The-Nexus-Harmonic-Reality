# Maintain the research interface

[Documentation](README.md) · [Catalog](catalog/README.md)

The catalog records commit [df0d09f](https://github.com/QuHarmonics/The-Nexus-Harmonic-Reality/commit/df0d09f8c430bce44660e4986209afdb20395e04), preceding this redesign. Each file has original path, collection, type, Git blob ID and byte count. A Git blob ID is not a raw-file SHA-256 fingerprint. These metadata do not establish a discovery date or unique publication count.

```bash
python tools/verify_public_catalog.py
```

Run from a Git checkout with the snapshot commit available. The checker compares paths, object IDs and byte counts to the exact revision. It does not execute research code. Refresh against an explicit immutable revision.

Keep historical source addresses intact. Link formulas to implementations, dates and evidence. Preserve licenses and attribution. Review publication intent and unrelated material before adding new sources; private working archives are not automatic public inputs.
