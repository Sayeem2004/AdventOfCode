fin = open("2.in","r");
fout = open("2.out","w");

def main():
    lines = [line.strip() for line in fin.read().split("\n")[0:-1]];
    fout.write(str(solve(lines)));

def solve(lines):
    x = 10; y = 1;
    dx = 0; dy = 0;
    for line in lines:
        if (line[0] == "F"):
            dx += int(line[1:]) * x;
            dy += int(line[1:]) * y;
            continue;
        if (line[0] == "N"): y += int(line[1:]); continue;
        if (line[0] == "S"): y -= int(line[1:]); continue;
        if (line[0] == "E"): x += int(line[1:]); continue;
        if (line[0] == "W"): x -= int(line[1:]); continue;
        if (line[0] == "R"):
            a = (int(line[1:])//90)%4;
            if (a == 1): t = x; x = y; y = -t;
            if (a == 2): x = -x; y = -y;
            if (a == 3): t = x; x = -y; y = t;
            continue;
        if (line[0] == "L"):
            a = (int(line[1:])//90)%4;
            if (a == 3): t = x; x = y; y = -t;
            if (a == 2): x = -x; y = -y;
            if (a == 1): t = x; x = -y; y = t;
            continue;
    return abs(dy)+abs(dx);

main();
