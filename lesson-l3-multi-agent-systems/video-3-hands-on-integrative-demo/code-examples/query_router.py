# query_router.py

import os
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage

def classify_and_route(query: str) -> str:
    llm = ChatOpenAI(temperature=0)
    functions = [
        {"name": "hr_agent", "description": "Handle HR related queries"},
        {"name": "tech_agent", "description": "Handle technical queries"},
    ]
    response = llm(
        messages=[HumanMessage(content=query)],
        functions=functions,
        function_call="auto"
    )
    function_call = response.additional_kwargs.get("function_call", {})
    func_name = function_call.get("name")
    if func_name == "hr_agent":
        return f"HR Agent: Responding to '{query}'"
    elif func_name == "tech_agent":
        return f"Tech Agent: Responding to '{query}'"
    else:
        return f"No suitable agent found for '{query}'"

def main():
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("Please set OPENAI_API_KEY environment variable.")
    while True:
        user_input = input("Enter your query (or 'exit'): ")
        if user_input.lower() == "exit":
            break
        print(classify_and_route(user_input))

if __name__ == "__main__":
    main()
