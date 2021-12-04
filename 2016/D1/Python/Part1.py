fin = open("../Input.in","r")
fout = open("../Part1.out","w")

def main():
    lines = [line.strip() for line in fin.read().split("\n")[0:-1]]
    lines = lines[0].split(", ")
    fout.write(str(solve(lines)))

def solve(lines):
    x,y,d = 0,0,0
    for line in lines:
        if (line[0] == 'R'): d = (d+1)%4
        if (line[0] == 'L'): d = (d-1)%4
        if (d == 0): y += int(line[1:])
        if (d == 1): x += int(line[1:])
        if (d == 2): y -= int(line[1:])
        if (d == 3): x -= int(line[1:])
    return abs(x)+abs(y)

main()
