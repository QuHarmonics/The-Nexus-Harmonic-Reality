"""Generate a browser edition from the authoritative Atlas; never edit the source."""
import ast
import hashlib
import json
import shutil
from importlib.metadata import version
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "The Nexus Domain/Code/NEXUS_Ring_Atlas.ipynb"
OUT = ROOT / "_browser_lab"
DEST = OUT / "NEXUS_Ring_Atlas_Browser.ipynb"
raw = SOURCE.read_bytes()
nb = json.loads(raw)
cells = nb["cells"]
def source(cell):
    return "".join(cell["source"])
assert "Setup" in source(cells[1]) and "subprocess.check_call" in source(cells[1]), "Atlas setup changed: review browser adapter"
for i, name in enumerate(("ring_core", "ring_lab", "ring_viz", "ring_ui"), 2):
    assert name in source(cells[i]) and "_load_engine" in source(cells[i]), "Atlas engines changed: review adapter"
original_sources = [source(cell) for cell in cells]
setup = f'''# Browser adapter: dependencies run in Pyodide, not in a server process.
# All four embedded engines and chapter cells are inherited unchanged.
RUN_LONG = False  # Set True before running to include the long two-lap checks.
import sys, types
import piplite
await piplite.install(["numpy", "pillow", "plotly=={version("plotly")}", "ipywidgets=={version("ipywidgets")}"])
import plotly.io as pio
pio.renderers.default = "plotly_mimetype"

def _load_engine(name, src):
    m = types.ModuleType(name)
    m.__file__ = name + ".py (embedded in this notebook)"
    sys.modules[name] = m
    exec(compile(src, name + ".py", "exec"), m.__dict__)
    return m

print("browser setup ready · RUN_LONG =", RUN_LONG)
'''
cells[1]["source"] = setup.splitlines(keepends=True)
for cell in cells:
    if cell["cell_type"] == "code":
        cell["outputs"] = []
        cell["execution_count"] = None
    # Saved widget/view state belongs to the original kernel session.
    cell["metadata"] = {}
assert all(source(cell) == original_sources[i] for i, cell in enumerate(cells) if i != 1)
for i in range(2, 6):
    ast.parse(source(cells[i]))
digest = hashlib.sha256(raw).hexdigest()
notice = (
    "## Browser edition\n\n"
    "Run the setup cell first, then the four engine cells and the chapter cells in order. "
    "First execution downloads Python packages into the browser. "
    "Long closure checks are skipped by default; set RUN_LONG=True in setup to run them. "
    "Skipped checks are not new evidence. No remote Python service is required.\n\n"
    "The original notebook is preserved in the repository. Only setup, kernel/display metadata and saved outputs differ; "
    "the mathematical engines and all fifteen chapters remain unchanged. "
    f"Source SHA-256: `{digest}`."
)
cells.insert(1, {"cell_type": "markdown", "metadata": {}, "source": notice.splitlines(keepends=True)})
nb["metadata"].pop("widgets", None)
nb["metadata"]["kernelspec"] = {"display_name": "Python (Pyodide)", "language": "python", "name": "python"}
nb["metadata"]["nexus_browser_adapter"] = {"source": str(SOURCE.relative_to(ROOT)), "source_sha256": digest, "long_checks_default": False}
OUT.mkdir(exist_ok=True)
shutil.copy2(ROOT / "lab/Nexus_Native_Operations.ipynb", OUT)
DEST.write_text(json.dumps(nb, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(f"Prepared {DEST.name}: {DEST.stat().st_size:,} bytes; original {len(raw):,} bytes; source {digest}")
