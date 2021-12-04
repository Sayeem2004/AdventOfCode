fin = open("2.in","r");
fout = open("2.out","w");

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
    others = [[int(o) for o in other.split(",")] for other in others[1:]];
    final = [];
    for other in others:
        c = True;
        for o in other:
            a = False;
            for s in ranges:
                if o in s: a = True; break;
            if (a == False): c = False;
        if (c == True): final.append(other);
    position = [0]*len(ranges);
    counts = [];
    for i,r in enumerate(ranges):
        count = [0]*len(final[0]);
        for fn in final:
            for q,f in enumerate(fn):
                if (f in r): count[q]+=1;
        counts.append(count);
        count = ["0" if (c != 190) else c for c in count];
        fout.write(str(count)+"\n");
    a = 5977293343129;
    for num in personal:
        fout.write(str(a%num)+" ");
    fout.write("\n"+str(5977293343129));
main();
