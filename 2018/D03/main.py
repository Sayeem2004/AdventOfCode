from io import FileIO


def main() -> None:
    fin: FileIO = open("input.in", "r")
    lines: list[str] = [line.strip() for line in fin.read().split("\n")[0:-1]]

    print("Part 1: " + str(part1(lines)))
    print("Part 2: " + str(part2(lines)))


def parse(lines: list[str]) -> dict[(int, int), int]:
    dct: dict[(int, int), int] = {}

    for line in lines:
        split: list[str] = line.split(" ")
        tlx: int = int(split[2][:-1].split(",")[0])
        tly: int = int(split[2][:-1].split(",")[1])
        wid: int = int(split[3].split("x")[0])
        hei: int = int(split[3].split("x")[1])

        for i in range(tlx, tlx + wid):
            for j in range(tly, tly + hei):
                if ((i, j) in dct):
                    dct[(i, j)] += 1
                else:
                    dct[(i, j)] = 1

    return dct


def part1(lines: list[str]) -> int:
    dct: dict[(int, int), int] = parse(lines)
    ret: int = sum([1 for v in dct.values() if v > 1])
    return ret


def part2(lines: list[str]) -> int:
    dct: dict[(int, int), int] = parse(lines)

    for line in lines:
        split: list[str] = line.split(" ")
        tlx: int = int(split[2][:-1].split(",")[0])
        tly: int = int(split[2][:-1].split(",")[1])
        wid: int = int(split[3].split("x")[0])
        hei: int = int(split[3].split("x")[1])
        br: bool = False

        for i in range(tlx, tlx + wid):
            for j in range(tly, tly + hei):
                if (dct[(i, j)] > 1):
                    br = True
                    break

        if (not br):
            return int(split[0][1:])

    return -1


main()
