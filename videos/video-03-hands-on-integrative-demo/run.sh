#!/usr/bin/env bash
set -euo pipefail

if [[ -z "${OPENAI_API_KEY:-}" ]]; then
  echo "Please set OPENAI_API_KEY before running the demo."
  exit 1
fi

python -m pip install --upgrade pip
python -m pip install -r code/requirements.txt
python code/query_router.py --demo
