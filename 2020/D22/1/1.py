fin = open("1.in","r");
fout = open("1.out","w");

def main():
    lines = [line.strip() for line in fin.read().split("\n\n")];
    p1 = [int(line) for line in lines[0].split("\n")[1:]];
    p2 = [int(line) for line in lines[1].split("\n")[1:]];
    fout.write(str(solve(p1,p2)));

def solve(p1,p2):
    while (len(p1) != 0 and len(p2) != 0):
        a = p1[0]; b = p2[0];
        if (a > b):
            p1.pop(0); p2.pop(0);
            p1.append(a); p1.append(b);
        if (b > a):
            p1.pop(0); p2.pop(0);
            p2.append(b); p2.append(a);
    ans = 0;
    if (len(p1) != 0):
        for i,x in enumerate(p1):
            ans += x * (len(p1)-i);
        return ans
    if (len(p2) != 0):
        for i,x in enumerate(p2):
            ans += x * (len(p2)-i);
        return ans

main();
