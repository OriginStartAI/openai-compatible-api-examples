import json
import os
import urllib.request


api_key = os.environ["ORIGINSTARTAI_API_KEY"]
base_url = os.environ.get("ORIGINSTARTAI_BASE_URL", "https://YOUR_PUBLIC_API_BASE_URL/v1")
model = os.environ.get("ORIGINSTARTAI_MODEL", "YOUR_ENABLED_MODEL")

payload = {
    "model": model,
    "messages": [
        {"role": "user", "content": "Give me a one sentence API integration checklist."}
    ],
}

request = urllib.request.Request(
    f"{base_url.rstrip('/')}/chat/completions",
    data=json.dumps(payload).encode("utf-8"),
    headers={
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    },
    method="POST",
)

with urllib.request.urlopen(request, timeout=60) as response:
    print(response.read().decode("utf-8"))
