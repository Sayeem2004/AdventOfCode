fin = open("1.in","r");
fout = open("1.out","w");

def main():
    lines = [line.strip() for line in fin.read().split("\n")[0:-1]];
    lines = [line[1:] for line in lines];
    lines = [" ".join(line.split(" @ ")) for line in lines];
    lines = [" ".join(line.split(": ")) for line in lines];
    lines = [" ".join(line.split(",")) for line in lines];
    lines = [" ".join(line.split("x")) for line in lines];
    lines = [line.split(" ") for line in lines];
    lines = [[int(l) for l in line] for line in lines]
    fout.write(str(solve(lines)));

def solve(lines):
    dt = {};
    for line in lines:
        for i in range(line[1],line[1]+line[3]):
            for q in range(line[2],line[2]+line[4]):
                if ((i,q) in dt): dt[(i,q)] += 1;
                else: dt[(i,q)] = 1;
    count = 0;
    for d in dt:
        if (dt[d] > 1): count += 1;
    return count;

main();
