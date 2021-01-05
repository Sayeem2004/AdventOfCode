fin = open("1.in","r");
fout = open("1.out","w");

def main():
    lines = [line.strip() for line in fin.read().split("\n")[0:-1]];
    a = int(lines[0])
    lines = lines[1].split(",");
    fout.write(str(solve(a,lines)));

def solve(a,lines):
    wait = 1000;
    index = -1;
    for i in range(0,len(lines)):
        if (lines[i] == "x"): continue;
        else:
            b = int(lines[i]);
            if (a//b * b + b - a < wait):
                wait = a//b * b + b - a; index = i;
    return int(lines[index]) * wait;

main();
