import sys
from collections import deque


def bfs(sy, sx, gy, gx):
    global visited, N
    visited[sy][sx] = True
    queue = deque([(sy, sx, 0)])

    while queue:
        cy, cx, cnt = queue.popleft()
        #print('cnt : ', cnt)
        if cy == gy and cx == gx:
            return cnt
        adjacent = [(cy-2, cx-1),(cy-2, cx+1),(cy+2, cx+1),(cy+2, cx-1),\
                    (cy+1, cx-2),(cy+1, cx+2),(cy-1, cx+2),(cy-1, cx-2)]
        for dy, dx in adjacent:
            if 0<=dy<N and 0<=dx<N and not visited[dy][dx]:
                visited[dy][dx] = True
                queue.append((dy, dx, cnt+1))


tests = int(sys.stdin.readline())
for test in range(tests):
    N = int(sys.stdin.readline())
    sY, sX = map(int, sys.stdin.readline().split())
    gY, gX = map(int, sys.stdin.readline().split())

    visited = [[False]*N for _ in range(N)]
    print(bfs(sY, sX, gY, gX))