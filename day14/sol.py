def get_input():
    with open("input") as f:
        for line in f.readlines():
            yield [(int(x), int(y)) for x, y in map(lambda c: c.split(","), line.strip().split(" -> "))]


def line_from_to(px, py, x, y):
    if x == px:
        for i in range(py, y+1) or range(y, py+1):
            yield x, i
    elif y == py:
        for i in range(x, px+1) or range(px, x+1):
            yield i, y


def parse_rocks(data):
    rocks = {}

    for line in data:
        px, py = line[0]
        for x, y in line[1:]:
            for rx, ry in line_from_to(px, py, x, y):
                rocks[rx, ry] = "#"
            px, py = x, y
    return rocks


def fall(x, y, rocks, floor_y):
    if y + 1 == floor_y:
        return x, y
    for dx, dy in [(0, 1), (-1, 1), (1, 1)]:
        if (x + dx, y + dy) not in rocks:
            return fall(x + dx, y + dy, rocks, floor_y)
    return x, y


def falling_sand(rocks, start, max_y, floor=False):
    x, y = start

    next = fall(x, y, rocks, max_y + 2)

    if not next:
        return False
    if not floor and next[1] > max_y:
        return False
    if floor and start in rocks:
        return False
    rocks[next] = "o"
    return True


def part1():
    rocks = parse_rocks(get_input())
    s = 0
    max_y = max(y for _, y in rocks)
    while True:
        if not falling_sand(rocks, (500, 0), max_y, False):
            break
        s += 1
    return s


def part2():
    rocks = parse_rocks(get_input())
    s = 0
    max_y = max(y for _, y in rocks)
    while True:
        if not falling_sand(rocks, (500, 0), max_y, True):
            break
        s += 1
    return s


if __name__ == "__main__":
    print(part1())
    print(part2())
