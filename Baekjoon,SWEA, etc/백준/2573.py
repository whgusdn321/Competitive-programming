import sys
from collections import deque
from copy import deepcopy
H, W = map(int, sys.stdin.readline().split())
maap = []
for _ in range(H):
    temp = [int(a) for a in sys.stdin.readline().split()]
    maap.append(temp)

k = 0


def updatemap(maap):
    temp_maap = [[-1]*W for _ in range(H)]
    for y in range(H):
        for x in range(W):
            if maap[y][x] == 0:
                temp_maap[y][x] = maap[y][x]
            else:
                adjacent = [(y, x-1), (y-1, x), (y, x+1), (y+1, x)]
                cnt = 0
                for dy, dx in adjacent:
                    if maap[dy][dx] == 0 and 0<=dy<H and 0<=dx<W :
                        cnt += 1
                if maap[y][x] - cnt >=0:
                    temp_maap[y][x] = maap[y][x] - cnt
                else:
                    temp_maap[y][x] = 0
    return temp_maap


def bfs(i, j, visited, maap):
    visited[i][j] = True
    queue = deque([(i, j)])
    while queue:
        cy, cx = queue.popleft()
        adjacent = [(cy, cx-1), (cy-1, cx), (cy, cx+1), (cy+1, cx)]
        for ny, nx in adjacent:
            if 0<=ny<H and 0<=nx<W and not visited[ny][nx]:
                if maap[ny][nx] != 0:
                    visited[ny][nx] = True
                    queue.append((ny, nx))



while(True):
    k += 1
    maap = updatemap(maap)
    # for _ in range(H):
    #     print('maap: ', maap[_])
    # print()
    visited = [[False]*W for __ in range(H)]
    num_bfs = 0
    for i in range(H):
        for j in range(W):
            if (not visited[i][j]) and maap[i][j] != 0:
                bfs(i, j, visited, maap)
                num_bfs += 1
    if num_bfs > 1:
        print(k)
        break
    if num_bfs == 0:
        print(0)
        break

