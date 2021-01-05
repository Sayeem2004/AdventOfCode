fin = open("2.in","r");
fout = open("2.out","w");

def main():
    line = fin.read().split("\n")[0].strip();
    fout.write(str(solve(line)));

def solve(line):
    ans = 1000000000;
    capital = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    lower = "abcdefghijklmnopqrstuvwxyz";
    for i,x in enumerate(capital):
        temp = line.replace(x,""); temp = temp.replace(lower[i],"");
        ans = min(ans,reduce(temp));
    return ans;

def reduce(line):
    i,n = 0,len(line);
    while (i < n-1):
        if (abs(ord(line[i])-ord(line[i+1])) == 32):
            line = line[:i] + line[i+2:];
            n -= 2; i -= 1; i = max(i,0)
            continue;
        i+=1;
    return len(line);

main();
