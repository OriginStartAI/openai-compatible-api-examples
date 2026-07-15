# OriginStartAI OpenAI-Compatible API Examples

Drop-in style examples for calling OriginStartAI with familiar OpenAI-compatible request patterns.

Use this repo when you want to test chat completions, streaming, JSON output, and simple migration patterns from existing OpenAI SDK code.

## Quick Start

1. Create an account at https://originstartai.com?utm_source=github&utm_medium=repo&utm_campaign=openai_compatible_examples
2. Get your API key from the console.
3. Copy `.env.example` to `.env`.
4. Set `ORIGINSTARTAI_API_KEY`, `ORIGINSTARTAI_BASE_URL`, and `ORIGINSTARTAI_MODEL`.
5. Run a curl, Python, or Node.js example.

New user bonus: recharge `$5` and get `$5` extra API credits.

## Examples

- `examples/curl/chat_completion.sh`
- `examples/python/chat_completion.py`
- `examples/python/streaming.py`
- `examples/python/json_output.py`
- `examples/node/chat_completion.mjs`
- `examples/node/streaming.mjs`
- `examples/node/json_output.mjs`

## OpenAI-Compatible Pattern

The migration idea is simple:

```text
baseURL/base_url -> OriginStartAI API base URL
apiKey/api_key   -> OriginStartAI API key
model            -> enabled model on your OriginStartAI account
```

## SDK Migration Notes

- Keep your app-level prompt logic.
- Replace the base URL with your OriginStartAI endpoint.
- Replace the API key with `ORIGINSTARTAI_API_KEY`.
- Confirm the model name in the OriginStartAI console.
- Test one low-risk prompt before moving production traffic.

## Docs

- [Migration guide](docs/migration-guide.md)
- [First call checklist](docs/first-call-checklist.md)
- [Error reference](docs/error-reference.md)
- [Tracking first call to recharge](docs/conversion-tracking.md)

## Links

- Website: https://originstartai.com?utm_source=github&utm_medium=repo&utm_campaign=openai_compatible_examples
- Support: support@originstartai.com
