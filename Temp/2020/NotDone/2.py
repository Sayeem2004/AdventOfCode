fin = open("2.in","r");
fout = open("2.out","w");

def find(line):
    x,y = 0,0;
    skip = False;
    for i in range(len(line)):
        if (skip): skip = False; continue;
        if (line[i] == "w"): x -= 1; continue;
        if (line[i] == "e"): x += 1; continue;
        if (line[i] == "n"):
            if (line[i+1] == "e"): x += 0.5; y += 0.5;
            else: x -= 0.5; y += 0.5;
            skip = True; continue;
        if (line[i] == "s"):
            if (line[i+1] == "e"): x += 0.5; y -= 0.5;
            else: x -= 0.5; y -= 0.5;
            skip = True; continue;
    return (x,y);

def main():
    lines = [line.strip() for line in fin.read().split("\n")[0:-1]];
    black = set();
    for line in lines:
        p = find(line);
        if (p in black):
            black.discard(p);
        else:
            black.add(p);
    fout.write(str(black)+"\n");
    xc = [1,0.5,-0.5,-1,-0.5,0.5];
    yc = [0,0.5,0.5,0,-0.5,-0.5];
    for i in range(100):
        count = {};
        for b in black:
            for q in range(6 ):
                p = (b[0]+xc[q],b[1]+yc[q]);
                if (p in count):
                    count[p] += 1;
                else:
                    count[p] = 1;
        for c in count:
            if (c in black):
                if (count[c] == 0 or count[c] > 2):
                    black.discard(c);
            else:
                if (count[c] == 2):
                    black.add(c);
        fout.write(str(len(black))+'\n');
        if (i == 0):
            fout.write(str(black)+"\n");
main();
