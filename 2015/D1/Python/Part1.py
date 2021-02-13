fin = open("../Input.in","r");
fout = open("../Part1.out","w");

def main():
    line = fin.read();
    fout.write(str(solve(line)));

def solve(line):
    floor = 0;
    for x in line:
        if (x == "("): floor+=1;
        if (x == ")"): floor-=1;
    return floor;

main();
