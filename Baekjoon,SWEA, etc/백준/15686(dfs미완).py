import sys
import itertools
read = lambda :sys.stdin.readline().rstrip()
from collections import deque

N, M = map(int, read().split())

maap = []
for _ in range(N):
    temp = [int(a) for a in read().split()]
    maap.append(temp)


def go(y, x, visited):
    global maap, limitt
    visited[y][x] = True
    queue = deque([(y, x, 0)])
    while queue:
        py, px, dep = queue.popleft()
        if maap[py][px] == 2:
            limitt -= dep
            return True
        adjacent = [(py, px-1), (py-1, px), (py, px+1), (py, px-1)]
        for dy, dx in adjacent:
            if 0<=dy<N and 0<=dx<N and not visited[dy][dx] and dep < limitt:
                queue.append((dy, dx, dep+1))
    return False




limit = 5

while True:
    limitt = limit
    flag = True

    for i in range(N):
        for j in range(N):
            visited = [[False] * N for _ in range(N)]
            if maap[i][j] == 1:
                go(i, j, visited)
            if limitt == 0:


    if flag:
        break
    else:
        limit += 1
    print('limit : ', limit)
print('limit : ', limit)

