fin = open("2.in","r");
fout = open("2.out","w");

def main():
    lines = fin.read().split("\n");
    lines = [line.split(" ") for line in lines];
    fout.write(str(solve(lines)));

def solve(lines):
    q = 0; n = len(lines);
    for e in range(0,n):
        d = check(lines,e);
        if (d == True): q = e; break;
    if (lines[q][0] == "jmp"): lines[q][0] = "nop";
    elif (lines[q][0] == "nop"): lines[q][0] = "jmp";
    acc = 0; i = 0;
    s = set();
    while (i < n):
        if (i in s): return 0;
        else:
            s.add(i);
            a = lines[i][0];
            if (a == "nop"): i+=1; continue;
            if (a == "acc"):
                if (lines[i][1][0] == "+"): acc += int(lines[i][1][1:]);
                else: acc -= int(lines[i][1][1:]);
            if (a == "jmp"):
                if (lines[i][1][0] == "+"): i += int(lines[i][1][1:])-1;
                else: i -= int(lines[i][1][1:])+1;
        i+=1;
    return acc;
    
def check(a,b):
    c = a;
    if (c[b][0] == "jmp"): c[b][0] = "nop";
    elif (c[b][0] == "nop"): c[b][0] = "jmp";
    n = len(c); s = set();
    i = 0;
    while (i < n):
        if (i in s):
            if (c[b][0] == "jmp"): c[b][0] = "nop";
            elif (c[b][0] == "nop"): c[b][0] = "jmp";
            return False;
        else:
            s.add(i);
            a = c[i][0];
            if (a == "nop"): i+=1; continue;
            if (a == "acc"): i+=1; continue;
            if (a == "jmp"):
                if (c[i][1][0] == "+"): i += int(c[i][1][1:])-1;
                else: i -= int(c[i][1][1:])+1;
        i+=1;
    if (c[b][0] == "jmp"): c[b][0] = "nop";
    elif (c[b][0] == "nop"): c[b][0] = "jmp";
    return True;

main();
