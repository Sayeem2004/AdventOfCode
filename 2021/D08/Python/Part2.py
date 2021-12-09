fin = open("../input.in", "r");
fout = open("../part2.out", "w");

def main():
    lines = [line.strip() for line in fin.read().split("\n")[0:-1]];
    lines = [line.split(" | ") for line in lines];
    lines = [[x.split() for x in line] for line in lines];
    fout.write(str(solve(lines)));

def diff(num1, num2):
    ret = "";
    for c in num1:
        if (c not in num2):
            ret += c;
    for c in num2:
        if (c not in num1):
            ret += c;
    return ret;

def solve(lines):
    cnt = 0;
    for line in lines:
        key = [-1 for i in range(10)];
        # Getting 1, 4, 7, 8
        for i,x in enumerate(line[0]):
            if (len(x) == 2): key[1] = i;
            if (len(x) == 3): key[7] = i;
            if (len(x) == 4): key[4] = i;
            if (len(x) == 7): key[8] = i;
        # Getting 0, 6, 9
        for i,x in enumerate(line[0]):
            if (len(x) == 6):
                cmp8_x = diff(line[0][key[8]], x);
                cmp1_8x = diff(cmp8_x, line[0][key[1]]);
                if (len(cmp1_8x) == 1): key[6] = i;
                else:
                    cmp4_8x = diff(cmp8_x, line[0][key[4]]);
                    if (len(cmp4_8x) == 5): key[9] = i;
                    else: key[0] = i;
        # Getting 2, 3, 5
        for i,x in enumerate(line[0]):
            if (i not in key):
                cmp6_x = diff(line[0][key[6]], x);
                if (len(cmp6_x) == 1): key[5] = i;
                else:
                    cmp4_6x = diff(line[0][key[4]], cmp6_x);
                    if (len(cmp4_6x) == 1): key[2] = i;
                    else: key[3] = i;
        # Getting Four Unknowns
        val = 0;
        for i,x in enumerate(line[1]):
            for q,k in enumerate(key):
                if (len(diff(x, line[0][k])) == 0):
                    val += q * (10 ** (4-i-1));
        cnt += val;
    return cnt;

main();
