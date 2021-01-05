fin = open("1.in","r");
fout = open("1.out","w");

def main():
    lines = [line.strip() for line in fin.read().split("\n")[0:-1]];
    fout.write(str(solve(lines)));

def solve(lines):
    two,three = 0,0
    for line in lines:
        dict = {};
        for l in line:
            if (l in dict): dict[l]+=1;
            else: dict[l] = 1;
        for d in dict:
            if (dict[d] == 2): two+=1; break;
        for d in dict:
            if (dict[d] == 3): three+=1; break;
    return two*three;

main();
