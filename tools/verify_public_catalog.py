#!/usr/bin/env python3
"""Check the public catalog against its immutable Git tree."""
import json
import pathlib
import subprocess
import sys

root = pathlib.Path(__file__).resolve().parents[1]
catalog = json.loads((root / "docs" / "catalog.json").read_text(encoding="utf-8"))
commit = catalog["source_commit"]
try:
    raw = subprocess.check_output(["git", "-C", str(root), "ls-tree", "-r", "-l", "-z", commit])
except (subprocess.CalledProcessError, FileNotFoundError) as exc:
    sys.exit(f"Cannot read snapshot {commit}: {exc}")
actual = {}
for entry in raw.split(b"\0"):
    if entry:
        meta, path = entry.split(b"\t", 1)
        mode, kind, sha, size = meta.decode("ascii").split()
        if kind == "blob":
            actual[path.decode("utf-8")] = (sha, int(size))
expected = {}
for row in catalog["files"]:
    path = row["path"]
    if path in expected:
        sys.exit(f"Duplicate catalog path: {path}")
    expected[path] = (row["blob"], row["bytes"])
missing = sorted(actual.keys() - expected.keys())
extra = sorted(expected.keys() - actual.keys())
changed = sorted(p for p in actual.keys() & expected.keys() if actual[p] != expected[p])
if missing or extra or changed:
    print(json.dumps({"missing": missing, "extra": extra, "changed": changed}, indent=2))
    sys.exit(1)
print(f"PASS: {len(expected)} source files match {commit} exactly.")
