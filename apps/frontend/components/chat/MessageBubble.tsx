import { Message } from "../../types/chat";

interface Props {
  message: Message;
}

export default function MessageBubble({ message }: Props) {
  const isUser = message.sender === "user";

  return (
    <div
      className={`flex items-end gap-3 mb-5 ${
        isUser ? "justify-end" : "justify-start"
      }`}
    >
      {!isUser && (
        <div className="w-10 h-10 rounded-full bg-blue-600 flex items-center justify-center text-lg">
          🤖
        </div>
      )}

      <div
        className={`max-w-[75%] px-5 py-3 rounded-2xl shadow-md whitespace-pre-wrap ${
          isUser
            ? "bg-blue-600 text-white rounded-br-md"
            : "bg-zinc-800 text-white rounded-bl-md"
        }`}
      >
        {message.text}
      </div>

      {isUser && (
        <div className="w-10 h-10 rounded-full bg-green-600 flex items-center justify-center text-lg">
          🙂
        </div>
      )}
    </div>
  );
}