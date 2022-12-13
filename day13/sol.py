from functools import cmp_to_key, reduce
from operator import mul


def get_input():
    with open("input") as f:
        for pair in f.read().split("\n\n"):
            yield [eval(x) for x in pair.split("\n")]


def compare(x, y):
    if x == y:
        return None
    if isinstance(x, list) and isinstance(y, list):
        if not x and y:
            return True
        if x and not y:
            return False

        res = compare(x[0], y[0])
        if res is not None:
            return res
        return compare(x[1:], y[1:])
    elif isinstance(x, list):
        return compare(x, [y])
    elif isinstance(y, list):
        return compare([x], y)
    else:
        if x == y:
            return None
        return x < y


def part1():
    s = 0
    for i, (l1, l2) in enumerate(get_input()):
        if compare(l1, l2):
            s += (i + 1)
    return s


def compare_to(x, y):
    res = compare(x, y)

    if res is None:
        return 0
    if res:
        return 1
    return -1


def part2():
    data = [x for y in get_input() for x in y]
    dividers = [[[2]], [[6]]]
    data.extend(dividers)
    data.sort(key=cmp_to_key(compare_to), reverse=True)
    return reduce(mul, map(lambda x: x[0] + 1, filter(lambda x: x[1] in dividers, enumerate(data))))


if __name__ == "__main__":
    print(part1())
    print(part2())
