def get_input():
    with open("input") as f:
        return f.read().splitlines()


def construct_tree():
    tree = {"size": 0, "children": {}, "parent": None}
    curr = tree

    for x in get_input():
        x = x.split(" ")

        if x[0] == "$":
            if x[1] == "cd":
                if x[2] == "/":
                    curr = tree
                elif x[2] == "..":
                    curr = curr["parent"]
                else:
                    curr = curr["children"][x[2]]
        elif x[0] == "dir":
            this = {"size": 0, "children": {}, "parent": curr}
            curr["children"][x[1]] = this
        else:
            curr["size"] += int(x[0])
    return tree


def total(node):
    return sum(total(child) for child in node["children"].values()) + node["size"]


def part1():
    root = construct_tree()

    def calc(node):
        max_size = 100000
        s = 0
        for x in node["children"].values():
            size = total(x)
            if size <= max_size:
                s += size
            s += calc(x)
        return s
    return calc(root)


min_disk_size = 70000000


def part2():
    avail_space = 70000000
    required_space = 30000000

    root = construct_tree()

    used_space = total(root)
    needed_space = required_space - (avail_space - used_space)

    def calc(node, needed_space):
        size = sum(calc(child, needed_space)
                   for child in node["children"].values()) + node["size"]
        if size >= needed_space:
            global min_disk_size
            min_disk_size = min(size, min_disk_size)
        return size
    calc(root, needed_space)
    return min_disk_size


if __name__ == "__main__":
    print(part1())
    print(part2())
