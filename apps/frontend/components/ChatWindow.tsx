import { Message } from "../types/chat";
import MessageBubble from "./MessageBubble";
import TypingIndicator from "./TypingIndicator";

interface Props {
  messages: Message[];
  loading: boolean;
}

export default function ChatWindow({ messages, loading }: Props) {
  return (
    <div className="flex-1 overflow-y-auto p-6">
      {messages.length === 0 ? (
        <div className="flex h-full items-center justify-center text-zinc-500">
          Start a conversation with First-Son 🚀
        </div>
      ) : (
        <>
          {messages.map((message) => (
            <MessageBubble key={message.id} message={message} />
          ))}

          {loading && <TypingIndicator />}
        </>
      )}
    </div>
  );
}