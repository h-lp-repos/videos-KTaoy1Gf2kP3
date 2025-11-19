# Hands-On: Building a Multi-Agent Query Router with LangChain & OpenAI Function Calling
Ubicación en la lecture
Section 3.3 Integrative Use Case, immediately after the technical deep-dive, showing a real implementation of an orchestrated multi-agent workflow.

Objetivo
Walk through the full implementation of the multi-agent query router using LangChain, covering role assignment, OpenAI function calling, and conversational handoffs.

Duración estimada
18 minutos

Prioridad
Alta

Prerequisitos
- Python 3.9+ installed with pip.
- Access to the OpenAI API (with `OPENAI_API_KEY` and optional `OPENAI_MODEL`).
- Familiarity with LangChain and the lessons that preceded this demo.

Materiales y ambiente
- VS Code or terminal that can show `code/query_router.py` and the sample outputs simultaneously.
- High-contrast colors, 1920×1080 resolution, large fonts (≥16pt) configured for both code and terminal windows.

Setup rápido
1. Populate `env.example` with your OpenAI credentials and source the file (e.g., `set -a && source env.example && set +a`).
2. Execute `bash run.sh` to install dependencies and run the demo with the default sample queries.
3. Use `bash verify.sh` to confirm the checkpoints without requiring a live OpenAI key (the verification script uses keyword routing and still prints the expected agent assignments and history).

Pasos para ejecutar la demo
1. Run `bash run.sh` while explaining the role of the orchestrator, HR Agent, and Tech Agent; highlight the sample queries printed from `data/sample_queries.txt`.
2. After the demo output, point to the conversation history snapshot to show how context is preserved across turns.
3. Run `bash verify.sh` live to show the checkpoint confirmations on-screen, and point out how fallback routing still hits both HR and Tech agents.

Checkpoints de verificación
- CHECKPOINT 1: Workflow routes HR queries to the HR Agent and Tech queries to the Tech Agent.
- CHECKPOINT 2: Conversation context remains intact across the entire run.

Errores comunes y soluciones rápidas
- API authentication failure: ensure `OPENAI_API_KEY` is exported before running `bash run.sh` or the demo will stop with a reminder.
- Classification gaps: use the fallback keyword lists in `query_router.py` and update `HR_KEYWORDS`/`TECH_KEYWORDS` to cover missing terms.
- Context loss: preserve the `history` list and print it after each query to track the handoff state.

Archivos incluidos
- `README.md`, `video.json`, `guion.md`, `recording.md`, `env.example`.
- `code/query_router.py`, `code/README.md`, `code/requirements.txt`, `data/sample_queries.txt`, `data/README.md`.
- `docker/` directory with Dockerfile and docker-compose, plus `assets/pipeline-overview.md`, `run.sh`, and `verify.sh`.

Instrucciones de grabación
Display the workflow diagram while highlighting each agent blade, then pan to the terminal while running `bash run.sh`. After the context snapshot prints, zoom in on the section that stores the conversation history and mention that it stays intact.

Referencias
- "LangChain Multi-Agent Routing Tutorial" – LangChain Official – https://www.youtube.com/watch?v=7vQ2lJv1c3g (2024-04).
- "OpenAI Function Calling in Multi-Agent Workflows" – AI with Python – https://www.youtube.com/watch?v=1kVv0KJZs4I (2023-11).
