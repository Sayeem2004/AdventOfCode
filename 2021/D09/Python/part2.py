fin = open("../input.in", "r");
fout = open("../part2.out", "w");

def main():
    lines = [line.strip() for line in fin.read().split("\n")[0:-1]];
    lines = [[int(num) for num in line] for line in lines];
    fout.write(str(solve(lines)));

def dfs(lines, visited, i, q, cnt):
    visited[i][q] = cnt;
    if (i > 0 and visited[i-1][q] == -1 and lines[i-1][q] != 9):
        dfs(lines, visited, i-1, q, cnt);
    if (q > 0 and visited[i][q-1] == -1 and lines[i][q-1] != 9):
        dfs(lines, visited, i, q-1, cnt);
    if (i < len(lines)-1 and visited[i+1][q] == -1 and lines[i+1][q] != 9):
        dfs(lines, visited, i+1, q, cnt);
    if (q < len(lines[0])-1 and visited[i][q+1] == -1 and lines[i][q+1] != 9):
        dfs(lines, visited, i, q+1, cnt);


def solve(lines):
    cnt = 0;
    visited = [[-1 for num in line] for line in lines];
    for i,line in enumerate(lines):
        for q,num in enumerate(line):
            if (visited[i][q] == -1 and lines[i][q] != 9):
                dfs(lines, visited, i, q, cnt);
                cnt += 1;
    size = [0 for x in range(cnt)];
    for line in visited:
        for num in line:
            if (num != -1): size[num] += 1;
    size.sort();
    return size[-1]*size[-2]*size[-3];

main();
