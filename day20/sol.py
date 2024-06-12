def get_input():
    with open("input") as f:
        return list(map(int, f.read().splitlines()))


def mix(f, f_c):
    for i, n in enumerate(f):
        j = f_c.index((i, n))
        if n > 0:
            # move list so it starts at j
            f_c = f_c[j:] + f_c[:j]
            j = 0
            step = n % (len(f_c) - 1)
        elif n < 0:
            # move list so it ends at j
            f_c = f_c[j + 1 :] + f_c[: j + 1]
            j = len(f_c) - 1
            step = -(abs(n) % (len(f_c) - 1))
        else:
            continue

        assert f_c[j] == (i, n)

        # move element at j the number of steps
        f_c.remove((i, n))
        f_c.insert(j + step, (i, n))
    return f_c


def calc_grove(f_c):
    f = [m for _, m in f_c]
    zero = f.index(0)

    return sum(f[(zero + i) % len(f)] for i in [1000, 2000, 3000])


def part1():
    f = get_input()
    f_c = [x for x in enumerate(f)]

    return calc_grove(mix(f, f_c))


def part2():
    f = [i * 811589153 for i in get_input()]
    f_c = [x for x in enumerate(f)]

    for _ in range(10):
        f_c = mix(f, f_c)
    return calc_grove(f_c)


if __name__ == "__main__":
    import time

    s = time.perf_counter()
    print(f"Part1: {part1()}, in {time.perf_counter() - s}")

    s = time.perf_counter()
    print(f"Part2: {part2()}, in {time.perf_counter() - s}")
