fin = open("1.in","r");
fout = open("1.out","w");

def main():
    lines = [int(line.strip()) for line in fin.read().split(",")];
    fout.write(str(solve(lines)));

def solve(lines):
    mem = {}; s = set();
    for i,x in enumerate(lines[:-1]):
        mem[x] = i; s.add(x);
    i = len(lines)-1;
    while (i < 2025):
        if (lines[i] in s):
            lines.append(i-mem[lines[i]]);
            mem[lines[i]] = i;
        else:
            lines.append(0);
            mem[lines[i]] = i;
            s.add(lines[i]);
        i+=1;
    return lines[2019];
    
main();
