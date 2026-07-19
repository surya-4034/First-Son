import { useState } from "react";
import { Message } from "../types/chat";
import { streamChat } from "../lib/chat";
import { updateConversation } from "../lib/conversations";
export function useChat() {
  const [messages, setMessages] = useState<Message[]>([]);
  const [loading, setLoading] = useState(false);

  async function sendMessage(
    conversationId: string,
    input: string,
    title: string,
    refreshSidebar: () => Promise<void>,
  ) {
    if (!input.trim() || loading) return;

    const userMessage: Message = {
      id: Date.now().toString(),
      sender: "user",
      text: input,
      timestamp: new Date(),
    };

    const assistantId = (Date.now() + 1).toString();

    const assistantMessage: Message = {
      id: assistantId,
      sender: "assistant",
      text: "",
      timestamp: new Date(),
    };

    const history = [...messages, userMessage];

    setMessages([...history, assistantMessage]);
    setLoading(true);

    try {
      const body = await streamChat(
        conversationId,
        history.map((m) => ({
          role: m.sender === "user" ? "user" : "assistant",
          content: m.text,
        })),
      );

      const reader = body.getReader();
      const decoder = new TextDecoder();

      let full = "";

      while (true) {
        const { done, value } = await reader.read();

        if (done) break;

        full += decoder.decode(value, {
          stream: true,
        });

        setMessages((prev) =>
          prev.map((msg) =>
            msg.id === assistantId
              ? {
                  ...msg,
                  text: full,
                }
              : msg,
          ),
        );
      }
      if (title === "New Chat") {
        await updateConversation(conversationId, input.slice(0, 40));

        await refreshSidebar();
      }
    } catch (err) {
      console.error(err);

      setMessages((prev) =>
        prev.map((msg) =>
          msg.id === assistantId
            ? {
                ...msg,
                text: "❌ Unable to connect to First-Son.",
              }
            : msg,
        ),
      );
    } finally {
      setLoading(false);
    }
  }

  return {
    messages,
    setMessages,
    loading,
    sendMessage,
  };
}
