fin = open("../input.in", "r");
fout = open("../part1.out", "w");

def main():
    lines = [line.strip() for line in fin.read().split("\n")[0:-1]];
    lines = [line.split(" | ") for line in lines];
    lines = [[x.split() for x in line] for line in lines];
    fout.write(str(solve(lines)));

def solve(lines):
    cnt = 0;
    for line in lines:
        for num in line[1]:
            if (len(num) == 2): cnt += 1;
            if (len(num) == 3): cnt += 1;
            if (len(num) == 4): cnt += 1;
            if (len(num) == 7): cnt += 1;
    return cnt;

main();
