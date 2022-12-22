from io import FileIO


def main() -> None:
    fin: FileIO = open("input.in", "r")
    polymer: str = fin.read()[:-1].strip()

    print("Part 1: " + str(part1(polymer)))
    print("Part 2: " + str(part2(polymer)))


def part1(polymer: str) -> int:
    i: int = 0

    while i < len(polymer) - 1:
        if polymer[i].lower() == polymer[i + 1].lower() and polymer[i] != polymer[i + 1]:
            polymer = polymer[:i] + polymer[i + 2:]
            i = max(0, i - 1)
        else:
            i += 1

    return len(polymer)


def part2(polymer: str) -> int:
    min_length: int = len(polymer)

    for c in "abcdefghijklmnopqrstuvwxyz":
        copy = polymer
        copy = copy.replace(c, "").replace(c.upper(), "")
        min_length = min(min_length, part1(copy))

    return min_length


main()
