def get_input():
    with open("input") as f:
        return [x.strip() for x in f.readlines()]


def part1():
    c = []
    for A, B in map(lambda x: (x[:len(x)//2], x[len(x)//2:]), get_input()):
        a = list(set(A).intersection(set(B)))[0]
        c.append(ord(a) - 96 if a.islower() else ord(a) - 38)
    return sum(c)


def part2():
    c = []
    for A, B, C in zip(*[iter(get_input())] * 3):
        a = list(set(A).intersection(set(B)).intersection(set(C)))[0]
        c.append(ord(a) - 96 if a.islower() else ord(a) - 38)
    return sum(c)


if __name__ == "__main__":
    print(part1())
    print(part2())
