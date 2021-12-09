fin = open("../input.in", "r");
fout = open("../part2.out", "w");

def main():
    lines = [line.strip() for line in fin.read().split("\n")[0:-1]];
    lines = [int(x) for x in lines[0].split(",")];
    fout.write(str(solve(lines)));

def solve(lines):
    dict = {};
    for x in lines:
        if (x in dict): dict[x] += 1;
        else: dict[x] = 1;
    for d in range(9):
        if (d not in dict): dict[d] = 0;
    for i in range(256):
        copy = {};
        for q in range(9):
            if (q == 8): copy[q] = dict[0];
            elif (q == 6): copy[q] = dict[0]+dict[7];
            else: copy[q] = dict[q+1];
        dict = copy;
    cnt = 0;
    for d in range(9):
        cnt += dict[d];
    return cnt;

main();
