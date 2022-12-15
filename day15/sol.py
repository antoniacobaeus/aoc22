from functools import reduce


def get_input():
    with open("input") as f:
        for line in f.readlines():
            line = line.strip().split(", ")
            x1 = line[0].split("=")[-1]
            y1 = line[1].split("=")[1].split(":")[0]
            x2 = line[1].split("=")[-1]
            y2 = line[2].split("=")[-1]
            yield ((int(x1), int(y1)), (int(x2), int(y2)))


def manhattan_distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)


def part1():
    distances = {}
    beacons = set()
    for (x1, y1), (x2, y2) in get_input():
        distances[(x1, y1)] = manhattan_distance(x1, y1, x2, y2)
        beacons.add((x2, y2))
    y = 2000000
    points = set()
    for k, v in distances.items():
        x1, y1 = k
        h = v - abs(y - y1)
        if h < 0:
            continue
        points |= set(range(x1 - h, x1 + h + 1))
    return len(points) - len(list(filter(lambda c: c[1] == y, beacons)))


def part2():
    pass


if __name__ == "__main__":
    print(part1())
    print(part2())
