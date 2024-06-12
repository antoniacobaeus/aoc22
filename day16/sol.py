import re
import math
from copy import deepcopy


def get_input():
    valves, rates, neighbors = [], [], []

    pattern = r"Valve (\w+) has flow rate=(\d+); tunnels? leads? to valves? (.+)$"
    with open("input") as f:
        for line in f.readlines():
            m = re.findall(pattern, line.strip())[0]
            valve, rate, neighbor = m
            valves += [valve]
            rates += [int(rate)]
            if "," in neighbor:
                neighbors += [[n for n in neighbor.split(", ")]]
            else:
                neighbors += [[neighbor]]
    return valves, rates, neighbors


def edge_weights(valves, neighbors):
    w = [
        [0 if i == j else math.inf for j in range(len(valves))]
        for i in range(len(valves))
    ]

    for i, neighs in enumerate(neighbors):
        for n in neighs:
            w[i][valves.index(n)] = 1
            # w[valves.index(n)][i] = 1
    return w


def floyd_warshall(W, n):
    D = deepcopy(W)

    for k in range(n):
        for i in range(n):
            for j in range(n):
                D[i][j] = min(D[i][j], D[i][k] + D[k][j])
    return D


def solve(T, valves, rates, D, visited=set(), final=dict()):
    def traverse(t, valve_i, visited):
        best = 0, set()
        for i, v in enumerate(valves):
            if rates[i] <= 0 or i in visited:
                continue
            dist = D[valve_i][i]

            new_t = t - dist - 1  # open a valve

            if new_t > 0:
                next_flow, next_visit = traverse(new_t, i, visited | {i})

                best = max(
                    best,
                    (next_flow + rates[i] * new_t, next_visit | {i}),
                    key=lambda x: x[0],
                )

        return best

    return traverse(T, valves.index("AA"), visited)


def part1(T=30):
    valves, rates, neighbors = get_input()

    w = edge_weights(valves, neighbors)

    D = floyd_warshall(w, len(valves))

    return solve(T, valves, rates, (D))


def part2(T=26):
    valves, rates, neighbors = get_input()

    w = edge_weights(valves, neighbors)

    D = floyd_warshall(w, len(valves))

    flow_1, visited = solve(T, valves, rates, D)
    # return flow_1

    flow_2, _ = solve(T, valves, rates, D, visited)

    return flow_1 + flow_2


if __name__ == "__main__":
    import time

    s = time.perf_counter()
    print(f"Part1: {part1()}, in {time.perf_counter() - s}")

    s = time.perf_counter()
    print(f"Part2: {part2()}, in {time.perf_counter() - s}")
