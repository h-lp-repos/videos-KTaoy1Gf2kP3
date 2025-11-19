# Why Multi-Agent Systems? Motivation, Real-World Scenarios & Learning Goals
Ubicación en la lecture
Section 3.1 Introduction, immediately after the opening keynote, so the audience understands the purpose before diving deeper.

Objetivo
Present the motivation for moving beyond single-agent systems, highlight the HR/Tech routing scenario, and preview the collaboration patterns the lesson will cover.

Duración estimada
6 minutos

Prioridad
Alta

Prerequisitos
- Completion of the prior modules covering LLM fundamentals, RAG, and LangChain basics.
- Comfortable with Python scripting and REST API concepts.

Materiales y ambiente
- Slide deck or digital whiteboard with diagrams contrasting single-agent vs multi-agent flows.
- Scripted dialogue referencing an AI assistant that routes HR and Technical queries in one funnel.
- Studio configured at 1920×1080 resolution with fonts no smaller than 16pt and high contrast colors.

Setup rápido
1. Confirm the system is running Python 3.9+ and has the ability to print to the console.
2. Run `bash run.sh` to narrate the motivation scenario.
3. Optional: `bash verify.sh` to double-check the script output and checkpoints.

Pasos para ejecutar la demo
1. Execute `bash run.sh` while keeping the slide deck visible; the script prints the bottlenecks and the scenario summary.
2. After reading the narrative, run `bash verify.sh` to confirm the checkpoints are satisfied and be ready to mention them in the narration cue.

Checkpoints de verificación
- CHECKPOINT 1: Scenario narrative articulates single-agent limitations and multi-agent advantages.
- CHECKPOINT 2: Learning objectives are listed for the lesson and scoped clearly.

Errores comunes y soluciones rápidas
- Confusing multi-agent systems with multi-modal pipelines. Reframe it as multiple cooperating agents with defined roles, not multiple data types.
- Assuming every query can be answered by one model; emphasize specialization and distributed reasoning instead.

Archivos incluidos
- `README.md`, `video.json`, `guion.md`, `recording.md` (guidance for the recording engineer).
- `code/` with `motivation_overview.py` plus its README.
- `env.example`, `run.sh`, `verify.sh`, `data/README.md`, `assets/diagram-overview.md`.

Instrucciones de grabación
Refer to `recording.md` for camera framing, resolution, and font-size notes. Show the diagram during the walkthrough and highlight the drone of the motivating scenario.

Referencias
- "Multi-Agent Systems Explained" – DeepLearning.AI – https://www.youtube.com/watch?v=9t9E2Q1r5iA (2023-10) for analogies on specialization.
- "From Single Agent to Multi-Agent AI" – AssemblyAI – https://www.youtube.com/watch?v=F4J7U6gG6vA (2024-03) for industry rationale and orchestration context.
