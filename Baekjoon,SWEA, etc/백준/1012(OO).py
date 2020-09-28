import sys
from collections import deque
test_cases = int(sys.stdin.readline())


def bfs(y, x, visited):
    if visited[y][x] or maap[y][x] == 0:
        return False
    else:
        visited[y][x] = True
        queue = deque([(y, x)])
        while queue:
            c_y, c_x = queue.popleft()
            adjacent = [(c_y, c_x-1), (c_y-1, c_x), (c_y, c_x+1), (c_y+1, c_x)]
            for n_y, n_x in adjacent:
                if 0<=n_y<H and 0<=n_x<W and not visited[n_y][n_x]:
                    if maap[n_y][n_x] == 1:
                        queue.append([n_y, n_x])
                        visited[n_y][n_x] = True
        return True


for test_case in range(test_cases):
    W, H, K = map(int, sys.stdin.readline().split())
    maap = [[0]*W for _ in range(H)]
    visited = [[False]*W for _ in range(H)]
    for __ in range(K):
        b_x, b_y = map(int, sys.stdin.readline().split())
        maap[b_y][b_x] = 1

    cnt = 0
    for i in range(H):
        for j in range(W):
            boool = False
            boool = bfs(i, j, visited)
            if boool:
                cnt += 1
    print(cnt)
