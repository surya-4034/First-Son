from app.rag.document_loader import DocumentLoader
from app.rag.chunker import Chunker
from app.memory.chroma_store import ChromaStore


class KnowledgeImporter:
    """
    Imports external knowledge into First-Son's
    vector database.
    """

    def __init__(self):
        self.loader = DocumentLoader()
        self.chunker = Chunker()
        self.vector = ChromaStore()

    def import_file(
        self,
        path: str,
        metadata: dict | None = None,
    ):
        """
        Load a document, split it into chunks,
        and store every chunk.
        """

        text = self.loader.load(path)

        chunks = self.chunker.split(text)

        for chunk in chunks:
            self.vector.add(
                chunk,
                metadata=metadata,
            )

        return len(chunks)