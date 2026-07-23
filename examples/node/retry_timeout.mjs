const apiKey = process.env.ORIGINSTARTAI_API_KEY;
const baseUrl = process.env.ORIGINSTARTAI_BASE_URL || "https://YOUR_PUBLIC_API_BASE_URL/v1";
const model = process.env.ORIGINSTARTAI_MODEL || "YOUR_ENABLED_MODEL";

const timeoutMs = Number(process.env.ORIGINSTARTAI_TIMEOUT_MS || "30000");
const maxAttempts = Number(process.env.ORIGINSTARTAI_MAX_ATTEMPTS || "3");

if (!apiKey) {
  throw new Error("Set ORIGINSTARTAI_API_KEY first.");
}

function shouldRetry(status) {
  return [408, 409, 429, 500, 502, 503, 504].includes(status);
}

let lastError;
for (let attempt = 1; attempt <= maxAttempts; attempt += 1) {
  try {
    const response = await fetch(`${baseUrl.replace(/\/$/, "")}/chat/completions`, {
      method: "POST",
      signal: AbortSignal.timeout(timeoutMs),
      headers: {
        Authorization: `Bearer ${apiKey}`,
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        model,
        messages: [
          { role: "user", content: "Give me a one sentence API integration checklist." },
        ],
      }),
    });

    const body = await response.text();
    if (!response.ok) {
      const error = new Error(`HTTP ${response.status}: ${body}`);
      error.status = response.status;
      throw error;
    }

    console.log(body);
    process.exit(0);
  } catch (error) {
    lastError = error;
    const retryable = error.name === "TimeoutError" || shouldRetry(error.status);
    if (attempt === maxAttempts || !retryable) {
      break;
    }
    const sleepMs = Math.min(2 ** (attempt - 1) * 1000, 8000);
    console.error(`attempt ${attempt} failed; retrying in ${sleepMs}ms`);
    await new Promise((resolve) => setTimeout(resolve, sleepMs));
  }
}

throw lastError;
