interface Props {
  message: string;
  setMessage: (value: string) => void;
  sendMessage: () => void;
}

export default function ChatInput({
  message,
  setMessage,
  sendMessage,
}: Props) {
  return (
    <div className="border-t border-zinc-800 p-4 flex gap-3">
      <input
        className="flex-1 rounded-lg bg-zinc-900 px-4 py-3 outline-none"
        placeholder="Ask First-Son anything..."
        value={message}
        onChange={(e) => setMessage(e.target.value)}
        onKeyDown={(e) => {
          if (e.key === "Enter") {
            sendMessage();
          }
        }}
      />

      <button
        onClick={sendMessage}
        className="rounded-lg bg-blue-600 px-6 py-3 hover:bg-blue-700"
      >
        Send
      </button>
    </div>
  );
}