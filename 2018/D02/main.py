from io import FileIO


def main() -> None:
    fin: FileIO = open("input.in", "r")
    lines: list[str] = [line.strip() for line in fin.read().split("\n")[0:-1]]

    print("Part 1: " + str(part1(lines)))
    print("Part 2: " + part2(lines))


def part1(lines: list[str]) -> int:
    cnt2: int = 0
    cnt3: int = 0

    for line in lines:
        dt: dict[str, int] = {}

        for c in line:
            if (c in dt):
                dt[c] += 1
            else:
                dt[c] = 1

        if (2 in dt.values()):
            cnt2 += 1

        if (3 in dt.values()):
            cnt3 += 1

    return cnt2 * cnt3


def part2(lines: list[str]) -> str:
    def diff(a: str, b: str) -> int:
        ret: int = 0

        for i in range(len(a)):
            if (a[i] != b[i]):
                ret += 1

        return ret

    def common(a: str, b: str) -> str:
        ret: str = ""

        for i in range(len(a)):
            if (a[i] == b[i]):
                ret += a[i]

        return ret

    for i in range(len(lines)):
        for j in range(i + 1, len(lines)):
            if (diff(lines[i], lines[j]) == 1):
                return common(lines[i], lines[j])

    return -1


main()
