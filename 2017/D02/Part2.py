fin = open("Input.in","r");
fout = open("Part2.out","w");

def main():
    lines = [line.strip() for line in fin.read().split("\n")[0:-1]];
    lines = [[int(l) for l in line.split("\t")] for line in lines];
    fout.write(str(solve(lines)));

def solve(lines):
    ans = 0;
    for line in lines:
        for i in range(len(line)):
            for q in range(len(line)):
                if (line[i]%line[q] == 0 and i != q):
                    ans += line[i]//line[q];
    return ans;
main();
