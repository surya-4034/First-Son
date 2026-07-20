class MarkdownLoader:

    def load(
        self,
        path: str,
    ):

        with open(
            path,
            "r",
            encoding="utf-8",
        ) as f:
            return f.read()