import { Message } from "../types/chat";

interface Props {
  message: Message;
}

export default function MessageBubble({ message }: Props) {
  const isUser = message.sender === "user";

  return (
    <div className={`flex ${isUser ? "justify-end" : "justify-start"} mb-4`}>
      <div
        className={`max-w-[70%] rounded-xl px-4 py-3 ${
          isUser ? "bg-blue-600 text-white" : "bg-zinc-800 text-white"
        }`}
      >
        {message.text}
      </div>
    </div>
  );
}