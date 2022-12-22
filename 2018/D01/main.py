from io import FileIO


def main() -> None:
    fin: FileIO = open("input.in", "r")
    lines: list[str] = [line.strip() for line in fin.read().split("\n")[0:-1]]

    print("Part 1: " + str(part1(lines)))
    print("Part 2: " + str(part2(lines)))


def part1(lines: list[str]) -> int:
    ret: int = 0

    for line in lines:
        ret = eval(str(ret) + line)

    return ret


def part2(lines: list[str]) -> int:
    dt: dict[int, bool] = {}
    curr: int = 0
    dt[curr] = True

    while True:
        for line in lines:
            curr = eval(str(curr) + line)

            if (curr in dt):
                return curr

            dt[curr] = True


main()
