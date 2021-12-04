fin = open("1.in","r");
fout = open("1.out","w");

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
    black = [];
    for line in lines:
        p = find(line);
        if (p in black):
            black.remove(p);
        else:
            black.append(p);
    fout.write(str(len(black)));
main();
