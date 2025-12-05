import sys
import os

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "src"))
)
from aoc import Client


def count_fresh_ids(intervals: list[list[int]], ids: list[int]) -> int:
    return sum(
        any(lower_bound <= idx <= upper_bound for lower_bound, upper_bound in intervals)
        for idx in ids
    )


def count_all_ids(intervals: list[list[int]]) -> int:
    count = 0
    current = 0
    for lower_bound, upper_bound in sorted(intervals):
        new_current = max(current, upper_bound)
        if lower_bound <= current:
            count += new_current - current
        else:
            count += upper_bound - lower_bound + 1
        current = new_current
    return count


def main():
    client = Client()
    intervals, ids = client.readlines(
        day=5,
        test=False,
        fn=lambda lines: (
            [
                [int(i) for i in x.split("-")]
                for x in "\n".join(lines).split("\n\n")[0].split()
            ],
            [int(i) for i in "\n".join(lines).split("\n\n")[1].split()],
        ),
    )
    print(count_fresh_ids(intervals, ids))
    print(count_all_ids(intervals))


if __name__ == "__main__":
    main()
