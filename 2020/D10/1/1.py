fin = open("1.in","r");
fout = open("1.out","w");

def main():
    lines = fin.read().split("\n");
    lines = [line.strip() for line in lines[0:-1]];
    lines = [int(line) for line in lines];
    lines.append(0);
    fout.write(str(solve(lines)));

def solve(lines):
    c1 = 0; c3 = 0;
    lines.sort();
    lines.append(lines[-1]+3);
    n = len(lines);
    for i in range(1,n):
        if (lines[i]-lines[i-1] == 1): c1+=1;
        if (lines[i]-lines[i-1] == 3): c3+=1;
    return c1*c3;

main();
