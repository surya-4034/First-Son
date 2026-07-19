from typing import List


class ConversationMemory:
    """
    Stores the current conversation context.

    Later this will support:
    - summarization
    - token trimming
    - vector retrieval
    """

    def build_context(
        self,
        messages: List[dict],
    ) -> List[dict]:

        return messages