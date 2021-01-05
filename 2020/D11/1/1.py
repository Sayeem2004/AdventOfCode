fin = open("1.in","r");
fout = open("1.out","w");

def main():
    lines = [list(line.strip()) for line in fin.read().split("\n")[0:-1]];
    fout.write(str(solve(lines)));

def solve(lines):
    prev = -1; curr = 0; e = 0;
    x = [0,1,1,1,0,-1,-1,-1];
    y = [-1,-1,0,1,1,1,0,-1];
    n = len(lines); m = len(lines[0]);
    while (prev != curr):
        prev = curr;
        if (e%2 == 0):
            l = [];
            for i in range(0,n):
                for q in range(0,m):
                    c = 0;
                    for r in range(0,len(x)):
                        if (i+y[r] >= 0 and i+y[r] < n and q+x[r] >= 0 and q+x[r] < m):
                            if (lines[i+y[r]][q+x[r]] == '#'): c+=1;
                    if (c == 0 and lines[i][q] == "L"):
                        curr+=1; l.append([i,q]);
            for s in l:
                lines[s[0]][s[1]] = "#";
        else:
            l = [];
            for i in range(0,n):
                for q in range(0,m):
                    c = 0;
                    for r in range(0,len(x)):
                        if (i+y[r] >= 0 and i+y[r] < n and q+x[r] >= 0 and q+x[r] < m):
                            if (lines[i+y[r]][q+x[r]] == '#'): c+=1;
                    if (c >= 4 and lines[i][q] == "#"):
                        curr-=1; l.append([i,q]);
            for s in l:
                lines[s[0]][s[1]] = "L";
        e+=1;
    return curr;

main();
