def main():
    fin = open("input.in", "r")
    line = fin.read()

    print("Part 1: " + str(part1(line)))
    print("Part 2: " + str(part2(line)))

def part1(line):
    floor = 0

    for x in line:
        if (x == "("):
            floor += 1
        if (x == ")"):
            floor -= 1

    return floor

def part2(line):
    floor = 0

    for i, x in enumerate(line):
        if (x == "("):
            floor += 1
        if (x == ")"):
            floor -= 1
        if (floor == -1):
            return i+1

    return -1

main()
