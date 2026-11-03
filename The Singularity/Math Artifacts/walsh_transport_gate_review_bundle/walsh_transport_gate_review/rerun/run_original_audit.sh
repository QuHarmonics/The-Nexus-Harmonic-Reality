#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
mkdir -p output
python walsh_transport_audit.py > output/main_stdout.json
python walsh_transport_extra_checks.py > output/extra_checks.json
