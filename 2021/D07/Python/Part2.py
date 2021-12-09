fin = open("../input.in", "r");
fout = open("../part2.out", "w");

def main():
    lines = [line.strip() for line in fin.read().split("\n")[0:-1]];
    lines = [int(x) for x in lines[0].split(",")];
    fout.write(str(solve(lines)));

def solve(lines):
    avg = 0.0;
    for x in lines:
        avg += x;
    avg /= len(lines);
    avg1 = int(avg);
    avg2 = int(avg+1);
    cost1 = 0;
    cost2 = 0;
    for x in lines:
        cost1 += abs(x-avg1)*(abs(x-avg1)+1)/2;
        cost2 += abs(x-avg2)*(abs(x-avg2)+1)/2;
    return min(cost1,cost2);

main();
