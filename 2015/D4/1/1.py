from hashlib import md5
fin = open("1.in","r");
fout = open("1.out","w");

def main():
    line = fin.read().strip();
    fout.write(str(solve(line)));

def solve(line):
    for i in range(1000000):
        temp = md5((line+str(i)).encode()).hexdigest();
        if temp[:5] == '00000': return i;

main();
