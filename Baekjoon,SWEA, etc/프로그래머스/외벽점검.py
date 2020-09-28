ans = 10000000


def dfs(n, weak, visited, dists, dvisited, cnt, cnt2):
    global ans

    if sum(dvisited) == len(dists):
        return

    if cnt2 == len(weak):
        ans = min(ans, cnt)
        return

    for i in range(len(weak)):
        if not visited[i]:
            # clock wise
            for j in range(len(dists)):
                if not dvisited[j]:
                    coverage = dists[j]
                    covered = []
                    for ii in range(len(weak)):
                        dist = weak[ii] - weak[i]
                        if dist < 0:
                            dist += n
                        if dist <= coverage:
                            visited[ii] = True
                            covered.append(ii)
                    dvisited[j] = True
                    dfs(n, weak, visited, dists, dvisited, cnt+1, cnt2+len(covered))
                    for co in covered:
                        visited[co] = False
                    dvisited[j] = False

            # counter clock wise
            for j in range(len(dists)):
                if not dvisited[j]:
                    coverage = dists[j]
                    covered = []
                    for ii in range(len(weak)):
                        dist = weak[i] - weak[ii]
                        if dist < 0 :
                            dist += n
                        if dist <= coverage:
                            visited[ii] = True
                            covered.append(ii)
                    dvisited[j] = True
                    dfs(n, weak, visited, dists, dvisited, cnt+1, cnt2+len(covered))
                    for co in covered:
                        visited[co] = False
                    dvisited[j] = False


def solution(n, weak, dist):
    visited = [False for _ in range(len(weak))]
    dvisited = [False for _ in range(len(dist))]
    dfs(n, weak, visited, dist, dvisited, 0, 0)
    if ans == 10000000:
        return -1
    else:
        return ans
    return ans

print(solution(12, [1,3,4,9,10], [3,5,7]))