from io import FileIO


def main() -> None:
    fin: FileIO = open("input.in", "r")
    split: list[str] = [line for line in fin.read().split("\n\n")]
    diagram: list[str] = [line for line in split[0].split("\n")[:-1]]
    moves: list[str] = [line.strip() for line in split[1].split("\n")[:-1]]

    print("Part 1: " + part1(diagram, moves))
    print("Part 2: " + part2(diagram, moves))


def ind(i: int) -> int:
    return i//4 + 1


def part1(diagram: list[str], moves: list[str]) -> str:
    stack: dict[int, str] = {}

    for row in diagram:
        for i in range(1, len(row), 4):
            if (row[i] == ' '):
                continue
            if (ind(i) in stack):
                stack[ind(i)].append(row[i])
            else:
                stack[ind(i)] = [row[i]]

    for move in moves:
        move: list[str] = move.split(" ")
        mv: int = int(move[1])
        src: int = int(move[3])
        sin: int = int(move[5])

        for i in range(mv):
            if (len(stack[src]) != 0):
                stack[sin].insert(0, stack[src].pop(0))

    ret: str = ""
    for i in range(1, len(stack)+1):
        ret += stack[i][0]

    return ret


def part2(diagram: list[str], moves: list[str]) -> str:
    stack: dict[int, str] = {}

    for row in diagram:
        for i in range(1, len(row), 4):
            if (row[i] == ' '):
                continue
            if (ind(i) in stack):
                stack[ind(i)].append(row[i])
            else:
                stack[ind(i)] = [row[i]]

    for move in moves:
        move: list[str] = move.split(" ")
        mv: int = int(move[1])
        src: int = int(move[3])
        sin: int = int(move[5])

        pref: list[str] = stack[src][0:mv]
        stack[src]: list[str] = stack[src][mv:]
        stack[sin]: list[str] = pref + stack[sin]

    ret: str = ""
    for i in range(1, len(stack)+1):
        ret += stack[i][0]

    return ret


main()
