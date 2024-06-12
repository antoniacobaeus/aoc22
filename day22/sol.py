import re
from enum import Enum
from math import sqrt


class MazeTile(Enum):
    OUTSIDE = 0
    WALL = 1
    EMPTY = 2

    def __repr__(self) -> str:
        match self:
            case MazeTile.OUTSIDE:
                return " "
            case MazeTile.WALL:
                return "#"
            case MazeTile.EMPTY:
                return "."
            case _:
                raise ValueError("Invalid MazeTile")


def get_input():
    symbols = {
        "#": MazeTile.WALL,
        ".": MazeTile.EMPTY,
        " ": MazeTile.OUTSIDE,
    }

    maze = []
    with open("input") as f:
        maze_string, instructions = f.read().split("\n\n")

        for line in maze_string.splitlines():
            maze.append([symbols[c] for c in line])

        max_length = max(map(len, maze))
        for line in maze:
            line.extend([MazeTile.OUTSIDE] * (max_length - len(line)))

        return maze, re.split(r"(R|L)", instructions)


class Facing(Enum):
    RIGHT = 0
    DOWN = 1
    LEFT = 2
    UP = 3

    def __repr__(self) -> str:
        match self:
            case Facing.RIGHT:
                return ">"
            case Facing.DOWN:
                return "v"
            case Facing.LEFT:
                return "<"
            case Facing.UP:
                return "^"

    def opposite(self) -> "Facing":
        match self:
            case Facing.RIGHT:
                return Facing.LEFT
            case Facing.DOWN:
                return Facing.UP
            case Facing.LEFT:
                return Facing.RIGHT
            case Facing.UP:
                return Facing.DOWN


def _move(x, y, facing: Facing) -> (int, int):
    match facing:
        case Facing.RIGHT:
            return x + 1, y
        case Facing.DOWN:
            return x, y + 1
        case Facing.LEFT:
            return x - 1, y
        case Facing.UP:
            return x, y - 1


def check_bounds(x, y, r, cube):
    def bounds(x, y, min_x, min_y, max_x, max_y):
        return x < min_x or y < min_y or x >= max_x or y >= max_y

    side = get_side(x, y, r, cube)

    if not side is None:
        _, (cx, cy) = cube[side]
        min_x, max_x = r * cx, r * (cx + 1)
        min_y, max_y = r * cy, r * (cy + 1)
        sx = x - min_x
        sy = y - min_y

        return bounds(sx, sy, min_x, min_y, max_x, max_y)
    else:
        return bounds(x, y, 0, 0, r, r)


def move(x, y, facing: Facing, r, steps, maze, wrap, cube, path):
    path[y][x] = facing

    for _ in range(steps):
        ox, oy = x, y
        x, y = _move(x, y, facing)
        # print_maze_with_path(maze, x, y, facing, path)

        if check_bounds(x, y, r, cube) or maze[y][x] == MazeTile.OUTSIDE:
            tx, ty, facing = wrap(x, y, facing, r, cube)

            while maze[ty][tx] == MazeTile.OUTSIDE:
                tx, ty = _move(tx, ty, facing)
            x, y = tx, ty
            # print_maze_with_path(maze, x, y, facing, path)

        if maze[y][x] == MazeTile.WALL:
            return (ox, oy, facing)
        else:
            path[y][x] = facing
    return x, y, facing


def execute(instruction, x, y, facing: Facing, r, maze, wrap, cube, path):
    if instruction == "R":
        return (
            x,
            y,
            Facing(facing.value + 1)
            if facing.value < len(Facing) - 1
            else Facing.RIGHT,
        )
    elif instruction == "L":
        return (
            x,
            y,
            Facing(facing.value - 1) if facing.value > 0 else Facing.UP,
        )
    else:
        return move(x, y, facing, r, int(instruction), maze, wrap, cube, path)


def print_maze(maze, x, y, facing):
    for i, line in enumerate(maze):
        if i == y:
            print("".join(map(lambda x: repr(x), line[:x])), end="")
            print(repr(facing), end="")
            print("".join(map(lambda x: repr(x), line[x + 1 :])))
        else:
            print("".join(map(lambda x: repr(x), line)))
    print()


def print_maze_with_path(maze, x, y, facing, path):
    for ix in range(len(maze)):
        for iy in range(len(maze[0])):
            if ix == y and iy == x:
                # print(repr(facing), end="")
                print("B", end="")
            elif path[ix][iy] is not None:
                print(repr(path[ix][iy]), end="")
            else:
                print(repr(maze[ix][iy]), end="")
        print()
    print()


