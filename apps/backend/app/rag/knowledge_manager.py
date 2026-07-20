from app.rag.retriever import Retriever


class KnowledgeManager:
    """
    Central access point for all external knowledge.
    """

    def __init__(self):
        self.retriever = Retriever()

    def search(
        self,
        query: str,
        limit: int = 5,
    ):
        """
        Search all available knowledge sources.
        """

        return self.retriever.search(
            query=query,
            limit=limit,
        )

    def add_document(
        self,
        text: str,
        metadata: dict | None = None,
    ):
        """
        Add a document into the knowledge base.
        """

        return self.retriever.add_document(
            text=text,
            metadata=metadata or {},
        )