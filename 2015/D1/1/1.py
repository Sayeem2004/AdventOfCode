fin = open("1.in","r");
fout = open("1.out","w");

def main():
    line = fin.read();
    fout.write(solve(line));

def solve(line):
    floor = 0;
    for x in line:
        if (x == "("): floor+=1;
        if (x == ")"): floor-=1;
    return str(floor);

main();
