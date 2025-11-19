# Contributing to Lesson L3 Video Materials

Thank you for helping keep the Lesson L3: Multi-Agent Systems repository accurate and ready for production. Follow these conventions when you add or update a video asset:

1. **Branches** use the `video/` prefix (e.g. `video/video-03-ready`).
2. **Folders** for each video must live under `videos/video-XX-slug` where `XX` is the two-digit index from the Lesson Plan. Include all required artifacts (README, video.json, guion.md, code/, run.sh, verify.sh, recording.md, env.example, data/ if needed). Anyone grabbing the folder should have a runnable story from start to finish.
3. **Metadata**: Update `video.json.last_verified` to the current date (`YYYY-MM-DD`) whenever you touch the code, script, or guion. Keep `priority`, `index`, and `language` accurate per video.
4. **Scripts**: `run.sh` must prepare the environment and execute the demo; `verify.sh` must finish with exit code 0 and print checkpoints that match those listed in the video README.
5. **Tests**: Execute `.github/scripts/validate-videos.sh` locally before pushing so the CI workflow passes without iteration.
6. **Assets**: Avoid committing large binaries; host them externally if needed and reference download helpers under `data/` with checksums.
7. **Review**: After uploading, create a PR describing the checklist from `CHECKLIST.md`, assign a pedagogical reviewer, and wait for sign-off before merging.

Feel free to open an issue if you hit edge cases, missing instructions, or need help verifying the workflow.
