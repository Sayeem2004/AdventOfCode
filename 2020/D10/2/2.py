fin = open("2.in","r");
fout = open("2.out","w");

def main():
    lines = fin.read().split("\n");
    lines = [line.strip() for line in lines[0:-1]];
    lines = [int(line) for line in lines];
    lines.append(0); lines.sort();
    lines.append(lines[-1]+3);
    fout.write(str(solve(lines)));

def solve(lines):
    n = len(lines);
    dp = [0] * (lines[-1]+1);
    dp[0] = 1;
    for i in range(1,n):
        dp[lines[i]] = dp[lines[i]-1] + dp[lines[i]-2] + dp[lines[i]-3];
    return dp[-1];

main();
