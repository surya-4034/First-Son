"use client";

import { useState } from "react";

import Header from "../components/layout/Header";
import Sidebar from "../components/layout/Sidebar";
import ChatWindow from "../components/chat/ChatWindow";
import ChatInput from "../components/chat/ChatInput";

import api from "../lib/api";
import { Message } from "../types/chat";

export default function Home() {
  const [message, setMessage] = useState("");

  const [messages, setMessages] = useState<Message[]>([]);

  const [loading, setLoading] = useState(false);

  const [chats] = useState<string[]>([
    "New Chat",
  ]);

  const [activeChat, setActiveChat] = useState(0);

  async function sendMessage() {
    if (!message.trim() || loading) return;

    const userMessage: Message = {
      id: Date.now().toString(),
      sender: "user",
      text: message,
      timestamp: new Date(),
    };

    setMessages((prev) => [...prev, userMessage]);

    const currentMessage = message;

    setMessage("");

    setLoading(true);

    try {
      const res = await api.post("/chat", {
        message: currentMessage,
      });

      const aiMessage: Message = {
        id: (Date.now() + 1).toString(),
        sender: "assistant",
        text: res.data.response,
        timestamp: new Date(),
      };

      setMessages((prev) => [...prev, aiMessage]);
    } catch (error) {
      console.error(error);

      const errorMessage: Message = {
        id: (Date.now() + 1).toString(),
        sender: "assistant",
        text: "❌ Unable to connect to First-Son.",
        timestamp: new Date(),
      };

      setMessages((prev) => [...prev, errorMessage]);
    } finally {
      setLoading(false);
    }
  }

  function newChat() {
    setMessages([]);
    setMessage("");
  }

  return (
    <main className="flex h-screen bg-black text-white">

      <Sidebar
        chats={chats}
        activeChat={activeChat}
        setActiveChat={setActiveChat}
      />

      <div className="flex flex-1 flex-col">

        <Header
          onNewChat={newChat}
        />

        <ChatWindow
          messages={messages}
          loading={loading}
        />

        <ChatInput
          message={message}
          setMessage={setMessage}
          sendMessage={sendMessage}
          loading={loading}
        />

      </div>

    </main>
  );
}