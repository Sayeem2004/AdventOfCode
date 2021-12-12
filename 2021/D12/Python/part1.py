def main():
    fin = open("../input.in", "r")
    fout = open("../part1.out", "w")
    lines = [line.strip() for line in fin.read().split("\n")[0:-1]]
    lines = [line.split("-") for line in lines]
    fout.write(str(solve(lines)))


def dfs(adj, visited, curr):
    if (curr == "end"):
        return 1
    sum = 0
    for node in adj[curr]:
        if (node.islower()):
            if (visited[node]):
                continue
            else:
                visited[node] = True
                sum += dfs(adj, visited, node)
                visited[node] = False
        else:
            visited[node] = True
            sum += dfs(adj, visited, node)
            visited[node] = False
    return sum


def solve(lines):
    adj, visited = {}, {}
    for line in lines:
        if (line[0] in adj):
            adj[line[0]].append(line[1])
        else:
            adj[line[0]] = [line[1]]
        if (line[1] in adj):
            adj[line[1]].append(line[0])
        else:
            adj[line[1]] = [line[0]]
        visited[line[0]] = False
        visited[line[1]] = False
    visited["start"] = True
    return dfs(adj, visited, "start")


main()
