fin = open("../Input.in","r")
fout = open("../Part2.out","w")

def main():
    lines = [line.strip() for line in fin.read().split("\n")[0:-1]]
    lines = lines[0].split(", ")
    fout.write(str(solve(lines)))

def solve(lines):
    x,y,d = 0,0,0
    S = set();
    S.add((x,y))
    for line in lines:
        if (line[0] == 'R'): d = (d+1)%4
        if (line[0] == 'L'): d = (d-1)%4
        if (d == 0):
            for i in range(int(line[1:])):
                y += 1;
                if ((x,y) in S): return abs(x)+abs(y)
                S.add((x,y))
        if (d == 1):
            for i in range(int(line[1:])):
                x += 1;
                if ((x,y) in S): return abs(x)+abs(y)
                S.add((x,y))
        if (d == 2):
            for i in range(int(line[1:])):
                y -= 1;
                if ((x,y) in S): return abs(x)+abs(y)
                S.add((x,y))
        if (d == 3):
            for i in range(int(line[1:])):
                x -= 1;
                if ((x,y) in S): return abs(x)+abs(y)
                S.add((x,y))

main()
