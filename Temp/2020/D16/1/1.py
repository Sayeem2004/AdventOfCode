fin = open("1.in","r");
fout = open("1.out","w");

def main():
    lines = [line.strip() for line in fin.read().split("\n")[0:-1]];
    fout.write(str(solve(lines)));

def solve(lines):
    i = 0; ran = []; personal = []; others = [];
    for line in lines:
        if (line == ""): i+=1; continue;
        if (i == 0): ran.append(line);
        if (i == 1): personal.append(line);
        if (i == 2): others.append(line);
    ran = [[r.split(" ")[-3],r.split(" ")[-1]] for r in ran];
    ranges = [];
    for r in ran:
        s = set();
        a,b = int(r[0].split("-")[0]), int(r[0].split("-")[1]);
        for i in range(a,b+1): s.add(i);
        c,d = int(r[1].split("-")[0]), int(r[1].split("-")[1]);
        for i in range(c,d+1): s.add(i);
        ranges.append(s);
    personal = [int(i) for i in personal[1].split(",")];
    others = [other.split(",") for other in others[1:]];
    ans = 0;
    for other in others:
        for o in other:
            a = False;
            b = int(o);
            for s in ranges:
                if b in s: a = True; break;
            if (a == False): ans += b;
    return ans;
    
main();
