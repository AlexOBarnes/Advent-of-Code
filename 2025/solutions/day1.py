import sys
import os

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "src"))
)
from aoc import Client


class Lock:
    """Lock object that can rotate L or R with min value 0 and max value 99"""

    def __init__(self):
        self.position = 50
        self.zero_passes = 0
        self.zeroes = 0

    def rotate(self, direction: str, value: int) -> None:
        full_cycles, remainder = divmod(value, 100)
        self.zero_passes += full_cycles
        for _ in range(remainder):
            if direction == "L":
                self.position -= 1
                if self.position < 0:
                    self.position = 99
            else:
                self.position += 1
                if self.position > 99:
                    self.position = 0
            if self.position == 0:
                self.zero_passes += 1

    def run_rotations(self, rotations: list[tuple[str, int]]) -> None:
        self.zeroes = 0
        for rotation in rotations:
            self.rotate(rotation[0], rotation[1])
            if self.position == 0:
                self.zeroes += 1


def part_one_main() -> int:
    client = Client()
    rotations = client.readlines(
        day=1, fn=lambda rows: [(row[0], int(row[1:])) for row in rows]
    )
    lock = Lock()
    lock.run_rotations(rotations)
    return lock.zeroes


def part_two_main() -> int:
    client = Client()
    rotations = client.readlines(
        day=1, fn=lambda rows: [(row[0], int(row[1:])) for row in rows]
    )
    lock = Lock()
    lock.run_rotations(rotations)
    return lock.zero_passes


if __name__ == "__main__":
    print(part_one_main())
    print(part_two_main())
