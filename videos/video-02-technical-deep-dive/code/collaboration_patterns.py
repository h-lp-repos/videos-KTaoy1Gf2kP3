from __future__ import annotations

import json
from pathlib import Path

DATA_FILE = Path(__file__).resolve().parent.parent / "data" / "collaboration_patterns.json"

ORCHESTRATOR_FLOW = [
    "Receive the user query and inspect metadata to decide which domain owns the intent.",
    "Apply role assignment to map the request to a specialized agent (HR, Tech, or fallback).",
    "Delegate execution to the selected agent while passing the conversation history for context.",
    "Collect the agent response and maintain the handoff log for future turns."
]

CONTEXT_SEQUENCE = [
    "history: [user question]",
    "context stack: [(agent_label, last_response)]",
    "handoff log: [...control messages...]",
]


def load_patterns() -> dict:
    with DATA_FILE.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def main() -> None:
    patterns = load_patterns()
    print("Orchestrator flow summary:")
    for step in ORCHESTRATOR_FLOW:
        print(f"- {step}")

    print("\nContext preservation sequence:")
    for item in CONTEXT_SEQUENCE:
        print(f"- {item}")

    print("\nCollaboration patterns:")
    for pattern in patterns.get("patterns", []):
        print(f"- {pattern['name']}: {pattern['description']}" )
        if pattern.get("example"):  # type: ignore[unreachable]
            print(f"  Example: {pattern['example']}")


if __name__ == "__main__":
    main()
