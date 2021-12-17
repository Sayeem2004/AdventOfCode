def main():
    fin, fout = open("../input.in", "r"), open("../part2.out", "w")
    lines = "".join(fin.read().split("\n")[0].strip().split("target area: x=")).split(", y=")
    lines = [[int(x) for x in line.split("..")] for line in lines]
    fout.write(str(solve(lines)))

def check(dy, dx, lines):
    x, y = 0, 0
    for cnt in range(250):
        y += dy
        dy -= 1
        x += dx
        if (dx > 0): dx -= 1
        elif (dx < 0): dx += 1
        if (lines[0][0] <= x and lines[0][1] >= x and lines[1][0] <= y and lines[1][1] >= y):
            return True
    return False

def solve(lines):
    ans = 0
    mxy = max(abs(lines[1][0]), abs(lines[1][1]))
    mxx = max(abs(lines[0][0]), abs(lines[0][1]))
    for dy in range(-mxy, mxy+1):
        for dx in range(-mxx, mxx+1):
            if (check(dy, dx, lines)): ans += 1
    return ans

main()
