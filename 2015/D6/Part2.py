fin = open("Input.in","r");
fout = open("Part2.out","w");

def main():
    lines = [line.strip() for line in fin.read().split("\n")[0:-1]];
    lines = [line[5:] if line[:4] == "turn" else line for line in lines];
    lines = [" ".join(line.split(" through ")) for line in lines];
    lines = [" ".join(line.split(",")) for line in lines];
    lines = [line.split(" ") for line in lines];
    fout.write(str(solve(lines)));

def solve(lines):
    active = {};
    for line in lines:
        x1 = int(line[1]); x2 = int(line[3]);
        y1 = int(line[2]); y2 = int(line[4]);
        if (line[0] == "on"):
            for i in range(x1,x2+1):
                for q in range(y1,y2+1):
                    if ((i,q) in active): active[(i,q)] += 1;
                    else: active[(i,q)] = 1;
        if (line[0] == "off"):
            for i in range(x1,x2+1):
                for q in range(y1,y2+1):
                    if ((i,q) in active): active[(i,q)] = max(active[(i,q)]-1,0);
                    else: active[(i,q)] = 0;
        if (line[0] == "toggle"):
            for i in range(x1,x2+1):
                for q in range(y1,y2+1):
                    if ((i,q) in active): active[(i,q)] += 2;
                    else: active[(i,q)] = 2;
    ans = 0;
    for act in active:
        ans += active[act];
    return ans;

main();
