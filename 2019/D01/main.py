from io import FileIO


def main() -> None:
    fin: FileIO = open("input.in", "r")
    lines: list[str] = [line.strip() for line in fin.read().split("\n")[0:-1]]

    print("Part 1: " + str(part1(lines)))
    print("Part 2: " + str(part2(lines)))


def part1(lines: list[str]) -> int:
    cnt: int = 0

    for line in lines:
        cnt += int(line)//3 - 2

    return cnt


def part2(lines: list[str]) -> int:
    cnt: int = 0

    for line in lines:
        curr = int(line)//3 - 2

        while curr > 0:
            cnt += curr
            curr = curr//3 - 2

    return cnt


main()
