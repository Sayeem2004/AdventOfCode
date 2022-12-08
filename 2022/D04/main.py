from io import FileIO


def main() -> None:
    fin: FileIO = open("input.in", "r")
    lines: list[str] = [line.strip() for line in fin.read().split("\n")[0:-1]]

    print("Part 1: " + str(part1(lines)))
    print("Part 2: " + str(part2(lines)))


def part1(lines: list[str]) -> int:
    cnt: int = 0

    for line in lines:
        split: list[str] = line.split(",")
        int1: list[int] = [int(i) for i in split[0].split("-")]
        int2: list[int] = [int(i) for i in split[1].split("-")]

        if (int1[0] <= int2[0] and int1[1] >= int2[1]):
            cnt += 1
        elif (int1[0] >= int2[0] and int1[1] <= int2[1]):
            cnt += 1

    return cnt


def part2(lines: list[str]) -> int:
    cnt: int = 0

    for line in lines:
        split: list[str] = line.split(",")
        int1: list[int] = [int(i) for i in split[0].split("-")]
        int2: list[int] = [int(i) for i in split[1].split("-")]

        if (int1[0] <= int2[0] and int2[0] <= int1[1]):
            cnt += 1
        elif (int1[0] >= int2[0] and int1[0] <= int2[1]):
            cnt += 1

    return cnt


main()
