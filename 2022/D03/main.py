from io import FileIO


def main() -> None:
    fin: FileIO = open("input.in", "r")
    lines: list[str] = [line.strip() for line in fin.read().split("\n")[0:-1]]

    print("Part 1: " + str(part1(lines)))
    print("Part 2: " + str(part2(lines)))


def part1(lines: list[str]) -> int:
    cnt: int = 0

    for line in lines:
        fir: str = line[:len(line)//2]
        sec: str = line[len(line)//2:]

        for c in fir:
            if (c in sec):
                if (c.islower()):
                    cnt += ord(c) - ord("a") + 1
                else:
                    cnt += ord(c) - ord("A") + 27
                break

    return cnt


def part2(lines: list[str]) -> int:
    cnt: int = 0

    for i in range(0, len(lines), 3):
        for c in lines[i]:
            if ((c in lines[i+1]) and (c in lines[i+2])):
                if (c.islower()):
                    cnt += ord(c) - ord("a") + 1
                else:
                    cnt += ord(c) - ord("A") + 27
                break

    return cnt


main()
