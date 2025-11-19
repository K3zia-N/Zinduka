// chatbot/genkit_app/flows.js
// Minimal Genkit-style flow: this is a placeholder - install and adapt from Genkit docs
import fetch from "node-fetch";

async function sendMessage(userId, text) {
  const res = await fetch("http://localhost:8000/chat", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ user_id: userId, text })
  });
  const j = await res.json();
  console.log("Agent reply:", j.reply);
  return j;
}

(async () => {
  // Demo conversation
  await sendMessage("kezia", "Hello, I need to generate a legal report about sexual assault.");
  await sendMessage("kezia", "I need resources nearby.");
})();
