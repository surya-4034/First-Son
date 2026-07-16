"use client";

interface Props {
  chats: string[];
  activeChat: number;
  setActiveChat: (index: number) => void;
}

export default function Sidebar({
  chats,
  activeChat,
  setActiveChat,
}: Props) {
  return (
    <aside className="w-72 border-r border-zinc-800 bg-zinc-950 p-5">

      <h2 className="text-xl font-bold mb-6">
        Chats
      </h2>

      <div className="space-y-2">

        {chats.map((chat, index) => (

          <button
            key={index}
            onClick={() => setActiveChat(index)}
            className={`w-full text-left rounded-lg px-4 py-3 transition
              ${
                activeChat === index
                  ? "bg-blue-600"
                  : "bg-zinc-900 hover:bg-zinc-800"
              }`}
          >
            {chat}
          </button>

        ))}

      </div>

    </aside>
  );
}