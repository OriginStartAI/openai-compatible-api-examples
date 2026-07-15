#!/usr/bin/env bash
set -euo pipefail

: "${ORIGINSTARTAI_API_KEY:?Set ORIGINSTARTAI_API_KEY}"
: "${ORIGINSTARTAI_BASE_URL:=https://YOUR_PUBLIC_API_BASE_URL/v1}"
: "${ORIGINSTARTAI_MODEL:=YOUR_ENABLED_MODEL}"

curl "$ORIGINSTARTAI_BASE_URL/chat/completions" \
  -H "Authorization: Bearer $ORIGINSTARTAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "'"$ORIGINSTARTAI_MODEL"'",
    "messages": [
      {"role": "user", "content": "Give me a one sentence API integration checklist."}
    ]
  }'
