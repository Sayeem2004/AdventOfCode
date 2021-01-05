fin = open("1.in","r");
fout = open("1.out","w");

def main():
    lines = fin.read().split("\n")[0:-1];
    lines = [line.split("contain") for line in lines];
    lines = [[line[0],line[1].split(",")] for line in lines];
    for line in lines:
        if (line[0][-2] == 's'): line[0] = line[0][0:-6];
        else: line[0] = line[0][0:-5];
    solve(lines);

def solve(lines):
    s = set();
    prev = 0; ans = 0;
    s.add("shiny gold");
    while (prev != len(s)):
        prev = len(s); ans = 0;
        for line in lines:
            i = 0;
            for l in line[1]:
                a = " ".join(l.split(" ")[-3:-1]);
                if (a in s):
                    s.add(line[0]);
                    if (i == 0): ans+=1; i+=1;
    fout.write(str(ans));
    fout.write("\n");

main()
