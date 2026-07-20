from app.memory.vector_store import VectorStore


class Retriever:
    """
    Retrieves relevant knowledge from the vector database.
    Every knowledge search in First-Son goes through this class.
    """

    def __init__(self):
        self.vector_store = VectorStore()

    def search(
        self,
        query: str,
        limit: int = 5,
    ):
        """
        Search the knowledge base.
        """

        return self.vector_store.search(
            query=query,
            limit=limit,
        )

    def add_document(
        self,
        text: str,
        metadata: dict | None = None,
    ):
        """
        Store a document in the vector database.
        """

        self.vector_store.add_document(
            text=text,
            metadata=metadata or {},
        )