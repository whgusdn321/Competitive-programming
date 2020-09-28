import sys
from collections import deque
sys.setrecursionlimit(10000000)
read = lambda :sys.stdin.readline().rstrip()

N = int(read())
maap = []
for _ in range(N):
    temp = [int(a) for a in read().split()]
    maap.append(temp)


def paint(y, x, maap, island, stack):
    global visited
    visited[y][x] = True
    maap[y][x] = island
    stack.append((y, x))
    adj = [(y, x-1), (y-1, x), (y, x+1), (y+1 , x)]
    for dy, dx in adj:
        if 0 <= dy < N and 0 <= dx < N and not visited[dy][dx]:
            if maap[dy][dx] == 1:
                paint(dy, dx, maap, island, stack)
    return stack


def bfs(y, x, color):
    global maap, visited
    visited[y][x] = True
    queue = deque([(y, x, 0)])
    while queue:
        py, px, pd = queue.popleft()
        if maap[py][px] != color and maap[py][px] != 0:
            return pd-1
        adj = [(py, px-1), (py-1, px), (py, px+1), (py+1, px)]
        for cy, cx in adj:
            if 0<=cy<N and 0<=cx<N and not visited[cy][cx]:
                if maap[cy][cx] != color:
                    visited[cy][cx] = True
                    queue.append((cy, cx, pd+1))
    return 9999




visited = [[False]*N for _ in range(N)]


island = 0
stacks = []
for i in range(N):
    for j in range(N):
        if not visited[i][j] and maap[i][j] == 1:
            island += 1
            stack = paint(i, j, maap, island, [])
            stacks.append(stack)


distances = []
for i, stack in enumerate(stacks):
    for y, x in stack:
        visited = [[False] * N for _ in range(N)]
        dist = bfs(y, x, i+1)
        distances.append(dist)
print(min(distances))