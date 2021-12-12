def main():
    fin = open("../input.in", "r")
    fout = open("../part2.out", "w")
    lines = [line.strip() for line in fin.read().split("\n")[0:-1]]
    lines = [line.split("-") for line in lines]
    fout.write(str(solve(lines)))


def dfs(adj, visited, curr, double):
    if (curr == "end"):
        if (double != "none"):
            if (visited[double] == 2):
                return 1
            else:
                return 0
        else:
            return 1
    sum = 0
    for node in adj[curr]:
        if (node.islower()):
            if (node == double and visited[node] < 2):
                visited[node] += 1
                sum += dfs(adj, visited, node, double)
                visited[node] -= 1
            elif (visited[node] == 0):
                visited[node] += 1
                sum += dfs(adj, visited, node, double)
                visited[node] -= 1
        else:
            visited[node] += 1
            sum += dfs(adj, visited, node, double)
            visited[node] -= 1
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
        visited[line[0]] = 0
        visited[line[1]] = 0
    ans = 0
    visited["start"] = 1
    for node in adj.keys():
        if (node.islower() and node != "start" and node != "end"):
            ans += dfs(adj, visited, "start", node)
    ans += dfs(adj, visited, "start", "none")
    return ans


main()
