from io import FileIO


def main() -> None:
    fin: FileIO = open("input.in", "r")
    lines: list[str] = [line.strip()
                        for line in fin.read()[0:-1].split("\n\n")]

    print("Part 1: " + str(part1(lines)))
    print("Part 2: " + str(part2(lines)))


def part1(lines: list[str]) -> int:
    mx: int = 0

    for inv in lines:
        cnt: int = 0

        for num in inv.split("\n"):
            cnt += int(num)

        mx = max(mx, cnt)

    return mx


def part2(lines: list[str]) -> int:
    lt: list[int] = []

    for inv in lines:
        cnt: int = 0

        for num in inv.split("\n"):
            cnt += int(num)

        lt.append(cnt)

    lt.sort()
    return lt[-1] + lt[-2] + lt[-3]


main()
