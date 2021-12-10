fin = open("../input.in", "r");
fout = open("../part1.out", "w");

def main():
    lines = [line.strip() for line in fin.read().split("\n")[0:-1]];
    lines = [[[int(y) for y in x.split(",")] for i,x in enumerate(line.split(" ")) if (i == 0 or i == 2)] for line in lines];
    fout.write(str(solve(lines)));

def solve(lines):
    lt = [[0 for x in range(1000)] for y in range(1000)];
    for line in lines:
        if (line[0][0] == line[1][0]):
            mx = max(line[0][1],line[1][1]);
            mn = min(line[0][1],line[1][1]);
            for i in range(mn,mx+1):
                lt[line[0][0]][i] += 1;
        elif (line[0][1] == line[1][1]):
            mx = max(line[0][0],line[1][0]);
            mn = min(line[0][0],line[1][0]);
            for i in range(mn,mx+1):
                lt[i][line[0][1]] += 1;
    cnt = 0;
    for x in lt:
        for y in x:
            if (y > 1): cnt += 1;
    return cnt;

main();
