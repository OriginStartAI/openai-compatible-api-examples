# OriginStartAI OpenAI-Compatible API Examples

Copyable curl, Python, and Node.js examples for testing OriginStartAI with familiar OpenAI-compatible API patterns.

Use this repo when you want to confirm one chat completion, stream tokens, request JSON output, or migrate a small existing OpenAI-style call.

## 30-Second First Call

1. Create an account: https://originstartai.com?utm_source=github&utm_medium=repo&utm_campaign=openai_compatible_examples
2. Create an API key in the OriginStartAI console.
3. Copy `.env.example` to `.env`.
4. Set `ORIGINSTARTAI_API_KEY`, `ORIGINSTARTAI_BASE_URL`, and `ORIGINSTARTAI_MODEL`.
5. Run the smallest example:

```bash
bash examples/curl/chat_completion.sh
```

```bash
python examples/python/chat_completion.py
```

```bash
node examples/node/chat_completion.mjs
```

New user bonus: after your first call works, recharge `$5` and get `$5` extra API credits to test a real workflow.

## What Is Included

| Goal | curl | Python | Node.js |
| --- | --- | --- | --- |
| Chat completion | `examples/curl/chat_completion.sh` | `examples/python/chat_completion.py` | `examples/node/chat_completion.mjs` |
| Streaming | - | `examples/python/streaming.py` | `examples/node/streaming.mjs` |
| JSON output | - | `examples/python/json_output.py` | `examples/node/json_output.mjs` |

## Migration Pattern

Most OpenAI-compatible migrations start with three changes:

```text
baseURL/base_url -> OriginStartAI API base URL
apiKey/api_key   -> OriginStartAI API key
model            -> enabled model on your OriginStartAI account
```

Keep your prompt, response parsing, and application logic the same for the first test. Once the first call works, add retries, timeout handling, and logging before moving production traffic.

## If The First Call Fails

| Symptom | Check |
| --- | --- |
| `401 Unauthorized` | Confirm the API key in `.env` is current and has no extra spaces. |
| `insufficient credits` | Recharge in the OriginStartAI console, then retry the same example. |
| `model not found` | Copy the enabled model name from the console into `ORIGINSTARTAI_MODEL`. |
| Slow response | Test streaming, shorten the prompt, and set explicit request timeouts. |

## Docs

- [Migration guide](docs/migration-guide.md)
- [First call checklist](docs/first-call-checklist.md)
- [Error reference](docs/error-reference.md)
- [Tracking first call to recharge](docs/conversion-tracking.md)

## Search Topics

- OpenAI-compatible API examples.
- Chat completions API example.
- Streaming chat completions.
- JSON structured output LLM.
- Python AI API example.
- Node.js AI API example.

## Links

- Website: https://originstartai.com?utm_source=github&utm_medium=repo&utm_campaign=openai_compatible_examples
- Support: support@originstartai.com
