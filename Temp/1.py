# 2015 Day 8
fin = open("1.in","r");
fout = open("1.out","w");

def main():
    lines = [line.strip()[1:-1] for line in fin.read().split("\n")[0:-1]];
    fout.write(str(solve(lines)));

def solve(lines):
    total = 0; actual = 0;
    for line in lines:
        count = 0; i = 0;
        total += len(line)+2;
        while (i < len(line)):
            if (i != len(line)-1 and line[i]+line[i+1] == "\\\\"): i += 1;
            if (i != len(line)-1 and line[i]+line[i+1] == "\\\""): i += 1;
            if (i != len(line)-1 and line[i]+line[i+1] == "\\x"): i += 3;
            i += 1; count += 1;
        actual += count;
        fout.write(str(count)+"\n")
    fout.write(str(total)+"\n");
    fout.write(str(actual)+"\n");
    return total-actual;
main();
