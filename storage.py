"""Storage: Handling loading and saving to file."""

from json import load, dump

from puzzles import Puzzle


def load_from_file() -> list[Puzzle]:
    """Load the puzzles from a file called storage.json"""
    with open("storage.json", mode="r", encoding="UTF-8") as f:
        return Puzzle.json_to_obj(load(f))


def save_to_file(puzzles: list[Puzzle]) -> None:
    """Save the puzzles to a file called storage.json"""
    with open("storage.json", mode="w", encoding="UTF-8") as f:
        dump(Puzzle.obj_to_json(puzzles), f)
