from app.memory.conversation_memory import ConversationMemory
from app.memory.long_term_memory import LongTermMemory
from app.memory.user_profile import UserProfile


class MemoryAgent:

    def __init__(self):
        self.short_memory = ConversationMemory()
        self.long_memory = LongTermMemory()
        self.profile = UserProfile()

    def prepare(self, messages):

        context = self.short_memory.build_context(
            messages
        )

        profile = self.profile.get_profile()

        memories = self.long_memory.search(
            messages[-1]["content"]
        )

        system_context = []

        if profile["preferences"]:
            system_context.append(
                "User Preferences:\n"
                + "\n".join(profile["preferences"])
            )

        if memories:
            system_context.append(
                "Relevant Memories:\n"
                + "\n".join(memories)
            )

        if system_context:

            context.insert(
                0,
                {
                    "role": "system",
                    "content": "\n\n".join(system_context),
                },
            )

        return context