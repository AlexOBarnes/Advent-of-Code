"""Solution for day 2 problem advent of code https://adventofcode.com/2025/day/2"""

import os
import re
import sys

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "src"))
)
from aoc import Client


def is_repeated(num, check_for_multiple_repeats=False):
    """Checks if a number is a repeated sequence using regex.
    If check_for_multiple_repeats is True, checks for multiple repeats.
    """
    s = str(num)
    pattern = r"(\d+)\1+" if check_for_multiple_repeats else r"(\d+)\1"
    return bool(re.fullmatch(pattern, s))


def id_iterator(ids: list, check_multiples=False):
    """Iterates through an id range"""
    return sum(
        [
            i
            for i in range(int(ids[0]), int(ids[1]) + 1)
            if is_repeated(i, check_multiples)
        ]
    )


def part_one_main():
    client = Client()
    id_ranges = client.read(
        day=2,
        test=False,
        fn=lambda line: [id_range.split("-") for id_range in line.split(",")],
    )
    return sum([id_iterator(id_range, False) for id_range in id_ranges])


def part_two_main():
    client = Client()
    id_ranges = client.read(
        day=2,
        test=False,
        fn=lambda line: [id_range.split("-") for id_range in line.split(",")],
    )
    return sum([id_iterator(id_range, True) for id_range in id_ranges])


if __name__ == "__main__":
    print(part_one_main())
    print(part_two_main())
