from pathlib import Path

from app.rag.parsers.txt_loader import TXTLoader
from app.rag.parsers.pdf_loader import PDFLoader
from app.rag.parsers.md_loader import MarkdownLoader
from app.rag.parsers.docx_loader import DocxLoader


class DocumentLoader:
    """
    Loads any supported document type.
    """

    def __init__(self):
        self.loaders = {
            ".txt": TXTLoader(),
            ".pdf": PDFLoader(),
            ".md": MarkdownLoader(),
            ".docx": DocxLoader(),
        }

    def load(self, path: str) -> str:

        extension = Path(path).suffix.lower()

        if extension not in self.loaders:
            raise ValueError(
                f"Unsupported document type: {extension}"
            )

        return self.loaders[extension].load(path)