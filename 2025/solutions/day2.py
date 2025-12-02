"""Solution for day 2 problem advent of code https://adventofcode.com/2025/day/2"""

import sys
import os

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "src"))
)
from aoc import Client


def is_double_sequence(num):
    """Checks if a sequence is a duplicated string of numbers"""
    s = str(num)
    n = len(s)
    if n % 2 != 0:
        return False
    half = n // 2
    return s[:half] == s[half:]


def is_repeated_sequence(num):
    """Checks if a number is made up of a repeated string of numbers"""
    s = str(num)
    n = len(s)
    for size in range(1, n // 2 + 1):
        if n % size == 0:
            if s == s[:size] * (n // size):
                return True
    return False


def id_iterator(ids: list, checker=is_double_sequence):
    """Iterates through a an id range"""
    total = 0
    for i in range(int(ids[0]), int(ids[1]) + 1):
        if checker(i):
            total += i
    return total


def part_one_main():
    client = Client()
    id_ranges = client.read(
        day=2,
        test=False,
        fn=lambda line: [id_range.split("-") for id_range in line.split(",")],
    )
    return sum([id_iterator(id_range) for id_range in id_ranges])


def part_two_main():
    client = Client()
    id_ranges = client.read(
        day=2,
        test=False,
        fn=lambda line: [id_range.split("-") for id_range in line.split(",")],
    )
    return sum(
        [id_iterator(id_range, checker=is_repeated_sequence) for id_range in id_ranges]
    )


if __name__ == "__main__":
    print(part_one_main())
    print(part_two_main())
