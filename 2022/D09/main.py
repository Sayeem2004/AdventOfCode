from io import FileIO


def main() -> None:
    fin: FileIO = open("input.in", "r")
    lines: list[str] = [line.strip() for line in fin.read().split("\n")[0:-1]]

    print("Part 1: " + str(part1(lines)))
    print("Part 2: " + str(part2(lines)))


def part1(lines: list[str]) -> int:
    moves: dict[str, list[int]] = {"U": [
        0, 1], "D": [0, -1], "L": [-1, 0], "R": [1, 0]}
    posT: list[int] = [0, 0]
    posH: list[int] = [0, 0]
    span: set[str] = set()
    span.add(str(posT))

    for line in lines:
        move: list[int] = moves[line[0]]
        num = int(line[2:])

        for _ in range(num):
            posH[0] += move[0]
            posH[1] += move[1]

            if abs(posH[0] - posT[0]) > 1 or abs(posH[1] - posT[1]) > 1:
                posT[0] = posH[0] - move[0]
                posT[1] = posH[1] - move[1]

            span.add(str(posT))

    return len(span)


def part2(lines: list[str]) -> int:
    moves: dict[str, list[int]] = {"U": [
        0, 1], "D": [0, -1], "L": [-1, 0], "R": [1, 0]}
    lt: list[list[int]] = {{0, 0}, {0, 0}, {0, 0}, {0, 0}, {0, 0}, {0, 0}, {0, 0}, {0, 0}, {0, 0}, {0, 0}}




main()
