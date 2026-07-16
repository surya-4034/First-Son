"use client";

import { useState } from "react";
import Header from "../components/Header";
import ChatWindow from "../components/ChatWindow";
import ChatInput from "../components/ChatInput";
import api from "../lib/api";
import { Message } from "../types/chat";

export default function Home() {
  const [message, setMessage] = useState("");
  const [messages, setMessages] = useState<Message[]>([]);
  const [loading, setLoading] = useState(false);

  async function sendMessage() {
    if (!message.trim()) return;

    // User message
    const userMessage: Message = {
      id: Date.now(),
      sender: "user",
      text: message,
    };

    setMessages((prev) => [...prev, userMessage]);

    const currentMessage = message;
    setMessage("");

    // Show typing indicator
    setLoading(true);

    try {
      const res = await api.post("/chat", {
        message: currentMessage,
      });

      // AI response
      const aiMessage: Message = {
        id: Date.now() + 1,
        sender: "assistant",
        text: res.data.response,
      };

      setMessages((prev) => [...prev, aiMessage]);
    } catch (error) {
      console.error(error);

      const errorMessage: Message = {
        id: Date.now() + 1,
        sender: "assistant",
        text: "❌ Unable to connect to First-Son.",
      };

      setMessages((prev) => [...prev, errorMessage]);
    } finally {
      // Hide typing indicator
      setLoading(false);
    }
  }

  return (
    <main className="min-h-screen bg-black text-white flex flex-col">
      <Header />

      <ChatWindow
        messages={messages}
        loading={loading}
      />

      <ChatInput
        message={message}
        setMessage={setMessage}
        sendMessage={sendMessage}
      />
    </main>
  );
}