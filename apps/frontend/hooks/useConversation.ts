import { useEffect, useState, useCallback } from "react";

import {
  createConversation,
  getConversation,
  getConversations,
} from "../lib/conversations";

import { Conversation } from "../types/conversation";
import { Message } from "../types/chat";

export function useConversation() {
  const [conversations, setConversations] = useState<Conversation[]>([]);
  const [activeConversationId, setActiveConversationId] = useState("");

  const initialize = useCallback(async () => {
    const data = await getConversations();

    setConversations(data);

    if (data.length > 0) {
      setActiveConversationId(data[0].id);
    }
  }, []);

  useEffect(() => {
    initialize().catch(console.error);
  }, [initialize]);

  const refreshSidebar = useCallback(async () => {
    const data = await getConversations();
    setConversations(data);
  }, []);

  const createNewConversation = useCallback(async () => {
    const conversation = await createConversation("New Chat");

    setConversations((prev) => [
      conversation,
      ...prev,
    ]);

    setActiveConversationId(conversation.id);

    return conversation.id;
  }, []);

  const loadConversation = useCallback(
    async (id: string): Promise<Message[]> => {
      setActiveConversationId(id);

      const conversation = await getConversation(id);

      return conversation.messages.map((m: any) => ({
        id: m.id,
        sender: m.role === "user" ? "user" : "assistant",
        text: m.content,
        timestamp: new Date(m.created_at),
      }));
    },
    [],
  );

  return {
    conversations,
    activeConversationId,
    refreshSidebar,
    initialize,
    loadConversation,
    createNewConversation,
    setActiveConversationId,
  };
}