fin = open("2.in","r");
fout = open("2.out","w");

def main():
    lines = [line.strip() for line in fin.read().split("\n")[0:-1]];
    fout.write(str(solve(lines)));

def solve(lines):
    n = len(lines);
    m = len(lines[0]);
    active = set();
    for x in range(n):
        for y in range(m):
            if (lines[x][y] == "#"):
                active.add((x,y,0,0));
    for i in range(6):
        count = {};
        for act in active: count[act] = 0;
        for act in active:
            for xd in range(-1,2):
                for yd in range(-1,2):
                    for zd in range(-1,2):
                        for td in range(-1,2):
                            if (xd == 0 and yd == 0 and zd == 0 and td == 0): continue;
                            else:
                                t = (act[0]+xd,act[1]+yd,act[2]+zd,act[3]+td);
                                if (t in count): count[t]+=1;
                                else: count[t] = 1;
        for c in count:
            if (c in active):
                if (count[c] != 2 and count[c] != 3):
                    active.remove(c);
            else:
                if (count[c] == 3):
                    active.add(c);
    return len(active);

main();
