import argparse
import os
import textwrap
from dataclasses import dataclass
from typing import List, Optional

from dotenv import load_dotenv
load_dotenv()

try:
    from langchain_openai import ChatOpenAI
    from langchain_core.messages import HumanMessage
except ImportError:  # pragma: no cover
    ChatOpenAI = None
    HumanMessage = None

TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "hr_agent",
            "description": "Handle HR related queries",
            "parameters": {"type": "object", "properties": {}},
        },
    },
    {
        "type": "function",
        "function": {
            "name": "tech_agent",
            "description": "Handle technical queries",
            "parameters": {"type": "object", "properties": {}},
        },
    },
]

SAMPLE_QUERIES = [
    "What are the remaining PTO policies for new hires?",
    "Why did the latest deploy fail in staging?",
    "Can you explain the payroll changes for contractors?",
]

HR_KEYWORDS = ["hr", "benefits", "payroll", "vacation", "leave"]
TECH_KEYWORDS = ["deploy", "error", "bug", "infrastructure", "service"]

DEFAULT_MODEL = os.getenv("OPENAI_MODEL", "gpt-4o-mini")


@dataclass
class RoutedResponse:
    agent: str
    response: str


def create_llm() -> Optional[ChatOpenAI]:
    api_key = os.getenv("OPENAI_API_KEY", "")
    if not api_key or ChatOpenAI is None or HumanMessage is None:
        return None
    return ChatOpenAI(model=DEFAULT_MODEL, temperature=0)


def fallback_route(query: str) -> str:
    lower = query.lower()
    if any(word in lower for word in HR_KEYWORDS):
        return "hr_agent"
    if any(word in lower for word in TECH_KEYWORDS):
        return "tech_agent"
    return "hr_agent"


def fallback_response(agent: str, query: str) -> str:
    if agent == "hr_agent":
        return "HR Agent: Refer to benefits documents and scheduling policy before replying."
    return "Tech Agent: Investigate logs, fetch deployment status, and replay the failing command."


def classify_and_route(query: str, llm: Optional[ChatOpenAI] = None) -> RoutedResponse:
    if llm and HumanMessage:
        messages = [HumanMessage(content=query)]
        response = llm.invoke(messages, tools=TOOLS)
        if hasattr(response, "tool_calls") and response.tool_calls:
            tool_call = response.tool_calls[0]
            agent = tool_call["name"]
            text = tool_call.get("arguments", {}).get("response", "")
            return RoutedResponse(agent=agent, response=text or fallback_response(agent, query))
    agent = fallback_route(query)
    return RoutedResponse(agent=agent, response=fallback_response(agent, query))


def describe_history(history: List[RoutedResponse]) -> str:
    lines = []
    for idx, entry in enumerate(history, start=1):
        lines.append(f"{idx}. {entry.agent} handled the request with response: {entry.response}")
    return "\n".join(lines)


def run_demo(llm: Optional[ChatOpenAI]) -> None:
    history: List[RoutedResponse] = []
    print("Running the multi-agent query router demo with sample data.\n")
    for query in SAMPLE_QUERIES:
        print(f"Query: {query}")
        routed = classify_and_route(query, llm)
        history.append(routed)
        print(f"Routed to: {routed.agent}")
        print(f"Agent response: {routed.response}\n")
    print("Conversation history snapshot:")
    print(describe_history(history))


def run_interactive(llm: Optional[ChatOpenAI]) -> None:
    history: List[RoutedResponse] = []
    print("Interactive mode ready. Type 'exit' to quit.")
    while True:
        prompt = input("Enter your query (or 'exit'): ").strip()
        if prompt.lower() == "exit":
            break
        routed = classify_and_route(prompt, llm)
        history.append(routed)
        print(f"Routed to: {routed.agent}")
        print(routed.response)
        print("---")
    print("Conversation summary:")
    print(describe_history(history))


def main() -> None:
    parser = argparse.ArgumentParser(description="Demo multi-agent query router.")
    parser.add_argument("--demo", action="store_true", help="Run the sample query demo.")
    args = parser.parse_args()

    llm = create_llm()
    if args.demo:
        run_demo(llm)
    else:
        if llm is None:
            print("No OPENAI_API_KEY found. Falling back to keyword routing for interactive mode.")
        run_interactive(llm)


if __name__ == "__main__":
    main()
