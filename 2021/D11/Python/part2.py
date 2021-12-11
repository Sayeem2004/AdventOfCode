def main():
    fin = open("../input.in", "r")
    fout = open("../part2.out", "w")
    lines = [line.strip() for line in fin.read().split("\n")[0:-1]]
    lines = [[int(x) for x in line] for line in lines]
    fout.write(str(solve(lines)))


def flash(lines, i, q, visited):
    if (lines[i][q] >= 10 and visited[i][q] == 0):
        visited[i][q] = 1
        x, y = {-1, 0, 1}, {-1, 0, 1}
        for dx in x:
            for dy in y:
                if ((dx == 0 and dy == 0) or i+dx < 0 or i+dx >= len(lines) or q+dy < 0 or q+dy >= len(lines[0])):
                    continue
                else:
                    lines[i+dx][q+dy] += 1
                    flash(lines, i+dx, q+dy, visited)


def solve(lines):
    for r in range(1000):
        cnt = 0
        visited = [[0 for x in range(10)] for y in range(10)]
        for i, line in enumerate(lines):
            for q, num in enumerate(line):
                lines[i][q] += 1
        for i, line in enumerate(lines):
            for q, num in enumerate(line):
                flash(lines, i, q, visited)
        for i, line in enumerate(lines):
            for q, num in enumerate(line):
                if (num >= 10):
                    lines[i][q] = 0
                    cnt += 1
        if (cnt == 100):
            return r+1
    return -1


main()
