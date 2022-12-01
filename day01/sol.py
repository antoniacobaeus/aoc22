def get_input():
    with open("input") as f:
        for block in f.read().strip().split("\n\n"):
            yield [int(x) for x in block.split("\n")]


def part1():
    elfs = get_input()
    return max(map(sum, elfs))


def part2():
    elfs = get_input()
    sums = map(sum, elfs)
    return sum(sorted(sums, reverse=True)[:3])


if __name__ == "__main__":
    print(part1())
    print(part2())
