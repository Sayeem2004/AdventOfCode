fin = open("../Input.in", "r");
fout = open("../Part2.out", "w");

def main():
    lines = [int(line.strip()) for line in fin.read().split("\n")[0:-1]];
    fout.write(str(solve(lines)));

def solve(lines):
    cnt = 0;
    for i in range (3, len(lines)):
        if (lines[i] > lines[i-3]):
            cnt += 1;
    return cnt;

main();