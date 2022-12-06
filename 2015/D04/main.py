from hashlib import md5


def main():
    fin = open("input.in", "r")
    line = fin.read().strip()

    print("Part 1: " + str(part1(line)))
    print("Part 2: " + str(part2(line)))


def part1(line):
    for i in range(1000000):
        temp = md5((line+str(i)).encode()).hexdigest()

        if temp[:5] == '00000':
            return i


def part2(line):
    for i in range(10000000):
        temp = md5((line+str(i)).encode()).hexdigest()

        if temp[:6] == '000000':
            return i


main()
