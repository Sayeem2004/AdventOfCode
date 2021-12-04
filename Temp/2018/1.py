fin = open("1.in","r");
fout = open("1.out","w");

def main():
    lines = [line.strip() for line in fin.read().split("\n")[0:-1]];
    lines = [" ".join(line.split(" must be finished before step ")) for line in lines];
    lines = [line[5:8].split(" ") for line in lines];
    fout.write(str(solve(lines)));

def solve(lines):
    fout.write(str(lines));
    rules = build(lines);

def build(lines):
    dict = {};
    for line in lines:

main();
