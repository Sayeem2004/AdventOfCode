def main():
    fin = open("input.in", "r")
    lines = [line.strip() for line in fin.read().split("\n")[0:-1]]

    print("Part 1: " + str(part1(lines)))
    print("Part 2: " + str(part2(lines)))


def part1(lines):
    cnt = 0

    for line in lines:
        fir, sec = line.split(",")
        l1, r1 = [int(i) for i in fir.split("-")]
        l2, r2 = [int(i) for i in sec.split("-")]

        if (l1 <= l2 and r1 >= r2):
            cnt += 1
        elif (l1 >= l2 and r1 <= r2):
            cnt += 1

    return cnt


def part2(lines):
    cnt = 0

    for line in lines:
        fir, sec = line.split(",")
        l1, r1 = [int(i) for i in fir.split("-")]
        l2, r2 = [int(i) for i in sec.split("-")]

        if (l1 <= l2 and l2 <= r1):
            cnt += 1
        elif (l1 >= l2 and l1 <= r2):
            cnt += 1

    return cnt


main()
