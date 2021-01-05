fin = open("1.in","r");
fout = open("1.out","w");

def main():
    line = fin.read().split("\n")[0].strip();
    fout.write(str(solve(line)));

def solve(line):
    i,n = 0,len(line);
    while (i < n-1):
        if (abs(ord(line[i])-ord(line[i+1])) == 32):
            line = line[:i] + line[i+2:];
            n -= 2; i -= 1; i = max(i,0)
            continue;
        i+=1;
    return len(line);

main();
