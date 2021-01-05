fin = open("1.in","r");
fout = open("1.out","w");

def main():
    lines = fin.read().split("\n")[0];
    lines = lines.split("-");
    fout.write(str(solve(lines)));

def solve(lines):
    count = 0;
    for i in range(int(lines[0]),int(lines[1])+1):
        if (i >= 100000 and i < 1000000):
            string = str(i);
            a = False; b = True;
            for q in range(len(string)-1):
                if (string[q] == string[q+1]): a = True;
                if (int(string[q]) > int(string[q+1])): b = False;
            if (a and b): count += 1;
    return count;
    
main();
