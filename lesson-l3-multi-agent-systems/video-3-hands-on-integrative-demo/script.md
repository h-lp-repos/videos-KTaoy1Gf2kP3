# Script: Video 3 – Hands-On Integrative Demo

## [00:00–01:30] Demo Overview
- Describe project goal: multi-agent query router with Orchestrator, HR, Tech Agents.
- Present workflow diagram.

## [01:30–03:30] Environment Setup
- Check Python version & packages.
- Open starter code/notebook.
- Checkpoint: `!pip show langchain` & `!pip show openai`

## [03:30–06:00] Defining Agents
- Walkthrough code: Orchestrator Agent class and HR/Tech Agents stub.
- Display code definitions.

## [06:00–09:00] Implementing Query Routing
- Demonstrate OpenAI function calling logic.
- Update workflow diagram accordingly.

## [09:00–12:00] Handling Conversational Handoffs
- Show passing context/state objects between agents.
- Execute multi-turn query example.

## [12:00–15:00] End-to-End Demo
- Run workflow with sample HR and Tech queries.
- Checkpoint: Correct domain routing & responses.

## [15:00–17:00] Error Handling & Best Practices
- Show ambiguous query handling, logging.
- Discuss modularity & maintainability.

## [17:00–18:00] Wrap-Up & Next Steps
- Recap built demo and learnings.
- Encourage extension and preview tracing lesson.

## Checkpoints
- “If your workflow routes HR queries correctly, you’re on track.”
- “If context is preserved across turns, handoff is correct.”
