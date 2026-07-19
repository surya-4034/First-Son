"use client";

import { useEffect, useState } from "react";

import Header from "../components/layout/Header";
import Sidebar from "../components/layout/Sidebar";
import ChatWindow from "../components/chat/ChatWindow";
import ChatInput from "../components/chat/ChatInput";

import { useChat } from "../hooks/useChat";
import { useConversation } from "../hooks/useConversation";

export default function Home() {
  const [message, setMessage] = useState("");

  const {
    messages,
    setMessages,
    loading,
    sendMessage,
  } = useChat();

  const {
    conversations,
    activeConversationId,
    createNewConversation,
    loadConversation,
    refreshSidebar,
  } = useConversation();

 useEffect(() => {
  if (conversations.length === 0) return;

  loadConversation(conversations[0].id)
    .then(setMessages)
    .catch(console.error);

// eslint-disable-next-line react-hooks/exhaustive-deps
}, []);

  async function handleNewChat() {
  const id = await createNewConversation();

  setMessage("");

  const msgs = await loadConversation(id);

  setMessages(msgs);
}
  async function handleOpenConversation(index: number) {
    if (!conversations[index]) return;

    const msgs = await loadConversation(
      conversations[index].id
    );

    setMessages(msgs);
  }

  async function handleSend() {
    if (!activeConversationId) return;

    const text = message.trim();

    if (!text) return;

    setMessage("");

  const activeConversation =
  conversations.find(
    (c) => c.id === activeConversationId
  );

await sendMessage(
  activeConversationId,
  text,
  activeConversation?.title ?? "New Chat",
  refreshSidebar
);
  }

  return (
    <main className="flex h-screen bg-black text-white">
      <Sidebar
        chats={conversations.map((c) => c.title)}
        activeChat={conversations.findIndex(
          (c) => c.id === activeConversationId
        )}
        setActiveChat={handleOpenConversation}
      />

      <div className="flex flex-1 flex-col">
        <Header onNewChat={handleNewChat} />

        <ChatWindow
          messages={messages}
          loading={loading}
        />

        <ChatInput
          message={message}
          setMessage={setMessage}
          sendMessage={handleSend}
          loading={loading}
        />
      </div>
    </main>
  );
}