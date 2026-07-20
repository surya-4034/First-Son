from pathlib import Path

from app.training.repository_scanner import (
    RepositoryScanner,
)

class RepositoryScanner:

    SUPPORTED = {
        ".py",
        ".md",
        ".txt",
        ".json",
        ".yaml",
        ".yml",
        ".toml",
        ".tsx",
        ".ts",
        ".js",
        ".jsx",
        ".html",
        ".css",
    }

    IGNORE = {
        ".git",
        ".venv",
        "__pycache__",
        "node_modules",
        "dist",
        "build",
        ".next",
        ".idea",
        ".vscode",
    }

    def scan(
        self,
        repository: Path,
    ):

        files = []

        for file in repository.rglob("*"):

            if any(
                part in self.IGNORE
                for part in file.parts
            ):
                continue

            if file.suffix.lower() not in self.SUPPORTED:
                continue

            files.append(file)

        return files