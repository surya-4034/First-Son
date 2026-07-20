from pathlib import Path

from app.rag.importer import KnowledgeImporter


class TrainingManager:
    """
    Central training manager for First-Son.

    Every knowledge source eventually comes through here.
    """

    def __init__(self):
        self.importer = KnowledgeImporter()
        from app.storage.knowledge_index import (
    KnowledgeIndex,
)
self.index = KnowledgeIndex()

    def train_file(
        self,
        file_path: str,
    ) -> int:

        path = Path(file_path)

        if not path.exists():
            raise FileNotFoundError(file_path)

        print(f"\n📄 Training on {path.name}")

        chunks = self.importer.import_file(
            str(path),
            metadata={
                "source": "file",
                "filename": path.name,
            },
        )

        print(
            f"✅ Imported {chunks} chunks"
        )

        return chunks

        def train_folder(
    self,
    folder: str,
):
    """
    Train First-Son on every supported file
    inside a folder.
    """

    folder = Path(folder)

    if not folder.exists():
        raise FileNotFoundError(folder)

    supported = {
        ".txt",
        ".md",
        ".pdf",
        ".docx",
    }

    total_chunks = 0

    for file in folder.rglob("*"):

        if file.suffix.lower() not in supported:
            continue

        print(f"\n📄 {file.name}")

       modified = file.stat().st_mtime

if self.index.is_trained(
    str(file),
    modified,
):
    print(f"⏩ Skipping {file.name}")
    continue

chunks = self.importer.import_file(
    str(file),
    metadata={
        "source": "folder",
        "filename": file.name,
    },
)

self.index.update(
    str(file),
    modified,
)

        total_chunks += chunks

    print(
        f"\n✅ Finished training."
    )

    print(
        f"Stored {total_chunks} chunks."
    )

def train_path(self, path: str):

    if Path(path).is_dir():
        self.train_folder(path)
    else:
        self.train_file(path)