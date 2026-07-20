import uuid

import chromadb

from app.memory.embedding import EmbeddingModel
from app.memory.vector_store import VectorStore


class ChromaStore(VectorStore):

    def __init__(self):

        self.client = chromadb.PersistentClient(
            path="storage/chroma",
        )

        self.collection = self.client.get_or_create_collection(
            name="first_son",
        )

        self.embedding = EmbeddingModel()

    def add(
        self,
        text: str,
        metadata: dict | None = None,
    ):

        embedding = self.embedding.encode(text)

        self.collection.add(
            ids=[str(uuid.uuid4())],
            documents=[text],
            embeddings=[embedding],
            metadatas=[metadata or {}],
        )

    def search(
        self,
        query: str,
        limit: int = 5,
    ):

        embedding = self.embedding.encode(query)

        results = self.collection.query(
            query_embeddings=[embedding],
            n_results=limit,
        )

        if not results["documents"]:
            return []

        return results["documents"][0]

    def delete(
        self,
        memory_id: str,
    ):

        self.collection.delete(
            ids=[memory_id],
        )

    def clear(self):

        self.client.delete_collection(
            "first_son",
        )

        self.collection = self.client.get_or_create_collection(
            name="first_son",
        )