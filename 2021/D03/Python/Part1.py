fin = open("../Input.in", "r");
fout = open("../Part1.out", "w");

def main():
    lines = [line.strip() for line in fin.read().split("\n")[0:-1]];
    fout.write(str(solve(lines)));

def solve(lines):
    gamma = "";
    epsilon = "";
    lt = [0] * len(lines[0]);
    for line in lines:
        for i,x in enumerate(line):
            if (x == "1"): lt[i] += 1;
    for x in lt:
        if (x > len(lines)-x):
            gamma += "1";
            epsilon += "0";
        else:
            gamma += "0";
            epsilon += "1";
    return int(gamma, 2) * int(epsilon, 2);

main();
