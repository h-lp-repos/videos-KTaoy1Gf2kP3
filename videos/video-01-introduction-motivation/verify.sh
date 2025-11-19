#!/usr/bin/env bash
set -euo pipefail

output=$(python code/motivation_overview.py)
if ! grep -q "Single-agent challenges:" <<< "$output"; then
  echo "Motivation script missing the single-agent narrative."
  exit 1
fi
if ! grep -q "Learning objectives for this section:" <<< "$output"; then
  echo "Motivation script is not printing the learning objectives."
  exit 1
fi

echo "CHECKPOINT 1: Scenario narrative articulates single-agent limitations and multi-agent advantages."
echo "CHECKPOINT 2: Learning objectives are listed for the lesson and scoped clearly."
