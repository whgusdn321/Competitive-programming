from collections import deque
H, W = map(int, input().split())
maap = []
for _ in range(H):
    temp = input()
    maap.append(temp)


def bfs(y, x):
    global maap, visited #50x50 size
    queue = deque([(y, x, 0)])
    visited[y][x] = True
    while queue:
        py, px, pdis = queue.popleft()
        adjacent = [(py, px-1), (py-1, px), (py, px+1), (py+1, px)]
        for dy, dx in adjacent:
            if 0<=dy<H and 0<=dx<W and not visited[dy][dx]:
                if maap[dy][dx] == 'L':
                    visited[dy][dx] = True
                    queue.append((dy, dx, pdis + 1))
        if not queue:
            return pdis
Ls = []
for i in range(H):
    for j in range(W):
        if maap[i][j] == 'L':
            Ls.append((i, j))

stack = []
for L in Ls:
    ly, lx = L[0], L[1]
    visited = [[False] * W for _ in range(H)]
    length = bfs(ly, lx)
    stack.append(length)
print('stack : ',stack)


