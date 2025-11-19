# Dockerized multi-agent demo

1. Set your OpenAI variables:
   ```bash
   export OPENAI_API_KEY=sk-your-key
   export OPENAI_MODEL=gpt-4o-mini
   ```
2. From the `docker/` directory, build and run:
   ```bash
   docker compose up --build
   ```
3. The container runs `bash run.sh`, which installs dependencies and executes the demo.
