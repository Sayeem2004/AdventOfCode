fin = open("1.in","r");
fout = open("1.out","w");

def main():
    lines = [line.strip() for line in fin.read().split("\n")[0:-1]];
    lines = [" ".join(line.split(" ")[2:]) for line in lines];
    lines = [line.split(", ") for line in lines];
    lines = [[l.split(": ") for l in line] for line in lines];
    dict = {};
    dict["children"] = 3;
    dict["cats"] = 7;
    dict["samoyeds"] = 2;
    dict["pomeranians"] = 3;
    dict["akitas"] = 0;
    dict["vizslas"] = 0;
    dict["goldfish"] = 5;
    dict["trees"] = 3;
    dict["cars"] = 2;
    dict["perfumes"] = 1;
    fout.write(str(solve(lines,dict)));

def solve(lines,dict):
    points = {};
    for i,line in enumerate(lines):
        p = 0;
        for l in line:
            if (int(l[1]) == dict[l[0]]):
                p += 1;
        points[i+1] = p;
    mx = 0;
    for p in points:
        mx = max(points[p],mx);
    for p in points:
        if (points[p] == mx):
            return p;
    return 0;

main();
