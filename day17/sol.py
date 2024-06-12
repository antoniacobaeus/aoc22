def get_input():
    with open("input") as f:
        return f.read()


rocks = [
    [b"1111"],
    [b"0100", b"1110", b"0100"],
    [b"0010", b"0010", b"1110"],
    [b"1000", b"1000", b"1000", b"1000"],
    [b"1100", b"1100"],
]


def check_collision(rock, y, tower):
    # print("Rock:")
    # print_tower(rock)
    # print("Tower:")
    # print_tower(tower[y - (len(rock) - 1) : y + 1][::-1])
    for r, t in zip(rock, tower[y - (len(rock) - 1) : y + 1][::-1]):
        if r & t > 0:
            return True


def place(rock, y, tower):
    for i, r in enumerate(rock):
        tower[y - i] = tower[y - i] | r
    return tower


def _push(rock, y, index, pattern, tower):
    p = pattern[index % len(pattern)]
    # print(p)
    o_rock = rock

    match p:
        case "<":
            rock = [r * 2 for r in rock]
            if max(rock) > 2**6:
                return o_rock
        case ">":
            if any(r % 2 != 0 for r in rock):
                return o_rock
            rock = [r // 2 for r in rock]
        case _:
            pass
    if check_collision(rock, y, tower):
        return o_rock
    return rock


def step(t, pattern, tower, s):
    rock = rocks[t % len(rocks)]
    rock = [b"00" + r + b"0" for r in rock]  # padd rock
    rock = [int(r, 2) for r in rock]

    for _ in range(3 + len(rock)):
        tower.append(0)

    y = len(tower) - 1
    print_tower_and_rock(tower, y, rock)

    while True:
        # print(t, s)
        # push
        rock = _push(rock, y, s, pattern, tower)
        s += 1
        # fall
        y -= 1
        if check_collision(rock, y, tower):
            tower = place(rock, y + 1, tower)
            break
    return tower, s


def print_tower(tower):
    for t in tower[::-1]:
        for b in bin(t)[2:].zfill(7):
            print("#" if b == "1" else ".", end="")
        print()


def print_tower_and_rock(tower, y, rock):
    for r, t in zip(rock, tower[y - (len(rock) - 1) : y + 1][::-1]):
        r = bin(r)[2:].zfill(7)
        t = bin(t)[2:].zfill(7)

        for br, bt in zip(r, t):
            if bt == "1":
                print("#", end="")
            elif br == "1":
                print("r", end="")
            else:
                print(".", end="")
        print()

    print_tower(tower[: y - (len(rock) - 1)])


def solve(T):
    pattern = get_input()

    tower = [int(b"1111111", 2)]

    s = 0
    for t in range(T):
        tower, s = step(t, pattern, tower, s)
        # print_tower(tower)
        tower = list(filter(lambda row: row != 0, tower))

    return len(tower) - 1


if __name__ == "__main__":
    print(solve(11))
    # print(solve(1000_000_000_000))
