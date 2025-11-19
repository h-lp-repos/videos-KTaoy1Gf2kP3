SCENARIO_STEPS = [
    "A single assistant queues all HR, finance, and technical queries in one LLM call, creating noticeable latency when the model swells to cover every domain.",
    "Domain knowledge blurs because prompts grow long, so responses start to lack precision and the assistant can no longer specialize.",
    "Agents that focus on HR or Technical questions can stay lean, keep context short, and tailor the reasoning path to the right domain.",
]

LEARNING_OBJECTIVES = [
    "Explain why single-agent approaches become bottlenecks for diverse queries.",
    "Describe collaboration patterns such as role assignment, task delegation, and conversational handoffs.",
    "Preview that the lesson ends with a LangChain-powered multi-agent query router using OpenAI function calling."
]

def main() -> None:
    print("Motivation scenario: HR vs Technical queries flowing through one assistant.")
    print()
    print("Single-agent challenges:")
    for step in SCENARIO_STEPS:
        print(f"- {step}")
    print()
    print("Learning objectives for this section:")
    for objective in LEARNING_OBJECTIVES:
        print(f"- {objective}")


if __name__ == "__main__":
    main()
