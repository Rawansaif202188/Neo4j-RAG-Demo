from pathlib import Path


def load_documents(file_path: str) -> list[str]:
    """Load non-empty lines from a text file."""

    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(
            f"Document file not found: {file_path}"
        )

    with path.open("r", encoding="utf-8") as file:
        documents = [
            line.strip()
            for line in file
            if line.strip()
        ]

    return documents