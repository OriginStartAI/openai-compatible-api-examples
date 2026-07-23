import json
import os
import time
import urllib.error
import urllib.request


api_key = os.environ["ORIGINSTARTAI_API_KEY"]
base_url = os.environ.get("ORIGINSTARTAI_BASE_URL", "https://YOUR_PUBLIC_API_BASE_URL/v1")
model = os.environ.get("ORIGINSTARTAI_MODEL", "YOUR_ENABLED_MODEL")

timeout_seconds = float(os.environ.get("ORIGINSTARTAI_TIMEOUT_SECONDS", "30"))
max_attempts = int(os.environ.get("ORIGINSTARTAI_MAX_ATTEMPTS", "3"))

payload = {
    "model": model,
    "messages": [
        {"role": "user", "content": "Give me a one sentence API integration checklist."}
    ],
}


def should_retry(error: Exception) -> bool:
    if isinstance(error, urllib.error.HTTPError):
        return error.code in {408, 409, 429, 500, 502, 503, 504}
    return isinstance(error, (TimeoutError, urllib.error.URLError))


last_error: Exception | None = None
for attempt in range(1, max_attempts + 1):
    request = urllib.request.Request(
        f"{base_url.rstrip('/')}/chat/completions",
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        method="POST",
    )

    try:
        with urllib.request.urlopen(request, timeout=timeout_seconds) as response:
            print(response.read().decode("utf-8"))
            raise SystemExit(0)
    except Exception as error:  # Keep example dependency-free and easy to copy.
        last_error = error
        if attempt == max_attempts or not should_retry(error):
            break
        sleep_seconds = min(2 ** (attempt - 1), 8)
        print(f"attempt {attempt} failed; retrying in {sleep_seconds}s")
        time.sleep(sleep_seconds)

raise SystemExit(f"request failed after {max_attempts} attempt(s): {last_error}")
