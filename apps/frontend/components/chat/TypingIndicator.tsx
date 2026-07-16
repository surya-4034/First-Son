export default function TypingIndicator() {
  return (
    <div className="flex items-end gap-3 mb-5">
      <div className="w-10 h-10 rounded-full bg-blue-600 flex items-center justify-center">
        🤖
      </div>

      <div className="bg-zinc-800 rounded-2xl px-5 py-4">
        <div className="flex gap-2">
          <span className="w-2 h-2 bg-white rounded-full animate-bounce"></span>
          <span
            className="w-2 h-2 bg-white rounded-full animate-bounce"
            style={{ animationDelay: "0.2s" }}
          ></span>
          <span
            className="w-2 h-2 bg-white rounded-full animate-bounce"
            style={{ animationDelay: "0.4s" }}
          ></span>
        </div>
      </div>
    </div>
  );
}