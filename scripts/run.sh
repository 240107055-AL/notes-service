#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
PY=python3
"$PY" --version >/dev/null 2>&1 || PY=python
exec "$PY" src/server.py
