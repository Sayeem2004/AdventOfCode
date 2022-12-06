def main():
    fin = open("input.in", "r")
    lines = fin.read()

    print("Part 1: " + str(part1(lines)))
    print("Part 2: " + str(part2(lines)))


def part1(lines):
    houses = {}
    x, y = 0, 0

    for l in lines:
        houses[(x, y)] = 1

        if (l == ">"):
            x += 1
        if (l == "<"):
            x -= 1
        if (l == "^"):
            y += 1
        if (l == "v"):
            y -= 1

    houses[(x, y)] = 1
    return len(houses)


def part2(lines):
    houses = {}
    x, y = 0, 0
    a, b = 0, 0

    for i, l in enumerate(lines):
        if (i % 2 == 0):
            houses[(x, y)] = 1
            if (l == ">"):
                x += 1
            if (l == "<"):
                x -= 1
            if (l == "^"):
                y += 1
            if (l == "v"):
                y -= 1
        else:
            houses[(a, b)] = 1
            if (l == ">"):
                a += 1
            if (l == "<"):
                a -= 1
            if (l == "^"):
                b += 1
            if (l == "v"):
                b -= 1

    houses[(x, y)] = 1
    houses[(a, b)] = 1

    return len(houses)


main()
