def get_input():
    with open("input") as f:
        layout, instructions = f.read().split("\n\n")
        rows = []
        for line in layout.split("\n")[:-1]:
            rows.append([line[i:i+4].strip()
                         for i in range(0, len(line), 4)])
        columns = []
        for i in range(len(rows[0])):
            columns.append([row[i][1] for row in rows if row[i] != ""])

        moves = []
        for line in instructions.split("\n"):
            moves.append([int(c)
                         for c in line.strip().split(" ") if c.isdigit()])
        return columns, moves


def part1():
    columns, moves = get_input()
    for (c, f, t) in moves:
        f = f - 1
        t = t - 1
        columns[t] = columns[f][:c][::-1] + columns[t]
        columns[f] = columns[f][c:]
    return "".join([c[0] for c in columns])


def part2():
    columns, moves = get_input()
    for (c, f, t) in moves:
        f = f - 1
        t = t - 1
        columns[t] = columns[f][:c] + columns[t]
        columns[f] = columns[f][c:]
    return "".join([c[0] for c in columns])


if __name__ == "__main__":
    print(part1())
    print(part2())
