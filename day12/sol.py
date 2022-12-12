def alfabet_to_height(letter):
    if letter == "S":
        letter = 'a'
    elif letter == "E":
        letter = 'z'
    return ord(letter) - ord('a')


def construct_grid(grid):
    start = None
    end = None
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == 'S':
                start = (x, y)
            elif grid[y][x] == 'E':
                end = (x, y)
            grid[y][x] = alfabet_to_height(grid[y][x])
    return start, end, grid


def get_input():
    with open("input") as f:
        grid = []
        for line in f.readlines():
            grid += [[x for x in line.strip()]]
        return construct_grid(grid)


def get_neighbours(current, grid, rev=False):
    cx, cy = current
    ch = grid[cy][cx]
    for x, y in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        if 0 <= cx + x < len(grid[0]) and 0 <= cy + y < len(grid):
            if (not rev and grid[cy + y][cx + x] - ch <= 1) \
                    or (rev and ch - grid[cy + y][cx + x] <= 1):
                yield (cx + x, cy + y)


def bfs(start, is_end, grid, down=False):
    queue = [(start, 0)]
    visited = set()
    while queue:
        current, dist = queue.pop(0)
        if is_end(*current):
            return dist
        if current in visited:
            continue
        visited.add(current)
        for neighbour in get_neighbours(current, grid, down):
            queue.append((neighbour, dist + 1))
    return -1


def part1():
    start, end, grid = get_input()
    def is_end(x, y): return (x, y) == end
    return bfs(start, is_end, grid)


def part2():
    start, end, grid = get_input()
    def is_end(x, y): return grid[y][x] == grid[start[1]][start[0]]
    return bfs(end, is_end, grid, True)


if __name__ == "__main__":
    print(part1())
    print(part2())
