# Guion para video 2

## [00:00–01:00] Recap del single-agent
1. Show the single-agent diagram and explain centralized reasoning and its limitations (template code, single prompt). Context: this is the starting point for the new architecture.
2. Mention the upcoming shift to multi-agent architecture and highlight that the next portion is covered by the script.

## [01:00–03:00] Multi-agent architecture
1. Reveal the orchestrator, HR Agent, and Tech Agent diagram.
2. Describe how the orchestrator routes the user query, what data it inspects, and why modularity matters for scaling.
3. Command cue: run `python code/collaboration_patterns.py` to print the orchestrator steps and the collaboration patterns it supports.

## [03:00–05:30] Collaboration patterns overview
1. Define role assignment, task delegation, and conversational handoffs with narrated examples.
2. Show the JSON entries in `data/collaboration_patterns.json` while explaining each pattern.
3. Signal: zoom into the context stack on the slide.

## [05:30–09:00] Code walkthrough
1. Walk through the script, pointing out how each agent class handles its own responsibilities and how the orchestrator calls them.
2. Highlight the `conversation_history` structure that keeps context across the lifecycle.
3. Mention the checkpoint line about the orchestrator flow and context preservation.

## [09:00–12:00] Live reinforcement
1. Re-execute the script output and narrate how a sample query moves from the orchestrator to the agents, and how the context is handed back.
2. Emphasize console output with context markers (synchronous or asynchronous). Use highlights or overlays to show the input and output at each stage.

## [12:00–13:00] Wrap-up
1. Summarize the advantages of multi-agent collaboration patterns and preview the hands-on router in Video 3.
2. Confirm that viewers are comfortable sketching the flow from the orchestrator to each specialized agent.

### Comandos
- `python code/collaboration_patterns.py` (run during the architecture and code walkthrough to show the orchestrator flow and context preservation.)
- `bash verify.sh` (optional, use the checkpoint lines to keep the narrator in sync with the script output.)
