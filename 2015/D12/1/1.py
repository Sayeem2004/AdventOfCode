fin = open("1.in","r");
fout = open("1.out","w");

def main():
    lines = [line.strip() for line in fin.read().split("\n")[0:-1]];
    fout.write(str(solve(lines)));

def solve(lines):
    ans = 0;
    for line in lines:
        ans += find(line);
    return ans;

def find(line):
    count = 0;
    i = 0;
    while (i < len(line)):
        if (line[i].isdigit()):
            c = 1;
            while (c < len(line)-i):
                if (line[i+c].isdigit()): c += 1;
                else: break;
            count += int(line[i:i+c]);
            i += c;
        elif (line[i] == "-"):
            c = 1;
            while (c < len(line)-i):
                if (line[i+c].isdigit()): c += 1;
                else: break;
            if (c != 1): count += int(line[i:i+c]);
            i += c;
        else: i+= 1;
    return count;

main();
