def main():
    fin = open("../input.in", "r");
    fout = open("../part2.out", "w");
    lines = [line.strip() for line in fin.read().split("\n")[0:-1]];
    fout.write(str(solve(lines)));

def solve(lines):
    dict = {"(": 1, "[": 2, "{": 3, "<": 4};
    cnt = 0;
    sorted = [];
    for line in lines:
        lt = [];
        br = False;
        for i,c in enumerate(line):
            if (c in "([{<"): lt.append(c);
            else:
                add = False;
                if (len(lt) == 0): add = True;
                elif (c == ")" and lt[-1] != "("): add = True;
                elif (c == "]" and lt[-1] != "["): add = True;
                elif (c == "}" and lt[-1] != "{"): add = True;
                elif (c == ">" and lt[-1] != "<"): add = True;
                if (add == True): br = True; break;
                else: lt.pop();
        if (br == False):
            val = 0;
            for c in lt[::-1]:
                val *= 5;
                val += dict[c];
            sorted.append(val);
    sorted.sort();
    return sorted[len(sorted)/2];

main();
