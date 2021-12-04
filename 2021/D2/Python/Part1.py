fin = open("../Input.in", "r");
fout = open("../Part1.out", "w");

def main():
    lines = [line.strip().split() for line in fin.read().split("\n")[0:-1]];
    fout.write(str(solve(lines)));

def solve(lines):
    x,y = 0,0;
    for i in range(len(lines)):
        if (lines[i][0] == "forward"): x += int(lines[i][1]);
        if (lines[i][0] == "down"): y += int(lines[i][1]);
        if (lines[i][0] == "up"): y -= int(lines[i][1]);
    return x*y;

main();
