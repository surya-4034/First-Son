"use client";

import { useState } from "react";
import api from "../lib/api";

export default function Home() {
  const [message, setMessage] = useState("");
  const [response, setResponse] = useState("");

  async function sendMessage() {
    if (!message.trim()) return;

    try {
      const res = await api.post("/chat", {
        message,
      });

      setResponse(res.data.response);
    } catch (error) {
      console.error(error);
      setResponse("❌ Unable to connect to First-Son.");
    }
  }

  return (
    <main className="min-h-screen bg-black text-white flex flex-col p-8">
      <h1 className="text-4xl font-bold mb-8">🤖 First-Son</h1>

      <textarea
        className="bg-zinc-900 p-4 rounded-lg border border-zinc-700"
        rows={4}
        placeholder="Ask First-Son anything..."
        value={message}
        onChange={(e) => setMessage(e.target.value)}
      />

      <button
        onClick={sendMessage}
        className="mt-4 bg-blue-600 hover:bg-blue-700 rounded-lg px-6 py-3"
      >
        Send
      </button>

      <div className="mt-8 bg-zinc-900 rounded-lg p-4 min-h-40">
        <h2 className="font-bold mb-2">First-Son says:</h2>
        <p>{response}</p>
      </div>
    </main>
  );
}