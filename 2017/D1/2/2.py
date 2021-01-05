fin = open("2.in","r");
fout = open("2.out","w");

def main():
    line = fin.read().split("\n")[0];
    line = line + line;
    fout.write(str(solve(line)));

def solve(line):
    ans = 0;
    n = len(line)/2
    for i in range(n):
        if (line[i] == line[i+n//2]):
            ans += int(line[i]);
    return ans;

main();
