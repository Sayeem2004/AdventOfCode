def main():
    fin = open("../input.in", "r");
    fout = open("../part1.out", "w");
    lines = [line.strip() for line in fin.read().split("\n")[0:-1]];
    fout.write(str(solve(lines)));

def solve(lines):
    dict = {")": 3, "]": 57, "}": 1197, ">": 25137};
    cnt = 0;
    for line in lines:
        lt = [];
        for i,c in enumerate(line):
            if (c in "([{<"): lt.append(c);
            else:
                add = False;
                if (len(lt) == 0): add = True;
                elif (c == ")" and lt[-1] != "("): add = True;
                elif (c == "]" and lt[-1] != "["): add = True;
                elif (c == "}" and lt[-1] != "{"): add = True;
                elif (c == ">" and lt[-1] != "<"): add = True;
                if (add == True): cnt += dict[c]; break;
                else: lt.pop();
    return cnt;

main();
