fin = open("../input.in", "r");
fout = open("../part1.out", "w");

def main():
    lines = [line.strip() for line in fin.read().split("\n")[0:-1]];
    lines = [[int(num) for num in line] for line in lines];
    fout.write(str(solve(lines)));

def solve(lines):
    cnt = 0;
    for i,line in enumerate(lines):
        for q,num in enumerate(line):
            add = True;
            if (i > 0 and lines[i-1][q] <= num): add = False;
            if (q > 0 and lines[i][q-1] <= num): add = False;
            if (i < len(lines)-1 and lines[i+1][q] <= num): add = False;
            if (q < len(line)-1 and lines[i][q+1] <= num): add = False;
            if (add): cnt += (num+1);
    return cnt;

main();
