"""Contains a client for interacting with advent of code"""

import os
from datetime import datetime as dt


class Client:
    """AOC client"""

    def __init__(self, year=None, input_dir=None):
        today = dt.now()
        self.today, self.year = today.day, today.year
        if input_dir:
            self.input_dir = input_dir
        else:
            self.input_dir = os.path.abspath(
                os.path.join(
                    os.path.dirname(__file__),
                    "..",
                    f"{year if year else self.year}",
                    "input",
                )
            )
        self._cache = {}

    def get_input_path(self, day: int = None, test: bool = False, part: int = 1) -> str:
        """Returns the path to the input file for a given day and defaults to today"""
        day = day or self.today
        filename = f"day{day}"
        if test:
            filename += "_test"
        if part == 2:
            filename += "_part2"
        filename += ".txt"
        return os.path.join(self.input_dir, filename)

    def read(self, day: int = None, test: bool = False, part2: bool = False) -> str:
        """Reads the entire input file."""
        path = self.get_input_path(day, test, part2)
        if path in self._cache:
            return self._cache[path]
        with open(path, "r") as f:
            data = f.read()
        self._cache[path] = data
        return data

    def readlines(
        self, day: int = None, test: bool = False, part: int = 1, fn=None
    ) -> list[str]:
        """Read the input file as a list of lines. Optionally can apply a function to each line."""
        path = self.get_input_path(day, test, part)
        if path in self._cache:
            lines = self._cache[path].splitlines()
        else:
            with open(path, "r") as f:
                lines = [line.rstrip("\n") for line in f]
            self._cache[path] = "\n".join(lines)
        if fn is not None:
            return fn(lines)
        return lines
