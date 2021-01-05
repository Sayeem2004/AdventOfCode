fin = open("1.in","r");
fout = open("1.out","w");

def main():
    lines = [line.strip() for line in fin.read().split("\n")[0:-1]];
    lines = ["".join(line.split(" ")) for line in lines];
    lines = [line.split("=") for line in lines];
    fout.write(str(solve(lines)));

def solve(lines):
    mem = {};
    mask = list(lines[0][1]);
    for x in lines:
        if (x[0] == "mask"): mask = list(x[1]);
        else:
            a = str(bin(int(x[1])))[2:];
            b = len(a);
            c = ["0" if m == "X" else m for m in mask];
            d = len(mask);
            for i in range(0,b):
                if (mask[d-b+i] == "X"): c[d-b+i] = a[i];
            y = 0;
            for i in range(0,d):
                if (c[i] == "1"): y = i; break;
            c = "".join(c[y:]);
            c = int("0b"+c,2);
            mem[x[0][4:-1]] = c
    sum = 0;
    for x in mem: sum += mem[x];
    return sum;

main();
