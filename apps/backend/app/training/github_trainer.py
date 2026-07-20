import shutil
import subprocess
from pathlib import Path

from app.rag.importer import KnowledgeImporter
from app.training.repository_scanner import RepositoryScanner


class GitHubTrainer:
    """
    Downloads a GitHub repository and imports it
    into First-Son's knowledge base.
    """

    def __init__(self):
        self.importer = KnowledgeImporter()
        self.scanner = RepositoryScanner()

    def train_repository(
        self,
        repo_url: str,
    ) -> int:

        workspace = Path("storage/github")
        workspace.mkdir(
            parents=True,
            exist_ok=True,
        )

        repo_name = repo_url.rstrip("/").split("/")[-1]
        repo_path = workspace / repo_name

        if repo_path.exists():
            shutil.rmtree(repo_path)

        print(f"\n📥 Cloning {repo_url}")

        subprocess.run(
            [
                "git",
                "clone",
                repo_url,
                str(repo_path),
            ],
            check=True,
        )

        files = self.scanner.scan(repo_path)

        total = 0

        for file in files:

            print(f"📄 {file.relative_to(repo_path)}")

            total += self.importer.import_file(
                str(file),
                metadata={
                    "source": "github",
                    "repository": repo_name,
                    "path": str(file.relative_to(repo_path)),
                },
            )

        print(f"\n✅ Imported {total} chunks")

        return total