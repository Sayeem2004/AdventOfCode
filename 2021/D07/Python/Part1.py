fin = open("../input.in", "r");
fout = open("../part1.out", "w");

def main():
    lines = [line.strip() for line in fin.read().split("\n")[0:-1]];
    lines = [int(x) for x in lines[0].split(",")];
    fout.write(str(solve(lines)));

def solve(lines):
    lines.sort();
    med = lines[len(lines)/2];
    ans = 0;
    for x in lines:
        ans += abs(x-med);
    return ans;

main();
