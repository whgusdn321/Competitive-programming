import sys
sys.setrecursionlimit(100000000)

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]

# print("graph is : ", graph)
# print("visited is : ", visited)
def dfs(node):
    visited[node] = True
    ret = 0
    for child in graph[node]:
        if not visited[child]:
            ret += dfs(child)
    return ret + 1


for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

rets = []
for node in range(1, n+1):
    if not visited[node] :
        counts = dfs(node)
        rets.append(counts)
print(max(rets))
