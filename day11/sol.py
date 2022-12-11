def get_input():
    monkeys = []
    with open("input") as f:
        for x in f.read().split("\n\n"):
            lines = list(map(lambda line: line.strip(), x.split("\n")))
            items = lines[1].split(": ")[1].split(", ")
            operator, value = lines[2].split(" ")[-2:]
            divisable = lines[3].split(" ")[-1]
            throw_to_true = lines[4].split(" ")[-1]
            throw_to_false = lines[5].split(" ")[-1]

            monkey = {
                "items": list(map(int, items)),
                "op": operator,
                "value": value,
                "test": {
                    "divisable": int(divisable),
                    "true": int(throw_to_true),
                    "false": int(throw_to_false),
                },
            }
            monkeys.append(monkey)
    return monkeys


exec_op = {
    "*": lambda x, y: x * y,
    "+": lambda x, y: x + y,
}


def part1():
    monkeys = get_input()
    throws = [0] * len(monkeys)

    for i in range(20):
        for i, monkey in enumerate(monkeys):
            op, value = monkey["op"], monkey["value"]
            throws[i] += len(monkey["items"])

            while monkey["items"]:
                x = monkey["items"].pop(0)
                if value == "old":
                    worry = exec_op[op](x, x)
                else:
                    worry = exec_op[op](x, int(value))

                if (worry % monkey["test"]["divisable"]) == 0:
                    to = monkey["test"]["true"]
                else:
                    to = monkey["test"]["false"]

                monkeys[to]["items"].append(worry // 3)
    throws.sort()
    return throws[-1] * throws[-2]


def part2():
    monkeys = get_input()
    throws = [0] * len(monkeys)

    for i in range(10000):
        for i, monkey in enumerate(monkeys):
            op, value = monkey["op"], monkey["value"]
            throws[i] += len(monkey["items"])

            while monkey["items"]:
                x = monkey["items"].pop(0)
                if value == "old":
                    worry = exec_op[op](x, x)
                else:
                    worry = exec_op[op](x, int(value))

                if (worry % monkey["test"]["divisable"]) == 0:
                    to = monkey["test"]["true"]
                else:
                    to = monkey["test"]["false"]

                monkeys[to]["items"].append(
                    worry % (2 * 3 * 5 * 7 * 11 * 13 * 17 * 19 * 23))
    throws.sort()
    return throws[-1] * throws[-2]


if __name__ == "__main__":
    print(part1())
    print(part2())
