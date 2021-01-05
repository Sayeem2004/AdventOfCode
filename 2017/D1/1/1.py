fin = open("1.in","r");
fout = open("1.out","w");

def main():
    line = fin.read().split("\n")[0];
    line = line + line[0];
    fout.write(str(solve(line)));

def solve(line):
    ans = 0;
    for i in range(len(line)-1):
        if (line[i] == line[i+1]):
            ans += int(line[i]);
    return ans;

main();
