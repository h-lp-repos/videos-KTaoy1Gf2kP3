# Lesson L3: Multi-Agent Systems Video Materials

This repository collects the production-ready artifacts for the three high-priority videos in Lesson L3: Multi-Agent Systems (Module 3: Agents, Orchestration and Tracing). Each folder under `videos/` contains everything a producer needs to explain, demo, and verify the concepts without requesting additional materials.

## Videos
- [video-01-introduction-motivation](videos/video-01-introduction-motivation) — "Why Multi-Agent Systems?" (Section 3.1, 6 min)
- [video-02-technical-deep-dive](videos/video-02-technical-deep-dive) — Architectures & Collaboration Patterns (Section 3.2, 13 min)
- [video-03-hands-on-integrative-demo](videos/video-03-hands-on-integrative-demo) — Multi-Agent Query Router with LangChain & OpenAI Function Calling (Section 3.3, 18 min)

## Local validation
Execute the standalone verification helper before pushing updates:

```
bash .github/scripts/validate-videos.sh
```

It checks each `video-XX-*` directory for the README, video.json, guion.md, code/, run.sh, verify.sh, and recording.md files required by the CI.

## Continuous integration
`.github/workflows/validate-videos.yml` runs on every change touching the `videos/` tree and enforces the same guardrails as the local script so missing artifacts fail the pipeline early.

## Contribution guidelines
See [CONTRIBUTING.md](CONTRIBUTING.md) for the naming conventions, branch and PR checklist, and how to add new videos or update existing ones.

## Artifact policies
Avoid packing large binaries; use scripts under `videos/video-XX-*/data/` to download sizable datasets, and describe their source and checksum in the respective README.
