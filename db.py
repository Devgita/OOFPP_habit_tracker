import json
from typing import List, Dict, Any


class JSONDatabase:
    """
    storing and looking up the JSON file.
    """

    def __init__(self, file_path:str):
        """
        sets up the database with a file path.

        :parameter file_path: Path to the JSON file.
        """
        self.file_path = file_path

    def load(self) -> List[Dict[str, Any]]:
        """
        Loads the data from the JSON file. Returns empty list for each
        file that does not exist.
        """
        try:
            with open(self.file_path, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            # Return empty list if file is not found.
            return []

    def save(self, data: List[Dict[str, Any]]) -> None:
        """
        Saves data to the JSON file.

        """
        with open(self.file_path, "w") as file:
            json.dump(data, file, indent=5)
