#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."

PY=python3
"$PY" --version >/dev/null 2>&1 || PY=python

set +e
out=$("$PY" -m unittest discover -s tests 2>&1)
code=$?
set -e

echo "$out"
total=$(echo "$out" | sed -n 's/^Ran \([0-9]*\) test.*/\1/p')
total=${total:-0}

if [ "$code" -eq 0 ]; then
  echo "TESTS: $total/$total"
else
  echo "TESTS: 0/$total"
  exit 1
fi
