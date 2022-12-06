def get_input():
    with open("input") as f:
        return f.read()


def part1():
    for i in range(len(get_input())):
        if len(set(get_input()[i:i+4])) == 4:
            return i + 4


def part2():
    for i in range(len(get_input())):
        if len(set(get_input()[i:i+14])) == 14:
            return i + 14


if __name__ == "__main__":
    print(part1())
    print(part2())
