"use client";

import { useState } from "react";

import Header from "../components/layout/Header";
import Sidebar from "../components/layout/Sidebar";
import ChatWindow from "../components/chat/ChatWindow";
import ChatInput from "../components/chat/ChatInput";

import { Message } from "../types/chat";

export default function Home() {
  const [message, setMessage] = useState("");

  const [messages, setMessages] = useState<Message[]>([]);

  const [loading, setLoading] = useState(false);

  const [chats] = useState<string[]>(["New Chat"]);

  const [activeChat, setActiveChat] = useState(0);

  async function sendMessage() {
    async function sendMessage() {
  console.log("sendMessage called");

  if (!message.trim() || loading) return;

  
}
    if (!message.trim() || loading) return;

    const currentMessage = message;

    const userMessage: Message = {
      id: Date.now().toString(),
      sender: "user",
      text: currentMessage,
      timestamp: new Date(),
    };

    setMessages((prev) => [...prev, userMessage]);

    setMessage("");
    setLoading(true);

    const assistantId = (Date.now() + 1).toString();

    setMessages((prev) => [
      ...prev,
      {
        id: assistantId,
        sender: "assistant",
        text: "",
        timestamp: new Date(),
      },
    ]);

    try {
      const response = await fetch("http://127.0.0.1:8000/chat/stream", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
       body: JSON.stringify({
  messages: [
    ...messages.map((msg) => ({
      role: msg.sender === "user" ? "user" : "assistant",
      content: msg.text,
    })),
    {
      role: "user",
      content: currentMessage,
    },
  ],
}),
      });

      if (!response.ok) {
        throw new Error("Request failed");
      }

      if (!response.body) {
        throw new Error("Streaming not supported.");
      }

      const reader = response.body.getReader();
      const decoder = new TextDecoder();

      let fullText = "";

      while (true) {
        const { done, value } = await reader.read();

        if (done) break;

        fullText += decoder.decode(value, { stream: true });

        setMessages((prev) =>
          prev.map((msg) =>
            msg.id === assistantId
              ? {
                  ...msg,
                  text: fullText,
                }
              : msg
          )
        );
      }
    } catch (error) {
      console.error(error);

      setMessages((prev) =>
        prev.map((msg) =>
          msg.id === assistantId
            ? {
                ...msg,
                text: "❌ Unable to connect to First-Son.",
              }
            : msg
        )
      );
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
        <Header onNewChat={newChat} />

        <ChatWindow messages={messages} loading={loading} />

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