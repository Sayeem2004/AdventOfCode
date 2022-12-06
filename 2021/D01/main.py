def main():
    fin = open("input.in", "r")
    lines = [int(line.strip()) for line in fin.read().split("\n")[0:-1]]

    print("Part 1: " + str(part1(lines)))
    print("Part 2: " + str(part2(lines)))


def part1(lines):
    cnt = 0

    for i in range(1, len(lines)):
        if (lines[i] > lines[i-1]):
            cnt += 1

    return cnt


def part2(lines):
    cnt = 0

    for i in range(3, len(lines)):
        if (lines[i] > lines[i-3]):
            cnt += 1

    return cnt


main()
