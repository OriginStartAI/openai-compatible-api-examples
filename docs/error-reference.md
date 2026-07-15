# Error Reference

## `401 Unauthorized`

The API key is missing, invalid, copied with extra spaces, or belongs to another account.

## `model not found`

The model is not enabled for the account or the name was copied incorrectly.

## `insufficient credits`

Recharge in the OriginStartAI console. New users can recharge `$5` and get `$5` extra API credits.

## Timeout

Try a shorter prompt, reduce context size, or retry the request.

## Invalid JSON

For structured output tasks:

- Add a system message such as `Return only valid JSON.`
- Validate and retry once.
- Keep schema instructions short and explicit.
