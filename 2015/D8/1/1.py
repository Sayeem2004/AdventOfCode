fin = open("1.in","r");
fout = open("1.out","w");

def main():
    lines = [line.strip() for line in fin.read().split("\n")[:-1]];
    fout.write(str(solve(lines)));

def solve(lines):
    count = 0;
    for line in lines:
        count += len(line)-len(eval(line));
    return count;

main();
