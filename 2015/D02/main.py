def main():
    fin = open("input.in", "r")
    lines = [line.strip() for line in fin.read().split("\n")[0:-1]]

    print("Part 1: " + str(part1(lines)))
    print("Part 2: " + str(part2(lines)))


def part1(lines):
    count = 0

    for line in lines:
        num = [int(l) for l in line.split("x")]
        num.sort()
        count += 3*num[0]*num[1]
        count += 2*num[0]*num[2]
        count += 2*num[1]*num[2]

    return count


def part2(lines):
    count = 0

    for line in lines:
        num = [int(l) for l in line.split("x")]
        num.sort()
        count += num[0]*num[1]*num[2]
        count += num[0]*2+num[1]*2

    return count


main()
