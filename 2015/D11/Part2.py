fin = open("Input.in","r");
fout = open("Part2.out","w");

def main():
    line = fin.read().split("\n")[0];
    fout.write(str(solve(line))+"\n");

def solve(line):
    count = 0;
    for i in range(stoi(line),26**8):
        if check(itos(i)):
            count += 1;
        if (count == 2):
            return itos(i);

def stoi(line):
    sum = 0;
    m = 1;
    for l in line[::-1]:
        sum += m * (ord(l) - ord('a'));
        m *= 26;
    return sum;

def itos(num):
    ret = "";
    while (num > 0 or len(ret) < 8):
        ret = chr(int(ord('a')+num%26)) + ret;
        num -= num%26;
        num /= 26;
    return ret;

def check(line):
    if ("i" in line or "o" in line or "l" in line):
        return False;
    a = False;
    b = 0;
    st = 0;
    skip = False;
    for i,c in enumerate(line):
        if (i == 0):
            continue;
        else:
            if (c == line[i-1] and skip == False):
                b += 1; skip = True;
            else:
                skip = False;
            if (ord(c)-ord(line[i-1]) == 1): st += 1;
            else: st = 0;
            if (st == 2): a = True
    return a and b == 2;

main();
