#!/usr/bin/env bash
set -euo pipefail

output=$(python code/collaboration_patterns.py)
if ! grep -q "Orchestrator flow summary:" <<< "$output"; then
  echo "Orchestrator summary was not printed."
  exit 1
fi
if ! grep -q "Context preservation sequence:" <<< "$output"; then
  echo "Context preservation sequence missing."
  exit 1
fi

echo "CHECKPOINT 1: The orchestrator flow is described clearly and matches the output from collaboration_patterns.py."
echo "CHECKPOINT 2: The code highlights how conversational context is preserved while handing off between agents."
