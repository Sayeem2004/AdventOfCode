def main():
    fin, fout = open("../input.in", "r"), open("../part1.out", "w")
    lines = [line.strip() for line in fin.read().split("\n")[0:-1]]
    fout.write(str(solve(lines)))

def solve(lines):
    return lines

main()
