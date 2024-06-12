import re
from functools import cache


def get_input():
    pattern = r"(\w+): (\w+[^\+|\/|\*|\-]) (\+|\/|\*|\-) (\w+)"
    pattern_num = r"(\w+): (\d+)"

    jobs = {}
    with open("input") as f:
        for line in f.readlines():
            if re.match(pattern, line.strip()):
                m = re.findall(pattern, line.strip())[0]
                jobs[m[0]] = m[1:]
            elif re.match(pattern_num, line.strip()):
                m = re.findall(pattern_num, line.strip())[0]
                jobs[m[0]] = int(m[1])
    return jobs


def traverse(start_job, jobs):
    op = {
        "+": lambda x, y: x + y,
        "*": lambda x, y: x * y,
        "/": lambda x, y: x // y,
        "-": lambda x, y: x - y,
    }

    def inner(job):
        if isinstance(job, int):
            return job
        elif job is None:
            return None
        else:
            left = inner(jobs[job[0]])
            right = inner(jobs[job[2]])

            if left is None or right is None:
                return None

            return op[job[1]](left, right)

    return inner(start_job)


def build(start_value, start_job, jobs):
    reverse_op = {
        "+": lambda x, y: x - y,
        "*": lambda x, y: x // y,
        "/": lambda x, y: x * y,
        "-": lambda x, y: x + y,
        "=": lambda _x, y: y,
    }

    @cache
    def inner(value, job):
        if job is None:
            return value
        else:
            left_branch = jobs[job[0]]
            right_branch = jobs[job[2]]

            left = traverse(left_branch, jobs)
            right = traverse(right_branch, jobs)

            if left is None:
                return inner(reverse_op[job[1]](value, right), left_branch)
            else:
                if job[1] == "-":  # sicko mode edge case
                    return inner(reverse_op["+"](left, value), right_branch)
                return inner(reverse_op[job[1]](value, left), right_branch)

    return inner(start_value, start_job)


def part1():
    jobs = get_input()

    return traverse(jobs["root"], jobs)


def part2():
    jobs = get_input()

    jobs["humn"] = None
    jobs["root"] = (jobs["root"][0], "=", jobs["root"][2])
    # 8764479278265
    # 8764479278274.196
    return build(0, jobs["root"], jobs)


if __name__ == "__main__":
    import time

    s = time.perf_counter()
    print(f"Part1: {part1()}, in {time.perf_counter() - s}")

    s = time.perf_counter()
    print(f"Part2: {part2()}, in {time.perf_counter() - s}")
