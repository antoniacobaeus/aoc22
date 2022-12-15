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


def parse_input(data):
    distances = {}
    beacons = set()
    for (x1, y1), (x2, y2) in data:
        distances[(x1, y1)] = manhattan_distance(x1, y1, x2, y2)
        beacons.add((x2, y2))
    return distances, beacons


def part1(y=10):
    distances, beacons = parse_input(get_input())
    points = set()
    for (x1, y1), v in distances.items():
        h = v - abs(y - y1)
        if h < 0:
            continue
        points |= set(range(x1 - h, x1 + h + 1))
    return len(points) - len(list(filter(lambda c: c[1] == y, beacons)))


def get_edge_of_circle(radius, x1, y1):
    for x in range(x1 - radius, x1 + radius + 1):
        y = y1 - radius + abs(x - x1)
        yield x, y
        y = y1 + radius - abs(x - x1)
        yield x, y


def in_circle(x, y, x1, y1, radius):
    return manhattan_distance(x, y, x1, y1) - radius <= 0


def part2(M=20):
    #  Math is hard...
    #  https://math.stackexchange.com/questions/3476324/find-closest-location-not-occupied-by-circles
    distances, _ = parse_input(get_input())
    for (x1, x2), v in distances.items():
        for x, y in get_edge_of_circle(v+1, x1, x2):
            if not (0 < x < M and 0 < y < M):
                continue
            if any(in_circle(x, y, cx, cy, v) for (cx, cy), v in distances.items()):
                continue
            return x * 4_000_000 + y


if __name__ == "__main__":
    print(part1(2_000_000))
    print(part2(4_000_000))
