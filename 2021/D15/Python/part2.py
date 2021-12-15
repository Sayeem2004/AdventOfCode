from queue import PriorityQueue


def main():
    fin = open("../input.in", "r")
    fout = open("../part2.out", "w")
    lines = [[int(x) for x in list(line.strip())] for line in fin.read().split("\n")[0:-1]]
    fout.write(str(solve(lines)))


def solve(lines):
    n, m = len(lines), len(lines[0])
    adj = [[0 for q in range(5*m)] for i in range(5*n)]
    for i in range(5*n):
        for q in range(5*m):
            dx = (i - (i % n)) // n
            dy = (q - (q % m)) // m
            if (i < n and q < m):
                adj[i][q] = lines[i][q]
            adj[i][q] = adj[i % n][q % m] + dx + dy
            while (adj[i][q] > 9):
                adj[i][q] -= 9
    dist = [[1000000000 for q in range(5*m)] for i in range(5*n)]
    vis = [[False for q in range(5*m)] for i in range(5*n)]
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
            if (nx >= 0 and nx < 5*n and ny >= 0 and ny < 5*m):
                if (dist[val[1]][val[2]]+adj[nx][ny] < dist[nx][ny]):
                    dist[nx][ny] = dist[val[1]][val[2]]+adj[nx][ny]
                    pq.put((dist[nx][ny], nx, ny))
        for dy in d:
            nx = val[1]
            ny = val[2]+dy
            if (nx >= 0 and nx < 5*n and ny >= 0 and ny < 5*m):
                if (dist[val[1]][val[2]]+adj[nx][ny] < dist[nx][ny]):
                    dist[nx][ny] = dist[val[1]][val[2]]+adj[nx][ny]
                    pq.put((dist[nx][ny], nx, ny))
    return dist[5*n-1][5*m-1]


main()
