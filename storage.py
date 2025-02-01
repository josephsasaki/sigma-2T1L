"""Storage: Handling loading and saving to file."""

from json import load, dump


def load_from_file() -> list[dict]:
    """Load the puzzles from a file called storage.json"""
    with open("storage.json", mode="r", encoding="UTF-8") as f:
        return load(f)


def save_to_file(data: list[dict[str]]) -> None:
    """Save the puzzles to a file called storage.json"""
    with open("storage.json", mode="w", encoding="UTF-8") as f:
        dump(data, f)
