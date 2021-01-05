fin = open("2.in","r");
fout = open("2.out","w");

def main():
    lines = [line.strip() for line in fin.read().split("\n")[0:-1]];
    fout.write(str(solve(lines)))

def solve(lines):
    count = 0;
    for line in lines:
        double = False;
        contains = False;
        for i,x in enumerate(line):
            if (i >= 2):
                if (x == line[i-2]): contains = True;
                if ((line[i-2]+line[i-1]) in line[i:]): double = True;
        if (double and contains): count+=1;
    return count;

main();
