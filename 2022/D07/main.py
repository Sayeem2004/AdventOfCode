from io import FileIO
from typing import Callable
from classes import File, Dir


def main() -> None:
    fin: FileIO = open("input.in", "r")
    lines: list[str] = [line.strip() for line in fin.read().split("\n")[0:-1]]

    print("Part 1: " + str(part1(lines)))
    print("Part 2: " + str(part2(lines)))


def parse(lines: list[str]) -> Dir:
    root: Dir = Dir.from_name("/")
    curr: Dir = root

    for line in lines[1:]:
        if (line[:3] == "dir"):
            name: str = line[4:]
            curr.add(Dir.from_parent(name, curr))

        elif (line[:4] == "$ ls"):
            continue

        elif (line[:5] == "$ cd "):
            name: str = line[5:]
            curr = curr.get(name)

        else:
            split: list[str] = line.split(" ")
            size: int = int(split[0])
            name: str = split[1]

            curr.add(File(name, size, curr))

    return root


def part1(lines: list[str]) -> int:
    root: Dir = parse(lines)

    def sum_satisfy(path: Dir | File, func: Callable[[File | Dir], bool]) -> int:
        ret: int = path.size() if func(path) else 0

        if (type(path) == Dir):
            ret += sum(sum_satisfy(child, func)
                        for child in path.children().values())

        return ret

    def func(path: File | Dir) -> bool:
        if (type(path) == File):
            return False

        return (path.size() <= 100000)

    return sum_satisfy(root, func)


def part2(lines: list[str]) -> int:
    root: Dir = parse(lines)
    min_size: int = root.size() - 40000000

    def find_satisfy(path: Dir | File, func: Callable[[File | Dir], bool]) -> int:
        ret: list[int] = [path.size()] if func(path) else []

        if (type(path) == Dir):
            ret += [find_satisfy(child, func)
                    for child in path.children().values()]

        return min(ret) if ret != [] else 1000000000000

    def func(path: File | Dir) -> bool:
        if (type(path) == File):
            return False

        return (path.size() >= min_size)

    return find_satisfy(root, func)


main()
