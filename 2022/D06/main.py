from io import FileIO


def main() -> None:
    fin: FileIO = open("input.in", "r")
    line: str = fin.read()

    print("Part 1: " + str(part1(line)))
    print("Part 2: " + str(part2(line)))


def part1(line: list[str]) -> int:
    for i in range(3, len(line)):
        st: set[str] = set()

        st.add(line[i-3])
        st.add(line[i-2])
        st.add(line[i-1])
        st.add(line[i])

        if (len(st) == 4):
            return i+1

    return -1


def part2(line: list[str]) -> int:
    for i in range(13, len(line)):
        st: set[str] = set()

        for q in range(14):
            st.add(line[i-q])

        if (len(st) == 14):
            return i+1

    return -1


main()
