# Multi-agent query router

`query_router.py` demonstrates how to:

1. Define an orchestrator that routes HR and Technical queries via OpenAI function calling.
2. Use keyword fallback routing when an API key is missing.
3. Preserve conversational context by storing responses in a history log.

## Ejecutar

```bash
python query_router.py --demo
```

The demo runs the sample prompts listed in `data/sample_queries.txt` and prints which agent handled each query. Interactive mode (`python query_router.py`) lets you type free-form prompts until you enter `exit`.
