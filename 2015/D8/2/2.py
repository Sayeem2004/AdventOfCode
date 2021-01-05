fin = open("2.in","r");
fout = open("2.out","w");

def main():
    lines = [line.strip() for line in fin.read().split("\n")[:-1]];
    fout.write(str(solve(lines)));

def solve(lines):
    count = 0;
    for line in lines:
        count += line.count("\\");
        count += line.count('"');
        count += 2;
    return count;

main();
