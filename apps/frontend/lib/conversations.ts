import api from "./api";

export async function getConversations() {
  const res = await api.get("/conversations");
  return res.data;
}

export async function createConversation(title = "New Chat") {
  const res = await api.post("/conversations", {
    title,
  });

  return res.data;
}

export async function getConversation(id: string) {
  const res = await api.get(`/conversations/${id}`);
  return res.data;
}

export async function updateConversation(
  id: string,
  title: string,
) {
  const res = await api.put(`/conversations/${id}`, {
    title,
  });

  return res.data;
}