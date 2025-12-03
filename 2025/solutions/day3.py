import os
import sys

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "src"))
)
from aoc import Client


def select_digit(pack: list[int], idx: int, digit: int) -> tuple[int, int]:
    candidates = pack[idx : len(pack) - digit] if digit >= 1 else pack[idx:]
    current_digit = max(candidates)
    next_idx = idx + candidates.index(current_digit) + 1
    return current_digit, next_idx


def calculate_joltage(pack: list[int], length: int) -> int:
    idx = 0
    digits = []
    for digit in range(length - 1, -1, -1):
        current_digit, idx = select_digit(pack, idx, digit)
        digits.append(str(current_digit))
    return int("".join(digits))


def find_total_joltage(battery_packs: list[list[int]], length: int = 2) -> int:
    return sum(calculate_joltage(pack, length) for pack in battery_packs)


def main(length):
    client = Client()
    data = client.readlines(
        day=3,
        test=False,
        fn=lambda lines: [
            [int(digit) for digit in num] for line in lines for num in line.split()
        ],
    )
    return find_total_joltage(data, length=length)


if __name__ == "__main__":
    print(main(2))
    print(main(12))
