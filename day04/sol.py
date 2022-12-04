def get_input():
    with open("input") as f:
        commas = [x.split(",") for x in f.readlines()]
        return [[tuple(map(int, x.split("-"))) for x in y] for y in commas]


def part1():
    s = 0
    for (x1, x2), (y1, y2) in get_input():
        if x1 >= y1 and x2 <= y2 or y1 >= x1 and y2 <= x2:
            s += 1
    return s


def part2():
    s = 0
    for (x1, x2), (y1, y2) in get_input():
        r1 = range(x1, x2 + 1)
        r2 = range(y1, y2 + 1)

        for x in r1:
            if x in r2:
                s += 1
                break
    return s


if __name__ == "__main__":
    print(part1())
    print(part2())
