fin = open("2.in","r");
fout = open("2.out","w");

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
            for q in range(5):
                if (int(string[q]) > int(string[q+1])): b = False; break;
            if (string[0] == string[1] and string[0] != string[2]): a = True;
            if (string[1] == string[2] and string[1] != string[0] and string[1] != string[3]): a = True;
            if (string[2] == string[3] and string[2] != string[1] and string[2] != string[4]): a = True;
            if (string[3] == string[4] and string[3] != string[2] and string[3] != string[5]): a = True;
            if (string[4] == string[5] and string[4] != string[3]): a = True
            if (a and b): count += 1;
    return count;
    
main();
