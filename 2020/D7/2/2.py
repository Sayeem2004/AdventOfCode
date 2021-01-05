fin = open("2.in","r");
fout = open("2.out","w");

def main():
    lines = fin.read().split("\n")[0:-1];
    lines = [line.split("contain") for line in lines];
    lines = [[line[0],line[1].split(",")] for line in lines];
    for line in lines:
        if (line[0][-2] == 's'): line[0] = line[0][0:-6];
        else: line[0] = line[0][0:-5];
    fout.write(str(solve(lines, "shiny gold")-1));

def solve(lines, color):
    for line in lines:
        sum = 0;
        if (color == line[0]):
            for l in line[1]:
                a = " ".join(l.split(" ")[-3:-1])
                if (a == "no other"): return 1;
                else: sum += int(l.split(" ")[-4]) * solve(lines,a);
            return sum + 1;

main()
