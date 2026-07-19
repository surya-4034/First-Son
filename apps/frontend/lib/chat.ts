import api from "./api";

export async function streamChat(
  conversationId: string,
  messages: {
    role: string;
    content: string;
  }[],
) {
  const response = await fetch(
    "http://127.0.0.1:8000/chat/stream",
    {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        conversation_id: conversationId,
        messages,
      }),
    }
  );

  if (!response.ok) {
    throw new Error("Request failed");
  }

  if (!response.body) {
    throw new Error("Streaming not supported");
  }

  return response.body;
}

export async function chat(
  conversationId: string,
  messages: {
    role: string;
    content: string;
  }[],
) {
  const response = await api.post("/chat", {
    conversation_id: conversationId,
    messages,
  });

  return response.data;
}