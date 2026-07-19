from abc import ABC, abstractmethod


class VectorStore(ABC):

    @abstractmethod
    def add(
        self,
        text: str,
        metadata: dict | None = None,
    ):
        pass

    @abstractmethod
    def search(
        self,
        query: str,
        limit: int = 5,
    ):
        pass

    @abstractmethod
    def delete(
        self,
        memory_id: str,
    ):
        pass

    @abstractmethod
    def clear(self):
        pass