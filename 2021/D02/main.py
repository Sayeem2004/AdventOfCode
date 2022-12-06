def main():
    fin = open("input.in", "r")
    lines = [line.strip().split() for line in fin.read().split("\n")[0:-1]]

    print("Part 1: " + str(part1(lines)))
    print("Part 2: " + str(part2(lines)))


def part1(lines):
    x, y = 0, 0

    for i in range(len(lines)):
        if (lines[i][0] == "forward"):
            x += int(lines[i][1])
        if (lines[i][0] == "down"):
            y += int(lines[i][1])
        if (lines[i][0] == "up"):
            y -= int(lines[i][1])

    return x*y


def part2(lines):
    x, y, a = 0, 0, 0

    for i in range(len(lines)):
        if (lines[i][0] == "forward"):
            x += int(lines[i][1])
            y += a * int(lines[i][1])

        if (lines[i][0] == "down"):
            a += int(lines[i][1])
        if (lines[i][0] == "up"):
            a -= int(lines[i][1])

    return x*y


main()
