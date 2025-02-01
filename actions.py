import random

from storage import load_from_file, save_to_file


def choose_random_puzzle():
    """Chooses a random puzzle from the database and returns the information.
    If there are no puzzles in the database, an error is raised."""
    puzzles = load_from_file()
    if len(puzzles) == 0:
        raise ValueError("There are currently no puzzles in storage.")
    return random.choice(puzzles)
