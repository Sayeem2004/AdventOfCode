fin = open("../Input.in","r")
fout = open("../Part1.out","w")

def main():
    lines = [line.strip() for line in fin.read().split("\n")[0:-1]]
    fout.write(str(solve(lines)))

def solve(lines):
    pw = ""
    code = [[1,2,3],[4,5,6],[7,8,9]]
    x,y = 1,1
    for line in lines:
        for l in line:
            if (l == 'U'): y = max(0,y-1)
            if (l == 'D'): y = min(2,y+1)
            if (l == 'L'): x = max(0,x-1)
            if (l == 'R'): x = min(2,x+1)
        pw += str(code[y][x])
    return pw
main()
