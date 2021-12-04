fin = open("1.in","r");
fout = open("1.out","w");

def main():
    lines = fin.read().split("\n");
    lines = [line.split(" ") for line in lines];
    fout.write(str(solve(lines)));

def solve(lines):
    n = len(lines); s = set();
    acc = 0; i = 0;
    while (i < n):
        if (i in s): return acc;
        else:
            s.add(i);
            a = lines[i][0];
            if (a == "nop"): i+=1; continue;
            if (a == "acc"):
                if (lines[i][1][0] == "+"): acc += int(lines[i][1][1:]);
                else: acc -= int(lines[i][1][1:]);
            if (a == "jmp"):
                if (lines[i][1][0] == "+"): i += int(lines[i][1][1:])-1;
                else: i -= int(lines[i][1][1:])+1;
        i+=1;

main();
