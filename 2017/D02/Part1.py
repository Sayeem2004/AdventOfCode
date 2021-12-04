fin = open("Input.in","r");
fout = open("Part1.out","w");

def main():
    lines = [line.strip() for line in fin.read().split("\n")[0:-1]];
    lines = [[int(l) for l in line.split("\t")] for line in lines];
    fout.write(str(solve(lines)));

def solve(lines):
    ans = 0;
    for line in lines:
        mx,mn = -1000000,1000000;
        for num in line:
            mx = max(num,mx);
            mn = min(num,mn);
        ans += mx-mn;
    return ans;
main();
