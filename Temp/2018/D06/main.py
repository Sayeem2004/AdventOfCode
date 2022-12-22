from io import FileIO


def main() -> None:
    fin: FileIO = open("input.in", "r")
    lines: list[str] = [line.strip() for line in fin.read().split("\n")[0:-1]]

    print("Part 1: " + str(part1(lines)))
    print("Part 2: " + str(part2(lines)))


def parse(lines: list[str]) -> dict[(int, int), (int, int)]:
    minX: int = 1000000
    minY: int = 1000000
    maxX: int = 0
    maxY: int = 0

    for coord in lines:
        split: list[str] = coord.split(", ")
        x: int = int(split[0])
        y: int = int(split[1])

        minX = min(minX, x)
        minY = min(minY, y)
        maxX = max(maxX, x)
        maxY = max(maxY, y)

    closest: dict[(int, int), (int, int)] = {}

    for x in range(minX, maxX + 1):
        for y in range(minY, maxY + 1):
            closest[(x, y)] = (1000000, 1000000)

            for coord in lines:
                split: list[str] = coord.split(", ")
                cx: int = int(split[0])
                cy: int = int(split[1])

                curr: int = abs(cx - x) + abs(cy - y)
                prev: int = abs(closest[(x, y)][0] - x) + \
                    abs(closest[(x, y)][1] - y)

                if curr < prev:
                    closest[(x, y)] = (cx, cy)

    return closest


def part1(lines: list[str]) -> int:
    closest: dict[(int, int), (int, int)] = parse(lines)
    count: dict[(int, int), int] = {}

    for coord in closest:
        if closest[coord] not in count:
            count[closest[coord]] = 0

        count[closest[coord]] += 1

    return max(count.values())


def part2(lines: list[str]) -> int:
    return 0


main()
