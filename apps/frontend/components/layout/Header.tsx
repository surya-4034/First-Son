"use client";

import Button from "../ui/Button";

interface Props {
  onNewChat: () => void;
}

export default function Header({
  onNewChat,
}: Props) {
  return (
    <header className="h-16 border-b border-zinc-800 bg-zinc-950 flex items-center justify-between px-6">

      <div>

        <h1 className="text-2xl font-bold">
          🤖 First-Son
        </h1>

        <p className="text-zinc-500 text-sm">
          Personal AI Assistant
        </p>

      </div>

      <Button
        onClick={onNewChat}
      >
        + New Chat
      </Button>

    </header>
  );
}