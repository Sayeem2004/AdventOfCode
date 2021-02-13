fin = open("../Input.in","r");
fout = open("../Part2.out","w");

def main():
    lines = [line.strip() for line in fin.read().split("\n")[0:-1]];
    fout.write(str(solve(lines)));

def solve(lines):
    count = 0;
    for line in lines:
        num = [int(l) for l in line.split("x")];
        num.sort();
        count += num[0]*num[1]*num[2];
        count += num[0]*2+num[1]*2;
    return count;

main();
