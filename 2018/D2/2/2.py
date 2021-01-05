fin = open("2.in","r");
fout = open("2.out","w");

def main():
    lines = [line.strip() for line in fin.read().split("\n")[0:-1]];
    fout.write(str(solve(lines)));

def solve(lines):
    ans = "";
    for i in range(len(lines)):
        for q in range(i+1,len(lines)):
            if (check(lines[i],lines[q]) == 1):
                for r in range(len(lines[i])):
                    if (lines[i][r] == lines[q][r]):
                        ans += lines[i][r];
    return ans;

def check(a,b):
    count = 0;
    for i,x in enumerate(a):
        if (x != b[i]): count+=1;
    return count;

main();
