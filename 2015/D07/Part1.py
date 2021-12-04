fin = open("Input.in","r");
fout = open("Part1.out","w");

def main():
    lines = [line.strip().split(" ") for line in fin.read().split("\n")[0:-1]];
    mem = {};
    fout.write(str(solve(lines,mem)));

def solve(lines,mem):
    next = [];
    for line in lines:
        if (line[1] == "->"):
            if (line[0].isdigit()): mem[line[2]] = int(line[0]);
            elif (line[0] in mem): mem[line[2]] = mem[line[0]];
            else: next.append(line);
            continue;
        if (line[1] == "AND"):
            if (line[0] in mem and line[2] in mem): mem[line[4]] = mem[line[0]] & mem[line[2]];
            elif (line[0] in mem and line[2].isdigit()): mem[line[4]] = mem[line[0]] & int(line[2]);
            elif (line[0].isdigit() and line[2] in mem): mem[line[4]] = int(line[0]) & mem[line[2]];
            elif (line[0].isdigit() and line[2].isdigit()): mem[line[4]] = int(line[0]) & int(line[2]);
            else: next.append(line);
            continue;
        if (line[1] == "OR"):
            if (line[0] in mem and line[2] in mem): mem[line[4]] = mem[line[0]] | mem[line[2]];
            elif (line[0] in mem and line[2].isdigit()): mem[line[4]] = mem[line[0]] | int(line[2]);
            elif (line[0].isdigit() and line[2] in mem): mem[line[4]] = int(line[0]) | mem[line[2]];
            elif (line[0].isdigit() and line[2].isdigit()): mem[line[4]] = int(line[0]) | int(line[2]);
            else: next.append(line);
            continue;
        if (line[1] == "LSHIFT"):
            if (line[0] in mem): mem[line[4]] = mem[line[0]] << int(line[2]);
            elif (line[0].isdigit()): mem[line[4]] = int(line[0]) << int(line[2]);
            else: next.append(line);
            continue;
        if (line[1] == "RSHIFT"):
            if (line[0] in mem): mem[line[4]] = mem[line[0]] >> int(line[2]);
            elif (line[0].isdigit()): mem[line[4]] = int(line[0]) >> int(line[2]);
            else: next.append(line);
            continue;
        if (line[0] == "NOT"):
            mx = 0b1111111111111111;
            if (line[1] in mem): mem[line[3]] = mx - mem[line[1]];
            elif (line[1].isdigit()): mem[line[3]] = mx - int(line[1]);
            else: next.append(line);
    if (len(next) == 0): return mem["a"];
    else: return solve(next,mem);

main();
