from io import FileIO


def main() -> None:
    fin: FileIO = open("input.in", "r")
    lines: list[int] = [int(line.strip())
                        for line in fin.read()[0:-1].split(",")]

    print("Part 1: " + str(part1(lines)))
    print("Part 2: " + str(part2(lines)))


def part1(lines: list[int]) -> int:
    lines[1]: int = 12
    lines[2]: int = 2
    i: int = 0

    while i < len(lines):
        if (lines[i] == 99):
            break

        if (lines[i] == 1):
            lines[lines[i + 3]] = lines[lines[i + 1]] + lines[lines[i + 2]]

        if (lines[i] == 2):
            lines[lines[i + 3]] = lines[lines[i + 1]] * lines[lines[i + 2]]

        i += 4

    return lines[0]


def part2(lines: list[str]) -> int:
    ans: int = 19690720

    for noun in range(100):
        for verb in range(100):
            lines[1]: int = noun
            lines[2]: int = verb
            i: int = 0

            while i < len(lines):
                if (lines[i] == 99):
                    break


                if (lines[i] == 1 and i + 3 < len(lines)):
                    if lines[i + 1] >= len(lines):
                        continue
                    if lines[i + 2] >= len(lines):
                        continue
                    if lines[i + 3] >= len(lines):
                        continue

                    lines[lines[i + 3]] = lines[lines[i + 1]] + \
                        lines[lines[i + 2]]

                if (lines[i] == 2 and i + 3 < len(lines)):
                    if lines[i + 1] >= len(lines):
                        continue
                    if lines[i + 2] >= len(lines):
                        continue
                    if lines[i + 3] >= len(lines):
                        continue

                    lines[lines[i + 3]] = lines[lines[i + 1]] * \
                        lines[lines[i + 2]]

                i += 4

            if (lines[0] == ans):
                return 100 * noun + verb

    return -1


main()
