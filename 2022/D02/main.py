def main():
    fin = open("input.in", "r")
    lines = [line.strip() for line in fin.read().split("\n")[0:-1]]

    print("Part 1: " + str(part1(lines)))
    print("Part 2: " + str(part2(lines)))


def part1(lines):
    key1 = "ABC"
    key2 = "XYZ"
    cnt = 0

    for line in lines:
        val1 = key1.index(line[0])
        val2 = key2.index(line[2])

        cnt += (val2 + 1)
        dif = (val2 - val1)

        if (abs(dif) == 2):
            dif = dif * -1 // 2
        cnt += (dif + 1) * 3

    return cnt


def part2(lines):
    key1 = "ABC"
    key2 = "XYZ"
    cnt = 0

    for line in lines:
        val1 = key1.index(line[0])
        val2 = key2.index(line[2])

        cnt += val2 * 3
        dif = (val2 - 1)
        cnt += (val1 + dif) % 3 + 1

    return cnt


main()
