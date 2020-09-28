import sys
sys.setrecursionlimit(10**8)
H, W, K = map(int, sys.stdin.readline().split())
maap = [[1]*W for _ in range(H)]
for k in range(K):
    lx, ly, rx, ry = map(int, sys.stdin.readline().split())
    for x in range(lx, rx):
        for y in range(ly, ry):
            maap[y][x] = 0

# for _ in range(H):
#     print(maap[_])


def dfs(y, x, maap, visited):
    global cnt
    visited[y][x] = 1
    cnt += 1
    adjacents = [(y, x-1), (y-1, x), (y, x+1), (y+1, x)]
    for ny, nx in adjacents:
        if 0<=ny<H and 0<=nx<W and not visited[ny][nx]:
            if maap[ny][nx]:
                dfs(ny, nx, maap, visited)

visited = [[False]*W for __ in range(H)]
a = []

for i in range(H):
    for j in range(W):
        cnt = 0
        if maap[i][j] and not visited[i][j]:
            dfs(i, j, maap, visited)
            a.append(cnt)
print(len(a))
a.sort()
for cnt in a:
    print(cnt, end=' ')

