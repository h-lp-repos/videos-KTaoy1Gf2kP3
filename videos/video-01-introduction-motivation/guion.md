# Guion para video 1

## [00:00–00:30] Opening (narrador + slide)
1. Welcome message mentioning that L3 unfolds from the previous lessons on LLMs and RAG.
2. Cue: show the first slide and zoom in on the timeline that lands at Section 3.1.
3. Mention the goal: prepare for the why of multi-agent systems.

## [00:30–02:00] Motivation
1. Script: "The single-agent assistant that handles HR, finance, and technical questions becomes a bottleneck. As scope grows, predictions degrade and latency spikes."
2. Show side-by-side diagram (single pipeline vs many agents) while narrating.
3. Command cue: run `python code/motivation_overview.py` to print the HR+Tech scenario and the repeated request to route queries.
4. Signal: close-up on console output and highlighter on the HR vs Tech bullet.

## [02:00–03:30] What Are Multi-Agent Systems?
1. Define multi-agent architecture: multiple cooperating agents with their own roles.
2. Mention distributed intelligence, modularity, and scalability with brief slide overlays.
3. Use the script output to highlight how responsibilities split and how the orchestrator hands off context.

## [03:30–05:00] Why Now? Industry Trends
1. Reference automation, orchestration in customer support, and large team needs.
2. Show the industry reference cards (DeepLearning.AI and AssemblyAI) and mention the two sample lessons from the references section.
3. Cue for narration: "Specialization unlocks higher quality service and faster responses."

## [05:00–06:00] Learning Objectives
1. Call out the three objectives: architectural distinction, collaboration patterns, and the hands-on implementation with LangChain.
2. End with a slide that lists the upcoming videos in the lesson plan as a teaser.
3. Mention the heading of the next video so the viewer knows the transition point.

### Comandos que se ejecutan
- `python code/motivation_overview.py` (early in the video, right after motivation) to print the HR vs Tech scenario and the learning objectives.
- `bash verify.sh` (optional, for the engineer to show the checkpoint lines) while the narrator explains the verification process.
