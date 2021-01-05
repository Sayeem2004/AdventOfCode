fin = open("1.in","r");
fout = open("1.out","w");

def main():
    lines = fin.read().split("\n");
    lines = [line.strip() for line in lines[0:-1]];
    lines = [int(line) for line in lines];
    fout.write(str(solve(lines)));

def solve(lines):
    n = len(lines);
    for i in range(25,n):
        a = False;
        for q in range(i-25,i):
            for r in range(i-25,i):
                if (lines[r] + lines[q] == lines[i] and r != q):
                    a = True;
        if (a == False):
            return lines[i];

main();
