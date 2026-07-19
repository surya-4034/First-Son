from app.memory.chroma_store import ChromaStore


class LongTermMemory:

    def __init__(self):

        self.store = ChromaStore()

    def add_memory(
        self,
        text: str,
        metadata: dict | None = None,
    ):

        self.store.add(
            text,
            metadata,
        )

    def search(
        self,
        query: str,
        limit: int = 5,
    ):

        return self.store.search(
            query,
            limit,
        )