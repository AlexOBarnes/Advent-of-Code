import sys
import os

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "src"))
)
from aoc import Client


class Matrix:
    def __init__(self, lines: list[str]) -> None:
        """Creates a matrix object from a grid of paper rolls"""
        self.grid = {}
        self.rows = len(lines)
        self.cols = len(lines[0])
        for i, line in enumerate(lines):
            for j, char in enumerate(line):
                self.grid[(i, j)] = char

    def is_accessible(self, coord: tuple[int, int]) -> bool:
        """Iterates through the 8 adjacent rolls and returns whether
        it has fewer than 4 adjacent rolls"""
        x = coord[0]
        y = coord[1]
        count = 0
        for di in range(-1, 2):
            for dj in range(-1, 2):
                if di == 0 and dj == 0:
                    continue
                nx, ny = x + di, y + dj
                if 0 <= nx < self.rows and 0 <= ny < self.cols:
                    if self.grid.get((nx, ny)) == "@":
                        count += 1
                        if count >= 4:
                            return False
        return True

    def paper_rolls(self) -> list[tuple[int, int]]:
        """Returns the coordiantes of all the paper rolls in the matrix"""
        return [key for key, value in self.grid.items() if value == "@"]

    def remove_rolls(self, rolls: list[tuple[int, int]]) -> None:
        """Changes a list of coordinates from @ to ."""
        for roll in rolls:
            self.grid[roll] = "."


def main():
    client = Client()
    data = client.readlines(day=4, test=False)
    matrix = Matrix(data)
    return len([roll for roll in matrix.paper_rolls() if matrix.is_accessible(roll)])


def part_two_main():
    client = Client()
    data = client.readlines(day=4, test=False)
    matrix = Matrix(data)
    total = 0
    while True:
        removed_rolls = [
            roll for roll in matrix.paper_rolls() if matrix.is_accessible(roll)
        ]
        total += len(removed_rolls)
        if len(removed_rolls) == 0:
            break
        matrix.remove_rolls(removed_rolls)
    return total


if __name__ == "__main__":
    print(main())
    print(part_two_main())
