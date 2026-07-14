const apiKey = process.env.ORIGINSTARTAI_API_KEY;
const baseUrl = process.env.ORIGINSTARTAI_BASE_URL || "https://YOUR_7016_API_BASE_URL/v1";
const model = process.env.ORIGINSTARTAI_MODEL || "YOUR_DEFAULT_MODEL";

if (!apiKey) {
  throw new Error("Set ORIGINSTARTAI_API_KEY first.");
}

const response = await fetch(`${baseUrl.replace(/\/$/, "")}/chat/completions`, {
  method: "POST",
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

console.log(await response.text());

