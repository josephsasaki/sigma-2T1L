from random import shuffle


class Puzzle():

    @staticmethod
    def json_to_obj(puzzles: list[dict[str]]) -> list["Puzzle"]:
        """Takes the json data on puzzles and produces the puzzle objects."""
        # Check argument is valid
        if not isinstance(puzzles, list):
            raise TypeError("Unexpected puzzles argument type.")
        if not all(isinstance(puzzle, dict) for puzzle in puzzles):
            raise TypeError("Unexpected puzzles argument type.")
        if any(puzzle.get("id") is None for puzzle in puzzles):
            raise KeyError("ID key missing from puzzle data.")
        if any(puzzle.get("name") is None for puzzle in puzzles):
            raise KeyError("Name key missing from puzzle data.")
        if any(puzzle.get("lie") is None for puzzle in puzzles):
            raise KeyError("Lie key missing from puzzle data.")
        if any(puzzle.get("truth_1") is None for puzzle in puzzles):
            raise KeyError("Truth key missing from puzzle data.")
        if any(puzzle.get("truth_2") is None for puzzle in puzzles):
            raise KeyError("Truth key missing from puzzle data.")

        obj_list = []
        for puzzle in puzzles:
            obj_puzzle = Puzzle(
                p_id=puzzle.get("id"),
                name=puzzle.get("name"),
                lie=puzzle.get("lie"),
                truths=[puzzle.get("truth_1"), puzzle.get("truth_2")]
            )
            obj_list.append(obj_puzzle)
        return obj_list

    @staticmethod
    def obj_to_json(puzzles: list["Puzzle"]) -> list[dict[str]]:
        """Takes a list of puzzles and converts it to a json object to dump in storage."""
        # Check argument is valid
        if not isinstance(puzzles, list):
            raise TypeError("Unexpected puzzles argument type.")
        if not all(isinstance(puzzle, Puzzle) for puzzle in puzzles):
            raise TypeError("Unexpected puzzle argument type.")

        json_list = []
        for puzzle in puzzles:
            json_list.append(puzzle.to_storage_json())
        return json_list

    def __init__(self, p_id: int, name: str, lie: str, truths: list[str]) -> None:
        # Check arguments are valid
        if not isinstance(p_id, int):
            raise TypeError("Unexpected id argument type.")
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

        self.__id = p_id
        self.__name = name
        self.__lie = lie
        self.__truths = truths

    def get_id(self) -> int:
        """Get the puzzle's id."""
        return self.__id

    def get_name(self) -> str:
        """Get the puzzle's person's name."""
        return self.__name

    def get_lie(self) -> str:
        """Get the puzzle's lie."""
        return self.__lie

    def get_truths(self) -> list[str]:
        """Get the puzzle's truths."""
        return self.__truths

    def to_storage_json(self) -> dict[str]:
        """Return the puzzle formatted as a json object to be stored in storage."""
        return {
            "id": self.__id,
            "name": self.__name,
            "lie": self.__lie,
            "truth_1": self.__truths[0],
            "truth_2": self.__truths[1],
        }

    def to_api_json(self) -> dict[str, int]:
        """Return the puzzle formatted as a json object to be send via the api to the front-end."""
        statements = [self.__lie, *self.__truths]
        shuffle(statements)
        lie_index = statements.index(self.__lie)
        return {
            "name": self.__name,
            "statements": statements,
            "lie_index": lie_index,
        }
