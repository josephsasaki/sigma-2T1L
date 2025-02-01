
from storage import load_from_file, save_to_file


class Puzzle():

    def __init__(self, name: str, lie: str, truths: list[str]):
        # Check arguments are valid
        if not isinstance(name, str):
            raise TypeError("Unexpected name argument type.")
        if name == "":
            raise ValueError("Name argument cannot be empty.")
        if not isinstance(name, str):
            raise TypeError("Unexpected lie argument type.")
        if lie == "":
            raise ValueError("Lie argument cannot be empty.")
        if not isinstance(truths, list):
            raise TypeError("Unexpected truths argument type.")
        if len(truths) != 2:
            raise ValueError("Two truths are expected.")
        if not all(isinstance(truth, str) for truth in truths):
            raise TypeError("Unexpected truth argument type.")
        if any(truth == "" for truth in truths):
            raise TypeError("Truth argument cannot be empty.")

        self.__name = name
        self.__lie = lie
        self.__truths = truths


def choose_random_puzzle():
    """Chooses a random puzzle from the database and returns the information.
    If there are no puzzles in the database, an error is raised."""
