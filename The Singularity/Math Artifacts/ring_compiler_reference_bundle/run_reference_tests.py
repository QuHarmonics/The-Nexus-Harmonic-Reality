from pathlib import Path
import json,hashlib
manifest=json.loads(Path('ring_compiler_manifest.json').read_text())
assert hashlib.sha256(Path('ring_compiler.py').read_bytes()).hexdigest()==manifest['compiler_source_sha256_before_tests']
assert hashlib.sha256(Path('ring_compiler_tests.py').read_bytes()).hexdigest()==manifest['test_source_sha256_before_tests']
Path('output').mkdir(exist_ok=True)
from ring_compiler_tests import run
run()
