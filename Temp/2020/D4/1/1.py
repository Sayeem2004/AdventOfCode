fin = open("1.in","r");
fout = open("1.out","w");

def main():
    lines = fin.read().split("\n");
    lines = [line.split(" ") for line in lines];
    fout.write(str(solve(lines)));

def solve(lines):
    count,c = 0,0;
    a = False;
    for pp in lines:
        for id in pp:
            c+=1;
            if (id[0:3] == "cid"):
                a = True;
        if (len(pp) == 0):
            c = 0;
            a = False;
        if (c == 8 or (c == 7 and not a)):
            count+=1;
            c = 0;
            a = False;
    return count;
main()
