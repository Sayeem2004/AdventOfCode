def main():
    fin = open("../input.in", "r");
    fout = open("../part.out", "w");
    lines = [line.strip() for line in fin.read().split("\n")[0:-1]];
    fout.write(str(solve(lines)));

def solve(lines):

main();
