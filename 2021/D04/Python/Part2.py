fin = open("../Input.in", "r");
fout = open("../Part2.out", "w");

def main():
    lines = [line.strip() for line in fin.read().split("\n")[0:-1]];
    fout.write(str(solve(lines)));

def solve(lines):


main();
