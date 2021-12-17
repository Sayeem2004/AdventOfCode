def main():
    fin, fout = open("../input.in", "r"), open("../part1.out", "w")
    lines = "".join(fin.read().split("\n")[0].strip().split("target area: x=")).split(", y=")
    lines = [[int(x) for x in line.split("..")] for line in lines]
    fout.write(str(solve(lines)))

def solve(lines):
    mxy = abs(min(lines[1][0], lines[1][1]))-1
    return (mxy)*(mxy+1)//2

main()
