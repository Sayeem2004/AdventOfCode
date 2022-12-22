from io import FileIO


def main() -> None:
    fin: FileIO = open("input.in", "r")
    lines: list[str] = [line.strip() for line in fin.read().split("\n")[0:-1]]

    print("Part 1: " + str(part1(lines)))
    print("Part 2: " + str(part2(lines)))


def part1(lines: list[str]) -> int:
    my: int = len(lines)
    mx: int = len(lines[0])
    visible: list[list[bool]] = [[False for _ in range(mx)] for _ in range(my)]

    for y in range(1, my-1):
        for x in range(1, mx-1):
            top_max: int = int(lines[0][x])
            bot_max: int = int(lines[my-1][x])
            lft_max: int = int(lines[y][0])
            rgt_max: int = int(lines[y][mx-1])

            for i in range(0, y):
                top_max = max(top_max, int(lines[i][x]))

            for i in range(y+1, my):
                bot_max = max(bot_max, int(lines[i][x]))

            for i in range(0, x):
                lft_max = max(lft_max, int(lines[y][i]))

            for i in range(x+1, mx):
                rgt_max = max(rgt_max, int(lines[y][i]))

            check: bool = False
            check |= (top_max < int(lines[y][x]))
            check |= (bot_max < int(lines[y][x]))
            check |= (lft_max < int(lines[y][x]))
            check |= (rgt_max < int(lines[y][x]))

            visible[y][x] = check

    ret: int = 2 * my + 2 * (mx - 2)
    ret += sum([sum([1 if visible[y][x] else 0 for x in range(mx)])
                for y in range(my)])
    return ret


def part2(lines: list[str]) -> int:
    my: int = len(lines)
    mx: int = len(lines[0])
    max_product: int = 0

    for y in range(0, my):
        for x in range(0, mx):
            val: int = int(lines[y][x])
            top: int = 0
            dwn: int = 0
            lft: int = 0
            rgt: int = 0

            for i in range(y-1, -1, -1):
                top += 1
                if (int(lines[i][x]) >= val):
                    break

            for i in range(y+1, my):
                dwn += 1
                if (int(lines[i][x]) >= val):
                    break

            for i in range(x-1, -1, -1):
                lft += 1
                if (int(lines[y][i]) >= val):
                    break

            for i in range(x+1, mx):
                rgt += 1
                if (int(lines[y][i]) >= val):
                    break

            max_product = max(max_product, top * dwn * lft * rgt)

    return max_product


main()
