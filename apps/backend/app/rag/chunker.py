class Chunker:
    """
    Splits large text into smaller overlapping chunks.
    """

    def __init__(
        self,
        chunk_size: int = 500,
        overlap: int = 100,
    ):
        self.chunk_size = chunk_size
        self.overlap = overlap

    def split(self, text: str) -> list[str]:

        if not text.strip():
            return []

        chunks = []

        start = 0

        while start < len(text):

            end = start + self.chunk_size

            chunks.append(
                text[start:end]
            )

            start += (
                self.chunk_size
                - self.overlap
            )

        return chunks