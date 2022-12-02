def get_input():
    with open("input") as f:
        for line in f.readlines():
            yield line.strip().split(" ")


O = ['A', 'B', 'C']
P = ['X', 'Y', 'Z']


def part1():
    s = 0
    for A, X in get_input():
        Oi = O.index(A)
        Pi = P.index(X)

        if Oi == Pi:
            s += 3 + (Pi + 1)
        elif Oi == (Pi - 1) % 3:
            s += 6 + (Pi + 1)
        else:
            s += 0 + (Pi + 1)
    return s


def part2():
    s = 0
    for A, X in get_input():
        Oi = O.index(A)
        Pi = P.index(X)

        if Pi == 1:
            s += 3 + (Oi + 1)
        elif Pi == 2:
            s += 6 + ((Oi + 1) % 3) + 1
        else:
            s += 0 + ((Oi - 1) % 3) + 1
    return s


if __name__ == "__main__":
    print(part1())
    print(part2())
