from collections import defaultdict

ans = 10**9


def dfs(n, weak, dist, visited, vnum, i, cnt):
    global ans
    if i == len(weak):
        if vnum == len(weak):
            ans = min(ans, cnt)
        return

    if visited[i]:
        dfs(n, weak, dist, visited, vnum, i+1, cnt)
        return

    for j in range(len(dist)):
        d = dist[j]
        coverage = d
        _visited = []
        for ii in range(len(weak)): # find _visited
            dd = weak[ii] - weak[i]
            if dd < 0:
                dd += n
            if dd <= coverage:
                _visited.append(ii)
                visited[ii] = True
        tmp = dist.pop(j)
        dfs(n, weak, dist, visited, vnum+len(_visited), i+1, cnt+1)
        dist.insert(j, tmp)
        for ii in _visited:
            visited[ii] = False
    dfs(n, weak, dist, visited, vnum, i+1, cnt)


def solution(n, weak, dist):
    visited = defaultdict(bool)
    dfs(n, weak, dist, visited, 0, 0, 0)
    if ans != 10**9:
        return ans
    else:
        return -1

print(solution(12, [1,5,6,10], [1, 2, 3, 4]))