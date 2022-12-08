from io import FileIO


def main() -> None:
    fin: FileIO = open("input.in", "r")
    lines: list[str] = [line.strip() for line in fin.read().split("\n")[0:-1]]

    print("Part 1: " + str(part1(lines)))
    print("Part 2: " + str(part2(lines)))


def part1(lines: list[str]) -> int:
    key1: str = "ABC"
    key2: str = "XYZ"
    cnt: int = 0

    for line in lines:
        val1: int = key1.index(line[0])
        val2: int = key2.index(line[2])
        dif: int = (val2 - val1)

        cnt += (val2 + 1)
        if (abs(dif) == 2):
            dif = dif * -1 // 2
        cnt += (dif + 1) * 3

    return cnt


def part2(lines: list[str]) -> int:
    key1: str = "ABC"
    key2: str = "XYZ"
    cnt: int = 0

    for line in lines:
        val1: int = key1.index(line[0])
        val2: int = key2.index(line[2])
        dif: int = (val2 - 1)

        cnt += val2 * 3
        cnt += (val1 + dif) % 3 + 1

    return cnt


main()
