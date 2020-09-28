#import sys
#sys.setrecursionlimit(100000000)
n, k = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(k):
    a, b = map(int, input().split())
    graph[a].append(b)

wants = []
nn = int(input())
for _ in range(nn):
    temp = [int(a) for a in input().split()]
    wants.append(temp)


def dfs(i, j, graph, visited):
    visited[i] = True
    if i == j:
        return True
    else:
        boool = False
        for child in graph[i]:
            if not visited[child]:
              boool |= dfs(child, j, graph, visited)
        return boool


for item in wants:
    left, right = item

    visited = [False] * (n+1)
    boool = dfs(left, right, graph, visited)
    if boool:
        print(-1)
        continue

    #renew visited
    visited = [False] * (n+1)
    boool = dfs(right, left, graph, visited)
    if boool:
        print(1)
        continue
    else:
        print(0)
