import { useRef, KeyboardEvent } from "react";
import Button from "../ui/Button";
import { PLACEHOLDER } from "../../utils/constants";

interface Props {
  message: string;
  setMessage: (value: string) => void;
  sendMessage: () => void;
  loading: boolean;
}

export default function ChatInput({
  message,
  setMessage,
  sendMessage,
  loading,
}: Props) {
  const inputRef = useRef<HTMLTextAreaElement>(null);

  function handleKeyDown(e: KeyboardEvent<HTMLTextAreaElement>) {
    if (e.key === "Enter" && !e.shiftKey) {
      e.preventDefault();

      if (!loading) {
        sendMessage();

        setTimeout(() => {
          inputRef.current?.focus();
        }, 50);
      }
    }
  }

  return (
    <div className="border-t border-zinc-800 bg-zinc-950 p-5">

      <div className="flex gap-3">

        <textarea
          ref={inputRef}
          rows={2}
          disabled={loading}
          value={message}
          placeholder={PLACEHOLDER}
          onChange={(e) => setMessage(e.target.value)}
          onKeyDown={handleKeyDown}
          className="flex-1 resize-none rounded-xl bg-zinc-900 px-4 py-3 outline-none disabled:opacity-50"
        />

        <Button
          onClick={sendMessage}
          disabled={loading}
        >
          {loading ? "Thinking..." : "Send"}
        </Button>

      </div>

    </div>
  );
}