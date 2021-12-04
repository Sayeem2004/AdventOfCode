fin = open("Input.in","r");
fout = open("Part1.out","w");

def main():
    lines = [line.strip() for line in fin.read().split("\n")[0:-1]];
    fout.write(str(solve(lines)));

def solve(lines):
    vowels = "aeiou";
    substrings = ["ab","cd","pq","xy"];
    count = 0;
    for line in lines:
        cv = 0;
        double = False;
        contains = True;
        for i,x in enumerate(line):
            if (x in vowels): cv+=1;
            if (i != 0):
                if (line[i-1] == x): double = True;
        for x in substrings:
            if x in line: contains = False;
        if (cv >= 3 and double and contains): count+=1;
    return count;

main();
