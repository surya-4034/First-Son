import argparse
from pathlib import Path

from app.training.training_manager import (
    TrainingManager,
)


def main():

    parser = argparse.ArgumentParser()

    parser.add_argument(
        "path",
        help="File or Folder",
    )

    args = parser.parse_args()

    trainer = TrainingManager()

    target = Path(args.path)

    if target.is_dir():

        trainer.train_folder(
            str(target)
        )

    else:

        trainer.train_file(
            str(target)
        )


if __name__ == "__main__":
    main()