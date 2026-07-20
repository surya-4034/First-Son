from app.memory.conversation_memory import ConversationMemory
from app.memory.long_term_memory import LongTermMemory
from app.memory.user_profile import UserProfile
from app.memory.chroma_store import ChromaStore

class MemoryAgent:
    """
    Handles every kind of memory used by First-Son.

    Responsibilities:
    - Conversation memory
    - Long-term memory
    - User profile
    - Semantic (vector) memory
    """

    def __init__(self):
        self.short_memory = ConversationMemory()
        self.long_memory = LongTermMemory()
        self.profile = UserProfile()
        self.vector = ChromaStore()

    def prepare(self, messages):
        """
        Build the context sent to the LLM.
        """

        context = self.short_memory.build_context(messages)

        profile = self.profile.get_profile()

        memories = self.long_memory.search(
            messages[-1]["content"]
        )

        semantic_results = self.vector.search(
            messages[-1]["content"],
            limit=3,
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

        if semantic_results:
            system_context.append(
                "Knowledge:\n"
                + "\n".join(semantic_results)
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

    def remember(
        self,
        user_message: str,
        assistant_message: str,
    ):
        """
        Save useful information.

        (Implemented later)
        """
        pass