fin = open("../Input.in", "r");
fout = open("../Part2.out", "w");

def main():
    lines = [line.strip() for line in fin.read().split("\n")[0:-1]];
    fout.write(str(solve(lines)));

def solve(lines):
    cpy1 = [x for x in lines];
    cpy2 = [x for x in lines];
    for i in range(len(lines[0])):
        cnt = 0;
        for x in cpy1:
            if (x[i] == "1"): cnt += 1;
        if (cnt >= len(cpy1)-cnt): rem = "0";
        else: rem = "1";
        cpy1 = [x for x in cpy1 if x[i] != rem];
        if (len(cpy1) == 1): break;
    for i in range(len(lines[0])):
        cnt = 0;
        for x in cpy2:
            if (x[i] == "1"): cnt += 1;
        if (cnt >= len(cpy2)-cnt): rem = "1";
        else: rem = "0";
        cpy2 = [x for x in cpy2 if x[i] != rem];
        if (len(cpy2) == 1): break;
    return int(cpy1[0], 2) * int(cpy2[0], 2);

main();
