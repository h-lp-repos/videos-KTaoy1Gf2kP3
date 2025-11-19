# Architectures & Collaboration Patterns: From Single-Agent to Multi-Agent Workflows
Ubicación en la lecture
Section 3.2 Technical Deep-Dive, just after the motivational overview and before the hands-on demo.

Objetivo
Explain the architectural differences between single-agent and multi-agent systems, and demonstrate role assignment, task delegation, and conversational handoffs with sample code.

Duración estimada
13 minutos

Prioridad
Alta

Prerequisitos
- Comfortable with LangChain fundamentals and Python.
- Familiarity with single-agent LLM flows from previous lessons.

Materiales y ambiente
- Slide deck or digital whiteboard showing diagrams of the orchestrator and agent teams.
- VS Code or Jupyter ready to display the `collaboration_patterns.py` script.
- Terminal theme with large, 16pt+ font and high contrast to display the code output.

Setup rápido
1. Ensure Python 3.9+ is active and `python -m pip --version` works.
2. Run `bash run.sh` to emit the architecture narrative and pattern definitions.
3. Optionally, run `bash verify.sh` so the recording assistant can highlight the checkpoints on camera.

Pasos para ejecutar la demo
1. Start the run script `bash run.sh` while alternately showing the orchestrator diagram and the console output that enumerates the collaboration patterns.
2. After the script runs, reference the `data/collaboration_patterns.json` file to explain how the orchestrator dynamically assigns roles and passes context.
3. End the segment by highlighting the conversational handoff example from the script and pointing out how context is preserved.

Checkpoints de verificación
- CHECKPOINT 1: The orchestrator flow is described clearly and matches the output from `collaboration_patterns.py`.
- CHECKPOINT 2: The code highlights how conversational context is preserved while handing off between agents.

Errores comunes y soluciones rápidas
- Assuming orchestration is just a function call; emphasize message routing, state capture, and agent specialization instead.
- Losing conversational context; show how the script collects input history and keeps agent labels together.

Archivos incluidos
- `README.md`, `video.json`, `guion.md`, `recording.md`.
- `code/collaboration_patterns.py` and its README.
- `data/collaboration_patterns.json`, `assets/architecture-notes.md`, `env.example`, `run.sh`, `verify.sh`.

Instrucciones de grabación
Follow `recording.md` for window stacking (diagram + code + terminal). Pause briefly after each collaboration pattern so the viewer can absorb the flow.

Referencias
- "LangChain Agents: Multi-Agent Workflows" – LangChain Official – https://www.youtube.com/watch?v=3YfNFR6gh2w (2024-02).
- "Building AI Agent Teams with Python" – Data Independent – https://www.youtube.com/watch?v=V7r2F9vQk1c (2023-12).
