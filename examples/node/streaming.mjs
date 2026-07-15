const apiKey = process.env.ORIGINSTARTAI_API_KEY;
const baseUrl = process.env.ORIGINSTARTAI_BASE_URL || "https://YOUR_PUBLIC_API_BASE_URL/v1";
const model = process.env.ORIGINSTARTAI_MODEL || "YOUR_ENABLED_MODEL";

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
    stream: true,
    messages: [
      { role: "user", content: "Stream a short welcome message." },
    ],
  }),
});

for await (const chunk of response.body) {
  process.stdout.write(new TextDecoder().decode(chunk));
}
