from io import FileIO


def main() -> None:
    fin: FileIO = open("input.in", "r")
    lines: list[str] = [line.strip() for line in fin.read().split("\n")[0:-1]]
    lines.sort()

    print("Part 1: " + str(part1(lines)))
    print("Part 2: " + str(part2(lines)))


def parse(lines: list[str]) -> int:
    curr: int = -1
    prev: int = -1
    dt: dict[int, dict[int, int]] = {}

    for line in lines:
        split: list[str] = line.split(" ")
        time: int = int(split[1][:-1].split(":")[1])

        if split[2] == "Guard":
            curr = int(split[3][1:])
            if curr not in dt:
                dt[curr] = {}

        elif split[2] == "falls":
            prev = time

        elif split[2] == "wakes":
            for i in range(prev, time):
                if i not in dt[curr]:
                    dt[curr][i] = 0
                dt[curr][i] += 1

    return dt


def part1(lines: list[str]) -> int:
    dt: dict[int, dict[int, int]] = parse(lines)

    max_guard: int = -1
    for guard in dt.keys():
        if max_guard == -1 or sum(dt[guard].values()) > sum(dt[max_guard].values()):
            max_guard = guard

    max_minute: int = -1
    for minute in dt[max_guard].keys():
        if max_minute == -1 or dt[max_guard][minute] > dt[max_guard][max_minute]:
            max_minute = minute

    return max_minute * max_guard


def part2(lines: list[str]) -> int:
    dt: dict[int, dict[int, int]] = parse(lines)

    max_guard: int = -1
    for guard in dt.keys():
        guard_count = max(dt[guard].values()) if len(
            dt[guard].values()) > 0 else 0
        max_guard_count = (max(dt[max_guard].values()) if len(
            dt[max_guard].values()) > 0 else 0) if max_guard != -1 else 0

        if max_guard == -1 or guard_count > max_guard_count:
            max_guard = guard

    max_minute: int = -1
    for minute in dt[max_guard].keys():
        if max_minute == -1 or dt[max_guard][minute] > dt[max_guard][max_minute]:
            max_minute = minute

    return max_minute * max_guard


main()
