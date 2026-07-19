export interface Conversation {
  id: string;
  title: string;
  created_at: string;
}

export interface ConversationDetail {
  id: string;
  title: string;
  created_at: string;
  messages: {
    id: string;
    role: string;
    content: string;
    created_at: string;
  }[];
}