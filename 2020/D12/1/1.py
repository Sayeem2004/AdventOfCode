fin = open("1.in","r");
fout = open("1.out","w");

def main():
    lines = [line.strip() for line in fin.read().split("\n")[0:-1]];
    fout.write(str(solve(lines)));

def solve(lines):
    direction = [False,True,False,False];
    x = 0; y = 0;
    for line in lines:
        if (line[0] == "F"):
            if (direction[0] == True): y += int(line[1:]);
            if (direction[1] == True): x += int(line[1:]);
            if (direction[2] == True): y -= int(line[1:]);
            if (direction[3] == True): x -= int(line[1:]);
            continue;
        if (line[0] == "N"): y += int(line[1:]); continue;
        if (line[0] == "S"): y -= int(line[1:]); continue;
        if (line[0] == "E"): x += int(line[1:]); continue;
        if (line[0] == "W"): x -= int(line[1:]); continue;
        if (line[0] == "R"):
            for i in range(0,4):
                if (direction[i] == True):
                    direction[i] = False;
                    direction[int(i+(int(line[1:])/90))%4] = True;
                    break;
            continue;
        if (line[0] == "L"):
            for i in range(0,4):
                if (direction[i] == True):
                    direction[i] = False;
                    direction[int(i-(int(line[1:])/90))%4] = True;
                    break;
            continue
    return abs(y)+abs(x);

main();
