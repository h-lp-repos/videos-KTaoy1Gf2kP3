# Guion para video 3

## [00:00–01:30] Demo overview
1. Describe the project goal: build an orchestrator that routes queries to HR and Tech agents.
2. Show the workflow diagram with arrows connecting the orchestrator to each agent and the conversation history store.
3. Mention that the guiding script uses LangChain function calling plus a keyword fallback for reliability.

## [01:30–03:30] Environment setup
1. Confirm Python 3.9+ is active and that `OPENAI_API_KEY` is exported (display `env.example`).
2. Open `code/query_router.py` in the editor and overview the structure (sample queries, classification logic, history tracking).
3. Optional checkpoint: run `python -m pip --version` and `python -m pip show langchain` to verify dependencies.

## [03:30–06:00] Defining the agents
1. Walk through the `TOOLS` list and explain how the orchestrator defines HR and Tech agent functions.
2. Show the fallback routing logic, highlighting the keyword lists, and mention default responses.
3. Cue: mention that actual classification uses OpenAI function calling when the API key is present.

## [06:00–09:00] Implementing query routing
1. Review `classify_and_route`, discussing how it first tries the LLM and falls back safely.
2. Stress the importance of the conversation history list maintained by `RoutedResponse` entries.
3. Use the script output to show sample queries being routed and the context lines that follow.

## [09:00–12:00] Handling conversational handoffs
1. Trigger `bash run.sh -- demo` (the script runs by default) to stream the sample queries.
2. After each query outputs, highlight which agent handled it and how the conversation history snapshot keeps track of previous turns.
3. Mention the console lines and labels for the HR agent and the Tech agent to align with the checkpoints.

## [12:00–15:00] End-to-end demo and error handling
1. Show a manual query in interactive mode (if time allows) and mention how the fallback triggers if the key is missing.
2. Discuss troubleshooting: verifying environment variables, verifying pip dependencies, editing keyword lists.

## [15:00–18:00] Wrap-up
1. Summarize what was built and encourage experimentation by adding more agents or logging.
2. Transition to the next lesson focused on tracing and evaluation.

### Comandos que se ejecutan
- `bash run.sh` – installs requirements and runs `python code/query_router.py --demo` with the sample queries.
- `bash verify.sh` – demonstrates the checkpoint lines without requiring a live OpenAI key.
