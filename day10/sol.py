def get_input():
    with open("input") as f:
        for x in f.read().splitlines():
            yield x


def stall(ins, t, pv, av):
    for _ in range(t):
        ins += [pv]
    return ins, pv + av


def get_instructions(data):
    ins = []
    v = 1
    for x in data:
        x = x.split(" ")
        if x[0] == "noop":
            ins, v = stall(ins, 1, v, 0)
        elif x[0] == "addx":
            ins, v = stall(ins, 2, v, int(x[1]))
    return ins


def part1():
    ins = get_instructions(get_input())
    return sum(map(lambda x: (x[0] + 1) * x[1], filter(lambda i: ((i[0] + 1) - 20) % 40 == 0, enumerate(ins))))


def part2():
    ins = get_instructions(get_input())
    screen = [["."] * 40 for _ in range(6)]
    CRT = 0
    for i in ins:
        y = CRT // 40
        x = CRT % 40
        if abs(i - x) <= 1:
            screen[y][x] = "#"
        CRT += 1
    return "\n".join(map(lambda x: "".join(x), screen))


if __name__ == "__main__":
    print(part1())
    print(part2())
