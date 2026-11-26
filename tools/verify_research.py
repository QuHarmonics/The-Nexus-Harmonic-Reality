#!/usr/bin/env python3
"""Verify public metadata, immutable source addresses and reference operations.

The default check uses Git tree names and blob IDs, not historical blob bodies.
Run verify_public_catalog.py separately for byte-size verification.
"""
import hashlib
import json
import pathlib
import re
import subprocess
from urllib.parse import unquote, urlsplit
from native_reference import audit

ROOT = pathlib.Path(__file__).resolve().parents[1]
REPO = "https://github.com/QuHarmonics/The-Nexus-Harmonic-Reality/"
def git(*args):
    return subprocess.check_output(["git", "-C", str(ROOT), *args])
def load(p):
    return json.loads((ROOT / p).read_text(encoding="utf-8"))
def tree(ref):
    files = {}
    dirs = {""}
    for item in git("ls-tree", "-r", "-z", ref).split(b"\0"):
        if not item:
            continue
        meta, path = item.split(b"\t", 1)
        mode, kind, oid = meta.decode("ascii").split()
        if kind != "blob":
            continue
        p = path.decode("utf-8")
        files[p] = oid
        dirs.update(str(x) for x in pathlib.PurePosixPath(p).parents)
    dirs.discard(".")
    return files, dirs
def check(cond, message):
    if not cond:
        raise AssertionError(message)
catalog = load("docs/catalog.json")
methods = load("docs/methods.json")
snapshot = catalog["source_commit"]
sources, _ = tree(snapshot)
expected = {r["path"]: r["blob"] for r in catalog["files"]}
check(len(expected) == len(catalog["files"]), "duplicate catalog path")
check(expected == sources, "historical catalog does not match source tree")
m = methods["methods"]
ids = {x["id"] for x in m}
check(len(ids) == len(m), "duplicate method ID")
method_sources, _ = tree(methods["source_commit"])
for x in m:
    check(x["source"] in method_sources, f"missing source: {x['id']}")
    check(set(x["dependencies"]) <= ids, f"missing dependency: {x['id']}")
    check(x["return_route"] and x["scope"], f"missing return/scope: {x['id']}")
# Validate only recognized Markdown inline destinations; no network requests.
current, folders = tree("HEAD")
trees = {"HEAD": (current, folders), snapshot: tree(snapshot)}
local_count = 0
for p in sorted(current):
    if not re.search(r"readme.*\.md$", pathlib.PurePosixPath(p).name, re.I) and not p.startswith("docs/catalog/"):
        continue
    if not p.endswith(".md"):
        continue
    s = (ROOT / p).read_text(encoding="utf-8")
    for u in re.findall(r"\]\(([^)\s]+)\)", s):
        if u.startswith("#"):
            continue
        if u.startswith(REPO):
            parts = urlsplit(u).path.strip("/").split("/")
            if len(parts) >= 4 and parts[2] in ("blob", "tree"):
                ref = parts[3]
                if ref == "main":
                    ref = "HEAD"
                if ref not in trees:
                    trees[ref] = tree(ref)
                target = unquote("/".join(parts[4:]))
                files, dirs = trees[ref]
                check(target in files or target in dirs, f"{p}: {u}")
                local_count += 1
            continue
        if urlsplit(u).scheme or u.startswith("//"):
            continue
        target = (ROOT / pathlib.PurePosixPath(p).parent / unquote(urlsplit(u).path)).resolve()
        check(target.is_relative_to(ROOT) and target.exists(), f"{p}: {u}")
        local_count += 1
crate = load("ro-crate-metadata.json")
entities = {x["@id"]: x for x in crate["@graph"]}
check("ro-crate-metadata.json" in entities and "./" in entities, "RO-Crate root missing")
for item in entities["./"]["hasPart"]:
    p = item["@id"]
    check(p in entities and (ROOT / unquote(p)).is_file(), f"missing crate part: {p}")
results = audit()
report = {
    "commit": git("rev-parse", "HEAD").decode().strip(),
    "source_snapshot": snapshot,
    "catalog_entries": len(expected),
    "method_records": len(m),
    "repository_link_destinations": local_count,
    "reference_checks": results,
    "scope": "File identity, dependency existence, recognized internal links and finite native reference audit; not independent verification of all research claims.",
    "method_registry_sha256": hashlib.sha256((ROOT / "docs/methods.json").read_bytes()).hexdigest(),
}
out = ROOT / "verification-report.json"
out.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
print(json.dumps(report, indent=2))
