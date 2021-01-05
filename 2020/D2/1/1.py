fin = open("1.in","r");
fout = open("1.out","w");

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
        for x in s:
            if (x == c): count+=1;
        if (count >= l and count <= r):
            ans+=1;
    return ans;

main();
