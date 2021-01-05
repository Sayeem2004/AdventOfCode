fin = open("2.in","r");
fout = open("2.out","w");

def main():
    lines = fin.read();
    fout.write(str(solve(lines)));

def solve(lines):
    houses = {};
    x,y = 0,0;
    a,b = 0,0;
    for i,l in enumerate(lines):
        if (i%2 == 0):
            houses[(x,y)] = 1;
            if (l == ">"): x+=1;
            if (l == "<"): x-=1;
            if (l == "^"): y+=1;
            if (l == "v"): y-=1;
        else:
            houses[(a,b)] = 1;
            if (l == ">"): a+=1;
            if (l == "<"): a-=1;
            if (l == "^"): b+=1;
            if (l == "v"): b-=1;
    houses[(x,y)] = 1;
    houses[(a,b)] = 1;
    return len(houses);

main();
