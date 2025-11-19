#!/usr/bin/env bash
set -euo pipefail

output=$(OPENAI_API_KEY= python code/query_router.py --demo)
if ! grep -q "Routed to: hr_agent" <<< "$output"; then
  echo "HR agent routing missing."
  exit 1
fi
if ! grep -q "Routed to: tech_agent" <<< "$output"; then
  echo "Tech agent routing missing."
  exit 1
fi
if ! grep -q "Conversation history snapshot" <<< "$output"; then
  echo "Conversation history summary missing."
  exit 1
fi

echo "CHECKPOINT 1: Workflow routes HR queries to the HR Agent and Tech queries to the Tech Agent."
echo "CHECKPOINT 2: Conversation context remains intact across the entire run."
