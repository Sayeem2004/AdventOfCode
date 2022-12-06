def main():
    fin = open("input.in", "r")
    [diagram, moves] = [line for line in fin.read().split("\n\n")]
    diagram = [line for line in diagram.split("\n")[:-1]]
    moves = [line.strip() for line in moves.split("\n")[:-1]]

    print("Part 1: " + str(part1(diagram, moves)))
    print("Part 2: " + str(part2(diagram, moves)))


def ind(i):
    return i//4 + 1


def part1(diagram, moves):
    stack = {}

    for row in diagram:
        for i in range(1, len(row), 4):
            if (row[i] == ' '):
                continue
            if (ind(i) in stack):
                stack[ind(i)].append(row[i])
            else:
                stack[ind(i)] = [row[i]]

    for move in moves:
        move = move.split(" ")
        mv, src, sin = int(move[1]), int(move[3]), int(move[5])

        for i in range(mv):
            if (len(stack[src]) != 0):
                stack[sin].insert(0, stack[src].pop(0))

    ret = ""
    for i in range(1, len(stack)+1):
        ret += stack[i][0]

    return ret


def part2(diagram, moves):
    stack = {}

    for row in diagram:
        for i in range(1, len(row), 4):
            if (row[i] == ' '):
                continue
            if (ind(i) in stack):
                stack[ind(i)].append(row[i])
            else:
                stack[ind(i)] = [row[i]]

    for move in moves:
        move = move.split(" ")
        mv, src, sin = int(move[1]), int(move[3]), int(move[5])

        pref = stack[src][0:mv]
        stack[src] = stack[src][mv:]
        stack[sin] = pref + stack[sin]

    ret = ""
    for i in range(1, len(stack)+1):
        ret += stack[i][0]

    return ret


main()
