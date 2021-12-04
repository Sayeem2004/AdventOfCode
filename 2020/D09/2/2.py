fin = open("2.in","r");
fout = open("2.out","w");

def main():
    lines = fin.read().split("\n");
    lines = [line.strip() for line in lines[0:-1]];
    lines = [int(line) for line in lines];
    fout.write(str(solve(lines)));

def solve(lines):
    n = len(lines);
    sum = 1930745883;
    for i in range(0,n):
        for q in range(i+1,n):
            sm = 0;
            mn = 1000000000000;
            mx = -100000000000;
            for r in range(i,q):
                mn = min(mn,lines[r]);
                mx = max(mx,lines[r]);
                sm += lines[r];
            if (sm == sum):
                return mn+mx
    return 0;
main();
