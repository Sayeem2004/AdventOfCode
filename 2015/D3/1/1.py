fin = open("1.in","r");
fout = open("1.out","w");

def main():
    lines = fin.read();
    fout.write(str(solve(lines)));

def solve(lines):
    houses = {};
    x,y = 0,0;
    for l in lines:
        houses[(x,y)] = 1;
        if (l == ">"): x+=1;
        if (l == "<"): x-=1;
        if (l == "^"): y+=1;
        if (l == "v"): y-=1;
    houses[(x,y)] = 1;
    return len(houses);

main();
