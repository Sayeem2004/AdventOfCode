fin = open("1.in","r");
fout = open("1.out","w");

def main():
    lines = [line.strip() for line in fin.read().split("\n")[0:-1]];
    a = int(lines[0]);
    b = int(lines[1]);
    b2 = int(lines[1]);
    f = 7; i = 1;
    while (f != a):
        f *= 7;
        f %= 20201227;
        i += 1;
    while (i > 1):
        b *= b2;
        b %= 20201227;
        i -= 1;
    fout.write(str(b));
main();
