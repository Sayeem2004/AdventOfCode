def solve(rules):
    final = [0];
    next = find(0)
def main():
    fin = open("1.in","r");
    fout = open("1.out","w");
    lines = [line.strip() for line in fin.read().split("\n\n")];
    rules = [line.strip().split(": ") for line in lines[0].split("\n")];
    messages = [line.strip() for line in lines[1].split("\n")[:-1]];
    fout.write(str(rules)+"\n");
    fout.write(str(messages));
    final = solve(rules);
main();
