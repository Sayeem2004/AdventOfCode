fin = open("../input.in", "r");
fout = open("../part2.out", "w");

def main():
    lines = [line.strip() for line in fin.read().split("\n")[0:-1]];
    fout.write(str(solve(lines)));

def solve(lines):
    ans = 0;
    for line in lines:
        l = int(line.split("-")[0]);
        r = int(line.split("-")[1].split(" ")[0]);
        c = line.split(": ")[0][-1];
        s = line.split(": ")[1];
        count = 0;
        if (s[l-1] == c): count+=1;
        if (s[r-1] == c): count+=1;
        if (count == 1): ans+=1;
    return ans;

main();
