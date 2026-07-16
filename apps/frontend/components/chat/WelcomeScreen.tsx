import Card from "../ui/Card";

export default function WelcomeScreen() {
  return (
    <div className="flex flex-1 items-center justify-center">
      <div className="max-w-3xl w-full text-center px-6">

        <h1 className="text-5xl font-bold mb-3">
          🤖 First-Son
        </h1>

        <p className="text-zinc-400 mb-10 text-lg">
          Your Personal AI Assistant
        </p>

        <div className="grid grid-cols-2 gap-5">

          <Card className="p-6 hover:border-blue-500 cursor-pointer transition">
            <h2 className="text-xl font-semibold mb-2">
              💻 Code
            </h2>

            <p className="text-zinc-400 text-sm">
              Debug, explain and generate code.
            </p>
          </Card>

          <Card className="p-6 hover:border-blue-500 cursor-pointer transition">
            <h2 className="text-xl font-semibold mb-2">
              📚 Study
            </h2>

            <p className="text-zinc-400 text-sm">
              Learn concepts and prepare notes.
            </p>
          </Card>

          <Card className="p-6 hover:border-blue-500 cursor-pointer transition">
            <h2 className="text-xl font-semibold mb-2">
              🧠 Brainstorm
            </h2>

            <p className="text-zinc-400 text-sm">
              Generate ideas and solve problems.
            </p>
          </Card>

          <Card className="p-6 hover:border-blue-500 cursor-pointer transition">
            <h2 className="text-xl font-semibold mb-2">
              🚀 Build
            </h2>

            <p className="text-zinc-400 text-sm">
              Create projects with First-Son.
            </p>
          </Card>

        </div>
      </div>
    </div>
  );
}