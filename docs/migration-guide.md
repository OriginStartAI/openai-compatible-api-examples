# Migration Guide

OriginStartAI uses OpenAI-compatible request patterns so teams can move from a local prototype to a production API workflow with minimal code changes.

## What Usually Changes

```text
base_url -> ORIGINSTARTAI_BASE_URL
api_key  -> ORIGINSTARTAI_API_KEY
model    -> ORIGINSTARTAI_MODEL
```

## What Usually Stays

- Your prompt structure.
- Your system and user message format.
- Your streaming parser.
- Your JSON parsing logic.
- Your retry and logging strategy.

## Recommended Migration Flow

1. Run `examples/curl/chat_completion.sh`.
2. Run `examples/python/chat_completion.py`.
3. Run `examples/python/json_output.py`.
4. Move one production-like prompt into the examples.
5. Add usage logging before increasing traffic.

## Production Checklist

- Store keys in environment variables or a secret manager.
- Log request IDs and error types.
- Add retries for transient network failures.
- Add budget alerts before large batch jobs.
- Keep a fallback path for business-critical workflows.
