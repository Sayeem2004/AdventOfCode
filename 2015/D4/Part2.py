from hashlib import md5
fin = open("Input.in","r");
fout = open("Part2.out","w");

def main():
    line = fin.read().strip();
    fout.write(str(solve(line)));

def solve(line):
    for i in range(10000000):
        temp = md5((line+str(i)).encode()).hexdigest();
        if temp[:6] == '000000': return i;

main();
