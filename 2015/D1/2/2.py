fin = open("2.in","r");
fout = open("2.out","w");

def main():
    line = fin.read();
    fout.write(str(solve(line)));

def solve(line):
    floor = 0;
    for i,x in enumerate(line):
        if (x == "("): floor+=1;
        if (x == ")"): floor-=1;
        if (floor == -1):
            return i+1; break;

main();
