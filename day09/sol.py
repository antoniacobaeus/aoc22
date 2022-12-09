def get_input():
    with open("input") as f:
        for x in f.read().splitlines():
            yield x.split(" ")[0], int(x.split(" ")[1])


def move(pos, dir):
    if dir == "R":
        return pos[0] + 1, pos[1]
    elif dir == "L":
        return pos[0] - 1, pos[1]
    elif dir == "U":
        return pos[0], pos[1] + 1
    elif dir == "D":
        return pos[0], pos[1] - 1


def move_towards(pos, target):
    if not (abs(target[0] - pos[0]) >= 2 or abs(target[1] - pos[1]) >= 2):
        return pos

    if pos[0] > target[0] and pos[1] > target[1]:
        return move(move(pos, "L"), "D")
    elif pos[0] > target[0] and pos[1] < target[1]:
        return move(move(pos, "L"), "U")
    elif pos[0] < target[0] and pos[1] > target[1]:
        return move(move(pos, "R"), "D")
    elif pos[0] < target[0] and pos[1] < target[1]:
        return move(move(pos, "R"), "U")
    elif pos[0] > target[0]:
        return move(pos, "L")
    elif pos[0] < target[0]:
        return move(pos, "R")
    elif pos[1] > target[1]:
        return move(pos, "D")
    elif pos[1] < target[1]:
        return move(pos, "U")


def part1():
    S = 0, 0
    H = S
    T = S
    visited = set()
    for dir, val in get_input():
        for _ in range(val):
            H = move(H, dir)

            T = move_towards(T, H)
            visited.add(T)
    return len(visited)


def part2():
    S = 0, 0
    H = S
    Ts = [S] * 9

    visited = set()
    for dir, val in get_input():
        for _ in range(val):
            H = move(H, dir)
            last = H
            for i, T in enumerate(Ts):
                T = move_towards(T, last)
                Ts[i] = T
                last = T
            visited.add(last)
    return len(visited)


if __name__ == "__main__":
    print(part1())
    print(part2())
