from queue import PriorityQueue


def main():
    fin = open("../input.in", "r")
    fout = open("../part1.out", "w")
    lines = [[int(x) for x in list(line.strip())] for line in fin.read().split("\n")[0:-1]]
    fout.write(str(solve(lines)))


def solve(lines):
    n, m = len(lines), len(lines[0])
    dist = [[1000000000 for q in range(m)] for i in range(n)]
    vis = [[False for q in range(m)] for i in range(n)]
    dist[0][0] = 0
    pq = PriorityQueue()
    pq.put((0, 0, 0))
    while (not pq.empty()):
        val = pq.get()
        if (vis[val[1]][val[2]]):
            continue
        vis[val[1]][val[2]] = True
        d = [-1, 1]
        for dx in d:
            nx = val[1]+dx
            ny = val[2]
            if (nx >= 0 and nx < n and ny >= 0 and ny < m):
                if (dist[val[1]][val[2]]+lines[nx][ny] < dist[nx][ny]):
                    dist[nx][ny] = dist[val[1]][val[2]]+lines[nx][ny]
                    pq.put((dist[nx][ny], nx, ny))
        for dy in d:
            nx = val[1]
            ny = val[2]+dy
            if (nx >= 0 and nx < n and ny >= 0 and ny < m):
                if (dist[val[1]][val[2]]+lines[nx][ny] < dist[nx][ny]):
                    dist[nx][ny] = dist[val[1]][val[2]]+lines[nx][ny]
                    pq.put((dist[nx][ny], nx, ny))
    return dist[n-1][m-1]


main()