def calc_password(column, row, facing):
    return (row + 1) * 1000 + 4 * (column + 1) + facing.value


def part1():
    maze, instructions = get_input()

    column = maze[0].index(MazeTile.EMPTY)
    row = 0
    facing = Facing.RIGHT

    path = [[None] * len(maze[0]) for _ in maze]

    # print(maze, instructions, column, row)

    def wrap(x, y, facing: Facing, r, cube) -> (int, int):
        match facing:
            case Facing.RIGHT:
                return 0, y, facing
            case Facing.DOWN:
                return x, 0, facing
            case Facing.LEFT:
                return r - 1, y, facing
            case Facing.UP:
                return x, r - 1, facing

    for instruction in instructions:
        # print_maze_with_path(maze, column, row, facing, path)
        column, row, facing = execute(
            instruction, column, row, facing, len(maze), maze, wrap, None, path
        )
    print_maze_with_path(maze, column, row, facing, path)
    return calc_password(column, row, facing)


def example_cube():
    return [
        ((6, 4, 3, 2), (2, 0)),
        ((3, 5, 6, 1), (0, 1)),
        ((4, 5, 2, 1), (1, 1)),
        ((6, 5, 3, 1), (2, 1)),
        ((6, 2, 3, 4), (2, 2)),
        ((1, 2, 5, 4), (3, 2)),
    ], 4


def real_cube():
    return [
        ((2, 3, 4, 6), (1, 0)),
        ((5, 3, 1, 6), (2, 0)),
        ((2, 5, 4, 1), (1, 1)),
        ((5, 6, 1, 3), (0, 2)),
        ((2, 6, 4, 3), (1, 2)),
        ((5, 2, 1, 4), (0, 3)),
    ], 50


def get_side(x, y, r, cube):
    nx, ny = x // r, y // r

    for side, (_, coord) in enumerate(cube):
        if coord == (nx, ny):
            return side
    return None


def transform_coords(x, y, to_facing: Facing, from_facing: Facing, r):
    nx = x % r
    ny = y % r
    nr = r - 1

    operations = {
        (Facing.RIGHT, Facing.RIGHT): (nr, nr - ny),
        (Facing.RIGHT, Facing.DOWN): (ny, nr),
        (Facing.RIGHT, Facing.LEFT): (0, ny),
        (Facing.RIGHT, Facing.UP): (nr - ny, 0),
        (Facing.DOWN, Facing.RIGHT): (nr, nx),
        (Facing.DOWN, Facing.DOWN): (nr - nx, nr),
        (Facing.DOWN, Facing.LEFT): (0, nr - nx),
        (Facing.DOWN, Facing.UP): (nx, 0),
        (Facing.LEFT, Facing.RIGHT): (nr, ny),
        (Facing.LEFT, Facing.DOWN): (nr - ny, nr),
        (Facing.LEFT, Facing.LEFT): (0, nr - ny),
        (Facing.LEFT, Facing.UP): (ny, 0),
        (Facing.UP, Facing.RIGHT): (nr, nx),
        (Facing.UP, Facing.DOWN): (nx, nr),
        (Facing.UP, Facing.LEFT): (0, nx),
        (Facing.UP, Facing.UP): (nr - nx, 0),
    }

    return operations[(to_facing, from_facing)]


def part2():
    maze, instructions = get_input()

    path = [[None] * len(maze[0]) for _ in maze]

    column = maze[0].index(MazeTile.EMPTY)
    row = 0
    facing = Facing.RIGHT

    cube, r = real_cube()

    def wrap(x, y, facing: Facing, r, cube):
        from_side = get_side(*_move(x, y, facing.opposite()), r, cube)
        new_side = cube[from_side][0][facing.value] - 1

        new_dirs, coord = cube[new_side]
        from_facing = Facing(new_dirs.index(from_side + 1))

        new_x, new_y = transform_coords(x, y, facing, from_facing, r)

        return (
            (r * coord[0]) + new_x,
            (r * coord[1]) + new_y,
            from_facing.opposite(),
        )

    for instruction in instructions:
        # print_maze_with_path(maze, column, row, facing, path)
        column, row, facing = execute(
            instruction, column, row, facing, r, maze, wrap, cube, path
        )
    print_maze_with_path(maze, column, row, facing, path)
    return calc_password(column, row, facing)


if __name__ == "__main__":
    import time

    # s = time.perf_counter()
    # print(f"Part1: {part1()}, in {time.perf_counter() - s}")

    s = time.perf_counter()
    print(f"Part2: {part2()}, in {time.perf_counter() - s}")
