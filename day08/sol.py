from functools import reduce
import operator


def get_input():
    with open("input") as f:
        for x in f.read().splitlines():
            yield list(map(int, x))


def get_column(data, index):
    return [x[index] for x in data]


def get_sides(x, y, values):
    row = values[y]
    column = get_column(values, x)

    return [
        row[x - 1::-1] if x > 0 else [],
        row[x + 1:],
        column[y - 1::-1] if y > 0 else [],
        column[y + 1:]
    ]


def part1():
    def is_visible(x, y, data):
        curr = data[y][x]
        sides = get_sides(x, y, data)

        return any([max(x or [-1]) < curr for x in sides])

    data = list(get_input())
    return sum([is_visible(x, y, data) for y, _ in enumerate(data) for x, _ in enumerate(data[y])])


def part2():
    def count(l, curr):
        if not l:
            return 0
        for i, v in enumerate(l):
            if v >= curr:
                return i + 1
        return len(l)

    data = list(get_input())
    s = 0
    for y, _ in enumerate(data):
        for x, _ in enumerate(data[y]):
            curr = data[y][x]
            sides = get_sides(x, y, data)

            s = max(s, reduce(operator.mul, [count(x, curr) for x in sides]))
    return s


if __name__ == "__main__":
    print(part1())
    print(part2())
