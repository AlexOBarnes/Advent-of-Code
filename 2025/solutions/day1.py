class Lock:
    def __init__(self):
        self.position = 50
        self.zero_passes = 0

    def left_rotation(self, val):
        full_cycles, remainder = divmod(val, 100)
        self.zero_passes += full_cycles
        for _ in range(remainder):
            self.position -= 1
            if self.position < 0:
                self.position = 99
            if self.position == 0:
                self.zero_passes += 1

    def right_rotation(self, val):
        full_cycles, remainder = divmod(val, 100)
        self.zero_passes += full_cycles
        for _ in range(remainder):
            self.position += 1
            if self.position > 99:
                self.position = 0
            if self.position == 0:
                self.zero_passes += 1


def read_file(filename):
    with open(f"input/{filename}", "r") as f:
        data = f.readlines()

    return [row.strip() for row in data]


def part_one_main():
    data = read_file("../input/day1.txt")
    rotations = [(row[0], int(row[1:])) for row in data]
    lock = Lock()
    total = 0
    for rotation in rotations:
        if rotation[0] == "L":
            lock.left_rotation(rotation[1])
        else:
            lock.right_rotation(rotation[1])
        if lock.position < 0:
            print(f"error low: {lock.position}")
        if lock.position > 99:
            print(f"error high: {lock.position}")
        if lock.position == 0:
            total += 1

    return total


def part_two_main():
    data = read_file("../input/day1.txt")
    rotations = [(row[0], int(row[1:])) for row in data]
    lock = Lock()
    for rotation in rotations:
        if rotation[0] == "L":
            lock.left_rotation(rotation[1])
        else:
            lock.right_rotation(rotation[1])

    return lock.zero_passes


if __name__ == "__main__":
    print(part_one_main())
    print(part_two_main())
