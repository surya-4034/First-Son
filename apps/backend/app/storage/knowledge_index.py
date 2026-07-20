import json
from pathlib import Path


class KnowledgeIndex:
    """
    Tracks which files have already been indexed.
    """

    INDEX_FILE = Path("storage/knowledge_index.json")

    def __init__(self):

        self.INDEX_FILE.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        if not self.INDEX_FILE.exists():

            self.INDEX_FILE.write_text(
                "{}",
                encoding="utf-8",
            )

    def load(self):

        return json.loads(
            self.INDEX_FILE.read_text(
                encoding="utf-8",
            )
        )

    def save(self, data):

        self.INDEX_FILE.write_text(
            json.dumps(
                data,
                indent=4,
            ),
            encoding="utf-8",
        )

    def is_trained(
        self,
        path: str,
        modified_time: float,
    ):

        data = self.load()

        return (
            path in data
            and data[path] == modified_time
        )

    def update(
        self,
        path: str,
        modified_time: float,
    ):

        data = self.load()

        data[path] = modified_time

        self.save(data)